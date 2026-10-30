import copy,hashlib,json
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HOME=ROOT.parents[1]
assert HOME.name=='A009'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
P=json.loads(PROTO.read_text(encoding='utf-8-sig'))
def read(name): return json.loads((ROOT/'out'/name).read_text(encoding='utf-8'))
def write(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
outputs={name:read(name) for name in ['PILOT.json','CHECK.json','VERIFY.json','DAMAGED_PILOT.json','DAMAGED_CHECK.json','DAMAGED_VERIFY.json']}
assert all(x['all_passed'] for x in outputs.values())
assert outputs['CHECK.json']['functions']==15
assert outputs['DAMAGED_CHECK.json']['functions']==10
total=sum(outputs[n]['checks'] for n in ['CHECK.json','VERIFY.json','DAMAGED_CHECK.json','DAMAGED_VERIFY.json'])
assert total==32100
stamp=datetime.now(timezone.utc).isoformat()
source=Path('~/brain_workers/FEI100_20261011/agents/A008/runs/20261021T234312Z-fleet03-A008-gate-label-compression')
oldclaims=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8-sig'))
rootclaim=copy.deepcopy(next(c for c in oldclaims if c['claim_id']=='A008-ALL-BOOLEAN-IMPLICANT-ROOT-NORMALIZER-PAYMENT'))
rootclaim['review_records'].append({'reviewer':'A009','verdict':'UNIVERSAL_ROOT_SUBSTATEMENT_HOLDS_UNCHANGED_NO_REPAIR; PRIVATE_LEAF_COROLLARY_HAS_UPSTREAM_AUTHOR_DISCLOSURE','proof_source':str(ROOT/'REVIEW_ROOT.md'),'validation':str(ROOT/'out/CHECK.json'),'method':'All-dimensional cube-cut/fiber/packing reconstruction; every signed implicant on all270 nonconstant functions n<=3 checked independently;1904 faces; no upstream private-leaf acceptance asserted','reviewer_supplied_substantive_repair':False,'timestamp_utc':stamp})
rootclaim['status']='UNIVERSAL_ROOT_SUBSTATEMENT_INDEPENDENTLY_RECONSTRUCTED_BY_A009; COROLLARY_UPSTREAM_AUTHOR_DISCLOSED; LOCAL_ADOPTION_PENDING'
statement='For every integer pair2<=a<=b, let G be the positive simple graph K_(a,b) with one named edge deleted and f_G its actual uniform Boolean edge DNF. On precisely its ab-1 surviving positive edge primes, fix both endpoint orders, rarity1/4 and global weights lambda_e=1/b. These satisfy every coordinate incidence row. The original nonempty-conditioned queue, with SAME D=(1+1/(4b))^(ab-1)-1, has an explicit distinct-run output subprobability Q positive on every nonempty Fourier set: one-sided isolated roots sum over actual neighbors; mixed sets use a double-star with at most one extra actual singleton root; the missing endpoint pair uses two actual isolated roots. Its complete nonempty cross-entropy C=sum_(A!=empty) fhat_G(A)^2[-log2 Q(A)] is strictly less than297I(f_G)/8<38I(f_G), including all root rarities, unused-root probabilities, selected subsets, counts, attachments, chronology and output ambiguity. Its complete non-root expectation is at most36I(f_G). No extra controller, private neighbor, optimal-weight assertion, arbitrary-edge-deletion transfer or new FEI class claim is used. The undamaged calibration on all K_(a,b),1<=a<=b, has the same construction at complete cost<97I/8<13I.'
hypotheses=['Uniform independent physical signs; actual Boolean squared Fourier spectrum and physical influence; costs in bits','Precisely the surviving positive edge primes; both orders and actual rarity1/4 fixed','One globally fixed feasible weight vector lambda=1/b, independent of the sampled set','Original queue and conditional root normalizer; ideal reference probabilities; no free prefix rounding','The damaged family requires a,b>=2 so all extra singleton-root neighbors exist; the main leafless subfamily has a,b>=3']
canonical=json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')
newclaim={
 'claim_id':'A009-ONE-MISSING-EDGE-LEAFLESS-COMPLETE-CERTIFICATE','version':1,
 'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(canonical).hexdigest(),
 'contributors':['A009'],'proof_source':{'path':str(ROOT/'ONE_MISSING_EDGE.md'),'calibration':str(ROOT/'LEAFLESS_CERTIFICATE.md'),'code':[str(ROOT/'code/damaged.py'),str(ROOT/'code/damaged_verify.py')],'certificates':[str(ROOT/'out/DAMAGED_CHECK.json'),str(ROOT/'out/DAMAGED_VERIFY.json')]},
 'proof_dependencies':[{'source':str(Path('~/mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex')),'use':'Original conditioned queue, actual root/count/multiset/label probabilities; no universal payment assumed'},{'claim_id':rootclaim['claim_id'],'version':rootclaim['version'],'statement_sha256':rootclaim['statement_sha256'],'use':'Universal width-two root substatement ONLY, independently reconstructed here; no private-leaf premise'}],
 'review_records':[{'reviewer':'A009','verdict':'AUTHOR_ANALYTIC_PROOF_AND_SEPARATE_ORIGINAL_PROBABILITY_REPLAY; NO_INDEPENDENT_AGENT_ACCEPTANCE','validation':str(ROOT/'out/DAMAGED_VERIFY.json'),'lean_status':'SETUP_UNVERIFIED; admission held, no compiler process','timestamp_utc':stamp}],
 'status':'ANALYTIC_PROOF_EXACT_CHECKED_PENDING_INDEPENDENT_AGENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A006','A007','A008','A010','A015','A086','B02','B20']}
