SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T18:47:16Z.
attacking: remove the row-volume marginal gate from the three-volume crossing route by promoting a heavy original row to a genuine hub; retain the whole independent-copy difference and extract the resulting half-Riesz/collision estimate.

# account02/B03 — marginal-free three-volume crossing by heavy-row promotion

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Decoupled time integral / complementary constructions  
**Status:** `NEW SUPPORTING THEOREM / 3-VOLUME ROW-MARGINAL GATE REMOVED / FULL QFORM OPEN`  
**Brain state:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open. This report proves a new analytic compiler for any *actual original-coordinate cross cut* with nonzero three-volume. It does **not** assert that the three-large-eigenvalue hypothesis forces such a cut at universal scale; the previously corrected rank-at-most-two cross-cut families remain outside this theorem.

No moment, support, log-concavity, diagonal-basis, post-rotation-independence, conditional cap, or law-uniform pointwise quadratic Fourier decay is used.

## 1. Fresh sources and exact slices used

1. Pinned source required by the assignment: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` read. I use its proved Theorem D at an actual equation below:

   if `M=A[I,J]`, `Z3=e_3(MM^T)>0`, and the 3-volume row marginals on I are all at most 1/2, then

       |phi_Q(t)| <= min{1,(2pi)^(3/2)e^(3/4) Z3^(-1/4)|t|^(-3/2)},
       ||p_Q||_infty <= 6 sqrt(e) Z3^(-1/6).                         (1.1)

   Same-side quadratic blocks and affine terms are arbitrary.

2. Fresh checked projected-crossing source: `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. I use two proved results exactly in their scopes:

   - grouped projected crossing with arbitrary internal hub function, rank-k hub crossing product S, projected ell-volume Z_ell, row marginals <=1/2, effective dimension d=k+ell;
   - exact-rank-r crossing with arbitrary internal functions on both physical sides and joint projection-density caps.

