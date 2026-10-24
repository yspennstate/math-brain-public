from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
assert A.name=='A061' and B.name=='FEI100_20261011'
rid=R.name;now=datetime.now(timezone.utc).isoformat()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
protocol_path=Path(r'~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=load(protocol_path)
cert=load(R/'out/FAMILY_CERTIFICATE.json');ind=load(R/'out/INDEPENDENT_CERTIFICATE.json')
assert cert['status']==ind['status']=='PASS'
assert [(x['l'],x['dimension_parent']) for x in cert['rows']]==[(1,6),(2,9),(3,12)]
lean_path=R/'out/LEAN_ATTEMPT.json'
assert lean_path.exists(),'Wait for the already running Lean attempt; never rerun it.'
lean=load(lean_path);stdout=(R/'out/LEAN_STDOUT.txt').read_text(encoding='utf-8')
lean_verdict='VERIFIED_TARGET for the integer-scaled sufficient condition only' if lean['returncode']==0 and 'VERIFIED_TARGET' in stdout else 'UNVERIFIED; no Lean certification claimed'
sourcepaths=[protocol_path,B/'BOARD.md',B/'claude/B13/STREAM_NOTES.md',A/'runs/20261014T085352Z-account05-A061-entropy-process/ACCOUNT.md',B/'agents/A064/runs/20261021T151814Z-account03-A064-global-debt-potential/PROOF.md',B/'agents/A064/runs/20261021T151814Z-account03-A064-global-debt-potential/REPORT.md',B/'agents/A039/runs/20261014T055326Z-account05-A039-projection-under-restrictions/PROOF.md',B/'agents/A038/runs/20261014T051947Z-account05-A038-occupancy-term-audit/REPORT.md']
root=protocol_path.parent
sourcepaths += [root/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
sourcepaths += list(root.glob('*.tex'))
supp=Path(r'~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
sourcepaths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sourcepaths += list((B/'context').glob('*.txt'))
sources=[]
for p in sourcepaths:
 if not p.exists():sources.append(dict(path=str(p),status='MISSING'));continue
 raw=p.read_bytes()
 try:text=raw.decode('utf-8-sig');encoding='utf-8-sig'
 except UnicodeDecodeError:text=raw.decode('cp1252');encoding='cp1252'
 sources.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=encoding,role='baseline navigation/relevant excerpts; not a new proof dependency' if p.parent==root or p.parent==supp or p.parent.name=='context' else 'mathematical source actually read'))
dump(R/'out/SOURCE_RECEIPTS.json',dict(at=now,sources=sources,note='Earlier baseline paper intake inherited; this stage uses no outside theorem from those papers. Full text byte receipts do not claim a new full mathematical audit.'))
statement=('For every integer l>=2, the explicit field-bilinear Boolean selector family F_l on 3l+3 bits in PROOF.md has every parent and child coordinate influence 1/2, B_i=JS_i=1, actual entropy decrement2, zero erased-indicator mutual information and zero spectator Jensen gaps. Under the actual parent product reference and the actual coherent physical kernel extended fairly on source-zero rows, r_G=2^(-l-1), O=(l-1)/2-(1/2)log2(1-2^(-l-1)), and signed product conversion D=1+O, so D/Inf_i>l+1. Thus no finite universal D<=C Inf_i holds for these prescribed conversions. If the one original Sbar=mean_child(4I-H) has no prior expenditure, this same transaction uses D<Sbar/4, retaining both complete terminal H+TC bills and leaving more than3Sbar/4 in that same expected owner.')
hyp=['Uniform physical Boolean signs; l>=2; K=GF(2^l) with a nontrivial additive character; h_l(a,b,x)=psi(a)(1-2*1[x=ab]).','Children are the common invertible physical parity shear of B(u,v) and B(u,v)h_l, where B=(-1)^(uv); selector has the two actual children.','Bits for entropy/KL; incoming reference is the actual product of parent spectral marginals; source-zero/reference-positive rows use fair kernel1/2 and are retained.','Conditional quarter-bank assertion requires exactly one original mean child Sbar to be unused before this booking; no universal or post-history availability is assumed.']
payload={'statement':statement,'hypotheses':hyp}
claim=dict(claim_id='A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),contributors=['A061/account03'],proof_source={'path':str(R/'PROOF.md'),'sha256':digest(R/'PROOF.md'),'validation':[str(R/'out/FAMILY_CERTIFICATE.json'),str(R/'out/INDEPENDENT_CERTIFICATE.json')]},proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['UNREGISTERED-CANDIDATE: outcome KL is bounded by erased spectral mutual information plus spectator Jensen gaps','UNREGISTERED-CANDIDATE: every prescribed actual-product conversion has a dimension-independent price by current queried influence'],first_unproved_line=None,next_consumers=['A064','A038','A039','A087','A094'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
next_action='Derive a selected physical-query or deferred-conversion rule that carries SAME unused ancestor capacity through the bilinear-field obstruction, with earlier bookings and both full terminal H+TC bills; A087/A094 independently review the counterfamily.'
progress=dict(protocol_revision=protocol['revision'],run_id=rid,stream='B13',packet_id='A061',gap_id='G-R-MISMATCH',attempt_id='A061-stage17-product-reference-price',method='Counterexample-driven structural audit, explicit bilinear-field Boolean family, exact Walsh/rational certificates and one-original-owner repair',mathematical_delta='Local product conversion price refuted: all influences1/2 and all MI/Jensen credits0, but D/d>l+1 while actual DeltaH=2. Conditional SAME original unused Sbar pays D<Sbar/4 with full terminals. No universal FEI constant changes.',deliverable_status='COMPLETE_LOCAL',mathematical_status='LOCAL_PRICE_REFUTED; CONDITIONAL_ONE_OWNER_PAYMENT_PROVED; FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':1}],source_artifacts=['PROOF.md','ADVERSARIAL_REVIEW.md','out/FAMILY_CERTIFICATE.json','out/INDEPENDENT_CERTIFICATE.json','out/SOURCE_RECEIPTS.json','out/LEAN_ATTEMPT.json'],next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['Arbitrary-history eligibility of SAME unused ancestor reserve remains unproved.','External independent review and supervisor mirror/adoption unobserved.']+([] if lean['returncode']==0 else ['Lean attempt unverified; written proof and exact arithmetic are the stated rung.']),packet_ids=['A061'])
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

