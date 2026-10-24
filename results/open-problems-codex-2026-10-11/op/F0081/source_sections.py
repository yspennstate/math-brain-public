import pathlib,pymupdf
s=pathlib.Path('source.txt').read_text(encoding='utf8')
for term in ['Theorem 6','Theorem 19','Theorem 5','8\n','s(d)','lower bound']:
 at=s.find(term);print('\nTERM',term,'\n',s[max(0,at-300):at+2600])
