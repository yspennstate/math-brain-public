from pathlib import Path
import json

here=Path(__file__).resolve().parent
excerpts=json.loads((here/'primary_source_excerpts.json').read_text(encoding='utf-8'))
by_id={x['problem_id']:x for x in excerpts}
assert by_id['P0193']['excerpts'] and '(3) For each R' in by_id['P0193']['excerpts'][0]['text']
assert by_id['P0411']['excerpts'] and 'Proposition 5.1' in by_id['P0411']['excerpts'][0]['text']
assert by_id['C0072']['excerpts'] and 'Open Problem 13.6' in by_id['C0072']['excerpts'][0]['text']
assert by_id['P0039']['excerpts'] and 'Conjecture 6.45' in by_id['P0039']['excerpts'][0]['text']
p=here/'P0193_PROOF.md'
s=p.read_text(encoding='utf-8')
s=s.replace('Label: proof of an elementary kernel lemma; conditional application to the free-probability problem. Blind audit pending w346. No solved-problem claim.', 'Label: author-checked kernel proof and candidate free-probability refutation. Cached primary criterion checked; blind audit pending w346. No solved-problem claim.')
s=s.replace("The paper's exact criterion and time normalization have not yet been independently checked from a cached primary source. The following algebra does not need that citation.", "The exact criterion and time normalization are now checked against the cached primary text at sources/free_positive_unimodality_2020_correct/text.txt, character 16998, as preserved in primary_source_excerpts.json. Lemma 4.1(3) states that log-unimodality is equivalent to the equation (sin R/R) integral r xi/[1+r^2 xi^2-2r xi cos R] dnu(xi)=1/t having at most two positive r-roots for every R in (0,pi). Thus its normalization is exactly integral=R/(t sin R). This is a source check by the author of this packet; the independent auditor must check it again.")
s=s.replace('Conditional consequence: if the exact cited criterion says that log-unimodality of sigma_t free-multiplicatively convolved with nu requires at most two positive r-roots of the corresponding integral = R/[t sin(R)] for every R in (0,pi), then', 'Candidate consequence using the checked criterion: the cited equivalence requires at most two such r-roots for every R in (0,pi) whenever sigma_t free-multiplicatively convolved with nu is log-unimodal. Therefore')
s=s.replace('Novelty and the final free-probability inference remain unverified.', 'The source criterion has been checked locally; novelty and independent approval of the full free-probability inference remain unverified.')
p.write_text(s,encoding='utf-8')
p=here/'P0411_PROOF.md'
s=p.read_text(encoding='utf-8')
s=s.replace('Label: proof for the displayed normalized integral; source identification and blind audit pending.', 'Label: author-checked proof for the displayed normalized integral; cached source identification checked and blind audit pending.')
s=s.replace("All results below are conditional on that representation being the paper's H_d with its stated distance variable u.", "The representation has now been checked against the cached paper, Proposition 5.1 and formula (5.1), arXiv:2303.16831. Substitute x=exp(-u)z in its integral for 1/H_d(u): this gives exactly the displayed normalized I_n formula. Physical radii satisfy u>=0. Conjecture 7.5 was also read in the cached text: its even-dimensional clause explicitly uses the variable u in H_d(u)=exp(-(d-1)u)/f(u), so the sixth coefficient targets that literal clause. These are author source checks, not an independent KEEP.")
s=s.replace('The last check still requires the cached primary statement.', 'The literal variable has been checked in cached Conjecture 7.5; the independent auditor must verify the identification and coefficient argument.')
p.write_text(s,encoding='utf-8')
receipt={
 'command':'python -B -X utf8 finalize_source_checks.py',
 'checks':[
  {'problem_id':'P0193','reference':'Hasebe, Ueda and Wang, Log-unimodality for free positive multiplicative Brownian motion, arXiv:2009.13848, Lemma 4.1(3), PDF pp. 8-9 and Problem 4.7, p. 11','verdict':'Exact root criterion and time normalization matched; blind review pending'},
  {'problem_id':'P0411','reference':"D Achille, Curien, Enriquez, Lyons and Unel, Ideal Poisson Voronoi tessellations on hyperbolic spaces, arXiv:2303.16831, Proposition 5.1 and Conjecture 7.5",'verdict':'Integral representation and literal coefficient variable u matched; blind review pending'},
  {'problem_id':'C0072','reference':'Heydenreich and van der Hofstad, Progress in high-dimensional percolation and random graphs, Open Problem 13.6','verdict':'Target scaling and original-vertex wired boundary convention matched; all tail hypotheses stay explicit'},
  {'problem_id':'P0039','reference':'Lyons and Peres, Probability on Trees and Networks, 2026-08-19 electronic edition, Conjecture 6.45','verdict':'Verified base-walk versus infinite-cluster-walk scope'},
  {'problem_id':'P0245','reference':'Aldous and Fill, Reversible Markov Chains and Random Walks on Graphs, Open Problem 6.30','verdict':'Verified E_pi C >= (n-1) H_(n-1); prescribed-law result treats only two states'},
 ],
 'current_literature_status_certified':False,
 'independent_keeps':0,
}
(here/'source_check_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'primary_checks':len(receipt['checks']),'independent_keeps':0,'current_literature_status_certified':False},indent=2))
