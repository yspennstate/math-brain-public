Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 221/2000 -> 1/4 - sqrt(5/(18D)) = 0.1103677111423229...`, where `D=pi^2/2-8G+416/25`; methods B2 / B5 / B24.**

# HARD7-05 bounded research iteration — the optimal integrated-Brownian spectral minorant

Status: **PARTIAL / source target OPEN.** This run exactly optimizes the integrated-Brownian spectral-minorization route opened in the preceding checkpoint. It proves the stronger continuous-path lower bound
\[
\boxed{\theta_{2,1/4}\ge
\frac14\sqrt{\frac{40}{9D}}
=\sqrt{\frac{5}{18D}}
=0.1396322888576770\ldots,}
\qquad
D:=\frac{\pi^2}{2}-8G+\frac{416}{25},
\tag{0.1}
\]
where \(G=\sum_{n\ge0}(-1)^n/(2n+1)^2\) is Catalan's constant. More importantly, it proves that the scale
\[
\boxed{c_*=\sqrt{\frac{40}{9D}}=0.5585291554307082\ldots}
\tag{0.2}
\]
is the **largest possible time scale within this exact integrated-Brownian spectral-comparison family**: every \(c>c_*\) fails the required spectral domination already in an arbitrarily small neighborhood of frequency zero.

The full Molchan problem — determining \(\theta_{2,H}\) throughout \(0<H<1,\ H\ne1/2\) — remains open.

## 1. Continuity, ownership, source/current-status refresh, and repository state

I resumed the exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`; I did not restart admission or create an alias claim.

