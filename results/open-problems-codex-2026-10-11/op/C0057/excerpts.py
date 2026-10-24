import pymupdf
D=pymupdf.open('source.pdf')
for i in [27,28,45,46,47,53,54]:print('PDF PAGE',i+1);print(D[i].get_text())
