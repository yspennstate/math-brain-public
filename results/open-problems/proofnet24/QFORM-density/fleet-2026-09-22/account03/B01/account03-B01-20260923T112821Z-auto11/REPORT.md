SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T11:28:21Z.
attacking: a distribution-domain L^p-L^q replacement for false pointwise Fresnel decay: one diffuse rank-one bilinear bank plus one source-disjoint grouped square, followed by exact signed-Fejer transfer.

# account03/B01 — rank-one bilinear plus independent square: an L^p-L^q N3 receiver

Run: `account03-B01-20260923T112821Z-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Oscillatory replacement`  
Status: **NEW SUPPORTING TARGET-VALID N3 THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Source and correction boundary

The full target remains open: for arbitrary independent real inputs with densities at most one and arbitrary real symmetric A with at least three eigenvalues of absolute value at least one, prove a universal output-density bound or give a valid counterexample.


This proof explicitly respects the current corrections:

- no law-uniform positive-power pointwise quadratic-phase decay is used;
- no independence is asserted after rotating eigen-coordinates;
- no arbitrary-joint rank-three coarea theorem or worst conditional-density moment is used;
- no uniformly good fixed physical minor is assumed;
- no small matrix coefficient is discarded as a small random perturbation on unbounded inputs;
- all stochastic conditioning is on disjoint ORIGINAL-coordinate banks.

The designated completed partner result actually applied is account04/B01's grouped-square/signed-Fejer report

`yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T234537Z-account04-B01-grouped-square-fejer-r2/REPORT.md`.

Its Section 5 proves the exact identity

\[
\|p_\mu\|_\infty=\sup_{T>0,\,y\in\mathbb R}D_T\mu(y),
\tag{1.1}
\]

where

\[
D_T\mu(y)=\frac1{2\pi}\int_{-T}^T
\left(1-\frac{|t|}{T}\right)
\operatorname{Re}\!\left(e^{-ity}\widehat\mu(t)\right)dt,
\tag{1.2}
\]

with both sides infinite if the law has no bounded density. The same partner report also records the source-valid one-dimensional product-projection estimate

\[
\|p_{a^TX}\|_\infty\le \frac{\sqrt2}{\|a\|_2}
\tag{1.3}
\]

for an original-coordinate product vector with coordinate density caps one.

This run deliberately changes mechanism from the preceding B01 rank-two-cross sequence. The new smoothing is a distribution-domain `L^p * L^q -> L^infinity` argument for a **rank-one** grouped bilinear block plus a source-disjoint square.

## 2. The phase-aligned pointwise counterexample remains

Fix `s>0` and `0<delta<pi/2`. The set

\[
E_\infty=\{x:\operatorname{dist}(s x^2,2\pi\mathbb Z)\le\delta\}
\]

has infinite Lebesgue measure: the component lengths around the positive solutions `x_k=sqrt(2 pi k/s)` are comparable to `k^{-1/2}`, whose sum diverges. Hence one may choose a finite union of intervals `E\subset E_\infty` of total measure exactly one. For the admissible cap-one probability density `f=1_E`,

\[
\operatorname{Re}\int e^{isx^2}f(x)\,dx\ge\cos\delta.
\tag{2.1}
\]

Thus there is no law-uniform estimate `|E exp(isX^2)| <= C |s|^{-alpha}` with any `alpha>0`. The theorem below never asserts or uses such a bound.

## 3. A translation-uniform inverse-moment lemma

### Lemma 3.1

Let `Y` be a real random variable with probability density bounded by `m<infinity`. For every `0<beta<1`, uniformly in `s in R`,

\[
\boxed{
\mathbb E|Y-s|^{-\beta}\le \frac{(2m)^\beta}{1-\beta}.
}
\tag{3.1}
\]

### Proof

The density cap gives

\[
\Pr\{|Y-s|<r\}\le\min(1,2mr).
\tag{3.2}
\]

By layer cake,

\[
\mathbb E|Y-s|^{-\beta}
=\int_0^\infty
\Pr\{|Y-s|<t^{-1/\beta}\}\,dt.
\]

Put `T=(2m)^beta`. Split at `T` and use (3.2):

\[
\begin{aligned}
\mathbb E|Y-s|^{-\beta}
&\le T+2m\int_T^\infty t^{-1/\beta}\,dt \\
&=(2m)^\beta+
\frac{\beta}{1-\beta}(2m)^\beta
=\frac{(2m)^\beta}{1-\beta}.
\end{aligned}
\]

This proves (3.1). QED.

## 4. Rank-one affine-slope packet in L^p

Partition the original independent coordinates into disjoint banks `I,J,D,C`. Condition on `X_C=c`. Let

