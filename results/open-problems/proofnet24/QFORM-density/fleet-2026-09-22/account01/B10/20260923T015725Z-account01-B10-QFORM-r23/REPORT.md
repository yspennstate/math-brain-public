SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T01:57:25Z.
attacking: singleton-heavy-hub exact-null endpoint: orient the transverse bank packet by the actual hub-coupling direction and force a scale-free hyperbolic-square curvature product before any local-minor inversion.

# account01/B10 r23 — N-oriented transverse bank split at an exact null hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: arbitrary exact-rank-three coupled case  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMA / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full exact-rank-three theorem is **not** proved here. The contribution is a new exact structural lemma for the singleton-heavy-hub/two-bank state left by the designated account02/B10 reduction. It aligns the two-bank exterior packet with the *actual spectral coupling direction* `P_{e1^perp} N e1` and converts the packet into the precise coefficient product occurring in the dependence-tolerant hyperbolic-square estimate. The remaining gap is no longer a coefficient-size problem: it is a product-provenance theorem for the same-bank nuisance projections.

## 1. Fresh source state and correction discipline

Fresh control before publication was read from `yspennstate/math-research-brain@87630581e34d4781b33a6dee2acc47c5cd154f64`; OWNER CONTROL revision is `2026-09-22.15`, QFORM is the sole research target, and there is no later stop for B10.

The live `CURRENT_RESEARCH.md` and `CORRECTION_INBOX.json` were enforced. In particular, this report does **not** use:

- the false arbitrary-joint rank-three coarea bound;
- the false positive conditional projection-height moment bound;
- law-uniform pointwise van-der-Corput/Fresnel decay;
- post-rotation independence;
- an unrestricted fiber supremum;
- a uniformly good single physical minor.

The exact target remains the original product-law statement for arbitrary independent cap-one coordinate densities.

## 2. Designated partner theorem actually used

The designated partner is account02/B10 run

`20260922T225540Z-account02-B10-QFORM-auto11`,

canonical source

`yspennstate/math-open-problems@9005415f079b7b46c0618c0187bf29b3f8d44167`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T225540Z-account02-B10-QFORM-auto11/REPORT.md`.

Its `QFORM-TRIPARTITE-HEAVY-HUB-DELETE-OR-ISOLATE-v1` reduces the near-unit heavy-hub alternative to an active original-coordinate set

`{h} union B2 union B3`

with normalized spectral rows `r_i in R^3`, a symmetric invertible spectral matrix `N`, and

`sum_i r_i r_i^T = I_3`,

`|det N| >= 2^(-18)`, `sigma_min(N) >= 2^(-18)`,

`L:=||r_h||^2 > 511/512`,

`T_h:=sum_(j in B2,k in B3) det(r_h,r_j,r_k)^2 >= 1/512`.      (2.1)

The variables remain the original independent physical coordinates; the whitening is deterministic coefficient geometry only.

My preceding B10 r21 proved the exact transverse identity

`T_h = L tr(adj(S2) S3) = L(1-det S2-det S3)`,                 (2.2)

where, after rotating only the deterministic spectral basis so that

`r_h=sqrt(L)e1`,

we write `r_i=a_i e1+w_i`, `w_i in e1^perp`, and

`S2=sum_(j in B2) w_j w_j^T`, `S3=sum_(k in B3) w_k w_k^T`,

so `S2+S3=I_2`.

The new point is to resolve (2.2) in the basis forced by `N`, rather than an eigenbasis of `S2`.

## 3. N-oriented transverse split lemma

### Lemma 3.1 — `QFORM-HUB-N-ORIENTED-TRANSVERSE-SPLIT-v1`

Let `S` be a real `2x2` matrix with

`0 <= S <= I_2`

in the PSD order, and put `K=I_2-S`. For **every** orthonormal basis `(e2,e3)`, set

`alpha=e2^T S e2`, `beta=e3^T S e3`, `gamma=e2^T S e3`.

Then

`tr(adj(S) K)
 = alpha(1-beta)+(1-alpha)beta+2 gamma^2`,                       (3.1)

and

`alpha(1-beta)+(1-alpha)beta >= (1/2) tr(adj(S)K)`.              (3.2)

Consequently at least one of

`alpha(1-beta)`, `(1-alpha)beta`

is at least

`(1/4) tr(adj(S)K)`.                                              (3.3)

#### Proof

In the chosen basis,

`S=[[alpha,gamma],[gamma,beta]]`,

`K=[[1-alpha,-gamma],[-gamma,1-beta]]`.

Direct multiplication gives (3.1). Since `S>=0` and `K>=0`,

`gamma^2 <= alpha beta`,

`gamma^2 <= (1-alpha)(1-beta)`.                                  (3.4)

Therefore

`gamma^2 <= sqrt(alpha beta(1-alpha)(1-beta))`.                   (3.5)

On the other hand, AM-GM gives

`alpha(1-beta)+(1-alpha)beta
 >= 2 sqrt(alpha beta(1-alpha)(1-beta))
 >= 2 gamma^2`.                                                   (3.6)

Thus the first two terms in (3.1) are at least the last term, proving (3.2). Since they are nonnegative, one is at least half their sum, proving (3.3). QED.

The constant `1/4` in (3.3) is sharp at the level of this argument: equality in (3.2) is approached by a rank-one projection `S` whose diagonal entries are both `1/2` in the chosen basis.

## 4. Apply the lemma in the actual hub-coupling basis

Now assume the surviving hub is **exactly null** for the active spectral matrix:

`e1^T N e1 = 0`.                                                     (4.1)

Because `N` is invertible, put

`R=||P_(e1^perp) N e1||=||N e1||>0`,

choose

`e2=P_(e1^perp)Ne1/R`,

and let `e3` be the orthogonal transverse direction. In the spectral basis `(e1,e2,e3)`, symmetry gives

`N=[[0,R,0],[R,p,q],[0,q,d]]`.                                      (4.2)

Hence

`det N = -R^2 d`,                                                    (4.3)

so in particular

`R^2 |d| = |det N|.                                                  (4.4)

