# fleet02/B17 — sharp constant and rotated witnesses for quadratic-form bounded density

**Run:** `B17-20260922T114529Z-qform-sharp-witness`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet02/B17, `Sharp constant and witnesses` / pathway `STRUCTURE`  
**Classification:** `RIGOROUS_UNIVERSAL-LOWER-BOUND / ROTATED-STRESS-FAMILY`; **full target OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 0. Live scope and corrections

The later owner order supersedes this slot's historical FEI prompt. The active target is: for independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one dimension- and law-independent constant, or give a valid counterexample.

I consumed the live corrections `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, and `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`. No pointwise law-uniform Fresnel decay, unrestricted fiber supremum, or post-rotation independence is used below.

## 1. Named partner result actually applied

The required partner source is fleet03/B17, run `fleet03-B17-20260922T112131Z`, scientific commit
`c64fcff680b0a252a3c92002c60eedba02bbb9ec`, report
`qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`.

That report proves two facts used here:

1. the coordinate-diagonal target has the sharp available upper control `||p_Q||_infinity<=pi`, by convolving a same-sign pair of square singularities;
2. the proposed law-uniform pointwise oscillatory-decay step is false.

Thus `pi` is a rigorous diagonal benchmark, not a justified universal constant.

I also apply fleet02/B06's completed Hadamard-delocalized construction
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`,
which supplies an exact rank-three matrix with spectrum `(+1,+1,-1,0,...)` for which every physical `2x2` principal determinant is nonpositive. Section 4 below shows that the same family asymptotically forces a density peak at least `3 sqrt(2)`.

## 2. Main theorem: every universal constant is at least `3 sqrt(2)`

### Theorem `QFORM-UNIVERSAL-CONSTANT-LOWER-3SQRT2-v1`

Let
\[
\mathcal C_* = \sup \|p_{X^TAX}\|_\infty
\]
where the supremum ranges over all target-admissible instances for which the density is defined. Then
\[
\boxed{\mathcal C_*\ge 3\sqrt2=4.242640687119285\ldots .}
\]
Equivalently, any universal constant in the conjecture must satisfy `C>=3 sqrt(2)`.

This strictly exceeds the diagonal benchmark `pi`.

### Proof by a three-block diffuse rotation

For an integer `m>=1`, take `n=3m` and independent
\[
X_1,\ldots,X_{3m}\sim {\rm Unif}[-1/2,1/2].
\]
Partition the coordinates into three disjoint blocks of size `m`, and let `r_1,r_2,r_3` be the normalized constant vectors on those blocks:
\[
r_j=m^{-1/2}{\bf 1}_{B_j}.
\]
Set
\[
A_m=r_1r_1^T+r_2r_2^T-r_3r_3^T.
\]
The vectors are orthonormal, hence
\[
\operatorname{spec}(A_m)=\{1,1,-1,0,\ldots,0\},
\]
so every `m` is a genuine target instance.

Write
\[
Y_{m,j}=\langle r_j,X\rangle
=m^{-1/2}\sum_{i\in B_j}X_i .
\]
The three variables are independent. Since the uniforms have mean zero and variance `1/12`, the ordinary central limit theorem gives
\[
(Y_{m,1},Y_{m,2},Y_{m,3})
\Longrightarrow
{1\over\sqrt{12}}(Z_1,Z_2,Z_3),
\]
with independent standard Gaussians `Z_j`. Therefore
\[
Q_m=X^TA_mX
=Y_{m,1}^2+Y_{m,2}^2-Y_{m,3}^2
\Longrightarrow
W={1\over12}(Z_1^2+Z_2^2-Z_3^2).
\tag{2.1}
\]

