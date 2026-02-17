import os
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLineEdit, QListWidget, QListWidgetItem, QLabel,
                             QFileDialog, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap, QIconEngine, QImage, QPainter
from PyQt5.QtCore import Qt, QSize, QRect, QPoint
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import Qt, QSize, QRect, QRectF, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QIconEngine, QImage, QPainter
from PyQt5.QtSvg import QSvgRenderer

class SmoothIconEngine(QIconEngine):
    """Custom icon engine with smooth rendering for sharp icons"""
    
    def __init__(self, icon_path: str):
        super().__init__()
        self.icon_path = icon_path
        self.is_svg = icon_path.lower().endswith('.svg')
    
    def paint(self, painter: QPainter, rect: QRect, mode: QIcon.Mode, state: QIcon.State):
        painter.setRenderHints(QPainter.Antialiasing | 
                               QPainter.SmoothPixmapTransform)
        
        if self.is_svg:
            # Render SVG directly for vector quality
            renderer = QSvgRenderer(self.icon_path)
            renderer.render(painter, QRectF(rect))  # Convert QRect to QRectF
        else:
            # For raster images, use smooth scaling
            painter.drawImage(rect, QImage(self.icon_path))
    
    def pixmap(self, size: QSize, mode: QIcon.Mode, state: QIcon.State) -> QPixmap:
        pixmap = QPixmap(size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        self.paint(painter, QRect(QPoint(0, 0), size), mode, state)
        painter.end()
        return pixmap


class SmoothIcon(QIcon):
    """QIcon subclass with smooth rendering"""
    def __init__(self, icon_path: str):
        super().__init__(SmoothIconEngine(icon_path))


class ImagePickerDialog(QDialog):
    """Dialog for selecting images from icons folder or custom path"""
    
    def __init__(self, icons_folder='icons', parent=None):
        super().__init__(parent)
        self.setWindowTitle('Select Image/Icon')
        self.setMinimumSize(600, 500)
        
        self.icons_folder = icons_folder
        self.selected_path = None
        self.all_icons = []
        
        self.setup_ui()
        self.load_icons()
    
    def setup_ui(self):
        """Setup the dialog UI"""
        layout = QVBoxLayout(self)
        
        # 1. Custom icon section with browse button
        custom_layout = QHBoxLayout()
        custom_label = QLabel('Custom Icon:')
        self.custom_path_input = QLineEdit()
        self.custom_path_input.setPlaceholderText('Enter or browse for custom icon path...')
        browse_btn = QPushButton('Browse')
        browse_btn.clicked.connect(self.browse_custom_icon)
        
        custom_layout.addWidget(custom_label)
        custom_layout.addWidget(self.custom_path_input, 1)
        custom_layout.addWidget(browse_btn)
        layout.addLayout(custom_layout)
        
        # 2. Search bar
        search_layout = QHBoxLayout()
        search_label = QLabel('Search Icon:')
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Type to filter icons...')
        self.search_input.textChanged.connect(self.filter_icons)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input, 1)
        layout.addLayout(search_layout)
        
        # 3. Icon grid display
        self.icon_list = QListWidget()
        self.icon_list.setViewMode(QListWidget.IconMode)
        self.icon_list.setIconSize(QSize(64, 64))
        self.icon_list.setResizeMode(QListWidget.Adjust)
        self.icon_list.setSpacing(10)
        self.icon_list.setMovement(QListWidget.Static)
        self.icon_list.setWrapping(True)
        self.icon_list.itemDoubleClicked.connect(self.accept_selection)
        
        layout.addWidget(QLabel(f'Available Icons ({self.icons_folder}/):'))
        layout.addWidget(self.icon_list, 1)
        
        # Bottom buttons
        button_layout = QHBoxLayout()
        ok_btn = QPushButton('OK')
        cancel_btn = QPushButton('Cancel')
        ok_btn.clicked.connect(self.accept_selection)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)
    
    def browse_custom_icon(self):
        """Open file dialog to browse for custom icon"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Select Image',
            '',
            'Images (*.png *.jpg *.jpeg *.gif *.bmp *.svg);;All Files (*)'
        )
        
        if file_path:
            self.custom_path_input.setText(file_path)
    
    def load_icons(self):
        """Load all icons from the icons folder"""
        if not os.path.exists(self.icons_folder):
            print(f"Icons folder '{self.icons_folder}' not found")
            return
        
        # Get all image files from icons folder
        supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')
        
        for filename in sorted(os.listdir(self.icons_folder)):
            if filename.lower().endswith(supported_formats):
                icon_path = os.path.join(self.icons_folder, filename)
                self.all_icons.append((filename, icon_path))
        
        self.display_icons(self.all_icons)
    
    def display_icons(self, icons_to_display):
        """Display icons in the list widget"""
        self.icon_list.clear()
        
        for filename, icon_path in icons_to_display:
            item = QListWidgetItem()
            
            # Use custom SmoothIcon for sharp rendering
            icon = SmoothIcon(icon_path)
            
            item.setIcon(icon)
            item.setText(filename)
            item.setData(Qt.UserRole, icon_path)
            item.setToolTip(icon_path)
            
            self.icon_list.addItem(item)
    
    def filter_icons(self, search_text):
        """Filter icons based on search text"""
        if not search_text:
            self.display_icons(self.all_icons)
        else:
            filtered = [
                (filename, path) 
                for filename, path in self.all_icons 
                if search_text.lower() in filename.lower()
            ]
            self.display_icons(filtered)
    
    def accept_selection(self):
        """Accept the selected icon or custom path"""
        custom_path = self.custom_path_input.text().strip()
        if custom_path:
            custom_path = custom_path.strip('"').strip("'")
            if os.path.exists(custom_path):
                self.selected_path = custom_path
                self.accept()
                return
            else:
                from PyQt5.QtWidgets import QMessageBox
                QMessageBox.warning(self, 'Invalid Path', 
                                  f'The custom path does not exist:\n{custom_path}')
                return
        
        current_item = self.icon_list.currentItem()
        if current_item:
            self.selected_path = current_item.data(Qt.UserRole)
            self.accept()
        else:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, 'No Selection', 
                              'Please select an icon or provide a custom path.')
    
    def get_selected_path(self):
        """Return the selected image path"""
        return self.selected_path
