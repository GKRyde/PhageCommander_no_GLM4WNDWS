# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['phagecom.py'],
             pathex=['/Users/ryderg3/Documents/GitHub/PhageCommander_no_Glimmer/phagecommander'],
             binaries=[],
             datas=[('species.txt', '.')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='phagecom',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='phagecom.app',
             icon=None,
             bundle_identifier=None)
