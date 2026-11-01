# Diffuse spectral-window frontier and robust diffuse-core leakage

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet01/B08` — Diffuse eigenvector case  
Run: `20260923T134051Z-fleet01-B08-qform-r30`  
Status: **PROVED SUPPORTING THEOREMS / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture is not claimed solved. The full continuity conclusion is likewise open. The results below prove a quantitatively stronger diffuse exit and make that exit stable under an arbitrary dense nonseparable operator tail, while preserving the true product coordinates.

## 1. Sources actually used

1. Current one-scale ridge theorem and its perturbation estimate:
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

   For an original-coordinate cross block `B`, `gamma>0`,
   
   `K=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K`,
   
   if `max_i K_ii<=q/2` and `theta>2q`, `1<=q<=2`, the full ambient quadratic form has a continuous `C_0` density with
   
   `||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.
   
   The same source proves: if `B=B0+F`, `||F||<=eta`, and the range projection of `B0` has diagonal at most `ell0`, then
   
   `K_ii <= (sqrt(ell0)+eta/gamma)^2`.

2. Designated partner fleet02/B08 r27:
   `yspennstate/math-open-problems@41ee49f6e9c3383e4c3a322bdc52779768a17eb7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T130941Z-fleet02-B08-qform-diffuse-r27/REPORT.md`.

   In particular its exact diffuse family
   
   `A_m^diff=[[u1 u1^T, B_m],[B_m,u1 u1^T]]`, `B_m=u2u2^T+u3u3^T`,
   
   has nonzero spectrum `{-1,-1,1,1,1,1}` and full physical-range leverage `3/m`. This source-valid family is used below in an actual perturbative inequality.

3. Current corrections were refreshed before publication. In particular no law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea bound, fiber-sup shortcut, or probabilistic deletion of a small matrix tail is used.

## 2. Main theorem: `QFORM-DIFFUSE-WINDOW-FRONTIER-v1`

Let `L>0`. Let `A` be a real symmetric matrix with at least three eigenvalues of modulus at least `L`. Fix `0<tau<1`, and let

`P_tau = 1_{|A|>=tau L}`

be the spectral projection onto **all** eigenspaces whose eigenvalues have modulus at least `tau L`. Suppose

`max_i (P_tau)_{ii} <= ell`.

Define

`delta = 1/2 - sqrt(2 ell) - ell`,

`sigma = delta-tau`.

Assume `sigma>0`. Let `q in [1,2]` and `r>0` satisfy

`h := (sqrt(ell/delta)+tau/(r sigma))^2 <= q/2`,                       (2.1)

`theta0 := 3/(1+r^2) > 2q`.                                          (2.2)

Then for every independent real input vector whose one-dimensional probability densities are bounded by one, `Q=X^T A X` has a continuous density vanishing at infinity and

`||p_Q||_infinity`

`<= sqrt(e)/(sqrt(2q) r sigma L) * theta0/(theta0-2q)`                 (2.3)

`= 3 sqrt(e) / [sqrt(2q) r sigma {3-2q(1+r^2)} L]`.                   (2.4)

All eigenvalues below the chosen window are retained. They may be nonzero, of either sign, arbitrarily numerous, and arbitrarily oriented.

### Proof

Write the exact spectral decomposition

`A=A_H+E`,

where `A_H=U Lambda U^T` contains **every** eigenspace with `|lambda|>=tau L` and `E` contains the complementary spectral part. Thus

`||E||<tau L`,                                                        (2.5)

`U^T U=I`, and every physical row `u_i` of `U` satisfies

`||u_i||^2=(P_tau)_{ii}<=ell`.                                        (2.6)

Also `Lambda` contains the three target eigenvalues, hence

`s_3(Lambda)>=L`.                                                     (2.7)

Apply the two-part MSS frame partition to the tight frame `(u_i)`. There is an original-coordinate partition `I union J` such that both partial Gram matrices

`M_I=U_I^T U_I`, `M_J=U_J^T U_J`

have operator norm at most

`(1/sqrt(2)+sqrt(ell))^2 = 1/2+sqrt(2ell)+ell = 1-delta`.

Because `M_I+M_J=I`, the same two matrices satisfy

`M_I>=delta I`, `M_J>=delta I`.                                      (2.8)

Consider the high-window cross block

`B0=(A_H)[I,J]=U_I Lambda U_J^T`.

Since both restricted frames have full column rank, write

`U_I=W_I M_I^(1/2)`, `U_J=W_J M_J^(1/2)`

with `W_I,W_J` having orthonormal columns. Hence the nonzero singular values of `B0` are those of

`M_I^(1/2) Lambda M_J^(1/2)`.

Using (2.8) and (2.7),

`s_3(B0)>=delta L`.                                                   (2.9)

Moreover `range(B0)=range(U_I)`. Its physical range projection equals

`Pi_0=U_I M_I^(-1) U_I^T`,

