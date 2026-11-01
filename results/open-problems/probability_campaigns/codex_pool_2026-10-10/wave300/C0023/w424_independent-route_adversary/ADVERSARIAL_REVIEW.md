Adversarial review for w425 of w423's author-written LEMMAS.md, L1-L3, read after my independent derivation was saved. This is a review of the proofs, not of another review. No C0023 resolution or new-result novelty is certified.

L1: KEEP within the finite independent Bernoulli model. The finite-product derivative equals the sum of pivotal probabilities. Pivotality does not depend on the edge's own state, and an open pivotal edge implies the increasing event. Therefore lambda_A(p)=p f'(p)/f(p). Integrating on 0<a<b<1 is valid because the finite-event polynomial is positive there. Independence between pivotal indicators is not needed, and the proof does not assert it. The endpoint restrictions and the nonempty-event premise matter.

L2: KEEP as a conditional criterion; GAP for a lattice proof. Nested finite origin-to-boundary events decrease to infinite connection. A finite liminf of the integrated load gives a subsequence with a common finite bound, so the positive lower bound survives that subsequence limit. No limit/derivative interchange is used. The exact missing premise is one fixed a<p_c with liminf_n integral_a^{p_c} lambda_n(s)/s ds finite, or an integrable envelope uniform in n on that whole interval. A bound at p_c alone, or a different a_n for every n, does not suffice.

The size of this gap can be stated directly. Write eta=theta(p_c)>0 hypothetically. Subcritical exponential decay at any fixed a<p_c gives constants C(a),c(a)>0 with f_n(a)<=C(a) exp(-c(a)n). L1 then implies

integral_a^{p_c} lambda_n(s)/s ds >= c(a)n + log(eta/C(a)).

Thus the proposed uniform interval bound conflicts with exactly the hypothetical jump; it is not an estimate obtained from subcritical sharpness. It requires an additional geometric proof. The established subcritical-decay input is stated in Duminil-Copin--Kozma--Tassion, arXiv:1902.03207v2, section 1.2; the exponential constants here depend on a.

L3: KEEP for the stated nontransitive, unbounded-degree graph. The blocks have disjoint edge sets, so their success events are independent, and conditioning on all block successes preserves product factorization over blocks. A crossed block has open pivotals exactly when a single full path is open. Its conditional probability is m_n x_n(1-x_n)^(m_n-1)/h_n. At b=1/2, the failure sum is bounded by e^-1+e^-4/(1-e^-5)<1, so the root percolates. For a<1/2, h_n(a)<=n^2(2a)^(n+1)->0. The exponential-moment series converges for every fixed t; that quantifier is different from a bound uniform in all t. Borel--Cantelli uses only summable failures and correctly gives one infinite tail cluster. Incompletely open paths in a finite block cannot create an additional infinite cluster.

My independently derived tree has maximum degree 9 and theta_T(p_c)>=4/5. It complements L3 by showing that bounded degree does not rescue finite-volume continuity by itself. My tree does not establish critical uniqueness. L3's graph has uniqueness but lacks a degree bound. These two examples cannot be combined into a counterexample satisfying both properties simultaneously. Neither is a counterexample to the Z^d conjecture.

For the tree, the fixed-interval cost is quantitative. L1 and my M_n bound give, for each fixed a<1/2,

integral_a^{1/2} lambda_n(s)/s ds >= -n log(2a)-2 log n-log 5 -> infinity.

In contrast, a_n=1/2-1/n^2 leaves finite-generation survival bounded away from zero by my separate pivotal-path bound. This supplies a concrete failure of the attempted choice of scales, not a diagnosis based only on words such as continuity.

Verdict: restricted lemmas acceptable; full lattice proof incomplete. w425 must independently check my new tree and narrow-window calculations. No independent review of those calculations has been received.

NEXT: Check the lattice-specific geometric premise for a fixed backward interval; reject any replacement that silently lets its interval shrink with n.
