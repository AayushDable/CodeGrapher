from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QTextEdit, QPushButton, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont



class InfoDialog(QDialog):
    """Dialog to show block information"""
    
    def __init__(self, block, parent=None):
        super().__init__(parent)
        
        self.block = block
        self.setWindowTitle(f"Info: {block.display_name}")
        self.setMinimumSize(500, 400)
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the dialog UI"""
        layout = QVBoxLayout()
        
        # Title with original name and alias
        if self.block.display_name != self.block.name:
            # Show both original name and alias
            title_label = QLabel(f"<h2>{self.block.display_name}</h2>")
            layout.addWidget(title_label)
            
            original_label = QLabel(f"<i>Original name: {self.block.name}</i>")
            original_label.setStyleSheet("color: #666; font-size: 11px;")
            layout.addWidget(original_label)
        else:
            # No alias, just show the name
            title_label = QLabel(f"<h2>{self.block.display_name}</h2>")
            layout.addWidget(title_label)
        
        # Type
        type_label = QLabel(f"<b>Type:</b> {self.block.block_type}")
        layout.addWidget(type_label)
        
        # Separator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        
        # File path (if available)
        if 'filePath' in self.block.metadata:
            file_label = QLabel(f"<b>File:</b> {self.block.metadata['filePath']}")
            layout.addWidget(file_label)
            
            line_label = QLabel(f"<b>Line:</b> {self.block.metadata.get('lineNumber', 'N/A')}")
            layout.addWidget(line_label)
            
            # Separator
            line2 = QFrame()
            line2.setFrameShape(QFrame.HLine)
            line2.setFrameShadow(QFrame.Sunken)
            layout.addWidget(line2)
        
        # Docstring or Description
        if self.block.block_type in ['METHOD', 'FUNCTION', 'CLASS']:
            # Show docstring (will be populated by main_window)
            docstring_label = QLabel("<b>Docstring:</b>")
            layout.addWidget(docstring_label)
            
            self.docstring_text = QTextEdit()
            self.docstring_text.setReadOnly(True)
            self.docstring_text.setPlainText("Loading...")
            self.docstring_text.setMaximumHeight(200)
            font = QFont("Courier", 9)
            self.docstring_text.setFont(font)
            layout.addWidget(self.docstring_text)
        
        else:
            # Show editable description for subdirectories
            desc_label = QLabel("<b>Description:</b>")
            layout.addWidget(desc_label)
            
            self.description_text = QTextEdit()
            self.description_text.setPlaceholderText("Add a description for this directory...")
            self.description_text.setMaximumHeight(150)
            
            # Load existing description
            existing_desc = self.block.metadata.get('description', '')
            self.description_text.setPlainText(existing_desc)
            
            layout.addWidget(self.description_text)
        
        layout.addStretch()
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        if self.block.block_type in ['SUBDIRECTORY', 'CLASS']:
            # Save button for editable description
            save_btn = QPushButton("💾 Save Description")
            save_btn.clicked.connect(self.save_description)
            button_layout.addWidget(save_btn)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def set_docstring(self, docstring):
        """Set the docstring text (called from main_window)"""
        if hasattr(self, 'docstring_text'):
            if docstring:
                self.docstring_text.setPlainText(docstring)
            else:
                self.docstring_text.setPlainText("No docstring available.")
                self.docstring_text.setStyleSheet("color: #999; font-style: italic;")
    
    def save_description(self):
        """Save the description to block metadata"""
        if hasattr(self, 'description_text'):
            new_desc = self.description_text.toPlainText().strip()
            self.block.metadata['description'] = new_desc
            self.accept()