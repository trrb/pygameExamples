import io
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

graf = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>FileStat</class>
 <widget class="QMainWindow" name="FileStat">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>367</width>
    <height>173</height>
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
      <width>361</width>
      <height>41</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>Имя файла</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="filenameEdit"/>
       </item>
       <item>
        <widget class="QPushButton" name="button">
         <property name="text">
          <string>Рассчитать</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>150</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Минимальное значение:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="minEdit">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>90</y>
      <width>91</width>
      <height>24</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>120</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Среднее значение:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="avgEdit">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>120</y>
      <width>91</width>
      <height>24</height>
     </rect>
    </property>
    <property name="text">
     <string>0,00</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="maxEdit">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>60</y>
      <width>91</width>
      <height>24</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>60</y>
      <width>150</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Максимальное значение:</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        tem = io.StringIO(graf)
        uic.loadUi(tem, self)
        self.button.clicked.connect(self.f)

    def f(self):
        file = self.filenameEdit.text()
        try:
            with open(file, mode='r', encoding='UTF-8') as inp:
                read = inp.readlines()
                for i in range(len(read)):
                    read[i] = read[i].replace('\n', '')
                read = list(filter(None, read))
                for i in range(len(read)):
                    read[i] = read[i].split()
                read1 = list()
                for e in read:
                    for el in e:
                        read1.append(el)
                read1 = list(map(int, read1))
                count = 0
                if len(read1) != 0:

                    maximum = max(read1)
                    minimum = min(read1)
                    for e in read1:
                        count += int(e)
                    sred = round(count / len(read1), 2)

            out = open('./out.txt', mode='w', encoding='UTF-8')
            if len(read1) == 0:
                out.close()
            else:
                out.write(f'{maximum}\n')
                out.write(f'{minimum}\n')
                out.write(f'{sred}')
                out.close()
            with open('out.txt', mode='r', encoding='UTF-8') as out:
                out = out.readlines()
                if len(read1) != 0:
                    self.maxEdit.setText(str(out[0]))
                    self.minEdit.setText(str(out[1]))
                    self.avgEdit.setText(str(out[2]))
                else:
                    raise ValueError
        except ValueError:
            if len(read1) == 0:
                self.maxEdit.setText(str(0))
                self.minEdit.setText(str(0))
                self.avgEdit.setText(str('0,00'))
                self.statusBar().showMessage(
                    'Указанный файл пуст')
            else:
                self.maxEdit.setText(str(0))
                self.minEdit.setText(str(0))
                self.avgEdit.setText(str('0,00'))
                self.statusBar().showMessage(
                    'Файл содержит некорректные данные')
        except FileNotFoundError:
            self.maxEdit.setText(str(0))
            self.minEdit.setText(str(0))
            self.avgEdit.setText(str(0.00))
            self.statusBar().showMessage(
                'Указанный файл не существует')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec_())
