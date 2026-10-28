"""Persist protocol records and audit their exact field sets. No shared writes."""
from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
checks=json.loads((root/'out/CHECKS.json').read_text(encoding='utf-8'))
repair=json.loads((root/'out/REPAIR_CHECKS.json').read_text(encoding='utf-8'))
assert checks['status']==repair['status']=='PASS'
stmt=('For m>=8, d=2^(1-m), L=floor(1/(md)), N=mL, let f be a zero-vertex flip of the product of L m-bit point signs, and a=d-2^(1-N). For every invertible affine physical input change (A,b), the KL of its squared Fourier law to its own actual marginal product is at least N*h2(a)-H(f), with equality in original coordinates. Its minimum over (A,b), even allowing Walsh character phases, divided by ORIGINAL I(f), exceeds (14m-83)/17. The source is full-support and affinely multiplicatively indecomposable, 7/8<I(f)<17/16 and H(f)<69/16. Nevertheless the explicit UNFLIPPED template spectrum Q is full-support and satisfies H(f)+KL(fhat^2||Q)<5*I(f) in the original coordinates. This follows from the general finite-template bound CE(fhat^2,Fhat^2)<=H(F)+2*sqrt(epsilon)*max_S log2(1/Fhat(S)^2), where f,F are Boolean and differ on an epsilon fraction of inputs and F has full Fourier support. No universal FEI claim or bound using transformed I is asserted.')
claim=dict(claim_id='A062-INDECOMPOSABLE-BOUNDED-INFLUENCE-ADMISSION-OBSTRUCTION',version=2,
 exact_statement=stmt,hypotheses=['Finite uniform Boolean cube, entropy and KL in bits','m integer >=8; budget is original physical influence','Affine input map invertible; marginal reference recomputed for transformed source','Template repair uses explicit full-support unflipped product spectrum; arbitrary references are not interchangeable'],
 statement_sha256=hashlib.sha256(stmt.encode()).hexdigest(),contributors=['A062'],
 proof_source=str(root/'PROOF.md'),proof_dependencies=['Stage21 construction, rederived in this run PROOF.md sections1-4','Finite Parseval, binary entropy concavity and TV expectation bound, proved or explained in PROOF.md','Previously established finite entropy/KL telescopes used only for the stated no-installation corollary'],
 review_records=[],status='PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=['A062-INDECOMPOSABLE-BOUNDED-INFLUENCE-ADMISSION-OBSTRUCTION@1'],
 refutes=['Unregistered repair allowing a freely selected affine basis for an O(ORIGINAL I) actual marginal-product KL source supplier'],
 first_unproved_line='Supply a noncircular ORIGINAL O(I) full nonproduct reference/template for an arbitrary Boolean core, or one necessary selected rule avoiding this admission, retaining old debits, signed E/O and all full terminals.',
 next_consumers=['A061','A063','A064','A065','A087','A094','B13'])
expected=set(protocol['required_per_run']['claim_fields']); assert set(claim)==expected
(root/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8',newline='\n')
progress=dict(protocol_revision=protocol['revision'],run_id=root.name,stream='B13',packet_id='A062',
 gap_id='C019-ORIGINAL-REFERENCE-OWNER-ADMISSION',attempt_id='A062-stage22-affine-minimum-and-template-repair',
 method='Exact directional counting, affine minimization, finite-template cross-entropy perturbation bound',
 mathematical_delta='Affine-selected actual marginal-product admission fails at unbounded cost/ORIGINAL I on SAME affine-prime full-support bounded-H bounded-I family; original basis is exact minimizer. Explicit block-nonproduct template pays FULL initial CE<5I on SAME family. Universal supplier remains open.',
 deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_PROOF_PENDING_REVIEW_FULL_FEI_OPEN',
 claim_versions_used=['A062-INDECOMPOSABLE-BOUNDED-INFLUENCE-ADMISSION-OBSTRUCTION@1 (rederived, extended to v2)','A087-PRODUCT-HISTORY-SIGNED-COCYCLE-INSTALLATION@1 via A065 stage20 reconstruction, capital hypothesis retained'],
 claims_created_or_changed=[claim['claim_id']+'@2'],
 source_artifacts=[str(root/'PROOF.md'),str(root/'FROZEN_SPEC.json'),str(root/'FROZEN_REPAIR_SPEC.json'),str(root/'out/CHECKS.json'),str(root/'out/REPAIR_CHECKS.json'),str(root/'out/LEAN.json'),str(root/'out/SOURCE_READS.json')],
 next_consumers=claim['next_consumers'],next_action=claim['first_unproved_line']+' A087/A094 reconstruct (1), affine minimum, and full CE template repair.',
 stagnant_substantive_attempts=0,blockers=['Universal initial arbitrary-core source remains unpaid','Independent mathematical review pending','Lean core admission held; no formal certificate','Remote archival and downstream use are supervisor-owned and unverified'],packet_ids=['A062'])
fields={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}; assert set(progress)==fields
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    (root/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8',newline='\n')
(agent/'STATUS.md').write_text('STATE: A062 stage22: affine-selected marginal-product KL fails; ORIGINAL basis exact minimum; SAME explicit nonproduct template pays FULL CE<5I; '+str(checks['checks'])+'+'+str(repair['checks'])+' exact checks PASS; review/FEI OPEN.\nNEXT: A087/A094 review v2 affine minimum and template repair; supply ORIGINAL nonproduct O(I) template/reference for arbitrary core, keeping old debits, signed E/O and all full terminals.\n',encoding='utf-8',newline='\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n'+now+' stage22 '+root.name+': exact all-affine marginal-product minimum and divergent ORIGINAL-I admission; SAME full nonproduct template CE<5I repair; '+str(checks['checks'])+' primary + '+str(repair['checks'])+' repair checks PASS. Lean core admission held; no compiler started. No universal claim. Artifacts local, supervisor archival unverified.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\nStage22: For the stage21 one-point-flipped equal-width point product, a nonzero direction touching t blocks has influence [1-(1-2d)^t]/2+(-1)^t u, u=2^(1-N). Every directional marginal lies in [d-u,1-d+u], so binary entropy is >=h2(d-u). Original axes attain the floor: min over ALL affine actual-marginal-product reference KL equals ORIGINAL TC, and minKL/ORIGINAL I>(14m-83)/17. Character phases do not change TC. Do not replace original I by transformed I: affine changes can increase it. SAME family has explicit unflipped-template nonproduct reference Q with FULL CE=H+KL<5 ORIGINAL I. General lemma: if Boolean f,F differ on epsilon fraction, Fhat^2 has full support and code lengths <=M, then CE(fhat^2,Fhat^2)<=H(F)+2sqrt(epsilon)M, by spectral TV and bounded score expectation. Tiny/zero reference atoms are a real hypothesis; no arbitrary-core paid template is supplied. Primary and repair exact checks PASS; formal admission held; v2 independent review pending.\n')
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='receipts.json':
        b=p.read_bytes(); assert len(b)<20_000_000
        receipts.append(dict(path=str(p.relative_to(root)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
(root/'out/receipts.json').write_text(json.dumps(dict(at=now,files=receipts,remote_mirror='NOT_VERIFIED',schema_checks='PASS'),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(status='PASS',protocol_field_sets='EXACT',primary_checks=checks['checks'],repair_checks=repair['checks'],files=len(receipts),bytes=sum(r['bytes'] for r in receipts))))
