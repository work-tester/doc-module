import os
from docx import Document
document = Document("Title.docx")

for table in document.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)