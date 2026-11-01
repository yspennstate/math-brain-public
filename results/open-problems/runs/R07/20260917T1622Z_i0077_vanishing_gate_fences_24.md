Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `23 -> 24` genuinely distinct nonparabolic shape families; Section-B moves tried: #1 CHANGE THE CATEGORY, #8 GO THE OTHER WAY AND DISCRETIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 24: vanishing-duty parabolic gates and sampled-OU persistence

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and the frozen metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the convention that trivial Brownian rescaling/reflection and parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T1525Z_i0077_critical_log_inward_tubes_23.md`,

which moved the metric `22 -> 23` and used Section-B moves `#5,#18,#24`. The present triple `#1,#8,#17` is different.

Before new mathematics I recovered current `master` evidence from the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical `operations/claims/I0077.md`, the complete newest R07 report and targeted searches through the preceding I0077 chain, the newest visible R06 report, and the newest visible R15 report. I also rechecked the old immutable R07 KPZ/FPP handoff; it remains retired and was not deleted or reopened.

`INDEX.md`/`RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. The canonical I0077 claim still names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; the owner's current task nevertheless explicitly assigns I0077 to R07. No competing live I0077 ownership was found. R15's distinct old Problem-7.2/I0076 assignment remains a handoff and is not I0077.

The large `probability_1000_intake_*/problems.jsonl` corpus and whole repository cannot be rendered literally byte-for-byte through the connector in one response; oversized searches are truncated. I therefore record the limitation honestly: exact I0077/source text, ownership, posted exclusions, queue state, neighboring ownership, and the prior R07 attempt chain were recovered by targeted reads/searches. I do **not** falsely claim a literal byte-for-byte reread of every intake row.

The entering metric is therefore `23`, not the stale old-R07 row still visible in the compact root `RESULTS.md` snapshot.

## 2. Primary source benchmark rechecked

I reopened the authors' PDF and visually rechecked the relevant pages.

Definition 2.1 says that an FBM `X` admits random witness times `S_n -> -infinity` such that, for each witness,

\[
W_n(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 gives decomposable FBMs by concatenating independent Brownian pieces stopped at a.s.-finite stopping times.

For `-infinity <= c_1<c_2<=infinity`, the source writes `lambda_0(c_1,c_2)` for the positive principal exponent of killed Ornstein--Uhlenbeck motion with generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Remark 4.1 gives continuity and strict domain monotonicity. Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal normalized far-past obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there is a decomposable FBM with the corresponding asymptotic normalized confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there is a decomposable FBM pointwise inside the exact parabolic strip for every negative time.

Problem 7.8 is exactly the one-line request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy sentence is Problem 7.9 and is not part of this assignment.

## 3. Fresh prior-art/status pass — 2026-09-17

Fresh bounded web searches covered:

- exact-title / exact-Problem-7.8 / later-author queries for *Forward Brownian Motion*;
- discretely sampled Ornstein--Uhlenbeck persistence;
- Gaussian AR(1) persistence exponents and integral-operator representations;
- Gaussian stationary-process ball exponents and sampling continuity.

The nearest literature found is substantial and is treated as prior art, not novelty: Ehrhardt--Majumdar--Bray (Phys. Rev. E 69, 016106, 2004) explicitly study discretely sampled Gaussian stationary processes including OU; Aurzada--Mukherjee--Zeitouni (AIHP 57 (2021), 1411--1441) prove persistence-exponent results for Markov chains including autoregressions; Aurzada--Kettner study the leading integral-operator eigenvalue for Gaussian AR(1); and Feldheim--Feldheim--Mukherjee, *Persistence and ball exponents for Gaussian stationary processes* (CPAM 78 (2025), 1949--2000), study persistence/ball exponents for continuous and discrete stationary Gaussian processes and sampling continuity.

I did not find in this bounded dated search a later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating the FBM theorem below. That is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The sampled-OU/AR(1) persistence mechanism itself is classical.

## 4. Negation-first test: can a finite-log-measure deformation be ignored?

A natural proposed extension rule is:

> If a moving parabolic-scale tube differs from a favorable static parabola only on a set of finite, or arbitrarily small, total logarithmic-time measure, then exact eventual FBM confinement should be unchanged.

This run falsifies that proposed rule.

The key observation is that a zero-duration constraint can still cost a nontrivial factor if it is repeated at exponentially separated physical scales. Residence-time spectral mass misses this effect because the constrained time set can have total logarithmic measure as small as desired. The correct object is instead the persistence operator of **sampled** OU motion.

This is not a refutation of Problem 7.8; it is a new source-appropriate family and an obstruction that a general theory has to retain.

## 5. Methods #1, #8, #17: from killed OU to sampled OU / AR(1)

Fix a logarithmic sampling period `P>0` and normalized aperture `a>0`. Let `gamma` be standard Gaussian measure and let `Q_P` be the stationary OU semigroup over time `P` on `L^2(gamma)`. Put

\[
I_a=[-a,a],\qquad M_a f=1_{I_a}f,
\]

and define the one-step sampled survival operator

\[
\boxed{K_{a,P}=M_aQ_PM_a.}
\tag{5.1}
\]

OU reversibility makes `K_{a,P}` positive and self-adjoint. Define

\[
\rho(a,P)=\|K_{a,P}\|_{2\to2},
\qquad
\boxed{\kappa_d(a,P)=-\frac1P\log\rho(a,P).}
\tag{5.2}
\]

If `Y` is stationary OU and `r_j=jP`, then

\[
\mathbb P_\gamma\{Y_0,Y_P,\ldots,Y_{NP}\in I_a\}
=
\langle1_{I_a},K_{a,P}^{N}1_{I_a}\rangle_\gamma
\le \rho(a,P)^N.
\tag{5.3}
\]

This is the discrete analogue of the source's killed-OU exponent.

Two elementary facts are needed later.

**Continuity in `a`.** For fixed `P`, the OU transition kernel relative to `gamma` is continuous and bounded on every bounded square. Hence, if `a_n->a` and all apertures lie below a fixed `A`, the kernels of `K_{a_n,P}-K_{a,P}` converge to zero in Hilbert--Schmidt norm: the difference is supported on a symmetric-difference set whose `gamma x gamma` measure tends to zero. Therefore

\[
\rho(a_n,P)\to\rho(a,P),\qquad
\kappa_d(a_n,P)\to\kappa_d(a,P).
\tag{5.4}
\]

**Discrete checking is weaker than continuous checking.** If `H_{a,P}` denotes OU killed continuously on leaving `I_a` during `[0,P]`, then its positive kernel is dominated by the endpoint-only operator `K_{a,P}`. Thus

\[
e^{-P\lambda_0(-a,a)}=\|H_{a,P}\|_{2\to2}
\le \rho(a,P),
\quad\text{so}\quad
\boxed{\kappa_d(a,P)\le\lambda_0(-a,a).}
\tag{5.5}
\]

Hence the obstruction and source-existence regimes below cannot conflict.

## 6. Theorem I0077-R07-T25 — geometric temporal fences

Let

\[
u_k=e^{kP},\qquad k\in\mathbb N_0,
\tag{6.1}
\]

and impose the parabolic constraint only at these scales:

\[
|X_{-u_k}|\le a\sqrt{u_k}.
\tag{6.2}
\]

### T25(i): sampled-persistence obstruction

If

\[
\boxed{\kappa_d(a,P)>1,}
\tag{T25.i-cond}
\]

then for **every** FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists K<\infty:\
|X_{-e^{kP}}|\le a e^{kP/2}
\quad\forall k\ge K
\right)=0.
}
\tag{T25.i}
\]

### T25(ii): source-subcritical existence

If

\[
\boxed{\lambda_0(-a,a)<1,}
\tag{T25.ii-cond}
\]

then there exists a decomposable FBM satisfying (6.2) for **every** `k`, indeed satisfying the stronger pointwise inequality

\[
|X_{-u}|\le a\sqrt u\qquad\forall u>0.
\tag{T25.ii}
\]

Part (ii) is an immediate application of source Theorem 4.3(iii). Part (i) is new in the present Problem-7.8 program and is proved next.

## 7. Proof of T25(i): arbitrary Brownian terminals, then an FBM witness

Assume `kappa_d(a,P)>1`. By (5.4), choose

\[
a<a_1<a_2
\tag{7.1}
\]

so close to `a` that

\[
\kappa:=\kappa_d(a_2,P)>1.
\tag{7.2}
\]

### 7.1 Brownian arbitrary-terminal lemma

Let `W` be standard Brownian motion. Fix a deterministic fence index `K_0`. Call `T` **good** if

\[
|W_T-W_{T-e^{kP}}|\le a_1e^{kP/2}
\quad\text{for every }k\ge K_0\text{ with }e^{kP}\le T.
\tag{7.3}
\]

I claim that almost surely there are only finitely many good `T`.

For integer `n>=3`, let

\[
M_n=\sup\{|W_t-W_s|:0\le s,t\le n+1,\ |t-s|\le1\}.
\tag{7.4}
\]

Covering by intervals of length two and using reflection plus a Gaussian tail gives, for all large `n`,

\[
\mathbb P\{M_n>8\sqrt{\log n}\}\le12n^{-3}.
\tag{7.5}
\]

Choose

\[
C_0>\left(\frac{16}{a_2-a_1}\right)^2
\tag{7.6}
\]

and let `m_n` be the least integer with

\[
R_n:=e^{m_nP}\ge C_0\log n.
\tag{7.7}
\]

Then `R_n<=e^PC_0 log n`.

Suppose `T in [n,n+1]` is good and the modulus event complementary to (7.5) holds. For each fence lag `u=e^{kP}` with `R_n<=u<=n`,

\[
\begin{aligned}
|W_n-W_{n-u}|
&\le |W_T-W_{T-u}|+2M_n\\
&\le a_1\sqrt u+16\sqrt{\log n}
\le a_2\sqrt u.
\end{aligned}
\tag{7.8}
\]

By Brownian time reversal, `(W_n-W_{n-u})_{0<=u<=n}` has the law of standard Brownian motion on `[0,n]`. Under Lamperti normalization at the geometric times `u=e^{kP}`, the variables

\[
Y_k=e^{-kP/2}B_{e^{kP}}
\tag{7.9}
\]

form the stationary sampled OU chain. If

\[
N_n=\left\lfloor\frac{\log n}{P}\right\rfloor-m_n,
\]

then (5.3) gives

\[
\mathbb P\{(7.8)\}
\le \rho(a_2,P)^{N_n}
\le C_P\left(\frac n{R_n}\right)^{-\kappa}.
\tag{7.10}
\]

Because `R_n=O(log n)` and `kappa>1`, the series of the right-hand side over `n` converges. Together with (7.5),

\[
\sum_n
\mathbb P\{\exists\text{ good }T\in[n,n+1]\}<\infty.
\tag{7.11}
\]

Borel--Cantelli proves

\[
\boxed{
\mathbb P\{\exists\text{ good }T\ge A\}\to0
\quad(A\to\infty).
}
\tag{7.12}
\]

This is the dependence-safe arbitrary-terminal statement needed for FBM witnesses.

### 7.2 Transfer to an arbitrary FBM

Suppose T25(i) fails for an FBM `X`. By taking a countable union over deterministic fence indices and deterministic bounds on `|X_0|`, there exist `K,M<infinity` and `q_0>0` such that

\[
E=\left\{|X_0|\le M,
\ |X_{-e^{kP}}|\le ae^{kP/2}\ \forall k\ge K\right\}
\tag{7.13}
\]

has probability at least `q_0`.

Increase `K` if necessary so that

\[
M\le(a_1-a)e^{kP/2}\qquad(k\ge K).
\tag{7.14}
\]

Then on `E`,

\[
|X_0-X_{-e^{kP}}|\le a_1e^{kP/2}\qquad(k\ge K).
\tag{7.15}
\]

Let `S_j->-infinity` be the FBM witness times and, for a fixed deterministic index `j`, let

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad T_j=-S_j.
\]

`W_j` is standard Brownian motion. Whenever `T_j` is large enough, (7.15) says that `T_j` is a good terminal for `W_j`, because

\[
W_j(T_j)-W_j(T_j-u)=X_0-X_{-u}.
\tag{7.16}
\]

Choose deterministic `A` so large that the Brownian probability in (7.12) is below `q_0/2`. Since `T_j->infinity` along the witness sequence almost surely, choose a **deterministic witness index** `j` such that

\[
\mathbb P(T_j<A)<q_0/2.
\]

Then (7.15)--(7.16) imply

\[
\mathbb P\{W_j\text{ has some good terminal }T\ge A\}
\ge q_0-\mathbb P(T_j<A)>q_0/2,
\]

contradicting (7.12). No conditioning on a random witness time and no independence between the witness time and its Brownian path is used. This proves T25(i). `square`

## 8. Continuous space-time family: vanishing-duty gate tubes

The discrete fence theorem immediately produces a continuous family, avoiding any reliance on a merely countable Borel shape.

Fix `A>a`, `P>0`, and pairwise disjoint intervals

\[
G_k=[kP-\varepsilon_k,kP+\varepsilon_k],
\qquad \varepsilon_k>0,
\qquad \sum_k\varepsilon_k<\infty.
\tag{8.1}
\]

Let `w:R->(0,infinity)` be continuous, equal to `A` outside `union_k G_k`, and on each `G_k` decrease continuously to

\[
w(kP)=a
\tag{8.2}
\]

and rise back to `A`. Define

\[
\boxed{
\mathcal V_w=
\{(-u,x):u>0,\ |x|\le w(\log u)\sqrt u\}\cup\{(0,0)\}.
}
\tag{8.3}
\]

### Corollary T25-V

If `kappa_d(a,P)>1`, then every FBM fails eventual confinement in `V_w`:

\[
\boxed{
\mathbb P\left(
\exists R:\ |X_{-u}|\le w(\log u)\sqrt u\ \forall u\ge R
\right)=0.
}
\tag{8.4}
\]

Indeed, confinement in the full tube implies the fence inequalities at `u=e^{kP}`, and T25(i) applies.

If instead `lambda_0(-a,a)<1`, source Theorem 4.3(iii) gives a decomposable FBM inside the static inner parabola `|x|<=a sqrt(u)` for every `u`; because `w>=a`, that process lies in `V_w` pointwise. Thus this new family has both a universal-obstruction regime and a decomposable pointwise-existence regime.

The striking feature is that

\[
\operatorname{Leb}\{r:w(r)\ne A\}
\le 2\sum_k\varepsilon_k
\tag{8.5}
\]

can be made **arbitrarily small**, even though the dents occur at infinitely many remote scales.

## 9. Exact canonical example: powers of four

Take

\[
P=\log4,\qquad a=\frac1{20},\qquad A=2.
\tag{9.1}
\]

Sampling stationary OU every `P` gives the exact AR(1) recursion

\[
\boxed{
Y_{j+1}=\frac12Y_j+\frac{\sqrt3}{2}Z_{j+1},
\qquad Z_{j+1}\sim N(0,1).
}
\tag{9.2}
\]

For any starting `x`, the transition density is Gaussian with variance `3/4`, hence its maximum is

\[
\sqrt{\frac{2}{3\pi}}<1.
\tag{9.3}
\]

Therefore, uniformly for `|x|<=1/20`,

\[
q:=\mathbb P_x\{|Y_1|\le1/20\}<2a=\frac1{10}.
\tag{9.4}
\]

The transition kernel is symmetric relative to `gamma`; Schur's test gives

\[
\rho(1/20,\log4)\le q<\frac1{10}<\frac14=e^{-P}.
\tag{9.5}
\]

Hence

\[
\boxed{\kappa_d(1/20,\log4)>1.}
\tag{9.6}
\]

T25(i) yields the completely explicit statement

\[
\boxed{
\mathbb P\left(
\exists K:\ |X_{-4^k}|\le\frac1{20}2^k\ \forall k\ge K
\right)=0
}
\tag{9.7}
\]

for every FBM.

For a concrete continuous profile, let `r_k=k log4`, choose

\[
\varepsilon_k=2^{-k-5},\qquad k\ge1,
\]

set `w=2` off the disjoint intervals `[r_k-epsilon_k,r_k+epsilon_k]`, and interpolate linearly from `2` down to `1/20` at `r_k` and back to `2`. Then

\[
\operatorname{Leb}\{r:w(r)\ne2\}
=2\sum_{k\ge1}2^{-k-5}=\frac1{16}.
\tag{9.8}
\]

Yet no FBM can be eventually confined to the resulting tube. By multiplying all `epsilon_k` by an arbitrarily small common factor, the total deformation measure can be made as small as desired without changing the obstruction at the gate centers.

Meanwhile the undeformed outer parabola `|x|<=2 sqrt(u)` is source-subcritical because `lambda_0(-1,1)=1` and strict domain monotonicity gives `lambda_0(-2,2)<1`; source Theorem 4.3(iii) therefore supplies a decomposable FBM pointwise confined to that outer parabola. Thus an arbitrarily small-total-log-measure sequence of dents can reverse pointwise-existence of the outer envelope into universal eventual nonconfinement.

This directly falsifies the proposed “finite/small log-measure perturbations are harmless” rule.

## 10. Exact-arithmetic self-check

The rational core of (9.1)--(9.6) was executed exactly and archived at

`artifacts/R07/20260917T1622Z_geometric_fence_constants.py`

with output

`artifacts/R07/20260917T1622Z_geometric_fence_constants.out`.

Source artifact commit: `25ff3bfb189041e76ad37cde559cff1fd4a9623b`.  
Executed-output commit: `cc0722099a2e6c7d8c3efc3f9b202d3ca36607c7`.

The archived output ends `PASS` and checks exactly

\[
r=1/2,\quad\sigma^2=3/4,\quad2a=1/10<1/4=e^{-P}.
\]

The Gaussian density inequality (9.3) is analytic and is proved on the page; the checker is a **self-check**, not an independent audit.

## 11. What the three Section-B methods actually did

### #1 — CHANGE THE CATEGORY

The earlier pulse theorems measured residence-time killing by continuous OU spectral mass. I changed category to a discrete-time transfer operator `K_{a,P}`. A zero-duration temporal fence has zero continuous-time mass but a nonzero sampled-persistence cost.

### #8 — GO THE OTHER WAY AND DISCRETIZE

I first stripped the moving shape to the geometric fence set `u_k=e^{kP}` and proved the arbitrary-terminal theorem there. Only after that did I thicken each fence into an arbitrarily narrow continuous gate. The discrete core is therefore the proof mechanism, not a numerical approximation.

### #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

Lamperti sampling turns Brownian motion at geometric scales into Gaussian AR(1). The relevant number is the leading survival-operator norm `rho(a,P)`, exactly the kind of persistence exponent studied in the AR(1)/sampled-Gaussian literature. That literature supplied the right language; the FBM witness-time compiler is the source-specific step proved here.

## 12. Why this earns metric point 24

This is not a parameter change inside runs 6--9.

- Run 6 used periodic gates of **fixed positive** logarithmic duration.
- Runs 7--8 used positive-duration aperiodic/nonsyndetic pulse sets with enough accumulated pulse-time density.
- Run 9 allowed zero pulse-time density only by making the fixed-interval OU cost grow so that weighted **residence-time spectral mass** still grows faster than the horizon.
- Here the gate aperture is bounded and fixed, while the total logarithmic duration of all nontrivial gates can be **finite and arbitrarily small**. The continuous killed-OU spectral-mass criterion from run 9 therefore gives no obstruction. Repeated point sampling alone does.
- Run 19's fast-transport family uses order-one motion of a connected window and transition cost between different locations. Here the center never moves; the novelty of the geometry is vanishing duty cycle, not transport.

Brownian rescaling translates logarithmic time and preserves the structural facts “summable gate widths / arbitrarily small total log measure / infinitely many geometric gate centers.” It cannot turn this family into a fixed-duty periodic pulse tube or an unbounded-severity drifting-pulse tube.

Accordingly the frozen metric moves

\[
\boxed{23\longrightarrow24},
\qquad\text{unchanged count}=0.
\]

Different choices of `P,a,A,(epsilon_k)` do **not** count as new families.

## 13. Limitations, audits, and next obligation

T25 does **not** claim a sharp classification for the gap

\[
\kappa_d(a,P)\le1\le\lambda_0(-a,a).
\]

The universal obstruction is proved when the sampled persistence exponent exceeds one; pointwise decomposable existence is inherited from the source when the stronger continuous exponent is below one. Determining whether `kappa_d=1` is the exact sampled-fence FBM threshold would require a new constructive decomposable-FBM argument and is deliberately left open.

No P26 end-to-end audit of T25 was found, and no second independent OTHER-track audit of T25 was found. Therefore:

- T25 is a theorem-sized R07 claim with a complete proof on this page;
- Problem 7.8 remains **PARTIAL**, not CLOSED;
- novelty remains **UNVERIFIED**;
- no `paper_<name>/` closure package is created.

The strongest next research route is not another aperture or gate-width parameter. It is to attack the sharp sampled-fence converse `kappa_d<1` constructively, or move to a new geometry if that route stalls.

## 14. Model / reasoning / scheduler-control status

The actual runtime identifies as **GPT-5.6 Sol**. The reasoning level is not authenticated by exposed telemetry, so it is reported **UNVERIFIED**, not GPT-6 maximum.

The exposed automation control schema still offers title/prompt, schedule/start offset, enabled state, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus GPT-6/maximum is still prompt text only. Enforcing it would require the product/API or an authorized owner/admin workspace surface to expose those controls.

The historical P26 `You cannot modify this task` event remains an authorization-boundary issue. Repository policy also records later success from an authorized context; the legitimate workaround is therefore the owning authorized context or platform support, not a worker-level bypass, permission change, or duplicate task. This run was research-only and made no scheduler mutation.

## 15. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  claim_id: I0077-R07-T25
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 23
  after: 24
  movement: +1
  unchanged_count: 0
  new_family: "vanishing-duty geometric parabolic gates / temporal fences"
  methods_this_run: [1, 8, 17]
  negation_test: "finite or arbitrarily small total log-time deformation need not preserve eventual confinement"
  theorem_scope:
    sampled_obstruction: "kappa_d(a,P)>1 implies universal eventual nonconfinement at geometric fences"
    continuous_gate_corollary: "same obstruction for continuous tubes with summable gate widths and minima a at geometric centers"
    existence: "lambda_0(-a,a)<1 gives decomposable pointwise confinement by source Theorem 4.3(iii)"
    sharp_gap: UNCLASSIFIED
  canonical_example:
    P: "log 4"
    a: "1/20"
    sampled_AR1: "Y_{j+1}=(1/2)Y_j+(sqrt(3)/2)Z_{j+1}"
    row_survival_bound: "q<1/10<1/4=e^{-P}"
    conclusion: "no FBM eventually satisfies |X_{-4^k}| <= 2^k/20"
    continuous_outer_aperture: 2
    canonical_total_gate_log_measure: "1/16, arbitrarily reducible"
  finite_core:
    checker: artifacts/R07/20260917T1622Z_geometric_fence_constants.py
    output: artifacts/R07/20260917T1622Z_geometric_fence_constants.out
    verdict: PASS_SELF_CHECK
  prior_art: "bounded dated search completed; sampled OU/AR(1) persistence and Gaussian ball-exponent literature found; no explicit exact Problem-7.8/T25 resolution located; novelty UNVERIFIED"
  audits:
    new_T25_p26: PENDING_NOT_FOUND
    new_T25_second_other_track: PENDING_NOT_FOUND
  source_status: PARTIAL
  closure: false
  paper_package: false
  remaining_obligation: "sharp sampled-fence converse kappa_d<1 or a genuinely different geometry; two external audits required before closure"
```

No email/Gmail, Drive, public posting, purchase, permission change, shared-root edit, peer-file edit, workflow execution, or scheduler change was performed.
