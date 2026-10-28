from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1];agent=run.parents[1];out=run/'out'
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
main=json.loads((out/'CHECK.json').read_text(encoding='utf-8'));front=json.loads((out/'FRONTIER.json').read_text(encoding='utf-8'))
assert main['status']==front['status']=='PASS';assert main['cases']==18 and front['cores']==278
assert all(Q(x['sigma2'][1])<0 and Q(x['remaining'][0])>Q(3,4) for x in main['rows'])
assert Q(front['minimum_pair_lower'])>Q(33,20)
checks=main['assertions']+front['assertions'];assert checks==7464
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
paths=[Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),Path('BOARD.md'),Path('claude/B10/STREAM_NOTES.md')]
for who,when,topic in [('A050','20261022T232833Z','repair-with-scope'),('A046','20261023T002101Z','current-candidate-intake'),('A047','20261023T014805Z','boundary-search')]:
 base=agent.parent/who/'runs'/f'{when}-account03-{who}-{topic}'
 paths.extend([base/'PROOF.md',base/'CLAIMS.json'])
receipts=[]
for p in paths:
 b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(out/'SOURCE_RECEIPTS.json',{'read_this_stage':receipts,'background':'Prior stage SOURCE_RECEIPTS preserves campaign indices, supplemental sources and all four supplied paper text versions; no new literature claim depends on them.'})
