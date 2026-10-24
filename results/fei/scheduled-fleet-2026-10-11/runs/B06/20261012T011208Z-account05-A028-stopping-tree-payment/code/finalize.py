from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
TEAM=AGENT.parents[1]
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
PREV=AGENT/'runs/20261011T221633Z-account05-A028-stopping-tree-payment'
stamp=datetime.now(timezone.utc).isoformat()

def digest(raw): return hashlib.sha256(raw).hexdigest()
def save(name,data):
    (RUN/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

protocol=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
out=json.loads((RUN/'out/full_validation.json').read_text(encoding='utf-8'))
assert out['cases']==6116 and out['assertions_passed']==55068
assert out['compute_seconds']<600
assert out['coefficient_four_countercertificate']['ratio_gt_4_integer_certificate']['left'] < out['coefficient_four_countercertificate']['ratio_gt_4_integer_certificate']['right']
pins=[]
def pin(path,scope):
    raw=path.read_bytes()
    pins.append({'path':str(path),'sha256':digest(raw),'bytes':len(raw),'scope':scope})
    return digest(raw)

pin(CANON/'EXECUTION_PROTOCOL.json','Reread complete current execution protocol')
pin(TEAM/'BOARD.md','Read at stage start; observed header 2026-10-12 01:21 UTC; hash captured at finalization of this mutable board')
pin(TEAM/'claude/B06/STREAM_NOTES.md','Read complete v2; assigned arbitrary indicator controller to A028')
pin(TEAM/'claude/B13/STREAM_NOTES.md','Actual path/leaf-partition interpretation and conserved budgets; no new telescope claim')
pin(TEAM/'claude/B16/STREAM_NOTES.md','Retained magnitude-KL sandwich scope, to distinguish J from actual Pi_H')
for who in ['A024','A057','A023','A097']:
    pin(TEAM/f'agents/{who}/LEARNED.md','New conventions, terminal/ownership guards consulted; not an unproved positive premise')
for name in ['REPORT.md','CLAIMS.json']:
    pin(TEAM/f'agents/A027/runs/20261011T234627Z-account05-A027-block-selection/{name}',
        'Consulted to avoid duplicate partial-core work; new theorem is not a proof premise')
prior_report_hash=pin(PREV/'REPORT.md','Retained A028 v1 point-control mismatch proof and prior source scope')
pin(PREV/'CLAIMS.json','Exact prior candidate version; original unchanged')
pin(TEAM/'context/threshold_paper_38pp.txt','Previously read terminal paper; this stage conditional controller examples use Theorems A/C/D and composition scope')
save('out/source_inventory.json',{'at':stamp,'sources':pins,'scope_note':'Mutable rolling hashes captured at finalization; no source or shared registry modified'})

cid='A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT'
statement=(
    'Version 2 retains version 1 point-control magnitude-KL payment: E sum J <= (3+log2(e)/e)Q and '
    'E sum(J+3log2(e)mu)<=kappa Q with kappa=3+log2(e)(3+1/e)<8. '
    'For every arbitrary uniform Boolean sign controller a=1-2c on a physical cube disjoint from '
    'a Boolean sign core u, p=Pr(a=-1), delta=Pr(u=-1), F=1+c(u-1), '
    'the actual control-first cost Pi_H=H(F)-pH(u) and queried influence Q=delta I(a) obey '
    'Pi_H<=delta Hplus(a)+C0 delta Var(a), C0=2+2log2(e)+log2(e)/sqrt(e)<6. '
    'Hence Hplus(a)<=T(I(a)-Var(a)) gives Pi_H<=max(T,C0)Q; ordinary controller FEI K gives '
    'Pi_H<=(K+C0)Q. With certified terminal allowance L I(u), complete expected path plus '
    'terminal cost is bounded by max(T,C0,L)I(F), respectively max(K+C0,L)I(F). '
    'All constants and mean orientations are included. Point-controller actual Pi_H<=6Q. '
    'The exact strong conjunction correction is bounded by (2+4log2(e)) times the unused '
    'variance deficit, yielding standard disjoint strong-certificate closure. '
    'Correction coefficient four is false already for dictator controller and two-bit point-defect '
    'core: Pi_H/Q=12-(9/2)log2(3)>4. A universal control-first rate for arbitrary controllers '
    'is FEI-equivalent in finiteness, with C_FEI<=K_ctrl<=C_FEI+C0.')
claim={
    'claim_id':cid,'version':2,'exact_statement':statement,
    'hypotheses':['Uniform independent physical cubes; Boolean sign core and 0/1 controller on DISJOINT coordinates',
                  'Entropy in bits; Hplus is the raw nonempty contribution, not conditional entropy',
                  'Control-only actual stopping tree determines c; all terminal core entropy retained',
                  'Controller and terminal certificates explicitly assumed for the conditional constant results',
                  'Nested controller modules have fresh physical supports; no shared-control extension'],
    'statement_sha256':digest(statement.encode('utf-8')),'contributors':['A028'],
    'proof_source':str(RUN/'REPORT.md'),
    'proof_dependencies':[{'claim':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@1',
                           'scope':'Only unchanged point-control KL component; new arbitrary-controller part proved independently',
                           'source':str(PREV/'REPORT.md'),'sha256':prior_report_hash,
                           'status':'AUTHOR_PROVED_INDEPENDENT_REVIEW_PENDING'},
                          'Exact actual physical-tree entropy/influence conservation, recovered C006/B06 R2',
                          'Elementary Parseval/Fourier tensor identities and explicit scalar convexity proof in current REPORT'],
    'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[{'claim_id':cid,'version':1,'reason':'Source-complete extension of same stopping-payment packet; no v1 theorem withdrawn'}],
    'refutes':[{'helper':'A028-ARBITRARY-CONTROLLER-CORRECTION-4','version':1,
                'statement':'Pi_H<=delta Hplus(a)+4delta Var(a) for every disjoint Boolean controller/core',
                'certificate':str(RUN/'out/full_validation.json')}],
    'first_unproved_line':None,
    'next_consumers':['A023','A024','A029','A057','A064','A065','A087','A094','A097','B20']}
save('CLAIMS.json',[claim])
progress={
    'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B06','packet_id':'A028',
    'gap_id':'C019','attempt_id':'A028-C019-arbitrary-control-partition-v2',
    'method':'Direct arbitrary-indicator spectral grouping, global semiconvex bias interpolation, exact physical-tree partition and rational certificates',
    'mathematical_delta':'Arbitrary-controller exact full path identity with C0<6 surcharge; controller/terminal max payment; point-controller actual Pi_H<=6Q; coefficient four refuted exactly; universal controller certificate explicitly FEI-equivalent',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
    'mathematical_status':'CONTROLLER_CERTIFICATE_TRANSPORT_PROVED_UNIVERSAL_FEI_OPEN',
    'claim_versions_used':['A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@1-point-component-author-proved',
                           'C006@recovered-physical-tree-conservation','B06-STREAM-NOTES@v2-direction',
                           'threshold-38pp@A-C-D-conditional-controller-terminal-examples'],
    'claims_created_or_changed':[{'claim_id':cid,'version':2,'status':claim['status']}],
    'source_artifacts':[str(RUN/'REPORT.md'),str(RUN/'DERIVATION.md'),str(RUN/'code/check.py'),
                        str(RUN/'out/full_validation.json'),str(RUN/'out/source_inventory.json')],
    'next_consumers':['A023','A024','A029','A057','A064','A065','A087','A094','A097','B20'],
    'next_action':'Derive signed single-use ownership correction for two activation events sharing exactly one physical control bit and acting on disjoint arbitrary core blocks; retain actual conditional controller and all weighted terminal core entropy',
    'stagnant_substantive_attempts':0,
    'blockers':['Arbitrary controller certificate is FEI-equivalent and unproved; no universal claim',
                'Shared control/core support invalidates pH(u); no overlapping ownership law proved',
                'Version 2 independent review, canonical adoption and mirror copy unobserved'],
    'packet_ids':['A028']}
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+k in report for k in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n')[-2]=='', 'Universal bridge ends in one paragraph'

state=('STATE: A028 stage 2 saved arbitrary-control full-path transport C0<6 and point-path rate6; coefficient4 refuted exactly; 6116 cases/55068 exact assertions; v2 review pending; full FEI OPEN.\n'
       'NEXT: A087/A094 review; derive one shared-control-bit ownership correction for two activation events with arbitrary disjoint cores and terminal entropy retained.\n')
(AGENT/'STATUS.md').write_text(state,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} — Stage 2 followed B06 v2 arbitrary-control assignment; A027 partial-core target not duplicated. Proved exact Pi_H and Hplus correction for arbitrary disjoint c/u, semiconvex empty-row correction C0=2+2log2(e)+log2(e)/sqrt(e)<6, certified-terminal max ledger, and point-path rate6. Dictator/point-defect3 witness refutes correction4 via 3^9<2^16. Universal controller payment remains FEI-equivalent. Pilot v1 passed in59.509s; outward dyadic rounding/cache v2 pilot0.179s. Full frozen6116 cases passed55068 assertions in104.698s under pre-amended600s ceiling. Same candidate extended to v2; no original/shared sources changed. Next: shared-bit ownership, not more fresh-module classes.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage 2: arbitrary control indicators

Lead B06 v2 assigns A028 arbitrary c(y), A027 partial-core exposure. For disjoint a=1-2c and core u, p=Pr(a=-1), delta=Pr(u=-1), F=1+c(u-1), Q=delta I(a), terminal influence/entropy pI(u)/pH(u). Hplus(F)=delta Hplus(a)+pHplus(u)+G, G=V_u eta(p^2)+V_u V_a/2+delta^2 V_a log2(1/delta^2). Actual Pi_H=delta Hplus(a)+G+phi(pdelta)-p phi(delta), phi(t)=eta((1-2t)^2).

Global phi''>=-24log2(e) gives convex phi+12log2(e)t^2 and the empty-row chord correction <=3log2(e)delta^2 V_a. Full Pi_H<=delta Hplus(a)+C0delta V_a, C0=2+2log2(e)+log2(e)/sqrt(e)<6 (rational upper2597/448). Controller Hplus<=T(I-Var) pays max(T,C0)Q; ordinary controller FEI K pays (K+C0)Q. Add weighted terminal cost from reserved pI(u), never recharge it.

Exact deficit composition residual D=4pdelta(1-p)(1-delta); G/D<=2+4log2(e)<8. Standard disjoint strong-certificate closure follows; scalar gate correction tends to this rate on actual almost-always-negative point-complement controllers, not an FEI disproof. Sequential fresh ordinary-certified controller modules preserve max(K0+C0,L) across depth.

Point controller Hplus<=6(I-Var) exactly, sharp for r=2; new ACTUAL point path Pi_H<=6Q. Do not conflate it with old magnitude-KL+linear upper bill: general J_tree<=Pi_H, but adding its full3mu/ln2 allowance may cost another3log2(e)Q.

Exact controller correction4 fails on dictator a and coreD2: Pi_H/Q=12-(9/2)log2(3)>4 by3^9<2^16. All leaves are certified. Setting u=-1 gives F=a, so universal arbitrary-controller rate is FEI-equivalent with C_FEI<=K_ctrl<=C_FEI+C0. Shared physical support invalidates pH(u), and two modules cannot own one control bit twice.

Full v2 certificate:6116 actual Boolean pairs,55068 assertions,104.698s; integer Walsh/edges, exact prime-log identities, outward rational atanh/dyadic signs. Cache bias-only interval expressions and outward-round to fixed denominator to prevent needless rational denominator growth; v1pilot59.509s became v2pilot0.179s on identical484 cases. Next universal mechanism is explicit single shared-bit ownership with arbitrary core terminals retained.
''')
receipt=[]
for q in sorted(RUN.rglob('*')):
    if q.is_file() and q.name!='persistence_receipt.json':
        raw=q.read_bytes()
        assert len(raw)<20*1024*1024
        receipt.append({'path':str(q.relative_to(RUN)),'bytes':len(raw),'sha256':digest(raw)})
save('out/persistence_receipt.json',{'at':stamp,'protocol_field_sets_checked':True,
                                    'progress_compatibility_equal':True,'artifacts':receipt,
                                    'schema_note':'packet_ids display annotation stripped; compatibility key is packet_ids',
                                    'mirror_status':'NOT_OBSERVED','independent_review_v2':'PENDING'})
print(json.dumps({'protocol_checks':'PASS','cases':out['cases'],'assertions':out['assertions_passed'],
                  'files':len(receipt),'run':str(RUN),'source_pins':len(pins)},indent=2))