claims=[rootclaim,newclaim]
for c in claims: assert set(c)==set(P['required_per_run']['claim_fields'])
write('CLAIMS.json',claims)
next_action='Pay a growing deleted matching on SAME surviving primes by actual bounded-cost forest repair and spectral/influence payment avoiding a square in the number of deleted edges; A008/A086 review38I theorem and A008 root substatement.'
progress={
 'protocol_revision':P['revision'],'run_id':ROOT.name,'stream':'B02','packet_id':'A009','gap_id':'G-J-COST','attempt_id':'A009-substantive-stage6-one-missing-edge',
 'method':'Independent root-lemma review; explicit global incidence weights; actual double-star/extra-root queue certificate; point-defect Fourier comparison; changed physical-influence payment',
 'mathematical_delta':'SAME complete reference on leafless K_(a,b) minus one edge paid below38I for ALL2<=a<=b; non-root<=36I; actual missing pair paid by two real roots. Calibration complete K_(a,b)<13I. A008 universal root substatement independently HOLDS.',
 'deliverable_status':'COMPLETE_LOCAL; SUPERVISOR_COPY_AND_MIRROR_UNOBSERVED',
 'mathematical_status':'RESTRICTED_MECHANISM_PROOF_EXACT_CHECKED; NEW_THEOREM_REVIEW_PENDING; FULL_FEI_OPEN; NOT_LEAN_CHECKED',
 'claim_versions_used':[{'claim_id':rootclaim['claim_id'],'version':1,'statement_sha256':rootclaim['statement_sha256'],'scope':'universal root substatement only'}],
 'claims_created_or_changed':[{'claim_id':newclaim['claim_id'],'version':1,'action':'created restricted same-reference certificate'},{'claim_id':rootclaim['claim_id'],'version':1,'action':'independent universal-root substatement review; upstream author disclosed'}],
 'source_artifacts':['REPORT.md','ONE_MISSING_EDGE.md','LEAFLESS_CERTIFICATE.md','REVIEW_ROOT.md','out/SOURCES.json','out/CHECK.json','out/VERIFY.json','out/DAMAGED_CHECK.json','out/DAMAGED_VERIFY.json','out/LEAN.json'],
 'next_consumers':newclaim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal complete graph/Boolean payment remains open','New38I certificate awaits independent-agent review','Lean admission held, no compiler process','Initial task working hook failed: checklist lock held too long','Wake flagged stale owner-model/state-of-mind notes; owner notified; no affected note used as a premise'],
 'packet_ids':['A009']}
