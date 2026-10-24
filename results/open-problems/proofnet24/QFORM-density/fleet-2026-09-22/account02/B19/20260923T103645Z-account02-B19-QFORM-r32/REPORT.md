SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T10:36:45Z.
attacking: the small-pivot high-star residue — compile strict-N3 pair-minor control into two disjoint original-coordinate star channels, then isolate the coupled leaf-spectrum payment.

# account02/B19 r32 — strict-N3 high-star two-channel compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Fresh owner control:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED`; the full QFORM conjecture remains OPEN.

The target remains: for every finite `n`, every independent real product law whose one-dimensional densities are at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, diagonal-coordinate, Gaussian, or post-rotation independence hypothesis is used below. Continuity is not claimed.

## 1. Incoming proof graph and the exact branch attacked

The newest completed designated-partner material used here is account03/B19's STAR compiler and its subsequent TRIANGLE cross-packet result.

The STAR compiler is source-pinned by brain commit `05553a75e2512c6b818a91f7e0edd4bc51e56267`, with canonical mathematics `yspennstate/math-open-problems@571c69f5a360dbdbadc433db25c03d3157d7e699`. After its light-row-excision/ridge exits, every surviving extreme-coloop/small-pivot STAR state contains an ORIGINAL physical row `h` satisfying

`|A_hh| < 1/64`,

`S_h := sum_(j != h) A_hj^2 > S0 := 123/4096`.                     (1.1)

It supplies square-root small-ball and quarter-Riesz currency but explicitly does not obtain `L^infinity`.

The chronologically later account03/B19 handoff, brain commit `c9154667dc38107286b8789f0e80c366fe94c86e`, canonical mathematics `yspennstate/math-open-problems@63e569420a83b6a9f073c2158e3b5f46214535d7`, pays the complementary TRIANGLE geometry down to a genuine physical two-gradient cross packet

`Delta_T > 0.05145877388595875`,                                     (1.2)

with `2/3` small-ball and half-Riesz estimates, but likewise leaves the coupled third-source `L^infinity` step open. Thus it is useful to sharpen the STAR side rather than repeat TRIANGLE.

The current owner synthesis also retains the strict no-pivot class `N3(tau)`: all physical diagonals and all physical principal `2x2` determinants are small while the actual matrix still has three eigenvalues of modulus at least one. The theorem below addresses the deep no-pivot STAR subbranch at the fixed numerical scale `tau0=1/256`.

## 2. New theorem: a strict-N3 high star forces two disjoint quantitative product channels

### Theorem 2.1 — `QFORM-N3-SMALLPIVOT-STAR-TWOCHANNEL-COMPILER-v1`

Let `A` be a real symmetric `n x n` matrix with at least three eigenvalues of modulus at least one. Assume

`|A_ii| < tau0 = 1/256`                                             (2.1)

for every physical coordinate `i`, and

`|A_ii A_jj - A_ij^2| < tau0`                                      (2.2)

for every distinct physical pair `i,j`. Suppose some physical row `h` satisfies the partner's STAR energy bound (1.1).

Then the complement of `h` can be partitioned into two disjoint ORIGINAL-coordinate banks

`[n] \ {h} = J disjoint_union K`                                   (2.3)

such that

`sum_(j in J) A_hj^2 >= beta0`,

`sum_(k in K) A_hk^2 >= beta0`,                                    (2.4)

where the explicit universal constant is

`beta0 = 1711/131072 = 0.01305389404296875`.                        (2.5)

Consequently, for arbitrary independent cap-one inputs, the two scalar star forms

`L_J = sum_(j in J) A_hj X_j`,

`L_K = sum_(k in K) A_hk X_k`                                      (2.6)

are genuinely independent and each has density cap

`||p_(L_J)||_infinity, ||p_(L_K)||_infinity
   <= sqrt(e/beta0)
   < 14.431`.                                                       (2.7)

In particular their joint density is bounded by

