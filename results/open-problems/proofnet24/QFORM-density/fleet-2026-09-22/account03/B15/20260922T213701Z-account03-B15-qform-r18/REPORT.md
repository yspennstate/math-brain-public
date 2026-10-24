# QFORM B15 — single-scale homogeneous height normal form

**Run:** `20260922T213701Z-account03-B15-qform-r18`  
**Account/slot:** account03/B15  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_TARGET_REDUCTION`  
**Full universal QFORM bound:** OPEN  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T21:37:01Z.

attacking: single-scale homogeneous reduction of the universal density height via the completed Gaussian heat-height theorem.

## 1. Exact target and notation

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_i<=1`. Let `A=A^T` be real symmetric and write

\[
s(A):=s_3(A),
\]

the third largest singular value. Thus the owner target is the class `s(A)>=1`. Put

\[
Q_A=X^TAX.
\]

For a probability law `mu` on the line, define

\[
\gamma_\varepsilon(u)=\frac{1}{\sqrt{2\pi}\varepsilon}
 e^{-u^2/(2\varepsilon^2)},\qquad
M_\varepsilon(\mu):=\sup_y(\mu*\gamma_\varepsilon)(y).
\]

For `Q_A` write `M_\varepsilon(A,f)` for this quantity.

Define the optimal target height in interval form

\[
C_*:=\sup_{\substack{n,f,\,A=A^T\\s(A)\ge1}}
\sup_{I:|I|>0}\frac{\Pr\{Q_A\in I\}}{|I|}\in[0,\infty].
\]

This definition is valid without presupposing a bounded density. The already completed fixed-instance regularity theorem gives a bounded `C_0` density for every rank-`>=3` instance, but that qualitative fact is not needed for the interval-scaling identity below.

## 2. New exact one-window identity

### Theorem 2.1 — unit-window homogeneous normal form

Let

\[
D_*:=\frac12\sup_{\substack{n,f,\,A=A^T\\s(A)>0}}
 s(A)\sup_{y\in\mathbb R}\Pr\{|Q_A-y|\le1\}.
\]

Then

\[
\boxed{C_*=D_*.}
\]

Consequently the full QFORM conjecture is equivalent, with the **same sharp constant**, to the single fixed-window estimate

\[
\boxed{
\Pr\{|X^TAX-y|\le1\}\le \frac{2C}{s_3(A)}
\quad\text{for every }s_3(A)>0.
}
\]

There is no radius parameter left.

### Proof

First suppose `A` is in the owner class, `s=s(A)>=1`, and let `I=[y-r,y+r]` with `r>0`. Set

\[
B=A/r.
\]

Then `s(B)=s/r` and `Q_B=Q_A/r`. Hence

\[
\Pr\{Q_A\in[y-r,y+r]\}
 =\Pr\{|Q_B-y/r|\le1\}
 \le \frac{2D_*}{s(B)}
 =\frac{2D_*r}{s}.
\]

Dividing by `|I|=2r` gives

\[
\frac{\Pr\{Q_A\in I\}}{|I|}\le\frac{D_*}{s}\le D_*.
\]

Thus `C_*<=D_*`.

Conversely fix any `B` with `s=s(B)>0` and normalize

\[
A=B/s,
\]

so `s(A)=1` and `Q_B=sQ_A`. For every `y`,

\[
\Pr\{|Q_B-y|\le1\}
 =\Pr\{|Q_A-y/s|\le1/s\}.
\]

The interval on the right has length `2/s`, and by the definition of `C_*`,

\[
\Pr\{|Q_B-y|\le1\}\le \frac{2C_*}{s}.
\]

Therefore `(s/2) sup_y Pr{|Q_B-y|<=1}<=C_*`. Taking the supremum gives `D_*<=C_*`. This proves the identity. `square`

## 3. New exact one-heat-scale identity

The completed partner result account04/B15 r4 proves for every probability law `mu`

\[
\sup_{\varepsilon>0}M_\varepsilon(\mu)=\|p_\mu\|_\infty,
\]

with value `+infinity` when no bounded density exists. For the target instances it also records the completed fixed-instance `C_0` regularity chain.

Apply that result to the spectral homogeneity rather than merely citing it.

### Theorem 3.1 — unit-heat homogeneous normal form

Define

\[
H_*:=\sup_{\substack{n,f,\,A=A^T\\s(A)>0}}
 s(A)\,M_1(A,f)
 =\sup_{\substack{n,f,\,A=A^T\\s(A)>0,\,y}}
 s(A)\,\mathbb E\gamma_1(X^TAX-y).
\]

Then

\[
\boxed{C_*=H_*.}
\]

Equivalently, the full conjecture with constant `C` is exactly equivalent to the **single positive finite-scale inequality**

\[
\boxed{
\sup_y\mathbb E\gamma_1(X^TAX-y)
 \le \frac{C}{s_3(A)}
\quad\text{for every }s_3(A)>0.
}
\]

### Proof

For every `c>0`, direct Gaussian scaling gives

\[
M_\varepsilon(cA,f)
 =c^{-1}M_{\varepsilon/c}(A,f).
\tag{3.1}
\]

Fix `B` with `s=s(B)>0` and put `A=B/s`, so `s(A)=1`. Then by (3.1),

\[
sM_1(B,f)=M_{1/s}(A,f).
\]

The partner heat-height theorem gives

\[
M_{1/s}(A,f)\le\sup_{\varepsilon>0}M_\varepsilon(A,f)
 =\|p_{Q_A}\|_\infty\le C_*.
\]

