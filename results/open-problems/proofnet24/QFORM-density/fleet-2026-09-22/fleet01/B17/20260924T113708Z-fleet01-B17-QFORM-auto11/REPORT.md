# QFORM-MICROCOMB-NO-FIXED-CARRIER-SHARP-WITNESS-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T113708Z-fleet01-B17-QFORM-auto11`  
Status: `NEW SUPPORTING SHARPNESS THEOREM / EXACT DENSE ROTATED WITNESS / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Unrestricted continuity remains a separate conclusion. The result below strengthens the source-valid lower obstruction `C_univ >= 3 sqrt(2)` by showing that the obstruction persists for cap-one inputs having increasingly fine disconnected support and **no independent uniform convolution factor of any fixed positive width**. Thus the newest fleet02/B17 growing-direction theorem is sharp in constant but its unit-uniform-carrier hypothesis cannot be made a necessary structural feature of near-extremizers.

Fresh controls used before mathematics: `yspennstate/math-research-brain@da1a3f0d4cc949f847bd31f0dd4148dc59b08130`, with AGENTS blob `af9b5936c3eed3bb1cced26eddef5fd3eea941ce`; the same AGENTS blob was re-read at later main `ae6b3cb2eae261a1268816b5510070c918e400b1`. Owner control revision remains `2026-09-22.15`; no B17 stop was observed. Execution context is `WITHOUT_VERIFIED_BRAIN`.

## 1. A micro-comb cap-one law with exact variance

For every integer `m>=2`, put

\[
a_m={1\over m},\qquad d_m={1\over m^3},\qquad h_m=a_m+d_m,
\]

and define centered tooth locations

\[
c_{m,j}=\left(j-{m-1\over2}\right)h_m,\qquad j=0,\ldots,m-1.
\]

Let

\[
E_m=\bigcup_{j=0}^{m-1}
\left[c_{m,j}-{1\over2m},\;c_{m,j}+{1\over2m}\right],
\qquad
f_m=\mathbf1_{E_m}.
\tag{1.1}
\]

The `m` components have length `1/m` and consecutive gaps exactly `1/m^3`. Hence

\[
\int f_m=1,\qquad 0\le f_m\le1,
\]

and symmetry gives mean zero. The total support span is

\[
1+{m-1\over m^3},
\tag{1.2}
\]

so the family is uniformly bounded.

The variance is exact. A tooth centered at `c` contributes

\[
\int_{c-a_m/2}^{c+a_m/2}x^2dx
=a_mc^2+{a_m^3\over12},
\]

and

\[
\sum_{j=0}^{m-1}\left(j-{m-1\over2}\right)^2
={m(m^2-1)\over12}.
\]

Therefore

\[
\begin{aligned}
v_m:=\operatorname{Var}_{f_m}(X)
&={h_m^2(m^2-1)\over12}+{1\over12m^2}\\
&={1+2m^{-2}-m^{-4}-m^{-6}\over12}.
\end{aligned}
\tag{1.3}
\]

In particular

\[
\boxed{
v_m-{1\over12}
={ (m^2-1)(2m^2+1)\over12m^6}>0,
\qquad v_m\downarrow {1\over12}.
}
\tag{1.4}
\]

Thus these increasingly fragmented laws approach the minimum cap-one variance while never having connected support at any finite stage.

## 2. No fixed positive-width uniform convolution carrier

The following elementary support lemma is the structural point.

**Lemma.** If a real random variable has a representation

\[
X=U_\ell+J
\tag{2.1}
\]

with `U_ell` independent of `J` and uniform on an interval of length `ell>0`, then the essential support of the density of `X` contains a connected interval of length `ell`.

**Proof.** Translate the uniform interval to `I=[-ell/2,ell/2]`. If `j` belongs to the support of the law `mu` of `J` and `x` belongs to `j+int(I)`, choose a neighborhood `V` of `j` so small that `x-y in I` for all `y in V`. Since `j in supp(mu)`, `mu(V)>0`, and

\[
f_X(x)={1\over\ell}\mu(x-I)\ge {1\over\ell}\mu(V)>0.
\]

Thus `j+int(I)` lies in the essential support. QED.

Every connected component of `E_m` in (1.1) has length exactly `1/m`. Consequently

\[
\boxed{
X_m\sim f_m\quad\Longrightarrow\quad
X_m\ne U_\ell+J\text{ in law for every independent uniform carrier with }\ell>{1\over m}.
}
\tag{2.2}
\]

In particular, for every fixed `ell>0`, all sufficiently large members of the sequence admit no independent uniform convolution carrier of width `ell`. This includes, a fortiori, the unit-uniform carrier used in the newest fleet02/B17 theorem.

## 3. Exact entrywise-dense rotated target matrices

Use the tetrahedral Parseval block

\[
T_0={1\over2}
\begin{pmatrix}
1&1&1\\
1&-1&-1\\
-1&1&-1\\
-1&-1&1
\end{pmatrix},
\qquad T_0^TT_0=I_3.
\tag{3.1}
\]

Let

\[
n={1\over\sqrt{14}}(1,2,3)^T,
\qquad
B=I_3-2nn^T
={1\over7}
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\tag{3.2}
\]

Then `B^2=I`, so

\[
\operatorname{spec}(B)=\{1,1,-1\}.
\tag{3.3}
\]

Stack `m` copies of `T_0/sqrt(m)` to form `T_m in R^{4m x 3}`. Then

\[
T_m^TT_m=I_3.
\tag{3.4}
\]

Set

\[
A_m=T_mBT_m^T.
\tag{3.5}
\]

Because `T_m` is an isometry on `R^3`,

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}}
\tag{3.6}
\]

for every finite `m`. Thus every stage satisfies the exact three-large-eigenvalue target at threshold, with no asymptotic spectral approximation.

The physical `4 x 4` block is

\[
C:=T_0BT_0^T=
\begin{pmatrix}
-15/28&17/28&5/28&-1/4\\
17/28&5/28&-15/28&-1/4\\
5/28&-15/28&17/28&-1/4\\
-1/4&-1/4&-1/4&3/4
\end{pmatrix}.
\tag{3.7}
\]

Every entry of `C` is nonzero, and every physical block of `A_m` equals `C/m`. Hence **every entry of `A_m` is nonzero**. Moreover

\[
\max_{ij}|(A_m)_{ij}|={3\over4m}.
\tag{3.8}
\]

Thus a physical principal block of size `r` has operator norm at most `3r/(4m)` by the row-sum bound. In particular, for `m>=3`, every physical `3 x 3` principal block has norm `<1`; the three target-scale eigenvalues arise only after aggregate mixing of many original independent coordinates.

## 4. The micro-comb witness converges to the sharp Gaussian reflection

Let all `4m` physical coordinates be independent with density `f_m` from (1.1). Group them into `m` four-vectors `X_m^{(k)}` and put

\[
W_{m,k}=T_0^T X_m^{(k)},
\qquad
Y_m=T_m^T X={1\over\sqrt m}\sum_{k=1}^mW_{m,k}.
\tag{4.1}
\]

For fixed `m`, the `W_{m,k}` are iid, centered, and

\[
\operatorname{Cov}(W_{m,k})
=T_0^T(v_mI_4)T_0=v_mI_3.
\tag{4.2}
\]

The support bound (1.2) makes `|W_{m,k}|` uniformly bounded in both `m` and `k`. Hence the triangular-array Lindeberg condition is automatic. Since `v_m->1/12`,

\[
\boxed{Y_m\Rightarrow G,\qquad G\sim N(0,I_3/12).}
\tag{4.3}
\]

Equivalently, for every fixed `xi`, the block characteristic expansion is uniform,

\[
E\exp\!\left(i{\xi\cdot W_{m,1}\over\sqrt m}\right)
=1-{v_m|\xi|^2\over2m}+O_\xi(m^{-3/2}),
\]

and raising to the `m`th power gives `exp(-|xi|^2/24)`.

Now

\[
Q_m=X^TA_mX=Y_m^TBY_m.
\tag{4.4}
\]

Weak convergence alone would not control density peaks. Here the completed pinned Fresnel--Brascamp--Lieb Theorem F at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

provides the required uniform Fourier tail. Diagonalize `B=O diag(1,1,-1) O^T`; the physical frame is `T_mO`, and every row leverage is exactly

\[
{3\over4m}\le{1\over2}
\tag{4.5}
\]

for `m>=2`. The inputs are cap-one and there is no residual quadratic block. Therefore, writing `Phi_m` for the characteristic function of `Q_m`,

\[
\boxed{
|\Phi_m(t)|\le
\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
}
\tag{4.6}
\]

This majorant is integrable and does not use post-rotation independence.

By (4.3), for every fixed `t`,

\[
\Phi_m(t)\to\Phi_\infty(t)
=E e^{itG^TBG}.
\tag{4.7}
\]

For the Gaussian limit,

\[
|\Phi_\infty(t)|=(1+t^2/36)^{-3/4},
\tag{4.8}
\]

which is also integrable. Dominated convergence therefore gives

\[
\|\Phi_m-\Phi_\infty\|_{L^1(\mathbb R)}\to0.
\tag{4.9}
\]

Fourier inversion yields continuous densities at every finite stage and the stronger uniform convergence

\[
\boxed{
\|p_{Q_m}-p_\infty\|_\infty\to0.
}
\tag{4.10}
\]

This is a continuity statement only for this witness family; it is not the unrestricted continuity theorem.

## 5. Exact limiting peak: `3 sqrt(2)`

Because the Gaussian is isotropic, `G^TBG` has the same law as

\[
R-Z,
\qquad
R=G_1^2+G_2^2,
\qquad Z=G_3^2,
\tag{5.1}
\]

with iid `G_j~N(0,1/12)`. Here `R` is exponential with rate `6`. Therefore

\[
p_\infty(0)=E[6e^{-6Z}]
=6(1+2\cdot6\cdot{1\over12})^{-1/2}
=3\sqrt2.
\tag{5.2}
\]

The global maximum is also at zero. For `s>=0`, direct convolution gives

\[
p_\infty(s)=3\sqrt2\,e^{-6s}.
\tag{5.3}
\]

For `s=-u<0`, up to a positive constant the density is

\[
F(u)=e^{6u}\int_u^\infty z^{-1/2}e^{-12z}\,dz.
\tag{5.4}
\]

For `u>0`,

\[
F'(u)=6F(u)-u^{-1/2}e^{-6u},
\]

while

\[
\int_u^\infty z^{-1/2}e^{-12z}\,dz
\le {u^{-1/2}e^{-12u}\over12},
\]

so

\[
6F(u)\le {1\over2}u^{-1/2}e^{-6u}
<u^{-1/2}e^{-6u}.
\]

Thus `F'(u)<0`, proving