`e/beta0 < 208.236`.                                                (2.8)

Finally the leaf principal block

`B=A[[n]\{h},[n]\{h}]`                                             (2.9)

has at least one eigenvalue of modulus at least one.

### Proof

For each `j != h`, the strict pair determinant condition gives

`A_hj^2
 <= |A_hh A_jj| + |A_hh A_jj - A_hj^2|
 < tau0^2 + tau0
 = 257/65536`.                                                      (2.10)

Write `w_j=A_hj^2`, `S=sum_j w_j=S_h`, and

`M0=257/65536`.                                                     (2.11)

Partition the nonnegative weights greedily: process the coordinates in any order and place the next weight into the currently lighter bin. If the final bin sums are `S_J,S_K`, the usual one-line discrepancy induction gives

`|S_J-S_K| <= max_j w_j < M0`.                                     (2.12)

Therefore

`min(S_J,S_K)
 = (S-|S_J-S_K|)/2
 > (S0-M0)/2
 = (1968-257)/(2*65536)
 = 1711/131072
 = beta0`.                                                         (2.13)

This proves (2.4).

The random variables in (2.6) depend on disjoint sets of the ORIGINAL independent coordinates, so their independence is genuine product provenance; no spectral rotation is being declared independent. The completed weighted projection theorem used in account02/B06 says that a unit scalar projection of a cap-one product vector has density at most `sqrt(e)`. Scaling that theorem by the coefficient norms gives

`||p_(L_J)||_infinity <= sqrt(e)/sqrt(sum_(j in J) A_hj^2)
                        <= sqrt(e/beta0)`,                         (2.14)

and similarly for `L_K`. Product independence gives (2.8).

It remains to prove the leaf-spectrum statement. Let `p` be the number of eigenvalues of `A` at least `1`, and `q` the number at most `-1`. Then `p+q>=3`. Cauchy interlacing for the codimension-one principal block `B` gives at least `max(p-1,0)` eigenvalues of `B` at least `1` and at least `max(q-1,0)` eigenvalues at most `-1`. Since `p+q>=3`,

`max(p-1,0)+max(q-1,0) >= 1`.                                     (2.15)

Thus `B` has at least one eigenvalue of modulus at least one. QED.

### A slightly more flexible threshold

The same proof works whenever `tau+tau^2 <= S0/4`; equivalently

`tau <= tau_* := (sqrt(1+S0)-1)/2 = 0.007451794970...`.             (2.16)

At that coarser threshold it gives the simpler lower bound `S_J,S_K >= 3S0/8`. The fixed choice `1/256` above gives the stronger explicit `beta0` in (2.5).

## 3. What the compiler buys, and what it does not

Writing `x=(x_h,y)` and `c=(A_hj)_(j!=h)`, the exact full form is

`Q = A_hh X_h^2 + 2 X_h (L_J+L_K) + X_{-h}^T B X_{-h}`.            (3.1)

The theorem converts the previous qualitative statement "large star energy" into two quantitatively nondegenerate, mutually independent ORIGINAL-coordinate linear smoothing channels. It also proves that a genuine large spectral direction survives entirely in the leaf block.

This is stronger than selecting one large star edge. In strict `N3(1/256)` every single edge can be tiny, but no survivor of (1.1) can concentrate its entire star energy into one leaf coordinate. The two-channel conclusion is therefore stable under the diffuse strict-N3 stress families that killed local-pivot forcing.

However, (3.1) is not yet an `L^infinity` theorem. The leaf quadratic `X_{-h}^T B X_{-h}` may contain arbitrary self curvature on `J` and `K` and arbitrary cross curvature between them. The two linears `L_J,L_K` are independent, but their critical values are coupled to that same leaf quadratic. The live corrections forbid replacing this by an arbitrary dependent planar density estimate, and forbid deleting a small matrix term as a law-uniform random perturbation. Thus the new theorem pays the structural extraction problem while leaving one analytic coupling problem explicit.