This is the key reason to orient by `N e1`: the hyperbolic coupling and the surviving square curvature multiply exactly to the full determinant.

Apply Lemma 3.1 with `S=S2`, `K=S3` in this **N-oriented** transverse basis. Define coefficient vectors

`y_2=(<w_j,e2>)_(j in B2)`, `z_2=(<w_j,e3>)_(j in B2)`,

`y_3=(<w_k,e2>)_(k in B3)`, `z_3=(<w_k,e3>)_(k in B3)`.

Then

`||y_2||^2=alpha`, `||z_2||^2=beta`,

`||y_3||^2=1-alpha`, `||z_3||^2=1-beta`.

Using (2.2), Lemma 3.1 yields the dichotomy

`||y_2||^2 ||z_3||^2 >= T_h/(4L)`                                   (4.5a)

or

`||y_3||^2 ||z_2||^2 >= T_h/(4L)`.                                  (4.5b)

Thus, **for the actual hub-coupling direction `e2` and the actual determinant-paying curvature direction `e3`, two disjoint original-coordinate banks carry a fixed opposite-bank product of coefficient energies.** No coordinate selection or reciprocal local minor is used.

## 5. Exact hyperbolic-square coefficient packet

Choose the bank assignment `(BY,BZ)` according to whichever of (4.5a)--(4.5b) holds, and put

`sigma_Y^2 = sum_(i in BY) <w_i,e2>^2`,

`sigma_Z^2 = sum_(i in BZ) <w_i,e3>^2`.

Then

`L sigma_Y^2 sigma_Z^2 >= T_h/4`.                                   (5.1)

The three coefficient scales that would enter a normalized hyperbolic-square smoother are:

- hub/hyperbolic coefficient `R sqrt(L) sigma_Y`;
- transverse square coefficient `d sigma_Z^2`;
- the two scalar bank projections supported on disjoint original-coordinate banks.

Combining (4.4) and (5.1) gives the exact scale-free identity/inequality

`(R sqrt(L) sigma_Y)^2 |d| sigma_Z^2
 = |det N| L sigma_Y^2 sigma_Z^2
 >= |det N| T_h/4`.                                                  (5.2)

Now apply the designated partner's actual quantitative bounds (2.1):

`|det N| >= 2^(-18)`, `T_h>=2^(-9)`.

Therefore

`boxed{(R sqrt(L) sigma_Y)^2 |d| sigma_Z^2 >= 2^(-29).}`             (5.3)

This is `QFORM-NULL-HUB-HYPERBOLIC-CURVATURE-PACKET-v1`.

Equation (5.3) is the concrete application of the assigned account02/B10 result in this run. It has exactly the homogeneity of the completed dependence-tolerant hyperbolic-square theorem