For every integer l>=2, construct an actual uniform Boolean parent on 3l+3 bits and audit its distinguished fair selector query under the prescribed actual marginal-product reference. Target the proposed local comparison O<=h2(d)-B+sum spectator Jensen gaps and the consequent D<=JS. Entropy and KL are bits. The no-go theorem and conditional SAME-owner quarter payment have exactly the hypotheses in CLAIMS. Full FEI remains OPEN. The owner's October23 campaign endpoint supersedes the older October21 protocol endpoint; no schedule is changed.

# sources actually read, revisions and theorem locators

Full execution protocol2, current BOARD (October21 19:51UTC), B13 leadv2, own rolling files and substantive prior stage6 proof/certificate interface. A064 October21 account03 PROOF and REPORT now close EVERY adaptive continuation of the three-bit fixture; no further depth extension is attempted and no new independent acceptance of its v2 is asserted. A038 parity payment and A039 final-frontier PROOF supply the ownership boundary. Baseline campaign/registry/plan navigation and both versions of both paper texts were checked at the relevant locators, with earlier full intake inherited; no new outside paper theorem is used. SOURCE_RECEIPTS pins bytes and distinguishes navigation from proof sources. Read-only math recall returned general restriction material but no new estimate is imported. Brain wake warned of stale owner-model/state notes; the owner was alerted and those notes are not mathematical premises.

# complete derivation or exact first unsupported line

PROOF.md gives the complete field-orthogonality calculation. The balanced core h_l(a,b,x)=psi(a)(1-2*1[x=ab]) has one squared coefficient (1-2^(1-l))^2 and (2^l-1)2^(2l) coefficients of mass2^(2-4l). Its empty coefficient is zero. Multiplying by a fresh two-bit bent sign and applying a common invertible physical parity shear makes EVERY child influence exactly1/2. Their spectra stay disjoint. The actual selector has d=1/2, B=JS=1, DeltaH=2 and all erased-MI/spectator-Jensen credits zero.

The erased product reference is uniform. Its G-support, H-support and reference-only masses are alpha=2^(-3l), beta=1-2^(-l)+2^(-3l), epsilon=2^(-l)-2*2^(-3l). Every reference-only row contributes its declared fair half, so r_G=alpha+epsilon/2=2^(-l-1). Therefore O=(l-1)/2-log2(1-2^(-l-1))/2, while mean TC_child-TC_parent=1. Signed D=1+O has D/d>l+1. This refutes the universal all-query local product-conversion price even with all influences1/2. Actual entropy drop remains exactly2; no entropy-drop theorem or FEI is refuted.

