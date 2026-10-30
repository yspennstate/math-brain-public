# fleet02/B15 — regularity ledger, principal-triple theorem, and delocalized obstruction

**Run:** `20260922T110507Z-fleet02-B15-qform-pivot-r1`  
**Assignment:** `Absolute continuity and regularity`  
**Classification:** `TARGET-SUPPORTING-THEOREMS / REGULARITY-SEPARATION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full conjecture:** **OPEN / NOT PROVED**.

## 0. Control pivot and consumed source

This invocation began under an older FEI order. Fresh protected-control rereads exposed first the owner-wide quadratic-form switch and then its implementation as revision `2026-09-22.5`; all FEI work stopped after that later order was observed. Earlier FEI artifacts from this invocation remain immutable historical work and are not promoted as the live result.

The live target is: for independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has an essentially bounded density with one universal bound. A continuous representative is a **strictly stronger regularity request** and is tracked separately.

The completed fleet source consumed is

`yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec:qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`.

It proves that the proposed law-uniform pointwise Fresnel decay is false, and proves `||p_Q||_infinity<=pi` for forms diagonal in the original independent coordinates. I use that diagonal theorem below to prove the stronger **continuous-density** conclusion on the diagonal branch, then prove a new arbitrary-sign `3x3` principal-block small-ball theorem.

## 1. Regularity upgrade on the complete diagonal branch

### Theorem 1.1 — `QFORM-DIAGONAL-CONTINUOUS-PI-v1`

Under the full target input hypotheses, suppose additionally that

\[
Q(X)=\sum_{j=1}^n\lambda_jX_j^2
\]

is diagonal in the original independent coordinates and at least three `|lambda_j|>=1`. Then `Q(X)` admits a bounded **uniformly continuous** density and

\[
\boxed{\|p_Q\|_\infty\le\pi.}
\tag{1.1}
\]

#### Proof

Among three large real coefficients, two have the same sign. Relabel them `lambda_1,lambda_2`. The completed fleet03/B17 beta-integral theorem gives a density `p_12` for

\[
Y=\lambda_1X_1^2+\lambda_2X_2^2
\]

with

\[
\|p_{12}\|_\infty\le {\pi\over\sqrt{|\lambda_1\lambda_2|}}\le\pi.
\tag{1.2}
\]

The third large term `Z=lambda_3X_3^2` is absolutely continuous: because `X_3` is absolutely continuous, it has no atom at zero, and the usual two-branch change of variables gives an `L^1` density `g_3` of total mass one. Thus `Y+Z` has density

\[
p_{123}=p_{12}*g_3.
\]

For every translation `h`,

\[
\begin{aligned}
\|\tau_h p_{123}-p_{123}\|_\infty
&=\|p_{12}*(\tau_hg_3-g_3)\|_\infty\\
&\le\|p_{12}\|_\infty\,\|\tau_hg_3-g_3\|_1
\longrightarrow0,
\end{aligned}
\tag{1.3}
\]

by translation continuity in `L^1`. Hence `p_123` has a uniformly continuous representative, and its sup norm is at most `pi`.

All remaining coordinates contribute an independent random variable `W`. If `mu_W` is its probability law, then

\[
p_Q=p_{123}*\mu_W.
\]

Convolution with a probability measure does not increase the sup norm, and

\[
\|\tau_hp_Q-p_Q\|_\infty
\le\|\tau_hp_{123}-p_{123}\|_\infty\to0.
\]

Therefore (1.1) and uniform continuity both persist. `QED`.

**Regularity lesson.** On this complete source-valid branch, the owner's stronger continuity request is not an extra hypothesis: it follows after the bounded same-sign two-term smoothing is convolved with the third absolutely continuous square term. This argument does **not** automatically transfer to a rotated form because the spectral terms cease to be independent.

## 2. Three original coordinates: bounded density for every nonsingular signature

Let `B` be real symmetric `3x3` and

\[
\kappa=\sigma_{\min}(B)=\min_j|\lambda_j(B)|.
\]

### Theorem 2.1 — `QFORM-3VAR-AFFINE-PRINCIPAL-v1`

Let `Y_1,Y_2,Y_3` be independent real variables with densities bounded by `1`. If `kappa>0`, then for every `b in R^3`, `c in R`,

\[
Z=Y^TBY+2b^TY+c
\]

has an essentially bounded density satisfying

\[
\boxed{
\|p_Z\|_\infty\le {C_3\over\kappa},
\qquad C_3:=2\pi+3\sqrt3<11.48.
}
\tag{2.1}
\]

No sign condition is imposed on the eigenvalues.

### Proof

Complete the square and translate the three independent coordinates:

\[
Y^TBY+2b^TY+c
=(Y+B^{-1}b)^TB(Y+B^{-1}b)+c-b^TB^{-1}b.
\]

Translation preserves independence and the density bounds. Scaling reduces to `kappa=1`. Put `F(y)=prod_i f_i(y_i)`, so `0<=F<=1`, `int F=1`. We prove for every interval `J` of length `eta` that

\[
\Pr(Y^TBY\in J)\le (2\pi+3\sqrt3)\eta.
\tag{2.2}
\]

Split into `N={|By|<=1}` and its complement.

### Near region

Write `B=S|B|`, with `S=sign(B)` symmetric orthogonal, and set `z=|B|^{1/2}y`. Then

\[
y^TBy=z^TSz,
\quad
dy=(\det|B|)^{-1/2}dz\le dz,
\]

and

\[
|By|^2=z^T|B|z\ge|z|^2.
\]

Hence `N` maps inside the Euclidean unit ball, and because `F<=1`, its contribution is no larger than

\[
|\{z:|z|\le1,\ z^TSz\in J\}|.
\]

For definite `S`, writing `t=|z|^2` gives volume density `2 pi sqrt(t)<=2pi` on `[0,1]`. For signature `(2,1)` or `(1,2)`, write `z^TSz=r^2-s^2`; for each fixed `s`, planar area is `pi d(r^2)`, so an output interval of length `eta` cuts at most `pi eta`, and integration over `s in[-1,1]` gives at most `2pi eta`. Thus

\[
\Pr(N,\ Y^TBY\in J)\le2\pi\eta.
\tag{2.3}
\]

### Far region

If `|By|>1`, some original coordinate satisfies `|(By)_i|>1/sqrt3`. For each `i` let

\[
E_i=\{Y^TBY\in J,\ |(By)_i|>1/\sqrt3\}.
\]

Condition on the other two **original independent coordinates**. As a function `g(t)` of `t=y_i`, `g` is quadratic and

\[
g'(t)=2(By)_i.
\]

On the part of the line in `E_i`, `|g'|>2/sqrt3`. Since an affine derivative has at most two monotone branches after excluding its central interval, each branch contributes at most `eta/(2/sqrt3)=sqrt3 eta/2` of `t`-length. The one-coordinate density is at most `1`, hence