The exact first unpaid STAR implication can now be stated without qualitative words:

### `QFORM-STAR-TWOCHANNEL-LEAFSOURCE-COUPLED-LINFINITY-v1`

Prove a universal `L^infinity` density bound for every quadratic form of the exact shape (3.1) under

`|A_hh| < 1/256`,

`sum_(j in J) A_hj^2 >= beta0`,

`sum_(k in K) A_hk^2 >= beta0`,                                   (3.2)

with `J,K` disjoint original-coordinate banks, cap-one product inputs, and with the leaf block `B` having at least one eigenvalue of modulus at least one, while retaining arbitrary `B_JJ,B_KK,B_JK` and all signs. Equivalently, give a product-preserving descent from this class to an already-paid grouped/ridge/physical-core branch.

The quantifiers in (3.2) are the exact debt. A generic bound depending only on the joint density of `(L_J,L_K)` is not enough: the leaf quadratic is generated by the same coordinates.

## 4. Equation-level application of the newest-Claude package

The required newest-Claude source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its proved unrestricted fifth-volume theorem `D5` says that for any genuine physical cross block `N`,

`||p_Q||_infinity <= 5 sqrt(2e) e_5(N^T N)^(-1/10)`.               (4.1)

Therefore, if any physical cut available before entering the STAR residue satisfies

`s_5(N) >= 1/64`,                                                   (4.2)

then

`e_5(N^T N) >= s_1(N)^2 ... s_5(N)^2 >= 64^(-10)`,                (4.3)

so

`||p_Q||_infinity
 <= 5 sqrt(2e) * 64
 = 320 sqrt(2e)
 = 746.126074111... < 746.127`.                                   (4.4)

Thus the two-channel debt (3.2) only needs attention after all such fifth-cross-direction exits have failed. This is an actual inequality application of the required source, not an assertion that D5 alone exhausts N3.

For context, the newest Claude report also proves the mixed-Fresnel theorem, but its Gram determinant hypothesis cannot simply be inferred from (3.2): the star vector may lie in the same leaf spectral span as the one surviving large direction. I therefore do not use a fictitious automatic mixed-Fresnel exit.

## 5. Corrections preserved

A fresh correction in account02/B01, `QFORM-ARBITRARY-JOINT-INDEFINITE-PLANAR-L2-FALSE-v1`, constructs dependent planar cap-one densities for which the indefinite `xy` output has unbounded `L^2` cost. It blocks forgetting the original-coordinate provenance of the pair `(L_J,L_K)`. The theorem here retains disjoint original-coordinate banks throughout.

The existing matrix-perturbation and no-post-rotation-independence corrections are also respected: no coefficient is discarded and no rotated spectral coordinate is asserted independent.

The previous account02/B19 r31 strict-N3 family remains a valid warning: extreme normalized coloop does not force any quantitative local scalar/pair pivot. That family is paid by an exact grouped square-plus-hyperbola packet. The present theorem identifies a different aggregate currency for the partner's generic high-star survivor: two disjoint star channels plus one unavoidable leaf spectral source.

## 6. Full proof graph status

Within the exact-rank-three/rank-two-cross branch, the current partner graph now has two quantitatively explicit unresolved analytic nodes:

1. TRIANGLE: a physical pair with `Delta_T>0.05145877388595875`, but the genuinely third source must still be coupled to it to reach `L^infinity`.
2. STAR/deep-N3: the new two-channel packet (3.2) plus at least one leaf eigenvalue of modulus at least one, with arbitrary leaf curvature still coupled to those channels.

Other completed scalar/pair, ridge/window, D/D'/D5, physical-core, semidefinite, one-sheet and grouped-coordinate exits remain available at their exact scopes. Arbitrary-extra-spectrum/full-N3 closure remains a separate global debt.

No full-proof claim is made. The unrestricted target is still OPEN, global continuity is still OPEN, and the required two independent end-to-end reviews do not exist.
