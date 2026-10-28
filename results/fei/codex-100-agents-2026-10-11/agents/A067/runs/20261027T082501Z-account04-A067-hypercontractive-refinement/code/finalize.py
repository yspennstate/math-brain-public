from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; AGENT=R.parents[1]
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def save(p,x):write(p,json.dumps(x,indent=2)+'\n')
results={name:json.loads(read(R/'out'/name)) for name in ['PILOT.json','CHECK.json','BOUNDARY.json','AUDIT.json']}
assert all(x['status']=='PASS' for x in results.values())
base=Path(r'math-open-problems/reports\fei-2026-10-11')
protocol=json.loads(read(base/'EXECUTION_PROTOCOL.json'))
statement='For every integer m>=6, every full-rank quadratic Boolean F2 phase b on 2m bits including affine terms, every set E of k distinct vertices with 1<=k<=2^(m-2), form c by flipping b only on E times {w=0} and G with z children b,c. Choose original rate4, I_X=(I(b)+I(c))/2, D=H(G)-(H(b)+H(c))/2, r4=4I_X-H(G), and inherit original squared-spectral marginals at every physical restriction. For every finite adaptive physical stopping forest below z, its complete actual entropy-drop-minus4-influence debit E_H obeys r4-E_H>m/2-25/12-(2m^2+2m-1)/(4*2^m)>=455/768. Every outcome, old D, actual removed influence J and both full terminal CE/KL bills are retained; no renewal or reset. Units bits.'
claim={
 'claim_id':'A067-GROWING-EDIT-QUADRATIC-ORIGINAL-RATE4-ALL-TREES','version':1,
 'exact_statement':statement,
 'hypotheses':['Boolean F2 quadratic phase; full polar rank 2m; arbitrary affine part','integer m>=6; 1<=k<=2^(m-2); distinct data marks flipped only at w=0','original physical z splice, fixed original rate4 and inherited marginals; all physical outcomes'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A067'],
 'proof_source':'PROOF.md sections1-6; out/CHECK.json, out/BOUNDARY.json, out/AUDIT.json',
 'proof_dependencies':[], 'review_records':[], 'status':'AUTHOR_PROOF_EXACT_CHECKED_REVIEW_PENDING',
 'supersedes':[], 'refutes':[],
 'first_unproved_line':'A noncircular original O(I) source for arbitrary nonquadratic cores with paid clean exits, or useful source-conditioned floors beyond k*2^-m<=1/4.',
 'next_consumers':['A088','A070','A094','B14','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A067',
 'gap_id':'C019-C024-ORIGINAL-SOURCE-GROWING-CANCELLATION','attempt_id':'A067-stage22-sector-weighted-integer-cancellation',
 'method':'Signed-bucket orthogonality and integer gaps; isolate actual rare W1 mass before pricing logs; mark occupation; actual quadratic clean rank.',
 'mathematical_delta':'Two edits extend to every growing set k<=2^(m-2), m>=6, with SAME original rate4 all-tree remainder>455/768. Removes a second log k from a naive worst-sector bound. Full FEI remains OPEN.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_PROOF_EXACT_CHECKED_INDEPENDENT_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[], 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['PROOF.md','SPEC.json','SPEC_BOUNDARY.json','SPEC_AUDIT.json','code/check.py','code/audit.py','out/PILOT.json','out/CHECK.json','out/BOUNDARY.json','out/AUDIT.json','out/AUDIT_V1_FAILURE.json','out/SOURCES.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A088/A070/A094 reconstruct sector-weighted growing-k payment; replace nonpositive quadratic clean exits by a SAME-source affordable criterion for nonquadratic seeds, retaining old D/J and full terminals.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending; no full-FEI arbitrary-core supplier.','Brain wake stale personal notes excluded; contract cache stale, no irreversible action.','Supervisor copying, mirror verification and downstream use unverified.'],
 'packet_ids':['A067']}
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
parent=Path(r'~\brain_workers\FEI100_20261011')
sources=[base/f for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
sources += [sup/f for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources+=list((sup/'sources').glob('*.md'))+list((parent/'context').glob('*.txt'))
sources +=[parent/'BOARD.md',parent/'claude/B14/STREAM_NOTES.md',parent/'agents/A088/runs/20261026T201930Z-account04-A088-booleanity-referee/PROOF.md',parent/'agents/A088/runs/20261026T201930Z-account04-A088-booleanity-referee/REPORT.md',AGENT/'runs/20261023T143305Z-account03-A067-hypercontractive-refinement/REPORT.md',AGENT/'runs/20261023T143305Z-account03-A067-hypercontractive-refinement/code/check.py',AGENT/'runs/20261023T120754Z-account03-A067-hypercontractive-refinement/code/check.py']
save(R/'out/SOURCES.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'reading_scope':'protocol full; board/handoff and recent proofs full; campaign/source context targeted refreshed, earlier full reading inherited; no new paper theorem premise'} for p in sources if p.is_file()])
counts='; '.join(name+': '+str(v['checks'])+' checks PASS ('+str(round(v['runtime_seconds'],3))+'s)' for name,v in results.items())
report=f'''# exact target, quantifiers, hypotheses and units

Pay EVERY adaptive physical stopping forest below the z splice of any full-rank quadratic Boolean phase on2m bits and its k-point edit at dummy w=0, for every m>=6 and 1<=k<=2^(m-2). Fix rate4 ONCE at the original source. The SAME original remainder is >455/768. Arbitrary affine terms, marked locations and signs are allowed. Units bits. Full FEI is OPEN. Precise statement/definitions are in CLAIMS.json and PROOF.md.

# sources actually read, revisions and theorem locators

Protocol2026-10-11-execution-v2 was read in full. BOARD27Oct08:21UTC, B14 STREAM_NOTES v2, own STATUS/LEARNED, stage21 REPORT/code, stage20 arithmetic helper and A08826Oct PROOF sections1-7/REPORT were read. The new BOARD says A088 has already closed two arbitrary edits; this stage consumes that result instead of repeating it. Campaign indices, supplemental files/sources, plan and four supplied paper texts were refreshed at relevant passages and hashed in out/SOURCES.json; prior full paper reading is inherited. No paper theorem or math-store card is a new premise. Math recall gave nearby scope warnings, not this growing-k theorem. Machine rules and compute snapshot were read. Wake reports stale model/state/dream sources; excluded from mathematical evidence.

# complete derivation or exact first unsupported line

PROOF.md contains the all-dimensional argument. Integer signed-bucket orthogonality retains every W1 zero and bounds an occupied conditional ratio by2k^2. Instead of charging that ratio to all spectral mass, the proof isolates the ACTUAL W1 mass: its summed data-query charge has weight at most nkd/2. W0 and w-erased data ratios stay<4. Every edited tree has total original occupation L<=(ceil(log2k)+2)/2; its full terminal KL is<=L before clean continuation. The complete debit is <3L+1/12+(nkd/2)log2(2k^2)+(n-2)kd/2. The ACTUAL original source gives r4>=2m-4mkd+2kd-2. Quadratic clean continuation has nonpositive actual rate4 debit, with full later KL retained. Substitution gives remainder>m/2-25/12-(2m^2+2m-1)/(4*2^m)>=455/768.

Thus k grows exponentially with seed half-dimension. A naive maximum over W1 and W0 would lose another log k; Boolean masked-Parseval mass avoids it. The first unsupported universal line is a corresponding ORIGINAL source/affordable clean-exit supplier for arbitrary nonquadratic cores (or useful source-conditioned floors beyond kA<=1/4). No universal FEI theorem is claimed.

# executed validation with domain, arithmetic, commands and outputs

{counts}. Specs were frozen before each search. Main has six specified sources and207 literal adaptive states; it retains64 zero labels. Boundary checks cover the complete adaptive pruning trees at(n,k)=(8,4),(12,16), including the minimum theorem dimension m6. Independent audit exhausts all6560 nonzero signed3-bit masks under every data marginal and retained frequency, plus every nonempty3-cube marked set and EVERY physical query policy after dummy embedding via rational dynamic programming.

Commands from this run: `python -X utf8 -B code/check.py pilot`, `... main`, `... boundary`, `python -X utf8 -B code/audit.py`. Integer Walsh/Fraction physical edges and probabilities; outward rational28-term atanh logarithms with proved tail. Independent audit uses direct characters and integer bucket sums, no inherited transform. The first audit failed assertion21 because its scatter helper reversed compact/original coordinates; exact failure and repair are preserved in out/AUDIT_V1_FAILURE.json. No predicate was weakened. All final checks pass. Samples corroborate the analytic all-dimensional theorem; they do not replace it. Frozen jobs<=120MB/<60s; no GPU, detached worker or automatic dimension escalation. Formal-check status is recorded separately in out/LEAN_STATUS.json if present; no complete Lean proof of the FEI statement is claimed.

# proof dependencies and changed downstream conclusions

The growing-k theorem is self-contained from integer orthogonality, Parseval, finite entropy domination and quadratic polar rank; proof_dependencies=[] means no unreviewed campaign supplier is required. A088's parity-sector/two-edit argument reconstructs unchanged; it is context, not a missing premise. Its rank continuation is restated and derived here. New theorem is author-proved with exact checks, independent review pending. The original rate4, old D, actual J, all branches and BOTH full terminal bills remain. Post-clean KL is not capped by the pruned-tree L. No mirror, reviewer acceptance or full-FEI status changes are asserted.

# one next mathematical action and independent reviewer

A088/A070/A094 reconstruct the growing-k cancellation/occupation/payment proof. Next replace quadratic nonpositive clean debits by an ORIGINAL-source affordable admission for nonquadratic seeds, retaining all prior debits and full terminals. This tests the remaining structural assumption; another fixed edit count no longer addresses the bottleneck. H<=n alone would not pay conditional histories, so this is more than a class entropy bound.

# actual persistence receipts or precise save blocker

The four exact-field protocol files, complete proof, frozen specs, scripts and exact outputs are saved here; out/RECEIPTS.json checks schema fields, statement hash, compatibility equality, file sizes and byte hashes. A067 STATUS has two current lines; WORKLOG/LEARNED carry the result. Only A067 research files were written; administrative wake/checklist helpers were invoked as required. No git, mail, brain writes, other-agent edits or deletions. Contract-cache reconciliation is stale; no irreversible operation was attempted. Personal brain self-care remains degraded as disclosed. Supervisor adoption/copying, mirror verification and independent acceptance remain unverified. No research job is intentionally left running.

# Universal bridge

C019 stopping-tree payment and C024 history transfer advance from TWO edits to every arbitrary growing edit set k<=2^(m-2), m>=6, with EVERY adaptive physical forest paid by ONE original rate4 source and remainder>455/768. The gain is a sector-weighted cancellation bound that removes a spurious second log k while retaining all zeros, old D/J and full terminals. This does not supply a universal FEI constant: arbitrary nonquadratic clean exits and original source floors remain unpaid. NEXT attacks that precise structural dependency, the shortest remaining route toward a supplier for arbitrary Boolean cores rather than another isolated fixed-k class.
'''
write(R/'REPORT.md',report)
state='STATE: Stage22: ALL growing edit sets k<=2^(m-2),m>=6/EVERY tree paid at ONE original rate4; remainder>455/768; exact checks PASS; review pending; FEI OPEN.\nNEXT: Nonquadratic clean-exit/original-source payment with SAME old D/J and both full terminals; A088/A070/A094 review sector-weighted growing-k proof.\n'
write(AGENT/'STATUS.md',state)
lesson='\n## 2026-10-27 stage22 (20261027T082501Z-account04-A067-hypercontractive-refinement)\nConsumed A088 two-edit supplier; no duplicate fixed-k stage. NEW: ANY full-rank quadratic F2 phase on2m bits including affine terms, ANY k marked data vertices at dummy w0, m>=6,k<=2^(m-2), EVERY adaptive physical forest below z, SAME original rate4 reference/old D/J/full terminal bills: remainder>455/768. Signed-bucket orthogonality gives occupied W1 ratio<=2k^2; actual rare-sector data mass<=nkd/2 avoids applying log(2k^2) to whole occupation L<=ceil(logk)/2+1. Complete debit<3L+1/12+(nkd/2)log(2k^2)+(n-2)kd/2. Full pre-clean KL<=L; later KL not capped. Arbitrary quadratic clean forests have nonpositive actual debit. First universal gap: nonquadratic clean admission/original source floors beyond kA<=1/4. '+counts+'. Independent audit initial reversed scatter bug preserved then repaired. Independent review/full FEI remain OPEN.\n'
for name in ['WORKLOG.md','LEARNED.md']:
 p=AGENT/name
 with p.open('a',encoding='utf-8',newline='\n') as f:f.write(lesson)
receipts={'status':'PASS','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_equal':read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json'),'statement_hash_verified':True,'files':[]}
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipts['files'].append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
save(R/'out/RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED_VERIFIED','run':R.name,'claim':claim['claim_id'],'results':{n:v['checks'] for n,v in results.items()},'receipt_files':len(receipts['files'])}))
