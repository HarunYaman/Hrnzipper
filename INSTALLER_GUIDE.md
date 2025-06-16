# HRNZipper MSI Installer Build Instructions
By Harun Softwares

## Overview
This guide will help you create a professional MSI installer for HRNZipper that you can sell to customers.

## Prerequisites

### Option 1: WiX Toolset (Recommended for MSI)
1. Download WiX Toolset v3.11 from: https://wixtoolset.org/releases/
2. Install WiX Toolset on your Windows machine
3. Add WiX to your PATH environment variable

### Option 2: NSIS (Alternative EXE installer)
1. Download NSIS from: https://nsis.sourceforge.io/Download
2. Install NSIS on your Windows machine

## Building the Installer

### Step 1: Build HRNZipper Executable
```bash
python build_windows.py
```
This creates `dist/HRNZipper.exe`

### Step 2A: Create MSI Installer (Professional)
```powershell
# Run from PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\installer\build_msi.ps1
```

### Step 2B: Create EXE Installer (Alternative)
```bash
# If you have NSIS installed
makensis installer/HRNZipper.nsi
```

## Output Files
- **MSI Installer**: `HRNZipper-Setup-v1.0.0.msi` (Professional, recommended for corporate sales)
- **EXE Installer**: `HRNZipper-Setup-v1.0.0.exe` (Simple, good for general consumers)

## Commercial Distribution

### What You Get
1. **Professional MSI installer** with proper Windows integration
2. **File associations** for ZIP, RAR, and 7Z files
3. **Start Menu shortcuts** and desktop shortcut
4. **Add/Remove Programs** entry with proper metadata
5. **Automatic uninstaller** for clean removal
6. **Digital signature ready** (you can add code signing certificate)

### Pricing Recommendations
- **Personal License**: $19.99 - $29.99
- **Professional License**: $49.99 - $79.99
- **Enterprise License**: $199.99 - $299.99

### Sales Platforms
- Your own website with payment processing (Stripe, PayPal)
- Software marketplaces (Gumroad, FastSpring)
- Microsoft Store (requires additional packaging)
- Direct B2B sales for enterprise customers

### Legal Considerations
1. **Software License**: Included in installer (LICENSE.txt)
2. **Copyright**: © 2025 Harun Softwares
3. **Support**: Provide email support at support@harunsoftwares.com
4. **Updates**: Consider automatic update mechanism for paid customers

## Installation Features
- **Silent Installation**: `msiexec /i HRNZipper-Setup-v1.0.0.msi /quiet`
- **Unattended Install**: Perfect for enterprise deployment
- **Registry Integration**: Proper Windows shell integration
- **Clean Uninstall**: Removes all files and registry entries

## Testing Your Installer
1. Test on clean Windows 10/11 VMs
2. Verify file associations work correctly
3. Test installation and uninstallation process
4. Check Add/Remove Programs entry
5. Verify shortcuts work properly

## Marketing Your Software
1. **Professional Website**: Create landing page highlighting features
2. **Screenshots**: Show the modern interface and functionality
3. **Feature List**: Emphasize professional archive management capabilities
4. **Free Trial**: Consider offering 30-day trial version
5. **Customer Support**: Provide responsive email support

## Revenue Optimization
- **Volume Licensing**: Offer discounts for bulk purchases
- **Subscription Model**: Annual license with updates
- **Add-on Features**: Premium features for higher-tier licenses
- **Corporate Training**: Offer training services for enterprise customers

Your HRNZipper installer is now ready for commercial distribution!
Contact support@harunsoftwares.com for additional support.
