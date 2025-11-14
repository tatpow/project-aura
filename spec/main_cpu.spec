# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['../main.py'],
    pathex=['..'],
    binaries=[
        ('../ffmpeg/ffmpeg.exe', '.'),
        ('../ffmpeg/ffprobe.exe', '.'), 
    ],
    datas=[
        ('../app/json/*.json', 'app/json'),  
        ('../app/**/*.py', 'app'),            
        ('../icon.ico', '.'),                 
    ],
    hiddenimports=[
        'customtkinter',
        'transformers',
        'librosa',
        'torch',
        'tkinter',
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
    name='Project Aura (CPU)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,           
    console=False,       
    icon='../icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='Project Aura (CPU)'
)