Before the new argument I reread the governing files
`operations/hard7_2026-09-18/CONTROL.md`,
`operations/NEW_METHODS_2026-09-16.md`,
`operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
`probability_campaign_2026_09/INDEX.md`,
`probability_campaign_2026_09/RANKING.md`,
root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
the claim file, the full indexed HARD7-05 checkpoint chain through
`2026-09-19T0440Z__spectral_minorization_279_2000.md`,
and the newest neighboring checkpoints located before this write:
HARD7-04 `2026-09-19T05-32Z__p0157_three_hub_whp.md` and
HARD7-06 `2026-09-19T04-49-49Z__cycle_code_duality.md`.
I also repeated repository-wide searches for the exact arXiv identifier, title, `theta_{2,H}`, integrated-fBM aliases, and the canonical claim. The large intake JSONL files are not honestly renderable byte-for-byte in one bounded connector response, so the intake check was done through their indexed/canonical aliases and repository-wide exact-source searches rather than represented as a fictitious full dump. No release, competing owner, posted equivalent, or canonical collision surfaced.

The primary source was refreshed on 2026-09-19:

- G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265 (current repository checkpoint records v11, revised 4 July 2026). The current source continues to treat the values \(\theta_{2,H}\), \(H\ne1/2\), as unresolved.
- N. D. Feldheim, O. N. Feldheim and S. Mukherjee, *Persistence and Ball Exponents for Gaussian Stationary Processes*, arXiv:2112.04820. Theorem 3(II) is the spectral-addition monotonicity used below.

Fresh bounded searches dated 2026-09-19 for the exact Molchan title/arXiv identifier, `theta_{2,1/4}`, integrated-fBM persistence, and the spectral-comparison literature recovered Molchan, Aurzada--Kilian and Feldheim--Feldheim--Mukherjee, but no exact value of \(\theta_{2,1/4}\) or later full solution. This is bounded negative evidence, not worldwide novelty certification.

The scheduler/capability state remains unchanged: GPT-6/maximum is prompt-requested only. The exposed automation interface has no model selector, reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed run duration. This invocation identifies as GPT-5.6 Sol and exposes no authenticated reasoning level, so the latter is `UNVERIFIED`. For a native task that returns `You cannot modify this task` (the historical P26-type failure), the authorized workaround is resolution through the owning account/workspace interface or platform support; a repository edit, duplicate schedule, or permission bypass is not a scheduler repair.

## 2. Frozen quantity — genuine movement

The fixed source-relevant metric is
\[
W_{1/4}=U_{1/4}-L_{1/4}.
\]

The preceding run proved
\[
L_{1/4}=\frac{279}{2000},\qquad
U_{1/4}=\frac14,\qquad
W_{1/4}=\frac{221}{2000}=0.1105.
\tag{2.1}
\]

This run proves (0.1), hence
\[
\boxed{
\sqrt{\frac{5}{18D}}
\le \theta_{2,1/4}\le\frac14,
}
\tag{2.2}
\]
and therefore
\[
\boxed{
W_{1/4}:
\frac{221}{2000}
\longrightarrow
\frac14-\sqrt{\frac{5}{18D}}
=0.1103677111423229\ldots .
}
\tag{2.3}
\]

The improvement in bracket width is
\[
0.0001322888576770685\ldots .
\]

The inequality is rigorous, not a decimal-fit claim. In §5 below the strict comparison
\(c_*>279/500\) is certified from rational bounds
\(\pi<22/7\) and an eight-term alternating lower bound for \(G\).
No sampled path, finite-time fit, or frequency grid is used.

## 3. Exact spectral quotient

Retain the exact normalized target spectrum proved in the preceding checkpoint. With
\[
u=\lambda^2\ge0,
\]
the \(H=1/4\), \(\alpha=2\) stationary dual has normalized spectral density
\[
A(\lambda)
=
\frac{\cosh(\pi\lambda)}{\cosh(2\pi\lambda)}
\frac{\Gamma(9/4)^2}{|\Gamma(9/4+i\lambda)|^2}.
\tag{3.1}
\]

The Lamperti stationary version of integrated Brownian motion, time-scaled by \(c>0\), has normalized spectrum
\[
G_c(\lambda)
=
\frac{9c^4}{(4\lambda^2+c^2)(4\lambda^2+9c^2)}
=
\frac{1}{
(1+4u/c^2)(1+4u/(9c^2))
}.
\tag{3.2}
\]

As in the previous run, proving
\[
A(\lambda)\ge G_c(\lambda)\qquad(\forall\lambda\in\mathbb R)
\tag{3.3}
\]
allows the two actual spectral densities to be matched at frequency zero. The residual is then a nonnegative spectral measure whose density vanishes at zero, so Feldheim--Feldheim--Mukherjee Theorem 3(II) yields
\[
\theta_{2,1/4}\ge \frac c4.
\tag{3.4}
\]

The new task is therefore not merely to find another feasible rational \(c\), but to solve the extremal spectral-minorization problem exactly.

Euler products give
\[
\cosh(\pi\lambda)
=\prod_{r\ge0}\left(1+\frac{4u}{(2r+1)^2}\right),
\tag{3.5}
\]
\[
\cosh(2\pi\lambda)
=\prod_{r\ge0}\left(1+\frac{16u}{(2r+1)^2}\right),
\tag{3.6}
\]
and
\[
\frac{\Gamma(9/4)^2}{|\Gamma(9/4+i\lambda)|^2}
=
\prod_{n\ge0}\left(1+\frac{16u}{(4n+9)^2}\right).
\tag{3.7}
\]

The Gamma product cancels the denominator factors \(9,13,17,\ldots\). Thus, after division by \(G_c\), the quotient
\[
R_c(u):=\frac{A(\sqrt u)}{G_c(\sqrt u)}
\tag{3.8}
\]
is a ratio of two convergent products
\[
R_c(u)=\frac{\prod_{i\ge1}(1+x_i u)}
{\prod_{i\ge1}(1+y_i u)}.
\tag{3.9}
\]

Write \(q=c^2\). The numerator multiset is
\[
\left\{\frac4q,\frac4{9q}\right\}
\cup
\left\{\frac4{(2j+1)^2}:j\ge0\right\},
\tag{3.10}
\]
while the denominator multiset is
\[
\left\{
16,\frac{16}{9},\frac{16}{25},\frac{16}{49},
\frac{16}{121},\frac{16}{225},\ldots
\right\}.
\tag{3.11}
\]

Both coefficient sequences are in \(\ell^1\), so (3.9) and all logarithmic sums below converge for every \(u\ge0\).

## 4. B2 + B5 — attack the negation and differentiate in the scale

The first-order behavior at frequency zero gives an obstruction to every too-large comparator.

The numerator coefficient sum is
\[
X(q)
=
\frac{\pi^2}{2}+\frac{40}{9q}.
\tag{4.1}
\]

For the denominator, use
\[
\sum_{\substack{m\ge1\\m\ {\rm odd}}}\frac1{m^2}
=\frac{\pi^2}{8}
\tag{4.2}
\]
and, with Catalan's constant \(G\),
\[
\sum_{n\ge0}\frac1{(4n+1)^2}
=\frac{\pi^2}{16}+\frac G2.
\tag{4.3}
\]
The canceled indices are \(9,13,17,\ldots\), so
\[
\begin{aligned}
Y
&=
16\left[
\frac{\pi^2}{8}
-\left(
\frac{\pi^2}{16}+\frac G2-1-\frac1{25}
\right)
\right]\\
&=
\pi^2-8G+\frac{416}{25}.
\end{aligned}
\tag{4.4}
\]

Hence
\[
\left.\frac{d}{du}\log R_c(u)\right|_{u=0}
=
X(q)-Y
=
\frac{40}{9q}
-\left(
\frac{\pi^2}{2}-8G+\frac{416}{25}
\right).
\tag{4.5}
\]

Define
\[
D:=\frac{\pi^2}{2}-8G+\frac{416}{25}>0,
\qquad
q_*:=\frac{40}{9D},
\qquad
c_*:=\sqrt{q_*}.
\tag{4.6}
\]

Then (4.5) vanishes exactly at \(q=q_*\).

This already proves the **negative** half of the extremal statement. If \(c>c_*\), equivalently \(q>q_*\), then
\[
\left.\frac{d}{du}\log R_c(u)\right|_{u=0}<0.
\]
Since \(R_c(0)=1\), continuity/differentiability gives
\[
R_c(u)<1
\]
for all sufficiently small positive \(u\). Thus (3.3) fails in every punctured sufficiently small neighborhood of frequency zero.

Therefore no \(c>c_*\) can work. The only remaining question is whether the tangent candidate \(c_*\) works globally.

This is B2 in the requested counterexample-first sense: the attempted stronger statement “some \(c>c_*\) also minorizes” is rigorously falsified by an explicit low-frequency obstruction, not by numerics. It is also B5: introducing the scale \(c\) and differentiating the exact quotient at zero identifies the unique extremal candidate.

## 5. B24 — the tangent candidate is globally feasible by infinite majorization

We now prove
\[
R_{c_*}(u)\ge1\qquad\forall u\ge0.
\tag{5.1}
\]

At \(q=q_*\), the total coefficient sums are equal:
\[
\sum_i x_i=\sum_i y_i.
\tag{5.2}
\]

We first put both sequences in decreasing order.

Elementary bounds give
\[
\frac14<q_*<1.
\tag{5.3}
\]
In fact the stronger \(q_*>9/31\) holds. One convenient proof uses
\(\pi^2<10\) and \(G>8/9\), which imply
\[
D<5-\frac{64}{9}+\frac{416}{25}
=\frac{3269}{225}
<\frac{1240}{81};
\]
hence \(q_*=40/(9D)>9/31\). Also \(\pi^2>9\) and \(G<1\) give
\[
D>\frac92-8+\frac{416}{25}
=\frac{657}{50}
>\frac{40}{9},
\]
so \(q_*<1\).

Consequently the decreasing numerator sequence is
\[
x_1=\frac4{q_*},\qquad
x_2=4,\qquad
x_3=\frac4{9q_*},
\tag{5.4}
\]
and for \(k\ge4\),
\[
x_k=\frac{16}{(4k-10)^2}.
\tag{5.5}
\]

The decreasing denominator sequence is
\[
y_1=16,\qquad
y_2=\frac{16}{9},\qquad
y_3=\frac{16}{25},
\tag{5.6}
\]
and for \(k\ge4\),
\[
y_k=\frac{16}{(4k-9)^2}.
\tag{5.7}
\]

Let
\[
S_k:=\sum_{i=1}^k(y_i-x_i).
\tag{5.8}
\]

The first two partial sums are nonnegative because
\[
S_1\ge0 \iff q_*\ge\frac14,
\qquad
S_2\ge0 \iff q_*\ge\frac9{31}.
\tag{5.9}
\]

At \(k=3\), substitute \(40/(9q_*)=D\):
\[
\begin{aligned}
S_3
&=
16+\frac{16}{9}+\frac{16}{25}
-4-\frac4{q_*}-\frac4{9q_*}\\
&=
8G-\frac{\pi^2}{2}-\frac{20}{9}.
\end{aligned}
\tag{5.10}
\]
This is strictly positive. A completely rational certificate follows from
\[
G>
1-\frac1{3^2}+\frac1{5^2}-\frac1{7^2}
=\frac{10016}{11025}
\tag{5.11}
\]
and \(\pi<22/7\):
\[
S_3>
8\frac{10016}{11025}
-\frac12\frac{484}{49}
-\frac{20}{9}
=
\frac{1178}{11025}>0.
\tag{5.12}
\]

For every \(k\ge4\),
\[
y_k
=
\frac{16}{(4k-9)^2}
<
\frac{16}{(4k-10)^2}
=x_k.
\tag{5.13}
\]
Thus \(S_k\) is strictly decreasing from \(k=3\) onward. But by the equal-total identity (5.2),
\[
S_k\longrightarrow0.
\tag{5.14}
\]
A decreasing sequence converging to zero cannot become negative, hence
\[
S_k\ge0\qquad\forall k.
\tag{5.15}
\]

Therefore the decreasing sequence \(y=(y_i)\) majorizes \(x=(x_i)\).

Apply the standard countable Karamata inequality to the increasing concave function
\[
\phi_u(s)=\log(1+us),\qquad u\ge0.
\tag{5.16}
\]
The countable extension follows from finite Karamata by truncation and dominated convergence, since \(x,y\in\ell^1\) and
\(0\le\log(1+us)\le us\). Because \(y\) majorizes \(x\),
\[
\sum_i\log(1+ux_i)
\ge
\sum_i\log(1+uy_i).
\tag{5.17}
\]
Exponentiating (5.17) yields exactly
\[
\boxed{R_{c_*}(u)\ge1\qquad\forall u\ge0.}
\tag{5.18}
\]
For \(u>0\), strict concavity and the fact that the two sequences are not permutations give strict inequality.

Combining §4 and §5 proves the route-level extremal theorem:

> **Optimal spectral-minorization scale.**
> For the exact \(H=1/4\) target spectrum \(A\) and the time-scaled integrated-Brownian spectra \(G_c\),
> \[
> A(\lambda)\ge G_c(\lambda)\quad\forall\lambda\in\mathbb R
> \]
> holds at \(c=c_*\), while it fails for every \(c>c_*\). Thus \(c_*\) is the largest feasible scale in this comparator family.

This is B24: instead of incrementally retaining more positive Euler factors, the run identifies and proves optimality of the extremal comparator by a global majorization order.

## 6. Persistence consequence and strict improvement over the previous checkpoint

Match the actual target and comparator spectral densities at zero exactly:
\[
a:=\frac{f_T(0)}{g_{c_*}(0)}>0,\qquad
\nu:=\rho_T-a\rho_{c_*}.
\tag{6.1}
\]
Equation (5.18) makes \(\nu\) a nonnegative spectral measure, and the normalization gives
\[
\nu'(0)=0.
\tag{6.2}
\]

The membership assumptions required by Feldheim--Feldheim--Mukherjee are the same ones checked in the preceding report: \(a\rho_{c_*}\in\mathcal M\); the target and residual are in \(\mathcal L\); the target density has the source spectral tail and the integrated-Brownian comparator decays as \(O(|\lambda|^{-4})\). Multiplying the comparator process by a positive amplitude does not change a level-zero sign event. Therefore Theorem 3(II) gives
\[
\theta_{2,1/4}
\ge
\theta^0_{\rho_{c_*}}
=
\frac{c_*}{4}
=
\sqrt{\frac{5}{18D}},
\tag{6.3}
\]
which is (0.1).

For rigorously certified movement relative to the preceding rational \(c_0=279/500\), take the eight-term alternating lower bound
\[
G>
\sum_{n=0}^{7}\frac{(-1)^n}{(2n+1)^2}
=
\frac{1854623872}{2029052025}.
\tag{6.4}
\]
Together with \(\pi<22/7\),
\[
D<
\frac{5789493434}{405810405}.
\tag{6.5}
\]
Exact arithmetic gives
\[
\frac{40}{9(279/500)^2}
-
\frac{5789493434}{405810405}
=
\frac{26721289334}{3509854192845}>0.
\tag{6.6}
\]
Hence
\[
D<\frac{40}{9(279/500)^2},
\qquad
c_*>\frac{279}{500},
\tag{6.7}
\]
so (6.3) is strictly stronger than the preceding \(279/2000\) lower bound.

Numerically, for orientation only,
\[
D=14.24707744712692718898\ldots,
\]
\[
c_*=0.55852915543070827405\ldots,
\]
\[
\frac{c_*}{4}
=0.13963228885767706851\ldots,
\]
and
\[
W_{1/4}
=0.11036771114232293149\ldots.
\tag{6.8}
\]

The theorem itself is the exact formula (6.3), not these decimal evaluations.

## 7. Exact finite self-check

The finite rational core was executed before archival.

Checker:
`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0550Z_optimal_spectral_majorization_check.py`

creation commit:
`305eac8b2f755924a960fe9bca1f36eb5d87091a`

Executed output:
`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0550Z_optimal_spectral_majorization_check.out`

creation commit:
`dec022d5c7700e39645a8247e5839def3897e864`

The self-check verifies with exact rational arithmetic:

- the four- and eight-term Catalan lower sums;
- the strict movement inequality \(c_*>279/500\);
- the coarse bounds \(9/31<q_*<1\) needed for sorting;
- the exact positive \(S_3\) lower margin \(1178/11025\);
- the tail-pair inequality \(y_k<x_k\) over a large finite sanity range;
- the constant bookkeeping in the \(S_3\) identity.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The finite loop over tail pairs is only a self-check of the closed-form inequality (5.13); the proof of (5.13) is the one-line denominator comparison on the page and is not inferred from the finite loop. Likewise the checker does not replace Euler products, countable Karamata, or the FFM theorem.

## 8. Required new-method accounting

- **B2 — ATTACK THE NEGATION FIRST: succeeded.** Assuming a larger Brownian time scale \(c>c_*\) gives a negative derivative of the exact spectral quotient at frequency zero, so the domination fails immediately for small nonzero frequencies. This proves an exact no-go statement for the entire comparator family beyond \(c_*\).
- **B5 — ADD A PARAMETER AND DIFFERENTIATE IN IT: succeeded.** Treating the comparator scale \(c\) as a parameter and differentiating at zero identifies the unique tangent scale \(c_*\) in closed form.
- **B24 — FIND THE EXTREMAL OBJECT: succeeded.** The tangent comparator is not merely locally admissible: an infinite majorization of the Euler-product coefficient sequences proves global domination, making \(c_*\) the extremal feasible comparator.

The preceding B1/B12/B30 triple was not repeated.

## 9. Scope and next checkpoint

What is established is a new restricted lower bound at one source-valid Hurst value and the exact solution of one proof-route optimization problem:
\[
\sqrt{\frac{5}{18D}}
\le \theta_{2,1/4}\le\frac14.
\]

This remains **PARTIAL** for Molchan's full question. No source closure, independent audit, or paper package is claimed.

The principal remaining mathematical question suggested by this run is no longer “how many Euler factors should be retained?” — that route is now exactly exhausted. Any next run should change category again. A natural direction is to seek a comparator family with more than two spectral poles, or to use the exact majorization structure to obtain an upper bound rather than another lower minorant. Repeating the integrated-Brownian scale optimization would not be new progress.

```yaml
ledger_delta:
  track: HARD7-05
  target: MOLCHAN-2025-THETA2H
  status: PARTIAL
  metric: W_1/4
  before: 221/2000
  after_exact: "1/4 - sqrt(5/(18D)), D=pi^2/2-8*Catalan+416/25"
  after_decimal: 0.11036771114232293149
  lower_before: 279/2000
  lower_after_exact: "sqrt(5/(18D))"
  lower_after_decimal: 0.13963228885767706851
  upper: 1/4
  movement: true
  methods: [B2, B5, B24]
  route_result: "optimal integrated-Brownian spectral minorant c_*"
  source_open: true
  closure: false
  self_check: PASS
  independent_audits: 0
```
