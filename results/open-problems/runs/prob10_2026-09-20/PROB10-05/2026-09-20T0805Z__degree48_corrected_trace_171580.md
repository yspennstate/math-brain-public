Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. PROB10-05 source-model metric MOVED: the strongest corrected repository bracket `343/2000 < theta_{2,1/4} <= 1/4` (width `157/2000 = 0.0785`) improves to `8579/50000 < theta_{2,1/4} <= 1/4` (width `3921/50000 = 0.07842`).**

# PROB10-05 bounded substantive iteration — degree-48 Ritz + corrected four-trace synthesis

**Status: PARTIAL / source target OPEN / exact synthesis self-check passed / independent validation still required.** The exact exponent at `H=1/4` is not determined, and the full Molchan `theta_{2,H}` problem is much broader. The old formula `theta_{2,H}=H(1-H)` is not a target; its refutation belongs to Molchan.

The new self-certified source-model bound is

\[
\boxed{\theta_{2,1/4}>\frac{8579}{50000}=0.17158},
\qquad
\boxed{W_{1/4}<\frac{3921}{50000}=0.07842}.
\tag{0.1}
\]

The gain over the newest complementary corrected repository bound is

\[
\frac{8579}{50000}-\frac{343}{2000}
=\frac1{12500}=0.00008.
\tag{0.2}
\]

The substantive point is a cross-route spectral synthesis: the canonical PROB10-05 track had a stronger **scale-correct** fourth-trace certificate, while the complementary NM13-09 route had a stronger **degree-48 quasimode** but had conservatively used the older hard-edge trace cap. Combining the two independently derived ingredients yields a strictly stronger Temple enclosure without changing the process, the covariance comparison, or the continuous-time direction.

## 1. Frozen source model and source status

Let `B_H` be centered standard fractional Brownian motion,

\[
\mathbb E B_H(t)B_H(s)
=\frac12\bigl(t^{2H}+s^{2H}-|t-s|^{2H}\bigr),
\]

freeze

\[
H=\frac14,
\qquad
I(t)=I_{1/4}(t)=\int_0^t B_{1/4}(u)\,du,
\tag{1.1}
\]

and keep the continuous fixed-barrier event

\[
p(T)=\Pr\left\{\sup_{0\le t\le T}I(t)\le1\right\}
=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.2}
\]

No sampled-path definition, two-sided interval, or Riemann--Liouville substitute is used.

The current source is G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v11. The repository's source recovery, rechecked in the preceding owning report, identifies Statement 1.2(a): for

\[
\Omega=\{(\alpha,H):\alpha+H>1,\ 0<H<1\},
\tag{1.3}
\]

the persistence exponents of the self-similar process and its Lamperti stationary dual exist and coincide. Thus `(alpha,H)=(2,1/4)` lies in the proved existence regime. The same revision reports that the old general proposal `theta_{2,H}=H(1-H)` is false and leaves the one-sided `alpha=2`, `H\ne1/2` values problematic.

A fresh bounded web/arXiv check in this run re-opened arXiv:2509.10265 and searched later 2026 persistence papers. It recovered Molchan arXiv:2608.26680 (multivariate-time fBM), Aurzada--Muller arXiv:2603.14934 (random Hurst exponent), and Aurzada--Helmer arXiv:2608.17463 (fractional Levy fields on Riemannian index sets). None of the retrieved theorem statements determines the exact continuous one-sided integrated-fBM exponent at `H=1/4`. This is bounded negative evidence only, not a worldwide novelty certificate.

The source-displayed special-point bracket remains

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\tag{1.4}
\]

Therefore the **published-source baseline is unchanged**. Equation (0.1) is repository research on the exact source model and remains PARTIAL pending independent validation.

## 2. Continuity, ownership, and consumed evidence

Canonical ownership is unchanged:

`operations/claims/MOLCHAN-2025-THETA2H.md`, owner `HARD7-05`, blob `40b93171d1258596780a7746de1d96bd028a41d9`.

The PROB10 refocus did not switch HARD7-05 to a different mathematical problem: earlier PROB10 reports record that the actual pre-refocus HARD7-05 target was already this Molchan integrated-fBM persistence problem, with the softened AR-edge comparator, covariance comparison, four-cycle trace analysis, and polynomial quasimodes. No new handoff or ownership transfer is needed here.

