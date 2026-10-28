# account01/B14 auto11 — shear-before-conditioning localization and an optimized logarithmic fragmentation barrier

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: translations and localization. Status: **NEW SUPPORTING LOCALIZATION THEOREM + TARGET-VALID CONDITIONING-ORDER BARRIER; FULL QFORM REMAINS OPEN.** Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Source pins actually used

2. Completed physical-pair logarithmic envelope: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. The only part used below is the exact pair envelope
   
   `p(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa |t-R|))`.
3. Assigned partner `account02/B14` completed report: `yspennstate/math-open-problems@8c74cde9c5de560923027d3af8debe2da5c79bc4`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T025915Z-account02-B14-QFORM-r24/REPORT.md`. I use its exact conjugate-fiber identity `||f_{V|U=u}||_infinity = 1/(2m_N(u))` and exact overlap-power formula.
4. Previous own B14 mass-proportional logarithmic compiler: `yspennstate/math-open-problems@59f3c6d5c18c5bbd6073f7061d32e54ff7bde23c`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B14/20260923T031130Z-account01-B14-QFORM-r28/REPORT.md`. Its hypothesis is kept explicit below; the present run shows that an unnormalized cap alone does **not** imply the mass-proportional hypothesis.

No post-rotation independence, arbitrary-joint coarea, bounded-diameter localization, fixed fragment count, moment assumption, or uniform pointwise quadratic Fourier decay is used.

---

## 1. Exact conjugate-shear cap lemma

Let `X,X'` be independent real random variables with densities bounded by one. Put

\[
U=X-X',\qquad V=X+X'.
\]

For arbitrary real `alpha,beta`, define

\[
W=V-\alpha U-\beta=(1-\alpha)X+(1+\alpha)X'-\beta.
\]

### Theorem 1 (QFORM-CONJUGATE-SHEAR-CAP-v1)

`W` has a density and

\[
\boxed{
\|p_W\|_\infty
\le
\frac{1}{\max\{|1-\alpha|,|1+\alpha|\}}
\le 1.
}
\tag{1.1}
\]

The result is completely independent of translations, fragment separation, support diameter and moments.

### Proof

Set `a=1-alpha`, `b=1+alpha`. If both are nonzero, the density of `aX` has mass one and cap at most `1/|a|`; likewise `bX'` has cap at most `1/|b|`. Since the two variables are independent,