fields={x.split(' (')[0] for x in P['required_per_run']['progress_fields']}
assert set(progress)==fields
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A009/B02 substantive stage6 (scheduled stage17). For ALL integers2<=a<=b pay the COMPLETE original nonempty-conditioned queue cross-entropy on the actual positive edge DNF K_(a,b) minus one named edge, using one globally fixed feasible vector on its SAME surviving primes. ONE_MISSING_EDGE.md proves C<297I/8<38I, including complete non-root occupation<=36I. For a,b>=3 no vertex is a private leaf. The complete K_(a,b) reference is an explicit <13I calibration, not a new FEI class result. Units are bits. Full FEI remains OPEN; the current user deadline23 October14:49UTC supersedes the11 October baseline endpoint.

# sources actually read, revisions and theorem locators

Full execution protocol revision{P['revision']}, current BOARD, B02 notes, own substantive stage5 STATUS/LEARNED/WORKLOG and proof were read before dispatch. New A006 stage7 REPORT, A007 stage7 REPORT/KMM_PAYMENT, and A008 stage6 REPORT/ROOT_PAYMENT/CLAIMS/REVIEW_A009 were consumed. Original forests.tex eq:forestpacking, eq:forestrootconstants, original queue items(i)--(iv), eq:forestconditioning and forest-cost locators fix all probabilities. Campaign README/current status/registries/packet matrix/plan and supplement were inspected at the joint-code navigation scope; prior complete baseline reading is inherited. out/SOURCES.json pins the actual bytes and out/BASELINE_EXCERPTS.json saves selected passages, including all four supplied paper text versions. These PDF-extracted texts fail strict UTF8 at single-byte soft hyphens; an explicit strict cp1252 view is recorded, source bytes untouched. No paper theorem is a new premise. The two-wording math recall returned unrelated graph-dependence and density-packing cards, none imported. Brain recall warned that read-once FEI class novelty is not progress; no such novelty is claimed here.

# complete derivation or exact first unsupported line

REVIEW_ROOT.md reconstructs A008's universal signed-implicant root inequality by cube min-cut, actual false fibers, packing rows and ln D<=S. Verdict HOLDS unchanged for that universal substatement; A009's upstream private-leaf authorship is disclosed for the separate<10I corollary. The new construction fixes lambda=1/b, both orders, rarity1/4, and original D before sampling. One-sided events sum over actual surviving neighbor labels. Mixed events use one actual double-star, at most one extra real singleton root, and two isolated roots on the missing pair. The complete numerator includes root rarity, selected subsets, child counts, attachment multiset, chronology and all absent surviving roots. No reference change or free gate is used.

Deleting the one edge changes exactly one physical input. Every coefficient perturbation has magnitude2^{{1-a-b}}, and every old nonempty coefficient has at least that magnitude, so P_actual<=4P_old pointwise. Physical influence obeys I_actual>=(2/3)I_old, proved from the exact single-vertex crossing change and a,b>=2. Two explicitly computed label charges are<=5I_old on the undamaged law, hence<=30I_actual on the damaged law; six bits per actual expected degree give complete occupation<=36I_actual. The independently reconstructed universal root bound is applied ONCE to actual D and I, giving<297I_actual/8<38I_actual. All-dimensional inequalities, exact boundary cases and positive denominators are written in the proofs.

The first unsupported line is a growing deletion matching: two roots need not repair all owned vertices, and naive Fourier domination grows quadratically with the number of deleted edges. Completion changes the Boolean function and supplies no free transfer. The38I result is a restricted coding-mechanism theorem, not arbitrary graph PI-J, global optimization or a new general FEI result.

# executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC/REVIEW_SPEC/VERIFY_SPEC preceded their jobs; DAMAGED_SPEC and DAMAGED_VERIFY_SPEC preceded the additional genuine deletion mechanism. Pilot complete tables:6 functions,{outputs['PILOT.json']['checks']} assertions,{outputs['PILOT.json']['elapsed_seconds']:.6f}s. Full complete tables:all15 integer pairs1<=a<=b<=5, maximum physical dimension10,{outputs['CHECK.json']['checks']} assertions,{outputs['CHECK.json']['elapsed_seconds']:.6f}s. Scalar checks cover all2080 pairs1<=a<=b<=64, count recurrences through128, and root fibers cover all270 nonconstant functions n<=3 and1904 actual signed implicant faces. This exhausts only those stated finite domains; written proofs give all-size conclusions.

Independent original Bernoulli-root/direct-character replay:6 complete tables,290 distinct explicit traces,{outputs['VERIFY.json']['checks']} assertions,{outputs['VERIFY.json']['elapsed_seconds']:.6f}s. Genuine deletion pilot:3 functions,{outputs['DAMAGED_PILOT.json']['checks']} assertions,{outputs['DAMAGED_PILOT.json']['elapsed_seconds']:.6f}s. Deletion full:all10 pairs2<=a<=b<=5,{outputs['DAMAGED_CHECK.json']['checks']} assertions,{outputs['DAMAGED_CHECK.json']['elapsed_seconds']:.6f}s. Separate deletion replay imports no author helper, chooses a maximum-coverage real root, checks all surviving labels and at most two roots, uses full present/absent Bernoulli factors:3 functions,211 traces,{outputs['DAMAGED_VERIFY.json']['checks']} assertions,{outputs['DAMAGED_VERIFY.json']['elapsed_seconds']:.6f}s. Nonpilot total32100 successful exact assertions; overlapping pilot assertions are separate. Every displayed sign uses integers/Fraction or positive atanh log bounds with proved tails and outward dyadic rounding. Floating ratios are diagnostics only.

Commands from A009: python -X utf8 runs/{ROOT.name}/code/check.py --pilot; check.py; verify.py; damaged.py --pilot; damaged.py; damaged_verify.py; read_sources.py; finalize.py (all same code directory). No symmetry quotient beyond exchanging parts, domain escalation, GPU, detached job or>300MB search was used. Memory estimates30--40MB; all mathematical algorithms finished under60s. Fresh memok before the optional formal check exited0 (4.6GB physical and21.8GB commit available), but lean_check's stricter admission held, exit1, no compiler process. out/LEAN.json preserves the scalar recurrence statement, command and result. Rung: analytic proof with exact finite and separate original-probability checks, NOT Lean-checked, independent-agent review pending.

# proof dependencies and changed downstream conclusions

The new theorem uses original queue definitions and only A008's universal root substatement, reconstructed here independently. The core spectrum, point perturbation and influence comparison are proved directly; no A007 controller transfer, unreviewed LP optimum, guessed phase or arbitrary FEI claim is needed. Root's dependency on A009 private leaves is only its optional corollary, not the universal substatement used here, so the proof graph is acyclic at actual used scope. A008's<10I improvement of the old private-leaf reference is consumed without rewriting that old claim. Its ceiling changes because root payment improved, not because old data changed. The new38I number concerns a DIFFERENT damaged leafless family. No independent-agent acceptance or supervisor adoption of the new certificate is presumed.

# one next mathematical action and independent reviewer

{next_action} This is the shortest extension because it tests whether bounded local repairs and exact spectral corrections compose on the SAME reference, rather than replacing them with another known FEI family. No messages were sent and no other-agent folder was written.

# actual persistence receipts or precise save blocker

All four required protocol files, three mathematical notes, frozen specs, own code, exact outputs, source receipts and Lean limitation are saved under this unique A009 run. out/RECEIPTS.json records local SHA256/size readback after verifying exact schema keys, PROGRESS=PACKET_DELTA, statement-hash convention, two-line STATUS, successful outputs and20MB caps. STATUS, WORKLOG and LEARNED are updated only under A009. Initial checklist working hook failed with lock held too long; source inventory's first strictUTF8 decode failed on legacy PDF text and was repaired by an explicitly recorded decoding view, without source edits. Neither is a mathematical failure. Session wake warned of stale owner-model/state-of-mind notes and the owner was alerted before relying on them. No existing work was stopped. No git, mail, trading access, research brain-store write, shared-index mutation or public release occurred. Supervisor copying, mirror verification and external acceptance are unobserved.

