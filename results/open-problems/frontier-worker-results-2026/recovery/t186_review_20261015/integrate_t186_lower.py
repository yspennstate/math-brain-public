"""Record only the reviewed lower-side strong-core result, preserving other work."""
from pathlib import Path
from datetime import datetime
import subprocess,json,hashlib
HERE=Path(__file__).resolve().parent
REPO=Path('~/brain-repo')
MESH=REPO/'12_cognitive_architecture/agent_mesh/agent_mesh.py'
PY='C:/Python314/python.exe'; AGENT='codex-term-362ebe34'
ROW=REPO/'06_math_research/frontier/rows/T186'
MEASURE=REPO/'06_math_research/frontier/measurements/T186_C013_v1_recovery_20261015.json'
REPORT=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
def mesh(*args):return subprocess.run([PY,str(MESH),*args,'--agent',AGENT],check=True,capture_output=True).stdout
def put(path,text):
    mesh('assert','--resource',str(path))
    path.write_bytes(text.encode('utf-8'))
receipt=json.loads((HERE/'T186_LOWER_RECEIPT.json').read_text(encoding='utf-8'))
assert receipt['status'].startswith('PASS') and len(receipt['covers'])==2
for item in receipt['reviews']:
    assert hashlib.sha256(Path(item['proof']).read_bytes()).hexdigest()==item['proof_sha256']
inbox=mesh('inbox','--pending')
(HERE/'T186_PREWRITE_INBOX.json').write_bytes(inbox)
assert json.loads(inbox)==[], 'Read incoming mesh mail before shared mutation'
mesh('claim','--resource',str(ROW/'DOSSIER.md'),'--resource',str(ROW/'moves.jsonl'),
     '--resource',str(MEASURE),'--resource',str(REPORT),
     '--mode','write','--ttl','1800','--purpose','Record fully reviewed T186 target3 lower-side finite-core emptiness')
at=datetime.now().astimezone().isoformat()
text=('T186 target 3 lower side recorded narrowed: for G(n,c/n), the maximal strong '
 '4-core is empty with high probability for each fixed c in [0,9.23414], and '
 'the strong 3-core is empty for each fixed c in [0,6.84256], endpoints included. '
 'Composition C005 v1 (c300345293448cb7), C007 v2 (8e8cbdb850b13175) and '
 'C013 v1 (9c127b0e5c3825d9), all exact-version reviewer and w683 PASS; '
 'w683 completed 1419 independent interval boxes at 512 bits. Lead checked '
 'the exact closed covers and all integer stopping inequalities and rederived '
 'the finite minimum-degree-set union bound. This is a lower bound on target3, '
 'not the exact finite onset, a positive-side transfer, or a claim to solve T186. '
 'The circumference result remains c>=13.962; literature priority is unverified.')
marker='<!-- T186-TARGET3-LOWER-RECOVERY -->'
mp=ROW/'moves.jsonl'; old=mp.read_bytes().decode('utf-8')
claim='T186-W674-C013 v1 (C005 v1/C007 v2)'
if not any(json.loads(l).get('claim')==claim for l in old.splitlines() if l.strip()):
    put(mp,old+json.dumps({'at':at,'by':AGENT,'kind':'narrowed','claim':claim,'text':text})+'\n')
dp=ROW/'DOSSIER.md'; old=dp.read_bytes().decode('utf-8')
if marker not in old:put(dp,old+'\n'+marker+'\n'+at+' '+text+'\n')
put(MEASURE,json.dumps(receipt,indent=2)+'\n')
html=REPORT.read_bytes().decode('utf-8')
if 'id="recovery-t186-lower"' not in html:
    assert '<tr id="recovery-t170">' in html
    row=('<tr id="recovery-t186-lower"><td>T186, strong-core lower bound: audit complete</td>'
      '<td>For each fixed nonnegative c &le; 9.23414 the strong 4-core is empty with high probability; '
      'for each fixed c &le; 6.84256 the strong 3-core is empty. Both endpoints are included.</td>'
      '<td class="ok">Recorded as narrowed after both exact-version reviews, the independent '
      '1,419-box replay and the lead&rsquo;s exact coverage and union-bound check. This is '
      'the lower side of target 3. The positive finite-graph transfer and exact onset remain open; '
      'the circumference theorem still starts at c = 13.962. Priority unverified.</td></tr>')
    put(REPORT,html.replace('<tr id="recovery-t170">',row+'\n<tr id="recovery-t170">',1))
put(HERE/'NEXT.md',(HERE/'NEXT.md').read_text(encoding='utf-8')+'\n'+at+': '+text+'\n')
print(json.dumps({'at':at,'claim':claim,'recorded':True,'scope':'lower side only','report_render_pending':True}))
