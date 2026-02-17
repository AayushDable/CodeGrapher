from PyQt5.QtWidgets import (QVBoxLayout, QListWidget, QLabel, QListWidgetItem,
                             QDialog, QDialogButtonBox, QTextEdit,)
from PyQt5.QtCore import Qt


class FunctionSearchDialog(QDialog):
    """Dialog showing search results for functions"""
    
    def __init__(self, function_name, results, parent=None):
        super().__init__(parent)
        
        self.function_name = function_name
        self.results = results
        self.selected_result = None
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle(f"Found {len(self.results)} match(es) for '{self.function_name}'")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        
        layout = QVBoxLayout()
        
        info_label = QLabel(f"<b>Select the correct function:</b>")
        layout.addWidget(info_label)
        
        self.results_list = QListWidget()
        for result in self.results:
            item_text = f"{result['file']} (line {result['line']})"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, result)
            self.results_list.addItem(item)
        
        self.results_list.itemDoubleClicked.connect(self.on_item_selected)
        layout.addWidget(self.results_list)
        
        preview_label = QLabel("<b>Preview:</b>")
        layout.addWidget(preview_label)
        
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setMaximumHeight(150)
        layout.addWidget(self.preview_text)
        
        self.results_list.currentItemChanged.connect(self.update_preview)
        
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        
        if self.results:
            self.results_list.setCurrentRow(0)
    
    def update_preview(self, current, previous):
        """Update preview when selection changes"""
        if not current:
            return
        
        result = current.data(Qt.UserRole)
        self.preview_text.setPlainText(result.get('code', ''))
    
    def on_item_selected(self, item):
        """Handle item selection"""
        self.selected_result = item.data(Qt.UserRole)
        self.accept()
    
    def accept(self):
        """Save selected result"""
        current_item = self.results_list.currentItem()
        if current_item:
            self.selected_result = current_item.data(Qt.UserRole)
        super().accept()
