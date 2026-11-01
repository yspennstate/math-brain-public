Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# I0006: mean-shift susceptibility, activation fronts, and reflection-transparent perturbations

Status: **proved deterministic/probabilistic finite-horizon theorems / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`.  
Target: `I0006`, Bou-Rabee–Panagiotis high-dimensional unbounded-below odometer rate.  
Admission: `research7_2026-09-17/R7-06/admissions/2026-09-18T100120Z__I0006.md`.  
Previous artifact: `research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T115600Z__I0006_reflection_sensitivity_killed_green.md`.

No source-level closure or publication-novelty claim is made here. The frozen milestone metric `M_crit(d)` remains zero; the results below attack the unresolved slowly varying factor without redefining that metric.

## 1. Starting point and the three new methods

At the critical lower-tail exponent

\[
\gamma=\frac d2,\qquad d\ge5,
\]

the preceding R7-06 work established two facts.

First, the admitted source milestone has logarithmic exponent exactly `2/d`:

\[
c(\log t)^{2/d}
\le \mathbb E u_t(0)
\le C(\log t)^{2/d}(\log\log t)^{(d-2)/d}.
\tag{1.1}
\]

Second, the logarithm in the corresponding **unreflected** Green-scenery large deviation is genuine. Therefore a route to a pure `(log t)^(2/d)` law cannot consist merely of sharpening the raw Green estimate.

The immediately preceding run changed category to an obstacle/optimal-stopping problem and identified the exact reflected sensitivity as a dynamically killed Green kernel. Its remaining unknown was the effective lifetime of that kernel.

This run uses three different Section-B moves from the preceding triple:

- **B5 — add a parameter and differentiate:** lower the scenery by a uniform penalty `r`, and identify the derivative with the expected optimal stopping time. This gives an exact susceptibility sum rule.
- **B18 — say it in another language:** rewrite killed-kernel lifetime as hitting of a space-time activation front, and replace the previous worst-case finite-amplitude lifetime by an averaged susceptibility.
- **B21 — import a technique from an analogous field:** use obstacle/complementarity ideas to identify an exact cone of downward perturbations on which reflection is completely transparent and the response is the raw Green response.

The combined conclusion is deliberately two-sided. Uniform mean shifts make the **expected** susceptibility collapse at the natural critical odometer scale, but specially shaped negative perturbations can pass through reflection with **no clipping at all** whenever their Green potential stays below the odometer. Thus the unresolved issue is not whether reflection can kill the critical Green logarithm — it can — but whether source-relevant rare negative profiles are typically clipped before they realize the raw critical variational optimizer.

## 2. Setup

Let `P` be the simple-random-walk averaging operator on `Z^d`. For a deterministic scenery `z:Z^d->R` and a uniform downward penalty `r>=0`, define

\[
u_0^{(r)}\equiv0,
\qquad
u_{k+1}^{(r)}=(z-r+Pu_k^{(r)})_+.
\tag{2.1}
\]

Write

\[
F_k^{(r)}=z-r+Pu_k^{(r)}.
\tag{2.2}
\]

For `r=0` this is the finite-horizon reflected recursion used in the preceding artifact.

The Bellman representation is

\[
\boxed{
 u_n^{(r)}(x)
 =
 \sup_{\tau\le n}
 \mathbb E_x\left[
 \sum_{j=0}^{\tau-1}(z(X_j)-r)
 \right],
}
\tag{2.3}
\]

where stopping immediately is allowed. This follows from the one-step recursion

\[
V_{k+1}(x)=\max\{0,z(x)-r+PV_k(x)\}.
\]

For fixed `n,x,z`, the function `r -> u_n^(r)(x)` is decreasing, convex, and piecewise affine: it is the supremum of affine functions with slopes in `[-n,0]`.

## 3. B5 — mean-shift susceptibility is the derivative of the odometer

### 3.1 The minimal-duration optimal rule

Define the strict-active indicator

\[
A_k^{(r)}(x)=\mathbf 1_{\{F_k^{(r)}(x)>0\}}.
\tag{3.1}
\]

For a horizon `n`, define the Bellman stopping time

\[
\tau_n^{(r)}
=
\inf\Bigl\{0\le j\le n:
 j=n\ \text{or}\ F_{n-1-j}^{(r)}(X_j)\le0
\Bigr\}.
\tag{3.2}
\]

Thus ties are resolved by stopping rather than continuing.

### Proposition 3.1 (minimal-duration optimizer)

`tau_n^(r)` is optimal in (2.3). Among all optimal stopping times for (2.3), it minimizes expected duration.

#### Proof

The statement is proved by backward induction on the remaining horizon.

At horizon zero, immediate stopping is the only rule. Suppose the claim holds for horizon `k`. At horizon `k+1`, if

\[
F_k^{(r)}(x)=z(x)-r+Pu_k^{(r)}(x)<0,
\]

continuing is strictly suboptimal; every optimal rule stops immediately. If `F_k^(r)(x)>0`, stopping is strictly suboptimal; every optimal rule continues one step, after which the inductively minimal-duration optimal rule is used. If `F_k^(r)(x)=0`, both stopping and continuing with an optimal continuation produce the same value zero at the first decision, but stopping has duration zero and therefore has minimal expected duration. This is exactly the rule (3.2). ∎

### 3.2 Killed-kernel mass equals optimal duration

The previous artifact defined, for scenery `z-r`,

\[
K_{n,r}(x,y)
=
\mathbb E_x\left[
\sum_{j=0}^{n-1}
\mathbf1_{\{X_j=y\}}
\prod_{i=0}^{j}
A_{n-1-i}^{(r)}(X_i)
\right].
\tag{3.3}
\]

Let

\[
L_n^{(r)}(x)=\sum_y K_{n,r}(x,y).
\tag{3.4}
\]

The product in (3.3) is one exactly through those times strictly before `tau_n^(r)`. Hence

\[
\boxed{
L_n^{(r)}(x)=\mathbb E_x\tau_n^{(r)}.
}
\tag{3.5}
\]

This turns the abstract effective lifetime from the preceding run into a concrete optimal-stopping duration.

### Proposition 3.2 (exact right derivative / susceptibility identity)

For every finite `n`, deterministic `z`, `x`, and `r>=0`,

\[
\boxed{
-\partial_{r+}u_n^{(r)}(x)
=L_n^{(r)}(x)
=\mathbb E_x\tau_n^{(r)}.
}
\tag{3.6}
\]

Moreover `r -> L_n^(r)(x)` is nonincreasing.

#### Proof

There are two equivalent proofs.

**Kernel proof.** Increasing `r` to `r+epsilon` lowers the scenery by the constant perturbation `epsilon * 1`. The preceding artifact proved that the one-sided downward derivative in a perturbation `eta` is

\[
d_n^{z,\eta}(x)=\sum_y K_{n,z}(x,y)\eta(y).
\]

Taking `eta=1` and scenery `z-r` gives (3.6).

**Envelope proof.** Each stopping time contributes the affine function

\[
B_\tau-r\,\mathbb E_x\tau,
\qquad
B_\tau=\mathbb E_x\sum_{j<\tau}z(X_j).
\]

For a supremum of affine functions, the right derivative is the largest slope among the active maximizers. Since the slopes are `-E tau`, this is minus the smallest expected duration among optimal rules. Proposition 3.1 identifies that duration with `E tau_n^(r)`, proving (3.6).

Convexity of `u_n^(r)(x)` implies that its right derivative is nondecreasing in `r`; therefore its negative, `L_n^(r)(x)`, is nonincreasing. ∎

## 4. Random scenery: an exact susceptibility sum rule

Now let `z=zeta` be the source-type i.i.d. translation-invariant scenery, with enough integrability that the finite-horizon odometer is integrable; the admitted exponential-moment hypothesis is more than sufficient. Define

\[
a_n(r)=\mathbb E\,u_n^{(r)}(0),
\qquad
\chi_n(r)=\mathbb E\,L_n^{(r)}(0).
\tag{4.1}
\]

Because changing `r` by `epsilon` changes the reward of every path by at most `n epsilon`, the random difference quotients are bounded by `n`. Hence differentiation can be passed through expectation.

### Theorem 4.1 (susceptibility sum rule)

For every finite `n`,

\[
\boxed{
\partial_{r+}a_n(r)=-\chi_n(r).
}
\tag{4.2}
\]

The function `a_n` is decreasing, convex and absolutely continuous; `chi_n` is nonincreasing. Furthermore

\[
\lim_{r\to\infty}a_n(r)=0
\tag{4.3}
\]

and therefore

\[
\boxed{
 a_n(r)=\int_r^\infty \chi_n(s)\,ds,
 \qquad
 a_n(0)=\int_0^\infty \chi_n(s)\,ds.
}
\tag{4.4}
\]

Consequently, for every `r>0`,

\[
\boxed{
\chi_n(r)\le \frac{a_n(0)}{r}.
}
\tag{4.5}
\]

In particular, for every fixed `theta in (0,1]` with `a_n(0)>0`,

\[
\boxed{
\chi_n(\theta a_n(0))\le \theta^{-1}.
}
\tag{4.6}
\]

#### Proof

Equation (4.2) follows from Proposition 3.2 and dominated convergence, using `0<=L_n^(r)<=n`.

For each realization, only the finite ball reachable in at most `n` steps can influence the value. Its scenery values are finite almost surely. For sufficiently large `r` every possible nonempty path has negative total penalized reward, so `u_n^(r)(0)` decreases pointwise to zero. Since `0<=u_n^(r)(0)<=u_n^(0)(0)` and the latter is integrable, dominated convergence proves (4.3).

An `n`-Lipschitz convex function is absolutely continuous on bounded intervals. Integrating (4.2), then letting the upper endpoint tend to infinity and using (4.3), gives (4.4).

Since `chi_n` is nonincreasing,

\[
a_n(0)
=\int_0^\infty\chi_n(s)ds
\ge\int_0^r\chi_n(s)ds
\ge r\chi_n(r),
\]

which is (4.5). Substituting `r=theta a_n(0)` gives (4.6). ∎

### Interpretation

The natural critical scale itself controls the stopping susceptibility. Once the scenery mean is shifted downward by a fixed fraction of `a_n(0)`, the expected optimal stopping horizon is bounded independently of `n`.

This is a genuine collapse that cannot be seen from the raw Green kernel, whose total mass is order `n`.

## 5. Consequence for critical killed-Green q-energy

For the pre-reflection field define, as previously,

\[
\widetilde K_{n,r}(x,y)
=
\mathbf1_{\{x=y\}}
+\sum_wP(x,w)K_{n,r}(w,y),
\tag{5.1}
\]

and

\[
\widetilde L_n^{(r)}(x)=\sum_y\widetilde K_{n,r}(x,y).
\tag{5.2}
\]

Then

\[
\widetilde L_n^{(r)}(x)=1+P L_n^{(r)}(x).
\tag{5.3}
\]

By translation invariance of the scenery law,

\[
\boxed{
\mathbb E\widetilde L_n^{(r)}(0)=1+\chi_n(r).
}
\tag{5.4}
\]

At the source endpoint put

\[
\gamma=\frac d2,
\qquad q=\frac d{d-2}.
\]

The preceding artifact proved pathwise that

\[
Q_n^{(r)}(x)
:=\sum_y\widetilde K_{n,r}(x,y)^q
\le C_d\bigl(1+\log(1+\widetilde L_n^{(r)}(x))\bigr).
\tag{5.5}
\]

Jensen's inequality and (5.4) give the following.

### Corollary 5.1 (mean-shift energy collapse)

For every `r>0`,

\[
\boxed{
\mathbb E Q_n^{(r)}(0)
\le
C_d\left[
1+\log\left(2+\frac{a_n(0)}r\right)
\right].
}
\tag{5.6}
\]

Hence for fixed `theta in (0,1]`,

\[
\boxed{
\mathbb E Q_n^{(\theta a_n(0))}(0)
\le C_{d,\theta},
}
\tag{5.7}
\]

uniformly in `n`.

Moreover, for every `R>0`,

\[
\boxed{
\frac1R\int_0^R
\mathbb E Q_n^{(r)}(0)\,dr
\le
C_d\left[
2+\log\left(2+\frac{a_n(0)}R\right)
\right].
}
\tag{5.8}
\]

#### Proof

Equation (5.6) follows from (5.5), concavity of `log`, (5.4), and (4.5).

For (5.8), put `A=a_n(0)` and `r=Rt`. For `0<t<=1`,

\[
2+\frac{A}{Rt}
\le \frac{2+A/R}{t}.
\]

Thus

\[
\int_0^1\log\left(2+\frac{A}{Rt}\right)dt
\le
\log(2+A/R)+\int_0^1\log(1/t)dt
=
\log(2+A/R)+1.
\]

Insert this into the averaged version of (5.6). ∎

This result says that the critical logarithmic `q`-energy is confined to a thin near-critical mean-shift window. It does **not** yet solve the source law at `r=0`: a mean shift changes the scenery distribution, and a source-faithful argument still has to transport this susceptibility information back to the critical law.

## 6. B18 — the killed lifetime is hitting of a space-time activation front

The Bellman values increase with horizon:

\[
u_{k+1}^{(r)}\ge u_k^{(r)}.
\tag{6.1}
\]

This follows immediately from the stopping representation because every stopping time allowed at horizon `k` is also allowed at horizon `k+1`. Consequently

\[
F_{k+1}^{(r)}\ge F_k^{(r)}
\tag{6.2}
\]

pointwise.

Define the activation time of a site by

\[
\sigma_r(y)
=
\inf\{k\ge0:F_k^{(r)}(y)>0\}
\in\{0,1,2,\ldots,\infty\}.
\tag{6.3}
\]

Then `A_k^(r)(y)=1` exactly when `sigma_r(y)<=k`. Substituting this in the Bellman rule gives the exact identity

\[
\boxed{
\tau_n^{(r)}
=
\inf\Bigl\{0\le j\le n:
 j=n\ \text{or}\
 \sigma_r(X_j)>n-1-j
\Bigr\}.
}
\tag{6.4}
\]

Thus the susceptibility is a **space-time first-passage quantity**: a random walk runs forward in space while Bellman time runs backward, and sensitivity dies when the walk crosses the activation front.

This language isolates the missing probabilistic estimate. It is not enough to know that the contact set is large at one time slice; one needs control of the slanted space-time crossing in (6.4).

### 6.1 Finite-amplitude response uses averaged, not worst-case, susceptibility

Let `eta>=0` be any bounded finite-horizon perturbation and set `z_s=z-s eta`, `0<=s<=1`. The previous artifact proved

\[
F_n^z(x)-F_n^{z-\eta}(x)
=
\int_0^1
\sum_y\widetilde K_{n,z_s}(x,y)\eta(y)\,ds.
\tag{6.5}
\]

Define the averaged kernel

\[
\overline K(y)
=
\int_0^1\widetilde K_{n,z_s}(x,y)\,ds
\tag{6.6}
\]

and its mass

\[
\overline L
=
\sum_y\overline K(y)
=
\int_0^1\widetilde L_{n,z_s}(x)\,ds.
\tag{6.7}
\]

Because each `widetilde K <= G`, also `0<=bar K<=G`. Therefore the preceding critical energy-compression lemma applies directly to `bar K`:

\[
\sum_y\overline K(y)^q
\le C_d\bigl(1+\log(1+\overline L)\bigr).
\tag{6.8}
\]

If the finite perturbation lowers the pre-field by `h`, then by (6.5)

\[
h=\sum_y\overline K(y)\eta(y).
\]

Holder gives the sharper finite-amplitude lower bound

\[
\boxed{
\sum_y\eta(y)^\gamma
\ge
c_d\frac{h^\gamma}
{\left[1+\log(1+\overline L)\right]^{\gamma-1}}.
}
\tag{6.9}
\]

This improves the preceding run's bound based on the **supremum** of the lifetime along the deformation. The exact finite-amplitude cost depends only on the averaged susceptibility encountered along the deformation path.

It still leaves the same fundamental source-probability question: how large is `bar L` for the rare downward deformations that actually dominate the critical odometer tail?

## 7. B21 — a reflection-transparent cone

The susceptibility results above show that reflection can strongly suppress response. The complementary question is whether there are perturbations for which it does not suppress response at all.

For `eta>=0`, define the finite Green potentials

\[
\psi_0=0,
\qquad
\psi_j=G_j\eta:=\sum_{i=0}^{j-1}P^i\eta,
\quad j\ge1.
\tag{7.1}
\]

### Theorem 7.1 (exact transparency criterion)

Fix a deterministic scenery `z`, perturbation `eta>=0`, and horizon `n`. Suppose

\[
\boxed{
G_j\eta\le u_j^z
\quad\text{pointwise for every }1\le j\le n.
}
\tag{7.2}
\]

Then for every `0<=j<=n`,

\[
\boxed{
 u_j^{z-\eta}=u_j^z-G_j\eta.
}
\tag{7.3}
\]

Consequently, for `0<=j<n`,

\[
\boxed{
F_j^z-F_j^{z-\eta}=G_{j+1}\eta,
}
\tag{7.4}
\]

so every contact-loss term in the previous reflection-loss decomposition vanishes through horizon `n`.

#### Proof

Induct on `j`. For `j=0`, both odometers are zero and `G_0 eta=0`.

Assume (7.3) holds at time `j<n`. Then

\[
\begin{aligned}
F_j^{z-\eta}
&=z-\eta+Pu_j^{z-\eta}\\
&=z-\eta+P(u_j^z-G_j\eta)\\
&=F_j^z-(\eta+PG_j\eta)\\
&=F_j^z-G_{j+1}\eta.
\end{aligned}
\tag{7.5}
\]

By hypothesis,

\[
0\le G_{j+1}\eta\le u_{j+1}^z=(F_j^z)_+.
\tag{7.6}
\]

For real numbers `a` and `b` satisfying `0<=b<=a_+`, one has

\[
(a-b)_+=a_+-b.
\tag{7.7}
\]

Applying (7.7) pointwise to (7.5) yields

\[
\begin{aligned}
u_{j+1}^{z-\eta}
&=(F_j^{z-\eta})_+\\
&=(F_j^z-G_{j+1}\eta)_+\\
&=(F_j^z)_+-G_{j+1}\eta\\
&=u_{j+1}^z-G_{j+1}\eta.
\end{aligned}
\]

This proves (7.3), and substituting it into (7.5) gives (7.4). ∎

Define the finite-horizon no-loss cone

\[
\boxed{
\mathcal C_n(z)
=
\{\eta\ge0:G_j\eta\le u_j^z\text{ for every }1\le j\le n\}.
}
\tag{7.8}
\]

On `C_n(z)`, the nonlinear reflected system responds **exactly linearly** to the downward perturbation: reflection is transparent.

This is the main obstruction found by B21. Any argument claiming that reflection automatically improves the raw Green large-deviation cost is false without additional information: there is a whole pathwise cone on which there is no improvement whatsoever.

## 8. Critical Green-shaped profiles sit at exactly the logarithmic variational cost

The transparency criterion becomes source-relevant because the raw critical optimizer has a simple multiscale shape.

Let

\[
\eta_R(y)
=
\lambda_R(1+|y|)^{-2}
\mathbf1_{\{1\le |y|\le R\}},
\qquad R\ge3.
\tag{8.1}
\]

Using the standard transient-lattice Green estimates

\[
G(0,y)\asymp_d |y|^{2-d}
\quad(|y|\ge1)
\tag{8.2}
\]

and shell cardinality `asymp r^(d-1)`, one obtains

\[
\sum_yG(0,y)\eta_R(y)
\asymp_d
\lambda_R\sum_{r=1}^R r^{-1}
\asymp_d \lambda_R\log R.
\tag{8.3}
\]

At `gamma=d/2`,

\[
\sum_y\eta_R(y)^\gamma
\asymp_d
\lambda_R^\gamma
\sum_{r=1}^Rr^{d-1-d}
\asymp_d
\lambda_R^\gamma\log R.
\tag{8.4}
\]

Choosing

\[
\lambda_R\asymp_d \frac h{\log R}
\tag{8.5}
\]

therefore gives Green response of order `h` at cost

\[
\boxed{
\sum_y\eta_R(y)^\gamma
\asymp_d
\frac{h^\gamma}{(\log R)^{\gamma-1}}.
}
\tag{8.6}
\]

This is exactly the critical logarithmic Weibull cost found in the sharp standalone Green theorem.

For finite horizons `n` with `n>=C R^2`, standard simple-random-walk heat-kernel lower bounds imply

\[
g_n(0,y)\asymp_d G(0,y)
\qquad (1\le |y|\le R),
\tag{8.7}
\]

so the same calculation applies to the finite Green response up to constants.

Hence, **conditionally on** `eta_R in C_n(z)`, Theorem 7.1 says that reflection transmits this entire critical deficit with no extra cost. Conversely, the susceptibility result says that sufficiently negative *uniform* shifts cause expected lifetime to collapse.

The open mechanism is now sharply localized between these two extremes.

## 9. Exact remaining barrier

The source-level slowly varying factor is not decided in this run. The exact blocking question can now be stated in either of two equivalent languages.

### Susceptibility language

For the critical scenery law, determine whether the source-relevant downward deformation paths have averaged effective lifetime

\[
\overline L
=
\int_0^1\sum_y\widetilde K_{n,z-s\eta}(0,y)\,ds
\tag{9.1}
\]

bounded, polylogarithmic, or of order the full horizon on the event producing a deficit of size comparable to `a_n`.

### Transparency language

For Green-shaped critical profiles `eta_R`, control the probability or geometry of

\[
\boxed{
G_j\eta_R\le u_j^\zeta
\quad\text{for every }j\le n.
}
\tag{9.2}
\]

If (9.2) occurs often enough on the large-deviation scale, the raw critical logarithmic cost can survive reflection. If such profiles are overwhelmingly clipped early, the killed-kernel energy can be much smaller and the current `log log` upper correction may be removable.

Neither conclusion follows from the deterministic theorems alone.

## 10. Literature status checked 2026-09-18

The current primary records recovered in the bounded check are still:

- Ahmed Bou-Rabee and Christoforos Panagiotis, *Sharpness and critical scaling of parking*, arXiv:2609.02820, submitted 2 September 2026;
- Ahmed Bou-Rabee and Christoforos Panagiotis, *Quantitative explosion and percolation of the divisible sandpile*, arXiv:2609.02829, submitted 2 September 2026.

The latter still describes the `d>=5` rate as tail-dependent in its current abstract. Bounded searches on 18 September 2026 for the exact arXiv IDs/titles/authors and `gamma=d/2` / borderline / follow-up terms did not recover a later source-matching resolution of the admitted endpoint or the full high-dimensional lower-tail classification.

The nearest solved category analogue remains Ahmed Bou-Rabee, Yuval Peres and Ecaterina Sava-Huss, *Divisible sandpiles via random walks in random scenery*, arXiv:2604.13968 (15 April 2026), which analyzes the associated optimal-stopping problem on general graphs. It supports the optimal-stopping language but does not supply the critical endpoint susceptibility estimate required here.

These search misses are **negative evidence only**, not proof of worldwide openness or publication novelty.

## 11. Status and metric

Frozen metric:

\[
M_{\rm crit}(d)
=
\text{width of the proved interval containing all subsequential values of }
\frac{\log\mathbb E u_t(0)}{\log\log t}.
\]

Before this run: `0`.  
After this run: `0`.  
Movement: **NO MOVEMENT**.

The useful advance is structural, not metric movement: the missing slowly varying factor is reduced to a quantitative space-time contact/susceptibility problem, and reflection is shown both to have a scale-free mean-shift suppression mechanism and an exact pathwise transparency cone.

Because this is the third consecutive ordinary research run with the frozen metric unchanged, the owner protocol requires the **next** R7-06 run to be a Section-I thinking-only stuck diagnosis, not another theorem/lemma run.
