from pathlib import Path
import json,hashlib,datetime
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(n):return json.loads((R/'out'/n).read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
required=['full.json','review.json','mean_full.json','moments.json','collision_full.json','bent_full.json']
D={n:load(n) for n in required}
assert all(x['status']=='PASS' for x in D.values())
assert D['collision_full.json']['queries']==197136 and D['collision_full.json']['failure_count']==0
assert len(D['bent_full.json']['compressed'])==8
assert all(x['guarded_price4_refuted'] for x in D['bent_full.json']['compressed'] if x['k']>=8)
P=Path(r'math-open-problems/reports\fei-2026-10-11')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
run=R.name; now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sources=[]
def source(p,scope):
 p=Path(p)
 if p.exists():sources.append({'path':str(p),'sha256':sha(p),'scope':scope})
for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
 source(P/n,'Protocol complete; navigation/status and relevant B16/A077/bridge entries; old endpoint superseded by current user order')
base=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
 source(base/n,'Campaign scope, baseline identities, controls and B16 mapping; no full-FEI proof premise')
for n in ['BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','OVERLAPPING_PRODUCT_NOTE.md','ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md','LOG_ALLOCATION_CURATED.md']:
 source(base/'sources'/n,'Actual block/overlap/collision controls; allocation sections on nonreuse')
shared=Path(r'~\brain_workers\FEI100_20261011')
source(shared/'BOARD.md','Stage-start board; A076 latest common-event transfer and other stream frontier')
source(shared/'claude/B16/STREAM_NOTES.md','v2 2026-10-11; majority target already settled in own stage2; current productive resume follows protocol')
for p in (shared/'context').glob('*.txt'):
 source(p,'Contextual abstract and relevant composition/shared-data/stopping sections. Original extraction is cp1252 after strict UTF8 failure; no percolation theorem is used')
source(shared/'agents/A076/runs/20261021T201341Z-account03-A076-threshold-and-tribes-controls/POINT_CARRIER_PROOF.md','Scoped independent review section7 inequality7 and bank conservation ONLY')
for r in ['20261014T020716Z-account05-A077-sparse-defect-towers','20261014T045011Z-account05-A077-sparse-defect-towers']:
 for n in ['REPORT.md','PROOF.md']:source(A/'runs'/r/n,'Inherited bent/point obstruction and point-exit stopping account; no claim of a new discovery of that family')
save(R/'SOURCE_MANIFEST.json',{'created_utc':now,'sources':sources,'brain_recall':'One read-only math_recall call with two wordings returned general/unresolved cards; no card used as proof dependency','wake':'OWNER ALERT stale owner-model/state notes disclosed; current task/source instructions used'})
next_action='Pay a further unequal correlated private split from SAME remaining original C5 bent donor after booked4e and all old debits; preserve selector account, full inherited core erasures and both terminal spectra; derive eligibility without resetting a child certificate. A092/A028/A094 review.'
statements=[
('A077-TWO-POINT-CORRELATED-TRANSFER',
 'For every d>=1,n>=0,h Boolean with h(0)=h(e1)=1 and arbitrary correlated Boolean V,W on a disjoint private n-cube, the two-point wrapper has H=H_sep+Xi with Xi=e sum_nonempty k(Vhat,What), -2e(VarV+VarW)<=Xi<=0, and every actual private i obeys Delta H(F)<=e[Delta H(V)+Delta H(W)]+Delta R+12Inf_i(F)+DeltaXi, R=de(2-mu^2-nu^2), e=2^-d. For the guarded bent/point pair at even k>=4 an actual unused C5 bent surplus S=e(3k/2+5), after old debit D0 with S-D0>=4e, pays one collision by booking4e and retaining S-D0-4e in both children; entropy price12 and erasure price12+2/ln2 retain full inherited core bills and terminals.',
 'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','PROOF.md sections1-6,8; out/full.json,out/mean_full.json,out/bent_full.json'),
('A077-CORRELATED-COLLISION-LOCAL-PRICE-NOGO',
 'For every even k>=6 and d>=1 the two-point wrapper with V*=y times quadratic bent_k and W*=y times (k+1)-bit point defect satisfies Delta_iXi/Inf_i(F)>=k-6, Inf_i(F)=2^(-d-k), while all controller parent/child means and mean-bank releases vanish and all four controller children are nonconstant. At d=k the wrapper is rare with I tending to0. H(F)<=10I(F), so this refutes every finite local collision-price K and not FEI. The exact signed collision is not determined by (EV,EW,EVW).',
 'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','PROOF.md sections5,7; out/bent_full.json,out/moments.json'),
('A077-FINITE-COLLISION-PRICE4',
 'For every ordered pair V,W of Boolean functions on n=1,2,3 uniform private bits and every physical private coordinate i, Delta_i(Xi/e)<=4[Inf_i(V)+Inf_i(W)]. Exactly65808 labelled roots and197136 private queries are certified; constant4 is attained. This finite statement does not extend universally: A077-CORRELATED-COLLISION-LOCAL-PRICE-NOGO refutes any finite all-dimensional K.',
 'EXACT_FINITE_CERTIFICATE_AUTHOR_CHECKED','code/scan_collision.py; COLLISION_FROZEN_SPEC.json; out/collision_full.json')]
claims=[]
for cid,s,status,proof in statements:
 claims.append({'claim_id':cid,'version':1,'exact_statement':s,'hypotheses':['uniform cube; entropy bits; actual Boolean controllers; shared/private inputs physically disjoint','Exact domain and side conditions as quantified in exact_statement'],
 'statement_sha256':hashlib.sha256(s.encode('utf-8')).hexdigest(),'contributors':['A077'],'proof_source':proof,
 'proof_dependencies':['Self-contained Walsh/Parseval, binary entropy and scalar derivative arguments in PROOF.md','Entropy decrement B+JS with JS<=2Inf/ln2 for erasure corollary; exact baseline reconstructed in prior work'],
 'review_records':[],'status':status,'supersedes':[],'refutes':(['candidate universal DeltaXi<=K Inf_i(F), all finite K','candidate collision paid only by mean-bank release'] if 'NOGO' in cid else []),
 'first_unproved_line':('None within the finite domain; general extension is refuted.' if 'FINITE' in cid else 'No independent acceptance or full Lean proof; arbitrary next-history donor eligibility and full FEI remain open.'),'next_consumers':['A076','A078','A028','A092','A094']})
expected=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==expected for c in claims)
save(R/'CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B16','packet_id':'A077','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A077-stage6-correlated-row-collision-original-donor',
 'method':'Exact two-point signed Fourier profile; mean-sector semiconvexity; adversarial bent/point reduction with common character guard; source-owned C5 surplus debit; exact finite census and scoped A076 review',
 'mathematical_delta':'Correlated two-point mean sector paid12 from SAME sum of original boundary banks; exact signed Xi retained. Finite n<=3 price4 certificate survives but ALL finite universal Xi query prices fail, with balanced nonconstant children and rare roots. One collision paid by4e from actual unused C5 bent surplus, leaving>=7e. Next-history eligibility remains unpaid.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_AUTHOR_PROOFS_AND_EXACT_FINITE_CERTIFICATE; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A076-STRUCTURED-SPECTRA@7 section7 scoped reconstruction; prior A077 stage4/5 family/ownership context; no unreviewed universal premise'],
 'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
 'source_artifacts':['PROOF.md','REVIEW_A076.md','SOURCE_MANIFEST.json','code/','out/','all frozen specifications'],
 'next_consumers':['A076','A078','A028','A092','A094'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Full FEI remains OPEN','Independent review of new results pending','Core Lean timeout: RUNTIME_UNVERIFIED; no theorem certification','Supervisor copy/shared-index adoption/remote mirror unobserved'],'packet_ids':['A077']}
keys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==keys
save(R/'PROGRESS.json',progress); save(R/'PACKET_DELTA.json',progress)
scales=[]
for k in [6,8,10,16,32,48,64]:
 d=k; e=a=Q(1,1<<k); b=Q(1,1<<(k//2)); S=e*(Q(3*k,2)+5)
 capacity=5*e*(Q(k,2)+1); terminal=e*k; debit=4*e
 assert capacity==terminal+debit+(S-debit)
 selector=e*(1-b+a); sc=[e*(1-b+2*a),e*(1-b)]
 assert sum(sc,Q(0))/2==selector
 I=e*(2*d+Q(k,2)+1-b+(k+2)*a)
 scales.append({'k':k,'d':d,'e':str(e),'a':str(a),'minority_root':str(e),'Inf_private_i':str(e*a),'I_root':str(I),
 'signed_collision_lower_bound':str((k-6)*e*a),'mean_bank_root':str(2*d*e),'mean_bank_release':'0',
 'selector_root':str(selector),'selector_children':[str(z) for z in sc],'selector_release':'0',
 'original_bent_C5_capacity':str(capacity),'full_bent_terminal_entropy':str(terminal),'actual_unused_bent_surplus':str(S),
 'old_debit_demo':'0','booked_collision_debit':str(debit),'remaining_same_donor':str(S-debit),
 'full_point_terminal_entropy':'e*[g(1-2a)+(a^-1-1)g(2a)] on active child,0 on character child; inherited parent e*[g(1-a)+(2/a-1)g(a)]',
 'source_balance_exact':True,'both_controller_children_nonconstant':True})
save(R/'MULTISCALE_COST_LEDGER.json',{'family':'guarded bent/point two-vertex wrapper,d=k','units':'entropy bits and physical uniform-cube influence','scales':scales,'warning':'booked4e is a conservative one-collision debit,not actual signed debt; next split inherits remaining_same_donor,never original surplus'})
(R/'SPARSE_DEFECT_TOWERS.tex').write_text(r'''\documentclass{article}
\usepackage{amsmath,amssymb}
\begin{document}
\title{A signed collision in sparse Boolean towers}\date{}\maketitle
Full Fourier entropy--influence remains open. Entropies are in bits.
Two shared vertices of mass $e=2^{-d}$ carry arbitrary correlated Boolean
controllers $V,W$. Put $g(t)=-t^2\log_2t^2$ and
\[
 \Xi=e\sum_{T\ne\varnothing}
 \left(\frac{g(\widehat V(T)+\widehat W(T))+g(\widehat V(T)-\widehat W(T))}{2}
       -g(\widehat V(T))-g(\widehat W(T))\right).
\]
The full entropy equals the separated-row expression plus $\Xi$;
the complete empty-private sector is retained. Although $\Xi\le0$,
its restriction decrement can be positive. The mean sector obeys
\[
 \Delta_iH(F)\le e(\Delta_iH(V)+\Delta_iH(W))+
 \Delta_i\{de(2-\mu^2-\nu^2)\}+12\operatorname{Inf}_i(F)+\Delta_i\Xi.
\]
The reserve is the original sum of point-event banks. Its directional
derivative distribution has entropy at least $d-1$; weighted log concavity
and $|g'|\le6$ give the midpoint price12.

For even $k\ge6$, set $a=2^{-k}$, $b=2^{-k/2}$, $V=yB_k$, where $B_k$
is quadratic bent, and $W=y(1-2\mathbf1_{\{z=0,i=0\}})$.
All controller parent/child means vanish and all four controller children
are nonconstant, but $\operatorname{Inf}_i(F)=ea$ and
\[
 \Delta_i\Xi/\operatorname{Inf}_i(F)\ge k-6.
\]
Indeed each nonempty bent label contributes at least $a^2(k-5)$,
by the decreasing second derivative of $g$ on $[b-2a,b+2a]$.
The common character introduces the old empty-label midpoint remainder
between $-a^2$ and zero. The actual family satisfies $H(F)\le10I(F)$;
it refutes a local-payment claim and not FEI. Taking $d=k$ makes roots rare.

An actual unused target-five bent surplus $S=e(3k/2+5)$ pays one collision
by a booked debit $4e$. For inherited old debit $0\le D_0\le S-4e$,
both children retain $S-D_0-4e$ and their full terminal entropy.
The next split receives that remaining donor, never $S$ again.
Full proofs and endpoint conventions are in \texttt{PROOF.md}; exact
per-scale source balances are in \texttt{MULTISCALE\_COST\_LEDGER.json}.
\end{document}
''',encoding='utf-8')
report=f'''# A077: correlated sparse defects retain a logarithmic collision

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. The stage advances the existing private-collision handoff: actual uniform-cube Boolean wrappers edited at two shared vertices, with arbitrary correlated private controllers and entropy in bits. PROOF.md gives the complete all-dimensional statements, endpoint conventions and source-owned debit. Every mean/selector bank and both actual terminal spectra stay explicit.

The correlated mean sector is paid at price12 from the SAME original point-event reserve R=de(2-mu^2-nu^2). The residual Xi is an exact signed Fourier-row collision. Every finite universal query price for DeltaXi is refuted, even with balanced parent/child controllers, both children nonconstant and rare roots. One actual collision can instead use4e of the original C5 bent-core surplus, leaving at least7e; an inherited old debit is retained in the eligibility test.

## sources actually read, revisions and theorem locators

Execution protocol v2, required campaign navigation/status/registries, B16 notes v2, stage-start board, campaign supplement and relevant source controls were read. The old campaign endpoints are superseded by the current user instruction. Source hashes/scopes are in SOURCE_MANIFEST.json. The later A077 folders contained no substantive saved derivations, so own stage5 was the last usable handoff; the old lead majority target was already completed at stage2. The new A076 v7 common-event theorem was consumed and independently reconstructed at POINT_CARRIER_PROOF.md section7 only (REVIEW_A076.md).

The threshold38 text Proposition8.6, equations75-79, supplies the known shared-data baseline; the two-point identity is a specialization, not a novelty claim. Both versions of the threshold/percolation texts were inspected for relevant context; no percolation result is a premise. Strict UTF8 decoding failed on the supplied PDF extractions, and explicit cp1252 decoding was used without modifying them. One two-wording read-only math recall supplied no applicable proof dependency. Wake stale-note warnings were disclosed.

## complete derivation or exact first unsupported line

PROOF.md sections1-2 derive H(F)=H_sep+Xi, Xi=e sum k, with k(a,b)=(a^2+b^2)[H(q)-H(p)-1]. Thus Xi<=0, but its private restriction decrement can be positive. Section3's xy/y witness has zero original mean-bank release and zero inherited core erasure/entropy drops, yet DeltaH=4e, B=2e, JS=2e and Inf=e, with both controller children nonconstant. Section5 gives balanced orthogonal pairs with the same three physical moments and Xi/e equal0 or-4.

Section6 pays the ENTIRE mean sector in every dimension. Its directional derivative law has entropy at least d-1. Gibbs plus the original-bank subtraction gives semiconvex curvature at least-(2+6/ln2)e(a^2+b^2); the midpoint and Boolean derivative bounds yield price12. The exact Xi and full inherited entropy remain.

The n<=3 census supports price4 for DeltaXi, but section7 explicitly defeats extrapolation: the bent/point pair, multiplied by one common fresh character so ALL controller children remain balanced and nonconstant, satisfies DeltaXi/Inf>=k-6 for every even k>=6. The proof uses a decreasing g'' midpoint estimate and separately bounds the shifted old-empty label. This is the inherited sparse-bent obstruction expressed in the new residual. Its actual global H/I stays <=10, so it is not an FEI disproof.

Section8 uses an ACTUAL unused C5 bent surplus S=e(3k/2+5), after old debit D0. If S-D0>=4e, book4e once and retain S-D0-4e in BOTH children. The mean/selector accounts and full terminals remain; erasure price is12+2/ln2<15 with full inherited core erasures. This is a one-node transfer, not a fresh child certificate. The first unsupported universal line is eligibility of a further unequal correlated split against that SAME remaining donor after all old bookings. No universal child-surplus bound is asserted.

## executed validation with domain, arithmetic, commands and outputs

All searches had saved frozen specifications. code/check_profiles.py --pilot passed; its full run checks816 labelled roots,1584 private queries and eight rare xy/y fixtures: {D['full.json']['exact_assertions']} exact assertions. code/check_mean.py --pilot then full checks the same root/query domain for price12 and SAME-bank release: {D['mean_full.json']['exact_assertions']} exact assertions. These are different properties on overlapping domains, not distinct independent function coverage.

code/check_profiles.py --review checks256 A076 roots and512 private queries by direct character sums, physical edges, rational prime-log identities and outward log signs: {D['review.json']['exact_assertions']} exact assertions. code/check_moments.py independently checks two n=3 pairs using direct sums and dyadic logarithms. code/scan_collision.py --pilot then full exhausts65808 ordered controller pairs and197136 actual private queries through n=3:0 failures,2044 equalities. Every sign is checked using prime-log integer vectors and outward 2^-60 logarithm intervals. The diagnostic maximum4 is not the certificate; the integer sign loop is.

code/check_bent_collision.py --pilot then full verifies eight compressed k values4,6,8,10,16,32,48,64 and both guarded/unguarded complete truth tables at k=2,4. Its final exact assertion count is {D['bent_full.json']['exact_assertions']}; model coefficients also agree with independent complete direct character sums. The compressed domain is justified by equal-magnitude bent rows and evenness of k(a,b), not a guessed symmetry. The analytic all-k proof is separate from these certificates. Both original and remaining donor amounts are checked.

All Python commands use python -X utf8 and paths under this run's code/. Largest completed mathematical helper runtime is {max(x['elapsed_seconds'] for x in D.values()):.6f}s; each frozen invocation cap is55s, with no automatic dimension increase. Memory estimates are <=80MB, actual peaks unmeasured; no >300MB or heavy search/GPU job was launched. Two failed bent pilots are preserved in out/FAILURE_RECEIPTS.json: integer1 entered a Fraction-only helper, then the k>=4 remainder bound was mistakenly tested on the extra k=2 boundary fixture. Both were repaired and unchanged domains rerun; failed attempts count as no coverage.

Core Lean was attempted on a pinned-source finite raw-Walsh witness with an allowlisted target and only Core imports. out/LEAN_RECEIPT.json reports RUNTIME_UNVERIFIED after timeout (62.652s wrapper elapsed against55s compiler timeout). No Lean theorem or axiom certificate was obtained, and no Lean-check claim is made. The mathematical rung is author proof plus exact finite certificates; independent review remains pending.

## proof dependencies and changed downstream conclusions

The new derivations are reconstructed from Walsh, Parseval, finite binary entropy, scalar log/derivative inequalities and exact influence ownership. The erasure corollary uses DeltaH=B+JS and JS<=2Inf/ln2. A076 section7 HOLDS at its common-controller private scope; its shared-query/global-FEI claims are not assumed. A076/A078/A028 receive the exact correlated-row residual, a complete mean-sector payment, and a guarded obstruction to ALL constant-price collision-only repairs. A092/A094 receive the actual donor debit/terminal audit. The finite price4 result is explicitly scoped and cannot be promoted; its universal extension is refuted by the same bundle.

## one next mathematical action and independent reviewer

{next_action} A092 is the primary independent reviewer; A094 checks both complete terminals and source ownership; A028/A076 can challenge the carrier-to-donor conversion. No message was sent and no other agent's output was changed.

## actual persistence receipts or precise save blocker

All four protocol artifacts, full proof, scoped review, frozen specifications, source manifest, scripts, completed outputs, failure receipts and Core Lean receipt are saved locally under the requested immutable run path. PERSISTENCE_RECEIPT.json records schema, hashes and readback. STATUS has two lines; WORKLOG is appended; LEARNED retains exact durable statements. All files are below20MB. Supervisor copying, GitHub mirrors, shared-index adoption and independent acceptance are unobserved; no Git command, public release or brain write was used.

## Universal bridge

C024 history transfer and C019 stopping-tree payment advance at the exact live-child frontier: the two-profile mean sector now has a dimension-independent SAME-bank price12, while the leftover collision is identified exactly and proved to defeat every local physical-query constant even under balanced nonconstant children and rare roots. One such collision is paid from a concrete unused C5 bent child surplus with an explicit4e debit and at least7e retained. Full FEI still needs eligibility and conversion for a further correlated split from that SAME remaining owner, with all inherited core bills and full terminals. That next step attacks the unpaid nonlocal source condition directly; more constant searches for DeltaXi alone are retired.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
state='STATE: A077 stage6 complete locally: correlated mean sector paid12 SAME banks; guarded Xi/Inf>=k-6 refutes every local price; one actual C5 surplus debit4e leaves7e;197136 finite splits certified; A076 scoped HOLDS; FEI OPEN.\nNEXT: '+next_action+'\n'
(A/'STATUS.md').write_text(state,encoding='utf-8')
entry=f'\n{now} stage6 {run}: Derived exact two-profile Xi and mean-sector price12 with original R; universal Xi query-price refuted analytically by guarded bent/point family, despite all197136 n<=3 splits certifying4. All controller children balanced/nonconstant; rarity preserved. One collision funded from actual unused C5 bent surplus, debit4e and retained>=7e. Scoped A076 v7 section7 HOLDS independently; two failed pilot guards repaired and recorded; Core Lean timeout, no certificate. New proof/review/mirror pending; full FEI OPEN. NEXT: same remaining donor eligibility, never renew original S.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(entry)
lesson='''\n## 2026-10-22 stage6: correlated profiles and a real donor\n\nFor two point-edited shared vertices (mass e=2^-d each), arbitrary correlated Boolean V,W have exact H=H_sep+Xi with Xi=e sum_nonempty k(v_T,w_T), k=R[H(Hadamard binary law)-H(original binary law)-1], hence -2e(VarV+VarW)<=Xi<=0. Its restriction decrement can be POSITIVE. The complete mean sector is paid at12Inf from the SAME original R=de(2-mu^2-nu^2), with full inherited core entropy and exact Xi retained (PROOF.md6).\n\nAll197136 private splits of ordered Boolean pairs through n=3 satisfy DeltaXi<=4Inf exactly, but there is NO universal finite constant. V*=y*bent_k, W*=y*point_defect_(k+1), query the point-private bit: all controller parent/child means0, all four children nonconstant, mean-bank release0, and DeltaXi/Inf>=k-6 for even k>=6. At d=k the root is rare and I tends to0; actual H<=10I. This is the old sparse-bent obstruction localized in the exact residual, not a new FEI counterexample. Never extrapolate the sharp finite4 certificate.\n\nA concrete original C5 bent surplus S=e(3k/2+5) can fund ONE collision by4e after old debit D0 provided S-D0>=4e, leaving at least7e when D0=0,k>=4; both child terminals, full inherited core erasures and selector reserve remain. The next node owns S-D0-4e, never S. Arbitrary next-history eligibility is unpaid. Physical moments (EV,EW,EVW) do not determine Xi: balanced orthogonal character and majority pairs have Xi/e0 and-4.\n\nExact checker lessons: coerce integer endpoints to Fraction before a rational logarithm helper; use a theorem's k>=4 restriction when testing extra k=2 boundary fixtures. Preserve failed pilots without coverage credit. Core Lean timed out; no formal proof is claimed. A076 v7 section7 common-controller private bound was independently reconstructed at that scope only.\n'''
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(lesson)
# Readback/schema checks precede the receipt. Receipt excludes itself.
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for c in claims:assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
artifacts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  artifacts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'PERSISTENCE_RECEIPT.json',{'created_utc':now,'protocol_revision':'2026-10-11-execution-v2','schema_checked':True,'compatibility_byte_equal':(R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes(),'status_two_lines':True,'local_readback':'PASS','independent_review':'PENDING','remote_mirror':'UNOBSERVED','full_fei':'OPEN','artifacts':artifacts})
print(json.dumps({'status':'SAVED_AND_READ_BACK','claims':len(claims),'artifacts':len(artifacts),'report_bytes':(R/'REPORT.md').stat().st_size,'full_fei':'OPEN'}))
