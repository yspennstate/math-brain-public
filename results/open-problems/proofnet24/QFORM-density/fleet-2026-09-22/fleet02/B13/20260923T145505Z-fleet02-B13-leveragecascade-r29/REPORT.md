SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T14:55:05Z.
attacking: the designated partner's high-leverage principal-volume star; force a five-deep physical leverage cascade into a D5 payment, a bounded five-coordinate spectral payment, or a physical third-volume bi-hub.

# fleet02/B13 r29 — five-deep leverage cascade collapses to a physical bi-hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / complementary constructions and source-valid obstructions  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**.

## 1. Source-pinned inputs actually used


### 1.1 Designated partner fleet03/B13

Canonical mathematics:

`yspennstate/math-open-problems@980dd55d0202bf513f4dd0d6f72e78c8e74883d7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T140232Z-fleet03-B13-qform-r27/REPORT.md`

and `POSTREFRESH_ADDENDUM.md` in the same directory.

The inputs used here are:

* no-attainment purification: arbitrary cap-one product slab suprema are approximated arbitrarily closely by bounded finite-union unit-product indicators; no optimizer, interval, diameter or fragment-count hypothesis is introduced;
* `QFORM-WEIGHTED-SPECTRAL-VOLUME-STAR-v1`: for a rank-d symmetric retained leaf matrix with range projection `P`, a coordinate with `P_jj>1/2` carries more than one half of the complete absolute d-principal-minor currency;
* the post-refresh rank-four cross compression: an actual high-ratio physical cross block is rank at most four modulo the explicit `O(rho^{-1})` singular tail, leaving the first unpaid `QFORM-RANK4-MISALIGNMENT-OR-STAR-CLOSURE-v1`.

### 1.2 Required pinned Claude/Fourier source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

`FOURIER_ROUTE_REPORT.md`

`COUNTEREXAMPLE_SEARCH.md`.

Two proved estimates are applied below at actual inequalities:

* D5, for every disjoint physical cross block `M`,

  `||p_Q||_inf <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`,

  with no volume-marginal hypothesis;
* D' at `h=2/3`: if the natural squared-3-minor row marginals of `M` are all at most `2/3`,

  `||p_Q||_inf <= C3 e_3(M^T M)^(-1/6)`,

  where `C3=9 sqrt(3e)`.

The counterexample search still reports no valid counterexample; none of its numerical observations is used as proof here.

### 1.3 Bounded five-coordinate receiver

