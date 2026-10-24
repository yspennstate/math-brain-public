# Same-hypothesis strengthening: `1820 K^2/s` at multiplicity 17

Run: `20260924T145851Z-account01-B18-auto11`  
Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Status: **proved full replacement constant improvement at the same 17-eigenvalue threshold; no 16-eigenvalue theorem claimed.**

The baseline uses deliberately loose constants. Two estimates already implicit in its proofs can be sharpened, after which the pivot/volume parameters can be retuned. No matrix, law, dimension, signature, affine, or support hypothesis is changed.

## The strengthened theorem

Let `X=(X_1,...,X_n)` have independent real coordinate densities bounded by `K`. Let `A=A^T`, and let `b,c` be arbitrary. If

\[
s_{17}(A)\ge s>0,
\]

then `X^T A X+b^T X+c` has a density and

\[
\boxed{\|p_Q\|_\infty<1820\,K^2/s.}
\]

The proof is exactly the manuscript architecture with the changes proved below.

---

## 1. Sharper elementary kernel

For

\[
J(d)=\int_{-1}^1 |x|^{-1/2}|x-d|^{-1/2}\,dx,
\qquad d\ne0,
\]

one has the stronger bound

\[
\boxed{J(d)\le 8+2\log_+(1/|d|).}
\tag{1}
\]

### Proof

By reflection it is enough to take `d>0`.

If `0<d<=1`, direct substitutions on `[-1,0]`, `[0,d]`, and `[d,1]` give

\[
J(d)
=2\operatorname{arsinh}(d^{-1/2})+\pi
 +2\operatorname{arcosh}(d^{-1/2}).
\tag{2}
\]

Put `u=d^{-1/2}>=1`. Since

\[
\operatorname{arsinh}u
=\log(u+\sqrt{u^2+1})
\le\log((1+\sqrt2)u),
\]

and

\[
\operatorname{arcosh}u
=\log(u+\sqrt{u^2-1})
\le\log(2u),
\]

we obtain

\[
J(d)
\le \pi+2\log(2(1+\sqrt2))+2\log(1/d).
\]

The constant before the logarithm is `<8`: use `pi<4`, `sqrt2<3/2`, hence `2(1+sqrt2)<5`, and `log5<2` because `e^2>1+2+2^2/2=5`. This proves (1) for `d<=1`.

If `d>=1`, the same substitutions give

\[
J(d)=2\operatorname{arsinh}(d^{-1/2})
+2\arcsin(d^{-1/2})
\le 2\operatorname{arsinh}(1)+\pi<8.
\]

Thus (1) holds for every nonzero `d`. QED.

The coefficient of the logarithmic singularity is now `2`, rather than the baseline's convenient `3`.

---

## 2. Keep the exact hyperbolic constant already proved before rounding

In the baseline proof of `lem:hyperbola`, before the line that rounds the branch integral to `<6+...`, the proof has already established for each branch

\[
\frac{15}{2}\log2
+\log_+\frac{32}{|z-v|\Lambda}.
\]

Since `Lambda>=2/sqrt(D)`, the identical proof therefore gives the stronger envelope

\[
\boxed{
 p_{q(W)}(z)
 \le D^{-1/2}
 \left(
 \frac{15}{2}\log2+
 \log_+\frac{16\sqrt D}{|z-v|}
 \right).
}
\tag{3}
\]

No new analytic input is needed; this only refrains from replacing `(15/2)log2` by `6`.

---

## 3. Retuned pivot/volume parameters

Set

\[
\boxed{
\eta=\frac1{45},\qquad
\rho=\sqrt\kappa=\frac{749}{50000},\qquad
\kappa=\rho^2.
}
\tag{4}
\]

We verify the only structural inequality that matters.

With no `eta`-pivot,

\[
|a_{ii}|<\eta,
\qquad
|a_{ij}|<a_0:=\sqrt{\eta+\eta^2}=\frac{\sqrt{46}}{45}.
\tag{5}
\]

For a sampled seed of order `1<=r<=4` satisfying `V_{r+1}<kappa V_r`, the baseline completion lemma gives

