from pathlib import Path
import json, hashlib, datetime

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]; TEAM=AGENT.parents[1]
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def receipt(p):
    b=p.read_bytes(); return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
protocol=read(PROTOCOL)
prior=AGENT/'runs'/'20261011T221240Z-fleet05-A097-cross-route-transfer'
previous=AGENT/'runs'/'20261012T005449Z-fleet05-A097-cross-route-transfer'
referee=TEAM/'agents'/'A086'/'runs'/'20261013T220217Z-fleet05-A086-joint-code-referee'
ownership=TEAM/'agents'/'A091'/'runs'/'20261013T220323Z-fleet05-A091-composition-referee'
spine=TEAM/'agents'/'A095'/'runs'/'20261013T213857Z-fleet05-A095-restricted-result-extraction'
tree=TEAM/'agents'/'A039'/'runs'/'20261012T040116Z-fleet05-A039-projection-under-restrictions'
deps=[]
for folder,cid,scope in [(prior,'A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','Prior theorem; one-node KL identity reconstructed directly here'),(referee,'A086-DISJOINT-SELECTOR-PRESCRIBED-REFERENCE','Author-proved pending review; collision packet and scalar JS lemmas independently reconstructed here, no full claim acceptance assumed')]:
    c=next(c for c in read(folder/'CLAIMS.json') if c['claim_id']==cid)
    deps.append(dict(claim_id=cid,version=c['version'],statement_sha256=c['statement_sha256'],source=str(folder/'CLAIMS.json'),status=scope))

statement=('For all Boolean G(s,X),H(s,Y) with one shared fair physical bit s, disjoint private uniform blocks X,Y and a fresh fair selector z, and normalized complete finite-cost references R_G,R_H, calibrate each reference separately on the two atoms empty and {s} to the true Fourier probabilities and rescale its complement. Costs c_G^c,c_H^c do not increase; the exact decrease is the categorical KL of those two atoms and the complement. The normalized compatible reference Q=rK, r=(R_G^c+R_H^c)/2 and K the actual conditional selector spectrum with a fixed normalized kernel on zero true fibers, has zero posterior mismatch kappa and D(P_F||Q)=[D(P_G||R_G^c)+D(P_H||R_H^c)]/2. Its complete cost is CE_F=(c_G^c+c_H^c)/2+Delta<=(c_G^c+c_H^c)/2+(2+4/ln2)Inf_z(F), where F=(G+H)/2+z(G-H)/2, Delta=B_z+J_z and I(F)=[I(G)+I(H)]/2+Inf_z(F), including s only through its actual averaged influence. Thus supplied child bounds transfer with constant max(K_G,K_H,2+4/ln2). For a t-bit shared block the same constant holds if both conditional-mean Fourier vectors have l1 norm <=1; without that hypothesis a proved coefficient is 2+(2*2^(t/2)+2)/ln2. No absolute selector-only coefficient holds for unrestricted sharing: selecting the even-k quadratic bent sign and its actual singleton flip has Inf_z=2^-k and Delta/Inf_z>=k-log2(16/9) for every even k>=4. This is a scoped reference transfer and an actual Boolean obstruction to its unrestricted selector-only extension, not a disproof of FEI.')
hypotheses=['Boolean signs on finite uniform physical cubes; one shared bit, private blocks disjoint, selector fresh; private blocks may be empty','Normalized complete references fixed before the spectral sample, positive on true supports and with finite cross entropy','Both collision atoms calibrated separately; all complement normalizers and complete calibrated seed costs retained','All information units bits, ordinary total physical influence; ideal costs with separate integer-word rounding','Larger shared-block extension uses the expressly stated l1 admission or the dimension-dependent coefficient; no repeated allocation of selector or shared data influence']
claim=dict(claim_id='A097-ONE-SHARED-DATA-COLLISION-TRANSFER',version=1,exact_statement=statement,hypotheses=hypotheses,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A097'],proof_source=dict(run_id=RUN.name,files=['REPORT.md','DERIVATION.md','BOUNDARY.md','TRANSFER_HYPOTHESIS_CHECK.json','code/check.py','code/check_boundary.py','out/EXACT_RESULTS.json','out/BOUNDARY_RESULTS.json']),proof_dependencies=deps,review_records=[],status='AUTHOR_PROVED_SCOPED_TRANSFER_AND_BOOLEAN_BOUNDARY_PENDING_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A086','A094','A011','A012','A095','A039','A064','B20'])
save(RUN/'CLAIMS.json',[claim])
next_action='Derive a signed excess-collision payment from certified terminal core slacks beyond l1 admission, retaining one exclusive core budget; use the bent-defect selector as a necessary stress test. A086 primary independent reviewer, A094 alternate.'
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B20',packet_id='A097',gap_id='G-R-MISMATCH',attempt_id='A097-CROSS-ROUTE-COMPATIBLE-REFERENCE-3',method='Transfer A086 Renyi collision-packet and JS lemmas into A097 compatible reference with two-atom calibration; conditional-mean l1 admission; exact Boolean obstruction to unrestricted selector-only payment',mathematical_delta='Closed one-shared-data-bit admission with the same selector coefficient 2+4/ln2 as disjoint children and exact calibrated debt retention; explicit t-shared coefficient; unrestricted absolute selector-only extension rigorously ruled out by bent/point-flip family',deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_TRANSFER_PROVED; GENERAL_SELECTOR_ONLY_EXTENSION_REFUTED; UNIVERSAL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',claim_versions_used=deps,claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=['REPORT.md','DERIVATION.md','BOUNDARY.md','TRANSFER_HYPOTHESIS_CHECK.json','out/FROZEN_SPEC.json','out/BOUNDARY_FROZEN_SPEC.json','out/EXACT_RESULTS.json','out/BOUNDARY_RESULTS.json','out/SOURCE_RECEIPTS.json'],next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['Universal non-l1 collision/core-slack payment remains unpaid; arbitrary terminal reference bounds remain hypotheses'],packet_ids=['A097'])
save(RUN/'PROGRESS.json',progress); save(RUN/'PACKET_DELTA.json',progress)
save(RUN/'TRANSFER_HYPOTHESIS_CHECK.json',dict(source_lemma='A086 RECONSTRUCTION disjoint interface: phi(A,B)<=2sqrt(AB)/ln2 and JS<=2Inf_z/ln2',target_missing_term='Previously nonempty shared data collision {s} in B_z; exact induced complete-reference posterior debt',substitution=dict(A='(Ghat(T)+Hhat(T))^2/4',B='(Ghat(T)-Hhat(T))^2/4',T=['empty','{s}'],collision_bound='sum |a_T^2-b_T^2|/(2ln2)<=2Inf_z/ln2',new_hypothesis_verified='Conditional means on one fair bit have Fourier l1<=1; coefficient difference <=2Inf_z'),reference_calibration='Both collision atoms individually, not just empty; categorical KL decrease explicit',posterior_credit='kappa=0; calibrated terminal debt remains exactly averaged',physical_budget='I_root=(I_G+I_H)/2+Inf_z; shared s is not separately queried or charged',constant='2+4/ln2',failed_generalization='Unrestricted collision coefficient: bent/point-flip Delta/Inf_z>=k-log2(16/9)',first_unpaid_line='Price excess non-l1 collision packets using certified seed slack without repeated allocation'))

sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B20'/'STREAM_NOTES.md',prior/'REPORT.md',previous/'DERIVATION.md',previous/'CLAIMS.json',referee/'REPORT.md',referee/'RECONSTRUCTION.md',referee/'CLAIMS.json',ownership/'OVERLAP_INTERFACE.md',spine/'REPORT.md',tree/'TREE_TARGET.md']
save(RUN/'out'/'SOURCE_RECEIPTS.json',[receipt(p) for p in sources])
res=read(RUN/'out'/'EXACT_RESULTS.json'); boundary=read(RUN/'out'/'BOUNDARY_RESULTS.json')
report=f'''# A097 stage 3: transfer into the nonempty shared collision

## exact target, quantifiers, hypotheses and units

For all Boolean cores G(s,X), H(s,Y), allow one shared physical data bit s, arbitrary disjoint private blocks, and a fresh fair selector z. Supply normalized complete finite-cost seed references; costs are in bits and influence is ordinary physical influence. Close the nonempty collision left open by A086's disjoint-child interface, retaining both complete calibrated seed bills. The result is CE_F <= (c_G^c+c_H^c)/2+(2+4/ln2)Inf_z. Calibration costs are expressly accounted for. Supplied bounds c_j<=K_j I(j) yield constant max(K_G,K_H,2+4/ln2); no arbitrary seed bound is proved. Ideal reference costs and any integer-word rounding are separate.

## sources actually read, revisions and theorem locators

Read BOARD at its 2026-10-13 22:25 UTC snapshot, B20 STREAM_NOTES v2, own STATUS/LEARNED/WORKLOG, and protocol v2. B20's recorded B05 task was completed in stage 2; this stage consumes the newly explicit A086 one-shared-data target. No disagreement with the lead. Read A086 stage-3 REPORT, RECONSTRUCTION's disjoint prescribed-reference section and CLAIMS; A091 OVERLAP_INTERFACE's exclusive ownership and unpaid conversion; A095 stage-2 REPORT's calibrated activation; A039 TREE_TARGET's complete-terminal Bellman ledger; own prior transfer and B05 derivation/claim. Source paths and byte hashes are in out/SOURCE_RECEIPTS.json. A091's overlapping CONTROL events are not equated to the shared DATA selector here. No new external literature dependency was used.

## complete derivation or exact first unsupported line

DERIVATION.md supplies the complete all-dimensional proof. Calibrate the seed atoms empty and {{s}} individually to their true probabilities and rescale the complement. The exact CE decrease is a three-cell categorical KL; conditional complement debt persists. Lift their mixture through the true signed selector kernel. On both shared-only atoms the true/reference posteriors agree, and every other true nonzero fiber identifies a unique child. Therefore kappa=0 exactly and root KL is the average complete calibrated seed KL.

The actual missing erasure term is phi((a_T+b_T)^2/4,(a_T-b_T)^2/4) at T={{s}}. Substituting into A086's Renyi packet lemma bounds it by |a_T^2-b_T^2|/(2ln2). Conditional means on a single bit imply ||a||_1,||b||_1<=1 and ||a-b||_infinity<=2Inf_z. Thus both collision packets together cost at most 2Inf_z/ln2. The noncollision erasure costs at most 2Inf_z; scalar JS costs at most 2Inf_z/ln2. This closes the exact formerly missing term with coefficient 2+4/ln2. The shared s influence enters only its actual average child influence; no separate reset account is used.

For t shared bits the same proof gives coefficient 2+(2*2^(t/2)+2)/ln2, or the original constant under l1<=1 admission. BOUNDARY.md proves there is no absolute selector-only coefficient for unrestricted overlap: the actual even-k bent sign and its singleton flip have Delta/Inf_z>=k-log2(16/9). Exact leaf laws already exhibit this obstruction. Total core influence is retained, so this is not an FEI counterexample. First unsupported universal line: allocate excess non-l1 collision erasure to quantitatively certified terminal seed slacks without double spending; arbitrary terminal reference payment also remains open.

## executed validation with domain, arithmetic, commands and outputs

Specs were frozen before execution. No symmetry quotient: all 256 ordered two-bit core pairs and all 4,096 ordered three-bit/two-bit pairs sharing s, with exact, uniform and increasing-weight normalized references (13,056 reference cases). Maximum root dimension five. Integer Walsh transforms and physical edges are separate representations; Fraction arithmetic verifies spectra, masses, posterior calibration and influence ownership. Prime-log coefficient maps certify the exact CE/KL identities; 40-term rational atanh enclosures certify inequalities, with remainder 2 z^81/[81(1-z^2)] after reduction to [1,2). No floating sign is accepted.

Commands, from A097:

    python -X utf8 runs/{RUN.name}/code/check.py
    python -X utf8 runs/{RUN.name}/code/check_boundary.py

Final transfer PASS: {res['assertions']:,} assertions, {res['family_cases']:,} Boolean pairs, {res['reference_cases']:,} reference cases, {res['seconds']:.3f} seconds. Boundary PASS: {boundary['assertions']} assertions in {boundary['seconds']:.3f} seconds; frozen even k=4,6,8,10,12, with direct Walsh verification at k=4,6 and compressed exact sign counts otherwise. The analytic proofs establish the infinite domains, not extrapolation. An initial weaker coefficient 2+6/ln2 passed 255,249 checks; its spec/results are preserved as INITIAL files. The sharper conditional-mean estimate warranted the final rerun in the same domain. Memory estimates 90 MB and 30 MB, below the memok trigger; no heavy job, background process or dimension increase occurred.

## proof dependencies and changed downstream conclusions

The exact substitution is in TRANSFER_HYPOTHESIS_CHECK.json. A097's compatible-reference lemma and A086's scalar packet/JS lemmas are the source-bound dependencies; their needed portions are reconstructed locally. A086's whole interface is not labeled independently accepted by this application. A011/A012/A095 can now admit a single shared data coordinate with varying magnitudes while retaining calibrated core debt. The unrestricted selector-only continuation is rigorously blocked, so future overlapping-core work must state a seed reserve instead of silently assuming a constant selector tax. This is a scoped continuation, not another broad universal candidate. Full FEI remains OPEN, and this new claim awaits independent review.

## one next mathematical action and independent reviewer

{next_action} This tests the exact universal obstruction that appears once bounded collision admission fails, rather than extending another already-paid activation census. No message to another agent was sent, and no review completion is assumed.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, DERIVATION.md, BOUNDARY.md, source-bound substitution, frozen specs, code and exact outputs are saved in this run. code/finalize.py checks protocol field sets, statement hash, compatibility equality and file sizes; out/PERSISTENCE_RECEIPTS.json records hashes and rolling-file receipts. STATUS has exactly two lines; dated WORKLOG and durable LEARNED entries are saved. Local persistence only; supervisor copying, mirror adoption and independent acceptance are unverified.

Universal bridge: This stage moves C020 whole-set reference cost and C024 history transfer by closing the first nonempty shared-data collision with zero posterior mismatch, exact calibrated terminal debt, and the same 2+4/ln2 selector coefficient as disjoint children. It also proves an actual Boolean obstruction to any absolute selector-only extension across unrestricted overlap; no universal FEI constant improves. Excess non-l1 collision payment and arbitrary terminal reference costs remain unpaid. NEXT is the shortest identified route toward full FEI because it forces a named, nonreused seed-slack reserve at precisely the collision that defeats absolute selector payment, rather than adding another isolated class with the same unresolved universal debt.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A097 stage 3 complete: one-shared-data collision reference transfer paid at 2+4/ln2; unrestricted selector-only payment refuted by actual bent/flip family; 259,627 exact checks PASS; FEI OPEN; review pending.\nNEXT: A086/A094 review; derive signed excess-collision payment from certified terminal seed slacks beyond l1 admission with one exclusive core reserve.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now}: Stage {RUN.name}: consumed A086 nonempty shared-data collision target, A091 ownership and A095 calibration. Two-atom calibration plus compatible lift retains averaged complete calibrated seed debt with kappa=0. Conditional means sharpened selector coefficient from 2+6/ln2 to 2+4/ln2. 4,352 labelled pairs/13,056 references: 259,601 exact assertions PASS; five bent/flip boundary cases: 26 PASS. All-dimensional proof and Delta/Inf_z>=k-log2(16/9) obstruction saved. Full FEI OPEN, independent review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 3 durable transfer: For G(s,X),H(s,Y) with one shared bit and disjoint private data, calibrate BOTH shared-only atoms empty,{s}; the CE decrease is the three-cell categorical KL. The compatible root reference has kappa=0 and D_root=(D_Gcal+D_Hcal)/2, including all complement normalizers. Conditional means give collision vectors l1<=1 and max_T|a_T-b_T|<=2Inf_z. Thus B_collision<=2Inf_z/ln2, B_noncollision<=2Inf_z, JS<=2Inf_z/ln2, and full CE<=avg calibrated seedCE+(2+4/ln2)Inf_z. Shared s influence is avg child influence, not a second account.\n\nFor t shared bits, calibrate all shared-only atoms: coefficient 2+(2*2^(t/2)+2)/ln2; if both conditional-mean Fourier l1 norms<=1 retain 2+4/ln2. Unrestricted dimension-independent selector-only admission is FALSE even with exact references: quadratic bent b and b-2*1_zero have selector influence delta=2^-k and Delta/Inf_z>=k-log2(16/9) for even k>=4. This does not disprove FEI because the terminal core influence is large. Any universal extension must name and allocate an additional core slack reserve.\n')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[p for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(RUN/'out'/'PERSISTENCE_RECEIPTS.json',dict(saved_at=now,protocol_schemas='PASS',statement_hash_convention='SHA256 exact_statement UTF-8; hypotheses stored separately, matching prior A097 runs',statement_hash='PASS',exact_assertions=res['assertions']+boundary['assertions'],local_only=True,independent_review='PENDING',mirror_verified=False,files=[receipt(p) for p in files],rolling_files=[receipt(AGENT/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]))
for item in read(RUN/'out'/'PERSISTENCE_RECEIPTS.json')['files']: assert receipt(Path(item['path']))==item
print(json.dumps(dict(schema='PASS',hashes='PASS',files=len(files),exact_assertions=res['assertions']+boundary['assertions'],full_FEI='OPEN')))