\[
\boxed{\|p_\infty\|_\infty=p_\infty(0)=3\sqrt2.}
\tag{5.5}
\]

Combining (4.10) and (5.5),

\[
\boxed{
\|p_{X^TA_mX}\|_\infty\longrightarrow3\sqrt2.
}
\tag{5.6}
\]

Hence the already source-valid universal obstruction is reconfirmed:

\[
\boxed{C_{\rm univ}\ge3\sqrt2.}
\tag{5.7}
\]

What is new is the structural strength of the witness: every finite `A_m` is entrywise dense and exactly target-valid, every physical marginal has `m` disconnected components, and for every fixed `ell>0` the marginals eventually admit **no** independent uniform convolution factor of width `ell`, yet the output peak still tends to `3sqrt(2)`.

Therefore a sharp proof cannot require extraction of a common positive-width uniform carrier from every marginal. Any carrier-based proof needs a stability/approximation argument whose carrier scale is allowed to vanish, or a different product-preserving smoothing mechanism.

## 6. Completed fleet02/B17 theorem applied to an actual inequality

The newest completed designated-partner result is fleet02/B17's

`QFORM-GROWING-DIRECTION-UNIFORM-CONVOLUTION-BARRIER-v1`,

source report

`yspennstate/math-open-problems@2da74cc48c98dc529e4f3463f3a3f960ffa90cd5`

