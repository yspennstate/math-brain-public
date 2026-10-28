from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];HOME=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
main=read(R/'out/MAIN.json');act=read(R/'out/ACTIVATION_MAIN.json');audit=read(R/'out/AUDIT.json')
assert all(x['status']=='PASS' for x in [main,act,audit])
formal=read(R/'out/FORMAL.json')
assert formal['returncode']==2 # observed timeout; never relabel as formal certification
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
statement=('For every m>=2, 1<=r<=m, put d_s=2^(1-s), N=2^(m-1), g_m the disjoint product of N actual point_m signs, and K_r=r*h2(d_r)/d_r. Declare a fair physical policy that queries any adaptive order of live block coordinates until each block dies or reaches r variables, then installs its actual marginal-product reference and freezes that block. Start at the exact actual spectral reference and admit every global adapted stopping cut. The nonnegative full-CE potential is the sum over active blocks of V_s=max(H(point_s),2^(r-s)*M(point_r)), zero on dead blocks and M(point_r) on frozen blocks. Every actual query outcome KL is zero. It is a supermartingale, and adding its predictable drops gives a martingale. The exact least ORIGINAL full-CE capital is max(H(g_m),K_r), or max(H(g_m)+2,K_r) after a first protected-v query in the bent-masked source. For t>=1 controls and Z=1+all_zero_controls*(g_m-1), query controls first then the same policy: Z has full Fourier support and is physically tensor indecomposable, I(Z)=2^(-t)*(m+t*(1-Eg_m)), H(Z)<=7I(Z), and the exact least capital is max(H(Z),2^(-t)*K_r). All old debits and both complete terminal H and KL remain paid. For r<=floor(sqrt(m)), ONE supplied ORIGINAL 8I(Z) account with old consumption at most I(Z) pays every cut, all control/data queries and actual product installations. Since r(r-1)<=K_r<r*(r+1/2), for t<=beta*m with fixed finite beta these policies have O(I) capital if and only if r=O(sqrt(m)). This is a selected policy theorem, not arbitrary-core source funding or a proof of full FEI.')
new={
 'claim_id':'A061-DEEP-SELECTED-DATA-RESET-SHARP-SQRT-BOUNDARY','version':1,
 'exact_statement':statement,
 'hypotheses':['Finite uniform physical cubes and fair predictable query trees; bits. All reference-only atoms retained. No unbounded stopping or exchanged limit.',
 'Literal disjoint point factors inside g_m; active factors retain exact source reference. Only r-boundary factors may reset, and frozen factors are not queried. The activated complete root is physically prime; no affine primeness is claimed.',
 'The same original account retains previously consumed omega. The rate8 corollary assumes omega<=I(Z), r<=floor(sqrt(m)); it does not renew any influence owner.',
 'The iff asymptotic statement assumes t<=beta*m. For unbounded t/m, only the exact capital formula and stated sufficient payment are claimed.',
 'The explicit entropy source price H(Z)<=7I(Z) is derived for this family; no arbitrary-core H price is assumed.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A061/account04; A064 post-release selection and A065 shallow full-support obstruction credited as motivation'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':[str(R/'out/MAIN.json'),str(R/'out/ACTIVATION_MAIN.json'),str(R/'out/AUDIT.json')]},
 'proof_dependencies':[],
 'review_records':[{'reviewer':'A061','verdict':'AUTHOR_ANALYTIC_PROOF_AND_EXACT_CHECKS; INDEPENDENT REVIEW PENDING; NOT LEAN-CHECKED','scope':'Full references, every-coordinate block drift, all cuts, explicit activated source price and matching depth boundary. Auxiliary core Lean attempt timed out and certifies nothing.'}],
 'status':'AUTHOR_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[], 'first_unproved_line':None,
 'next_consumers':['A064','A065','A087','A094','B20']}
sourcepath=Path(r'agents\A064\runs\20261026T223614Z-account04-A064-global-debt-potential\CLAIMS.json')
source=next(c for c in read(sourcepath) if c['claim_id']=='A064-SELECTED-RESET-ENTROPY-RELEASE-ORDER')
source['review_records'].append({'reviewer':'A061/account04','verdict':'HOLDS_AT_STATED_NO_DATA_QUERY_SCOPE; NO_REPAIR','scope':'Independent harmonic full-CE potentials, adapted-cut necessity, lottery order and retained terminal entropy; 256 labelled cores and depths0..4 via separate Bellman recurrence. No arbitrary initial entropy price or GU acceptance.','proof_source':str(R/'PROOF.md'),'validation':str(R/'out/AUDIT.json')})
source['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE'
assert source['statement_sha256']==hashlib.sha256(source['exact_statement'].encode('utf-8')).hexdigest()
save(R/'CLAIMS.json',[new,source])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B13','packet_id':'A061',
 'gap_id':'B13-ARBITRARY-CORE-ORIGINAL-SOURCE-SELECTED-FULL-TERMINAL-PAYMENT',
 'attempt_id':'A061-stage22-deep-physical-data-selected-reset',
 'method':'Consume A064 selection/order and A065 shallow-prime obstruction; change from dummy lotteries to actual data queries with mixed exact/frozen references; construct maximum-floor supermartingale and exact capital.',
 'mathematical_delta':'Exact deep-policy capital max(H(Z),delta*K_r) for full-support physically-prime activated point tensors; matching sqrt(m) survivor-depth threshold for t=O(m); SAME original8I pays all cuts with old debit<=I. A064 order theorem independently HOLDS at no-data scope.',
 'deliverable_status':'COMPLETE_LOCAL; supervisor archive and mirror unverified',
 'mathematical_status':'NEW_SCOPED_ANALYTIC_PROOF_EXACT_CHECKED_REVIEW_PENDING; FULL_FEI_OPEN; AUXILIARY_LEAN_UNVERIFIED',
 'claim_versions_used':['A064-SELECTED-RESET-ENTROPY-RELEASE-ORDER@1 (independently reconstructed context)','A065 stage21 PROOF sections1-6,9 (shallow-policy obstruction reconstructed as target boundary)','A087-FULL-TERMINAL-ANY-REFERENCE-PRODUCT-STOP-LOWER-BOUND@1 (accepted scoped motivation)'],
 'claims_created_or_changed':[new['claim_id']+'@1',source['claim_id']+'@1 review only'],
 'source_artifacts':[str(R/'out/SOURCE_RECEIPTS.json'),str(R/'PROOF.md'),str(R/'out/MAIN.json'),str(R/'out/ACTIVATION_MAIN.json'),str(R/'out/AUDIT.json'),str(R/'out/FORMAL.json')],
 'next_consumers':['A064','A065','A087','A094','B20'],
 'next_action':'Independently review the exact full-terminal data policy, then replace the point-factor source by a useful arbitrary-core continuation with ORIGINAL O(I) funding and actual query KL retained; do not demand all shallow product stops.',
 'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary-core ORIGINAL source/selected continuation not influence-priced; universal FEI OPEN.','Auxiliary core Lean maximum lemma timed out: RUNTIME_UNVERIFIED, no axioms/target identity certified.','New theorem independent review and supervisor archive/mirror pending.'],
 'packet_ids':['A061']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A061 stage22: deep data queries pay a selected product terminal

## exact target, quantifiers, hypotheses and units

The deep selected policy is paid even on A065's full-support physically indecomposable adversary. For every m>=2 and 1<=r<=m, reduce each live point block to r coordinates before actual product installation; freeze installed blocks while querying other data. The exact least capital is max(H(g_m),K_r), K_r=r*h2(2^(1-r))/2^(1-r). A first bent pivot changes the entropy floor to H(g_m)+2. With t controls and rare activation delta=2^-t it is max(H(Z),delta*K_r). All quantifiers, declared actions, fair physical filtration, endpoints and full reference atoms are in PROOF.md. Units bits. A valid source-specific bound H(Z)<=7I(Z) makes ONE ORIGINAL8I account with old consumption<=I sufficient when r<=floor(sqrt(m)). Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol {protocol['revision']}, current BOARD/B13 notes v2 and own stage21 report/proof were consumed. A087's independent acceptance of that prior theorem is recorded on the board and in its 20261023T143823Z PROOF sections1-6. New target dependencies: A064 20261026T223614Z PROOF sections1-5, and A065 20261027T011923Z PROOF sections1-9. Their original CLAIMS and source byte pins are in out/SOURCE_RECEIPTS.json. Canonical README/status/claims/obstructions/packet/actions/plan, supplemental campaign and source notes, four paper text versions and prior local reports were read. Threshold38pp Proposition8.1, section8.1, Proposition8.6 and Corollary8.10 were inspected as scope context; no unreviewed threshold/percolation theorem supplies this proof. Out/SOURCE_RECEIPTS.json distinguishes byte encodings and pins49 sources. No source tree or other-agent folder was modified.

## complete derivation or exact first unsupported line

PROOF sections1-4 give V_s=max(H_s,2^(r-s)M_r), with V=0 on killed blocks and V=M_r on frozen product terminals. The half-constant/half-smaller-point physical query has expected child V=V_(s-1)/2<=V_s, using H_s>=H_(s-1)/2. Reset preserves V and raises actual CE only to M_r. Exact references on active factors and retained full frozen references give zero actual outcome KL, including source-zero rows. The sum is a nonnegative supermartingale for every admitted physical interleaving and every cut. Its predictable drops compensate it to a martingale. Initial stopping and completing all resets give matching lower bounds, hence exact root capital. Both expected terminal H and expected terminal KL are separately retained.

Section5 proves r(r-1)<=K_r<r(r+1/2), H(g_m)<=4m. Section8 adds all actual activation controls with W_l=max(H(Z_l),2^-l*V_core). The inactive child is an actual constant; the active child is Z_(l-1), so the same maximum inequality applies. Direct spectrum summation prices H(Z)<=7I(Z) and verifies full support and physical tensor primeness. This yields SAME-original payment at8I after old debit<=I. For t<=beta*m the matching all-dimensional boundary is r=O(sqrt(m)); for unrestricted t only the stated sufficient result and exact cost formula are claimed.

Section6 independently reconstructs A064-SELECTED-RESET-ENTROPY-RELEASE-ORDER@1 without repair. Its before reserve E[(L-2)_+] differs from after reserve (E L-2)_+ because the adapted early stopping cut can depend on the lottery only in the former order. Verdict HOLDS at its no-data scope; arbitrary H is still explicitly paid. A087's full-terminal lower bound reconstructs as context, without reviewing GU again.

No unsupported line remains in the new scoped analytic theorem. The first universal unpaid line is an ORIGINAL influence-priced source and useful selected continuation on an arbitrary indecomposable core, with all actual physical-query KL, old debits and both full terminals. Q=P sets KL to zero but does not pay H. No all-product-stop necessity is restored.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the main computation; ACTIVATION_SPEC.json separately freezes the added carrier domain before its computation. These are fixed-domain exact validations, with no floating discovery search. `python -X utf8 code/check.py` runs pilot then main. Main: {main['predicates']} predicates,35 (m,r) pairs m2..8,161 mixed exact/frozen two-block states,146 independent Bellman states, {main['seconds']:.3f}s PASS. Pilot2583 overlapping predicates/9 pairs are excluded from the main count. Integer labelled Walsh spectra, separately counted physical edges, Fraction normalized full references, prime-exponent logarithms and48-term outward rational atanh intervals check all signs. Both physical children, character and immediate-reset boundaries, current CE, installed KL and every legal mixed-reference query are tested. Two-block Bellman maxima independently enumerate adapted stopping decisions.

`python -X utf8 code/activation.py`: main6 labelled Boolean sources (m2,t1..4; m3,t1..2),12 compressed exact sources m2..4,t1..4,36 triples with all r; {act['exact_predicates']} direct/equality predicates and {act['interval_predicates']} interval predicates PASS in {act['seconds']:.3f}s. Pilot4 sources/28 overlapping checks excluded. Actual spectra, each physical influence, full support, inactive-control slices and source price are checked independently. The analytic proof supplies all dimensions and all factor counts; no truth table of the enormous virtual tensor is materialized.

`python -X utf8 code/audit.py`:256 labelled3-bit cores and lotteries depth0..4; {audit['independent_cut_predicates']} cut predicates and {audit['interval_predicates']} interval/helper predicates PASS in {audit['seconds']:.3f}s. It separately reconstructs before/after Bellman costs, both full terminal laws, and A064's64-point3-factor epsilon1/8 strict-gap example. This is deterministic validation of the read theorem, not a parameter search. Its counts are kept separate from our theorem's checks.

FORMAL_SPEC.json and code/formal.py admit only a fresh-memok-approved core Lean check with an enforced1024MB cap. Mathlib was not started because its known~4GB cost violates this packet's1.5GB ceiling. The named Nat scaled-max lemma attempt ended RUNTIME_UNVERIFIED after the55-second compiler timeout (receipt wall59.443s including overhead); compiler hash and exact reviewed source hash are recorded in out/FORMAL.json. Target identity and axioms remain unverified. It certifies NOTHING about the Nat lemma, entropy, real logs or stopping. The result's rung is analytic proof with exact validation, pending independent review; NOT Lean-checked. Other jobs had frozen memory estimates <=100MB, with no GPU, auto-escalation, detached work or process shedding.

## proof dependencies and changed downstream conclusions

New A061-DEEP-SELECTED-DATA-RESET-SHARP-SQRT-BOUNDARY@1 is self-contained, author-proved and exactly checked, pending external review. A064@1 receives a source-bound independent HOLDS review without changing its mathematical statement/version. A065's shallow obstruction is preserved: the new policy queries deeply enough to escape its insufficient-depth regime and proves a matching constructive scale on its actual activated family. A087/A064's ALL-product-stop obstruction remains valid. No arbitrary-core supplier or universal source price follows. Source and output artifacts are locally handed to A064/A065/A087/A094/B20; downstream use is not claimed.

## one next mathematical action and independent reviewer

A087/A094 should reconstruct the max potential, full inherited mixed references and exact activated root cost. A064/A065 should use the deep policy as a mandatory positive control against rejecting every product terminal. Then replace the explicit point-factor initial source by a noncircular arbitrary-core source/continuation whose full price is O(I), retaining actual query KL and old consumption. A further point dimension or shallower prefix cannot remove that remaining hypothesis.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, PROOF.md, frozen specs, code and exact outputs are saved locally. code/finalize.py checks exact protocol fields, statement hashes, proof hash, byte-identical compatibility, two-line STATUS and local UTF-8 readback; out/PERSISTENCE_RECEIPTS.json records byte hashes and sizes. No local save blocker. Supervisor archive/mirror, native ingestion, external review and downstream use remain pending. No git, mail, external writes or other-agent edits were performed. Mandatory wake/checklist infrastructure calls were separate from research writes; wake flagged stale personal/context/dream notes and those notes supplied no proof premises. The bounded auxiliary compiler attempt is finished; no research job was detached or left running.

**Universal bridge:** C019 stopping-tree payment and C024 history transfer advance from a no-data selected lottery to a complete selected physical DATA continuation with mixed frozen/exact references, on the same full-support physically prime rare-activation family that defeats shallow product stops. Exact capital max(H(Z),delta*K_r) closes the depth scale at r=Theta(sqrt(m)) and pays all old debits/full terminals from one supplied original8I owner. What remains is an arbitrary-core ORIGINAL O(I) source and compatible selected continuation. NEXT targets that missing source while preserving a constructive deep-policy positive control, rather than asking for the already-refuted ALL-product-stop budget or collecting another isolated finite case.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A061 stage22 complete: exact deep DATA reset capital max(H(Z),delta*K_r), sharp sqrt(m) boundary on full-support physical-prime activation; SAME original8I with old debit I pays all cuts; exact audits PASS; review pending; FEI OPEN.\nNEXT: A064/A065/A087/A094 review selected deep full-terminal policy; supply arbitrary-core ORIGINAL O(I) source/continuation with actual query KL and old consumption retained.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8')
tag='stage22 (20261027T044753Z)'
entry=f'\n{now} — {tag}: consumed A087 acceptance and new A064 order/A065 shallow-prime obstruction; proved exact selected deep DATA capital max(H(Z),delta*K_r), matching sqrt(m) depth on physical-prime full-support sources. SAME original8I after old debit I pays every cut/full terminal. Main3263, activation80+312, independent A0643841+15940 predicates PASS, pilots excluded. Core Lean1024MB-capped attempt timed out UNVERIFIED; no formal certificate. New external review/arbitrary-core source/FEI OPEN; local protocol/rolling files saved, supervisor archive pending.\n'
for name,text in [('WORKLOG.md',entry),('LEARNED.md',f'\n{now} — {tag}: A live point_s block frozen only at r admits V_s=max(H_s,2^(r-s)M_r); sum V dominates FULL CE of mixed exact/frozen references and is a fair physical supermartingale. For N=2^(m-1) blocks, exact root capital=max(H(g_m),K_r), K_r=r*h2(2^(1-r))/2^(1-r) in[r(r-1),r(r+1/2)). Actual controls-first activation transports it to max(H(Z),delta*K_r), with H(Z)<=7I(Z) and physical primeness/full support. For t=O(m), r=O(sqrt(m)) is necessary and sufficient for O(I) selected capital. This closes the deep side of A065 shallow obstruction, not arbitrary-core initial funding. Frozen factors retain ALL product-reference-only atoms; active factors remain exact, so actual outcome KL is0. A064 before/after lottery theorem HOLDS at no-data scope. Nat maximum formal attempt timed out; do not cite as Lean-checked.\n')]:
 p=HOME/name;old=p.read_text(encoding='utf-8')
 if tag not in old:p.write_text(old+text,encoding='utf-8')
# Exact protocol and persistence verification, including independently reread owner-visible report.
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
cf=set(protocol['required_per_run']['claim_fields'])
for c in read(R/'CLAIMS.json'):
 assert set(c)==cf
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
report_read=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+f in report_read for f in protocol['required_per_run']['report_fields'])
assert report_read.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'status':'PASS_LOCAL_READBACK','protocol_fields':'EXACT','packet_delta':'BYTE_IDENTICAL','review_status':'PENDING_NEW_CLAIM','remote_archive':'NOT_VERIFIED','files':files})
print(json.dumps({'status':'PASS_LOCAL','files':len(files),'claim_id':new['claim_id'],'A064_review':'HOLDS','FEI':'OPEN','formal':'UNVERIFIED'},indent=2))
