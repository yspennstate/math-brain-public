Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 14 -> 15 genuinely distinct nonparabolic shape families; Section-B moves tried: #6 DEFORM TO A SOLVABLE POINT, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 15: periodically gated disconnected parabolic fans

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and fixed metric

The frozen R07 metric remains:

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo Brownian rescaling/reflection/translation and mere parameter changes inside one structural family.

The preceding authoritative report is

`runs/R07/20260917T0624Z_i0077_fat_cantor_fans_14.md`,

which moved the metric `13 -> 14` for perfect totally disconnected/fat-Cantor parabolic fans. That report explicitly left **time-dependent gated disconnected fans** as the next high-value obstruction and proposed the triple `6,12,20`. I use exactly that triple here; it differs from the preceding `4,11,23`.

This run adds exactly one new structural family: **periodically gated disconnected parabolic fans**, whose normalized cross-section has two connected components during one positive-measure set of logarithmic phases and merges to a single narrow component during another positive-measure set of phases. Different periods, gate duty cycles, branch endpoints and interpolation speeds are not counted separately.

The metric moves

\[
\boxed{14\longrightarrow15}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains retired by its immutable handoff. No historical R07 file was modified or deleted.

## 2. Required repository/source reread

Before doing new mathematics I recovered the current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the searchable R07/I0077 report chain through run 14;
- the R15 Burdzy–Scheutzow Problem-7.2 six-run handoff and newer R15 reports, which show R15 has rotated to a different source;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`operations/claims/I0077.md` still names R07 as the exclusive provisional owner and still has the text `PENDING_ADMISSION, not READY`. The current owner instruction nevertheless assigns this exact source target to R07. I do not rewrite the canonical claim or turn a pending shared-root label into a fabricated READY state. `INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no Problem-7.8 exclusion. `QUEUE.md` lists I0077 distinctly from assigned Problem 7.2. The root `RESULTS.md` R07/FPP row is stale by its own warning and is not used as the current mathematical baseline.

The large intake JSONLs cannot be read wholesale through the exposed connector without truncation. The intake reread is therefore honestly **PARTIAL / targeted**, not described as complete. The full current R07 report chain itself is available and was recovered; I do not restart from the intake snippet.

## 3. Primary source recovered exactly

I reread arXiv:1302.6958v4, including Definitions 2.1–2.2, Theorem 4.3, its proof, and the open-problem page.

Definition 2.1: an FBM has random witness times `S_n -> -infinity` such that for each witness

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent Brownian pieces stopped at finite stopping times.

Theorem 4.3 says, for a fixed parabolic normalized interval `[c_1,c_2]`:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal normalized limsup/liminf obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM has the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM is confined pointwise to the exact parabola for all negative times.

The source proof of part (i) is already a terminal-time/summability argument: it proves summability of Brownian survival probabilities when the killed-OU exponent is greater than one, then converts that to an FBM contradiction using a sufficiently far-left Brownian witness. This is the source-appropriate template generalized below.

Problem 7.8 is exactly the single sentence

> “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?”

The following forward-Lévy sentence is separately Problem 7.9 and is not part of I0077.

## 4. Fresh current-literature check, dated 2026-09-17

Fresh bounded searches included:

- exact title + `Problem 7.8` + `other space-time shapes`;
- exact source wording and later Burdzy/Scheutzow/citing-paper variants;
- `time-periodic parabolic principal eigenvalue moving domain Dirichlet`;
- `Ornstein-Uhlenbeck periodic boundary survival`;
- `time-periodic domains disconnected principal eigenvalue parabolic` and moving/disconnected-domain variants.

Relevant prior art recovered:

- Grégoire Nadin, *The principal eigenvalue of a space–time periodic parabolic operator*, Annali di Matematica 188 (2009), 269–295: general periodic-parabolic principal-eigenvalue machinery.
- L. Sacerdote, *Asymptotic behaviour of Ornstein–Uhlenbeck first-passage-time density through periodic boundaries* (1990): periodic OU boundary first-passage asymptotics.
- Jane Allwright, *Reaction–Diffusion Problems on Time-Periodic Domains*, J. Dyn. Diff. Eq. 37 (2025), 71–94, published online 2023: moving time-periodic Dirichlet domains and principal periodic eigenvalues. Its setup explicitly maps each moving domain to a fixed **connected** reference domain, so it is nearby PDE prior art rather than the topology-changing FBM result below.
- Modern nonautonomous OU survival papers likewise confirm that periodic/nonautonomous absorbing-boundary survival is a classical subject.

I found no later paper in this bounded dated search explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the FBM theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**. I do not claim the periodic-parabolic/OU spectral mechanism itself is new.

## 5. The new shape class

Let `D(r)` be a nonempty compact subset of `R` for every `r in R`, periodic with period `P>0`. Define the log-periodic parabolic-scale region

\[
\mathcal G_D
=
\left\{(-u,x):u>0,\ \frac{x}{\sqrt u}\in D(\log u)\right\}\cup\{(0,0)\}.
\tag{5.1}
\]

For `eta>0`, write

\[
D(r)^{+\eta}=D(r)+[-\eta,\eta]
\tag{5.2}
\]

for the closed Minkowski padding.

Assume there is an interval `J subset [0,P)` of length `tau>0`, a number `eta>0`, and `c>0` such that on every copy of the gate phase,

\[
\boxed{
D(r)^{+2\eta}\subset[-c,c]
\quad\text{whenever }r\bmod P\in J.
}
\tag{5.3}
\]

Let

\[
\lambda_c:=\lambda_0(-c,c),
\qquad
\kappa:=\frac{\tau}{P}\lambda_c.
\tag{5.4}
\]

The profile may be disconnected outside the gates, may merge and split as `r` evolves, and need not satisfy any nesting assumption.

## 6. I0077-R07-T16 — periodic gate obstruction theorem

**Status of theorem: PROVED on the page below. Overall source status remains PARTIAL.**

If the gate condition (5.3) holds and

\[
\boxed{\kappa>1,}
\tag{6.1}
\]

then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\frac{X_{-u}}{\sqrt u}\in D(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T16}
\]

Thus a repeated narrow gate can rule out eventual confinement even when the shape is disconnected and wide/subcritical during the rest of each logarithmic period.

The statement is deliberately one-sided: `kappa<=1` is **not** claimed to imply existence. The theorem is a complete sufficient obstruction, not a false sharp phase claim.

## 7. Proof of T16, part I: the conserved object is `L^2(gamma)`

This is method #12.

Let `B` be standard Brownian motion and, for a deterministic integer terminal time `n`, define reversed increments

\[
Z^{(n)}_u=B_{n-u}-B_n,
\qquad 0\le u\le n.
\tag{7.1}
\]

As a process in `u`, `Z^(n)` has the law of standard Brownian motion on `[0,n]`. Its Lamperti transform

\[
Y_r=e^{-r/2}Z^{(n)}_{e^r}
\tag{7.2}
\]

is the stationary Ornstein–Uhlenbeck process with generator

\[
\mathcal A=\frac12\partial_{xx}-\frac12x\partial_x
\tag{7.3}
\]

and invariant standard Gaussian measure `gamma`.

The key conserved Hilbert space is `L^2(gamma)`. Free OU evolution is a contraction in this norm. Multiplication by an indicator (additional killing) is also a contraction. During a complete gate interval of logarithmic length `tau`, survival in the twice-padded target implies survival in `(-c,c)`. The killed-OU semigroup on `(-c,c)` has operator norm

\[
\|K_\tau\|_{2\to2}=e^{-\lambda_c\tau}.
\tag{7.4}
\]

Therefore every complete gate costs at least the fixed factor `e^{-lambda_c tau}`, while all motion between gates can be discarded at unit operator cost.

If `[r,s]` contains `N(r,s)` complete gate copies, composition and Cauchy–Schwarz give

\[
\mathbb P\left(
Y_q\in D(q)^{+2\eta}\ \forall q\in[r,s]
\right)
\le e^{-\lambda_c\tau N(r,s)}.
\tag{7.5}
\]

Because the gates repeat with period `P`,

\[
N(r,s)\ge \frac{s-r}{P}-2.
\tag{7.6}
\]

Hence, with a finite constant `C=C(c,tau)`, for `1<=R<T`,

\[
\boxed{
\mathbb P\left(
\frac{Z^{(n)}_u}{\sqrt u}\in D(\log u)^{+2\eta}
\ \forall u\in[R,T]
\right)
\le C(T/R)^{-\kappa}.
}
\tag{7.7}
\]

For an integer terminal `n` we will use `T=n`.

No Floquet theorem is needed for this estimate. It is exactly the gate-by-gate `L^2(gamma)` dissipation that run 14 was missing.

## 8. Proof of T16, part II: real Brownian terminal times

The FBM witness time is random and need not be an integer, so (7.7) alone is insufficient. The next lemma makes the terminal-time step explicit instead of assuming independence.

For a real terminal `t>0` and fixed `R_0>0`, call `t` **once-padded good** if

\[
\frac{B_{t-u}-B_t}{\sqrt u}
\in D(\log u)^{+\eta}
\qquad\forall u\in[R_0,t].
\tag{8.1}
\]

### Lemma 8.1 — boundedness of good real terminals

If `kappa>1`, then for every deterministic `R_0>0`, almost surely the set of once-padded good terminal times is bounded.

### Proof

For `n>=3`, set

\[
M_n=\max_{0\le k\le n}\operatorname{osc}_{[k,k+2]}B.
\tag{8.2}
\]

If the oscillation on one interval of length two exceeds `a`, then the Brownian path relative to its left endpoint has absolute supremum greater than `a/2`. The reflection principle plus the Gaussian Chernoff bound therefore gives

\[
\mathbb P(M_n>8\sqrt{\log n})\le 8n^{-3}
\tag{8.3}
\]

for all sufficiently large `n`.

Define

\[
R_n=\left\lceil 256\eta^{-2}\log n\right\rceil.
\tag{8.4}
\]

For large `n`, `R_n<n` and `R_n>=R_0`. If `t in [n,n+1]`, then for every `u in [R_n,n]`,

\[
\begin{aligned}
&\left|
(B_{t-u}-B_t)-(B_{n-u}-B_n)
\right|\\
&\qquad\le
|B_{t-u}-B_{n-u}|+|B_t-B_n|
\le2M_n.
\end{aligned}
\tag{8.5}
\]

On the event `M_n<=8 sqrt(log n)`, (8.4) implies

\[
\frac{2M_n}{\sqrt u}
\le
\frac{16\sqrt{\log n}}{\sqrt{R_n}}
\le\eta.
\tag{8.6}
\]

Consequently, if there is a once-padded good real terminal `t in [n,n+1]`, then outside the modulus failure event the integer terminal `n` satisfies the **twice-padded** condition throughout `[R_n,n]`. By (7.7),

\[
\mathbb P\{\exists\text{ once-padded good }t\in[n,n+1]\}
\le
8n^{-3}+C(n/R_n)^{-\kappa}.
\tag{8.7}
\]

Since `R_n=O(log n)` and `kappa>1`,

\[
\sum_n n^{-\kappa}(\log n)^\kappa<\infty.
\tag{8.8}
\]

The right side of (8.7) is summable. Borel–Cantelli proves that only finitely many unit intervals contain a good real terminal. QED.

This is the exact terminal-time crossing compiler required by run 14; no deterministic regularity of an arbitrary FBM trajectory at predetermined far-past times was inserted.

## 9. Proof of T16, part III: transfer to an arbitrary FBM without independence

Assume for contradiction that the T16 confinement event has positive probability. By taking a countable union over deterministic thresholds and then truncating `|X_0|`, choose deterministic `R_0,A<infinity` and `q>0` such that

\[
E=
\left\{
\frac{X_{-u}}{\sqrt u}\in D(\log u)\ \forall u\ge R_0,
\quad |X_0|\le A
\right\}
\tag{9.1}
\]

has probability `q`. Increase `R_0` if necessary so that

\[
A/\sqrt{R_0}\le\eta.
\tag{9.2}
\]

By Lemma 8.1, for standard Brownian motion the events

\[
H_T=\{\exists\text{ once-padded good terminal }t\ge T\}
\tag{9.3}
\]

decrease to the empty event almost surely. Hence choose deterministic `T>=R_0` with

\[
\mathbb P_{BM}(H_T)<q/4.
\tag{9.4}
\]

Let `S_j -> -infinity` be the FBM witness sequence. Choose one **deterministic index** `j` so far along the sequence that

\[
\mathbb P(-S_j<T)<q/4.
\tag{9.5}
\]

The single process

\[
B^{(j)}_s=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\tag{9.6}
\]

is standard Brownian motion, with no conditioning and no independence assumption.

On `E cap {-S_j>=T}`, put `t=-S_j`. For every `u in [R_0,t]`,

\[
B^{(j)}_{t-u}-B^{(j)}_t
=X_{-u}-X_0.
\tag{9.7}
\]

By (9.1) and (9.2),

\[
\frac{X_{-u}-X_0}{\sqrt u}
\in D(\log u)^{+\eta}.
\tag{9.8}
\]

Thus `t` is a once-padded good terminal for the standard Brownian path `B^(j)`. But

\[
\mathbb P(E\cap\{-S_j\ge T\})
\ge q-q/4=3q/4,
\tag{9.9}
\]

whereas the Brownian event containing it has probability less than `q/4` by (9.4). Contradiction. This proves T16.

The proof never conditions on the random witness time and never assumes that a witness time is independent of its Brownian future. That dependence issue is exactly why the preceding run refused to claim a gate theorem without this compiler.

## 10. Method #6 — deform a solvable disconnected fan and track the obstruction

I now build an explicit continuous topology-changing profile whose **zero-gate endpoint is source-admissible**, while a positive gate duty cycle satisfies T16.

### 10.1 A source-subcritical positive branch exists, explicitly anchored at `(0,3)`

First prove

\[
\boxed{\lambda_0(0,3)<1.}
\tag{10.1}
\]

Use the trial function `f(x)=x(3-x)` in the OU Dirichlet Rayleigh quotient. Put

\[
I_0=\int_0^3e^{-x^2/2}\,dx,
\qquad E=e^{-9/2}.
\tag{10.2}
\]

Integration by parts gives

\[
N:=\frac12\int_0^3|f'|^2e^{-x^2/2}\,dx
=\frac{13}{2}I_0-6,
\tag{10.3}
\]

and

\[
D:=\int_0^3f^2e^{-x^2/2}\,dx
=12I_0+3E-12.
\tag{10.4}
\]

Taylor's formula with positive fourth-order remainder gives, for `z>=0`,

\[
e^{-z}\ge1-z+\frac{z^2}{2}-\frac{z^3}{6}.
\tag{10.5}
\]

Integrating (10.5) with `z=x^2/2` over `[0,8/5]` yields the exact rational bound

\[
I_0>
\frac{601336}{546875}
>
\frac{12}{11}.
\tag{10.6}
\]

Therefore

\[
D-N=3E+\frac{11}{2}I_0-6>0,
\tag{10.7}
\]

so the trial Rayleigh quotient is strictly below one, proving (10.1).

By the endpoint continuity of `lambda_0` used in the source itself, choose once and for all

\[
0<\delta<1/8
\quad\text{such that}\quad
\lambda_0(\delta,3)<1.
\tag{10.8}
\]

By symmetry, `lambda_0(-3,-delta)<1` as well. Thus the **static disconnected fan**

\[
D_0=[-3,-\delta]\cup[\delta,3]
\tag{10.9}
\]

is source-admissible for eventual confinement: shrink one branch slightly while retaining exponent `<1`, apply Theorem 4.3(ii), and the strict interior margin makes the resulting decomposable FBM eventually stay in that branch, hence in `D_0`.

### 10.2 A Hausdorff-continuous periodic gate deformation

Fix

\[
a=1/4.
\tag{10.10}
\]

For a duty parameter `theta in [0,1/2]`, define a period-one profile. At `theta=0`, simply set `D_theta(r)=D_0` for every `r`.

For `theta>0`, use phase `s=r mod 1`. Center a gate plateau of length `theta` at `s=1/2`. Immediately to either side place transition intervals of length `theta/4`; on the remaining phases set `D_theta=D_0`.

During a transition use a parameter `q in [0,1]` increasing from the outer state to the gate and set

\[
M(q)=3-(3-a)q,
\qquad
 d(q)=\delta(1-q),
\tag{10.11}
\]

\[
D_q=[-M(q),-d(q)]\cup[d(q),M(q)].
\tag{10.12}
\]

At `q=0` this is `D_0`; at `q=1` the two pieces meet at zero and become the connected gate

\[
D_{gate}=[-a,a].
\tag{10.13}
\]

Reverse this interpolation on the exit transition. The resulting `D_theta` is periodic and Hausdorff-continuous. Its number of connected components genuinely changes with phase.

For the canonical value

\[
\theta=1/2,
\tag{10.14}
\]

the phase decomposition is especially simple:

- outer disconnected plateau: `[0,1/8] union [7/8,1)`, total length `1/4`;
- two transition windows: `[1/8,1/4]` and `[3/4,7/8]`, total length `1/4`;
- connected narrow gate: `[1/4,3/4]`, length `1/2`.

So this is not an instantaneous topological surgery; the two branches approach, merge continuously, stay merged for positive logarithmic time, and split continuously again.

## 11. Explicit gate exponent and exact certificate

Take

\[
\eta=1/16.
\tag{11.1}
\]

The twice-padded canonical gate is contained in

\[
[-a-2\eta,a+2\eta]=[-3/8,3/8].
\tag{11.2}
\]

Thus `c=3/8`. The OU Dirichlet Rayleigh/Poincaré bound gives

\[
\lambda_c
\ge
\frac{\pi^2e^{-c^2/2}}{8c^2}
=
\frac{8\pi^2}{9}e^{-9/128}.
\tag{11.3}
\]

Using only the exact inequalities `pi^2>9` and `e^{-x}>1-x` for `x>0`,

\[
\boxed{
\lambda_c>
8\left(1-\frac9{128}\right)
=\frac{119}{16}.
}
\tag{11.4}
\]

For the canonical gate length `tau=theta=1/2` and period one,

\[
\boxed{
\kappa=\frac12\lambda_c>rac{119}{32}>1.
}
\tag{11.5}
\]

T16 therefore gives

\[
\boxed{
\text{Every FBM fails eventual confinement in the canonical gated disconnected fan.}
}
\tag{11.6}
\]

More generally, the same explicit lower bound shows universal obstruction for every duty cycle

\[
\theta\ge\frac{16}{119}
\tag{11.7}
\]

within this deformation, because then `theta lambda_c>1`. I do **not** classify the interval `0<theta<16/119`.

The finite/rational inequalities were checked exactly after the mathematical route was established, not before it:

- `artifacts/R07/20260917T0724Z_gated_fan_constants_check.py` @ creation commit `2f9265aef99fc4327a03dd950192df4671c1315c`;
- `artifacts/R07/20260917T0724Z_gated_fan_constants_check.out` @ creation commit `4a9b7684ac8ccd13b9440523dd334291e3dcfb19`.

The executed output begins `PASS` and records

\[
 c=3/8,
\quad
\lambda_c>119/16,
\quad
\kappa>119/32,
\tag{11.8}
\]

as well as the exact Taylor-integral comparison

\[
\frac{601336}{546875}-\frac{12}{11}
=
\frac{52196}{6015625}>0.
\tag{11.9}
\]

The checker certifies only these finite inequalities; T16 is proved on the page.

## 12. What method #6 actually learned

At `theta=0`, the normalized domain is the fixed two-branch fan `D_0`; one branch has `lambda<1`, so a decomposable FBM can eventually live in that branch.

As the gate duty cycle is turned on, the branch gap closes during a controlled transition and every eventual path must repeatedly pass through the narrow merged gate. At `theta=1/2` — and in fact throughout the certified region (11.7) — the accumulated gate dissipation makes Brownian terminal opportunities summable, so **no FBM at all** can remain eventually in the shape.

Thus the solvable deformation tracks an exact sufficient obstruction:

\[
\boxed{
\text{gate spectral mass per log period}
=\theta\lambda_c>1.
}
\tag{12.1}
\]

This is stronger information than simply giving another narrow moving tube. It identifies a topology-changing deformation from a source-admissible disconnected endpoint to a universal-obstruction regime.

## 13. Method #20 — why the obvious algorithm fails

Run 14 isolated the problem correctly. In a static disconnected fan, continuity forces a confined normalized path to choose one component forever. If that component is subcritical, the source construction can exploit it.

The obvious attempt for a gated fan is to keep following one subcritical branch and cross to the other side whenever the gap closes. The missing issue is not geometric connectivity; it is **terminal-time abundance**. An arbitrary FBM witness can occur at a random, path-dependent time, so one cannot justify the crossings by placing deterministic modulus bounds at predetermined far-past gate times.

T16 supplies the missing source-valid statement. It does not try to schedule branch switches. It bounds **all possible Brownian terminal times**. Every complete narrow gate costs `e^{-lambda_c tau}` in the conserved Gaussian `L^2` norm; real terminal times are discretized with a summable Brownian modulus error; and the final FBM contradiction uses one deterministic witness index without conditioning on its location.

So the algorithm fails precisely when the repeated-gate survival exponent crosses the summability threshold `1`. That is the exact obstruction that the prior run could not state rigorously.

## 14. Why this is a genuinely new metric point

This family is not a new parameter value of any of the preceding fourteen classes.

- Runs 6–9 used periodic/aperiodic/sparse **connected interval** cross-sections; the normalized slice had one component at every phase.
- Runs 13–14 used **static disconnected** normalized cross-sections; their component structure did not vary with logarithmic time.
- The present family has two components during a positive-measure phase set and one component during another positive-measure phase set, with Hausdorff-continuous merging and splitting.

Brownian rescaling translates logarithmic phase. Reflection/translation do not turn a phase-varying component count into an everywhere-connected or time-static component count. The invariant statement

> “the number of connected components of the normalized slice is nonconstant over one logarithmic period”

survives the frozen trivial equivalences.

Accordingly the whole periodically gated disconnected class is counted once:

\[
\boxed{14\to15}.
\]

Changing `theta`, `delta`, the period, or the interpolation is not counted again.

## 15. Closure state

Problem 7.8 remains **PARTIAL**, not closed. T16 and the canonical family have a full written proof and an exact finite-arithmetic self-check, and a fresh bounded prior-art search is recorded, but they do **not** yet have:

1. the required P26 independent end-to-end audit; and
2. a second independent OTHER-track audit.

No `paper_<name>/` folder is created. The earlier R06 scoped audit concerned an earlier R07 theorem and does not automatically audit T16.

## 16. Model/scheduler control status

The limitation remains exactly the one recorded in the current repository policy and `RESULTS.md`: the exposed task control surface has fields for prompt/title, schedule, enabled state, and timing mode, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` is prompt text only and this run reports the actual available identity as GPT-5.6 Sol with reasoning `UNVERIFIED`.

A verifiable fix would require the product/API to expose persistent model and reasoning controls together with authenticated run metadata, or action from the authorized owning/admin product surface. Historical `You cannot modify this task` errors are context/ownership scoped: the current root ledger records that P26's full update later succeeded in one authorized context while R-series edits were denied in another. There is no legitimate R07-level permission bypass and no duplicate scheduler should be created. No scheduler change was attempted in this run.

## 17. Next mathematical target

The high-value next question is the **converse/subcritical gated regime**, not another obstruction-only variant:

\[
\theta\Lambda_{gate}<1
\quad\Longrightarrow\quad ?
\tag{17.1}
\]

where `Lambda_gate` should be the true principal Lyapunov/Floquet exponent of the complete topology-changing periodic domain rather than the crude isolated-gate lower bound. A useful next triple, different from `6,12,20`, is:

- `#5 ADD A PARAMETER AND DIFFERENTIATE IN IT` — gate duty/frequency;
- `#14 FIND THE GROUP ACTING` — one-period OU transfer operator;
- `#19 MAKE IT AN ALGORITHM` — a phase-aware decomposable stopping construction if the periodic survival exponent is below one.

The concrete aim is to prove an existence theorem for one gated disconnected profile, or else isolate a rigorous obstruction showing why a principal-exponent `<1` condition still fails to produce source-valid stopping times.

## 18. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source:
    authors: [Krzysztof Burdzy, Michael Scheutzow]
    work: "Forward Brownian Motion"
    year: 2014
    arxiv: "1302.6958"
    locator: "Problem 7.8"
    intake: I0077
  target: >-
    Generalize Theorem 4.3 from parabolic regions to a genuinely distinct
    nonparabolic space-time shape family.
  metric: >-
    Number of genuinely distinct nonparabolic shape families with a complete
    source-appropriate theorem, modulo frozen trivial-equivalence convention.
  before: 14
  after: 15
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_this_run: [6, 12, 20]
  theorem:
    id: I0077-R07-T16
    class: "periodically gated disconnected parabolic fans"
    statement: >-
      For period-P normalized compact profile D(r), if a gate of log-length tau
      per period has twice-padded cross-section contained in [-c,c] and
      (tau/P)*lambda_0(-c,c)>1, then every FBM has probability zero of eventual
      confinement to x/sqrt(u) in D(log u).
    dependence_handling: >-
      Brownian real-terminal compiler plus one deterministic FBM witness index;
      no conditioning on or independence of the witness time.
  new_metric_family:
    name: "periodically gated disconnected parabolic fans"
    topology: >-
      two components on outer phases, Hausdorff-continuous merge to one narrow
      component on a positive-length gate, then split again
    canonical_gate_radius: "a=1/4"
    padding: "eta=1/16; twice-padded c=3/8"
    canonical_gate_length: "theta=tau=1/2, period P=1"
    certified_lambda_lower: "lambda_0(-3/8,3/8) > 119/16"
    certified_kappa_lower: "kappa > 119/32 > 1"
    verdict: "every FBM fails eventual confinement"
    solvable_endpoint: >-
      theta=0 static fan [-3,-delta] union [delta,3], for sufficiently small
      delta>0, has a subcritical branch and admits decomposable eventual confinement
    sufficient_obstruction_region: "theta >= 16/119 for the displayed gate"
    subthreshold_region: "unclassified"
  exact_evidence:
    - "artifacts/R07/20260917T0724Z_gated_fan_constants_check.py @ 2f9265aef99fc4327a03dd950192df4671c1315c"
    - "artifacts/R07/20260917T0724Z_gated_fan_constants_check.out @ 4a9b7684ac8ccd13b9440523dd334291e3dcfb19"
  prior_art: >-
    Nadin 2009 periodic-parabolic principal eigenvalues; Sacerdote 1990 OU periodic
    boundaries; Allwright 2025 time-periodic connected domains. Bounded dated search
    found no explicit later Problem-7.8 resolution or T16; novelty UNVERIFIED.
  source_status: PARTIAL
  source_closure: false
  audits: []
  shared_roots_modified: false
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  scheduler_selector_exposed: false
  next_methods: [5, 14, 19]
```
