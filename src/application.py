import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from page import Page
import ZODB.FileStorage
import ZODB

if __name__ == "__main__":
    storage = ZODB.FileStorage.FileStorage("testdata.fs")
    db = ZODB.DB(storage)
    conn = db.open()
    root = conn.root()
    if "user" not in root:
        root["user"] = {}

    app = QApplication(sys.argv)
    page = Page(root, conn)
    page.show()
    sys.exit(app.exec())
