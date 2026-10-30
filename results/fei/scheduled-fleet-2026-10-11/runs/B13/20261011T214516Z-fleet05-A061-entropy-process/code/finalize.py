from pathlib import Path
import json,hashlib,datetime

root=Path(__file__).resolve().parents[3]
run=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
runid=run.name
def save(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
consumers=['A023','A026','A028','A029','A037','A062','A063','A064','A066','A087','A094','B20']
statements=[
 ('A061-FAIR-TREE-PROCESS',
  'For every finite-dimensional uniform Boolean sign and fair adaptive physical restriction policy querying each coordinate at most once, with filtration given by past physical observations and an independent policy seed, H(g_t)+sum_{s<t}D_s and I(g_t)+sum_{s<t}d_s are stopped martingales, where D_s=B_s+J_s is the conditional spectral erasure plus the actual physical-child/spectral mutual information and d_s is queried influence. For tau<=n, H(f)=E H(g_tau)+E sum_{s<tau}D_s and I(f)=E I(g_tau)+E sum_{s<tau}d_s.',
  ['Boolean sign output','uniform finite input cube','fair physical queries selected using past only','no coordinate queried twice','entropy in bits','tau<=n']),
 ('A061-LOG-COMPENSATION',
  'On every such fair finite tree, lambda_t=sum_{T:b_T^2>0}b_T^2 log2((a_T^2+b_T^2)/b_T^2) satisfies D_t<=lambda_t+(3/ln(2))d_t. Therefore (3/ln(2))I(g_t)-H(g_t)-sum_{s<t}lambda_s is a supermartingale. If at every live node every positive b_T^2/(a_T^2+b_T^2)>=epsilon for fixed epsilon in (0,1], then C I(g_t)-H(g_t) is a supermartingale for C=log2(1/epsilon)+3/ln(2); hence H(f)<=C I(f)+E[H(g_tau)-C I(g_tau)].',
  ['same fair finite tree as A061-FAIR-TREE-PROCESS v1','entropy in bits','a_T and b_T are actual parent Fourier coefficients without and with queried coordinate','density bound required only for second supermartingale','no universal density or logarithmic payment hypothesis claimed'])
]
claims=[]
for cid,statement,hyp in statements:
    digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    claims.append({'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A061'],'proof_source':{'run_id':runid,'path':'REPORT.md','sections':'1--2' if cid.endswith('PROCESS') else '3--4'},'proof_dependencies':[] if cid.endswith('PROCESS') else [{'claim_id':'A061-FAIR-TREE-PROCESS','version':1}],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers})
