# fleet04/B11 — sign-frustrated near-null triangles pay both sheets

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B11, 2026-09-23T02:15:12Z.

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T021512Z-fleet04-B11-sign-frustrated-triangle-r4`  
Assignment: indefinite signatures `(2,1)` and `(1,2)`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_TARGET-LEVEL SUBCLASS / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Scope and sources actually used

The target is the original unrestricted conjecture: independent real coordinates with densities at most one, arbitrary dimension, and a symmetric matrix with at least three eigenvalues of modulus at least one. Essential boundedness is the target; continuity is separate.

The newest Claude package was read at the required source pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. The files actually used have current blobs `RESULTS.md@62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`, `FOURIER_ROUTE_REPORT.md@9da148eed6cd43b1046a6f91d0f9329e12921cb4`, and `COUNTEREXAMPLE_SEARCH.md@ee721b237e206f31298b1871979faaab37a1bac2`. The relevant new input is the ruled one-sheet estimate: an invertible physical three-dimensional block of inertia `(2,1)`, with smallest singular value `sigma`, has conditional density at most `pi sqrt(2)/sigma` on the one-sheet side after completing its affine term.

The completed fleet01/B11 sign-specific Schur result actually applied below is the report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260922T231431Z-fleet01-B11-QFORM-r11/REPORT.md`

at blob `f696979d58d0e6fcc39a7a519405c1591a34b53a`. Its majority-sign theorem says that for an invertible physical triple `H` of inertia `(2,1)`, a positive original-coordinate pivot `d` gives

`||p||_infinity <= 4 C_bin^(3/4) (d |det H|)^(-1/4)`,             (1.1)

uniformly in all affine terms and arbitrary conditioned outside coordinates. Here `C_bin` is the universal constant in its binary-indefinite `L^3` theorem. Negation covers inertia `(1,2)`.

