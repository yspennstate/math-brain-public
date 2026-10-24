SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T22:24:40Z.
attacking: the shared-hub near-coloop receiver; turn the account02/B10 pure-longitudinal recombination into an arbitrary-rough-law theorem and identify the exact structural gate that remains in the generic coupled collar.

# account01/B10 — rough-law three-bank hyperbolic-square receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Assignment: rank-three coupled case  
Status: `NEW_ANALYTIC_RECEIVER / PARTNER_RESULT_APPLIED / ROUGH-LAW_SPECIAL_BRANCH_CLOSED / GENERIC_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction boundary

Fresh brain control was resolved from `yspennstate/math-research-brain` main at the start of this run and refreshed before publication. OWNER CONTROL remains revision `2026-09-22.15`, with QFORM as the sole research target. The full unrestricted theorem and unrestricted continuity claim remain open.

This report explicitly preserves the live corrections: no independence is inferred after a spectral rotation; no arbitrary-joint coarea cap, conditional projection-density supremum, pointwise van-der-Corput decay, moment assumption, support regularity, fragment-count bound, or small-random-perturbation deletion is used. The argument below uses independence only between disjoint ORIGINAL-coordinate banks.

The immediate account01/B10 predecessor is

`yspennstate/math-open-problems@8103579cff840cf3e09607ac05841bd156fa8744`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T184744Z-account01-B10-QFORM-auto11/REPORT.md`.

It showed that in the diffuse ultra-coloop state the hub-containing rank-three determinant mass stays order one while fully disjoint three-basis determinant entropy necessarily loses the coloop factor. Its first unpaid implication was a shared-hub receiver.

The designated partner result actually used here is account02/B10:

`yspennstate/math-open-problems@ca0549ef8c582478415aba1a953bdc6115fe84c6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T214702Z-account02-B10-QFORM-auto11/REPORT.md`.

The partner supplied an exact target-valid near-coloop family and, crucially, the ORIGINAL-bank identity

`Q_rho = 2 ZY + W^2`,                                                 (1.1)

with `Z,Y,W` depending on three disjoint original-coordinate banks. Its displayed global bound used uniform non-hub laws and was `<128.51`; the partner explicitly left arbitrary rough cap-one gluing as the generic endpoint problem.

## 2. A sharp elementary half-potential lemma

### Lemma 2.1

If `S` has a probability density `f` with `0<=f<=K`, then

`sup_a E |S-a|^(-1/2) <= 2 sqrt(2K)`.                                (2.1)

Proof. For fixed `a`, the kernel `|x-a|^(-1/2)` is symmetric decreasing away from `a`. Among all densities of mass one bounded by `K`, its integral is maximized by the bathtub profile `K 1_{|x-a|<=1/(2K)}`. Therefore

`int f(x)|x-a|^(-1/2) dx
 <= K int_{-1/(2K)}^{1/(2K)} |u|^(-1/2) du
 = 2 sqrt(2K)`.

No moment or support hypothesis appears. QED.

## 3. Main analytic receiver

### Theorem 3.1 — `QFORM-THREE-BANK-HYPERBOLIC-SQUARE-RECEIVER-v1`

Let `Z,Y,W` be mutually independent real random variables with probability densities bounded by `K_Z,K_Y,K_W`. Let `s,d` be nonzero real numbers and `b,c` arbitrary. Define