save('CLAIMS.json',claims)
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':runid,'stream':'B13','packet_id':'A061','gap_id':'G-R-MISMATCH','attempt_id':'A061-entropy-process-1',
 'method':'Reconstruct fair physical filtration and exact Parseval/entropy increments; prove one-sided logarithmic compensation and sufficient density drift; exact symbolic finite checks',
 'mathematical_delta':'A061 baseline interface closed locally: exact entropy/influence martingales with retained terminal terms, unconditional log-cost supermartingale, and CI-H supermartingale under an explicit proved spectral density hypothesis. Universal cumulative log payment remains open; B05 no-go excludes all-policy fixed-price drift.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW',
 'mathematical_status':'A061_INTERFACE_PROVED; FULL_FEI_OPEN; G-R-MISMATCH_OPEN',
 'claim_versions_used':[{'claim_id':'B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO','version':1,'use':'scope obstruction only; not a positive-proof dependency'}],
 'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':1} for x in claims],
 'source_artifacts':['REPORT.md','FAIR_TREE_ENTROPY_PROCESS.tex','PROCESS_INTERFACE.json','FROZEN_SPEC.json','code/check_process.py','out/CHECK_RESULTS.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':consumers,
 'next_action':'A064 constructs a state debt Q for selector-first B05 restrictions with D<=Cd+Q-E Q_child and a paid terminal boundary; A087/A094 independently reconstruct current finite process.',
 'stagnant_substantive_attempts':0,'blockers':['Universal adaptive cumulative logarithmic payment unproved; independent review pending. B13 lead notes absent at initial read.'],
 'packet_ids':['A061']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
base=Path(r'~\mop_fei100')
sources=[]
paths=list((base/'reports'/'fei-2026-10-11').glob('*.json'))+list((base/'reports'/'fei-2026-10-11').glob('*.md'))+list((base/'reports'/'fei-2026-10-11').glob('*.tex'))
sup=base/'research_pushes'/'2026-10-11-full-fei-100-agents'
paths += [sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((sup/'sources').glob('*.md'))
paths += list((base/'reports'/'fei-2026-10-11'/'runs').rglob('REPORT.md'))
paths += list(Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
for p in paths:
    raw=p.read_bytes()
    try: content=raw.decode('utf-8'); enc='utf-8'
    except UnicodeDecodeError: content=raw.decode('cp1252'); enc='cp1252'
    sources.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc,'inspection':'full protocol; mathematical source/plan and paper targeted passages displayed; remaining content inventoried, not claimed as theorem validation'})
save('out/SOURCE_RECEIPTS.json',{'recorded_at':now,'sources':sources,'lead_notes_initially_absent':True,'scope':'Hashes record versions accessed, not independent mathematical review of every source.'})
results=json.loads((run/'out'/'CHECK_RESULTS.json').read_text())
assert results['status']=='PASS' and results['functions']==278
report=(run/'REPORT.md').read_text(encoding='utf-8')
import re
report=re.sub(r'out/CHECK_RESULTS.json records .*?checker runtime\.|out/CHECK_RESULTS.json records counts and elapsed runtime\.',f"out/CHECK_RESULTS.json records {results['exact_assertions']:,} exact assertions passed, {results['adaptive_trees']} adaptive trees, {results['coordinate_splits_including_tree_rechecks']:,} split checks including tree rechecks, and {results['elapsed_seconds']:.3f} seconds of checker runtime.",report)
(run/'REPORT.md').write_text(report,encoding='utf-8')
(root/'STATUS.md').write_text(f"STATE: A061 entropy-process packet complete locally: exact fair-tree increments and terminal telescope; log compensation and density-hypothesis supermartingale proved; {results['exact_assertions']:,} exact assertions passed; review pending; full FEI OPEN.\nNEXT: A087/A094 review; A064 pay cumulative logarithmic charge using a nonreusing state debt on the actual B05 tree; B13 lead notes absent at initial read.\n",encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f"\n{now} — A061 final validation: exact all-functions n<=3 Walsh/prime-log check passed {results['exact_assertions']:,} assertions across 556 adaptive trees, including early stop at two residual bits with nonzero terminal entropy. Initial one-bit stopping check replaced because its terminal H was always zero. UTF-8 decoding of paper texts failed; reread with cp1252. Local artifacts complete, independent review and universal payment pending.\n")
with (root/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA061 durable interface: fair adaptive physical queries preserve a uniform unqueried cube. Entropy decrement D=B+J>=0; queried influence loss is d. H+sum D and I+sum d are martingales; terminal H must be retained. The sign for FEI is CI-H supermartingale under D<=Cd. With lambda=sum b^2 log2((a^2+b^2)/b^2), D<=lambda+3d/ln2; hence (3/ln2)I-H-sum lambda is always a supermartingale. Positive theta>=epsilon gives C=log2(1/epsilon)+3/ln2. A debt Q needs D<=Cd+Q-E Q_child. B05 excludes all-policy finite C but not good-coordinate or nonlocal selection. Exact entropy equalities can be checked with rational prime-log coefficient dictionaries rather than floating-point logs.\n')
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        raw=p.read_bytes(); assert len(raw)<20*1024*1024
        receipts.append({'path':str(p.relative_to(run)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save('out/PERSISTENCE_RECEIPTS.json',{'recorded_at':now,'local_only':True,'files':receipts,'mirrors_verified':False,'independent_review_completed':False})
protocol=json.loads((base/'reports'/'fei-2026-10-11'/'EXECUTION_PROTOCOL.json').read_text())
# Protocol's final array entry includes explanatory parentheses, while its
# compatibility section explicitly specifies the actual JSON key packet_ids.
expected_progress={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
for c in claims: assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((run/'PROGRESS.json').read_text())==json.loads((run/'PACKET_DELTA.json').read_text())
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','run':str(run),'files':len(receipts),'claim_count':len(claims),'validation':results},indent=2))
