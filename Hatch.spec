# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
help = [('h', 'Run just ./Hatch to default, otherwise input a time', 'OPTION')]

a = Analysis(['Hatch.py'],
             pathex=['/Users/weichiang/Desktop/cs/prx_code/Hatch'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          help = True,
          exclude_binaries=True,
          name='Hatch',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Hatch')
