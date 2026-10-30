from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,s):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def js(name,obj):write(name,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
v=json.loads((ROOT/'out/all.json').read_text(encoding='utf-8'))
assert v['status']=='PASS' and v['checks']==11485
sources=[]
peer=Path(r'agents\A059\runs\20261026T223551Z-fleet04-A059-decomposition-depth')
for name in ('PROOF.md','CLAIMS.json','REPORT.md'):
    p=peer/name;b=p.read_bytes();dest=ROOT/'out/sources'/('A059_'+name)
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
    sources.append({'path':str(p),'sha256':sha(b),'snapshot':str(dest.relative_to(ROOT))})
assert sources[0]['sha256']=='5fc2cd77ad465db2b6bcb7ba664c6775d6322ccb242a92609f2e89eb6e1e8696'
for p in [Path(r'BOARD.md'),Path(r'claude\B12\STREAM_NOTES.md'),AGENT/'runs/20261023T132943Z-fleet03-A060-composition-sharpness/REPORT.md']:
    sources.append({'path':str(p),'sha256':sha(p.read_bytes()),'snapshot':None})
js('out/SOURCES.json',sources)
write('out/PILOT_ERRATUM.md','The first pilot failed assertion 6 on a constant function: subtracting equal nonexact log intervals created positive numerical width at exact entropy zero. The helper now evaluates logarithms of powers of two exactly. This changes no search domain or mathematical inequality. Corrected pilot: 661 checks PASS. Main: 11485 checks PASS. Frozen parameters were written before either run.\n')
review={
 'source_claim':'A059-PREPAID-TWO-TICKETS-AND-GEOMETRIC-STOPPING@1',
 'source_statement_sha256':'555770aacd78f4d05d5b613a5c02e406a267155705995d1bf2aac71b7c63303b',
 'verdict':'HOLDS_SCOPED_CONDITIONAL_TRANSACTION_RECONSTRUCTION',
 'scope':'New two-ticket split and independent geometric-stop transaction, conditional on already reviewed A059@2 original source/exterior escrow and universal singleton inequality. All old fees and full terminal functions retained. No retrospective enlargement of A060 smaller owner.',
 'independence_limit':'A060 contributed the singleton dependency. This is a separate reconstruction of the new transaction, not an independent full-chain acceptance.',
 'method':'Exact finite spectra reconstruct influence conservation and pending-principal release on every three-variable core edge; direct actual wrapper and full stopped-tree checks; analytic conditional-mean conservation.',
 'unsupported_extension':'No universal useful entropy-decaying no-killing continuation follows. Fixed-q depth-free stopping can retain asymptotically all root entropy.'}
js('REVIEW.json',review)
statement=('For G_r=z times r disjoint AND2 signs and the actual four-bit bent-point wrapper F_r=b-C+C G_r with C the all-one point, query one first variable per factor, retaining all physical answers and independent dyadic continuation outcomes. If s_j is the survival probability of query j and S_r=sum_j s_j, then H(F_r)=E0+r/8, I(F_r)=7/4+(r+1)/16, E H(F_leaf)=E0+(r-S_r)/8 and E I(F_leaf)=7/4+(r+1-S_r/2)/16, where E0=8-(45/64)log2(3)-(75/64)log2(5). Thus full debit is exactly four times removed influence. For constant horizon-dependent q_r, terminal/root entropy tends to zero iff r(1-q_r) tends to zero; fixed q<1 retains terminal/root ratio tending to one. The same identities retain a positive already-booked deterministic prefix. This obstructs terminal exhaustion using A059 geometric pending potential at fixed original rate, but deterministic no-killing exhaustion of this particular family remains affordable.')
claims=[{
 'claim_id':'A060-EXACT-STOPPED-TERMINAL-RETENTION','version':1,'exact_statement':statement,
 'hypotheses':['finite uniform Boolean cube; entropy bits','r>=1; tag z untouched; disjoint two-variable AND factors','four-bit bent b=(-1)^(u1u2+u3u4), u=(1+x)/2; C all-one point','each selected query is the first variable of a new factor; stopping coins fresh and independent of all core answers','dyadic continuation probabilities in [0,1] for finite physical realizations; both stopped and surviving siblings retained','asymptotic horizon statements have r tending to infinity; old booked prefix is retained, not recredited'],
 'statement_sha256':sha(statement.encode('utf-8')),'contributors':['A060'],
 'proof_source':{'path':'PROOF.md','sha256':sha((ROOT/'PROOF.md').read_bytes()),'validation':'out/all.json','code':'code/check.py'},
 'proof_dependencies':['disjoint Boolean product Fourier entropy/influence identities, rederived in PROOF Section2','A059-PREPAID-TWO-TICKETS-AND-GEOMETRIC-STOPPING@1 supplies target certificate, not a premise of exact terminal formulas'],
 'review_records':[{'reviewer':'A060','verdict':'AUTHOR_PROOF_AND_EXACT_FINITE_CONTROLS','checks':11485,'independent_external_review':False}],
 'status':'PROVED_AUTHOR_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],
 'refutes':['Fixed-q depth-free stopping alone forces a vanishing full-terminal entropy fraction under tensorization'],
 'first_unproved_line':'A necessary entropy-decaying arbitrary-core continuation paid from the same unused original owner, with all old fees and full terminals retained.',
 'next_consumers':['A059','A057','A091','A087','B12','B20']}]
js('CLAIMS.json',claims)
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B12','packet_id':'A060',
 'gap_id':'C019-ORIGINAL-OWNER-USEFUL-CONTINUATION','attempt_id':'A060-stage10-terminal-retention',
 'method':'Scoped new-transaction review plus exact complete-terminal Boolean tensor law and sharp survival asymptotics',
 'mathematical_delta':'A059 new transactions reconstructed conditionally; exact actual-wrapper terminal retention and iff r(1-q_r)->0 exhaustion condition. Fixed original geometric rate cannot exhaust terminals, while deterministic same-family work is affordable; no global impossibility inferred.',
 'deliverable_status':'COMPLETE_LOCALLY','mathematical_status':'FULL_FEI_OPEN; exact theorem author-checked; new independent review pending',
 'claim_versions_used':['A059-PREPAID-TWO-TICKETS-AND-GEOMETRIC-STOPPING@1','A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2','A060 stage9 universal singleton bound'],
 'claims_created_or_changed':['A060-EXACT-STOPPED-TERMINAL-RETENTION@1'],
 'source_artifacts':['out/SOURCES.json','out/sources/A059_PROOF.md','PROOF.md','REVIEW.json','FROZEN_SPEC.json','code/check.py','out/pilot.json','out/all.json','out/lean.log'],
 'next_consumers':['A059','A057','A091','A087','B12','B20'],
 'next_action':'Construct useful entropy-sensitive arbitrary-core continuation whose fee is paid by actual decreasing original influence/resource; test full terminal decay rather than merely unbounded possible depth.',
 'stagnant_substantive_attempts':0,'blockers':['Universal original-owner entropy-decaying continuation unpaid','New theorem external review and supervisor/mirror adoption unverified','Brain wake reported stale personal-context notes; these were not used as mathematical premises'],
 'packet_ids':['A060']}
