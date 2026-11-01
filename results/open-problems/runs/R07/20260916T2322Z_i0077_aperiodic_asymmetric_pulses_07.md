Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **METRIC MOVEMENT: 6 -> 7 genuinely distinct nonparabolic shape families; Section-B moves tried: #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS, #7 TAKE THE LIMIT.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the open-ended source problem is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 7: aperiodic asymmetric parabolic-scale pulse tubes

Run date: 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric is the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260916T2226Z_i0077_log_periodic_pulses_06.md`.

It records metric `6` from:

1. mixed two-power zero-seam cusps `u^alpha+u^beta`, `0<alpha<1/2<beta`;
2. logarithmic zero-seam cusps of regular-variation index `1/2` at both ends;
3. homogeneous pure-power tubes `u^beta`, with the complete `beta<1/2`, `beta=1/2`, `beta>1/2` phase portrait proved in run 3;
4. outward `o(sqrt u)` corrugations of a parabolic strip;
5. positive-seam superdiffusive gauges such as `1+u^(3/4)`;
6. exactly log-periodic pulsed parabolic-scale tubes.

This run proves a universal nonconfinement theorem for a seventh family: **aperiodic, asymmetric parabolic-scale pulse tubes with a positive lower density of narrow logarithmic-time pulses**. Exact periodicity is absent and the two walls need not be symmetric.

Therefore

\[
\boxed{6\longrightarrow7.}
\]

`unchanged_count` resets to `0`.

## 2. Required repository continuity / admission / ownership

Before new mathematics I reread or rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- all six previous R07/I0077 reports, especially run 6;
- newest same-source neighboring R15 report `runs/R15/20260916_2258Z_i0076_excursion_palm_a19.md`, which owns distinct Problem 7.2 / I0076;
- targeted repository/intake searches for I0077, `1302.6958`, Problem 7.8, and duplicate attempts.

`INDEX.md` and `RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. The canonical claim remains R07's exclusive reservation; its shared text still says `PENDING_ADMISSION, not READY`, but run 1 recorded complete source/status/ownership admission evidence and this worker does not mutate shared operational files. C29 previously detected the reservation and declined to duplicate I0077. R15 remains on distinct Problem 7.2.

The large `probability_1000_intake_*/problems.jsonl` resources are connector-truncated. I therefore record the whole-intake reread as **PARTIAL / targeted due connector limits**, not as a fictitious complete row-by-row read. Exact I0077 source, ownership, exclusions and prior attempts were directly rechecked.

No peer or shared-root file was edited.

## 3. Primary source and current-status pass

The primary source was rechecked. Definition 2.1 says an FBM is a continuous real-indexed process `X` for which there are random times `S_j -> -infinity` a.s. such that every centered future

\[
(X_{S_j+t}-X_{S_j})_{t\ge0}
\]

is standard Brownian motion. Definition 2.2 gives decomposable FBMs by concatenating independent Brownian motions stopped at a.s.-finite stopping times.

Theorem 4.3 is the source benchmark for the parabolic strip

\[
c_1\sqrt{|t|}\le x\le c_2\sqrt{|t|},\qquad t\le0,
\]

with the Ornstein--Uhlenbeck/Sturm--Liouville exponent `lambda_0(c1,c2)`: `lambda_0>=1` gives the universal asymptotic obstruction; `lambda_0<=1` gives decomposable asymptotic confinement; and if `c1<=0<=c2` and `lambda_0<1`, a decomposable FBM is pointwise confined for all `t<=0`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Lévy question is Problem 7.9 and is not part of I0077.

Fresh bounded searches dated 2026-09-17 Asia/Jerusalem included:

- `"Forward Brownian Motion" "Problem 7.8" Burdzy Scheutzow`;
- later-author and citing-paper queries around arXiv:1302.6958;
- `aperiodic moving boundary Ornstein-Uhlenbeck survival`;
- `almost periodic parabolic principal eigenvalue Dirichlet`;
- `time heterogeneous parabolic generalized principal eigenvalue Nadin Rossi`;
- `Brownian square root moving boundary aperiodic`;
- `Ornstein-Uhlenbeck time dependent absorbing interval`.

I found no later paper explicitly resolving exact Problem 7.8 or stating the FBM theorem below. This is **bounded negative evidence only, not a novelty certificate**.

