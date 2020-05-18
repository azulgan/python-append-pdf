from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter, PageRange
from reportlab.pdfgen import canvas

def mergefiles(filename1, filename2, output):
    merger = PdfFileMerger()
    merger.append(PdfFileReader(filename1))
    merger.append(fileobj=PdfFileReader(filename2))
    merger.write(output)

def createPageWithImage(image, name):
    c = canvas.Canvas(name)
    # Draw the image at x, y. I positioned the x,y to be where i like here
    c.drawImage(image, 100, 720, 80, 50)
    # Add some custom text for good measure
    c.drawString(15, 720, "Signature")
    c.save()


if __name__ == "__main__":
    filename1 = "orig.pdf"
    filename2 = "tocreateimage.pdf"
    imageName = 'signature.gif'
    createPageWithImage(imageName, filename2)
    mergefiles(filename1, filename2, "document-output.pdf")
