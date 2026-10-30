from pathlib import Path
import hashlib, json, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
P=Path(r'math-open-problems/reports\fei-2026-10-11')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
old=R.parent/'20261023T123929Z-fleet03-A063-information-revelation'
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
paths=[P/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list(Path(r'context').glob('*.txt'))
paths += [old/n for n in ['REPORT.md','PROOF.md','PROOF_PREFIX.md','CONE_BOUNDARY.md','code/quadratic_audit.py']]
paths += [Path(r'BOARD.md'),Path(r'claude\B13\STREAM_NOTES.md')]
paths += [p for p in (supp/'sources').iterdir() if p.suffix=='.md' and any(k in p.name for k in ['BLOCK_RESTRICTION','ERASURE','ENTROPY_RESTRICTION'])]
manifest=[]; excerpts=[]
for p in paths:
    raw=p.read_bytes()
    try: text=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: text=raw.decode('cp1252'); enc='cp1252 fallback; initial UTF-8 reader failed, source unmodified'
    manifest.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'decoding':enc})
    if p.suffix=='.txt' or p.parent.name=='sources':
        relevant=[(i+1,line[:240]) for i,line in enumerate(text.splitlines()) if any(w in line.lower() for w in ['chain rule','restriction','composition ident','spectral entropy'])]
        excerpts.append({'path':str(p),'decoding':enc,'matches_first_12':relevant[:12]})
write(R/'out/SOURCE_MANIFEST.json',manifest); write(R/'out/SOURCE_EXCERPTS.json',excerpts)
main=json.loads((R/'out/main.json').read_text(encoding='utf-8')); rank=json.loads((R/'out/rank_audit.json').read_text(encoding='utf-8'))
assert main['status']==rank['status']=='PASS'
assert main['script_sha256']==sha(R/'code/audit.py') and rank['script_sha256']==sha(R/'code/rank_audit.py')
statement=('For every even n>=2, every nonsingular quadratic Boolean phase on n bits, every normalized inherited reference positive on the actual full spectral support, and every adaptive physical query policy with optional actual full-product resets and stopping, using the source-induced kernel with fair zero-source extension, cumulative gross positive reset price C plus current Fourier entropy H is at most n pathwise. Thus the physically weighted sum of erasure KL E and actual outcome KL O, plus full terminal reference KL and entropy, is at most the initial source KL plus n. For the actual selector between dense=sum uj*vj and sparse=(sum uj)*(sum vj), on even n>=4 data bits, start with the ORIGINAL full product, query selector without reset, allow all such dense histories and retain the sparse reference with no resets. The SAME original S=4I bank pays all reached E/O, both full terminal H/K and any old debit omega<=S/4, retaining at least n/2-1>=1. No descendant admission is renewed. Full FEI remains open.')
cid='A063-INHERITED-BENT-FIRST-RESET-SELECTOR-OWNER'
dep='A063-QUADRATIC-ORIGINAL-RANK-OWNER-OPTIONAL-RESETS@1'
cons=['A061','A064','A065','A087','A094','B13 lead']
claim={'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['uniform cube; entropy and KL in bits','bent quadratic for arbitrary inherited-reference theorem; n even>=2','reference positive on actual source support; exact source kernel; fair zero-source extension','selector fixture n even>=4; selector queried first; no sparse product resets','physical reach probabilities; SAME original owner and prior relative quarter'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A063'],
 'proof_source':['PROOF.md sections 1-2','out/main.json','out/rank_audit.json'],
 'proof_dependencies':[dep],
 'review_records':[{'reviewer':'A063','kind':'author analytic reconstruction and exact finite checks; NOT independent agent acceptance','artifacts':['out/main.json','out/rank_audit.json'],'scope':'source chain and all finite query/reset/cut histories for frozen roots; independent integer-rank representation; no Lean compilation'}],
 'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':cons}
