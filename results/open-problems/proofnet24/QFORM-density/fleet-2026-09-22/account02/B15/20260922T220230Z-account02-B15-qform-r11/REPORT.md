# QFORM B15 — no target-uniform continuity modulus, even in the analytic-Schwartz normal form

**Run:** `20260922T220230Z-account02-B15-qform-r11`  
**Account/slot:** account02/B15  
**Assignment:** Absolute continuity and regularity  
**Status:** `SOURCE-VALID REGULARITY SEPARATION / FULL UNIVERSAL HEIGHT OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-22T22:02:30Z.

attacking: whether fixed-instance C0 regularity can yield any target-uniform local modulus near an attained peak; seek a source-valid counterexample or a quantitative regularity lemma without using continuity to pay the universal height.

## 1. Exact target and first unpaid implication

The owner target is: for independent real coordinates with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite constant `C` such that

\[
\|p_{X^TAX}\|_\infty\le C,
\]

or give a valid counterexample. The completed fixed-instance regularity chain gives, for every fixed rank-`>=3` matrix, a bounded `C_0` density with a matrix-dependent bound. The full universal height remains open.

I apply the completed assigned-partner result account03/B15 r18, canonical source

- `yspennstate/math-open-problems@ae1acd1eb774e59dd80eb9ddfb8ea9c7e72b79a1`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T213701Z-account03-B15-qform-r18/REPORT.md`.

Writing `s(A)=s_3(A)`, that result proves the exact identities

\[
C_*=
\frac12\sup_{s(A)>0,f,y}s(A)\Pr\{|X^TAX-y|\le1\}
\tag{1.1}
\]

and

\[
C_*=\sup_{s(A)>0,f,y}s(A)\,\mathbb E\gamma_1(X^TAX-y),
\tag{1.2}
\]

where `gamma_1` is the standard Gaussian density. It also records a zero-loss restriction of the heat normal form to strictly positive analytic-Schwartz cap-one marginal densities. Thus the first unpaid implication is exactly the single-scale bound in (1.1) or (1.2), not continuity.

This run proves that even on that very smooth source class there is **no common modulus of continuity at all** for the raw output densities. Hence no proof may extract a target-uniform local modulus from the already completed `C_0` conclusion and use that modulus as the missing height payment.

## 2. Main theorem — no common output continuity modulus

### Theorem 2.1

Fix the target matrix

\[
A=I_3.
\]

There exists a sequence of iid product inputs `X^{(m)}=(X_1^{(m)},X_2^{(m)},X_3^{(m)})` such that each one-dimensional marginal density `f_m` is

1. strictly positive on `R`;
2. real analytic and Schwartz;
3. a probability density satisfying `0<f_m<=1`;
4. uniformly tight as `m` varies;

and, writing

\[
Q_m=(X_1^{(m)})^2+(X_2^{(m)})^2+(X_3^{(m)})^2,
\]

the continuous densities `p_m` satisfy a uniform height bound

\[
\|p_m\|_\infty\le 2\pi,
\tag{2.1}
\]

but there is **no** function `omega(r)->0` as `r downarrow0` such that

\[
|p_m(t)-p_m(s)|\le \omega(|t-s|)
\quad\text{for all }m,s,t.
\tag{2.2}
\]

Equivalently, this fixed normalized target family is not equicontinuous despite every member lying in `C_0 cap L_infinity` and despite the uniform height bound (2.1).

A quantitative certificate is available: there are frequencies `tau_m->infinity` such that

\[
|\widehat p_m(\tau_m)|\ge \left(\frac38\right)^3=\frac{27}{512}.
\tag{2.3}
\]

The construction uses only valid independent cap-one marginals and no rotation of independence.

## 3. Phase-aligned unit sets inside a fixed compact interval

For `tau>0` set

\[
D_\tau=\{x\in[1,3]:\cos(\tau x^2)\ge0\}.
\]

We first record a standard periodic averaging fact in the exact form needed here.

### Lemma 3.1 — nonstationary periodic averaging

If `h` is a bounded `2pi`-periodic Riemann-integrable function with mean

\[
\bar h=\frac1{2\pi}\int_0^{2\pi}h(\theta)\,d\theta,
\]

then

