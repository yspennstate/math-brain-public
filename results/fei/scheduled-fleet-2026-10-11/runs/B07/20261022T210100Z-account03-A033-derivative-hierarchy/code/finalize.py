from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]; O=R.parents[1]
T=O.parents[1]; NOW=datetime.now(timezone.utc).isoformat()
def write(p,s): p.write_text(s,encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
check=json.loads((R/'out/interleaving.json').read_text(encoding='utf-8'))
boundary=json.loads((R/'out/tag_boundary.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and check['cases_completed']==1280 and boundary['status']=='PASS'
assert sha(R/'code/interleaving.py')==check['source_sha256']
formal=(R/'out/lean_status.txt').read_text(encoding='utf-8-sig') if (R/'out/lean_status.txt').exists() else 'NOT_EXECUTED'
# A successful compiler exit by itself is NOT a theorem certificate.
formal_description='Formal verification is not asserted; inspect out/lean_status.txt and out/lean_output.txt for the exact admission/runtime receipt. The proved rung claimed here is the paper derivation with exact finite validation.'
sources=[T/'BOARD.md',T/'claude/B07/STREAM_NOTES.md',O/'LEARNED.md']
for agent,slot in [('A079','20261021T153136Z-account03-A079-correlated-auxiliaries'),('A032','20261021T215120Z-account03-A032-boolean-phase-realizability')]:
 for name in ['REPORT.md','PROOF.md','CLAIMS.json']:
  sources.append(T/'agents'/agent/'runs'/slot/name)
sources += [T/'agents/A034/LEARNED.md',T/'agents/A079/LEARNED.md',T/'agents/A032/LEARNED.md']
source_receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources if p.exists()]
dump(R/'out/dependency_receipts.json',source_receipts)
used=[]
for p in sources:
 if p.name=='CLAIMS.json' and p.exists():
  rows=json.loads(p.read_text(encoding='utf-8'))
  if isinstance(rows,list):
   used.extend({'claim_id':x.get('claim_id'),'version':x.get('version'),'statement_sha256':x.get('statement_sha256'),'use':'source-bound application/background; main separation theorem self-contained'} for x in rows)
statement=('For every C>=0, every pair of ternary controller functions A,B with AB=0 and A^2+B^2=1 pointwise, every Boolean seed h on an independent uniform cube, and a balancing physical bit ell protected from queries, put F=A+B ell h and beta=E B^2. The maximum stopped sum of reach*(Delta H-C Inf) over all adaptive interleavings of any fixed allowed controller subset and the seed coordinates is exactly U_C(A+B ell)+beta V_C(h), where U and V are the corresponding controller-only and seed-only optimal stopping costs. Every complete terminal spectrum and physical influence is retained. The identity holds at every partial controller/seed restriction, including beta=0 and 1. Querying ell is excluded essentially: A=(1+c)/2,B=(1-c)/2 has tag entropy drop 2 for h=1 and 0 for h=y, both with tag influence 1/2. This is a route-separation identity, also valid for normalized real seed amplitudes, not a new Booleanity-specific FEI inequality.')
claim={'claim_id':'A033-PROTECTED-TAG-INTERLEAVING-SEPARATION','version':1,'exact_statement':statement,'hypotheses':['Independent uniform physical controller, tag and seed inputs','AB=0 and A^2+B^2=1 pointwise; A,B ternary','Tag ell is not queried; fixed allowed controller subset; finite coordinate stopping trees','Normalized squared Fourier entropy in bits; original physical influence; C>=0'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A033'],'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'certificates':['out/interleaving.json','out/tag_boundary.json']},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A032','A079','A088','A094','B07','B20','A096','A097']}
dump(R/'CLAIMS.json',[claim])
next_action='Expose the protected balancing tag once after an inherited mixed controller/seed history; price empty-frequency interference in BOTH complete spectra A_s +/- B_s h_t using the SAME unused structural/seed reserve and a specified incoming reference. A088/A094 independently reconstruct separation and beta conservation; A032/A079 review the source specialization.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B07','packet_id':'A033','gap_id':'G-BOOLEANITY','attempt_id':'A033-PROTECTED-TAG-INTERLEAVING-1','method':'Consume all-product closure and arbitrary-seed completion; full signed hierarchy; disjoint Fourier tag sectors; exact Bellman factorization and protected-tag boundary countertest','mathematical_delta':'All protected-tag controller/seed interleavings have EXACT cost U_C+beta V_C. For the A032 fixed mask at C=4 this is 1-(9/16)log2(3)+(3/8)V_4(h). No extra adaptive discount and no renewed structural bank; unpaid arbitrary seed cost remains. New universal FEI payment gained: zero.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ROUTE_OBSTRUCTION_PROOF; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':used,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['PROOF.md','FROZEN_SPEC.json','FROZEN_BOUNDARY_FORMAL.json','code/interleaving.py','code/boundary.py','out/interleaving.json','out/tag_boundary.json','out/source_read_manifest.json','out/dependency_receipts.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Fixed cyclic atom-cap original construction/checker still absent locally; source import is summary-only','No prescribed inherited nonflat reference supplied; Shannon cancellation is not a reference-reset theorem','Formal status: '+formal.strip()],'packet_ids':['A033']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. For every finite independent uniform controller/seed cube, every exact ternary disjoint mask A,B with AB=0,A^2+B^2=1, every Boolean seed h and every C>=0, F=A+B ell h has optimal stopped signed query cost exactly U_C+beta V_C(h), beta=E B^2, for ALL adaptive controller/seed interleavings that protect ell. Entropy is in bits, influence is on original physical coordinates, and every stopping cut retains both complete terminal spectra. This is an exact route obstruction and conditional transport result, not a new Booleanity inequality or unrestricted reference-reset theorem.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (2026-10-11-execution-v2), machine AGENTS, current BOARD snapshot 2026-10-22 20:55 UTC, B07 lead notes v2, own rolling files and substantive 20261014T051927Z proof. Read campaign README/CURRENT_STATUS and relevant claim/obstruction/packet/next-action/plan entries, supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING, and source route-map section3 and one-bit norm lemma. Scanned current/earlier paper text versions at scope/composition locators, particularly threshold38pp Proposition8.6; no full-paper audit or new paper theorem dependency is claimed. Text exports require cp1252, explicitly detected after a strict UTF8 failure. out/source_read_manifest.json records encodings, hashes and located lines.

Consumed A034's all-product closure as reported in its LEARNED and independently reconstructed in A079 LEARNED; therefore retired A033's stale bounded-nonfair next step. Read A079 run20261021T153136Z REPORT/PROOF, and A032 run20261021T215120Z REPORT/PROOF and source claim records. They supply the fixed-mask arbitrary-seed completion and paid controller histories. Main theorem (*) is reconstructed without relying on their finite census. Source receipts are in out/dependency_receipts.json. Recent empty/marker run directories were not treated as results. The current owner campaign endpoint is 2026-10-23 14:49 UTC, overriding the historical protocol endpoint; no new schedules or workers were created.

# complete derivation or exact first unsupported line

PROOF.md states the complete convolution, split-pair, derivative and granularity hierarchy. The fixed-order G_(K,w) no-go is imported at the curated source's precise scope. The distinct cyclic fixed-cap family remains summary-only because its original construction/checker is absent locally; this stage does not manufacture an exact definition. Neither fixed prefixes, dyadic coefficients nor small defects are proposed as a new admission condition.

The balancing tag makes the A and B*h frequency sectors disjoint. This proves H(F_s,t)=H(G_s)+beta_s H(h_t) and I(F_s,t)=I(G_s)+beta_s I(h_t) at EVERY partial controller/seed state. Controller debts are seed-independent; seed debts equal beta_s times the seed debt; beta is conserved across controller children. Bellman induction bounds every interleaving by U_C+beta V_C. An optimal controller tree followed at each leaf by an optimal seed tree attains equality. Nonnegative beta and the beta=0 boundary are explicit, and no infinite optional-stopping limit is used.

Source specialization: A032's original rate4 reserve1/8 covers controller cost delta=1-(9/16)log2(3). Arbitrary interleaved seed queries extend this cost EXACTLY to delta+(3/8)V_4(h), without renewing either bank or dropping a seed terminal. The whole signed hierarchy is preserved because F^2-1=B^2(h^2-1); beta>0 makes Booleanity equivalent to seed Booleanity. The separation equality also holds for normalized non-Boolean amplitudes, so it is explicitly NOT offered as the additional Booleanity consequence demanded by B07's inequality test.

The first unsupported universal line is payment of the surviving arbitrary seed stopping/reference debt. On querying ell, children A_s +/- B_s h_t have interfering empty seed-frequency coefficients; the protected-sector proof ends there. Actual Boolean seeds1 and y already give different tag entropy drops2 and0 at identical tag influence1/2, so extending seed-independent controller accounting to the tag is false.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the search. Command: python -X utf8 runs/{R.name}/code/interleaving.py from A033. All16 one-control masks times all16 two-bit seeds, plus all256 two-control masks times all4 one-bit seeds:1280 actual Boolean constructions, no symmetry, both rates2 and4. Direct physical restriction/edge-count Bellman DP is compared with separate controller/seed DP. Integer Walsh transforms and dyadic prime-log signatures are exact; every comparison uses rational40-term atanh intervals with a proved positive tail. PASS:{check['exact_assertions']} assertions,{check['Bellman_states']} cached Bellman states,{check['positive_local_options']} positive local options,{check['comparisons_certified']} distinct exact comparisons,{check['seconds']:.6f}s observed compute. No floating signs establish a claim. All cases finished within the frozen55s limit; estimate45MB, no automatic dimension increase.

FROZEN_BOUNDARY_FORMAL.json precedes the separate two-case tag check. Command: python -X utf8 runs/{R.name}/code/boundary.py. PASS: complete three-bit truth tables, direct character sums, rational power-of-two entropies, both tag children and physical tag influence; output out/tag_boundary.json. This tests the substantive tag-protection side condition rather than repeating the search.

A small core Lean theorem for signed integer controller Bellman bookkeeping is submitted through the installed lean_check.py with a pinned source hash, named target, explicit artifact directory under A033, fresh memok admission and20s timeout. Actual wrapper status: {formal.strip()}. {formal_description} Finite exact validation supports the proof; independent mathematical review is pending.

No >300MB computation, GPU, git, mail, background producer, remote publication, or research write outside A033 was used. Latest compute snapshot read in this session showed about2.4GB free RAM,95.7% live commit and7.8GB disk free; its top groups were Claude/Python/ffmpeg and the owner terminal. These are timestamped readings, not a new live census. Existing work was left running; no load was shed. The interventions ledger was inspected read-only. Wake warned that owner-model and state-of-mind notes were stale; disclosed and not relied upon for authorization.

# proof dependencies and changed downstream conclusions

The all-product case is already closed by A034/A079 at its stated scope; a bounded nonfair extension would duplicate it. New claim A033-PROTECTED-TAG-INTERLEAVING-SEPARATION@1 is self-contained. The displayed A032 numerical specialization is conditional on its source certificate, credited without claiming to have rerun238145 trees. This extends controller-only cancellation to all protected-tag interleavings and removes that proposed source of an extra seed discount. It pays ZERO new universal entropy and is not FEI or a counterfamily. C018/C019/C024 remain OPEN. No registry, mirror or independent-review acceptance is asserted.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, frozen specifications, exact checker outputs and source/statement hashes are locally saved. STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md carry the new result and superseded frontier. out/PERSISTENCE_RECEIPT.json verifies keys, hashes, sizes, check statuses and identical progress/delta. All files are under20MB. Local persistence only is verified; supervisor publication and independent review remain pending. Finalized {NOW}.

# Universal bridge

This stage moves B07's full-Booleanity/nonproduct transport target toward C019 and C024 by proving the exact all-interleaving price U_C+beta V_C, consuming A032/A079's new fixed-mask seed dependency instead of reopening the solved product class. The gain is an exact obstruction to extra payment from protected-tag adaptivity; universal FEI payment gained is zero. The seed stopping/reference term and the first actual tag-induced spectral collision remain unpaid. NEXT exposes that precise collision with both full terminals and one unchanged incoming reserve, the shortest continuation because all protected-tag interleavings are now accounted for and cannot hide the missing payment.
'''
write(R/'REPORT.md',report)
write(O/'STATUS.md','STATE: Exact protected-tag interleaving price U+beta V proved;1280 Boolean cases/11466 assertions PASS; no extra seed discount; full FEI OPEN, review pending.\nNEXT: A032/A079/A088/A094 review; expose balancing tag once with BOTH A_s +/- B_s h terminals, original reference and SAME unused seed/structural reserve.\n')
with (O/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write(f'\n{NOW} - Stage {R.name}: consumed A034 all-product closure and A032/A079 fixed-mask arbitrary-seed/controller payment. Changed to protected-tag interleaving mechanism. Derived exact optimal stopping factorization U_C+beta V_C for all partial states/all adaptive interleavings; 1280 frozen Boolean constructions,11466 assertions PASS; separate2-case tag interference guard PASS. No new universal payment. Formal status: {formal.strip()}. Source encoding failure and two nonmutating patch-context failures were repaired; exact checker itself passed first run. Current-source/remote review not asserted.\n')
with (O/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write(f'''\n{NOW} - The old at-most-two-nonfair frontier is superseded by A034 all-product closure as independently reconstructed in A079 LEARNED; do not re-enumerate norm25. For disjoint ternary A,B with A^2+B^2=1 and independent Boolean seed h, F=A+B ell h has H=H(A+B ell)+beta H(h), I=I(A+B ell)+beta I(h), beta=E B^2 at every controller/seed restriction while ell is protected. ALL adaptive interleavings have EXACT stopped signed cost U_C+beta V_C; proof is Bellman upper bound plus controller-first/seed-second attainment. A032 fixed-mask specialization at4 is delta+(3/8)V_4(h), delta=1-(9/16)log2(3); original1/8 reserve cannot silently pay arbitrary seed cost. Exact1280-case certificate PASS. This identity is also generic for normalized real amplitudes, so it is a route obstruction, NOT a new Booleanity inequality. Complete Booleanity is inherited exactly through F^2-1=B^2(h^2-1); equivalence requires beta>0. Tag protection is essential: A=(1+c)/2,B=(1-c)/2 has tag drop2 for seed1 and0 for seed y, same influence1/2. After tag query retain both interfering full spectra A+Bh,A-Bh and SAME incoming reference/reserve.\n''')
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
p=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in p['progress_fields']}
assert set(claim)==set(p['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((O/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(len(q.read_bytes())<20*1024*1024 for q in R.rglob('*') if q.is_file())
receipt={'finalized_at':NOW,'protocol_keys':'PASS','statement_sha256':'PASS','progress_delta_identical':True,'validation':check,'boundary_status':boundary['status'],'formal_status':formal.strip(),'local_only':True,'artifacts':[{'path':str(q.relative_to(R)),'sha256':sha(q),'bytes':q.stat().st_size} for q in R.rglob('*') if q.is_file() and q.name!='PERSISTENCE_RECEIPT.json']}
dump(R/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'saved':str(R),'claim':claim['claim_id'],'exact_assertions':check['exact_assertions'],'formal_status':formal.strip(),'schema':'PASS','files':len(receipt['artifacts'])}))
