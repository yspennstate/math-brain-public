Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — quadratic neutral comparator and a sharper fixed-c coarse-entry target

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1230+0300__fixed_c_signed_comparator.md`, creation commit `9eeb9d4acfdbf8ebc178bd1c17da2ebb2f48849f`, readback blob `d6b978467d6df566f982babe55e1d7c3976b2c19`.

Outside P07 source: Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed here.

The previous run proved at

\[
a_*={c_*\over4}=0.430159709001947\ldots,
\qquad c_*=1.72063883600779\ldots,
\]

the source-coupled bound

\[
\nu_{c_*}^2\le 0.593984648584427+o_{\mathbf P}(1)
\]

for the exact sharp selected-moment target. The present run strengthens that bound by adding a **quadratic target-neutral signed correction** before applying the same projection/comparator lemma. The resulting actual finite-model theorem is

\[
\boxed{\nu_{c_*}^2\le 0.450370864992+o_{\mathbf P}(1),}
\]

hence

\[
\boxed{\nu_{c_*}\le 0.671096763+o_{\mathbf P}(1).}
\]

The proof still avoids a global inverse-covariance estimate: the new signed comparator has the target moments exactly, and the only probabilistic input is the already-developed fixed-projector quadratic-convolution / exponential-insertion machinery.

A second deterministic improvement sharpens the old kurtosis shortcut from `Gamma<=sqrt(K)` to

\[
\boxed{\Gamma^2\le K-1,}
\]

where `K=E g_N^4/(E g_N^2)^2` is the kurtosis of the actual Newton score. Combining the new decrement bound with this inequality, it is now sufficient to prove the scalar fourth-moment estimate

\[
\boxed{K_{c_*}<7.73304804+o(1)}
\]

with source-sufficient failure. This is substantially weaker than proving the previous direct vector target `Gamma<2.12`.

The calibrated fixed-projector Hermite surrogate predicts much more room: its all-chaos values at `a_*` are approximately

\[
\nu^2=0.4391124040,\qquad K=5.54563817,
\qquad \Gamma=1.39597810,
\qquad A=0.26446332.
\]

These last constants remain **SURROGATE**, not a finite-model skew theorem.

---

## 1. Normalization and the exact target-neutral quadratic residual

Continue on odd cyclic order and the nonzero support

\[
\Omega_n=\mathbb Z_n\setminus\{0\},
\]

with `u_*` uniform on `Omega_n`. Let

\[
X_D={S_D\over\sqrt n},
\qquad
Z_D:=4X_D.
\]

At `c=4a`, the fixed-c Gibbs density relative to `u_*` is

\[
f_{D,a}(j)={e^{-aZ_D(j)}\over M_D(-4a)}.
\]

The inherited fixed-parameter partition theorem gives

\[
M_D(-4a)=e^{a^2/2}+o_{\mathbf P}(1).
\]

Thus, in every fixed polynomial-exponential moment,

\[
f_{D,a}=e^{-aZ_D-a^2/2}+o_{\mathbf P}(1).
\]

The exact sharp signed target density from the preceding report is `L_n`; in this normalization

\[
L_n=1-Z_D+o_{\mathbf P}(1)
\]

inside every fixed exponential moment.

Let `F_{*,D}` denote the centered selected-frequency feature span in `L^2(u_*)`, and let

\[
\Pi_{*,D}:L^2(u_*)\to F_{*,D}
\]

be its orthogonal projection. Put

\[
H_2(z)=z^2-1
\]

and define the quadratic residual

\[
\boxed{
R_{2,D}:=(I-\Pi_{*,D})H_2(Z_D).
}
\tag{1.1}
\]

Because constants are orthogonal to `F_{*,D}` and `H_2(Z_D)` is centered up to `o_P(1)` (one may subtract its exact `u_*` mean without changing anything below), the exact orthogonality relations are

\[
\mathbf E_* R_{2,D}=0,
\qquad
\mathbf E_*[R_{2,D}(\Phi_D-\mu_*)]=0.
\tag{1.2}
\]

Consequently, for every real scalar `b`,

\[
\boxed{L_{n,b}:=L_n+bR_{2,D}}
\tag{1.3}
\]

has exactly the same normalization and exactly the same selected-frequency target moments as `L_n`:

\[
\mathbf E_*L_{n,b}=1,
\qquad
\mathbf E_*[L_{n,b}\Phi_D]=t_n.
\tag{1.4}
\]

No positivity of `L_{n,b}` is needed; it is used only as a signed comparator.

---

## 2. Comparator lemma with the neutral correction

Apply Lemma 4.1 of the previous report with the positive Gibbs law `p_{D,a}=f_{D,a}u_*` and the exact signed target law `L_{n,b}u_*`. The actual Newton decrement therefore obeys

\[
\boxed{
\nu_{D,a}^2
\le
\mathbf E_*\left[{L_{n,b}^2\over f_{D,a}}\right]-1.
}
\tag{2.1}
\]

Equivalently,

\[
\nu_{D,a}^2
\le
M_D(-4a)\,
\mathbf E_*\left[e^{aZ_D}(L_n+bR_{2,D})^2\right]-1.
\tag{2.2}
\]

The point of (2.2) is that the inverse covariance has again disappeared. We only have to evaluate one weighted quadratic form in the explicit target-neutral residual `R_{2,D}`.

---

## 3. Weighted half-capture identity for the second chaos

Write

\[
U_{2,D}:=\Pi_{*,D}H_2(Z_D),
\qquad
R_{2,D}=H_2(Z_D)-U_{2,D}.
\]

The earlier transverse-convolution theorem identified the selected quadratic direction through the same-mask convolution `Q=e*e`, and proved that the selected projector captures asymptotically one half of the Gaussian second-chaos energy. The same fixed-degree Walsh/additive-collision calculation allows any fixed polynomial insertion and, after truncating the exponential and using the inherited subgaussian exponential moments, any fixed exponential insertion.

For every fixed polynomial `P` and fixed real `a`, outside failure `o(1/sqrt(log n))`,

\[
\mathbf E_*\left[e^{aZ_D}U_{2,D}P(Z_D)\right]
=
{1\over2}\,
\mathbf E\left[e^{aZ}H_2(Z)P(Z)\right]
+o(1),
\tag{3.1}
\]

and

\[
\mathbf E_*\left[e^{aZ_D}U_{2,D}^2\right]
=
{1\over4}\mathbf E[e^{aZ}H_2(Z)^2]
+{1\over2}\mathbf E[e^{aZ}]
+o(1),
\tag{3.2}
\]

where `Z~N(0,1)`.

### Why (3.1)--(3.2) are the same collision theorem, not a new independence assumption

For a polynomial insertion of fixed degree, both sides expand into a fixed list of cyclic convolution words in the mask Rademachers. Pairing/disconnected diagrams give the Gaussian Wick terms. Selecting the output frequency contributes the already-proved half-frequency factor. Every connected two-copy diagram loses at least one free cyclic frequency, so its normalized contribution has variance `O_a(1/n)`. Truncate `e^{aZ}` at fixed degree, apply the finite list result, then let the truncation degree grow after the `n->infinity` limit; the fixed-parameter subgaussian exponential-moment bound controls the tail. This gives source-sufficient failure after the same `n^{-1/4}` tolerance choice used in the previous partition report.

Equations (3.1)--(3.2) are equivalently represented by the calibrated bookkeeping model

\[
U_2={H_2(Z)\over2}+{W\over\sqrt2},
\qquad
R_2={H_2(Z)\over2}-{W\over\sqrt2},
\tag{3.3}
\]

with `W` a formal orthogonal unit-variance noise. Equation (3.3) is only shorthand for the Wick constants in (3.1)--(3.2); the proof uses the finite cyclic collision expansion.

It follows that, with

\[
w_a(Z):=e^{aZ+a^2/2},
\]

we have

\[
\mathbf E_*\left[{R_{2,D}^2\over f_{D,a}}\right]
\to
A(a),
\tag{3.4}
\]

\[
\mathbf E_*\left[{(1-Z_D)R_{2,D}\over f_{D,a}}\right]
\to
B(a),
\tag{3.5}
\]

and

\[
\mathbf E_*\left[{(1-Z_D)^2\over f_{D,a}}\right]
\to
C(a),
\tag{3.6}
\]

where the Gaussian integrals are explicit.

---

## 4. Exact Gaussian evaluation of the comparator quadratic form

Tilting a standard Gaussian by `e^{aZ}` shifts it to `N(a,1)`. Direct moment calculation gives

\[
\boxed{
A(a)
=e^{a^2}\left(1+a^2+{a^4\over4}\right),
}
\tag{4.1}
\]

\[
\boxed{
B(a)
=-{e^{a^2}\over2}
a(a^2-a+2),
}
\tag{4.2}
\]

and

\[
\boxed{
C(a)
=e^{a^2}\big((1-a)^2+1\big).
}
\tag{4.3}
\]

For completeness, (4.1) follows from

\[
\mathbf E_{N(a,1)}(Z^2-1)^2
=2+4a^2+a^4,
\]

and the extra orthogonal half-energy in (3.3). Likewise

\[
{1\over2}\mathbf E_{N(a,1)}[(1-Z)(Z^2-1)]
=-{a(a^2-a+2)\over2},
\]

which is (4.2).

Thus the asymptotic comparator bound from (2.2) is

\[
J_a(b)
=C(a)+2bB(a)+b^2A(a)-1.
\tag{4.4}
\]

Since `A(a)>0`, the exact minimizing coefficient is

\[
\boxed{
b_*(a)=-{B(a)\over A(a)}
={a(a^2-a+2)\over2(1+a^2+a^4/4)}.}
\tag{4.5}
\]

The minimized value is

\[
\boxed{
J_2(a):=C(a)-{B(a)^2\over A(a)}-1.
}
\tag{4.6}
\]

This is a strict improvement over the affine comparator value `V(c)=C(a)-1` whenever `a>0`.

---

## 5. New actual finite-model decrement theorem at the inherited optimizer

The owner directive for this line asked to stay at the inherited `c_*` unless a different fixed-c choice is separately justified. Accordingly I keep

\[
a_*=0.430159709001947\ldots .
\]

At this value,

\[
A(a_*)=1.436211697883841\ldots,
\]

\[
B(a_*)=-0.454158337997890\ldots,
\]

\[
C(a_*)=1.593984648584427\ldots,
\]

and

\[
\boxed{
b_*(a_*)=0.316219634380545\ldots .}
\tag{5.1}
\]

Therefore

\[
\boxed{
J_2(a_*)
=0.450370864991858\ldots .
}
\tag{5.2}
\]

Combining Sections 1--4 proves:

### Theorem 5.1 — quadratic-neutral source-coupled decrement bound

For the actual odd-order random-circulant finite model, the fixed-c Gibbs seed at `c=c_*` and the exact sharp target `t_n=-n^{-1/2}1_D` satisfy, outside failure `o(1/sqrt(log n))`,

\[
\boxed{
\nu_{c_*}^2
\le0.450370864992+o(1),
}
\tag{5.3}
\]

hence

\[
\boxed{
\nu_{c_*}
\le0.671096763+o(1).
}
\tag{5.4}
\]

The comparator is signed, but the Gibbs seed itself remains positive. No global minimum-eigenvalue lower bound is used in the leading estimate.

This is a genuine finite-model improvement over the preceding `0.593984649` decrement-square bound.

---

## 6. Deterministic sharpening: `Gamma^2 <= K-1`

Let a current positive law have centered feature vector `X`, covariance `Sigma`, residual `r`, Newton score

\[
g_N=-r^T\Sigma^{-1}X,
\qquad
\nu^2=\mathbf E g_N^2,
\]

and third-cumulant vector

\[
\tau=\mathbf E[Xg_N^2].
\]

Whiten the feature span, or equivalently let `P_F` denote orthogonal projection in `L^2(p)` onto the centered feature-linear span. Since `X` is centered,

\[
\tau
\quad\text{is exactly the coefficient vector of}\quad
P_F(g_N^2-\nu^2).
\]

Therefore

\[
\tau^T\Sigma^{-1}\tau
=
\|P_F(g_N^2-\nu^2)\|_2^2
\le
\|g_N^2-\nu^2\|_2^2.
\]

Writing

\[
K={\mathbf E g_N^4\over\nu^4},
\]

we obtain the sharper deterministic inequality

\[
\boxed{
\Gamma^2
={\tau^T\Sigma^{-1}\tau\over\nu^4}
\le K-1.
}
\tag{6.1}
\]

The earlier generic statement `Gamma<=sqrt(K)` loses the centering subtraction; (6.1) is strictly stronger.

---

## 7. Consequence: the fixed-c probabilistic target is now only a scalar kurtosis bound

For the positive square-Newton step define

\[
\beta(\nu)={\nu\over1+\sqrt{1-\nu^2}}.
\]

The contraction condition is

\[
A={\Gamma\beta\over2}<\frac12,
\]

or simply

\[
\Gamma<\beta^{-1}.
\]

Using the new rigorous upper bound (5.4),

\[
\beta\le0.38538441091+o(1),
\]

so it is enough to prove

\[
\boxed{
\Gamma<2.594811756+o(1).
}
\tag{7.1}
\]

By (6.1), a still simpler sufficient condition is

\[
\boxed{
K<1+\beta^{-2}
=7.733048049+o(1).
}
\tag{7.2}
\]

Thus the fixed-c coarse-entry problem has been reduced from a vector inverse-covariance skew estimate to a scalar fourth-moment estimate for the **actual** source-coupled Newton score.

---

## 8. Calibrated all-chaos fixed-projector benchmark

This subsection is a benchmark, not a finite-model theorem.

The earlier two-chaos fixed-c surrogate can be extended without resampling the selected projector. Under the base Gaussian reference let

\[
U_1=Z,
\]

and for `k>=2`

\[
U_k={H_k(Z)\over\sqrt{2k!}}+{W_k\over\sqrt2},
\]

where the `W_k` are formal mutually orthogonal unit-variance noises. This keeps one fixed half-projection of every higher Hermite chaos. Under the Gibbs tilt `e^{-aZ-a^2/2}`, put `Y=Z+a`. After centering,

\[
U_k-\mathbf E_aU_k
=
\sum_{j=1}^k
{\binom{k}{j}(-a)^{k-j}\sqrt{j!}\over\sqrt{2k!}}
{H_j(Y)\over\sqrt{j!}}
+{W_k\over\sqrt2},
\qquad k\ge2,
\tag{8.1}
\]

while `U_1-E_aU_1=Y`.

For a truncation at degree `R`, define the lower-triangular matrix `T_R` by

\[
(T_R)_{11}=1,
\]

\[
(T_R)_{kj}
={\binom{k}{j}(-a)^{k-j}\sqrt{j!}\over\sqrt{2k!}},
\qquad 2\le k\le R,\ 1\le j\le k,
\tag{8.2}
\]

and noise matrix

\[
N_R=\operatorname{diag}(0,1/2,\ldots,1/2).
\]

Then

\[
C_R=T_RT_R^T+N_R.
\tag{8.3}
\]

The sharp-target residual is

\[
r_1=1-a,
\qquad
r_k={(-a)^k\over\sqrt{2k!}},\quad k\ge2.
\tag{8.4}
\]

Solving the finite system gives

\[
\nu_R^2=r_R^TC_R^{-1}r_R.
\tag{8.5}
\]

At `a=a_*`, the values stabilize very rapidly:

\[
\begin{array}{c|c|c|c}
R&\nu_R^2&\Gamma_R&K_R\\ \hline
2&0.4387194166&1.330155205&5.510505452\\
4&0.4391098038&1.393080287&5.548050873\\
8&0.4391124035&1.395973638&5.545641356\\
12&0.4391124040&1.395978085&5.545638178
\end{array}
\tag{8.6}
\]

The limiting benchmark is therefore

\[
\boxed{
\nu^2\approx0.4391124040,
\quad
\Gamma\approx1.395978095,
\quad
K\approx5.545638173.
}
\tag{8.7}
\]

Its square-Newton skew parameter is only

\[
A\approx0.264463323.
\tag{8.8}
\]

This benchmark preserves the fixed selected projector; it is **not** the invalid model in which a fresh random half-projection is resampled after every repair step.

Equation (8.7) is not yet promoted to the finite model. Its role is to show that the new sufficient scalar target (7.2) has a meaningful numerical margin: the calibrated value `5.54564` is about `2.19` below the allowed `7.73305`.

---

## 9. What remains open after this run

The actual fixed-c directional skew is **not** proved in this report. The exact remaining probabilistic obligation is now narrower:

> Prove, with failure `o(1/sqrt(log n))`, that the actual Newton score at `c=c_*` satisfies `K<7.733048` (preferably `K<=6`) or directly `Gamma<2.594812`.

A source-valid way to do it is now clear.

1. Use the degree-`R` fixed-projector convolution/Krylov directions generated by the mask, with `R=8` as the first concrete target.
2. Transport the weighted covariance and restricted Newton system using the existing fixed-degree collision theorem. The deterministic reference matrix is (8.2)--(8.4), not an independently resampled projector.
3. Evaluate the fourth moment of the resulting finite-degree score. The benchmark at `R=8` is `K_8=5.545641356`.
4. Bound the analytic Hermite tail directly from fixed-parameter exponential moments. The fixed-c likelihood has factorial Hermite decay; do not use a worst-case Fourier operator norm.
5. It is enough to keep the total fourth-moment error below about `2.18`; no publication-level constant optimization is required.

If this scalar kurtosis estimate is established, (5.4), (6.1), and (7.2) give an **actual absolute contracting coarse-entry step**. At that point the already-proved growing-degree tail

\[
\nu_{j+1}\le\sqrt{2\Gamma_j}\,\nu_j^{3/2}
\]

can be invoked rather than rebuilding the old near-boundary argument.

---

## 10. Obligation ledger

- **Full-source P07 metric:** unchanged, `sqrt(n) <= E theta <= C sqrt(n log log n)`.
- **P06 source status:** KNOWN in later literature; `U_ER^cert=1` preserved, no rescreening.
- **New actual theorem:** fixed-c sharp-target decrement improved from `nu^2<=0.593984649+o_P(1)` to `nu^2<=0.450370865+o_P(1)`.
- **New deterministic lemma:** `Gamma^2<=K-1`.
- **New sufficient fixed-c scalar target:** actual Newton-score kurtosis `K<7.733048`.
- **Surrogate benchmark:** `K≈5.545638`, `Gamma≈1.395978`, `A≈0.264463`; not yet finite-model proof.
- **Remaining source-closing bridge:** actual fixed-c fourth-moment/skew control, then invoke the inherited superlinear coarse tail.
- **Parity:** odd cyclic order only here; even-order self-inverse frequency remains untreated.

Next attack: **actual finite-model Newton-score kurtosis at `c=c_*` via the degree-8 fixed-projector Hermite/convolution system, with an explicit fourth-moment error budget below `2.18`.**
