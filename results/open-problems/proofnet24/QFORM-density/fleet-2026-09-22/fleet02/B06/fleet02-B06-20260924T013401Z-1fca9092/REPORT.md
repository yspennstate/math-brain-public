SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T01:34:01Z.
attacking: QFORM-R48-RANK1T-SHARED-DIAGONAL-SQUARE-AVERAGING-v1; aggregate the diagonal-versus-off-diagonal curvature of the exact rank-one Schur residual, cut the off-diagonal packet only after averaging over literal product-coordinate cuts, and feed its square-root small-ball profile into the physical indefinite-pair logarithmic receiver.

# fleet02/B06 — diagonal-plus-rank-one Schur residual has dimension-free square-root small-ball

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: curved fiber integration / complementary constructions and source-valid counterexamples  
Partner: fleet03/B06  
Status: `NEW SUPPORTING THEOREM + PARTNER r48 SINGULAR-T ANALYTIC DEBT PAID AT PAIR CURRENCY / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted QFORM conjecture remains OPEN. No moment, bounded-support, log-concavity, iid, diagonal-basis, arbitrary-joint coarea, post-rotation independence, or deletion of nonzero curvature is introduced. Every probabilistic split below is a split of literal original coordinates. Continuity is not claimed from the pair-log endpoint; all density bounds below are essential bounds.

## 1. Source boundary and the exact unpaid implication

Fresh owner control at startup was revision `2026-09-22.15`, QFORM-only. The required pinned packet

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. I use two proved pieces from that packet at equations below:

1. its Schur-complement spectral lemma: after completing an invertible physical `2 x 2` principal block in a matrix with at least three eigenvalues of modulus at least one, the Schur complement still has at least one eigenvalue of modulus at least one;
2. its physical-indefinite-pair theorem: if the exact remainder has concentration function at most `H sqrt(rho)`, then the full pair-plus-remainder density is at most `4 sqrt(2H)(|det B| sigma_min(B))^(-1/4)`.

I also use the independently checked exact-rank crossing theorem with arbitrary internal functions in

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`,

and its already-published rank-one square-root small-ball specialization from fleet03/B08:

`QFORM-RANK1-CROSSING-SQRT-SMALLBALL-v1`.

That theorem says that if two disjoint original-coordinate product banks `X,Y` are coupled by an exact rank-one physical cross block `C` of sole singular value `sigma>0`, while arbitrary measurable same-bank functions `F(X),G(Y)` are retained, then

`P(|F(X)+2X^T C Y+G(Y)-t|<rho)
 <= H1 sigma^(-1/2) sqrt(rho),`

where

`H1 = exp(1/2) 2^(1/4) Gamma(1/4)
    = 7.108628442830306... .`                                     (1.1)

This is a product-bank Fourier/Plancherel statement, not a law-uniform one-dimensional quadratic-phase estimate.

The immediate fleet02/B06 debt was the partner-r48 singular-shear residual

`S = D + lambda w w^T`                                            (1.2)

with **the diagonal `D` and rank-one statistic `w.Y` using the same original coordinates**. The previous run paid `D=0` and disjoint-diagonal-bank versions. The purpose of this run is to pay the shared-coordinate case without taking a curved-fiber supremum.

## 2. Main theorem: diagonal plus rank one has universal square-root concentration

### Theorem 2.1 — `QFORM-DIAG-RANK1-SQRT-SMALLBALL-v1`

Let `Y=(Y_1,...,Y_m)` have independent scalar densities bounded by one. Let

`S = D + lambda w w^T`                                            (2.1)

with `D` real diagonal, `lambda` real, and `w in R^m`. Let `ell in R^m`, `c in R`, and put

`R(Y)=Y^T S Y + ell^T Y + c`.                                    (2.2)

Write

`L=||S||op`.                                                       (2.3)

If `L>0`, then for every `rho>0`,

`boxed:
 sup_t P(|R-t|<rho)
 <= min(1, H_* L^(-1/2) sqrt(rho)),`                              (2.4)

where, with `H1` from (1.1),

`tau_* = 4/(H1^2+4)
       = 0.07335062186458903... ,`                                (2.5)

and

`boxed:
 H_* = sqrt(2(H1^2+4))
     = 10.443428396672811... .}`                                  (2.6)

The exponent `1/2` is optimal in this class because a single original-coordinate square already has `sqrt(rho)` small-ball behavior.

