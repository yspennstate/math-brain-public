SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T01:35:00Z.
attacking: Q0 fixed bi-anchor receiver: turn determinant-weighted disjoint third-minor mass through two fixed original-coordinate anchors into either a genuinely bounded physical spectral core or a finite-depth conditional-diffuse collar, without asserting one good minor from aggregate mass.

# account02/B07 — two-level determinant concentration closes the bounded physical-core branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T013500Z-account02-B07-QFORM-636525`  
**Status:** `ESSENTIAL_STEP_APPLIED / BOUNDED-CORE BRANCH PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The target is the unrestricted statement: for arbitrary independent real original-coordinate inputs with marginal probability densities bounded by one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or produce a valid target counterexample. No moments, bounded support, log-concavity, iid assumption, spectral-coordinate independence, or continuity assumption is used below. Continuity is separate.

Fresh owner control is revision `2026-09-22.15`; QFORM is the sole research target. I retain the live corrections, especially:

- no law-uniform pointwise quadratic-phase decay;
- no independence after spectral rotation;
- no arbitrary-joint 3D coarea cap;
- no universal bounded-cardinality core extracted merely from global third-compound mass;
- `QFORM-ANCHOR-PACKET-ONE-LOCAL-MINOR-FALSE-v1`: a constant anchor packet does **not** by itself force one large local physical minor.

The result below does not contradict the last correction. It selects a single physical minor only after **two additional quantitative concentration tests** show that at least `1/9` of an already anchored determinant-weighted packet is carried by that exact minor. If either concentration test fails, the determinant mass is retained as a diffuse packet rather than inverted.

## 2. Sources actually used

1. Newest required Claude source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Its Theorem D and D' give an original-coordinate determinant-volume Fourier receiver. For a 3-minor weight with row marginals at most `h<3/4`,

   `||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) K^(-1/6)`,

   where `K=exp(E log det^2 + H)`; for normalized squared-minor weights on a packet of total mass `P`, `K=P` exactly. All self blocks, outside couplings and affine terms remain arbitrary.

2. Finite-dimensional spectral receiver: `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1. On `m` independent cap-one original coordinates, if the actual symmetric quadratic matrix has three eigenvalues of modulus at least `sigma`, then uniformly over arbitrary affine terms

   `||p_q||_infinity <= 2 sqrt(6 pi m)/sigma`.

