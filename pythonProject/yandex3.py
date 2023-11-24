import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import io
import sqlite3
from PyQt5 import uic

dis = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyWidget</class>
 <widget class="QMainWindow" name="MyWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>794</width>
    <height>347</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>69</y>
      <width>781</width>
      <height>241</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_8">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_8">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>ID:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_3">
         <property name="text">
          <string>Название:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_4">
         <property name="text">
          <string>Год выпуска:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_5">
         <property name="text">
          <string>Жанр:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_2">
         <property name="text">
          <string>Продолжительность:</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_9">
       <item>
        <widget class="QLineEdit" name="idEdit"/>
       </item>
       <item>
        <widget class="QLineEdit" name="titleEdit"/>
       </item>
       <item>
        <widget class="QLineEdit" name="yearEdit"/>
       </item>
       <item>
        <widget class="QLineEdit" name="genreEdit"/>
       </item>
       <item>
        <widget class="QLineEdit" name="durationEdit"/>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QComboBox" name="parameterSelection">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>30</y>
      <width>211</width>
      <height>31</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Год выпуска</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Название</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Продолжительность</string>
     </property>
    </item>
   </widget>
   <widget class="QLineEdit" name="queryLine">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>30</y>
      <width>441</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="queryButton">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>30</y>
      <width>111</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Поиск</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        tem = io.StringIO(dis)
        uic.loadUi(tem, self)
        self.queryButton.clicked.connect(self.finding)

    def finding(self):
        text = self.queryLine.text()
        bd = sqlite3.connect('films_db.sqlite')
        cursor = bd.cursor()
        if self.parameterSelection.currentText() == 'Год выпуска':
            self.yearEdit.setText(cursor.execute(f'''SELECT year FROM films
                    WHERE year = {text}'''))
            self.titleEdit.setText(cursor.execute(f'''SELECT title FROM films
                    WHERE year = {text}'''))
            self.idEdit.setText(cursor.execute(f'''SELECT id FROM films
                    WHERE year = {text}'''))
            self.genreEdit.setText(cursor.execute(f'''SELECT genre FROM films
                    WHERE year = {text}'''))
            self.durationEdit.setText(cursor.execute(f'''SELECT duration
                    FROM films WHERE year = {text}'''))
        elif self.parameterSelection.currentText() == 'Название':
            self.yearEdit.setText(cursor.execute(f'''SELECT year FROM films
                    WHERE title = {text}'''))
            self.titleEdit.setText(cursor.execute(f'''SELECT title FROM films
                    WHERE title = {text}'''))
            self.idEdit.setText(cursor.execute(f'''SELECT id FROM films
                    WHERE title = {text}'''))
            self.genreEdit.setText(cursor.execute(f'''SELECT genre FROM films
                    WHERE title = {text}'''))
            self.durationEdit.setText(cursor.execute(f'''SELECT duration
                    FROM films WHERE title = {text}'''))
        elif self.parameterSelection.currentText() == 'Продолжительность':
            self.yearEdit.setText(cursor.execute(f'''SELECT year FROM films
                    WHERE duration = {text}'''))
            self.titleEdit.setText(cursor.execute(f'''SELECT title FROM films
                    WHERE duration = {text}'''))
            self.idEdit.setText(cursor.execute(f'''SELECT id FROM films
                    WHERE duration = {text}'''))
            self.genreEdit.setText(cursor.execute(f'''SELECT genre FROM films
                    WHERE duration = {text}'''))
            self.durationEdit.setText(cursor.execute(f'''SELECT duration
                    FROM films WHERE duration = {text}'''))

        bd.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
