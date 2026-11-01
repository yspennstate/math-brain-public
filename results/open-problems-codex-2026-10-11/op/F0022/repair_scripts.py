from pathlib import Path
q=chr(39)*3
d=chr(34)*3
for name in ['write_literature.py','finalize.py']:
 p=Path(name);s=p.read_text(encoding='utf-8-sig')
 s=s.replace('s='+q,'s='+d).replace('s+='+q,'s+='+d).replace('write_text('+q,'write_text('+d).replace('\n'+q,'\n'+d)
 s=s.replace('**Julien Dubédat**','**Clément Hongler and Stanislav Smirnov**')
 p.write_text(s,encoding='utf-8')
