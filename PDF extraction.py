# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import PyPDF2

PATH = "../input"
FILE = "/PracticePepperFile.pdf"
    

def open_PDF(PATH, filename):
    file = PATH + filename
    openedFile = open (file, 'rb')
    return openedFile
#%%

#opening the PDF file
practicePDF = openPDF(PATH,FILE)

#applying PyPDF2 reader tool to the open PDF 
Readpdf = PyPDF2.PdfFileReader (practicePDFD)

#return the number of pages in the PDF
print (Readpdf.numPages)

#extract all page text starting with page 0 
p = 0
while p <= Readpdf.numPages:
    nextpage = pdfReader.getPage(p)
    print (nextpage.extractText())
    p = p+1
   