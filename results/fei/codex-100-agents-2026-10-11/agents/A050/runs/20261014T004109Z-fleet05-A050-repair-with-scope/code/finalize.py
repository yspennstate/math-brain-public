from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1]
CAM=AGENT.parents[1];REPORTS=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def write(p,s):p.write_text(s,encoding='utf-8')
def js(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads((RUN/'out'/'CHECK.json').read_text(encoding='utf-8'))
assert result['status']=='PASS' and result['cases']==1883
targeted=json.loads((RUN/'out'/'TARGETED_CHECK.json').read_text(encoding='utf-8'))
assert targeted['status']=='PASS' and targeted['cases']==3
statement=('For every uniform-cube Boolean sign and finite deterministic fresh-singleton stopping tree, on its actual coherent root lift let S be the root Fourier-square sample, Q the final queried set, W=S\\Q, D=S intersect Q, and A any fixed superset of all possibly queried coordinates. With a=I_A(f) and R=I(f)-E I(f_leaf), the injected information is e=I(W;Pi|S)=H(D|S), E|D|=R, a-R=E I_A(f_leaf), and e<=a h2(R/a). The bound is the cross-entropy of ONE normalized conditional reference rho_theta(d|S)=theta^|d|(1-theta)^(|S intersect A|-|d|), theta=R/a, minus its conditional KL. Root-Markov compatibility of the actual W is equivalent to e=0. Every leaf independent of A implies e=0 despite variable query sets; E I_A(f_leaf)<=kappa R implies e<=(1+kappa)h2(1/(1+kappa))R. With output information o and Gamma_W=H(Pi|Y)-H(Pi|W), one has o/2+[Gamma_W]_+/2<=R/ln(2)+e/2. The coefficient one in the active entropy capacity is asymptotically sharp on A048\'s actual indexed-parity point-defect family with k=2r+2. Arbitrary overlapping or identical terminal data cores are permitted when all controller dependence is resolved. Terminal Fourier entropy and influence remain retained; no universal history-bank supply or FEI conclusion is proved.')
claim={'claim_id':'A050-ACTIVE-LABEL-SCHEDULE-REPAIR','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite cube; entropy in bits','Actual Boolean sign and function-specific coherent lift with original coordinate labels','Finite deterministic singleton stopping tree with fresh queries; terminals may remain nonconstant','A fixed superset of all potentially queried coordinates; actual physical influence','Zero-reservoir and bounded-reservoir clauses carry their explicitly stated additional hypotheses'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A050'],
 'proof_source':['PROOF.md','code/check.py','out/CHECK.json','out/FIXTURES.json','code/targeted.py','out/TARGETED_CHECK.json'],
 'proof_dependencies':[], 'review_records':[], 'status':'SCOPED_REPAIR_PROVED_AND_EXACTLY_CHECKED_LOCALLY_REVIEW_PENDING',
 'supersedes':[], 'refutes':[],
 'first_unproved_line':'The same normalized spectral reference supplies H(Pi|W)/2 once and pays signed erasure and complete terminal Fourier entropy from nonduplicated physical influence.',
 'next_consumers':['A048','A047','A092','A087','A091','A057','A064','B10','B20']}
js(RUN/'CLAIMS.json',[claim])
sources=[REPORTS/'EXECUTION_PROTOCOL.json',CAM/'BOARD.md',CAM/'claude'/'B10'/'STREAM_NOTES.md',
 AGENT/'runs'/'20261013T212442Z-fleet05-A050-repair-with-scope'/'REPORT.md',
 AGENT/'runs'/'20261013T212442Z-fleet05-A050-repair-with-scope'/'CLAIMS.json',
 CAM/'agents'/'A047'/'runs'/'20261013T221434Z-fleet05-A047-boundary-search'/'REPORT.md',
 CAM/'agents'/'A047'/'runs'/'20261013T221434Z-fleet05-A047-boundary-search'/'CLAIMS.json',
 CAM/'agents'/'A048'/'runs'/'20261013T234007Z-fleet05-A048-tensor-stress'/'REPORT.md',
 CAM/'agents'/'A048'/'runs'/'20261013T234007Z-fleet05-A048-tensor-stress'/'PROOF.md',
 CAM/'agents'/'A048'/'runs'/'20261013T234007Z-fleet05-A048-tensor-stress'/'CLAIMS.json',
 CAM/'agents'/'A091'/'runs'/'20261013T220323Z-fleet05-A091-composition-referee'/'REPORT.md',
 CAM/'agents'/'A056'/'runs'/'20261013T215801Z-fleet05-A056-balanced-composition'/'REPORT.md',
 CAM/'agents'/'A064'/'runs'/'20261013T235917Z-fleet05-A064-global-debt-potential'/'REPORT.md']
js(RUN/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':digest(p)} for p in sources])
report=f'''# A050 stage 3: active-label schedule repair

## exact target, quantifiers, hypotheses and units

Repair the failed application of root-compatible conversion to an actual adaptively reset descendant spectrum. For every finite uniform Boolean function and physical fresh-singleton stopping tree, quantify the schedule information inserted in the ambient terminal spectrum. Bits, actual physical influence, exact inherited Fourier laws. This is a narrow repair of A048's new scope objection, not a third broad B10 potential. Full FEI remains OPEN.

Let S be the root sample, W=S\\Q the actual terminal sample, and A a fixed superset of possible queries. With a=I_A(f), R=I(f)-E I(f_leaf), prove e=I(W;Pi|S)=H(S intersect Q|S)<=a h2(R/a). One normalized deletion reference certifies the bound, including its exact KL rebate. The weakest zero-injection condition is e=0, equivalent to actual root-Markov compatibility. A useful physical sufficient hypothesis is terminal independence of A; the quantitative alternative is bounded terminal active-block influence E I_A(f_leaf)<=kappa R.

## sources actually read, revisions and theorem locators

The complete execution protocol revision 2026-10-11-execution-v2 was reread. BOARD was read at the start; its later opening says 2026-10-14 00:50 UTC. B10 lead notes remain v2, 2026-10-11 23:31Z: repair the failed potential with explicit scope and preserve terminal balances. No disagreement with that direction; the newly consumed A048 obstruction determines this stage's concrete repair. Own STATUS and stage-2 report, claim and checker were recovered. Earlier campaign papers and registries were read in previous stages, not newly re-audited here.

Sources used: A048 PROOF sections 'Coherent root lift', 'Exact guard and repair boundary', and its Boolean counterfamily; A047 REPORT's root-compatible paid conversion; A091 priority shared-controller ledger; A056 REPORT's disjoint-core scope; A064 REPORT's fixed-controller data-prefix scope. The precise source paths and SHA256 values are in out/SOURCE_RECEIPTS.json. BOARD reports A046/A092 independent acceptance of our previous output-conditional theorem; this stage does not manufacture new review records for that theorem.

## complete derivation or exact first unsupported line

PROOF.md gives the complete argument: invertible deletion/retention maps conditional on S; influence telescoping E|D|=R; conditional Bernoulli-subset reference normalization; exact KL identity; optimal theta=R/a; structural zero-injection and bounded-reservoir consequences; self-contained uniform channel/output bounds; terminal-inclusive ledger and Boolean asymptotic sharpness.

The corrected actual-descendant conversion is max(o,j_W)/2<=R/ln(2)+e/2<=R/ln(2)+a h2(R/a)/2. Terminal independence of A removes the extra cost even when final query sets vary. It admits adaptive short-circuit evaluation of overlapping controllers followed by arbitrary shared-data Boolean cores. It excludes the unrestricted indexed-parity reset. Under bounded residual active-block influence the repaired coefficient is 1/ln(2)+(1+kappa)h2(1/(1+kappa))/2.

A048's family with k=2r+2 has a=2^r+r2^(-2r-1), R=1+r2^(-2r-1), e=r-o(1), and capacity a h2(R/a)=r+log2(euler_number)+o(1). Thus the new capacity has asymptotically sharp factor one within actual Boolean functions. No unbounded Hhat/I is claimed. FIRST UNSUPPORTED universal line: pay H(Pi|W)/2 together with signed erasure and retained terminal entropy from one nonduplicated influence budget. The deletion reference is a normalized schedule code; it does not itself generate the physical transcript or fund that conditional bank.

## executed validation with domain, arithmetic, commands and outputs

Frozen before search: out/FROZEN_SPEC.json; arithmetic repair history is out/VALIDATION_REPAIR.md. Final helper A050-active-label-v1.2. Pilot command `python -X utf8 code/check.py --pilot`: 48 exact cases, 1,025 assertions PASS. Main command `python -X utf8 code/check.py`: {result['cases']:,} cases and {result['assertions']:,} assertions PASS in {result['runtime_seconds']:.3f} arithmetic seconds. Commands are run from this run directory or with its explicit relative prefix. The initial main wait was interrupted without a result; no failed or unfinished run is called PASS.

Domain: all 278 truth tables n=0..3, four policies (complete, first-query partial, history-dependent second-coordinate partial, and controller-block prefix), giving 1,112 trees; all 256 ordered pairs of 2-bit cores sharing the SAME two data coordinates in a 3-controller priority function, with three policies, giving 768 trees; three explicit indexed-parity fixtures (r,k)=(1,2),(2,2),(3,2), largest n=14. No symmetry reduction and no automatic dimension increase. Rational Fourier-square laws and coherent joint kernels are reconstructed directly. Checks include physical marginals, actual leaf spectra, E|D|=R, a-R=terminal active influence, conditional injection, KL-bound signs, normalized deletion references, signed conditioning conversion and endpoint zero cost. Integer-log identity vectors with rational 32-term atanh tail bounds are used; each log interval is rounded outward to 2^-256. No floating search is a certificate. All-dimensional validity and sharpness are proved analytically, not extrapolated from these cases. Runtime cap 300 seconds, memory estimate 80 MB, so no >300 MB job was launched. No GPU or background job.

Additional targeted verification was frozen separately in out/TARGETED_SPEC.json after discovering that the k=2 indexed fixtures have zero injection (their root spectrum determines the controller schedule). Command `python -X utf8 code/targeted.py` passed three cases and {targeted['assertions']} exact assertions in {targeted['runtime_seconds']:.3f}s. It proves: three-bit parity with an adaptive second query injects exactly one bit; the shared-data parity/point-defect priority fixture has zero injection, variable final masks 1,3,7, and retained terminal Fourier entropy exactly 1/4 bit; the indexed-parity r=2,k=3,n=10 fixture has strictly positive injection 2(1-j_3) and retained terminal Fourier entropy exactly 2 bits. These certificates are in out/TARGETED_CHECK.json. They supplement, rather than replace, the completed 1,883-case main check.

## proof dependencies and changed downstream conclusions

The new active-cost theorem and conversion bound are self-contained in PROOF.md; claim proof_dependencies is empty. A048-ACTUAL-DESCENDANT-SCHEDULE-INJECTION@1 supplies the known sharpness family and is reconstructed at three small instances; its all-dimensional asymptotic is independently derived from the displayed formulas. A047-PAID-COMPATIBLE-CONDITIONING-CONVERSION@1 is recovered with an elementary uniform channel proof, not accepted beyond its stated scope. The ledger application uses A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 as an optional versioned corollary; it is not necessary for the new active-cost claim.

Downstream substitution: actual descendant reset cannot be used solely because its marginal is a genuine Fourier law. It is valid at unchanged root-compatible price if terminal controller dependence vanishes, including variable-query-set priority controllers with shared data. Otherwise carry HALF the exact active schedule entropy, bounded by HALF the new normalized-reference capacity. This replaces A048's coarser H(Q|S) guard without asserting a universal removed-influence payment. No claim is refuted or superseded here.

## one next mathematical action and independent reviewer

NEXT: on a three-output shared-control priority tree with controller dependence fully resolved, use W=S\\A and one complete reference to test/pay H(Pi|W)/2 jointly with the signed erasure ledger and full terminal core entropy. Zero injection removes the newly exposed reset distraction. This is the missing C024/C019 bank-supply step, not another isolated Boolean class. Independent reviewer: A048, with A092 checking that no actual/future conditioning or terminal entropy is silently discarded. Handoffs are local files only; no messages were sent.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, PROOF.md, code/check.py, code/finalize.py and out/ certificates are saved under this stage's assigned run. STATUS.md is two lines; WORKLOG.md and LEARNED.md are appended. out/ARTIFACT_RECEIPTS.json records local SHA256 and sizes. The compatibility delta equals PROGRESS exactly with packet_ids=["A050"]. Local save is complete; independent review, supervisor mirrors and downstream adoption are pending, not claimed. No shared/read-only tree was modified.

**Universal bridge:** This stage advances C024 history transfer and C019 stopping-tree payment by replacing an unpriced adaptive descendant injection with the exact active deletion entropy and a sharp normalized-reference cap a h2(R/a), and closes that added cost entirely when terminal controller dependence is zero. It admits shared-control/shared-data priority stopping trees that the disjoint-core repairs do not cover, but proves only their reset conversion. The remaining universal bridge is funding H(Pi|W)/2 plus signed erasure and full terminal Fourier entropy with a single influence budget. NEXT is the shortest route because it attacks that surviving bank directly after removing the newly demonstrated schedule obstruction, rather than counting another admitted class as FEI progress.
'''
write(RUN/'REPORT.md',report)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B10','packet_id':'A050',
 'gap_id':'C024-ACTUAL-DESCENDANT-SCHEDULE-INJECTION','attempt_id':'A050-stage3-active-label-reference',
 'method':'Normalized root-conditional deletion reference, physical active-influence telescoping, sharp actual Boolean family, exhaustive rational coherent joints',
 'mathematical_delta':'Exact injection H(S intersect Q|S)<=I_A h2(R/I_A); terminal controller independence restores compatibility despite adaptive query sets; bounded reservoir repairs conversion at explicit price; factor-one capacity asymptotically sharp.',
 'deliverable_status':'COMPLETE_LOCAL_SAVE_REVIEW_PENDING','mathematical_status':'SCOPED_REPAIR_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':['A048-ACTUAL-DESCENDANT-SCHEDULE-INJECTION@1','A047-PAID-COMPATIBLE-CONDITIONING-CONVERSION@1','A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 (ledger corollary only)'],
 'claims_created_or_changed':['A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1'],
 'source_artifacts':['PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/VALIDATION_REPAIR.md','code/check.py','out/PILOT.json','out/CHECK.json','out/FIXTURES.json','out/TARGETED_SPEC.json','code/targeted.py','out/TARGETED_CHECK.json'],
 'next_consumers':claim['next_consumers'],'next_action':'Pay a complete W=S\\A conditional history bank jointly with signed erasure and retained terminal entropy on a three-output shared-control tree; A048/A092 review.',
 'stagnant_substantive_attempts':0,'blockers':['Universal conditional-history bank and signed/terminal payment remain open; independent review and mirrors pending.'], 'packet_ids':['A050']}
js(RUN/'PROGRESS.json',progress);js(RUN/'PACKET_DELTA.json',progress)
write(AGENT/'STATUS.md',f'STATE: A050 stage3 proved sharp active-label schedule bound and zero-residual-controller repair; {result["cases"]:,} exact cases PASS; review pending; full FEI OPEN.\nNEXT: A048/A092 review; pay W=S\\A conditional history bank with signed erasure and terminal core entropy on a three-output shared-control tree.\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as fp:
 if '--refresh' not in sys.argv:fp.write(f'\n{stamp} — Stage3 {RUN.name}. Consumed A048 descendant schedule obstruction and A047 surviving compatible conversion. Proved H(S intersect Q|S)<=a h2(R/a) by one normalized deletion reference; controller-complete leaves give zero injection with adaptive short-circuit sets and shared data. Bounded residual active influence gives explicit conversion coefficient. A048 indexed-parity family makes capacity factor one sharp. Initial main wait interrupted; arithmetic factoring capped and interval bounds rounded outward, with repair frozen. Final {result["cases"]:,} cases/{result["assertions"]:,} exact assertions PASS in {result["runtime_seconds"]:.3f}s. Terminal entropy/influence preserved; conditional bank plus signed erasure remains first unsupported universal step.\n')
 if '--targeted-note' in sys.argv:fp.write(f'\n{stamp} — Stage3 targeted certificate supplement: initial indexed k=2 fixtures inject zero; froze three explicit follow-ups, all PASS ({targeted["assertions"]} assertions). Adaptive three-bit parity injects exactly one bit; shared-data priority retains 1/4 bit Fourier entropy with zero injection; indexed r=2,k=3 retains 2 bits Fourier entropy and positive injection. Updated report/claim proof sources and persistence receipts without rerunning or altering main certificate.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as fp:
 if '--refresh' not in sys.argv:fp.write('''\nStage3 durable fact: for uniform coherent fresh-coordinate trees, actual W=S\\Q injects exactly H(S intersect Q|S). For query superset A, a=I_A(root), R=removed I=E|S intersect Q|, a-R=E I_A(leaf). One normalized Bernoulli deletion reference gives H(S intersect Q|S)<=a h2(R/a), with exact conditional KL rebate. Root-Markov of W is equivalent to zero injection. All leaves independent of A suffice even if final query sets vary; arbitrary shared terminal data is allowed. Residual I_A<=kappa R gives injection<=R(1+kappa)h2(1/(1+kappa)). Actual conversion<=R/ln2+injection/2. A048 k=2r+2 indexed-parity family has injection r-o(1), capacity r+log2(e)+o(1), proving factor-one asymptotic sharpness. This normalized schedule code does NOT fund H(Pi|W), signed erasure, or terminal Fourier entropy. Avoid full prime factorization of large rational marginal numerators: residual integer log atoms suffice; round rigorous log endpoints outward to a fixed grid before summing.\n''')
 if '--targeted-note' in sys.argv:fp.write('\nStage3 certificate lesson: indexed parity k=2 has j_k=1 and zero injection, so use k>=3 to test that obstruction. Exact r=2,k=3 joint confirms positive injection with 2 retained terminal entropy bits. The same-data priority pair g=2-bit parity,h=point defect has a=R=11/16, terminal I=5/8, terminal Fourier entropy=1/4 bit, e=0 despite masks {1,3,7}. Adaptive two-query three-bit parity has e=1 bit although root Fourier entropy is zero.\n')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)})
js(RUN/'out'/'ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','claim':claim['claim_id'],'cases':result['cases'],'files':len(receipts)}))
