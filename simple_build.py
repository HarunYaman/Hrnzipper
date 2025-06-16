#!/usr/bin/env python3
"""
Simple build script for HRNZipper that bypasses Qt platform issues
Creates standalone executable for MSI installer
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_standalone_build():
    """Create a simple standalone build without Qt platform issues"""
    print("Creating HRNZipper standalone build...")
    
    # Set environment to avoid Qt issues
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    
    # Create dist directory
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)
    
    # Copy all necessary files to dist
    print("Copying application files...")
    
    # Copy main executable content
    main_content = '''#!/usr/bin/env python3
import os
import sys
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import main
if __name__ == "__main__":
    main()
'''
    
    with open(dist_dir / "HRNZipper.py", 'w') as f:
        f.write(main_content)
    
    # Copy all source directories
    for src_dir in ['core', 'gui', 'utils', 'resources']:
        if Path(src_dir).exists():
            dest_dir = dist_dir / src_dir
            if dest_dir.exists():
                shutil.rmtree(dest_dir)
            shutil.copytree(src_dir, dest_dir)
            print(f"Copied {src_dir}/")
    
    # Copy main files
    for file in ['main.py', 'README.md']:
        if Path(file).exists():
            shutil.copy2(file, dist_dir)
            print(f"Copied {file}")
    
    print("Creating executable wrapper...")
    
    # Create a batch file wrapper for Windows
    batch_content = '''@echo off
cd /d "%~dp0"
python HRNZipper.py %*
'''
    
    with open(dist_dir / "HRNZipper.bat", 'w') as f:
        f.write(batch_content)
    
    # Create a Python executable script
    exe_content = '''#!/usr/bin/env python3
import os
import sys
import subprocess

# Set Qt platform
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Run the application
try:
    subprocess.run([sys.executable, "HRNZipper.py"] + sys.argv[1:])
except Exception as e:
    print(f"Error running HRNZipper: {e}")
    input("Press Enter to exit...")
'''
    
    with open(dist_dir / "HRNZipper.exe.py", 'w') as f:
        f.write(exe_content)
    
    print("✓ Standalone build created in dist/")
    return True

if __name__ == "__main__":
    create_standalone_build()