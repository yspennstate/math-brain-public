from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json

RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];TEAM=OWN.parents[1]
SRC=TEAM/'agents/A064/runs/20261014T030103Z-account05-A064-global-debt-potential'
REF=TEAM/'agents/A087/runs/20261014T020842Z-account05-A087-restriction-referee'
PRIOR=TEAM/'agents/A064/runs/20261013T235917Z-account05-A064-global-debt-potential'
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.now(timezone.utc).isoformat()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
claim=json.loads((SRC/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert claim['claim_id']=='A064-REPEATED-FALLBACK-PRIORITY-GLOBAL-DEBT' and claim['version']==1
recorded=claim['statement_sha256'];raw=sha256(claim['exact_statement'].encode()).hexdigest()
semantic=sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
# Preserve the source hash rather than silently changing its convention.
dump(RUN/'out/CLAIM_HASH_RECEIPT.json',{'recorded_source_hash':recorded,'raw_statement_hash':raw,'statement_hypotheses_hash':semantic,'source_claim_file_hash':sha256((SRC/'CLAIMS.json').read_bytes()).hexdigest(),'local_statement_and_hypotheses':'UNCHANGED'})
pilot=json.loads((RUN/'out/PILOT_CHECK.json').read_text());local=json.loads((RUN/'out/LOCAL_CHECK.json').read_text());trees=json.loads((RUN/'out/TREES_CHECK.json').read_text())
assert all(a['status']=='PASS' for a in (pilot,local,trees))
total=local['assertions']+trees['assertions'];assert total==114242
claim['review_records'].append({'reviewer':'A061','at':now,'verdict':'INDEPENDENT_NEW_CONTROLLER_CLAUSE_AND_GLOBAL_ASSEMBLY_HOLDS',
 'scope':'Full new repeated-fallback controller derivation and ordered-priority Bellman assembly reconstructed; data-node price/root ownership imported only at additional A064-v2 scope already independently reviewed by A087; shared-X uses exact A087 clause reviewed by A064. No older bundled v1 acceptance or universal core payment.',
 'method':'Different standalone labelled truth-table/Walsh implementation; same fallback on both children; complete physical branches and actual partial terminal ledger; analytic arbitrary-width sector proof',
 'source_run':RUN.name,'proof_source':['REVIEW.md','code/check_priority.py','out/LOCAL_CHECK.json','out/TREES_CHECK.json'],
 'substantive_repair':False,'dependency_status':'CONDITIONAL_ON_EXACT_REVIEWED_ADDITIONAL_V2_DATA_LIFT_AND_SHARED_X_CLAUSES'})
claim['status']='INDEPENDENT_NEW_CONTROLLER_CLAUSE_AND_GLOBAL_ASSEMBLY_HOLDS_BY_A061'
dump(RUN/'CLAIMS.json',[claim]);assert set(claim)==set(protocol['required_per_run']['claim_fields'])
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B13/STREAM_NOTES.md',SRC/'REPORT.md',SRC/'CLAIMS.json',SRC/'DERIVATION.md',SRC/'GLOBAL_DEBT_POTENTIAL.tex',SRC/'REVIEW_A087.md',REF/'REPORT.md',REF/'PROOF.md',PRIOR/'DERIVATION.md',OWN/'runs/20261014T012929Z-account05-A061-entropy-process/code/check_review.py']
dump(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in sources])
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B13','packet_id':'A061','gap_id':'C019-SIGNED-CHILD-TERMINAL-PAYMENT','attempt_id':'A061-stage5-A064-repeated-physical-fallback-review',
 'method':'Independent physical-sector proof and standalone exact truth-table/Walsh/Bellman implementation, with actual same fallback and unchanged source statement',
 'mathematical_delta':'A064 new repeated-fallback controller clause HOLDS at rate D-kappa<=(8+2/ln2)d<11d; ordered-priority nonnegative potential assembly accepted conditional on exact reviewed data/root and shared-X dependencies. 2592 local cases plus64 complete data-interleaved trees pass114242 primary assertions, retaining actual partial boundaries and117 positive reserve-growth occurrences.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_INDEPENDENT_REVIEW_COMPLETE; UNIVERSAL_CORE_AND_OVERLAPPING_CONTROLLER_PAYMENT_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1},{'claim_id':'A064-TERMINAL-CORRECTED-GLOBAL-DEBT','version':2,'scope':'additional data lift and root rarity ownership only; A087 accepted'},{'claim_id':'A087-OWNED-CONTROLLER-REVEAL-AND-RESOLVED-CONTINUATION','version':1,'scope':'shared-X clauses only; A064 accepted'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'local independent review record; unchanged source statement and hash; no new broad candidate'}],
 'source_artifacts':['REVIEW.md','FROZEN_SPEC.json','code/arithmetic.py','code/check_priority.py','out/PILOT_CHECK.json','out/LOCAL_CHECK.json','out/TREES_CHECK.json','out/SOURCE_RECEIPTS.json','out/CLAIM_HASH_RECEIPT.json'],
 'next_consumers':['A064','A087','A091','A062','A065','A038','A039','B20'],
 'next_action':'Audit one selected non-point overlapping controller reveal after actual data exposure with the same physical sector rows, inherited own-history core reserves, owned rarity release, and both H-Q terminal bills; use A038/A039 mixed-history fixture without refreshing its influence bank.',
 'stagnant_substantive_attempts':0,'blockers':['Universal initial inherited-core payment and overlapping/shared-data controller representation remain unproved.','Two earlier A061 authored claims still await independent review; scoped source consumption does not change that.','Shared-index adoption and supervisor mirror unverified.'],'packet_ids':['A061']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
report=f'''# A061 stage 5: repeated physical fallback review

## exact target, quantifiers, hypotheses and units

Independently audit A064-REPEATED-FALLBACK-PRIORITY-GLOBAL-DEBT@1. Local scope: every finite uniform point override F=A*u+(1-A)G with u physically independent of the whole fallback G, G an exclusive controller of disjoint independent cores or constants, and the SAME G on both query children. Entropy is in bits; kappa is the actual release of R=sum phi(q_j)Var(core_j). Global scope: ordered disjoint point-priority policies with declared nonnegative own-history core reserves and actual finite stops. No arbitrary initial core payment or universal representation is assumed.

## sources actually read, revisions and theorem locators

Full execution protocol {protocol['revision']}; BOARD dated 2026-10-14 04:19 UTC, B13 lead v2 still dated 2026-10-11, own STATUS. A064 stage5-target run 20261014T030103Z: REPORT, CLAIMS, DERIVATION Sections1--6, GLOBAL_DEBT_POTENTIAL.tex and REVIEW_A087.md. A087 run20261014T020842Z: REPORT, PROOF Sections Source-bound review, shared-controller clauses and priority boundary. A064 additional-v2 DERIVATION in run20261013T235917Z. Own previous standalone checker reused as arithmetic source; no source-agent code imported. out/SOURCE_RECEIPTS.json pins exact bytes. Earlier campaign/paper intake inherited; no new paper claim or literature search.

## complete derivation or exact first unsupported line

REVIEW.md gives an independent reconstruction by empty and nonempty physical data sectors. The exact profile residual is B-kappa=Bprofile+(c(p)-k(p))W, with c<=2p, k>=0, W+Var(g)=1-(EG)^2. Actual query influence is p(1-Eu*EG). The amplitude packet inequality and explicit two-case scalar bound yield B-kappa<=8d; physical JS<=2d/ln2 gives D-kappa<=(8+2/ln2)d<11d. The proof covers all point widths and finite fallback-controller complexities, including zero influence. No sign assumption on D-kappa is used.

At a controller query the inherited sum q_j*r_j has zero expected drift, because no own-core history changes. Combining this new controller price with the reviewed additional-v2 data price C+11/2 yields the SAME nonnegative Q and Bellman domination, with root rarity debit<=2I_ctrl, expected Q_terminal<=Q0+C Pi_data, and actual terminal H-Q retained. The control rate11 and root2 add to13. The source statement is accepted at this new-clause/assembly scope, with exact already-reviewed dependencies; older bundled v1 assertions are not reaccepted.

First unsupported universal line: fund arbitrary inherited core reserves and a selected overlapping non-point controller residual from unused physical influence while retaining both actual child functions and terminal debt. A physically shared data core does not satisfy the reviewed independent-core sector hypotheses.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json predates all searches. Commands from this run: `python -X utf8 code/check_priority.py pilot`, then `... local`, then `... trees`. Pilot: {pilot['local_cases']} local cases, {pilot['complete_trees']} complete trees, {pilot['assertions']} assertions in {pilot['seconds']:.4f}s (<60s), excluded from primary totals. Local full: all81 labelled ternary fallback maps on two controls, widths1,2, four named independent u and v cores (constant+1, point-sign AND2, XOR2, first dictator): {local['local_cases']} cases, {local['assertions']} assertions in {local['seconds']:.4f}s. No symmetry quotient or all-function claim.

Complete continuation: every pair of those four named two-bit cores, both shared-X orientations, C=0,4, policy X,A0,u0,A1,B,v0,u1,v1. All {trees['complete_trees']} trees and {trees['physical_tree_nodes']} physical nodes retained. At C=0 inherited core r is its actual remaining H; at C=4 these named core trees have zero r. Complete and partial frontiers at depths3,5,8 retain actual H-Q. The certificate checks node prices, initial controller ownership, inherited controller martingale, stopped expectation, least nonnegative reserve domination and full influence partition. {trees['positive_child_growth_occurrences']} positive child-reserve growth occurrences are recorded without assuming branchwise monotonicity. {trees['assertions']} assertions in {trees['seconds']:.4f}s. Primary total {total}; no failures or retry.

Arithmetic: integer Walsh and physical edge counts, exact Fraction prime-log expressions, zero expressions recognized algebraically, strict signs enclosed by range-reduced 48-term positive atanh logarithm series with proved tail, outward dyadic160 rounding. Analytic proof supplies arbitrary-width quantifiers; no floating finite-to-infinite extrapolation. Jobs sequential, estimated memory120MB, no >300MB trigger, no heavy/background/GPU job and no dimension escalation. The source helper was reused only from our own prior stage; exact version/hash recorded.

## proof dependencies and changed downstream conclusions

CLAIMS.json is a local reviewer copy of the unchanged A064 v1 statement. The independent new local proof and global assembly HOLD conditional on additional A064-v2 data lift/root ownership already reviewed by A087 and shared-X geometry already reviewed by A064. No source repair, contributor conflict or new broad authored candidate. Source hash convention preserved, with raw and statement/hypothesis digests recorded separately in out/CLAIM_HASH_RECEIPT.json rather than silently renaming the source version.

This closes the interrupted repeated-fallback controller boundary at disjoint point-priority geometry, including one core bit revealed between the private A controls. It does not provide universal inherited-core payment, non-point overlapping controllers or physically shared data. Earlier A061 point and admission claims remain externally pending; reviewer activity does not self-accept them. This stage consumes a new proved payment rather than another point-edit admission census.

## one next mathematical action and independent reviewer

Audit one selected non-point overlapping controller reveal after actual data exposure, keeping the same physical sector rows, inherited core reserves, owned kappa release and both H-Q terminal bills. A038/A039's mixed-history fixture is the concrete next dependency; the current independent point-priority theorem isolates exactly which geometry must change. A087/A091/A094 should challenge this review scope and that transfer. Arbitrary inherited r stays explicit until a genuinely unused core influence account is certified.

## actual persistence receipts or precise save blocker

The four protocol files, REVIEW.md, frozen spec, own arithmetic and independent checker, three passing outputs, source/hash receipts and finalizer are saved in this run. STATUS has two lines; WORKLOG and LEARNED updated. Exact claim/progress field sets and identical PROGRESS/PACKET_DELTA with packet_ids=[A061] checked. out/PERSISTENCE_RECEIPTS.json records local sizes/hashes; all files below20MB. Source folders untouched. Shared registry adoption, remote mirror, additional external review and publication unverified. No save blocker.

## Universal bridge

C019 stopping-tree payment moves from an unpaid repeated-fallback boundary to independent scoped acceptance of A064's point-control residual rate8+2/ln2<11 and its data-interleaved nonnegative global reserve, verified by114242 exact assertions with actual stopped terminals. No universal FEI constant improves: arbitrary initial core reserves and overlapping non-point/shared-data controller transfer remain unpaid. NEXT changes precisely that geometry at one A038/A039 mixed-history query with one owned release and both terminal bills; it is the shortest route from this paid mechanism toward universal FEI because repeating disjoint point-priority families would leave the same universal resource gap untouched.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A061 stage5 complete: A064 repeated physical fallback controller clause and conditional priority assembly independently HOLDS; 114242 exact primary assertions PASS; universal core/overlapping-controller payment OPEN.\nNEXT: Audit one selected non-point overlapping mixed-history query on A038/A039 with inherited core reserves, owned kappa, both H-Q terminals and one unused influence account; A087/A091/A094 challenge scope.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Stage5 consumed A064 repeated-fallback payment. Independent sector proof reconstructs B-kappa and actual p(1-xy) mismatch; rate<11 and conditional global assembly HOLDS without repair. Separate labelled truth-table checker:2592 local cases plus64 complete interleaved trees/32704 nodes,114242 primary exact assertions PASS; pilot23869 separate.117 growing reserve branches retained with actual H-Q terminals. No new broad claim; universal inherited-core and overlapping non-point payment still open.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage5 reviewed A064 repeated fallback: for F=A*u+(1-A)G with u independent of actual same G on both children, d=p(1-Eu*EG), and B-kappa=Bprofile+(c-k)W. Bound c<=2p, k>=0 and amplitude Phi(a²,b²)<=2|ab| give B-kappa<=8d, D-kappa<11d. In ordered disjoint point priorities, inherited q*r is a controller martingale, so SAME Q handles data and controls with reviewed price C+11/2 and11. Root2I_ctrl and queried rate11 add to13. Growing individual child reserve is legal; expected Q grows by at most C Pi_data. Controller-resolved, data-resolved and full-completion boundaries differ: retain actual H-Q. Scoped independent local/assembly review does not pay arbitrary initial r, overlapping non-point controllers or physically shared data.\n')
assert len((OWN/'STATUS.md').read_text().splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
files=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json')+[OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']
for p in files:assert p.stat().st_size<20*1024*1024
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'at':now,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in files],'full_fei':'OPEN','mirror':'UNVERIFIED'})
print(json.dumps({'status':'SAVED','assertions':total,'review':'INDEPENDENT_NEW_SCOPE_HOLDS_WITH_REVIEWED_DEPENDENCIES','files':len(files),'run':str(RUN)},indent=2))
