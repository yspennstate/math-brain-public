from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];assert A==Path(r'agents\A067')
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,v):(R/n).write_text(v if isinstance(v,str) else json.dumps(v,indent=2)+'\n',encoding='utf-8')
p=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json');protocol=json.loads(p.read_text(encoding='utf-8-sig'))
prev=A/'runs/20261023T120754Z-fleet03-A067-hypercontractive-refinement'
source=Path(r'agents\A088\runs\20261023T124326Z-fleet03-A088-booleanity-referee\PROOF.md')
paths=[Path(x['path']) for x in json.loads((prev/'out/SOURCES.json').read_text())]+[source,prev/'PROOF.md',prev/'CLAIMS.json',p]
sources=[]
for x in dict.fromkeys(paths):
 if x.is_file():
  b=x.read_bytes();sources.append({'path':str(x),'sha256':sha(b),'bytes':len(b)})
write('out/SOURCES.json',sources);(R/'out/SOURCE_A088_PROOF.md').write_bytes(source.read_bytes())
pilot=json.loads((R/'out/PILOT.json').read_text());main=json.loads((R/'out/CHECK.json').read_text());assert pilot['status']==main['status']=='PASS'
statement=('For every m>=2 and every pure F2 quadratic phase b=(-1)^q on2m coordinates with full alternating polar rank, adjoin dummy w, take c=b-2*1_origin and actual G z terminals b,c. Choose rate4 once at this ORIGINAL source, with only original spectrum marginals used thereafter. The actual source has r=2I_X-H(G)>4^-m/8 and I_X=m+(2m+1)4^-m/2. Every finite adaptive physical stopping tree below the fixed original z split, including ANY data/w order on its surviving edited zero path and arbitrary clean off-path refinements, has complete actual entropy debit E_H<299/96. The SAME original remaining account r+2I_X-E_H>2m-299/96>=85/96; old D, signed terminal banks, full CE/H/KL and legacy E_2=E_4+2J remain. At the zero-path frontier only, E_Q<203/96 and full terminal KL<=1-2^-h<1. The KL cap is not asserted after arbitrary clean refinement; clean quadratic actual rate4 debits are nonpositive with full inherited KL change retained. This is a noncanonical quadratic source/continuation theorem, not full FEI or a rate3 claim.')
claim={'claim_id':'A067-OVERLAPPING-QUADRATIC-ORIGINAL-RATE4-ALL-TREES','version':1,'exact_statement':statement,'hypotheses':['Pure quadratic F2 phase, full rank2m, m>=2; origin and all incident neighbors +1','Original z split first; fixed rate4 before all subsequent physical restrictions','All outcomes and full spectra retained; reference marginalization only; adaptive choices depend only on observed history','KL cap below1 applies before clean refinements only; full later KL changes are included'],
 'statement_sha256':sha(statement.encode()),'contributors':['fleet03/A067; A088 credited for independent review and next-source challenge'],
 'proof_source':str(R/'PROOF.md'),'proof_dependencies':['A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1','A067-QUADRATIC-BELLMAN-ALL-CLEAN-REFINEMENTS@1'],
 'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A088','A070','A094','A068','B14','B20']}
write('CLAIMS.json',[claim])
nextaction='Test original conditional floor and actual source allowance for two marked edits or a nonflat seed, with fixed original rate/reference and full terminal bills; isolate cancellations before asserting a universal supplier. A088/A070/A094 review the overlapping quadratic all-tree supplier.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A067','gap_id':'G-R-MISMATCH-POSTCORE-UNUSED-CHILD-RESERVE','attempt_id':'A067-stage21-overlapping-quadratic-all-tree-rate4','method':'Original bent-law conditional envelope, one edited path reach payment, exact full terminal KL domination, quadratic clean rate4 nonpositive stopping debits','mathematical_delta':'ALL overlapping full-rank pure quadratic seeds now have their ACTUAL original supplier and EVERY descendant physical tree below z paid at ONE original rate4, remaining>85/96. Zero-path CE<203/96 and actual bill<299/96; no matching or conditional-equality hypothesis. Full FEI remains open.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ALL_DIMENSIONAL_PROOF_PENDING_REVIEW_FULL_FEI_OPEN','claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','FROZEN_SPEC.json','code/check.py','code/finish.py','out/PILOT.json','out/CHECK.json','out/SOURCES.json','out/SOURCE_A088_PROOF.md','out/RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['Independent review pending; arbitrary nonflat/higher-degree/multiple-edit supplier open','Supervisor adoption/mirrors unverified; no git performed','Brain self-care degraded: three stale personal-context sources excluded','Prior disclosed outside-tree placeholder remains untouched pending cleanup approval'],'packet_ids':['A067']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

