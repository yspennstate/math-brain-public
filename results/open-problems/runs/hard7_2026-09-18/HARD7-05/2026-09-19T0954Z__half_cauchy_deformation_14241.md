Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 2153/20000 = 0.10765 -> 10759/100000 = 0.10759`; methods B6 / B9 / B17.**

# HARD7-05 bounded research iteration — half-Cauchy deformation and a sharper certified six-cycle endpoint

Status: **PARTIAL / source target OPEN.** This run proves the source-valid continuous-time bound

\[
\boxed{\theta_{2,1/4}\ge \frac{14241}{100000}=0.14241,}
\tag{0.1}
\]

improving the preceding certified endpoint `2847/20000=0.14235`. Hence

\[
\boxed{\frac{14241}{100000}\le \theta_{2,1/4}\le\frac14},\qquad
\boxed{W_{1/4}=\frac{10759}{100000}=0.10759.}
\tag{0.2}
\]

The main research work in this run is not another checker parameter sweep: it finds a second, Pólya-free representation of the Gaussian tail as a random-rate exponential mixture, identifies a monotone finite-mixture hierarchy preserving the Gaussian quadratic-tilt structure, and uses that independent language to diagnose where the present comparison loses. The final exact certificate is then a small boundary refinement of the already established six-cycle architecture.

## 1. Continuity, ownership, fleet state, and current-source refresh

I resumed the existing exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`. I did not restart admission, mint an alias, overwrite a claim, update shared root ledgers, or touch another track's files.

At run start I reread the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the canonical claim; the indexed HARD7-05 chain through `2026-09-19T0838Z__optimized_grid_polya12_14235.md`; the newest visible neighboring HARD7-04/HARD7-06 reports; and repository/intake searches for Molchan, `theta_{2,H}`, integrated-fBM persistence aliases, and the source arXiv id. No ownership collision or posted equivalent was found.

Fresh literature search dated **2026-09-19** checked the exact source title/arXiv id, `theta_{2,H}`, `integrated fractional Brownian persistence H=1/4`, and recent follow-ups. The primary source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, whose current abstract still treats the `e(2,H)` values as the problematic exponents and refutes the former `H(1-H)` formula rather than solving them. The search also recovered Aurzada--Kilian, arXiv:2007.01254, and adjacent persistence literature, but no later exact determination or stronger source-matching `H=1/4` bound. This is bounded negative evidence only, **not** certification of worldwide novelty.

The frozen source metric entering this run is the verified bracket

\[
\frac{2847}{20000}\le\theta_{2,1/4}\le\frac14,
\qquad W_{1/4}=\frac{2153}{20000}.
\tag{1.1}
\]

## 2. The three new Section-B moves

The previous run used B5/B18/B24. This run deliberately changes category of attack and uses three methods not previously used on this target.

- **B9 — RANDOMIZE: SUCCESS.** Craig's Gaussian-tail integral is exactly a half-Cauchy random-rate Laplace transform. This turns the deterministic tail approximation problem into approximation of a one-dimensional mixing law.
- **B6 — DEFORM TO A SOLVABLE POINT: SUCCESS STRUCTURALLY.** Truncating and atomizing that half-Cauchy law gives a monotone hierarchy of positive exponential minorants. Every atom remains exactly compatible with the existing Gaussian quadratic-tilt evaluation, so the deformation does not destroy computability.
- **B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: SUCCESS AS A DIAGNOSTIC.** The tangent/Craig parametrization reveals that the relevant rates are `beta=(1+t^2)/2` under half-Cauchy measure. Exploratory, explicitly non-certifying quadrature showed that coarse atomizations lose too much mass, while finer nonuniform atomizations become competitive with the Catalan/Pólya hierarchy. The obstruction is therefore quadrature sharpness, not incompatibility with the killed-operator trace.

Counterexample-first aspect: I first tried to falsify the implicit working premise that the Pólya/Catalan expansion was essential to the six-cycle route. The exact identity below disproves that premise. I then tried to falsify the stronger hope that a coarse Craig discretization would automatically improve the certified endpoint; exploratory probes did not support that stronger hope. No numerical probe is used as a theorem or as movement of the source metric.

## 3. B9: exact half-Cauchy representation of the Gaussian tail

For `u>=0`, Craig's representation is

\[
\bar\Phi(u):=1-\Phi(u)
=\frac1\pi\int_0^{\pi/2}
\exp\!\left(-\frac{u^2}{2\sin^2\vartheta}\right)d\vartheta.
\tag{3.1}
\]

Set `t=cot(vartheta)`. Since `d vartheta=-dt/(1+t^2)` and `sin^{-2}(vartheta)=1+t^2`, this becomes

\[
\bar\Phi(u)
=\frac1\pi\int_0^\infty
\frac{\exp[-(1+t^2)u^2/2]}{1+t^2}\,dt.
\tag{3.2}
\]