`yspennstate/math-open-problems@472b70df7d1edbb3af23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1.

If an actual symmetric `m x m` physical principal block has at least three eigenvalues of absolute value at least `sigma`, conditioning every other original coordinate gives

`||p_Q||_inf <= 2 sqrt(6 pi m)/sigma`.

For `m=5` this is `2 sqrt(30 pi)/sigma`. This receiver uses the actual total principal block, not a cancellable rank-three component.

## 2. Projection-DPP leverage peeling without selecting a tiny minor

Let `P` be an orthogonal projection of rank `d` on a physical coordinate set `V`. For a selected set `H` with `P[H,H]` invertible define the conditional projection on `H^c`

`P^H = P[H^c,H^c] - P[H^c,H] P[H,H]^(-1) P[H,H^c]`.          (2.1)

This is again an orthogonal projection, of rank `d-|H|`. For a singleton `j`, this follows directly by writing

`P=[[p,b^T],[b,C]]`, `P^2=P`

and checking that `C-bb^T/p` is idempotent and symmetric. Iteration gives the determinant chain rule

`det P[H,H] = product_{r=0}^{|H|-1} p_r`,                       (2.2)

where `p_r` is the diagonal leverage selected at the r-th conditional projection. Equivalently, this is the usual fixed-size projection-DPP conditioning identity, but only the elementary Schur formula is needed.

### Theorem 2.1 — `QFORM-FOUR-OR-FIVE-LEVERAGE-CASCADE-v1`

Starting from any rank-`d` projection `P`, greedily choose a physical coordinate with conditional leverage `>1/2` whenever the current conditional projection has such a coordinate. After at most five choices exactly one of the following occurs:

1. for some `H` with `|H|<=4`, the residual conditional projection has maximum diagonal at most `1/2`;
2. for some `H` with `|H|<=4`, the residual rank is below three;
3. there is a five-set `H` such that

   `det P[H,H] > 2^(-5)=1/32`.                                  (2.3)

Proof: if neither (1) nor (2) occurs before the fifth choice, five successive conditional pivots exceed `1/2`; (2.2) gives (2.3). No global optimizer and no single coefficient minor is selected.

This is the first useful alignment with the partner's rank-four obstruction: a high-leverage chain either terminates after at most four physical centers, or produces a quantitatively robust five-coordinate spectral localization.

## 3. A five-deep retained star has five units of physical row energy

Let `R` be the **actual physical symmetric leaf block** of the coefficient matrix and, for `tau>0`, let

`P_tau = 1_{|R|>=tau}`                                           (3.1)

be the deterministic spectral projection onto eigenvalues of modulus at least `tau`. No random variables are rotated.

Assume the five-deep alternative (2.3) occurs for `P_tau`; write its physical five-set as `H`. Since every eigenvalue of a principal compression of a projection lies in `[0,1]`,

`lambda_min(P_tau[H,H]) >= det P_tau[H,H] > 1/32`.              (3.2)

Functional calculus gives the PSD inequality

`R^2 >= tau^2 P_tau`.                                            (3.3)

Taking the physical `H x H` principal compression and using symmetry,

`R[H,:] R[:,H] = (R^2)[H,H] > (tau^2/32) I_5`.                 (3.4)

Hence, with

`c_tau := tau/sqrt(32)`,                                        (3.5)

all five singular values of the **actual physical row block** `R[H,:]` exceed `c_tau`. This is important: unlike a perturbative comparison with the truncated matrix, (3.4) has no low-spectrum error term; the omitted spectral modes contribute positively after squaring.

Split the row block into its internal and external physical columns,

`D = R[H,H]`, `M = R[H,H^c]`.                                  (3.6)

Then exactly

`D D^T + M M^T > c_tau^2 I_5`.                                 (3.7)

## 4. Required D5 applied: a five-deep star cannot be externally diffuse for free

Suppose first

`||D||_op <= tau/8`.                                             (4.1)

Because `tau^2/64` is the square of `tau/8`, (3.7) yields

`M M^T >= (tau^2/32 - tau^2/64) I_5 = (tau^2/64) I_5`.          (4.2)

Thus all five singular values of the physical disjoint cross block `M` are at least `tau/8`, and therefore

`e_5(M^T M) >= (tau/8)^10`.                                     (4.3)

The pinned D5 theorem now gives the **actual target inequality**

`||p_Q||_inf <= 5 sqrt(2e) (tau/8)^(-1)
              = 40 sqrt(2e)/tau
              = 93.265759263884.../tau`.                        (4.4)

Consequently any slab witness of ratio `rho` with

`rho > 40 sqrt(2e)/tau`                                         (4.5)

must satisfy

`boxed: ||R[H,H]||_op > tau/8.`                                 (4.6)

This is a real D5 obstruction, not a claim that a small coefficient tail is a small random perturbation.

## 5. If the internal five-block has three directions, the finite core pays

If

`s_3(D) >= tau/sqrt(128)`,                                       (5.1)

then the symmetric actual physical five-block `D` has three actual eigenvalues of absolute value at least `tau/sqrt(128)`. Condition all original coordinates outside `H` and apply the bounded-dimensional receiver with `m=5`:

`||p_Q||_inf
 <= 2 sqrt(30 pi) sqrt(128)/tau
 = 16 sqrt(60 pi)/tau
 = 219.669895887304.../tau`.                                    (5.2)

Thus a witness with

`rho > C_* / tau`, `C_*:=16 sqrt(60 pi)`,                       (5.3)

cannot satisfy (5.1).

## 6. Otherwise the external cross block has three strong directions

Assume instead

`s_3(D) < tau/sqrt(128)`.                                        (6.1)

Let `L` be the three-dimensional singular subspace of `D^T` corresponding to its three smallest singular values. For `x in L`,

`||D^T x|| <= (tau/sqrt(128)) ||x||`.                            (6.2)

From (3.7),

`||M^T x||^2
 > (tau^2/32 - tau^2/128)||x||^2
 = (3 tau^2/128)||x||^2`.                                       (6.3)

The min-max principle therefore yields

`boxed: s_3(M) > tau sqrt(3/128).`                               (6.4)

In particular

`Z_3:=e_3(M^T M) >= s_1(M)^2 s_2(M)^2 s_3(M)^2 > s_3(M)^6`.     (6.5)

## 7. Required D' applied: the only high-ratio escape is a physical 3-volume bi-hub

Let `w_{S,T}=det(M[S,T])^2/Z_3` be the natural squared-3-minor volume law, with row marginals `alpha_h` (`h in H`) and column marginals `beta_j` (`j in H^c`).

If every `alpha_h<=2/3`, pinned D' at `h=2/3` and (6.4)-(6.5) give

`||p_Q||_inf <= 9 sqrt(3e) / s_3(M)
              < 9 sqrt(3e) sqrt(128/3)/tau
              = 72 sqrt(2e)/tau
              = 167.878366674992.../tau`.                       (7.1)

Apply the same theorem to `M^T`. If every `beta_j<=2/3`, the identical bound follows. Therefore, whenever

`rho > 72 sqrt(2e)/tau`,                                        (7.2)

both marginal gates must fail. There exist physical `h in H` and `j in H^c` with

`alpha_h>2/3`, `beta_j>2/3`.                                    (7.3)

Under the same volume law, inclusion-exclusion gives

`boxed: P_w(h in S, j in T) > 1/3.`                             (7.4)

Thus more than one third of the complete squared 3-minor currency of the physical cross block `R[H,H^c]` is simultaneously anchored on one physical row and one physical column.

### Theorem 7.1 — `QFORM-FIVE-DEEP-STAR-TO-BIHUB-v1`

Let `rho` be an actual slab ratio for the full ambient quadratic form. Let `R` be any physical symmetric leaf principal block and `P_tau=1_{|R|>=tau}`. If the leverage peeling of Theorem 2.1 reaches five coordinates `H`, then:

* always, `R[H,:]R[:,H]>(tau^2/32)I_5`;
* if `rho>40sqrt(2e)/tau`, then `||R[H,H]||op>tau/8`;
* if `rho>C_*/tau`, `C_*=16sqrt(60pi)=219.669895887304...`, then necessarily

  `s_3(R[H,H])<tau/sqrt(128)`                                   (7.5)

  and the physical cross block `M=R[H,H^c]` has a row-column 3-volume bi-hub satisfying (7.4).

The third bullet follows because `C_*>72sqrt(2e)`: the bounded five-coordinate branch (5.2) is excluded, and the remaining branch (6.1) is either paid by D' or forces (7.4).

This theorem uses the **actual** physical principal and cross blocks throughout. It does not rotate product variables, assume moments/support bounds, or delete `R-R_tau` as a random quadratic perturbation.

## 8. Consequence for the partner's rank-four misalignment obstruction

The designated partner reduced the moderate-spread cross leakage to a rank-at-most-four misaligned piece `H_0(I-P_tau)` plus an explicit `O(rho^{-1})` residual, and left a high-leverage principal-volume star as the complementary obstruction.

Theorem 2.1 plus Theorem 7.1 sharpen that star branch as follows. At every scale satisfying

`tau > C_*/rho`,                                                  (8.1)

one cannot have an unstructured high-leverage chain of length five. Either:

1. leverage peeling terminates after at most four physical centers with a diffuse conditional projection;
2. the residual projection rank drops below three after at most four centers; or
3. a physical 3-volume bi-hub (7.4) is forced, together with the nontrivial internal five-block condition (4.6).

Thus the number of unresolved leverage centers is now bounded by **four**, exactly matching the partner's rank-four misalignment dimension. The previous unpaid implication is reduced to

`QFORM-FOUR-CENTER-RANK4-MISALIGNMENT-GLUE-v1`:

> combine at most four physical leverage centers with the rank-at-most-four misaligned cross piece on the partner's canonical positive-slab-mass core, or route the forced third-volume bi-hub through the already-developed hub/star compilers; handle the residual-rank-below-three endpoint without rotating product variables. No coefficient residual may be globally deleted.

This is strictly narrower than `QFORM-RANK4-MISALIGNMENT-OR-STAR-CLOSURE-v1`: a fifth unresolved high-leverage center at any spectral scale larger than `C_*/rho` is no longer possible without creating the explicit physical bi-hub resource.

## 9. Extremal-product provenance

Nothing above assumes an attained global bathtub optimizer. For an arbitrary cap-one product law with slab ratio `rho`, the designated partner's no-attainment purification gives, for every `epsilon>0`, a bounded finite-union unit-product indicator witness with the same coefficient matrix and slab ratio at least `rho-epsilon`. The physical projection/cross-block argument above is then applied to that witness, and `epsilon` is sent to zero.

This transfer preserves arbitrary original fragmentation and unbounded support scales. No bound on fragment diameter/count and no centered/single-interval extremality is introduced. The D5, D', and bounded-five-coordinate receivers are uniform in all outside affine terms, so conditioning does not smuggle in support or moment assumptions.

## 10. Status and exact remaining gap

The full QFORM conjecture remains **OPEN** and full continuity remains **OPEN**. The new result is a supporting structural theorem, not an end-to-end proof.

First unpaid implication:

`QFORM-FOUR-CENTER-RANK4-MISALIGNMENT-GLUE-v1`.

A useful next attack is to put the four leverage centers and the at-most-four left/right singular directions of the misaligned cross piece into one physical grouped-bank determinant/half-Riesz argument. The key constraint is that the conditional projection is a deterministic coefficient object only; it must not be interpreted as producing independent rotated random coordinates.

No counterexample was found or claimed. The pinned numerical counterexample search is source evidence only, not a proof component.
