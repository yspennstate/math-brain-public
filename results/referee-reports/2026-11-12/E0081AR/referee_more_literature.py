"""Additional full-text retrievals; all outputs remain local."""
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from pathlib import Path
import json,re,subprocess
out=Path('referee_results/literature')
requests=[
 ('li1980.pdf','https://statistics.uconn.edu/wp-content/uploads/sites/729/2019/03/A-Martingale-Approach-to-the-Study-of-Occurrence-of-Sequence-Patterns-in-Repeated-Experiments.pdf'),
 ('odlyzko_index.html','https://www-users.cse.umn.edu/~odlyzko/doc/arch/'),
 ('gerber_li.html','https://www.sciencedirect.com/science/article/pii/0304414981900259'),
 ('ostaszewska_zajkowski.pdf','https://arxiv.org/pdf/1302.4859'),
 ('chapter.pdf','https://www.columbia.edu/~wt2319/Patterns.pdf'),
 ('thesis.pdf','https://escholarship.org/content/qt51j6244c/qt51j6244c.pdf'),
 ('arxiv_doi_record.json','https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1411.0041')]
records=[]
for name,url in requests:
    try:
        r=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20)
        data=r.read();out.joinpath(name).write_bytes(data)
        records.append(dict(file=name,url=url,status=r.status,bytes=len(data),content_type=r.headers.get('Content-Type')))
        print(name,r.status,len(data),flush=True)
        if name.endswith('.pdf') and data.startswith(b'%PDF'):
            subprocess.run(['/opt/homebrew/bin/pdftotext','-layout',str(out/name),str(out/name.replace('.pdf','.txt'))],check=True)
        if name=='odlyzko_index.html':
            links=re.findall(r'href=["\']([^"\']+)["\']',data.decode(errors='replace'))
            print('Possible overlap papers:',[x for x in links if any(w in x.lower() for w in ('overlap','string','game','pattern'))],flush=True)
    except Exception as e:
        records.append(dict(file=name,url=url,error=str(e)));print(name,str(e),flush=True)
out.joinpath('more_fetch_log.json').write_text(json.dumps(records,indent=2)+'\n')
