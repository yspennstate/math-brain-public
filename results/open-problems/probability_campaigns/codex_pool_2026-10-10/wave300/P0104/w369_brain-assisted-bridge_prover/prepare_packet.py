"""Author-side packet preparation. No integration, global controls, or store writes."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATE='2026-10-10'
attempt=(ROOT/'ATTEMPT.md').read_text(encoding='utf-8')
retrieval=json.loads((ROOT/'math_retrieval.json').read_text(encoding='utf-8'))
measurements=json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
legacy_id='claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4'
legacy=next(n for n in retrieval['nodes'] if n['id']==legacy_id)

def write(name,value):
    (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def section(key):
    match=re.search(r'^## '+key+r'\..*?(?=^## |\Z)',attempt,re.M|re.S)
    assert match,key
    return match.group(0)

statements={
'L0':('Quantitative interval anti-concentration implies a variance lower bound',
       'If X is a real square-integrable random variable, L>0, 0<epsilon<=1, and every closed real interval of length L has probability at most 1-epsilon under X, then Var(X)>=epsilon*L^2/4.',
       ['X is real and square-integrable','The interval bound is uniform over all interval locations','L>0 and 0<epsilon<=1']),
'L1':('Sharp variance lower bound from two separated quantiles',
       'If X is real and square-integrable, a<b, p,q>0, P(X<=a)>=p, and P(X>=b)>=q, then Var(X)>=[pq/(p+q)]*(b-a)^2. The constant is attained by masses p at a, q at b, and 1-p-q at (pa+qb)/(p+q).',
       ['X is real and square-integrable','a<b and p,q>0','The displayed two probability lower bounds hold']),
'L2':('Uniform kurtosis makes interval width comparable to standard deviation',
       'Let X be real with 0<sigma^2=Var(X)<infinity and E|X-E X|^4<=K*sigma^4 for a finite K. For 0<p<=1/(32K), let W_p(X) be the infimum of lengths of closed real intervals containing probability at least 1-p. Then sigma<=W_p(X)<=2*sigma/sqrt(p).',
       ['Positive finite variance','Fourth centered moment bounded by K times variance squared','0<p<=1/(32K)']),
'L3':('Weak fluctuation scaling transfers to variance under uniform kurtosis',
       'Let X_n be real random variables with positive finite variances sigma_n^2 and E|X_n-E X_n|^4<=K*sigma_n^4 for one finite K and every n. If a_n>0, m_n is deterministic, and (X_n-m_n)/a_n converges in distribution to a nondegenerate real Z, then Z has finite fourth moment and Var(X_n)/a_n^2 converges to Var(Z) in (0,infinity). No independence across n is needed.',
       ['One uniform fourth-centered-moment constant K','Positive finite variances','Deterministic m_n and a_n>0','Nondegenerate weak limit']),
'L4':('Weak one-third scaling and subdiffusive concentration do not force one-third variance exponent',
       'For n>=3 put p=n^(-1/6), a=n^(1/3), b=sqrt(n*log n). Let R have masses (1-p)/2 at +/-a and p/2 at +/-b, and X_n=n+R. Then X_n>0, E X_n=n, and (X_n-n)/n^(1/3) converges in total variation to a symmetric sign, but Var(X_n)=(1-p)*n^(2/3)+n^(5/6)*log n, with log Var(X_n)/(2 log n)->5/12. For every lambda>=0, P(|X_n-E X_n|>=lambda*sqrt(n/log n))<=exp(1/3)*exp(-lambda/6). This is an abstract random-variable counterexample, not an iid lattice FPP construction.',
       ['The explicit four-atom laws in the statement','n>=3','No assertion that these laws are lattice passage times']),
'L5':('Fourth-moment martingale expansion retains a cubic mixed term',
       'For a finite real martingale M_k with M_0=0 and finite fourth moments, put D_k=M_k-M_{k-1}. Then E M_N^4=sum_{k=1}^N(6 E M_{k-1}^2 D_k^2+4 E M_{k-1}D_k^3+E D_k^4). The cubic term need not vanish: if M_1 is a symmetric sign and conditionally on M_1=1, D_2=-1 with probability 2/3 and 2 with probability 1/3, with reversed signs when M_1=-1, then E[M_1D_2^3]=2 and E M_2^4=27. Dropping that term gives 19.',
       ['Finite real martingale with M_0=0','Each M_k has finite fourth moment','No conditional symmetry of D_k is assumed'])}
entries=[]
claim_rows=[]
for key,(title,statement,assumptions) in statements.items():
    logical={
    'L0':'quantitative-interval-anticoncentration-variance-lower-bound',
    'L1':'sharp-separated-quantiles-variance-lower-bound',
    'L2':'uniform-kurtosis-interval-width-standard-deviation-comparison',
    'L3':'uniform-kurtosis-weak-scaling-variance-transfer',
    'L4':'rare-tail-counterexample-weak-scaling-variance-exponent-transfer',
    'L5':'martingale-fourth-moment-expansion-nonzero-cubic-term'}[key]
    entries.append({'key':key.lower(),'namespace':'probability.fluctuations',
                    'logical_name':logical,'kind':'lemma','title':title,
                    'statement':statement,'proof_text':section(key),'assumptions':assumptions,
                    'domain':'probability theory','source':{
                      'source_id':f'owner-probability-campaign-20261010:w369:{key.lower()}',
                      'url':'file:///~/brain_workers/w369/ATTEMPT.md',
                      'revision':'author-proof-awaiting-independent-review-20261010',
                      'license':'owner-own-work (campaign deduction; no novelty claim)',
                      'excerpt':None}})
    claim_rows.append({'id':f'w369-{key.lower()}','type':'conditional_bridge_or_counterexample',
                       'statement':statement,'assumptions':assumptions,
                       'source':{'path':str(ROOT/'ATTEMPT.md'),'section':key},
                       'proof_or_counterexample':section(key),
                       'independent_reviewer':'w371; pending',
                       'remaining_gap':'For a P0104 application: uniform lattice standardized fourth moments and independent n^(1/3) typical-scale input remain unproved. Scalar result awaits independent review.',
                       'status':'proved special case','scope':'author proof of stated scalar/conditional result; not proof of P0104',
                       'review_status':'unreviewed','novelty_claim':False})

route='The abstract implication "nondegenerate n^(1/3) weak scaling plus exponential concentration at sqrt(n/log n) implies variance exponent 1/3" is false without an additional moment or uniform-integrability argument at the claimed scale. The explicit four-atom counterexample has variance exponent 5/12. This refutes only that abstract route, not lattice KPZ.'
entries.append({'key':'refuted-route','namespace':'probability.fluctuations',
                'logical_name':'refuted-weak-kpz-scale-to-variance-route-without-moment-control',
                'kind':'concept','title':'Refuted route: weak KPZ scaling plus a larger concentration scale',
                'statement':route,'proof_text':None,
                'assumptions':['The route uses only the numerical distributional and tail inputs, without lattice structure'],
                'domain':'probability theory','source':{
                  'source_id':'owner-probability-campaign-20261010:w369:refuted-route',
                  'url':'file:///~/brain_workers/w369/ATTEMPT.md',
                  'revision':'author-refutation-awaiting-independent-review-20261010',
                  'license':'owner-own-work','excerpt':None}})
relations=[
 {'from_key':'l3','to_key':'l2','kind':'depends_on','rationale':'L3 uses L2 to bound sigma_n/a_n from tightness before proving uniform integrability.'},
 {'from_key':'l4','to_key':'refuted-route','kind':'refutes','rationale':'All stated numerical inputs hold in L4, but its variance exponent is 5/12.'},
 {'from_key':'l0','to_key':'l1','kind':'semantic_association','rationale':'Both quantify a valid lower bound from interval or separated-quantile information; their assumptions are distinct.'},
 {'from_key':'l3','to_key':'l5','kind':'semantic_association','rationale':'L5 isolates mixed-moment obligations in an attempted proof of L3\'s uniform kurtosis input for lattice FPP.'},
 {'from_key':'l0','to_existing_logical':'math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents','kind':'semantic_association','rationale':'Corrects a retrieved inference used in P0104 fluctuation reasoning; this is not a solution to the open problem.'},
 {'from_key':'l4','to_existing_logical':'math:probability.core:attempt-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents','kind':'semantic_association','rationale':'A disjoint obstruction: weak scaling plus larger-scale concentration does not determine variance, beyond the prior logarithmic-barrier observation.'}]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w369',
        'bundle_slug':'p0104-typical-scale-variance-bridge-w369-20261010',
        'entries':entries,'relations':relations}
write('DRAFT_BUNDLE.json',bundle)

# Local validation is deliberately separate from ingestion.
keys={e['key'] for e in entries}
assert len(keys)==len(entries)<200
for e in entries:
    assert all(k in e for k in ['key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'])
    assert e['source']['license'].startswith('owner-own-work')
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert e['proof_text'] if e['kind'] in ['lemma','theorem'] else e['proof_text'] is None
for edge in relations:
    assert edge['from_key'] in keys
    assert edge['kind'] in ['depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association']
    assert ('to_key' in edge and edge['to_key'] in keys) or 'to_existing_logical' in edge
write('BUNDLE_VALIDATION.json',{'validated_locally':True,'entries':len(entries),
      'relations':len(relations),'proof_lemmas':len(statements),
      'depends_on_acyclic':True,'integration_run':False,'independent_proof_audit':False})

existing={json.loads(line)['id'] for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()}
with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:
    for row in claim_rows:
        if row['id'] not in existing:
            stream.write(json.dumps(row,ensure_ascii=False)+'\n')

old='an anti-concentration statement bounds how much mass the law of T(0,x) can put in a short interval. It does not by itself lower-bound the variance, and a variance lower bound does not by itself give anti-concentration. Chaining them silently is a category error.'
assert old in legacy['statement']
replacement='Quantitative anti-concentration DOES imply a variance lower bound: if every interval of length L has probability at most 1-epsilon and X is square-integrable, Var(X)>=epsilon L^2/4. A variance lower bound alone need not imply anti-concentration. The cited planar Theorem 1 also gives two separated quantiles with positive probability; these imply a logarithmic variance lower bound when the passage time is square-integrable. For d>2 the paper says its method gives only a constant-scale lower bound.'
write('CORRECTION.json',{'state':'DRAFT; independent review required',
      'original_node_id':legacy_id,'original_logical_id':legacy['metadata'].get('logical_id'),
      'original_statement':legacy['statement'],'exact_fragment_to_replace':old,
      'replacement_fragment':replacement,'supporting_claim_ids':['w369-l0','w369-l1'],
      'primary_source':'https://arxiv.org/html/1810.08270v2',
      'primary_locator':'Theorem 1, condition (1.2.1), Remark 2',
      'application':'Append a reviewed corrected revision through the coordinator; preserve the old node and its provenance.'})

write('SOURCE_STATUS.json',{'problem_id':'P0104','date':DATE,
 'current_openness':'UNKNOWN','exact_statement_recovered':True,
 'source_precision':'The original questions use suitable conditions and do not fix the asymptotic convention. The packet explicitly specializes rather than treating these as precise universal assumptions.',
 'precise_specialization':{'graph':'nearest-neighbor undirected Z^2','weights':'iid Exp(1)',
                         'T_n':'infimum of weight sums over finite paths from (0,0) to (n,0)',
                         'target':'lim log Var(T_n)/(2 log n)=1/3'},
 'original_target':{'source':'Auffinger-Damron-Hanson, arXiv:1511.03262',
                    'locator':'Section 3.1, Questions 13 and 15',
                    'parts':['exponent below 1/2 in d>=2 under suitable F conditions','planar exponent 1/3','positive exponent in suitable d'],
                    'store_node':'claim_32684d2ece2943d218971312722a87f42333b030b9c7a29f034d6c11f31f8f1d',
                    'legacy_page_locators':'The old card gives PDF pp.34 and40; the checked current PDF was located by question numbers, avoiding that version-dependent page attribution.'},
 'full_hypotheses_compared':[
  {'source':'https://arxiv.org/html/1401.0917v2','locator':'Theorem 1.1, (1.2), (1.3)',
   'hypotheses':['iid nonnegative nearest-neighbor edge weights on Z^d','d>=2','F(0)<p_c(d)','E exp(alpha t_e)<infinity for some alpha>0'],
   'conclusion':'Two-tail exponential concentration at sqrt(||x||_1/log ||x||_1), ||x||_1>1, lambda>=0',
   'proof_need_mismatch':'Scale is not standard deviation and not n^(1/3); it does not supply uniform kurtosis at the claimed scale.'},
  {'source':'https://arxiv.org/html/1810.08270v2','locator':'Theorem 1, (1.2.1), Remark 2',
   'hypotheses':['planar Z^2 iid nonnegative edge weights','F(0)<1/2','if I=inf supp F>0, F(I)<oriented-bond critical threshold'],
   'conclusion':'Two deterministic quantile levels with positive probability liminfs separated by at least a fixed multiple of sqrt(log ||x||)',
   'own_deduction':'With square-integrable T, L1 yields Var T>=c log ||x||. In d>2 the cited method gives constant lower scale only.'},
  {'source':'https://arxiv.org/html/2604.01214v1','locator':'Sections 1.1 and 2.1.1, Theorem 2.1',
   'hypotheses':['Riemannian path lengths on R^2, not edge-weight lattice lengths','radial nonnegative smooth bounded kernel K supported in unit ball','Gaussian white noise or homogeneous Poisson input','smooth monotone field transform bounded between positive finite d1,d2','continuous path metric, scaled to time constant 1'],
   'conclusion':'Stretched-exponential concentration around n at Q_n comparable to the actual standard deviation; the main theorem gives some polynomial variance saving.',
   'proof_need_mismatch':'No verified transfer of this model and its assumptions to lattice Exp(1) FPP.'}],
 'prior_attempts':{'recovered':'claim_9ffe9930e9d9ed5c9d98ff4d61a32155d942cd754628487fc173a2d2c6493b2f',
                   'digest':'Prior elementary example isolates the n/log n logarithmic barrier; not repeated here.',
                   'named_H_I_directories':'Targeted ID/exponent grep found no relevant attempt row.',
                   'Lean_directory':'Only dated attempted_un ranking annotation located; no actual theorem receipt for P0104.'},
 'owner_solved_retired_check':{'scars_read':['fpp_width3_strip_time_constant_solved_2026_07_12','openproblem_recon_fpp_chi_target_2026_08_09','l1prime_tightness_means_no_lossy_argument_can_work_2026_08_29','perceptron_proof_open_gaps_fleet_2026_07_12'],
                             'finding':'Solved strip time constant is a different model and quantity; unresolved sharp variance recursion not reused. No target-solution certificate found in the named reads.',
                             'limitation':'No exhaustive solved/retired registry located; current openness stays UNKNOWN.'},
 'novelty_claim':False,'formal_check_receipt':None})

edge_rows=[]
by_key={e['key']:e for e in entries}
for edge in relations:
    source=by_key[edge['from_key']]
    if 'to_key' in edge:
        target=by_key[edge['to_key']]
        target_statement=target['statement']
    else:
        logical=edge['to_existing_logical']
        target_statement=next(n['statement'] for n in retrieval['nodes'] if n['metadata'].get('logical_id')==logical)
    edge_rows.append({**edge,'from_statement_quote':source['statement'],
                      'to_statement_quote':target_statement,'status':'draft-unreviewed'})
(ROOT/'DRAFT_EDGE_ROWS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in edge_rows),encoding='utf-8')

hooks=[{'id':'variance-transfer-w369-01','area':'math','event':'PostToolUse',
 'cue':'A returned probability card says anti-concentration cannot imply a variance lower bound.',
 'fire_when':'The retrieved legacy card claim_3ccc6fc... is used to reject a uniform interval-mass argument.',
 'silent_when':'The agent correctly states that variance alone does not imply anti-concentration.',
 'text':'Check the implication direction. A uniform interval bound P(X in I)<=1-epsilon for every interval of length L gives Var(X)>=epsilon L^2/4 in L2. Rare tails obstruct the converse.',
 'evidence':'math_retrieval.json:claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4; ATTEMPT.md L0; MEASUREMENTS.json L0-exact cases',
 'proposer':'w369'},
 {'id':'variance-transfer-w369-02','area':'math','event':'stage-start',
 'cue':'A proof converts a weak KPZ-scale limit to a variance exponent.',
 'fire_when':'Only weak n^(1/3) scaling and sqrt(n/log n) tails are cited for the variance conclusion.',
 'silent_when':'Uniform integrability of the squared claimed-scale fluctuations is proved, for example via uniform standardized fourth moments plus tightness.',
 'text':'Weak scaling alone does not determine variance. Name and prove the moment or uniform-integrability input at the claimed scale. Lattice concentration at sqrt(n/log n) cannot be substituted for standard-deviation concentration.',
 'evidence':'ATTEMPT.md L3-L4; MEASUREMENTS.json log_n=192: TV=1.2664e-14 but variance/n^(2/3)=1.5161e16; perceptron_proof_open_gaps_fleet_2026_07_12',
 'proposer':'w369'}]
assert all(len(h['text'])<=300 for h in hooks)
(ROOT/'HOOK_PROPOSALS.jsonl').write_text(''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks),encoding='utf-8')

# The user explicitly authorizes this worker's draft inbox. The integrator is
# NOT called: its live-store mutation conflicts with this worker's brief.
inbox=Path('~/math-brain-inbox/w369')
inbox.mkdir(parents=True,exist_ok=True)
number=1
while (inbox/f'bundle_{number:03}.json').exists():
    number+=1
destination=inbox/f'bundle_{number:03}.json'
part=destination.with_suffix('.json.part')
part.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
part.rename(destination)
write('SUBMISSION_STATE.json',{'draft_created':True,'submitted':True,
      'inbox_path':str(destination),'reviewed':False,'reviewer':'w371; pending',
      'ingested':False,'retrievable':False,'local_validation':True,
      'integration_run':False,'status':'DRAFT_ONLY'})

last=measurements['counterexample_measurements'][-1]
write('REASONING_FAILURE.json',{'retrieval_command':'python -X utf8 ~/brain_workers/w369/math_probe.py',
      'store':retrieval['database'],'cards_read':len(retrieval['nodes']),
      'seconds':retrieval['seconds'],'confirmed_false_inferences':1,
      'incorrect_node_id':legacy_id,'incorrect_fragment':old,
      'primary_check':'Theorem 1 of arXiv:1810.08270v2 gives separated planar quantiles; ATTEMPT L1 derives the variance lower bound.',
      'bounded_repair':'Review CORRECTION.json and append a corrected revision; land L0-L4 as typed proof/route nodes; hook requires moment control when weak scaling is used for variance.',
      'measured_counterexample':last,'checks_passed':measurements['checks_passed'],
      'checks_failed':measurements['checks_failed'],
      'deployment_improvement_claim':False,'repair_state':'proposed; not ingested or independently audited'})

review=f'''# w369 review packet: P0104 typical-scale to variance bridge

State: DRAFT, author proofs complete, independent review pending. P0104 is not solved; current openness UNKNOWN. Precise target and assumptions are in STATEMENT_FOR_ADVERSARY.md. Referee: w371; adversary: w370.

The concrete brain repair is CORRECTION.json, targeting {legacy_id}. The retrieved card reversed an implication: quantitative anti-concentration does yield a variance lower bound; variance alone need not yield anti-concentration. The cited primary theorem is planar and supplies two separated quantiles. Preserve its dimension and distribution assumptions.

Review ATTEMPT.md L0--L5. Check L2's 1/(32K) constant; L3's tightness-to-moment argument and arbitrary centering; L4's complete tail bound and absence of an iid FPP construction; and L5's nonzero cubic conditional moment. SOURCE_STATUS.json compares complete theorem hypotheses to the proof need. CLAIMS.jsonl and DRAFT_EDGE_ROWS.jsonl contain exact statements, statuses, and supporting ends.

Validation: {measurements['checks_passed']} checks passed, zero failed in {measurements['seconds']:.6f} seconds; the read-only eight-card probe took {retrieval['seconds']:.6f} seconds. At log n={last['log_n']}, the counterexample has TV distance {last['total_variation_to_sign']:.6g}, yet variance/n^(2/3)={last['variance_over_n_two_thirds']:.6g}. These are supporting calculations; no formal proof certificate or independent keep is claimed.

Inbox: {destination.as_posix()}. Local schema checks passed. Submitted=true, reviewed=false, ingested=false, retrievable=false. Coordinator integration is a later state. The legacy card lacks a logical_id, so its correction is keyed by its exact node id in CORRECTION.json; no unresolved cross-bundle correction edge was invented.

Hardest gap G: uniform standardized fourth moments for actual iid Exp(1) planar lattice passage times. Nondegenerate n^(1/3) typical scaling is also unproved. The known lattice concentration bound only gives a fourth-moment budget at the larger sqrt(n/log n) scale.

NEXT: Bound the cross and cubic sums of the finite FPP Doob martingale in L5 relative to Var(T_n)^2, or produce a lattice counterexample to that uniform-kurtosis input.
'''
(ROOT/'REVIEW_PACKET.md').write_text(review,encoding='utf-8')
report=f'''# w369 report

Found one wrong inference in eight targeted FPP cards: the anti-concentration card said its information cannot lower-bound variance. Quantitative interval avoidance and the primary paper's two-quantile statement do imply lower bounds. CORRECTION.json stages an exact append-only revision for independent review.

Saved six scalar/conditional lemmas and a refuted route. Uniform kurtosis makes typical scale determine variance; an explicit rare-tail law shows that weak n^(1/3) scaling plus the known-form larger-scale tail bound is insufficient. A martingale example exposes the cubic term that cannot be dropped.

Measurements: {measurements['checks_passed']} checks passed, zero failed; command: `python -X utf8 ~/brain_workers/w369/check_bridge.py`. Read-only probe: eight cards in {retrieval['seconds']:.6f}s. No deployed improvement is claimed.

Apply: w371 reviews ATTEMPT.md and CORRECTION.json; the validating coordinator integrates {destination.as_posix()} and appends a corrected legacy-card revision while preserving prior data. This deliverable is a mathematical data revision proposal, with no live code changes.

Risk: uniform lattice kurtosis and nondegenerate one-third typical scaling remain unproved. Counterexample laws are not lattice FPP. HOOK_PROPOSALS.jsonl and the progress event below are staged here because the worker brief confines global writes.

NEXT: Bound L5's FPP cross and cubic sums relative to Var(T_n)^2.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'PROGRESS_EVENT.txt').write_text('w369 P0104: exact source recovered; quantitative anti-concentration correction and conditional variance bridge saved; 11 checks pass; draft inbox submitted for w371 review. Evidence: ~/brain_workers/w369/REVIEW_PACKET.md; row S1.P0104.w369\n',encoding='utf-8')
print(json.dumps({'bundle':str(destination),'entries':len(entries),'relations':len(relations),
                  'claims_appended':len(claim_rows),'checks_passed':measurements['checks_passed'],
                  'state':'DRAFT submitted; unreviewed, not ingested, not retrievable'}))
