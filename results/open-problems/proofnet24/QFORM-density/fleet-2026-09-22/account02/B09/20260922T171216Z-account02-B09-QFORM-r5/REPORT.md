# QFORM-ZERODIAG-TRIANGLE-LOGSMOOTH-v1

Run: `20260922T171216Z-account02-B09-QFORM-r5`  
Worker: `account02/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Current owner control observed before publication: revision `2026-09-22.8`, brain main `de226dc67ba68b7aca9507746c55f636a4347e4d`  
Status: **ESSENTIAL_STEP_APPLIED; full conjecture remains OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The fleet target is the universal density bound for `Q=X^T A X` under arbitrary independent real input densities bounded by one and at least three eigenvalues `|lambda|>=1` of a real symmetric `A`.

The previous B09 run reduced one remaining structural branch to heavy/low-stable-rank grouped geometry. The current proof-first owner continuation additionally names the zero/near-isotropic physical-pivot branch as a priority. This run changes mechanism within the same target: instead of extracting a square pivot, it treats a genuine **zero-diagonal three-cycle** directly by conditioning one coordinate, preserving the two-variable bilinear product and paying its logarithmic singularity with the third coordinate.

The sharpened unpaid implication after this run is:

`QFORM-ZEROPIVOT-TRIANGLE-OR-RIDGE-AGGREGATION-v1` — from the bare three-large-eigenvalue hypothesis, force either (i) a zero-diagonal physical triangle with determinant at universal scale, (ii) a completed pivot/ridge certificate, or (iii) another already-paid grouped-coordinate branch; otherwise isolate the remaining nonseparable geometry and prove a new product-preserving estimate there.

## 2. Source-pinned dependencies and corrections

Fresh controls and programme state were read from `yspennstate/math-research-brain@5f30a16adc2545f6e86487708600b235d571d270`, then reread before publication at `de226dc67ba68b7aca9507746c55f636a4347e4d`. The current owner continuation is `QFORM-PROOF-FIRST-20260922T161801Z`.

Consumed corrections include the failure of law-uniform pointwise quadratic Fourier decay, loss from naive fiber suprema, loss of independence after spectral rotation, failure of a universal single rank-two Schur extraction, failure of a local rank-three-cross-cut dichotomy, failure of conditional-cap-as-independence substitutions, and the preceding B09 correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`. None is used as a positive premise.

Named partner dependency actually applied below:

* account03/B09, `QFORM-PIVOT-RIDGE-BILINEAR-v1`, canonical report `yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T155042Z-qform12/REPORT.md`.

## 3. Product logarithm lemma

### Lemma 3.1
Let `U,V` be independent real random variables with densities bounded by one. Then `W=UV` has an a.e. density `g` satisfying

`g(w) <= 2 [1 + log_+(1/|w|)]`.

### Proof
For `w!=0`,

`g(w)=int f_U(u) f_V(w/u) du/|u|`.

If `0<|w|<1`, split into `|u|<=|w|`, `|w|<|u|<=1`, and `|u|>1`.

On the first region substitute `v=w/u`; then

`int_{|u|<=|w|} ... <= int_{|v|>=1} f_V(v) dv/|v| <=1`.

The middle region is at most

`int_{|w|<|u|<=1} du/|u| = 2 log(1/|w|)`.

The last region is at most `int f_U(u)du=1`. Thus the claim holds for `|w|<1`.

If `|w|>=1`, split at `|u|=|w|`. The inner part is again at most one after `v=w/u`; the outer part is at most `|w|^{-1} int f_U <=1`. Hence `g(w)<=2`.

Translations of `U,V` preserve independence and the density cap, so the same bound is uniform over arbitrary separate shifts. Scaling gives, for `a!=0`,

`p_{2aUV}(s) <= |a|^{-1}[1+log_+(2|a|/|s|)]`.  QED.

This exact logarithm is the rank-two opposite-sign obstruction; no false bounded-density claim for a two-variable product is made.