3. Designated partner account03/B03, latest visible completed report `20260923T181128Z-account03-B03-QFORM-r36/REPORT.md`. I apply its proved effective-dimension Riesz compiler: if

       |phi_Y(t)| <= min{1,K|t|^(-d/2)},

   then for d>1/2

       int_R |t|^(-1/2)|phi_Y(t)|^2 dt <= [8d/(2d-1)] K^(1/d),       (1.2)

   and the exact whole-copy identity is

       int_R |t|^(-1/2)|phi_Y(t)|^2 dt
          = sqrt(2pi) E|Y-Y'|^(-1/2).                                (1.3)

   For d>1 its L2 consequence gives

       P(|Y-Y'|<=eps) <= [2d/(pi(d-1))]K^(2/d) eps.                   (1.4)

No coordinate sum is separated from its conjugate difference in (1.3).

4. Current continuation source `math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`, semidefinite-and-hub-reduction README and the `single_hub_core/REPORT.md`, was read for current hub scope and corrections. The newer arbitrary-rank projected crossing result above is the input that makes the promotion argument below close without an exact-rank-two hypothesis.

## 2. One-hub/two-volume theorem with **no** row-marginal hypothesis

Consider a genuine product-coordinate decomposition

    Q = F(X_H) + 2 W (m.X' + beta) + R(X'),                           (2.1)

where `X_H` and `X'` are independent, `W=U^T X_H` is one orthogonal hub projection with density bounded by `M_H`, `F` is arbitrary measurable, and `R` is an arbitrary quadratic polynomial. Split `X'=(X_I,X_J)`. Let

    r = m_J,      S=||r||_2>0,
    N = (A_R)_{I,J},
    C = N(I-P_r),
    Z2 = e_2(CC^T)>0.                                                  (2.2)

Here `P_r` is orthogonal projection onto span(r). No rank restriction is imposed on C.

### Theorem 2.1 — `QFORM-ONEHUB-Z2-MARGINAL-FREE-v1`

Under (2.1)-(2.2), without any row-volume marginal hypothesis,

    ||p_Q||_infty
      <= C0 M_H^(1/3) S^(-1/3) Z2^(-1/6),                             (2.3)

where

    C0 = 3*2^(7/6)*e^(1/3) = 9.39913188784886... .                     (2.4)

Moreover

    int_R |t|^(-1/2)|phi_Q(t)|^2 dt
      <= R0 M_H^(1/6) S^(-1/6) Z2^(-1/12),                            (2.5)

    R0 = (24/5) 2^(7/12) sqrt(pi) e^(1/6)
       = 15.0591139025981... ,                                        (2.6)

and for an independent copy Q'

    P(|Q-Q'|<=eps)
      <= C0 M_H^(1/3) S^(-1/3) Z2^(-1/6) eps.                          (2.7)

The density is continuous on this branch because every case below has an integrable `|t|^(-3/2)` envelope.

### Proof

Write the rows of C as `c_i`. Let

    w_{ij} = area(c_i,c_j)^2/Z2,
    alpha_i = sum_{j!=i} w_{ij}.                                      (2.8)

#### Case A: all `alpha_i<=1/2`

Apply the fresh grouped projected-crossing theorem with `(k,ell,d)=(1,2,3)`. Its envelope is

    |phi_Q(t)| <= min{1,K_A |t|^(-3/2)},                              (2.9)

    K_A = M_H^(1/2) 2^(7/4) pi^(3/2)e^(1/2)
          S^(-1/2) Z2^(-1/4).                                        (2.10)

Direct inversion gives exactly (2.3) with C0. Applying partner equation (1.2) with d=3 gives (2.5), and (1.4) gives (2.7).

#### Case B: some `alpha_i>1/2`, but the next one-volume is spread

Promote the *original coordinate* `X_i` from I into the hub bank. This is product-preserving: `(W,X_i)` is independent of the remaining light coordinates and has joint density at most `M_H`.

Because `c_i` is orthogonal to r, write for each `j!=i`

    d_j = P_{c_i^perp} c_j,
    F_i^2 = sum_{j!=i} ||d_j||^2.                                     (2.11)

The exact exterior-area identity is

    alpha_i Z2
      = sum_{j!=i} area(c_i,c_j)^2
      = ||c_i||^2 F_i^2.                                              (2.12)

The promoted two-row hub-to-J block has row span `span(r,c_i)` and product of its two nonzero singular values

    S_i = S ||c_i||.                                                   (2.13)

After projection off that row span, the remaining I-to-J rows are precisely the d_j, so the projected one-volume is

    Z1 = F_i^2.                                                        (2.14)

If every one-volume marginal satisfies `||d_j||^2/F_i^2<=1/2`, the fresh theorem with `(k,ell,d)=(2,1,3)` applies. The ell=1 exponential factor is absent. Its density coefficient is

    3*2^(5/6) M_H^(1/3)
       S^(-1/3)(||c_i||^2F_i^2)^(-1/6)
      < 6 M_H^(1/3) S^(-1/3) Z2^(-1/6),                              (2.15)

using (2.12) and `alpha_i>1/2`. This is smaller than C0. The partner Riesz and collision constants are also smaller than (2.5)-(2.7): after (2.12) the Riesz outer coefficient is at most `(24/5)sqrt(2pi)`.

#### Case C: a second heavy row

Suppose some j satisfies

    ||d_j||^2 > F_i^2/2.                                              (2.16)

Promote the genuine original coordinate X_j too and condition every still-unpromoted I-coordinate. The literal hub-to-J three-row block has rows `r,n_i,n_j`, where n_i,n_j are the corresponding rows of N. Row operations removing components parallel to r and then to c_i show that the product P3 of its three nonzero singular values is exactly

    P3 = S ||c_i|| ||d_j||.                                           (2.17)

By (2.12) and (2.16),

    P3 > S sqrt(Z2)/2.                                                 (2.18)

The three-dimensional hub projection is an orthogonal transform of `(W,X_i,X_j)`, whose joint density is at most `M_H`; no independence is asserted after that transform. The J-side orthogonal three-projection has density at most `2^(3/2)` by the product-projection theorem. The exact-rank-three crossing theorem therefore gives

    ||p_Q||_infty
      <= 3(2^(3/2)M_H/P3)^(1/3)
      < 3*2^(5/6) M_H^(1/3)S^(-1/3)Z2^(-1/6),                        (2.19)

again below C0. Its d=3 envelope inserted in partner (1.2)-(1.4) is also below (2.5)-(2.7).

The three cases are exhaustive. QED.

## 3. Main theorem: arbitrary physical three-volume, no leverage/marginal gate

Let I,J be any disjoint sets of original coordinates and condition every coordinate outside `I union J`. Put

    M=A[I,J],
    Z3=e_3(MM^T)
      = sum_{|S|=|T|=3} det(M_{S,T})^2.                               (3.1)

### Theorem 3.1 — `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`

If `Z3>0`, then for arbitrary same-side quadratic blocks, arbitrary additional spectrum and arbitrary affine terms,

    boxed:
    ||p_Q||_infty <= C3 Z3^(-1/6),                                    (3.2)

with

    C3 = 3*2^(4/3)*e^(1/3)
       = 10.5501688311648... .                                        (3.3)

Equivalently, every interval B obeys the **linear** one-copy small-ball estimate

    P(Q in B) <= C3 Z3^(-1/6) |B|.                                   (3.4)

The whole-copy decoupled-time estimates are

    boxed:
    int_R |t|^(-1/2)|phi_Q(t)|^2 dt
      <= R3 Z3^(-1/12),                                               (3.5)

    R3 = (24/5)2^(2/3)sqrt(pi)e^(1/6)
       = 15.9545754135557... ,                                        (3.6)

and, by (1.3),

    boxed:
    E|Q-Q'|^(-1/2)
      <= (24/5)(2e)^(1/6) Z3^(-1/12)
      = 6.36495469832054... Z3^(-1/12).                               (3.7)

Also

    boxed:
    P(|Q-Q'|<=eps) <= C3 Z3^(-1/6) eps.                               (3.8)

No sum/difference independence is used anywhere in (3.5)-(3.8).

### Proof

Give the 3-row subsets the volume weights

    w_S = det(M_S M_S^T)/Z3,
    alpha_i = sum_{S containing i} w_S.                               (3.9)

(Equivalently, expand over the column triples as in Cauchy-Binet.)

If every `alpha_i<=1/2`, apply the pinned e5 Theorem D exactly as (1.1). Its density coefficient is `6sqrt(e)=9.8923276242...<C3`. Partner (1.2) gives

    int |t|^(-1/2)|phi|^2
      <= (24/5)sqrt(2pi)e^(1/4) Z3^(-1/12)
      =15.4491571911... Z3^(-1/12)<R3 Z3^(-1/12),                     (3.10)

and (1.4) gives the collision coefficient `6sqrt(e)<C3`.

Otherwise choose an original row i with `alpha_i>1/2`. Let `m=M_i`, `S=||m||`, and

    C=M_{I\{i},J}(I-P_m).                                             (3.11)

Every 3-volume containing row i is `S^2` times the corresponding projected 2-volume. Summing gives the exact identity

    S^2 e_2(CC^T) = alpha_i Z3 > Z3/2.                                (3.12)

Now regard X_i as a genuine one-dimensional hub. Its density cap is one. Theorem 2.1 yields

    ||p_Q||_infty
      <= C0 (alpha_i Z3)^(-1/6)
      < C0 2^(1/6) Z3^(-1/6)
      = C3 Z3^(-1/6),                                                 (3.13)

which proves (3.2). Likewise (2.5) and (3.12) give

    int |t|^(-1/2)|phi|^2
      <= R0 2^(1/12) Z3^(-1/12)
      =R3 Z3^(-1/12),                                                 (3.14)

and (2.7) gives (3.8). Equation (3.7) is (3.5) divided by sqrt(2pi).

Conditioning the coordinates outside `I union J` only produces affine terms, and every source estimate used above is uniform in them. QED.

## 4. Concrete stress family: D/D' gate fails, exact-rank-all-directions degrades, Z3 theorem stays uniform

Let q be a Hadamard order and choose four orthonormal flat vectors `v_1,...,v_4 in R^q`, so every coordinate has modulus `q^(-1/2)`. For `0<eps<1`, let B_eps be the `4 x q` matrix with rows

    v_1, v_2, v_3, eps v_4,                                          (4.1)

and form the symmetric bipartite matrix

    A_eps = [[0,B_eps],[B_eps^T,0]].                                  (4.2)

Its nonzero eigenvalues are

    +1,-1,+1,-1,+1,-1,+eps,-eps,                                    (4.3)

so it is an exact owner-target family with at least three eigenvalues of modulus at least one. Every physical diagonal is zero and every physical `2 x 2` principal determinant has modulus at most `1/q`; hence for large q it lies in any fixed small-pivot regime.

For the natural physical cut, the squared singular values of B_eps are `1,1,1,eps^2`, hence

    Z3 = e_3(B_eps B_eps^T)=1+3eps^2.                                 (4.4)

The three strong-row 3-volume marginals are

    alpha_strong=(1+2eps^2)/(1+3eps^2)>3/4    (eps<1),                (4.5)

so both the pinned Theorem D threshold 1/2 and its D' threshold `h<3/4` are blocked on this cut. D5 is unavailable because the cross rank is four. The exact-rank-four crossing bound carries the product of all four singular values and therefore deteriorates like a negative power of eps.

Theorem 3.1 instead gives, uniformly in q and eps,

    boxed:
    ||p_{X^T A_eps X}||_infty
       <= C3 (1+3eps^2)^(-1/6)
       <= 10.5501688312,                                               (4.6)

for **every** independent cap-one product input. Thus the marginal-free theorem is stable as the fourth crossing singular value tends to zero. This example is an obstruction to using the old D/D' row-marginal gate as an exhaustive analytic receiver; it is not a QFORM counterexample.

For comparison only, other hub theorems can also pay special members of this deliberately simple family. No exclusivity claim is made for (4.6).

## 5. What this pays, and what remains genuinely unpaid

The analytic high-cross-rank obligation is now sharper:

> For any actual original-coordinate cut with `e_3(A[I,J]^T A[I,J])` bounded below, no leverage or volume-row marginal verification is needed. The output density and the whole-copy half-Riesz integral are universally controlled by (3.2) and (3.5).

Hence all remaining difficulty lies in the structural/low-cross-volume regime. The first unpaid implication for this slot is now:

    from s_3(A)>=1 in the no-pivot/hub survivor, either produce a physical cut with Z3 >= c>0,
    or reduce product-preservingly to one of the already-paid genuinely rank<=2 / grouped-hub / ridge / exact-coloop / square-plus-critical-crossing mechanisms.                    (5.1)

The existing correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` prevents replacing (5.1) by a claim that every target matrix has a universal rank-three cut: the family `[1] direct_sum J_m/m direct_sum (-J_m/m)` has every cross cut of rank at most two. Thus Theorem 3.1 removes an analytic gate but does not erase the known structural obstruction.

The current Claude `(SP)` conditional-adaptation proposal remains open and was not used. The arbitrary-joint coarea claim, conditional projection-cap shortcuts, post-rotation independence, and pointwise quadratic-decay claims remain excluded.

## 6. Provenance and continuity scope

All promotions are promotions of **genuine original coordinates**. Orthogonal rotations appear only inside already-proved projection-density estimates or singular-value identities; no rotated coordinates are declared independent. In the exact-rank-three terminal branch, the left singular projection is an orthogonal transform of the joint vector `(W,X_i,X_j)`, whose *joint density* is bounded by `M_H`; this is rotation-invariant as a joint L-infinity statement and does not assert coordinate independence.

Every branch has an integrable `|t|^(-3/2)` characteristic-function envelope, so Theorem 3.1 actually gives a continuous `C_0` density on its stated cross-volume branch. This does not settle unrestricted continuity because the full QFORM conjecture is still open in the low-cross-volume survivors.
