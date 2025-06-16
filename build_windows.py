#!/usr/bin/env python3
"""
Windows Build Script for HRNZipper
Creates standalone Windows executable with PyInstaller
By Harun Softwares
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_spec_file():
    """Create PyInstaller spec file for Windows build"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('resources', 'resources'),
        ('README.md', '.'),
    ],
    hiddenimports=[
        'PyQt5.QtCore',
        'PyQt5.QtGui', 
        'PyQt5.QtWidgets',
        'PyQt5.QtSvg',
        'cryptography',
        'py7zr',
        'rarfile',
        'psutil',
        'PIL',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='HRNZipper',
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
    icon='resources/app_icon.ico',
    version='version_info.txt',
)
'''
    
    with open('desktop_archiver.spec', 'w') as f:
        f.write(spec_content)
    print("Created PyInstaller spec file")

def create_version_info():
    """Create version info file for Windows executable"""
    version_info = '''# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Harun Softwares'),
        StringStruct(u'FileDescription', u'HRNZipper - Archive Management Tool by Harun Softwares'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'HRNZipper'),
        StringStruct(u'LegalCopyright', u'Copyright 2025 Harun Softwares'),
        StringStruct(u'OriginalFilename', u'HRNZipper.exe'),
        StringStruct(u'ProductName', u'HRNZipper'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)'''
    
    with open('version_info.txt', 'w') as f:
        f.write(version_info)
    print("Created version info file")

def create_app_icon():
    """Create application icon from existing resources"""
    try:
        from PIL import Image
        from resources.icons import create_app_icon
        
        # Create app icon at different sizes for ICO file
        sizes = [16, 32, 48, 64, 128, 256]
        images = []
        
        for size in sizes:
            pixmap = create_app_icon(size)
            # Convert QPixmap to PIL Image
            img_data = pixmap.toImage()
            w, h = img_data.width(), img_data.height()
            
            # Convert to bytes
            ptr = img_data.bits()
            ptr.setsize(w * h * 4)
            arr = bytearray(ptr)
            
            # Create PIL image
            pil_img = Image.frombytes('RGBA', (w, h), bytes(arr), 'raw', 'BGRA')
            images.append(pil_img)
        
        # Save as ICO file
        os.makedirs('resources', exist_ok=True)
        images[0].save('resources/app_icon.ico', format='ICO', sizes=[(img.width, img.height) for img in images])
        print("Created application icon")
        
    except Exception as e:
        print(f"Warning: Could not create icon: {e}")

def build_executable():
    """Build the Windows executable"""
    print("Starting Windows build process...")
    
    # Clean previous builds
    build_dirs = ['build', 'dist', '__pycache__']
    for dir_name in build_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Cleaned {dir_name} directory")
    
    # Create necessary files
    create_spec_file()
    create_version_info()
    create_app_icon()
    
    # Run PyInstaller
    try:
        print("Running PyInstaller...")
        result = subprocess.run([
            sys.executable, '-m', 'PyInstaller',
            '--clean',
            '--onefile',
            'desktop_archiver.spec'
        ], check=True, capture_output=True, text=True)
        
        print("Build completed successfully!")
        print(f"Executable created at: {os.path.abspath('dist/DesktopArchiver.exe')}")
        
        # Create installer package
        create_installer_package()
        
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        print("Error output:", e.stderr)
        return False
    
    return True

def create_installer_package():
    """Create installer package with additional files"""
    print("Creating installer package...")
    
    # Create package directory
    package_dir = Path('package')
    package_dir.mkdir(exist_ok=True)
    
    # Copy executable
    if os.path.exists('dist/DesktopArchiver.exe'):
        shutil.copy2('dist/DesktopArchiver.exe', package_dir)
    
    # Create README for Windows
    readme_content = '''# Desktop Archiver v1.0

## Installation
1. Run DesktopArchiver.exe
2. The application will automatically integrate with Windows Explorer
3. Right-click on archive files or folders to access compression options

## Features
- Support for ZIP, RAR, 7Z, TAR formats
- Windows Explorer integration
- Password protection
- Batch operations
- Modern dark theme interface

## System Requirements
- Windows 10 or Windows 11
- 100 MB free disk space

## Usage
- Double-click archive files to open them
- Right-click folders to compress them
- Use the application interface for advanced operations

For support, visit: https://github.com/your-repo/desktop-archiver
'''
    
    with open(package_dir / 'README.txt', 'w') as f:
        f.write(readme_content)
    
    # Create batch file for installation
    install_bat = '''@echo off
echo Installing Desktop Archiver...
echo.
echo This will integrate Desktop Archiver with Windows Explorer.
echo You can uninstall by running this application and selecting "Remove Integration"
echo.
pause
echo.
echo Starting Desktop Archiver...
DesktopArchiver.exe
'''
    
    with open(package_dir / 'Install.bat', 'w') as f:
        f.write(install_bat)
    
    print(f"Package created in: {package_dir.absolute()}")

def main():
    """Main build function"""
    print("Desktop Archiver - Windows Build Tool")
    print("=" * 40)
    
    # Check if running on Windows for best results
    if os.name != 'nt':
        print("Warning: Building on non-Windows system. Some features may not work correctly.")
    
    # Check dependencies
    try:
        import PyQt5
        import PIL
        import py7zr
        import rarfile
        import cryptography
        import psutil
        print("All dependencies found")
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install all required packages first")
        return False
    
    # Build executable
    success = build_executable()
    
    if success:
        print("\nBuild completed successfully!")
        print("Your Windows executable is ready for distribution.")
        print("\nFiles created:")
        print("- dist/DesktopArchiver.exe (standalone executable)")
        print("- package/ (distribution package)")
    else:
        print("\nBuild failed. Please check the error messages above.")
    
    return success

if __name__ == '__main__':
    main()