`||p||_infinity <= 3*2^(2/3) H^(2/3) |a|^(-2/3)|b|^(-1/3)`,

because the latter depends on `(a^2 |b|)^(-1/3)`.

## 6. Product provenance of the two selected scalar bank directions

Define the normalized scalar linear forms

`Y_* = sigma_Y^(-1) sum_(i in BY)<w_i,e2>X_i`,

`Z_* = sigma_Z^(-1) sum_(i in BZ)<w_i,e3>X_i`.                      (6.1)

Their coefficient vectors have Euclidean norm one and are supported on disjoint original-coordinate banks. Therefore:

1. `Y_*` and `Z_*` are genuinely independent;
2. each is a normalized original-product linear form;
3. the completed weighted affine-fiber Brascamp--Lieb projection theorem gives

`||p_(Y_*)||_infinity, ||p_(Z_*)||_infinity <= exp(1/2)`.             (6.2)

The hub coordinate `X_h` is also genuinely independent of both banks and has density cap one.

Thus the coefficient-size and scalar-product-provenance pieces needed for a hyperbolic-square payment are simultaneously present. What is **not** yet justified is discarding the other spectral projections carried by `BY` and `BZ`.

## 7. Why (5.3) does not by itself finish the branch

Writing the residual aggregate spectral coordinate as

`W=(A,Y,Z)` in the basis `(e1,e2,e3)`, the null-hub form is

`Q = 2R( sqrt(L) X_h + A )Y + pY^2+2qYZ+dZ^2`.                       (7.1)

The longitudinal leakage `A` is coefficient-orthogonal to the total transverse forms `Y,Z` by Parseval, but it is generally **dependent** on them. Splitting `Y,Z` into their `BY/BZ` pieces leaves additional same-bank projections in (7.1). Conditioning on those projections is not allowed to manufacture a uniform conditional density cap; the live correction inbox contains explicit failures of that interface.

There is a sharp reason not to silently extend the hyperbolic-square theorem to an arbitrary shift of the isolated variable depending on both transverse variables. If one allowed arbitrary measurable `psi(y,z)` in

`2a (X+psi(Y,Z))Y + bZ^2`,

one could take `psi(y,z)=-b z^2/(2ay)` away from `y=0`, cancelling the square and reducing to the logarithmically singular product `2aXY`. Therefore the remaining theorem must use the **linear/product-provenant origin** of `A`, not merely its measurability or a conditional density bound.

This is consistent with the designated partner's source-valid counterexample to replacing genuine independence by conditional caps.

## 8. First unpaid implication after this run

The first missing implication is now

`QFORM-ORTHOGONAL-LEAKAGE-BORDERED-HYPERBOLIC-v1`:

> In the exact-null singleton-hub state, with three original-product coefficient vectors `(a_i),(y_i),(z_i)` satisfying the Parseval orthogonality identities, and with the N-oriented opposite-bank coefficient packet (5.3), prove a universal density bound while retaining the same-bank nuisance projections inside the integral.

A sufficient theorem may be formulated as a two-bank Brascamp--Lieb/hyperbolic-square estimate: aggregate each bank before conditioning, use the isolated physical hub only in the one-dimensional rearrangement step, and spend the determinant packet only after the linear leakage has been integrated using its coefficient orthogonality. It must not take a conditional-profile supremum.

The exact-null hub is a genuine boundary of the remaining singleton-hub chamber. The nonzero physical-pivot branch is already covered by the current rank-two affine half-Riesz Schur theorem, with a constant that deteriorates as the pivot tends to zero. The purpose of (5.3) is to supply a nondegenerate coefficient packet precisely at that zero-pivot boundary.

## 9. Status and regularity

- Lemma 3.1: proved exactly.
- N-oriented opposite-bank energy split (4.5): proved exactly.
- Hyperbolic-square curvature packet (5.2)--(5.3): proved exactly and uses the designated account02/B10 result quantitatively.
- Scalar product provenance (6.1)--(6.2): source-backed and uses disjoint original-coordinate banks.
- Universal density bound for the full singleton-hub state: **OPEN**.
- Arbitrary exact-rank-three target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: no new continuity result is claimed for the unpaid hub state.

No Gaussianity, moments, compact support, connected support, post-rotation independence, Monte Carlo extremality, or local-minor pigeonhole principle is used.
