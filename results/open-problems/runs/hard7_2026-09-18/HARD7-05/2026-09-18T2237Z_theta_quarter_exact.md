Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}=1/8 -> 0`; methods B3 / B15 / B24.**

# HARD7-05 run 3 — exact special point `theta_{2,1/4}=1/8` by an asymmetric solvable Gaussian comparison

Status: **PARTIAL for the full Molchan source problem; exact tracked special point resolved in this run.** The source asks for the full function `H -> theta_{2,H}` for `0<H<1`, `H != 1/2`; this run determines only `H=1/4`. It is therefore not source closure and no paper/audit completion is claimed.

## 1. Continuity, source version, ownership, neighboring state

This run resumed the exclusive claim `operations/claims/MOLCHAN-2025-THETA2H.md` and the latest own checkpoint `runs/hard7_2026-09-18/HARD7-05/2026-09-18T2138Z_half_parameter_tangent.md`. It did not restart admission or change the frozen metric.

Before doing mathematics I re-read the controlling HARD7 file, the 16 September new-methods policy and owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest neighboring HARD7-04 and HARD7-06 reports, and repository/intake search results for this source family. No claim collision or equivalent posted target was found.

A current-source correction matters: the claim record was created from arXiv:2509.10265v1, but the arXiv record now has **v11, revised 4 July 2026**. I read the current v11 PDF rather than assuming v1 was still the latest. On printed p. 3, v11 still states that the exponent values for `alpha=2, H != 1/2` remain unsolved and retains the bound

`(1/2)(H min (1-H)) <= theta_{2,H}`

with the displayed upper estimate (3). At `H=1/4` this gives the same verified baseline

\[
\frac18\le \theta_{2,1/4}\le\frac14,
\qquad W_{1/4}=\frac18.
\]

The same v11 paper, Statement 1.4 on printed p. 6, gives an exact persistence exponent for the stationary Gaussian family with covariance

\[
K_H(t)=\frac{\cosh((2H-1)t/2)}{\cosh(t/2)}:
\qquad \theta(K_H)=\frac38\,(H\wedge(1-H)).
\tag{1}
\]

Fresh bounded searches on 19 September 2026 for the exact title, `theta_{2,1/4}`, `integrated fractional Brownian H=1/4 persistence exponent`, and the comparison covariance below recovered Molchan's current paper, the earlier Molchan 2018 estimates, Aurzada--Kilian, and adjacent persistence literature, but no exact determination of `theta_{2,1/4}`. This is a bounded negative search, **not** a proof of worldwide novelty.

The scheduler capability statement is still the same. The exposed automation interface has title/prompt/schedule/timing/enabled controls, but no model selector, no reasoning-effort selector, and no guaranteed execution duration; GPT-6/maximum is prompt text only. Changing that would require a platform/API capability that exposes authenticated model/effort controls. Historical native probes for P26/P01/P03 returned `You cannot modify this task`; the authorized workaround is account/workspace ownership resolution or platform support, not a duplicate schedule or permission bypass. This run did not attempt to modify any scheduler.

## 2. Frozen metric — before and after

Before this run:

\[
[L_{1/4},U_{1/4}]=[1/8,1/4],\qquad W_{1/4}=1/8.
\]

After the comparison theorem proved below:

\[
\boxed{\theta_{2,1/4}=\frac18},
\qquad
[L_{1/4},U_{1/4}]=[1/8,1/8],
\qquad
\boxed{W_{1/4}:\frac18\longrightarrow0}.
\]

This is genuine source-relevant movement. It does not determine `theta_{2,H}` away from `H=1/4`.

## 3. B15 — break the Brownian symmetry on purpose and tune an exact reference

Run 1 showed that time-rescaled integrated Brownian motion cannot improve the tracked lower endpoint; run 2 showed a positive all-lag tangent at the Brownian point. Instead of staying at `H=1/2`, I used Molchan's exactly solvable family (1) with a deliberately asymmetric parameter.

Let `m=H_0 wedge (1-H_0)` and compare to `K_{H_0}(ct)`. Its persistence rate is

\[
\frac38\,c m.
\]

To hit the existing lower bound `1/8` exactly, impose

\[
cm=\frac13. \tag{2}
\]

For the source process at `H=1/4`, the run-1 local covariance expansion is

\[
R_{1/4}(t)=1-\frac{15}{32}t^2+o(t^2).
\]

The reference has

\[
K_{H_0}(ct)=1-\frac{c^2m(1-m)}2t^2+O(t^4).
\]

Under (2), local domination `R_{1/4} >= K_{H_0}(c\cdot)` requires

\[
\frac{1-m}{18m}\ge\frac{15}{32},
\qquad\text{i.e.}\qquad m\le\frac{16}{151}.
\tag{3}
\]

The simple rational choice

\[
H_0=m=\frac1{10},\qquad c=\frac{10}{3}
\]

has strict local margin and gives the reference covariance

\[
\boxed{K(t)=\frac{\cosh(4t/3)}{\cosh(5t/3)}}. \tag{4}
\]

Its exact persistence exponent is, by (1),

\[
\theta(K)=\frac{10}{3}\cdot\frac38\cdot\frac1{10}=\frac18. \tag{5}
\]

The long-lag rates are also aligned in the favorable direction: run 1 gives `R_{1/4}(t) ~ (5/6)e^{-t/4}`, whereas (4) is asymptotic to `e^{-t/3}`. Thus the only real issue is whether an intermediate-lag crossing occurs. B24 below removes that possibility exactly.

## 4. B3 — prove the stronger all-lag covariance statement

### Theorem 1
For every `t>=0`,

\[
\boxed{R_{1/4}(t)\ge \frac{\cosh(4t/3)}{\cosh(5t/3)}}. \tag{6}
\]

The inequality is strict for every finite `t>0`.

### Proof
Use the exact normalized Lamperti covariance from runs 1--2 and put

\[
x=e^{-t/12}\in(0,1].
\]

At `H=1/4`, exact simplification gives

\[
R_{1/4}(t)=
\frac{(1-x^{12})^{5/2}+\frac52(x^{12}+x^{18})-1-x^{30}}
{3x^{15}}. \tag{7}
\]

The reference covariance (4) is

\[
K(t)=x^4\frac{1+x^{32}}{1+x^{40}}. \tag{8}
\]

All denominators are positive on `(0,1)`. Therefore (6) is equivalent to

\[
F(x):=(1+x^{40})(1-x^{12})^{5/2}+P(x)\ge0, \tag{9}
\]

where

\[
P(x)=\left[\frac52(x^{12}+x^{18})-1-x^{30}\right](1+x^{40})
-3x^{19}(1+x^{32}). \tag{10}
\]

Define the exact polynomial

\[
C(x):=\frac{-2P(x)}{(1-x)^2(x^2+x+1)}. \tag{11}
\]

The quotient is a degree-66 polynomial over the rationals. Also set

\[
D(x):=(1+x^{40})^2(1-x^{12})^5-P(x)^2 \tag{12}
\]

and define the degree-114 rational polynomial `J` by the exact factorization

\[
D(x)=-\frac14x^{18}(1-x)^4(x^2+x+1)^2J(x). \tag{13}
\]

The finite algebraic core is exact root isolation. The archived checker proves the quotient/factor identities (11)--(13) and gives:

\[
C(0)=2,\qquad C(1)=-18,
\]

with exactly one root of `C` in `(0,1)`, isolated in

\[
\left(\frac{940}{959},\frac{1039}{1060}\right), \tag{14}
\]

and

\[
J(0)=-20,\qquad J(1)=324,
\]

with exactly one root of `J` in `(0,1)`, isolated in

\[
\left(\frac{1368}{1369},\frac{1369}{1370}\right). \tag{15}
\]

The intervals are disjoint and ordered: the `C` root lies strictly before the `J` root.

Now on `(0,1)`, equation (11) says

\[
P(x)=-\frac12(1-x)^2(x^2+x+1)C(x).
\]

If `P(x)>=0`, then (9) is immediate because the radical term is positive.

If `P(x)<0`, then `C(x)>0`. By (14), `x` lies to the left of the unique `C` root. Since that root lies left of the unique `J` root and `J(0)<0`, we have `J(x)<0`. Equation (13) then gives `D(x)>0`, i.e.

\[
(1+x^{40})^2(1-x^{12})^5>P(x)^2.
\]

Both `(1+x^{40})(1-x^{12})^{5/2}` and `-P(x)` are positive, so taking square roots yields

\[
(1+x^{40})(1-x^{12})^{5/2}>-P(x),
\]

which is exactly `F(x)>0`. At `t=0` both covariances equal one. This proves (6), with strictness for `t>0`. QED.

The root isolation is a finite exact-arithmetic certificate, not a sampled plot. It is archived as a self-check and is not represented as an independent audit.

## 5. B24 — extremal defect analysis closes the comparison and the tracked special point

The covariance defect

\[
\Delta(t):=R_{1/4}(t)-K(t)
\]

was not certified by gridding. The B24 step was to locate the only possible sign obstruction after algebraization. Equations (11)--(15) show that the sign-danger region `P<0` ends before the squared-defect obstruction `J` can change sign. That ordered pair of exact roots is the whole finite obstruction: there is no hidden intermediate-lag negative defect.

Both processes are centered, stationary, variance one, and have the persistence exponents used above. By Slepian comparison in the same direction used in Molchan 2018,

\[
K(t)\le R_{1/4}(t)\quad\forall t
\quad\Longrightarrow\quad
\theta_{2,1/4}\le\theta(K)=\frac18. \tag{16}
\]

Molchan's rigorous lower bound (current v11 equation (3), and already in the 2018 Proposition 1(b)) gives

\[
\theta_{2,1/4}\ge\frac12\min\{1/4,3/4\}=\frac18. \tag{17}
\]

Combining (16)--(17) proves

\[
\boxed{\theta_{2,1/4}=\frac18}. \tag{18}
\]

This is a continuous-path Gaussian comparison; no discretely sampled persistence event is used anywhere.

## 6. Exact artifacts and readback

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-18T2237Z_theta_quarter_exact_check.py`

