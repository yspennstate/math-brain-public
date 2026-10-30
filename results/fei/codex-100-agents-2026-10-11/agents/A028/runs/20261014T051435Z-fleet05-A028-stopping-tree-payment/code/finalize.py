from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];BASE=HOME.parents[1]
old=HOME/'runs'/'20261014T022306Z-fleet05-A028-stopping-tree-payment'
a23=BASE/'agents'/'A023'/'runs'/'20261014T022245Z-fleet05-A023-amortized-rarity-budget'
a29=BASE/'agents'/'A029'/'runs'/'20261014T025327Z-fleet05-A029-child-deficit-transport'
a56=BASE/'agents'/'A056'/'runs'/'20261014T042008Z-fleet05-A056-balanced-composition'
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,s):Path(p).write_text(s,encoding='utf-8')
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
sources=[protocol,BASE/'BOARD.md',BASE/'claude'/'B06'/'STREAM_NOTES.md',old/'REPORT.md',old/'DERIVATION.md',old/'CLAIMS.json',
a23/'REPORT.md',a23/'PROOF.md',a23/'CLAIMS.json',a29/'REPORT.md',a56/'REPORT.md']
sources += [BASE/'agents'/a/'LEARNED.md' for a in ['A023','A025','A029','A030','A056','A086','A097']]
js(R/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
source=next(c for c in json.loads((a23/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id'].startswith('A023-'))
scope={'source_claim_id':source['claim_id'],'version':source['version'],'original_statement':source['exact_statement'],
'original_declared_statement_sha256':source['statement_sha256'],'proof_source_sha256':sha(a23/'PROOF.md'),
'consumed_scope':'arbitrary-shared-data one-whole-point-controller block, marked R=2p(1-p)I(GH), source ownership and full terminal entropy',
'existing_review_evidence':'A025 LEARNED stage4 and A029 stage4 REPORT accept this whole-block clause only',
'this_stage':'new arbitrary-controller application; no third broad re-review or blanket acceptance',
'excluded':'bundled older separator, localized bad bill and nested renewal claims'}
js(R/'out'/'DEPENDENCY_SCOPE.json',scope)
v=json.loads((R/'out'/'full_validation.json').read_text());pilot=json.loads((R/'out'/'pilot_validation.json').read_text())
m=json.loads((R/'out'/'mixed_bank_full.json').read_text());mp=json.loads((R/'out'/'mixed_bank_pilot.json').read_text())
probe=json.loads((R/'out'/'drift_probe.json').read_text())
claim=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))[0]
statement=('Version5 retains v4 and earlier conclusions at their original scopes. For every Boolean sign controller a=1-2c on a fresh uniform physical cube '
'and arbitrary Boolean branches G,H on an independent data cube, with any amount of shared data, put p=Ec, gamma=Pr(G!=H), '
'F=(1-c)G+cH, Q=gamma I(a), R=2p(1-p)I(GH). The complete control-only stopping-tree signed entropy bill '
'Pi=H(F)-(1-p)H(G)-pH(H) obeys Pi<=gamma Hplus(a)+log2(e)gamma Var(a)+2log2(e)Q+R '
'<=gamma Hplus(a)+3log2(e)Q+R, where Hplus is raw nonempty Fourier entropy. '
'Thus controller Hplus<=K I gives rate K+3log2(e) against Q, plus the one R bank; a strong Hplus<=T(I-Var) certificate gives max(T,log2(e))+2log2(e). '
'With certified terminal allowances L_G,L_H, full path plus terminal cost is at most '
'max(K+3log2(e),L_G+2p,L_H+2(1-p))I(F), with the analogous strong-controller substitution. '
'Calibrating all shared-only atoms yields one normalized complete output reference with CE=(1-p)CE_Gcal+pCE_Hcal+Pi '
'and KL=(1-p)D_Gcal+pD_Hcal, including off-target private mass. '
'Under arbitrary adaptive physical control/data interleaving the same source boundary bank is a nonnegative supermartingale: '
'controller release=(p0-p1)^2 I(GH)/2; data release=2p(1-p)Inf_i(GH)<=2Inf_i(F). '
'For every stopped tree Rroot=sum reach-weighted releases+expected terminal R; marks are not reissued. '
'Release-alone data entropy payment is false even for a dictator controller,G=+1,H=data dictator: root H=2, data release1/2, excess3/2, '
'so an added local data price must be at least3 in the tested residual rule. '
'No local mixed-query entropy price, nested renewal, universal controller/terminal FEI certificate, integer prefix rounding or full FEI is asserted.')
claim.update(version=5,exact_statement=statement,hypotheses=[
'Uniform physical cube; Boolean sign controller and Boolean data branches; entropy/KL/CE bits',
'Controller coordinates absent from both data branches; branches may share their entire data support',
'Control-only complete block for the entropy theorem; arbitrary physical interleaving only for bank conservation',
'Certified controller and terminal allowances must be supplied, not inferred from rarity',
'Exact signed entropy increments; normalized supplied references positive on true support; shared-atom calibration and off-target private mass retained',
'Boundary marks issued once; no inference of local entropy payment from martingale budget alone'],
statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),proof_source={'report':str(R/'REPORT.md'),'proof':str(R/'DERIVATION.md'),'validation':str(R/'out'/'full_validation.json'),'bank':str(R/'out'/'mixed_bank_full.json'),'countercertificate':str(R/'out'/'drift_probe.json')},
proof_dependencies=[{'claim':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@4','scope':'unchanged earlier components','source':str(old/'REPORT.md'),'sha256':sha(old/'REPORT.md')},
{'claim':source['claim_id']+'@'+str(source['version']),'scope':scope['consumed_scope'],'source':str(a23/'PROOF.md'),'status':'SCOPED_EXISTING_A025_A029_REVIEWS_CONSUMED; arbitrary-controller extension reconstructed independently'},
'Elementary scalar entropy inequality plus product tensorization; recovered cube block-JS bound proved directly here',
'Boolean disagreement-set edge isoperimetry and physical influence conservation; both reconstructed',
'A056@3 compatible-reference history scope credited; current theorem proves root reference algebra, does not accept its entire history chain'],
review_records=[],status='PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
supersedes=[{'claim_id':claim['claim_id'],'version':4,'reason':'Same stopping-payment packet: arbitrary certified controller and mixed-history bank extension, earlier scopes unchanged'}],
refutes=[{'exact_statement':'data entropy residual <= released R alone','scope':'tentative local upgrade only; no published/source theorem withdrawn','actual_witness':str(R/'out'/'drift_probe.json')}],
first_unproved_line=None,next_consumers=['A023','A025','A027','A029','A030','A039','A056','A064','A087','A091','A094','B06','B20'])
js(R/'CLAIMS.json',[claim])
report=f'''# A028 stage5: arbitrary-controller stopping payment and one carried boundary bank

## exact target, quantifiers, hypotheses and units

For every Boolean sign controller a=1-2c on a fresh physical uniform cube and arbitrary Boolean G,H on an independent data cube, including full shared data, pay the complete control-only stopping tree and retain both original terminal costs. Let p=Ec,gamma=Pr(G!=H),Q=gamma I(a),R=2p(1-p)I(GH). All entropy/CE/KL is bits; physical influence uses uniform flips. The theorem is Pi<=gamma Hplus(a)+b gamma Var(a)+2b Q+R<=gamma Hplus(a)+3b Q+R,b=log2(e). Hplus is raw nonempty Fourier entropy. Certified controller/terminal rates give FULL path-plus-terminal root rate max(K+3b,L_G+2p,L_H+2(1-p)), with strong-controller refinement max(T,b)+2b against Q.

In particular, if controller and both terminal certificates have rates at most9, the full root rate is below40/3; if the controller has strong rate at most9 and both terminal rates at most9, it is below12. These are explicit certificate criteria, not blanket new admission of opaque functions. The normalized complete output reference retains both calibrated terminal debts. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read current BOARD supervisor2026-10-14 05:13UTC, B06 STREAM_NOTES v2, own STATUS and full EXECUTION_PROTOCOL.json v2. Read board in slices after output truncation; read LEARNED from A023,A025,A029,A030,A056,A086,A097. Read A023 stage4 REPORT and complete PROOF, its original claim source; A029 stage4 REPORT; A056 stage5 REPORT through its controller-corollary/history/validation scope. Source receipts pin actual bytes. Earlier required campaign, registries, plans and papers retain prior-run source scope; no new external/brain premise used.

A023's one-point-block reserve and A025/A029's existing scoped reviews already close last NEXT's point case. A029 identifies the exact nested surcharge; A056 supplies compatible-reference closure, which is not entropy payment. A030's arbitrary controller transport assumes disjoint data branches; A056's profile bound assumes a shared Fourier norm cap. The new theorem removes the point-controller/profile-norm restrictions by retaining controller entropy plus one physical boundary reserve for arbitrary shared branches. No sharper point constant or already known reference closure is republished as new. B06's original arbitrary-controller activation target is consumed beyond its completed v2 constant-branch scope.

## complete derivation or exact first unsupported line

DERIVATION.md is complete. The exact spectrum has data marginal q=(1-p)P_G+pP_H. At every data row, split empty/nonempty controller sectors; conditional nonempty controller law is its own normalized nonempty spectrum. This proves Pi=gamma Hplus(a)+J_p+B_binary+w log2 Var(a), w=gamma Var(a). Jensen and h2 bound cancel the selector scale and leave w[log2(1/gamma)+b]. Boolean edge isoperimetry pays the logarithm with R. A two-point entropy inequality and elementary product tensorization prove J_p<=2bQ directly on the physical controller cube. Poincare gives the stated coefficient; per-coordinate product edge counting assigns R once to actual terminal capacities.

The reference calibrates every shared-only child atom and retains the incoming private conditional law, including off-target mass. Its CE equals weighted calibrated terminal CE plus Pi, and its KL equals weighted calibrated terminal KL exactly. This is a root algebraic proof; A056's inherited-kernel closure is credited at its stated scope, not independently accepted wholesale here.

A stronger ownership conclusion is now proved: R is a nonnegative supermartingale under arbitrary adaptive physical controller/data interleaving. Controller-query release is (p0-p1)^2 I(GH)/2. Data-query release is2p(1-p)Inf_i(GH), at most twice actual queried data influence. Both are conditional identities, so every stopped tree retains Rroot=sum weighted releases+expected terminal R. Branches may change after data restriction, but their actual product restricts identically; no bank is recreated. This is budget conservation, NOT local entropy payment.

The exact separately frozen probe refutes release-only local data payment. For dictator a=(-1,+1),G=(+1,+1),H=(-1,+1), F=(-1,+1,+1,+1) has four squared Fourier coefficients1/4, H(F)=2,I(F)=1. Data children and branch spectra have entropy0. Rrelease=1/2 and actual data influence1/2, so excess is exactly3/2 and a repaired local data price must be at least3. The whole controller theorem and the bank identity remain valid. This obstruction concerns the proposed currency, not FEI or any A023/A056 source theorem.

FIRST UNSUPPORTED LINE: fund the actual signed mixed-query entropy/CE excess using released R, the carried controller certificate/future-control account and one genuinely UNUSED signed child surplus. The bank is conserved but insufficient alone; both seed bills and actual history weights must remain. Nested nonconstant fallback introduces another source conversion that this theorem does not pay. No arbitrary local drift theorem or universal terminal admission follows.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede every job. Main pilot: {pilot['cases']} cases/{pilot['assertions_passed']} exact assertions PASS in {pilot['compute_seconds']:.6f}sec. Main full: all controllers dimensions0..2, all ordered full-shared child pairs dimensions0..2, and all16x16 two-bit children with one shared and disjoint one-bit private blocks: {v['cases']} cases/{v['assertions_passed']} exact assertions PASS in {v['compute_seconds']:.6f}sec. {v['partially_shared_reference_cases']} partial-overlap cases additionally check arbitrary uniform-private reference mass, all off-target atoms, full CE and KL identities. Maximum actual dimension5, no symmetry quotient or dimension escalation.

Separate independent boundary checker uses only truth tables, directed edges and Fraction, not the entropy/Walsh helper. Pilot {mp['cases']} roots/{mp['assertions_passed']} assertions PASS; full {m['cases']} roots/{m['one_query_instances']} physical one-query instances/{m['assertions_passed']} assertions PASS in {m['compute_seconds']:.6f}sec. Every controller and data coordinate verifies exact bank release, and every data release verifies its price<=2 actual query influence. The all-dimensional adaptive extension follows from conditional identities and finite telescoping, not enumeration.

The frozen drift probe domain permits11616 queries; it stopped on the first exact countercertificate after {probe['cases_executed']} queries, in {probe['compute_seconds']:.6f}sec. Witness excess is the pure prime-log vector 3/2*log2(2)=3/2, so no interval ambiguity. It does not enlarge a Boolean family or refute a source claim.

Commands from A028: python -X utf8 runs/{R.name}/code/setup.py; same run code/check.py pilot then full; code/mixed_bank.py pilot then full; code/drift_probe.py pilot. Main checker uses integer Walsh/Fraction/canonical prime-log identities and rigorously outward24-term atanh intervals. Tests use the conservative rational constants13/3 for3b and26/9 for2b, from ln2>9/13; analytic proofs retain exact b. Main controller-release checks were added after the first passing pilot on the SAME frozen domain, then pilot rerun before full. No passing full entropy job was repeated. Main estimate160MB, separate bank32MB, drift100MB; no >300MB job was expected/started, no GPU or background task. Pilots have internal55sec cutoffs; full caps600sec and300sec. All observed jobs meet their frozen caps.

## proof dependencies and changed downstream conclusions

Version5 narrowly extends the same A028 stopping-payment candidate, retaining v1-v4 at their original scope rather than opening another broad universal route. Existing A023@3 whole-block acceptances by A025/A029 are consumed with original statement/proof receipts in out/DEPENDENCY_SCOPE.json; no third blanket review is claimed. The general-controller proof reconstructs its sector, tensorization, boundary and ownership premises directly. A056 history closure remains an explicitly separate upstream scope, not a hidden entropy bank.

A027/A030/A056/A064 can use a full arbitrary-certified-controller stopping bound with fully shared cores, without a common-point/profile-norm hypothesis. C024 users get an exact one-source boundary reserve through mixed physical histories, but the same bank cannot be added again at descendants. The new AND2 countercertificate requires a signed local data/future-controller price in any drift upgrade. Controller and terminal FEI certificates remain conditional; selecting opposite constants recovers the controller's own FEI, so no universal admission is inferred.

## one next mathematical action and independent reviewer

At one actual non-flat DATA query with a non-point controller and shared cores, compute the signed residual after weighted ORIGINAL branch entropy decrements. Compare it to a constant times actual data influence plus released R and the inherited signed future-controller/child surplus; carry A056's compatible reference and preserve both terminal CE bills. Use the exact AND2 lower price3 as a guard, and consume A027/A030's signed data/controller transfers at their valid scopes rather than reissuing the mark. Reviewer A091, alternate A094; A056/A087 should check the separation between structural KL transport, physical bank conservation and actual entropy payment. Handoffs are saved only, not sent or assumed reviewed.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json, complete DERIVATION.md, code and out directories, frozen specs, exact pilot/full/reference/mixed-bank outputs and the standalone countercertificate. Source hashes and scoped dependency receipts are present. code/finalize.py validates exact protocol field sets, required headings, statement hash, output counts, all file sizes and two-line STATUS, then writes out/PERSISTENCE_RECEIPTS.json with artifact/rolling hashes. Writes remain inside A028. Independent v5 review, supervisor copies, canonical adoption and mirror verification are unobserved.

## Universal bridge

This stage moves C019 stopping-tree payment from point controllers to ANY certified Boolean controller selecting arbitrarily overlapping data branches, with explicit controller entropy and one marked terminal boundary reserve. It also moves C024 by proving that this SAME physical reserve is conserved through arbitrary data/control interleaving, retaining expected terminal capacity; no descendant renewal is needed for the bank itself. The exact release-only AND2 obstruction separates conservation from the missing mixed-query payment and forces an added data price>=3 in that rule. Remaining work is a signed mixed-query price using owned future-control/child slack and universally certified terminal costs. NEXT tests that precise residual under one carried reference, which attacks the universal drift gap instead of another already-paid point or fixed-overlap class.
'''
write(R/'REPORT.md',report)
progress=json.loads((old/'PROGRESS.json').read_text(encoding='utf-8'))
progress.update(run_id=R.name,attempt_id='A028-C019-arbitrary-controller-boundary-bank-v5',
method='Exact binary-controller sector factorization, physical tensorized JS, source disagreement boundary reserve, mixed-history influence telescope and exact release-only countercertificate',
mathematical_delta='Arbitrary certified controller/full shared-data cost <=gammaHplus(a)+3bQ+R; strong-controller refinement and complete terminal CE/KL; one R bank contracts at all mixed physical queries; release-only data rule fails exactly, requiring added price>=3',
deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='GENERAL_CONTROLLER_BLOCK_AND_MIXED_BANK_PROVED_LOCAL_DRIFT_AND_UNIVERSAL_FEI_OPEN',
claim_versions_used=['A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@4-preserved-scope',source['claim_id']+'@'+str(source['version'])+'-whole-point-block-scoped-existing-reviews','A056@3-root-reference/history-distinction'],
claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':5,'status':claim['status']}],
source_artifacts=[str(R/p) for p in ['REPORT.md','DERIVATION.md','code/check.py','code/mixed_bank.py','out/full_validation.json','out/mixed_bank_full.json','out/drift_probe.json','out/DEPENDENCY_SCOPE.json','out/SOURCE_RECEIPTS.json']],
next_consumers=claim['next_consumers'],next_action='Pay one non-flat data-query entropy residual from actual query influence plus released marked R and inherited signed controller/child surplus, with A056 compatible reference and AND2 price3 guard',
stagnant_substantive_attempts=0,blockers=['Mixed bank conservation does not bound local entropy/CE excess; bare-release data rule refuted','Nested nonconstant fallback requires one source-owned transfer; no reserve renewal','Controller/terminal certificates remain conditional and universal FEI open','Independent v5 review and supervisor copying/adoption/mirror unobserved'])
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
write(HOME/'STATUS.md','STATE: A028 stage5 saved arbitrary-controller shared-core full payment with one R bank; R contracts through all mixed physical queries; 230304 entropy/reference+87881 bank assertions; release-only data rule refuted (extra price>=3); v5 review pending; FEI OPEN.\nNEXT: A091/A094 review; pay one non-flat DATA residual from actual query influence, released R and inherited signed controller/child surplus with both terminal references retained.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{stamp} — stage5 {R.name}: consumed A023 whole-point payment and A029/A025 nonrenewal scopes; changed to arbitrary certified controller. Proved Pi<=gammaHplus(a)+3bQ+R and full weighted CE/KL; reconstructed tensorized JS and boundary ownership. Found exact controller AND data release identities for same marked R; arbitrary adaptive bank telescopes. Main11704/230304 and independent bank11704/87881 assertions PASS; extra frozen probe refutes release-only data rule at AND2, excess3/2 and added price>=3. Estimates<=160MB/no heavy jobs. v5 same candidate; universal FEI and local mixed entropy payment remain open.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('''\n## Stage5: arbitrary controller and a carried boundary bank

* F=(1-c)G+cH with arbitrary controller signa=1-2c on independent physical controls, fully shared data allowed: p=Ec,gamma=P(G!=H),Q=gammaIa,R=2p(1-p)I(GH). Pi<=gammaHplus(a)+b gammaVar(a)+2bQ+R<=gammaHplus(a)+3bQ+R, b=log2(e). Full rate max(K+3b,LG+2p,LH+2(1-p)); strong Hplus<=T(I-Var) gives max(T,b)+2b for control rate. All terminal certificates conditional.
* Exact binary-sector Pi=gammaHplus(a)+JS_p+B_binary+w logVar(a), w=gammaVar(a). Jensen h2(w) cancels the selector scale; boundary pays wlog1/gamma with R. Tensorized two-point scalar JS gives JS_p<=2bQ. Root reference calibrates every shared-only atom; private conditional/off-target masses remain and weighted terminal KL is exact.
* R is a nonnegative supermartingale under arbitrary physical control/data interleaving: controller release=(p0-p1)^2 I(GH)/2, data release=2p(1-p)Inf_i(GH)<=2actual Inf_data(F). One stopped-tree Rroot=sum weighted releases+E terminalR. This proves bank conservation, not entropy drift or unlimited mark reissue.
* Exact AND2 guard: a=(-1,1),G=(1,1),H=(-1,1), p1/2; rootH2, branch/query-child entropy0; datareleaseR1/2 and actual queryI1/2. Bare-release residual fails by3/2; any added local data price in that rule must be>=3. It does not refute whole-controller bound, bank martingale or FEI. Future-controller/source credit remains, and cannot be silently renewed.
* A023 point-block theorem already has scoped A025/A029 acceptance; A056 structural history/KL closure releases zero controller KL, not a paid entropy bank. NEXT actual non-flat data residual with carried compatible reference, one released R and inherited signed controller/child surplus. Main11704 cases/230304 assertions; separate edges11704 roots/47664 queries/87881 assertions PASS.\n''')
pf=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(pf['claim_fields'])
assert set(progress)==set('packet_ids' if x.startswith('packet_ids') else x for x in pf['progress_fields'])
assert all('## '+h in report for h in pf['report_fields'])
assert claim['statement_sha256']==hashlib.sha256(statement.encode()).hexdigest()
assert sha(R/'PROGRESS.json')==sha(R/'PACKET_DELTA.json')
assert len((HOME/'STATUS.md').read_text().splitlines())==2
assert v['cases']==11704 and v['assertions_passed']==230304 and m['assertions_passed']==87881
assert probe['status']=='REFUTED' and probe['witness']['excess_prime_log']=={'2':'3/2'}
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
js(R/'out'/'PERSISTENCE_RECEIPTS.json',{'run_id':R.name,'schema_validation':'PASS','claim_version':5,'local_status':'SAVED',
'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
'rolling_files':[{'path':str(HOME/p),'sha256':sha(HOME/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']],
'mirror_and_adoption':'UNOBSERVED; supervisor owns copying','write_scope':'A028 only'})
print(json.dumps({'status':'PASS','artifact_count':len(files),'entropy_assertions':v['assertions_passed'],'bank_assertions':m['assertions_passed'],'drift_probe':probe['status'],'claim_version':5},indent=2))
