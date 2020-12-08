from PyQt5 import QtCore, QtGui, QtWidgets

from selenium import webdriver
import time,box,threading,os,urllib.request
from PyQt5.QtWidgets import QMessageBox
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

class Ui_Form(object):
    def setupUi(self, Form):
        self.x = 0
        
        Form.setObjectName("Form")
        Form.resize(678, 554)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 20, 162, 42))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 20, 226, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 20, 122, 42))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 494, 112, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 494, 112, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")     
        


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "视频解析"))
        self.comboBox.setItemText(0, _translate("Form", "腾讯视频"))
        self.comboBox.setItemText(1, _translate("Form", "爱 奇 艺"))
        self.comboBox.setItemText(2, _translate("Form", "芒果 TV"))
        self.comboBox.setItemText(3, _translate("Form", "优酷视频"))
        self.comboBox.setItemText(4, _translate("Form", "BILIBILI"))
        self.comboBox.setItemText(5, _translate("Form", "搜狐视频"))
        self.pushButton.setText(_translate("Form", "搜  索"))
        self.pushButton_2.setText(_translate("Form", "播  放"))
        self.pushButton_3.setText(_translate("Form", "下  载"))
        
        self.pushButton.clicked.connect(self.th1)
        self.pushButton_3.clicked.connect(self.th3)
        #self.pushButton_2.clicked.connect()

    def search(self,):
        
        cmb = self.comboBox.currentText()
        name = self.lineEdit.text()
        path = os.getcwd()

        chrome_options = webdriver.ChromeOptions()     
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument("--user-data-dir="+r"C:\Users\surface\AppData\Local\Google\Chrome\User Data")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        '''
        web = webdriver.Edge(path+"\msedgedriver.exe")
        self.driver = web
        '''
        print(cmb)    
        if cmb == "腾讯视频":
            url = f'https://v.qq.com/x/search/?q={name}&stag=&smartbox_ab='

        if cmb == "爱 奇 艺":
            url = f'https://so.iqiyi.com/so/q_{name}?source=input&sr=8523391404870155&ssrt=20201204013614292&ssra=6e9d7a91547ea2c599c12ddc55333723'
        
        if cmb == "芒果 TV":
            url = f'https://so.mgtv.com/so?k={name}&lastp=ch_home'

        if cmb == "优酷视频":
            url = f'https://so.youku.com/search_video/q_{name}?searchfrom=5'

        if cmb == "BILIBILI":
            url = f'https://search.bilibili.com/all?keyword={name}&from_source=nav_search&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.9'

        if cmb == "搜狐视频":
            url = f'https://so.tv.sohu.com/mts?box=1&wd={name}'
        self.th2()
        self.driver.get(url)
        self.driver.set_page_load_timeout(2) 
        
        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/div/a').click()
            self.driver.get(url)
        except:
            pass
        

    
    def messbox(self):
        f = open(r"C:\Users\surface\Desktop\电影解析\解析网址.txt",'r',encoding="utf-8")
        f_list = f.read().split('\n')
        Dialog.exec()
        self.handles = self.driver.window_handles
        self.driver.switch_to_window(self.handles[-1])
        self.driver.set_page_load_timeout(2)       
        titles = self.driver.current_url
        print(titles)

        for i in [0]:
            self.handles = self.driver.window_handles
            self.driver.switch_to_window(self.handles[-1])
            self.driver.close()
            self.driver.switch_to_window(self.handles[0])

            new = f'window.open("{f_list[i]}"+"{titles}");'
            self.driver.execute_script(new)
            self.handles = self.driver.window_handles
            self.driver.switch_to_window(self.handles[-1])

    def down(self):#/html/body/div/div[2]/video
        for link in self.driver.find_elements_by_xpath('/html/body/div/div[2]/video'):
            Downloadpath = link.get_attribute('src')
            print(Downloadpath)
        urllib.request.urlretrieve(Downloadpath,'Video.mp4')
        
    def th1(self):  
        th1 = threading.Thread(target=self.search)
        th1.start()

    def th2(self):
        th2 = threading.Thread(target=self.messbox)
        th2.start()

    def th3(self):
        th3 = threading.Thread(target=self.down)
        th3.start()
if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()
    uidialog = box.Ui_Dialog()
    uidialog.setupUi(Dialog)
    Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    
    Form = QtWidgets.QWidget()  
    ui = Ui_Form()
    ui.setupUi(Form)
    
    Form.show()
    sys.exit(app.exec_())