The PDE/operator mechanism is not claimed novel. Nadin's 2009 work develops principal eigenvalues for time-periodic parabolic operators. Berestycki--Nadin--Rossi (2025) develop generalized principal eigenvalues for time-heterogeneous parabolic operators and explicitly include periodic, almost-periodic, uniquely ergodic and random stationary regimes. The result below deliberately avoids claiming a new general spectral theory: it uses only OU reversibility, a static Dirichlet Rayleigh bound, contraction, positive pulse density and Borel--Cantelli, then transfers the terminal-time obstruction to FBMs.

The tool's PDF text extraction was available for the source. Two attempted page-image screenshots returned cache-miss failures; no OCR inference was substituted for unavailable screenshots.

## 4. New family and theorem

Let `L,U:R->R` be continuous and bounded with

\[
L(r)<U(r)\qquad\text{for every }r\in\mathbb R.
\]

Define the backward tube

\[
D_{L,U}
=
\Bigl\{(t,x):t<0,\ 
\sqrt{|t|}\,L(\log|t|)
\le x\le
\sqrt{|t|}\,U(\log|t|)
\Bigr\}\cup\{(0,0)\}.
\tag{4.1}
\]

Because `L,U` are bounded, both walls tend to `0` as `t↑0`.

Assume there are constants

\[
\tau>0,\qquad G\ge\tau,\qquad \eta>0,
\qquad \ell_*<u_*,
\tag{4.2}
\]

and a bi-infinite increasing sequence `(a_k)_{k in Z}` such that:

1. the pulse intervals `I_k=[a_k,a_k+tau]` are disjoint;
2. `a_{k+1}-a_k<=G` for every `k`;
3. throughout every pulse,

\[
[L(r)-2\eta,\ U(r)+2\eta]
\subseteq [\ell_*,u_*];
\tag{4.3}
\]

4. with

\[
d=u_*-\ell_*,\qquad
M=\max\{|\ell_*|,|u_*|\},
\]

the explicit pulse exponent

\[
\boxed{
\kappa
:=
\frac{\tau}{G}
\frac{\pi^2e^{-M^2/2}}{2d^2}
>1.
}
\tag{4.4}
\]

No periodicity or symmetry is assumed.

### Theorem I0077-R07-T8 — aperiodic/asymmetric positive-density pulse obstruction

Under (4.2)--(4.4), every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\!\left(
\exists R<\infty:\ 
\sqrt u\,L(\log u)
\le X_{-u}\le
\sqrt u\,U(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T8}
\]

Therefore no FBM can be pointwise confined in `D_{L,U}` on the whole negative half-line either.

The theorem is source-appropriate: it gives a universal clause analogous to Theorem 4.3(i), but for a genuinely moving nonparabolic corridor.

## 5. Move #15 — BREAK THE SYMMETRY ON PURPOSE

Run 6 used a symmetric exactly periodic tube. This run removes both conveniences.

Under the Lamperti transform

\[
Y_r=e^{-r/2}B_{e^r},
\tag{5.1}
\]

standard Brownian motion becomes stationary Ornstein--Uhlenbeck motion with generator

\[
\mathcal A
=\frac12(\partial_{xx}-x\partial_x)
\tag{5.2}
\]

and invariant Gaussian probability measure

\[
\gamma(dx)=(2\pi)^{-1/2}e^{-x^2/2}\,dx.
\]

The moving Brownian event

\[
\sqrt s\,h_-(\log s)\le B_s\le\sqrt s\,h_+(\log s),
\qquad R\le s\le T,
\]

becomes OU survival in the moving interval `(h_-(r),h_+(r))` for `log R<=r<=log T`.

For the static interval `I_*=(ell_*,u_*)`, let `lambda_*` be the principal Dirichlet eigenvalue of killed OU. Its Rayleigh quotient is