with deterministic checks at

`yspennstate/math-open-problems@8ff6e7d56ebf33665f965a721771c8e58ae8cb50`.

For the same tetrahedral frame and any additive physical noises `J_i`, it proves

\[
\|p_{X^TA_mX}\|_\infty
\le3\sqrt2+\delta_m,
\qquad
\delta_m={3\over\pi}C_*^{2/3}\varepsilon_m^{1/3},
\tag{6.1}
\]

where

\[
C_*=(4\pi)^{3/2}+6^{3/2},
\qquad
{3\over\pi}C_*^{2/3}
=14.51216338024275\ldots,
\tag{6.2}
\]

and `epsilon_m` is the partner's unit-uniform tetrahedral carrier total-variation error, with `epsilon_m->0` uniformly in the block rotations.

Apply it to the concrete rough product law

\[
\widetilde X_{m,i}=U_i+mC_i,
\tag{6.3}
\]

where `U_i~Uniform[-1/2,1/2]`, `C_i` are iid standard Cauchy, and all variables are independent. Each `mC_i` has no first absolute moment, while the convolution law of `widetilde X_{m,i}` still has density at most one. Use exactly the matrix `A_m` from (3.5), which is the partner frame with all rotations equal to the identity and the dense reflection (3.2). Then every finite stage has active spectrum `{1,1,-1}` and all physical matrix entries are nonzero, and the completed partner theorem gives the actual finite-stage inequality