so for `i in I`,

`(Pi_0)_{ii}=u_i^T M_I^(-1)u_i <= ell/delta`.                         (2.10)

Now restore the complete matrix. Its actual cross block is

`B=A[I,J]=B0+F`, `F=E[I,J]`,

and `||F||<=tau L`. Weyl gives

`s_3(B)>= (delta-tau)L = sigma L`.                                   (2.11)

Set

`gamma=r sigma L`.

The deterministic ridge-leverage perturbation estimate from source 1, applied to (2.10), yields

`max_i K_gamma(ii)`

`<= (sqrt(ell/delta)+tau L/gamma)^2`

`= (sqrt(ell/delta)+tau/(r sigma))^2`

`=h<=q/2`.                                                           (2.12)

On the other hand, (2.11) supplies three singular values at least `sigma L`. Therefore

`theta_gamma=tr K_gamma`

`>=3 * (sigma L)^2/(gamma^2+(sigma L)^2)`

`=3/(1+r^2)=theta0>2q`.                                              (2.13)

The one-scale ridge theorem applies to the **full ambient form**, with all self blocks, outside couplings and the actual low-window tail retained. It gives

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)`.

The function `theta/(theta-2q)` decreases for `theta>2q`. Use (2.13) and `gamma=r sigma L` to obtain (2.3)-(2.4). The ridge theorem also supplies `p_Q in C_0`. QED.

### Why this is not the prohibited perturbation shortcut

The low-window matrix `E` is never replaced by an independent random error and never declared small after evaluating it on an unbounded random vector. Its only roles are deterministic matrix inequalities (2.5), (2.11), and (2.12); the final Fourier/ridge theorem is applied to the actual full cross block `B` and therefore to the original full quadratic form.

## 3. Explicit corollaries

### 3.1 Exact finite-range leverage `1/18`

For an exact finite-rank matrix with range projection `P` satisfying

`max_i P_ii<=1/18`,

apply the same proof with no tail. Here

`delta=1/9`.

Take `q=1`, `r=1/sqrt(6)`. Then

`ell/delta=1/2`, `theta0=18/7>2`.

Therefore

`||p_Q||_infinity <= 81 sqrt(3e)/(2L)`

`=115.654594839.../L`,                                               (3.1)

and the density is continuous `C_0`.

This cleanly expands the exact-range diffuse gate beyond the earlier `1/32` threshold.

### 3.2 Exact finite-range leverage `1/16`

The fractional parameter `q>1` pushes the exact-range gate further. If

`max_i P_ii<=1/16`,

then

`delta=(7-4sqrt(2))/16=0.0839466094067...`.

Choose

`q=149/100`, `r=1/20`.

Then

`ell/delta=(7+4sqrt(2))/17=0.744520838205... <149/200=q/2`,

while

`theta0=1200/401=2.99251870324... >2q=2.98`.

Thus

`||p_Q||_infinity <54394/L`,                                         (3.2)

continuously. The constant is intentionally not optimized; the point is the larger proved leverage region. In the formal limit `q->3/2`, `r->0`, this particular exact-range scheme reaches the leverage frontier

`ell < 39/98 - 3sqrt(30)/49 =0.0626188423438...`.                    (3.3)

No endpoint conclusion is asserted at equality because the time-integrability exponent degenerates there.

### 3.3 Deeper full spectral window with leverage `1/20`

Suppose instead that the actual spectral projection of `A` onto

`|lambda|>=L/128`

has diagonal at most `1/20`. Take

`tau=1/128`, `q=11/10`, `r=1/2`.

Then

`delta=0.133772233983162...`,

`sigma=0.125959733983162...`,

`h=0.540834642418502... <0.55=q/2`,

`theta0=2.4>2.2=2q`.

Consequently

`||p_Q||_infinity <211.795/L`,                                       (3.4)

with a continuous `C_0` density. This permits arbitrary dense spectrum below `L/128` and allows substantially more high-window coordinate leverage than the fixed `1/32` theorem.

## 4. New structural lemma: `QFORM-DIFFUSE-CORE-SPECTRAL-LEAKAGE-v1`

Let `H` be real symmetric and let `S` denote the orthogonal projection onto `range(H)`. Let

`A=H+E`, `||E||<=eps`.

For `a>0`, let

`P_a=1_{|A|>=a}`.

Then

`||(I-S)P_a|| <= eps/a`.                                             (4.1)

Hence if

`max_i S_ii<=ell0`,

then

`max_i (P_a)_{ii} <= (sqrt(ell0)+eps/a)^2`.                          (4.2)

### Proof

Take `x in range(P_a)`. Since every eigenvalue of `A` on this spectral subspace has modulus at least `a`, there is a unique `z in range(P_a)` with

`x=Az`, `||z||<=||x||/a`.

Because `range(H)` lies in `range(S)`, `(I-S)H=0`. Therefore

`||(I-S)x||=||(I-S)Ez||<=eps ||x||/a`,

proving (4.1). By adjoint symmetry, `||P_a(I-S)||=||(I-S)P_a||`. For each physical basis vector,

`||P_a e_i|| <= ||P_a S e_i||+||P_a(I-S)e_i||`

`<=sqrt(S_ii)+eps/a`.

Squaring gives (4.2). QED.

The lemma is useful precisely because it transfers **diffuseness of a low-rank spectral core to the actual spectral window of the full matrix** without deleting the remainder from the random quadratic form.

## 5. Required designated-partner application

Fleet02/B08 r27 supplies the exact target-valid diffuse family

`A_m^diff=[[u1u1^T,B_m],[B_m,u1u1^T]]`,

`B_m=u2u2^T+u3u3^T`,

with nonzero spectrum

`{-1,-1,1,1,1,1}`

and physical range leverage exactly `3/m` at every coordinate in the normalized Hadamard construction.

Scale that partner family by `L` and call the result `H`. Let `m>=128`. Add an **arbitrary symmetric matrix** `E`, with no rank, sign, support or eigenvector restriction, satisfying

`||E||<=L/1024`,

and put

`A=H+E`.

This is a real extension of the partner's exact family, not a deletion of the perturbation.

Weyl leaves at least three eigenvalues of `A` with modulus at least

`L0=(1-1/1024)L=(1023/1024)L`.                                       (5.1)

Use the actual `A`-spectral window

`|lambda(A)|>=tau L0`, `tau=1/32`.

The leakage lemma (4.2), with `ell0=3/m<=3/128`, gives

`ell <= (sqrt(3/128)+(L/1024)/(L0/32))^2`

`=(sqrt(3/128)+32/1023)^2`

`=0.033993645149794...`.                                             (5.2)

Apply Theorem 2 with the scale `L0`, and choose `q=1`, `r=3/5`. The actual numbers are

`delta=0.205262629519014...`,

`sigma=delta-1/32=0.174012629519014...`,

`h=0.498803848329426... <1/2`,

`theta0=75/34=2.20588235294...>2`.                                  (5.3)

Therefore the **full perturbed quadratic form** has a continuous `C_0` density and

`||p_Q||_infinity`

`<=119.636430375.../L0`

`<119.754/L`.                                                        (5.4)

This is the requested concrete application of a completed designated-partner result to an actual inequality. It shows that the diffuse rank-two-cross/one-child Hadamard family remains uniformly controlled after an arbitrary dense, high-rank, nonseparable operator perturbation of size `L/1024`. No moments or compact support are used.

For comparison, fleet02/B08 r27's exact unperturbed family was paid by a whole-range theorem with constant `6`; (5.4) is weaker numerically but has the materially larger scope of arbitrary dense operator perturbations.

## 6. Relation to the current B08 proof map

The result sharpens the distributed exit in two ways.

First, it replaces one fixed spectral-window point `(tau,ell)=(1/64,1/32)` by an explicit admissible frontier (2.1)-(2.2). Thus a consumer can optimize the window depth, allowed physical leverage and density constant for the actual survivor matrix instead of forcing a single threshold.

Second, (4.1)-(4.2) gives a rigorous way to pass from a genuinely diffuse spectral core to the **actual** high spectral projection of a full matrix under an operator tail. That is exactly the kind of full-spectrum stability missing from naive low-rank truncations.

This result complements, rather than replaces, the current low-cross-rank/high-leverage routes. In particular the singleton-plus-two-banks obstruction can have cross rank only two; no three-cross ridge theorem can pay it by itself. The newest leverage-free compiler in fleet01/B20 likewise leaves near-rank-one/rank-two and double-anchor packets. Those remain genuine aggregate branches.

## 7. First unpaid implication

`QFORM-HIGHWINDOW-HEAVY-LOWRANK-AGGREGATE-COMPILER-v1`:

Starting from failure of every admissible diffuse spectral-window point in Theorem 2, convert the resulting high coordinate leverage of `P_tau` into one of the already quantified physical low-rank/grouped-anchor currencies **without selecting only finitely many tiny scalar pivots**, and pay that currency while retaining arbitrary same-bank curvature and the full complementary spectrum.

The partner r27 Hadamard calculation is a stress test for the form this compiler must take: finite physical hub selection can lose powers of the bank size even when whole-range aggregation is dimension-free.

## 8. Verification and status

`CHECKS.py` and the executed `CHECKS.txt` in this run directory verify the displayed threshold inequalities and constants; output terminates `QFORM_B08_R30_CHECK_PASS`. These finite arithmetic checks are not substitutes for the analytic proof.

Independent end-to-end review of this new supporting theorem was not performed in this run and is not claimed. Since this is not a full-target proof, no full-solution review status is asserted.

The full conjecture remains **OPEN**. Continuity is proved only on the branches covered by Theorem 2 and its corollaries/application; it is not claimed for the unrestricted target.
