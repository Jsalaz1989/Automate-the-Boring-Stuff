# This script runs on Windows only, and you must have Word installed.

import win32com.client      # install with "pip install pywin32==224"
import docx

wordFilename = 'C:\\Users\\Jaime\\Documents\\Automate the Boring Stuff, 2nd Ed\\15 Word and PDF\\demo.docx'
pdfFilename = 'C:\\Users\\Jaime\\Documents\\Automate the Boring Stuff, 2nd Ed\\15 Word and PDF\\demo.pdf'

wdFormatPDF = 17            # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)

docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()

wordObj.Quit()