## 4. Quadratic averaging of the logarithmic singularity

### Lemma 4.1
Let `Z` have density bounded by one. Let `q(z)=d z^2+e z+f` with `d!=0`. For every `L>0` and every `t`,

`int f_Z(z) log_+(L/|t-q(z)|) dz <= 2 + log_+(8L/|d|)`.

### Proof
Complete the square and translate `z`; translations preserve the density cap. Put `r=L/|d|`. By layer cake,

`int f_Z log_+(L/|t-q|)
 = int_0^infinity P(|(Z-z0)^2-s|<r e^{-u}) du`.

For every real `s` and every `eps>0`,

`|{z: |z^2-s|<eps}| <= 2 sqrt(2 eps)`.

Indeed if `s<=eps`, the set is contained in `|z|<sqrt(s+eps)` when nonempty; if `s>=eps`, its length is `2(sqrt(s+eps)-sqrt(s-eps))`, maximized at `s=eps`. Therefore

`P(...) <= min(1, 2 sqrt(2r) e^{-u/2})`.

If `2sqrt(2r)<=1`, integration gives `4sqrt(2r)<=2`; otherwise it gives `2+log(8r)`. The unified bound is the displayed formula. QED.

## 5. Main theorem: a zero-diagonal physical triangle has bounded density

### Theorem 5.1 — QFORM-ZERODIAG-TRIANGLE-LOGSMOOTH-v1
Let `X_1,...,X_n` be independent with densities bounded by one and let `A` be any real symmetric matrix. Suppose three original coordinates `i,j,k` satisfy

`A_ii=A_jj=A_kk=0`

and, writing

`a=A_ij`, `b=A_ik`, `c=A_jk`,

one has `abc!=0`. Then `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity <= (3+log 8) |abc|^{-1/3}`.

Equivalently, since

`det A[{i,j,k}] = 2abc`,

`||p_Q||_infinity <= 2^(1/3)(3+log 8) |det A[{i,j,k}]|^{-1/3}`.

All coefficients outside this principal triangle, including arbitrary outside quadratic terms and all couplings into the three selected coordinates, are allowed.

### Proof
Condition on all coordinates outside `{i,j,k}`. They contribute an arbitrary constant plus arbitrary affine terms in the selected coordinates, so it suffices to prove the uniform bound for

`F(x,y,z)=2axy+2bxz+2cyz + alpha x+ beta y+ gamma z+ delta`.

Choose the names of the three selected variables so that

`A0:=|a|=max(|a|,|b|,|c|)`.

For fixed `z`, define

`U = x + c z/a + beta/(2a)`,

`V = y + b z/a + alpha/(2a)`.

Conditional on `z`, `U,V` are independent translates of the original `x,y` variables and still have density caps one. Direct expansion gives

`F = 2a U V + q0(z)`,

where `q0` is a quadratic polynomial whose quadratic coefficient is

`d = -2bc/a`.

By Lemma 3.1, conditionally on `z`,

`p_{F|z}(t) <= A0^{-1}[1+log_+(2A0/|t-q0(z)|)]`.

Average in `z` and apply Lemma 4.1 with `L=2A0`. Since

`L/|d| = A0^2/|bc| = A0^3/P`,  where `P=|abc|`,

and `A0^3>=P`, put `r=A0^3/P>=1`. Then

`p_F(t) <= A0^{-1}[3+log(8r)]`.

Because `A0=(Pr)^(1/3)`,

`A0^{-1}[3+log(8r)]
 = P^(-1/3) r^(-1/3)[3+log(8r)]`.

For `r>=1`, the bracketed factor is decreasing, because

`d/dr {r^(-1/3)[3+log(8r)]}
 = -(log(8r)/3) r^(-4/3) <0`.

Hence it is at most `3+log 8`, proving the theorem. The conditional bound is uniform in the outside variables, so averaging over them preserves it. QED.