This run consumed the current `master` versions of:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md` (no integrated-fBM posting exclusion);
- `operations/claims/MOLCHAN-2025-THETA2H.md`;
- newest canonical-owning report before this run, `runs/prob10_2026-09-20/PROB10-05/2026-09-20T0706Z__circulant_hermite_170000.md`, blob `c9be524a14ff20d700072c03b19ee7197e21a1a8`;
- its corrected trace checker `artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0652Z__circulant_hermite_170000_exact_check.py`, blob `b02178d08eb9b5b4baaf825d7f90a43afb503356`;
- newest complementary persistence report found after the initial idea checkpoint, `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0645Z__degree48_safe_trace_171500.md`;
- its executed exact output `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0645Z__degree48_safe_trace_exact_check.out`, blob `4ba6771727a2b60d92037021b03a338851339940`.

The run first wrote the degree-40 idea checkpoint, before any new checker, at

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0742Z__degree40_ritz_171000_idea.md`

(commit `839be7f2e9d88027a59d1653b293ffd2c52bc108`). During the required newest-neighbor read, the later complementary degree-48 certificate was found. Since that already reached `0.1715`, the planned degree-40 `0.171` certificate was dominated and was not promoted merely to manufacture another checker. Instead the mathematics was redirected to the nonduplicating synthesis below.

## 3. Frozen valid covariance/operator reduction

Retain the unit-variance Lamperti process

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\tag{3.1}
\]

At

\[
r=\frac78,
\qquad
s=\frac{24861}{25000},
\qquad
c=s\frac{1+r}{2}=\frac{74583}{80000},
\tag{3.2}
\]

the earlier exact covariance comparison proves, for every integer `k>=1`,

\[
R(r^k)<cr^{k-1},
\tag{3.3}
\]

where `R` is the covariance of the stationary Lamperti process.

The corresponding compact self-adjoint killed/soft-edge transfer operator on `L^2(phi)` is

\[
(Kf)(x)=\int p_r(x,dy)\,
\Phi\!\left(-\sqrt{\frac{s}{1-s}}
\frac{x+y}{\sqrt{2(1+r)}}\right)f(y),
\tag{3.4}
\]

with Perron eigenvalue `lambda_1>0`.

With

\[
\Delta=4\log(8/7),
\tag{3.5}
\]

the continuous zero-survival event is contained in the grid-survival event. Slepian plus (3.3) therefore gives the source-valid one-way implication

\[
\boxed{
\theta_{2,1/4}\ge
\frac{-\log\lambda_1}{4\log(8/7)}.}
\tag{3.6}
\]

This run never reverses the sampled/continuous inclusion. Hence no discrete-path interpolation assumption enters the new lower bound.

## 4. Three materially different attacks

### Attack A — independent degree-40 Rayleigh--Ritz improvement: mathematically successful but dominated

The first route was to retain the corrected four-trace and lower the quasimode residual by increasing the polynomial space from degree 30 to degree 40. Exact moment recurrences were worked through locally for a Hermite-coordinate trial vector. They gave, before any decision to promote,

\[
\mu\approx0.9121701313701458,
\qquad
\varepsilon^2\approx5.095209372543047\times10^{-5},
\tag{4.1}
\]

which is enough, together with the corrected trace cap, to clear `theta>0.171`.

However, the current-neighbor read then found the already archived degree-48 complementary certificate with `theta>0.1715`. Thus this degree-40 route was no longer source-metric progress. In accordance with the 90/10 rule, I did **not** spend the rest of the run packaging a dominated certificate. The idea checkpoint is preserved, but the source metric is not credited for (4.1).

### Attack B — cross-certificate spectral synthesis: SUCCESS and promoted

The canonical track's newest corrected four-cycle Hermite factorization proves the stronger scale-correct trace bound

\[
\boxed{\operatorname{tr}K^4<\frac{881}{800}=1.10125.}
\tag{4.2}
\]

The complementary degree-48 report, by a separate exact moment calculation, proves for a unit polynomial trial vector `f`

\[
\mu=\langle f,Kf\rangle,
\qquad
\varepsilon^2=\|(K-\mu)f\|_2^2,
\tag{4.3}
\]

with

\[
\boxed{
\frac{9121983}{10^7}<\mu<\frac{91219831}{10^8},
\qquad
\varepsilon^2<\frac{25851}{10^9}.}
\tag{4.4}
\]

That degree-48 report used only the older conservative hard-edge trace cap `553151/500000=1.106302`. Nothing in its quasimode/residual certificate depends on the weaker trace number. Conversely, the corrected trace proof (4.2) is independent of the degree-48 polynomial. Therefore the two certified ingredients may be combined without circularity. Section 5 gives the full new Temple argument.

### Attack C — sixth-trace tail localization: promising but not certified in this run

Temple loses information by bounding the entire non-Perron spectrum from a single fourth moment. A genuinely different route is to derive a scale-correct six-cycle orthant representation and use

\[
\sum_{j\ge2}|\lambda_j|^6
=\operatorname{tr}K^6-\lambda_1^6
\tag{4.5}
\]

