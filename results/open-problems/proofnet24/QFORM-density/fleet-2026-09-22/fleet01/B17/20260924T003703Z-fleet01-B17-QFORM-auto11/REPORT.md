# QFORM-DIFFUSE-BANK-SPECTRAL-SLACK-COMPACTIFICATION-v1

Status: **new supporting sharp-witness theorem. The unrestricted QFORM target remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains separate.**

Worker: `fleet01/B17`, run `20260924T003703Z-fleet01-B17-QFORM-auto11`.

Fresh control source at start: `yspennstate/math-research-brain@bdc146bfbc18be1c90e7a1570b857e970ebc5d86`, owner revision `2026-09-22.15`. Execution status: `WITHOUT_VERIFIED_BRAIN`.

The designated partner result actually used below is the completed fleet02/B17 theorem

- `yspennstate/math-open-problems@103fe9295f04e9fae87c2ef9a88ba46a3b1e7fcc`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/fleet02-B17-20260923T234600Z-1da1d1ec/REPORT.md`,
- theorem name `QFORM-THREEBANK-ALLROT-DIFFUSE-NOSPIKE-v1`.

Its Fourier input is the proved Fresnel--Brascamp--Lieb Theorem F at

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

No independence after rotation is used anywhere.

## 1. Exact finite family with arbitrary spectral magnitudes

For integers `m_j>=2`, let all physical variables be independent
\[
U_{jk}\sim \operatorname{Unif}[-1/2,1/2],\qquad
Y_j=m_j^{-1/2}\sum_{k=1}^{m_j}U_{jk},\qquad j=1,2,3.
\]
Let `R_m` be the synthesis matrix whose rows in bank `j` equal `e_j/sqrt(m_j)`, so `R_m^T R_m=I_3`.
For
\[
a,b,c\ge1,\qquad \Lambda=\operatorname{diag}(a,b,-c),\qquad O\in O(3),
\]
define
\[
B_{a,b,c,O}=O^T\Lambda O,\qquad
A_{m,a,b,c,O}=R_mB_{a,b,c,O}R_m^T,
\]
and
\[
Q_{m,a,b,c,O}=Y^TB_{a,b,c,O}Y.
\]
Then every finite physical matrix has exact nonzero spectrum
\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,a,b,c,O})=\{a,b,-c\}.}
\tag{1.1}
\]
Thus every member is an exact target instance.

Put
\[
S(a,b,c)=(a-1)+(b-1)+(c-1).
\tag{1.2}
\]
The point of this run is to determine the exact asymptotic sharp constant of this entire all-diffuse bank architecture, uniformly over **all** rotations and **all** spectral magnitudes `a,b,c>=1`, and then determine the exact loss when `S` is kept away from zero.

## 2. Product-dependent global ceiling from the partner's Fourier mechanism

The spectral frame is
\[
V=R_mO^T.
\]
Its columns are orthonormal. A physical row in bank `j` has squared leverage exactly `1/m_j<=1/2`, independently of `O`. With the full physical coordinate set `I`, the frame Gram matrix is `G_I=I_3`, and the residual quadratic block is zero.

Therefore the completed Theorem F gives, for every real `t`,
\[
\boxed{
|\Phi_{m,a,b,c,O}(t)|
\le
\min\left\{1,(4\pi)^{3/2}(abc)^{-1/2}|t|^{-3/2}\right\}.
}
\tag{2.1}
\]
In particular
\[
\boxed{
\|p_{m,a,b,c,O}\|_\infty\le12(abc)^{-1/3}.
}
\tag{2.2}
\]
This also proves continuity for this finite family only, since the characteristic function is integrable. No full-target continuity claim is made.

Equation (2.2) is the first key compactification device: a putative near-`3sqrt(2)` diffuse-bank witness cannot send one spectral magnitude to infinity, because large spectral product automatically lowers the density norm.

### A concrete actual inequality from the same completed mechanism

Take `m_1=m_2=m_3=2`, let
\[
n=(1,1,1)/\sqrt3,\qquad B=I-28nn^T.
\]
Then `B` has spectrum `{1,1,-27}`, all of its entries are nonzero, and the resulting physical `6 x 6` matrix is entrywise nonzero and has exact nonzero spectrum `{1,1,-27}`. Equation (2.2) gives the actual global bound
\[
\boxed{\|p_Q\|_\infty\le12\,27^{-1/3}=4<3\sqrt2.}
\tag{2.3}
\]

The designated fleet02/B17 theorem itself is also applied directly to its exact-`J` dense Householder family. For
\[
B_*=I-\frac23\mathbf1\mathbf1^T,
\qquad m_1=m_2=m_3=m,
\]
its equation (4.4) gives, for every `epsilon>0`, an `M_epsilon` such that for every `m>=M_epsilon`,
\[
\boxed{
3\sqrt2-\epsilon
\le \|p_{Q_{m,B_*}}\|_\infty
\le 3\sqrt2+\epsilon.
}
\tag{2.4}
\]
For example, with `epsilon=10^{-2}` this places the exact finite dense rotated witness in
\[
4.2326406871\ldots\le\|p_Q\|_\infty\le4.2526406871\ldots
\]
for all sufficiently large `m`. This is a direct partner-result application, not merely a citation.

## 3. Uniform Gaussianization on compact spectral boxes

Let
\[
G=(G_1,G_2,G_3)\sim N(0,I_3/12)
\]
and let `p^G_{a,b,c}` denote the density of
\[
Q^G_{a,b,c}=aG_1^2+bG_2^2-cG_3^2.
\]

### Proposition 3.1
For every finite `L>=1`,
\[
\boxed{
\lim_{M\to\infty}
\sup_{\substack{m_j\ge M,\ O\in O(3)\\1\le a,b,c\le L}}
\|p_{m,a,b,c,O}-p^G_{a,b,c}\|_\infty=0.
}
\tag{3.1}
\]

### Proof
Suppose not. Then for some `epsilon>0` there are sequences with `min_j m_j^(r)->infinity`, `O_r in O(3)`, and `(a_r,b_r,c_r) in [1,L]^3` for which the left side stays at least `epsilon`.
Pass to a subsequence with
\[
O_r\to O,\qquad (a_r,b_r,c_r)\to(a,b,c).
\]
The three normalized uniform banks are independent and each satisfies the ordinary CLT, hence
\[
Y_{m^{(r)}}\Rightarrow G.
\]
The matrices `B_r=O_r^T diag(a_r,b_r,-c_r) O_r` converge to `B=O^T diag(a,b,-c)O`; therefore the continuous mapping theorem gives
\[
Y_{m^{(r)}}^TB_rY_{m^{(r)}}\Rightarrow G^TBG.
\]
By isotropy of `G`, the latter law is exactly that of `Q^G_{a,b,c}`. Hence the finite characteristic functions converge pointwise to the Gaussian characteristic function with limiting coefficients.

The Gaussian characteristic functions with coefficients `(a_r,b_r,c_r)` also converge pointwise to the same limit. Moreover (2.1), using `abc>=1`, supplies the common integrable majorant
\[
g(t)=\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}
\]
for all finite characteristic functions; the same majorant holds for their Gaussian limits. Dominated convergence therefore gives `L^1(dt)` convergence of the difference of the finite and corresponding Gaussian characteristic functions. Fourier inversion then yields uniform convergence of the densities, contradicting the assumed gap. This proves (3.1). \(\square\)

The use of the partner's integrable Fresnel majorant is essential here: weak convergence alone would not exclude a narrowing off-zero spike.

## 4. Exact global Gaussian norm for arbitrary `a,b,c>=1`

This section strengthens the previous cone-tip calculation by proving that zero is the global mode for every Gaussian coefficient triple, not only for the symmetric one-parameter family.

Let `sigma^2=1/12`. Write
\[
P=aG_1^2+bG_2^2,\qquad N=cG_3^2,
\qquad Q^G=P-N.
\]
The density of `P` is
\[
f_{a,b}(s)=\frac1{2\sigma^2\sqrt{ab}}
\exp\!\left[-\frac{s}{4\sigma^2}\left(\frac1a+\frac1b\right)\right]
I_0\!\left(\frac{s}{4\sigma^2}\left|\frac1a-\frac1b\right|\right),\quad s\ge0.
\tag{4.1}
\]
Put
\[
A=\frac1{4\sigma^2}\left(\frac1a+\frac1b\right),\qquad
B=\frac1{4\sigma^2}\left|\frac1a-\frac1b\right|.
\]
Then `A>B>=0`. Since
\[
I_0(x)-I_1(x)=\frac1\pi\int_0^\pi e^{x\cos\theta}(1-\cos\theta)\,d\theta>0
\]
for `x>0`, differentiation of (4.1) gives
\[
f'_{a,b}(s)<0\qquad(s>0).
\tag{4.2}
\]
The density `h_c` of `N` is also decreasing on `(0,infinity)`.

For `t>=0`,
\[
p^G_{a,b,c}(t)=\int_0^\infty f_{a,b}(t+u)h_c(u)\,du
\le p^G_{a,b,c}(0).
\]
For `r>=0`,
\[
p^G_{a,b,c}(-r)=\int_0^\infty f_{a,b}(u)h_c(u+r)\,du
\le p^G_{a,b,c}(0).
\]
Thus
\[
\boxed{\|p^G_{a,b,c}\|_\infty=p^G_{a,b,c}(0).}
\tag{4.3}
\]

A direct Gaussian cone integral gives
\[
\boxed{
p^G_{a,b,c}(0)=
\frac1{4\pi\sigma^2}
\int_0^{2\pi}
\frac{d\theta}
{\sqrt{ab+bc\cos^2\theta+ac\sin^2\theta}}.
}
\tag{4.4}
\]
At `sigma^2=1/12` the prefactor is `3/pi`.

Now set `u=cos^2(theta)`. The exact identity
\[
\begin{aligned}
&ab+bc\cos^2\theta+ac\sin^2\theta-(2+S)\\
&=(a-1)\sin^2\theta+(b-1)\cos^2\theta+(a-1)(b-1)\\
&\quad +(b-1)(c-1)\cos^2\theta+(a-1)(c-1)\sin^2\theta
\end{aligned}
\tag{4.5}
\]
shows pointwise that the denominator squared is at least `2+S`. Consequently
\[
\boxed{
\|p^G_{a,b,c}\|_\infty
\le \frac6{\sqrt{2+S(a,b,c)}}.
}
\tag{4.6}
\]
The bound is sharp for every fixed `S=delta`: equality is attained by
\[
(a,b,c)=(1,1,1+\delta)
\tag{4.7}
\]
(up to exchanging the two same-sign directions and overall sign reversal). Indeed then the denominator in (4.4) is identically `sqrt(2+delta)`.

In particular the Gaussian sharp constant at zero spectral slack is exactly
\[
\boxed{3\sqrt2.}
\tag{4.8}
\]

## 5. Exact asymptotic sharp constant with a prescribed spectral slack

For `delta>=0` define
\[
K_M(\delta)=
\sup\left\{
\|p_{m,a,b,c,O}\|_\infty:
\min_jm_j\ge M,\ O\in O(3),\ a,b,c\ge1,\ S(a,b,c)\ge\delta
\right\}.
\tag{5.1}
\]

### Theorem 5.1
For every `delta>=0`,
\[
\boxed{
\lim_{M\to\infty}K_M(\delta)=\frac6{\sqrt{2+\delta}}.
}
\tag{5.2}
\]

### Proof: upper bound
Fix `epsilon>0` and put
\[
C_{\delta,\epsilon}=\frac6{\sqrt{2+\delta}}+\epsilon.
\]
If
\[
abc\ge P_{\delta,\epsilon}:=\left(\frac{12}{C_{\delta,\epsilon}}\right)^3,
\]
then (2.2) immediately gives
\[
\|p_{m,a,b,c,O}\|_\infty\le C_{\delta,\epsilon}.
\]
If `abc<P_{delta,epsilon}`, then because each coefficient is at least one,
\[
1\le a,b,c\le P_{\delta,\epsilon}.
\]
This is a compact spectral box. Proposition 3.1 therefore gives, uniformly over all such triples and all rotations, for all sufficiently large `M`,
\[
\|p_{m,a,b,c,O}\|_\infty
\le\|p^G_{a,b,c}\|_\infty+\epsilon.
\]
Using (4.6) and `S>=delta` yields
\[
\|p_{m,a,b,c,O}\|_\infty
\le\frac6{\sqrt{2+\delta}}+\epsilon.
\]
Hence `limsup K_M(delta)<=6/sqrt(2+delta)`.

### Proof: lower bound
Take `(a,b,c)=(1,1,1+delta)` and any fixed rotation `O`. With `m_1=m_2=m_3=M`, Proposition 3.1 and the equality case (4.7) imply
\[
\|p_{M,1,1,1+\delta,O}\|_\infty
\longrightarrow\frac6{\sqrt{2+\delta}}.
\]
Therefore `liminf K_M(delta)` is at least the same value. This proves (5.2). \(\square\)

The zero-slack case is the exact asymptotic statement
\[
\boxed{
\lim_{M\to\infty}
\sup_{\substack{m_j\ge M,\ O\in O(3)\\a,b,c\ge1}}
\|p_{m,a,b,c,O}\|_\infty
=3\sqrt2.
}
\tag{5.3}
\]
Thus **arbitrarily large spectral magnitudes and arbitrary non-aligned minority-sign rotations do not create an asymptotic overshoot above `3sqrt(2)` in the all-diffuse three-bank architecture.**

## 6. Spectral-threshold rigidity of every near-extremizer in this chamber

A direct corollary of (5.2) is the following.

Suppose `min_jm_j^(r)->infinity`, `a_r,b_r,c_r>=1`, `O_r in O(3)`, and
\[
\liminf_{r\to\infty}\|p_{m^{(r)},a_r,b_r,c_r,O_r}\|_\infty\ge3\sqrt2.
\]
Then necessarily
\[
\boxed{
(a_r-1)+(b_r-1)+(c_r-1)\to0,
}
\tag{6.1}
\]
hence each of `a_r,b_r,c_r` tends to one.

Indeed, if a subsequence had `S>=delta>0`, (5.2) would force its density norm asymptotically to be at most `6/sqrt(2+delta)<3sqrt(2)`.

This is a genuine sharp-witness constraint: in a fully diffuse three-bank sequence, near-extremality requires not only diffuse leverage but simultaneous **spectral threshold saturation**. Any fixed positive amount of excess eigenvalue magnitude creates a fixed asymptotic density gap.

## 7. Exact dense rotated strict-slack stress family

The rigidity statement does not mean finite strict slack is harmless. It can vanish with dimension while retaining the `3sqrt(2)` obstruction.

For every integer `m>=2`, let
\[
n=\frac{(1,2,3)}{\sqrt{14}},\qquad
\delta_m=\frac1m,\qquad
B_m=I-(2+\delta_m)nn^T.
\tag{7.1}
\]
Then
\[
\operatorname{spec}(B_m)=\{1,1,-(1+1/m)\}.
\]
All nine entries of `B_m` are nonzero for `m>=2`: the off-diagonal entries are manifestly nonzero, while its diagonal entries are
\[
\frac{12-1/m}{14},\qquad
\frac{3-2/m}{7},\qquad
-\frac{4+9/m}{14}.
\]
Take three banks of size `m` and let `A_m=R_mB_mR_m^T`. Every one of the `(3m)^2` physical matrix entries is nonzero, and
\[
\boxed{
\operatorname{spec}_{\ne0}(A_m)=\{1,1,-(1+1/m)\}.
}
\tag{7.2}
\]
With independent physical centered unit intervals, compact spectral Gaussianization gives
\[
\boxed{
\|p_{X^TA_mX}\|_\infty\longrightarrow3\sqrt2.
}
\tag{7.3}
\]
Thus the source-valid lower obstruction survives a genuinely rotated, entrywise-dense exact target sequence in which one eigenvalue is **strictly beyond threshold at every finite dimension**. A proof cannot gain a dimension-free improvement merely from the strict inequality `|lambda|>1`; it would have to quantify the amount of spectral slack.

For fixed `delta>0`, the same construction with `delta_m=delta` instead converges to the exact smaller constant `6/sqrt(2+delta)`.

## 8. What this does and does not settle

This report strengthens the sharp-constant picture only inside the exact three independent normalized-uniform-bank architecture. It proves:

1. the exact asymptotic sharp constant over **all rotations and all spectral magnitudes >=1** is `3sqrt(2)`;
2. imposing total spectral slack `S>=delta` changes that exact asymptotic constant to `6/sqrt(2+delta)`;
3. every fully diffuse near-extremizer must have all three active eigenvalue magnitudes tend to one;
4. there is an explicit entrywise-dense strict-slack exact-spectrum sequence still tending to `3sqrt(2)` when the slack vanishes;
5. the completed fleet02/B17 all-rotation theorem is applied to the exact dense Householder family via (2.4), and its pinned Fresnel mechanism is used quantitatively in (2.1)--(2.2).

The unrestricted QFORM conjecture is **not** proved. Still unpaid are rough non-uniform cap-one laws, finite/intermediate leverage banks, shared macroscopic rows that do not split into three independent banks, multiscale fragmented supports, off-bank product structure, and arbitrary additional active spectrum. The full continuity conclusion is also not proved.

Corrections preserved: no arbitrary-joint coarea bound, no conditional-density-moment bound, no independence after spectral rotation, no pointwise oscillatory decay, no fiber-supremum dimension-free shortcut, and no universal `pi` claim.
