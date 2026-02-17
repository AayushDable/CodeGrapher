from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsEllipseItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor

class ConnectionPoint(QGraphicsEllipseItem):
    """A connection point on a block"""
    
    def __init__(self, parent_block, side, scene_manager):
        super().__init__(-3, -3, 6, 6)  # Even smaller: 6x6 pixels
        
        self.parent_block = parent_block
        self.side = side
        self.scene_manager = scene_manager
        self.is_active = False
        
        # Default style (green)
        self.normal_brush = QBrush(QColor(76, 175, 80))
        self.normal_pen = QPen(QColor(56, 142, 60), 2)
        
        # Active style (red)
        self.active_brush = QBrush(QColor(244, 67, 54))
        self.active_pen = QPen(QColor(198, 40, 40), 2)
        
        self.setBrush(self.normal_brush)
        self.setPen(self.normal_pen)
        
        self.setFlag(QGraphicsItem.ItemIsSelectable, False)
        self.setAcceptedMouseButtons(Qt.LeftButton)
        self.setCursor(Qt.PointingHandCursor)
        
        self.setParentItem(parent_block)
        self.update_position()
        
        self.setToolTip(f"Click to connect from {side}")
    
    def update_position(self):
        """Update position based on parent block size and side"""
        rect = self.parent_block.rect()
        
        if self.side == 'top':
            self.setPos(rect.width() / 2, 0)
        elif self.side == 'bottom':
            self.setPos(rect.width() / 2, rect.height())
        elif self.side == 'left':
            self.setPos(0, rect.height() / 2)
        elif self.side == 'right':
            self.setPos(rect.width(), rect.height() / 2)
    
    def set_active(self, active):
        """Set active state"""
        self.is_active = active
        if active:
            self.setBrush(self.active_brush)
            self.setPen(self.active_pen)
            self.setToolTip("Click another dot to complete connection")
        else:
            self.setBrush(self.normal_brush)
            self.setPen(self.normal_pen)
            self.setToolTip(f"Click to connect from {self.side}")
    
    def mousePressEvent(self, event):
        """Handle click on connection point"""
        if event.button() == Qt.LeftButton:
            self.scene_manager.on_connection_point_clicked(self)
            event.accept()
        else:
            super().mousePressEvent(event)
