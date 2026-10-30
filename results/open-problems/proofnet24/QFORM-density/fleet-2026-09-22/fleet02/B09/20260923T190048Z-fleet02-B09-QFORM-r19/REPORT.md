SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T19:00:48Z.
attacking: strengthen the newest exact rank-three/rank-four carrier crossing theorem into a parameterized original-coordinate localization fork, then apply it through the rank-four-to-rank-three transition while retaining dense same-side curvature.

# fleet02/B09 r19 — parameterized finite-localization fork for the dual-zero carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: bilinear block mechanism / complementary constructions  
Status: **ESSENTIAL STEP APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted target remains OPEN: independent real coordinates with densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal essential density bound for `X^T A X` (or a valid counterexample). No moment, support, log-concavity, iid, post-rotation independence, or small-random-perturbation hypothesis is introduced below. Continuity is claimed only where an integrable Fourier envelope is explicitly available.

The first unpaid B09 implication after the newest partner refresh is

`QFORM-R4-CARRIER-STRONG-LOCALIZATION-OR-RESIDUAL-ROUTING-v1`:

> In the exact two-sided-zero-aggregate rank-two hub/star survivor, either pay the diagonal-plus-rank-three/rank-four carrier by an aggregate physical cross cut, or force an arbitrarily strongly localized carrier direction on a quantitatively finite set of ORIGINAL coordinates; then route that finite-localization certificate, and separately r38's nonzero retained residual, through a physical hub/pivot/projected-crossing receiver without deleting the residual as a small random quadratic error.

This run proves the parameterized exact-carrier fork and applies it to a target-valid overlapping Walsh family whose fourth carrier singular value tends to zero. The dense same-side couplings and the diagonal twist are retained.

## 1. Fresh source state and correction discipline

