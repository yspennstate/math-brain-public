SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T07:56:25Z.
attacking: `QFORM-HUBSINGULAR-DIFFUSE-BILINEAR-CURVED-RECEIVER-v1` by keeping a literal indefinite physical pair, averaging its logarithmic hyperbola singularity first against the remaining physical hub coordinate and then against the diffuse original-product tail slope.

# account03/B06 r54 — the diffuse singular-hub bilinear endpoint is density-paid

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.  
Immediate B06 input: `QFORM-HUBSINGULAR-FOURMINOR-BANK-v1`, `yspennstate/math-open-problems@5659cc902d288c63efcd6774ca8c9510d10c8a42`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T071843Z-account03-B06-qform-r53/REPORT.md`.  
Analytic input: `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1`, `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.  
Designated partner actually applied below: account04/B06 `QFORM-FRESH-TRANSVERSE-CURVED-SECTION-v1`, `yspennstate/math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`.  
Execution label: `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport is not native learned-memory ingestion.

The full QFORM conjecture remains OPEN. This run closes the exact rank-two singular three-hub face whenever its hub-null direction is genuinely coupled to the tail (`omega != 0`). It does not close the near-singular transition, the exact `omega=0` global-null branch, `rank F<=1`, or the global compiler.

## 1. Compact conditional end-to-end argument

The r53 exact localized packet is

\[
A=[I_3\ Z]^T B_0[I_3\ Z]
 +\operatorname{diag}(D_H,\Delta),
\qquad F:=B_0+D_H,
\]

with

\[
\det F=0,\qquad \operatorname{rank}F=2.
\]

Let `v` be a unit null vector of `F`, let

\[
\kappa_F:=|\operatorname{pdet}_*(F)|>0,
\qquad
\omega:=Z^TD_Hv.
\]

The r53 bank identity shows that `omega=0` is exactly the case in which `(v,0)` is a global null vector of the full matrix. Assume in this run that `omega != 0`.

If one normalized tail coefficient has squared size at least `1/64`, r53 already pays the full scalar output by a literal physical four-coordinate determinant. Thus the first essential missing implication is the diffuse alternative

\[
\max_j\frac{\omega_j^2}{\|\omega\|_2^2}<\frac1{64}.
\tag{1.1}
\]

Put

\[
W=\frac{\omega\cdot X_{\rm tail}}{\|\omega\|_2}.
\]

The completed product Fourier/Brascamp--Lieb calculation used in r53 gives a continuous `C_0` density with

\[
\|p_W\|_\infty\le2.
\tag{1.2}
\]

The point of this run is to use (1.2) **without** conditioning on `W`, without taking `E|W|^{-1}`, and without replacing a curved fiber by its supremum.

When the two nonzero eigenvalues of `F` have the same sign, Section 6 below gives an immediate definite-pair payment. The hard case is therefore the rank-two **indefinite** hub. Choose an index `i` with

\[
|v_i|=\max_k|v_k|\ge\frac1{\sqrt3}.
\tag{1.3}
\]

Let `P` be the complementary literal physical `2 x 2` principal block of `F`. Then `P` is invertible indefinite and

\[
D:=|\det P|=\kappa_Fv_i^2\ge\frac{\kappa_F}{3}.
\tag{1.4}
\]

Write

\[
\kappa:=\sigma_{\min}(P)>0.
\tag{1.5}
\]

Conditioning on all tail ORIGINAL coordinates turns the three-hub polynomial into a rank-two hub quadratic plus an affine term. Completing the literal pair `P` leaves **no quadratic term** in the remaining physical hub coordinate `X_i`; the remaining slope is

\[
\Gamma(X_{\rm tail})
=
\frac{\beta_0-2\|\omega\|_2W}{v_i},
\tag{1.6}
\]

where `beta_0` contains arbitrary ambient affine terms. Hence (1.2) implies that `Gamma` itself has a density satisfying

\[
\boxed{
\|p_\Gamma\|_\infty
\le \frac{|v_i|}{\|\omega\|_2}.
}
\tag{1.7}
\]

The physical pair-log envelope, averaged first in `X_i` and then in `Gamma`, gives the full scalar estimate

\[
\boxed{
\|p_Q\|_\infty
\le
8\sqrt{\frac{|v_i|}{\kappa\,\|\omega\|_2}}
+\frac2{\sqrt D}.
}
\tag{1.8}
\]

All same-bank tail quadratic curvature is retained inside an arbitrary translation during the averaging. There is no reciprocal tail slope and no fiber maximum.

Using only

\[
\kappa\ge\frac{D}{\|F\|_{\rm op}}
\ge\frac{\kappa_F}{3\|F\|_{\rm op}},
\]

(1.8) has the coordinate-free corollary

\[
\boxed{
\|p_Q\|_\infty
\le
8\sqrt{\frac{3\|F\|_{\rm op}}
{\kappa_F\|\omega\|_2}}
+2\sqrt{\frac3{\kappa_F}}.
}
\tag{1.9}
\]

This is an essential-supremum conclusion. Continuity is not claimed from this proof.

## 2. Exact physical-pair algebra

Reorder the three hub coordinates so the chosen index `i` is last and write

\[
F=
\begin{pmatrix}
P&r\\ r^T&a
\end{pmatrix},
\qquad
v=\binom{v'}{v_i}.
\tag{2.1}
\]

Since a symmetric rank-two matrix with null vector `v` satisfies

\[
\operatorname{adj}(F)=\operatorname{pdet}_*(F)vv^T,
\]

the complementary principal minor gives

\[
\det P=\operatorname{pdet}_*(F)v_i^2.
\tag{2.2}
\]

In the indefinite case `operatorname{pdet}_*(F)<0`, so `P` is an indefinite invertible physical pair and (1.4) follows.

The null equations are

\[
Pv'+rv_i=0,
\qquad
r^Tv'+av_i=0.
\]

Because `v_i !=0`,

\[
v'=-P^{-1}rv_i,
\qquad
\boxed{a-r^TP^{-1}r=0.}
\tag{2.3}
\]

Now allow an arbitrary affine hub vector `b=(c,d)`. Completing the literal physical pair gives

\[
U^TPU+2x\,r^TU+c^TU+ax^2+dx
=
\left(U+P^{-1}(rx+c/2)\right)^TP
\left(U+P^{-1}(rx+c/2)\right)
+\gamma x+C,
\tag{2.4}
\]

where the `x^2` term vanishes by (2.3) and

\[
\gamma=d-c^TP^{-1}r.
\tag{2.5}
\]

Taking the scalar product of `b` with the null vector and using `v'=-P^{-1}rv_i` gives the exact slope identity

