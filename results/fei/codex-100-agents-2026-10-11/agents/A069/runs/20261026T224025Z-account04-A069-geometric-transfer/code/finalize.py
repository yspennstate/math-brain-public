from pathlib import Path
import hashlib, json, datetime

RUN=Path(__file__).resolve().parents[1]
HOME=RUN.parents[1]
BASE=HOME.parent
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,value):
    Path(p).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def write(p,text): Path(p).write_text(text,encoding='utf-8')

def main():
    results=read(RUN/'out/results.json'); pilot=read(RUN/'out/pilot.json')
    assert results['status']=='PASS' and results['checks']==1145
    assert results['source_sha256']==sha(RUN/'code/certificate.py')
    formal=RUN/'out/lean_attempt.json'
    raw=formal.read_text(encoding='utf-8-sig')
    if raw.startswith('SETUP_UNVERIFIED'):
        write(RUN/'out/lean_attempt.txt',raw)
        save(formal,dict(status='SETUP_UNVERIFIED',compiler_launched=False,reason=raw.strip(),memory_cap_mb=1024,timeout_seconds=45,formal_claim='NONE'))
    lean=read(formal)
    assert lean['status']=='SETUP_UNVERIFIED'
    lead=BASE/'A070/runs/20261023T133455Z-account03-A070-analytic-route-referee'
    prior=HOME/'runs/20261023T130535Z-account03-A069-geometric-transfer'
    original=read(prior/'CLAIMS.json')
    oldclaims=read(lead/'CLAIMS.json')
    old=next(c for c in original if c['claim_id']=='A069-SHARP-INHERITED-CORE-ORDER-COMPARISON')
    reviewed=next(c for c in oldclaims if c['claim_id']==old['claim_id'])
    for field in ['exact_statement','hypotheses','statement_sha256','version']:
        assert old[field]==reviewed[field]
    boundary=next(c for c in oldclaims if c['claim_id']=='A070-HOMOGENEOUS-SOURCE-BOOLEAN-BOUNDARY')
    canonical_boundary=json.dumps({'exact_statement':boundary['exact_statement'],'hypotheses':boundary['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    assert boundary['statement_sha256']==hashlib.sha256(canonical_boundary).hexdigest()
    boundary['review_records'].append(dict(reviewer='account04/A069',verdict='HOLDS_AT_FULL_STATED_SCOPE',independent=True,substantive_repair=False,reviewer_conflict=False,review_source=str(RUN/'DERIVATION.md'),review_sha256=sha(RUN/'DERIVATION.md'),locators='Section 1 and out/results.json',method='Independent homogeneous coefficient-erasure and all-n singleton-source reconstruction; exact physical/normalized child masses and rational entropy upper/log lower sign bounds, without importing A070 code. No repair supplied.'))
    boundary['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A069_PENDING_B20'
    statement=('There are finite REAL uniform-cube functions g_k of unit squared norm, k>=2, that converge uniformly to the actual Boolean dictator x0 and have uniformly nearly unit squared norms at EVERY physical restriction, yet H(ghat_k^2)/J(g_k) diverges, where J is squared-derivative Fourier energy, not change-indicator influence. Explicitly epsilon=1/k, n=2^(2*k^4), m=2^(k^4), h_n=Im product_j (m+i*y_j)/sqrt(n+1), A_n=(1-((n-1)/(n+1))^n)/2>1/3, and g_k=(x0+epsilon*h_n)/sqrt(1+epsilon^2*A_n). Then abs(h_n)<=1 pointwise, sign(g_k)=x0, sup abs(g_k-x0)<epsilon+epsilon^2/2, sup abs(g_k^2-1)<=2epsilon+epsilon^2, every restriction has abs(E g_alpha^2-1)<=2epsilon+epsilon^2, J(g_k)<=1+epsilon^2, and H/J>2*k^2/(3*(1+1/k^2)). Each nonempty signed Fourier convolution residual is bounded by 2epsilon+epsilon^2 and the squared residuals sum to at most its square. For EVERY normalized original support-dominating reference R and EVERY complete adaptive physical tree, retaining homogeneous child spectra, both outcomes and all terminal costs, positive rate4 invoice V satisfies V/J>=H/J-4. Hence no finite influence-energy-priced original source or homogeneous invoice bound depending only on any fixed positive uniform Booleanity/norm tolerance exists. These real functions are uniformly bounded and round EXACTLY to a dictator; they are not Boolean FEI counterexamples. Exact Boolean source payment and full FEI remain open.')
    new=dict(claim_id='A069-UNIFORM-NEAR-BOOLEAN-SOURCE-OBSTRUCTION',version=1,exact_statement=statement,hypotheses=[
        'Uniform finite cubes; real g rather than Boolean f; base-two spectral entropy of the unit root squared law.',
        'J is Fourier squared-derivative energy; no identification with real change-indicator pivotal influence.',
        'k>=2 integer; n=2^(2*k^4), m=2^(k^4); huge dimensions are analytic parameters and never allocated.',
        'Original normalized reference dominates actual spectral support; descendants inherit only frequency marginals; homogeneous child masses are never separately normalized.',
        'Complete adaptive physical exposure including all coordinates after constant outputs, both full children and complete terminals; independent initial random seeds retain original law.',
        'This refutes a relaxed real-source route. The sign-rounded Boolean family is exactly x0; no Boolean FEI counterfamily or universal source is asserted.'
    ],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['account04/A069'],proof_source=dict(path=str(RUN/'DERIVATION.md'),sha256=sha(RUN/'DERIVATION.md'),locators='Sections 2-5, with homogeneous invoice reconstruction in Section 1'),proof_dependencies=[dict(claim_id=boundary['claim_id'],version=boundary['version'],statement_sha256=boundary['statement_sha256'],acceptance='Independently reconstructed unchanged in this run; used only for homogeneous invoice interpretation; direct proof included.')],review_records=[],status='AUTHOR_PROOF_WITH_EXACT_FINITE_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['Unregistered relaxed source principle: uniform closeness to Boolean values, uniformly approximate normalization at every physical restriction, or uniformly small full convolution residuals suffice for a finite dimension-independent source-payment constant depending only on their positive error tolerance.'],first_unproved_line=None,next_consumers=['A070','A088','A094','A096','B14','B20'])
    new['statement_sha256']=hashlib.sha256(json.dumps({'statement':new['exact_statement'],'hypotheses':new['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
    claims=[boundary,new]
    save(RUN/'CLAIMS.json',claims)
    receipt=dict(claim_id=old['claim_id'],version=old['version'],statement_sha256=old['statement_sha256'],statement_and_hypotheses_unchanged=True,reviewer='account03/A070',review_source=str(lead/'DERIVATION.md'),review_sha256=sha(lead/'DERIVATION.md'),verdict='HOLDS_AT_FULL_STATED_SCOPE',registry_adoption='UNVERIFIED')
    save(RUN/'out/CONSUMED_REVIEW.json',receipt)
    write(RUN/'out/COMPUTE_ADMISSION.md','Fresh memok output before the formal attempt: OK, physical free 6.7 GB (need 4.0), commit free 22.1 GB (need 8.0). This later admission differs from the earlier heavy-load snapshot because it is a new observation. The formal wrapper then rejected its fresh telemetry as distressed or unknown, before launching a compiler. No resource settings were changed and no other process was stopped. Python certificates used <48 MB estimate and <0.1 seconds measured arithmetic runtime.\n')
    sourcefiles=[lead/'DERIVATION.md',lead/'CLAIMS.json',prior/'REPORT.md',prior/'DERIVATION.md',prior/'CLAIMS.json',BASE.parent/'BOARD.md',BASE.parent/'claude/B14/STREAM_NOTES.md']
    context=BASE.parent/'context'
    sourcefiles += [context/name for name in ['percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt','threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt']]
    save(RUN/'out/SOURCE_MANIFEST.json',[dict(path=str(p),sha256=sha(p),read_scope=('Full new source or targeted baseline passages; current work uses only DERIVATION claims, not unstated geometric estimates.')) for p in sourcefiles])
    next_action='A070/A088/A094 reconstruct the bounded sine-product proof. Then derive from EXACT Boolean f^2=1 a selected inherited conditional log-loss payment with a once-owned influence-priced source potential; positive norm/convolution tolerances cannot replace this input. Preserve all old debits and both full terminals.'
    progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN.name,stream='B14',packet_id='A069',gap_id='C024-C019-ORIGINAL-OWNER-CUMULATIVE-CORE-EXCESS',attempt_id='A069-stage21-uniform-near-Boolean-source-boundary',method='Consume unchanged A070 sharp-order acceptance, independently reconstruct A070 real boundary, strengthen by bounded rational sine-product uniformly approaching a dictator, with exact finite physical and spectral checks.',mathematical_delta='Uniform approximate Booleanity, nearly unit norm at EVERY physical restriction, and small full signed-convolution residuals still permit unbounded homogeneous source payment even for uniformly bounded functions rounding exactly to a dictator. This closes the positive-tolerance relaxation, not Boolean FEI.',deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW_AND_SUPERVISOR_COPY',mathematical_status='SCOPED_ANALYTIC_PROOF_AND_EXACT_FINITE_CERTIFICATES;FULL_FEI_OPEN;NOT_LEAN_CHECKED',claim_versions_used=[dict(claim_id=old['claim_id'],version=old['version'],statement_sha256=old['statement_sha256']),dict(claim_id=boundary['claim_id'],version=boundary['version'],statement_sha256=boundary['statement_sha256'])],claims_created_or_changed=[dict(claim_id=boundary['claim_id'],version=1,change='Independent full-scope reconstruction unchanged'),dict(claim_id=new['claim_id'],version=1,change='New positive-tolerance obstruction with uniformly bounded near-Boolean real family')],source_artifacts=['DERIVATION.md','FROZEN_SPEC.json','code/certificate.py','code/ProductNorm.lean','code/finalize.py','out/pilot.json','out/results.json','out/lean_attempt.json','out/SOURCE_MANIFEST.json','out/CONSUMED_REVIEW.json','out/COMPUTE_ADMISSION.md'],next_consumers=['A070','A088','A094','A096','B14','B20'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['Original exact-Boolean source payment remains open; real route obstruction is not an FEI counterexample.','Formal checker rejected fresh compute admission before launching compiler; no Lean certification.','Independent new-claim review, B20 adoption and remote/mirror copy unverified.','Wake flagged stale owner-model 181.1h, state-of-mind 165.7h and latest dream38.1h; current instructions and original source evidence govern.'],packet_ids=['A069'])
    save(RUN/'PROGRESS.json',progress); save(RUN/'PACKET_DELTA.json',progress)
    report=f'''# A069 stage21: the uniform approximate-Boolean boundary

## exact target, quantifiers, hypotheses and units

Test whether approximate Booleanity can supply the still-unpaid ORIGINAL influence-priced source in C024/C019. The exact negative result concerns REAL functions, squared-derivative energy J, unit ROOT squared spectra and EVERY inherited support-dominating reference/complete physical tree. It does not concern a Boolean FEI counterfamily. Units are bits; ordinary influence is used only for actual Boolean functions.

## sources actually read, revisions and theorem locators

Current BOARD (26 October22:39), B14 lead notesv2, own STATUS/LEARNED and prior stage10 report/derivation, machine rules, full execution protocol2026-10-11-execution-v2 and targeted campaign/registry/plan/source baselines were read. The percolation30pp text Lemma2.1 remains the abstract complete occupied-cell encoding; arm payment is not transferred. Threshold38pp and earlier-version opening/scope passages were revisited, with no new threshold premise. New primary evidence is A070/run20261023T133455Z DERIVATION Sections1-6 and CLAIMS. Its unchanged full-scope acceptance of A069's sharp4J theorem is source/hash matched and consumed in out/CONSUMED_REVIEW.json. A070's real boundary is independently reconstructed without its code. The read-only math recall found the existing exact-singleton Booleanity guard, not this stronger bounded uniform-proximity claim; no novelty priority is asserted. Source hashes are in out/SOURCE_MANIFEST.json. Current user continuation governs despite old campaign dates.

## complete derivation or exact first unsupported line

DERIVATION Sections1-5 provide the proof. Gaussian-integer product factors have unit normalized modulus, so their imaginary part h_n is pointwise bounded by1. Its explicit odd-set spectrum has squared norm A_n>1/3, energy<=1, and every occupied atom at most1/(n+1). Add epsilon*h_n to a fresh dictator and normalize once at the ROOT. The resulting real g has J<=1+epsilon^2, sign(g)=x0 at every input, sup|g-x0|<epsilon+epsilon^2/2, and sup|g^2-1|<=2epsilon+epsilon^2. Therefore every actual physical restriction has squared norm within that same error of1, and the full convolution residual has squared l2 norm at most the error squared. Nevertheless H/J>epsilon^2 log2(n+1)/(3(1+epsilon^2)). Taking epsilon=1/k,n=2^(2k^4) makes H/J>2k^2/(3(1+1/k^2)), which diverges while all those errors vanish.

Homogeneous full-reference telescoping gives V>=CE-4J>=H-4J for EVERY original normalized dominating source and complete adaptive tree, including all constant-output continuations. Thus no positive tolerance, even uniform at all inputs/restrictions, supplies a dimension-independent source-payment constant. The sign-rounded actual Boolean family is exactly a dictator with H=0,I=1. This rules out a relaxation; it does not disprove FEI. First unsupported Boolean line: construct an ORIGINAL influence-paid source or selected-tree supersolution using EXACT Boolean relations, with all old debits and both full terminals.

## executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC.json precedes execution. Pilot m2 with epsilon1/2,1/4,1/8: PASS {pilot['checks']} exact predicates in {pilot['elapsed_seconds']:.6f}s. Final m2,4,8 (n4,16,64), same three epsilons: PASS {results['checks']} exact predicates in {results['elapsed_seconds']:.6f}s. No symmetry beyond the proved equal-coordinate cardinality/parity formula, and no automatic dimension increase. Finite validation is separate from the all-k proof.

All arithmetic is Fraction/integer. At n4 an independent direct complex product constructs every physical value; integer Walsh coefficients match the symbolic product spectrum, all full convolution sums match direct h^2 Walsh, signs match the dictator, and ALL729 restriction states across the three epsilons obey the claimed norm bound. At n16,64 exact binomial masses/energy match the closed formulas. Entropy signs use analytic atom/log bounds; no floating entropy decision is used. A070's child-renormalization mismatch is checked rationally; h2(1/5)<=1,4095>2^11 and(64/585)*11>1 prove its negative decrement analytically. The infinite k family is symbolic and is never allocated.

Executed commands: python -B -X utf8 runs/{RUN.name}/code/certificate.py --pilot; the same command without --pilot; and code/finalize.py. Resource estimate48MB, arithmetic cap55s. Fresh memok passed (6.7GB physical,22.1GB commit available), but the subsequent core-Lean wrapper rejected its refreshed compute state before compiler launch. ProductNorm.lean formalizes the Gaussian-integer numerator identity; no Lean-checked status is claimed. The planned compiler had1024MB hard cap, one thread, BelowNormal priority and45s limit; all logs were directed inside this run. No compiler, heavy job, detached worker, GPU job or process termination occurred.

## proof dependencies and changed downstream conclusions

A069-SHARP-INHERITED-CORE-ORDER-COMPARISON@1 has unchanged A070 full-scope acceptance, explicitly consumed rather than self-awarded. A070-HOMOGENEOUS-SOURCE-BOOLEAN-BOUNDARY@1 now has an independent unchanged reconstruction in this run. The new uniform-proximity obstruction is author-proved with exact finite checks, pending external review. The prior Boolean source/order theorem is preserved; the new real guard excludes relying only on approximate normalization or small signed-convolution residuals. It grants no new owner, source reset, omitted terminal or universal Boolean source.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

All four protocol artifacts, complete derivation, frozen spec, code and outputs are saved inside this requested A069 run. STATUS has exactly two lines and WORKLOG/LEARNED are updated. out/RECEIPTS.json hashes and reads back the run artifacts/rolling files and checks exact protocol key sets, statement hashes, file limits and matching packet delta. Local save is complete. Supervisor remote copies, brain ingestion, B20 adoption and independent review of the new theorem are unverified. No git, mail, shared indices, brain research write, other-agent mutation, trading access, or unrelated process stop occurred. Wake degradation was reported before relying on affected notes; those stale remembered owner contexts were not used as evidence.

## Universal bridge

This stage advances C024/C019 by proving that even UNIFORM approximate Booleanity at every input and every physical restriction cannot pay the ORIGINAL source; the explicit lower bound grows like k^2 while all normalization and convolution errors vanish. It consumes the independent acceptance of the previous sharp order comparison and closes the next tempting relaxation, without spending old owner capacity. The exact Boolean original-source payment remains unpaid. NEXT must use exact signed Boolean constraints to price a selected inherited conditional log-loss from an influence-priced source potential; that is the shortest route to full FEI because ordering and positive-tolerance normalization are now closed, and another transfer example cannot fund the original arbitrary core.
'''
    write(RUN/'REPORT.md',report)
    write(HOME/'STATUS.md','STATE: A069 stage21 saved: A070 prior theorem accepted unchanged; uniform near-Boolean REAL source obstruction proved;1145 exact checks PASS;formal admission held;FEI OPEN.\nNEXT: A070/A088/A094 review bounded product family; use EXACT Boolean f^2=1 to fund ORIGINAL influence-priced source/selected log-loss, all old debits and both full terminals; approximate norms/residuals fail.\n')
    with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write('\n2026-10-27 (requested stage20261026T224025Z, account04/A069): Consumed A070 unchanged sharp4J review and independently reconstructed its homogeneous real boundary. Strengthened mechanism: bounded sine-product g uniformly approaches and rounds exactly to a dictator, all restriction norms approach1, but H/J diverges. All-k proof saved; pilot941 and final1145 exact checks pass,729 physical restrictions. Core formal checker held on refreshed telemetry before compiler launch after memok0; no formal certification. Exact Boolean ORIGINAL source remains unpaid. No outside writes, git, messaging, heavy job or process stops.\n')
    with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
        f.write('\nStage21 durable: Approximate Booleanity is insufficient EVEN uniformly at all physical inputs/restrictions. For n=m^2, m even, h=Im product(m+i*y)/sqrt(n+1) is bounded1, has odd-set atom p^s(1-p)^(n-s), p1/(n+1), normA=(1-((n-1)/(n+1))^n)/2>1/3, energy<=1. g=(x0+eps*h)/sqrt(1+eps^2 A) has unit root norm, signx0, sup|g^2-1|<=2eps+eps^2, all restricted norms within this error, full convolution residual l2<=error, yet H/J>eps^2 log2(n+1)/(3(1+eps^2)). eps1/k,n2^(2k^4) gives divergence despite uniform convergence to dictator. Every homogeneous full-tree/source invoiceV/J>=H/J-4. REAL route guard only; no Boolean counterfamily. Exact f^2=1 or a stronger structural input must fund the ORIGINAL source; tolerances alone cannot. A070 prior-order acceptance consumed unchanged and A070 real-boundary proof independently reconstructed.\n')
    protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
    expected_progress={x.split(' (')[0] for x in protocol['progress_fields']}
    assert set(progress)==expected_progress
    assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
    assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
    for c in claims:
        assert set(c)==set(protocol['claim_fields'])
        if c['claim_id']==new['claim_id']:
            expected=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
            assert c['statement_sha256']==expected
        else:
            assert c['statement_sha256']==boundary['statement_sha256']
    for field in protocol['report_fields']: assert '## '+field in report
    files=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='RECEIPTS.json')+[HOME/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
    receipts=[]
    for p in files:
        assert p.stat().st_size<20*1024*1024
        receipts.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
    save(RUN/'out/RECEIPTS.json',dict(status='LOCAL_READBACK_PASS',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),artifacts=receipts,protocol_schema='PASS',external_save='UNVERIFIED',full_fei='OPEN'))
    print(json.dumps(dict(status='LOCAL_READBACK_PASS',checks=results['checks'],files=len(receipts),new_claim=new['claim_id'],formal=lean['status'],full_fei='OPEN')))

if __name__=='__main__': main()
