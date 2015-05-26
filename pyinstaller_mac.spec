# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['/Users/quankiquanki/Documents/projects/wxPython-OpenCV'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='run',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='run')
app = BUNDLE(coll,
             name='run.app',
             icon=None,
             bundle_identifier=None)