creation commit: `1fee48a063f544e50e777a3ed533d8d818f1f929`.

Executed output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-18T2237Z_theta_quarter_exact_check.out`

creation commit: `20937885bbaadc3e9a2dd93cfbcdd632373835c3`.

The output was read back at that commit and ends

`ALL_EXACT_CHECKS_PASS`.

It records degree `66` and `114` quotient polynomials, the exact rational isolating intervals (14)--(15), their ordering, endpoint signs, and the exact reference exponent `1/8`.

## 7. What is and is not claimed

**Claimed in this track:** a complete on-page argument, conditional only on the standard/source Slepian comparison and Molchan's stated exact reference exponent/lower bound, that the source special value is `theta_{2,1/4}=1/8`; its finite polynomial core has an executed exact self-check.

**Not claimed:** determination of `theta_{2,H}` for all `H`; source closure; independent audit; worldwide novelty; a paper-ready package; or any inference from simulation.

The full source target remains **PARTIAL / OPEN**. The frozen metric itself is now saturated at zero, so later runs must not pretend further movement in `W_{1/4}`; they should continue the full source question with honest status and follow section I if the remaining obligation stagnates.

## 8. Next mathematical routes — do not repeat B3/B15/B24

A next run should use genuinely different moves. Suggested triple: **B1 / B4 / B13**.

- `B1` change category: interpret the successful covariance domination as a cone/positive-kernel problem and identify a reusable operator criterion for other rational `H`.
- `B4` prove something weaker completely: seek a second exact rational Hurst value by choosing a solvable `K_{H_0}(ct)` whose exponent matches one endpoint of Molchan's current bracket and whose algebraic substitution has a finite root certificate.
- `B13` find what only increases: vary the reference parameter `m` under the exponent constraint `cm=constant` and seek a monotone covariance defect, which could replace high-degree one-off algebra by a parameter interval theorem.

Because this run moves the frozen metric, the three-run stuck trigger is **not** activated.

## 9. ledger_delta

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  source_current_version: "arXiv:2509.10265v11, revised 2026-07-04"
  status: PARTIAL
  source_full_problem: OPEN
  metric: W_{1/4}
  before: 1/8
  after: 0
  movement: "yes"
  methods: [B3, B15, B24]
  new_result: "theta_{2,1/4}=1/8 via exact all-lag covariance domination by the time-scaled Molchan Laplace-FBM reference H0=1/10, c=10/3"
  reference_covariance: "cosh(4t/3)/cosh(5t/3)"
  exact_checker_commit: 1fee48a063f544e50e777a3ed533d8d818f1f929
  exact_output_commit: 20937885bbaadc3e9a2dd93cfbcdd632373835c3
  exact_output_tail: ALL_EXACT_CHECKS_PASS
  independent_audits: 0
  closure: false
  next_methods: [B1, B4, B13]
```
