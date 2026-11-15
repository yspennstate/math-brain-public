# T056 literature update — 14 November 2026

The search found a reported negative solution and a substantial direct-product advance. The former's proof has not been independently audited here. Either finding warrants stopping under instruction 1; the direct-product theorem alone suffices for the substantial-advance branch.

## Reported negative solution

**OpenAI**, *A group without fixed price*, 5 October 2026, OpenAI Math Release preprint. **arXiv id:** none supplied in the primary citation; none verified here.

Primary sources actually opened: [title and abstract](https://raw.githubusercontent.com/openai/math/main/preprints/A-group-without-fixed-price-October-5-2026/build/paper.tex), [first theorem](https://raw.githubusercontent.com/openai/math/main/preprints/A-group-without-fixed-price-October-5-2026/build/introduction.tex), [conclusion](https://raw.githubusercontent.com/openai/math/main/preprints/A-group-without-fixed-price-October-5-2026/build/conclusion.tex). [PDF landing page](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/unequal-costs-rank-100-amalgam.pdf).

The theorem concerns

\[
A=F(a,b_1,\ldots,b_{99}),\quad
w=ab_1ab_2\cdots ab_{99}a,\quad
J=\langle b_1,\ldots,b_{99},w\rangle,\qquad
\Gamma=A*_J(J\times\mathbb Z).
\]

It claims that the Bernoulli action X has cost at least 1+eta for a specified eta>0, whereas the finite-height action Y_M has cost at most 1+99/M for every integer M>100. Choosing M>99/eta gives different costs and would disprove the universal fixed-price assertion. These are bounds, not exact cost evaluations. No independent verification of the lower-bound argument or of publication/refereeing status was completed.

Here K=e^96·96^99/95^95, 0<alpha<1/200, K·alpha^3<1/2, and eta=alpha/100. The space X is the free conull part of [0,1]^Gamma with product Lebesgue measure. On Y_M=X×Z/MZ, the action adds chi(g) to the second coordinate, where chi(a)=1 and chi(b_i)=chi(t)=0; t generates the displayed Z factor.

## Substantial direct-product advance

**Ali Khezeli**, *Products of Infinite Countable Groups Have Fixed Price One*, [arXiv:2509.08325v4](https://arxiv.org/abs/2509.08325v4), revised 4 January 2026.

[Theorem 1.1 in the full text](https://arxiv.org/html/2509.08325v4) states: for any two infinite countable groups G and H, G×H has fixed price one. No growth, amenability, or finite-generation hypothesis remains. This addresses all free pmp actions, strengthening the older existence of a cost-one action. The theorem statement was checked against the abstract and introduction; the full proof was not independently re-proved.

The brief's November 2026 status summary omits both items, although both are dated earlier than that status check.