\[
p_W=p_{aX}*p_{bX'}(\,\cdot+\beta\,),
\]

and Young's `L^infinity * L^1` bound in either order gives

\[
\|p_W\|_\infty
\le
\min\{ |a|^{-1},|b|^{-1}\}
=
\frac1{\max\{|a|,|b|\}}.
\]

If one coefficient is zero, the other has magnitude two and the same formula follows directly. Finally

\[
|1-\alpha|+|1+\alpha|\ge 2,
\]

so their maximum is at least one. This proves (1.1). ∎

### Conditional/product version

Let `(X_i,X_i')`, `1<=i<=m`, be mutually independent pairs of cap-one inputs and let `Z` be independent of all pairs. For deterministic `alpha_i` and arbitrary measurable shifts `beta_i(Z)`, set

\[
W_i=V_i-\alpha_i U_i-\beta_i(Z).
\]

Conditioned on `Z=z`, the variables `W_i` remain independent because they use disjoint original-coordinate pairs, and each has density cap at most one by (1.1), uniformly in `z`. Therefore **any downstream theorem whose only probabilistic input is conditional product independence plus one-dimensional cap one may be applied after this shear with exactly the same constant**. This is a zero-tax translation/localization rule.

The important point is proof order: one should form the sheared marginal `W_i` first. Conditioning on `U_i` first can create arbitrarily large normalized conditional caps even though `W_i` itself remains cap one.

---

## 2. A target-valid three-large-eigenvalue family controlled uniformly under every shear

Let `X_1,...,X_4` be independent cap-one variables. Put

\[
U=X_3-X_4,\qquad V=X_3+X_4,
\]

and for fixed `alpha` set

\[
W_\alpha=V-\alpha U=(1-\alpha)X_3+(1+\alpha)X_4.
\]

Consider

\[
Q_\alpha=2X_1X_2+\frac12 W_\alpha^2. \tag{2.1}
\]

The matrix of the first term is `[[0,1],[1,0]]`, with eigenvalues `+1,-1`. The second term is the rank-one matrix

\[
\frac12
\begin{pmatrix}1-\alpha\\1+\alpha\end{pmatrix}
\begin{pmatrix}1-\alpha&1+\alpha\end{pmatrix},
\]

whose nonzero eigenvalue is

\[
\frac12\big((1-\alpha)^2+(1+\alpha)^2\big)=1+\alpha^2\ge1.
\]

Hence the four-dimensional matrix has spectrum

\[
\{1,-1,1+\alpha^2,0\},
\]

so it lies in the exact QFORM target for every real `alpha`.

By Theorem 1, `W_alpha` has density cap at most one and is independent of `(X_1,X_2)`. Apply the physical-pair log envelope to the pair block

\[
B=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad D=|\det B|=1,
\qquad \kappa=\sigma_{\min}(B)=1.
\]

The remainder is `R=W_alpha^2/2`. For every `rho>0` and every center `t`, the set

\[
\{w: |w^2/2-t|<\rho\}
\]

has Lebesgue measure at most `4 sqrt(rho)`. Therefore

\[
\sup_t\Pr\{|R-t|<\rho\}\le \min\{1,4\sqrt\rho\}. \tag{2.2}
\]

For any `r>0`, layer cake gives

\[
\begin{aligned}
\mathbb E\log_+\frac{2r^2}{|t-R|}
&=\int_0^\infty
\Pr\{|t-R|<2r^2e^{-s}\}\,ds\\
&\le\int_0^\infty \min\{1,4\sqrt2\,r e^{-s/2}\}\,ds\\
&=2\Psi(4\sqrt2\,r),
\end{aligned}
\tag{2.3}
\]

where

\[
\Psi(z)=
\begin{cases}
z,&0\le z\le1,\\
1+\log z,&z\ge1.
\end{cases}
\]

Consequently

\[
\|p_{Q_\alpha}\|_\infty
\le
\inf_{r>0}
\left[
\frac{2\sqrt2}{r}+2\Psi(4\sqrt2 r)
\right]. \tag{2.4}
\]

On the low branch `r<=1/(4sqrt(2))` the expression decreases up to the branch endpoint and is at least `18`. On the high branch it equals

\[
\frac{2\sqrt2}{r}+2+2\log(4\sqrt2 r),
\]

whose unique minimizer is `r=sqrt(2)`. Thus

\[
\boxed{
\|p_{Q_\alpha}\|_\infty
\le 4+2\log 8
<8.159,
\qquad \text{uniformly in }\alpha.
}
\tag{2.5}
\]

This is a genuinely target-valid inequality, and it is insensitive to arbitrary translations or remote fragments of any input law.

The same estimate remains true after conditioning on any independent outside coordinates `Z` if the conditional form is allowed arbitrary affine shifts of the active pair and replaces `W_alpha` by

\[
V-\alpha U-\beta(Z),
\]

because Theorem 1 is uniform in the translation `beta`, and the pair-log envelope is uniform in deterministic affine shifts of the active pair. An additional scalar term depending only on `Z` merely shifts the output before the conditional estimate is averaged.

---

## 3. The partner fragmented family: every unbounded normalized-cap penalty is unsafe

Now use the assigned partner result at its exact source. Let

\[
E_N=\bigcup_{j=1}^N [4^j,4^j+N^{-1}],
\]

and let `X,X'` be iid uniform on `E_N`. Put

\[
U=X-X',\qquad V=X+X',\qquad
m_N(u)=|E_N\cap(E_N-u)|.
\]

The partner proves

\[
p_U(u)=m_N(u),
\qquad
\|p_{V\mid U=u}\|_\infty=\frac1{2m_N(u)}
\quad(m_N(u)>0). \tag{3.1}
\]

It also proves, for every `gamma>-1`,

\[
I_\gamma(N):=\int m_N(u)^\gamma\,du
=
\frac{2}{\gamma+1}
\left[(1-N^{-1})N^{1-\gamma}+N^{-1}\right]. \tag{3.2}
\]

There is a stronger consequence than the positive-power barrier recorded previously.

### Theorem 2 (QFORM-UNBOUNDED-NORMALIZED-CAP-PENALTY-UNSAFE-v1)

Let

\[
M_N(u)=\frac1{2m_N(u)}.
\]

For every nonnegative nondecreasing function `Phi`,

\[
\boxed{
\mathbb E\,\Phi(M_N(U))
\ge
\left(1-\frac1N\right)\Phi(N/2).
}
\tag{3.3}
\]

In particular, if `Phi(s)->infinity`, then averaging a conditional certificate of the form

\[
\|p_{Q\mid U=u}\|_\infty\le C\,\Phi(M_N(u))
\]

cannot yield a fragmentation-uniform constant by itself.

### Proof

Each fragment of `E_N` has probability mass `1/N`. Therefore the probability that `X` and `X'` lie in distinct fragments is `1-1/N`. For distinct fragments, the corresponding difference interval has overlap height at most `1/N`; the centers `4^j-4^k` are distinct (their `2`-adic valuations determine the smaller index), so these cross-difference triangles do not stack. Hence on this event

\[
m_N(U)\le \frac1N,
\qquad
M_N(U)\ge \frac N2.
\]

Monotonicity of `Phi` gives (3.3). ∎

Thus **not only positive powers, but every unbounded monotone dependence on the normalized conjugate-fiber cap is unsafe**. A logarithm is already too much.

---

## 4. Exact logarithmic divergence of the optimized condition-first pair-log compiler

This section applies the partner result to an actual target inequality and compares the two proof orders sharply.

Take `X_3,X_4` iid uniform on `E_N`, let `X_1,X_2` be arbitrary independent cap-one laws, and keep the target-valid form (2.1). Conditional on `U=u`, the sheared variable

\[
W_\alpha=V-\alpha u
\]

is merely a translate of `V`, so its conditional density cap is still

\[
M(u)=\frac1{2m_N(u)}\ge\frac12. \tag{4.1}
\]

For a scalar law of cap `M`, the same square-sublevel calculation gives

\[
\sup_t\Pr\{|W^2/2-t|<\rho\}\le\min\{1,4M\sqrt\rho\}. \tag{4.2}
\]

Feeding (4.2) into the pair-log envelope gives the conditional majorant

\[
F(M)=
\inf_{r>0}
\left[
\frac{2\sqrt2}{r}+2\Psi(4\sqrt2 M r)
\right]. \tag{4.3}
\]

Since `M>=1/2`, the global minimizer is always on the logarithmic branch. Differentiation gives `r=sqrt(2)`, hence

\[
\boxed{
F(M)=4+2\log(8M).
}
\tag{4.4}
\]

Using (4.1),

\[
F(M(u))=4+2\log\frac4{m_N(u)}. \tag{4.5}
\]

The average of the **optimized conditional certificate** is therefore

\[
B_N
=4+2\log4
+2\int m_N(u)\log\frac1{m_N(u)}\,du. \tag{4.6}
\]

Differentiate the partner's exact formula (3.2) at `gamma=1`. Since

\[
I_1(N)=1,
\]

we obtain

\[
I_1'(N)
=-\frac12-\left(1-\frac1N\right)\log N,
\]

so

\[
\boxed{
\int m_N(u)\log\frac1{m_N(u)}\,du
=
\frac12+\left(1-\frac1N\right)\log N.
}
\tag{4.7}
\]

Substitution gives the exact proof bound

\[
\boxed{
B_N
=
5+2\log4
+2\left(1-\frac1N\right)\log N,
}
\tag{4.8}
\]

which diverges like `2 log N`.

By contrast, **shear before conditioning** uses (1.1) and gives the direct bound

\[
\boxed{
\|p_{Q_\alpha}\|_\infty\le4+2\log8<8.159
}
\tag{4.9}
\]

for the very same laws, every `N`, and every `alpha`.

This is a sharper conditioning-order barrier than the earlier half-Holder `sqrt(N)` certificate loss: even after optimizing the physical-pair logarithmic envelope and reducing the local cap cost from a power to a logarithm, normalized thin-fiber conditioning still incurs an unavoidable `log N` tax on this target-valid family.

---

## 5. What the result changes in the localization interface

The previous B14 mass-proportional logarithmic lemma remains correct under its explicit hypothesis

\[
\nu_u\{|R-t|<\rho\}
\le w(u)\min\{1,K\rho^\alpha\}.
\]

The present run shows that this hypothesis does **not** follow merely from saying that the unnormalized conjugate fiber has a bounded density. For square singularities, a fiber of mass `m` and fixed unnormalized density cap can still contribute order

\[
m\log(1/m)
\]

to the logarithmic kernel. The exact entropy (4.7) then diverges over remote fragmented laws.

The correct zero-tax operation in the new branch is stronger and simpler:

1. if the moving shift is an affine shear `V-alpha U-beta`, form that sheared marginal **before** conditioning on `U`;
2. Theorem 1 returns a genuine cap-one scalar law with the original product provenance intact;
3. only then apply the pair/ridge/square smoothing theorem;
4. condition on genuinely independent outside variables only after this product-preserving shear.

This handles arbitrary translations, distant fragments and unbounded supports with no moments, and with no localization constant loss, for the entire coordinatewise shear class.

---

## 6. Remaining implication toward full QFORM

The full conjecture is not proved. The first unpaid structural step for this B14 line is now precise:

> In the surviving heavy-star / diffuse / no-uniform-pivot configurations, rewrite each dangerous conditioning-generated translation as either (a) a coordinatewise conjugate shear covered by Theorem 1, or (b) a genuinely joint aggregate that is smoothed **before** normalized fiber conditioning. If neither is possible, quantify the non-shear kernel leakage and route it to an existing bank/ridge/cross certificate without a normalized-cap penalty.

Theorem 2 shows why an argument that conditions first and then pays **any unbounded monotone function** of the conjugate-fiber density cap cannot be the universal localization step. Theorem 1 gives an exact escape whenever the dependence is a coordinatewise affine shear.

Claim labels for this run: `QFORM-CONJUGATE-SHEAR-CAP-v1`; `QFORM-SHEAR-BEFORE-CONDITIONING-PAIRLOG-v1`; `QFORM-UNBOUNDED-NORMALIZED-CAP-PENALTY-UNSAFE-v1`; `QFORM-PAIRLOG-ENTROPY-BARRIER-v1`.
