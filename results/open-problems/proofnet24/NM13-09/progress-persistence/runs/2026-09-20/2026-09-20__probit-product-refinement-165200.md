Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. T05 source metric MOVED: `16517/100000 < theta_{2,1/4} <= 1/4` (width `8483/100000`) -> `413/2500 < theta_{2,1/4} <= 1/4` (width `53/625`); mechanism gain: fourth-trace cap `1.092044 -> 1.09116`, with exact zero-loss continuum-to-grid inclusion in the lower-bound direction.**

# NM13-09 T05 progress — sharpened probit-product envelope gives `theta_{2,1/4}>0.1652`

**Status: PARTIAL / CANDIDATE source-level improvement pending later independent review.** The exact exponent remains open. This run proves, conditional only on the already archived and exactly certified degree-18 quasimode bounds at the same comparator parameters,

\[
\boxed{\theta_{2,1/4}>\frac{413}{2500}=0.1652.}
\tag{0.1}
\]

Together with the retained source-valid upper bound `theta_{2,1/4}<=1/4`, this gives

\[
\boxed{\frac{413}{2500}<\theta_{2,1/4}\le\frac14},\qquad
\boxed{W_{1/4}=\frac{53}{625}=0.0848}.
\tag{0.2}
\]

The incoming current-master bound from the newest PROB10-05 continuation was

\[
\frac{16517}{100000}<\theta_{2,1/4}\le\frac14,
\qquad W_{1/4}=\frac{8483}{100000}=0.08483,
\tag{0.3}
\]

so the source-level lower endpoint increases by `3/100000` and the width decreases by the same amount.

## 1. Handoff, ownership, and current baseline

The previous native NM13-09 history ended in an admission-only loop with no admitted source and no mathematical metric. The later controlling policy `operations/PROGRESS20_2026-09-20.md` supersedes that intake-only behavior and assigns LIVE20 slot NM09 to T05, with report root `proofnet24/NM13-09/progress-persistence` and mandate to do covariance/comparison research on continuous integrated-fBM persistence.

I preserved that prior state rather than relabeling its screenings as progress. Canonical parent ownership is also preserved: `operations/claims/MOLCHAN-2025-THETA2H.md` remains owned by HARD7-05 / its PROB10-05 continuation. This NM09 run is a complementary LIVE20 derivation, not an ownership transfer and not a duplicate claim.

A critical current-master read found a newer PROB10-05 report, `runs/prob10_2026-09-20/PROB10-05/2026-09-20T0010Z__equicorrelation_probit_16517.md`, which had already improved the recovered fleet lower endpoint from `0.1648` to `0.16517`. An initial HGR/canonical-correlation trace route developed before that read only supported `0.16483`; once the stronger current baseline was recovered, that route was immediately abandoned as source-level nonprogress. Its checker/output remain immutable failed-route evidence under this run directory. The successful route below materially changes the inequality used inside the equicorrelation/probit argument and clears `0.16517`.

## 2. Exact source model, event, normalization, and exponent existence

Let `B_H` be centered standard fractional Brownian motion,

\[
\mathbb E[B_H(t)B_H(s)]
=\frac12\left(t^{2H}+s^{2H}-|t-s|^{2H}\right),
\]

and freeze `H=1/4` and

\[
I(t)=I_{1/4}(t)=\int_0^t B_{1/4}(u)\,du.
\tag{2.1}
\]

The source event is the continuous one-sided fixed-level event

\[
p(T)=\Pr\{I(t)\le 1\text{ for every }0\le t\le T\},
\qquad
p(T)=T^{-\theta_{2,1/4}+o(1)}.
\tag{2.2}
\]

This is not a discrete-grid definition. No sampled-path numerical estimate is used as a persistence exponent.

Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, current v11 as recorded by the project (revised 4 July 2026), explicitly treats the `alpha=2, H!=1/2` one-sided exponents as unsolved, and the current revision refutes the old candidate formula `theta_{2,H}=H(1-H)`. This run does not assume or attempt to prove that obsolete formula.

Molchan's Statement 1.2(a) states that throughout `Omega={alpha+H>1, 0<H<1}` the persistence exponents of the self-similar process and its Lamperti-dual stationary process exist and are identical. Since `(alpha,H)=(2,1/4)` lies in `Omega`, exponent existence needed for (2.2) is therefore already supplied by the source; it is not a new claim of this run.

