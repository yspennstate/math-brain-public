import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
SOURCE=AGENT.parent/'A071'/'runs'/'20261011T233808Z-account05-A071-search-space-design'
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
run=json.loads((ROOT/'out'/'review_census.json').read_text());assert run['status']=='PASS' and not run['pilot']
pilot=json.loads((ROOT/'out'/'pilot.json').read_text())
assert 2**316*89**445<3**45*13**845
assert 2**319*89**445>3**45*13**845
orbit=set()
for t in range(32):
    for i in range(5):
        for j in range(i+1,5):orbit.add((1<<t)|(1<<(t^(1<<i)))|(1<<(t^(1<<j))))
assert len(orbit)==320 and not(orbit&{x^0xffffffff for x in orbit})
certificate={'source_claim':'A071-EXACT-FIVEBIT-ERASURE-SELECTION@1','reviewer':'A082','verdict':'HOLDS_AT_STATED_SCOPE',
 'exact_constant':'16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89)',
 'rational_bounds':['107/40','27/10'],'bound_certificates':['2^319 * 89^445 > 3^45 * 13^845','2^316 * 89^445 < 3^45 * 13^845'],
 'extremal_negative_masks':len(orbit),'extremal_truth_tables_with_output_complement':640,
 'checked_domain':run,'seed':'out/seed_certificate.json','separate_physical_bridge':'EXHAUSTIVENESS_LEMMA.tex, Theorem 2',
 'source_reconstruction':'covering proof, direct parity-popcount coefficient engine, independent Fraction 50-term logarithm intervals, exact integer-product seed signs',
 'universal_status':'OPEN; a known six-bit witness excludes extending K5 universally'}
dump(ROOT/'FINITE_INEQUALITY_CERTIFICATE.json',certificate)
dump(ROOT/'out'/'review_verdict.json',{'reviewed_claim':'A071-EXACT-FIVEBIT-ERASURE-SELECTION','version':1,'reviewer':'A082','verdict':'HOLDS_AT_STATED_SCOPE','contributor_conflict':False,'substantive_repair':False,'source_claim_sha256':'7e30279e1c16bc098377bb8dad61dc8357cff0fe4f760865a4766e2ff3de1a67','method':certificate['source_reconstruction'],'evidence':'out/review_census.json; out/seed_certificate.json; EXHAUSTIVENESS_LEMMA.tex','adoption':'shared source records not modified'})
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
sourceclaim=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
sourcecopy=dict(sourceclaim)
sourcecopy['review_records']=sourcecopy['review_records']+[json.loads((ROOT/'out'/'review_verdict.json').read_text())]
sourcecopy['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_REVIEW_RECORD'
sourcecopy['proof_source']=[str(SOURCE/p) for p in sourceclaim['proof_source']]+[str(ROOT/'EXHAUSTIVENESS_LEMMA.tex'),str(ROOT/'out'/'review_census.json')]
s='For every finite uniform physical cube, each nonconstant Boolean sign whose nonzero Fourier support has affine F2 dimension at most five, and each disjoint product of such factors, admits a relevant coordinate with B_i<=K5 I_i at every physical restriction, and H(f)<=(K5+2/ln2)I(f), where K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89)<27/10. K5 is optimal for the selectable-erasure statement in this class.'
h=['Boolean sign outputs on a uniform finite cube','entropy in bits','affine Fourier support dimension at most five for each disjoint factor','only physical coordinate restrictions; factors have disjoint variable sets']
bridge={'claim_id':'A082-AFFINE5-ERASURE-BRIDGE','version':1,'exact_statement':s,'hypotheses':h,
 'statement_sha256':sha(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()),
 'contributors':['A082','A026 (source of parameterized affine-support argument)'],
 'proof_source':str(ROOT/'EXHAUSTIVENESS_LEMMA.tex')+', Theorem 2','proof_dependencies':[{'claim_id':'A071-EXACT-FIVEBIT-ERASURE-SELECTION','version':1},'C005 exact decrement and JS bound (reconstructed in prior A082 and B17 sources)'],
 'review_records':[],'status':'PROVED_LOCAL_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A026','A027','A028','A061','A075','A081','A085','A090','A094','B20']}
