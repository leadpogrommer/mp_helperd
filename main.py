#!/usr/bin/env python3


import asyncio
from asyncio import run
from udisks import OrgFreedesktopUDisks2ManagerInterface, OrgFreedesktopUDisks2FilesystemInterface, OrgFreedesktopUDisks2DriveInterface

from sdbus import sd_bus_open_system, DbusObjectManagerInterfaceAsync
from sdbus.utils import parse_interfaces_added

bus = sd_bus_open_system()




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


async def main():
    om = DbusObjectManagerInterfaceAsync.new_proxy('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2', bus=bus)
    import json

    # print(json.dumps(await om.get_managed_objects(), indent=2))
    managed_objects = await om.get_managed_objects()
    # print(res)

    # exit(0)
    for path, obj in managed_objects.items():
        if 'org.freedesktop.UDisks2.Filesystem' not in obj or 'org.freedesktop.UDisks2.Block' not in obj:
            continue
        # print(path, obj)
        try:
            await mount_bd(bd_path=path, drive_path=obj['org.freedesktop.UDisks2.Block']['Drive'][1])
        except Exception as e:
            print('Failed to process obj ', path, e)

    async for s in om.interfaces_added:
        path, obj = s
        if 'org.freedesktop.UDisks2.Filesystem' not in obj or 'org.freedesktop.UDisks2.Block' not in obj:
            continue
        try:
            await mount_bd(bd_path=path, drive_path=obj['org.freedesktop.UDisks2.Block']['Drive'][1])
        except Exception as e:
            print('Failed to process obj ', path, e)


    # manager = OrgFreedesktopUDisks2ManagerInterface.new_proxy('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/Manager', bus=bus)
    # res = await manager.get_block_devices({})
    # print(res)
    # for bd_path in res:
    #     print(bd_path)
    #     fs = OrgFreedesktopUDisks2FilesystemInterface.new_proxy('org.freedesktop.UDisks2', bd_path, bus=bus)
    #     print(bd_path, await fs.size)
    #
    # pass

if __name__ == '__main__':
    asyncio.run(main())