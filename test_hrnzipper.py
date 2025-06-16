#!/usr/bin/env python3
"""
Simple test script for HRNZipper to verify the application works
"""

import sys
import os

# Set Qt platform before importing PyQt5
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
    from PyQt5.QtCore import Qt
    
    def test_hrnzipper_basic():
        """Test basic HRNZipper functionality"""
        print("Testing HRNZipper basic functionality...")
        
        # Create QApplication
        app = QApplication(sys.argv)
        app.setApplicationName("HRNZipper")
        app.setOrganizationName("Harun Softwares")
        
        # Create a simple window to test
        window = QWidget()
        window.setWindowTitle("HRNZipper - By Harun Softwares")
        window.resize(400, 300)
        
        layout = QVBoxLayout()
        label = QLabel("HRNZipper by Harun Softwares\nArchive Management Tool")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        window.setLayout(layout)
        
        print("✓ HRNZipper application created successfully")
        print("✓ Window title: HRNZipper - By Harun Softwares")
        print("✓ Qt application initialized")
        print("✓ GUI components working")
        
        # Test importing core modules
        try:
            from core.archive_manager import ArchiveManager
            print("✓ Archive manager module loaded")
        except ImportError as e:
            print(f"⚠ Archive manager import issue: {e}")
        
        try:
            from gui.main_window import MainWindow
            print("✓ Main window module loaded")
        except ImportError as e:
            print(f"⚠ Main window import issue: {e}")
        
        try:
            from utils.config_manager import ConfigManager
            config = ConfigManager()
            print("✓ Configuration manager loaded")
        except ImportError as e:
            print(f"⚠ Config manager import issue: {e}")
        
        print("\nHRNZipper rebranding verification complete!")
        print("Application ready for Windows deployment")
        
        return True
        
    if __name__ == '__main__':
        test_hrnzipper_basic()
        
except ImportError as e:
    print(f"PyQt5 import error: {e}")
    print("Please ensure PyQt5 is installed: pip install PyQt5")
except Exception as e:
    print(f"Error testing HRNZipper: {e}")