### Proof

Set

`a_j=S_jj`, `A0=diag(a_1,...,a_m)`, `C=S-A0`.                    (2.7)

Since `D` is diagonal, the off-diagonal part is exactly

`C_ij=lambda w_i w_j` for `i!=j`, `C_ii=0`.                      (2.8)

Fix a parameter `0<tau<1`. There are two exhaustive branches.

#### Branch I: one physical diagonal carries `tau L`

Suppose some literal original coordinate `j` satisfies

`|a_j| >= tau L`.                                                 (2.9)

Condition on all other original coordinates. Uniformly in those conditioned values and in the target `t`, the remaining polynomial in `y=Y_j` is

`a_j y^2 + b y + d`.                                              (2.10)

After completing its scalar square, the inverse image of any interval of radius `rho` has total Lebesgue length at most

`2 sqrt(2 rho/|a_j|)`.                                            (2.11)

Indeed the maximum occurs when the interval touches the quadratic vertex. Since the conditional density of `Y_j` is bounded by one,

`sup_t P(|R-t|<rho)
 <= 2 sqrt(2) tau^(-1/2) L^(-1/2) sqrt(rho).`                     (2.12)

No conditional density supremum in the other variables appears; their actual probability law is simply averaged after (2.11).

#### Branch II: all physical diagonals are below `tau L`

Assume instead

`max_j |a_j| < tau L`.                                            (2.13)

Then

`||C||op >= ||S||op-||A0||op > (1-tau)L`,                        (2.14)

so

`||C||F > (1-tau)L`.                                              (2.15)

Now assign every literal original coordinate independently to a set `I` or `J` with probability `1/2`. Since `C` is symmetric with zero diagonal,

`E ||C[I,J]||F^2 = ||C||F^2/4`.                                  (2.16)

Therefore some deterministic original-coordinate cut satisfies

`||C[I,J]||F >= ||C||F/2 > (1-tau)L/2`.                          (2.17)

But by (2.8) this cross block is not merely approximately rank one: it is exactly

`C[I,J]=lambda w_I w_J^T`.                                       (2.18)

Thus its sole nonzero singular value is

`sigma=|lambda| ||w_I||_2 ||w_J||_2
      =||C[I,J]||F
      > (1-tau)L/2`.                                              (2.19)

With this literal product cut, rewrite the *complete* residual as

`R=F(Y_I)+2Y_I^T C[I,J]Y_J+G(Y_J)`,                              (2.20)

where `F` and `G` contain every diagonal term, every within-bank piece of `lambda(w.Y)^2`, every affine term, and the constant. The rank-one crossing theorem (1.1) explicitly allows arbitrary measurable `F,G`; hence

`sup_t P(|R-t|<rho)
 <= H1 sigma^(-1/2) sqrt(rho)
 <= H1 sqrt(2/(1-tau)) L^(-1/2) sqrt(rho).`                       (2.21)

This is the requested weighted product-structure replacement: the off-diagonal curvature is first aggregated through the Frobenius identity (2.16), and only then is one full product cut used. No individual cross coefficient is selected and no tail is discarded.

#### Optimize the branch threshold

The coefficients in (2.12) and (2.21) are

`A(tau)=2 sqrt(2) tau^(-1/2)`,
`B(tau)=H1 sqrt(2/(1-tau))`.                                     (2.22)

Equating them gives exactly

`tau=tau_*=4/(H1^2+4)`.                                          (2.23)

At this value

`A(tau_*)=B(tau_*)=sqrt(2(H1^2+4))=H_*`,                         (2.24)

which proves (2.4). QED.

### Remarks

1. The theorem includes `lambda=0`: then Branch II cannot occur when `L>0`, so a diagonal pivot pays.
2. A single huge physical coefficient is not required. In Branch II, the payment is the aggregate off-diagonal Frobenius mass and a product cut produced by averaging.
3. No rotated collection of input coordinates is declared independent. Singular vectors enter only inside the already-checked rank-one crossing theorem through scalar projection-density bounds on two disjoint original-coordinate banks.
4. The theorem is translation-uniform because affine terms are absorbed in (2.10) or in the arbitrary internal functions of (2.20).

