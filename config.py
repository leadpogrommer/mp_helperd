from dataclasses import dataclass


@dataclass
class SmbShare:
    addr: str
    share: str
    mountpoint: str
    options: str


mpd_music_dir = '/var/lib/mpd/music'

nas_share = SmbShare(
    '8.8.8.8',
    'redacted',
    '/var/lib/mpd/music/NAS',
    'username=redacted,password=redacted,iocharset=utf8,ro'
)
