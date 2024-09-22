# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['login.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Wesllei Brito\\PycharmProjects\\aso_3.0\\icons\\passkey_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.svg', '.'), ('C:\\Users\\Wesllei Brito\\PycharmProjects\\aso_3.0\\images\\Blue_Flat_Illustrative_Human_Artificial_Intelligence_Technology_Logo-removebg-preview.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='login',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
