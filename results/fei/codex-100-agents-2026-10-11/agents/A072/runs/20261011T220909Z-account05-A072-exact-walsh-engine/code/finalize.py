"""Persist packet metadata and verify local artifact/schema integrity."""
import ast, hashlib, json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
CAM=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM=Path(r'~\brain_workers\FEI100_20261011')
RUNID=ROOT.name

def dump(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads((CAM/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
engine=json.loads((ROOT/'ENGINE_CERTIFICATE.json').read_text())
assert engine['failures']==0 and engine['physical_block_cases']==20736
assert engine['physical_child_occurrences']==62208
assert engine['A071_exact_spectrum_matches']==3612
assert engine['entropy_comparisons']==0
assert len((ROOT/'out/grid.jsonl').read_text().splitlines())==3456
uniform=json.loads((ROOT/'out/uniform.json').read_text())
assert len(uniform)==278
assert [sum(r['n']==n for r in uniform) for n in range(4)]==[2,4,16,256]
old=TEAM/'agents/A016/runs/20261011T213934Z-account05-A016-addressing-benchmark/code/check_addressing.py'
def fnode(path,name):
    return next(t for t in ast.parse(path.read_text(encoding='utf-8')).body
                if isinstance(t,ast.FunctionDef) and t.name==name)
assert ast.dump(fnode(old,'fwht'))==ast.dump(fnode(ROOT/'EXACT_WALSH_INTERFACE.py','fwht'))

statement=('For every representative three-bit sign table f(000)=+1, every bias vector '
 'p in {1/8,1/4,1/2}^3 and every nonempty proper physical block, the saved exact '
 'Walsh/centered-polynomial spectra have Parseval mass one and sign-valued inverses, '
 'their coordinate spectral influences equal 4p_i(1-p_i) times independently '
 'enumerated pivotal probabilities, and physical-child mixtures and retained '
 'influence averages agree with the parent marginals. These 20736 block cases '
 'and all 278 uniform sign tables in dimensions zero through three pass the '
 'integer/Fraction checker with no failure; 3612 distinct spectra match A071.')
hyp=['Boolean sign tables and little-endian assignment order stated in REPORT.md',
     'Interior rational independent biases in the specified finite grid',
     'Uniform integer characters (-1)^popcount(x&s); biased centered orthonormal basis',
     'No entropy, off-grid or higher-dimensional inequality conclusion']
hash_payload=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'))
claim={
 'claim_id':'A072-EXACT-GRID-ALGEBRA','version':1,'exact_statement':statement,
 'hypotheses':hyp,'statement_sha256':hashlib.sha256(hash_payload.encode()).hexdigest(),
 'contributors':['A072'],'proof_source':['REPORT.md','EXACT_WALSH_INTERFACE.py','code/verify.py','ENGINE_CERTIFICATE.json'],
 'proof_dependencies':[],'review_records':[],
 'status':'FINITE_ALGEBRAIC_CERTIFICATE_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A073','A074','A085','A092','B09','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':RUNID,'stream':'B15','packet_id':'A072',
 'gap_id':'G-BIASED-TAX','attempt_id':'A072-ALGEBRA-1',
 'method':'Reuse checked integer FWHT; rational centered-polynomial conversion; exact sign inverses and independent physical edges',
 'mathematical_delta':'Closed baseline algebraic verification on A071 grid: 20736 blocks, 62208 child occurrences, 3612 exact spectrum matches; no entropy or universal payment conclusion.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED_REVIEW_PENDING',
 'mathematical_status':'BASELINE_ALGEBRAIC_CERTIFICATE_COMPLETE_FULL_FEI_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':['A072-EXACT-GRID-ALGEBRA@1'],
 'source_artifacts':['FROZEN_SPEC.json','EXACT_WALSH_INTERFACE.py','ENGINE_CERTIFICATE.json','out/grid.jsonl','out/uniform.json','out/witnesses.json','out/source_receipts.json'],
 'next_consumers':['A073','A074','A085','A092','B09','B20'],
 'next_action':'Consume a separately versioned sharper singleton tax and certify its sign on the saved exact Boolean grid; independent engine review by A085/A092.',
 'stagnant_substantive_attempts':0,
 'blockers':['B15 STREAM_NOTES.md absent; no block to algebraic work.','Universal conditional entropy and nonreused bias-tax influence payment remain open.'],
 'packet_ids':['A072']}
# Protocol annotates the packet_ids field with prose; its wire key is packet_ids
# as explicitly required by the compatibility section and packet contract.
progress_fields={f.split(' (',1)[0] for f in protocol['required_per_run']['progress_fields']}
assert set(progress)==progress_fields
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
receipts=[]
def receipt(p,scope):
    if p.exists(): receipts.append({'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size,'consultation_scope':scope})
    else: receipts.append({'path':str(p),'status':'ABSENT','consultation_scope':scope})
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    receipt(CAM/name,'Protocol in full; campaign state/registries; packet and plan B15 contracts as located in REPORT.md')
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    receipt(SUP/name,'Campaign context and scope guards consulted; no imported entropy theorem dependency')
receipt(SUP/'sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','Sections 1-3 physical mixture and influence ledger; complete note returned')
for n in ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    receipt(TEAM/'context'/n,'Introduction/normalization locators stated in REPORT.md; no full independent proof reconstruction')
receipt(TEAM/'BOARD.md','Stage-start snapshot')
receipt(TEAM/'claude/B15/STREAM_NOTES.md','Requested stage direction; absent')
for s,r in [('B05','20261011T193057Z-account01-B05-rare-restrictions'),('B09','20261011T195500Z-account01-B09-biased-restriction-uncertainty'),('B19','20261011T195038Z-account01-B19-independent-review')]:
    receipt(CAM/'runs'/s/r/'REPORT.md','Earlier run scope and source definitions read')
receipt(old,'FWHT copied verbatim; AST equality verified by finalizer')
A071=TEAM/'agents/A071/runs/20261011T214639Z-account05-A071-search-space-design'
for n in ['REPORT.md','SEARCH_DOMAIN.json','code/search.py']:
    receipt(A071/n,'Existing family and spectrum implementation consulted; entropy checker not rerun')
dump(ROOT/'out/source_receipts.json',receipts)
report=(ROOT/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:
    assert '\n## '+field+'\n' in '\n'+report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
(AGENT/'STATUS.md').write_text(
 'STATE: A072 baseline complete locally: 20736 exact blocks, 62208 children, 3612 A071 spectrum matches; review pending; full FEI OPEN.\n'
 'NEXT: A085/A092 review engine; A073/A074 consume exact records and versioned singleton-tax candidate without repeating baseline.\n',encoding='utf-8')
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='manifest.json':
        assert p.stat().st_size<20_000_000
        manifest.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)})
dump(ROOT/'out/manifest.json',{'saved_at_utc':datetime.now(timezone.utc).isoformat(),'files':manifest,
 'schema_field_sets_verified':True,'delta_identical':True,'fwht_AST_matches_A016':True,
 'mirror_verification':'PENDING_SUPERVISOR','independent_review':'PENDING'})
print(json.dumps({'files':len(manifest),'all_files_under_20_MB':True,'protocol_fields_exact':True,
 'full_grid_verified':True,'fwht_reuse_confirmed':True,'persistence':'LOCAL_SAVED'}))