\[
\boxed{
\gamma=\frac{v^Tb}{v_i}.
}
\tag{2.6}
\]

For the ambient localized packet, conditional on a tail value `y`,

\[
b(y)=b_0+2B_0Zy.
\]

Since `(B_0+D_H)v=0`,

\[
v^TB_0Z=-(D_Hv)^TZ=-\omega^T.
\]

Therefore (2.6) is exactly (1.6). Notice that the rest of the tail polynomial, including every diagonal coefficient and every same-bank quadratic term created by completing the pair, is merely part of the translation `R_0(y)` below. It is never discarded.

## 3. First weighted replacement: integrate the pair logarithm against one physical hub

The completed pair-log theorem states that an affine perturbation of the fixed indefinite physical pair `P` has density envelope, for every cutoff `s>0`,

\[
p_{\rm pair}(t)
\le
\frac{2\sqrt2}{s}
+D^{-1/2}
\log_+\!\left(
\frac{2s^2}{\kappa|t-t_0|}
\right).
\tag{3.1}
\]

After (2.4), for fixed tail `y` the moving critical value is

\[
t_0=R_0(y)+\Gamma(y)X_i.
\tag{3.2}
\]

The original coordinate `X_i` is independent of the literal physical pair and has density cap one. We use the following elementary layer-cake estimate.

### Lemma 3.1

If `X` has density at most one, `gamma !=0`, and `A>0`, then uniformly in `u`,

\[
\mathbb E\log_+\frac{A}{|u-\gamma X|}
\le \Psi\!\left(\frac{2A}{|\gamma|}\right),
\tag{3.3}
\]

where

\[
\Psi(q)=
\begin{cases}
q,&0\le q\le1,\\
1+\log q,&q>1.
\end{cases}
\tag{3.4}
\]

Indeed the density of `gamma X` is at most `|gamma|^{-1}`, and