\[
U=a^TX_I+h(c),\qquad \sigma_I=\|a\|_2>0,
\]

let `b in R^J` with `sigma_J=||b||_2>0`, let `gamma !=0`, and let `d(c) in R^J`. Let `F_c(X_I)` be arbitrary measurable. Define

\[
Y_c=F_c(X_I)+\bigl(2\gamma U b+d(c)\bigr)^T X_J.
\tag{4.1}
\]

Set

\[
\kappa=|\gamma|\sigma_I\sigma_J.
\tag{4.2}
\]

### Lemma 4.1

For every `p>1`, with `beta=(p-1)/p`, `Y_c` has a density and

\[
\boxed{
\|p_{Y_c}\|_p\le p\,2^\beta\,\kappa^{-\beta},
}
\tag{4.3}
\]

uniformly in `c`, `F_c`, `h(c)` and `d(c)`.

### Proof

Condition further on `X_I`. Except on a null event, the coefficient

\[
w(U)=2\gamma U b+d(c)
\]

is nonzero. By the product-projection theorem (1.3), the conditional density of `w(U)^T X_J` is bounded by

\[
M(U)=\frac{\sqrt2}{\|w(U)\|_2}.
\]

A probability density bounded by `M` has `L^p` norm at most `M^beta`, because `int f^p <=M^{p-1}int f`. Translation by `F_c(X_I)` does not alter the norm. Minkowski therefore gives

\[
\|p_{Y_c}\|_p
\le 2^{\beta/2}\,\mathbb E\|w(U)\|^{-\beta}.
\tag{4.4}
\]

Project `w(U)` onto `b/||b||`. With

\[
u_0=-\frac{\langle d(c),b\rangle}{2\gamma\sigma_J^2},
\]

we have

\[
\|w(U)\|_2\ge
2|\gamma|\sigma_J|U-u_0|.
\tag{4.5}
\]

The variable `U` is a translate of `a^TX_I`, so by (1.3) its density cap satisfies

\[
m_U\le\frac{\sqrt2}{\sigma_I}.
\tag{4.6}
\]

Lemma 3.1 with `1/(1-beta)=p` yields

\[
\mathbb E|U-u_0|^{-\beta}
\le p(2m_U)^\beta
\le p\,2^{3\beta/2}\sigma_I^{-\beta}.
\tag{4.7}
\]

Combining (4.4)-(4.7), the powers of two are

\[
2^{\beta/2}\,2^{-\beta}\,2^{3\beta/2}=2^\beta,
\]

which proves (4.3). QED.

This is not a bounded-density theorem for the rank-one bilinear packet by itself; the `L^p` norm is the currency used by an independent third direction below.

## 5. One grouped square in the conjugate L^q space

Let `Z` have a probability density `g` bounded by `m`, let `lambda !=0`, and let `s` be arbitrary. Put

\[
S=\lambda(Z+s)^2.
\]

### Lemma 5.1

For every `p>2`, set `q=p/(p-1) in (1,2)`. Then

\[
\boxed{
\|p_S\|_q
\le
2^{1/p}
\left(\frac{p-1}{p-2}\right)^{(p-1)/p}
 m^{2/p}|\lambda|^{-1/p}.
}
\tag{5.1}
\]

### Proof

It suffices first to take `lambda=1` and absorb `s` into the density `g`. For `W=Z^2`,

\[
h(w)=\frac{g(\sqrt w)+g(-\sqrt w)}{2\sqrt w}\,1_{w>0}.
\tag{5.2}
\]

Write `beta=q-1=1/(p-1)`. Changing variables `w=r^2` and using `(x+y)^q <=2^{q-1}(x^q+y^q)` gives

\[
\int h(w)^q\,dw
\le\int_{\mathbb R}g(x)^q|x|^{1-q}\,dx.
\tag{5.3}
\]

Since `g<=m`,

\[
\int g(x)^q|x|^{-\beta}\,dx
\le m^\beta\,\mathbb E|Z|^{-\beta}.
\]

Lemma 3.1 gives

\[
\int h^q
\le \frac{2^\beta m^{2\beta}}{1-\beta}.
\tag{5.4}
\]

Taking the `q`th root, using `beta/q=1/p` and `1/q=(p-1)/p`, yields (5.1) for `lambda=1`. Scaling by `lambda` multiplies an `L^q` density norm by `|lambda|^{1/q-1}=|lambda|^{-1/p}`. QED.

Now take

\[
Z=z^TX_D+k(c),\qquad \sigma_D=\|z\|_2>0,
\]

on the source-disjoint original-coordinate bank `D`, and define

