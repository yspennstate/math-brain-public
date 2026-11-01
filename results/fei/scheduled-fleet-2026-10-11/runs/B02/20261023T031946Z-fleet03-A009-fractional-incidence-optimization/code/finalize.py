from pathlib import Path
import json, hashlib
from datetime import datetime,timezone

R=Path(__file__).resolve().parents[1]; A=R.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
S6=BASE/'agents/A006/runs/20261023T000406Z-fleet03-A006-posterior-forest-optimization'
S10=BASE/'agents/A010/runs/20261022T231523Z-fleet03-A010-universal-residual-falsifier'
stamp=datetime.now(timezone.utc).isoformat()
def save(name,x):
    (R/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
full=json.loads((R/'out/full.json').read_text(encoding='utf-8'))
pilot=json.loads((R/'out/pilot.json').read_text(encoding='utf-8'))
assert full['status']==pilot['status']=='PASS'
sources=[S6/'DELETED_DEGREE_TWO.md',S6/'CLAIMS.json',S10/'GROWING_MATCHING.md',S10/'CLAIMS.json',BASE/'BOARD.md',BASE/'claude/B02/STREAM_NOTES.md',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
pins=[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources]
save('out/SOURCE_PINS.json',pins)
source=json.loads((S6/'CLAIMS.json').read_text(encoding='utf-8'))[0]
source['review_records'].append({'reviewer':'A009','verdict':'HOLDS; whole version independently reconstructed without substantive repair; local adoption only','timestamp_utc':stamp,'proof_source':str(R/'REVIEW_A006.md'),'finite_validation':'out/full.json: independent exact forests, Walsh and physical-boundary checks','formal_status':'NOT_LEAN_CHECKED'})
source['status']='INDEPENDENT_A009_REVIEW_HOLDS; SHARED_REGISTRY_ADOPTION_NOT_PERFORMED'
def claim(cid,statement,hyp,proof,deps):
    h=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    return dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=h,contributors=['A009'],proof_source={'path':str(R/proof),'checker':'code/check.py','exact_output':'out/full.json'},proof_dependencies=deps,review_records=[{'reviewer':'A009','verdict':'AUTHOR_ANALYTIC_PROOF_WITH_EXACT_FINITE_AUDIT; NOT INDEPENDENT_AGENT_ACCEPTANCE','timestamp_utc':stamp,'formal_status':'NOT_LEAN_CHECKED'}],status='AUTHOR_CHECKED_PROOF; INDEPENDENT_AGENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A006','A008','A010','A086','Claude/B02','B20'])
positive=claim('A009-GROWING-DELETED-DEGREE-COMPLETE-COST',
 'For every labelled bipartite H on integers4<=a<=b with maximum degree at most integer0<=d<=a/2, let G=K_ab minus H and f_G its actual uniform Boolean positive edge DNF. Fix precisely its surviving width-two primes, both endpoint orders, pi=1/4 and lambda_e=1/b. The SAME original nonempty-conditioned all-partitions queue complete nonempty output cost obeys C/I(f_G)<91/8+2 b^2 2^(2d-b)/(1-2^(-(b-d))). Consequently C<22I for d<=a/4, and C<15I whenever a^2 4^d<=2^a. These are feasible fixed-reference complete-cost upper certificates, not optimality assertions.',
 ['Uniform independent physical bits; Walsh normalization and logarithms in bits.','Both left and right deletion degrees are at most d; all surviving primes and the same original queue reference are retained.','C=sum over nonempty A of fhat_G(A)^2 log2(1/Q_G(A)); original root conditioning D=(1+1/(4b))^|G|-1.'],
 'GROWING_DEGREE.md',[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'use':'whole-version A009 review HOLDS; only general half-dense transfer clause needed'}])
obstruction=claim('A009-HALF-DENSE-DEFECT-LOG-PAYMENT-OBSTRUCTION',
 'For every m>=2 take a=b=2m, delete the two within-index K_mm blocks, and retain the two disjoint crossed K_mm blocks. With E the physical event that both active sides are nonempty but no surviving edge is active, u=2^-m, the actual Boolean influence is I=8m u^2(1-u)(2-u) and J=I(1_E)=8m u^2(1-u). Thus J/I=1/(2-u)>1/2, and J log2 b/I is unbounded along m=2^t despite every surviving degree being half the opposite side. No universal bound J log2 b<=K I holds for all half-dense graphs. This is a transfer-bill obstruction, not a lower bound on complete queue cost, not a variational obstruction and not a disproof of FEI.',
 ['Uniform physical cube; E is the exact completion-defect event.','I and J are sums of physical flip probabilities, not arbitrary spectral laws.'],
 'HALF_DENSITY_OBSTRUCTION.md',[])