`Q = 2s ZY + bY^2 + 2cYW + dW^2`.                                   (3.1)

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <= 4 sqrt(2) K_W sqrt(K_Z K_Y) / sqrt(|s d|).`                       (3.2)

The statement is completely insensitive to fragmentation of any of the three input densities.

#### Proof

Complete the `W` square:

`Q = d (W+(c/d)Y)^2 + 2sZY + kappa Y^2`,

where

`kappa = b-c^2/d`.                                                     (3.3)

Fix `(Y,Z)`. Since `W` is independent of `(Y,Z)`, the conditional variable `W+(c/d)Y` has a translate of the density of `W` and hence the same cap `K_W`. The pushforward of a density bounded by `K_W` under `w -> d w^2` has density bounded by

`K_W / (sqrt(|d|) sqrt(|u|))`                                        (3.4)

on the appropriate one-sided support. Consequently, for almost every `q`,

`p_Q(q)
 <= K_W |d|^(-1/2)
    E |q-(2sZY+kappa Y^2)|^(-1/2).`                                  (3.5)

Now condition on `Y=y`. Since

`2s y Z+kappa y^2 = 2s y (Z+kappa y/(2s))`,                          (3.6)

Lemma 2.1 gives, for `y !=0`,

`E_Z |q-(2s y Z+kappa y^2)|^(-1/2)
 <= |2sy|^(-1/2) 2 sqrt(2K_Z)
 = 2 sqrt(K_Z/|s|) |y|^(-1/2).`                                     (3.7)

The exceptional event `Y=0` has probability zero because `Y` has a density. Averaging (3.7) and applying Lemma 2.1 to `Y` at `a=0`,

`sup_q E |q-(2sZY+kappa Y^2)|^(-1/2)
 <= 2 sqrt(K_Z/|s|) E|Y|^(-1/2)
 <= 4 sqrt(2) sqrt(K_Z K_Y/|s|).`                                   (3.8)

Insert (3.8) into (3.5) to obtain (3.2). Since every conditional `W`-square pushforward is absolutely continuous, their mixture is absolutely continuous; (3.2) is an essential density bound. QED.

### 3.2 Triangular stability actually used by the proof

The same proof permits the shifts in (3.3) to depend on already-conditioned banks. More precisely, if three independent original-coordinate blocks carry scalar observables `Z,Y,W` with the same density caps and

`Q = d(W+eta)^2 + 2sY(Z+xi) + chi`,                                  (3.9)

where, at the first peel, `eta` is measurable with respect to the `Z`- and `Y`-blocks, while `xi,chi` are measurable with respect to the `Y`-block, then (3.2) is unchanged. The proof conditions first on the first two blocks, so `eta` is only a translation of `W`; it then conditions on the `Y` block, so `xi` and `chi` are only a translation of `Z` and of the target level. This is the exact source-valid sense in which the receiver tolerates shears.

This triangular formulation is useful for the generic collar: it shows that arbitrary roughness is not itself the obstruction. What is still missing is a structural decomposition of the mixed transverse leaves into three source-disjoint banks with this triangular dependence.

## 4. Rank-three null-axis corollary

The receiver has a clean exact-rank-three interpretation.

Let

`A=R M R^T`, `R^T R=I_3`,                                            (4.1)

where `M` is real symmetric, invertible, and its three eigenvalues satisfy `|lambda_j(M)|>=1`. Put

`D=|det M|`.

Assume there is a unit vector `r` with

`r^T M r=0`.                                                          (4.2)

Set

`s=||Mr||>0`, `v=Mr/s`,                                                (4.3)

and let `q` complete `(r,v,q)` to an orthonormal basis. In this basis symmetry gives

`M = [[0,s,0],[s,b,c],[0,c,d]]`.                                     (4.4)

Its determinant is

`det M = -s^2 d`, so `d!=0` and

`D=s^2 |d|`.                                                          (4.5)

Suppose, now as an ORIGINAL-coordinate structural hypothesis, that the physical rows of `R` split into three disjoint banks `B_r,B_v,B_q` and every row in those banks is respectively parallel to `r,v,q`. Then the three spectral projections can be written

`R^T X = Z r + Y v + W q`,                                            (4.6)

where `Z,Y,W` are functions of disjoint original-coordinate banks and hence are genuinely independent. Parseval `R^TR=I_3` forces the coefficient vector of each of `Z,Y,W` to have Euclidean norm one.

The standard one-dimensional orthonormal-projection density theorem for independent cap-one coordinates therefore gives

`K_Z,K_Y,K_W <= sqrt(2)`.                                             (4.7)

Substitution of (4.4)-(4.6) gives exactly (3.1). Hence Theorem 3.1 implies

`||p_Q||_infinity <= 8 sqrt(2) / sqrt(|s d|)
                   = 8 sqrt(2) sqrt(s/D).`                            (4.8)

Because `M` is symmetric and every singular value is at least one,

`s <= ||M|| <= |det M|=D`,                                           (4.9)

and therefore

`boxed: ||p_Q||_infinity <= 8 sqrt(2) < 11.314.`                      (4.10)

This closes every exact-rank-three null-axis form satisfying the three-disjoint-rank-one-bank geometry, for arbitrary cap-one source laws. It is not the generic rotated theorem: arbitrary mixed transverse rows do not satisfy the bank-alignment hypothesis.

Continuity is not asserted by this argument. The proven output here is existence of an essentially bounded density.

## 5. Designated partner applied to an actual inequality

Account02/B10's completed family has, for `0<=rho<1/64` and `c_0=1-rho`,

`u_0=sqrt(c_0)e_1`, `u_1=sqrt(rho)e_1`,

sixty-four rows `e_2/8`, sixty-four rows `e_3/8`, and

`M=[[0,1,0],[1,0,0],[0,0,1]]`.                                      (5.1)

Thus the nonzero spectrum is exactly `{-1,1,1}` and the partner proved the source-valid identity

`Q_rho = 2 ZY + W^2`,                                                 (5.2)

where

`Z=sqrt(c_0)H+sqrt(rho)P`,
`Y=(1/8) sum_{i=1}^{64} U_i`,
`W=(1/8) sum_{i=1}^{64} V_i`,                                        (5.3)

with the three aggregates depending on disjoint original-coordinate banks.

Here is the new actual inequality. Let **every** physical original in (5.3) have an arbitrary probability density bounded by one; no uniform, compact-support, connected-support, or finite-fragment assumption is imposed. Since convolution does not increase `L^infinity`, scaling the hub gives

`K_Z <= c_0^(-1/2)`.                                                  (5.4)

The coefficient vectors of `Y` and `W` have norm one, so the one-dimensional projection theorem gives

`K_Y,K_W <= sqrt(2)`.                                                 (5.5)

Applying Theorem 3.1 to (5.2), with `s=d=1`,

`||p_{Q_rho}||_infinity
 <= 4 sqrt(2) K_W sqrt(K_Z K_Y)
 <= 8 * 2^(1/4) c_0^(-1/4).`                                        (5.6)

Since `c_0>63/64`,

`boxed: ||p_{Q_rho}||_infinity
 < 8*2^(1/4)*(64/63)^(1/4)
 < 9.552.`                                                           (5.7)

This improves the partner's `<128.51` global payment and, more importantly, removes its specialization of the non-hub laws to uniforms. The bound is uniform in `rho`, including `rho=0`, and is insensitive to arbitrary or infinite fragmentation of the physical hub and of every other original density.

Equation (5.7) is the required application of a completed `account02/B10` result to an actual inequality: the partner's exact ORIGINAL-bank factorization (5.2) is the input, and the new receiver pays the whole output for all target-admissible cap-one sources in that exact matrix family.

## 6. Why this does not silently prove the generic ultra-coloop collar

In the generic ultra-coloop state from the preceding B10 run,

`u_0=sqrt(h)r`, `u_i=t_i r+p_i`,

with

`sum_i t_i^2=1-h`, `sum_i t_i p_i=0`, `sum_i p_i p_i^T=I_2`,          (6.1)

and the transverse rows `p_i` are generally mixed in both transverse directions. Even at the exact-null spectral endpoint `r^TMr=0`, after choosing `v=Mr/||Mr||` and `q`, the quadratic form depends on the totals

`Z_tot=sqrt(h)H+sum_i t_i X_i`,
`Y_tot=sum_i <p_i,v>X_i`,
`W_tot=sum_i <p_i,q>X_i`.                                             (6.2)

The Parseval identities make the three coefficient vectors in (6.2) orthogonal in coefficient space, but they are not independent random variables because the same original leaf may occur in all three sums. Declaring them independent would be exactly the forbidden post-rotation/product-provenance error.

Theorem 3.1 shows something more precise than a generic special-case bound: if one can reorganize the original leaves into three source-disjoint banks so that, after exact shears, the dependence becomes triangular as in (3.9), then arbitrary rough cap-one laws cost no fragmentation functional and no leakage factor. The generic obstruction is therefore a **bank-separation/gluing obstruction**, not a failure of the half-potential estimate.

The current predecessor's volume law still supplies order-one hub-containing third-rank currency:

`sum_{i<j} |det A[{0,i,j}]| = Dh`,                                   (6.3)

and a disjoint leaf-pair law with leaf incidences at most `1/2`; but (6.3) alone does not produce the source-disjoint triangular factorization (3.9). A volume-sampled pair can remain spread over many mixed rows, and one cannot split a single original random variable into independent longitudinal and transverse pieces.

Thus the next unpaid implication is sharpened to

`QFORM-SHARED-HUB-TRIANGULAR-BANK-GLUING-v1`:

> From the generic diffuse near-coloop geometry, either construct a source-disjoint three-bank triangular representation to which Theorem 3.1 applies with order-one `|sd|`, or replace the last two scalar peels by a product-preserving grouped Fourier argument that spends the same hub-containing pair-volume currency without splitting any original coordinate.

The fresh grouped projected-crossing theorem is compatible with the second option, but its one-hub `k=1, ell=2` currency in the present ultra-coloop state is the already-identified `hD^2(1-h)` scale and therefore still degenerates. The new receiver explains what a successful replacement has to preserve: the hub/leakage aggregate must survive as a whole until after one genuinely source-disjoint transverse smoothing resource has been spent.

## 7. Scope table

- Three-bank receiver (Theorem 3.1): **PROVED**, arbitrary rough densities with explicit caps.
- Exact-rank-three null-axis, three disjoint rank-one banks: **PROVED**, `||p_Q||_infinity<=8sqrt(2)`.
- account02/B10 exact near-coloop family, now all arbitrary cap-one originals: **PROVED**, `||p_Q||_infinity<9.552` uniformly to `rho=0`.
- Generic mixed-row near-coloop collar: **OPEN**.
- Arbitrary exact rank three: **OPEN**.
- Full owner QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity for the new rough-law receiver: **NOT CLAIMED**; only an essentially bounded density is proved.

## 8. First essential missing implication for the next run

Attempt `QFORM-SHARED-HUB-TRIANGULAR-BANK-GLUING-v1` immediately. The two plausible mechanisms are:

1. a deterministic original-coordinate partition driven by the existing pair-volume law `w_ij=det(p_i,p_j)^2`, with one bank reserved for the hub/leakage aggregate and the other two providing the two scalar peels without reusing an original coordinate; or
2. a grouped Fourier version of Theorem 3.1 in which the `Y` and `W` scalar density caps are replaced by complex pushforwards of two disjoint original-coordinate banks, allowing arbitrary internal same-bank curvature while retaining the same `|sd|^(-1/2)` cost.

A proof must keep the exact live correction boundary: no conditional density cap after projecting mixed coordinates, no independence of `(Z_tot,Y_tot,W_tot)`, and no perturbative deletion based only on `sum t_i^2`.
