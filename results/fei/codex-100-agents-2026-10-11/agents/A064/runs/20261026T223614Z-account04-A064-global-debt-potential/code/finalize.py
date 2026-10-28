"""Persist protocol artifacts only after exact checks pass; verify readback."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
BASE=Path(r'math-open-problems/reports\fei-2026-10-11')
PEER=Path(r'agents\A087\runs\20261023T143823Z-account03-A087-restriction-referee')
def read(p): return p.read_text(encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
main=json.loads(read(R/'out'/'MAIN.json'))
audit=json.loads(read(R/'out'/'AUDIT.json'))
assert main['status']==audit['status']=='PASS'
protocol=json.loads(read(BASE/'EXECUTION_PROTOCOL.json'))
peerclaims=json.loads(read(PEER/'CLAIMS.json'))
source=next(x for x in peerclaims if x['claim_id']=='A087-FULL-TERMINAL-ANY-REFERENCE-PRODUCT-STOP-LOWER-BOUND')
assert source['statement_sha256']==hashlib.sha256(source['exact_statement'].encode()).hexdigest()
assert source['proof_source']['sha256']==sha(Path(source['proof_source']['path']))
source['review_records'].append({'reviewer':'A064/account04','verdict':'HOLDS','scope':'Independent full-terminal argument: every reset terminal CE=M=N*m*h2(d), retain -d log2 d; integer direct-character point checks m2..8. GU theorem not part of this acceptance.','proof_source':str(R/'PROOF.md'),'validation':str(R/'out'/'AUDIT.json')})
source['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE'
statement=('Let g be ANY finite uniform-cube Boolean core, H its spectral entropy, and F(u,v,y)=g(y) for v=0 and (-1)^u*g(y) for v=1. Start with the actual spectral reference Q=P_F, whose full initial CE is H+2. Declare a finite fair physical-dummy lottery that installs actual product references once, with nonnegative terminal KL cost L (for disjoint data blocks any correlated subset selection has L=sum selected TC_j). No data coordinate is queried. All adapted stopping cuts retain actual entropy and KL, including immediate root stopping and cuts on both sides of v and reset. If the lottery is physically revealed AFTER protected query v, the exact least total initial full-CE account is H+max(2,E L); if revealed BEFORE v it is H+2+E[(L-2)_+]. Their difference is E[(L-2)_+]-(E L-2)_+>=0. All actual query prediction-KL charges are zero. Explicit harmonic potentials in PROOF sections2-3 dominate actual current CE at every node; the complete terminal separately retains entropy H and expected KL E L. From a SAME original supplied account S with old consumption omega, funding requires S-omega at least the stated minimum; no influence-price for arbitrary H is assumed. For a single-core reset event epsilon with T=TC(g)>2, extra reserves are epsilon(T-2) before and (epsilon*T-2)_+ after. A genuine 64-fold disjoint point3 tensor with epsilon=1/8 has before extra in(11/8,3/2) and after extra0. Full FEI remains OPEN.')
claim={'claim_id':'A064-SELECTED-RESET-ENTROPY-RELEASE-ORDER','version':1,
 'exact_statement':statement,'hypotheses':['All cubes and fair physical dummy trees finite; bits; no limit or independence of reset events used.','Initial reference is actual source spectrum and full initial entropy H+2 is explicitly paid. No unknown entropy is treated as zero-cost capital.','No data queries and only one declared installation. Tensor option requires disjoint physical blocks; all source-zero product mass retained.','Actual adapted stopping cuts include before/after release, lottery and reset. An outcome or an arbitrary core is never presumed FEI-certified.'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A064/account04; A087 full-terminal obstruction reviewed as motivation'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':[str(R/'out'/'MAIN.json'),str(R/'out'/'AUDIT.json')]},
 'proof_dependencies':[],'review_records':[{'reviewer':'A064','verdict':'AUTHOR_PROOF_AND_EXACT_CHECKS; EXTERNAL REVIEW PENDING; NOT LEAN-CHECKED','scope':'Explicit full-CE potentials, adapted-cut lower bounds, exact Fourier pivot, direct-character reproduction and independent cut enumeration.'}],
 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['UNREGISTERED: identical complete terminal reference laws imply identical least all-cut full-CE initial capital regardless of physical order of information'],
 'first_unproved_line':None,'next_consumers':['A061','A065','A087','A094','B20']}
claims=[source,claim]
for x in claims: assert set(x)==set(protocol['required_per_run']['claim_fields'])
put(R/'CLAIMS.json',claims)
prior=R.parent/'20261023T130211Z-account03-A064-global-debt-potential'/'PROGRESS.json'
priorj=json.loads(read(prior))
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B13','packet_id':'A064',
 'gap_id':priorj['gap_id'],'attempt_id':'A064-selected-reset-order-v1','method':'Consume A087 full-terminal refinement; use actual protected-query entropy release BEFORE revealing a selected reset lottery; exact minimal full-CE potentials and adapted-cut audit.',
 'mathematical_delta':'A087 refinement independently HOLDS. Selected reset capital after revelation order is H+max(2,E L), before is H+2+E[(L-2)+]. Strict actual Boolean example saves >11/8 bits. Every full H/KL terminal and old consumption retained. Arbitrary-core initial entropy supplier remains unpaid.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'LOCAL_THEOREM_AUTHOR_PROVED_EXACT_CHECKED; A087_REFINEMENT_INDEPENDENTLY_HOLDS; FULL_FEI_OPEN',
 'claim_versions_used':['A087-FULL-TERMINAL-ANY-REFERENCE-PRODUCT-STOP-LOWER-BOUND@1'],
 'claims_created_or_changed':[source['claim_id']+'@1',claim['claim_id']+'@1'],
 'source_artifacts':[str(PEER/'PROOF.md'),str(PEER/'CLAIMS.json'),str(prior),str(R/'PROOF.md'),str(R/'out'/'MAIN.json'),str(R/'out'/'AUDIT.json')],
 'next_consumers':['A061','A065','A087','A094','B20'],
 'next_action':'A087/A094 reconstruct exact information-order premium; extend entropy-release-before-choice to useful ordinary data queries with ACTUAL inherited references, paying initial full entropy from SAME unused original influence. Do not widen ALL-product-stop class.',
 'stagnant_substantive_attempts':0,'blockers':['No universal influence-priced initial entropy/reference supplier for arbitrary indecomposable core.','Mathlib admission held: memok exit1, physical free3.9GB<4GB. No Lean result claimed.','Supervisor publication, external review and mirror adoption unverified.'],
 'packet_ids':['A064']}
expected=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(expected)
put(R/'PROGRESS.json',progress); put(R/'PACKET_DELTA.json',progress)
pins=[]
for p in [BASE/'EXECUTION_PROTOCOL.json',PEER/'PROOF.md',PEER/'CLAIMS.json',Path(r'BOARD.md'),Path(r'claude\B13\STREAM_NOTES.md'),prior]:
    pins.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
put(R/'out'/'SOURCE_PINS.json',pins)
report=f'''# A064 selected reset policy: information order has an exact price

## exact target, quantifiers, hypotheses and units

For ANY Boolean core, construct a full cross-entropy potential for ONE selected finite dummy-lottery reset policy, allowing rare branch growth and all adapted stopping cuts. Bits; fair physical cube; no data queries; initial reference is actual spectrum and its entropy is explicitly booked. PROOF.md sections1--3 gives the exact theorem, initial account and every boundary. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD, B13 lead v2, own STATUS/LEARNED and preceding A064 REPORT/PROOF; entire execution protocol2026-10-11-execution-v2; current status/README and claim/obstruction registries; B13 stream dispatch and packet baseline; relevant plan/campaign/claims/counterexample/seed/mapping locators rechecked. A087 run20261023T143823Z PROOF sections4--6 and exact CLAIMS payload were read and independently reconstructed. Source statement and proof hashes matched. Required papers and earlier source intake remain the prior completed baseline; no paper theorem is a new premise. The new proof is self-contained from Fourier definitions. Math recall returned standard stopping leads, used as orientation only; no unread memory result is a proof premise. Source byte pins are in out/SOURCE_PINS.json.

## complete derivation or exact first unsupported line

Protected v releases EXACTLY2 bits of full spectral entropy at zero prediction-KL and erased-KL cost. A selected reset costs nonnegative L. Reveal its fair physical-dummy lottery AFTER v: least full initial capital H+max(2,E L). Reveal the SAME lottery BEFORE v: least capital H+2+E[(L-2)_+]. Explicit harmonic potentials dominate actual current H+KL at every node; adapted stopping cuts attain both lower bounds. All full terminal entropy H and expected KL E L remain. Correlated subset choices across disjoint blocks need no independence. A 64-fold point3 tensor at epsilon1/8 has extra reserve0 after, but between11/8 and3/2 before. Each rare success path can grow its conditional potential. This is a selected physically implementable rule, rather than an account for all product cuts.

A087 full-terminal any-reference obstruction independently HOLDS unchanged: account/I>=m(m-1)/(m+1) because both actual product terminals cost exactly M. Accept only that refinement here, not the source GU chain. For the explicitly paid tensor point family, S=5I(F) with old omega<=I(F) funds the selected after-order rule when epsilon*TC<=2. For an arbitrary core the first unsupported universal line remains S-omega>=H(g)+max(2,E L) from an influence-priced original supplier. Q=P eliminates KL, not entropy; the theorem does not solve this initial price.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede execution. Primary: ALL278 Boolean truth tables n0..3, integer FWHT, independent physical edges, full product reference normalization/support/KL, actual protected pivot and zero-source rows; eight finite lotteries per core plus declared disjoint tensor costs. PASS {main['checks']} assertions in {main['seconds']}s. This includes ALL65536 nonnegative depth3 leaf-cost vectors in{{0,1,2,3}}; {main['algebra_strict']} have a strict ordering premium. Algebra vectors are a finite check of the recursion, not invented Boolean functions.

Independent audit: direct character sums for ALL278 small cores, all26 cuts for each of6561 vectors in{{0,1,3}}, point dimensions2..8, and exact analytic tensor fixture. PASS {audit['checks']} assertions in {audit['seconds']}s. Independent Fourier/cut implementations share the explicitly disclosed rational logarithm primitive. The all-dimensional result follows the written proof, not extrapolation. Tensor194 physical bits are NEVER expanded. Primary exact total={main['checks']+audit['checks']}; pilot510 separate. Arithmetic is integer/Fraction, symbolic prime logs and rigorous outward atanh intervals. Commands: python -B -X utf8 code/check.py pilot; code/check.py; code/audit.py from run directory. Estimates45MB, no heavy job. memok exit1 (3.9GB physical free below4GB) held Mathlib; no Lean process or Lean-check claim. A syntax parenthesis and unused audit expression were repaired BEFORE the corresponding first execution; no failed mathematical certificate or changed search domain. The theorem reached written PROOF plus exact checks, external review pending.

## proof dependencies and changed downstream conclusions

New A064-SELECTED-RESET-ENTROPY-RELEASE-ORDER@1 is self-contained. A087-FULL-TERMINAL-ANY-REFERENCE-PRODUCT-STOP-LOWER-BOUND@1 receives an independent HOLDS record with source unchanged. The result separates selected reset policy price from impossible universal all-product-stop price, and shows why checking only final laws misses an ordering premium. Previous all-prefix KL theorem is not revoked; full CE can consume actual entropy release under this different explicit floor. There is no arbitrary data-query continuation or second reset theorem here.

## one next mathematical action and independent reviewer

A087/A094 should reconstruct the two minimality cuts and source Fourier calculation. Next mathematical action: extend entropy-release-before-choice to a useful ordinary DATA query with its actual inherited reference and an actual initial supplier, retaining BOTH full child entropies and all old bills. An arbitrary-core O(I) initial entropy source is still the universal bottleneck. Another dummy lottery or point dimension does not address it.

## actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specs, code and exact outputs saved under this A064 run. Source hashes, exact schemas, statement hashes, compatibility bytes and sizes are checked on readback by code/finalize.py; out/MANIFEST.json pins run bytes. STATUS is two lines; WORKLOG and LEARNED updated. External adoption/publication unverified. No git, mail, other-agent writes, brain writes, trading access, deletion or detached worker. Wake disclosed stale personal model/state/dream and excluded them from mathematical authority. No research process remains running after bounded verification.

Universal bridge: C019 stopping-tree payment and C024 history transfer advance by an exact selected-policy full-CE order theorem: moving the SAME reset lottery after a paid two-bit entropy release changes extra reserve from E[(L-2)_+] to (E L-2)_+, with a strict actual Boolean saving>11/8 and all adapted cuts/full terminals retained. This consumes A087's all-product-stop objection without repeating that impossible target. What remains is to obtain usable entropy release and ORIGINAL full-entropy/reference funding for arbitrary indecomposable cores from the SAME unused influence account. NEXT addresses actual data-query inheritance and initial payment, the shortest route to the universal gap; another finite lottery class would leave it unchanged.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: Selected-reset full-CE order theorem proved/exactly checked; A087 full-terminal obstruction independently HOLDS; AFTER extra(E L-2)+ vs BEFORE E(L-2)+; FEI OPEN.\nNEXT: A087/A094 review minimality cuts; extend paid entropy-release-before-choice to actual DATA queries/inherited references and fund arbitrary-core INITIAL full entropy from SAME unused original influence.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {R.name}: reviewed A087 full-terminal refinement HOLDS; proved selected-lottery order theorem with exact minimal all-cut full-CE capital; {main["checks"]}+{audit["checks"]} exact checks PASS. Extra before>11/8 vs after0 on actual tensor. memok held Lean; no heavy job. Universal arbitrary-core initial entropy price unpaid.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA protected fresh bent mask on ANY core has H(F)=H(g)+2,I(F)=I(g)+1; query v releases2 entropy bits with zero outcome/erased KL under Q=P_F. For ONE selected finite fair physical-dummy reset lottery of nonnegative KL cost L, no data queries, exact minimal FULL-CE capital is H(g)+max(2,E L) if lottery AFTER v, but H(g)+2+E[(L-2)+] if BEFORE v. Identical final laws do not determine all-cut price. Potentials H+conditional E L and H+2+conditional E(L-2)+ give all-cut control and rare growth. Full terminal H remains. 64 disjoint point3 factors, epsilon1/8: after extra0, before63/4-9log2(3) in(11/8,3/2). Actual-root Q=P is not a universal influence-priced entropy supplier; no ordinary data-query continuation or repeated reset is established. A087 full-terminal any-reference bound m(m-1)/(m+1) independently HOLDS.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for section in protocol['required_per_run']['report_fields']: assert '## '+section in report
assert len(read(A/'STATUS.md').splitlines())==2
for x in json.loads(read(R/'CLAIMS.json')):
    assert hashlib.sha256(x['exact_statement'].encode()).hexdigest()==x['statement_sha256']
files=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='MANIFEST.json':
        assert p.stat().st_size<20_000_000
        files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
put(R/'out'/'MANIFEST.json',{'run_id':R.name,'files':files})
assert len(json.loads(read(R/'out'/'MANIFEST.json'))['files'])==len(files)
print(json.dumps({'status':'PASS','protocol_schemas':'exact','compatibility_bytes':'identical','statement_hashes':'matched','source_hashes':'matched','files':len(files),'primary_exact_checks':main['checks']+audit['checks']}))
