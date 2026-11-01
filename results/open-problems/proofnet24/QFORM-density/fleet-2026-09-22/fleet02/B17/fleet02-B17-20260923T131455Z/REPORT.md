SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-23T13:14:55Z.
attacking: close the all-finite-bank sharp-constant gap for the exact one-heavy majority-sign family, and extend it from equal banks to arbitrary unit-norm rank-one cube banks.

# QFORM B17 — all finite one-heavy majority banks lie below 3sqrt(2)

Run: `fleet02-B17-20260923T131455Z`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and strengthened target class

The predecessor theorem at `yspennstate/math-open-problems@189fc052089ae2d3237bc0865b290b01b26a6513` reduced the exact one-heavy majority-sign family
\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m)
\]
to a single scalar sequence
\[
C_m=p_{U^2+S_m^2-T_m^2}(0),\qquad U\sim\mathrm{Unif}[-1/2,1/2],
\]
and proved the arbitrary heavy cap-one law is exactly optimized by this centered interval at output zero. It also proved the Gaussian limit is only `3.5306641257...<3sqrt(2)`, with a negative first finite-bank correction, but left `C_m<=3sqrt(2)` for every finite `m` unpaid.

This run closes that gap in a stronger form. Let `a=(a_1,...,a_m)\in\mathbb R^m` satisfy `sum a_j^2=1`. On two disjoint physical banks take iid centered unit intervals and define
\[
S_a=\sum_j a_jU_j,\qquad T_a=\sum_j a_jV_j.
\]
On one additional physical coordinate put an arbitrary probability density `0<=f<=1`. Define
\[
A_a=\operatorname{diag}(1,aa^\top,-aa^\top).
\tag{1.1}
\]
Because `aa^T` has nonzero spectrum `{1}`, every finite physical matrix has exact nonzero spectrum
\[
\boxed{\operatorname{spec}_{\ne0}(A_a)=\{1,1,-1\}.}
\tag{1.2}
\]
All physical variables are independent. There is no post-rotation independence assumption. The equal-bank family is recovered from `a=(1,...,1)/sqrt(m)`.

## 2. Main theorem

### `QFORM-ONE-HEAVY-MAJORITY-ALL-BANKS-BARRIER-v1`

For every finite `m`, every unit vector `a\in\mathbb R^m`, and every cap-one heavy-coordinate density `f`, let
\[
Q_{a,f}=X_f^2+S_a^2-T_a^2.
\]
Then
\[
\boxed{
\sup_{0\le f\le1,\ \int f=1}\|p_{Q_{a,f}}\|_\infty
=p_{U^2+S_a^2-T_a^2}(0)
\le K_*:=\frac\pi2\left(\sqrt2+2^{1/4}\right)
<3\sqrt2.
}
\tag{2.1}
\]
Numerically only as a scale check, `K_*=4.0894436371...`, so `3sqrt(2)-K_*=0.1531970499...`.

Thus no finite one-heavy majority-sign witness with two identical rank-one centered-cube banks can exceed the current `3sqrt(2)` obstruction, for any bank size or leverage profile. The arbitrary heavy coordinate may be fragmented, translated, disconnected or unbounded.

## 3. Exact heavy-law extremizer survives arbitrary bank weights

Let `h` be the density of `S_a`. Each summand `a_jU_j` has an even density nonincreasing on `[0,infinity)`, and convolution preserves this property. Hence `h` is even and nonincreasing on `[0,infinity)`.

The density of `S_a^2` is
\[
b(y)=\frac{h(\sqrt y)}{\sqrt y},\qquad y>0,
\tag{3.1}
\]
which is also nonincreasing. Since `S_a,T_a` are iid, the residual `R=S_a^2-T_a^2` has an even density `k`, and for `w>=0`
\[
k(w)=\int_0^\infty b(u)b(u+w)\,du.
\tag{3.2}
\]
Therefore `k(w)` is nonincreasing in `|w|`. Its logarithmic value at zero may be infinite; truncate `k` and pass by monotone convergence in the bathtub argument below.

For fixed output `s`,
\[
p_{Q_{a,f}}(s)=\int_{\mathbb R}f(x)k(s-x^2)\,dx.
\tag{3.3}
\]
Since the kernel is ordered by `|s-x^2|`, the cap-one bathtub optimizer is the measure-one set closest to the level `x^2=s`. Exactly as in the predecessor proof, it is the centered unit interval for `s<=1/8`, while for `s>=1/8` it is the two-shell set
\[
[-A,-B]\cup[B,A],\qquad A-B=\frac12,\qquad A^2+B^2=2s.
\tag{3.4}
\]
For `s>=1/8`, the distance variable `|x^2-s|` under that shell is stochastically increasing in `s`, so the optimized value is at most its value at `s=1/8`.

