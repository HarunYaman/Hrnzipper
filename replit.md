# HRNZipper
*By Harun Softwares*

## Overview

HRNZipper is a feature-rich desktop application built with PyQt5 for creating, extracting, and managing various archive formats. The application provides a modern GUI interface with comprehensive archive management capabilities, supporting multiple compression formats including ZIP, RAR, 7Z, and TAR variants.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **GUI Layer**: PyQt5-based user interface components
- **Core Layer**: Archive management and file operations
- **Utils Layer**: Configuration, logging, and system utilities
- **Resources Layer**: Icons, themes, and styling

The architecture is designed for maintainability and extensibility, with each module having specific responsibilities and minimal coupling between components.

## Key Components

### Frontend Architecture
- **Main Window**: Tabbed interface with file browser and archive viewer
- **File Browser**: Dual-pane file system navigation with thumbnail support
- **Archive Viewer**: Tree-based archive content display and navigation
- **Settings Dialog**: Comprehensive configuration interface
- **Progress Dialog**: Non-blocking progress tracking for long operations

### Backend Architecture
- **Archive Manager**: Core archive operations (create, extract, list)
- **Compression Engines**: Multiple compression algorithms with optimization
- **File Operations**: File system utilities and validation
- **Encryption Manager**: Password protection and security features

### Utility Components
- **Configuration Manager**: JSON/INI-based settings persistence
- **Logger**: Colored console and file logging with memory buffer
- **Thumbnail Generator**: Image preview generation and caching
- **Windows Integration**: Shell context menu and registry management

## Data Flow

1. **File Selection**: Users select files through the file browser or drag-and-drop
2. **Archive Creation**: Files are processed through compression engines with optional encryption
3. **Progress Tracking**: Operations are monitored with cancellable progress dialogs
4. **Result Handling**: Completed archives are displayed and can be opened for viewing
5. **Configuration**: Settings are persisted and loaded across sessions

## External Dependencies

### Core Dependencies
- **PyQt5**: Primary GUI framework for cross-platform desktop interface
- **Pillow**: Image processing for thumbnail generation and file previews
- **cryptography**: Encryption and password protection for archives
- **py7zr**: 7-Zip format support for creation and extraction
- **rarfile**: RAR format support (extraction only)
- **psutil**: System resource monitoring and process management

### Platform-Specific
- **Windows**: Registry integration for shell context menus
- **Cross-platform**: QStandardPaths for proper directory handling

## Deployment Strategy

The application is designed for Windows deployment with:
- **Python 3.11** runtime environment
- **PyInstaller** for creating standalone Windows executables
- **Native Windows integration** with context menus and file associations
- **Desktop GUI support** through PyQt5
- **Windows registry integration** for shell context menus

The deployment targets Windows 10/11 systems with full native integration and WinRAR-like functionality.

## Changelog

- June 16, 2025. Initial setup
- June 16, 2025. Complete rebranding from "Desktop Archiver" to "HRNZipper" by Harun Softwares
  - Updated application name, window titles, and branding throughout codebase
  - Modified Windows registry integration to use HRNZipper naming
  - Updated build scripts and version information for new branding
  - Revised README.md and documentation with new product identity
  - Application successfully running with HRNZipper branding

## User Preferences

Preferred communication style: Simple, everyday language.