If `T` is standard half-Cauchy,

\[
\Pr(T\in dt)=\frac{2}{\pi(1+t^2)}1_{\{t\ge0\}}dt,
\tag{3.3}
\]

then the exact identity is

\[
\boxed{
\bar\Phi(u)=\frac12\,\mathbb E
\exp\!\left[-\frac{1+T^2}{2}u^2\right].
}
\tag{3.4}
\]

Thus the Gaussian tail is not merely bounded by Gaussian exponentials: it is exactly a positive mixture of them. This is the independent language sought in the preceding checkpoint.

## 4. B6: a monotone finite-mixture hierarchy

Fix a finite partition

\[
0=b_0<b_1<\cdots<b_M=B.
\]

The exponential factor in (3.2) decreases with `t`, so interval by interval,

\[
\frac1\pi\int_{b_{j-1}}^{b_j}
\frac{e^{-(1+t^2)u^2/2}}{1+t^2}\,dt
\ge
w_j e^{-\beta_j u^2},
\tag{4.1}
\]

where

\[
w_j=\frac{\arctan b_j-\arctan b_{j-1}}\pi,
\qquad
\beta_j=\frac{1+b_j^2}{2}.
\tag{4.2}
\]

Consequently

\[
\boxed{
\bar\Phi(u)\ge \sum_{j=1}^M w_j e^{-\beta_j u^2}
}
\qquad(u\ge0).
\tag{4.3}
\]

Refining the partition can only improve the lower sum: when one interval is split, the left subinterval receives a smaller right endpoint and hence a larger exponential factor, while the right subinterval retains the old endpoint. Increasing `B` adds a positive term. Therefore nested refinements with mesh tending to zero and `B\to\infty` converge monotonically to the exact Craig integral (3.2).

This matters for the six-cycle trace. If

\[
g(u)=\sum_j w_j e^{-\beta_j u^2}\le\bar\Phi(u),
\]

then

\[
\Phi(u)\le1-g(u).
\tag{4.4}
\]

After conditioning on the three even sites of the AR(1) six-cycle, expanding the product of the three factors in (4.4) again leaves finite sums of terms

\[
\mathbb E\left[1_{\{Y>0\}}e^{-Y^T A Y}\right]
=\det(I+2CA)^{-1/2}\Pr\{Z_A>0\},
\tag{4.5}
\]

and the last probability is still the centered trivariate Gaussian orthant formula. Thus Craig atomization is a **Pólya-free exact hierarchy in the same computational category**, not a simulation or a discretization of sample paths.

The remaining bookkeeping issue is only certification of the `arctan` weights in (4.2). That is a one-dimensional transcendental interval problem, not a new Gaussian orthant problem. I did not spend this run manufacturing a large quadrature certificate before the route had been mathematically identified.

## 5. B17 diagnosis: where the current comparison can still move

Equation (3.4) says the exponential rate is

\[
\beta(T)=\frac{1+T^2}{2},
\tag{5.1}
\]

with half-Cauchy mixing. This exposes two distinct sources of loss that the single-rate Pólya inequality merges:

1. **rate homogenization loss** — replacing all `beta(T)` by one global rate;
2. **mixing-law discretization loss** — replacing the half-Cauchy continuum by finitely many atoms.

The first loss can now be attacked independently of the second. In particular, the finite atomization retains positive coefficients, so there is no alternating-sign instability analogous to taking a very long Catalan truncation. The natural next proof object is therefore an interval-certified nonuniform half-Cauchy quadrature, optimized for the range of `u` weighted by the three-dimensional tilted Gaussian law.

This is the substantive new route from the run. The exact source-metric improvement below is deliberately kept small and fully certified rather than inferred from exploratory quadrature.

## 6. Exact metric movement: push the covariance grid to `r=287831/500000`

The preceding checkpoint proved the exact covariance reduction. I use it rather than rederive it. For the stationary Lamperti process at `H=1/4`, with `q=e^{-t/4}` and `z=q^2`,

\[
R_X(t)-q=\frac{1-q^2}{6q^5}F(q),
\tag{6.1}
\]

where

\[
F(q)=-P(z)+2(1+z)(1-z^2)^{3/2},
\tag{6.2}
\]
\[
P(z)=2+2z-3z^2-2z^3-2z^4,
\tag{6.3}
\]

and

\[
P(z)^2-4(1+z)^2(1-z^2)^3=z^3Q(z),
\tag{6.4}
\]
\[
Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4.
\tag{6.5}
\]

Choose the sharper rational

\[
\boxed{r=\frac{287831}{500000}=0.575662},
\qquad \Delta=4\log(1/r).
\tag{6.6}
\]

Set `z_0=r^2`. The exact checker verifies

