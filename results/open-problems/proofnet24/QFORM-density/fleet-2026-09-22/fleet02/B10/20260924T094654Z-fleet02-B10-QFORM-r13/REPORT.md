# fleet02/B10 r13 — dependent-pair receiver closes the exact-coloop null-hub endpoint

## Status and first unpaid implication

**PROVED SUPPORTING THEOREM / EXACT-COLOOP NULL-HUB CHAMBER CLOSED / RULED-SIDE SOURCE RESULT APPLIED.** Full exact-rank-three QFORM remains OPEN, hence full QFORM remains OPEN.

First unpaid implication: **QFORM-COLOOP-TO-NEARCOLOOP-THIRD-AGGREGATE-GLUING-v1.** In the generic near-coloop endpoint, fleet03/B10's current physical normal form has an additional ORIGINAL-leaf aggregate created by longitudinal leakage. Extend the receiver below from the exact-coloop form

`2 a H L + b L^2 + 2 c L V + d V^2`

to the leakage form with a third same-bank aggregate, without conditioning on that aggregate, without a conditional-density supremum, and without any loss as the leakage tends to zero. The exact-coloop endpoint itself is now paid uniformly before any post-projection independence is asserted.

Control used: owner programme `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.15`. Required source pin: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. Fresh compatible partner handoff read: fleet03/B10 r28, which supplies the endpoint-stable physical hub-partner frame and isolates same-bank transverse contamination as the remaining issue. No refuted conditional-cap/independence premise is used.

## 1. A dependence-safe hyperbolic-square lemma

### Lemma (dependent transverse pair receiver)

Let `H` be independent of `(L,V)`. Assume `H` has a probability density `f_H` with `0 <= f_H <= 1`, while `(L,V)` has a joint probability density `p(l,v)` with

`||p||_infinity <= K`.

For real `a,d != 0` and arbitrary real `b,c`, put

