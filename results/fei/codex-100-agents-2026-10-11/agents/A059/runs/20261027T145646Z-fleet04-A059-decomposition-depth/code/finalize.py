from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];B=R.parents[1]
def write(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=json.loads((R/'out/validation.json').read_text(encoding='utf-8'));a=json.loads((R/'out/audit.json').read_text(encoding='utf-8'));c=json.loads((R/'out/coins.json').read_text(encoding='utf-8'))
assert all(z['status']=='PASS' for z in [v,a,c]);total=sum(z['assertions'] for z in [v,a,c])
cid='A059-TENSOR-RESERVOIR-FULL-TERMINAL-PRICE'
statement=('For any actual Boolean g, physical seed query i, and independent nonconstant Boolean reservoir h with j=I(h)>0,s=H(h)>0, put G_N=g times N disjoint h copies. At fixed rate A>0 and eligible received cash R_N=A I(G_N)-u, with fixed old depletion u>=0 independent of N, define e=(u+D_iH(g)-A Inf_i(g))_+. For e>0 and all sufficiently large N the minimal newly frozen FULL entropy of an outcome-dependent feasible A058 transaction is Fopt(N)=e min_a (H(g_a)+Ns)/(A(I(g_a)+Nj)), with |Fopt-e s/(Aj)|<=e M/(ANj), M=max_a|H(g_a)-(s/j)I(g_a)|. Its advantage over common continuation is at most2eM/(ANj). Any feasible post-query decision using at most b fresh irrelevant fair bits per outcome freezes at least Ns/2^(b+1). Dyadic rounding with b_N=ceil(2log2(N+1))+b0 attains the positive ideal limit and can be implemented with fewer than2 expected dummy queries per nontrivial action. On arbitrary adaptive restriction trees of AND2 products, full expected terminal entropy is2(N-E distinct factors touched); coherent-mask transport gives E H(Fleaf)>=2(cN-sum_first-touch w_v t_v). This is a necessary terminal price, not a universal initial supplier or FEI proof.')
claim=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=['uniform finite Boolean physical cubes; entropy bits','all reservoir factors use disjoint physical variables','A>0, I(h)>0, H(h)>0; fixed u independent of N; e>0 for positive-floor assertions','received cash is ACTUALLY eligible after old debits/protected reserves; no source reset','R_N>=D and e<=min_a AJ_a(N)/2 for exact one-outcome optimum; both hold for sufficiently large N when e>0','coin lower bound concerns worst-case at most b fresh irrelevant fair bits after each outcome, not expected coin work','coherent transport requires physical KC=0, C indicator and sign K off C; all actual siblings, biases and terminal functions retained'],statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A059; A058 local liquidation action independently reconstructed; A060 earlier independent-schedule terminal-law context'],proof_source={'path':'PROOF.md','sha256':sha(R/'PROOF.md'),'certificates':['out/validation.json','out/audit.json','out/coins.json']},proof_dependencies=['A058 stage11 PROOF Sections1-3 actual-cash LP, independently reconstructed at local scope','finite disjoint Fourier product identities','A059@2 exact coherent marginal, directly reproduced for all3^7 physical states','elementary rational LP dual and fair-bit cylinder identities'],review_records=[{'reviewer':'A059','verdict':'AUTHOR_PROOF_EXACT_CONTROLS_PASS','independent_acceptance':False}],status='PROVED_AUTHOR_CHECKED_INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=['Zero frozen-entropy bill for mandatory liquidation even under large tensor padding: actual rate6 seed has limiting floor>=1/768','Fixed worst-case coin width can attain bounded frozen entropy on the padded mandatory-liquidation family'],first_unproved_line='Pay accumulated FULL frozen bills and make live entropy vanish for arbitrary Boolean cores from a sufficiently large SAME original unused influence owner.',next_consumers=['A058','A060','A057','A091','A087','B12','B20'])
dump(R/'CLAIMS.json',[claim])
review='''# Source-bound review

A058 stage11 PROOF Sections1-3: HOLDS at the local received-cash/expected-resource scope. After paying D, discard capacity e=max(0,A average child I-(R-D)). Every unit discarded in outcome a costs H_a/(A I_a) full frozen entropy. Sorting those ratios, respecting capacities and omitting zero-I constant children gives the stated primal optimum and nonnegative dual decomposition. Bias does not change answer probability1/2. Dyadic survival floors preserve feasibility and retain both stopped/live sectors. No initial source or globally optimal policy is inferred. A059 contributes no repair to this input.

The new reservoir theorem follows by exact disjoint tensor identities, not by changing A058's action. Its lower price survives optimal outcome selection; fixed-width physical coins need a separate precision bill. The lazy comparator shows that increasing maximum coin depth does not imply growing EXPECTED dummy work. These new conclusions are A059 author results pending A058/A091 independent review.

A060's prior independent-survival obstruction and A091's fixed9/2 source obstruction are consumed as scope warnings, not newly accepted full-chain claims. No review of A057's41/20 continuum certificate is claimed in this run.
'''
write(R/'REVIEW.md',review)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B12',packet_id='A059',gap_id='G-A059-DECOMPOSITION-DEPTH',attempt_id='stage22-tensor-reservoir-frozen-entropy-price',method='Independent local LP reconstruction; tensor-reservoir asymptotic/finite entropy lower bound; physical coin-resolution obstruction and lazy comparator; all-adaptive masked distinct-touch accounting',mathematical_delta='Outcome-optimal liquidation retains a strictly positive FULL frozen-entropy price e H(h)/(A I(h)); fixed coin width forces linear reservoir entropy loss. Growing width implements the sharp limit with<2 expected dummy queries per decision. ALL-adaptive masked distinct-touch lower bound extends prior independent-schedule terminal warning. Actual rate6 seed floor>=1/768; no fixed9/2 full-source retry.',deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='AUTHOR_PROOF_EXACT_CERTIFICATES_PASS; INDEPENDENT_REVIEW_PENDING; FEI_OPEN',claim_versions_used=['A058 stage11 received-cash local LP: A059 scoped HOLDS','A059-PREPAID-TWO-TICKETS-AND-GEOMETRIC-STOPPING@1: prior accepted partial scope','A060 stage10 full-terminal law and A091 stage22 source obstruction: scope warnings, no new full-chain acceptance'],claims_created_or_changed=[cid+'@1','A058 stage11 local action: independent A059 scoped HOLDS review'],source_artifacts=['PROOF.md','REVIEW.md','SPEC.json','AUDIT_SPEC.json','COIN_SPEC.json','code/check.py','code/audit.py','code/coins.py','code/Reservoir.lean','out/validation.json','out/audit.json','out/coins.json'],next_consumers=['A058','A060','A057','A091','A087','B12','B20'],next_action='A058/A091 reconstruct exact reservoir price and adaptive masked occupation; build a Bellman inequality charging ACCUMULATED full frozen entropy plus live decay to sufficiently large SAME original unused influence. Use lazy physical coins, not ideal probabilities or dropped terminal bills.',stagnant_substantive_attempts=0,blockers=['New reservoir/physical-implementation theorem independent review pending','Universal original source and accumulated frozen-plus-live entropy payment remain OPEN','Supervisor mirror/adoption not observed'],packet_ids=['A059'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
formal='Supporting scalar formal attempt receipt pending; no Lean certification claimed.'
if (R/'out/formal_status.json').exists():
 f=json.loads((R/'out/formal_status.json').read_text(encoding='utf-8'));text=(R/'out/lean.txt').read_text(encoding='utf-8');formal='Supporting scalar Lean attempt returned'+str(f['returncode'])+'; see out/lean.txt. '
 formal+=('VERIFIED_TARGET for the scalar nonnegative-price inequality ONLY; not the entropy theorem.' if f['returncode']==0 and 'VERIFIED_TARGET' in text else 'No verified target/axiom receipt: not Lean-certified. A held or failed formal attempt is not a mathematical refutation.')