\[
\mathbb E\log_+\frac{A}{|u-\gamma X|}
=
\int_0^\infty
\Pr\{|u-\gamma X|<Ae^{-z}\}\,dz
\]

is at most

\[
\int_0^\infty
\min\left\{1,\frac{2Ae^{-z}}{|\gamma|}\right\}dz,
\]

which is exactly (3.3).

Applying Lemma 3.1 to (3.1) with `A=2s^2/kappa` gives, conditional only on the tail,

\[
p_{Q\mid X_{\rm tail}=y}(t)
\le
\frac{2\sqrt2}{s}
+D^{-1/2}\Psi\!\left(
\frac{4s^2}{\kappa|\Gamma(y)|}
\right).
\tag{3.5}
\]

The arbitrary function `R_0(y)` has disappeared from the upper bound by translation-uniformity. This is the first place where the curved pair is averaged rather than maximized.

## 4. Second weighted replacement: average the moving slope with the product law

Let a random variable `G` have a density bounded by `K`. For fixed `C>0`, the function

\[
g(u)=\Psi(C/|u|)
\]

is even and decreasing in `|u|`. Layer cake (equivalently the one-dimensional bathtub principle) therefore shows that among all probability densities bounded by `K`, its expectation is maximized by density `K` on the centered interval of length `1/K`.

In particular, if

\[
C=\frac1{2K},
\tag{4.1}
\]

then

\[
\mathbb E\Psi(C/|G|)
\le
2K\int_0^{1/(2K)}
\left[1+\log\frac{1/(2K)}u\right]du
=2.
\tag{4.2}
\]

For the actual `Gamma` in (1.6), (1.7) permits

\[
K=\frac{|v_i|}{\|\omega\|_2}.
\]

Choose the pair cutoff by

\[
\boxed{
s^2=
\frac{\kappa\|\omega\|_2}{8|v_i|}.
}
\tag{4.3}
\]

Then

\[
\frac{4s^2}{\kappa}=\frac1{2K},
\]

so (3.5), (4.2), and Tonelli yield

\[
p_Q(t)
\le
\frac{2\sqrt2}{s}+rac2{\sqrt D}
=
8\sqrt{\frac{|v_i|}{\kappa\|\omega\|_2}}
+\frac2{\sqrt D}
\]

for almost every `t`. This proves (1.8).

Two dependencies that would be dangerous are deliberately **not** asserted. We never condition on `W` and claim the remaining coordinates are independent, and we never use a worst conditional density of one projected variable. We condition only on actual ORIGINAL coordinates while applying the pair envelope, integrate the remaining physical hub with its original cap-one density, and only then use the marginal cap (1.7). Thus the recorded conditional-cap and arbitrary-joint-coarea corrections are respected.

## 5. `QFORM-HUBSINGULAR-DIFFUSE-PAIRLOG-COMPILER-v1`

Combining Sections 1--4 gives the new supporting theorem.

### Theorem 5.1

In the r53 exact localized packet, assume

\[
\operatorname{rank}F=2,
\quad \det F=0,
\quad \omega=Z^TD_Hv\ne0,
\]

and the two nonzero eigenvalues of `F` have opposite signs. If the normalized bank is diffuse as in (1.1), choose `i` satisfying (1.3), let `P=F_{i^c,i^c}`, `D=|det P|`, and `kappa=sigma_min(P)`. Then the **full ambient scalar quadratic form**, including arbitrary same-bank tail quadratic curvature and arbitrary affine terms, has an essentially bounded density satisfying (1.8), hence (1.9).

No moment, support, connectedness, log-concavity, Gaussianity, or rotated-coordinate independence assumption is used.

The proof establishes absolute continuity and essential boundedness. It does not establish continuity.

## 6. The same-sign rank-two singular hub is easier

If the two nonzero eigenvalues of `F` have the same sign, keep the same `i`. Equation (2.2) now has positive determinant, so `P` is a definite physical pair with

\[
D=\kappa_Fv_i^2\ge\kappa_F/3.
\]

Condition on every original coordinate outside that literal pair. The complete ellipse integral for a definite physical pair gives, uniformly over all affine shifts and all conditioned translations,

\[
\|p_Q\|_\infty\le\frac\pi{\sqrt D}
\le
\boxed{\pi\sqrt{\frac3{\kappa_F}}}.
\tag{6.1}
\]

