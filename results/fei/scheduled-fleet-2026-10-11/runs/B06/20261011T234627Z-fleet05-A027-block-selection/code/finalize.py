import json, hashlib
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
campaign=Path('~/mop_fei100/reports/fei-2026-10-11')
team=agent.parents[1]
previous=agent/'runs'/'20261011T215911Z-fleet05-A027-block-selection'
review=team/'agents'/'A087'/'runs'/'20261011T221055Z-fleet05-A087-restriction-referee'
lead=team/'claude'/'B06'/'STREAM_NOTES.md'
now=datetime.now(timezone.utc).isoformat()

def dump(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

validation=json.loads((run/'out'/'validation.json').read_text(encoding='utf-8'))
certificate=json.loads((run/'out'/'overhead_certificate.json').read_text(encoding='utf-8'))
assert validation['status']==certificate['status']=='PASS'
certlo,certhi=map(Q,certificate['Pi_H_over_Pi_I_rational_enclosure'])
assert certlo>Q(8193,2048)
dump('out/strong_surcharge_sign.json',{'status':'PASS','exact_lower_threshold':'8193/2048','exported_lower_bound':str(certlo),'exported_upper_bound':str(certhi),'consequence':'The helper Pi_H(F)<=p Pi_H(u)+4 Pi_I(F) is false on the actual fixed Boolean core z*D_32 activated by 16 fresh controls','arithmetic':'Exact Fraction comparison of the outward rational enclosure; not a decimal sign'})

reviewed=json.loads((review/'CLAIMS.json').read_text(encoding='utf-8'))
prior=[c for c in reviewed if c['claim_id'] in ('A027-DATA-FIRST-PROPER-BLOCK','A027-CORE-BLOCK-HARDNESS')]
assert len(prior)==2
assert all(c['status']=='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A087' for c in prior)
dump('out/CONSUMED_REVIEWS.json',{'observed_at':now,'review_source':str(review/'CLAIMS.json'),'verdicts':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status'],'review_records':c['review_records']} for c in prior],'scope':'Stage-1 hypotheses remain; source originals untouched; new transport is not independently reviewed'})

statement=('For every uniform Boolean core u, r>=1 fresh point controls with p=2^(-r), F=1+A_r(u-1), and finite adaptive physical core-only restriction tree T, the lifted actual leaf partition obeys Pi_I(F)=p*Pi_I(u) and |Pi_H(F)-p*Pi_H(u)|<=(12+8/ln(2))*Pi_I(F), with all remaining-core entropy and terminal control reserve retained. For proper-core stopping trees with Pi_H(u)<=K*Pi_I(u) and C001-regular core terminals, H(F)<=max(K+12+8/ln(2),C_reg)*I(F). In particular u=chi_[t]*g with t>=1 and regular g on at least one remaining core coordinate admits the proper character-block rule H(F)<=(12+8/ln(2))*I(F), even for g=D_s where core density tends to zero. A universal forward activation surcharge exactly 4 is refuted by the actual proper-core example u=z*D_32, r=16: the certified Pi_H(F)/Pi_I(F)>8193/2048 while Pi_H(u)=0. The iterated r->infinity then s->infinity surcharge limit on u=z*D_s is 4.')
deps=['C001@threshold_paper_38pp-Theorem-A','C006@BLOCK_RESTRICTION_IDENTITY_2026-09-18-sections-1-3']
new={'claim_id':'A027-PARTIAL-CORE-ACTIVATION-TRANSPORT','version':1,'exact_statement':statement,'hypotheses':['Uniform normalized Boolean Fourier spectrum; entropy in bits','Fresh point-indicator controls remain unqueried throughout the core stopping partition','Finite actual core restriction tree, no repeated coordinate on a path; core-first rule stops before exhausting the core','The terminal-inclusive implication explicitly assumes a paid core partition and C001-regular core leaves'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A027'],'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':deps,'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':None,'refutes':['FORWARD-ACTIVATION-SURCHARGE-4 (new explicit helper, not the unrelated amplitude-proxy K=4)'],'first_unproved_line':None,'next_consumers':['A028','A029','A064','A065','A087','A094','A097']}
claims=prior+[new]
dump('CLAIMS.json',claims)
nextaction=('Use the exact signed J_p correction as a labelled reserve when selecting a proper core partition, and test it against A029 terminal deficits on arbitrary-core activations; require regular/point-defect leaves and retain pH(core). Do not charge the Lipschitz surcharge repeatedly to the same core influence.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B06','packet_id':'A027','gap_id':'G-R-SELECT','attempt_id':'A027-G-R-SELECT-002','method':'Affine rarity cancellation plus globally Lipschitz bias correction on the actual core leaf partition; martingale variation paid by queried influence','mathematical_delta':'Universal partial-core activation transport at additive rate kappa=12+8/ln2<24, with complete terminal payment for regular leaves. Proper low-density character/regular-core partition proved; exact actual Boolean witness refutes surcharge 4. Two stage-1 reviews consumed at scope.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT; NEW_CLAIM_REVIEW_PENDING','mathematical_status':'PROVED_UNIVERSAL_TRANSPORT_AND_RESTRICTED_SELECTION; UNIVERSAL_CORE_SELECTION_AND_FULL_FEI_OPEN','claim_versions_used':deps+['A027-DATA-FIRST-PROPER-BLOCK@1 (A087 review consumed)','A027-CORE-BLOCK-HARDNESS@1 (A087 review consumed)'],'claims_created_or_changed':['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@1','A027-DATA-FIRST-PROPER-BLOCK@1 review record copied','A027-CORE-BLOCK-HARDNESS@1 review record copied'],'source_artifacts':['DERIVATION.md','ADAPTIVE_BLOCK_SELECTION.tex','BLOCK_CONTROLS.md','FROZEN_SPEC.json','VALIDATION_EXTENSION.json','code/check.py','code/overhead_certificate.py','out/pilot.json','out/validation.json','out/overhead_certificate.json','out/strong_surcharge_sign.json','out/FAILED_CERTIFICATE.md','out/CONSUMED_REVIEWS.json','SOURCE_READS.json'],'next_consumers':['A028','A029','A064','A065','A087','A094','A097'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['A universal paid proper-core partition with certified leaves remains unproved','Independent review of the new bundled claim and supervisor mirror/adoption are not observed'],'packet_ids':['A027']}
dump('PROGRESS.json',progress)
dump('PACKET_DELTA.json',progress)

sources=[]
for path,scope in [
    (campaign/'EXECUTION_PROTOCOL.json','Read in full, current revision 2026-10-11-execution-v2'),
    (team/'BOARD.md','Read at stage opening; B05/B06/B16 and reviewer results prioritized'),
    (lead,'Read in full: v2 23:26Z; followed assigned proper partial-core target'),
    (previous/'DERIVATION.md','Not present; proof carried in ADAPTIVE_BLOCK_SELECTION.tex'),
    (previous/'ADAPTIVE_BLOCK_SELECTION.tex','Prior derivation and original density boundary; not re-enumerated'),
    (previous/'CLAIMS.json','Original exact statement hashes retained'),
    (review/'CLAIMS.json','A027 v1 independent verdicts and proof provenance'),
    (review/'REPORT.md','A027 review and terminal-boundary guards'),
    (team/'agents'/'A028'/'runs'/'20261011T221633Z-fleet05-A028-stopping-tree-payment'/'INDEPENDENT_REVIEW.md','Independent A027 reconstructions read in full; arbitrary-control work not duplicated'),
    (team/'context'/'threshold_paper_38pp.txt','Definition (4), Theorem A; C001 regular terminal bound and activation baseline'),
    (Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md'),'Previously read exact physical block identities; consumed baseline, not rediscovered')]:
    if path.exists():
        data=path.read_bytes(); sources.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'read_scope':scope})
dump('SOURCE_READS.json',{'observed_at':now,'sources':sources,'review_queue_note':'A087 and A028 accepted both prior A027 v1 claims at stated scope. This stage finishes the already assigned partial-core continuation and bundles its transport, terminal certificate and surcharge guard as one new claim.'})

report=f'''# A027 stage 2 — Proper partial-core activation transport

Full FEI remains OPEN. The lead-directed partial-core transport is proved locally, with a complete certified-terminal consequence and an exact surcharge obstruction. A087/A094 review of the new bundled claim is pending.

## exact target, quantifiers, hypotheses and units

All outputs are Boolean signs, input cubes uniform, Fourier coefficients normalized, entropy in bits. For every Boolean core u, r>=1 fresh point controls, p=2^-r and F=1+A_r(u-1), lift an actual finite adaptive core-only stopping tree to F, leaving controls unqueried. Pi_H is the full entropy drop to the actual weighted leaf partition; Pi_I is weighted actual queried influence. The proper-subset rule stops with at least one core coordinate unqueried on every path.

The new universal transport is |Pi_H(F)-p Pi_H(u)|<=kappa Pi_I(F), kappa=12+8/ln2<24, and Pi_I(F)=p Pi_I(u). Thus a specified core payment Pi_H(u)<=K Pi_I(u) transfers to Pi_H(F)<=(K+kappa)Pi_I(F). With C001-regular core leaves (including constants), activated leaves are regular and H(F)<=max(K+kappa,C_reg)I(F). This does not assert a paid core partition exists universally.

The proved proper low-density selection class is u=chi_[t]*g, t>=1, with regular g on s>=1 remaining coordinates. Query only the character block: Pi_H(u)=0, activated charge<=kappa*p, and the complete constant is kappa. For g=D_s, I(u)/(s+t)->0, so the old density condition cannot be substituted as its proof.

## sources actually read, revisions and theorem locators

Read BOARD.md and B06 STREAM_NOTES.md v2 (23:26Z), own rolling status and learned facts, and the execution protocol revision 2026-10-11-execution-v2. The lead owns the tree reduction baseline and explicitly assigned A027 proper partial-core transport; A028's arbitrary-control indicator target is separate. The lead's objection that the old dense-core condition already gives core FEI is accepted and retained.

A087's stage-1 CLAIMS.json and A027 review section accept both prior claims at scope; A028's INDEPENDENT_REVIEW.md independently reconstructs the same two claims. These reviews are consumed without changing old source artifacts or repeating the old census. The relevant regularity definition (4) and Theorem A in the current 38-page threshold text supply C001. The physical block telescope is the previously read C006 source, not a new result claimed here. SOURCE_READS.json gives observed SHA256 pins and exact scope. No new external literature priority claim is made.

## complete derivation or exact first unsupported line

DERIVATION.md gives a complete proof, with ADAPTIVE_BLOCK_SELECTION.tex as the formal theorem deliverable. Direct unbalanced Fourier summation gives H(F)=pH(u)+G_p(delta), retaining all empty coefficients. Remove the affine term 8rp*delta from G_p to obtain J_p; it cancels exactly across any actual leaf partition. The global derivative bound |J_p'|<=p(24+16/ln2) includes delta=0,1/2,1. Actual minority probabilities form a finite reveal martingale, and weighted absolute mean-bias variation is <=Pi_I(u)/2 because each mean difference is no greater than the physical node disagreement. Their combination proves the complete entropy transport independently of core dimension, depth, rarity and child bias. Remaining-core entropy is still in every F_l terminal.

Point activation preserves a regular negative indicator's total desirability order: put oriented controls first and inherit the data order. This supplies actual C001-regular activated terminals. Their influence sum is p E I(u_l)+2rp*delta, disjoint from the queried p Pi_I(u) budget. In the character/regular-core rule the core entropy drop is exactly zero. For D_s, the positive terminal is D_(s+r), while the negative terminal has regular negative event A_r*(1-A_s).

The exact surcharge on u=zD_s tends to 4 as r->infinity then s->infinity. The actual fixed witness s=32,r=16 has an outward rational interval strictly above 8193/2048>4, so surcharge exactly 4 is false even with certified terminals. This is a precise helper refutation; H/I remains bounded.

First unsupported universal line: for every Boolean core choose a proper stopping partition with Pi_H(u)<=K Pi_I(u), one absolute K, and regular/point-defect terminals. The new theorem transfers such a partition, but does not supply it. Revealing a character in an arbitrary g leaves the full entropy of g at terminals; no hidden arbitrary-core leaf is declared easy.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before the pilot. Every Boolean table at m=2,3 is tested with r=1,2,3. There are 4,704 proper nonempty fixed-core subset partitions and 6,912 declared adaptive policies (root 0, then independently stop or query 1/2 in each child). Every leaf retains a core coordinate. There is no symmetry quotient or dimension escalation. The pilot tested 96 partitions and passed 1,443 assertions in 0.094 seconds.

Full command: `python -X utf8 runs\\{run.name}\\code\\check.py`. It passed {validation['assertions']:,} assertions in {validation['elapsed_seconds']:.3f} seconds across 11,616 partitions plus 90 explicit symbolic low-density parameter triples. Exact integer Walsh spectra, independent physical edge counts, actual restricted truth tables, terminal reserves and regularity order certificates are checked. Signed formal sums of rational logarithms retain exact zero cancellations; 22-term rational atanh-series bounds with proved remainders certify the comparisons. Identity intervals are consistency validation, not a replacement for the analytic identity proof. Rational rate 24 is used in finite sign certificates; the analytic theorem proves the sharper kappa.

VALIDATION_EXTENSION.json freezes the separate actual Boolean compressed-spectrum witness s=32,r=16, t=1. Command: `python -X utf8 runs\\{run.name}\\code\\overhead_certificate.py`. Its three histogram normalizations and physical influence partition are exact, and its rational log enclosure gives the sign above 4. out/strong_surcharge_sign.json certifies the stronger bound above 8193/2048 by exact Fraction comparison. No 2^49 cube is enumerated. Mathematical runtime was {certificate['elapsed_seconds']:.3f} seconds. All jobs were estimated below 100 MB, so the >300 MB memok gate did not apply; no GPU was used.

Two auxiliary failures are preserved in out/FAILED_CERTIFICATE.md: an unsupported guessed upper sign below 4 failed, then direct serialization of a huge Fraction denominator hit Python's digit cap. The guess was withdrawn; exact OUTWARD rounding to denominator 2^64 fixed export without increasing any conversion limit. The Boolean witness, frozen domain and rational arithmetic did not change. Neither failure affected the proved safe transfer constant or the main census.

## proof dependencies and changed downstream conclusions

The positive transfer uses the directly proved arbitrary-bias activation identity, elementary finite probability, the inherited physical influence telescope, and C001 only for the certified-terminal implication. Prior v1 claims are review continuity and calibration, not an assumed universal payment. Their A087 records are copied into this stage's CLAIMS.json at unchanged version and exact statement hash. One new bundled downstream claim is created, covering transport, regular-terminal closure, the explicit proper-subset class and the surcharge guard.

A028/A029/A064/A065/A097 can now lift a genuinely paid core leaf partition without a dimension or child-bias logarithm surcharge. They must still pay Pi_H(u), preserve pH(core) at arbitrary terminals, and spend queried influence once. This new rate is for complete Pi_H=B+M, not only an amplitude proxy or singleton erasure. A universal surcharge 4 is refuted for this helper; the B06 lead's unrelated instruction to retire amplitude-proxy K=4 searches is respected.

## one next mathematical action and independent reviewer

{nextaction} This targets the unpaid core selection/terminal deficit, rather than collecting more dense or character-core classes. Fresh nested point controls on one unchanged core collapse to a single point indicator, so merely stacking them is not a new mechanism. A087 is the primary independent reviewer; A094 is the alternate. No review of the new bundled claim or message delivery is asserted.

## actual persistence receipts or precise save blocker

All four protocol files, code and exact outputs, both packet deliverables, DERIVATION.md, frozen specs, source pins and failure record are saved inside this run. STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md are updated without changing old run files or any shared source tree. out/PERSISTENCE_RECEIPT.json records observed hashes and byte sizes, exact claim/progress field checks, report field checks, and identical PROGRESS/PACKET_DELTA content. Supervisor copying, canonical adoption and independent review of the new claim are pending; local saves are not mirror receipts.

## Universal bridge

This stage advances C019 and the lead's proper partial-core target by completely bounding the activation transport correction at additive rate kappa=12+8/ln2<24 for every actual core leaf partition, with complete regular-terminal payment and a growing low-density proper-subset rule. It removes the old core-density requirement from the transport step, and records an actual Boolean obstruction to dropping its surcharge to 4. The remaining universal gap is a paid proper CORE partition with certified leaves; arbitrary terminal entropy remains explicit. NEXT applies the exact signed correction as a nonreusing reserve against that core selection/terminal deficit. That is the shortest universal continuation because activation rarity and child bias are now bounded, while another isolated class or a repeated charge to the same influence would leave the core FEI-strength debt untouched.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: Stage 2 universal partial-core activation transport proved locally; 149,883 assertions and exact surcharge>4 certificate PASS; prior v1 claims independently accepted; full FEI OPEN.\nNEXT: Use the exact signed bias correction as a nonreusing reserve in proper-core selection with paid terminal deficits; A087/A094 review the new bundled transport theorem.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — {run.name}: Followed B06 v2 proper partial-core target; consumed A087/A028 acceptance of both v1 claims. Proved |Pi_H(F)-pPi_H(u)|<=kappa Pi_I(F), kappa=12+8/ln2<24, by affine rarity cancellation and a globally Lipschitz bias row. Preserved actual remaining-core entropy and control reserve; regular activation closure gives a proper low-density character/point-defect rule. Frozen 96-case pilot and 11,616-partition full validation plus90 symbolic cases passed149,883 assertions in15.123s. Additional exact compressed witness u=zD_32,r=16 refutes surcharge4 (>8193/2048). Failed guessed upper sign and huge-Fraction export are preserved and corrected via exact outward rounding. One new bundled claim awaits A087/A094; universal core partition and FEI remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage 2: proper partial-core transport and its surcharge

Both stage-1 claims were independently accepted at scope by A087 and A028. B06 lead's correction is right: I(u)>=eta*m already makes that core an easy entropy class; it cannot be a universal exclusion argument.

For fresh point activation F=1+A_r(u-1), any finite actual core-only leaf partition has Pi_I(F)=pPi_I(u) and |Pi_H(F)-pPi_H(u)|<=(12+8/ln2)Pi_I(F). Direct H(F)=pH(u)+G_p(delta) retains all empty rows; J_p=G_p-8rp*delta has global derivative <=p(24+16/ln2). The affine part cancels across physical leaves. Mean-bias martingale variation <=Pi_I(u)/2 pays the correction without a dimension, rarity or bias logarithm. Remaining core entropy and 2rp*delta terminal control influence are retained.

Activation preserves C001 regularity by putting oriented control coordinates first in the regular negative indicator's desirability order. A paid core partition at K with regular leaves therefore gives full activated constant max(K+12+8/ln2,C_reg). The premise is explicit; no universally paid core partition is proved.

u=chi_[t]*g, g regular on remaining data, has proper character-block core entropy drop0, queried activated influence pt, and full bound H(F)<=(12+8/ln2)I(F). For g=D_s, core density tends to zero. Positive terminal is D_(s+r); negative terminal A_r*(1-A_s) is regular. Arbitrary g instead retains full difficulty at those leaves.

Necessary surcharge: u=zD_s, query z only; exact iterated r->infinity then s->infinity Pi_H/Pi_I limit is4. Its finite s32,r16 ratio is rigorously >8193/2048>4 (approximately4.00049328 only for display). Thus surcharge4 fails for this helper; it is distinct from amplitude-proxy K4. The failed guess that the ratio approached4 from below is withdrawn. Huge Fraction export is fixed by exact outward rounding to denominator2^64, preserving sign and without raising Python's conversion limit.

Validation: 4,704 fixed and6,912 adaptive proper-core partitions over all m2,3 cores and r1,2,3 activations;90 symbolic low-density parameter cases;149,883 exact assertions in15.123s. Separate compressed Fourier certificate avoids2^49 enumeration. New bundled claim remains independently unreviewed. Next universal gap is a genuinely paid core partition/terminal deficit, not activation transfer or another dense-core class. Fresh nested point controls on one core collapse to one indicator; repeated application must not spend the same core influence again.
''')

protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claimkeys=set(protocol['required_per_run']['claim_fields'])
progresskeys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==claimkeys for c in claims)
assert set(progress)==progresskeys
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert all(field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('This stage advances C019')
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for path in sorted(run.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPT.json':
        data=path.read_bytes(); assert len(data)<20*1024*1024
        files.append({'path':str(path.relative_to(run)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
for path in (agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md'):
    data=path.read_bytes(); files.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump('out/PERSISTENCE_RECEIPT.json',{'observed_at':now,'local_save':'VERIFIED','protocol_fields':'PASS','compatibility_copy':'IDENTICAL','files':files,'new_claim_independent_review':'PENDING','supervisor_mirror':'NOT_OBSERVED'})
print(json.dumps({'local_save':'VERIFIED','protocol_fields':'PASS','files':len(files),'new_claims':1,'prior_claims_with_consumed_acceptance':2,'surcharge_4':'REFUTED_EXACTLY','full_fei':'OPEN'},indent=2))