The displayed source bound (3) gives at `H=1/4`

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\tag{2.3}
\]

That is the external-source literature baseline. The stronger incoming `0.16517` lower endpoint is repository progress beyond (2.3), not a claim that Molchan printed it.

## 3. Lamperti covariance and an exact all-lag comparator

At `H=1/4`, `Var(I(1))=2/5` and the self-similarity index is `5/4`. Normalize the stationary Lamperti process by

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\tag{3.1}
\]

For `u=e^{-|\tau|/4}` its covariance is

\[
R(u)=
\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5},
\qquad 0<u\le1.
\tag{3.2}
\]

Equivalently, with

\[
P(z)=2+2z-3z^2-2z^3-2z^4,
\]

\[
R(u)-u
=\frac{1-u^2}{6u^5}
\left[-P(u^2)+2(1+u^2)(1-u^4)^{3/2}\right].
\tag{3.3}
\]

Use the current comparator parameters

\[
r=\frac78,\qquad s=\frac{24861}{25000},\qquad
c=s\frac{1+r}{2}=\frac{74583}{80000}.
\tag{3.4}
\]

Let `(U_j)` be stationary standard Gaussian AR(1) with correlation `r`, let `(E_j)` be iid standard Gaussian independent of `U`, and put

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},
\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j.
\tag{3.5}
\]

Then

\[
\operatorname{Cov}(Z_0,Z_k)=c r^{k-1}\qquad(k\ge1).
\tag{3.6}
\]

### Proposition 3.1 — all-lag source covariance domination

For every integer `k>=1`,

\[
\boxed{R(r^k)<c r^{k-1}.}
\tag{3.7}
\]

**Proof.** For `k=1,...,5`, set `u=r^k`, `b_k=c r^{k-1}`, `z=u^2`, and

\[
T=P(z)+\frac{6u^5(b_k-u)}{1-u^2}.
\]

Isolating the radical in (3.3) shows that `R(u)<b_k` follows from `T>0` and

\[
T^2>4(1+z)^2(1-z^2)^3.
\tag{3.8}
\]

The exact checker executes these rational inequalities for all five lags. The squared margins are strictly positive; their floating displays are

`0.0001416572, 0.0227285119, 0.1165539078, 0.1012524720, 0.0625352794`.

For `k>=6`, `u<=r^6<1/2`, hence `z=u^2<=1/4`. Direct factorization gives

\[
P(z)^2-4(1+z)^2(1-z^2)^3
=z^3 Q(z),
\]

\[
Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4.
\tag{3.9}
\]

On `0<=z<=1/4`,

\[
Q(z)\ge 4-7z-20z^2\ge1,
\]

and `P(z)>0`. Thus

\[
P(z)\ge2(1+z)(1-z^2)^{3/2},
\]

so (3.3) gives `R(u)<=u`. Finally

\[
\frac{c}{r}=\frac{74583}{70000}>1,
\]

hence `u=r^k<c r^{k-1}`. This proves (3.7). `QED`

## 4. Continuous-time control: the interpolation loss is exactly zero in this direction

Let

\[
\Delta=-4\log r=4\log\frac87.
\tag{4.1}
\]

Molchan's source theorem identifies the exponent in (2.2) with the zero-level persistence exponent of the stationary Lamperti dual `X`. Therefore, for `L=n\Delta`, define

\[
A_L=\{X(t)<0\ \forall 0\le t\le L\},
\qquad
G_n=\{X(j\Delta)<0\ \forall j=1,\ldots,n\}.
\]

There is the deterministic inclusion

\[
A_{n\Delta}\subseteq G_n.
\tag{4.2}
\]

Thus the continuum-to-grid error for the **lower-bound-on-the-exponent direction used here is exactly zero**: no modulus estimate, missed-crossing probability, or discrete-path numerical extrapolation is needed.

By (3.7), the sampled covariance of `Z` dominates that of `X` at every nonzero lag. Slepian's inequality at the common zero threshold gives

\[
\Pr(A_{n\Delta})
\le \Pr(G_n)
\le \Pr(Z_1<0,\ldots,Z_n<0).
\tag{4.3}
\]

This is the required covariance/comparison bridge from the exact continuous source event to the tractable comparator. A reverse grid-to-continuum implication, which would be needed for a new upper bound on `theta`, would require a genuine interpolation/modulus estimate and is **not** claimed here.

