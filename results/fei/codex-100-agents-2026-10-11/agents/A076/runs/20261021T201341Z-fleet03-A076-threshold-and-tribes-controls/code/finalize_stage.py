"""Persist stage7, validate schema and reread every saved artifact."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parents[1]
OLD=AGENT/'runs/20261014T091637Z-fleet05-A076-threshold-and-tribes-controls'
PROTO=Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(n,v):(ROOT/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
pr=load(PROTO);point=load(ROOT/'out/FULL.json');event=load(ROOT/'out/EVENT_FULL.json')
pilots=[load(ROOT/'out/PILOT.json'),load(ROOT/'out/EVENT_PILOT.json')]
assert all(x['status']=='PASS' for x in [point,event]+pilots)
assert point['roots']==3336 and point['private_queries']==5808 and event['roots']==6072
total=point['exact_assertions']+event['exact_assertions'];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
lean=(ROOT/'out/LEAN_RECEIPT.txt').read_text(encoding='utf-8')
lean_ok='VERIFIED_TARGET' in lean
save('out/VALIDATION_RECEIPTS.json',dict(point=point,event=event,pilots=pilots,exact_assertions_excluding_pilots=total,
 independent_reproduction_scope='Direct character sums and physical-edge influence within same agent; not independent referee acceptance',
 formal_scope='Only integer quadratic reserve identity submitted to core Lean; no analytic theorem formalized',lean_receipt='out/LEAN_RECEIPT.txt',
 runtime_deviation=load(ROOT/'out/RUNTIME_DEVIATION.json')))
ext1=' Stage7: For ANY Boolean h,D on one uniform shared cube, ANY Boolean V on a disjoint uniform private cube, p=Pr(D=-1), kappa=I(D)/2 and F=h[1+1{D=-1}(V-1)], each private query i obeys Delta_i H(F)<=p Delta_i H(V)+kappa Vhat(i)^2+11 Inf_i(F), with Inf_i(F)=p Inf_i(V). The single original reserve is R=kappa(1-(EV)^2); its release is exactly kappa Vhat(i)^2. Every adaptive private stopping tree retains p[H(V)-E H(V_leaf)], both full terminal spectra and terminal R, with total residual at most11 times consumed actual private influence; the corresponding retained-input erasure price is14. No equal Fourier heights, nonzero-support, balance or derivative-gap hypothesis is needed. Proof uses complete shifted-row relative entropy curvature and the self-contained cube boundary inequality I(D)/2>=p log2(1/p); shifted-zero singularities are handled by C1 convexity gluing. Different private functions at different activated vertices and actual arbitrary shared-query bills are not covered.'
ext2=' Stage7: At the SAME original source with h=Maj5 on five shared bits and V=1-2*1{x1=x2=x3=z=0}, the x1,x2,s1,x3 history along surviving zero answers, with every sibling and both final children retained and z never queried, is paid by inherited private input entropy plus ONE original point-boundary R release plus11P_private+6P_shared. The full Maj5 spectrum has six coefficients3/8, ten coefficients-1/8 and sixteen zeros, so unequal heights are genuine. All inherited quarter-core erasures, both nonconstant mux cores, complete terminal entropies/influences and exact signed C=5 source/child surpluses are retained. No source surplus or selector reserve is renewed. The arbitrary-event extension likewise gives local private payment for any two fixed shared branches and one disjoint common controller, while its input entropy and general shared-query cost remain unpaid.'
claims=load(OLD/'CLAIMS.json')
for c,ext in zip(claims,[ext1,ext2]):
 c['version']=7;c['exact_statement']+=ext;c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
 c['hypotheses'].append('Stage7 alternative module: arbitrary shared Boolean h,D, one common disjoint Boolean private V on uniform cubes; bits. p=0 handled separately. Unequal profiles allowed. Mixed shared-query payment asserted only for specified Maj5 history. No arbitrary-input FEI certificate supplied.')
 c['proof_source'].update(stage7=str(ROOT/'POINT_CARRIER_PROOF.md'),stage7_locator='sections1-7, especially curvature(8)',stage7_validation=str(ROOT/'out/VALIDATION_RECEIPTS.json'))
 c['proof_dependencies'].append(c['claim_id']+'@6 (prior bundle retained; new private-payment derivation self-contained)')
 c['review_records'].append(dict(claim_version=7,status='NOT_INDEPENDENTLY_REVIEWED',requested_reviewers=['A028','A092','A088','A094'],formal_scope='Core integer identity only; not analytic curvature theorem'))
 c['status']='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW';c['supersedes']=[c['claim_id']+'@6'];c['first_unproved_line']=None
 c['next_consumers']=['A027','A028','A077','A078','A088','A092','A094','B16','B20']
 assert set(c)==set(pr['required_per_run']['claim_fields'])
save('CLAIMS.json',claims)
nextact='Replace the common private controller by two correlated private profiles on two activated shared vertices; derive the exact covariance/conditional-entropy remainder and test payment from SAME unused product-boundary/source surplus, retaining both inherited profiles, old debit and full terminals. A028/A092/A094 review v7 first.'
progress=dict(protocol_revision=pr['revision'],run_id=ROOT.name,stream='B16',packet_id='A076',gap_id='FEI-B16-A076-INITIAL',attempt_id='A076-stage7-arbitrary-row-curvature-common-controller',
 method='Complete translated-row entropy curvature, weighted KL, self-contained edge isoperimetry, exact Walsh/interval certificates and fixed mixed-history ledger',
 mathematical_delta='Closes unequal-height point-carrier private payment, then arbitrary common-event/two-shared-branch private controller payment with coefficient11 from SAME product-boundary reserve. Actual Maj5 mixed private/private/shared/private history retains inherited inputs, quarter core, signed surplus and both terminals.',
 deliverable_status='COMPLETE_LOCAL_PENDING_V7_REVIEW',mathematical_status='AUTHOR_PROOF_OF_SCOPED_UNIVERSAL_PRIVATE_PAYMENT; MULTIPROFILE_SHARED_PAYMENT_AND_FULL_FEI_OPEN',
 claim_versions_used=['A076-STRUCTURED-SPECTRA@6 retained','A076-TRIBES-PAYMENT-DISCRIMINATION@6 retained','A028 stage5 boundary bank and explicit mixed-query gap: context; specialized conservation independently rederived'],
 claims_created_or_changed=[c['claim_id']+'@7' for c in claims],source_artifacts=['POINT_CARRIER_PROOF.md','SOURCE_MANIFEST.json','code/check_carriers.py','code/check_events.py','code/arithmetic.py','code/Bank.lean','out/FROZEN_SPEC.json','out/EVENT_FROZEN_SPEC.json','out/VALIDATION_RECEIPTS.json','out/MIXED_HISTORY.json','out/RUNTIME_DEVIATION.json','out/LEAN_RECEIPT.txt'],
 next_consumers=['A027','A028','A077','A078','A088','A092','A094','B16','B20'],next_action=nextact,stagnant_substantive_attempts=0,
 blockers=['Different private profiles destroy the common Fourier tensor factor; their signed conditional remainder is unpaid','General shared-query entropy cost and arbitrary inherited input certificate remain unpaid','Independent review and supervisor adoption/mirror verification not observed','Point full checker exceeded frozen180s: actual440.257s; result retained with explicit procedural deviation'],packet_ids=['A076'])
assert set(progress)=={x.split(' (')[0] for x in pr['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
paths=[PROTO,BASE/'BOARD.md',BASE/'claude/B16/STREAM_NOTES.md',OLD/'PHASE_BANK_PROOF.md',OLD/'CLAIMS.json',OLD/'code/arithmetic.py',
 BASE/'agents/A028/runs/20261014T051435Z-fleet05-A028-stopping-tree-payment/DERIVATION.md']
reportdir=Path(r'math-open-problems/reports/fei-2026-10-11')
paths += [reportdir/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=Path(r'math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((BASE/'context').glob('*.txt'))
paths += [supp/'sources'/x for x in ['ERASURE_REDUCTION.md','ISOSPECTRAL_SPLICING_CURATED.md','LOG_ALLOCATION_CURATED.md']]
save('SOURCE_MANIFEST.json',dict(captured_at=now,hash_scope='Actual save-time bytes; not retroactive read snapshots',sources=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in paths],
 context='Protocol/indices and B16 notes retain old deadlines; current owner packet extends campaign to2026-10-23 14:49UTC. Prior ten runs have marker only; productive baseline is stage6. Paper texts are context, not proof dependencies. One math recall returned weak matches, no answering card; no store theorem imported.',
 encoding='Explicit UTF8 throughout; non-UTF8 paper extraction decoded cp1252 without rewriting sources.'))
report=f'''# A076: arbitrary-height and common-event private payment

## exact target, quantifiers, hypotheses and units

For every uniform-cube Boolean pair of shared branches h,hD and every Boolean common controller V on disjoint private physical inputs, pay each private restriction's signed Fourier-entropy decrement using inherited controller entropy, the SAME original product-boundary reserve and a dimension-independent physical price. Entropy is in bits; no balance or equal-height hypothesis is imposed. Full FEI remains OPEN. The precise theorem and all endpoint conventions are in POINT_CARRIER_PROOF.md, sections1-7.

## sources actually read, revisions and theorem locators

Read execution protocol v2, board, B16 notes v2, own rolling files and productive stage6 proof/code. Ten later A076 run directories contain only .final markers; they add no mathematical result. Read the campaign indices, plan and supplement; their old endpoints are superseded by this packet's23October order. Both versions of both supplied papers were read as contextual text: threshold Proposition7.1 and Corollaries7.2-7.3 identify the disjoint-composition baseline; the percolation crossing theorems are not used. Read A028's stage5 DERIVATION sections1-6 and explicit mixed-query gap. SOURCE_MANIFEST.json records paths/hashes and encoding. Math recall returned weak, unrelated matches; no unverified card is a proof dependency.

## complete derivation or exact first unsupported line

POINT_CARRIER_PROOF.md gives the complete argument. Point-carrier translated rows have entropy curvature bounded below by Parseval and log concavity, including original zero rows. The weighted version replaces uniform row averaging by the COMPLETE relative entropy D(w||q). Cube edge isoperimetry gives I(D)/2>=p log2(1/p); this is proved by internal-edge induction. Consequently the compensated row profile is semiconvex with curvature at least-6p/ln2. The midpoint estimate, |g'|<=6 and |Vhat(i)|<=Inf_i(V) imply

    Delta_i H(F)<=p Delta_i H(V)+(I(D)/2)Vhat(i)^2+11 Inf_i(F).

The middle term is the released part of R=(I(D)/2)(1-(EV)^2). It is exactly the already owned A028 reserve. Every adaptive private tree telescopes this SAME R and retains full input entropy and both terminal spectra. Erasure payment has coefficient14 with inherited p B_T(V). Actual shared-query conservation is shown separately from its entropy cost. The specified Maj5 history pays shared exposure at price6 and private exposures at price11, retains every inherited quarter-core row and signed C5 source/child surplus, and never renews a bank.

The first unsupported line is the analogous signed payment when two activated shared vertices carry different correlated private functions. Their Fourier amplitudes no longer factor as c_S Vhat(T). General shared-query costs and arbitrary inherited p H(V) also remain unpaid. This is a scoped universal private-payment theorem, not full FEI.

## executed validation with domain, arithmetic, commands and outputs

The two FROZEN_SPEC files declare domains before their jobs. Run python -X utf8 code/check_carriers.py --pilot and then without --pilot: pilot72 roots/760 assertions; full3336 roots,5808 private queries,{point['exact_assertions']} exact assertions. Every h(0)=1 carrier with d<=3, every controller n<=2, and Maj5 with every n<=3 controller is included. The Maj5 x1,x2,s1,x3 ledger retains all siblings, both last children, the unqueried selector, full entropies and signed surpluses. Independent direct character sums and physical-edge counts check the declared small subdomain within the same agent.

Run python -X utf8 code/check_events.py --pilot and then without --pilot: pilot120 roots/1214 assertions; full6072 roots,{event['private_queries']} private queries,{event['exact_assertions']} exact assertions. It exhausts all shared h and activation events on d<=2 and all controllers n<=2, including p=0,1. All spectrum coefficients, influence identities, original-bank releases, local bounds, rarity charges and signed child surpluses are verified. This yields {total} exact assertions excluding pilots. Full-event elapsed seconds: {event['elapsed_seconds']:.3f}.

Arithmetic uses integer Walsh transforms, Fraction identities, prime-exponent exact logarithm equality and rational outward log bounds with proved atanh tails. No floating sign is a certificate. Analytic inequalities apply in every dimension; finite tests are supplementary. Side conditions checked include zero coefficients, all constants, zero influence, mu=0,+/-1, p=0,1, negative carrier edge changes and complete terminal accounting. The proof explicitly handles zero denominators before use and glues finitely many C1 singularities; no limit crosses an infinite sum.

The point full run took440.257seconds, exceeding its frozen180second cap because that checker lacked a runtime guard. This procedural deviation is preserved in out/RUNTIME_DEVIATION.json; it does not erase its completed finite evidence. No larger dimension was launched. The separate event cap900seconds was frozen before launch and guarded in code. Memory estimate180MB; peak not measured. No GPU or heavy job was launched. Core Lean receipt: {'VERIFIED_TARGET for the integer quadratic reserve identity only' if lean_ok else 'no VERIFIED_TARGET; inspect out/LEAN_RECEIPT.txt for the exact failed or held formalization'}. The main analytic theorem is at author-proof rung, pending independent review, and is NOT Lean-certified.

## proof dependencies and changed downstream conclusions

Both existing A076 bundles extend from v6 to v7; no third broad unreviewed candidate is opened. The new argument is self-contained from Walsh/Parseval, Gibbs/log concavity, the elementary boundary induction and the scalar derivative estimate. A028 supplies prior ownership/context, not an assumed mixed-query inequality. Its block theorem and reserve conservation are not claimed as new. Unequal Fourier heights and a common arbitrary activation event are removed from the private-payment obstruction. Prior scoped reviews do not accept v7. No independent acceptance, universal controller certificate or all-dimensional FEI conclusion is inferred from these tests.

## one next mathematical action and independent reviewer

{nextact}

## actual persistence receipts or precise save blocker

All four required protocol files, proof, frozen specifications, code, finite outputs and rolling files are saved only in A076. PERSISTENCE_RECEIPT.json binds the final files by SHA256 after schema/identity checks and reread. Supervisor copying/adoption and remote mirrors are unobserved; no git or external publication is performed. Checklist entry T-20261021-200 closes this stage's artifact, not FEI. The wake warned that owner-model/state notes were stale; the owner was told, and current instructions/source files governed.

## Universal bridge

C024 history transfer and C019 stopping-tree payment advance from flat/plateaued point carriers to arbitrary unequal-height carriers and arbitrary common events between two shared Boolean branches. Private restriction price improves from40/60 to11 while the SAME original boundary reserve, inherited controller entropy, signed child surpluses and complete terminals remain. General shared-query cost and multiple correlated private profiles are still unpaid. The next two-profile covariance calculation attacks the exact failed factorization in the universal mixed-history step, rather than collecting another isolated class constant; independent A028/A092/A094 review is required before downstream adoption.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: A076 stage7 saved: arbitrary-height/common-event private payment11 from SAME boundary bank; Maj5 mixed history retained; {total} exact assertions PASS; review pending; FEI OPEN.\nNEXT: Two correlated private profiles: price exact covariance remainder from SAME unused ancestor source with inherited profiles and full terminals; A028/A092/A094 review v7.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n## {now} — Stage7 fleet03\nResumed productive stage6 after ten marker-only runs. Proved arbitrary-height point-carrier private price11, then arbitrary common-event/two-shared-branch private controller price11 from SAME product-boundary bank via weighted KL curvature and edge isoperimetry. Full inherited input entropy and all terminals remain. Maj5 mixed history exact; {total} exact assertions excluding pilots PASS. Point run exceeded frozen180s at440.257s; deviation retained. Event cap900 guarded. Core Lean result in run; analytic proof pending independent review. Full FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\nStage7 durable facts: For arbitrary shared Boolean h,D, common disjoint private V, p=Pr(D=-1), kappa=I(D)/2, F=h[1+1{D=-1}(V-1)], every private query pays Delta H(F)<=p Delta H(V)+kappa Vhat(i)^2+11Inf_i(F); erasure price14 retains pB(V). R=kappa Var(V) is the ORIGINAL A028 boundary bank, with exact release kappa Vhat(i)^2. No equal-height/support/balance hypothesis. Weighted shifted-row curvature uses full KL(w||q), mass1-pVar(V), and kappa>=p log2(1/p); C1 gluing handles zero rows. All terminal entropy and inherited input remain. Maj5 x1,x2,s1,x3 history pays11private+6shared with all quarter-core costs and signed surpluses. Different correlated controllers at different activated vertices destroy the tensor factor and remain open. One-sided residual bound only; no absolute Lipschitz claim. Exact point3336 roots plus event6072 roots; runtime protocol deviation point440s versus180 frozen is recorded, not hidden. Main analytic result author-proof pending independent review.\n')
files=list(ROOT.rglob('*'))
for p in files:
 if p.is_file():assert p.stat().st_size<20_000_000
for c in load(ROOT/'CLAIMS.json'):assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
assert load(ROOT/'PACKET_DELTA.json')==load(ROOT/'PROGRESS.json')
assert (ROOT/'REPORT.md').read_text(encoding='utf-8').rstrip().split('\n')[-1].startswith('C024 history transfer')
save('PERSISTENCE_RECEIPT.json',dict(saved_at=now,status='LOCAL_REREAD_AND_SCHEMA_PASS',remote='UNVERIFIED',exact_assertions=total,
 files=[dict(path=str(p.relative_to(ROOT)),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']))
print(json.dumps(dict(status='SAVED_AND_REREAD',assertions=total,point=point,event=event,lean_verified_integer_identity=lean_ok,full_fei='OPEN')))