3. Designated partner account03/B07 r21: `yspennstate/math-open-problems@ab1c4ce8b0b7ef940e057001a6936389b9a55b23`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T004111Z-account03-B07-qform-r21/REPORT.md`. In the current O0/no-pivot branch it has an actual physical cross block

   `B=[[b,r^T],[c,D]]`

   and a fixed physical anchor row `i` and anchor column `a` such that the squared mass of anchored `3x3` minors is

   `Z = sum_{|J|=|K|=2} det B[{i} union J,{a} union K]^2 > 1/768`.       (2.1)

   Its transverse deshearing theorem then refines the sibling `E2(D)<=1/48` branch to four genuinely disjoint physical banks. I use the stronger incoming anchored mass (2.1) itself here.

The current no-pivot reduction uses `tau=1/128`: every physical diagonal has magnitude `<tau` and every physical principal `2x2` determinant has magnitude `<tau`.

## 3. The first unpaid implication, attacked immediately

Previous B07 work reduced the q=0 determinant bank either to a D'-paid diffuse packet or to fixed row/column anchors carrying constant third-minor mass. Partner r21 strengthens the latter to (2.1). The precise remaining finite-core question is:

> When does the anchored packet itself force a **bounded physical coordinate core**, without falsely asserting that aggregate mass always contains a universal atom?

There is an exact two-level answer.

## 4. Two-level concentration lemma for an anchored 3-minor packet

Normalize the anchored packet (2.1):

`w(J,K) = det B[{i} union J,{a} union K]^2 / Z`,

where `J` is a residual physical row pair and `K` is a residual physical column pair. Define first-level inclusion marginals

`alpha_j = P_w(j in J)`,       `beta_p = P_w(p in K)`.

Both marginal sums equal two.

Fix a threshold `h in (1/2,1)`. Say the packet is **level-0 row diffuse** if `max_j alpha_j<=h`, and analogously on the column side.

If neither side is level-0 diffuse, choose `j,p` with

`alpha_j>h`, `beta_p>h`.

Then by the union bound in the same determinant law,

`P_w(j in J, p in K) > 2h-1`.                                      (4.1)

Condition on that joint event. Since `J` and `K` are pairs, there is now one remaining row coordinate and one remaining column coordinate. Let

`gamma_k = P_w(k in J\{j} | j in J,p in K)`,
`delta_q = P_w(q in K\{p} | j in J,p in K)`.

These are probability distributions (their sums are one). Call the conditional packet **level-1 row diffuse** if `max_k gamma_k<=h`, and similarly on the column side.

### Theorem 4.1 — `QFORM-BIANCHOR-TWOLEVEL-CORE-v1`

For every anchored packet of mass `Z>0` and every `h>1/2`, exactly one of the following structural outcomes occurs:

1. one side is level-0 diffuse;
2. after choosing first-level heavy `j,p` as above, one side is level-1 diffuse;
3. there is an actual physical anchored `3x3` minor with

   `|det B[S,T]|^2 > (2h-1)^2 Z`.                                 (4.2)

#### Proof

If neither level-0 diffuse alternative holds, (4.1) supplies a joint first-level event of probability `>2h-1`. If neither level-1 diffuse alternative holds, choose `k,q` with `gamma_k>h`, `delta_q>h`. Conditional on the first event,

`P_w(k in J\{j}, q in K\{p} | j in J,p in K) > 2h-1`.             (4.3)

Multiplying (4.1) and (4.3), the exact atom

`J={j,k}`, `K={p,q}`

has `w`-mass `>(2h-1)^2`. Multiplication by `Z` gives (4.2). QED.

This is deliberately **not** a universal single-minor extraction. A diffuse branch is preserved whenever either concentration test fails.

For the convenient threshold `h=2/3`, the concentration price is only

`(2h-1)^2 = 1/9`.                                             (4.4)

## 5. Deep concentration produces an actual six-coordinate spectral core

Assume now the current no-pivot class `N3(tau)` and structural outcome 3 of Theorem 4.1. Let `S,T` be the resulting disjoint physical triples and `H=S union T`, so `|H|=6`.

The no-pivot inequalities give, for distinct physical coordinates `u,v`,

`A_uv^2 <= |A_uu A_vv| + |det A[{u,v},{u,v}]| < tau^2+tau`.     (5.1)

Put

`eta_tau = sqrt(tau+tau^2)`.

Every entry of the cross submatrix `C=A[S,T]` therefore has magnitude `<eta_tau`, so

`||C||_op <= ||C||_F < 3 eta_tau`.                               (5.2)

Let its singular values be `s1>=s2>=s3`. From (4.2),

`s1 s2 s3 = |det C| > (2h-1) sqrt(Z)`.

Together with (5.2),

`boxed: s3(C) > (2h-1) sqrt(Z) / [9(tau+tau^2)].`                (5.3)

Since `C` is a row/column compression of the symmetric six-coordinate principal block `A_HH`, singular-value contraction gives

`s3(A_HH) >= s3(C)`.                                             (5.4)

Because `A_HH` is symmetric, its singular values are the absolute values of its eigenvalues. Thus `A_HH` has **three actual eigenvalues** of modulus at least

`sigma_core := (2h-1) sqrt(Z) / [9(tau+tau^2)].`                 (5.5)

Condition on all original coordinates outside `H`. The six remaining inputs retain independence and their density caps, while the outside variables create only deterministic affine terms. The finite-dimensional spectral receiver therefore gives

`boxed:
 ||p_Q||_infinity
 <= 12 sqrt(pi)/sigma_core
 = 108 sqrt(pi)(tau+tau^2)/[(2h-1)sqrt(Z)].