\[
\Pr(E_i\mid Y_{\widehat i})\le\sqrt3\eta.
\]

Summing the three coordinates yields

\[
\Pr(N^c,\ Y^TBY\in J)\le3\sqrt3\eta.
\tag{2.4}
\]

Equations (2.3) and (2.4) prove (2.2). The interval domination implies that the pushforward measure is dominated by `C_3` times Lebesgue measure, hence by Radon-Nikodym it has a density with essential supremum at most `C_3`. Scaling restores `1/kappa`. `QED`.

**Continuity status:** The proof establishes absolute continuity and the `L^infinity` bound. It does **not** establish a continuous representative for arbitrary rotated `B` with merely measurable input densities. That stronger statement remains separate.

## 3. High-dimensional principal-triple conditioning

### Theorem 3.1 — `QFORM-PRINCIPAL-TRIPLE-CONDITIONING-v1`

Let `A` be any real symmetric `n x n` matrix. If some principal coordinate block `B=A_{I,I}`, `|I|=3`, satisfies

\[
\sigma_{\min}(B)\ge\kappa>0,
\]

then under the target input laws

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {2\pi+3\sqrt3\over\kappa}.
}
\tag{3.1}
\]

#### Proof

Condition on all variables outside `I`. The conditional polynomial in the three remaining original coordinates is

