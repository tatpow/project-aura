# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None
root_dir = os.path.abspath(os.path.join(SPECPATH, '..'))

a = Analysis(
    [os.path.join(root_dir, 'main.py')],
    pathex=[root_dir],
    binaries=[
        (os.path.join(root_dir, 'ffmpeg', 'ffmpeg.exe'), 'ffmpeg'),
        (os.path.join(root_dir, 'ffmpeg', 'ffprobe.exe'), 'ffmpeg'),
    ],
    datas=[
        (os.path.join(root_dir, 'app', 'json', '*.json'), 'app/json'),
        (os.path.join(root_dir, 'app', '**', '*.py'), 'app'),
        (os.path.join(root_dir, 'icon.ico'), '.'),
    ],
    hiddenimports=[
        'customtkinter',
        'transformers',
        'librosa',
        'torch',
        'tkinter',
        'protobuf',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Project Aura (GPU)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    icon=os.path.join(root_dir, 'icon.ico')
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='Project Aura (GPU)'
)