For EVERY full-rank pure quadratic F2 phase on2m bits, m>=2, pay the actual original source and EVERY adaptive physical stopping tree below its specified z split after one origin edit with dummy w. Units are bits. This advances from matching interactions to arbitrary overlapping graphs. Rate4 is chosen ONCE at the original source; it does not preserve the earlier canonical rate3 price. Full FEI is OPEN.

# sources actually read, revisions and theorem locators

Current BOARD, B14 STREAM_NOTES v2 and own STATUS were read. A088 run20261023T124326Z PROOF sections1 and5 independently accepts the rank/clean result and names the overlapping-source gap; its matching continuation is not repeated. The primary proof is byte-snapshotted in out/SOURCE_A088_PROOF.md. Own stage20 PROOF supplies the quadratic rank/physical-query calculation; stage17 supplies the exact scalar root certificate. Campaign/protocol/paper context and earlier sources are read-only refreshed and pinned in out/SOURCES.json. No new paper theorem is asserted and no external message is sent.

# complete derivation or exact first unsupported line

PROOF.md gives the all-dimensional proof. Full quadratic rank implies every Fourier magnitude is A=2^-m. Its sign counts and marked physical first jet give EXACTLY the previously certified root histogram and influence, now proved for the actual noncanonical source. Thus r=2I_X-H(G)>4^-m/8 and the original rate4 residual is r+2I_X>2m.

The ORIGINAL Q_c law has W0 entries between d(1-A)^2 and d(1+A)^2, W1=d^2. Marginalization over any data history preserves their ratio bound, and summing w improves it. Therefore every data query has complete inherited CE drop<2. The total original reaches of all edited-path queries sum to<1, so every data ordering costs<2, without assuming each debit is negative. A w query in any position costs<d(m-1/6)<=11/96 after its actual influence is deducted. Entire source debit<203/96. All terminal KL before clean continuation is at most1-2^-h by actual spectral mixture domination. Thus complete actual debit<299/96, paid from SAME original residual, with remainder>2m-299/96>=85/96.

All off-path branches are quadratic phases, including affine terms. At rate4 EVERY actual physical query in a clean quadratic has nonpositive entropy debit. Arbitrary adaptive clean forests therefore preserve the lower margin. Their KL may grow; the earlier KL<1 cap is NOT reused. Both full CE/KL child bills and old D remain. Legacy E2=E4+2J is explicit. New rate4 at the original source is disclosed rather than hidden at a later node.

The first unsupported line for universal FEI is a source conditional floor and affordable clean admission after nonflat seeds, higher F2 degree or multiple edits cause coefficient cancellations. The all-dimensional theorem here covers the stated one-edit quadratic regime, not arbitrary Boolean functions.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes searches. Pilot: {pilot['checks']} exact checks, K4, {pilot['runtime_seconds']:.6f}s. Main: {main['checks']} exact checks, {main['runtime_seconds']:.6f}s, {main['graphs']} graphs: all28 full-rank labelled4-vertex graphs, plus explicit matching and K6 examples on6 vertices. Checked {main['subset_states']} zero-prefix subsets, {main['local_query_edges']} full local physical-query edges and {main['cyclic_prefix_frontiers']} cyclic-order prefix frontiers. Cyclic orders are not claimed exhaustive; the all-order/all-tree statement follows analytically. Every inherited full CE/H/KL bill and original J is rebuilt from actual Boolean truth tables. A K4 changed-profile guard has unequal source/actual conditionals and still paid rate4 debit. A flat phase with an added linear term violates the marked-jet influence formula, guarding the exact source hypothesis. All PASS.

