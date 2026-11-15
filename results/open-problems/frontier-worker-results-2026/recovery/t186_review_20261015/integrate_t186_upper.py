"""Reconcile both exact-version reviews and record sufficient finite upper ranges."""
from pathlib import Path
from datetime import datetime
import subprocess,hashlib,json
HERE=Path(__file__).resolve().parent
REPO=Path('~/brain-repo')
W=Path('~/brain_workers/w674')
A=Path('~/brain_workers/w683')
OTHER=Path('~/brain_workers/w679/T186/audits')
PY='C:/Python314/python.exe'; AGENT='codex-term-362ebe34'
MESH=REPO/'12_cognitive_architecture/agent_mesh/agent_mesh.py'
ROW=REPO/'06_math_research/frontier/rows/T186'
MEASURE=REPO/'06_math_research/frontier/measurements/T186_C014_C015_v1_recovery_20261015.json'
REPORT=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def mesh(*args):return subprocess.run([PY,str(MESH),*args,'--agent',AGENT],check=True,capture_output=True).stdout
def put(path,text):
    mesh('assert','--resource',str(path));path.write_bytes(text.encode('utf-8'))
proof=W/'T186/proofs/C014_C015_global_snapshot_forest.md'
digest='29593274c1dd79d14dfee5963e41bd24c26b2d51febaf77f5753bc8bb47e26d7'
assert sha(proof)==digest
first=(W/'AUDITS_FROM_REVIEWER.tsv').read_text(encoding='utf-8').splitlines()
second=(A/'AUDITS.tsv').read_text(encoding='utf-8').splitlines()
reviews=[]
for claim in ['T186-W674-C014','T186-W674-C015']:
    rows=[l for l in first if l.split('\t')[:3]==[claim,'1','PASS'] and digest in l]
    assert rows and 'w679' in rows[-1]
    a=OTHER/(claim+'_v1.md');b=A/'audits'/('w674_'+claim+'_v1.md')
    assert digest in a.read_text(encoding='utf-8') and digest in b.read_text(encoding='utf-8')
    verdicts=[l for l in second if l.split('\t')[1:5]==['w674',claim,'1','PASS']]
    assert verdicts
    reviews.append({'claim':claim,'w679_review':str(a),'w679_sha256':sha(a),
        'w679_row':rows[-1],'w683_review':str(b),'w683_sha256':sha(b),'w683_row':verdicts[-1]})
own=json.loads((HERE/'T186_UPPER_CONSTANTS_RECEIPT.json').read_text(encoding='utf-8'))
assert own['proof_sha256']==digest and own['status'].startswith('PASS')
assert own['script_sha256']==sha(HERE/'audit_t186_upper_constants.py')
at=datetime.now().astimezone().isoformat()
receipt={'at':at,'claim':'T186-W674-C014/C015 v1','proof_sha256':digest,
    'status':'PASS both exact-version independent reviews plus lead analytic and own Arb constant checks',
    'reviews':reviews,'lead_note_sha256':sha(HERE/'T186_UPPER_LEAD_ANALYTIC_REVIEW.md'),
    'lead_constant_receipt_sha256':sha(HERE/'T186_UPPER_CONSTANTS_RECEIPT.json'),
    'rows':own['rows'],'scope':'Sufficient finite positive-core bounds only; exact onset, finite WP transfer, complement tails and priority remain open. Circumference cutoff unchanged.'}
(HERE/'T186_UPPER_RECONCILIATION.json').write_bytes((json.dumps(receipt,indent=2)+'\n').encode('utf-8'))
inbox=mesh('inbox','--pending');(HERE/'T186_UPPER_PREWRITE_INBOX.json').write_bytes(inbox)
assert json.loads(inbox)==[],'Handle new mesh mail before recording'
mesh('claim','--resource',str(ROW/'DOSSIER.md'),'--resource',str(ROW/'moves.jsonl'),
     '--resource',str(MEASURE),'--resource',str(REPORT),'--mode','write','--ttl','1800',
     '--purpose','Record independently reviewed stopped-forest strong-core density bounds')
text=('T186 target3 upper side recorded narrowed: for n>=4000000 and every c in [11.415,n], '
 'Pr(|S4(G(n,c/n))|<=9n/10)<=5 exp(-n/1000000); for n>=3000000 and every c in [9.053,n], '
 'Pr(|S3|<=7n/8)<=4 exp(-n/1000000). C014/C015 v1 share exact proof SHA256 '+digest+'. '
 'Both w679 and w683 PASS on this hash; lead rederived the all-size stopped birth-forest/EGF '
 'argument and checked the rational-input inequalities at 200 bits without solver imports. '
 'Uniformity in c is proved analytically, without core edge-monotonicity. No tree-to-finite '
 'positive transfer is assumed. Together with C013 this gives certified empty and positive '
 'ranges, not an exact finite onset. The circumference cutoff stays13.962; priority unverified.')
claim=receipt['claim'];mp=ROW/'moves.jsonl';old=mp.read_bytes().decode('utf-8')
if not any(json.loads(l).get('claim')==claim for l in old.splitlines() if l.strip()):
    put(mp,old+json.dumps({'at':at,'by':AGENT,'kind':'narrowed','claim':claim,'text':text})+'\n')
marker='<!-- T186-TARGET3-UPPER-RECOVERY -->';dp=ROW/'DOSSIER.md';old=dp.read_bytes().decode('utf-8')
if marker not in old:put(dp,old+'\n'+marker+'\n'+at+' '+text+'\n')
put(MEASURE,json.dumps(receipt,indent=2)+'\n')
html=REPORT.read_bytes().decode('utf-8')
if 'id="recovery-t186-upper"' not in html:
    assert '<tr id="recovery-t186-lower">' in html,'Record verified lower side first'
    row=('<tr id="recovery-t186-upper"><td>T186, strong-core upper bound: audit complete</td>'
      '<td>For each fixed c &ge; 11.415 the strong 4-core exceeds 90% of the vertices with high probability. '
      'For c &ge; 9.053 the strong 3-core exceeds 87.5%.</td>'
      '<td class="ok">Both exact-version reviews passed; the lead independently checked the '
      'stopped-forest argument and interval constants. These sufficient positive ranges and the '
      'empty ranges below leave the exact onset open. The circumference cutoff remains 13.962; '
      'priority unverified.</td></tr>')
    put(REPORT,html.replace('<tr id="recovery-t186-lower">',row+'\n<tr id="recovery-t186-lower">',1))
put(HERE/'NEXT.md',(HERE/'NEXT.md').read_text(encoding='utf-8')+'\n'+at+': '+text+'\n')
print(json.dumps({'at':at,'claim':claim,'recorded':True,'report_render_pending':True}))