It remains to compute the limiting density exactly. Put
`S=Z_1^2+Z_2^2` and `T=Z_3^2`. Then
\[
f_S(s)={1\over2}e^{-s/2}{\bf1}_{s>0},\qquad
f_T(t)={e^{-t/2}\over\sqrt{2\pi t}}{\bf1}_{t>0}.
\]
For `V=S-T`,
\[
p_V(v)=
\begin{cases}
{e^{-v/2}\over2\sqrt2},&v\ge0,\\[2mm]
{e^{-v/2}\over2\sqrt2}\,
\operatorname{erfc}\!\sqrt{-v},&v<0.
\end{cases}
\]
Scaling by `1/12`,
\[
p_W(y)=
\begin{cases}
3\sqrt2\,e^{-6y},&y\ge0,\\[1mm]
3\sqrt2\,e^{-6y}\operatorname{erfc}\!\sqrt{-12y},&y<0.
\end{cases}
\tag{2.2}
\]
In particular `p_W` is continuous at zero and
\[
p_W(0)=3\sqrt2.
\]
Moreover this is its maximum: for `y>=0` it is immediate, and for `y<0`, writing `a=-12y`,
\[
e^{-6y}\operatorname{erfc}\sqrt{-12y}
=e^{a/2}\operatorname{erfc}\sqrt a
\le e^{a/2}e^{-a}=e^{-a/2}\le1.
\]

Each finite `Q_m` has a density: each `Y_{m,j}` has an absolutely continuous density, its square has a density, and the three blocks are independent. Fix `delta>0`. By continuity of `p_W` at zero, choose `epsilon>0` with
\[
{1\over2\epsilon}\Pr(|W|\le\epsilon)>3\sqrt2-\delta/2.
\]
Weak convergence in (2.1), whose limiting interval boundary has probability zero, gives the same lower bound with `delta` in place of `delta/2` for all sufficiently large `m`. Since the average of a density over an interval cannot exceed its essential supremum,
\[
\|p_{Q_m}\|_\infty>3\sqrt2-\delta
\]
for all sufficiently large `m`. Thus `C_*>=3 sqrt(2)`. QED.

## 3. Exact finite rotated witness beating `pi`

The preceding proof is asymptotic. Already `m=2` gives an exact six-variable witness above the entire diagonal benchmark.

For one block,
\[
Y={X_1+X_2\over\sqrt2}
\]
has triangular density
\[
f_Y(y)=\sqrt2(1-\sqrt2|y|),\qquad |y|\le1/\sqrt2.
\]
Hence `U=Y^2` has
\[
g(u)=\sqrt2\,u^{-1/2}-2,\qquad 0<u<1/2.
\]
For `0<t<1/2`, the density of `U_1+U_2` is
\[
(g*g)(t)=2\pi-8\sqrt{2t}+4t.
\]
Therefore for
\[
Q_2=U_1+U_2-U_3
\]
we obtain exactly
\[
\begin{aligned}
p_{Q_2}(0)
&=\int_0^{1/2}
(2\pi-8\sqrt{2t}+4t)(\sqrt2\,t^{-1/2}-2)\,dt\\
&=\boxed{2\pi-{7\over3}}
=3.949851973846253\ldots>\pi.
\end{aligned}
\tag{3.1}
\]
Thus no proof can hope that the diagonal constant `pi` remains valid after arbitrary rotation.

## 4. Applying B06's Hadamard adversary: the lower bound survives when every physical pair is indefinite/degenerate

For `n=2^k`, let `H_n` be the Sylvester Hadamard matrix and let `U_n` be its first three normalized columns. Put
\[
D=\operatorname{diag}(1,1,-1),\qquad A_n=U_nDU_n^T.
\]
The B06 source proves exactly that `A_n` has spectrum `(+1,+1,-1,0,...)` and every physical `2x2` principal determinant is nonpositive. I now use this exact family with i.i.d. `Unif[-1/2,1/2]` inputs.

Write `Y_n=U_n^TX`. The rows of the unnormalized first-three-column matrix are
\[
(1,s,t),\qquad s,t\in\{\pm1\},
\]
each sign pair occurring exactly `n/4` times. If
\[
\psi(z)={\sin(z/2)\over z/2}
\]
is the characteristic function of `Unif[-1/2,1/2]`, then for fixed
`\theta=(\theta_1,\theta_2,\theta_3)`,
\[
\phi_{Y_n}(\theta)
=
\prod_{s,t=\pm1}
\psi\!\left({\theta_1+s\theta_2+t\theta_3\over\sqrt n}\right)^{n/4}.
\tag{4.1}
\]
Since
\[
\log\psi(z)=-{z^2\over24}+O(z^4)
\]
near zero and
\[
\sum_{s,t=\pm1}(\theta_1+s\theta_2+t\theta_3)^2
=4\|\theta\|_2^2,
\]
(4.1) yields
\[
Y_n\Longrightarrow N(0,I_3/12).
\]
Consequently
\[
X^TA_nX=Y_{n,1}^2+Y_{n,2}^2-Y_{n,3}^2
\Longrightarrow W
\]
with the same `W` as (2.1). Coarea gives absolute continuity for every finite `n` because `A_n` has rank three and the critical set `ker A_n` has Lebesgue measure zero. The same small-interval argument therefore gives
\[
\liminf_{n\to\infty,\ n=2^k}\|p_{X^TA_nX}\|_\infty\ge3\sqrt2.
\tag{4.2}
\]

