SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B10, 2026-09-22T18:22:36Z.
attacking: exact-rank-three heavy near-isotropic rows; replace bounded-depth peeling by two-row spectral-compression geometry and a product-preserving zero-pivot endpoint estimate.

# account01/B10 — rank-three coupled case, r15

**Programme:** QFORM-DENSITY-3EIG-20260922.  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full target `OPEN_NOT_PROVED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  

The current source corrections are enforced. In particular, this report does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, positive conditional projection moments, fiber-sup integration, or a bounded conditional density as a substitute for genuine product provenance.

## 1. Conditional end-to-end map and the first unpaid implication

Write an exact-rank-three target as

\[
A=U\Lambda U^T,\qquad U^TU=I_3,\qquad \sigma_{\min}(\Lambda)\ge1,
\]

with physical spectral rows \(u_i\in\mathbb R^3\). Existing completed supporting branches give a universal bound when the frame is diffuse, and a nonzero physical scalar pivot can be reduced to the orientation-free rank-two affine half-Riesz theorem. The designated partner account02/B10 further proved that a large-leverage row with small pivot still has strong total cross energy,

\[
\sigma_i^2:=\sum_{j\ne i}A_{ij}^2
=u_i^T\Lambda^2u_i-A_{ii}^2
\ge \|u_i\|^2-A_{ii}^2,
\tag{1.1}
\]

and exhibited arbitrarily long exact-zero-pivot heavy peeling chains on one isotropic spectral ray. Thus bounded-depth deletion is not a possible closure mechanism.

This run changes mechanism. It proves:

1. a dimension-free \(L^{3/2}\) endpoint and an explicit \(\varepsilon\log(1/\varepsilon)\) small-ball bound for **every heavy exact-zero physical pivot**, with arbitrary product-origin leakage;
2. a two-row spectral-compression lemma showing that **two macroscopic near-isotropic heavy rows cannot coexist as an unpaid state**: if both leverages are at least \(5/8\) and both normalized pivots are at most \(1/16\), their physical \(2\times2\) pair is uniformly indefinite and the completed pair-log theorem gives \(\|p_Q\|_\infty<72\).

Consequently the first remaining rank-three obstruction is narrower: one macroscopic light-cone row together with a genuinely multiscale bank of smaller residual rows. The missing endpoint upgrade is to remove the single logarithm while preserving the original product provenance.

## 2. Heavy exact-zero pivot: product-preserving \(L^p\) endpoint

### Theorem 2.1 — `QFORM-RANK3-HEAVY-ZEROPIVOT-L32-v1`

Assume an original physical row \(u_i\) has leverage

\[
c:=\|u_i\|^2\ge \frac12,
\]

and exact pivot

\[
A_{ii}=u_i^T\Lambda u_i=0.
\]

Then the law of \(Q=X^TAX\) is absolutely continuous and

\[
\boxed{\|p_Q\|_{3/2}\le2.}
\tag{2.1}
\]

More generally, for every \(1<p<2\),

\[
\boxed{
\|p_Q\|_p^p
\le
\frac{1}{2-p}
\left(\frac{\sqrt2}{r\sqrt c}\right)^{p-1}
\le
\frac{2^{p-1}}{2-p},
}
\tag{2.2}
\]

where \(r=\|\Lambda e\|\ge1\) and \(e=u_i/\sqrt c\).

#### Proof

Rotate only the three-dimensional spectral basis, never the physical independent coordinates. Put \(e_1=e=u_i/\sqrt c\). Since \(e^T\Lambda e=0\), the first row of \(\Lambda\) is transverse to \(e\). Rotate the transverse spectral plane so

\[
\Lambda=
\begin{pmatrix}
0&r&0\\
r&\alpha&\beta\\
0&\beta&\gamma
\end{pmatrix},
\qquad r=\|\Lambda e\|.
\tag{2.3}
\]

Because \(\sigma_{\min}(\Lambda)\ge1\),

\[
r=\|\Lambda e\|\ge1.
\tag{2.4}
\]

Equivalently, applying the account02/B10 identity (1.1) at the zero pivot gives \(\sigma_i^2\ge c\), while \(\sigma_i^2=c r^2\), again yielding \(r\ge1\). This is the required direct use of the designated partner result.

Let \(S,W,V\) be the three spectral linear forms corresponding to the basis in (2.3). The physical coordinate \(i\) occurs only in \(S\):

\[
S=\sqrt c\,X_i+T,
\]

where \(T,W,V\) are functions only of \(X_{-i}\). Therefore

\[
Q=2rSW+\alpha W^2+2\beta WV+\gamma V^2
=2r\sqrt c\,W X_i+C(X_{-i}).
\tag{2.5}
\]

Condition on the full residual sigma-field \(\mathcal F=\sigma(X_j:j\ne i)\). For \(W\ne0\), the conditional law is an affine image of the genuine independent variable \(X_i\). Hence, using \(0\le f_i\le1\) and \(\int f_i=1\),

\[
\|p_{Q\mid\mathcal F}\|_p^p
=(2r\sqrt c\,|W|)^{1-p}\int f_i(x)^p\,dx
\le(2r\sqrt c\,|W|)^{1-p}.
\tag{2.6}
\]

The coefficient vector defining \(W\) has Euclidean norm one and has zero \(i\)-th coordinate. Thus \(W\) is a normalized linear form in the remaining independent cap-one coordinates. The scalar Ball--Rogozin projection bound gives

\[
\|p_W\|_\infty\le H:=\sqrt2.
\tag{2.7}
\]

For \(0<\eta<1\), any probability density bounded by \(H\) obeys the elementary symmetric-decreasing rearrangement estimate

\[
\mathbb E|W|^{-\eta}
\le 2H\int_0^{1/(2H)}x^{-\eta}\,dx
=\frac{(2H)^\eta}{1-\eta}.
\tag{2.8}
\]

Set \(\eta=p-1\). Jensen for the conditional density mixture and (2.6)--(2.8) give

\[
\|p_Q\|_p^p
\le
(2r\sqrt c)^{1-p}
\frac{(2H)^{p-1}}{2-p}
=
\frac{1}{2-p}
\left(\frac{H}{r\sqrt c}\right)^{p-1}.
\tag{2.9}
\]

Using \(H=\sqrt2\), \(r\ge1\), \(c\ge1/2\) gives (2.2). At \(p=3/2\), the right side of (2.9) equals \(2\sqrt2\), and raising to the power \(2/3\) yields exactly \(2\). The event \(W=0\) has probability zero because \(W\) has a density, so the conditional densities above assemble to an unconditional density. QED.

### Corollary 2.2 — logarithmic small-ball endpoint

Under the hypotheses of Theorem 2.1, for every interval \(I\) of length \(\varepsilon\le1/2\),

\[
\boxed{
\Pr\{Q\in I\}
\le
2\varepsilon\left(1+\log\frac1{2\varepsilon}\right)
\le
2\varepsilon\left(1+\log\frac1\varepsilon\right).
}
\tag{2.10}
\]

Indeed, conditioning as above gives

\[
\Pr(Q\in I\mid\mathcal F)
\le
\min\left\{1,\frac{\varepsilon}{2r\sqrt c\,|W|}\right\}.
\tag{2.11}
\]

For a random variable with density at most \(H\), symmetric-decreasing rearrangement yields, with \(x=H\varepsilon/(r\sqrt c)\le2\varepsilon\le1\),

\[
\mathbb E\min\left\{1,\frac{\varepsilon}{2r\sqrt c\,|W|}\right\}
\le x(1+\log(1/x)).
\tag{2.12}
\]

Since \(x(1+\log(1/x))\) is increasing on \((0,1]\), (2.10) follows.

This is not the desired \(O(\varepsilon)\) endpoint, but it is dimension-free, requires no independence between the leakage \(T\) and \((W,V)\), and applies directly to the long exact-zero-pivot cascade of account02/B10. It shows that the cascade itself creates at most one logarithmic endpoint loss, rather than an iterated or dimension-growing singularity.

Continuity is **not** proved by Theorem 2.1; only absolute continuity and the stated \(L^p\) bounds are proved.

## 3. Two heavy near-isotropic rows force a uniformly good physical pair

The previous three B10 runs repeatedly encountered heavy near-isotropic rows, so this run switches from peeling to a two-row compression mechanism.

### Lemma 3.1 — two-vector compression rigidity

Let \(M=M^T\in\mathbb R^{3\times3}\) satisfy \(\sigma_{\min}(M)\ge s>0\). Let \(e,f\) be unit vectors with \(\kappa=|e\cdot f|<1\). Put

\[
a=e^TMe,\qquad d=f^TMf,\qquad b=e^TMf.
\]

Then

\[
\boxed{
|b|\ge s(1-\kappa)-\max\{|a|,|d|\}.
}
\tag{3.1}
\]

#### Proof

Let \(P=\operatorname{span}\{e,f\}\) and let \(O\) be a \(3\times2\) orthonormal basis for \(P\). Write

\[
MO=OH+nq^T,
\]

where \(n\) is a unit normal to \(P\), \(H=O^TMO\), and \(q\in\mathbb R^2\). Choose a unit \(x\in\ker q^T\). Then

\[
\|Hx\|=\|MOx\|\ge s,
\]

so \(\|H\|_{op}\ge s\).

Let \(E=[e\ f]\) and \(G=E^TE\). Since one may take \(O=EG^{-1/2}\),

\[
H=G^{-1/2}
\begin{pmatrix}a&b\\b&d\end{pmatrix}
G^{-1/2}.
\]

The least eigenvalue of \(G\) is \(1-\kappa\), hence

\[
s\le\|H\|_{op}
\le\frac{1}{1-\kappa}
\left\|\begin{pmatrix}a&b\\b&d\end{pmatrix}\right\|_{op}
\le\frac{|b|+\max(|a|,|d|)}{1-\kappa}.
\]

Rearrange. QED.

### Lemma 3.2 — Parseval rows cannot be too parallel

If \(u,v\) are two physical spectral rows of \(U\), with

\[
c=\|u\|^2,\qquad d_0=\|v\|^2,
\]

then

\[
\boxed{|u\cdot v|^2\le(1-c)(1-d_0).}
\tag{3.2}
\]

Proof: \(uu^T+vv^T\le\sum_k u_ku_k^T=I_3\). The two nonzero eigenvalues of \(uu^T+vv^T\) equal those of the Gram matrix \(\begin{psmallmatrix}c&u\cdot v\\u\cdot v&d_0\end{psmallmatrix}\). Thus \(I-G\succeq0\), whose determinant condition is (3.2). QED.

### Theorem 3.3 — `QFORM-RANK3-TWO-HEAVY-NEARNULL-PAIR-v1`

Suppose two distinct physical rows \(u_i,u_j\) satisfy

\[
\|u_i\|^2,\|u_j\|^2\ge\frac58,
\tag{3.3}
\]

and normalized pivots

\[
\frac{|A_{ii}|}{\|u_i\|^2},\quad
\frac{|A_{jj}|}{\|u_j\|^2}
\le\frac1{16}.
\tag{3.4}
\]

Then their physical principal pair

\[
B=\begin{pmatrix}A_{ii}&A_{ij}\\A_{ij}&A_{jj}\end{pmatrix}
\]

is uniformly indefinite and obeys

\[
|A_{ij}|\ge\frac3{16},\qquad
\sigma_{\min}(B)\ge\frac18,
\qquad
|\det B|\ge\frac1{32}.
\tag{3.5}
\]

Consequently, applying the completed pair-log theorem at spectral scale \(s=1\),

\[
\boxed{
\|p_Q\|_\infty
\le
8\sqrt5\,(|\det B|\,\sigma_{\min}(B))^{-1/4}
\le32\sqrt5<71.56.
}
\tag{3.6}
\]

The pair-log theorem is currently a complete supplied supporting proof with independent review pending; accordingly (3.6) inherits that review status rather than being promoted to a fully independently certified theorem.

#### Proof of the exact structural inequalities

Normalize

\[
e=\frac{u_i}{\sqrt c},\qquad f=\frac{u_j}{\sqrt{d_0}},
\]

where \(c,d_0\ge5/8\). Lemma 3.2 gives

\[
|e\cdot f|
\le
\sqrt{\frac{(1-c)(1-d_0)}{cd_0}}.
\]

Apply Lemma 3.1 with \(M=\Lambda\), \(s=1\), and normalized diagonal errors at most \(1/16\). Multiplying by \(\sqrt{cd_0}\),

\[
|A_{ij}|
\ge
\sqrt{cd_0}
-\sqrt{(1-c)(1-d_0)}
-\frac1{16}\sqrt{cd_0}.
\]

Since \(\sqrt{cd_0}\ge5/8\), \(\sqrt{(1-c)(1-d_0)}\le3/8\), and \(\sqrt{cd_0}\le1\),

\[
|A_{ij}|\ge\frac58-\frac38-\frac1{16}=\frac3{16}.
\]

Also \(|A_{ii}|,|A_{jj}|\le1/16\). Decomposing \(B\) into its off-diagonal part plus a diagonal perturbation gives

\[
\sigma_{\min}(B)\ge |A_{ij}|-\frac1{16}\ge\frac18.
\]

Finally

\[
|\det B|
=|A_{ij}^2-A_{ii}A_{jj}|
\ge\frac9{256}-\frac1{256}
=\frac1{32}.
\]

The determinant is negative, so the pair is indefinite. Substitute these two bounds into the pair-log estimate to obtain (3.6). QED.

## 4. What the partner cascade now means

The named account02/B10 r13 construction gives arbitrarily long heavy whitening steps on one isotropic ray; at each successive stage the *whitened* leverage can stay \(2/3\), although the original physical row weights shrink geometrically. Theorem 3.3 explains why such shrinking is necessary in an unpaid state: two distinct top-level original rows cannot both carry leverage at least \(5/8\) while remaining near the light cone. If they did, their cross interaction would itself furnish a uniformly conditioned indefinite physical pair and the pair-log theorem would close the branch.

Thus the long cascade is not evidence for multiple unresolved macroscopic null directions. It is a **multiscale fragmentation phenomenon**: at most one original row can remain macroscopically heavy near the light cone, and the rest of the cascade must live in smaller original-coordinate rows even if whitening repeatedly makes them heavy.

Together with Theorem 2.1, this leaves a more precise endpoint problem:

`QFORM-ONE-MACRO-NULLROW-MULTISCALE-BANK-ENDPOINT-v1`.

Starting from one heavy exact/near-null row, use the orthogonal transverse coefficient bank and the Parseval constraints to improve the universal

\[
\Pr(Q\in I)\lesssim |I|\log(1/|I|)
\]

from Theorem 2.1 to \(O(|I|)\), before whitening/local inversion loses the original product structure. Equivalently, one must exploit transverse quadratic curvature jointly with the product-linear bank to pay the logarithmic \(1/|W|\) singularity. A bounded conditional density alone cannot do this, by the account02/B10 r11 counterexample.

## 5. Conditional end-to-end argument after this run

For the exact-rank-three assignment, a compact current route is now:

- diffuse frame: use the completed diffuse branch;
- nonzero outer pivot: use the orientation-free rank-two affine half-Riesz Schur theorem;
- two macroscopic near-null heavy rows: Theorem 3.3 plus pair-log gives \(<72\);
- one exact macroscopic null row: Theorem 2.1 gives \(L^{3/2}\le2\) and the dimension-free one-log small-ball bound;
- remaining case: one macro light-cone row plus a multiscale smaller-row bank. Prove the endpoint upgrade above, or construct a genuine independent-product counterexample.

No claim here closes the arbitrary rank-three orientation or the full higher-rank owner target.

## 6. Sources actually consumed

1. **Designated OTHER-account partner, account02/B10 r12:** `yspennstate/math-open-problems@f767f80b1bd5750d5485e534b10e14dc5f46c0e2`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T151650Z-account02-B10-QFORM-r12/REPORT.md`. Applied to (1.1) and the quantitative zero-pivot transverse bound \(r\ge1\).
2. **account02/B10 r13:** `yspennstate/math-open-problems@9a34dc516006d7eb417687b3d7d409f7dfaf33d9`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T154900Z-account02-B10-QFORM-r13/REPORT.md`. Its arbitrary-length isotropic cascade is used as the mandatory structural test that rules out bounded-depth peeling.
3. **Rank-two affine half-Riesz synthesis:** `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
4. **Pair-log replacement theorem:** `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`; complete supplied analytic proof, independent review pending.
5. **Current correction bundle:** `yspennstate/math-open-problems@f305dcc8ae0f602f2b21ab32cf4d8ddcdcb56b92`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/CORRECTIONS.md`; in particular the arbitrary-joint coarea and positive conditional-moment gates are not used.

## 7. Status

- `QFORM-RANK3-HEAVY-ZEROPIVOT-L32-v1`: **PROVED SUPPORTING THEOREM** (absolute continuity; \(L^{3/2}\le2\); no continuity claim).
- one-log zero-pivot small-ball estimate: **PROVED SUPPORTING THEOREM**.
- `QFORM-RANK3-TWO-HEAVY-NEARNULL-PAIR-v1` structural inequalities: **PROVED**; the resulting \(L^\infty<72\) branch is conditional on the current supplied pair-log theorem's pending independent review status.
- arbitrary exact-rank-three orientation: **OPEN**.
- full three-large-eigenvalue target with arbitrary additional spectrum: **OPEN**.

No Gaussianity, moments, compactness, log-concavity, diagonal-basis independence, finite fragment count, or continuity of input laws is assumed.
