from PyPDF2 import PdfFileReader, PdfFileWriter
def printMeta():
	pdfFile = PdfFileReader(file('','rb'))
	docInfo = pdfFile.getDocumentInfo()
	for metaItem in docInfo:
		print '[+] ' + metaItem + ':' +docInfo[metaItem]