This is the main stress-test consequence: the lower-bound family can be chosen precisely so that the local “find one definite physical pair” route fails everywhere. Delocalization is not merely a proof nuisance; it increases the attainable density peak beyond the diagonal value.

## 5. A low-dimensional rotated control

For three independent `Unif[-1/2,1/2]` variables, take
\[
A_{45}=
\begin{pmatrix}
0&-1&0\\
-1&0&0\\
0&0&1
\end{pmatrix},
\qquad
Q=Z^2-2XY.
\]
Its eigenvalues are again `(+1,+1,-1)`, and it is genuinely non-diagonal. The density of `Z^2` is `u^{-1/2}` on `(0,1/4)`, while the density of `2XY` is
\[
h(v)=\log {1\over2|v|},\qquad |v|<1/2.
\]
Hence
\[
p_Q(0)
=\int_0^{1/4}u^{-1/2}\log{1\over2u}\,du
=\boxed{2+\log2}
=2.693147180559945\ldots .
\tag{5.1}
\]
This control shows that rotation by itself does not automatically increase the peak; the stronger phenomenon is diffuse averaging toward the minimal-variance Gaussian limit.

## 6. Why `3 sqrt(2)` is the ceiling of the simple i.i.d. diffuse-CLT mechanism

If a probability density `f` satisfies `f<=1` and has finite variance about its mean `mu`, then
\[
\Pr(|X-\mu|\le r)\le2r.
\]
Therefore
\[
\operatorname{Var}X
=\int_0^\infty2r\,\Pr(|X-\mu|>r)\,dr
\ge\int_0^{1/2}2r(1-2r)\,dr
={1\over12}.
\tag{6.1}
\]
Equality is attained by a uniform interval of length one.

Thus, for the same three-block i.i.d. CLT construction using any admissible finite-variance input law, the Gaussian limit has variance `sigma^2>=1/12` in each spectral coordinate and its mixed-sign quadratic density has peak
\[
{1\over2\sqrt2\,\sigma^2}\le3\sqrt2.
\]
So the uniform interval is extremal inside this particular diffuse-i.i.d.-CLT mechanism. This is not a global sharpness theorem for the conjecture.

## 7. Consequences and remaining target

The present run changes the quantitative landscape:

- rigorous diagonal control: `pi`;
- exact rotated six-variable witness: `2 pi-7/3 = 3.94985...`;
- rigorous diffuse rotated lower floor: `3 sqrt(2) = 4.24264...`.

Hence any universal theorem must have
\[
\boxed{C\ge3\sqrt2}.
\]
The full conjecture remains OPEN. In particular, this report supplies no universal upper bound and does not claim `3 sqrt(2)` is globally sharp.

A useful next stress question is now precise: can a non-i.i.d., mesoscopically localized, or correlated-in-eigenbasis product construction force a peak strictly above `3 sqrt(2)` while retaining the coordinate-density cap one? The Hadamard application says any proposed upper-bound mechanism must also survive a family with no definite physical `2x2` principal block.

## 8. Verification status

The deterministic checker verifies for Sylvester orders `4,8,16,32`:

- orthogonality of the first three columns;
- `M^3=n^2 M` for `A=M/n`, hence the nonzero spectrum lies in `{+1,-1}` and the trace identities give the intended rank-three signature;
- every physical pair determinant numerator is nonpositive;
- each of the four `(s,t)` row patterns occurs exactly `n/4` times;
- the exact constant ordering `3 sqrt(2) > 2 pi-7/3 > pi > 2+log 2`.

The checker is a finite implementation check. The lower-bound theorem itself is analytic, based on the CLT and the exact density calculation above.

No full solution or novelty priority is claimed.