\[
\boxed{
\|p_{\widetilde X^TA_m\widetilde X}\|_\infty
\le
4.242640687119285\ldots
+14.51216338024275\ldots\,\varepsilon_m^{1/3}.
}
\tag{6.4}
\]

Consequently

\[
\boxed{
\limsup_{m\to\infty}
\|p_{\widetilde X^TA_m\widetilde X}\|_\infty
\le3\sqrt2.
}
\tag{6.5}
\]

This is a direct application of the designated partner theorem to a genuine target-valid finite matrix family with unbounded, momentless physical noise. It is distinct from the comb witness: the Cauchy-convolution family lies inside the partner's carrier class, while the micro-comb family provably escapes every fixed positive carrier width.

## 7. Constraint on a proposed sharp proof

The combined conclusion is a useful two-sided stress test on the same exact dense spectral geometry:

1. **Carrier class:** even arbitrarily rough, momentless additive noise on top of a unit-uniform carrier is asymptotically capped by `3sqrt(2)` by fleet02/B17.
2. **No-fixed-carrier class:** the micro-comb laws have no uniform convolution factor of any fixed positive width, but still approach `3sqrt(2)` from the same minimum-variance diffuse mechanism.

Thus a proof of a sharp `3sqrt(2)` theorem, if true, cannot be organized around a dichotomy saying that near-extremizers possess a fixed-width uniform convolution core. The correct invariant is more plausibly quantitative proximity to the minimum-variance cap-one shape after aggregation, rather than an exact convolution factor at the physical-coordinate level.

This run does **not** show `C_univ=3sqrt(2)`. Remaining possible overshoot mechanisms include non-diffuse rough arrays that do not converge to a Gaussian core, multiple macroscopic components coupled to that rough residual before aggregation, and additional active spectrum interacting before an exact rank-three receiver is isolated.

## 8. Correction compliance

No refuted law-uniform pointwise oscillatory decay is used. No arbitrary-joint coarea bound is used. No positive conditional projection-density moment is used. No fiber supremum is integrated dimension-freely. No independence is asserted after spectral rotation. The only rotation in the Fourier-tail step rotates the deterministic coefficient frame inside the source-pinned Theorem F, which explicitly operates on the original independent physical inputs.

Exact symbolic checks are in `CHECK.py`; executed output is in `CHECK_OUTPUT.txt` and ends with

`PASS_QFORM_B17_MICROCOMB_NO_FIXED_CARRIER`.

The full target and unrestricted continuity remain open.
