SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-22T22:04:58Z.
attacking: literature-to-proof transfer for the first unpaid outer heavy-star branch; force a genuine transverse curvature direction and transfer the sharp LPP two-dimensional marginal theorem to it.

# account01/B18 — transverse-curvature/LPP certificate for every unresolved outer heavy star

**Run:** `20260922T220458Z-qform-B18-a01-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control source initially bound:** `yspennstate/math-research-brain@bf829e58518dfa3920733b1809379ecebeb40226`  
**Owner control revision:** `2026-09-22.15`  
**Assignment:** Literature-to-proof transfer  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_REDUCTION`  
**Full target:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and live correction discipline

The full target remains: for every dimension, every independent real input vector with marginal densities at most one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one (equivalently `s_3(A)>=1`), prove one universal finite bound on the density of `X^T A X`. Continuity is tracked separately.

I retain the current corrections: no law-uniform pointwise Fresnel decay for arbitrary fragmented cap-one densities; no independence after spectral rotation; no arbitrary-joint rank-three coarea theorem; no positive conditional-projection-density moment; no worst conditional scalar-remainder cap; no inference that a merely small star diagonal can be replaced by an exact zero diagonal. In particular the near-zero rank-one collapse `[[eps,1],[1,eps^{-1}]]` remains a valid obstruction to a naive half-Riesz perturbation argument.

The designated partner result actually applied is account02/B18 run `20260922T203852Z-b18-qform-lit-r12`, canonical mathematics

