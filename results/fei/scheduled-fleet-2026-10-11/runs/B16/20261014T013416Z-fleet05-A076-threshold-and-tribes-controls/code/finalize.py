"""A076 stage4 protocol output and local persistence receipts."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
PREV=AGENT/'runs/20261013T220051Z-fleet05-A076-threshold-and-tribes-controls'
BASE=Path(r'~\brain_workers\FEI100_20261011')
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,obj):
    (ROOT/p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=load(protocol_path);pilot=load(ROOT/'out/PILOT.json');full=load(ROOT/'out/FULL.json');review=load(ROOT/'out/REVIEW_VALIDATION.json')
assert full['status']==review['status']==pilot['status']=='PASS'
# Align descriptive metadata with the pre-run cache specification; no math changes.
if full['memory_estimate_MB']!=180:
    full['metadata_correction']='Legacy stdout/result field estimated 120MB; pre-run HELPER_CACHE_SPEC.json used 180MB. No measured peak or assertion change.'
    full['memory_estimate_MB']=180
    full['arithmetic']='Fraction spectra/edges; exact rational prime-exponent identities; rigorous rational log intervals'
    save('out/FULL.json',full)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
a077=BASE/'agents/A077/runs/20261013T222235Z-fleet05-A077-sparse-defect-towers'
a078=BASE/'agents/A078/runs/20261013T234208Z-fleet05-A078-coding-and-padding'
incoming=load(a077/'REVIEW_A076.json');old=load(PREV/'CLAIMS.json')
for c,r in zip(old,incoming):
    assert c['claim_id']==r['claim_id'] and c['version']==r['version']
    assert c['statement_sha256']==r['original_statement_sha256']
save('out/CONSUMED_A077_REVIEW.json',dict(source=str(a077/'REVIEW_A076.json'),sha256=digest(a077/'REVIEW_A076.json'),
    verdicts=incoming,scope_guard='Only stage3 extension accepted; no acceptance of entire historical bundle inferred'))
review_record=dict(claim_id='A078-PAIRED-QUARTER-PROFILE-AND-PADDING',version=2,
 original_statement_sha256=load(a078/'CLAIMS.json')[0]['statement_sha256'],reviewer='A076/fleet05',
 verdict='HOLDS_AT_SCOPED_STAGE3_SIGNED_OBSTRUCTION',scope='PROOF.md sections1-2 actual family, full influence and D_x/Inf_x>=k-4 only; not earlier quarter theorem or L clauses',
 substantive_repair=False,proof='REVIEW_A078.md; code/check_review.py; out/REVIEW_VALIDATION.json')
save('REVIEW_A078.json',review_record)
extensions=[
 ' Stage-4 extension: For arbitrary Boolean branches G,H on one common uniform data cube and fresh-selector F=(G+H)/2+z(G-H)/2, every data query has B_i(F)=sum_T[Phi((g_T+h_T)^2,(g_(T+i)+h_(T+i))^2)+Phi((g_T-h_T)^2,(g_(T+i)-h_(T+i))^2)]/4 and Inf_i(F)=[Inf_i(G)+Inf_i(H)]/2. Writing D_i=B_i(F)-[B_i(G)+B_i(H)]/2, |D_i|<=1. If every restriction of H has each relevant influence >=eta>0, a policy querying H-relevant coordinates while H is nonconstant has |D_i|<=Inf_i(H)/eta and B_i(F)<=2Inf_i(F)/eta. After H is constant, |D_i|<=Inf_i(G). For H=(-1)^P with F2 algebraic degree <=d>=1, eta=2^(1-d); in particular every quadratic H has eta=1/2. All shared Fourier rows and the exact leaf potential R=H(F)-[H(G)+H(H)]/2 are retained.',
 ' Stage-4 extension: Under the derivative-gap policy, any adaptive partial data prefix T satisfies B_T(F)=[B_T(G)+B_T(H)]/2+sum wD_i and sum w|D_i|<=P_H/eta+P_G0. Here P_H=I(H)-E I(H_leaf) is spent only on H-relevant queries and P_G0 is G influence spent after H becomes constant; P_G0=I(G)-E I(G_leaf)-P_G1, where P_G1 is G influence already spent in the first phase. Thus one exclusive source reserve is used without recharging terminal cores. For every even k>=2 A078 bent/spike fixture G=1-2*1{s=0,x=0}, H=(-1)^sum paired shared-bit products, the complete policy has B_i(F)<=4Inf_i(F) in the H phase and <=5Inf_i(F) in the point-core suffix, with zero-entropy terminal character/constant. Therefore its actual B_T and retained Q_T are <=5I(F). This is a hereditary paid data-only policy, not an improvement of the existing H(F)<4I(F) class bound. Inherited arbitrary-core erasure/terminal entropy and uniform derivative-gap removal remain unpaid.'
]
claims=[]
for c,ext,r in zip(old,extensions,incoming):
    c['version']=4;c['exact_statement']+=ext;c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    c['hypotheses'].append('Stage4 both Boolean branches may share all data; fresh uniform selector; policy must select a current H-relevant coordinate until H constant; hereditary eta gap is explicit; arbitrary stopping leaves retained.')
    c['proof_source']['stage4']=str(ROOT/'OWNED_PIVOT_PROOF.md');c['proof_source']['stage4_locator']='sections1-5 equations(1)-(9)'
    c['proof_source']['stage4_validation']=str(ROOT/'out/FULL.json')
    c['proof_dependencies'].append(c['claim_id']+'@3');c['supersedes']=[c['claim_id']+'@3']
    c['review_records'].append(dict(claim_version=3,record=r,source=str(a077/'REVIEW_A076.json'),scope='Stage3 extension only; version4 new extension not independently accepted'))
    c['next_consumers']=['A077','A078','A058','A057','A097','A092','A088','B16','B20']
    assert set(c)==set(protocol['required_per_run']['claim_fields']);claims.append(c)
save('CLAIMS.json',claims)
sources=[protocol_path,BASE/'BOARD.md',BASE/'claude/B16/STREAM_NOTES.md',
 PREV/'CLAIMS.json',PREV/'SHIFTED_ROW_PROOF.md',PREV/'code/check_shifted.py',
 a077/'PROOF.md',a077/'REVIEW_A076.json',a078/'REPORT.md',a078/'PROOF.md',a078/'CLAIMS.json']
save('SOURCE_MANIFEST.json',dict(captured_at=now,scope='Save-time source hashes, not stage-start snapshots',
 sources=[dict(path=str(p),sha256=digest(p),bytes=p.stat().st_size) for p in sources],
 board='2026-10-14 01:30 UTC; full read with middle sections reread after truncation',
 lead='B16 v2 2026-10-11 23:25Z unchanged; previous assigned mixed-majority control completed at stage2'))
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B16',packet_id='A076',gap_id='FEI-B16-A076-INITIAL',
 attempt_id='A076-stage4-owned-scaffold-pivot',method='Consume A077 scoped review and A078 actual multishared obstruction; exact shared-row formulas, hereditary derivative-gap pivot and exclusive influence telescope; independent exact spectra/edges/polynomial restrictions',
 mathematical_delta='Pays multishared signed correction with one labelled derivative-gap branch reserve: sum w|D|<=P_H/eta+P_G0, quadratic eta=1/2. Provides actual complete data-only B,Q<=5I policy for every A078 bent/spike fixture while preserving arbitrary inherited and terminal costs.',
 deliverable_status='COMPLETE_LOCAL_PENDING_NEW_EXTENSION_REVIEW',mathematical_status='OWNED_PIVOT_INTERFACE_AUTHOR_PROVED; A078_SIGNED_OBSTRUCTION_SCOPED_REVIEW_HOLDS; FULL_FEI_OPEN',
 claim_versions_used=['A076-STRUCTURED-SPECTRA@3 (stage3 extension independently accepted by A077)','A076-TRIBES-PAYMENT-DISCRIMINATION@3 (stage3 extension accepted only)','A077-ONE-SHARED-BIT-SIGNED-TRANSPORT@1 (context)','A078-PAIRED-QUARTER-PROFILE-AND-PADDING@2 (sections1-2 reviewed scope only)'],
 claims_created_or_changed=[c['claim_id']+'@4' for c in claims],
 source_artifacts=['OWNED_PIVOT_PROOF.md','REVIEW_A078.md','REVIEW_A078.json','SOURCE_MANIFEST.json','code/check_owned.py','code/check_review.py','code/arithmetic.py','code/finalize.py','out/FROZEN_SPEC.json','out/HELPER_REPAIR_SPEC.json','out/HELPER_CACHE_SPEC.json','out/FULL_V1_FAILURE.json','out/FULL_V1B_FAILURE.json','out/PILOT.json','out/FULL.json','out/FULL_LEDGERS.json','out/REVIEW_VALIDATION.json','out/CONSUMED_A077_REVIEW.json'],
 next_consumers=['A077','A078','A058','A057','A097','A092','A088','B16','B20'],
 next_action='At the first rare/rare collision with no hereditary derivative gap in either branch, derive an adaptive branch-switch or signed terminal-slack payment replacing eta^-1, with one exclusive physical influence reserve. A092/A088 review equations(1)-(9) and A078/A077 challenge fixture policy.',
 stagnant_substantive_attempts=0,blockers=['Hereditary gap eta is not uniform for arbitrary Boolean branches','Inherited erasure and arbitrary terminal core entropy remain unpaid','New v4 extension review, supervisor adoption and mirror receipt not observed'],packet_ids=['A076'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# A076 stage 4: an exclusive pivot reserve for multishared collisions

## exact target, quantifiers, hypotheses and units

Resolve the previous NEXT against the new board: A077 has already closed one shared bit, while A078 gives an actual multishared rare-private-query obstruction. For arbitrary Boolean G,H on the same uniform data cube and one fresh selector, this stage proves an adaptive collision-payment interface when one branch has a hereditary relevant-influence gap eta. In particular every quadratic F2 branch has eta=1/2, independently of the number of shared bits. Entropies are bits. Arbitrary stopping leaves retain their true core and selector-potential entropy. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md 2026-10-14 01:30 UTC including omitted middle sections separately, unchanged B16 lead notes v2, STATUS and the execution protocol v2. Read A077 stage3 PROOF.md sections1-6 and source-bound REVIEW_A076.json; the review accepts only our stage3 extension, and both original claim digests match. Read A078 stage3 REPORT.md, PROOF.md sections1-4 and CLAIMS.json. Prior shifted-row proof/helper and v3 claims are reused. SOURCE_MANIFEST.json pins save-time bytes without pretending they were immutable stage-start snapshots. No new external theorem or web source is needed.

A077's one-shared-bit theorem and A078's bounded-H/I result are credited and not rerun as new targets. The new scope is a selected data-only pivot policy beyond Fourier l1<=1, with one source-owned reserve.

## complete derivation or exact first unsupported line

OWNED_PIVOT_PROOF.md sections1-5 equations(1)-(9) give the full proof. At any data query the exact coherent row formula gives D_i=B_i(F)-[B_i(G)+B_i(H)]/2, with |D_i|<=1. Query a relevant H coordinate until H becomes constant. The hereditary gap converts this to |D_i|<=Inf_i(H)/eta. After H is constant, stage3 gives |D_i|<=Inf_i(G). The exact source-owned sum is sum w|D_i|<=P_H/eta+P_G0, where P_H=I(H)-E I(H_leaf) and P_G0 excludes both already-consumed first-phase G influence and terminal G influence. The full inherited half-core erasures and exact leaf potential remain present.

An elementary induction proves nonzero degree-r F2 polynomials have weight >=2^-r; derivatives give eta=2^(1-d) for degree-d sign branches. Thus quadratic shared data has a dimension-independent first-phase reserve 2I(H), and a paid local pivot B<=4Inf. For every even-k A078 bent/spike fixture, the suffix core is a point defect and has B<=3Inf; shifted-row transport gives B<=5Inf in the suffix. The complete adaptive data-only policy has B_T,Q_T<=5I, zero-entropy final character/constant, and no repeatedly spent shared-core reserve. This is weaker than the existing H<4I bound as an entropy estimate; its new content is the hereditary policy and ownership.

The exact first unsupported universal line is replacing eta^-1 by one uniform signed reserve when both branches have arbitrarily rare relevant derivatives, while paying inherited erasure and terminal core entropy. No general C018 constant, universal C019 selection rule or FEI closure follows.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes enumeration. Pilot: all 276 ordered labelled core pairs on n=0,1,2, two coordinate orders and three stopping modes; {pilot['exact_assertions']:,} exact assertions PASS in {pilot['elapsed_seconds']:.3f}s. Full fixed domain: 791 actual Boolean roots, including all 256 three-bit G with either sign of H=(-1)^(b0*b1+b2), plus k=2,4,6 A078 fixtures; {full['tree_cases']:,} complete/partial adaptive trees and {full['nodes']:,} data nodes; **{full['exact_assertions']:,} exact assertions PASS** in {full['elapsed_seconds']:.3f}s.

Commands: `python -X utf8 runs\\{ROOT.name}\\code\\check_owned.py --pilot`, then the same command without `--pilot`. Two full attempts hit the frozen 170-second runtime guard without a mathematical assertion failure; out/FULL_V1_FAILURE.json and out/FULL_V1B_FAILURE.json preserve both failures. The first arithmetic repair uses exact rational prime-exponent maps instead of giant rational powers; it was insufficient under the cap. out/HELPER_CACHE_SPEC.json then froze bounded memoization of repeated pure restriction/row/interval computations and a 600-second full cap, below the campaign 30-minute limit. Family, domain and mathematical sign claims are unchanged. The successful cached run is the reported full acceptance.

Independent review command: `python -X utf8 runs\\{ROOT.name}\\code\\check_review.py`. It passed {review['exact_assertions']:,} exact assertions in {review['elapsed_seconds']:.3f}s, covering all 128 three-bit quadratic polynomials under all 27 coordinate restrictions (3,456 cases), and direct actual-spectrum reconstruction of A078's k=2,4,6 rare query. The k=4 strict factor-two violation is certified. The analytic all-k lower-bound reconstruction is in REVIEW_A078.md.

Actual truth tables use integer FWHT, Fraction spectra and separately counted physical edges. Coherent row and terminal equalities use exact rational prime exponents. Inequalities use outward 70-bit rational intervals from 24-term atanh series after reduction to [1,2], with tail 2*z^(2N+1)/((2N+1)*(1-z^2)); exact prime identities handle zero boundaries. Full tree expressions are saved in out/FULL_LEDGERS.json. The cached run's memory estimate is 180 MB, not a measured peak; no job was expected above 300 MB, and no GPU, background process or automatic dimension increase was used. Finite validation does not replace the analytic all-dimensional proof.

## proof dependencies and changed downstream conclusions

The two existing bundles extend to v4; no third broad pending candidate is opened. A077's scope-limited acceptance of v3 is consumed with matching statement hashes; it is not reported as acceptance of the entire historical bundle or new v4 extension. A078 v2 receives an independent HOLDS verdict only for the actual family/influences and signed rare-query obstruction in sections1-2; other old quarter-profile clauses are explicitly outside review. No substantive repair to the reviewed mathematics was supplied.

A077/A058/A078 receive an all-shared quadratic interface beyond the one-bit l1 argument, plus an explicit safe policy on the mandatory adverse fixture. A057/A097/B20 receive one labelled reserve, its precise consumed/terminal split and its nonuniform eta boundary. Both inherited branch costs remain explicit. New independent review, adoption and mirrors remain unverified.

## one next mathematical action and independent reviewer

Derive a branch-switch or signed terminal-slack payment for the first rare/rare collision when neither branch has a hereditary derivative gap, retaining both core terminals and one exclusive physical influence reserve. A092 primary/A088 alternate should reconstruct equations(1)-(9), polynomial-weight induction and point-core suffix; A077/A078 should challenge the proposed policy on their exact packets.

## actual persistence receipts or precise save blocker

All four protocol files, proof, frozen specifications, timeout receipt, scripts, exact full-tree ledgers, independent review and consumed prior review are saved under this run. Exact protocol keys, claim digests and compatibility bytes are checked by code/finalize.py. STATUS has two lines; WORKLOG and LEARNED are appended. out/PERSISTENCE.json contains local hashes/byte counts at {now}. Files stay below 20 MB. No remote mirror, continuous execution or approval by another agent is inferred from local persistence.

## Universal bridge

C018/C019 moves from a refuted all-query multishared correction to a selected-pivot payment with an exclusive source reserve: for quadratic H, sum w|D_i|<=2P_H+P_G0 at every partial adaptive prefix, and the complete A078 adverse family admits actual B_T,Q_T<=5I. The inherited half-core erasures and exact terminal entropy remain unpaid, and general algebraic degree costs eta^-1=2^(d-1), so no universal FEI constant is obtained. NEXT removes this derivative-gap dependence at the first rare/rare collision using one signed terminal reserve or branch switch; this directly tests the missing universal selection mechanism rather than adding another isolated threshold/tribes entropy bound.
'''
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: A076 stage4 saved: multishared derivative-gap pivot pays signed correction from one exclusive branch reserve; quadratic eta=1/2; A078 fixture B,Q tree<=5I; {full["exact_assertions"]:,} full exact checks PASS; v4 review pending, FEI OPEN.\nNEXT: Remove derivative-gap dependence at first rare/rare collision via branch switch or owned signed terminal slack; A092/A088 review new interface; inherited core erasure/terminal entropy remain explicit.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {now} (requested stage 2026-10-14 01:34 UTC)\nConsumed A077 scoped acceptance of v3 and independently reviewed A078 signed rare-query obstruction. Proved owned derivative-gap pivot for arbitrary shared data, quadratic eta=1/2, exact adaptive correction budget and terminal ledger; complete A078 data-only policy B,Q<=5I. Pilot {pilot["exact_assertions"]} checks; two full attempts timed out at frozen guard; exact prime-exponent and bounded-cache repairs, same domain with predeclared 600s cap: {full["exact_assertions"]} assertions/{full["tree_cases"]} trees PASS in {full["elapsed_seconds"]:.3f}s. Independent polynomial/review check {review["exact_assertions"]} assertions PASS. General rare/rare pivot and inherited terminal costs remain open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage4 durable fact: for arbitrary shared-data mux F=(G+H)/2+z(G-H)/2, D_i=B_i(F)-[B_i(G)+B_i(H)]/2 has |D_i|<=1. A hereditary H relevant-influence gap eta permits H-relevant-first adaptive queries with sum w|D|<=P_H/eta+P_G0; P_H=I(H)-E I(H_leaf), P_G0 excludes G influence already consumed before H became constant and terminal G influence. F2 degree d gives eta=2^(1-d) by the polynomial weight induction; quadratic branches give eta=1/2 independent of shared width, beyond l1<=1. For A078 bent/spike, local B<=4Inf in H phase and <=5Inf in point-core suffix, complete actual B,Q tree<=5I. This pays a selected physical policy, not arbitrary rare private queries or arbitrary inherited core entropy. The degree dependence is exponential; no universal derivative gap exists. Exact prime-exponent log equalities avoid giant rational-power computation; first full timeout preserved, same-domain rerun passed. A077 accepted only our v3 extension; A076 independently accepts only A078 stage3 sections1-2 signed obstruction.\n')
paths=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
for p in paths:assert p.stat().st_size<20*1024*1024,(p,p.stat().st_size)
save('out/PERSISTENCE.json',dict(saved_at=now,scope='verified local files only; no independent acceptance or mirror receipt',
 artifacts=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p)) for p in paths],
 rolling=[dict(path=str(AGENT/p),bytes=(AGENT/p).stat().st_size,sha256=digest(AGENT/p)) for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]))
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
print(json.dumps(dict(saved=True,run=str(ROOT),schema='PASS',full_exact_assertions=full['exact_assertions'],review_assertions=review['exact_assertions'],files=len(paths)+1)))
