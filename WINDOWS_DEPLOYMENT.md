# Windows Deployment Guide

## Desktop Archiver - Windows Distribution Package

This document provides instructions for deploying Desktop Archiver on Windows systems.

### Package Contents

- `DesktopArchiver.exe` - Main application executable
- `README.txt` - User documentation
- `Install.bat` - Quick installation script
- `LICENSE` - Software license

### System Requirements

- Windows 10 or Windows 11 (64-bit)
- 100 MB free disk space
- Administrator privileges for Windows integration

### Installation Options

#### Option 1: Portable Installation
1. Copy `DesktopArchiver.exe` to desired location
2. Run the executable - no installation required
3. Windows integration will be offered on first run

#### Option 2: Full Windows Integration
1. Run `Install.bat` as Administrator
2. Follow prompts to integrate with Windows Explorer
3. Archive files will show context menus for extraction
4. Folders will show context menus for compression

### Windows Integration Features

After installation with Windows integration:

**Archive Files (ZIP, RAR, 7Z, TAR)**
- Right-click → "Extract Here"
- Right-click → "Extract To..."
- Double-click to open in Desktop Archiver

**Folders**
- Right-click → "Add to Archive" → Choose format
- Submenu options: ZIP, 7Z, TAR

**Background (Empty Space)**
- Right-click → "Desktop Archiver" → Create new archive

### Registry Entries

The application creates these registry entries:
```
HKEY_CLASSES_ROOT\DesktopArchiverZIP
HKEY_CLASSES_ROOT\DesktopArchiverRAR
HKEY_CLASSES_ROOT\DesktopArchiver7Z
HKEY_CLASSES_ROOT\Directory\shell\DesktopArchiver
```

### Uninstall

To remove Windows integration:
1. Run Desktop Archiver
2. Go to Settings → Windows Integration
3. Click "Remove Integration"

Or manually delete registry entries above.

### Build Instructions

To build from source on Windows:

1. Install Python 3.11+
2. Install dependencies:
   ```
   pip install PyQt5 Pillow cryptography py7zr rarfile psutil pyinstaller
   ```
3. Run build script:
   ```
   python build_windows.py
   ```
4. Find executable in `dist/DesktopArchiver.exe`

### Distribution

The built executable is self-contained and can be distributed without Python installation. It includes all necessary dependencies and resources.

### Security Notes

- The application requires administrator privileges only for Windows integration setup
- Normal operation does not require elevated privileges
- Registry entries are standard Windows integration patterns
- No system files are modified outside of user data directories