\[
\rho=|\lambda|\sigma_D^2.
\tag{5.5}
\]

By (1.3), `m<=sqrt(2)/sigma_D`. Therefore Lemma 5.1 becomes

\[
\boxed{
\|p_{\lambda Z^2}\|_q
\le
2^{2/p}
\left(\frac{p-1}{p-2}\right)^{(p-1)/p}
\rho^{-1/p}.
}
\tag{5.6}
\]

## 6. Main theorem: rank-one bilinear plus a source-disjoint square

### Theorem 6.1 (`QFORM-RANK1-BILINEAR-PLUS-SQUARE-LP-v1`)

Let `I,J,D,C` be disjoint original-coordinate banks. Conditional on `X_C=c`, suppose

\[
\boxed{
Q_c=
F_c(X_I)
+\bigl(2\gamma(a^TX_I+h(c))b+d(c)\bigr)^TX_J
+\lambda(z^TX_D+k(c))^2+r(c),
}
\tag{6.1}
\]

where `gamma,lambda !=0`, `a,b,z` are nonzero, and `F_c,h,d,k,r` are arbitrary measurable functions compatible with (6.1). Put

\[
\kappa=|\gamma|\|a\|_2\|b\|_2,
\qquad
\rho=|\lambda|\|z\|_2^2.
\tag{6.2}
\]

Then for every real `p>2`, the law of `Q` has a continuous `C_0(R)` density and

\[
\boxed{
\|p_Q\|_\infty
\le
K_p\,\kappa^{-(p-1)/p}\rho^{-1/p},
}
\tag{6.3}
\]

where

\[
K_p=
 p\,2^{1+1/p}
\left(\frac{p-1}{p-2}\right)^{(p-1)/p}.
\tag{6.4}
\]

In particular, the clean choice `p=3` gives the exact constant

\[
\boxed{
\|p_Q\|_\infty
\le12\,\kappa^{-2/3}\rho^{-1/3}.
}
\tag{6.5}
\]

Consequently every interval `L` satisfies

\[
\boxed{
\Pr\{Q\in L\}
\le12\,\kappa^{-2/3}\rho^{-1/3}|L|.
}
\tag{6.6}
\]

### Proof

Conditional on `X_C=c`, the bank `D` is independent of the pair `(I,J)`. Hence the first two terms of (6.1) have density `p_{Y_c}` from Lemma 4.1, while the square term has density from Lemma 5.1, and the conditional law of `Q_c-r(c)` is their convolution.

For conjugate exponents `p` and `q=p/(p-1)`, Young's inequality gives

\[
\|p_{Q\mid C=c}\|_\infty
\le\|p_{Y_c}\|_p\|p_{\lambda Z^2}\|_q.
\]

Multiplying (4.3) and (5.6) gives

\[
\|p_{Q\mid C=c}\|_\infty
\le
p\,2^{(p-1)/p+2/p}
\left(\frac{p-1}{p-2}\right)^{(p-1)/p}
\kappa^{-(p-1)/p}\rho^{-1/p},
\]

and `(p-1)/p+2/p=1+1/p`, proving (6.3) uniformly in `c`. Averaging the conditional interval inequality over `C` proves the unconditional density cap.

For regularity, `p_{Y_c} in L^p` and `p_{lambda Z^2} in L^q` with finite conjugate exponents. The standard translation-continuity approximation for `L^p * L^q` shows each conditional convolution belongs to `C_0(R)`. It is uniformly bounded by (6.3). Dominated convergence in `c` gives continuity and vanishing at infinity for the averaged density. Thus `p_Q in C_0(R)`.

At `p=3`,

\[
K_3=3\,2^{4/3}\,2^{2/3}=12,
\]

which proves (6.5)-(6.6). QED.

### Scope boundary

The theorem allows arbitrary same-bank curvature and arbitrary measurable dependence in the **I-side** term `F_c(X_I)` and arbitrary outside conditioned curvature through `c`; it also allows arbitrary conditioning-generated affine terms in the untouched J-bank. It does **not** permit arbitrary quadratic self-curvature in the active J-bank simultaneously with the rank-one cross term. That overlapping two-sided-curvature regime remains a genuine gap.

## 7. A bona fide N3/no-pivot target class

Take `C` empty and the pure grouped quadratic form

\[
Q=2\gamma(a^TX_I)(b^TX_J)+\lambda(z^TX_D)^2.
\tag{7.1}
\]

On the orthonormal grouped span generated by

\[
e_I=a/\|a\|,
\quad e_J=b/\|b\|,
\quad e_D=z/\|z\|,
\]

the matrix is