The family also supplies a concrete conditional repair. Its original Sbar=mean(4I_child-H_child)>=9l/2+2. If unused, one booking D<(l+2)/2<Sbar/4 leaves more than3Sbar/4 in THAT expected owner, with both full terminal H+TC retained. Along the one-step fair filtration, R_0=TC_parent+Sbar and R_1=TC_child+Sbar-D obey E(R_1+O)=R_0. The old CI-H entropy process is a martingale at this step for C=4. No bank is renewed. First unsupported universal line: a selected query/history or deferred-conversion rule has complete signed costs within genuinely unused SAME ancestor capacity after earlier bookings.

# executed validation with domain, arithmetic, commands and outputs

All searches have preceding frozen specs. `python -X utf8 code/discover.py` evaluates804 labelled n<=3 query pairs; the explicitly frozen four-bit extension `code/discover4.py` evaluates32768 representatives covering all four-bit query pairs by coordinate permutation and output negation. These use float logs only, report no counterexample to D<=JS, and remain numerical discovery evidence. `code/pairs.py` reads32768 exact four-bit child profiles, compares557 same-influence support profiles and finds a genuine five-bit pair with r_G=5/16. This prompted the explicit all-dimensional construction; the discovery statistics are not theorem certificates.

`python -X utf8 code/family.py`: PASS, {cert['checks']} exact assertions, {cert['seconds']:.6f}s. It evaluates ALL truth-table entries/Walsh coefficients and EVERY physical coordinate for l=2,3 (parents9,12 bits), plus excluded l=1 boundary (6bits). Integer field arithmetic/FWHT, direct edge influences, Fraction kernel reaches, prime-log entropy identities and rational strict power comparisons; no floating sign. l=2 predicts1/8 with56 reference-only erased atoms; l=3 predicts1/16 with248. l=1 loses the distinguished coefficient and correctly does not satisfy the l>=2 support formula.

`python -X utf8 code/independent2.py`: PASS, {ind['checks']} exact assertions, {ind['seconds']:.6f}s. Separate explicit GF4 multiplication and DIRECT character sums reproduce the entire nine-bit parent and both children without importing earlier helpers. Child H=(2,7), parent H=13/2, parent TC=5/2, mean child TC=7/2, Sbar=23/2, O=log2(16/7)/2, D=1+O, D/d=6-log2(7)>3. The larger ratios relative to the four-bit pilot reflect an explicitly different, larger family; there is no contradiction or extrapolation from that pilot.

Fresh memok exit0 before the core Lean attempt:15.3GB physical and22.3GB commit free. Lean helper return code{lean['returncode']}, {lean['seconds']:.3f}s: {lean_verdict}. Submitted source is code/QuarterBank.lean with explicit reviewed SHA256 and named target quarter_bank_scaled; full helper output is retained. Its statement is only integer-scaled linear arithmetic sufficient for the quarter-bank bound. It does not formalize real logarithms, field orthogonality, influence definitions or the all-dimensional family. Rung of the main result: written proof plus exact finite checks, external review pending. Each mathematical job is bounded under55s; estimates25--70MB, one separate core Lean estimate512MB admitted by memok, no Mathlib4GB job, GPU, background producer or automatic dimension escalation.

# proof dependencies and changed downstream conclusions

The all-dimensional proof is self-contained apart from elementary finite-field existence and character orthogonality, whose nondegeneracy and summation step are spelled out. No earlier pending A061 theorem is used to prove this counterfamily. Finite-field checks do not establish existence in all dimensions; the written field proof does. Direct reproduction is a second representation by the same contributor, not external independent review. This attacks a narrow proposed local helper rather than opens another broad FEI proof candidate at the existing review cap.

A064/A038/A039 must retain a genuine ancestor owner or defer product conversion: zero spectator Jensen gaps and matched influence vectors cannot pay physical outcome KL. Their prior finite/parity results remain intact. The quarter repair supplies one explicitly quantified eligible transaction if its original bank is unused, not eligibility after arbitrary history. No shared registry has been modified and no universal FEI constant changes. ADversarial failure modes, side conditions and scope exclusions are checked in ADVERSARIAL_REVIEW.

# one next mathematical action and independent reviewer

