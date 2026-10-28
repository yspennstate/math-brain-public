import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OWN=ROOT.parent.parent
BASE=OWN.parent.parent
OUT=ROOT/'out'
def write(p,x):
    p.write_text(x if isinstance(x,str) else json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))
main=read(OUT/'CHECK_main.json')
audit=read(OUT/'AUDIT.json')
assert main['status']==audit['status']=='PASS'
assert main['family_profiles']==20 and main['roots']==278
total=main['exact_assertions']+audit['exact_assertions']
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
source_receipts=read(OUT/'SOURCE_RECEIPTS.json')

lean={
 'command':'python -X utf8 lean_check.py --core --timeout 45 --stmt "example (terminal loss fee initial query bound : Nat) (ledger : terminal + loss + fee = initial + query) (budget : initial + query ≤ bound) : terminal + loss + fee ≤ bound := by rw [ledger]; exact budget"',
 'exit_code':1,'output':'SETUP_UNVERIFIED: Compute status is distressed or unknown',
 'compiler_started':False,'proof_rung':'UNVERIFIED; no formal certification',
 'scope':'Only integer ledger-to-budget substitution; would not certify Fourier/entropy claims even if checked.'}
write(OUT/'LEAN_RECEIPT.json',lean)
write(OUT/'CHECKLIST_CLOSURE.json',{'task_id':'T-20261027-057','action':'done','exit_code':1,'output':"checklist: error: RuntimeError('checklist lock held too long')",'disposition':'Local research artifacts complete; shared administrative closure unconfirmed. No lock bypass or brain mutation attempted.'})
state=read(Path(r'~\.claude\compute\compute_state.json'))
write(OUT/'COMPUTE_RECEIPT.json',{k:state.get(k) for k in ['ts','status','reasons','disk_free_gb','mem_avail_mb','commit_avail_mb','cpu_pct','top_private_groups']})

deps=[]
for who in ['A012','A096']:
    latest=sorted((BASE/'agents'/who/'runs').iterdir())[-1]
    obj=read(latest/'CLAIMS.json')
    def walk(x):
        if isinstance(x,dict):
            if 'claim_id' in x:
                if x['claim_id'] in ['A012-UNIVERSAL-PROJECTION-PROFILE-HISTORY','A096-FREE-VACUUM-INFLUENCE-CALIBRATION']:
                    deps.append({'agent':who,'claim_id':x['claim_id'],'version':x.get('version'),'statement_sha256':x.get('statement_sha256'),'source':str(latest/'CLAIMS.json')})
            else:
                for z in x.values(): walk(z)
        elif isinstance(x,list):
            for z in x: walk(z)
    walk(obj)
write(OUT/'DEPENDENCY_CLAIM_RECEIPTS.json',deps)
write(OUT/'REVIEW_DISPOSITIONS.json',[
 {'source':'A096 stage22 DERIVATION section2','verdict':'HOLDS at finite affine information-projection identity; independently reconstructed by support/first-variation proof','scope_exclusion':'Separate exponential atom-count theorem not reviewed here; no independent acceptance of our new transfer.'},
 {'source':'A097 stage21 PROOF','verdict':'Statement survives; derivative must include factor t; inherited CE sentence must specify convention and include erasure term','repair':'PROOF section4; no immutable source overwritten'},
 {'source':'A012 stage22 DERIVATION equations2-6','verdict':'Identity and scalar-bound chain reconstructed for precise projection interface; new affine-fee substitution in PROOF section2','scope_exclusion':'No free conversion to true-kernel inheritance; no new initial-source supplier.'}])

