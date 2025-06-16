# HRNZipper
*By Harun Softwares*

A feature-rich Windows desktop archiver with modern PyQt5 GUI, supporting multiple archive formats with WinRAR-like functionality and native Windows Explorer integration.

## Features

### Archive Formats Support
- **ZIP** - Create and extract ZIP archives with password protection
- **RAR** - Extract RAR archives (creation requires WinRAR)
- **7Z** - Full support for 7-Zip format with advanced compression
- **TAR** - TAR, TAR.GZ, TAR.BZ2 support for Unix archives

### Windows Integration
- **Windows Explorer Context Menus** - Right-click archives to extract or folders to compress
- **File Associations** - Double-click archive files to open with HRNZipper
- **Registry Integration** - Professional Windows integration with proper uninstall

### User Interface
- **Modern Dark Theme** - Professional dark interface optimized for long usage
- **Tabbed Interface** - File browser and compression settings in organized tabs
- **Progress Tracking** - Real-time progress for all operations with cancel support
- **Dual-Pane Design** - File browser and archive viewer side-by-side

### Advanced Features
- **Password Protection** - Secure archives with AES-256 encryption
- **Batch Operations** - Process multiple files and folders simultaneously
- **Compression Levels** - Adjustable compression from fastest to maximum
- **File Thumbnails** - Preview images and documents before extraction
- **Archive Testing** - Verify archive integrity before extraction

## System Requirements

- **Windows 10** or **Windows 11** (64-bit)
- **100 MB** free disk space
- **4 GB RAM** recommended
- **Administrator privileges** for Windows integration setup

## Installation

### Quick Install
1. Download `HRNZipper.exe` from the releases
2. Run the executable - no installation required
3. The application will offer to integrate with Windows Explorer

### Windows Integration Setup
On first run, HRNZipper will offer to integrate with Windows:
- Context menus for archive files (Extract Here, Extract To...)
- Context menus for folders (Add to Archive)
- File associations for supported formats

### Build from Source
```bash
# Clone the repository
git clone https://github.com/HarunYaman/Hrnzipper
cd hrnzipper

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Build Windows executable
python build_windows.py
```

## Usage

### Basic Operations
- **Open Archive**: Double-click archive files or use File → Open
- **Create Archive**: Select files/folders and use Create Archive tab
- **Extract Archive**: Right-click archive and select extraction option
- **Add to Archive**: Right-click folder and select archive format

### Context Menu Operations
After Windows integration setup:
- Right-click **archive files** → Extract Here / Extract To...
- Right-click **folders** → Add to ZIP/7Z/TAR archive
- Right-click **empty space** → HRNZipper (create new archive)

### Advanced Settings
- **Compression Level**: Adjust speed vs. size ratio
- **Password Protection**: Enable encryption for sensitive data
- **Solid Compression**: Better compression for similar files
- **Multi-threading**: Utilize multiple CPU cores for faster operations

## Configuration

Settings are automatically saved and include:
- **Window layout and size**
- **Default compression settings**
- **File associations preferences**
- **Theme and appearance options**

Configuration files are stored in:
```
%APPDATA%\HRNZipper\
```

## Supported Formats

| Format | Create | Extract | Password | Notes |
|--------|--------|---------|----------|-------|
| ZIP | ✓ | ✓ | ✓ | Full support with deflate/LZMA |
| RAR | ✗ | ✓ | ✓ | Extraction only (license required for creation) |
| 7Z | ✓ | ✓ | ✓ | Best compression ratio |
| TAR | ✓ | ✓ | ✗ | Unix/Linux standard |
| TAR.GZ | ✓ | ✓ | ✗ | Gzip compressed TAR |
| TAR.BZ2 | ✓ | ✓ | ✗ | Bzip2 compressed TAR |

## Windows Integration Details

### Registry Entries
Desktop Archiver creates registry entries for:
- File type associations (HKEY_CLASSES_ROOT)
- Context menu commands
- Application registration

### Uninstall
To remove Windows integration:
1. Run Desktop Archiver
2. Go to Settings → Windows Integration
3. Click "Remove Integration"

Or manually remove registry entries under:
```
HKEY_CLASSES_ROOT\DesktopArchiver*
HKEY_CLASSES_ROOT\Directory\shell\DesktopArchiver
```

## Security

### Password Protection
- **AES-256 encryption** for ZIP and 7Z archives
- **PBKDF2 key derivation** with configurable iterations
- **Secure password validation** without full decryption

### File Safety
- **Integrity verification** with SHA-256 checksums
- **Secure temporary files** with proper cleanup
- **Safe extraction** with path traversal protection

## Troubleshooting

### Common Issues

**Archive won't open**
- Verify the file isn't corrupted using Test Archive
- Check if password protection is enabled
- Ensure sufficient disk space for extraction

**Context menus missing**
- Run as Administrator and reinstall integration
- Check Windows registry permissions
- Verify antivirus isn't blocking registry changes

**Slow compression**
- Reduce compression level for faster processing
- Disable solid compression for many small files
- Check available system memory

**Extract errors**
- Verify archive integrity with Test function
- Check destination folder permissions
- Ensure sufficient disk space

### Log Files
Debug information is saved to:
```
%APPDATA%\Desktop Archiver\logs\
```

## Development

### Architecture
- **PyQt5** - Modern cross-platform GUI framework
- **Modular design** - Separated core, GUI, and utility components
- **Plugin architecture** - Extensible compression engines
- **Windows API integration** - Native shell and registry operations

### Contributing
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

### Building
Use the included `build_windows.py` script to create distributable executables:
```bash
python build_windows.py
```

This creates:
- `dist/DesktopArchiver.exe` - Standalone executable
- `package/` - Distribution package with documentation

## License

Desktop Archiver is released under the MIT License. See LICENSE file for details.

## Credits

- **PyQt5** - GUI framework
- **py7zr** - 7-Zip format support
- **rarfile** - RAR extraction support
- **cryptography** - Encryption and security
- **Pillow** - Image processing and thumbnails

## Support

For support and bug reports:
- GitHub Issues: https://github.com/your-repo/desktop-archiver/issues
- Documentation: https://your-repo.github.io/desktop-archiver/

---

**Desktop Archiver** - Professional archive management for Windows
