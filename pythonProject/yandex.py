import io
from random import choice
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

templ = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>RandomString</class>
 <widget class="QMainWindow" name="RandomString">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>398</width>
    <height>59</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="mouseTracking">
    <bool>false</bool>
   </property>
   <property name="tabletTracking">
    <bool>true</bool>
   </property>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QPushButton" name="button">
         <property name="text">
          <string>Получить</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QTextEdit" name="text_field"/>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        tem = io.StringIO(templ)
        uic.loadUi(tem, self)
        self.button.clicked.connect(self.rand)

    def rand(self):
        try:
            with open('input.txt', encoding='UTF-8') as f:
                lines = f.readlines()
            self.text_field.setPlainText(choice(lines))
        except IndexError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec_())
