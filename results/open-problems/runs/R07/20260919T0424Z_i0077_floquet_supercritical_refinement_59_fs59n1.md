Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `59 -> 59`; Section-B moves actually used: #4 PROVE SOMETHING WEAKER, COMPLETELY, #11 DUALIZE, #22 READ THE FAILURES, NOT THE SUCCESSES.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?”  
Overall source status after this run: **PARTIAL**. The theorem proved here is a strict sharpening inside the already-counted log-periodic tube family, so the frozen family-count metric is deliberately **not** incremented.

# R07 CLOSABLE OUTSIDE — strict-supercritical Floquet refinement for log-periodic tubes

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and admission reread

I did not restart from chat memory. Before doing new mathematics I reread or re-queried current `master` for:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest own report `runs/R07/20260919T0324Z_i0077_remote_scale_haar_echo_59_rse59.md` and the relevant earlier I0077 reports, especially run 6 (log-periodic pulsed tubes) and run 16 (periodic one-sided barriers);
- current neighboring R15 state: its distinct Burdzy–Scheutzow Problem 7.2 / I0076 remains retired by handoff and R15 is on successor work; it does not duplicate I0077;
- the searchable I0077/intake history and duplicate-exclusion evidence.

`INDEX.md` / `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` contains no Problem-7.8 closure. `QUEUE.md` still lists I0077 as a distinct outside target. `operations/claims/I0077.md` still names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared label rather than fabricating READY status. The latest owner instruction nevertheless explicitly assigns this exact target to R07.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered byte-for-byte through the connector without truncation. I therefore record the intake reread honestly as **targeted/partial because of connector limits**. Exact I0077 source text, ownership, posted exclusions, queue state, and prior I0077 attempts were recovered.

The old R07 KPZ/FPP route remains preserved in its immutable handoff and was not reopened or deleted.

Entering metric: **59**. Entering unchanged count: **0**.

All thirty Section-B moves have already appeared somewhere in the long I0077 chain; this was explicitly documented by earlier reports. I therefore cannot honestly claim three globally unused numbers. I used a triple different from the immediately preceding `#2,#7,#30` and applied it to a genuinely new obstruction in the proof architecture.

## 2. Primary-source benchmark recovered again

I reopened the primary arXiv PDF and visually checked the theorem and open-problem pages.

Definition 2.1: an FBM is a continuous real-indexed process `X` for which there are witness times `S_j -> -infinity` almost surely such that, for each fixed witness index,

