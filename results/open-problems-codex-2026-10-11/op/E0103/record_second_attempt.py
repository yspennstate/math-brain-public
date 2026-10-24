from pathlib import Path
import json

p=Path('.')
claims=[
('Exact factorial density of exposed right endpoints in a stationary marked interval Boolean model is rho_t times the product of k_t over consecutive gaps, where k_t(h)=lambda P(ell_t<h) exp(-lambda E min(h,ell_t)).',
 'proved','SECOND_ATTEMPT.md Lemma F1','An exact reduction by itself does not solve general tail asymptotics.','Marked Poisson insertion and equal-length union identity; ClusterAlgebra.lean; finite pair-moment diagnostics.'),
('In dimension one with fixed radius-r grains and (log h) E[|V|1_(|V|>h)] -> 0, lambda m C([0,L])+2 lambda r-log(lambda L)-log(theta) converges to standard Gumbel, theta=(1-p0)/(1-p0+p0 exp(-2 lambda r)), p0=P(V=0), m=E|V|>0.',
 'proved_special_case','SECOND_ATTEMPT.md Theorem F','General finite-mean tails outside the specified tail condition and higher-dimensional centered laws remain unresolved.','Complete kernel/factorial-moment proof; exact boundary lemma; bounded and exponential-speed simulations; independent static-clump calculation.'),
('At the centered time in Theorem F, the uncovered-component count converges to compound Poisson with rate exp(-z)*theta and positive geometric(theta) cluster sizes; it is Poisson only when p0=0.',
 'proved_special_case','SECOND_ATTEMPT.md Theorem F steps 2-3','The count result is for one-dimensional interval targets and the stated tail hypothesis.','All factorial moments; explicit generating function; exponential-moment determinacy; finite exact and sampled variances.'),
('For one-dimensional speeds P(|V|>u) ~ c/(u (log u)^2), C([0,L])/log L converges to min(Exp(lambda c),1/(lambda m)), and its normalized mean converges to (1-exp(-c/m))/(lambda c).',
 'proved_special_case','SECOND_ATTEMPT.md Theorem G','Not a classification of arbitrary oscillating or other finite-mean tails.','Conditional Poisson deletion of all spanning grains; exact common-hit subtraction; three-range covariance proof; critical_tail_checks.json.'),
('If E[(|V|-h)_+] ~ A/(log h)^alpha with 0<alpha<1, then C([0,L])/(log L)^alpha converges to Exp(lambda A), with normalized mean converging to 1/(lambda A).',
 'proved_special_case','SECOND_ATTEMPT.md Theorem H','Higher-dimensional and non-logarithmic integrated-tail laws are not covered by this theorem.','Same exact conditional void identities; full covariance bounds and spanning-based uniform integrability; critical_tail_checks.json.'),
('For P(|V|>u) ~ c/(u (log u)^p), all p>1 are classified for one-dimensional interval coverage: exponential for 1<p<2, truncated exponential for p=2, corrected Gumbel for p>2.',
 'proved_special_case','SECOND_ATTEMPT.md final corollary','The source problem permits wider target, grain and velocity classes.','Each row reduced with exact integrated-tail asymptotics to proved Theorems F, G or H.'),
('Two deterministic algebraic steps for the second attempt passed Lean: equal-length interval increment and the cluster-index rational identity.',
 'proved','ClusterAlgebra.lean; cluster_lean_check.txt','Stochastic and asymptotic arguments are written proofs rather than Lean formalizations.','lake env lean exited 0 without sorry or native_decide; harmless unused-tactic/simp warnings.')
]
existing=[json.loads(x) for x in p.joinpath('CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
seen={x['claim'] for x in existing}
with p.joinpath('CLAIMS.jsonl').open('a',encoding='utf-8') as f:
    for claim,status,loc,gap,checks in claims:
        if claim not in seen:
            f.write(json.dumps({'problem_id':'E0103','claim':claim,'status':status,
                               'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')

lit=p.joinpath('LITERATURE.md').read_text(encoding='utf-8')
header='## Second-attempt gap-directed recall and searches'
if header not in lit:
    lit+='\n'+header+'\n\nDate: 2026-10-11.\n\n'
    lit+='- math_recall.py "Boolean interval coverage clump M/G/infinity busy period Gumbel Poisson approximation". General Poisson approximation, Le Cam, extreme-value and Last-Penrose cards; no matching coverage theorem.\n'
    lit+='- brain.py recall "one dimensional Boolean coverage random interval lengths Gumbel mistakes". Mostly off-target hits plus adjacent inertial detection memory; none used as a verdict.\n'
    lit+='- math_recall.py "Hall coverage processes Poisson clumps random intervals M/G infinity busy period". General stochastic geometry and Poisson mapping/Mecke cards; no specific busy-period theorem was supplied. The argument was derived and checked directly.\n'
    for row in json.loads(p.joinpath('search_log.json').read_text()):
        if row['service'].startswith('second_'):
            lit+=f"- {row['date']} - {row['service']} - HTTP {row.get('status','ERROR')} - {row['url']}\n"
    lit+='\nThe arXiv random-interval/Gumbel query returned zero entries. The Crossref query mainly returned queueing busy-period papers; none was used as a solution or as an unverified theorem. These broad queries do not establish novelty.\n\n'
    x=json.loads(p.joinpath('second_crossref_clumps.txt').read_text())['message']['items']
    for w in x:
        title=' '.join(w.get('title',[]))
        if 'In the search for the infinite' in title:
            authors=', '.join(' '.join([a.get('given',''),a.get('family','')]).strip() for a in w.get('author',[]))
            lit+=f"Neighbouring-area lead from Crossref metadata: {authors}, *{title}*, {w.get('container-title',[])}, volume {w.get('volume','?')}, issue {w.get('issue','?')}, pages {w.get('page','?')}, {w.get('published',{})}. DOI {w['DOI']}. Full text was not audited; this is an infinite-server queue lead, not a matching mobile Boolean coverage solution.\n"
    p.joinpath('LITERATURE.md').write_text(lit,encoding='utf-8')
print('Added second-attempt claims and gap-directed literature log.')
