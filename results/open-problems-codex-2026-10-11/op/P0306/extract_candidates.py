import fitz,pathlib
root=pathlib.Path(__file__).resolve().parent
for p in root.glob('lead_*.pdf'):
    with fitz.open(p) as d:
        txt='\n'.join('=== PDF PAGE '+str(i+1)+' ===\n'+x.get_text() for i,x in enumerate(d))
        p.with_suffix('.txt').write_text(txt,encoding='utf-8')
        print(p.name,len(d),'pages\n'+''.join(d[i].get_text() for i in range(min(3,len(d))))[:10000])