## 5. The inherited transfer operator and exact quasimode input

The softened AR-edge construction has a self-adjoint killed transfer operator `K=K_{r,s}` on `L^2(phi)` with Perron eigenvalue `lambda_1`, and

\[
\Pr(Z_1<0,\ldots,Z_n<0)
=\langle 1,K^n1\rangle
\le \lambda_1^n.
\tag{5.1}
\]

Combining (4.3) with exponent existence gives

\[
\theta_{2,1/4}
\ge \frac{-\log\lambda_1}{4\log(8/7)}.
\tag{5.2}
\]

The current exact degree-18 trial-vector certificate at the same `(r,s)` was recovered from

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2140Z__softening_frontier_exact_check.py`

and its archived output. For normalized `f`, with

\[
\mu=\langle f,Kf\rangle,
\qquad
\varepsilon^2=\|(K-\mu)f\|_2^2,
\]

it certifies

\[
\frac{9116948312}{10^{10}}<\mu<\frac{9116948313}{10^{10}},
\qquad
\varepsilon^2<\frac{47004495}{10^{11}}.
\tag{5.3}
\]

This run does not relabel those inherited values as new progress. Its new exact checker consumes only the rational bounds (5.3), while independently recomputing the covariance and trace quantities used below.

## 6. New comparison lemma: a sharpened probit product bound

The newest PROB10-05 argument dominates the softened cyclic four-cycle by an equicorrelated Gaussian vector with off-diagonal correlation

\[
\rho=\rho_{\rm adj}
=\frac{168557580}{170952323},
\tag{6.1}
\]

while the opposite correlation is smaller,

\[
\rho_{\rm opp}=\frac{167065920}{170952323}<\rho.
\tag{6.2}
\]

For the equicorrelated vector use the one-factor representation

\[
G_i=\sqrt\rho\,Z+\sqrt{1-\rho}\,E_i,
\]

with independent standard normals. Put

\[
C=\sqrt{\frac{\rho}{1-\rho}},
\qquad U=\Phi(-CZ),
\qquad Q=U(1-U).
\]

Then the four-orthant probability is `M_4=E[U^4]` and the symmetry `U law=1-U` gives

\[
M_4=\frac{\arcsin\rho}{\pi}+\mathbb E Q^2.
\tag{6.3}
\]

The preceding PROB10-05 run used

\[
\Phi(x)\Phi(-x)\le\frac14 e^{-x^2/2}.
\]

The following strict refinement is the new analytic mechanism.

### Lemma 6.1
For every real `x`,

\[
\boxed{
\Phi(x)\Phi(-x)
\le
\frac{e^{-x^2/2}}{4\sqrt{1+x^2/5}}.
}
\tag{6.4}
\]

**Proof.** By symmetry assume `x>=0` and put `y=x/sqrt(2)`, `a=2/5`. Since

\[
4\Phi(x)\Phi(-x)=1-\operatorname{erf}(y)^2,
\]

(6.4) is equivalent to `F(y)>=0`, where

\[
F(y)=\operatorname{erf}(y)^2+rac{e^{-y^2}}{\sqrt{1+ay^2}}-1.
\tag{6.5}
\]

Differentiation gives

\[
F'(y)=e^{-y^2}g(y),
\]

\[
g(y)=\frac4{\sqrt\pi}\operatorname{erf}(y)-A(y),
\qquad
A(y)=\frac{y[(2+a)+2ay^2]}{(1+ay^2)^{3/2}}.
\tag{6.6}
\]

For `a=2/5`,

\[
A'(y)=\frac{12\sqrt5\,(y^2+5)}{(2y^2+5)^{5/2}}.
\tag{6.7}
\]

Let `H(y)=e^{y^2}A'(y)`. A second differentiation gives

\[
H'(y)=e^{y^2}y\,
\frac{24\sqrt5\,(2y^4+12y^2+5)}{(2y^2+5)^{7/2}}>0
\qquad(y>0).
\tag{6.8}
\]

Hence `H` is strictly increasing, with `H(0)=12/5<8/pi` and `H(y)->infinity`. Since

\[
g'(y)=e^{-y^2}\left(\frac8\pi-H(y)\right),
\tag{6.9}
\]

`g` first increases and then strictly decreases. Also `g(0)=0` and