# Universal bridge

C020/PI-J moves from arbitrary-core/private-leaf complete certificates to an actual shared, leafless incidence with one missing edge: SAME surviving-prime complete cost<38I for every2<=a<=b, without extra physical controller influence, with a real paid two-root repair and changed-spectrum/changed-influence accounting. The root term is independently reconstructed universally and used once; all non-root occupation is paid on this explicit family. No universal FEI constant changes. A growing deleted matching still needs a bounded actual forest repair plus spectral payment without quadratic loss; NEXT attacks exactly that compositional obstruction on the original table, rather than collecting an isolated known class result.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(HOME/'STATUS.md').write_text('STATE: A009 stage6 saved: SAME leafless K_ab minus one edge complete cost<38I; A008 universal root substatement HOLDS;32100 nonpilot exact checks PASS; Lean admission held; FEI OPEN.\nNEXT: Pay growing deleted matching with SAME surviving-prime reference, bounded actual roots and nonquadratic spectral payment; A008/A086 review38I theorem.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{stamp} | Substantive stage6 {ROOT.name}: independent universal-root review; full same-reference complete K_ab<13I then actual K_ab-minus-one-edge<38I, all integer2<=a<=b. Pointwise actual spectrum<=4old, I_actual>=2old/3; missing pair paid by two real roots.32100 nonpilot exact checks;501 independent original queue traces; Lean admission held/no compiler; new certificate review pending, full FEI OPEN. Initial checklist lock and legacy PDF-text decode issues recorded. All research writes local.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage6: On precisely K_(a,b) minus one edge primes, all2<=a<=b, lambda=1/b and original D=(1+1/(4b))^(ab-1)-1 give complete C<297I/8<38I. One-sided runs sum surviving neighbors; mixed double-star needs at most one extra singleton root, missing pair uses two roots with outside neighbors. Actual perturbation is one physical point, so P_new<=4P_old and I_new>=2I_old/3. All rarity/count/attachment/absent-root factors retained. At a,b>=3 there are no private leaves. This is a coding certificate, not new FEI class novelty. Complete K_ab calibration<13I. A008 universal root substatement independently reconstructed;<10I private-leaf corollary has our upstream author disclosure. Growing deletion count can break both bounded repair and constant Fourier comparison; completion is not a transfer.\n')
(ROOT/'REVIEW_ROOT.md').write_text((ROOT/'REVIEW_ROOT.md').read_text(encoding='utf-8')+'\nValidation completed: all270 nonconstant n<=3 functions,1904 signed implicant faces, every actual outside false fiber, AND sharpness through64. out/CHECK.json and separate full queue receipts passed. No Lean certification; admission held.\n',encoding='utf-8')
write('out/HASH_CONVENTION.json',{'new_claim':'SHA256 UTF8 of sorted compact JSON with exact_statement and hypotheses, ensure_ascii=False','source_claim':'Original source-declared digest retained unchanged; raw file hash pinned in SOURCES.json; scope of independent review stated explicitly'})
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in P['required_per_run']['report_fields']:
 assert '# '+field in report
receipts=[]
for p in ROOT.rglob('*'):
 if not p.is_file() or p.name=='RECEIPTS.json' or '__pycache__' in p.parts: continue
 raw=p.read_bytes(); assert len(raw)<20*1024*1024
 receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('out/RECEIPTS.json',{'at_utc':stamp,'status':'LOCAL_READBACK_VALIDATED','nonpilot_checks':total,'files':receipts,'remote_save':'UNOBSERVED','independent_agent_review':'PENDING'})
print(json.dumps({'status':'LOCAL_COMPLETE','nonpilot_checks':total,'files':len(receipts),'run':str(ROOT),'new_claim':newclaim['claim_id']}))
