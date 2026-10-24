from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parent.parent
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def H(b):return hashlib.sha256(b).hexdigest()
def save(p,x): (RUN/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
V=json.loads((RUN/'out/validation.json').read_text());assert V['status']=='PASS' and V['cases']==1652
sourcepaths={
 'A056_REPORT':Path(r'~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T233147Z-account05-A056-balanced-composition\REPORT.md'),
 'A056_INTERFACE':Path(r'~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T233147Z-account05-A056-balanced-composition\BIASED_ERASURE_INTERFACE.json'),
 'A056_CLAIMS':Path(r'~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T233147Z-account05-A056-balanced-composition\CLAIMS.json'),
 'A059_REVIEW_A057':Path(r'~\brain_workers\FEI100_20261011\agents\A059\runs\20261011T224320Z-account05-A059-decomposition-depth\REVIEW_A057.md'),
 'B12_NOTES':Path(r'~\brain_workers\FEI100_20261011\claude\B12\STREAM_NOTES.md'),
 'A024_REPORT':Path(r'~\brain_workers\FEI100_20261011\agents\A024\runs\20261011T223622Z-account05-A024-biased-child-stability\REPORT.md'),
 'A027_REPORT':Path(r'~\brain_workers\FEI100_20261011\agents\A027\runs\20261011T234627Z-account05-A027-block-selection\REPORT.md')}
receipts=[]
for name,path in sourcepaths.items():
 b=path.read_bytes();ext=path.suffix;(RUN/'out'/f'{name}{ext}').write_bytes(b)
 receipts.append({'name':name,'source':str(path),'sha256':H(b),'bytes':len(b)})
save('out/SOURCE_RECEIPTS.json',receipts)
old=json.loads((ROOT/'runs/20261011T220314Z-account05-A057-coherent-restriction-remainder/CLAIMS.json').read_text())
for claim in old:
 claim['review_records'].append({'reviewer':'A059','verdict':'ACCEPT_AT_STATED_SCOPE','source':'out/A059_REVIEW_A057.md','method':'Independent analytic reconstruction; no source repair and no claim of rerunning original census'})
 claim['status']='ACCEPTED_LOCAL_INDEPENDENT_REVIEW'
 claim['proof_source']={'author_run':'20261011T220314Z-account05-A057-coherent-restriction-remainder','path':str(ROOT/'runs/20261011T220314Z-account05-A057-coherent-restriction-remainder/COHERENT_REMAINDER_PAYMENT.tex')}
statement='For every Boolean sign core u on a finite uniform cube, r>=1 fresh point-control bits, p=2^(-r), a=1-Eu, and F=1+A_r(u-1), any complete adaptive physical core-first tree followed by the complete control suffix has total capped current biased outer-erasure bank <=(4+2/(e ln2))p I(u)+5rp a<=(4+2/(e ln2))I(F), in bits. At a core node m=Eu_v, beta=hat u_v({i}), v=1-m^2, t=beta^2, the cap is min{M(v),(t/v)M(v)+pt log2(v/t)}, M(s)=Phi((1-p+pm)^2,p^2s)+p(1-p)Phi((1-m)^2,s), Phi(s,t)=(s+t)h2(t/(s+t)); zero-variance and zero-t caps are zero. More precisely any partial core-tree prefix costs <=[4p(1-p)+p^2/ln2+2p/(e ln2)]Pi_I(u)+2rp^2[Var(u)-E Var(u_leaf)]. The nonempty inner-decrement cost and terminal entropy are not asserted to be universally paid.'
hyp=['Boolean +/-1 core; uniform independent physical signs; A_r indicator of one control assignment; r>=1; controls disjoint from core.','At each reached node recompute actual core mean and variance; no restriction-balancedness assumption.','Complete theorem queries core to constant leaves then controls; partial-prefix formula retains actual activated terminal functions.','Entropy units bits; influence uniform total flip influence.']
new={'claim_id':'A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':H(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()),'contributors':['A057'],'proof_source':{'run':RUN.name,'path':'PROOF.md'},'proof_dependencies':['A056 biased positive-sector split/envelope, independently reconstructed in REVIEW_A056.md','Elementary packet bound, Boolean singleton bound, physical influence and mean-variance telescopes; all price estimates proved in PROOF.md'],'review_records':[],'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A056','A059','A091','A090','A024','A064','A097']}
claims=old+[new]
author=json.loads(sourcepaths['A056_CLAIMS'].read_text(encoding='utf-8-sig'))
if isinstance(author,dict):author=author.get('claims',[])
reviewed=[]
for c in author:
 if 'claim_id' not in c:continue
 c['review_records'].append({'reviewer':'A057','verdict':'ACCEPT_AT_STATED_SCOPE','source':'REVIEW_A056.md','method':'Independent physical-pair reconstruction and exact activation-domain implementation; no source repair'})
 c['status']='ACCEPTED_LOCAL_INDEPENDENT_REVIEW';c['proof_source']={'author_run':'20261011T233147Z-account05-A056-balanced-composition','source':'out/A056_REPORT.md','review':'REVIEW_A056.md'}
 claims.append(c);reviewed.append(c['claim_id'])
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',claims)
P={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B12','packet_id':'A057','gap_id':'FEI-B12-A057-INITIAL','attempt_id':'A057-02-recentered-cap-variance-account','method':'Consume A059 review and independently reconstruct A056 biased interface; price exact capped activation gate bank by core influence plus mean-martingale variance; complete point-defect suffix; certify actual physical trees with rational prime-log arithmetic.','mathematical_delta':'Resolved the lead-requested capped current biased gate bank on any complete core-first fresh point-activation tree at K=4+2/(e ln2) bits, keeping negative inner empty-pair credits. Partial-prefix bound names a single variance/control reserve. Arbitrary inner entropy and terminal costs remain open.','deliverable_status':'COMPLETE_SCOPED_PAYMENT_AND_DEPENDENCY_REVIEW','mathematical_status':'CAPPED_ACTIVATION_GATE_BANK_PAID; UNIVERSAL_C019_AND_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'review':'A059' if c in old else 'A057' } for c in old+author],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],'source_artifacts':['PROOF.md','REVIEW_A056.md','FROZEN_SPEC.json','FROZEN_SPEC_V2.json','code/check.py','out/pilot.json','out/validation.json','out/v1_main_stop.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A056','A059','A091','A090','A024','A064','A097'],'next_action':'Test one priority-composed two-core activation with point events sharing a physical control bit; derive its signed capped-gate allocation under a single common control reserve, retaining both terminal core entropies.','stagnant_substantive_attempts':0,'blockers':['No universal payment for nonempty core decrements or arbitrary terminal entropy.','The two-class gate formula relies on a fresh point activation; two different cores with overlapping controls require a common reserve.','New scoped payment awaits A091/A090 review; supervisor adoption and mirroring not observed.'],'packet_ids':['A057']}
assert set(P)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',P);save('PACKET_DELTA.json',P)
R='''# A057 stage 2: the capped recentered activation bank is paid

## exact target, quantifiers, hypotheses and units

The B12 lead asks for a physical-tree payment of the minimum outer-allocation envelope, starting with the original sparse-bent family. This stage proves a scoped all-dimensional payment for every Boolean core u, every fresh point activation F=1+A_r(u-1), r>=1, and every complete adaptive core-first physical tree followed by all control queries. Entropies here are bits. Put p=2^-r, a=1-Eu, K=4+2/(e ln2). The cumulative capped current biased gate bank is at most K p I(u)+5rp a<=K I(F). The constant is approximately 5.0615; the exact symbolic value is used in the proof. A partial core-tree prefix has a separately conserved variance/control reserve. This is not a complete inner-and-terminal entropy payment and does not prove FEI.

## sources actually read, revisions and theorem locators

Read BOARD.md at the stage start, snapshot 2026-10-12 00:39 UTC, B12 STREAM_NOTES.md v2 (23:30 UTC), own STATUS/LEARNED/NEXT_HANDOFF, and EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. The lead assigns the biased identity to A056 and the capped physical-tree bank to A057; this stage follows that allocation instead of rederiving the already completed identity as a new result.

Read in full: A056 stage 20261011T233147Z REPORT, BIASED_ERASURE_INTERFACE and CLAIMS; A024 REPORT stage 20261011T223622Z; B12 lead's L1/L2/R1 claim statements; A059 REVIEW_A057.md stage 20261011T224320Z. A023/A021/A089 learned facts supplied sparse-bent and accounting context. A027 stage 20261011T234627Z report's theorem/proof/terminal/reserve sections and rolling facts distinguish its signed entropy-transport result from this positive cap price. Source snapshots and SHA256 pins are in out/SOURCE_RECEIPTS.json. The earlier stage's exact coherent source is retained there and was not imported anew. No external literature novelty or entire-manuscript audit is claimed.

The A059 review independently reconstructs both A057 v1 claims with no repair. Its acceptance is consumed and recorded locally; original author artifacts and shared registries remain unchanged. REVIEW_A056.md independently reconstructs the biased pair identities and envelope, with a distinct physical activation checker. It records acceptance at source scope, not acceptance of a universal C019 theorem.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete analytic argument. At a core node let m be the actual mean, v=1-m^2, beta the singleton coefficient, t=beta^2, and d its physical influence. The positive gate erasure is
M(s)=Phi((1-p+pm)^2,p^2s)+p(1-p)Phi((1-m)^2,s),
with Phi(s,t)=(s+t)h2(t/(s+t)). The capped envelope is C=min{M(v),(t/v)M(v)+pt log2(v/t)}; t=0 and v=0 give zero. This is A056's current induced-bias outer erasure, not a uniform gate erasure reused after restriction.

The proof shows Phi(s^2,t^2)<=2st in bits by a monotone ratio calculation. The shifted empty-control row obeys (1-p+pm)^2+p^2v<=1. In the second cap branch its p^2 t log2(1/v) term combines with p t log2(v/t), leaving p t log2(1/t)+p(1-p)t log2(v). The latter term is nonpositive. Thus
C<=4p(1-p)d+p^2(2r+1/ln2)t+p t log2(1/t).

The retained rarity term is bounded by [2/(e ln2)]p d. Mean-martingale conservation gives sum w t=Var(u)-E Var(core_leaf), while ordinary physical influence gives sum w d=Pi_I(u). Hence the prefix is at most
[4p(1-p)+p^2/ln2+2p/(e ln2)]Pi_I(u)+2rp^2 V_drop.

For complete core trees, V_drop=Var(u)<=2a and Pi_I=I(u), so the prefix costs at most K pI(u)+2rp a. The control suffix only visits an r-bit point defect with probability a/2. Every point-defect queried erasure is <=3 times that query's influence, so the suffix costs <=3rp a. This gives K p I(u)+5rp a<=K I(F). The prefix's terminal control reserve and the suffix's consumed control influence are accounted for together; the same budget is not reopened at each depth.

The exact erasure ledger retains the negative core empty-pair subtraction:
B_tree(F)=p[B_tree(u)-sum w Phi(m_v^2,t_v)]+sum w M_v(t_v)+expected suffix erasure.
The physical entropy ledger retains the analogous nonempty inner decrement plus actual terminal entropy for partial core trees. Their general payment is not inferred from the cap bound. With outer JS paid separately, the complete-tree inner decrement remains bounded by the explicit pH(u), which is FEI-strength for arbitrary u.

The first unsupported universal line is a common-budget payment of nonempty inner-decrement sums and terminal entropies under a universally valid physical selection policy. For overlapping events with two different cores, even the present two-multiplicity-class gate formula and ownership of control reserve must be rederived; no such extension is claimed. Fresh repeated point controls on a single core collapse to one activation and do not create a new mechanism.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the v1 pilot and main. The 32-case pilot passed in 0.2726 seconds. The first main run reached the 60-second watchdog with no mathematical assertion failure; out/v1_main_stop.json preserves the event. FROZEN_SPEC_V2.json then freezes caching of repeated exact states, unchanged domain, a 60-second pilot and a 120-second main limit. This is a runtime optimization, not a new dimension or search domain. Estimated memory was 70 MB initially and 100 MB for cached v2; no >300 MB job or heavy job was started.

Commands: python -X utf8 runs/20261012T003930Z-account05-A057-coherent-restriction-remainder/code/check.py --pilot, then the same command without --pilot.

V2 pilot: 32 cases PASS. Main: all Boolean cores on n=2,3, r=1,2,3, forward and reverse complete core orders, 1632 actual activation trees; plus the original bent-marker core k=4,6, r=1,2,4,8,12 in marker-first and marker-last order, 20 compressed trees. This includes the original sparse-bent r=2k cases. No symmetry reduction, random sampling, automatic dimension escalation, or Boolean proxy was used.

Main PASS: ASSERTIONS exact assertions/certificates in ELAPSED seconds. Caching means identity counts are distinct evaluated states rather than the number of repeated occurrences. The output records 964 exact biased erasure and 964 exact biased decrement state identities, 1208 cap certificates and singleton bounds, 1652 variance telescope and capped-budget certificates, and 1632 complete-tree erasure/influence identities. Integer Walsh/Fraction spectra reconstruct actual small physical cubes; compressed sparse cases use exact control multiplicities. Rational prime-log coefficient equality proves the identities. Forty-eight-term atanh-series intervals with explicit tails certify signs; a factorial-series interval for e and rational log(2) bound certifies the exact K. Displayed floating ratios are diagnostics only. The maximum observed certified upper ratio was MAXRATIO, which is not an optimal universal constant claim.

## proof dependencies and changed downstream conclusions

The A056 v2 positive-sector split and minimum envelope are independently reconstructed in REVIEW_A056.md. The new price uses elementary packet entropy bounds, the Boolean singleton coefficient domination, and physical influence/mean-variance telescopes, all proved in PROOF.md. It does not assume full FEI, ignore core entropy, use the balanced class at biased nodes, or apply overlapping-product entropy subadditivity. A059's review supplies local independent acceptance of A057 v1; the new payment awaits its own independent review.

A056/A059/A064/A097 can now substitute the actual capped activation-bank price on any specified core-first fresh-point tree, rather than placing an unpaid cap at every depth. A027's signed entropy transport remains a different, compatible statement; this stage controls the positive capped gate envelope itself and does not re-advertise the known H<=8I sparse-bent result.

## one next mathematical action and independent reviewer

Test a priority-composed two-core activation whose two point-control events share one physical control bit. Derive the actual signed gate pairs and a single common control reserve while retaining both terminal core entropies. This is the first ownership extension that does not merely stack equivalent fresh point activations. Reviewers A091 (primary) and A090 (alternate) should independently reconstruct the variance-log cancellation, prefix reserve, and point-defect suffix bound; A024 can challenge the subtraction and induced-bias scope. Reviews of this new payment have not run.

## actual persistence receipts or precise save blocker

All required run files, proof/review, frozen specs, helper code, outputs, source snapshots and rolling files are written only inside A057. Claim and progress keys are checked against the protocol; the explanatory suffix of its packet_ids field is normalized to the JSON key packet_ids. PROGRESS and PACKET_DELTA are byte-identical. out/PERSISTENCE.json gives file sizes and hashes after readback; no artifact exceeds 20 MB. Shared registries, other agents' files, brain stores and repositories are untouched. Supervisor adoption/mirror copies and new independent review are pending.

## Universal bridge

This stage moves C019 stopping-tree payment by paying the lead's complete capped recentered gate bank, including the control suffix, at K=4+2/(e ln2) on every core-first fresh point-activation tree, with an explicit partial-prefix variance reserve. It removes this outer charge even for arbitrary biased cores and preserves all inner empty-sector credits. Universal inner-decrement and terminal payments, and common-reserve ownership for two distinct cores with overlapping controls, remain open. NEXT tests that first genuine ownership extension rather than another isolated gate class or a repeated activation transfer that still hides arbitrary core entropy.
'''
R=R.replace('ASSERTIONS',str(sum(V['counts'].values()))).replace('ELAPSED',str(V['elapsed_seconds'])).replace('MAXRATIO',str(V['maximum_bank_over_I_upper_diagnostic']))
(RUN/'REPORT.md').write_text(R,encoding='utf-8')
for key in protocol['required_per_run']['report_fields']:assert '## '+key in R
(ROOT/'STATUS.md').write_text('STATE: A057 stage2 capped biased gate bank paid at K=4+2/(e ln2) on all core-first point activations; 1652 cases/10912 checks PASS; prior v1 reviewed; new payment pending; FEI OPEN.\nNEXT: Price one two-core priority activation with events sharing a control bit using a common reserve and explicit terminal core entropies; A091/A090 review the new capped-bank proof.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-12 00:39Z stage — '+RUN.name+': Read board/lead; consumed A059 independent v1 review and A056 biased split. Independently reconstructed A056 v2. Proved capped core-first activation bank K=4+2/(e ln2) using shifted empty-control row, signed variance-log cancellation and a one-time variance/control reserve; exact core empty-pair subtraction retained. v1 main watchdog60s; cached v2 PASS1652 cases,10912 certificates in5.5327s, including original sparse-bent r=2k. Full inner/terminal and overlapping two-core ownership remain open.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
## Stage 2 durable facts

- A059 REVIEW_A057 independently accepts both stage1 claims at their actual balanced/physical-tree scope. Source is preserved with SHA256; acceptance is local pending supervisor adoption.
- A056 biased split is consumed/reconstructed: B_i(F)=q[B_i(h)-Phi(m^2,beta^2)]+M(beta^2), and D_i uses the nonempty paird subtraction plus M+N. Signed corrections may be negative; cap applies to positive M.
- For fresh point activation p=2^-r, M(s)=Phi((1-p+pm)^2,p^2s)+p(1-p)Phi((1-m)^2,s). Keeping its variance log together with p beta^2 log(v/beta^2) leaves a nonpositive p(1-p) beta^2 log(v) term.
- Capped gate prefix <=[4p(1-p)+p^2/ln2+2p/(e ln2)]Pi_I(core)+2rp^2 V_drop. V_drop is the mean-martingale variance budget, introduced once, not a whole-subformula entropy recharge.
- Any complete adaptive core-first point-activation tree plus control suffix has capped gate bank <=(4+2/(e ln2))pI(core)+5rp(1-Ecore)<=(4+2/(e ln2))I(root) bits. Point-defect suffix queried erasure <=3 queried influence. Arbitrary pH(core) and partial-tree terminal entropy remain explicit and unpaid.
- Exact v2 checks passed1652 frozen activation trees and10912 assertions; small-domain actual spectra and trees, sparse-bent controls compressed. Caching repeated exact states repairs runtime, not mathematics. Rational prime-log intervals certify K using a factorial e enclosure. Diagnostic maxratio1.29798 is not an optimality theorem.
- Two overlapping point events on different cores require common control-reserve ownership. Fresh nested events on one unchanged core collapse and are not a new universal mechanism.
''')
files=[]
for path in sorted(RUN.rglob('*')):
 if path.is_file() and path.name!='PERSISTENCE.json':
  b=path.read_bytes();assert len(b)<20_000_000;files.append({'path':str(path.relative_to(RUN)),'bytes':len(b),'sha256':H(b)})
save('out/PERSISTENCE.json',{'run_id':RUN.name,'files':files,'local_readback':True,'mirror_status':'PENDING_SUPERVISOR','new_independent_review':'PENDING','prior_A057_review':'A059 ACCEPT_AT_STATED_SCOPE'})
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'files':len(files)+1,'claims':len(claims),'A056_reviewed':reviewed,'assertions':sum(V['counts'].values()),'schemas':'PASS','run':str(RUN)},indent=2))