\[
\int_1^3 h(\tau x^2)\,dx\longrightarrow 2\bar h
\qquad(\tau\to\infty).
\tag{3.1}
\]

#### Proof

With `u=x^2`,

\[
\int_1^3h(\tau x^2)\,dx
=\int_1^9 h(\tau u)\frac{du}{2\sqrt u}.
\]

For a trigonometric polynomial the zero Fourier mode contributes `2\bar h`; every nonzero mode is `O(1/tau)` after one integration by parts because `u -> (2sqrt u)^{-1}` is `C^1` on `[1,9]`. Approximate a bounded periodic Riemann-integrable `h` from above and below in `L^1` over one period by trigonometric polynomials (or continuous periodic functions followed by Fejer approximation). This gives (3.1). `square`

Apply the lemma to

\[
h_0(\theta)=1_{\{\cos\theta\ge0\}},
\qquad
h_1(\theta)=e^{i\theta}1_{\{\cos\theta\ge0\}}.
\]

Their means are

\[
\bar h_0=\frac12,
\qquad
\bar h_1=
\frac1{2\pi}\int_{-\pi/2}^{\pi/2}e^{i\theta}\,d\theta
=\frac1\pi.
\]

Therefore

\[
|D_\tau|\to1,
\qquad
\int_{D_\tau}e^{i\tau x^2}\,dx\to\frac2\pi.
\tag{3.2}
\]

For all sufficiently large `tau`, modify `D_tau` on a set of measure `||D_tau|-1|` to obtain a measurable `E_tau subset [1,3]` of **exact measure one**. If `|D_tau|>1`, delete an arbitrary subset of the excess mass; if `|D_tau|<1`, add an arbitrary subset of the complement. The oscillatory integral changes by at most the amount of mass changed, hence from (3.2)

\[
\operatorname{Re}\int_{E_\tau}e^{i\tau x^2}\,dx\ge\frac12
\tag{3.3}
\]

for every sufficiently large `tau`.

Thus already the compactly supported cap-one probability density `1_{E_tau}` has a uniformly nonvanishing quadratic Fourier coefficient at the prescribed arbitrarily high frequency.

## 4. Upgrade to strictly positive analytic-Schwartz cap-one marginals

Let `g_sigma` be the centered Gaussian density with variance `sigma^2`, and define

\[
f_{\tau,\sigma}=1_{E_\tau}*g_\sigma.
\]

For every `sigma>0`, this is a strictly positive real-analytic Schwartz probability density. Since convolution by a probability kernel contracts `L^infinity`,

\[
0<f_{\tau,\sigma}\le1.
\tag{4.1}
\]

For each fixed `E_tau`, Gaussian approximate-identity convergence gives

\[
\|f_{\tau,\sigma}-1_{E_\tau}\|_1\to0
\qquad(\sigma\downarrow0).
\]

Choose `sigma_tau<=1` so small that

\[
\|f_{\tau,\sigma_\tau}-1_{E_\tau}\|_1\le\frac18.
\tag{4.2}
\]

Write `f_tau=f_{tau,sigma_tau}`. By (3.3), (4.2), and `|e^{i tau x^2}|=1`,

\[
\left|\int_\mathbb R f_\tau(x)e^{i\tau x^2}\,dx\right|
\ge
\operatorname{Re}\int f_\tau(x)e^{i\tau x^2}\,dx
\ge\frac12-\frac18=\frac38.
\tag{4.3}
\]

Now take `X_1,X_2,X_3` iid with density `f_tau` and `Q_tau=X_1^2+X_2^2+X_3^2`. Independence in the **original coordinates** gives

\[
\phi_{Q_\tau}(\tau)
=\prod_{j=1}^3\int f_\tau(x)e^{i\tau x^2}\,dx,
\]

hence

\[
\boxed{
|\phi_{Q_\tau}(\tau)|\ge\frac{27}{512}.
}
\tag{4.4}
\]

Taking any sequence `tau_m->infinity` proves (2.3).

This construction lies in the same strictly positive analytic-Schwartz cap-one source class appearing in the assigned partner's exact heat-height normal form. The obstruction is therefore not an artifact of rough source boundaries.

## 5. Uniform height bound for this family

For completeness, no matrix-dependent theorem is needed to get a uniform bound for this specific fixed matrix. Let `f_1,f_2,f_3<=1` be any cap-one probability densities and let

