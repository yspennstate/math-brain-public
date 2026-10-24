import pymupdf
D=pymupdf.open('resolution_pdf.pdf')
for i in [5,6]:print('PDF PAGE',i+1,D[i].get_text())