\[
2-3z_0^2-2z_0^3-2z_0^4>0,
\tag{6.7}
\]

so `P(z)>0` for `0<=z<=z_0`, and

\[
40z_0^4+64z_0^3+24z_0^2-7<0.
\tag{6.8}
\]

Since

\[
Q'(z)=40z^4+64z^3+24z^2-40z-7,
\]

(6.8) implies `Q'<0` throughout `[0,z_0]`. The checker also verifies exactly `Q(z_0)>0`. Hence `Q(z)>0` on that whole interval, so (6.4) and positivity imply `F(q)<0` for `0<q<=r`. Therefore

\[
R_X(k\Delta)\le r^k\qquad(k\ge1).
\tag{6.9}
\]

Slepian comparison with stationary Gaussian AR(1) of correlation `r^{|i-j|}` is thus valid at every grid separation. Continuous persistence implies the sampled event, so this direction requires no discrete-to-continuous interpolation or modulus estimate.

## 7. Exact six-cycle certificate at Catalan depth 13

Let `K=1_{(0,\infty)}P_r1_{(0,\infty)}` be the killed AR(1) operator. The preceding derivation gives

\[
\|K\|^6\le \operatorname{tr}K^6=\frac{P_6}{1-r^6}.
\tag{7.1}
\]

For the final finite certificate I keep the already proved Pólya inequality and use

\[
\beta=\frac{191}{300}>\frac2\pi,
\tag{7.2}
\]

with Catalan depth `m=13`. Conditioning on even sites reduces all `14^3=2744` expanded terms, or `560` sorted symmetry classes, to exact quadratic Gaussian tilts. Rational matrix arithmetic, integer square-root enclosures, positive arcsine Taylor bounds with an exact geometric remainder, and

\[
\frac{333}{106}<\pi<\frac{355}{113}
\]

produce the certified inequality

\[
\boxed{
\operatorname{tr}K^6<\frac{3029}{20000}=0.15145.
}
\tag{7.3}
\]

The exact power comparison in the checker is

\[
\left(\frac{3029}{20000}\right)^{12500}
<
\left(\frac{287831}{500000}\right)^{42723}.
\tag{7.4}
\]

Since

\[
24\cdot\frac{14241}{100000}=\frac{42723}{12500},
\]

(7.4) is precisely

\[
\frac{-\log(3029/20000)}{24\log(1/r)}
>\frac{14241}{100000}.
\tag{7.5}
\]

Combining (6.9), Slepian, the killed-operator bound and (7.5) proves (0.1). The displayed floating-point values in the artifact are diagnostics only; every decisive inequality used for the certificate is exact integer/rational arithmetic with rigorous algebraic/transcendental enclosures.

Executed artifacts:

- `artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0954Z__half_cauchy_polya13_exact_check.py`
- `artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0954Z__half_cauchy_polya13_exact_check.out`

The archived output ends `ALL_EXACT_CHECKS_PASS = True`.

## 8. Honest status and next obstruction

The source problem remains **OPEN** and this run remains **PARTIAL**. The certified special-point bracket is now

\[
\frac{14241}{100000}\le\theta_{2,1/4}\le\frac14.
\]

The metric moved, so Section I is not triggered and the unchanged counter resets. The cleanest next mathematical obstruction is no longer the existence of an alternative tail representation: (3.4) settles that. It is to obtain a sufficiently sharp **rigorous finite minorant of the half-Cauchy mixing measure** whose resulting six-cycle trace can be compared exactly with the Catalan certificate. A second genuinely different direction is an eight-cycle trace, whose new obstacle is a four-dimensional tilted orthant probability.

## 9. Scheduler/model capability statement

The currently exposed scheduler interface still provides prompt/title/schedule/timing-mode/enablement controls but **no model selector, no reasoning-effort selector, and no guaranteed run duration**. Therefore GPT-6 maximum remains a prompt request only. This run's actual model is GPT-5.6 Sol; reasoning telemetry is unavailable and is reported as UNVERIFIED. Changing the actual scheduler-selected model/reasoning would require the platform/native scheduler to expose and authorize those fields; a repository edit or prompt assertion cannot do it.

The historical P26 `You cannot modify this task` event was an authorization-context failure. Current root `RESULTS.md` records that a later authorized context successfully updated P26, so the earlier denial is not evidence that P26 is permanently immutable. For any future denied scheduler edit, the lawful workaround is the owning/authorized task context or authorized platform/admin support, not a duplicate schedule or a permission bypass.

## ledger_delta

`HARD7-05 | Molchan 2025 theta_{2,H}; fixed metric W_{1/4} | 2153/20000 -> 10759/100000 | PARTIAL / source OPEN | certified theta_{2,1/4} >= 14241/100000; new exact half-Cauchy Craig-mixture hierarchy recorded`.
