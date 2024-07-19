import os
import shutil
from pathlib import Path


class colors:
  MAGENTA = '\033[95m'
  RED = '\033[91m'
  YELLOW = '\033[93m'
  ORANGE = '\033[38;5;208m'
  GREEN = '\033[1;32;40m'
  RESET = '\033[0m'


pictures_ext = [
    'gif', 'jpeg', 'png', 'jpg', 'bmp', 'tiff', 'psd', 'svg', 'ai', 'eps'
]
documents_ext = ['doc', 'pdf', 'ps', 'txt', 'rtf']
music_ext = ['mp3', 'wav', 'ogg', 'flac', 'm4a', 'wma', 'aac']
video_ext = ['webm', 'mp4', 'avi', 'mov', 'flv', 'mkv', 'wmv']
compressed_ext = ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'lzma']
programs_ext = [
    'exe', 'msi', 'deb', 'rpm', 'apk', 'jar', 'dmg', 'iso', 'img', 'iso'
]
scripts_ext = ['py', 'js', 'php', 'html', 'css', 'js', 'sh', 'bat', 'ps1']

files = os.listdir(os.getcwd())

dirs = []
for file in files:
  ext = file.split('.')[-1]
  if ext in pictures_ext:
    dirs.append('Pictures')
  elif ext in documents_ext:
    dirs.append('Documents')
  elif ext in music_ext:
    dirs.append('Music')
  elif ext in video_ext:
    dirs.append('Videos')
  elif ext in compressed_ext:
    dirs.append('Compressed')
  elif ext in programs_ext:
    dirs.append('Programs')
  elif ext in scripts_ext:
    dirs.append('Scripts')

for dir in dirs:
  if Path(dir).is_dir():
    pass
  else:
    os.mkdir(dir)

for file in files:
  if file == 'organize.py':
    pass
  else:
    ext = file.split('.')[-1]
    if ext in pictures_ext:
      shutil.move(file, Path('Pictures') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to {colors.GREEN}Pictures'
      )
    elif ext in documents_ext:
      shutil.move(file, Path('Documents') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to {colors.GREEN}Documents'
      )
    elif ext in music_ext:
      shutil.move(file, Path('Music') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to {colors.GREEN}Music'
      )
    elif ext in video_ext:
      shutil.move(file, Path('Videos') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to {colors.GREEN}Videos'
      )
    elif ext in compressed_ext:
      shutil.move(file, Path('Compressed') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to {colors.GREEN}Compressed'
      )
    elif ext in programs_ext:
      shutil.move(file, Path('Programs') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to {colors.GREEN}Programs'
      )
    elif ext in scripts_ext:
      shutil.move(file, Path('Scripts') / file)
      print(
          f'{colors.RESET}Moved {colors.MAGENTA}{file}{colors.RESET} to   {colors.GREEN}Scripts'
      )

x = input()
