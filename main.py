# -*- coding: utf-8 -*-
# @Time   : 2024/10/13 16:22
# @Author : WWEE
# @File   : main.py
# main.py
# import sys
# from PyQt5.QtWidgets import QApplication
# from views.ex import MainWindow
import multiprocessing
import os
import time
import json
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from controller.weather import weather
from controller.winController.cabWin import cabWin
from ultralytics import YOLO
from Views.t import Ui_Form
from controller.winController.videoWin import videoWin
from controller.winController.takePhotoWin import takePhotoWin
from controller.winController.photoWin import photoWin
from controller.winController.roadWin import roadWin
from controller.winController.userWin import userWin
from controller.winController.mainWin import mainWin

from controller.App import main
import PyQt5
import pyqt5_plugins

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()










