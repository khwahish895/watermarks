#pip install pikepdf

from pikepdf import  Pdf,Page,Rectangle

old_pdf1 = Pdf.open("np.pdf.pdf")
old_pdf2 = Pdf.open("java.pdf.pdf")
des_page = Page(old_pdf1.pages[0])
sur_page = Page(old_pdf2.pages[0])

des_page .add_overlay(sur_page,Rectangle(0,0,500,500))
old_pdf1.save("new_pdf.pdf")