statements=[
 ('A097-AFFINE-PROJECTION-HISTORY-TRANSFER',
  'For every Boolean f on a finite uniform cube and every normalized covering squared-Fourier reference Q, every finite adaptive physical-query history whose two children inherit pi_i Q, augmented by any finite affine information projections containing the current true law and charged at their full fee D(u||q), has complete signed entropy-increment + full query-KL contraction + conversion-fee + full-terminal-CE bill at most CE(P_f,Q)+(2/ln 2)I(f). Any fixed old booking U stays added. The SAME original capacity B pays whenever U+CE(P_f,Q)+(2/ln 2)I(f)<=B. Scalar subprobability masses may be preserved without dropping their penalties.',
  ['Finite uniform Boolean cube; all units bits','Finite adaptive tree and finite update sequences; actual physical reach probabilities; both outcomes retained','Normalized Q covers P_f; or fixed inherited positive subprobability scalar times such Q','Every update minimizes D(v||q) over a nonempty closed affine moment slice containing current P; support restricted to supp(q)','Projection inheritance specifically; signed entropy increments, without clipping positive parts or extra mandatory floor costs'],
  ['A096 stage22 section2 finite information-projection identity, rederived in PROOF section1','A012 stage22 DERIVATION equations2-6, including J_i<=(2/ln 2)Inf_i and physical influence telescope'], []),
 ('A097-HIGH-MOMENT-MATCHED-QUERY-LOSS',
  'For every even n>=4 there is an explicit actual Boolean f_n, a product of n/2 disjoint two-bit signs, and a strictly positive rational reference Q_n with H(f_n)=n, I(f_n)=n/2, CE(P_n,Q_n)<4I(f_n), Q_n(empty)=P_n(empty), and all spectral marginals on at most n-2 coordinates identical to P_n, such that for every i<=n-1 projection loss L_i=D(P_n||Q_n)-D(pi_i P_n||pi_i Q_n) satisfies n-1/4<L_i<n and 2n-1/2<L_i/Inf_i(f_n)<2n. Q_n is already feasible for any calibration using only those moments, so its information-projection release is zero. No universal local L_i<=K Inf_i follows from these hypotheses; H/I=2 and FEI is not refuted.',
  ['Every even integer n>=4','Two-bit sign is negative only at (+,+); disjoint physical pairs','Q_n is the explicit parity perturbation on spectral face {n} union V, V subset [n-1], with epsilon=2^(-4n)','Loss uses the explicit spectral projection; both normalized references and true laws are retained'],
  ['Direct Boolean Walsh tensor computation','Finite parity cancellation on every projection fiber and inclusion moment'],
  ['Any hypothetical dimension-independent query-local payment deduced only from covering rate4, vacuum calibration and marginals through order n-2'])
]
claims=[]
for cid,stmt,hyp,pdeps,refutes in statements:
    c={'claim_id':cid,'version':1,'exact_statement':stmt,'hypotheses':hyp,
       'statement_sha256':hashlib.sha256(stmt.encode('utf-8')).hexdigest(),
       'contributors':['A097; A096 supplied calibration dependency; A012 supplied projection-history dependency'] if 'TRANSFER' in cid else ['A097'],
       'proof_source':str(ROOT/'PROOF.md'),'proof_dependencies':pdeps,
       'review_records':[{'reviewer':'A097','kind':'separate exact representation audit, not independent-agent acceptance','source':str(OUT/'AUDIT.json')}],
       'status':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[], 'refutes':refutes,
       'first_unproved_line':'Noncircular useful ORIGINAL arbitrary-core full reference CE<=C0 I, or paid required interface conversion from SAME unused original account; full FEI remains OPEN.',
       'next_consumers':['A012','A096','A094','A050','A011','A099','A100']}
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    claims.append(c)
write(ROOT/'CLAIMS.json',claims)

progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B20','packet_id':'A097',
 'gap_id':'C024-AFFINE-CALIBRATION-IN-FULL-PROJECTION-LEDGER','attempt_id':'A097-stage22-affine-transfer-and-moment-obstruction',
 'method':'Source-bound finite information-projection identity substituted into exact physical-query potential; explicit Boolean parity-face reference control',
 'mathematical_delta':'A096 affine calibration enters A012 all-history projection ledger at unchanged additive 2/ln2 influence; even marginals through n-2 plus vacuum and ORIGINAL rate4 do not yield local query-KL payment. Stage21 derivative and erasure-text errata recorded.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOFS_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':deps,
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version']} for c in claims],
 'source_artifacts':['PROOF.md','FROZEN_SPEC.json','FROZEN_AUDIT.json','out/SOURCE_RECEIPTS.json','out/DEPENDENCY_CLAIM_RECEIPTS.json','out/CHECK_main.json','out/AUDIT.json','out/LEAN_RECEIPT.json'],
 'next_consumers':['A012','A096','A094','A050','A011','A099','A100'],
 'next_action':'A012/A096/A094 independently check affine full-fee substitution and high-moment Boolean witness; A050/A011 supply required ORIGINAL arbitrary-core O(I) source or pay structured conversion with full query KL, old U and both terminals.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal initial source/necessary productive policy unpaid','Lean setup refused compute state; compiler not started','Independent-agent acceptance and supervisor mirror not observed','T-20261027-057 checklist closure failed: shared checklist lock held too long'],
 'packet_ids':['A097']}
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
write(ROOT/'PROGRESS.json',progress)
write(ROOT/'PACKET_DELTA.json',progress)