report=f'''# A059 stage22: the full entropy price of tensor-reservoir liquidation

## exact target, quantifiers, hypotheses and units

For EVERY finite Boolean seed g, queried physical coordinate and independent Boolean reservoir h with positive influence and spectral entropy, price A058's optimal outcome-sensitive action from ACTUAL received cash A I(G_N)-u. Preserve old depletion, protected reserves and BOTH full terminal laws. Entropy bits; A>0; fixed u independent of N; N arbitrary. Supply a rate6 actual seed, growing-depth reservoir family and a physical implementation whose expected dummy overhead stays bounded. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Current BOARD B12/B19/B20 and own STATUS; B12 STREAM_NOTESv2 remains2026-10-11. Read A058 run20261027T114055Z REPORT/PROOF Sections1-5; A060 run20261027T011815Z REPORT/PROOF Sections1-5; A091 run20261027T054729Z REPORT and PROOF Section4; A057 run20261027T080128Z REPORT contextual41/20 result. Exact protocol fields refreshed. Prior mandatory campaign/paper baseline is reused; no new literature or priority assertion. Sources pinned in out/SOURCES.json. No brain card is a mathematical premise. Current explicit stage request governs continuation; no schedule/date reset.

## complete derivation or exact first unsupported line

PROOF Section1 independently reconstructs A058's actual-cash LP at local scope: a forced discarded capacity e costs the capacity-weighted child entropy/influence ratio. REVIEW.md records scoped HOLDS, not global-policy optimality or an initial source.

Sections2-4 give the new all-N reservoir theorem. G_N=g times N DISJOINT h copies has child H=H_a+N H(h), I=I_a+N I(h), while d,p and e=(u+d-Ap)+ are fixed. For large enough N one cheaper outcome has sufficient capacity, so Fopt=e min_a(H_a+Ns)/(A(I_a+Nj)). Its distance from e s/(Aj) is<=eM/(ANj), and all outcome-adaptive advantage over common continuation is<=2eM/(ANj). Thus the optimal frozen FULL entropy price stays strictly positive. At A6 the actual9-bit bent-point rare-tag seed has d>=7/256,p1/256 and e>=1/256; h=AND2 gives limiting frozen price>=1/768. This avoids the already refuted universal rate9/2 completion target. A supplied received state is not represented as an invented physical old prefix.

Physical implementation is part of the theorem. At most b post-answer fair bits imply F>=N H(h)/2^(b+1); fixed maximum coin width loses linear entropy even when the ideal optimum is bounded. Width b_N=ceil(2log2(N+1))+b0 gives rounding errorO(1/N). A LAZY threshold comparator realizes every dyadic action with exact probabilities and expected work2(1-2^-b)<2; endpoints require0. Thus maximum depth may grow without accumulated expected dummy overhead. This is a standard comparison construction used here with the newly priced full-terminal action; no novelty of sampling a dyadic coin is claimed.

Section5 removes the independent-survival assumption of A060's tensor control. For ANY adaptive physical stopping tree of AND2 products, full terminal entropy is exactly2(N-number of distinct touched factors). Under any coherent mask, E H(Fleaf)>=2(cN-sum_first-touch w_v t_v), with current density and all coherent mean sectors retained. This gives a necessary occupation/terminal target for arbitrary outcome-dependent continuation.

First unsupported line: pay the ACCUMULATED full frozen bills while exhausting live entropy for arbitrary cores from a sufficiently large SAME original influence source. No implication from a cheap local action or unbounded possible depth to complete FEI is asserted.

## executed validation with domain, arithmetic, commands and outputs

All three specs precede their jobs; helper pinned before pilot. Commands: python -B -X utf8 code/check.py --pilot; code/check.py; code/audit.py; code/coins.py. Pilot576 PASS. Main **{v['assertions']} exact assertions PASS**, {v['seconds']:.3f}s:804 physical coordinates on all n<=3 signs,1596 eligible received states,46 liquidation states,1104 feasible quarter-grid competitors;64 compressed reservoirs and832 physical precision guards; three complete/early-stop adaptive product controls. Both full frozen/live laws and all exact first-touch terminal spectra are retained.

Independent path audit **{a['assertions']} assertions PASS**, {a['seconds']:.3f}s: ALL2187 coherent physical restriction states and5103 remaining edges, including1215 dead masks,1458 collapsed tags and882 biased-core states. Direct character sums reproduce the root and actual9-bit seed independently of butterfly Walsh. Exact spectral marginals and every density/first-touch drift are checked.

Coin audit **{c['assertions']} assertions PASS**, {c['seconds']:.3f}s: all{c['threshold_cases']} dyadic thresholds b0..12, with independent enumeration of{c['independently_enumerated_words']} uniform words for b<=6. Total main/audit/coin **{total} exact assertions PASS**; pilot counted separately. All-dimensional conclusions use the displayed finite products, dual argument and analytic bounds, never finite extrapolation.

Integer/Fraction spectra and prime-log identities; rigorous32-term atanh intervals with explicit geometric tails. The main finite rounding comparison includes an explicit rational1e-15 enclosure allowance; the mathematical exact rounding bound is proved analytically in (9), and the script separately verifies exact probability/capacity guards. No floating sign decisions. Estimated140MB research/40MB coin audit, no measured peak. No >300MB search, GPU, automatic dimension escalation, detached task, process shedding or new worker. {formal}

## proof dependencies and changed downstream conclusions

A058 local optimum independently HOLDS unchanged. New combined theorem prices mandatory frozen entropy under arbitrary independent reservoir padding, proves the fixed-width obstruction, and preserves bounded EXPECTED physical coin work at increasing precision. Prior A059 partial transactions survive; A060's schedule obstruction is sharpened to ALL adaptive distinct-factor occupation. A05741/20 and A091 NAND source result are contextual, not newly accepted without reconstruction. External A058/A091/A087 review remains pending. Full FEI OPEN.

## one next mathematical action and independent reviewer

A058/A091 reconstruct (5)-(9a) and the all-adaptive coherent lower bound; A087 challenges side conditions. Next supply a Bellman inequality that charges total frozen full entropy AND live decay against actual original capacity. The exact local reservoir price, not discarded influence alone, is the necessary input. No full-source theorem at fixed9/2 should be retried.

## actual persistence receipts or precise save blocker

Four protocol files, proof, scoped source review, three frozen specs, exact scripts/outputs and source pins saved inside A059. STATUS two lines; dated WORKLOG/LEARNED updated. out/PERSISTENCE.json validates exact schemas, statement hash, identical progress copies, size caps and local SHA256 readback. Supervisor copy, index adoption and mirrors NOT_OBSERVED. No Git, mail, peer messages, brain research writes or edits to another agent's folder.

Brain self-care degraded/unverified: personal-model196.8h/state181.4h/dream53.8h stale at stage start; owner alerted before reliance. Research uses current saved proofs. Initial distress snapshot had1.1GB free disk; a later snapshot had3.4GB (new observation, no cleanup credited to this stage). Existing film/research holders were left alone. The required useless-work diagnostic was invoked; its final structured output was not retained, so no cleanup verdict or stop is claimed. Only small bounded jobs were launched and all owned jobs are awaited.

## Universal bridge

C019 stopping-tree payment and C024 history transfer gain a necessary full-terminal liquidation price that survives optimal outcome selection: tensor padding forces Fopt to e H(h)/(A I(h)), with an actual rate6 floor>=1/768. ALL-adaptive coherent first-touch accounting prevents replacing terminal entropy by mere possible depth. Increasing physical precision attains the ideal price with<2 expected dummy queries per action, so that implementation overhead need not grow with depth. What remains is the universal Bellman inequality paying accumulated frozen entropy and exhausting the live core from the SAME sufficiently large original source. NEXT targets exactly that unpaid bill, rather than another optional stopping class or a source rate already disproved by NAND tensors.
'''
write(R/'REPORT.md',report)
state=f'STATE: Stage22 full-terminal tensor price proved; rate6 floor>=1/768; ALL-adaptive coherent first-touch bound; lazy coins<2 expected queries; {total} exact assertions PASS; review pending; FEI OPEN.'
nxt='NEXT: A058/A091/A087 review reservoir price/physical precision/all-adaptive mask bound; fund ACCUMULATED frozen entropy plus live decay from SAME sufficiently large original unused influence; no fixed9/2 full-source retry.'
write(B/'STATUS.md',state+'\n'+nxt+'\n')
entry=f'\n2026-10-27 stage22: A058 local LP independently HOLDS. Tensor reservoir gives exact compulsory frozen price Fopt->e H(h)/(A I(h)); actual rate6 rare-tag+AND2 floor>=1/768. Fixed worst-case coin width freezes linear entropy, but logarithmically growing width attains the ideal price using<2 expected lazy dummy queries. ALL-adaptive coherent mask occupation E Hleaf>=2(cN-J) proven. {total} exact main/audit/coin assertions PASS, pilot576 separately. External review and universal accumulated frozen/live Bellman payment OPEN.\n'
for name in ['WORKLOG.md','LEARNED.md']:
 p=B/name;s=p.read_text(encoding='utf-8') if p.exists() else ''
 if entry.strip() not in s:write(p,s+entry)
sources=[];base=Path('~/brain_workers/FEI100_20261011')
for p in [base/'BOARD.md',base/'claude/B12/STREAM_NOTES.md',base/'agents/A058/runs/20261027T114055Z-fleet04-A058-overlapping-compositions/PROOF.md',base/'agents/A060/runs/20261027T011815Z-fleet04-A060-composition-sharpness/PROOF.md',base/'agents/A091/runs/20261027T054729Z-fleet04-A091-composition-referee/PROOF.md',base/'agents/A057/runs/20261027T080128Z-fleet04-A057-coherent-restriction-remainder/REPORT.md']:
 sources.append({'path':str(p),'sha256':sha(p)})
dump(R/'out/SOURCES.json',sources)
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((B/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
receipts=[]
for p in list(R.rglob('*'))+[B/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]:
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE.json',{'status':'PASS_LOCAL_READBACK','schemas':'EXACT_FIELDS','files':receipts,'remote_mirror':'NOT_OBSERVED','independent_review':'PENDING','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
print(json.dumps({'status':'COMPLETE_LOCAL','checks':total,'files_hashed':len(receipts),'FEI':'OPEN'}))