save('CLAIMS.json',[source,positive,obstruction])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B02',packet_id='A009',gap_id='C020-SAME-REFERENCE-GROWING-DELETION-OCCUPATION',attempt_id='A009-stage7-growing-degree-and-half-density-obstruction',method='Consume and independently review A006 whole claim; anchored physical biclique count and exact joint defect energy; actual-Boolean obstruction to universal coarse label payment.',mathematical_delta='A006 whole version HOLDS locally. Pay same-reference growing deletion degree with C<22I at d<=a/4, C<15I at a^2 4^d<=2^a. Exhibit half-dense actual family with unbounded J log b/I.',deliverable_status='COMPLETE_LOCAL_ARTIFACTS; SUPERVISOR_COPY_AND_SHARED_ADOPTION_NOT_PERFORMED',mathematical_status='RESTRICTED_PAYMENT_PROVED_AND_EXACTLY_AUDITED; COARSE_UNIVERSAL_PAYMENT_REFUTED; FULL_FEI_OPEN',claim_versions_used=[{'claim_id':source['claim_id'],'version':1,'status':'INDEPENDENT_A009_HOLDS'}, {'claim_id':'A010-GENERIC-WIDTH-TWO-FOREST-MASS','version':1,'status':'INDEPENDENTLY_RECONSTRUCTED_IN_REVIEW_A006'}],claims_created_or_changed=[{'claim_id':source['claim_id'],'version':1,'change':'local independent review record only'}, {'claim_id':positive['claim_id'],'version':1,'change':'new author-checked theorem'}, {'claim_id':obstruction['claim_id'],'version':1,'change':'new actual Boolean route obstruction'}],source_artifacts=pins,next_consumers=['A006','A008','A010','A086','Claude/B02','B20'],next_action='Replace the joint J log b bill by component/sector-sensitive occupation within the SAME reference; require it to pay the crossed-biclique obstruction before a universal claim.',stagnant_substantive_attempts=0,blockers=['Full FEI requires universal same-reference occupation payment, still open.','New claims await independent-agent review; shared registry adoption and supervisor mirrors not verified.','Brain self-care personal-state sources are stale/unverified; not used as mathematical premises.'],packet_ids=['A009'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Pay the complete SAME-prime queue cost for growing deletion degree beyond bounded-read formulas, using global feasible lambda=1/b. For all4<=a<=b and maxdeg H<=d<=a/2, G=K_ab-H, prove C/I<91/8+2b^2 2^(2d-b)/(1-2^(-(b-d))). In particular C<22I for d<=a/4 and C<15I if a^2 4^d<=2^a. Physical read remains unbounded on both sides as dimensions grow. These are complete feasible-reference upper certificates, not an optimization dual or optimal-weight result. Independently accept A006's entire version; test the exposed universal J log b bill. Entropy units are bits and influences are physical flip probabilities.

# sources actually read, revisions and theorem locators

Fresh BOARD.md and Claude/B02 STREAM_NOTES.md, own rolling state and previous run were consumed. A010 has already closed arbitrary matching deletions, so that NEXT was retired. Read A006 DELETED_DEGREE_TWO.md sections1--5 and its CLAIMS.json; A010 GROWING_MATCHING.md generic source-SCC forest proof and CLAIMS.json; full execution protocol revision2026-10-11-execution-v2. Exact paths and hashes are in out/SOURCE_PINS.json. Earlier full campaign/context intake is inherited, not represented as a fresh reading. Read-only math recall returned generic Boolean-realizability and coordinate-charge obstructions but no new relevant dense-deletion theorem; no recalled theorem is used here. Personal owner-model/state-of-mind brain sources remain stale/unverified and do not supply mathematical premises.

# complete derivation or exact first unsupported line

GROWING_DEGREE.md proves the entire positive theorem: anchor the first active left vertex to count exceptional inputs e<=a(2^d-1)2^(d-1); then J<=2(a+b)e2^(-a-b), while sole-left pivots give I>=2a2^-a(1-2^(-(b-d))). Substitute into A006's independently reconstructed C<(91/8)I+2J log b. Parity induction bounds b^2 2^(-b/2)<=9/2; a ratio induction pays the exact tail regime. All root and label factors, original posterior ambiguity and D stay unchanged. REVIEW_A006.md reconstructs every clause of the source version without repair, including small a and constant endpoints and generic queue factors.

HALF_DENSITY_OBSTRUCTION.md proves an actual all-m Boolean obstruction: two crossed surviving K_mm components give I=8m u^2(1-u)(2-u), J=8m u^2(1-u), u=2^-m. Hence J log b/I is unbounded. No first unsupported line occurs in these restricted proofs. The still unsupported universal step is a replacement component/sector occupation payment for the SAME full reference. The false universal J log b payment is explicitly excluded; neither complete-cost lower bounds nor FEI failure follow.

# executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC.json, REVIEW_SPEC.json and OBSTRUCTION_SPEC.json preceded execution. Commands from A009: `python -X utf8 runs/{R.name}/code/check.py pilot` and then the same command ending `full`. Pilot: {pilot['total_checks']} exact checks, {pilot['elapsed_seconds']:.3f}s. Nonpilot full: {full['total_checks']} exact checks, {full['elapsed_seconds']:.3f}s; PASS, out/full.json. Integer Walsh/direct physical flips cover all330 labelled degree-two deletion graphs on2<=a<=b<=3 and all declared fixtures with n<=16. Sparse exact exceptional boundaries cover larger declared fixtures through a=b=32. Original queue factors are independently replayed for17,951 selected-set forests on the small graphs; larger fixtures use the proved general event bound and do not exhaust all their forests. Scalar exact checks cover4<=a<=b<=128,0<=d<=floor(a/2), and parity induction through256. Obstruction truth tables cover m=2,3,4; exact formula checks cover m=2..128. The written proofs, rather than finite checks, cover all parameters. Arithmetic is integers and Fraction; floating time is telemetry only. No logarithm intervals were necessary: the planned interval option was unused because constants were proved algebraically. No Lean/formal-kernel check is claimed.

The first pilot completed its assertions but failed to save because out/ did not yet exist. Added explicit directory creation and reran successfully; no mathematical failure was hidden. Each completed run was below60s and the frozen90MB estimate; no job expected above300MB or detached work was launched, so no memok admission was required. Shared CPU/memory pressure was inspected; no other work was stopped or throttled.

# proof dependencies and changed downstream conclusions

The positive theorem uses A006-DELETED-DEGREE-TWO-COMPLETE-POSTERIOR-COST@1 only for its half-density transfer. A009 accepts its whole version locally, with unchanged statement digest and no contributor repair; shared registry adoption is not asserted. Its generic mass premise A010-GENERIC-WIDTH-TWO-FOREST-MASS@1 is independently reconstructed here. Source dependencies are acyclic. The new obstruction has no unproved campaign dependencies. The universal coarse bill is disproved, while A006's conditional transfer remains valid. The new claims have author analytic proofs and exact finite audits, with independent-agent review still pending. Full FEI remains OPEN.

# one next mathematical action and independent reviewer

Replace 2J log b by a component/sector-sensitive occupation payment within the original global prime reference, and require it to stay influence-paid on the crossed-biclique family. This directly addresses the universal bottleneck exposed by the transfer. A006/A010 should review the new count, factor-two identities and obstruction; A008/A086 can independently review the full same-reference cost implication. No new worker or schedule was created.

# actual persistence receipts or precise save blocker

The four protocol files, code, exact outputs, source pins and both proof notes are saved in this run. STATUS.md is two lines and WORKLOG.md/LEARNED.md are updated. out/RECEIPTS.json pins every other finished run file; its generation time is telemetry. Files remain below20MB. New statement digests use UTF8 compact sorted JSON of exact_statement and hypotheses; copied source digest is unchanged. Supervisor copying, remote mirrors, shared adoption and downstream use are unverified.

Did: completed the local proof/review/certificate package. Stopped: no existing work. Left running: no research job.

Universal bridge: This stage advances C020 whole-set witness cost by paying the original global-prime queue for arbitrary growing deleted degree in two explicit regimes and independently accepting the dense transfer; it also rules out a universal payment of that transfer's coarse J log b term by an exact actual-Boolean family. The remaining bridge is component/sector-compatible occupation payment for unrestricted overlap within the SAME reference. NEXT addresses that precise universal unpaid line and its new falsifier, rather than collecting another isolated FEI class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Stage7 saved: A006 whole claim HOLDS; SAME-reference growing deletions C<22I (d<=a/4), C<15I (a^2 4^d<=2^a); half-dense J log b payment refuted;280228 nonpilot checks PASS; FEI OPEN.\nNEXT: Replace joint J log b by component/sector-compatible occupation in SAME reference; A006/A010 review new proofs and crossed-biclique obstruction.\n',encoding='utf-8')
for name,line in [('WORKLOG.md',f'\n- {stamp} stage7 {R.name}: consumed new matching/degree-two results; independently accepted A006 whole v1 without repair, proved growing-degree fixed-reference payments and half-density coarse-bill obstruction. Full {full["total_checks"]} exact checks PASS in{full["elapsed_seconds"]:.3f}s. First pilot save-directory defect repaired; successful rerun saved. No detached jobs.\n'),('LEARNED.md','\n- Stage7 durable: for K_ab-H,4<=a<=b,maxdeg H<=d<=a/2, the SAME-prime lambda=1/b complete cost obeys C/I<91/8+2b^2 2^(2d-b)/(1-2^(-(b-d))). Thus C<22I at d<=a/4 and C<15I at a^2 4^d<=2^a. Anchor first active left vertex to count physical bicliques using BOTH degree bounds.\n- Half-density alone cannot pay J log b: delete two K_mm blocks from K_(2m,2m), leaving crossed disjoint K_mm. With u=2^-m actual J/I=1/(2-u)>1/2. This refutes only that transfer bill, not cost or FEI. Use component/sector-compatible occupation next. A006 degree-two whole v1 independently reconstructed HOLDS without repair.\n')]:
    with (A/name).open('a',encoding='utf-8') as f:f.write(line)
receipts=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json']
assert all(x['bytes']<20*1024*1024 for x in receipts)
save('out/RECEIPTS.json',{'saved_at_utc':stamp,'files':receipts,'excludes':'this self-referential manifest only'})
print(json.dumps({'status':'SAVED','files_pinned':len(receipts),'full_checks':full['total_checks']}))