`yspennstate/math-open-problems@6cda809756c61201f08cdee2dd7e07f20e5d5596`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T203852Z-b18-qform-lit-r12/REPORT.md`.

It gives an exhaustive five-way reduction at threshold `delta=2^-9`. After the diffuse branches and the physical-pair branch are paid, its first remaining outer-star alternative has, in original physical coordinates,

`A=[[a,b^T],[b,C]],   |a|<delta,   beta:=||b||_2>delta,   s_3(A)>=1`.      (1.1)

The partner normalized `Y=<u,W>` with `u=b/beta` and used Livshyts--Paouris--Pivovarov only to obtain the scalar cap `||p_Y||_infinity<=sqrt(2)`. The source-valid missing issue was where the *third curvature* must live without conditioning away product structure. This run closes that deterministic-and-marginal implication exactly.

## 2. Primary literature transfer: use LPP at dimension two, not one

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949.

Their theorem says that if `W` has product probability density `prod_j f_j` with every `||f_j||_infinity<=1`, then every `k`-dimensional **orthogonal** marginal has density bounded by `2^(k/2)`. There are no moment, centering, bounded-support, smoothness, iid or log-concavity hypotheses.

Hence for any orthonormal pair `u,v` in the residual physical coordinate space,

`(Y,Z)=(<u,W>,<v,W>)`

has a genuine joint density satisfying

`||p_(Y,Z)||_infinity <= 2`.                                  (2.1)

This is a joint-density statement only; it does not make `Y,Z` independent and I do not use them as independent variables.

I also checked the recent polynomial-regularity route of E. Kosov, *Oscillatory integrals with polynomial phase and regularity of distributions*, arXiv:2511.02679 (2025). Its product-measure regularity statements require additional regularity such as bounded-variation control on the one-dimensional input densities. Arbitrary cap-one densities in the owner target can be highly fragmented and need not have any uniform BV bound. Thus that theorem is not a source-valid closure of the present full target. No exact prior theorem matching all owner quantifiers was located in the targeted literature check; this is not a novelty claim.

## 3. New deterministic lemma: a near-zero heavy star cannot consume the third singular direction

### Theorem 3.1 — `QFORM-HEAVYSTAR-TRANSVERSE-CURVATURE-v1`

Let

`A=[[a,b^T],[b,C]]`

be real symmetric, let `b!=0`, put

`beta=||b||_2,   u=b/beta`,

and let `H=u^perp` inside the residual coordinate space. Denote by

`D=P_H C P_H |_H`

the compression of `C` to `H`. If

` s_3(A)>=s>0,    |a|<s,`                                    (3.1)

then

` ||D|| >= s.`                                                 (3.2)

Consequently there is a unit `v in H` and a real `lambda` with

`D v=lambda v,     |lambda|>=s`.                               (3.3)

Moreover, after the purely deterministic orthogonal decomposition

`R^(n-1)=span{u} direct_sum span{v} direct_sum H_0`,

where `H_0={u,v}^perp`, the matrix has the exact arrowhead form

`A = [[a,    beta, 0,      0],
      [beta, c,    alpha,  d^T],
      [0,    alpha,lambda, 0],
      [0,    d,    0,      F]].`                               (3.4)

In particular the `v` direction has no coupling to `H_0`; all uncontrolled residual coupling enters through the star direction `u`.

### Proof

Write `C` relative to `span{u} direct_sum H` as

`C=[[c,d^T],[d,D]]`.

Then in coordinates `e_i,u,H`,

`A=[[a,beta,0],[beta,c,d^T],[0,d,D]].`                          (3.5)

Define

`K=[[0,beta,0],[beta,c,d^T],[0,d,0]].`                         (3.6)

If

`q=(beta,c/2,d)`,

then `K=e_u q^T+q e_u^T`, so

`rank K<=2`.                                                    (3.7)

Also

`A-K=diag(a,0,D)`, hence

`||A-K||=max{|a|,||D||}`.                                      (3.8)

By the Eckart--Young characterization of the third singular value,

`s_3(A)=inf_{rank R<=2} ||A-R|| <= ||A-K||`.                   (3.9)

Combining (3.1), (3.8), (3.9) and `|a|<s` forces `||D||>=s`, proving (3.2). Since `D` is symmetric, choose a unit eigenvector `v` with eigenvalue `lambda` of modulus `||D||`. For every `h in H_0`,

`<v,Ch>=<v,Dh>=<Dv,h>=lambda<v,h>=0`,                          (3.10)

which is exactly the vanishing `v-H_0` block in (3.4). QED.

This is a rank statement in matrix space only. The orthogonal coordinates in (3.4) are **not** declared independent random variables.

## 4. Literature-to-proof synthesis: the transverse pair has a universal joint density cap

### Corollary 4.1 — `QFORM-HEAVYSTAR-LPP-PAIR-v1`

Under Theorem 3.1, let `W` denote the residual vector of the original independent cap-one coordinates and define

`Y=<u,W>,   Z=<v,W>`.

Then

`|lambda|>=s` and `||p_(Y,Z)||_infinity<=2`.                   (4.1)

Thus every near-zero physical star satisfying (3.1) carries, without deleting or conditioning any original coordinate, a **transverse curvature direction of size at least `s` whose joint source with the star coordinate is a sharp LPP-controlled two-dimensional product marginal**.

Proof: (3.3) gives the curvature. The vectors `u,v` are orthonormal, so (2.1) applies verbatim. QED.

This is stronger than the scalar cap `||p_Y||_infinity<=sqrt(2)`: it identifies the third spectral resource and puts it into the same two-dimensional marginal before any conditioning can destroy product provenance.

## 5. Actual application to the designated account02/B18 reduction

Use account02/B18 Alternative 2, equation (1.1), with the partner's fixed

`delta=2^-9=1/512`.

Set `s=1` in Theorem 3.1. Since `|a|<delta<1`, every still-unpaid **outer heavy star** in that reduction admits orthonormal residual directions `u,v` for which

`beta=||b||>1/512`,                                            (5.1)

`|v^T C v|=|lambda|>=1`,                                      (5.2)

`||p_(<u,W>,<v,W>)||_infinity<=2`,                             (5.3)

and the exact matrix representation is (3.4), with no coupling from `v` to `H_0`.

Therefore the outer-star branch is no longer allowed to treat the third large eigenvalue as an unspecified global remainder: it is forced into the explicit transverse packet `(u,v)` with quantitative curvature one and the source-valid joint cap two.

This does **not** by itself bound the density of the full quadratic form, because the term `2Y<d,H_0>` and the quadratic remainder on `H_0` are generated by the same original product source as `(Y,Z)`. Taking a worst conditional law of `(Y,Z)` given that remainder would invoke a live-refuted interface. The exact remaining analytic object is the arrowhead trace

`Q=aX^2+2 beta X Y+cY^2+2 alpha YZ+lambda Z^2+2Y T+R_0`,       (5.4)

with

`|a|<1/512, beta>1/512, |lambda|>=1, ||p_(Y,Z)||_infinity<=2`, (5.5)

where `(Y,Z,T,R_0)` retain their common original-product provenance. A valid next theorem must integrate (5.4) jointly; it may not replace `(T,R_0)` by a worst conditional parameter.

The partner's Alternative 5 occurs *after* one large physical pivot and only guarantees two large singular values in the Schur residual. The rank-two approximation above spends two singular slots, so I do not falsely apply Theorem 3.1 to that residual branch. The result here is specifically the partner's outer-star Alternative 2.

## 6. Why this survives the current corrections

1. **No independence after rotation.** The orthogonal basis is used only for deterministic matrix identities. Probabilistically I retain exactly one statement: the pair `(Y,Z)` is an orthogonal marginal of the original product vector and hence has the LPP joint density cap two.
2. **No arbitrary-joint coarea.** A cap-two pair is not promoted to a full curved-trace bound.
3. **No conditional projection cap.** Nothing is conditioned on the orthogonal complement of `span{u,v}`.
4. **No near-zero-to-zero perturbation.** The physical diagonal `a` remains present in (5.4); the theorem uses only the strict numerical inequality `|a|<s` in the rank-two approximation.
5. **No raw pointwise Fresnel estimate.** The only literature anti-concentration transfer is the exact LPP marginal theorem.
6. **No single-minor conclusion.** `u,v` may be completely diffuse over the physical coordinates; no fixed coordinate pair is extracted.

## 7. What changed and what remains

**Proved this run:** `QFORM-HEAVYSTAR-TRANSVERSE-CURVATURE-v1` and `QFORM-HEAVYSTAR-LPP-PAIR-v1`. Applied to the designated partner reduction, every unresolved outer heavy star has the quantitative packet (5.5) and arrowhead identity (5.4).

**Still unpaid:** turn (5.4)-(5.5), with common product provenance retained, into a uniform density bound; separately pay the partner's post-pivot residual-heavy-star branch. This is now a translation-uniform joint-trace problem, not a search for where the third curvature lives.

**Full QFORM:** OPEN / NOT PROVED.  
**Continuity:** not claimed from the new reduction alone.

## 8. Source pins

- Control snapshot used for derivation: `yspennstate/math-research-brain@bf829e58518dfa3920733b1809379ecebeb40226`, owner revision `2026-09-22.15`.
- Designated partner: `yspennstate/math-open-problems@6cda809756c61201f08cdee2dd7e07f20e5d5596`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T203852Z-b18-qform-lit-r12/REPORT.md`.
- Primary marginal-density source: Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), 877--889.
- Recent polynomial-regularity source checked for hypothesis compatibility: Egor Kosov, arXiv:2511.02679 (2025); not transferred to the unrestricted cap-one class because its product-measure regularity hypotheses require extra marginal regularity.
