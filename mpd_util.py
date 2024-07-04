import subprocess


def update_db(path_to_update):
    print('Updating db in', path_to_update)
    subprocess.run(['mpc', 'update', path_to_update], shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)