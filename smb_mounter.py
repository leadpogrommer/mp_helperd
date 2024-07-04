import time
from dataclasses import dataclass
from threading import Thread
import subprocess
import socket
from mpd_util import update_db
from time import sleep

from config import nas_share, SmbShare


def handle_share(share: SmbShare):
    time.sleep(3.33)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((share.addr, 445))
    if res == 0:
        sock.close()
    is_available = res == 0
    # print(is_available)

    mount_lines = subprocess.check_output('mount', shell=False).decode().split()
    mounted = False
    for line in mount_lines:
        if share.mountpoint in line:
            mounted = True
            break

    if mounted and not is_available:
        # unmount
        subprocess.run(['umount', '-l', share.mountpoint], shell=False)
        print('Unmounted share', share.mountpoint)
    elif not mounted and is_available:
        # mount
        res = subprocess.run(['mount', '-t', 'cifs', f'//{share.addr}/{share.share}', share.mountpoint, '-o', share.options], shell=False)
        if res.returncode == 0:
            print('Mounted share', share.mountpoint)
            update_db('NAS')
        else:
            print(f'Failed to mount share {share.mountpoint}: {res.returncode}')


def mounter_loop():
    while True:
        time.sleep(3.33)
        try:
            handle_share(nas_share)
        except Exception as e:
            print('Error while handling share:', e)


def start_mounter():
    Thread(target=mounter_loop, daemon=True).start()