\[
Q=X_1^2+X_2^2+X_3^2.
\]

For `0<t<=1`, coarea in spherical coordinates gives

\[
p_Q(t)=\frac{\sqrt t}{2}\int_{S^2}
\prod_{j=1}^3 f_j(\sqrt t\,\omega_j)\,d\sigma(\omega)
\le 2\pi\sqrt t\le2\pi.
\tag{5.1}
\]

For `t>=1`, partition the level sphere into three measurable sectors so that on sector `i`,

\[
|x_i|\ge\sqrt{t/3}.
\]

Fix the other two coordinates. Along the `x_i` line the equation `x_i^2+c=t` has at most two roots, and on the selected sector each root contributes at most `1/(2|x_i|)` to the one-dimensional change-of-variables density. Thus the two roots together contribute at most

\[
\sqrt{\frac3t}.
\]

Integrating the other two product densities (total mass one) and summing the three sectors yields

\[
p_Q(t)\le3\sqrt{\frac3t}\le3\sqrt3<2\pi.
\tag{5.2}
\]

Together with `p_Q(t)=0` for `t<0`, (5.1)-(5.2) prove

\[
\boxed{\|p_Q\|_\infty\le2\pi.}
\tag{5.3}
\]

In particular, the failure of a common modulus below occurs despite a common finite height bound.

## 6. Uniform tightness

The law with density `f_tau=1_{E_tau}*g_{sigma_tau}` can be represented as

\[
X_\tau=U_\tau+\sigma_\tau G,
\]

where `U_tau` has density `1_{E_tau}`, hence `U_tau in [1,3]` almost surely, `G` is standard Gaussian, and `sigma_tau<=1`. Therefore for `R>3`,

\[
\sup_\tau\Pr\{|X_\tau|>R\}
\le \Pr\{|G|>R-3\}\to0.
\tag{6.1}
\]

Consequently

\[
\sup_\tau\Pr\{Q_\tau>3R^2\}
\le3\Pr\{|G|>R-3\}\to0.
\tag{6.2}
\]

So the output laws are uniformly tight. The nondecaying Fourier coefficients in (4.4) cannot be blamed on mass escaping to infinity.

## 7. Common modulus would force uniform Fourier decay

Assume, for contradiction, that a deterministic modulus `omega(r)->0` existed for all the continuous densities `p_tau`:

\[
|p_\tau(t)-p_\tau(s)|\le\omega(|t-s|).
\tag{7.1}
\]

The already completed fixed-rank regularity result gives continuous representatives; in this smooth three-square case continuity also follows directly from the spherical formula. By (5.3) the family is uniformly bounded, and by (7.1) it is equicontinuous on every compact interval.

Fix `eta>0`. Uniform tightness (6.2) gives `R` such that

\[
\sup_\tau\int_{|t|>R}p_\tau(t)\,dt<\eta.
\tag{7.2}
\]

On `[-R,R]`, Arzela-Ascoli makes the restrictions `{p_tau}` relatively compact in the sup norm. Choose a finite `delta`-net `q_1,...,q_N` from their closure. For every `xi`,

\[
\left|\int_{-R}^R e^{i\xi t}(p_\tau(t)-q_j(t))\,dt\right|
\le2R\delta
\tag{7.3}
\]

for a suitable `j`. Each fixed continuous `q_j` is integrable on `[-R,R]`, so Riemann-Lebesgue gives

\[
\int_{-R}^R e^{i\xi t}q_j(t)\,dt\to0
\quad(|\xi|\to\infty).
\]

Because the net is finite, this convergence is uniform in `j`. Combining with (7.2)-(7.3) and then sending `delta,eta` to zero gives

\[
\sup_\tau|\phi_{Q_\tau}(\xi)|\longrightarrow0
\qquad(|\xi|\to\infty).
\tag{7.4}
\]

But (4.4) supplies `xi=tau->infinity` with

\[
|\phi_{Q_\tau}(\tau)|\ge27/512,
\]

a contradiction. This proves Theorem 2.1. `square`

## 8. A sharper local regularity ceiling: the square-root hard edge

There is also a direct local obstruction even without the phase-aligned sequence. Let `f_1,f_2,f_3` be continuous at zero with `f_j(0)>0` and let again `Q=sum X_j^2`. For `t>0`, spherical coarea gives

