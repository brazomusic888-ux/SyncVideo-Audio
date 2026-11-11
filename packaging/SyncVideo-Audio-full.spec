# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

hiddenimports = []
binaries = []
datas = [
    ("../assets/logo.png", "assets"),
    ("../assets/logo-64.png", "assets"),
    ("../assets/logo-taskbar.png", "assets"),
    ("../assets/logo.ico", "assets"),
    ("../assets/fonts/NotoSansCJK-Regular.ttc", "assets/fonts"),
    ("../assets/fonts/OFL-1.1.txt", "licenses"),
    ("../assets/models/small", "assets/models/small"),
    ("../assets/tools/ffmpeg.exe", "assets/tools"),
    ("../assets/tools/ffprobe.exe", "assets/tools"),
    ("../LICENSE", "licenses"),
    ("../THIRD_PARTY_NOTICES.md", "licenses"),
    ("licenses/FFmpeg-NOTICE.txt", "licenses"),
    ("licenses/WHISPER-MODEL-NOTICE.txt", "licenses"),
]

# faster-whisper loads CTranslate2, tokenizers and PyAV at runtime. Collect
# package data, native DLLs and hidden imports so the frozen GUI can load them.
for package in (
    "faster_whisper",
    "ctranslate2",
    "tokenizers",
    "av",
    "huggingface_hub",
):
    package_datas, package_binaries, package_hiddenimports = collect_all(package)
    datas += package_datas
    binaries += package_binaries
    hiddenimports += package_hiddenimports

a = Analysis(
    ["gui_launcher.py"],
    pathex=["../src"],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["torch", "tensorflow"],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SyncVideo-Audio",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="../assets/logo.ico",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="SyncVideo-Audio",
)