## 3. Pair upgrade: a target-level conditional theorem

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-DIAGRANK1-SCHUR-v1`

Let an ambient real symmetric matrix be split along two literal original coordinates as

`A = [[H,E],[E^T,C0]]`,                                           (3.1)

where `H` is an invertible **indefinite** `2 x 2` principal block. Put

`delta=det H`, `kappa=sigma_min(H)`,                              (3.2)

and let its exact Schur complement be

`S=C0-E^T H^(-1)E = D+lambda w w^T`.                             (3.3)

Assume the ambient matrix `A` has at least three eigenvalues of modulus at least one. Then

`L=||S||op >= 1`,                                                 (3.4)

and for arbitrary independent cap-one original-coordinate inputs the complete quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||infinity
 <= C_* (|delta| kappa L)^(-1/4),`                                (3.5)

where

`boxed:
 C_* = 4 sqrt(2 H_*)
     = 18.280856344644523... .}`                                  (3.6)

In particular,

`||p_Q||infinity
 <= 18.281 (|det H| sigma_min(H))^(-1/4).`                        (3.7)

#### Proof

The pinned `e5f71d79...` Schur-complement spectral lemma applies to the literal invertible physical pair `H`: removing two coordinates from a matrix with at least three eigenvalues of modulus at least one leaves the Schur complement with at least one eigenvalue of modulus at least one. Thus (3.4) holds.

Complete the physical pair exactly. Its translated centre may depend arbitrarily on the environment coordinates, while its exact remainder has quadratic matrix `S`. By Theorem 2.1 its concentration function obeys

`sup_t P(|R-t|<rho)
 <= H_* L^(-1/2) sqrt(rho).`                                      (3.8)

Now apply the completed physical-pair logarithmic receiver from the required pinned RESULTS packet with

`H0=H_* L^(-1/2)`.                                                (3.9)

It gives

`||p_Q||infinity
 <=4 sqrt(2 H0)(|delta| kappa)^(-1/4)
 =4 sqrt(2H_*) (|delta| kappa L)^(-1/4),`                         (3.10)

which is (3.5). QED.

This is a genuine target-level implication in its stated physical-pair chamber: the only remaining quantitative currency is the actual physical pair factor `|det H| sigma_min(H)` (and retaining `L` only improves the estimate).

For a definite invertible `H`, the usual two-dimensional physical area argument already gives a direct conditional density bound; the new content here is the hyperbolic/indefinite pair where a third smoothing resource is needed.

## 4. Application to partner fleet03/B06 r48

The latest compatible designated partner packet read in this run is

`yspennstate/math-open-problems@a4090a876e18635918b87f87a7af42726b29337a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T001713Z-fleet03-B06-qform-r48/REPORT.md`.

Its exact shear-flat normal form is

`A=[[H,E],[E^T,C0]],`
`S=C0-E^T H^(-1)E = D+E^T T E`.                                 (4.1)

The unresolved singular endpoint has

`T=lambda v v^T`.                                                 (4.2)

Put

`w=E^T v`.                                                        (4.3)

Then **without any approximation**

`S=D+lambda w w^T`,                                               (4.4)

so Theorem 3.1 applies to the entire shared-coordinate diagonal-plus-rank-one residual. In the live indefinite-pair branch,

`boxed:
 ||p_Q||infinity
 <=18.281
   ( |det H| sigma_min(H) ||D+lambda(E^T v)(E^T v)^T||op )^(-1/4).}`  (4.5)

Since the ambient target has three large eigenvalues, the last operator norm is at least one by the pinned Schur lemma, giving the simpler pair-currency bound

`boxed:
 ||p_Q||infinity
 <=18.281 (|det H| sigma_min(H))^(-1/4).}`                        (4.6)

This pays the previous fleet02/B06 first debt

`QFORM-R48-RANK1T-SHARED-DIAGONAL-SQUARE-AVERAGING-v1`

at the analytic level. In particular:

- `D` may use exactly the same original coordinates as `w.Y`;
- no `D_hh` pivot is required;
- the rank-one nonresonance scalar `1+lambda v^T H v` is not needed to establish (4.5);
- all diagonal coefficients, all within-bank rank-one terms, all affine terms produced by conditioning, and all conditioning weights are retained;
- the random cut is used only after the exact aggregate identity (2.16), so diffuse `w` is not reduced to a largest physical coefficient.

The partner's nonresonance and two-heavy-hub information remain useful **structurally** when the physical-pair currency in (4.6) is small. They are no longer needed merely to solve the shared-diagonal analytic subproblem.

## 5. Why the square-root profile is the right endpoint