js('PROGRESS.json',progress);js('PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

A060 stage10 quantifies the terminal limitation of A059's new depth-free stopping theorem. The target is C019: useful entropy-decaying continuation from the SAME original owner. On the actual Boolean bent-point tensor control, the complete debit and both full terminal entropies are exact for every finite number of factors and every independent dyadic stopping schedule. Units are bits. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Execution protocol v2 in full; BOARD snapshot 2026-10-27 01:15 UTC; B12 STREAM_NOTES v2; own STATUS, LEARNED, WORKLOG and prior stage9 REPORT. A059's 20261026T223551Z PROOF Sections1-4 and claim version1 are pinned in out/SOURCES.json and copied locally. The source statement hash is 555770aacd78f4d05d5b613a5c02e406a267155705995d1bf2aac71b7c63303b. Campaign registries, plan and supplement were consulted at relevant navigation lines; all four local paper text versions were inspected at abstracts/composition or pivotal locators, without importing a new literature claim. Their PDF-extracted text requires cp1252 decoding; an initial UTF-8 read failed explicitly and was retried with that encoding. No new remote literature or public release was used.

# complete derivation or exact first unsupported line

PROOF Section1 reconstructs A059's new two-ticket and geometric transactions conditional on its established original source: 9/2=2(29/13)+1/26, and pending rate A=(29/13)/(1-q) releases at least q A t Inf_i after the actual fee. REVIEW.json records the scope and the conflict that A060 supplied the earlier singleton dependency; no independent full-chain acceptance is claimed.

Sections2-3 calculate the complete actual-wrapper law. With r AND2 factors and untouched tag, H(root)=E0+r/8. If S_r is expected number of selected factor queries, then E H(leaf)=E0+(r-S_r)/8; actual removed influence is S_r/32 and entropy debit is S_r/8. At q=1/2 the paid debit is (1-2^-r)/4, but terminal/root entropy tends to one. A positive old prefix debit can remain booked. Tensorization removes E0/r, not the extensive terminal term. Terminal exhaustion for horizon-dependent constant q_r occurs iff r(1-q_r)->0. A fixed infinite nonincreasing survival schedule exhausts entropy only if every continuation is one.

Section4 compares the SAME original owner. The geometric potential's preserved reserve forces q<=1/2 (q<=59/117 even without that reserve). Exhaustion instead needs 1-q_r=o(1/r), so this sufficient pending rate cannot fit. This is a limitation of that certificate: deterministic no-killing work on this same family costs r/8 and IS affordable from its original core owner. No universal no-killing impossibility or FEI counterexample follows. The first unsupported line is useful arbitrary-core terminal decay paid by genuinely unused original capacity.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes computation. Commands: python -X utf8 code/check.py pilot and python -X utf8 code/check.py all, using this run's paths from A060. Corrected pilot: 661 checks PASS. Main: 11485 checks PASS, 0.206 seconds measured computation. Every Boolean function on three bits and every coordinate is checked for conditional source transaction release at q=0,1/4,1/2. Actual one- and two-factor wrapper spectra are reproduced by direct character sums independent of the fast Walsh transform. Small complete stopping trees retain every core answer and both coin outcomes. Thirty rational survival profiles and heterogeneous schedules check the exact law and boundary inequalities. Rational logarithm intervals use the positive artanh series with 70 terms and an explicit tail, while powers of two are exact. Decimal timings are observations; theorem signs use rational arithmetic. The first pilot's zero-entropy interval bug and its correction are preserved in out/PILOT_ERRATUM.md. No finite test is used as the asymptotic proof.

Memory estimate is 60 MB; no large search, GPU, dimension escalation or detached job was launched. Fresh memok returned exit0 with 7.3 GB physical and 16.5 GB commit availability before the Lean supporting-algebra check. Its exact result and scope are recorded separately in out/FORMAL_STATUS.json; the full theorem is not Lean-certified.

# proof dependencies and changed downstream conclusions

The new terminal theorem follows from explicit product spectra, the exact balanced wrapper profile, and finite survival identities, with a written all-horizon proof. A059's new transactions hold at their stated expected-resource scope, conditional on the original source and singleton dependency. A060's smaller original owner has not been enlarged. The downstream correction is quantitative: unbounded possible depth and an affordable stopped bill do not give vanishing terminal entropy, and fixed additive overhead disappears under tensors while this terminal term survives. A059 already states the qualitative limitation; this stage supplies the exact law and sharp horizon condition.

# one next mathematical action and independent reviewer

A059/A057 should construct one necessary entropy-sensitive arbitrary-core continuation whose fees are charged to actual removed influence or another decreasing ORIGINAL resource. Check full expected terminal decay, both child functions, old bookings and current unused capacity. This is a mechanism change from geometrically killing an arbitrary policy. Reviewer A091, alternate A087/A094; A060's contribution to the singleton dependency remains disclosed.

# actual persistence receipts or precise save blocker

All four protocol artifacts, PROOF.md, REVIEW.json, frozen spec, code, exact outputs and source snapshots are local to A060. out/SCHEMA_VALIDATION.json checks exact protocol fields, statement hashes, compatibility equality, report headings, rolling-status format and size limits. out/PERSISTENCE_RECEIPT.json hashes and reads back saved files. STATUS is two lines; WORKLOG and LEARNED have dated entries. Supervisor adoption, mirrors and independent acceptance remain unverified. No campaign tree, other agent folder, git state or brain research data was changed. The required wake and checklist hooks were run; wake reported stale personal-context notes, and no affected note supports a mathematical step.

# Universal bridge

This moves C019 by independently reconstructing the new original-owner transactions at scope and closing their precise terminal-decay boundary: exact full-terminal laws prove that fixed-q paid depth-free stopping retains asymptotically all entropy, while useful exhaustion requires r(1-q_r)->0 and falls outside this fixed-rate geometric potential. The remaining universal step is an entropy-sensitive continuation charged to a decreasing unused original resource, with complete terminals and prior debits retained. That is the shortest route to full FEI here because the calculation separates an inadequate certificate from an actually affordable deterministic control and rules out mistaking additive-slack tensorization or unbounded possible depth for payment of arbitrary terminal entropy.
'''
write('REPORT.md',report)
status='STATE: Stage10 saved: A059 new transactions scoped HOLDS; exact full-terminal survival law; exhaustion iff r(1-q_r)->0; fixed-rate geometric bank cannot exhaust;11485 checks PASS;FEI OPEN.\nNEXT: A059/A057 build entropy-sensitive necessary arbitrary-core continuation paid by actual decreasing ORIGINAL resource; retain full terminals/old fees; A091/A087 review exact horizon obstruction.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+NOW+' Stage10: scoped A059 two-ticket/geometric transactions reconstructed; exact actual-wrapper complete-terminal law and sharp iff r(1-q_r)->0. Fixed original geometric price cannot exhaust; same-family deterministic work affordable. 11485 exact assertions PASS. First pilot interval-zero bug fixed with exact power-of-two logs, pilot661 PASS. Universal terminal-decay continuation remains unpaid; external review/adoption unverified.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage10 durable: A059 geometric theorem already covers two tickets/unbounded possible depth; do not repeat. On its actual four-bit bent-point AND2 tensor G_r=z*prod h, E0=8-(45/64)log2(3)-(75/64)log2(5), root H=E0+r/8,I=7/4+(r+1)/16. With survival sum S, complete expected terminal H=E0+(r-S)/8, removed I=S/32; actual fee=4 removed I. Fixed q<1 retains terminal/root ratio->1; entropy exhaustion iff r(1-q_r)->0. For a fixed infinite schedule any single lost continuation leaves positive residual fraction. SAME geometric rate9/2 with reserve1/26 forces q<=1/2 (without reserve59/117), hence cannot exhaust. This is NOT a no-killing affordability lower bound: deterministic same-family debit r/8 fits original core owner. Positive old prefix remains bookable. Fixed additive tensor slack vanishes; extensive stopped-terminal entropy does not. Next mechanism must pay useful terminal decay from a decreasing original resource.\n')
print(json.dumps({'saved':str(ROOT),'checks':v['checks'],'claim_sha256':claims[0]['statement_sha256']}))