\[
\lim_{y\to\infty}g(y)=\frac4{\sqrt\pi}-\sqrt{10}<0.
\]

Thus `g` has exactly one positive zero. Consequently `F` first increases and then decreases. Finally `F(0)=0` and `F(y)->0` as `y->infinity`; therefore `F(y)>=0` for all `y>=0`. This proves (6.4). `QED`

## 7. Improved four-cycle trace bound

Apply Lemma 6.1 with `x=CZ` and square it:

\[
Q^2\le
\frac1{16}\frac{e^{-C^2Z^2}}{1+C^2Z^2/5}.
\tag{7.1}
\]

For every `y>=0`,

\[
\frac1{1+y}\le1-y+y^2
\tag{7.2}
\]

because the difference is `y^3/(1+y)`. Let

\[
A=1+2C^2=\frac{1+\rho}{1-\rho},
\qquad d=\frac{C^2}{5},
\qquad q=\frac dA=\frac{\rho}{5(1+\rho)}.
\]

Using the exact Gaussian identities

\[
\mathbb E e^{-C^2Z^2}=A^{-1/2},\quad
\mathbb E Z^2e^{-C^2Z^2}=A^{-3/2},\quad
\mathbb E Z^4e^{-C^2Z^2}=3A^{-5/2},
\]

(7.1)-(7.2) give

\[
\mathbb E Q^2
\le
\frac1{16}\sqrt{\frac{1-\rho}{1+\rho}}
\left(1-q+3q^2\right).
\tag{7.3}
\]

This replaces the preceding factor `1` by the exact rational factor

\[
1-q+3q^2
=
\frac{107230979640981229}{115266974235069409}
\approx0.9302836337.
\tag{7.4}
\]

Therefore the equicorrelated four-orthant satisfies

\[
M_4\le
\frac{\arcsin\rho}{\pi}
+rac1{16}\sqrt{\frac{1-\rho}{1+\rho}}(1-q+3q^2).
\tag{7.5}
\]

The softened cyclic four-cycle is entrywise covariance-dominated by this equicorrelated vector, so Slepian gives the same expression as an upper bound for its four-orthant. With the exact trace representation

\[
\operatorname{tr}(K^4)
=\frac1{1-r^4}\Pr(V_0,V_1,V_2,V_3<0),
\tag{7.6}
\]

the executed checker encloses `pi` by Machin's formula, `arcsin(rho)` by alternating rational `arctan` bounds, and the square root by integer-square-root bracketing. It certifies

\[
\operatorname{tr}(K^4)<1.0911589756436038
<\boxed{\frac{27279}{25000}=1.09116}.
\tag{7.7}
\]

This strictly improves the incoming exact cap

\[
\operatorname{tr}(K^4)<\frac{273011}{250000}=1.092044.
\tag{7.8}
\]

## 8. Spectral separation and Temple contradiction at `theta*=0.1652`

Set

\[
\theta_*:=\frac{413}{2500}=0.1652,
\qquad
x:=\frac{915543}{10^6},
\qquad
\beta:=\frac{9869}{12500}=0.78952.
\tag{8.1}
\]

The checker proves the exact integer-power inequality

\[
x^{625}<r^{413},
\tag{8.2}
\]

so `x<r^{4 theta_*}`.

Assume for contradiction that `lambda_1>=r^{4 theta_*}`. Then `lambda_1>x`. Since `K` is compact self-adjoint,

\[
\operatorname{tr}(K^4)=\sum_j\lambda_j^4.
\]

Using (7.7) and `lambda_1>x`, the checker certifies

\[
\beta^4-\left(\frac{27279}{25000}-x^4\right)>0
\tag{8.3}
\]

with exact positive margin (floating display `>6.10e-6`). Hence every non-Perron spectral point lies below `beta` in absolute value. Also `beta<mu` by (5.3).

On the spectrum,

\[
(\lambda_1-K)(K-\beta I)\le0.
\]

Taking expectation in the normalized quasimode state yields the elementary Temple inequality

\[
\varepsilon^2\ge(\lambda_1-\mu)(\mu-\beta).
\tag{8.4}
\]

But under the contradiction hypothesis the exact rational coarsenings give

\[
(\lambda_1-\mu)(\mu-\beta)
>(x-\mu_{hi})(\mu_{lo}-\beta)
>0.00047014936135162343,
\]

while

