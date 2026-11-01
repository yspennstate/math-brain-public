from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def put(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
stats=[json.loads((R/'out'/n).read_text(encoding='utf-8')) for n in ('RESERVES.json','RIGIDITY.json')]
assert all(s['status']=='PASS' for s in stats)
count=sum(s['checks'] for s in stats)
statement='For any nonconstant uniform Boolean f on n>=2 relevant coordinates and K>=0, put D=H-KI, t_i=E_b[I(f_i^b)-a(f_i^b)], s_i*=E_b[K a(f_i^b)-H(f_i^b)], N*=sum_i(-s_i*)_+, and T=H-sum_i H(S_i|S_-i). Then N*>=(n-1)D+T+K sum_i t_i-(2/ln2)I. Therefore H/I<=K+[(2/ln2)+N*/I]/(n-1); growing relevant-dimension ratio-preserving embeddings of a seed with H/I>K cannot have N*=o(nI). a is the full affine-input/output-character minimum influence, and children are complete Boolean physical restrictions.'
claim=dict(claim_id='A005-NORMALIZED-OPTIMIZED-CHILD-DEFICIT',version=1,exact_statement=statement,hypotheses=['Uniform Boolean signs; entropy bits; K>=0; nonconstant f; n>=2 relevant physical coordinates','Complete physical children including constants; a minimizes over full invertible affine inputs and output characters'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A005'],proof_source='PROOF.md equations(1)--(3)',proof_dependencies=['A005 stage2 signed restriction identity, rederived here','C005 Boolean JS row bound <=(2/ln2) influence; B17 independent packet-scalar proof recorded on BOARD','Finite entropy chain rule and exact influence restriction identity'],review_records=[],status='PROOF_AUTHOR_CHECKED_EXACT_VALIDATION; INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A052','A055','A051','A094','B20'])
source=Path('agents/A052/runs/20261023T142511Z-fleet03-A052-critical-source-structure/CLAIMS.json')
review=json.loads(source.read_text(encoding='utf-8'))[0]
assert hashlib.sha256(review['exact_statement'].encode()).hexdigest()==review['statement_sha256']
review['review_records']=review.get('review_records',[])+[dict(reviewer='A005',verdict='HOLDS_SCOPED',source='PROOF.md scoped review; out/RIGIDITY.json',scope='Analytic corollary and elementary rank/cost proof only; no giant certificate or arbitrary-core embedding dependency; no repair',exact_checks=stats[1]['checks'])]
review['status']='INDEPENDENT_SCOPED_RECONSTRUCTION_HOLDS; SHARED_ADOPTION_UNVERIFIED'
put(R/'CLAIMS.json',[claim,review])
next_action='A052/A051/A055: exploit EXACT nonnegative complete-child reserves in the remaining D/I=O(1/n) critical regime to fund one ORIGINAL pair, retaining Pi, all mixed rows, old debits and unused quotient rank from SAME owner; A094 audit.'
p=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B01',packet_id='A005',gap_id='C019-CRITICAL-ORIGINAL-PAIR-LOWER-FUNDING',attempt_id='A005-stage21-normalized-child-deficit-referee',method='Independent reconstruction of A052 rank rigidity; affine-optimized signed restriction identity; exact prime-log and rational enclosure checks',mathematical_delta=f'Normalized negative complete-child reserve must be at least the retained fixed H/I gap times nI asymptotically. This excludes near-critical arbitrary-seed admission when N*=o(nI), not the O(1/n) genuine critical regime. A052 rigidity scoped HOLDS; {count} exact checks PASS; universal constant gain0.',deliverable_status='COMPLETE_LOCAL_VERIFIED',mathematical_status='FULL_FEI_OPEN; normalized deficit corollary author proof/exact validation; independent-agent review pending',claim_versions_used=['A052-RARE-PHASE-RIGIDITY@1 analytic scope independently HOLDS','A005 stage2 signed child-slack identity','C005 Boolean JS bound and B17 packet-scalar proof'],claims_created_or_changed=['A005-NORMALIZED-OPTIMIZED-CHILD-DEFICIT@1','A052-RARE-PHASE-RIGIDITY@1: local scoped review record only'],source_artifacts=['PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/RESERVES.json','out/RIGIDITY.json','out/FORMAL_STATUS.json'],next_consumers=['A052','A055','A051','A094','B20'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['Exact high-K ORIGINAL-pair funding in genuine critical regime remains unproved','Independent acceptance of new corollary, registry adoption, supervisor copying and remote mirrors unverified','Wake flagged stale personal-model/state/dream notes; owner alerted; not used as proof evidence','Checklist working registration failed: checklist lock held too long; no lock bypass or shared-file edits'],packet_ids=['A005'])
put(R/'PROGRESS.json',p);put(R/'PACKET_DELTA.json',p)
formal=json.loads((R/'out/FORMAL_STATUS.json').read_text(encoding='utf-8')) if (R/'out/FORMAL_STATUS.json').exists() else {'status':'UNVERIFIED','scope':'Scalar algebra formal check requested; no result receipt yet. Full entropy theorem is an analytic proof, not Lean-checked.'}
put(R/'out/FORMAL_STATUS.json',formal)
report=f'''# A005 stage21: negative child reserve has a necessary scale

## exact target, quantifiers, hypotheses and units

For nonconstant uniform Boolean f, K>=0 and n>=2 relevant coordinates, quantify the complete optimized-child negative reserve N*. The conclusion is N*>=(n-1)(H-KI)+DTC+K sum t_i-(2/ln2)I. Entropy is in bits; influence is physical; a(child) permits full affine inputs and output characters. A growing-dimensional seed-ratio embedding with R>K cannot satisfy N*=o(nI). This is a scoped obstruction to an endpoint, not a disproof of FEI. It does not exclude embeddings without growing relevant dimension.

## sources actually read, revisions and theorem locators

Execution protocol rev2026-10-11-execution-v2 read in full; current BOARD and B01 STREAM_NOTES; own stage20 report/proof and rolling notes; A052 stage11 REPORT, CLAIMS and RIGIDITY_REVIEW items1--6. Campaign README/status/registries/plan and research-push baseline plus all four manuscript text versions were refreshed through targeted excerpts; hashes, encodings and exact inspection scope are in out/SOURCE_RECEIPTS.json. This is not a new complete paper audit. A052's analytic corollary is reviewed; its giant examples and unexamined embedding dependencies are excluded. The lead's old no-rebuilding-gap-table direction is followed by auditing the newly supplied rigidity dependency and the surviving C019 reserve obstruction.

## complete derivation or exact first unsupported line

PROOF.md gives the exact identity DTC+(n-1)D+sum s_i*+K sum t_i=sum J_i and the negative-part consequence. Applying the Boolean JS row bound and dividing only for I>0,n>=2 gives the limit obstruction. This extends the prior signed-slack identity to optimized negative reserve; it is a narrow corollary, not a new universal proof mechanism. A052's rank/cost proof reconstructs without repair: gamma>=0 and m>0 are used at their specific steps; rank0 and epsilon=m boundaries are retained. First unpaid line: select and fund an ORIGINAL pair from EXACT nonnegative full-child reserves, unused independent quotient rank and the SAME original owner, retaining phase price Pi, every mixed row and old debit. The residual D/I=O(1/n) genuine-critical regime is not excluded.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec in out/FROZEN_SPEC.json precedes the jobs. Pilot:100 reserve cases,598 checks PASS. Main:all276 Boolean tables n<=3 and52 prescribed n4/5 controls, each at five K, total1640 cases and{stats[0]['checks']} checks PASS in {stats[0]['seconds']:.3f}s. All256 three-bit phases lifted to a five-bit point defect, cubic K10 and quadratic K4 subdomain:384 comparisons and{stats[1]['checks']} checks PASS in {stats[1]['seconds']:.3f}s. Total {count} main exact checks, pilot excluded. Commands: python -X utf8 -B code/check.py pilot; reserves; phase. Character sums and physical edges are independent representations; symbolic prime-log identities are exact and inequalities use40-term rational atanh enclosures. A final audit strengthened the JS check to compare with a LOWER rational bound on2/ln2; the main reserve check was rerun and only its final result is counted. Constants, dummy coordinates, n1 identities, K0 and positive/zero/negative reserves are included. Every job<55s; estimate80MB; no >300MB job, GPU, detached work or automatic escalation. Formal status: {formal['status']}; only the scalar consequence was submitted, never the full entropy theorem. No blanket Lean-certified claim is made.

## proof dependencies and changed downstream conclusions

New A005-NORMALIZED-OPTIMIZED-CHILD-DEFICIT@1 is an author-checked analytic proof with finite exact validation, independent review pending. C005's Boolean row bound and elementary restriction identities are explicit dependencies. A052-RARE-PHASE-RIGIDITY@1 receives a scoped independent HOLDS without repair; its source statement hash is unchanged. No universal constant improves. Small absolute complete-child deficits are insufficient: their total must be compared with n times ORIGINAL influence. Approximate phase stationarity does not supply this condition or pay an original pair.

## one next mathematical action and independent reviewer

{next_action} A052/A055 are requested reviewers of the new corollary. This is a local source-bound handoff, with no message sent or other-agent file changed.

## actual persistence receipts or precise save blocker

All four protocol files, proof, code, frozen spec and exact outputs are saved only inside this A005 run. out/VERIFY.json checks schema sets, statement hashes, identical progress copies, required headings and file-size caps. out/PERSISTENCE_RECEIPTS.json contains readback-verified local byte hashes. STATUS is two lines; WORKLOG and LEARNED are appended. Shared adoption, brain ingestion and remote mirrors remain UNVERIFIED. Brain wake warned that personal model/state/dream notes are stale; current campaign sources govern. Checklist working registration failed on a shared lock; it was not bypassed. Existing jobs are untouched and bounded mathematical commands finish.

**Universal bridge.** C019 original-pair payment gains an independent acceptance of A052's analytic rigidity corollary and a quantitative exclusion of approximate child-eligibility endpoints: a preserved fixed positive seed gap forces negative reserve of order nI, including the affine-release term. The universal constant improves by0. Exact nonnegative critical children still leave the D/I=O(1/n) regime and the ORIGINAL pair bill unpaid. NEXT asks what criticality adds in precisely that regime, the shortest surviving step toward full FEI rather than another isolated class result.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A005 stage21 saved: normalized optimized-child debt >= fixed seed gap times nI; A052 rigidity scoped HOLDS; '+str(count)+' exact main checks PASS; FEI OPEN.\nNEXT: '+next_action+'\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
for name,text in [('WORKLOG.md',f'{stamp} stage21: reconstructed A052 rank rigidity without repair; extended signed child identity to optimized negative-part scale. Main {count} exact checks pass. Original pair funding remains open; checklist registration lock failure recorded.'),('LEARNED.md',f'{stamp} stage21 durable fact: for full optimized children N*=sum(-E[Ka-H])+, N*>=(n-1)(H-KI)+DTC+K sum E[I-a]-(2/ln2)I. Therefore a growing relevant-dimensional fixed-gap embedding cannot have N*=o(nI). Absolute-small reserves do not give normalized criticality. This does not rule out true critical gaps O(I/n). A052 rank rigidity independently holds at analytic scope; new corollary review pending.')]:
 with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+text+'\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
cf=set(protocol['required_per_run']['claim_fields']);pf=set(protocol['required_per_run']['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(p)==pf
for c in (claim,review):assert set(c)==cf;assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for head in protocol['required_per_run']['report_fields']:assert '## '+head in report
for f in R.rglob('*'):
 if f.is_file():assert f.stat().st_size<20*1024*1024
put(R/'out/VERIFY.json',dict(status='PASS',claim_schema=True,progress_schema=True,hashes=True,compatibility=True,status_two_lines=True,report_fields=True,cap20mb=True,full_fei='OPEN'))
receipts=[]
for f in sorted(R.rglob('*')):
 if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json':receipts.append(dict(path=str(f.relative_to(R)),bytes=f.stat().st_size,sha256=digest(f)))
for v in receipts:assert digest(R/v['path'])==v['sha256']
put(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='LOCAL_READBACK_PASS',remote='UNVERIFIED',files=receipts))
print(json.dumps(dict(status='SAVED_VERIFIED',main_checks=count,run=str(R),full_fei='OPEN')))
