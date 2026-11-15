"""Fetch primary-source text/metadata; PDF payloads stay in memory only."""
import json, os, re, subprocess, time, urllib.request, urllib.parse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'sources'
HEAD={'User-Agent':'Probability-referee-local-audit/1.0'}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers=HEAD),timeout=40) as r:
        return r.read(),r.headers.get('Content-Type','')
def save_text(name,url):
    try:
        data,typ=get(url)
        if data.startswith(b'%PDF'):
            text=subprocess.run(['pdftotext','-layout','-','-'],input=data,capture_output=True,check=True).stdout.decode()
        else: text=data.decode('utf-8',errors='replace')
        (S/(name+'.txt')).write_text('Source: '+url+'\nRetrieved during referee audit: '+time.strftime('%Y-%m-%d %H:%M:%S %z')+'\n\n'+text)
        print(name, len(text),typ,flush=True)
    except Exception as e: print(name,'ERROR',str(e),flush=True)
if __name__=='__main__':
    for name,url in [
      ('ramirez_rider_virag','https://arxiv.org/pdf/math/0607331'),
      ('trotter','https://www.sciencedirect.com/science/article/pii/0001870884900379'),
      ('bufetov_kawamoto_2025','https://ousar.lib.okayama-u.ac.jp/files/public/6/68721/20250520183729415073/fulltext.pdf')]: save_text(name,url)
    titles=[]
    for line in (ROOT/'paper/main.tex').read_text().splitlines():
        if line.startswith('\\bibitem') and not any(k in line for k in ['MathBrain','BrainFramework']):
            key=re.search(r'\\bibitem\{(.*?)\}',line)[1]
            title=re.search(r'\\emph\{(.*?)\}',line)[1]
            doi=re.search(r'doi:([^,\s]+)',line)
            url=('https://api.crossref.org/works/'+urllib.parse.quote(doi[1],safe='') if doi else 'https://api.crossref.org/works?rows=2&query.bibliographic='+urllib.parse.quote(title))
            try:
                data,typ=get(url); obj=json.loads(data)
                (S/('metadata_'+key+'.json.txt')).write_text(json.dumps({'source_url':url,'crossref':obj},ensure_ascii=False,indent=2))
                msg=obj['message']; items=msg.get('items',[msg]); a=items[0]
                print(key,a.get('title'),a.get('author'),a.get('container-title'),a.get('volume'),a.get('issue'),a.get('page'),a.get('published'),a.get('DOI'),flush=True)
            except Exception as e: print(key,'ERROR',str(e),flush=True)
