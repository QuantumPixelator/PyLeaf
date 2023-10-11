# This code is provided to you for free, with no warranty, and no guarantee of support.

# This is a simple GUI application that allows you to search a SQLite database of cannabis strains.

# License: MIT License (https://opensource.org/licenses/MIT)
# (do whatever you want with it)

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QFrame, QListWidget, QTextEdit, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import sqlite3
import sys

# SQLite Setup
# Using SQLite3 for the database, in our app path
db_path = 'pyleafdata.db'  # The database, in the same folder as this script

# App Setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyLeaf")
window.setWindowIcon(QIcon("leaf.png"))
window.setFixedHeight(600)

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

# About Button
about_button = QPushButton("About")
details_layout.addWidget(about_button)

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

# Function to perform database query and update results_list
def perform_search():
    search_column = combo_box.currentText()
    search_value = search_text.text()
    
    # Connect to our database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query database
    query = f"SELECT * FROM cannabis WHERE {search_column} LIKE ?"
    cursor.execute(query, (f"%{search_value}%",))
    results = cursor.fetchall()
    
    # Clear existing items from the results list
    results_list.clear()
    
    # Populate results list with new items (Strain names)
    for result in results:
        results_list.addItem(result[0])  # Strain is the first column, index 0
    
    # Close database connection
    conn.close()

# Function to clear search results and detail fields
def clear_results():
    results_list.clear()
    strain_text.clear()
    type_text.clear()
    rating_text.clear()
    effects_list.clear()
    flavor_list.clear()
    description_text.clear()

# Connect search button and clear button to their respective functions
search_button.clicked.connect(perform_search)
clear_button.clicked.connect(clear_results)

# Function to populate details when a list item is selected
def populate_details():
    selected_strain = results_list.currentItem().text()
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query database for details
    query = "SELECT * FROM cannabis WHERE Strain = ?"
    cursor.execute(query, (selected_strain,))
    result = cursor.fetchone()
    
    # Populate detail fields
    strain_text.setText(result[0])
    type_text.setText(result[1])
    rating_text.setText(str(result[2]))
    
    # Clear existing items from effects and flavor lists
    effects_list.clear()
    flavor_list.clear()
    
    # Populate effects and flavor lists
    for effect in result[3].split(','):
        effects_list.addItem(effect.strip())
    for flavor in result[4].split(','):
        flavor_list.addItem(flavor.strip())
    
    # Populate description
    description_text.setPlainText(result[5])
    
    # Close database connection
    conn.close()

# Connect the item selection signal to the populate_details function
results_list.itemSelectionChanged.connect(populate_details)


# Function to open the About window
def open_about_window():
    about_window = QWidget()
    about_window.setWindowTitle("About PyLeaf")
    about_window.setFixedSize(400, 300)

    about_layout = QVBoxLayout()
    
    about_label = QLabel("PyLeaf: Cannabis Strain Information\n\nVersion: 1.0\n\nDatabase: pyleafdata.db")
    about_label.setAlignment(Qt.AlignCenter)
    
    about_layout.addWidget(about_label)
    about_window.setLayout(about_layout)
    
    about_window.show()

# Connect the About button to open_about_window
about_button.clicked.connect(open_about_window)

app.setStyleSheet(stylesheet)
window.show()
app.exec()
