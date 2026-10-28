SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T12:41:09Z.
attacking: strengthen the r31 collision-to-plane-hub compiler so the forced hub carries target-scale singular-value weight, then expose the resulting one-index bordered packet without taking fiber suprema.

# account01/B06 r32 — high collision forces one physical index to carry two-sided bordered packet mass

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / TWO-SIDED-PACKET-HUB-COMPILER / FULL_TARGET_OPEN`.

The full arbitrary-dimensional quadratic-form bounded-density conjecture is **not** proved or disproved here. No new global continuity claim is made. The new result strengthens r31's high-collision physical-plane certificate in two ways: the selected transverse singular direction is quantitatively target-scale, and the same original physical coordinate carries a fixed fraction of the full bordered packet on both the left-incidence and right-incidence sides.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval was used, but no authenticated native learned-memory retrieval plus receiver use was established.

## 1. Source boundary and actual partner use


The immediate predecessor is account01/B06 r31,

`yspennstate/math-open-problems@7ca9a0a1ff12547d4791b2ffed064150e85fcad7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T120046Z-account01-B06-QFORM-r31/REPORT.md`.

It introduced the exterior pair-index representation and proved that a high-collision, low-rank bordered packet forces at least one heavy physical two-plane marginal. The present run strengthens that compiler instead of reverting to a physical-minor supremum.

### 1.1 Designated partner account02/B06 actually applied

Two completed account02/B06 results are used as real inequalities.

First, `QFORM-SHARED-COEFFICIENT-MAX-RECIPROCAL-v1`, canonical

`yspennstate/math-open-problems@2fdec7c0b085cb5acf5a09847b293b5bcb296b80`,

states that in the two-hub zero-anchor chamber the full density obeys

`||p_Q||_inf <= 2 sqrt(e/Delta(a,b))`,

where

`Delta(a,b)=sqrt(||a||^2||b||^2-(a.b)^2)`.

Therefore at the r29/r30 area gate

`Delta(a,b) >= s^2/(8 sqrt(2))`,  `s=s_3(A)`,                       (1.1)

the actual full-form inequality is

`boxed: ||p_Q||_inf <= 2 sqrt(e) sqrt(8 sqrt(2))/s
                         < 11.092/s.`                               (1.2)

Thus the packet analysis below is needed only after this explicit partner exit has failed.

Second, the newest completed account02/B06 theorem `QFORM-191-STAR-HUB-INTERNAL-PAYMENT-v1`, canonical

`yspennstate/math-open-problems@328a550b1ddde3d2d9b7c2d245678f0b6fd5e7ae`,

proves in the exact-rank-three high-leverage star-hub branch that

`boxed: either ||p_Q||_inf < 1447/s,
        or ||B_(i,L)||_2 >= s/(16 sqrt(2)) for every heavy i.`       (1.3)

So every failure of that robust-light gate is already paid by the explicit density bound `1447/s`; no unproved transversality of individual light edges is used.

## 2. Pair-index collision notation

Let `E=binom([m],2)` be the set of unordered physical pairs, and let

`D in R^(E x E)`.

Write

`Omega={(R,T): R cap T != empty}`,                                  (2.1)

`W=||D||_F^2`,

`chi=||1_Omega .* D||_F^2/W`,                                      (2.2)

where `W>0`. Let the top-`r` SVD truncation be

`D_r=sum_(k=1)^r sigma_k u_k v_k^T`,                               (2.3)

and define the relative Frobenius tail

`delta=||D-D_r||_F^2/W`.                                           (2.4)

For a unit pair-vector `u_k`, define its physical incidence marginal

`p_(k,i)=sum_(R contains i)|u_k(R)|^2`;                              (2.5)

for `v_k`, define

`q_(k,i)=sum_(T contains i)|v_k(T)|^2`.                              (2.6)

Every pair contains exactly two physical indices, so

`sum_i p_(k,i)=sum_i q_(k,i)=2`,                                   (2.7)

and `0<=p_(k,i),q_(k,i)<=1`.

Put

`eta=(sqrt(chi)-sqrt(delta))_+`.                                    (2.8)

## 3. Main abstract theorem: a collision component has weight and a common physical hub

### Theorem 3.1 — `QFORM-LOWRANK-COLLISION-DOUBLE-PLANE-HUB-v1`

If `eta>0`, then there exist `k<=r` and one **same physical index** `i` such that

`boxed: sigma_k >= (eta/r) sqrt(W),`                                (3.1)

and simultaneously

`boxed: p_(k,i) >= eta^2/(4r^2),
        q_(k,i) >= eta^2/(4r^2).`                                  (3.2)

Thus the collision cannot be explained solely by a tiny singular component or by unrelated left and right physical hubs.

### Proof

For each top singular component set

`c_k=||1_Omega .* (u_k v_k^T)||_F`.                                (3.3)

Restriction to `Omega`, the triangle inequality, and (2.4) give

`sqrt(chi) sqrt(W)
 <= ||1_Omega .* D_r||_F + ||D-D_r||_F
 <= sum_(k<=r) sigma_k c_k + sqrt(delta) sqrt(W)`.

Hence

`sum_(k<=r) sigma_k c_k >= eta sqrt(W)`.                            (3.4)

For some `k`,

`sigma_k c_k >= eta sqrt(W)/r`.                                    (3.5)

Because `c_k<=||u_kv_k^T||_F=1` and `sigma_k<=||D||_F=sqrt(W)`, (3.5) separately implies

`sigma_k >= (eta/r)sqrt(W)`,
`c_k >= eta/r`.                                                     (3.6)

For this component, a union bound over the shared physical index gives

`c_k^2
 =sum_(R,T:R cap T != empty)|u_k(R)|^2|v_k(T)|^2
 <=sum_i p_(k,i)q_(k,i).`                                          (3.7)

Let

`h=max_i min(p_(k,i),q_(k,i))`.

For every `i`,

`p_i q_i = min(p_i,q_i) max(p_i,q_i)
          <= h (p_i+q_i)`.

Using (2.7),

`sum_i p_iq_i <=4h`.                                                (3.8)

Equations (3.6)-(3.8) imply

`h >= c_k^2/4 >= eta^2/(4r^2)`.                                    (3.9)

Choose an index attaining `h`. At that same index both marginals are at least `h`, proving (3.2). QED.

### Difference from r31

R31 proved that some top singular plane had a one-sided physical leverage at least a fixed number. Theorem 3.1 additionally forces:

1. the selected singular value itself to carry a fixed fraction of the packet Frobenius scale;
2. one and the same original physical coordinate to be quantitatively present on **both** the left and right exterior planes.

This extra information is essential for a local product-preserving receiver.

## 4. Exact bordered realization

Return to the r30 bordered packet. Let nonzero `a,b in R^m`, let `C` be arbitrary, and set

`P_a=I-aa^T/||a||^2`, `P_b=I-bb^T/||b||^2`,

`K=P_b C P_a`.                                                       (4.1)

Define contraction maps on `Lambda^2 R^m` by

`J_b(e_i wedge e_j)=b_i e_j-b_j e_i`,                              (4.2)

and similarly `J_a`. The bordered pair-index matrix is

`mathcal D=J_b^T C J_a`.                                            (4.3)

Its entries are the bordered `3 x 3` minors from r30 up to a harmless fixed sign convention, and

`W=||mathcal D||_F^2
  =||a||^2||b||^2||K||_F^2`.                                       (4.4)

The positive singular values of `mathcal D` are `||a||||b||` times those of `K`. If `w_k perp b`, `z_k perp a` are a left/right singular pair of `K`, then the corresponding pair-index singular vectors have exact physical marginals

`p_(k,i)=b_i^2/||b||^2+w_(k,i)^2`,
`q_(k,i)=a_i^2/||a||^2+z_(k,i)^2`.                                (4.5)

This is deterministic exterior algebra only; it does not rotate the random input law.

## 5. New exact identity: one-index bordered packet mass

For a physical coordinate `i`, define the full left-incident and right-incident bordered masses

`W_i^L=sum_(R contains i,T) |mathcal D_(R,T)|^2`,
`W_i^R=sum_(R,T contains i) |mathcal D_(R,T)|^2`.                   (5.1)

### Proposition 5.1 — `QFORM-ONE-INDEX-BORDERED-PACKET-IDENTITY-v1`

One has the exact identities

`boxed:
 W_i^L
 =||a||^2||b||^2 [
      (b_i^2/||b||^2)||K||_F^2 + ||e_i^T K||_2^2 ],`               (5.2)

and

`boxed:
 W_i^R
 =||a||^2||b||^2 [
      (a_i^2/||a||^2)||K||_F^2 + ||K e_i||_2^2 ].`                 (5.3)

### Proof

Take an SVD

`K=sum_l tau_l w_l z_l^T`.

By (4.4)-(4.5), the corresponding singular value of `mathcal D` is `||a||||b|| tau_l`, so

`W_i^L
 =||a||^2||b||^2 sum_l tau_l^2
    [b_i^2/||b||^2+w_(l,i)^2]`.

Now

`sum_l tau_l^2=||K||_F^2`,
`sum_l tau_l^2 w_(l,i)^2=(KK^T)_(ii)=||e_i^T K||_2^2`.

This proves (5.2); (5.3) is identical on the right. QED.

This identity is the aggregate-before-inversion object sought by the B06 assignment: it keeps an entire physical star of curved bordered minors, and it separates that star exactly into coefficient mass plus genuine transverse-curvature row/column energy. There is no fiber supremum and no reciprocal of one minor.

## 6. Collision theorem plus packet identity

Apply Theorem 3.1 to `mathcal D`. Let `tau_k` denote the corresponding singular value of `K`. Equations (3.1), (4.4) give

`tau_k >= (eta/r)||K||_F`.                                         (6.1)

At the common physical index supplied by (3.2), (4.5) gives

`b_i^2/||b||^2+w_(k,i)^2 >= eta^2/(4r^2)`,
`a_i^2/||a||^2+z_(k,i)^2 >= eta^2/(4r^2)`.                         (6.2)

Moreover (5.2) and the singular-vector row lower bound

`||e_i^T K||_2^2 >= tau_k^2 w_(k,i)^2`

give

`W_i^L
 >=||a||^2||b||^2 tau_k^2
    [b_i^2/||b||^2+w_(k,i)^2]`.

Combining (6.1)-(6.2) with (4.4),

`boxed: W_i^L/W >= eta^4/(4r^4).`                                  (6.3)

The right side is identical:

`boxed: W_i^R/W >= eta^4/(4r^4).`                                  (6.4)

Thus **the same physical coordinate carries a fixed fraction of the entire bordered packet on both incidence sides**.

## 7. Concrete r31/r30 constants

Use the exact r31 high-collision/low-tail gates

`chi>=1/2`, `delta<=1/32`, `r=2`.                                  (7.1)

Then

`eta=sqrt(1/2)-sqrt(1/32)=3/(4sqrt(2))`.                            (7.2)

Theorem 3.1 and (6.3)-(6.4) give one singular pair and one physical coordinate `i` satisfying

`boxed: tau_k >= [3/(8sqrt(2))] ||K||_F,`                          (7.3)

`boxed:
 b_i^2/||b||^2+w_(k,i)^2 >=9/512,
 a_i^2/||a||^2+z_(k,i)^2 >=9/512,`                                (7.4)

and

`boxed:
 W_i^L >=(81/65536)W,
 W_i^R >=(81/65536)W.`                                             (7.5)

In the r30 transverse-curvature survivor `||K||_F>s/2`, hence

`boxed: tau_k > 3s/(16sqrt(2)).`                                   (7.6)

There is a further useful same-index four-way alternative. Since each quantity in (7.4) is a sum of two nonnegative squares, on the left either

`|b_i|/||b|| >=3/32`,                                               (7.7a)

or

`|w_(k,i)|>=3/32`, hence
`||e_i^T K||_2 >= tau_k |w_(k,i)|
                >9s/(512sqrt(2)).`                                 (7.7b)

Likewise on the right either

`|a_i|/||a||>=3/32`,                                                (7.8a)

or

`||K e_i||_2>9s/(512sqrt(2)).`                                     (7.8b)

In the specific r30 near-collinear subbranch where `||a||>s/(2sqrt(2))` and `||b||>=s/2`, the coefficient alternatives become actual physical-edge lower bounds

`|a_i|>3s/(64sqrt(2))`,
`|b_i|>=3s/64`,                                                     (7.9)

respectively.

Thus the high-collision/low-tail obstruction has been reduced from an unstructured exterior collision to one original physical coordinate which simultaneously sees both coefficient/curvature planes and carries target-scale bordered mass on both sides.

## 8. What is still unpaid

This does **not** yet imply a universal density bound. In particular:

- `W_i^L` and `W_i^R` are incidence sums, not a single good minor;
- one may not rotate the background to make `w_k,z_k` independent coordinates;
- a large transverse row/column norm can still be diffusely spread over many original coordinates;
- a small matrix tail cannot be discarded as a small random perturbation under unbounded inputs.

The first unpaid implication is now

`QFORM-TWO-SIDED-ONE-INDEX-BORDERED-RECEIVER-v1`:

> Starting from (7.3)-(7.8), keep the distinguished original coordinate `i` explicit. Either expose a product-preserving physical pair / mixed-Fresnel receiver from the coefficient alternatives, or aggregate the target-scale transverse row/column packet before conditioning in the curvature alternatives. The receiver must consume the incidence mass without taking a worst spectral-fiber section or selecting one tiny minor.

A promising next decomposition is to fix `i` on one side of a physical cut and randomly partition only the remaining coordinates. If enough of `W_i^L` avoids reusing the second index of the left pair, the existing volume-sampling theorem receives it. If not, the residual mass is a two-step physical hub centered at `i`, a strictly more local object than the pre-r32 collision packet.

## 9. Quantifier and regularity status

All structural identities above are dimension-free deterministic statements. The density exits (1.2) and (1.3) use only completed product-preserving theorems in their stated scopes. No Gaussian, compact-support, moment, log-concavity, connected-support, or diagonal-basis assumption is inserted. Full QFORM remains **OPEN**. No valid target counterexample is produced. Global continuity remains **OPEN**; the present new compiler is structural rather than a new density-regularity theorem.