For the centered interval heavy law `U`, the three independent variables `U,S_a,T_a` all have even densities nonincreasing on the positive half-line. The separated symmetric-unimodal argument therefore gives
\[
p_{U^2+S_a^2-T_a^2}(s)\le p_{U^2+S_a^2-T_a^2}(0)
\qquad\text{for every }s.
\tag{3.5}
\]
Indeed the density of `U^2+S_a^2` is decreasing by the polar formula for two independent symmetric-unimodal variables, while the density of `T_a^2` is decreasing; translating either factor away from zero can only decrease their overlap. Combining this with the shell comparison proves
\[
\boxed{
\sup_f\|p_{Q_{a,f}}\|_\infty
=p_{U^2+S_a^2-T_a^2}(0).
}
\tag{3.6}
\]
Thus it remains only to bound one exact cone-tip integral.

## 4. Two cube-projection norms

The pinned Claude source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` uses the Rogozin/Ball cube-slicing theorem in its proved `L^p` characteristic-function lemma. Apply that same completed projection bound to the actual bank here.

Because `||a||_2=1`, `S_a` is a unit-direction one-dimensional projection of the centered unit cube. Therefore
\[
\boxed{H:=\|h\|_\infty\le\sqrt2.}
\tag{4.1}
\]
A second application gives the crucial `L^2` improvement. Let `S_a'` be an independent copy. Then
\[
\|h\|_2^2=(h*\widetilde h)(0)=p_{S_a-S_a'}(0).
\tag{4.2}
\]
Set `Z=(S_a-S_a')/sqrt(2)`. The `2m` coefficient vector of `Z` is `(a,-a)/sqrt(2)`, which again has Euclidean norm one. Hence Ball's projection bound gives `||p_Z||_infty<=sqrt(2)`. Since `S_a-S_a'=sqrt(2)Z`,
\[
\boxed{L^2:=\|h\|_2^2\le1.}
\tag{4.3}
\]
This is the quantitative input that the previous `pi h(0)` estimate did not exploit.

## 5. New cone-Hoelder estimate

At zero, the square-density formula gives
\[
C(a):=p_{U^2+S_a^2-T_a^2}(0)
=\int_{-1/2}^{1/2}\int_{\mathbb R}
 h(s)\frac{h(\sqrt{x^2+s^2})}{\sqrt{x^2+s^2}}\,ds\,dx.
\tag{5.1}
\]
The singularity at the origin is integrable in two dimensions. Enlarge the `x`-strip to the whole plane and pass to polar coordinates `x=r cos(theta)`, `s=r sin(theta)`:
\[
C(a)
\le \int_0^{2\pi}\int_0^\infty h(r\sin\theta)h(r)\,dr\,d\theta.
\tag{5.2}
\]
By evenness, with `u=sin(theta)`,
\[
C(a)\le4\int_0^1\frac{I(u)}{\sqrt{1-u^2}}\,du,
\qquad
I(u):=\int_0^\infty h(r)h(ur)\,dr.
\tag{5.3}
\]
For `0<=u<=1/2`, use the `L^infinity` bound and half the mass:
\[
I(u)\le H\int_0^\infty h(r)\,dr=\frac H2\le\frac{\sqrt2}{2}.
\tag{5.4}
\]
For `1/2<=u<=1`, Cauchy-Schwarz and evenness give
\[
I(u)
\le
\left(\int_0^\infty h(r)^2dr\right)^{1/2}
\left(\int_0^\infty h(ur)^2dr\right)^{1/2}
=\frac{\|h\|_2^2}{2\sqrt u}
\le\frac1{2\sqrt u}.
\tag{5.5}
\]
Therefore
\[
C(a)
\le \frac{\pi\sqrt2}{3}
+2\int_{1/2}^1\frac{du}{\sqrt u\sqrt{1-u^2}}.
\tag{5.6}
\]
Split the last integral at `u=1/sqrt(2)`. On `[1/2,1/sqrt(2)]`, `u^{-1/2}<=sqrt(2)`; on `[1/sqrt(2),1]`, `u^{-1/2}<=2^{1/4}`. Hence
\[
\int_{1/2}^1\frac{du}{\sqrt u\sqrt{1-u^2}}
\le \sqrt2\left(\frac\pi4-\frac\pi6\right)
+2^{1/4}\left(\frac\pi2-\frac\pi4\right)
=\frac{\pi\sqrt2}{12}+\frac{\pi2^{1/4}}4.
\tag{5.7}
\]
Substitution into (5.6) yields
\[
\boxed{
C(a)\le\frac\pi2\left(\sqrt2+2^{1/4}\right)=K_*.
}
\tag{5.8}
\]
No bank size, coefficient profile, support diameter or moment parameter appears.

## 6. Strict comparison with 3sqrt(2)

Divide (5.8) by `sqrt(2)`:
\[
\frac{K_*}{\sqrt2}=\frac\pi2\left(1+2^{-1/4}\right).
\]
Use the elementary strict bounds
\[
\pi<\frac{22}{7},\qquad 2^{-1/4}<\frac{10}{11},
\]
where the second follows from `(11/10)^4<2`. Then
\[
\frac{K_*}{\sqrt2}
<\frac{11}{7}\left(1+\frac{10}{11}\right)
=3.
\]
Thus
\[
\boxed{K_*<3\sqrt2.}
\tag{6.1}
\]
This closes the previously unpaid all-finite-`m` scalar question and simultaneously allows arbitrary unit-norm bank leverage profiles.

## 7. Application of the pinned Claude result and partner result

The pinned `e5f71d79...` source is used at a real inequality, not only cited: its Ball/Rogozin cube-projection input gives both (4.1) and the self-difference estimate (4.3). Those two estimates are exactly what convert the cone integral into the strict sharp-obstruction bound (5.8).

The same source's proved ruled-level-set Theorem C independently gives, for every member of this exact `(+,+,-)` family and every `s>=0`,
\[
p_Q(s)\le\pi\sqrt2.
\]
That constant is above `3sqrt(2)` and therefore is only an auxiliary one-sheet control. The exact bathtub reduction plus (5.8) improves it to a global bound below `3sqrt(2)` for the present source-valid family. Failure of `pi sqrt(2)` to reach the candidate sharp constant is a proof-constant limitation, not a QFORM counterexample.

The latest completed designated partner `fleet03/B17` result is `yspennstate/math-open-problems@86b970bb350ff450a5f3672eff13aaec60c18447`. For the genuinely dense three-coordinate Householder cube
\[
A=I-2ee^\top,\qquad e=(1,1,1)/\sqrt3,
\]
it proves the exact global maximum
\[
\|p_Q\|_\infty
=6\sqrt3\,\operatorname{artanh}\!\left(\frac{\sqrt2-1}{\sqrt3}\right)
=2.5343552034\ldots<3\sqrt2.
\]
That family is not contained in the block-rank-one class above. Combining the two complementary exact-spectrum stress mechanisms gives
\[
\boxed{
\max\left\{
\sup_{m,a,f}\|p_{Q_{a,f}}\|_\infty,
\|p_{Q_{\rm Householder\ cube}}\|_\infty
\right\}
\le K_*<3\sqrt2.
}
\tag{7.1}
\]
Thus neither arbitrary finite leverage redistribution inside two opposite rank-one cube banks nor the canonical fully shared three-heavy Householder cube can beat the Gaussian diffuse obstruction.

## 8. Scope and remaining sharp-witness mechanisms

This theorem is a supporting witness-class theorem, not the unrestricted QFORM theorem. It fixes both rank-one banks to centered unit-interval physical laws and requires the two bank coefficient profiles to be identical. The arbitrary cap-one freedom is on the singleton majority-sign coordinate. It does not cover two different bank laws/profiles, several non-collinear macroscopic rows sharing physical coordinates, additional active spectrum, or fully coupled multiscale fragmented marginals.

A future example above `3sqrt(2)` would refute the proposed sharp constant but would not by itself refute existence of a larger universal QFORM constant. Conversely, inability to extend the cone-Hoelder estimate beyond the identical-bank geometry would only be a limitation of this mechanism.

The next nonredundant B17 witness target is therefore an unequal-bank or genuinely shared-coordinate intermediate-leverage construction, not another equal-bank finite-`m` calculation.

## 9. Correction discipline

No arbitrary-joint coarea estimate, conditional projection-density moment, post-rotation independence, pointwise quadratic stationary-phase bound, bounded fragment-count reduction, or single-good-minor principle is used. The proof stays entirely in original physical product coordinates and checks the exact matrix spectrum before any density estimate.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity for the full target: **OPEN and separate**.