to force a smaller tail radius. A private exploratory Gauss--Hermite/Nystrom calculation indicated that the sixth spectral moment should materially tighten the non-Perron separator compared with the fourth moment. I do **not** promote those numbers: they are finite numerical evidence, not an asymptotic theorem or certified trace bound.

The exact obstruction is structural. The four-cycle succeeded because opposite-pair sum/difference coordinates split the corrected circulant covariance into independent Gaussian modes, giving a positive one-dimensional Hermite expansion. For a six-cycle, Fourier diagonalization gives more modes but the six simultaneous half-space constraints do not collapse to a product of two one-dimensional cone factors. A useful next run must either find a positive multivariate Hermite tail certificate for that six-cycle orthant or abandon this trace route; simply evaluating the six-dimensional Gaussian probability numerically would not move the metric.

### Attack D — continuous-time conditional interpolation toward the upper endpoint: obstruction sharpened

The source upper endpoint remains `1/4`. The earlier exact local estimate

\[
\Pr\{X(0)\le-\eta,\ \sup_{0\le t\le\delta}X(t)>0\}
\le \frac{15\delta^2}{16\eta^2}
\tag{4.6}
\]

is unconditional. Summed over `n` intervals it gives only a polynomial/additive control, whereas persistence over Lamperti time `n\delta` is exponentially small in `n`. Thus (4.6) cannot provide a reverse continuous/grid exponent comparison.

The sharper operator formulation is: one would need an **exponentially compatible relative bridge estimate**, not a modulus estimate. In a Markov setting this would amount to comparing the one-step grid-killed kernel with the one-step continuously-killed kernel and proving that the spectral-radius loss tends to zero as `delta->0`. Here the actual Lamperti process is non-Markov in its one-dimensional state, so a proof must either use a Gaussian-history state or a covariance comparison that controls bridge crossings conditioned on long survival. This identifies the missing object precisely and explains why a discrete path checker cannot improve the source upper endpoint by itself.

## 5. Full new proof of `theta_{2,1/4}>8579/50000`

Let the spectrum of the compact self-adjoint operator `K` be

\[
\lambda_1,\lambda_2,\ldots,
\]

with `lambda_1>0` its Perron eigenvalue. By (4.2),

\[
\sum_j |\lambda_j|^4
=\operatorname{tr}K^4
<\frac{881}{800}.
\tag{5.1}
\]

Fix the exact rationals

\[
\theta_*:=\frac{8579}{50000}=0.17158,
\qquad
x:=\frac{228107}{250000}=0.912428,
\qquad
\beta:=\frac{799297}{10^6}=0.799297.
\tag{5.2}
\]

The synthesis checker proves the integer-power comparison

\[
x^{12500}<r^{8579}.
\tag{5.3}
\]

Since `r=7/8<1`, this is exactly

\[
x<r^{8579/12500}=r^{4\theta_*}.
\tag{5.4}
\]

Assume for contradiction that

\[
\lambda_1\ge r^{4\theta_*}>x.
\tag{5.5}
\]

Then (5.1) gives

\[
\sum_{j\ge2}|\lambda_j|^4
<\frac{881}{800}-x^4.
\tag{5.6}
\]

The exact checker proves

\[
\beta^4-\left(\frac{881}{800}-x^4\right)
=
\frac{9787150171847809537}{10^{24}}>0.
\tag{5.7}
\]

Therefore every non-Perron spectral value satisfies

\[
|\lambda_j|<\beta,
\qquad j\ge2.
\tag{5.8}
\]

The degree-48 lower Rayleigh bound in (4.4) satisfies

\[
\mu>\frac{9121983}{10^7}>\beta.
\tag{5.9}
\]

For the spectral measure `nu_f` of the unit trial vector `f`, the mean is `mu` and the variance is `epsilon^2`. Under (5.5), the spectral support is contained in

\[
(-\infty,\beta]\cup[\lambda_1,\infty),
\qquad \beta<\mu<\lambda_1.
\]

The spectral-measure form of Temple's inequality therefore gives

\[
\varepsilon^2\ge(\lambda_1-\mu)(\mu-\beta).
\tag{5.10}
\]

For completeness, this is the elementary variance bound obtained by minimizing `int (lambda-mu)^2 dnu(lambda)` over probability measures of mean `mu` whose support lies outside `(beta,lambda_1)`: the minimizer is the two-point distribution at the boundary points and has variance `(lambda_1-mu)(mu-beta)`.

Using (5.5) and the outward bounds (4.4),

\[
\varepsilon^2
>
\left(x-\frac{91219831}{10^8}\right)
\left(\frac{9121983}{10^7}-\beta\right).
\tag{5.11}
\]

The exact value of the right-hand side is

\[
\frac{25932299597}{10^{15}}
=2.5932299597\times10^{-5}.
\tag{5.12}
\]

