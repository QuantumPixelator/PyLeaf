# This is a Python program that uses PySide6 to create a GUI app that displays information about cannabis strains.

# This script comes to you without any warranty whatsoever. I've tried to ensure it is bug-free, but I can't guarantee it. Use at your own risk. If you find any bugs, please let me know or open a pull request on GitHub.

# The data used in this app was obtained from Kaggle:
# https://www.kaggle.com/datasets/kingburrito666/cannabis-strains/

# License: MIT License (do whatever you want with it)

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QFrame, QListWidget, QTextEdit, QSizePolicy, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QDesktopServices, QIcon, QFont
import sqlite3
import sys

# SQLite database, complete with full path
db_path = 'pyleafdata.db'

# Function to populate details
def display_details(current_item):
    if current_item:
        selected_strain = current_item.text()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT * FROM cannabis WHERE Strain = ?"
        cursor.execute(query, (selected_strain,))
        result = cursor.fetchone()
        
        if result:
            strain_text.setText(result[0])
            type_text.setText(result[1])
            rating_text.setText(str(result[2]))
            effects_list.clear()
            effects_list.addItems(result[3].split(","))
            flavor_list.clear()
            flavor_list.addItems(result[4].split(","))
            description_text.setText(result[5])
        
        conn.close()

# App Setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyLeaf")
window.setWindowIcon(QIcon("resources/leaf.png"))

main_layout = QVBoxLayout()
header_label = QLabel(" \nPyLeaf: Cannabis Strain Information\n ")
font = QFont()
font.setBold(True)
header_label.setFont(font)
header_label.setAlignment(Qt.AlignCenter)
main_layout.addWidget(header_label)

search_layout = QHBoxLayout()
combo_box = QComboBox()
combo_box.addItems(["Strain", "Type", "Rating", "Effects", "Flavor", "Description"])
search_layout.addWidget(combo_box)

search_text = QLineEdit()
search_layout.addWidget(search_text)

search_button = QPushButton("Search")
search_layout.addWidget(search_button)

clear_button = QPushButton("Clear")
search_layout.addWidget(clear_button)

main_layout.addLayout(search_layout)

divider = QFrame()
divider.setFrameShape(QFrame.HLine)
divider.setFrameShadow(QFrame.Sunken)
main_layout.addWidget(divider)

results_details_layout = QHBoxLayout()

results_list = QListWidget()
results_details_layout.addWidget(results_list)

details_layout = QVBoxLayout()

details_top_layout = QHBoxLayout()

strain_text = QLineEdit()
strain_text.setReadOnly(True)
strain_text.setMinimumWidth(200)
strain_label = QLabel("Strain:")
details_top_layout.addWidget(strain_label)
details_top_layout.addWidget(strain_text)

type_text = QLineEdit()
type_text.setReadOnly(True)
type_text.setMaximumWidth(150)
type_label = QLabel("Type:")
details_top_layout.addWidget(type_label)
details_top_layout.addWidget(type_text)

rating_text = QLineEdit()
rating_text.setReadOnly(True)
rating_text.setMaximumWidth(50)
rating_text.setAlignment(Qt.AlignCenter)
rating_label = QLabel("Rating:")
details_top_layout.addWidget(rating_label)
details_top_layout.addWidget(rating_text)

details_layout.addLayout(details_top_layout)

divider2 = QFrame()
divider2.setFrameShape(QFrame.HLine)
divider2.setFrameShadow(QFrame.Sunken)
details_layout.addWidget(divider2)

effects_list = QListWidget()
effects_list.setFixedHeight(100)
effects_list.setFixedWidth(150)
effects_list.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
effects_label = QLabel("Effects:")
effects_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

flavor_list = QListWidget()
flavor_list.setFixedHeight(100)
flavor_list.setFixedWidth(150)
flavor_list.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
flavor_label = QLabel("Flavor:")
flavor_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

about_button = QPushButton("About")
about_button.setFixedWidth(150)

# Function to display app info
def show_about_info():
    msg = QMessageBox()
    msg.setWindowTitle("About PyLeaf")
    msg.setText('PyLeaf: Cannabis Strain Information<br><br>Developed by Quantum Pixelator<br><br>The data used is from:<br>'
                '<a href="https://www.kaggle.com/datasets/kingburrito666/cannabis-strains/">Cannabis Strains from Kaggle</a><br><br>License: MIT License<br><br>Source code available on <a href="https://github.com/QuantumPixelator/PyLeaf">GitHub</a>')
    # Enable link interaction.
    msg.setTextInteractionFlags(Qt.TextBrowserInteraction)

    # Open the link in an external browser when the user clicks the OK button.
    msg.buttonClicked.connect(lambda button: QDesktopServices.openUrl("https://www.kaggle.com/datasets/kingburrito666/cannabis-strains/") if button == QMessageBox.Ok else None)

    msg.exec()


about_button.clicked.connect(show_about_info)

effects_flavor_layout = QVBoxLayout()
effects_flavor_layout.addWidget(effects_label)
effects_flavor_layout.addWidget(effects_list)
effects_flavor_layout.addWidget(flavor_label)
effects_flavor_layout.addWidget(flavor_list)
effects_flavor_layout.addStretch(1)
effects_flavor_layout.addWidget(about_button)

description_text = QTextEdit()
description_text.setReadOnly(True)
description_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
description_label = QLabel("Description:")

description_layout = QVBoxLayout()
description_layout.addWidget(description_label)
description_layout.addWidget(description_text)

effects_flavor_description_layout = QHBoxLayout()
effects_flavor_description_layout.addLayout(effects_flavor_layout)
effects_flavor_description_layout.addLayout(description_layout)

details_layout.addLayout(effects_flavor_description_layout)
results_details_layout.addLayout(details_layout)

main_layout.addLayout(results_details_layout)

window.setLayout(main_layout)

stylesheet = """
    QWidget {
        font-family: Arial;
        font-size: 14px;
    }
    QLabel {
        color: green;
    }
    QPushButton {
        background-color: lightgreen;
        border: 2px solid green;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: green;
        color: white;
    }
    QLineEdit, QTextEdit, QListWidget, QComboBox {
        background-color: lightyellow;
        border: 2px solid green;
        border-radius: 5px;
    }
"""

def perform_search():
    search_column = combo_box.currentText()
    search_value = search_text.text()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM cannabis WHERE {search_column} LIKE ?"
    cursor.execute(query, (f"%{search_value}%",))
    results = cursor.fetchall()
    results_list.clear()
    for result in results:
        results_list.addItem(result[0])
    conn.close()

def clear_results():
    results_list.clear()
    strain_text.clear()
    type_text.clear()
    rating_text.clear()
    effects_list.clear()
    flavor_list.clear()
    description_text.clear()

search_button.clicked.connect(perform_search)
clear_button.clicked.connect(clear_results)
results_list.currentItemChanged.connect(lambda current_item: display_details(current_item))

app.setStyleSheet(stylesheet)
window.resize(700, 600)
window.show()
app.exec()
