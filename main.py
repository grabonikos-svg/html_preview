import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QListWidget, QFileDialog, QPushButton, QSplitter)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt


class HTMLPreviewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML File Previewer")
        self.resize(1400, 900)
        self.apply_dark_mode()

        # Κεντρικό Widget και Διάταξη (Layout)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Splitter για να μπορούμε να αυξομειώνουμε το πλάτος της λίστας και της προεπισκόπησης
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # ---------------- ΑΡΙΣΤΕΡΟ ΠΑΝΕΛ (Λίστα Αρχείων) ----------------
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)

        # Κουμπί για επιλογή φακέλου
        self.btn_open_folder = QPushButton("Επιλογή Φακέλου...")
        self.btn_open_folder.setCursor(Qt.PointingHandCursor)
        self.btn_open_folder.clicked.connect(self.open_folder)
        left_layout.addWidget(self.btn_open_folder)

        # Λίστα που θα εμφανίζει τα αρχεία .html
        self.file_list = QListWidget()
        self.file_list.itemClicked.connect(self.load_html)
        left_layout.addWidget(self.file_list)

        # ---------------- ΔΕΞΙ ΠΑΝΕΛ (Προεπισκόπηση HTML) ----------------
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)

        # Ενσωματωμένος Web Browser
        self.browser = QWebEngineView()
        right_layout.addWidget(self.browser)

        # Προσθήκη των πάνελ στο Splitter
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        # Ορίζουμε το αρχικό πλάτος (π.χ. 300px η λίστα, 1100px το browser view)
        splitter.setSizes([300, 1100])

        # Μεταβλητή για αποθήκευση της διαδρομής του τρέχοντος φακέλου
        self.current_folder = ""

    def apply_dark_mode(self):
        """Εφαρμογή Dark Mode σε όλο το UI χρησιμοποιώντας QSS (Qt StyleSheet)"""
        dark_stylesheet = """
        QMainWindow {
            background-color: #1e1e1e;
        }
        QWidget {
            background-color: #1e1e1e;
            color: #d4d4d4;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 14px;
        }
        QPushButton {
            background-color: #333333;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 10px;
            color: #ffffff;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #444444;
            border: 1px solid #777777;
        }
        QPushButton:pressed {
            background-color: #222222;
        }
        QListWidget {
            background-color: #252526;
            border: 1px solid #3c3c3c;
            border-radius: 5px;
            padding: 5px;
            outline: none;
        }
        QListWidget::item {
            padding: 8px;
            border-radius: 3px;
        }
        QListWidget::item:hover {
            background-color: #2a2d2e;
        }
        QListWidget::item:selected {
            background-color: #094771;
            color: #ffffff;
        }
        QSplitter::handle {
            background-color: #3c3c3c;
            width: 2px;
            margin: 0px 5px;
        }
        """
        self.setStyleSheet(dark_stylesheet)

    def open_folder(self):
        """Ανοίγει παράθυρο διαλόγου για επιλογή φακέλου και φορτώνει τα HTML αρχεία."""
        folder = QFileDialog.getExistingDirectory(self, "Επιλογή Φακέλου με HTML Αρχεία")

        if folder:
            self.current_folder = folder
            self.file_list.clear()

            # Διάβασμα των αρχείων του φακέλου και φιλτράρισμα για .html / .htm
            try:
                for file_name in os.listdir(folder):
                    if file_name.lower().endswith(('.html', '.htm')):
                        self.file_list.addItem(file_name)
            except Exception as e:
                print(f"Σφάλμα κατά την ανάγνωση του φακέλου: {e}")

    def load_html(self, item):
        """Φορτώνει το επιλεγμένο αρχείο HTML στον ενσωματωμένο browser."""
        file_name = item.text()
        file_path = os.path.join(self.current_folder, file_name)

        # Μετατροπή της τοπικής διαδρομής σε συμβατό QUrl
        local_url = QUrl.fromLocalFile(file_path)
        self.browser.setUrl(local_url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HTMLPreviewer()
    window.show()
    sys.exit(app.exec())