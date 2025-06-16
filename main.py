#!/usr/bin/env python3
"""
HRNZipper - Main Application Entry Point
A feature-rich desktop archiver with modern PyQt GUI supporting multiple formats
By Harun Softwares
"""

import sys
import os
import logging
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtCore import Qt, QDir, QStandardPaths
from PyQt5.QtGui import QIcon, QPixmap

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow
from utils.config_manager import ConfigManager
from utils.logger import setup_logging

def setup_application():
    """Initialize the application with proper settings"""
    # Enable high DPI scaling BEFORE creating QApplication
    try:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    except AttributeError:
        # Older Qt versions may not have these attributes
        pass
    
    app = QApplication(sys.argv)
    app.setApplicationName("HRNZipper")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Harun Softwares")
    
    # Set application icon after QApplication is created
    try:
        from resources.icons import create_app_icon
        icon_pixmap = create_app_icon(64)
        app.setWindowIcon(QIcon(icon_pixmap))
    except ImportError:
        # Fallback if icon resources not available
        pass
    
    return app

def setup_directories():
    """Create necessary application directories"""
    config_dir = QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)
    cache_dir = QStandardPaths.writableLocation(QStandardPaths.CacheLocation)
    
    for directory in [config_dir, cache_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

def main():
    """Main application entry point"""
    try:
        # Setup logging
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Starting HRNZipper...")
        
        # Create application directories
        setup_directories()
        
        # Initialize PyQt application
        app = setup_application()
        
        # Load configuration
        config = ConfigManager()
        
        # Apply theme
        theme = config.get_setting('appearance', 'theme', 'dark')
        if theme == 'fusion':
            app.setStyle(QStyleFactory.create('Fusion'))
        
        # Load stylesheet
        try:
            with open('resources/styles.qss', 'r') as f:
                app.setStyleSheet(f.read())
        except FileNotFoundError:
            logger.warning("Style sheet not found, using default theme")
        
        # Create and show main window
        main_window = MainWindow()
        main_window.show()
        
        # Handle command line arguments
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            if os.path.exists(file_path):
                main_window.open_file(file_path)
        
        logger.info("Application started successfully")
        return app.exec_()
        
    except Exception as e:
        logging.error(f"Critical error during startup: {e}")
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