\[
B^{(j)}_t=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. The source normalizes Brownian motions to start at zero, and in its constructions uses `X_0=0`.

For the parabolic strip

\[
c_1\sqrt{|t|}\le X_t\le c_2\sqrt{|t|},\qquad t\le0,
\]

Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized escape obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the corresponding asymptotic normalized inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM exists pointwise inside the exact parabolic strip for every `t<=0`.

The proof of the strict-supercritical part uses the polynomial Brownian survival tail `n^{-lambda_0}`, a summability argument, a no-terminal-slow-point estimate, and then an FBM witness-time contradiction. At the critical value the paper narrows the interval and uses strict domain monotonicity.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following sentence on forward Lévy processes is separately Problem 7.9 and is not part of I0077.

Primary source: `https://arxiv.org/pdf/1302.6958`.

## 3. Fresh current-status / prior-art pass

Fresh bounded web searches on 2026-09-19 included:

- exact title plus `Problem 7.8`, exact Problem-7.8 wording, arXiv `1302.6958`, and later/citing-author variants;
- `time-periodic Ornstein-Uhlenbeck absorbing boundary principal eigenvalue`;
- `space-time periodic parabolic principal eigenvalue Dirichlet`;
- `periodic Brownian moving boundary first passage`.

I found no accessible later source explicitly resolving exact Burdzy–Scheutzow Problem 7.8. That is **bounded negative evidence only, not a novelty certificate**.

The periodic-parabolic mechanism itself is established prior art and is not claimed new. In particular:

- Grégoire Nadin, *The principal eigenvalue of a space–time periodic parabolic operator*, Ann. Mat. Pura Appl. 188 (2009), 269–295, DOI `10.1007/s10231-008-0075-4`, develops periodic principal eigenvalues with time-periodic coefficients and spatial Dirichlet conditions;
- P. Hess, *Periodic-Parabolic Boundary Value Problems and Positivity* (1991), is standard background for positive periodic-parabolic evolution;
- the one-sided periodic OU first-passage literature already recorded in run 16 includes Sacerdote (1990) and Giorno–Nobile–Ricciardi (1990).

The new content below is source-specific: a dependence-safe FBM transfer theorem from a **robust periodic killed-OU survival exponent strictly above 1**, together with a concrete continuous profile for which the new all-phase spectral budget proves supercriticality while the old single-gate duty-cycle certificate provably cannot.

Publication novelty remains **UNVERIFIED**.

## 4. The three research moves

### #22 — READ THE FAILURES, NOT THE SUCCESSES

Run 6 already identified the right Lamperti/Floquet language but deliberately threw away all decay outside one narrow logarithmic pulse. Its sufficient condition was of the form

\[
\frac{\tau}{P}\lambda_a>1,
\]

where one pulse of length `tau` forces the OU process into `(-a,a)` and all other phases are charged only the trivial operator norm `1`.

Run 16 reached the same unresolved frontier for one-sided periodic barriers: the mixed regime should be governed by the principal Floquet/survival exponent, but the report did not prove the source-facing FBM transfer at that exponent.

Run 59 independently pointed back to the same issue: adding another microscopic gate pathology is lower value than obtaining a genuine geometric threshold mechanism.

The exact proof obstruction was not “define a Floquet exponent.” It was the **random FBM witness terminal time**. One needs a no-terminal-slow-point statement uniform enough that the witness is selected only after the probability-one Brownian statement has been proved.

**Outcome #22:** identified the missing lemma precisely: a strict survival exponent `>1` should make the set of candidate terminal points empty by a mesh-plus-modulus argument, replacing the parabola-specific Perkins input in the strict-supercritical direction.

### #11 — DUALIZE

Pass from Brownian physical time to logarithmic time. If `B` is Brownian and

\[
Y_r=e^{-r/2}B_{e^r},
\]

then `Y` is stationary Ornstein–Uhlenbeck with invariant standard Gaussian law `gamma` and generator

\[
\mathcal A=\frac12(\partial_{xx}-x\partial_x).
\]

A Brownian tube

\[
|B_u|\le\sqrt u\,w(\log u)
\]

becomes ordinary survival of `Y` in the time-periodic interval

\[
(-w(r),w(r)).
\]

Thus the relevant dual object is the killed-OU survival cocycle / periodic parabolic evolution operator, not an isolated narrow gate.

**Outcome #11:** successful. The correct strict-supercritical invariant is the uniform logarithmic-time survival exponent, equivalently the principal Floquet exponent in the standard periodic-parabolic formulation.

### #4 — PROVE SOMETHING WEAKER, COMPLETELY

I did **not** claim the critical equality case or the subcritical constructive direction. Those require a general periodic analogue of the deep slow-point existence/nonexistence statement that Perkins supplies for static parabolas.

Instead I proved the strict-supercritical implication completely, including the random-terminal-time issue, and then built an explicit profile where this theorem beats the previous duty-cycle route.

**Outcome #4:** successful theorem T85 plus strict-example T86 below. The fixed family-count metric does not move because the geometry is still the already-counted log-periodic tube family.

## 5. Robust periodic survival exponent

Let

\[
w:\mathbb R\to(0,\infty)
\]

be a positive `P`-periodic Lipschitz function. Set

\[
\phi(u)=\sqrt u\,w(\log u),\qquad u>0.
\tag{5.1}
\]

For `delta>=0`, let `Y` be stationary OU started from `gamma` and define

\[
\Psi_\delta(T)
:=
\sup_{\theta\in[0,P]}
\mathbb P_\gamma\left(
|Y_s|\le w(\theta+s)+\delta
\ \forall s\in[0,T]
\right),
\tag{5.2}
\]

\[
\Lambda_\delta(w)
:=
\liminf_{T\to\infty}
-\frac1T\log\Psi_\delta(T).
\tag{5.3}
\]

For a periodic Lipschitz moving interval, standard positive periodic-parabolic theory identifies the exponential decay rate in (5.3) with the principal Floquet exponent of the killed OU evolution (after the standard fixed-domain change of variables). I use (5.3) as the self-contained probabilistic definition, so the proof below does not depend on choosing a PDE normalization convention.

The adjective **robustly supercritical** means:

\[
\boxed{
\exists\delta>0:\ \Lambda_\delta(w)>1.
}
\tag{5.4}
\]

Because enlarging the tube lowers the exponent, (5.4) is stronger than merely writing `Lambda_0>1`. For regular periodic domains, standard domain-continuity of the principal periodic eigenvalue implies that strict `Lambda_0>1` entails (5.4).

## 6. T85 — robust Floquet obstruction for log-periodic tubes

Define the closed backward tube

\[
\mathcal D_w
=
\left\{(-u,x):u>0,\ |x|\le\phi(u)\right\}
\cup\{(0,0)\}.
\tag{6.1}
\]

(The closure at `u=0` follows because `w` is bounded and `sqrt(u)->0`.)

### Theorem I0077-R07-T85

If `w` satisfies (5.4), then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ |X_{-u}|\le\sqrt u\,w(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T85}
\]

