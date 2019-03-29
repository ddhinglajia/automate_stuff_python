#! /usr/bin/python3 
# combines or merges pdf files in the current working directory
# sorts files with name and excludes cover pages

import PyPDF2, os

# get all the pdf filenames

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

sorted(pdfFiles)

pdfWriter = PyPDF2.PdfFileWriter()

# loop for merging all pdfs and removing the cover page

for filename in pdfFiles:
    pdfFileOBj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileOBj)
    for pageNum in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()