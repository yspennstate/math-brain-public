"""Persist the exact checked v9 package and validate protocol keys."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p): return p.read_text(encoding='utf-8-sig')
def js(p): return json.loads(read(p))
def write(p,s): p.write_text(s,encoding='utf-8',newline='')
def dump(p,x): write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
names=('check_pilot','check_full','independent','finite_label','obstruction')
results={k:js(R/'out'/f'{k}.json') for k in names}
assert all(x['status']=='PASS' for x in results.values())
assert results['check_pilot']['seconds']<60
assert results['check_full']['cases']==10560 and results['check_full']['seconds']<480
assert results['independent']['nodes']==166
old=js(R.parent/'20261023T063447Z-fleet03-A028-stopping-tree-payment/CLAIMS.json')[0]
reviews=js(R/'out/new_review_receipts.json')
protocol=js(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
claimid=old['claim_id']; consumers=['A029','A056','A087','A091','A094','A096','A097']
first=('An influence-priced ORIGINAL initial reference supplier for every Boolean input remains unproved. '
       'A prescribed necessary target outside the conditional posterior-channel image also needs a genuine payer; '
       'this theorem does not price arbitrary resets or supply universal FEI admission.')
next_action=('A029/A096: test a specified necessary stopping-class reference at the already-paid DATA frontier against '
             'the exact admissible posterior-channel image; if outside, expose its residual KL and an original unused payer. '
             'Do not repeat optional resets. Universal initial-reference admission remains the main open bridge.')
statement=('Version9 retains the prior scoped clauses and adds: for every finite-label selector L(Y) independent of shared data X, '
 'arbitrary Boolean sources g_j, and original support-positive source references R_j inherited through EACH source own physical '
 'phase kernel, let pi=law(L), q=sum pi P_j, r=sum pi R_j, W=sum pi D(P_j||R_j), alpha_j=pi_j P_j/q, '
 'rho_j=pi_j R_j/r, and k(U|t)=Pf(U,t)/q_t. For ANY history-adapted stochastic K_t(U|j) with alpha K=k, '
 'prescribe Q(U,t)=r_t(rho K)(U), completing zero-true rows at empty U. Then D(Pf||Q)=D(q||r)+C, '
 'C=sum q D(alpha K||rho K)<=Z=W-D(q||r), S=W-D(Pf||Q)>=0. W is a supermartingale under all physical '
 'DATA/CONTROL restrictions. Every finite adaptive mixed stopping tree obeys sum reach*(E Dchild-Dparent) '
 '+sum reach*(Wparent-E Wchild)+E Sleaf=Sroot, and the FULL entropy path plus full terminal CE equals '
 'Hroot+Wroot-sum reach*(Wparent-E Wchild)-E Sleaf<=Hroot+Wroot. For binary muxes whose nonempty '
 'controller SHAPE has already changed via the original inherited Ra of v8, admissible sector odds ell=rho*u+(1-rho)*v '
 'with alpha*u+(1-alpha)*v=b add C=sum q D(Bern(b)||Bern(ell))<=Zdata to D8; SAME original '
 'T=Wdata+gamma D(Pa||Ra) suffices and S9=Zdata-C+gamma Cvac>=0, with the same exact mixed-tree identity '
 'and no new liability or rate constant. Transport CURRENT Q through the actual output channel; raw reset equals '
 'signed debt increment plus actual erasure/outcome refunds. Both full terminal bills, vacuum KL, actual reference '
 'outcome normalizers, off-target mass and all previous debits remain. Exact admissible binary odds are the affine '
 'image of tau in [max(0,alpha+b-1),min(alpha,b)]. A Boolean odds-only witness with a=(-1,1,1,1), G=z,H=-z '
 'and dummy data d has H=I=2, W=Da=Z=0, alpha=rho=b=3/4; prescribed ell=1/2 costs (1/4)log2(27/16)>0 '
 'and lies outside the admissible image, refuting arbitrary odds-only payment from a tight quota but not FEI.')
hyp=[
 'Finite uniform independent control/data blocks, finite labels and arbitrary shared Boolean source functions.',
 'Original normalized references positive on true supports; reference-only mass retained and each source/controller uses its OWN inherited physical kernel and actual branch normalizer.',
 'At every node the SAME stochastic row channel is used on true/reference source-label posteriors and reproduces the true controller conditional law (or binary sector law). This is a genuine feasibility condition, not only a KL budget.',
 'Binary v8-shape extension keeps original Ra, full controller KL including vacuum, and all original source references; beta=0 forces ell=0; zero true rows retain reference mass at empty U.',
 'All actual output erasure/outcome refunds and both full terminal CE/KL bills are retained; signed costs are not clipped or replaced by a positive-part total.',
 'Any influence bound remains conditional on original admission Hroot+Troot+old_debit<=C Iroot; the previous conditional source/controller supplier corollary stays conditional.'
]
records=list(old['review_records'])
for x in reviews:
 records.append(dict(reviewer='A029/fleet03',reviewed_version=8,verdict='EXTERNAL_REVIEW_SOURCE_PINNED_SEE_EXACT_SCOPE',
                     scope='Earlier v8 supplied-reference scope only; no independent v9 acceptance inferred.',source=x['path'],source_sha256=x['sha256']))
claim=dict(claim_id=claimid,version=9,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A028'],
 proof_source=['DERIVATION.md sections1-5']+[f'out/{k}.json' for k in names],
 proof_dependencies=[{'claim':claimid+'@8','scope':'Original controller/source T account; fully reconstructed here, not assumed to supply universal admission.'},
                     {'claim':claimid+'@5','scope':'Prior influence-rate corollary only, explicitly conditional; not needed for the new KL theorem.'}],
 review_records=records,status='V9_AUTHOR_PROOF_EXACT_CHECKED; INDEPENDENT_PEER_REVIEW_PENDING; FULL_FEI_OPEN',
 supersedes=[{'claim_id':claimid,'version':8,'reason':'Adds admissible FULL conditional Markov profile references and DATA-row sector changes on already changed inherited v8 shapes, with SAME initial T.'}],
 refutes=[{'statement':'Any arbitrary DATA-row odds change can be paid from the original tight allowance without a supplier or extra liability.',
           'witness':'out/obstruction.json: H=I=2, source/controller liabilities0; true odds3/4, target1/2, extra=(1/4)log2(27/16)>0.',
           'scope':'Reference-payment obstruction; not a FEI refutation.'}],first_unproved_line=first,next_consumers=consumers)
dump(R/'CLAIMS.json',[claim])
delta=('Closed supplied-reference conditional Markov profile payment for arbitrary finite label selectors; exact posterior KL residual '
       'pays admissible full controller-profile changes. Extended v8 to genuine DATA-row odds changes after prior shape payment '
       'using EXACT SAME original T=Wdata+gamma Da and old debits, checked current-parent output inheritance. '
       'Certified distinct odds-only obstruction outside admissible image. No universal initial supplier or full FEI conclusion.')
artifacts=[dict(path=str(R/'DERIVATION.md'),sha256=sha(R/'DERIVATION.md'))]
for p in sorted((R/'out').glob('*.json')):
 if p.name not in ('artifact_manifest.json','validation.json'):
  artifacts.append(dict(path=str(p),sha256=sha(p)))
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B06',packet_id='A028',gap_id='C019',attempt_id='A028-stage20-v9-admissible-posterior-channels',
 method='Exact KL chain rule/data processing; physical phase-sensitive source/output inheritance; finite-label conditional Markov kernels; rational Walsh spectra and prime-log certificates.',
 mathematical_delta=delta,deliverable_status='COMPLETE_LOCAL_ARTIFACTS; PEER_REVIEW_AND_SUPERVISOR_PUBLICATION_PENDING',
 mathematical_status='SCOPED_SUPPLIED_REFERENCE_THEOREM_PROVED_AND_EXACT_CHECKED; UNIVERSAL_C019_AND_FULL_FEI_OPEN',
 claim_versions_used=[claimid+'@8',claimid+'@5 (conditional influence corollary only)'],claims_created_or_changed=[claimid+'@9'],
 source_artifacts=artifacts,next_consumers=consumers,next_action=next_action,stagnant_substantive_attempts=0,
 blockers=[first,'Independent peer review of v9 pending; direct-character verification is an independent implementation, not an independent reviewer.',
           'Brain self-care degraded/unverified: stale owner-model, state-of-mind and dream evidence; personalized owner-state assumptions and self-care freshness are affected.',
           'Shared governor snapshot stale; not claimed as current resource clearance. Jobs stayed below the 300MB admission threshold.'],packet_ids=['A028'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
f=results['check_full']; ind=results['independent']; fl=results['finite_label']
report=f'''# A028 B06 stage20: admissible posterior-channel stopping payment (v9)

## exact target, quantifiers, hypotheses and units

For every finite adaptive physical restriction tree, pay the full entropy path and both full terminal cross-entropy bills from one ORIGINAL account. All entropy, CE and KL are in bits. This stage closes the supplied-reference case for any finite-label selector and any admissible conditional Markov reference. For binary muxes it also pays genuine DATA-row odds changes AFTER the inherited nonempty controller shape has changed, from EXACT SAME v8 T=Wdata+gamma Da. It does not supply universal influence-priced root admission. See CLAIMS.json for all quantified hypotheses and DERIVATION.md for complete formulae.

## sources actually read, revisions and theorem locators

Read current BOARD.md, B06 STREAM_NOTES.md, own STATUS/LEARNED/prior v7-v8 packages; protocol revision {protocol['revision']}; required campaign indices/plan, supplementary sources and the threshold/percolation text interfaces as recorded in intake receipts. Current A029 LEARNED supplies its v8 original-T/occupancy-debit frontier; A056 distinguishes true-law CE from entropy under a reference. A096 warns against another optional reset loop; A097 records the phase/profile gap. Pins and extracted context are in out/context_receipts.json; external review sources are pinned in out/new_review_receipts.json. Prior v7 scoped independent acceptance is retained without promoting it to v9 acceptance. No shared input was modified.

## complete derivation or exact first unsupported line

DERIVATION.md sections1-5 prove the result. Given true/reference source posteriors alpha,rho and SAME stochastic kernel K with alpha K equal to the actual controller conditional law, KL chain rule gives D(alpha||rho)=D(alpha K||rho K)+conditional posterior KL. Thus the changed conditional reference costs at most the ORIGINAL source-label slack. In the finite-label case D= W-S. In the already changed binary v8 case D9=T-(Z-C+gamma Cvac), C<=Z, with unchanged T. Source/controller physical KL releases make W or T a supermartingale on all mixed histories. Its telescope pays the complete entropy path plus full terminal CE, retaining the current output reference refunds and both child bills. The exact feasible binary interval is supplied, and general finite-label couplings are constructed rationally.

The distinct Boolean odds-only obstruction has H=I=2 and zero original liabilities; target odds1/2 instead of3/4 adds (1/4)log2(27/16)>0. Strict sign is the integer certificate27>16. This is a payment obstruction, not a FEI counterexample.

First unsupported universal line: {first}

## executed validation with domain, arithmetic, commands and outputs

Frozen before computation: out/FROZEN_SPEC.json. No symmetry reduction; exact Fraction Walsh spectra and prime-log vectors, with outward rational log enclosures for necessary signs. Memory estimate180MB; no job expected above300MB, no GPU, no detached work or automatic dimension increase. Timing is performance evidence only.

- `python -X utf8 code/check.py pilot`: PASS {results['check_pilot']['cases']} cases, {results['check_pilot']['queries']} queries, {results['check_pilot']['assertions']} assertions; {results['check_pilot']['seconds']:.3f}s, below60s.
- `python -X utf8 code/check.py full`: PASS {f['cases']} cases, {f['queries']} physical-query checks, {f['assertions']} assertions, {f['positive_row_cost_visits']} positive row-cost visits; {f['seconds']:.3f}s, below frozen480s. Controllers through2bits and source data through1bit, all Boolean truth tables, two references per controller/source and three declared couplings; three additional seven-variable fixed/adaptive policies switch AFTER DATA queries.
- The seven-variable fixture keeps I=45/16, old U=4I=45/4 and old debit1/8. Its original T and reserve are EXACTLY the v8 vectors, with no new liability, quota or depth factor; both terminal bills and CURRENT changed-parent inheritance are checked.
- `python -X utf8 code/prepare_independent.py` then `python -X utf8 code/independent.py`: PASS {ind['nodes']} nodes, {ind['leaves']} leaves, {ind['assertions']} checks, {ind['changed_row_node_visits']} changed row-node visits; separate direct-character transform and conditional-posterior implementation, without importing main checker. This is independent implementation, not independent peer review.
- `python -X utf8 code/finite_label.py`: PASS; three-label actual selector, full controller-profile quantile coupling and complete mixed tree. Details: out/finite_label.json.
- `python -X utf8 code/obstruction.py`: PASS; actual four-variable Boolean witness and strict integer odds-only certificate. Details: out/obstruction.json.

All commands above run from this run directory; preparation copied pinned old helpers within A028 only. Two attempted quoted inline reads failed before executing; subsequent file reads and checks succeeded. Those access failures supplied no mathematical evidence.

## proof dependencies and changed downstream conclusions

The supplied-reference v8 T account is reconstructed in section5; the v5 root influence-rate premise remains conditional. New posterior-chain proof is self-contained. Consumers may now use SAME T for admissible row odds after changed shape, or use the general finite-label conditional-profile theorem, without rebilling a source/controller supplier. They must check channel feasibility and retain every original liability/refund. Prior JS-only and new odds-only guards prevent claiming arbitrary target payment. No root supplier, unbounded H/I family, positive-part cost bound or universal FEI claim is created. Independent peer review of v9 is pending.

## one next mathematical action and independent reviewer

{next_action} A029 is requested reviewer through this source-bound handoff; A056/A094 can check the original allowance and reference supplier. No external message was sent.

## actual persistence receipts or precise save blocker

All results saved locally in this unique A028 run, with code and outputs. CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json have exact protocol keys; out/artifact_manifest.json pins saved artifacts and out/validation.json records read-back verification. STATUS.md is two lines and WORKLOG/LEARNED are updated. No save blocker; supervisor publication/mirror verification remains pending, no git run. Final saved at {now}. No calculation is left running by the final handoff.

Universal bridge: C019 now includes arbitrary finite-label admissible conditional-profile changes and binary sector-odds changes on an ALREADY changed controller shape, for ALL finite mixed stopping trees, with zero increase in the original v8 T liability or conditional influence constant. What remains is influence-priced initial admission for every Boolean input and any necessary target outside the exact feasible channel image. Testing one necessary stopping-class target against that image, exposing its residual and an original payer when infeasible, is the shortest next route to universal FEI; another optional reset or isolated class enumeration would not close the missing admission.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A028 v9 saved exact admissible conditional Markov profile payment for all finite-label mixed trees; binary row odds after paid shape use SAME original T; finite checks PASS; peer review pending; FEI OPEN.\nNEXT: '+next_action+'\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as w:
 w.write(f'\n{now} — stage20/v9: {delta} Full run10560cases/25893queries/4312259checks PASS; independent166nodes/10785checks PASS; finite-label and odds-only certificates PASS. Same7variable old4I/debit/reserve. v9 peer review pending; universal supplier still open. Saved {R.name}.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as w:
 w.write('\n## v9 admissible posterior-channel payment\nFor any finite-label selector with shared Boolean sources, SAME row kernel K on true/reference source-label posteriors, reproducing actual controller law, costs C<=conditional source-label KL Z exactly, with posterior KL residual. Supplied-reference W remains a physical mixed-history supermartingale. For v8 changed controller SHAPE, binary admissible row odds add C<=Z and use SAME T=Wdata+gamma Da: S9=Z-C+gamma Cvac. Signed physical output refunds are retained from CURRENT Q. Binary feasibility is affine tau in [max(0,alpha+b-1),min(alpha,b)], not arbitrary KL affordability. If alpha=rho, admissible odds are unchanged. Actual a=pointdefect2,G=z,H=-z,dummy d with exact references has H=I=2,T=Z=0; changing ONLY odds3/4 to1/2 costs(1/4)log2(27/16)>0. General finite-label quantile couplings give genuine full-profile changes. Initial universal influence-priced reference supplier remains open; a necessary outside-image target still needs an original payer. v9 independent peer review pending.\n')
# Validate exact keys and persistence only after all writes have succeeded.
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
pk=[x.split(' (')[0] for x in required['progress_fields']]
assert set(progress)==set(pk)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
assert read(R/'REPORT.md').strip().splitlines()[-1].startswith('Universal bridge:')
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ('artifact_manifest.json','validation.json')]
assert all(p.stat().st_size<20*1024*1024 for p in files)
manifest={str(p.relative_to(R)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(files)}
dump(R/'out/artifact_manifest.json',manifest)
validation=dict(status='PASS',claim_fields_exact=True,progress_fields_exact=True,packet_delta_identical=True,status_two_lines=True,
                statement_hash_verified=True,all_files_under20MB=True,all_five_mathematical_outputs_PASS=True,
                saved_files=len(files),timestamp_utc=now,peer_review='PENDING_V9',full_fei='OPEN')
dump(R/'out/validation.json',validation)
print(json.dumps(validation))
