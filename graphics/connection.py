from PyQt5.QtWidgets import (QGraphicsItem,QGraphicsPathItem,QGraphicsPolygonItem)
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QBrush, QColor, QPainterPath, QPolygonF
import math



class Connection(QGraphicsPathItem):
    """Connection between blocks with bezier curve and arrows"""
    
    def __init__(self, from_block, to_block, from_side='right', to_side='left', 
                 flow_type='one_way', line_style='solid', line_color=None):
        super().__init__()
        
        self.from_block = from_block
        self.to_block = to_block
        self.from_side = from_side
        self.to_side = to_side
        self.flow_type = flow_type
        self.line_style = line_style
        self.line_color = line_color if line_color else QColor(100, 100, 100)
        
        self.arrow_size = 15
        
        self.arrow_end = None
        self.arrow_start = None
        
        self.update_style()
        
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges) 
        self.setZValue(-1)
        
        self.update_path()
    
    def set_line_color(self, color):
        """Change line color"""
        self.line_color = color
        self.update_style()
        self.update_path()
    
    def update_style(self):
        """Update pen style based on line_style and color"""
        pen = QPen(self.line_color)
        pen.setWidth(3)
        
        if self.line_style == 'dashed':
            pen.setStyle(Qt.DashLine)
        else:
            pen.setStyle(Qt.SolidLine)
        
        self.setPen(pen)
    
    def get_connection_point(self, block, side):
        """Get the connection point position for a block side"""
        rect = block.sceneBoundingRect()
        
        if side == 'top':
            return QPointF(rect.center().x(), rect.top())
        elif side == 'bottom':
            return QPointF(rect.center().x(), rect.bottom())
        elif side == 'left':
            return QPointF(rect.left(), rect.center().y())
        elif side == 'right':
            return QPointF(rect.right(), rect.center().y())
        
        return rect.center()
    
    def update_path(self):
        """Update the bezier curve path with arrows"""
        start = self.get_connection_point(self.from_block, self.from_side)
        end = self.get_connection_point(self.to_block, self.to_side)
        
        path = QPainterPath()
        path.moveTo(start)
        
        distance = abs(end.x() - start.x()) + abs(end.y() - start.y())
        offset = min(distance / 3, 100)
        
        if self.from_side == 'right':
            cp1 = QPointF(start.x() + offset, start.y())
        elif self.from_side == 'left':
            cp1 = QPointF(start.x() - offset, start.y())
        elif self.from_side == 'top':
            cp1 = QPointF(start.x(), start.y() - offset)
        elif self.from_side == 'bottom':
            cp1 = QPointF(start.x(), start.y() + offset)
        else:
            cp1 = start
        
        if self.to_side == 'left':
            cp2 = QPointF(end.x() - offset, end.y())
        elif self.to_side == 'right':
            cp2 = QPointF(end.x() + offset, end.y())
        elif self.to_side == 'top':
            cp2 = QPointF(end.x(), end.y() - offset)
        elif self.to_side == 'bottom':
            cp2 = QPointF(end.x(), end.y() + offset)
        else:
            cp2 = end
        
        path.cubicTo(cp1, cp2, end)
        
        self.setPath(path)
        
        # Clean up old arrows
        if self.arrow_end:
            if self.arrow_end.scene():
                self.scene().removeItem(self.arrow_end)
            self.arrow_end = None
        
        if self.arrow_start:
            if self.arrow_start.scene():
                self.scene().removeItem(self.arrow_start)
            self.arrow_start = None
        
        # Create new arrows
        if self.flow_type == 'one_way':
            self.arrow_end = self.create_arrow_head(end, cp2)
            # Add to scene immediately if available
            if self.scene():
                self.scene().addItem(self.arrow_end)
        
        elif self.flow_type == 'bidirectional':
            self.arrow_end = self.create_arrow_head(end, cp2)
            self.arrow_start = self.create_arrow_head(start, cp1, reverse=True)
            # Add to scene immediately if available
            if self.scene():
                self.scene().addItem(self.arrow_end)
                self.scene().addItem(self.arrow_start)

    
    def create_arrow_head(self, tip, direction_point, reverse=False):
        """Create an arrow head as a filled polygon"""
        dx = tip.x() - direction_point.x()
        dy = tip.y() - direction_point.y()
        
        angle = math.atan2(dy, dx)
        
        if reverse:
            angle += math.pi
        
        arrow_p1 = tip
        arrow_p2 = QPointF(
            tip.x() - self.arrow_size * math.cos(angle - math.pi / 6),
            tip.y() - self.arrow_size * math.sin(angle - math.pi / 6)
        )
        arrow_p3 = QPointF(
            tip.x() - self.arrow_size * math.cos(angle + math.pi / 6),
            tip.y() - self.arrow_size * math.sin(angle + math.pi / 6)
        )
        
        polygon = QPolygonF([arrow_p1, arrow_p2, arrow_p3])
        
        arrow_item = QGraphicsPolygonItem(polygon)
        arrow_item.setBrush(QBrush(self.line_color))
        arrow_item.setPen(QPen(self.line_color))
        arrow_item.setZValue(-1)
        
        return arrow_item
    
    def set_flow_type(self, flow_type):
        """Change flow type"""
        self.flow_type = flow_type
        self.update_path()
    
    def set_line_style(self, line_style):
        """Change line style"""
        self.line_style = line_style
        self.update_style()
        self.update_path()

    def itemChange(self, change, value):
        """Handle item changes - particularly when added to scene"""
        if change == QGraphicsItem.ItemSceneChange:
            # When being added to a scene, ensure arrows are also added
            new_scene = value
            if new_scene:
                # Re-create arrows if they exist but aren't in the scene
                if self.arrow_end and not self.arrow_end.scene():
                    new_scene.addItem(self.arrow_end)
                if self.arrow_start and not self.arrow_start.scene():
                    new_scene.addItem(self.arrow_start)
        
        return super().itemChange(change, value)
