import pathlib,pymupdf
for k in ['broman','liggett_steif']:
 p=pathlib.Path('second_'+k+'_pdf.pdf')
 if p.exists():
  d=pymupdf.open(p);s='\n'.join('PDF PAGE '+str(i+1)+'\n'+x.get_text() for i,x in enumerate(d));pathlib.Path('second_'+k+'.txt').write_text(s,encoding='utf8');print(k,s[:1200]);print('\n'.join(str(i+1)+': '+l for i,l in enumerate(s.splitlines()) if ('movab' in l.lower() or 'downward fkg' in l.lower() or 'Theorem 1.' in l) )[:12000])
