from pathlib import Path
import hashlib,json,datetime

RUN=Path(__file__).resolve().parents[1]
OWN=RUN.parents[1]
ROOT=OWN.parents[1]
RUN_ID=RUN.name
OLD=OWN/'runs/20261013T213857Z-account05-A095-restricted-result-extraction'
A097=ROOT/'agents/A097/runs/20261013T222610Z-account05-A097-cross-route-transfer'
A094=ROOT/'agents/A094/runs/20261014T001244Z-account05-A094-proof-chain-challenger'
A012=ROOT/'agents/A012/runs/20261013T220914Z-account05-A012-sparse-activation-accounting'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
results=json.loads((RUN/'out/EXACT_RESULTS.json').read_text())
pilot=json.loads((RUN/'out/PILOT.json').read_text())
assert results['status']==pilot['status']=='PASS'

def write(path,value):path.write_text(value,encoding='utf-8')
def dump(path,value):write(path,json.dumps(value,indent=2,ensure_ascii=False)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
sources=[PROTO,ROOT/'BOARD.md',ROOT/'claude/B19/STREAM_NOTES.md',OWN/'STATUS.md',OWN/'LEARNED.md',OLD/'CLAIMS.json',OLD/'DERIVATION.md',A097/'REPORT.md',A097/'CLAIMS.json',A097/'DERIVATION.md',A097/'BOUNDARY.md',A094/'REPORT.md',A012/'REPORT.md']
dump(RUN/'out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources])

oldclaim=json.loads((OLD/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
newstatement=oldclaim['exact_statement']+' Further complete-reference application: for every integer t>=2, Boolean children G(s,X), H(s,Y) sharing a uniform t-bit block s with disjoint arbitrary private cubes, fresh selector z and F=(G+H)/2+z(G-H)/2, put d=Inf_z(F), d*=min(d,1-d). Shared-collision minority mass delta obeys delta<=min(d*,2^t d*^2) and B_C<=h2(delta). Consequently Delta=H(F)-(H(G)+H(H))/2 <= (t+2+3/ln2)d*. Every supplied normalized finite-cost positive-support child reference can be calibrated at all shared-only atoms, decreasing CE by exact categorical KL; their lifted single normalized full-output reference Q retains exact debt D(P_F||Q)=(D(P_G||R_Gc)+D(P_H||R_Hc))/2 and CE_F<=(c_Gc+c_Hc)/2+(t+2+3/ln2)d*. I(F)=(I(G)+I(H))/2+d, counting shared physical bits once. Given supplied child CE bounds K_G I(G), K_H I(H), this closes CE_F<=max(K_G,K_H,t+2+3/ln2)I(F). If kappa_t=sup Delta/d* over all such children and private dimensions with 0<d*<=1/2, then t-1-log2(16/9)<=kappa_t<=t+2+3/ln2 for t>=4, and kappa_t/t tends to 1. These dimension-dependent transfers do not give an absolute selector-only coefficient, a universal arbitrary-terminal reference, or a full FEI bound.'
claim={
 'claim_id':'A095-RANK-KL-EQUIVALENCE','version':3,'exact_statement':newstatement,
 'hypotheses':[('Earlier activation application only: '+x if x.startswith('Shared controls') else x) for x in oldclaim['hypotheses']]+['The new selector application uses t>=2 arbitrary shared uniform bits and disjoint private cubes; it does not use the common-spine hypothesis of the earlier activation application','d*=min(d,1-d) is justified by sign folding; child spectra and all entropy costs are preserved','All references are calibrated and fixed before spectral sampling; complete off-target reference mass retained'],
 'statement_sha256':hashlib.sha256(newstatement.encode()).hexdigest(),
 'contributors':['A095; A097/A086 collision-calibration transfer and bent-flip lower witness credited as prior inputs'],
 'proof_source':{'original_equivalence':oldclaim['proof_source']['old_exact_equivalence'],'retained_v2':str(OLD/'DERIVATION.md'),'new_linear_tax_and_sharpness':str(RUN/'DERIVATION.md'),'validation':str(RUN/'out/EXACT_RESULTS.json')},
 'proof_dependencies':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':2,'status':'Earlier exact equivalence and paid applications retained unchanged; author-proved with independent review pending'},{'claim_id':'A097-ONE-SHARED-DATA-COLLISION-TRANSFER','version':1,'status':'Calibration identity and bent-flip witness reconstructed from cited DERIVATION and BOUNDARY; independently accepted by A094 stage 3 at full stated scope; larger-block exponential bound replaced only as an upper estimate, not refuted'},'Elementary Parseval, signed selector expansion, Jensen for binary entropy, scalar JS inequality, and all-parameter calculus in current DERIVATION'],
 'review_records':[], 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':2,'scope':'Prior statements retained; same C020 candidate extended with a linear all-overlap paid-reference application and sharp asymptotic tax'}],
 'refutes':[], 'first_unproved_line':None, 'next_consumers':['A094','A097','A086','A085','B19','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(RUN/'CLAIMS.json',[claim])

progress={
 'protocol_revision':protocol['revision'],'run_id':RUN_ID,'stream':'B19','packet_id':'A095',
 'gap_id':'C020-SHARED-COLLISION-NONREUSED-CORE-RESERVE',
 'attempt_id':'A095-stage3-minority-cap-linear-tax',
 'method':'Consume independently accepted A097 calibration/bent boundary; combine collision total-mass and per-coordinate caps, exact entropy concavity, rare-selector optimization, and normalized full-reference lifting',
 'mathematical_delta':'Replaces exponential shared-t selector tax by t+2+3/ln2, retains exact entire calibrated terminal debt, and proves asymptotically sharp leading coefficient kappa_t/t -> 1. No universal FEI constant changes.',
 'deliverable_status':'COMPLETE_LOCALLY_SAVED',
 'mathematical_status':'RESTRICTED_ALL_PARAMETER_THEOREM_AUTHOR_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':2},{'claim_id':'A097-ONE-SHARED-DATA-COLLISION-TRANSFER','version':1}],
 'claims_created_or_changed':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':3}],
 'source_artifacts':[str(RUN/'DERIVATION.md'),str(RUN/'out/SOURCE_MANIFEST.json'),str(RUN/'out/EXACT_RESULTS.json'),str(A097/'DERIVATION.md'),str(A097/'BOUNDARY.md'),str(A094/'REPORT.md')],
 'next_consumers':['A094','A097','A086','A085','B19','B20'],
 'next_action':'Construct or refute a signed nonreused child-slack reserve paying excess collision erasure, using the minority cap and the balanced bent/flip arbitrary-terminal stress test, retaining complete terminal CE and one physical influence budget.',
 'stagnant_substantive_attempts':0,'blockers':['No independently reviewed universal core-reserve payment; no universal arbitrary-terminal CE bound; new linear/sharpness theorem awaits independent review'], 'packet_ids':['A095']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)

report=f'''# A095 restricted-result extraction, stage 3

## exact target, quantifiers, hypotheses and units

For every t>=2, every pair of Boolean children G(s,X), H(s,Y) with a common t-bit fair block and arbitrary disjoint private cubes, extract a complete selector-reference transfer uniform in the private dimensions. Retain both entire supplied core costs and count shared physical influence once. Entropy, CE and KL are in bits; ln is natural logarithm. Ideal reference costs have a separate prefix-rounding convention. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the latest supervisor BOARD (01:10 UTC header on re-read), B19 STREAM_NOTES v2 (2026-10-11 23:35 UTC), own STATUS/LEARNED and full execution protocol v2. Prior original campaign/paper reads remain those in stages 1-2; no new external literature or priority claim is made. Read A097 stage-3 REPORT, CLAIMS, DERIVATION Sections 1-4 and BOUNDARY in full. Read A094 stage-3 REPORT (complete independent acceptance of that transfer and its balanced arbitrary-terminal stress test) and A012 stage-3 REPORT (opposite shared-literal case already paid). Consume those results rather than repeat the former STATUS target. B19's requested block reference was already closed in stages 1-2; no disagreement with the lead. File hashes and sizes are in out/SOURCE_MANIFEST.json. The A094 tensor strengthening is a proposed next stress test, not an assumed proof dependency in this theorem.

## complete derivation or exact first unsupported line

DERIVATION.md is the full all-parameter proof, including sign folding, collision entropy concavity, scalar JS, reference calibration, exact retained terminal debt and the bent/flip lower bound. Let d*=min(Inf_z,1-Inf_z). Shared collision minority mass delta satisfies delta<=min(d*,2^t d*^2). Jensen gives B_C<=h2(delta). Splitting at d*=2^-t and optimizing the rare-selector expression proves B_C<=(t+1/ln2)d*. Noncollision erasure <=2d* and JS<=2d*/ln2 give Delta<=(t+2+3/ln2)d*. For the single normalized lifted reference, CE=(c_Gc+c_Hc)/2+Delta and exact full debt is the average child calibrated debt. Under supplied child CE bounds, the root has constant max(K_G,K_H,t+2+3/ln2). No arbitrary child reference is silently declared paid.

The known bent point-flip witness has Delta/d*>=t-log2(16/9) for even t>=4. One dummy shared bit handles odd t. Together the upper bound proves kappa_t/t -> 1 over all private dimensions. Thus the selector-only collision tax has asymptotically sharp linear growth. The new result is the matching upper bound, not the already-known lower witness. No line of this restricted theorem is left unsupported. The first unsupported universal line is paying excess collision erasure from a specified nonreused child/core influence reserve while retaining arbitrary terminal costs. These examples refute an absolute selector-only extension, not FEI.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before either search. Commands from A095: `python -X utf8 runs\\{RUN_ID}\\code\\check.py pilot` and `python -X utf8 runs\\{RUN_ID}\\code\\check.py full`. Pilot: {pilot['exact_assertions']} exact assertions on 64 pairs, PASS, {pilot['elapsed_seconds']:.6f} seconds. Full: {results['exact_assertions']} assertions, PASS, {results['elapsed_seconds']:.6f} seconds. Exhaust all 256 three-bit G truth tables with shared bits 0,1 and private bit 2 against all 16 two-bit H tables: 4,096 labelled pairs without symmetry. Add 64 frozen two-private-child pairs, two direct bent/flip cases t=4,6, and 31 compressed bent/flip cases at even t=4..64. The largest actual parent cube has seven bits; large bent parameters use exact tensor-certified sign counts, not expanded truth tables. No exhaustive higher-dimensional claim is made.

Validation uses integer Walsh transforms, rational squared spectra, independent physical edge counts, normalized complete references, and exact ratio-mass equality proving the full KL identity formally. Bounds on entropy and linear-tax signs use rational logarithm enclosures: 24 atanh terms after binary range reduction, with tail <=2*y^49/[49(1-y^2)]. The printed timings are observational. Estimated memory 80 MB, not measured; no job expected above 300 MB, no heavy job or GPU, no automatic dimension increase. Finite checks support the proof; they do not replace its all-dimensional derivation.

## proof dependencies and changed downstream conclusions

This is version 3 of the existing A095-RANK-KL-EQUIVALENCE candidate: v2's equivalence/common-spine applications remain intact, and the same C020 complete-reference continuation gains a linear arbitrary-overlap estimate. No third broad pending candidate is opened. Earlier pivotal-height candidate remains unchanged and pending; stream review cap is respected by continuation of the existing mechanism and consumption of an independently audited dependency. A097's calibration/lift and bent witness are reconstructed directly, so no unproved stopping-tree or universal transfer is imported. A094 has independently accepted A097's full stated scope; this stage does not impersonate a new A094/A097 review. The exponential fallback is a valid but looser estimate, not a false theorem. Source statement SHA256 here means UTF-8 exact_statement bytes; imported originals are not rehashed under a different convention.

The result is a separate-manuscript-sized theorem with honest fixed-overlap scope and sharp asymptotic tax. It supplies a quantitative interface for shared-coordinate references while keeping the entire arbitrary-core FEI difficulty visible. No universal FEI constant changes, no mirror adoption or public release is claimed.

## one next mathematical action and independent reviewer

Target a signed nonreused child-slack reserve for collision erasure beyond a constant selector payment, starting with the new minority cap and A094's balanced bent/flip tensor carrying arbitrary terminal q. Keep the terminal CE term in the same inequality as one physical influence reserve. A097 or A094 should independently reconstruct the rare-selector optimization and exact debt; A085/A086 are reserve consumers. This changes the failed selector-only budget rather than enlarging the one-bit census.

## actual persistence receipts or precise save blocker

All four protocol files, DERIVATION.md, frozen spec, independent code, exact outputs, source manifest and byte/hash receipts are saved in this unique run. code/finalize.py verifies field sets, required headings, byte-identical progress compatibility copy, exact statement hash, two-line STATUS and the 20 MB file ceiling; out/PERSISTENCE_RECEIPTS.json records hashes. WORKLOG and LEARNED receive dated entries. Writes remain inside A095; persistence is local. No supervisor copy, remote receipt, independent acceptance of the new theorem or downstream use is asserted.

## Universal bridge

This stage advances C020 whole-set witness cost through its compatible complete-reference interface: the shared-t collision tax drops from exponential to t+2+3/ln2 while exact full terminal debt and one physical influence budget are preserved; its leading coefficient 1 is sharp. No dimension-independent bridge closes. What remains is an influence-owned, nonreused reserve for the excess collision term and an arbitrary-terminal reference payment. NEXT targets that exact obstruction using the minority-mass cap and balanced bent/flip terminal stress test, making it the shortest identified route toward full FEI rather than another fixed-overlap theorem.
'''
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
write(RUN/'REPORT.md',report)
write(OWN/'STATUS.md','STATE: A095 stage 3 complete locally: shared-t complete-reference tax <=t+2+3/ln2 with sharp leading coefficient 1, exact terminal debt retained; 62,481 exact assertions PASS; independent review pending; full FEI OPEN.\nNEXT: A097/A094 review linear-tax proof; derive nonreused child-slack collision reserve using minority cap and balanced bent/flip arbitrary-terminal stress test (C020).\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 stage 3 ('+RUN_ID+'): Consumed A012 opposite-literal closure and A097/A094 shared-data transfer. Replaced exponential overlap tax by linear t+2+3/ln2 using delta<=min(d*,2^t d*^2). Reconstructed normalized lift and exact terminal KL, paired with prior bent point-flip lower bound to prove kappa_t/t->1. Pilot 957 and full 62,481 exact assertions PASS (0.633 and 9.160 sec). No unsupported restricted line; universal nonreused child-reserve remains open. Saved v3 of existing candidate; no third broad pending claim.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14: For Boolean G(s,X),H(s,Y), t>=2 shared bits and disjoint private cubes, sign folding gives d*=min(d,1-d) without changing spectra or entropy increment. Shared conditional means imply each collision minority atom <=d*^2, total delta<=d*, hence B_C<=h2(delta)<= (t+1/ln2)d*. The rare regime uses x=2^t d* and monotonic x(1+t ln2-2ln x) on [0,1]. Complete calibrated-reference CE increment <=(t+2+3/ln2)d*; exact KL is the average entire child calibrated KL, including off-target reference normalizers. Known bent point flips plus a dummy shared coordinate imply t-1-log2(16/9)<=kappa_t<=t+2+3/ln2, so kappa_t/t->1. This is sharp selector tax, not FEI ratio growth. Absolute selector-only admission fails; child-owned slack and arbitrary terminal payment remain the real gap. Proof and exact rational checks in stage-3 DERIVATION/code/out.\n')

assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((OWN/'STATUS.md').read_text().splitlines())==2
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in [OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']:
    assert p.stat().st_size<20_000_000
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'scope':'LOCAL_ONLY','generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_fields':'PASS','statement_sha256':claim['statement_sha256'],'progress_identical':True,'files':receipts})
print(json.dumps({'status':'PASS','run_id':RUN_ID,'claim_version':3,'files_receipted':len(receipts),'exact_assertions':results['exact_assertions']}))