\[
x_I^TBx_I+2b(w)^Tx_I+c(w).
\]

Those three coordinates remain independent with unchanged densities bounded by `1`. Theorem 2.1 is uniform in `b,c`, so every conditional output law is dominated by `(C_3/kappa) Leb`. Averaging the conditional laws proves the same domination for the unconditional output. `QED`.

Thus arbitrary couplings to all conditioned coordinates are allowed; diagonalization of `A` is never used.

A related two-coordinate statement is also useful: if a `2x2` principal block `C` is positive or negative definite, the same conditioning/completing-square argument and the beta integral give

\[
\boxed{\|p_{X^TAX}\|_\infty\le\pi/\sqrt{\det C}.}
\tag{3.2}
\]

This includes arbitrary cross-couplings to the conditioned variables.

## 4. Fixed coordinate conditioning is not enough: a flat rank-three projector

### Proposition 4.1 — `QFORM-FLAT-RANK3-PRINCIPAL-TRIPLE-OBSTRUCTION-v1`

For infinitely many `n` there is a real symmetric `A` with exactly three nonzero eigenvalues, all equal to `1`, such that every principal coordinate triple obeys

\[
\boxed{\sigma_{\min}(A_{I,I})\le3/n.}
\tag{4.1}
\]

Yet the total determinant mass satisfies

\[
\boxed{\sum_{|I|=3}\det(A_{I,I})=1.}
\tag{4.2}
\]

#### Proof

For a Sylvester order `n=2^m`, take three normalized real Hadamard columns and assemble them as an `n x 3` matrix `U`. Its columns are orthonormal and every row `u_i` has squared norm `3/n`. Set `A=UU^T`. Then `A` is a rank-three orthogonal projection, so its three nonzero eigenvalues equal `1`.

For each coordinate triple `I`,

\[
A_{I,I}=U_IU_I^T\succeq0,
\qquad
\operatorname{tr}(A_{I,I})=\sum_{i\in I}|u_i|^2=9/n.
\]

The least of its three nonnegative eigenvalues is at most one third of the trace, proving (4.1). Cauchy-Binet gives

\[
\sum_{|I|=3}\det(A_{I,I})
=
\sum_{|I|=3}\det(U_I)^2
=
det(U^TU)=1,
\]

which is (4.2). `QED`.

So the owner spectral assumption does not permit selecting one uniformly good original-coordinate triple. The first genuinely delocalized test case is already

\[
Q(X)=|U^TX|^2
\]

for a flat three-frame `U`.

## 5. Exact remaining bridge

The live target remains open. The new local theorem says that **if curvature is localized on one coordinate triple, the conjecture is done with an explicit constant**. Proposition 4.1 proves why this cannot be the universal mechanism: in a valid rank-three example every fixed triple has curvature scale `O(1/n)`, while the aggregate Cauchy-Binet resource remains exactly one.

The next target-level implication is therefore an aggregate-minor/coarea estimate: convert

\[
\sum_{|I|=3}\det(U_I)^2=1
\]

(or its appropriate signed/singular-value analogue) into

\[
\Pr(X^TAX\in J)\le C|J|
\]

without first choosing a single triple. A multilinear coarea, Brascamp-Lieb, or determinant-weighted averaging argument must keep the original product structure throughout. The known dimension-free bounds for low-dimensional marginals of product measures are relevant but not sufficient alone, because an arbitrary bounded three-dimensional density can place mass in a thin spherical shell.

On regularity: interval domination is enough for absolute continuity and an essentially bounded density; it is **not** by itself a continuity theorem. Continuity is proved above for the full diagonal branch using a third independent absolutely continuous term. For the general rotated target, continuity remains a separate unpaid implication even if the central `L^infinity` conjecture is eventually established by small-ball methods.

## 6. Immutable source pins

* Consumed completed fleet source: `yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec:qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`.
* Earlier noncanonical write from the mid-control transition is preserved at `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`; this canonical report supersedes its location and adds the assignment-specific continuity ledger.

No novelty or publication-priority claim is made. Full arbitrary-eigenvector bounded density remains OPEN.
