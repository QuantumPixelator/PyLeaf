from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QFrame, QListWidget, QTextEdit, QSizePolicy
from PySide6.QtCore import Qt
import sqlite3
import sys

# SQLite Setup
# Using SQLite3 for the database, in our app path
db_path = 'pyleafdata.db'  # Path to the database

# App Setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyLeaf")

main_layout = QVBoxLayout()

# Header Label
header_label = QLabel("PyLeaf: Cannabis Strain Information")
header_label.setAlignment(Qt.AlignCenter)
main_layout.addWidget(header_label)

# Search Controls
search_layout = QHBoxLayout()
combo_box = QComboBox()
combo_box.addItems(["Strain", "Type", "Rating", "Effects", "Flavor", "Descriptions"])
search_layout.addWidget(combo_box)

search_text = QLineEdit()
search_layout.addWidget(search_text)

search_button = QPushButton("Search")
search_layout.addWidget(search_button)

clear_button = QPushButton("Clear")
search_layout.addWidget(clear_button)

main_layout.addLayout(search_layout)

# Divider
divider = QFrame()
divider.setFrameShape(QFrame.HLine)
divider.setFrameShadow(QFrame.Sunken)
main_layout.addWidget(divider)

# Results and Details
results_details_layout = QHBoxLayout()

# Results List
results_list = QListWidget()
results_details_layout.addWidget(results_list)

# Details
details_layout = QVBoxLayout()

# Strain, Type, Rating
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

# Divider
divider2 = QFrame()
divider2.setFrameShape(QFrame.HLine)
divider2.setFrameShadow(QFrame.Sunken)
details_layout.addWidget(divider2)

# Effects and Flavor List
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

effects_flavor_layout = QVBoxLayout()
effects_flavor_layout.addWidget(effects_label)
effects_flavor_layout.addWidget(effects_list)
effects_flavor_layout.addWidget(flavor_label)
effects_flavor_layout.addWidget(flavor_list)
effects_flavor_layout.addStretch(1)  # Anchor widgets to the top

# Description Text Box
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

# Apply Styles and Layouts
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
app.setStyleSheet(stylesheet)

window.show()
app.exec()
