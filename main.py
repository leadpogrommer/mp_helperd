#!/usr/bin/env python3


import asyncio
from asyncio import run

from mpd_util import update_db
from udisks import OrgFreedesktopUDisks2ManagerInterface, OrgFreedesktopUDisks2FilesystemInterface, OrgFreedesktopUDisks2DriveInterface

from sdbus import sd_bus_open_system, DbusObjectManagerInterfaceAsync
from smb_mounter import start_mounter
from file_browser import start_server

start_mounter()
start_server()

bus = sd_bus_open_system()

mount_paths = {}

async def mount_bd(bd_path, drive_path):
    drive_if = OrgFreedesktopUDisks2DriveInterface.new_proxy('org.freedesktop.UDisks2', drive_path, bus=bus)
    if not (await drive_if.removable):
        return
    fs_if = OrgFreedesktopUDisks2FilesystemInterface.new_proxy('org.freedesktop.UDisks2', bd_path, bus=bus)
    if len(await fs_if.mount_points) != 0:
        return

    print('Mounting', bd_path, drive_path)
    res = await fs_if.mount({'options': ('s', 'ro')})
    print('Mounted to', res)
    path_to_update = 'USB/'+res.split('/')[-1]
    update_db(path_to_update)
    mount_paths[bd_path] = path_to_update


async def unmounted_usb_loop(om: DbusObjectManagerInterfaceAsync):
    async for s in om.interfaces_removed:
        path, obj = s
        if 'org.freedesktop.UDisks2.Filesystem' not in obj or 'org.freedesktop.UDisks2.Block' not in obj:
            continue
        print('Removed', path)
        if path in mount_paths:
            update_db(mount_paths[path])


async def main():
    om = DbusObjectManagerInterfaceAsync.new_proxy('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2', bus=bus)

    managed_objects = await om.get_managed_objects()

    for path, obj in managed_objects.items():
        if 'org.freedesktop.UDisks2.Filesystem' not in obj or 'org.freedesktop.UDisks2.Block' not in obj:
            continue
        # print(path, obj)
        try:
            await mount_bd(bd_path=path, drive_path=obj['org.freedesktop.UDisks2.Block']['Drive'][1])
        except Exception as e:
            print('Failed to process obj ', path, e)

    asyncio.ensure_future(unmounted_usb_loop(om))
    async for s in om.interfaces_added:
        path, obj = s
        if 'org.freedesktop.UDisks2.Filesystem' not in obj or 'org.freedesktop.UDisks2.Block' not in obj:
            continue
        try:
            await mount_bd(bd_path=path, drive_path=obj['org.freedesktop.UDisks2.Block']['Drive'][1])
        except Exception as e:
            print('Failed to process obj ', path, e)


if __name__ == '__main__':
    asyncio.run(main())