write(R/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B13','packet_id':'A063','gap_id':'G-R-MISMATCH',
 'attempt_id':'A063-inherited-bent-first-reset-and-selected-selector-v1',
 'method':'bound first reset by already-earned rank drops without inherited cone; retain sparse source reference; exact E/O/K physical telescope and same original account',
 'mathematical_delta':'C+H<=n for bent quadratic with arbitrary supported inherited reference; actual cubic selector fixture crosses cone failure using SAME original4I, oldquarter and full terminal H/K, residual>=n/2-1. 7978 primary +1257 helper assertions;898 independent-rank assertions. FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_WITH_EXACT_FINITE_CERTIFICATES; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[dep],'claims_created_or_changed':[cid+'@1'],
 'source_artifacts':['REPORT.md','PROOF.md','SEARCH_SPEC.json','CLAIMS.json','code/audit.py','code/rank_audit.py','code/KeyStep.lean','out/pilot.json','out/main.json','out/rank_audit.json','out/SOURCE_MANIFEST.json','out/SOURCE_EXCERPTS.json'],
 'next_consumers':cons,'next_action':'A087/A094 reconstruct inherited-bent first-reset and original selector payment. Next pay or defer a NECESSARY first product return for a non-source-equal rank-deficient inherited child from SAME remaining original owner, retaining old debits/full terminal H/K.',
 'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary rank-deficient inherited child original supplier/eligible return policy open','Independent review of prior interval lemma and new extension pending','Lean compile HELD: memok exit1 physical free2.0GB commit free2.2GB','Wake warns stale owner model/state/dream; no affected note is mathematical evidence','Remote supervisor adoption unverified; git/shared research writes forbidden'],
 'packet_ids':['A063']}
write(R/'PROGRESS.json',progress); write(R/'PACKET_DELTA.json',progress)
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
pf={k.split(' (')[0] for k in required['progress_fields']}
assert set(progress)==pf,(set(progress)^pf)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+field in report for field in required['report_fields'])
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
(A/'STATUS.md').write_text('STATE: Bent arbitrary inherited refs: C+H<=n; actual cubic selector paid SAME original4I with sparse reference retained, oldquarter/full H/K, residual>=n/2-1; exact checks PASS; review pending; FEI OPEN.\nNEXT: A087/A094 review first-reset/selector proof; pay or defer NECESSARY first product return of non-source-equal rank-deficient inherited child from SAME original unused owner; no renewed admission.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': '+R.name+': Proved arbitrary-supported-reference bent first-reset C+H<=n and selected cubic boundary SAME4I payment, residual>=n/2-1 after oldquarter/full H/K. Pilot2129+622, main7978+1257, independent rank898 exact assertions PASS. Lean HELD fresh memok refusal. Rank-deficient star guard TC2 before drops rejects dropping bent hypothesis. Initial supplemental/paper read failed UTF8; explicit cp1252 fallback used only for affected source, no source mutation. FEI OPEN; independent review and general deficient-child supplier unpaid.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-26: A bent quadratic with ANY supported inherited reference needs no cone repair before its first reset: first TC<=earned rank drops, then prior product-interval bound gives pathwise C+H<=n and cumulative E+O+terminalK+H<=Kinitial+n. At dense/sparse cubic selector keep sparse inherited p (never pay optional n-2 product admission), allow dense optional histories; SAME original4I minus oldquarter retains>=n/2-1. Actual selector O is paid by original source chain, not called physical J. Deficient star has TC2 at D0, so full-rank hypothesis is essential to this mechanism. Do not reserve maximum gross resets and full root H independently when C+H has a joint bound. Review pending; FEI OPEN.\n')
bundle=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='BUNDLE_MANIFEST.json':
        assert p.stat().st_size<20_000_000
        bundle.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
write(R/'out/BUNDLE_MANIFEST.json',bundle)
print(json.dumps({'status':'PASS','claim_fields':len(claim),'progress_fields':len(progress),'bundle_files':len(bundle),'source_files':len(manifest),'paper_encodings':[e['decoding'] for e in excerpts],'rank_assertions':rank['assertions']}))