The newest fleet01/B11 Lorentz report was also checked:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260923T014132Z-fleet01-B11-QFORM-r13/REPORT.md`, blob `d08cde8957cf615c877b28a70ad069848dc47cdb`.

It supplies the five-near-ray reduction for the distinct exact-rank-three zero-diagonal residual. The theorem below treats a complementary physical near-null-pair chamber and does not delete or approximate that residual.

Binding corrections are retained: no post-rotation independence, arbitrary-joint coarea bound, conditional-cap substitute for independence, pointwise uniform quadratic decay, fixed good minor, moment/support hypothesis, or perturbative deletion of a dense remainder is used.

## 2. Robust sign-frustrated triangle theorem

Let `S={i,j,k}` be three ORIGINAL coordinates and let `H=A[S,S]`. After possibly replacing the whole quadratic form by its negative, suppose

`a_r:=A_rr>0` for `r in S`.

Assume there are signs `epsilon_rs in {+1,-1}` and a number `0<=eta<1/2` such that

`| A_rs/sqrt(a_r a_s) - epsilon_rs | <= eta`,                    (2.1)

for all distinct `r,s in S`, and that the triangle is sign-frustrated:

`epsilon_ij epsilon_jk epsilon_ki=-1`.                           (2.2)

Put `m=min(a_i,a_j,a_k)` and `sigma=m(1-2 eta)`.

### Theorem 2.1 — `QFORM-SIGN-FRUSTRATED-NEAR-NULL-TRIANGLE-v1`

For every ambient symmetric matrix having this physical triple, every collection of independent cap-one input densities, and every interval `I`,

`P{X^T A X in I} <= K_S |I|`,                                  (2.3)

where

`K_S = min( 6 sqrt(pi)/sigma,
             min_{r in S} 4 C_bin^(3/4) (a_r |det H|)^(-1/4) )`. (2.4)

Moreover, after conditioning on the outside original coordinates `Z`, define the exact moving critical value

`tau(Z)=c(Z)-(1/4) ell(Z)^T H^(-1) ell(Z)`,                      (2.5)

where the conditional polynomial is `u^T H u+ell(Z)^T u+c(Z)`. Then for almost every `y`,

`p_{Q|Z}(y) 1{y>=tau(Z)} <= (pi sqrt(2)/sigma) 1{y>=tau(Z)}`,   (2.6)

while on the two-sheet side

`p_{Q|Z}(y) 1{y<tau(Z)} <= K_S 1{y<tau(Z)}`.                    (2.7)

Thus the half-line ruled theorem is not called a full density theorem: (2.7) is paid separately by sign-specific Schur smoothing (or by the full three-dimensional physical-fibre estimate).

### Proof

Let `D=diag(sqrt(a_i),sqrt(a_j),sqrt(a_k))`. Then

`H=D(C_0+E)D`,                                                   (2.8)

where `C_0` has diagonal one, off-diagonal entries `epsilon_rs`, and `E` has zero diagonal and off-diagonal entries of modulus at most `eta`. Diagonal sign switching makes `C_0` congruent to

`[[1,1,1],[1,1,-1],[1,-1,1]]`,                                 (2.9)

whose eigenvalues are `{2,2,-1}`. Hence `s_min(C_0)=1`. Every row of `E` has absolute row sum at most `2 eta`, so

`||E||_op<=2 eta`.                                               (2.10)

Weyl's inequality gives inertia `(2,1)` and

`s_min(C_0+E)>=1-2 eta`.                                        (2.11)

For every vector `x`,

`||Hx|| = ||D(C_0+E)Dx|| >= sqrt(m)(1-2eta)||Dx||`
`        >= m(1-2eta)||x||`,                                    (2.12)

so `s_min(H)>=sigma`.

Condition on every coordinate outside `S`. Independence of the three coordinates in `S` is unchanged; outside self-couplings and cross-couplings create only the affine term `ell(Z)` and scalar `c(Z)`. Since `H` is invertible, completing the square in the deterministic polynomial gives (2.5), with no random rotation.

On `y>=tau(Z)`, the level set has the one-sheet sign. Applying the ruled theorem to the actual physical fibre and (2.12) yields (2.6), including its rough-input approximation/trace justification.

Every physical diagonal `a_r` is a majority-sign pivot. Apply the completed fleet01/B11 theorem (1.1) to the same conditioned fibre:

`p_{Q|Z}(y) <= 4 C_bin^(3/4)(a_r |det H|)^(-1/4)`                (2.13)

for every `r in S` and almost every `y`. This is the promised actual application of the completed partner inequality. It pays the convex/two-sheet side without assuming any coarea estimate for an arbitrary joint spectral density.

Independently, Claude's physical three-variable theorem applied to (2.12) gives

`p_{Q|Z}(y)<=6 sqrt(pi)/sigma`.                                  (2.14)

Taking the minimum of (2.13) over the three pivots and (2.14) proves (2.7) and (2.4). The estimates are uniform in `Z`; averaging proves (2.3). QED.

## 3. Exact saturated-pair endpoint

The robust theorem has a useful exact structural corollary. Suppose a real symmetric matrix `A` has rank at least three and every physical principal pair is singular:

`A_ii A_jj-A_ij^2=0` for all `i,j`.                              (3.1)

If `A_ii=0`, then (3.1) forces `A_ij=0` for every `j`, so that coordinate is a zero row. All nonzero diagonal entries have one common sign. Reverse the global sign and restrict to active coordinates, so every diagonal is positive. Define

`epsilon_ij=A_ij/sqrt(A_ii A_jj) in {+1,-1}`.                   (3.2)

If every triangle product were `+1`, choosing a base coordinate `o` and putting `s_i=epsilon_oi` would give `epsilon_ij=s_i s_j`; hence the normalized active matrix would equal `ss^T` and have rank one. This contradicts `rank A>=3`. Therefore some physical triangle is sign-frustrated.

For that triangle `eta=0`, and Theorem 2.1 applies. Its normalized matrix has eigenvalues `{2,2,-1}` and

`|det H|=4 a_i a_j a_k`.                                        (3.3)

Consequently

`boxed:
 ||p_{X^TAX}||_infinity
 <= min{ 6 sqrt(pi)/m,
          min_{r in S} 4 C_bin^(3/4)(4 a_r a_i a_j a_k)^(-1/4) }.` (3.4)

The conditional one-sheet contribution obeys the sharper `pi sqrt(2)/m` bound. Arbitrary additional spectrum, dense outside self-couplings, and conditioning-generated affine terms are allowed because only the actual physical triple is left unconditioned.

This closes the **exact all-pairs-null endpoint at fixed diagonal scale**. It does not claim that the global three-large-eigenvalue hypothesis forces `m` to be universal.

## 4. What the near-null analysis leaves

For a near-null active physical graph, (2.1) says each normalized edge is close to a sign. There are now two sharply different cases.

1. A frustrated triangle exists. Theorem 2.1 supplies a genuine three-coordinate core and pays both sheets, quantitatively.
2. Every triangle is balanced. After diagonal sign switching the normalized matrix is locally close to the rank-one all-ones matrix. In a large dimension, many individually tiny deviations can collectively create two further spectral directions. No single physical diagonal or triangle need retain a universal scale. Small operator norm or small entries cannot be discarded under arbitrary unbounded inputs.

Thus the first unpaid implication is an aggregation theorem for the balanced-sign near-rank-one chamber: turn its collective deviation from rank one into either (i) a product-preserving cross-volume certificate, (ii) disjoint innovation banks, or (iii) a quantitative physical pivot. This is consistent with the fleet01/B11 five-near-ray survivor: near-null geometry is forced into a small number of aligned ray classes, but tangent/opposite-null leakage must be aggregated rather than removed.

The unrestricted full conjecture and a universal constant remain open. No counterexample was found. Continuity is not derived from the present Schur argument; it is tracked separately from essential boundedness.
