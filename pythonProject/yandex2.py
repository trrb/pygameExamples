import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtWidgets import QFileDialog
import io
from PyQt5 import uic

textQT = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyPillow</class>
 <widget class="QMainWindow" name="MyPillow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>485</width>
    <height>430</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>191</width>
      <height>351</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="channelButtons">
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>R</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_3">
       <property name="text">
        <string>G</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>B</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_4">
       <property name="text">
        <string>ALL</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>350</y>
      <width>481</width>
      <height>51</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="rotateButtons">
     <item>
      <widget class="QPushButton" name="pushButton_6">
       <property name="text">
        <string>Против часовой стрелки</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_5">
       <property name="text">
        <string>По часовой стрелке</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="curr_image">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>291</width>
      <height>311</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        tem = io.StringIO(textQT)
        uic.loadUi(tem, self)
        curr_image = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec_())