\[
\lambda_*
=
\inf_{0\ne f\in H^1_0(I_*)}
\frac{\frac12\int_{I_*}|f'|^2e^{-x^2/2}\,dx}
{\int_{I_*}f^2e^{-x^2/2}\,dx}.
\]

On `I_*`, `e^{-x^2/2}>=e^{-M^2/2}` in the numerator and `e^{-x^2/2}<=1` in the denominator. The ordinary interval Dirichlet Poincaré inequality gives

\[
\int_{I_*}|f'|^2dx
\ge
\left(\frac\pi d\right)^2\int_{I_*}f^2dx.
\]

Hence

\[
\boxed{
\lambda_*
\ge
\frac{\pi^2e^{-M^2/2}}{2d^2}.
}
\tag{5.3}
\]

This proof does not require `I_*` to be centered.

Let `Q_{r,s}` be the killed OU evolution in the twice-padded moving corridor

\[
J(v)=(L(v)-2\eta,U(v)+2\eta).
\]

OU evolution is contractive on `L^2(gamma)`, and killing is multiplication by an indicator, hence contractive too. During each pulse `I_k`, (4.3) gives `J(v) subset I_*`. Positive-kernel domination by OU killed in the static interval `I_*` therefore gives

\[
\|Q_{a_k,a_k+\tau}\|_{2\to2}
\le e^{-\lambda_*\tau}.
\tag{5.4}
\]

All nonpulse pieces cost norm at most `1`. Exact centered symmetry and exact periodicity have disappeared: the only input is one fixed containing interval on each pulse.

**Outcome #15: success.** The spectral-decay mechanism survives both spatial asymmetry and temporal aperiodicity.

## 6. Move #7 — TAKE THE LIMIT: replace a Floquet period by pulse density

Let `H=s-r`. Since consecutive pulse starts are at most `G` apart, after losing at most one pulse at each endpoint and the terminal length `tau`, the number `N(r,s)` of complete pulse intervals contained in `[r,s]` satisfies

\[
N(r,s)
\ge
\frac{H}{G}-C_0,
\tag{6.1}
\]

where one may take the finite constant

\[
C_0=2+\frac\tau G.
\]

Indeed, the first start at or after `r` occurs before `r+G`, and thereafter each next start appears within another `G`; restricting the last start to `<=s-tau` loses only the displayed endpoint allowance.

Combining (5.4) over all complete pulses gives

\[
\|Q_{r,s}\|_{2\to2}
\le
\exp\{-\lambda_*\tau N(r,s)\}
\le
C_1e^{-\kappa H},
\tag{6.2}
\]

where

\[
C_1=e^{\lambda_*\tau C_0}<\infty,
\qquad
\kappa=\frac{\tau}{G}\lambda_*.
\]

Starting OU in its invariant law `gamma`, Cauchy--Schwarz gives survival probability at most the `L^2` operator norm. Returning to physical time,

\[
\boxed{
\mathbb P\!\left(
\sqrt s[L(\log s)-2\eta]
\le B_s\le
\sqrt s[U(\log s)+2\eta]
\ \forall s\in[R,T]
\right)
\le
C_1(T/R)^{-\kappa}.
}
\tag{6.3}
\]

The important quantity is not a Floquet eigenvalue but the long-log-time dissipation rate `pulse density x static killed-OU eigenvalue`. Assumption (4.4) makes it strictly larger than `1`.

**Outcome #7: success.** Exact scale periodicity is unnecessary; a positive lower density of sufficiently narrow logarithmic pulses is enough.

## 7. Continuum terminal times: the dependence claim needed for FBMs

The source FBM witness times need not be integers. We therefore prove the continuum-terminal version explicitly rather than using an invalid integer-only reduction.

Fix deterministic `R_0>0`. For standard Brownian motion `B`, define

\[
G(t;R_0)=
\left\{
\sqrt s[L(\log s)-\eta]
\le B_{t-s}-B_t
\le\sqrt s[U(\log s)+\eta]
\quad\forall s\in[R_0,t]
\right\}.
\tag{7.1}
\]

We claim

\[
\boxed{
\mathbb P\{G(t;R_0)\text{ occurs for arbitrarily large }t\}=0.
}
\tag{7.2}
\]

For integer `n`, let

\[
M_n=\max_{0\le k\le n}
\operatorname{osc}_{[k,k+2]}B.
\]

A reflection-principle/Gaussian-tail union bound gives, for all sufficiently large `n`,

\[
\mathbb P\{M_n>8\sqrt{\log n}\}\le8n^{-3}.
\tag{7.3}
\]

Set

\[
R_n=\left\lceil\frac{256}{\eta^2}\log n\right\rceil.
\tag{7.4}
\]

Then for `s>=R_n`,

\[
2M_n\le16\sqrt{\log n}\le\eta\sqrt s
\tag{7.5}
\]

outside the event in (7.3).

Suppose some `t in [n,n+1]` satisfies `G(t;R_0)` and `M_n<=8 sqrt(log n)`. For every `s in [R_n,n]`,

\[
\begin{aligned}
&|(B_{n-s}-B_n)-(B_{t-s}-B_t)|\\
&\qquad\le
|B_{n-s}-B_{t-s}|+|B_n-B_t|
\le2M_n
\le\eta\sqrt s.
\end{aligned}
\tag{7.6}
\]

Thus the integer-terminal reversed path satisfies the **twice-padded** corridor on `[R_n,n]`.

For deterministic `n`, the reversed increment process `(B_{n-s}-B_n)_{0<=s<=n}` has standard Brownian law up to an irrelevant sign/reflection. The reflected moving interval has the same width, the same `M`, and the same eigenvalue bound. Therefore (6.3) gives

\[
\mathbb P\{\exists t\in[n,n+1]:G(t;R_0)\}
\le
8n^{-3}
+C_1(n/R_n)^{-\kappa}.
\tag{7.7}
\]

Since `R_n=O(log n)` and `kappa>1`,

\[
\sum_n n^{-\kappa}(\log n)^\kappa<\infty.
\]

Hence the right side of (7.7) is summable. Borel--Cantelli proves (7.2).

Every dependence statement has now been exposed: no terminal-time independence is assumed; arbitrary real terminal times are controlled by deterministic integer intervals and a Brownian modulus event.

## 8. Proof of T8: transfer from Brownian terminal times to every FBM

Assume contrariwise that an FBM `X` has eventual confinement event

\[
E=
\left\{
\exists R<\infty:
\sqrt uL(\log u)\le X_{-u}\le\sqrt uU(\log u)
\quad\forall u\ge R
\right\}
\]

with probability `q>0`.

Choose deterministic `R_0` so large that

\[
E_0=
\left\{
\sqrt uL(\log u)\le X_{-u}\le\sqrt uU(\log u)
\quad\forall u\ge R_0,
\quad |X_0|\le\eta\sqrt{R_0}
\right\}
\]

has probability at least `q/2`. This is possible because the random eventual threshold is finite on `E` and `X_0` is finite almost surely.

By the FBM definition there are witness times `S_j->-infinity` a.s. such that

\[
B^{(j)}_r=X_{S_j+r}-X_{S_j},\qquad r\ge0,
\tag{8.1}
\]

is standard Brownian motion for every fixed `j`. Put `T_j=-S_j`; then `T_j->infinity` a.s. For `R_0<=s<=T_j`,

\[
B^{(j)}_{T_j-s}-B^{(j)}_{T_j}
=X_{-s}-X_0.
\tag{8.2}
\]

On `E_0`, since `|X_0|<=eta sqrt(R_0)<=eta sqrt s`, (8.2) lies in the once-padded corridor, so `G(T_j;R_0)` holds for the standard Brownian path `B^{(j)}` whenever `T_j>=R_0`.

Let

\[
p_N=
\mathbb P\{\exists t\ge N:G(t;R_0)\text{ for a standard Brownian motion}\}.
\]

By (7.2), `p_N downarrow 0`. Choose `N` with `p_N<q/4`, then choose deterministic `j` with

\[
\mathbb P(E_0\cap\{T_j<N\})<q/4
\]

using `T_j->infinity` a.s. On `E_0 cap {T_j>=N}`, `G(T_j;R_0)` occurs, so

\[
q/4
<
\mathbb P(E_0\cap\{T_j\ge N\})
\le p_N
<q/4,
\]

a contradiction.

No independence between `E_0`, `S_j`, and the witness Brownian path was used. No decomposability assumption was used. This proves T8 for **every** FBM. `QED`

## 9. Canonical explicit aperiodic asymmetric representative

Take

\[
\alpha=\sqrt2,\qquad \varepsilon=\frac1{10},
\qquad
a_k=k+\varepsilon\sin(2\pi\alpha k),\quad k\in\mathbb Z.
\tag{9.1}
\]

Then

\[
\frac45\le a_{k+1}-a_k\le\frac65,
\tag{9.2}
\]

because the sine difference has absolute value at most `2`. Set

\[
\tau=\frac25,
\qquad G=\frac65.
\tag{9.3}
\]

The pulse plateaux `P_k=[a_k,a_k+2/5]` are disjoint. On every `P_k`, define

\[
L=-\frac1{10},\qquad U=\frac25.
\tag{9.4}
\]

On each open gap between `P_k` and `P_{k+1}`, interpolate continuously and piecewise-linearly from the narrow values to

\[
(L,U)=(-2,3)
\]

at the midpoint of the gap, then linearly back to the next narrow plateau. Thus `L,U` are continuous and bounded, the corridor is asymmetric, and it has no exact logarithmic period.

Take

\[
\eta=\frac1{40}.
\]

On a pulse, the twice-padded interval is

\[
\left[-\frac1{10}-\frac1{20},
\frac25+\frac1{20}\right]
=
\left[-\frac3{20},\frac9{20}\right]
\subset
\left[-\frac14,\frac12\right]
=:I_*.
\tag{9.5}
\]

For this fixed static containing interval,

\[
d=\frac34,\qquad M=\frac12.
\]

Therefore

\[
\lambda_*
\ge
\frac{\pi^2e^{-1/8}}{2(3/4)^2}
=
\frac{8\pi^2}{9}e^{-1/8}.
\tag{9.6}
\]

Using the elementary strict inequalities `pi^2>9` and `e^{-x}>1-x` for `x>0`,

\[
\lambda_*
>
8\cdot\frac78
=7.
\tag{9.7}
\]

Since

\[
\frac\tau G
=
\frac{2/5}{6/5}
=
\frac13,
\]

we obtain

\[
\boxed{
\kappa>\frac73>1.
}
\tag{9.8}
\]

T8 therefore applies: **every FBM almost surely fails eventual confinement in this explicit aperiodic asymmetric tube.**

### Exact aperiodicity

Suppose `(L,U)` had a nonzero period `P`. The maximal intervals on which `(L,U)` equals its narrow value `(-1/10,2/5)` are exactly the `P_k`, all of the same length `2/5`. Translation by `P` must permute these ordered components, hence for some fixed nonzero integer `m`,

\[
a_{k+m}-a_k=P
\quad\text{for every }k.
\tag{9.9}
\]

But

\[
\begin{aligned}
a_{k+m}-a_k
&=m+\varepsilon
[\sin(2\pi\alpha(k+m))-\sin(2\pi\alpha k)]\\
&=m+2\varepsilon\sin(\pi\alpha m)
\cos(2\pi\alpha k+\pi\alpha m).
\end{aligned}
\tag{9.10}
\]

For irrational `alpha=sqrt2` and nonzero integer `m`, `sin(pi alpha m) != 0`, while the cosine sequence is not constant. Thus (9.9) is impossible. There is no nonzero period.

Brownian rescaling `u -> cu` only translates logarithmic time by `log c`; it cannot turn an aperiodic profile into a periodic one. The new family is therefore not a rescaling or phase shift of run 6.

It is also distinct from the first five families: its normalized corridor is bounded, nonconvergent and aperiodic; it neither tends to a fixed parabolic corridor, nor diverges/collapses as a pure power, nor has a slowly varying logarithmic widening, nor has a positive seam.

Hence it contributes exactly **one** new metric point, regardless of changes to `epsilon`, `alpha`, pulse width or wall levels inside the same aperiodic-positive-density mechanism.

## 10. Move #20 — FIND WHY THE ALGORITHM FAILS

I also tested the source's constructive slow-point/stopping-piece route against the new moving corridor. The obvious **phase-blind** version fails sharply.

A stopping rule depending only on the Brownian piece's age, not on its absolute logarithmic phase, would have to fit every possible phase of the corridor. For the canonical example, the intersection over all phases is exactly the narrow plateau corridor

\[
\left[-\frac1{10},\frac25\right]\sqrt u.
\tag{10.1}
\]

Its static OU eigenvalue satisfies, by the same Rayleigh estimate,

\[
\lambda_0\!\left(-\frac1{10},\frac25\right)
\ge
2\pi^2e^{-2/25}
>
2\cdot9\cdot\frac{23}{25}
=
\frac{414}{25}>1.
\tag{10.2}
\]

Here `e^{-2/25}>1-2/25=23/25`. The source's Brownian slow-point threshold is on the opposite side when `lambda_0>1`: the phase-blind narrow intersection does not supply the slow points used by the constructive `lambda_0<1` mechanism.

This is an exact failure of the **naive phase-blind algorithm**, not a proof that every phase-aware construction is impossible. In particular, T8 already gives a universal nonconfinement theorem only under the stronger positive-density pulse criterion (4.4); the route-failure calculation is not used to inflate that theorem.

**Outcome #20: failed constructive route, with its exact obstruction identified.**

## 11. Exact finite check

The canonical rational constant chain was independently checked with exact `Fraction` arithmetic in

`artifacts/R07/20260916T2322Z_aperiodic_pulse_constants.py`.

Archived output:

`artifacts/R07/20260916T2322Z_aperiodic_pulse_constants.out`.

It verifies

\[
\text{gap}_{min}=4/5,
\quad
\text{gap}_{max}=6/5,
\quad
\tau=2/5,
\quad
\tau/G=1/3,
\quad
d=3/4,
\]

and, after inserting the analytic lower bounds `pi^2>9` and `e^{-1/8}>7/8`, obtains

\[
\lambda_{lower}=7,\qquad
\kappa_{lower}=7/3>1.
\]

The checker output begins `PASS`. The transcendental inequalities themselves are proved on the page and are not mislabeled as finite arithmetic certification.

## 12. Why this is movement rather than another parameterization

Run 6's family had exact discrete scale invariance: after Lamperti transformation the moving domain was periodic. The present family has **no** nonzero log-time period, hence no discrete dilation symmetry at all. Its theorem is proved by lower pulse density, not by one-period repetition or a Floquet operator. Spatial symmetry is also removed.

The structural distinction survives the frozen equivalence group. Brownian scaling corresponds to log-time translation; translation preserves (a)periodicity. Reflection swaps the two asymmetric walls but does not create periodicity. Time/space scalar rescaling cannot turn the irrationally jittered pulse-start sequence into an arithmetic progression.

Therefore the fixed metric moves `6 -> 7`; no parameter choice within T8 is counted separately.

## 13. Honest status, audits, and remaining obligation

**Source status: PARTIAL / open-ended.** T8 answers Problem 7.8 for one more structural family. It does not classify arbitrary space-time shapes and does not settle the open-ended source question globally.

There is no independent T8 audit yet, including no P26 audit. The earlier R06 audit of the run-2 super-LIL gauge theorem is scoped to T2 and does not audit T8. Closure criteria are therefore not met and no `paper_<name>/` folder was created.

The new theorem is analytic. The only finite core was the explicit canonical constant chain, which has the exact checker/output above. The theorem-sized proof is written in full in this report.

The highest-value next question is no longer to add another easy family. It is whether the sufficient pulse-rate condition can be sharpened toward a **general nonautonomous OU critical exponent** that gives both obstruction and existence, rather than only a universal obstruction. Natural unused next moves are #9 RANDOMIZE the pulse environment, #17 LOOK FOR THE EXPONENT ELSEWHERE in generalized principal-eigenvalue/quenched-survival theory, and #28 REPLACE FOR ALL WITH TYPICAL to separate deterministic worst-case pulse density from stationary-ergodic shape laws.

## 14. Runtime/model and permission status

The scheduler limitation is unchanged. The exposed task-update interface has fields for prompt/title, schedule, enablement and timing mode, but no model-family selector and no reasoning-effort selector. GPT-6/maximum is therefore a prompt request, not a verified runtime setting. A real model/reasoning change requires product support for those fields or an authorized owning/admin context with such controls.

Repository reconciliation records historical `You cannot modify this task` errors in some contexts, including an earlier P26 probe, while a later P26 update succeeded from another authorized context. The correct conclusion is context/ownership scoping, not a worker-level bypass. The permitted route is the task's authorized owning context or platform support; creating a duplicate scheduler job is not an authorized workaround.

## 15. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source: "Burdzy--Scheutzow (2014), Forward Brownian Motion, Problem 7.8 / I0077"
  target: "Generalize Theorem 4.3 to genuinely distinct nonparabolic space-time shape families"
  metric: "number of distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 6
  after: 7
  status: PARTIAL
  unchanged_count: 0
  exact_evidence:
    - "runs/R07/20260916T2322Z_i0077_aperiodic_asymmetric_pulses_07.md"
    - "artifacts/R07/20260916T2322Z_aperiodic_pulse_constants.py @ 7c08e02c2915bbb8bc8e52de389e7c61e94fdeb6"
    - "artifacts/R07/20260916T2322Z_aperiodic_pulse_constants.out @ 4deeb3c7f25e8f80b1384fde4befd85e11dfdc4b"
  audits:
    incoming_T8: []
    outgoing: []
  prior_art_scope: "bounded dated search; generalized parabolic principal-eigenvalue theory acknowledged; novelty UNVERIFIED"
```