report=f'''# A097 stage22: moment calibration transfers; query loss stays payable

## exact target, quantifiers, hypotheses and units

For every finite uniform-cube Boolean f and supplied covering complete Fourier reference, transfer A096's affine moment-calibration identity into A012's FULL projection-history ledger, retaining actual query contractions, full fees, BOTH terminals and old U. Bits throughout. The resulting original rate is C0+2/ln2 conditional on CE<=C0 I. An actual Boolean rate4 reference matching all marginals through order n-2 shows why those constraints cannot instead pay each query locally. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol revision {protocol['revision']} read in full; current BOARD27Oct09:23UTC and B20 STREAM_NOTESv2; own stage21 proof/report and rolling handoff. Exact dependency locators: A09620261027T055827Z DERIVATION section2; A01220261027T062634Z DERIVATION sections2--4, equations2--6; A09420261026T232939Z accounting objection and A01120261027T025625Z v6 scope. A004/A085 reports supply stage21 proof-text review notices, independently checked here. Forty source receipts pin bytes/hashes and decoding in out/SOURCE_RECEIPTS; canonical navigation/registries/plan, supplement sources and four local paper versions were intake-read with selected passages located. This is no new full-paper audit. The paper's shared-data mixture identity is rederived directly. One two-wording math recall returned contextual/irrelevant leads; no recalled card is adopted as a premise. Wake's stale personal-context alert was surfaced; current sources govern.

## complete derivation or exact first unsupported line

PROOF1 independently reconstructs the finite affine information-projection identity, including covering support, feasible boundary points and unchanged scalar mass. PROOF2 substitutes the EXACT full fee into A012's update bracket, giving all finite physical-query/affine-calibration histories at unchanged additive2/ln2, from the SAME original owner. This is the explicit cross-route transfer. PROOF3 gives the actual product-of-AND2-signs family: H=n, I=n/2, rate4 complete reference, vacuum and all marginals through n-2 matched, yet n-1/4<L_i<n for every i<=n-1. Its calibration release is zero. PROOF4 records the missing factor t in the old derivative and the missing erasure term in a generic inherited-CE sentence; terminal signed-floor statements and owner subtraction remain unchanged.

FIRST UNPAID UNIVERSAL LINE: construct a noncircular useful original full reference CE<=C0 I on arbitrary Boolean cores, or pay a required productive interface conversion from SAME remaining original capacity, including full query KL. No such supplier or universal FEI constant is established.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede searches. From A097 run python -X utf8 runs/{ROOT.name}/code/check.py pilot, then main. Pilot PASS{read(OUT/'CHECK_pilot.json')['exact_assertions']} assertions on22 roots and2 family profiles; not added to final total. Main PASS{main['exact_assertions']} assertions on ALL278 labelled n0..3 Boolean truth tables,1608 coordinate/reference cases,20 family profiles at n4,6,8,10 and283 rational calibration fixtures; runtime{main['seconds']:.3f}s. No symmetry reduction or automatic escalation. Every family has a direct actual truth table and exact Walsh spectrum. Main checks all relevant inclusion moments via an integer zeta transform and every declared projection cancellation, and tests the complete CE/query identity and rigorous JS bound.

Separate code/audit.py uses direct characters and exact rational likelihood products without author-helper imports: PASS{audit['exact_assertions']} assertions on n4,6 and three NONPARTITION size-tilt fixtures, runtime{audit['seconds']:.3f}s. Completed main plus audit total{total}; overlapping pilot excluded. This is independent representation/code, not independent-agent review. Arithmetic is integer/Fraction, exact formal prime-log cancellation and24-term atanh intervals with geometric tail; strict family signs need only rational1<2-epsilon<2. Every computation stayed below55s and estimated100MB. Frozen case count was corrected from24 to20 BEFORE execution; domains did not change.

Checks that could fail: Boolean realizability, moment order, unchanged vacuum, full normalization/cover, actual projection convention, fee direction, scalar mass retention, n2 boundary and zero influence. These were checked analytically and in the declared finite domains. Generic affine support at zero is handled by the t log t first-variation argument. Continuum/all-dimensional conclusions rely on the finite analytic proof, not samples. The requested core Lean ledger substitution returned SETUP_UNVERIFIED because compute was distressed or unknown; compiler not started, no axioms or formal result verified. Rung: analytic proof with exact checks, independent review pending.

## proof dependencies and changed downstream conclusions

A096's finite projection identity holds at its stated scope; its separate atom-count theorem is not reviewed here. A012's actual spectral projection convention and its scalar two-point bound are essential dependencies. The new update class includes arbitrary affine moment constraints, rather than partition profiles alone; exact full fee cancels its current divergence decrease. The high-order moment control refutes only a local-query shortcut, even with an explicit original rate4 source. It gives no FEI counterfamily (H/I=2), no initial source for arbitrary cores, and no free projection-to-true-kernel conversion. out/REVIEW_DISPOSITIONS and dependency claim receipts keep these scopes separate. Stage21 immutable artifacts remain untouched; its proof-text errata are recorded here.

## one next mathematical action and independent reviewer

A012/A096/A094 independently reconstruct PROOF1--3, especially fee direction, all n-2 marginals and original-owner substitution. Then A050/A011 must price ONE useful ORIGINAL arbitrary-core source or a necessary structured conversion while retaining query KL, old U and BOTH full terminals. Another moment-matching constraint cannot itself supply that price. No peer message is sent; supervisor can route this source-bound handoff.

## actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specs, helpers, source/validation/formal receipts are saved only in A097; rolling STATUS has exactly two lines, WORKLOG and LEARNED are updated. code/finalize.py checks exact protocol key sets, statement hashes, identical progress/delta, file sizes and byte hashes in out/PERSISTENCE_RECEIPT.json. Supervisor mirror and independent acceptance remain unverified. T-20261027-057 closure returned exit1: shared checklist lock held too long; out/CHECKLIST_CLOSURE.json preserves the blocker. No lock bypass was attempted. Required operational wake/checklist tools own their external receipts; research work changes no shared/source tree, brain store, trading path or other agent file. No git, mail, GPU, remote job, deletion or detached process. The fresh compute snapshot is saved; near-full disk motivated tiny artifacts and no Mathlib build. No running work was stopped or throttled; all own finite checkers ended.

## Universal bridge

This moves C024 history transfer inside C019 by substituting A096's COMPLETE affine-calibration fee into A012's universal projection ledger with ZERO additional constant: the original supplied rate remains C0+2/ln2, including full query losses, old U and both terminals. The exact Boolean witness shows that vacuum plus marginals through n-2 still cannot erase the query bill: one loss is between n-1/4 and n at local influence1/2, despite original CE<4I. C020's arbitrary-core original source is unpaid and the universal FEI improvement is zero. NEXT targets that source or a required structured interface conversion, because moment matching alone now has an explicit all-dimensional failure of the tempting local substitution.
'''
write(ROOT/'REPORT.md',report)
stamp=datetime.now(timezone.utc).isoformat()
write(OWN/'STATUS.md',f'STATE: A097 stage22 COMPLETE_LOCAL: affine calibration enters FULL projection ledger at unchanged2/ln2; high-order moment matched rate4 Boolean reference has query loss>n-1/4; {total} exact checks PASS; FEI OPEN.\nNEXT: A012/A096/A094 review full-fee substitution and n-2-marginal witness; A050/A011 price ORIGINAL arbitrary-core O(I) source with full query KL/old U/BOTH terminals; mirror pending; T-20261027-057 closure lock-blocked.\n')
lesson='''Stage22 durable fact: for finite normalized covering q, an affine information projection u onto a closed moment slice containing p covers p and satisfies D(p||q)-D(p||u)=D(u||q), including boundary faces. Charge the FULL D(u||q) fee and its update bracket in A012 projection-history identity is exactly zero. Thus arbitrary finite affine-moment updates enter the SAME-original universal projection ledger at unchanged rate C0+2/ln2, old U and both complete terminals retained. This is the explicit spectral projection convention, not true-kernel replacement.

Actual Boolean boundary: even n>=4, product of n/2 AND2 signs has uniform spectrum, H=n,I=n/2. On spectral face {n} union V, V subset[n-1], use Q/P=1+(1-2^(-4n))(-1)^|V|, and1 outside. Q is positive, vacuum matched, EVERY marginal through n-2 matched, CE<4I, yet every i<n has pi_iQ=pi_iP and L_i=n-(1/4)log2(2-2^(-4n)) in(n-1/4,n). All already matched-moment calibration releases are zero; L_i/Inf_i>2n-1/2 diverges. This refutes only local query payment from matching moments; H/I=2 and initial arbitrary-core source remains unpaid.

Stage21 text corrections: floor derivative is t(z-a)/(z(t-z)ln2), factor t was missing; minimizer unchanged. Under spectral projection avg childCE-parentCE=-B_i(P)-L_i, not merely minus KL. The fixed-terminal signed-floor owner subtraction survives. No old immutable artifacts changed. Lean setup refused compute status before compiler; no formal certificate.
'''
for name,entry in [('LEARNED.md',lesson),('WORKLOG.md',f'{stamp} A097 stage22: transferred affine full-fee calibration into A012 ledger; explicit high-order Boolean moment control; {total} exact main/audit assertions PASS. Reviewed A096 section2, documented old derivative/erasure errata. Core Lean admission refused, no compiler. Source remains unpaid; FEI OPEN.\n')]:
    p=OWN/name
    old=p.read_text(encoding='utf-8') if p.exists() else ''
    marker='Stage22 durable fact:' if name=='LEARNED.md' else 'A097 stage22: transferred affine'
    if marker not in old:
        write(p,old.rstrip()+'\n\n'+entry)

assert read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json')
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest() for c in read(ROOT/'CLAIMS.json'))
assert all(field in report for field in protocol['required_per_run']['report_fields'])
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        raw=p.read_bytes()
        assert len(raw)<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write(OUT/'PERSISTENCE_RECEIPT.json',{'schema':'PASS','statement_hashes':'PASS','progress_delta_identical':True,'status_two_lines':True,'main_and_audit_checks':total,'independent_review':'PENDING','mirror':'UNVERIFIED','files':receipts})
print(json.dumps({'status':'COMPLETE_LOCAL','exact_checks':total,'files_hashed':len(receipts),'total_bytes':sum(x['bytes'] for x in receipts),'full_FEI':'OPEN','lean':lean['output']}))