\[
p_Q(t)
=\frac{\sqrt t}{2}\int_{S^2}
\prod_{j=1}^3 f_j(\sqrt t\,\omega_j)\,d\sigma(\omega).
\tag{8.1}
\]

By dominated convergence on the sphere,

\[
\boxed{
p_Q(t)=2\pi f_1(0)f_2(0)f_3(0)\sqrt t+o(\sqrt t)
\qquad(t\downarrow0).
}
\tag{8.2}
\]

Since `p_Q(t)=0` for `t<0`, the continuous representative satisfies `p_Q(0)=0`. Thus this single target output is not Lipschitz at zero and is not `C^{0,alpha}` there for any `alpha>1/2`. Taking the `f_j` to be any strictly positive analytic-Schwartz cap-one density (for example a Gaussian smoothing of a unit interval) shows that even highly regular sources do not improve the geometric square-root edge.

This local statement is weaker than Theorem 2.1 but identifies `1/2` as an unavoidable hard-edge exponent in rank three.

## 9. Exact implication ledger

The qualitative implications and non-implications remain separated as follows.

1. **Absolute continuity.** Any nonzero quadratic form of an absolutely continuous joint input has an absolutely continuous pushforward; this uses coarea away from the null critical affine space and contains no universal-height information.
2. **Instancewise essential boundedness.** Under the target product hypothesis and rank at least three, every fixed matrix has a finite `L^infinity` density bound, but the known constant may depend on physical-coordinate conditioning of the matrix.
3. **Continuity.** Under the same target hypotheses every fixed output has a `C_0` representative. This is a separate regularity conclusion, not a consequence used to manufacture the universal height.
4. **Uniform essential boundedness across the target class.** This remains open and is exactly `C_*<infinity`.
5. **No quantitative continuity upgrade.** Theorem 2.1 shows that the target class has no common output continuity modulus, even for `A=I_3`, analytic-Schwartz cap-one iid marginals, uniformly tight source laws, and a common finite output-height bound. Therefore target-level `C_0` regularity is qualitatively useful but quantitatively powerless as a uniform local-modulus input.

For comparison outside the rank-three target threshold, absolute continuity does not imply bounded density (`X^2` for `X~Uniform[0,1]`), and bounded density does not imply a continuous representative (`X^2+Y^2` for iid `Uniform[0,1]`, whose density jumps at zero). These controls explain why the three properties must not be conflated.

## 10. Application of the assigned partner result and next step

The assigned completed partner account03/B15 r18 is applied, not merely cited: its exact homogeneous reduction identifies the still-unpaid target as

\[
\boxed{
\sup_{A,f,y}s_3(A)\,\mathbb E\gamma_1(X^TAX-y)<\infty,
}
\tag{10.1}
\]

or equivalently

\[
\boxed{
\sup_{A,f,y}\frac{s_3(A)}2\Pr\{|X^TAX-y|\le1\}<\infty.
}
\tag{10.2}
\]

Moreover the partner permits the source class in (10.1) to be restricted with zero loss to strictly positive analytic-Schwartz cap-one marginals. Theorem 2.1 lives exactly in that smooth source class and rules out an intervening theorem of the form "all normalized outputs share one continuity modulus". Hence the surviving proof route must attack the positive fixed-scale kernel/window quantity (10.1)/(10.2) directly, aggregating original-coordinate product curvature before any reciprocal tiny-minor payment. Continuity should remain a terminal qualitative conclusion, not a surrogate payment for the height.

## 11. Source state and correction discipline

Fresh owner/control source consumed before publication: `yspennstate/math-research-brain@01fc2380364e045d0b692d7754bdfb556fda5f8d`, OWNER CONTROL revision `2026-09-22.15`; QFORM remains the sole target and no account02/B15 stop is present. The live correction inbox was reread at that source. This proof does not use the refuted single-minor, rank-three cross-cut, projection-integrality, arbitrary-joint coarea, positive conditional-height-moment, pointwise per-direction van-der-Corput, raw-normalizer, or rotation-independence shortcuts.

The full QFORM conjecture remains OPEN. This run proves a source-valid counterexample only to a proposed **uniform regularity mechanism**, not to the conjecture itself.
