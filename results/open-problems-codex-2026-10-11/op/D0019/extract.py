import pymupdf,pathlib
D=pymupdf.open('source.pdf'); pathlib.Path('source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(D)),encoding='utf8')
for i in [0,1,32,33,34]:
 if i<len(D): print('PAGE',i+1,D[i].get_text())