{next_action} A064/A038/A039 consume the explicit stress fixture; A087/A094 independently reconstruct its field Walsh calculation, common shear, fair extension and ownership condition. The central selected nonlocal payment remains the next unpaid step; another depth extension of the already closed three-bit fixture is unnecessary.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA, complete PROOF, frozen specs, discovery and exact independent scripts, all outputs, source hashes and Lean attempt evidence are saved in this A061 run. Schema validation checks exact protocol key sets, canonical statement hash, byte-identical delta and every file below20MB. Rolling STATUS is two lines, WORKLOG appended and LEARNED updated. PERSISTENCE_RECEIPTS records local sizes/hashes excluding itself. No save blocker; supervisor copy, mirror verification, shared-index adoption and external independent review remain unobserved. No git, messaging, brain writes, remote jobs, trading operations, deletions or other-agent mutations are performed.

**Universal bridge:** C024 history transfer and C019 stopping-tree payment move by a sharp obstruction and its owned repair: even with all parent/child influences1/2 and zero erased-MI/spectator-Jensen credits, the prescribed product-reference transaction costs D/d>l+1, while a genuinely unused SAME original Sbar pays it using less than1/4 and retains both full H+TC terminals. The unpaid universal step is selecting or deferring conversions so earlier charges and future bills fit truly unused ancestor capacity. NEXT targets that ownership transfer on this explicit all-dimensional stress family, which removes a false local shortcut to full FEI instead of repeating an isolated class ratio. Full FEI remains OPEN.
'''
report=report.replace('ADversarial','Adversarial')
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A061 stage17 saved: explicit all-l product-price obstruction D/d>l+1 despite all influences1/2 and zero MI/Jensen; SAME unused Sbar pays<1/4;7505 exact checks PASS; FEI OPEN.\nNEXT: A064/A038/A039 derive selected/deferred conversion using SAME unused ancestor bank on bilinear-field stress family, retaining bookings and both H+TC terminals; A087/A094 review.\n',encoding='utf-8')
work=f'\n{now} — Stage17 account03: consumed A064 all-history finite completion and changed to structural product-query payment. Explicit field family refutes D<=JS and any universal current-influence product price: D/d>l+1 with all influences1/2 and zero MI/Jensen. Conditional SAME original unused Sbar pays<1/4; full terminals retained. Family6868 plus independent direct637=7505 exact assertions PASS; excluded l=1 tested. Lean {lean_verdict}. Full FEI OPEN; saved {rid}.\n'
wp=A/'WORKLOG.md'
if rid not in wp.read_text(encoding='utf-8-sig'):
 with wp.open('a',encoding='utf-8') as f:f.write(work)
lesson='''\nStage17 product-reference obstruction (all l>=2): h_l(a,b,x)=psi(a)(1-2*1[x=ab]) over GF(2^l) is balanced with support (2^l-1)2^(2l)+1. A common bent factor/parity shear makes disjoint children all-influence1/2. Actual selector DeltaH=2, B=JS=1, all erased-MI and spectator Jensen gaps0, but incoming product predicts r_G=2^(-l-1) including reference-only rows. Hence O=(l-1)/2-log2(1-2^(-l-1))/2, signed D=1+O and D/d>l+1. A universal all-query product-conversion price fails even at dense influences. Actual H/I<2, so this is no FEI counterfamily. If original mean child Sbar is genuinely unused, D<Sbar/4 leaves>3/4 in THAT same owner with both H+TC terminals retained. Delay conversion or prove ancestor ownership; matched influence vectors alone cannot pay normalization. At l=1 the gamma0 coefficient vanishes and support formula changes. Exact family and separate direct nine-bit Walsh checks total7505 assertions; finite checks validate the written all-dimensional field proof, not replace it.\n'''
lp=A/'LEARNED.md'
if 'Stage17 product-reference obstruction' not in lp.read_text(encoding='utf-8-sig'):
 with lp.open('a',encoding='utf-8') as f:f.write(lesson)
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(x in report for x in protocol['required_per_run']['report_fields'])
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
dump(R/'out/SCHEMA_CHECK.json',dict(status='PASS',claim_fields=len(claim),progress_fields=len(progress),claim_hash=claim['statement_sha256'],primary_exact_assertions=cert['checks']+ind['checks'],full_fei='OPEN',at=now))
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json' and p.suffix!='.pyc']
dump(R/'out/PERSISTENCE_RECEIPTS.json',dict(at=now,local_only=True,files=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=digest(p)) for p in files],rolling=[dict(path=str(p),bytes=p.stat().st_size,sha256=digest(p)) for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]))
print(json.dumps(dict(status='SAVED_AND_SCHEMA_CHECKED',run_id=rid,exact_checks=cert['checks']+ind['checks'],lean=lean_verdict,files=len(files),full_fei='OPEN')))