Commands: python -X utf8 -B code/check.py pilot, then full, from this run. Immutable named arithmetic helpers from stage20 are extracted with AST; the previous search is never executed. Arithmetic uses integer Walsh/GF2 rank, exact Fraction probabilities/edges and28-term positive atanh log bounds with explicit rational tail. Floats display only. The root histogram and finite source ledger are checked by distinct physical-edge and Fourier computations; new independent human review remains pending. Memory estimate120MB; no >300MB job, GPU, detached process or automatic dimension escalation. No Lean certificate claimed. All-m proof is analytic.

# proof dependencies and changed downstream conclusions

The independently accepted stage17 root scalar certificate extends by equal ACTUAL histograms and energies; no reserve is borrowed from another function. Stage20's general quadratic clean calculation is independently accepted by A088. New noncanonical source/continuation theorem awaits A088/A070/A094 review. The stated margin changes from earlier rate3 matching margins because this stage starts a different, disclosed rate4 experiment covering overlapping cores and every subsequent order/tree. No full FEI status changes.

# one next mathematical action and independent reviewer

{nextaction}

# actual persistence receipts or precise save blocker

Four protocol files, proof, frozen spec, code and exact outputs are saved in this A067 run. STATUS has exactly two lines; WORKLOG and LEARNED are updated. Required field sets, claim digest, compatibility equality and file-size/SHA256 receipts are checked below. Shared source trees and other agents' outputs remain untouched; private supervisor adoption/mirrors are unverified. The prior disclosed outside-tree placeholder remains untouched. Brain self-care is degraded/unverified: owner model, state of mind and latest dream are stale and excluded from mathematics. No stage computation is intentionally left running.

# Universal bridge

C019 stopping-tree payment and C024 full history transfer now have an ACTUAL supplier for every overlapping full-rank pure quadratic origin-edit source, with every descendant physical tree below z paid at ONE original rate4 and remaining>85/96. The original-law conditional envelope replaces matching-specific phase equality; full terminal KL and old invoices remain. What remains is a comparable floor/source supplier when flatness or the one-edit structure fails. Testing two genuine edits or a nonflat seed directly challenges that universal supplier, rather than another isolated H/I class estimate; full FEI remains OPEN.
'''
write('REPORT.md',report)
(A/'STATUS.md').write_text('STATE: Stage21: ALL overlapping full-rank quadratic one-edit sources/EVERY tree below z PAID at ONE original rate4; remainder>85/96; exact checks PASS; review pending; FEI OPEN.\nNEXT: Nonflat or two-edit original source floor/payment with SAME old D/J, reference and full KL; A088/A070/A094 review rate4 all-tree supplier.\n',encoding='utf-8')
entry=f'\n## 2026-10-23 stage21, fleet03 ({R.name})\nConsumed A088 rank acceptance/overlapping-source challenge. NEW actual source scalar certificate extends to every pure full-rank quadratic phase by identical flat sign histogram and physical marked jet. Original rate4 fixed once. Any data/w zero-path order has E_Q<203/96 and full pre-clean KL<1, so E_H<299/96; arbitrary clean quadratic forests add nonpositive actual debit. SAME original remainder>2m-299/96>=85/96. Old D/full bills and E2=E4+2J retained; no post-clean KL cap claimed. Main{main["checks"]} exact checks PASS on30 graphs,1152 subsets,3136 edges,952 cyclic prefix frontiers. General all-tree claim analytic, independent review pending. Full FEI OPEN. NEXT nonflat/two-edit cancellations in original conditional floor. Brain self-care degraded and excluded; old outside-tree placeholder untouched.\n'
for f in ['WORKLOG.md','LEARNED.md']:
 with (A/f).open('a',encoding='utf-8') as h:h.write(entry)
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']};assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert all('# '+x in report for x in protocol['required_per_run']['report_fields']);assert json.loads((R/'PACKET_DELTA.json').read_text())==progress
art=[]
for x in sorted(R.rglob('*')):
 if x.is_file() and x.name!='RECEIPTS.json':
  b=x.read_bytes();assert len(b)<20_000_000;art.append({'path':str(x.relative_to(R)),'sha256':sha(b),'bytes':len(b)})
write('out/RECEIPTS.json',{'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifacts':art,'independent_review':'PENDING','mirrors':'UNVERIFIED'})
assert all(sha((R/x['path']).read_bytes())==x['sha256'] for x in art)
print(json.dumps({'status':'PASS','main_checks':main['checks'],'artifacts':len(art),'claim_sha256':claim['statement_sha256'],'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
