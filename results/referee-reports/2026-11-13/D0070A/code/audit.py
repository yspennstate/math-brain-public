#!/usr/bin/env python3
"""Final artifact audit; uses data and independent closed-form checks."""
import hashlib,json,math,pathlib,re
from family import coefficients,decimal_root
ROOT=pathlib.Path(__file__).resolve().parents[1]
report=(ROOT/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
assert not list(ROOT.rglob('*.pdf'))
for p in ROOT.rglob('*'):
    if not p.is_file():continue
    assert p.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.tif','.tiff','.webp','.gif','.djvu'}
    with p.open('rb') as f:assert not f.read(8).startswith(b'%PDF')
for p in (ROOT/'sources').iterdir():
    assert p.suffix=='.txt'
    raw=p.read_bytes();assert not raw.startswith(b'%PDF')
    raw.decode('utf8')
for line in (ROOT/'data'/'sources.jsonl').read_text().splitlines():
    r=json.loads(line);raw=(ROOT/'sources'/r['text']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==r['text_sha256']
    assert raw.count(b'\x0c')==r['pages']
records=[json.loads(l) for l in (ROOT/'data'/'enumerations.jsonl').read_text().splitlines()]
assert len(records)==35
lookup={r['name']:r for r in records}
expected={'ladder_Z_x_K2':6656290,'honeycomb':2479692,'cylinder_Z_x_C3':2491666,'cylinder_Z_x_C4':6249358,'Z_D4_component':2118466,'Z_S4_component':10794564,'K3_free_K2':552,'K4_free_K2':18684}
for name,n in expected.items():
    assert lookup[name]['counts'][-1]==n
    assert f'{n:,}' in report
fib=[0,1]
for _ in range(35):fib.append(sum(fib[-2:]))
ladder=lookup['ladder_Z_x_K2']
assert ladder['bridge_counts'][1:]==fib[2:32]
# Extra closed-form numerical consistency check (not needed for the proof).
assert ladder['counts'][2:]==[8*fib[n]-(n if n%2==0 else 4) for n in range(2,31)]
assert lookup['prism_C31_x_K2_cover_check']['counts']==ladder['counts']
for m in (3,4,5):
    c=coefficients(m,400)
    assert abs(c[-1]/c[-2]-float(decimal_root(m)))<1e-12
for r in records:
    if r['kind']!='infinite':continue
    d=r['degree']
    for n,c in enumerate(r['counts'][1:],1):assert c<=d*(d-1)**(n-1)<2**64
    if r['degree']==3:
        assert all(c>=math.sqrt(2)**n*(1-1e-12) for n,c in enumerate(r['counts']))
checks=json.loads((ROOT/'data'/'checks.json').read_text())
assert checks['nice']>=10
assert checks['python_maxrss_bytes']+checks['enumerator_child_maxrss_bytes']<4_000_000_000
# Every explicitly versioned arXiv reference in the report must agree with a retained header.
headers='\n'.join(p.read_text()[:4500] for p in (ROOT/'sources').glob('*.txt'))
for ref in set(re.findall(r'\d{4}\.\d{4,5}v\d+',report)):
    assert 'arXiv:'+ref in headers,ref
summary={'status':'passed','source_texts':len(list((ROOT/'sources').glob('*.txt'))),'graph_cases':len(records),'finite_cases':sum(r['kind']=='finite' for r in records),'infinite_cases':sum(r['kind']=='infinite' for r in records),'cubic_infinite_cases':sum(r['kind']=='infinite' and r['degree']==3 for r in records),'independent_checks':['source hashes and version headers','report counts against raw data','Fibonacci ladder bridges','ladder closed form numerical consistency','finite voltage quotient counts','renewal coefficient ratios against decimal roots','nonbacktracking and square-root sanity bounds','resource records','plain-text-only sources']}
(ROOT/'data'/'audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
