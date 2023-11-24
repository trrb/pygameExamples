import io
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

templ = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AntiPlagiarism</class>
 <widget class="QMainWindow" name="AntiPlagiarism">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>685</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>AntiPlagiarism</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QWidget" name="widget" native="true">
      <widget class="QDoubleSpinBox" name="alert_value">
       <property name="geometry">
        <rect>
         <x>150</x>
         <y>0</y>
         <width>621</width>
         <height>21</height>
        </rect>
       </property>
      </widget>
      <widget class="QLabel" name="label">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>151</width>
         <height>21</height>
        </rect>
       </property>
       <property name="text">
        <string>Порог срабатывания (%)</string>
       </property>
      </widget>
      <widget class="QPlainTextEdit" name="text1">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>70</y>
         <width>381</width>
         <height>511</height>
        </rect>
       </property>
      </widget>
      <widget class="QPlainTextEdit" name="text2">
       <property name="geometry">
        <rect>
         <x>390</x>
         <y>70</y>
         <width>381</width>
         <height>511</height>
        </rect>
       </property>
      </widget>
      <widget class="QLabel" name="label_2">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>50</y>
         <width>81</width>
         <height>21</height>
        </rect>
       </property>
       <property name="text">
        <string>Текст 1</string>
       </property>
      </widget>
      <widget class="QLabel" name="label_3">
       <property name="geometry">
        <rect>
         <x>390</x>
         <y>50</y>
         <width>81</width>
         <height>21</height>
        </rect>
       </property>
       <property name="text">
        <string>Текст 2</string>
       </property>
      </widget>
      <widget class="QPushButton" name="checkBtn">
       <property name="geometry">
        <rect>
         <x>10</x>
         <y>600</y>
         <width>761</width>
         <height>28</height>
        </rect>
       </property>
       <property name="text">
        <string>Сравнить</string>
       </property>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        tem = io.StringIO(templ)
        uic.loadUi(tem, self)
        self.checkBtn.clicked.connect(self.start)

    def start(self):
        count = 0
        count2 = 0
        text = self.text1.toPlainText().split('\n')
        text2 = self.text2.toPlainText().split('\n')
        for el in text:
            if el not in text2:
                count += 1
            else:
                count2 += 1
        print(count / count2 * 100)
        if self.alert_value.value() < count / count2 * 100:
            self.statusBar().showMessage(
                f"Тексты похожи на {round(count / count2 * 100, 2)}%, не плагиат")
        else:
            self.statusBar().showMessage(
                f"Тексты похожи на {round(count / count2 * 100, 2)}%, плагиат")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec_())