But (4.4) gives

\[
\varepsilon^2<\frac{25851}{10^9}
=2.5851\times10^{-5}.
\tag{5.13}
\]

The strict contradiction margin is

\[
\frac{25932299597}{10^{15}}-
\frac{25851}{10^9}
=
\boxed{\frac{81299597}{10^{15}}}>0.
\tag{5.14}
\]

Hence assumption (5.5) is impossible and

\[
\lambda_1<r^{4\theta_*}.
\tag{5.15}
\]

Substitute (5.15) into the already proved continuous source bound (3.6):

\[
\theta_{2,1/4}
\ge\frac{-\log\lambda_1}{4\log(8/7)}
>\theta_*
=\boxed{\frac{8579}{50000}}.
\tag{5.16}
\]

This completes the new mathematical step. No finite-size persistence simulation, no reverse sampled-to-continuous assertion, and no obsolete formula `H(1-H)` is used.

## 6. Before/after source metric and mechanism progress

### Published external baseline

Unchanged:

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\tag{6.1}
\]

The exact value is still UNKNOWN.

### Strongest corrected repository source-model bound at run start

After reading the concurrent/complementary degree-48 report, the real incoming best was not the canonical track's `0.17`, but

\[
\frac{343}{2000}<\theta_{2,1/4}\le\frac14,
\qquad
W_{1/4}=\frac{157}{2000}=0.0785.
\tag{6.2}
\]

### After this run

\[
\boxed{
\frac{8579}{50000}<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W_{1/4}=\frac{3921}{50000}=0.07842}.
\tag{6.3}
\]

Thus the rigorous repository lower endpoint moves by `1/12500=0.00008`, and the gap shrinks by the same amount.

### Auxiliary mechanism progress

1. The run identified that the degree-48 quasimode and the corrected Hermite four-trace certificate are logically independent and composable; this removes unnecessary conservatism in the complementary proof.
2. The planned degree-40 route was correctly abandoned after the current-neighbor read showed it was dominated, avoiding certificate-only work.
3. The next spectral target is now sharply identified: a scale-correct `tr K^6` certificate could reduce the Temple tail separator materially, but requires a new six-cycle orthant factorization rather than numerical integration.
4. The upper-endpoint obstruction is formulated at the correct exponential/operator level: one needs conditional continuous bridge control compatible with persistence spectral radii, not an unconditional modulus estimate.

## 7. Actual tests and artifacts

The new exact synthesis checker is

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0750Z__degree48_plus_corrected_trace_171580_exact_check.py`

created at commit `fd59226aa09e627416414f3b6c85ad41a156397d`.

It checks with exact `Fraction`/integer arithmetic:

- `x^12500 < r^8579`;
- the fourth-trace tail inequality (5.7);
- `beta < mu_lower` and `x > mu_upper`;
- the Temple contradiction (5.14);
- the before/after width calculation.

The checker was executed successfully. The authoritative archived rerun output is

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0750Z__degree48_plus_corrected_trace_171580_exact_check.rerun.out`

at commit `f42ebe0ff6b4b430856a16dd6264138659637e52`; it ends

`ALL_EXACT_CHECKS_PASS = True`.

An earlier `.out` file created in this run transcribed the **decimal-correct** tail margin with a rounded rational numerator/denominator rather than Python's exact reduced `Fraction`. It is not used as evidence. The rerun output above records the exact fraction `9787150171847809537/10^24` and is the controlling output artifact. The mathematical inequalities and promoted endpoint were unchanged by this archival correction.

The degree-48 input certificate itself was independently executed by its originating complementary track; its current archived output has `PROCESS_RETURN_CODE = 0`, reports

`mu interval = (0.9121983078586597, 0.9121983078586597)`

and

`eps2 interval = (2.5850637468877914e-05, 2.5850637468877914e-05)`,

and ends `ALL_EXACT_CHECKS_PASS = True`. This is still a repository self-check, not one of the two independent closure audits required by policy.

## 8. Remaining full-scope gap

The source problem remains OPEN. Even at `H=1/4`, the bracket width is still `0.07842`; the upper endpoint `1/4` has not moved. The full family `theta_{2,H}` for `H\ne1/2` is much broader.

For the lower endpoint, the immediate nonexhausted mathematical routes are: a true six-cycle/higher-trace certificate, a still-lower-residual quasimode combined with the corrected trace, or a positive-operator supersolution giving a direct Perron upper bound without Temple. For the upper endpoint, the missing theorem is an exponentially compatible continuous bridge/interpolation comparison; discrete sampling alone cannot supply it.

No scheduler, cadence, enabled state, email, Drive, public posting, permissions, or unrelated claim ownership was changed in this run.