So no tail-null coupling is needed in the same-sign rank-two face.

## 7. The exact rank-two singular `omega !=0` face is now exhausted

For an indefinite rank-two singular hub with `omega !=0`, exactly one of the following holds:

1. **heavy bank:** some `omega_j^2 >= ||omega||^2/64`; r53 gives
   \[
   \|p_Q\|_\infty
   <263.043723\,[\kappa_F\|\omega\|_2^2]^{-1/4};
   \tag{7.1}
   \]
2. **diffuse bank:** every normalized square is `<1/64`; Theorem 5.1 gives (1.8).

If the rank-two hub is same-sign, (6.1) pays it regardless of `omega`.

Therefore the exact singular rank-two three-hub face is no longer blocked by the diffuse bilinear endpoint whenever `omega !=0`. The only exact rank-two singular survivor is

\[
\boxed{\omega=0,}
\]

which r53 identifies exactly with `(v,0)` being a genuine global null vector of the full matrix. That branch must be compiled from the remaining large spectrum rather than by trying to regularize a nonexistent null-direction coupling.

This is a stricter reduction than the previous `64/65` tangential collar: the positive-coupling singular face is fully paid without any normal-floor assumption.

## 8. Actual designated-partner application

The freshest completed designated partner result on the source-pinned tree is account04/B06 `QFORM-FRESH-TRANSVERSE-CURVED-SECTION-v1` at `math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`.

Apply it to the actual post-pair tail remainder whenever a physical tail partition `S sqcup R` exposes

\[
L=\langle w,X_S\rangle,
\qquad
V=\langle u,X_S\rangle,
\qquad
w\perp u,
\qquad
w_k^2+u_k^2\le\frac12,
\]

and the transverse statistic `B_R` is determined by the disjoint bank `X_R`. For a curved remainder component

\[
\lambda_*(V-v_0)^2+\beta B_R+c,
\]

the partner theorem gives on the actual off-fold event `|V-v_0|>r`

\[
\boxed{
\|g_r\|_\infty
\le\frac4{|\lambda_*|r}.
}
\tag{8.1}
\]

At the programme's standard scale `r=1/64`,

\[
\boxed{
\|g_{1/64}\|_\infty
\le\frac{256}{|\lambda_*|},
}
\tag{8.2}
\]

uniformly in the transverse coefficient `beta`, including `beta=0`. This is an actual inequality on the current same-bank tail remainder whenever its transverse resource is source-separated by the stated physical partition. I do not promote (8.2) to a shared-bank statement; the main diffuse singular-hub payment is instead Theorem 5.1.

## 9. Sanity checks

The committed `check_r54.py` tests the exact algebra in Section 2 on 10,000 fixed-seed random symmetric rank-two indefinite hub matrices. The maximum normalized discrepancies were

- `2.2899950095657363e-15` for `|det P|=kappa_F v_i^2`;
- `9.225415354448772e-16` for the zero Schur complement;
- `5.5271421607602644e-15` for `gamma=(v^T b)/v_i`.

These calculations are diagnostics only. The density estimates are the exact layer-cake arguments in Sections 3--4.

## 10. Status and next debt

**New proved claim:** `QFORM-HUBSINGULAR-DIFFUSE-PAIRLOG-COMPILER-v1`.  
**Combined with r53:** the exact rank-two singular three-hub face with `omega !=0` is density-paid for both signatures.  
**Continuity:** not proved by the new scalar receiver; partner branch (8.1) is continuous `C_0` in its two-output scope.  
**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.

The next B06 debt is

`QFORM-HUBSINGULAR-GLOBALNULL-OR-NEARSINGULAR-TRANSITION-v1`:

> if `omega=0`, use the exact global-null certificate `(v,0) in ker A` to route the remaining three-large-eigenvalue resource into a different physical/product bank; in parallel, make the r53/r54 compiler stable for small nonzero `det F` so the proof does not lose a reciprocal hub determinant while passing from an invertible localized hub to the exact singular face.

The separately listed `rank F<=1`, zero physical pivot, and low-rank `Z` endpoints remain explicit. The newest correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` is respected: no absolute mixed norm `int |t|^{-1/2}||G_t||_2 dt` is used. The entire mechanism here is original-coordinate pair logarithm plus two successive probability-weighted averages.