report='''# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. Close the actual terminal-budget gap after a paid fair a-pair by allowing arbitrary divergent subsequent DATA-only histories, under supplied core-leaf FEI certificates. All cubes are finite and uniform; Boolean signs; entropy, cross-entropy and KL in bits. The two sign branches and every stopped terminal are retained. Initial source, first prescribed reset and an eligible old booking omega<=1/4 remain in the same account.

New exact statement: for ANY Boolean core h and separately chosen finite adaptive DATA-only stopping trees T_+,T_- on J_s(x,z)=s on x0,h(z) on x1, if every actual terminal restricted core g satisfies H(g)<=4I(g), then the fair pair has mean final surplus E[4I(J_s(g))-H(J_s(g))]>=0. The policies may be different and have different stopping depths. No further query of x is included. In the existing B10 account this preserves total S>=1, so the original signed source/reset owner still has at least3/4 after the old quarter. This is an all-dimensional conditional lemma, not a universal supplier certificate or a proof of FEI.

Separate exact finite result: on six frozen point-tensor cores, querying one data bit in either or both a branches and refreshing the queried children to full-spike1/7 references gives18 paid transactions, each with negative second signed reset. The all-width/general-history refresh assertion remains OPEN.

# sources actually read, revisions and theorem locators

Read the updated supervisor BOARD2026-10-23 03:34UTC, B10 lead v2, own STATUS, and full execution protocol2026-10-11-execution-v2. The old lead finite-grid assignment was completed earlier; this stage follows the newer productive frontier. Read A05020261022T232833 PROOF sections1-5 (correlated lift, paired scope, signed owner); A04620261023T002101 PROOF sections1-7 (original1/8 account and paid1/7 reset); A04720261023T014805 PROOF sections1-6 and A050 claim/review record (post-x full-spike refresh). Source bytes and claim versions are pinned in SOURCE_RECEIPTS. A047 already pays arbitrary post-x data refreshes; that work is not repeated.

The prior A049 stage's source receipts retain the initial campaign documents, supplemental sources and all four context-paper versions. They are background, not new reviewed proof premises here. This stage uses no new outside literature or speculative brain theorem. Current wake receipt reports stale owner-model/state-of-mind notes (about90/74hours); the owner was told before work. Current instructions and current source files govern. Current compute state was ok but physical memory about1.7GB and CPU about98percent; no running work was stopped or throttled. The historical intervention ledger was read-only.

# complete derivation or exact first unsupported line

The full derivation is PROOF.md. Put mu_g=E g and S_g=4I(g)-H(g). Physical edges and finite spectral entropy chain rules give

    I(J_s(g))=(1-s*mu_g)/2+I(g)/2,
    H(J_s(g))<=2+H(g)/2,
    4I(J_s(g))-H(J_s(g))>=-2s*mu_g+S_g/2.       (1)

For the entropy inequality erase x: its remaining spectral law is(delta_empty+p_g)/2, whose entropy is at most1+H(g)/2; the erased bit contributes at most1. This does not use FEI. Each finite adaptive stopping policy partitions the original uniform data cube into disjoint cylinders, so separately for each sign E(mu_g|s)=E h. Averaging(1) over the fair sign cancels its two mean terms exactly, even when T_+ and T_- differ. Consequently

    E_{s,leaf}[4I(J_s(g))-H(J_s(g))]
      >=(1/4)sum_s E_{leaf|s} S_g>=0.             (2)

No independence between stopping policy and data is assumed. The cancellation uses the same original core, the fair pair and both complete sign subtrees. The supplied terminal S_g>=0 is used exactly in the last inequality; it is not asserted for arbitrary Boolean cores without a certificate. The proof remains a finite sum for every dimension and every finite tree; no limit or sampled extrapolation is involved. Individual activation surplus need not be assigned a nonnegative budget.

Application: retain the original1/8 correlated full reference from A046, its actual already-paid1/7 post-a/x reset sigma1, all data-prefix siblings, the b0 child and the old omega<=1/4. The original root margin M0 and actual first reset satisfy M0-sigma1>1. Equation(2) makes every continuing a-pair nonnegative; ordinary core restrictions and retained x-character partners are nonnegative; b0 contributes1. Thus the COMPLETE actual frontier has S>=1 through arbitrary divergent post-a data histories, with inherited references and no further reset. For A0 the original source KL and e=H0-Hf-4(I0-If), exact algebra retains

    S-[A0+e+sigma1]_+=min(S,M0-sigma1)>=1,
    S-[A0+e+sigma1]_+-omega>=3/4.                 (3)

The original source/erasure/outcome/terminal KL chain is unchanged except for its already booked sigma1; it is never restarted. PROOF reconstructs the incoming constants from point-factor entropy, the signs8^4<2*7^4 and7^4<2*6^4, and finite conditional variance. This does not claim a free conversion from the canonical reference falsified in the previous stage.

The finite refresh experiment additionally retains an actual sigma2 after the post-a data query. It builds all full Boolean tables and every inherited/fresh law. The exact atomwise product of conditional-erasure likelihood, outcome likelihood and inherited-child likelihood equals the old likelihood on every positive source/channel atom. Reference-only rows remain in normalization with fair fallback on source-zero rows. All actual child source support is dominated, and every normalization denominator is checked positive. The fresh reference copies the two actual zero-data control masses and uses product full-spike1/7 core masses/4 on the two nonempty-data copies. Data-inactive dummy coordinates retain zero frequency; no artificial factor is added.

All18 tested policies have sigma2<0 and S-[A0+e+sigma1+sigma2]_+-1/4>3/4. This finite statement is deliberately separate from the all-dimensional proof(2)-(3). The smallest frozen example has five physical bits(r2,m1), the exact circuit F=(-1)^a on x0, 1-2*z0*z1 on x=b=1,+1 otherwise. It has no free parameter; the active second-reset KL change is in(-0.002614706806,-0.002614706805), while its inactive reset is exactly zero. These signs are interval certificates in CHECK.json, not a new counterexample to a valid helper.

FIRST UNSUPPORTED LINE: after arbitrary post-a histories, prove the prescribed full-spike refresh has nonpositive signed increment for every width and spectator configuration, or pay its positive cost from the SAME diminished original owner. No such all-dimensional reset statement follows from the18 certificates. More fundamentally, an arbitrary Boolean core still lacks a complete paid correlation-preserving initial supplier; full FEI remains open. The earlier frontier-eligibility gap under supplied terminal core certificates is now closed, and should no longer be conflated with the reset/supplier gap.

# executed validation with domain, arithmetic, commands and outputs

Both specs were written before their searches. FROZEN_SPEC: check.py v1, six fixed(r,m)=(2,1),(3,1),(4,1),(5,1),(2,2),(3,2), all three nonempty a-branch query subsets,18 policies, n<=9, no symmetry other than homogeneous factor/coordinate relabeling. Integer Walsh and Fraction probabilities;32-term positive atanh log series, range reduction to[1,2], geometric omitted tail2z^65/[65(1-z^2)], z<=1/3, and outward80-bit dyadic rounding. Memory estimate80MB, maximum55seconds, no automatic dimension growth. Pilot6policies/618assertions PASS0.1326seconds; main18policies/3646assertions PASS0.8146seconds. Commands: python -X utf8 code/check.py --freeze; --pilot; then without flags.

FRONTIER_SPEC: independently written frontier.py, ALL278 Boolean cores on0..3 variables with no symmetry quotient. Direct character sums rather than Walsh; separate40-term rational log arithmetic. It verifies the supplied H(core)<=4I(core) for each nonconstant core, exact zero entropy for constants, conditional-mean partitions and activation influences. Dynamic programming includes stopping and every fresh-coordinate continuation at every state. It covers every pair of independently chosen data trees: at n3 there are244 trees per sign and59,536 policy pairs per core. Interval minima enclose all policies even when candidate intervals overlap; no unique optimum is claimed from an overlapping comparison. All resulting pair-surplus lower bounds exceed33/20. Pilot22cores/266assertions PASS0.0458seconds; main278cores/3818assertions PASS1.0428seconds. Commands: python -X utf8 code/frontier.py --freeze; --pilot; then without flags.

Main plus independent frontier checks total7464 exact assertions. Small/boundary cases include constant, character, all0..3bit cores, width-two factor endpoints and separately queried sign branches. The formal all-dimensional implication is the finite-partition proof, not finite enumeration. Source/reference denominator positivity and full terminal retention are checked where used. No mathematical checker failed. No blind external review is claimed.

All executed computations estimated<=80MB and completed below60seconds; no GPU, heavy admission job or detached process. Fresh memory admission result is in ADMISSION.json; when not admitted no compiler is launched. Lean rung is NOT Lean-checked: the key entropy/conditional-mean argument is an analytic proof with exact finite reproduction. A scalar formalization would certify neither the entropy translation nor the actual full-source account, and no such certification is represented here.

# proof dependencies and changed downstream conclusions

The abstract paired-data lemma(1)-(2) is self-contained and uses explicit terminal core certificates as hypotheses. Its application(3) consumes the source-bound A046 incoming margin and first-reset theorem at the exact supplied reference/old-booking scope; PROOF rederives the required constants. Current A050 correlated lift and A047 post-x refresh remain unchanged. This is a repair/continuation of an existing live mechanism rather than another broad candidate. The finite additional reset check is not used to justify the all-history theorem.

Changed downstream conclusion: a-pair eligibility is no longer restricted to stopping immediately after a, or to identical subsequent data policies. Source-bound conditional-mean cancellation transports the actual terminal budget through arbitrary divergent data histories. New resets and arbitrary-core initial suppliers remain unpaid. No universal FEI constant improves. Independent acceptance and supervisor adoption are pending.

# one next mathematical action and independent reviewer

NEXT: derive or refute an all-width signed refresh inequality for the activation lift J_s(point-factor*tensor spectators) after one data query, using the already1/7-reset incoming law and preserving the original source, sigma1, old quarter and both sign/data subtrees. If a positive increment occurs, extract the smallest exact full-law circuit and compare it to the actual remaining original margin. A046/A050 should reconstruct the conditional-mean frontier argument, and A047/A092 should independently audit the signed reset/interface. No messages are sent; the local source-bound files are the handoff.

# actual persistence receipts or precise save blocker

Four exact-schema protocol files, PROOF, frozen specs, two independent implementations and all exact outputs are saved in this assigned A049 run. STATUS is current and has two lines; WORKLOG and LEARNED append this stage. SOURCE_RECEIPTS pins read-only inputs; PERSISTENCE validates required keys, statement hashes, matching PROGRESS/PACKET_DELTA bytes and file-size caps. No local save blocker. No git, mail, other-agent mutation, protected-tree edit, brain write, deletion or remote publication. Independent review, canonical adoption, supervisor copying and mirror verification are pending or unverified.

Universal bridge: This stage moves C019 stopping-tree payment and C024 history transfer by proving fair activation-pair conditional-mean cancellation for every dimension and arbitrary divergent finite data policies, under explicit core-terminal certificates. It closes the actual paired frontier-eligibility gap and preserves at least3/4 of the SAME signed original owner after the earlier paid reset and old quarter;7464 exact checks corroborate the interfaces. The universal FEI constant improves by zero. General prescribed refresh payment and an arbitrary-core correlated supplier remain unpaid. NEXT attacks the reset inequality at the exact now-certified frontier, rather than repeating canonical-source counterexamples or another isolated class entropy bound.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
cid='A049-DIVERGENT-ACTIVATION-PAIR-DATA-FRONTIER'
statement='For every finite uniform Boolean core h and separate finite adaptive fresh-data-only stopping policies for J_s(x,z)=s on x0,h(z) on x1, s=+/-1 fair, retaining both complete subtrees and keeping x unqueried, if every actual terminal core g has H(g)<=4I(g), then mean terminal surplus E[4I(J_s(g))-H(J_s(g))]>=(1/4)sum_s E[4I(g)-H(g)|s]>=0. The proof uses E[Eg|s]=Eh separately under each finite partition; the two policies need not agree. Applied after the source-bound already paid A0461/7 reset with original lifted1/8 source, M0-sigma1>1 and old omega<=1/4, arbitrary further divergent data-only histories WITHOUT new resets keep whole S>=1 and SAME signed margin>=3/4. Separately18 fixed one-query/reset policies have strictly negative second signed reset and same-owner margin>3/4; no general additional-reset or arbitrary-core supplier theorem is asserted.'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Finite independent uniform bits; Boolean signs; bit entropy and KL.','Same original core and fair sign pair; each sign may use a different finite adaptive data-only stopping partition; x remains unqueried.','Every actual terminal restricted core has supplied H<=4I certificate; all physical reaches and both subtrees retained.','Application inherits exactly A046 original1/8 correlated full reference, actual paid first1/7 reset sigma1 and old booking<=1/4; further histories inherit references without additional reset.','Additional-reset claim is finite only: six specified homogeneous point-tensor cores, first data bit in either/both a branches, same1/7 full-spike activation target.'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A049'],'proof_source':['PROOF.md','REPORT.md','code/check.py','code/frontier.py','out/CHECK.json','out/FRONTIER.json'],'proof_dependencies':[],'review_records':[],'status':'ANALYTIC_PROOF_EXACT_REPRODUCTION_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'General paid post-a prescribed refresh with inherited1/7 law after divergent histories; arbitrary-core paid correlated supplier.','next_consumers':['A046','A050','A047','A092','A036']}
dump(run/'CLAIMS.json',[claim])
next_action='Derive or refute all-width post-a full-spike1/7 refresh inequality with same source, booked first reset and old quarter, at the now-certified divergent-data frontier; retain both subtrees.'
p={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B10','packet_id':'A049','gap_id':'G-R-MISMATCH','attempt_id':'A049-stage18-divergent-pair-frontier','method':'Finite conditional-mean cancellation plus exact full-law post-a reset checks and independent all-core/all-policy direct-character audit.','mathematical_delta':'All-dimensional paired terminal eligibility after arbitrary divergent data histories; SAME owner>=3/4 after old reset/quarter.18 finite reset policies negative;7464 exact main checks.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'CONDITIONAL_ALL_DIMENSIONAL_PROOF_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[cid+'@1'],'source_artifacts':['PROOF.md','REPORT.md','out/FROZEN_SPEC.json','out/FRONTIER_SPEC.json','out/CHECK.json','out/FRONTIER.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['General additional reset and arbitrary-core supplier remain open.','Independent review, supervisor adoption and mirrors unverified.','No Lean certification; low physical memory admission recorded.'],'packet_ids':['A049']}
dump(run/'PROGRESS.json',p);dump(run/'PACKET_DELTA.json',p)
(agent/'STATUS.md').write_text('STATE: A049 stage18 saved: arbitrary divergent post-a data histories retain SAME owner>=3/4 after old reset/quarter;18 finite second-reset policies negative;7464 exact checks PASS; review pending, FEI OPEN.\nNEXT: A046/A050/A047/A092 review; prove or refute all-width post-a full-spike1/7 refresh against SAME original Q, sigma1 and old quarter, with both full subtrees retained.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' — Stage18: consumed A050 correlated lift, A046 paid1/7 reset and A047 all-post-x refresh. Derived arbitrary-core paired-data eligibility under actual terminal core certificates: signed means cancel across independent divergent a-policies; SAME full owner>=3/4 after old reset/quarter.18 finite second-reset policies/3646 checks PASS0.8146s; all278 small cores/all data-policy pairs3818 checks PASS1.0428s. Total7464. Additional all-width refresh remains unproved; no universal supplier or FEI resolution. Saved full protocol outputs.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' — Post-a frontier repair: J_s(x,z)=s atx0,g atx1 satisfies surplus>=-2s Eg+(4I(g)-H(g))/2 by exact influence and H(J)<=2+H(g)/2. For ANY separate finite adaptive data partitions in the two fair sign branches, E Eg|s=Eh; signed means cancel, so paired mean surplus>=0 under supplied terminal core FEI. Thus prior same-source1/7-reset B10 account retainsS>=1 and>=3/4 after oldquarter through arbitrary divergent data histories, WITHOUT new resets.18 tested further1/7 refreshes negative; that is finite evidence only, not an all-width refresh theorem. Next missing component is reset price, not paired eligibility.\n')
proto=json.loads(paths[0].read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(proto['claim_fields']);assert set(p)=={x.split(' (')[0] for x in proto['progress_fields']}
assert all('# '+x in report for x in proto['report_fields']);assert report.rstrip().split('\n\n')[-1].startswith('Universal bridge:')
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
fs=[x for x in run.rglob('*') if x.is_file() and x.name!='PERSISTENCE.json']+[agent/x for x in ('STATUS.md','WORKLOG.md','LEARNED.md')]
saved=[]
for x in fs:
 b=x.read_bytes();assert len(b)<20*1024*1024;saved.append({'path':str(x),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(out/'PERSISTENCE.json',{'status':'PASS_LOCAL','stamp':stamp,'files':saved,'independent_review':'PENDING','remote_copy':'UNVERIFIED','exact_protocol_fields':True})
print('SAVED',checks,'exact main checks;',len(saved),'persistence hashes; FEI OPEN')