Fresh owner control remained revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`, with fleet02/B09 active. The current QFORM manifest, research state, claim ledger, deltas, correction inbox, pathways, memory protocol, assignment card, proof-first continuation, current Claude continuation, current exclusive-signin continuation, and Fisher continuation were read before publication.

The required historical source was reread at the exact owner-pinned commit

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The counterexample search still contains no valid counterexample to the full target. I use its completed Theorem H at an actual source-coordinate star in Section 6.

The newest completed designated fleet03/B09 work available at the final source refresh is r39, canonical report

`yspennstate/math-open-problems@4b076c614a1e1b826433acf811adcffc29e8f05d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T184804Z-fleet03-B09-QFORM-r39/REPORT.md`,

with late-source reconciliation at commit

`af81ace54b10d45b8284185c92e89df38b92063c`.

Its surviving new theorem is `QFORM-R4-CARRIER-DIFFUSE-OR-256-LOCALIZED-v1`: for an original-coordinate diagonal plus rank-three/rank-four carrier `A=D+VKV^T`, `V^TV=I_r`, `r in {3,4}`, `s_3(K)>=gamma`, either aggregate physical third-volume smoothing gives

`||p_Q||inf < 64.617 gamma^(-1)`

with a continuous density, or one unit carrier direction has more than half its squared mass on at most 256 original coordinates. The r39 proof keeps arbitrary same-side curvature and uses a literal original-coordinate cut; no random source is rotated.

All relevant corrections remain active. In particular: small matrix norm is not a uniformly small random quadratic perturbation on arbitrary unbounded product inputs; independence cannot be claimed after spectral rotation; no law-uniform scalar pointwise oscillatory decay is used; no worst conditional projection-density moment is used; and a single uniformly good physical minor is not inferred from aggregate volume.

### Same-run source reconciliation

The early checkpoint in this run proved the correct rank-three endpoint by Theorem F and initially identified the rank-four-to-rank-three transition as the next debt. A later fresh partner query found fleet03/B09 r39, already completed at 19:07 UTC, which pays that transition whenever the carrier is diffuse and reduces the general exact carrier to finite physical localization. The early theorem remains correct, but its stated frontier is superseded by r39. The mathematics below starts from that stronger current endpoint rather than duplicating the obsolete frontier.

## 2. Partner receiver used here

I use two completed statements from r39.

First, if `B=A[J,I]` is a literal original-coordinate cross block and

`Z_3(B)=e_3(BB^T)`,

with size-three volume row marginals `alpha_j<=1/2` on the row bank, then

`boxed: ||p_Q||inf <= 6 sqrt(2e) Z_3(B)^(-1/6).`                 (2.1)

The density is continuous and every interval `L` obeys the same coefficient times `|L|`. All same-side quadratic blocks remain in the phase.

Second, for a rank-`r` matrix `B` with left range frame `U`, its size-three volume marginal satisfies

`alpha_i <= (P_range(B))_ii`.                                    (2.2)

These are aggregate statements: all physical minors are paid before taking a reciprocal power.

## 3. New parameterized carrier-localization theorem

The fixed `1/2 on 256 coordinates` endpoint of r39 can be tuned continuously. This is useful because later hub/pivot routing may need the carrier direction to be much more concentrated than one half.

### Theorem `QFORM-R4-CARRIER-ETA-LOCALIZATION-FORK-v1`

Let

`A=D+V K V^T`,                                                   (3.1)

where

- `D` is diagonal in the ORIGINAL independent coordinates;
- `V in R^(n x r)`, `V^T V=I_r`;
- `r in {3,4}`;
- `K=K^T` is invertible;
- `s_3(K)>=gamma>0`.

Fix any

`0<eta<=1`.                                                      (3.2)

Then at least one of the following holds.

**(A) aggregate physical-cross payment:** `Q=X^TAX` has a continuous density and

`boxed:
 ||p_Q||inf
 <= [24 sqrt(2e)]/[gamma sqrt(eta(2-eta))].`                     (3.3)

The same coefficient gives `P{Q in L}<=C|L|` for every interval `L`.

**(B) strong finite original-coordinate localization:** there are a set `H` of original coordinates and a unit `u in R^r` such that

`boxed:
 |H| <= 64 eta^(-2),
 ||(Vu)_H||_2^2 > 1-eta.`                                       (3.4)

Thus the localization mass can be driven arbitrarily close to one at a finite, explicit cost in physical support size; no approximation of the random quadratic form is made.

### Proof

Write the physical rows of `V` as `v_i^T` and their carrier leverages as

`ell_i=||v_i||_2^2`, `sum_i ell_i=r<=4`.                         (3.5)

Set

`delta=eta^2/16`,
`H={i: ell_i>delta}`, `L=H^c`.                                  (3.6)

Then

`|H| delta < sum_i ell_i=r<=4`,

so

`boxed: |H|<=4/delta=64 eta^(-2).`                               (3.7)

Let

`G_L=V_L^T V_L`, `G_H=I_r-G_L`.                                 (3.8)

If `lambda_min(G_L)<eta`, choose a unit `u` realizing that Rayleigh quotient. Then

`||(Vu)_H||_2^2
 =u^T G_Hu
 =1-u^T G_Lu
 >1-eta`,                                                       (3.9)

which is alternative (B).

Assume therefore

`G_L>=eta I_r`.                                                   (3.10)

Randomly put each coordinate of `L` into a row bank `J` with probability `1/2`, independently, and put every heavy coordinate in the opposite bank `I`. Set

`G_J=sum_(j in J) v_jv_j^T`, `G_I=I_r-G_J`.                     (3.11)

Since the Bernoulli fluctuations have mean zero,

`E ||G_J-G_L/2||_F^2
 =(1/4) sum_(j in L) ||v_jv_j^T||_F^2
 =(1/4) sum_(j in L) ell_j^2
 <=(delta/4) sum_(j in L) ell_j
 <=delta r/4
 <=delta.`                                                       (3.12)

Hence one literal original-coordinate partition satisfies

`||G_J-G_L/2||op
 <=||G_J-G_L/2||F
 <=sqrt(delta)=eta/4.`                                           (3.13)

Using (3.10) and `G_L<=I_r`,

`G_J >= (eta/4) I_r`,                                           (3.14)

while

`G_J <= (1/2+eta/4)I_r`,
`G_I=I_r-G_J >= ((2-eta)/4)I_r`.                                (3.15)

Because `D` is physically diagonal, it contributes nothing to the cross block

`B=A[J,I]=V_J K V_I^T`.                                         (3.16)

Normalize the two restricted frames by their Gram matrices. The nonzero singular values of `B` are those of

`G_J^(1/2) K G_I^(1/2)`,                                        (3.17)

so

`s_3(B)
 >= sqrt(eta/4) gamma sqrt((2-eta)/4)
 = (gamma/4) sqrt(eta(2-eta)).`                                 (3.18)

Consequently

`Z_3(B)>=s_1(B)^2s_2(B)^2s_3(B)^2>=s_3(B)^6`.                   (3.19)

Because `K` and `G_I` are invertible, `range(B)=range(V_J)`. For any selected row `j in J`, (3.14) and the fact that `j` is light give

`(P_range(B))_jj
 =v_j^T G_J^(-1)v_j
 <=(4/eta) ell_j
 <=(4/eta)delta
 =eta/4
 <=1/4.`                                                        (3.20)

The r39 range-leverage lemma therefore gives every size-three volume marginal `alpha_j<=1/4<1/2`. Applying the completed aggregate receiver (2.1) and (3.18),

`||p_Q||inf
 <=6sqrt(2e)/s_3(B)
 <=24sqrt(2e)/[gamma sqrt(eta(2-eta))],`                         (3.21)

which is alternative (A). Its Fourier envelope is integrable, hence the density is continuous and the interval estimate is linear. QED.

### Checks and useful fixed choices

At `eta=1/2`, (3.3)--(3.4) reproduce r39's fixed fork:

`C=64.6164134606 gamma^(-1)`, `|H|<=256`, mass `>1/2`.

At `eta=1/4` one gets

`boxed: C<84.603 gamma^(-1), |H|<=1024, mass>3/4.}`              (3.22)

At `eta=1/8` one gets

`boxed: C<115.590 gamma^(-1), |H|<=4096, mass>7/8.}`             (3.23)

The point is not the numerical constant; it is that failure of the paid branch forces an arbitrarily high fraction of one carrier direction onto a quantitatively finite set of physical source coordinates.

## 4. Actual application to the r38 exact dual-zero carrier

Fleet03/B09 r38 proves that at exact two-sided singleton aggregate zero, away from its coloop endpoints, the rank-two hub/star matrix has

`A=D_0+S`, `rank S<=4`,                                          (4.1)

where `D_0` is physical diagonal and the carrier is built in the original two bank coefficient planes. If the owner target holds and

`||D_0||op<=tau<1`,                                              (4.2)

then its spectral corollary gives

`gamma:=s_3(S)>=1-tau.`                                         (4.3)

Apply Theorem 3 with an orthonormal frame for `range(S)`. For every fixed `eta in (0,1]`, either

`boxed:
 ||p_Q||inf
 <= [24sqrt(2e)]/[(1-tau)sqrt(eta(2-eta))]`                     (4.4)

with a continuous density and direct linear interval bound, or a unit vector of `range(S)` carries more than `1-eta` of its squared mass on at most `64 eta^(-2)` original coordinates.

This upgrades the r39 fixed localization fork into a tunable structural endpoint. The residual case in r38, where

`A=D_0+S+E`                                                      (4.5)

with nonzero block-diagonal `E`, is NOT covered by (4.4): no norm-smallness of `E` is used to delete it.

## 5. Target-valid overlapping Walsh family: uniform through rank four -> rank three

The partner theorem can be applied to an actual inequality in the precise hard geometry that motivated the early checkpoint.

Let `N` be a Walsh size with `N>=8`. On two disjoint ORIGINAL-coordinate banks, choose orthonormal two-frames `P_N,C_N`, each with every row leverage `2/N`. Their two columns overlap on all coordinates of their own bank; the two projected coordinates within a bank are generally dependent.

Let

`W=diag(P_N,C_N)`,                                               (5.1)

and in the four-dimensional coefficient space define

`K_epsilon = [[N_0,I_2],[I_2,M_epsilon]],`                      (5.2)

where

`N_0=diag(1,0)`, `M_epsilon=diag(1+epsilon,0)`, `epsilon>=0`.

Equivalently, after grouping the first coefficient of each bank and then the second,

`K_epsilon`

is the direct sum of

`[[1,1],[1,1+epsilon]]`

and

`[[0,1],[1,0]]`.                                                 (5.3)

Hence its spectrum is

`{1,-1,
  (2+epsilon+sqrt(4+epsilon^2))/2,
  (2+epsilon-sqrt(4+epsilon^2))/2}.`                             (5.4)

For every `epsilon>=0` there are at least three eigenvalues of modulus at least one. At `epsilon=0` the carrier rank is exactly three. For every `epsilon>0` it is rank four, but the fourth singular value tends to zero like `epsilon/2` as `epsilon downarrow0`. All physical cross and same-side carrier coefficients are `O(1/N)`. Because both same-side blocks lie inside their respective rank-two cross planes, every r38 singleton augmented third-volume on both sides is exactly zero.

Now add **any physical diagonal matrix** `D`; it need not be small for the analytic estimate below. Put

`A_epsilon=D+W K_epsilon W^T`.                                  (5.5)

Choose on each source bank a third Walsh character independent of the two frame columns, and put the `+1` half of each bank into the row side `J` and the `-1` half into the column side `I`. Then exactly

`W_J^T W_J=W_I^T W_I=I_4/2`.                                   (5.6)

The physical diagonal `D` contributes no cross term, so

`B=A_epsilon[J,I]=W_J K_epsilon W_I^T`.                          (5.7)

The nonzero singular values of `B` are exactly one half those of `K_epsilon`. Therefore

`Z_3(B)
 = (1/64) e_3(sing(K_epsilon)^2).`                               (5.8)

If the two positive eigenvalues of the first block are `a,b`, then `ab=epsilon` and

`a^2+b^2=(2+epsilon)^2-2epsilon=4+2epsilon+epsilon^2`.           (5.9)

Together with the two unit singular values from the hyperbolic block,

`e_3(sing(K_epsilon)^2)
 =a^2+b^2+2a^2b^2
 =4+2epsilon+3epsilon^2`.                                       (5.10)

Thus

`boxed: Z_3(B)=(4+2epsilon+3epsilon^2)/64 >=1/16.}`              (5.11)

For a selected physical row, the full normalized range leverage is at most

`2*(2/N)=4/N<=1/2`;                                              (5.12)

when `epsilon=0` the actual rank-three range leverage is no larger. By the partner marginal lemma the row-volume gate holds. The r39 aggregate receiver therefore gives, uniformly for every `epsilon>=0`, every physical diagonal `D`, and every admissible independent cap-one source law,

`boxed:
 ||p_(X^T A_epsilon X)||inf
 <= 6sqrt(2e) (1/16)^(-1/6)
 = 6sqrt(2e) 2^(2/3)
 = 22.2075246553... .}`                                         (5.13)

The same coefficient multiplies interval length, and the density is continuous.

At `D=0` this is a genuine owner-target family for every `epsilon>=0`, including the exact rank-three endpoint. Thus the apparent small-fourth-singular-value obstruction from the early checkpoint is not a real obstruction in the diffuse carrier: aggregate physical third-volume smoothing passes through the rank drop with a fixed constant while keeping the dense same-side rank-one blocks. No spectral-tail term is discarded.

This is the required actual use of the newest designated partner result at an equation-level target inequality.

## 6. Required pinned mixed-hub theorem on an actual source-coordinate star

The completed Theorem H at the owner-pinned `e5f71d79...` source is also applied directly.

Take one literal physical hub `h` and an `m`-coordinate leaf bank `I`, with `m` a Walsh size at least eight. Choose three flat orthonormal Walsh vectors

`c,v_1,v_2 in R^m`                                               (6.1)

and consider the source-coordinate star with dense same-side leaf curvature

`Q_0
 =2 X_h <c,X_I>
  +<v_1,X_I>^2+<v_2,X_I>^2.`                                    (6.2)

The active matrix on the coefficient basis `{e_h,c,v_1,v_2}` has spectrum

`{1,-1,1,1}`.                                                    (6.3)

Thus this is a literal target instance. More generally arbitrary blocks on a disjoint outside bank `J`, arbitrary hub self-curvature, arbitrary hub-to-`J` and leaf-to-`J` couplings, and arbitrary affine terms may be retained exactly at the theorem's scope; the displayed principal block already forces at least three positive eigenvalues at least one in any full extension by interlacing.

For each physical leaf coordinate the mixed row is

`rho_i=((v_1)_i,(v_2)_i,c_i)`,                                  (6.4)

so

`sum_i rho_i rho_i^T=I_3`,
`rho_i^T rho_i=3/m<=1/2`.                                       (6.5)

Theorem H with one hub and two same-side squares gives the direct characteristic-function envelope

`boxed: |phi_Q(t)|<=8 pi^2 |t|^(-2).}`                           (6.6)

Integrating `min(1,8pi^2|t|^-2)` exactly,

`boxed: ||p_Q||inf<=4sqrt(2)<5.657,}`                            (6.7)

and hence

`boxed: P{Q in L}<=4sqrt(2)|L|.}`                                (6.8)

The two dense leaf squares are retained in original source coordinates. The projections `<v_1,X_I>`, `<v_2,X_I>`, and `<c,X_I>` are never asserted independent. There is no probability squaring and no square-root small-ball loss.

## 7. Why the strong localization certificate still cannot be truncated

The parameterized fork makes the remaining geometry increasingly finite-dimensional, but it does **not** authorize deletion of the light tail.

For any `0<eta<1`, let

`v=sqrt(1-eta)e_1+sqrt(eta)e_2`.                                 (7.1)

The coefficient direction has mass `1-eta` on the single coordinate `{1}`. Nevertheless choose admissible independent cap-one laws

`X_1 ~ Uniform[0,1]`,
`X_2 ~ Uniform[eta^(-1/2), eta^(-1/2)+1]`.                       (7.2)

Then

`sqrt(eta) X_2 in [1,1+sqrt(eta)]`,                              (7.3)

so the nominally `eta`-small coefficient tail contributes order one to `v^T X`. In particular the difference between `(v^T X)^2` and `(sqrt(1-eta)X_1)^2` is not uniformly small as `eta downarrow0` over the allowed product laws.

This is not a QFORM counterexample. It is a source-valid obstruction to turning (3.4) into a bounded-support perturbation argument. Any closure of the localized branch must keep the tail in the phase, use a physical cross-volume/pivot receiver, or make a product-preserving quotient/conditioning move whose bound is uniform in the frozen values.

## 8. Current first unpaid implication

The new first B09 debt is

`QFORM-R4-CARRIER-STRONG-LOCALIZED-HUB-OR-RESIDUAL-CROSSING-v1`:

1. Starting from alternative (B) of Theorem 3 for a fixed useful `eta` (for example `eta=1/4`, giving `>3/4` mass on at most 1024 original coordinates), route the finite original-coordinate set into an already-paid physical hub/fixed-pair/projected-crossing theorem, or iterate an exact product-preserving quotient split. The light tail must remain in the phase.
2. In parallel, extend the exact-carrier crossing argument to r38's quantitative decomposition `A=D_0+S+E` with nonzero retained block-diagonal residual `E`. The residual may be compiled through its own literal cross volume, but may not be declared probabilistically negligible from Frobenius/operator smallness alone.

The diffuse exact diagonal-plus-rank-three/rank-four carrier, including the rank-four-to-rank-three transition, is now paid. The remaining exact-carrier obstruction is finite physical localization, not diffuse fourth-mode instability.

Full-target essential boundedness: **OPEN**.  
Full-target continuous density: **OPEN**.  
No valid counterexample was found in this run.