No moment, support, connectedness, symmetry, centering, or post-rotation independence assumption enters the proof. The interval consequence is immediate:

`P(Q in L) <= (3+log 8)|abc|^(-1/3) |L|`.

## 6. Genuine target corollary: the three-variable zero-pivot core is closed

Let

`A = [[0,1,1],[1,0,-1],[1,-1,0]]`.

Its characteristic polynomial is

`(lambda-1)^2(lambda+2)`,

so its spectrum is `{1,1,-2}` and it satisfies the full three-large-eigenvalue hypothesis while having **no physical square pivot at all**. Here `|abc|=1`, and Theorem 5.1 gives, for every admissible independent input law,

`||p_{X^TAX}||_infinity <= 3+log 8 = 5.07944...`.

More generally, every three-dimensional zero-diagonal target matrix whose three eigenvalues all have absolute value at least one has

`|det A|>=1`, hence `|abc|>=1/2`, and therefore

`||p_{X^TAX}||_infinity <= 2^(1/3)(3+log 8) < 6.400`.

Thus the exact `n=3`, zero-diagonal, indefinite branch is completely paid with arbitrary cap-one product inputs.

The theorem also applies inside larger matrices: any zero-diagonal physical principal triangle with `|det|>=1` already supplies the same universal `<6.400` density bound after conditioning all other coordinates.

As one edge tends to zero, the bound diverges and the form approaches a rank-two hyperbolic product. This correctly preserves the known logarithmic rank-two barrier rather than concealing it.

## 7. Required named-partner application

The latest completed named-partner result available at source check is account03/B09 `QFORM-PIVOT-RIDGE-BILINEAR-v1` from commit `62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`.

Apply its no-leverage `q=2` consequence to the independent-coordinate form

`Q_* = X_0^2 + 2(X_1Y_1+X_2Y_2+X_3Y_3)`.

Use physical pivot `a=1`; after the scalar Schur step the residual cross block between the `X` bank and `Y` bank is `N=I_3`, so its three singular values are all `sigma=1`. The partner theorem with `gamma=sigma/3` therefore gives the actual inequality

`||p_{Q_*}||_infinity < 18.084`.

The matrix of `Q_*` has one `+1` pivot eigenvalue and residual eigenvalues `+1,+1,+1,-1,-1,-1`, so this is a genuine target-valid application, not a lower-rank surrogate. Together with Theorem 5.1 it exhibits two complementary product-preserving mechanisms: square-pivot plus diffuse/ridge cross mass, and zero-pivot triangle plus logarithmic product smoothing by the third coordinate.

## 8. Conditional end-to-end route and remaining gap

A conditional full proof can now route a candidate matrix as follows.

1. Apply the completed spectral-window/diffuse branches from the shared state when their hypotheses hold.
2. If a universal-scale physical pivot and ridge cross certificate exists, invoke account03/B09 `QFORM-PIVOT-RIDGE-BILINEAR-v1`.
3. If the pivot disappears but there is a universal-scale zero-diagonal physical triangle, invoke Theorem 5.1.
4. Use the already-paid grouped hyperbolic/square branches for the known singleton-plus-bank obstructions.

The first unproved structural implication is therefore `QFORM-ZEROPIVOT-TRIANGLE-OR-RIDGE-AGGREGATION-v1`: prove the bare `s_3(A)>=1` hypothesis forces one of these paid original-coordinate mechanisms at universal scale, or isolate and control the genuine residual. A fixed small principal minor or a fixed rank-three cross cut is known not to be forced, so the proof must aggregate before reciprocal local-minor payment.

## 9. Integrity

No numerical experiment or external computation is used as mathematical evidence. The decimal constants are only evaluations of displayed exact expressions. The result is a proved supporting theorem and a closed target subclass, not the full conjecture. No continuity claim is made. No scheduler, notification, email, permission, paid-call, public-release, or cross-account mutation was made.
