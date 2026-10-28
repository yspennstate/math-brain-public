"""Persist the proved empty-component repair alongside the frozen counterexample."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];AG=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s,h):return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
v=read(R/'out/VACUUM.json');assert v['query_rows']==768
claims=read(R/'CLAIMS.json');assert len(claims)==1
s='For every Boolean f on any uniform cube, with entropy in bits, let phi(t)=-t²log2(t²), phi(0)=0, and V(f)=phi(Ef)+3I(f). Then V is superharmonic under EVERY physical coordinate query and 0<=V(f)<=9I(f)/2. It majorizes the EMPTY Fourier entropy term phi(Ef); it is not asserted to majorize the whole Fourier entropy or FEI deficit. On the stage20 seven-bit witness, the entire positive outer-correction drift is explained by the empty term: subtracting its drift leaves -1269/512-(567/512)log2(3)+(3087/2048)log2(7)<0, exactly certified by7^3087<2^5076*3^2268. This component payment does not establish coherence or influence-priced initialization for the remaining nonempty spectrum.'
h=['uniform physical input cube; f is sign valued; base2 entropy','full physical-query children retained; influences use the original physical coordinates','the component potential may use only an actually unused original influence owner when inserted into a previously paid account']
c={'claim_id':'A071-VACUUM-COMPONENT-ENVELOPE','version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':digest(s,h),'contributors':['A071'],'proof_source':['VACUUM_PROOF.md','code/vacuum.py','out/VACUUM.json'],'proof_dependencies':['global Lipschitz bound2/ln2 for phi on[-1,1], ln2>2/3, direct mean coupling and influence telescoping proved in VACUUM_PROOF.md','Parseval Var<=I and elementary-u ln u<=1-u','integer inequality7^3087<2^5076*3^2268 for the fixed witness split'],'review_records':[{'reviewer':'A071','independent_reviewer':False,'verdict':'AUTHOR_ANALYTIC_ALL_DIMENSION_COMPONENT_PROOF_AND_EXACT_SANITY_CHECK','scope':'all-dimensional claim follows from calculus/mean coupling, not extrapolation; finite validation256 tables/768 query rows; external review pending'}],'status':'AUTHOR_PROVED_UNIVERSAL_COMPONENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'Pay and make coherent the remaining NONEMPTY signed composition correction with the same original influence account; V alone does not cover the whole FEI deficit.','next_consumers':['A072','A074','A075','A089','A092','B15','B20']}
claims.append(c);save(R/'CLAIMS.json',claims)
p=read(R/'PROGRESS.json');p['claims_created_or_changed'].append(c['claim_id']+'@1');p['mathematical_delta']+=' The complete empty-term source is isolated; universal V=phi(Ef)+3I is superharmonic with V<=9I/2. Nonempty drift is negative on the witness.'
p['mathematical_status']='EXACT_CANDIDATE_REFUTATION_AND_PROVED_UNIVERSAL_VACUUM_COMPONENT; FULL_FEI_OPEN'
p['source_artifacts']+=['VACUUM_SPEC.json','VACUUM_PROOF.md','out/VACUUM.json','code/vacuum.py']
p['next_action']='A074/A089/A092 review BOTH scoped proofs. With the complete empty Fourier term paid using V=phi(Ef)+3I from SAME actually unused influence stock, test coherence and initial price of the remaining NONEMPTY signed outer correction plus pivotal inner hulls near a nonempty coefficient cancellation; preserve old labels, both full children and spent donor.'
save(R/'PROGRESS.json',p);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
# heeded:heredoc_verbatim_surgery Byte replacements assert one exact match and preserve line endings; all writes stay inside this A071 run.
raw=(R/'REPORT.md').read_bytes();nl=b'\r\n' if b'\r\n' in raw else b'\n'
heading=b'## executed validation with domain, arithmetic, commands and outputs';assert raw.count(heading)==1
para='A further component repair is proved in VACUUM_PROOF: for EVERY Boolean f in every dimension, V(f)=-[Ef]^2 log2([Ef]^2)+3I(f) is full-query superharmonic and V<=9I/2. A global Lipschitz bound and physical mean coupling prove this analytically. On the witness, subtracting the empty-term drift leaves strictly NEGATIVE nonempty drift, certified by7^3087<2^5076*3^2268. The complete empty entropy remains paid; it is not dropped from terminal bills. Exact validation on256 three-bit tables and768 queries passes '+str(v['checks'])+' predicates in'+str(v['seconds'])+'s. This is a narrow repair of the witnessed component, not a whole-spectrum envelope.'
raw=raw.replace(heading,para.encode('utf-8')+nl+nl+heading,1)
heading=b'## actual persistence receipts or precise save blocker';assert raw.count(heading)==1
raw=raw.replace(heading,('Refined NEXT: '+p['next_action']).encode('utf-8')+nl+nl+heading,1)
heading=b'## Universal bridge';assert raw.count(heading)==1
new='This stage advances C019 stopping-tree payment and C024 history transfer by refuting the proposed positive-outer-correction envelope on an actual seven-bit query, uniformly K>=3, with exact missing mean stockG>0.107184 bits. It then isolates the responsible EMPTY Fourier entropy term and proves an ALL-DIMENSION component envelope V=phi(Ef)+3I<=9I/2 that pays it under every physical query. The residual nonempty drift is negative on this witness, but its universal coherence and initial influence payment remain unproved. NEXT retains the full empty-term bill and tests nonempty coefficient cancellations from SAME actually unused original influence stock, old labels and both complete terminals; this targets the unpaid universal component rather than extending a closed finite census. Full FEI remains OPEN.'
raw=raw[:raw.index(heading)]+heading+nl+nl+new.encode('utf-8')+nl;(R/'REPORT.md').write_bytes(raw)
(AG/'STATUS.md').write_text('STATE: A071 stage20: C_plus+sum(q inner hull) refuted on7bits forALL K>=3;exact drift>0.107184;EMPTY term isolated and universal component V=phi(Ef)+3I<=9I/2 proved;nonempty witness drift<0;FEI OPEN, review pending.\nNEXT: A074/A089/A092 review witness+vacuum proof;retain full empty-term payment, test NONEMPTY signed outer correction at coefficient cancellations from SAME unused influence owner, old labels and both full children.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
for name in ['WORKLOG.md','LEARNED.md']:
 with (AG/name).open('a',encoding='utf-8',newline='') as f:f.write('\n'+stamp+' '+R.name+' VACUUM: Isolated all positive witness drift in empty coefficient; nonempty remainder<0 iff7^3087<2^5076*3^2268. Universal phi(t)=-t²log2(t²) is2/ln2-Lipschitz; mean coupling and influence telescoping give superharmonic V=phi(Ef)+3I<=9I/2. This pays only EMPTY entropy, using actually unused influence; full nonempty envelope remains open.256 tables/768 queries checked, all-dimensional proof analytic.\n')
fields=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert set(p)=={x.split(' (')[0] for x in fields['progress_fields']}
for q in claims:assert set(q)==set(fields['claim_fields']) and q['statement_sha256']==digest(q['exact_statement'],q['hypotheses'])
assert all(('## '+x).encode() in raw for x in fields['report_fields'])
receipt={'saved_at':stamp,'schema':'PASS','claims':2,'external_review':'PENDING','supervisor_mirror':'UNVERIFIED','own_jobs_remaining':'NONE','full_fei':'OPEN','files':[],'rolling_files':[]}
for f in sorted(R.rglob('*')):
 if f.is_file() and f.name!='PERSISTENCE.json':
  assert f.stat().st_size<20*1024**2;receipt['files'].append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:receipt['rolling_files'].append({'path':str(AG/n),'sha256':sha(AG/n)})
assert len((AG/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes();save(R/'out/PERSISTENCE.json',receipt)
assert all(sha(R/z['path'])==z['sha256'] for z in receipt['files'])
print(json.dumps({'claims':2,'files_verified':len(receipt['files']),'schema':'PASS','vacuum_component':'UNIVERSAL_PROOF','nonempty_universal':'OPEN','full_fei':'OPEN','jobs_remaining':'NONE'}))
