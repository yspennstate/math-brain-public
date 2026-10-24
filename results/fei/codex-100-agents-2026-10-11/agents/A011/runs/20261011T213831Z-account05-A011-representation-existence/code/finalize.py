import pathlib,json,hashlib,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
CAM=pathlib.Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=pathlib.Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CTX=pathlib.Path(r'~\brain_workers\FEI100_20261011\context')
PROTOCOL=json.loads((CAM/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,x):
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def record(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
sources=[]
for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']:
    sources.append(record(CAM/f))
for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','baseline/current-threshold-paper.tex','sources/OVERLAPPING_PRODUCT_NOTE.md','sources/ERASURE_REDUCTION.md']:
    sources.append(record(SUP/f))
for f in ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    sources.append(record(CTX/f))
for p in (CAM/'runs').rglob('REPORT.md'): sources.append(record(p))
sources.append(record(pathlib.Path(r'~\brain_workers\FEI100_20261011\BOARD.md')))
save(ROOT/'out'/'SOURCE_ARTIFACTS.json',{'recorded_at_utc':NOW,'actual_read_scopes':'REPORT.md source section; hashes do not assert every line was read','files':sources,'missing_source':r'~\brain_workers\FEI100_20261011\claude\B03\STREAM_NOTES.md','web_sources':[{'url':'https://arxiv.org/html/1806.03646v2','locator':'introduction and prior work','version':'v2'},{'url':'https://arxiv.org/abs/1312.3003','locator':'abstract','version':'abstract page'}]})
statement=('For every finite uniform selector decision tree with no repeated query along any path and Boolean leaves on an independent common data cube, given complete leaf spectral prefix codes of expected costs c_l, there is a constructive cover C_l AND [g_l=1] and an exact joint spectral witness with a prefix code of expected cost 2D+sum_l p_l c_l, where p_l=2^(-d_l) and D=sum_l p_l d_l. If I_sel(F)>=gamma D and c_l<=K I(g_l), this full cost is <=max(2/gamma,K) I(F). For unsigned nonempty character leaves with repeated labels allowed, the leaf costs are zero and I_sel=B/2, where B=E_x sum_j 1[label(x)!=label(x^flip_j)]; B>=beta D gives full cost <=(4/beta) I_sel. The alternating two-label first-positive comb has D=2(1-2^(-a)), B>=D/2, I_data=1 and I_sel<1 for every a>=1, hence full cost <=8 I_sel while conjunction-cover read and a are unbounded.')
hypotheses=['uniform finite selector and data cubes, independent blocks','finite selector tree, coordinate never queried twice along a path','Boolean leaves on the common data cube; overlaps and repeated leaves allowed','leaf witness codebooks fixed before spectral sample, prefix-free, exact decoded Fourier law','gamma>0 and K>=0 only for the stated admitted general-leaf consequence','unsigned nonempty character leaves and beta>0 only for the character consequence','entropy and code lengths in bits; ordinary uniform physical total influence']
claim={'claim_id':'A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A011/account05'],'proof_source':{'run_id':ROOT.name,'path':'STRUCTURED_COVER.tex','cost_ledger':'COVER_COST.md','validation':'out/EXACT_RESULTS.json'},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A008','A009','A012','A013','A014','A015','A019','A058','A086','A094','B20']}
assert set(claim)==set(PROTOCOL['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':PROTOCOL['revision'],'run_id':ROOT.name,'stream':'B03','packet_id':'A011','gap_id':'G-J-COST','attempt_id':'A011-representation-transcript-1','method':'exact physical/spectral transcript coupling, prefix/Kraft reference, boundary-retention admission, rational exhaustive tree validation','mathematical_delta':'Constructive repeated-label selector-tree covers with complete joint cost 2D+average leaf code cost; explicit influence admission and unbounded-read low-energy alternating-comb family. Distinct-label affine selectors recognized as baseline and not recounted.','deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION','mathematical_status':'RESTRICTED_CLASS_AUTHOR_PROVED; UNIVERSAL_REPRESENTATION_AND_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['STRUCTURED_COVER.tex','COVER_COST.md','REPORT.md','CLAIMS.json','code/validate.py','out/FROZEN_SPEC.json','out/EXACT_RESULTS.json','out/SOURCE_ARTIFACTS.json'],'next_consumers':claim['next_consumers'],'next_action':'A086/A094 independently reconstruct coupling and prefix decoder; next substantive work is a whole-cost reference on low-boundary repeated-label trees retaining posterior entropy.','stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor adoption pending.','General Boolean admission I_sel>=gamma D is unproved.','B03 STREAM_NOTES.md absent at source intake; independent work proceeded.'],'packet_ids':['A011']}
fields=[x for x in PROTOCOL['required_per_run']['progress_fields'] if not x.startswith('packet_ids')]+['packet_ids']
assert set(progress)==set(fields)
save(ROOT/'PROGRESS.json',progress); save(ROOT/'PACKET_DELTA.json',progress)
status='STATE: A011 local artifact complete: repeated-label selector transcript cost <=2D, explicit boundary admission, unbounded-read comb; 50,089 exact checks passed; independent review pending; full FEI OPEN.\nNEXT: A086/A094 review code/coupling; optimize complete label and support cost on low-boundary trees, retaining posterior entropy.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{NOW}: Completed STRUCTURED_COVER.tex and COVER_COST.md. True witness uses fair child choice followed by exact signed packet theta. Prefix code length 2d+leafcost; Kraft sum <=1. Boundary admission pays cost without duplicate influence. Exhausted 1446 depth-three two-label trees, checked 64 comb recurrences and six comb truth tables; 50089 assertions passed in 0.967 seconds. Preserved average-depth prior art and universal admission gap. Required artifacts saved; A086/A094 independent review and supervisor copy pending.\n')
(AGENT/'LEARNED.md').write_text('''# Durable A011 facts

For finite no-repeat-on-path selector trees with shared Boolean data leaves and complete leaf spectral prefix codes, exact recursive Fourier-law coupling admits a prefix code of expected length 2D+sum p_l c_l. D is average selector tree depth. Encode the physical leaf path, the complete leaf code, then one spectral membership bit per path query. Kraft sum <=1; output collisions sum; posterior witness entropy remains H(W|S).

At a node, q=(u^2+v^2)/2 and theta=(u-v)^2/(4q). Fair physical child plus its spectral set, then Bernoulli(theta), yields the actual parent spectrum including coherent cross terms. Zero packets are omitted safely.

Physical selector admission I_sel>=gamma D and c_l<=K I(leaf) pay the entire code by max(2/gamma,K) I(F). Character leaves have zero code cost. For unsigned nonempty labels, I_sel=B/2 where B counts physical label-flipping selector edges. B>=beta D gives cost <=4 I_sel/beta. This is a hypothesis, not a universal theorem.

Alternating two-label first-positive comb: D=2(1-2^-a), r_a=1, r_j=1-r_(j+1)/2, B=sum 2^-(j-1)r_j>=D/2, I_data=1, I_sel<1. Conjunction cover read grows to a+1 and labels repeat; I_sel/a tends to zero. Full code <=8 I_sel. Author proof and 50089 exact self-checks complete; independent review pending.

All stopping leaves y1 and only terminal y2 give the same D but B=a 2^-(a-1), so boundary admission degenerates. A valid cheap-cover theorem cannot infer boundary retention from DNF existence or cell disjointness alone.

Distinct-character subcube selectors are already C011 affine-selector baseline. Expected-depth entropy bounds and decision-tree Fourier coding have prior art (Wan-Wright-Wu; Shalev prior-work discussion). The A011 claim is a complete campaign interface, with literature novelty unverified. Its prefix reference is separate from the original queue minimum.
''',encoding='utf-8')
required=['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json','STRUCTURED_COVER.tex','COVER_COST.md','code/validate.py','code/finalize.py','out/FROZEN_SPEC.json','out/EXACT_RESULTS.json','out/SOURCE_ARTIFACTS.json']
for name in required:
    p=ROOT/name; assert p.exists() and p.stat().st_size<20_000_000
    if p.suffix=='.json': json.loads(p.read_text(encoding='utf-8-sig'))
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in PROTOCOL['required_per_run']['report_fields']: assert '## '+field in report
receipts={'saved_at_utc':NOW,'local_only':True,'independent_review':'PENDING','supervisor_adoption':'PENDING','mirror_verification':'NOT_PERFORMED','files':[record(ROOT/name) for name in required],'rolling_files':[record(AGENT/name) for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]}
save(ROOT/'out'/'PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'saved':len(required),'protocol_fields':'PASS','report_fields':'PASS','compatibility_copy':'BYTE_EQUAL','statement_sha256':claim['statement_sha256'],'local_receipts':'out/PERSISTENCE_RECEIPTS.json'}))
