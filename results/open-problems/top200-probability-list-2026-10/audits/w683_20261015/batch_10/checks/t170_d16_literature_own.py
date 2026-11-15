from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from hashlib import sha256
from datetime import datetime
import xml.etree.ElementTree as ET
import json,re
root=Path(__file__).resolve().parent.parent;at=datetime.now().astimezone().isoformat();records=[]
base=next((r for line in (root/'SOURCES.jsonl').read_text(encoding='utf8').splitlines() if (r:=json.loads(line)).get('url','').startswith(('https://arxiv.org/abs/1705.08143','https://arxiv.org/pdf/1705.08143'))),None)
def fetch(url,name,why):
    p=root/'papers'/name;r={'at':at,'url':url,'file':str(p.relative_to(root)),'title':why,'authors':['arXiv or OpenAlex metadata'],'year':2026,'what you used it for':'D16 prior-work discovery; bounded metadata is not priority proof'}
    try:
        if p.exists():raw=p.read_bytes()
        else:
            with urlopen(Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=25) as response:raw=response.read(2000001)
            assert len(raw)<=2000000;p.write_bytes(raw)
        r.update(status='fetched',sha256=sha256(raw).hexdigest())
        value=ET.fromstring(raw) if name.endswith('.xml') else json.loads(raw)
    except Exception as e:r.update(status='unavailable',error=type(e).__name__+': '+str(e)[:160]);value=None
    records.append(r)
    with (root/'SOURCES.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(r)+'\n')
    return value
if base is None:
    ns={'a':'http://www.w3.org/2005/Atom'}
    meta=fetch('https://export.arxiv.org/api/query?id_list=1705.08143v2','t170_bp_primary_metadata_own.xml','Official metadata of cited BP source')
    assert meta is not None,'Primary metadata unavailable; do not invent missing source ledger entry'
    entry=meta.find('a:entry',ns);assert entry is not None
    base={'url':'https://arxiv.org/abs/1705.08143v2','file':'papers/t170_bp_primary_metadata_own.xml','sha256':sha256((root/'papers/t170_bp_primary_metadata_own.xml').read_bytes()).hexdigest(),'title':entry.findtext('a:title',namespaces=ns).strip(),'authors':[a.findtext('a:name',namespaces=ns) for a in entry.findall('a:author',ns)],'year':int(entry.findtext('a:published',namespaces=ns)[:4]),'what you used it for':'Repair missing primary-source metadata entry for earlier T170 citation'}
    with (root/'SOURCES.jsonl').open('a',encoding='utf8') as out:out.write(json.dumps(base)+'\n')
    print('Official closest-source metadata '+json.dumps(base))
    with (root/'NEXT.md').open('a',encoding='utf8') as out:out.write('\n'+at+' D16 literature helper failed StopIteration because old SOURCES ledger lacked cited1705.08143 entry. Replaced assumption with explicit official arXiv metadata retrieval; no mathematical evaluator failed or was rerun. Do not retry the old unguarded next() form.\n')
query='all:"first passage percolation" AND (all:anisotropy OR all:"limit shape" OR all:Eden) AND submittedDate:[202607170000 TO 202610152359]'
xml=fetch('https://export.arxiv.org/api/query?'+urlencode({'search_query':query,'max_results':12,'sortBy':'submittedDate','sortOrder':'descending'}),'t170_d16_recent_own.xml','Recent90day FPP anisotropy/shape metadata')
entries=[]
if xml is not None:
    ns={'a':'http://www.w3.org/2005/Atom'}
    entries=[{'title':e.findtext('a:title',default='',namespaces=ns).strip(),'id':e.findtext('a:id',default='',namespaces=ns),'published':e.findtext('a:published',default='',namespaces=ns)} for e in xml.findall('a:entry',ns)]
lookup=fetch('https://api.openalex.org/works?'+urlencode({'search':base['title'],'per-page':5}),'t170_d16_closest_lookup_own.json','Closest BP primary paper citation lookup')
def key(s):return re.sub('[^a-z0-9]','',s.lower())
closest=[] if lookup is None else [r for r in lookup.get('results',[]) if key(r.get('title',''))==key(base['title'])]
citations=None
if len(closest)==1:
    identifier=closest[0]['id'].rsplit('/',1)[-1]
    citations=fetch('https://api.openalex.org/works?'+urlencode({'filter':f'cites:{identifier},from_publication_date:2026-07-17','per-page':20,'sort':'publication_date:desc'}),'t170_d16_citing_own.json','Recent papers citing closest BP source, cap20')
    allcites=fetch('https://api.openalex.org/works?'+urlencode({'filter':f'cites:{identifier}','per-page':50,'sort':'publication_date:desc'}),'t170_d16_alltime_citing_own.json','All-time closest-source citing screen, cap50')
else:allcites=None
allquery='all:"first passage percolation" AND (all:anisotropy OR all:"Eden conjecture" OR all:Dhar)'
allxml=fetch('https://export.arxiv.org/api/query?'+urlencode({'search_query':allquery,'max_results':20,'sortBy':'relevance'}),'t170_d16_alltime_arxiv_own.xml','All-time FPP Eden anisotropy metadata, cap20')
allentries=[]
if allxml is not None:
    ns={'a':'http://www.w3.org/2005/Atom'}
    allentries=[{'title':e.findtext('a:title',default='',namespaces=ns).strip(),'id':e.findtext('a:id',default='',namespaces=ns),'published':e.findtext('a:published',default='',namespaces=ns)} for e in allxml.findall('a:entry',ns)]
summary={'at':at,'priority':'unclear; no global priority assertion','base_primary_source':base,'query':query,'recent_cap':12,'recent_entries':entries,'closest_matches':len(closest),'citing_status':'lookup ambiguous/unavailable' if len(closest)!=1 else 'fetched' if citations is not None else 'unavailable','citing_cap':20,'citing_entries':[] if citations is None else [{'title':r.get('title'),'id':r.get('id'),'doi':r.get('doi'),'published':r.get('publication_date')} for r in citations.get('results',[])],'records':records}
summary.update(alltime_query=allquery,alltime_arxiv_cap=20,alltime_arxiv_entries=allentries,alltime_primary_positive_control=any('1705.08143' in e['id'] for e in allentries),alltime_citing_cap=50,alltime_citing_total=None if allcites is None else allcites.get('meta',{}).get('count'),alltime_citing_entries=[] if allcites is None else [{'title':r.get('title'),'id':r.get('id'),'doi':r.get('doi'),'published':r.get('publication_date')} for r in allcites.get('results',[])])
(root/'checks/t170_d16_literature_own.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:summary[k] for k in ['recent_entries','alltime_arxiv_entries','alltime_primary_positive_control','alltime_citing_total','alltime_citing_entries']}))