\[
\varepsilon:=\|E\|_F\le(r+1)\rho\le5\rho.
\]

On the `r+1` large diagonal locations in the complement,

\[
|R_{ii}|\ge1-5\rho-\eta,
\qquad
|R_{ij}|\le a_0+5\rho.
\]

It is therefore enough that

\[
1-\eta-5\rho>4(a_0+5\rho),
\]

or equivalently

\[
1-\eta-4a_0>25\rho.
\tag{6}
\]

For (4), (6) is exact:

\[
\frac{44-4\sqrt{46}}{45}>\frac{749}{2000}.
\]

Indeed this is equivalent to

\[
\sqrt{46}<\frac{10859}{1600},
\]

and squaring gives

\[
46=\frac{117760000}{2560000}
<\frac{117917881}{2560000}.
\]

Thus the strict diagonal-dominance contradiction in `prop:volume` survives for every `r<=4`.

For `r=0`, `V_1<kappa` gives

\[
\|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\eta+\rho<1,
\]

again contradicting any singular value at least one. Consequently the baseline spectral-to-volume proposition remains valid, for `k<=5`, with the retuned parameters (4):

\[
\boxed{
A\text{ no pivot},\quad s_{4k-3}(A)\ge1
\implies V_k(A)\ge\kappa^k.
}
\tag{7}
\]

---

## 4. Retuned no-pivot analytic bounds

The baseline random-cut identity gives, from (7), a physical cut with

\[
Z_k^{-1/(2k)}\le 2\kappa^{-1/2}=\frac2\rho.
\]

Thus:

### Order five

\[
\|p_Q\|_\infty
\le5e\frac2\rho
=\frac{10e}{\rho}.
\tag{8}
\]

A completely elementary upper bound `e<2.72` suffices. For example,

\[
e=\sum_{n=0}^\infty\frac1{n!}
<\sum_{n=0}^9\frac1{n!}
+\frac{11}{10\cdot10!}
=\frac{4697191}{1728000}<2.72.
\]

Therefore

\[
\frac{10e}{\rho}
<\frac{1360000}{749}<1820.
\tag{9}
\]

### Order three

The full negative-half-moment estimate becomes

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le12\sqrt{e/\rho}.
\tag{10}
\]

Using merely `e<3`,

\[
\frac e\rho<\frac{150000}{749}<225,
\]

so the right side of (10) is `<180`. In particular the no-pivot `s_9` branch has truncated half-potential `<180`.

---

## 5. Retuned pivot half-potential bound

Retain the baseline

\[
L_0=4+4\log16.
\]

We will use the elementary numerical inequalities

\[
\log2<0.694,\qquad \sqrt{45}<6.709.
\tag{11}
\]

They can be checked without numerical black boxes: for the first, with `x=347/500`, the fourth Taylor partial sum

\[
1+x+x^2/2+x^3/6+x^4/24>2,
\]

so `e^{0.694}>2`; for the second, `6.709^2=45.010681>45`.

### Scalar pivot inside the nine-mode proposition

By the sharpened kernel (1), the baseline conditional square profile gives

\[
H(Q)
\le\eta^{-1/2}(8+2L_0)
=\sqrt{45}\,(16+32\log2)
<257.
\tag{12}
\]

### Definite pair

Exactly as in the manuscript,

\[
H(Q)\le4\pi\eta^{-1/2}<4\cdot4\cdot6.709<108.
\tag{13}
\]

### Indefinite pair

Use (3), the baseline log-kernel integral `<=8`, and

\[
\log_+(16\sqrt D)
\le\log16+\frac12\log_+D.
\]

Since `sup_{D>0} D^{-1/2} log_+D=2/e`, we obtain

\[
\begin{aligned}
H(Q)
&\le \eta^{-1/2}
\left(4\cdot\frac{15}{2}\log2+8+4\log16\right)
+\frac4e\\
&=\sqrt{45}\,(8+46\log2)+\frac4e.
\end{aligned}
\tag{14}
\]

Using (11) and `e>2`,

\[
H(Q)<6.709(8+46\cdot0.694)+2
=269.850116<270.
\tag{15}
\]