This is the strict-supercritical analogue of the universal direction of source Theorem 4.3 for the whole continuous log-periodic tube, with the true periodic survival exponent replacing one isolated gate estimate.

### Proof overview

There are three lemmas:

1. strict OU survival exponent `>1` makes all padded long-tube probabilities summable;
2. the same exponent makes the probability of **any** candidate Brownian terminal point on a unit interval tend to zero as the short-lag cutoff tends to zero;
3. the source-style split into a local two-unit Brownian segment and an independent long tail converts those two facts into an all-time terminal-search estimate.

The final FBM step uses one deterministic witness index with high probability of being far enough left; it never conditions on the witness time.

### Lemma 6.1 — padded tail survival is summable

Fix `delta>0` with `Lambda_delta(w)>1`. Choose

\[
1<c<\Lambda_\delta(w).
\tag{6.2}
\]

By definition of the liminf, for all sufficiently large `T`,

\[
\Psi_\delta(T)\le e^{-cT}.
\tag{6.3}
\]

For `A>=0`, define

\[
r_A(n)
=
\mathbb P\left(
|B_u|\le\phi(u)+A\quad\forall u\in[1,n]
\right).
\tag{6.4}
\]

Choose

\[
H\ge1\quad\text{so large that}\quad A/\sqrt H\le\delta.
\]

On `[H,n]`, (6.4) implies

\[
\left|\frac{B_u}{\sqrt u}\right|
\le w(\log u)+\delta.
\]

Under `r=log u`, `B_u/sqrt(u)` is stationary OU. The logarithmic interval has length `log(n/H)`, and its starting phase is handled by the supremum in (5.2). Thus for all large `n`,

\[
r_A(n)
\le
\Psi_\delta(\log(n/H))
\le
(n/H)^{-c}.
\tag{6.5}
\]

Since `c>1`,

\[
\boxed{\sum_{n=2}^\infty r_A(n)<\infty.}
\tag{6.6}
\]

QED.

### Lemma 6.2 — strict exponent `>1` kills continuum terminal points

For `b in (0,1)`, let

\[
q(b)=
\mathbb P\left(
\exists t\in[0,1]:
|B_{t+h}-B_t|\le\phi(h)
\ \forall h\in[b,1]
\right),
\tag{6.7}
\]

where `B` is Brownian on `[0,2]`.

Then

\[
\boxed{q(b)\to0\quad(b\downarrow0).}
\tag{6.8}
\]

#### Proof

Fix `delta` as above and choose

\[
1<\alpha<c<\Lambda_\delta(w).
\tag{6.9}
\]

Let

\[
d_b=b^\alpha
\]

and mesh `[0,1]` with spacing at most `d_b`. There are `O(b^{-alpha})` mesh points.

Write `omega_B(d;[0,2])` for the Brownian modulus of continuity. The classical Brownian modulus estimate gives almost surely

\[
\omega_B(d;[0,2])
=O\!\left(\sqrt{d\log(1/d)}\right).
\]

Because `alpha>1`,

\[
\frac{\omega_B(d_b;[0,2])}{\sqrt b}
\longrightarrow0
\quad\text{a.s.}
\tag{6.10}
\]

Hence the event

\[
M_b:=
\left\{
2\omega_B(d_b;[0,2])\le\delta\sqrt b
\right\}
\tag{6.11}
\]

has probability tending to one.