Therefore `H_*<=C_*`.

For the reverse inequality it is enough, by ordinary spectral scaling, to take matrices `A` with `s(A)=1`. Fix such an `A` and `epsilon>0`, and set

\[
B=A/\varepsilon.
\]

Then `s(B)=1/epsilon`, and again by (3.1),

\[
M_1(B,f)=\varepsilon M_\varepsilon(A,f).
\]

Thus

\[
s(B)M_1(B,f)=M_\varepsilon(A,f).
\]

Taking the supremum over `B` on the left and then over `epsilon,y` on the right, the partner theorem yields

\[
H_*\ge \sup_{\varepsilon>0}M_\varepsilon(A,f)=\|p_{Q_A}\|_\infty.
\]

Finally take the supremum over normalized target instances. Hence `H_*>=C_*`, proving equality. `square`

## 4. Application of the completed account04/B15 partner result

The named compatible completed partner artifact is:

- `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`;
- result: exact Gaussian heat-height closure, plus the source-pinned reduction through account01/B15 to strictly positive analytic-Schwartz cap-one marginals.

That result is applied above in the actual inequality

\[
s(A)M_1(A,f)
 =M_{1/s(A)}(A/s(A),f)
 \le \|p_{Q_{A/s(A)}}\|_\infty.
\tag{4.1}
\]

It also gives a stronger smooth normal form. The partner report proves

\[
C_*=\sup_{\substack{s_3(A)=1\\f_i>0\text{ analytic Schwartz}\\\|f_i\|_\infty\le1}}
\sup_{\varepsilon>0,y}\mathbb E\gamma_\varepsilon(Q_A-y).
\]

The bijective scaling `B=A/epsilon` converts this with **zero loss** into

\[
\boxed{
C_*=\sup_{\substack{s_3(B)>0\\f_i>0\text{ analytic Schwartz}\\\|f_i\|_\infty\le1}}
 s_3(B)\sup_y\mathbb E\gamma_1(Q_B-y).
}
\tag{4.2}
\]

Thus a proof may simultaneously use: one fixed Gaussian output scale, smooth positive rapidly decaying input marginals, and arbitrary spectral scale recorded only through the prefactor `s_3(B)`.

## 5. Damped Fourier form at one fixed scale

For every probability law the partner theorem gives the absolutely convergent identity

\[
M_1(A,f;y)
 =\frac1{2\pi}\int_{\mathbb R}
 e^{-ity}\phi_A(t)e^{-t^2/2}\,dt,
\]

where `phi_A(t)=E exp(it X^TAX)`. Therefore the entire target is equivalently the bound

\[
\boxed{
 s_3(A)\sup_y
 \left|\frac1{2\pi}\int e^{-ity}\phi_A(t)e^{-t^2/2}\,dt\right|
 \le C.
}
\tag{5.1}
\]

The absolute value is harmless because the integral equals the nonnegative real-space heat convolution. Crucially, (5.1) does **not** require taking `integral |phi_A|`, and it does not assert the false law-uniform pointwise van-der-Corput estimate. Frequency is now fixed at Gaussian scale `|t|=O(1)`; small output scales have been moved into large `s_3(A)` by exact homogeneity.

This is potentially useful for the current aggregate-before-inversion programme: a grouped-coordinate estimate only has to prove a unit-scale positive kernel bound with the correct `1/s_3(A)` homogeneity.

## 6. Fixed-instance regularity remains separate and qualitatively closed

The account04/B15 partner report records the completed account02/B15 theorem that every fixed rank-`>=3` target instance has

\[
p_{Q_A}\in C_0(\mathbb R)\cap L^\infty(\mathbb R),
\]

with a matrix-dependent constant. Consequently:

- absolute continuity is qualitatively proved for every target instance;
- a continuous representative, uniform continuity, vanishing at infinity, and attainment of the peak are qualitatively proved;
- the still-open statement is precisely the dimension- and matrix-independent height bound.

Theorems 2.1 and 3.1 do not confuse these statements: they reformulate only the universal height.

## 7. Corrections respected and first unpaid implication

This proof does not use:

- a pointwise `|t|^{-1/2}` oscillatory estimate;
- the false arbitrary-joint rank-three coarea lemma;
- a positive conditional projection-density moment;
- a single uniformly conditioned physical minor;
- rotation of the independent coordinates into an eigenbasis.

It is compatible with the live correction inbox, including the shell counterexample to unrestricted joint coarea and the families refuting single-local-block extraction.

**First unpaid implication after this run:** prove either one of the equivalent single-scale bounds

\[
\sup_{A,f,y}s_3(A)\,\mathbb E\gamma_1(Q_A-y)<\infty,
\]

or

\[
\sup_{A,f,y}\frac{s_3(A)}2\Pr\{|Q_A-y|\le1\}<\infty,
\]

while retaining the original-coordinate product structure and aggregating diffuse/heavy coordinates before any reciprocal tiny-minor payment.

This is exactly the full universal QFORM height problem, not a weaker auxiliary target.

## 8. Source state

Fresh control read before publication: `yspennstate/math-research-brain@49f2c35d027d97346db1494c21b7a4ff9ac607dc`; OWNER CONTROL revision `2026-09-22.15`, QFORM sole research target, no account03/B15 pause. Live correction blob observed: `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. Repository retrieval is not native mathematical-brain ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.

No scheduler/task mutation, notification change, email/Drive action, workflow dispatch, paid model/API/Codex call, public release, cross-account authentication, or permission expansion was performed.