\[
\varepsilon^2<0.00047004495.
\]

The exact contradiction margin is positive (floating display `>1.04e-7`). Therefore

\[
\lambda_1<r^{4\theta_*}.
\tag{8.5}
\]

Equation (5.2) now gives the claimed strict source-level improvement

\[
\boxed{\theta_{2,1/4}>\frac{413}{2500}=0.1652.}
\]

## 9. Fresh primary-literature check

I inspected the current Molchan arXiv source/PDF, including the page stating that the one-sided `alpha=2, H!=1/2` exponent values remain unsolved and Statement 1.2(a), which supplies exponent existence/equality for primal and dual processes. I also searched current 2026 primary work around fractional-Brownian persistence. The later Molchan paper on multivariate-time fBM (arXiv:2608.26680) and Aurzada--Helmer on fractional Levy fields over hyperbolic/Riemannian index sets (arXiv:2608.17463) concern different processes; adjacent integrated-fractional-process small-ball/LIL work likewise does not state an exact one-sided `theta_{2,1/4}`. I found no later primary theorem in this bounded search that supersedes the exact T05 target or the bracket above. This is dated bounded negative evidence only, not a worldwide novelty or priority certificate.

## 10. Failed route and next obstruction

The first new route in this invocation split the cyclic Gaussian four-cycle into opposite two-dimensional blocks and applied the Gaussian maximal-correlation/HGR inequality. It produced a rigorous trace cap `1.10263`, which would only support `theta>0.16483`; after the current PROB10-05 `0.16517` baseline was discovered, that route was source-level obsolete and was not promoted.

The successful route instead strengthens the one-factor probit product pointwise before integrating. The residual bottleneck is now the equicorrelation domination `rho_opp -> rho_adj`, which discards the exact cyclic gap. The next materially different attack should keep both correlations and rigorously enclose the exact cyclic quadrivariate orthant, e.g. through a one-dimensional Plackett/Childs derivative integral with outward rational interval quadrature. That route can improve (7.7) without changing the source process, the continuum event, or the already-certified quasimode.

## 11. Artifacts and exact execution

Successful exact checker:

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20__probit_refinement_exact_check.py`

creation commit `32358e783e9fa08726e935e2628ce5d557189396`.

Executed output:

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20__probit_refinement_exact_check.out`

creation commit `6db2dd8fe79a234c6a1255c7b99677442ab9264f`, ending in `ALL_EXACT_CHECKS_PASS = True`.

The abandoned HGR route is preserved, not erased, in

- `2026-09-20__hgr_quad_trace_exact_check.py` @ `d97e1f7f469e22657c7fac3a0be394f57cc1cb84`;
- `2026-09-20__hgr_quad_trace_exact_check.out` @ `9eaf1419bf363815290e83aeb776c7c28872a1b1`.

No shared root, canonical claim, peer report, schedule, permission, email/Drive resource, public posting, paid compute, or workflow was modified.

```yaml
ledger_delta:
  worker: NM13-09
  parent: T05 integrated-fBM persistence
  canonical_parent_claim: MOLCHAN-2025-THETA2H
  ownership_change: none
  source_process: I(t)=integral_0^t B_{1/4}(u)du
  source_event: P(I(t)<=1 for all 0<=t<=T)=T^(-theta+o(1))
  exponent_existence: recovered_from_Molchan_Statement_1_2a
  status: PARTIAL_CANDIDATE_PENDING_INDEPENDENT_REVIEW
  source_metric:
    quantity: W_1_4 = 1/4 - lower_endpoint
    before: 8483/100000
    after: 53/625
    delta: -3/100000
  lower_endpoint:
    before: 16517/100000
    after: 413/2500
    gain: 3/100000
  upper_endpoint:
    before: 1/4
    after: 1/4
  mechanism_progress:
    all_lag_covariance_domination: exact_for_every_integer_lag
    continuum_interpolation_penalty_lower_bound_direction: 0
    fourth_trace_cap_before: 273011/250000
    fourth_trace_cap_after: 27279/25000
    new_lemma: Phi(x)Phi(-x) <= exp(-x^2/2)/(4 sqrt(1+x^2/5))
  failed_route:
    hgr_fourcycle_trace_cap: 110263/100000
    source_metric_gain: none_against_current_baseline
  next_attack: exact_cyclic_quadrivariate_orthant_interval_bound
```