Thus every pivot branch with two surviving unit spectral directions obeys

\[
\boxed{H(Q)<270.}
\tag{16}
\]

Combining (10) and (16), the nine-eigenvalue proposition strengthens to

\[
\boxed{
 s_9(A)\ge1
 \implies H(Q)<270,
 \qquad
 \sup_a\mathbb E|Q-a|^{-1/2}<271.
}
\tag{17}
\]

---

## 6. Main normalized theorem with constant 1820

Assume `K=s=1`.

1. **No pivot.** Equation (9) gives `||p_Q||_infty<1820`.
2. **Scalar pivot.** Its Schur complement retains at least sixteen unit spectral directions, hence at least nine. The square profile and (17) give
   \[
   \|p_Q\|_\infty
   <\eta^{-1/2}\,271
   =271\sqrt{45}
   <271\cdot6.709
   =1818.139<1820.
   \tag{18}
   \]
3. **Definite pair.** `||p_Q||_infty<=pi/sqrt(eta)=pi sqrt45<27`.
4. **Indefinite pair.** The sharper hyperbolic envelope (3), the surviving Schur direction, and the baseline logarithmic-potential bound give
   \[
   p_Q(z)
   \le
   \sqrt{45}\left(\frac{15}{2}\log2+\log16+L_0\right)+\frac1e
   <156.
   \tag{19}
   \]

Thus every normalized branch is `<1820`.

For general `K,s`, use the identical baseline scaling `Y=KX` and `Q=(s/K^2) Qtilde`. This gives

\[
\boxed{
\|p_Q\|_\infty<1820\frac{K^2}{s}.
}
\tag{20}
\]

This is a complete replacement proof of the stronger numerical constant at multiplicity 17.

---

## 7. Why this still does not lower 17 to 16

The retuning changes constants, not the endpoint exponents/ranks. At the terminal interpolation order `r=4`, `s_16` plus global rank loss `3r=12` transfers only four large diagonal entries, while the restricted rank-four contradiction needs five. Separately, order-four crossing volume still gives only the nonintegrable characteristic-function endpoint `O(|t|^{-1})`.

I read the current source-pinned `s_16` improvements: the near-rank-four reduction, carrier-transverse same-bank mass, and mixed four-plus-one exterior identity. They pay substantial sub-branches but leave explicit row-leverage/self-coordinate overlap traps. No complete product-preserving receiver for those traps is currently proved in the material checked here. Therefore this artifact does **not** claim `s_16`.

---

## 8. Prior-art patch recommended for the manuscript

This is bibliography/positioning, not a dependency of the proof above.

- J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp–Lieb inequalities: finiteness, structure and extremals*, Geom. Funct. Anal. 17 (2008), 1343–1415, DOI `10.1007/s00039-007-0619-6`.
- M. Rudelson, R. Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, Int. Math. Res. Not. 2015(19), 9594–9617, DOI `10.1093/imrn/rnu243`.
- G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889, DOI `10.1007/s11856-016-1431-5`. Their cap-one product-marginal bound is `2^{d/2}` and is sharper than the manuscript's self-contained `e^{d/2}` estimate.
- J. Banks, J. Garza Vargas, A. Kulkarni, N. Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, Ann. Inst. H. Poincaré Probab. Statist. 60(4) (2024), 2736–2766, DOI `10.1214/23-AIHP1400`. Their Theorem 2.1 is explicitly “Density of Quadratic Forms” for a bilinear-affine form, and Corollary 2.4 has a scalar geometric-mean singular-value improvement. It does not contain arbitrary same-bank quadratic phases and so does not subsume the present cut argument.
- R. Herry, D. Malicet, G. Poly, *Regularity of laws via Dirichlet forms — Application to quadratic forms in independent and identically distributed random variables*, Probab. Theory Relat. Fields 191 (2025), 523–567, DOI `10.1007/s00440-024-01332-x`. This has materially narrower iid/Gaussian-field-representation hypotheses.

No novelty assertion follows from the literature search; the recommendation is only to state the relation to known results accurately.