`                                                                      (5.6)

This is a genuine full-form density bound: every coefficient outside the six-coordinate core is retained through conditioning.

### Current numerical constants

Use the partner mass `Z>1/768`, the current `tau=1/128`, and `h=2/3`. Then

`|det C| > 1/(48 sqrt(3))`,                                      (5.7)

`sigma_core > 1024/(3483 sqrt(3)) = 0.1697406476...`,            (5.8)

and

`boxed: ||p_Q||_infinity < (10449/256) sqrt(3 pi)
                              = 125.3055559141... .}`             (5.9)

Hence the **doubly concentrated anchored O0 branch is completely paid** by an actual six-coordinate spectral core.

## 6. Required newest-Claude theorem applied to the live proof tree

The e5 determinant-volume theorem is used at a real inequality before the anchored branch is entered. The preceding q=0 packet has total squared-minor mass `P>=1/5184`. If either orientation has all natural packet marginals at most `2/3`, D' at `h=2/3` gives

`||p_Q||_infinity
 <= 9 sqrt(3e) P^(-1/6)
 <= 106.921... .`                                                (6.1)

Thus the current q=0 proof tree is now:

- **global determinant-volume diffuse:** paid by e5 D', (6.1);
- **global high-leverage:** fixed row/column anchors are extracted without selecting a minor;
- **anchored packet doubly concentrated:** paid by the six-coordinate core, (5.9);
- **anchored packet not doubly concentrated:** retained as one of the conditional-diffuse collars from Theorem 4.1.

The step from aggregate volume to one local minor therefore occurs only at the terminal leaf where determinant weight has already concentrated twice by a fixed universal factor.

## 7. Integration with the designated partner r21 packet

Partner r21 additionally proves, in the sibling `E2(D)<=1/48` branch,

`||c_L|| ||r_R|| ||D[L',R']||_F > 1/(256 sqrt(3))`

on four genuinely disjoint original-coordinate banks. This remains useful in the **conditional-diffuse collars**: failure of the six-coordinate terminal leaf does not erase the star-star-transverse-core reserve. The two pieces of information now coexist:

1. determinant weight has not concentrated enough to justify reciprocal local extraction;
2. a product-provenance-friendly four-bank transverse reserve is still present.

That is a materially narrower and safer analytic target than the former unrestricted bi-anchor packet.

## 8. What remains unpaid

The first unpaid implication is now

**`QFORM-BIANCHOR-CONDITIONAL-DIFFUSE-PAYMENT-v1`.** In the partner anchored packet `Z>1/768`, assume outcome 1 or 2 of Theorem 4.1 at `h=2/3`. Pay that determinant mass while retaining the fixed anchor(s), the four-bank transverse reserve from r21 when in the low-`E2` branch, and arbitrary same-side quadratic curvature. A valid endpoint may be a variable-order minor/Fourier law, a mixed-hub theorem, a pair/zero-pivot receiver, or a low-tail certificate. Do not replace the conditional diffuse packet by one reciprocal residual cofactor.

The sibling `E2(D)>1/48` branch and its current low-rank/nested-packet analysis remain separate. Full QFORM is `OPEN / NOT PROVED / NOT DISPROVED`; unrestricted continuity is also open.

## 9. Sanity checks

The quantitative chain is elementary:

- `sqrt(1/768)=1/(16sqrt(3))`;
- two concentration steps at `h=2/3` retain more than `1/9` of squared determinant mass, so `|det C|>1/(48sqrt(3))`;
- `tau+tau^2=129/16384`;
- dividing by `9(tau+tau^2)` gives `sigma_core>1024/(3483sqrt(3))`;
- the six-dimensional projected-gradient cap is `12sqrt(pi)/sigma_core=(10449/256)sqrt(3pi)=125.3055559141...`.

No numerical experiment is used as a premise.