`Q = 2 a H L + b L^2 + 2 c L V + d V^2`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 6 K^(2/3) |a|^(-2/3) |d|^(-1/3).`        (1)

Crucially, **no independence between `L` and `V` is assumed**.

### Proof

Complete the square in the transverse variable:

`d V^2 + 2 c L V + b L^2
 = d (V + (c/d)L)^2 + (b-c^2/d)L^2.`

For each fixed `l`, translation `v -> u=v+(c/d)l` preserves the two-dimensional density cap. Write the translated joint density as `q(l,u)`, still with `q <= K`, and let

`m(l)=int q(l,u) du`

be the density of `L`. Let

`r(l)=(b-c^2/d)l^2`.

For `l != 0`, the contribution of the `L=l` slice to the density at a level `s` is

`A_s(l)=int int f_H(h) q(l,u)
          delta(s-r(l)-2 a l h-d u^2) dh du.`                 (2)

There are two complementary bounds on this same slice.

**Hub bound.** Integrate in `h`. The affine map has Jacobian `2|a l|`; since `f_H <= 1`,

`A_s(l) <= m(l)/(2 |a| |l|).`                                (3)

This is good away from `l=0` and uses the full probability mass normalization through `m`.

**Square bound.** Instead integrate in `u`. For any real `w`,

`int q(l,u) delta(w-d u^2) du
 <= K / sqrt(|d| |w|)`                                       (4)

on the sign-compatible side and is zero on the other side. Indeed, the two roots of `d u^2=w` contribute reciprocal derivatives whose sum is exactly `1/sqrt(|d||w|)`.

For a cap-one probability density `f`, the one-half potential obeys the sharp elementary bathtub estimate

`sup_x int f(h) |h-x|^(-1/2) dh <= 2 sqrt(2).`                (5)

To see (5), rearrange the mass of `f` toward `x`; the extremizer under `0<=f<=1`, `int f=1` is the indicator of an interval of length one centered at `x`, and its integral is `2 sqrt(2)`.

Using (4), then (5), and

`|s-r(l)-2 a l h| = 2 |a l| |h-h_0|`

for the appropriate `h_0`, gives

`A_s(l) <= 2 K / (sqrt(|a d|) sqrt(|l|)).`                    (6)

Now split the `l` integral at an arbitrary `R>0`. On `|l|<=R`, use (6); on `|l|>R`, use (3). Since `int m=1`,

`p_Q(s)
 <= [2K/sqrt(|ad|)] int_{|l|<=R} |l|^(-1/2) dl
    + [1/(2|a|R)] int_{|l|>R} m(l) dl
 <= 8K sqrt(R)/sqrt(|ad|) + 1/(2|a|R).`                       (7)

Minimizing `A sqrt(R)+B/R` gives

`min_{R>0} = 3*2^(-2/3) A^(2/3) B^(1/3)`.

With `A=8K/sqrt(|ad|)` and `B=1/(2|a|)`, all powers simplify to

`p_Q(s) <= 6 K^(2/3) |a|^(-2/3) |d|^(-1/3).`                 (8)

The bound is independent of `b,c,s`. Since `L` has a density, the exceptional slice `l=0` has zero mass; the above conditional/coarea calculation therefore gives the a.e. density and the essential bound. This proves (1).

The mechanism is important: the logarithmic hyperbolic singularity `1/|l|` is used only away from the origin, while near `l=0` the hard square turns it into the integrable `|l|^(-1/2)` singularity. No conditional density of `V` given `L` is introduced.

## 2. Application: exact-coloop null-hub rank three is uniformly bounded

Consider an exact-rank-three target instance

`A = R M R^T`, `R^T R = I_3`,

whose three nonzero eigenvalues all have modulus at least one. Suppose an ORIGINAL physical coordinate, relabelled `0`, is an exact coloop of the spectral frame: its row has norm one. Assume its physical quadratic coefficient vanishes:

`A_00 = 0.`

After an orthogonal change of basis **inside the three-dimensional coefficient bookkeeping only** (not a probabilistic rotation of the source), the coloop row is `e_1`. Parseval then forces every other physical row to have zero first component. Choosing the second basis vector along `M e_1`, write

`M = [[0,s,0],
      [s,b,k],
      [0,k,d]].`                                               (9)

Let `H=X_0`. If the remaining ORIGINAL inputs are `X_i`, define

`L = sum_i y_i X_i`,   `V = sum_i z_i X_i`,                    (10)

where `(y_i,z_i)` are the last two coordinates of the physical spectral-frame rows. Parseval gives

`sum y_i^2 = sum z_i^2 = 1`, `sum y_i z_i=0`.                  (11)

Thus `(L,V)` is an orthogonal two-dimensional linear image of the ORIGINAL product source. No claim that `L` and `V` are independent is made. The original variable `H` is genuinely independent of the entire leaf bank.

The quadratic form is exactly

`Q = 2 s H L + b L^2 + 2 k L V + d V^2.`                     (12)

The spectral hypothesis supplies the two coefficient floors needed by the lemma. Since every singular value of `M` is at least one,

`|s| = ||M e_1|| >= 1.`                                       (13)

Also `M` is invertible and `||M^{-1}||<=1`. The `(3,3)` entry of the inverse is especially simple: using `det M=-s^2 d`,

`(M^{-1})_33 = det[[0,s],[s,b]] / det M = 1/d.`               (14)

Hence

`|d| >= 1.`                                                    (15)

The two-dimensional product-projection theorem used in the pinned ruled-side argument gives

`||p_{L,V}||_infinity <= 2.`                                  (16)

Apply Lemma (1) with `K=2`, `a=s`. From (13)-(16),

`||p_Q||_infinity
 <= 6 * 2^(2/3) |s|^(-2/3) |d|^(-1/3)
 <= 6 * 2^(2/3)
 < 9.525.`                                                     (17)

This proves a universal essential-density bound for the full exact-coloop/null-hub chamber under arbitrary independent cap-one ORIGINAL sources, arbitrary fragmented or unbounded supports, and arbitrary `b,k`. There is no moment, support, log-concavity, continuity, or projected-independence hypothesis.

This is stronger than the earlier one-clean-bank endpoint receivers: the two transverse aggregates may be maximally dependent as a two-dimensional product projection. The proof retains precisely the source provenance that survives legally: `H` is an ORIGINAL coordinate independent of the leaf bank, while `(L,V)` is kept jointly rather than split into fictitiously independent spectral coordinates.

## 3. Required pinned ruled-side result spent on the same geometry

The matrix (9) is indefinite: an invertible symmetric matrix with a zero Rayleigh quotient on `e_1` cannot be positive or negative definite. Thus its signature is either `(2,1)` or `(1,2)`.

At the required source pin `e5f71d79eff325201dd0274053d20268ce65b837`, Theorem C for ruled level sets proves that for signature `(+,+,-)` with eigenvalue moduli at least one,

`p_Q(s) <= pi sqrt(2),   s>=0.`                               (18)

If the signature is `(1,2)`, apply the same theorem to `-Q`, giving the corresponding bound on `s<=0`. Therefore the majority-sign/one-sheet side of (12) is already paid at the sharper universal constant

`pi sqrt(2) < 4.443.`                                         (19)

The new dependent-pair receiver is genuinely used on the remaining side too; (17) is global. Hence this run consumes rather than reproves the ruled theorem and closes the two-sheet side for this exact-coloop endpoint chamber.

## 4. Relation to the current fleet03/B10 endpoint frame

The fresh fleet03/B10 r28 handoff constructs an endpoint-stable physical hub-partner direction and an orthogonal transverse direction in the generic near-coloop collar, while preserving ORIGINAL-coordinate coefficient provenance. It also isolates the remaining difficulty as same-bank transverse contamination rather than collapse of the star coefficient.

At the exact-coloop/null-hub endpoint, the longitudinal leakage is zero and there are only two nontrivial leaf coefficient directions. The r28 physical geometry then reduces to exactly the structure (12): one genuine ORIGINAL hub coupled to one leaf aggregate, plus a hard quadratic direction in the dependent transverse pair. The receiver above shows that **no disjoint-bank extraction and no independence of the leaf aggregates are needed at that endpoint**.

What changes as soon as longitudinal leakage is positive is structural, not merely quantitative. The leaf system acquires a third aggregate sharing the same ORIGINAL variables. The generic normal form has the schematic shape

`Q = 2 a H L + R(L,W,V)`                                      (20)

at the null hub-Rayleigh endpoint, with `W` genuinely present in `R`. Conditioning on `W` is not legal for this purpose because it can destroy the uniform two-dimensional marginal cap of `(L,V)`; the correction ledger contains explicit failures of such conditional-cap shortcuts. Dropping `W` before the quadratic pushforward similarly loses product provenance.

Thus the exact remaining near-coloop question is not whether the `rho=0` limit is singular: (17) shows it is not. It is whether the third same-bank aggregate in (20) can be integrated jointly before any conditional supremum is taken.

## 5. Connection to the r12 curved-complex-section formula

The preceding fleet02/B10 r12 representation treated the harmonic leakage family

`Q_rho = 2(sqrt(1-rho) H + sqrt(rho) Z)L + V^2`,              (21)

where `(Z,L,V)` is an orthonormal ORIGINAL-product projection. It removed a false logarithmic Fourier majorant but left an integrated curved complex-section debt.

At `rho=0`, (21) becomes

`Q_0 = 2 H L + V^2`,                                         (22)

and (17) gives immediately

`||p_{Q_0}||_infinity <= 6*2^(2/3) < 9.525.`                  (23)

So the exact endpoint no longer needs a Fresnel cancellation argument at all. The only unpaid content in (21) is the **shared leaf leakage term** `2 sqrt(rho) Z L`; treating it as a small perturbation is forbidden because the sources have no support or moment bound. Any successful gluing theorem must therefore use the ORIGINAL-product three-aggregate structure uniformly in `rho`, not continuity in coefficient size.

This sharply refines the first unpaid implication to `QFORM-COLOOP-TO-NEARCOLOOP-THIRD-AGGREGATE-GLUING-v1`.

## 6. Scope and status

Proved here:
- the dependence-safe receiver (1);
- the target-valid exact-coloop/null-hub rank-three bound (17), with constant `<9.525`;
- the exact harmonic `rho=0` endpoint as a special case;
- majority-sign levels additionally satisfy the pinned ruled-side bound `<4.443`.

Not proved here:
- the generic positive-leakage near-coloop collar;
- arbitrary exact-rank-three forms without an exact physical coloop;
- the full QFORM theorem;
- continuity of the output density.

No hidden moments, bounded supports, log-concavity, diagonal-basis reduction, fiber supremum, or post-rotation independence is used. The only independence invoked is the genuine ORIGINAL-coordinate independence of the coloop source variable from the remaining ORIGINAL coordinates. The transverse pair is retained jointly and controlled by the valid two-dimensional product-projection density theorem.
