import json
from pathlib import Path
import xml.etree.ElementTree as E
root=Path(__file__).parent
lit=root/'LITERATURE.md'
s=lit.read_text(encoding='utf8')
marker='## Second serious attempt — 2026-10-11'
if marker not in s:
 s+='\n'+marker+'''\n
Two new routes are in SECOND_APPROACHES.md. The gap-directed brain calls
were math_recall.py on “circular law weak moments quantitative Hermitization
upper bound Götze Tikhomirov”, “small singular values Gaussian perturbation
Wegner estimate logarithmic integrability”, “local circular law sparse
matrices cumulants truncation”, “Tao Vu controlled second moment least
singular value truncation”, and “negative second moment identity singular
values distance Gaussian projection”. None returned a matching optimal
rate theorem; unrelated or withdrawn cards were not used as evidence.

Published inputs rechecked directly in downloaded PDFs:

- Tao–Vu, arXiv:0708.2895v5, Definition 2.2, pp.6–7; Lemma 2.4, p.7;
  Theorem 2.5, p.8. Its constants precede the entry-law quantifier and
  depend on a controlled second moment and the prescribed shift/failure
  exponents. It proves arbitrarily high polynomial least-singular-value
  probability bounds, not the optimal circular-law rate. Theorem 2.5
  is used for the fixed original law and fixed matching Gaussian in the
  direct upper proof; also uniform raw truncations in the transfer lemma.
- Jalowy, arXiv:2111.03595v3, Corollary 2, p.2, fixed all-moments expected
  W_1 rate. Used ONLY for a fixed matching Gaussian law, after phase
  rotation diagonalizes its real covariance. No n-dependent all-moments
  rate is imported.
- Götze–Tikhomirov, arXiv:0709.3995v4, Theorems 1.1–1.2, p.2. The
  exact checked hypothesis is finite E|X|^2(log(1+|X|))^(19+eta),
  and the stated object is the EXPECTED ESD. This is a qualitative lead,
  not a theorem resolving the requested optimal random-ESD rate.

New searches, all from Python urllib and saved raw:

'''
 for x in json.loads((root/'second_search_log.json').read_text()):
  s+=f"- {x['date']}; {x['service']}; `{x['url']}`; {x['status']}"+(f"; {x['bytes']} bytes." if 'bytes' in x else '.')+'\n\n'
 ns={'a':'http://www.w3.org/2005/Atom'}
 for filename in ['second_arxiv_sparse.json','second_arxiv_gaussian.json']:
  s+='\nInventory: '+filename+'\n\n'
  entries=E.parse(root/filename).findall('a:entry',ns)
  if not entries:s+='No entries returned. This is not an absence proof.\n'
  for e in entries:
   s+='- '+' '.join(e.find('a:title',ns).text.split())+'; '+e.find('a:id',ns).text+'\n'
 s+='''\nThe Gaussian-perturbation search yielded condition-number and
pseudospectral results rather than a matching optimal-rate theorem.
Crossref's relevant sparse-circular-law leads were Basak–Rudelson,
“The circular law for sparse non-Hermitian matrices,” Ann. Probab. 47
(2019), 2359–2416, DOI 10.1214/18-AOP1310, and Rudelson–Tikhomirov,
“The sparse circular law under minimal assumptions,” GAFA 29 (2019),
561–637, DOI 10.1007/s00039-019-00492-6. These are citation-level leads;
their full theorems were not fetched or used. No novelty claim is made
for the direct derivation, and no SOLVED_IN_LITERATURE conclusion follows.
'''
 lit.write_text(s,encoding='utf8')

claimsfile=root/'CLAIMS.jsonl'
old=[json.loads(x) for x in claimsfile.read_text(encoding='utf8').splitlines()]
new=[
 {'problem_id':'C0109','claim':'For every fixed centered variance-one complex iid law with finite (2+eps)-moment, e=min(eps,1), d_K(mu_n,mu_circ)=O(n^(-e/(12+4e)) log n) almost surely eventually, with failure below every prescribed polynomial power and the same expected-distance upper bound.','status':'proved','proof_location':'DIRECT_UPPER.md, complete theorem proof A–G; DIRECT_REFEREE.md','remaining_gap':'Nonoptimal exponent; does not identify exact dependence or match the previous fixed-law lower obstruction. External inputs: Tao–Vu Theorem 2.5 and Jalowy Corollary 2.','checks':'Full normalization/covariance/quantifier audit; area-scaled local lemma and finite strip covering; derivative, rational exponent, row replacement and projection checks. Formal checks are auxiliary only.'},
 {'problem_id':'C0109','claim':'For an iid finite-second-moment matrix and its coupled centered raw truncation, expected local L1 logarithmic-potential difference is bounded by C[(n P(|X|>R)+1/n)log n+n^(-D)], uniformly in R sufficiently large.','status':'proved','proof_location':'SECOND_ATTEMPT.md, Sections 2–5','remaining_gap':'Transfer bound alone is not a circular-law rate; uses Tao–Vu uniform controlled-moment inverse bound.','checks':'Exact preservation of controlled moment, singular-value rank interlacing, product-space Cauchy–Schwarz, deterministic L2 bound with only second moments.'},
 {'problem_id':'C0109','claim':'The normalized truncation comparison for compact C2 spectral statistics has expected error bounded by C||Delta f||[(n M R^(-2-eps)+1/n)log n+n^(-D)]+2 Lip(f) M R^(-eps).','status':'proved','proof_location':'SECOND_ATTEMPT.md, Section 6','remaining_gap':'Not itself a sharp spectral rate.','checks':'Variance correction via Schur/Frobenius energy and Cauchy–Schwarz; no eigenvalue rank inequality.'},
 {'problem_id':'C0109','claim':'For a Gaussian iid matrix with any real two-coordinate covariance of trace one plus any deterministic complex shift, expected singular-value proportion below u is <=C(u+1/n), uniformly in the shift.','status':'proved','proof_location':'DIRECT_UPPER.md, Section B','remaining_gap':'Gaussian comparison ingredient only; no sharp constant claimed.','checks':'Row deletion, Gram-inverse identity, complex projection real part, noncentral Gaussian Laplace transform, k>=2 condition; numerical translated-projection checks.'},
 {'problem_id':'C0109','claim':'The new direct-comparison auxiliary checks passed in finite computations.','status':'numerical_evidence','proof_location':'direct_checks.py; direct_checks.json','remaining_gap':'Does not formalize or independently prove the stochastic upper-rate theorem.','checks':'Six rational balances; 18 row replacements; three 12000-sample projection cases; six derivative identities to <1e-35; 1201 scalar inequalities.'}
]
for c in new:
 if not any(x['claim']==c['claim'] for x in old):old.append(c)
claimsfile.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in old),encoding='utf8')
print('Saved second-pass literature receipts and',len(old),'claims.')