\[
\begin{pmatrix}
0&\gamma\sigma_I\sigma_J&0\\
\gamma\sigma_I\sigma_J&0&0\\
0&0&\lambda\sigma_D^2
\end{pmatrix}.
\]

Its nonzero eigenvalues are exactly

\[
\{-\kappa,+\kappa,\lambda\sigma_D^2\}.
\tag{7.2}
\]

Therefore `kappa>=1` and `rho>=1` imply the exact target hypothesis of at least three eigenvalues of absolute value at least one, and Theorem 6.1 gives

\[
\boxed{
\|p_Q\|_\infty\le12,
\qquad p_Q\in C_0(\mathbb R).
}
\tag{7.3}
\]

This is not merely a fixed-coordinate localized case. Let `I,J,D` each have `m` coordinates, take

\[
a=b=z=m^{-1/2}(1,\ldots,1),
\qquad \gamma=\lambda=1.
\tag{7.4}
\]

Then the nonzero spectrum is exactly `{-1,1,1}` for every `m`, while

\[
\max_i|A_{ii}|=\frac1m,
\qquad
\max_{i<j}|\det A_{\{i,j\}}|=\frac1{m^2}.
\tag{7.5}
\]

Hence for every fixed N3 threshold `tau in (0,1]`, all diagonal pivots and all physical `2x2` determinants are below `tau` once `m` is sufficiently large, yet (7.3) remains uniform. This is exactly the kind of aggregate-before-coordinate-selection no-pivot family that a valid full proof must handle.

The executed deterministic checker in this run verifies `K_3=12`, the spectrum `{-1,1,1}` for `m=3,5,17,64`, the values in (7.5), and scaling homogeneity. It ends `STATUS=PASS`. These finite checks are diagnostics, not the analytic proof.

## 8. Designated partner application: exact averaged-frequency bound

Apply the completed account04/B01 identity (1.1) to Theorem 6.1. This is an actual equation-level application of the designated partner result, not a copied citation. From (6.5),

\[
\boxed{
\sup_{T>0,\,y\in\mathbb R}
D_T\operatorname{law}(Q)(y)
\le
12\,\kappa^{-2/3}\rho^{-1/3}.
}
\tag{8.1}
\]

For the normalized diffuse N3 family (7.4),

\[
\boxed{
\sup_{T>0,y}D_T\operatorname{law}(Q)(y)\le12.
}
\tag{8.2}
\]

This is the requested frequency-averaged replacement for the false scalar pointwise Fresnel estimate. It is phase-sensitive and does not require `int |hat mu(t)|dt<infinity`; in particular it does not contradict the live absolute-Wiener correction.

## 9. Relation to nearby completed work and the remaining implication

This theorem is distinct from account03/B09's physical rank-one hub-pair theorem. B09 pays a selected **physical 2x2 rank-one core** by completing a physical square and using a transverse random slope, with a scale involving the core eigenvalue and the null-direction coupling. The present result instead pays a **grouped rank-one cross bank** directly in its aggregate singular resource `kappa`, and uses a disjoint grouped square through conjugate `L^p-L^q` smoothing. It is especially useful when every fixed physical coefficient tends to zero but the grouped resources stay at target scale.

The full QFORM conjecture is nevertheless still OPEN. The new theorem pays the N3 subclass in which a target-scale rank-one cross bicore can be paired with a source-disjoint target-scale square after conditioning one side, without J-side self-curvature. The first unpaid structural/analytic implication for this route is:

**`QFORM-N3-RANK1-CROSS-PLUS-THIRD-DIRECTION-ROUTING-v1`.** Starting only from the N3 assumptions and three actual large eigenvalues, either expose a source-valid packet of the form (6.1) with dimension-free lower bounds on `kappa` and `rho`, or prove that failure routes to one of the already-paid rank-two/rank-three cross-volume, mixed-hub, grouped-square, ridge-window, pair-log, or null-coloop branches. If the third direction necessarily overlaps the J bank, extend (6.3) to simultaneous J-side curvature without inventing post-rotation independence.

No claim here proves that routing implication, and no fixed-good-minor assertion is smuggled into it.

## 10. Reproducibility and review status

Files in this immutable run folder:

- `EARLY_CHECKPOINT.md` — first substantive derivation;
- `CHECKS.py` — deterministic spectrum/constant/scaling checks;
- `CHECKS.txt` — actual executed output, ending `STATUS=PASS`;
- `REPORT.md` — this complete proof.

Independent end-to-end review of this new theorem has **not yet occurred**. It is a supporting theorem, not a full-solution candidate. Full QFORM still requires the global structural routing plus two independent reviews of any eventual complete proof.