claims=[sourcecopy,bridge]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
dump(ROOT/'CLAIMS.json',claims)
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A082','gap_id':'G-R-SELECT','attempt_id':'A082-INDEPENDENT-K5-02',
 'method':'independent full finite review with direct parity-popcount engine and exact rational intervals; separate hereditary affine5 exhaustiveness proof',
 'mathematical_delta':'A071 K5 exact upper bound and all 640 extremizers independently reconstructed; hereditary affine-support leaf certificate expands dimension four to five with constant K5+2/ln2; universal C018/C019 gap remains open.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'FINITE_K5_INDEPENDENTLY_REVIEWED_AFFINE5_BRIDGE_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A071-EXACT-FIVEBIT-ERASURE-SELECTION','version':1},{'claim_id':'A082-AFFINE4-ERASURE-BRIDGE','version':1},{'claim_id':'B17-JS-PACKET-SCALAR','version':1}],
 'claims_created_or_changed':[{'claim_id':'A071-EXACT-FIVEBIT-ERASURE-SELECTION','version':1,'change':'local independent review attached; no source mutation'},{'claim_id':bridge['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','CLAIMS.json','FINITE_INEQUALITY_CERTIFICATE.json','EXHAUSTIVENESS_LEMMA.tex','FROZEN_SPEC.json','code/reconstruct.py','out/review_census.json','out/seed_certificate.json','out/review_verdict.json'],
 'next_consumers':bridge['next_consumers']+['A071','A074','A092'],
 'next_action':'Consume an explicit A027/A028 or A097/A064 proper-stopping candidate and certify its unpaid path-to-leaf residual with the affine5 terminal constant; do not enumerate n=6.',
 'stagnant_substantive_attempts':0,'blockers':['No universal influence-paid stopping transport to affine5 leaves has been proved. New affine5 application still needs independent review.'], 'packet_ids':['A082']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
sources=[PROTO,AGENT.parents[1]/'BOARD.md',AGENT.parents[1]/'claude'/'B17'/'STREAM_NOTES.md',AGENT.parents[1]/'claude'/'B15'/'STREAM_NOTES.md']
sources += [SOURCE/p for p in sourceclaim['proof_source']]+[SOURCE/'CLAIMS.json']
sources += [AGENT/'runs'/'20261011T221008Z-account05-A082-finite-inequalities'/'EXHAUSTIVENESS_LEMMA.tex']
dump(ROOT/'out'/'source_receipts.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sources])
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('@PILOT_SECONDS@',f'{pilot["elapsed_seconds"]:.6f}').replace('@FULL_SECONDS@',f'{run["elapsed_seconds"]:.6f}')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
for f in protocol['required_per_run']['report_fields']:assert f in report
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: Stage2 saved: A071 exact K5 and 640 extremizers independently reconstructed; hereditary affine5/product bridge proved; bridge review pending; full FEI OPEN.\nNEXT: Audit a concrete A027/A028 or A097/A064 stopping residual with certified affine5 terminal cost; A090/A094 review bridge; no n=6 census.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now}: Stage2 consumed the newer A071 completed census instead of repeating discovery. Independent parity-popcount/Fraction replay checked 2^31 masks, 5778648 retained representatives, one exact equality, 640 extremizers; elapsed {run["elapsed_seconds"]:.6f}s. Created affine5 hereditary bridge and local A071 review. Guard returned 1 on two checks; all jobs estimated <=80 MB, below the 300 MB guarded-job threshold. Full FEI remains open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nExact E*(5)=K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89), with 640 three-vertex path extremizers. Independently reproduced the full covering scan without FWHT. Covering influence-order and anchored-translation filters can both hold: input translations preserve the entire influence vector. Direct c_s=16 1_{s=0}-|A|+2 popcount(A intersect odd-character-mask) reconstructs every Walsh coefficient.\nThe physical affine-support projection bridge is parameterized: a certified r-junta constant extends to affine Fourier dimension<=r and disjoint products at every restriction. For r=5 it gives H<=(K5+2/ln2)I. Neither the finite search nor that bridge gives a dimension bound on unrestricted residuals; the known six-bit witness exceeds K5. Independent finite review is a completed artifact, not proof of universal selection.\n')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='persistence_receipts.json':
        b=p.read_bytes();assert len(b)<20*1024*1024;files.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b)})
dump(ROOT/'out'/'persistence_receipts.json',{'saved_at':now,'files':files,'regeneration_commands':['python -X utf8 code/reconstruct.py --pilot','python -X utf8 code/reconstruct.py','python -X utf8 code/finalize.py'],'command_workdir':str(ROOT),'mirror':'not observed','bridge_independent_review':'pending'})
assert all(sha((ROOT/x['path']).read_bytes())==x['sha256'] for x in files)
print(json.dumps({'status':'SAVED_AND_VERIFIED','artifacts':len(files),'schema_checks':'PASS','review':'A071 v1 HOLDS','bridge':'PROVED_LOCAL_PENDING_REVIEW'},indent=2))
