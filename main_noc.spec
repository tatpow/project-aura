# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('app/json/*.json', 'app/json'),   # JSON-файлы
        ('app/**/*.py', 'app'),            # Весь код из app
        ('icon.ico', '.'),                 # Иконка
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
    name='Project Aura',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,           # отключаем UPX — меньше шанс, что антивирус заорёт
    console=False,       # если нужна консоль — поставь True
    icon='icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='Project Aura'
)