Suppose the event inside (6.7) occurs at a terminal point `t`, and `M_b` also occurs. Choose a mesh point `t_i` with `|t-t_i|<=d_b`. For every `h in [b,1]`,

\[
\begin{aligned}
&|(B_{t_i+h}-B_{t_i})-(B_{t+h}-B_t)|\\
&\qquad\le
|B_{t_i+h}-B_{t+h}|+|B_{t_i}-B_t|\\
&\qquad\le2\omega_B(d_b;[0,2])
\le\delta\sqrt b
\le\delta\sqrt h.
\end{aligned}
\tag{6.12}
\]

Therefore

\[
|B_{t_i+h}-B_{t_i}|
\le
\sqrt h\,[w(\log h)+\delta]
\quad\forall h\in[b,1].
\tag{6.13}
\]

For each deterministic `t_i`, the process

\[
h\mapsto B_{t_i+h}-B_{t_i}
\]

is standard Brownian motion. Applying Lamperti on `h in [b,1]` gives, uniformly in the logarithmic starting phase,

\[
\mathbb P((6.13))
\le
\Psi_\delta(\log(1/b))
\le b^c
\tag{6.14}
\]

for all sufficiently small `b`.

A union bound over the `O(b^{-alpha})` mesh points yields

\[
q(b)
\le
\mathbb P(M_b^c)+C b^{c-\alpha}
\longrightarrow0,
\]

because `c>alpha`. QED.

**Why `1` is the threshold in this argument.** The continuum of candidate terminal times costs approximately one factor `b^{-1}`. A survival event across logarithmic scales from `b` to `1` costs `b^{Lambda}`. The mesh can be chosen with exponent strictly between them exactly when `Lambda>1`. This recovers the same critical number as source Theorem 4.3 without importing the parabola-specific slow-point theorem.

### Lemma 6.3 — full terminal search

For `a,b>0`, define

\[
T_{a,b}
=
\inf\left\{
 t\ge a\vee b:
 |B_{t-h}-B_t|\le\phi(h)
 \quad\forall h\in[b,t]
\right\}.
\tag{6.15}
\]

Then

\[
\boxed{
\lim_{b\downarrow0}
\mathbb P(T_{2,b}<\infty)=0.
}
\tag{6.16}
\]

#### Proof

Because `w` is Lipschitz and periodic, it is bounded together with its a.e. derivative. The function

\[
\phi(u)=\sqrt u\,w(\log u)
\]

is locally absolutely continuous and for a.e. `u>=1`,

\[
|\phi'(u)|
\le
\frac{C_w}{\sqrt u}
\tag{6.17}
\]

for a deterministic `C_w<infinity`. Hence there is `A<infinity` such that, simultaneously for all `u>=1` and `h_0 in [1,2]`,

\[
\phi(u+h_0)+\phi(h_0)
\le\phi(u)+A.
\tag{6.18}
\]

Fix integer `n>=2`. Define two Brownian processes from disjoint increments,

\[
B'_s=B_{n+1-s}-B_{n+1},\qquad 0\le s\le2,
\tag{6.19}
\]

and

\[
B''_u=B_{n-1-u}-B_{n-1},\qquad0\le u\le n-1.
\tag{6.20}
\]

They are independent standard Brownian motions on their respective intervals.

If `T_{2,b}=t in [n,n+1)`, put

\[
r=n+1-t\in[0,1],
\qquad
h_0=t-(n-1)\in[1,2].
\]

For `h in [b,1]`,

\[
B'_{r+h}-B'_r
=B_{t-h}-B_t,
\]

so `B'` realizes the local event counted by `q(b)`.

For the tail, write

\[
z(h)=B_{t-h}-B_t.
\]

Then for `1<=u<=n-1`,

\[
B''_u=z(h_0+u)-z(h_0).
\]

The terminal constraint and (6.18) give

\[
|B''_u|
\le\phi(h_0+u)+\phi(h_0)
\le\phi(u)+A.
\tag{6.21}
\]

Thus