A stronger intermediate statement — that a diagonal-plus-rank-one residual with `||S||op>=1` must itself have a bounded density — is false in the simplest possible source-valid example. Take one cap-one variable `Z` uniform on `[-1/2,1/2]` and

`R=Z^2`.                                                          (5.1)

Then for `0<s<1/4`,

`p_R(s)=s^(-1/2)`,                                                (5.2)

so `||p_R||infinity=infinity`, while

`P(R<rho)=2 sqrt(rho)`                                           (5.3)

for `rho<=1/4`. Thus exponent `1/2` in Theorem 2.1 cannot in general be improved to residual `L^infinity` control.

Embedding this obstruction into

`Q_*=X_1^2-X_2^2+Z^2`                                            (5.4)

produces an exact QFORM target with spectrum `{1,-1,1}`. The completed Theorem A in the required pinned `COUNTEREXAMPLE_SEARCH.md` applies directly to this literal three-coordinate matrix and gives the all-level bound

`boxed:
 ||p_(Q_*)||infinity <= 6 sqrt(pi).}`                             (5.5)

This is the requested application of a completed pinned result to a real obstruction: the isolated third residual square is singular at its critical value, but the full three-direction target is uniformly bounded. The pair-log mechanism in Theorem 3.1 is therefore consuming a genuinely necessary third small-ball resource rather than trying to prove a false residual density bound.

## 6. Quantitative audit of the aggregate cut

The key deterministic inequality can be isolated as follows. For any `S=D+lambda w w^T`, define

`C=S-diag(S_11,...,S_mm)`.

If `max_j |S_jj|<tau ||S||op`, then

`||C||F >= ||C||op > (1-tau)||S||op`.                            (6.1)

For a uniform Bernoulli cut,

`E ||C[I,J]||F^2=||C||F^2/4`,                                   (6.2)

so a cut exists with

`|lambda| ||w_I|| ||w_J||
 =||C[I,J]||F
 >=(1-tau)||S||op/2`.                                            (6.3)

The equality on the left of (6.3) uses the full rank-one cross block; it is not a lower bound by a selected edge. I independently enumerated all cuts in random dimensions `2<=m<=8` for 593 random instances landing in the off-diagonal branch at the cruder threshold `tau=1/2`; there were zero violations of the guaranteed `sigma>=||S||op/4`. The computation is only a sanity check; (6.1)-(6.3) are exact algebraic identities/inequalities and constitute the proof.

## 7. What remains

The first unpaid implication is now

`QFORM-R48-SINGULART-PAIR-CURRENCY-OR-DIRECT-SHEAR-EXIT-v1`.

In the r48 singular-`T` shear-flat chamber, Theorem 3.1 has removed the shared-coordinate analytic obstruction. What remains is purely structural: when

`eta = |det H| sigma_min(H) ||S||op`                              (7.1)

is small, use the **complete** physical shear frame `E`, the r48 nonresonance/two-heavy-hub certificates, and the actual third large spectral direction to force a different product-preserving exit — e.g. an aggregate rank-two crossing, a three-hub projected-crossing volume, or a determinant-controlled literal four-coordinate block. The desired implication must retain `D`, `E`, and every nonzero tail; it may not declare a small coefficient to be a small random perturbation on arbitrary unbounded inputs.

A model showing why this structural step is real is

`A_eps=[[eps I_2, I_2],[I_2,0]]`                                 (7.2)

(or its indefinite-hub analogue). Its full spectrum stays at order one while the physical pair currency tends to zero; the strong resource is instead the literal rank-two hub-to-environment crossing. Thus no universal proof can finish by lower-bounding `|det H| sigma_min(H)` alone. The next compiler must route small pair currency into that crossing/shear resource.

## 8. Correction boundary and conclusion

This run does not use the refuted critical rank-one **same-bank half-Riesz** claim. The only rank-one Fourier theorem invoked is an exact **crossing between two disjoint original-coordinate product banks**, after the aggregate cut (2.16) has been chosen. It does not use post-rotation independence, arbitrary-joint coarea, a good single minor, or a dimension-losing fiber supremum.

The full conjecture is still OPEN. The new result is a dimension-free, translation-uniform square-root small-ball theorem for every diagonal-plus-rank-one quadratic form under arbitrary independent cap-one laws, and it closes the analytic shared-diagonal singular-`T` debt in partner r48 at the natural physical-pair currency.
