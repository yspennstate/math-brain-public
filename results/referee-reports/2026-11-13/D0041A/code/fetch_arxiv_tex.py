import io, tarfile, sys, requests
from pathlib import Path
name, arxiv=sys.argv[1:3]
r=requests.get('https://arxiv.org/src/'+arxiv,timeout=90);r.raise_for_status()
try:
    archive=tarfile.open(fileobj=io.BytesIO(r.content),mode='r:*')
    blocks=[]
    for member in archive.getmembers():
        if member.isfile() and member.name.endswith(('.tex','.bbl')):
            blocks.append('\n===== '+member.name+' =====\n'+archive.extractfile(member).read().decode('utf-8',errors='replace'))
    txt='\n'.join(blocks)
except tarfile.ReadError:
    import gzip
    txt=gzip.decompress(r.content).decode('utf-8',errors='replace')
Path('sources/'+name+'_tex.txt').write_text(txt)
print(name,len(txt))