\[
\{T_{2,b}\in[n,n+1)\}
\subseteq
\{\text{local event for }B'\}
\cap
\{|B''_u|\le\phi(u)+A,\ 1\le u\le n-1\}.
\]

Independence gives

\[
\mathbb P(T_{2,b}\in[n,n+1))
\le q(b)\,r_A(n-1).
\tag{6.22}
\]

Summing and applying Lemmas 6.1–6.2,

\[
\mathbb P(T_{2,b}<\infty)
\le
q(b)\sum_{n=2}^\infty r_A(n-1)
\longrightarrow0.
\]

QED.

### Completion of T85 — dependence-safe FBM transfer

Suppose contrary to T85 that

\[
E:=\{\exists R:\ |X_{-u}|\le\phi(u)\ \forall u\ge R\}
\]

has positive probability. Since `E` is a countable union over deterministic integer cutoffs, there is a deterministic `R>=1` with

\[
p:=\mathbb P(E_R)>0,
\]

where

\[
E_R=\{|X_{-u}|\le\phi(u)\ \forall u\ge R\}.
\]

Choose an integer `m` so large that

\[
\alpha=e^{-mP}
\]

satisfies

\[
\mathbb P(T_{2,\alpha R}<\infty)<p/4.
\tag{6.23}
\]

Set

\[
M_f=-2/\alpha.
\]

Because the FBM witness times tend to `-infinity`, there is a **deterministic witness index** `j` with

\[
\mathbb P(S_j\le M_f)>1-p/4.
\tag{6.24}
\]

On

\[
E_R\cap\{S_j\le M_f\},
\]

let

\[
B_t=X_{S_j+t}-X_{S_j}.
\]

This whole process `B` has the unconditional law of standard Brownian motion. Put `t_0=-S_j`. Since the source normalization has `X_0=0`, for every `h in [R,t_0]`,

\[
B_{t_0-h}-B_{t_0}=X_{-h}.
\tag{6.25}
\]

Now Brownian-scale by

\[
\widetilde B_s=\sqrt\alpha\,B_{s/\alpha}.
\]

Then `widetilde B` is again standard Brownian motion, its terminal time is

\[
\widetilde t_0=\alpha t_0\ge2,
\]

and its lower lag cutoff is `alpha R`. Moreover periodicity gives

\[
w(\log(h/\alpha))
=w(\log h+mP)
=w(\log h).
\]

Therefore the intersection event above is contained in the **path-only** event

\[
\{T_{2,\alpha R}(\widetilde B)<\infty\}.
\]

No conditioning on `S_j` is performed. Consequently

\[
\begin{aligned}
p
&\le
\mathbb P(S_j>M_f)
+
\mathbb P(T_{2,\alpha R}(\widetilde B)<\infty)\\
&<p/4+p/4=p/2,
\end{aligned}
\]

a contradiction. This proves T85. QED.

## 7. T86 — a continuous profile that the old single-gate certificate cannot see

T85 is not merely a repackaging of run 6's pulse inequality. The following explicit profile proves strict separation.

Let `P=1`, and define the continuous 1-periodic piecewise-linear half-width `w_*` on `[0,1]` by

\[
w_*(r)=\frac12,
\qquad 0\le r\le\frac3{20};
\tag{7.1}
\]

linearly increase from `1/2` to `6/5` on

\[
\left[\frac3{20},\frac4{25}\right]
\quad\text{(length }1/100\text{)};
\tag{7.2}
\]

\[
w_*(r)=\frac65,
\qquad \frac4{25}\le r\le\frac{99}{100};
\tag{7.3}
\]

then linearly decrease from `6/5` to `1/2` on `[99/100,1]` and extend periodically. It is positive, continuous and Lipschitz.

For `c>0`, let

\[
\lambda_c:=\lambda_0(-c,c)
\]

be the principal static killed-OU exponent.

### Static spectral bounds

The Gaussian Rayleigh quotient and the elementary weight bounds on `[-c,c]` give

\[
\boxed{
\frac{\pi^2 e^{-c^2/2}}{8c^2}
\le\lambda_c
\le
\frac{\pi^2 e^{c^2/2}}{8c^2}.
}
\tag{7.4}
\]

The source also gives

\[
\lambda_1=1
\tag{7.5}
\]

and strict domain monotonicity.

### The old single-threshold route fails for every threshold

For every `c<6/5`, any connected logarithmic interval on which `w_*(r)<=c` has length at most

\[
\frac3{20}+\frac1{100}+\frac1{100}
=\frac{17}{100}.
\tag{7.6}
\]

If such an interval is nonempty then `c>=1/2`, and monotonicity gives

\[
\lambda_c\le\lambda_{1/2}.
\]

Using `pi^2<10` and

\[
e^{1/8}<\frac1{1-1/8}=\frac87,
\]

(7.4) gives

\[
\lambda_{1/2}<\frac{40}{7}.
\]

Hence every old single-threshold pulse product with `c<6/5` satisfies

\[
\tau(c)\lambda_c
<
\frac{17}{100}\frac{40}{7}
=
\frac{34}{35}<1.
\tag{7.7}
\]

For `c>=6/5`, the available duty is at most `1`, while strict domain monotonicity and (7.5) give

\[
\lambda_c\le\lambda_{6/5}<\lambda_1=1.
\tag{7.8}
\]

Thus **no threshold `c` can make the run-6 one-pulse criterion exceed 1**.

### The all-phase spectral budget is nevertheless supercritical

At every logarithmic phase the current interval is contained in `(-6/5,6/5)`, and during the narrow plateau of length `3/20` it is exactly `(-1/2,1/2)`.

For killed OU evolution `U(s,t)`, the Dirichlet-form identity (or a smooth approximation at the finitely many corners) gives

\[
\frac{d}{dt}\|U(s,t)f\|_{L^2(\gamma)}^2
\le
-2\lambda_{w_*(t)}\|U(s,t)f\|_{L^2(\gamma)}^2.
\tag{7.9}
\]

Therefore over one period the logarithmic survival decay is at least

\[
\frac3{20}\lambda_{1/2}
+
\frac{17}{20}\lambda_{6/5}.
\tag{7.10}
\]

Now use rigorous rational lower bounds. First,

\[
\pi^2>\frac{493}{50},
\qquad
 e^{-1/8}>1-\frac18=\frac78,
\]

so

\[
\lambda_{1/2}>
\frac{3451}{800}.
\tag{7.11}
\]

For `x=18/25`, the alternating exponential series gives the rigorous lower bound

\[
e^{-18/25}
>
1-x+\frac{x^2}{2}-\frac{x^3}{6}
+\frac{x^4}{24}-\frac{x^5}{120}
=
\frac{23758643}{48828125}.
\tag{7.12}
\]

Hence

\[
\lambda_{6/5}
>
\frac{11713010999}{28125000000}.
\tag{7.13}
\]

Substituting (7.11)–(7.13) into (7.10),

\[
\boxed{
\frac3{20}\lambda_{1/2}
+
\frac{17}{20}\lambda_{6/5}
>
\frac{563093843233}{562500000000}
=1+
\frac{593843233}{562500000000}
>1.
}
\tag{7.14}
\]

The gap is strict. By continuity of `c -> lambda_c`, the same weighted bound remains `>1` after replacing `w_*` by `w_*+delta` for all sufficiently small `delta>0`. The energy estimate therefore gives

\[
\Lambda_\delta(w_*)>1
\]

for some `delta>0`. T85 applies.

### Theorem I0077-R07-T86

For the explicit continuous profile `w_*` above, every FBM satisfies

\[
\boxed{
\mathbb P\left(
\exists R:
|X_{-u}|\le\sqrt u\,w_*(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T86}
\]

At the same time, **every** old single-threshold duty-cycle certificate from run 6 fails by (7.7)–(7.8). Thus T85/T86 are a strict theorem-level strengthening of the previous periodic-tube result, not another checker for an unchanged statement.

## 8. Exact finite self-check

Only the finite rational arithmetic in the canonical separation example was delegated to code. The Brownian/Floquet theorem is proved on the page.

Artifacts:

- `artifacts/R07/20260919T0424Z_floquet_budget_check.py` — creation commit `ff47b8c8fac4b0a459eb51998b9e16c3e071c5e3`;
- `artifacts/R07/20260919T0424Z_floquet_budget_check.out` — creation commit `0ecfb4ebcfca75dcd5b87858f84a0d31a68b264c`.

The executed output ends

`SELF-CHECK PASS`.

It verifies exactly:

\[
\frac3{20}\lambda_{1/2}^{\rm LB}
+
\frac{17}{20}\lambda_{6/5}^{\rm LB}
=
\frac{563093843233}{562500000000}>1,
\]

and

\[
\frac{17}{100}\lambda_{1/2}^{\rm UB}
\le\frac{34}{35}<1.
\]

This is explicitly a **self-check**, not an independent audit.

## 9. Frozen-equivalence / metric audit

I do **not** count T85/T86 as family 60.

Run 6 already counted the structural family

\[
|x|\le\sqrt{|t|}\,w(\log|t|)
\]

with nonconstant periodic `w`. The present profile `w_*` is another member of that same family. The new contribution is a stronger theorem and a strictly stronger spectral criterion, not a new shape family under the frozen convention.

Therefore

\[
\boxed{59\longrightarrow59\quad\text{(no metric movement).}}
\]

This is intentional and follows the owner's instruction not to inflate the metric by parameter/profile changes inside one family.

## 10. What remains genuinely hard

The strict-supercritical direction is now source-facing and no longer tied to one narrow gate. Two obligations remain:

1. **Critical case `Lambda=1`.** The mesh proof has no room to choose `1<alpha<Lambda`; this is exactly where source Theorem 4.3 uses the finer Perkins slow-point theorem plus domain monotonicity.
2. **Subcritical construction `Lambda<1`.** A first-moment count predicts many candidate terminal points, but a decomposable-FBM construction needs a second-moment/localization theorem for periodic slow points, plus endpoint control to concatenate pieces. Merely knowing the survival exponent is not enough on the page yet.

A plausible next source-facing target is therefore:

> prove a periodic slow-point theorem with Hausdorff dimension `1-Lambda_F` for a Lipschitz periodic moving OU interval, or at least the existence/nonexistence dichotomy at `Lambda_F=1` needed to complete all three clauses of the Theorem-4.3 analogue.

That would be substantially more valuable than manufacturing a 60th profile via another parameter variation.

## 11. Closure / audit state

- T85: **PROVED ON PAGE, SELF-CHECKED WHERE FINITE, UNAUDITED**.
- T86: **PROVED ON PAGE, exact arithmetic self-check PASS, UNAUDITED**.
- Independent OTHER-track audits: **0/2** for these new claims.
- Prior-art status: **bounded search completed; publication novelty UNVERIFIED**.
- Source Problem 7.8: **PARTIAL**, not `PROVED` or `CLOSED`.
- No paper folder is created because the source is not closed and the two-audit closure condition is not met.

## 12. Model / scheduler control status

The requested prompt says GPT-6 with maximum reasoning, but this actual run identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort receipt, so I report reasoning as **UNVERIFIED** and do not claim GPT-6 maximum.

The currently exposed scheduling interface still offers prompt/title, schedule or start offset, enablement, and timing mode. It still exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-model receipt**. Changing this for real would require the product/scheduler surface or an owning-workspace policy to expose persistent model/reasoning routing plus per-run telemetry.

The repository records the historical P26 `You cannot modify this task` response as authorization-context-specific; a later authorized P/C context succeeded while another context continued to reject R-series task edits. For a task that still rejects modification, the legitimate route is its owning/authorized workspace or account, an authorized ownership/admin correction, or platform support. No permission bypass, duplicate schedule, or scheduler change was attempted in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  intake: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 59
  after: 59
  movement: "NO MOVEMENT"
  unchanged_count_before: 0
  unchanged_count_after: 1
  methods: [4, 11, 22]
  new_claims:
    - "I0077-R07-T85: robust strict-supercritical Floquet/survival-exponent obstruction for continuous log-periodic tubes"
    - "I0077-R07-T86: explicit continuous profile certified supercritical by all-phase spectral budget while every old single-threshold pulse certificate fails"
  metric_reason: "T85/T86 sharpen the already-counted log-periodic tube family from run 6; frozen convention forbids counting a new profile in the same family"
  finite_core:
    checker: "artifacts/R07/20260919T0424Z_floquet_budget_check.py"
    output: "artifacts/R07/20260919T0424Z_floquet_budget_check.out"
    result: "SELF-CHECK PASS"
  audits_other_tracks: "0/2"
  publication_novelty: "UNVERIFIED"
  source_status: "PARTIAL"
  claim_status: "PROVED_SELF_CHECKED_UNAUDITED"
  remaining_obligation: "critical Lambda_F=1 and subcritical Lambda_F<1 periodic slow-point / decomposable-FBM construction; alternatively a genuinely distinct family, not a parameter variant"
  shared_roots_modified: false
  peer_files_modified: false
  email_or_drive: false
```
