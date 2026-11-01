Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `30 -> 31` genuinely distinct nonparabolic shape families; Section-B moves actually used: #7 TAKE THE LIMIT, #13 FIND WHAT ONLY INCREASES, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The following source sentence is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 31: accelerating logarithmic chirp tubes

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T2242Z_i0077_cantor_parity_shutters_30.md`,

which moved the metric `29 -> 30` and used moves `#2,#15,#27`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain. Thus the literal instruction to choose three moves never previously used on this problem is exhausted; I do not invent a false history. What matters here is a genuinely new mechanism and a different triple from the immediately preceding run.

Before new mathematics I recovered current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, current `RESULTS.md` state through repository search, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the searchable R07/I0077 chain through run 30;
- current neighbouring R15 state and its preserved handoff from distinct Burdzy–Scheutzow Problem 7.2 / I0076;
- the C29/NM duplicate-exclusion records for I0077;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still lists I0077 separately. The canonical claim names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared status while following the owner's explicit assignment of this exact target to R07. R15's old I0076 / Problem 7.2 line is retired-handoff and is not reopened here. The old R07 KPZ/FPP route remains preserved by immutable handoff rather than deleted.

The large `probability_1000_intake_*/problems.jsonl` resources cannot be rendered byte-for-byte through the available connector without truncation. The intake reread this run is therefore honestly **targeted/partial because of connector limits**: the exact I0077 row, source statement, ownership, exclusions and searchable prior attempts were recovered; I do not claim a literal reread of every unrelated intake row.

Entering metric: **30**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

The primary paper was rechecked, including its FBM/decomposable-FBM definitions, Theorem 4.3, Remark 4.1/4.2, Proposition 4.4, and the open-problem page.

An FBM is a continuous real-indexed process `X`, with witness times `S_j -> -infinity`, such that for each fixed `j`

\[
W_j(t):=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{2.1}
\]

is standard Brownian motion. A decomposable FBM is built by concatenating independent Brownian pieces stopped at finite stopping times.

For `-infinity <= c_1<c_2<=infinity`, the paper writes `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized limsup/liminf obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the exact static parabolic strip for every `t<=0`.

Remark 4.1 gives continuity and strict domain monotonicity of `lambda_0`; Remark 4.2 records the critical centered identity

\[
\lambda_0(-1,1)=1.
\tag{2.2}
\]

Proposition 4.4 gives the useful strongly-decomposable one-sided construction. Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 beyond parabolas. The next sentence is separately Problem 7.9 on forward Lévy processes.

## 3. Fresh current-status / prior-art pass

Fresh bounded searches on 2026-09-17 UTC included:

- the exact quoted wording of Problem 7.8 and the exact paper title/arXiv id;
- `Forward Brownian Motion` with `moving boundary`, `oscillating boundary`, `rapidly oscillating boundary`, `chirp`, and `space-time shape`;
- Ornstein–Uhlenbeck first passage through periodic and time-varying boundaries;
- Brownian/diffusion first passage through moving and oscillatory boundaries;
- later/current pages and citation-oriented searches around the Burdzy–Scheutzow paper.

Nearby prior art found includes Sacerdote (1990), *Asymptotic behaviour of Ornstein–Uhlenbeck first-passage-time density through periodic boundaries*; Giorno–Nobile–Ricciardi (1990), *On the asymptotic behaviour of first-passage-time densities for one-dimensional diffusion processes and varying boundaries*; Ahari–Alili–Tamborrino, *Boundary crossing problems and functional transformations for Ornstein–Uhlenbeck processes* (arXiv:2210.01658); and Giorgini–Moon–Wettlaufer (2024), *Analytical Survival Analysis of the Non-autonomous Ornstein–Uhlenbeck Process*. These establish substantial moving-boundary/OU prior art, especially for periodic or prescribed boundaries. I found no explicit later resolution of exact Burdzy–Scheutzow Problem 7.8 and no explicit FBM theorem matching the accelerating-log-chirp result below in this bounded search.

That is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The Brownian modulus argument below is elementary and is not claimed as a new general theorem about Brownian motion.

## 4. New family: accelerating logarithmic chirp tubes

Fix

\[
p>1,\qquad A>0,\qquad h>0.
\]

Let

\[
\phi_p(r)=
\begin{cases}
0,&r\le0,\\
r^p,&r>0,
\end{cases}
\tag{4.1}
\]

which is continuous and `C^1` for `p>1`. Define the normalized moving center

\[
m_{p,A}(r)=A\sin\phi_p(r),
\tag{4.2}
\]

and the backward space-time tube

\[
\boxed{
\mathcal C_{p,A,h}
=
\left\{(-u,x):u>0,\ 
\left|\frac{x}{\sqrt u}-A\sin\phi_p(\log u)\right|\le h
\right\}\cup\{(0,0)\}.
}
\tag{4.3}
\]

Equivalently, its physical cross-section at lag `u` is

\[
\sqrt u\,[m_{p,A}(\log u)-h,\,m_{p,A}(\log u)+h].
\tag{4.4}
\]

The shape is closed. For `u<=1` its center is zero, while for `u>1` the normalized center oscillates with phase `(log u)^p` whose logarithmic frequency

\[
\phi_p'(r)=p r^{p-1}
\tag{4.5}
\]

diverges.

### Why this is a new metric family

Run 19's fast-transport windows were **log-periodic**: after some fixed logarithmic period `P`, their normalized geometry repeats exactly. Run 24/26/27/28 used geometric sampled gates with `O(1)` gates per fixed-ratio annulus. Run 25 used additive-time point fences with unit-scale physical switching. The present shape is a **continuous tube** and has no nonzero log period. More invariantly, for every fixed `c>1`, the number of center oscillations in the annulus `[T,cT]` is

\[
\frac{(\log(cT))^p-(\log T)^p}{2\pi}+O(1)
\sim \frac{p\log c}{2\pi}(\log T)^{p-1}\longrightarrow\infty.
\tag{4.6}
\]

A Brownian rescaling only translates `log T` by a constant, so the divergence in (4.6) is preserved. It cannot turn this family into a fixed-period moving tube or a fixed-density geometric gate family. This is a structural temporal-frequency invariant, not a parameter rescaling.

## 5. Section-B moves actually used

### #7 TAKE THE LIMIT

Instead of freezing a periodic moving tube, I drove its logarithmic frequency to infinity in the far past. The limiting phenomenon is that opposite normalized positions `+A` and `-A` must be visited in a physical-time window that is `o(T)` at horizon `T`.

### #13 FIND WHAT ONLY INCREASES

For `r>0`, the chirp frequency `phi_p'(r)=p r^{p-1}` is strictly increasing. Hence the maximum log-time separation between consecutive opposite extrema eventually decreases monotonically like `r^{-(p-1)}`. This monotone frequency is the mechanism that converts continuous confinement into a shrinking-window Brownian increment contradiction.

### #30 DO ONE SCALE / ONE DIRECTION AT A TIME

At each large witness horizon `T`, I ignore the rest of the tube and use exactly one max-to-min transition lying inside the fixed multiplicative annulus `[T/2,3T/4]`. A single forced displacement at each scale is enough; no global spectral/Floquet calculation is needed.

## 6. Brownian shrinking-window modulus lemma

Put

\[
q=p-1>0.
\]

For fixed `C>0` and standard Brownian motion `B`, define, for large `T`,

\[
\Omega_{C,q}(T)
:=
\sup\left\{
|B_t-B_s|:
0\le s,t\le T,
|t-s|\le \frac{CT}{(\log T)^q}
\right\}.
\tag{6.1}
\]

### Lemma 6.1

Almost surely,

\[
\boxed{
\frac{\Omega_{C,q}(T)}{\sqrt T}\longrightarrow0
\qquad(T\to\infty).
}
\tag{6.2}
\]

### Proof

Set `T_n=2^n`. For `T in [2^n,2^{n+1}]`,

\[
\frac{CT}{(\log T)^q}
\le
\frac{C2^{n+1}}{(n\log2)^q}
=:d_n.
\tag{6.3}
\]

Cover `[0,2^{n+1}]` by intervals

\[
J_{n,k}=[k d_n,(k+2)d_n]
\]

for the relevant integers `k`. Any pair with separation at most `d_n` lies in one such `J_{n,k}`, and the number of these intervals is `O(n^q)` because

\[
\frac{2^{n+1}}{d_n}=\frac{(n\log2)^q}{C}.
\tag{6.4}
\]

For an interval `J` of length `2d_n`, stationarity of Brownian increments and the reflection principle give, for every `epsilon>0`,

\[
\begin{aligned}
\mathbb P\left(
\operatorname{osc}_J B>\epsilon\sqrt{2^n}
\right)
&\le
\mathbb P\left(
2\sup_{0\le t\le2d_n}|B_t|>
\epsilon\sqrt{2^n}
\right)\\
&\le
4\exp\left(-\frac{\epsilon^2 2^n}{16d_n}\right)\\
&\le
4\exp(-c_{C,q}\epsilon^2 n^q)
\end{aligned}
\tag{6.5}
\]

for a constant `c_{C,q}>0`. A union bound over `O(n^q)` intervals gives

\[
\mathbb P\left(
\sup_k\operatorname{osc}_{J_{n,k}}B>
\epsilon\sqrt{2^n}
\right)
\le
C' n^q e^{-c'\epsilon^2 n^q}.
\tag{6.6}
\]

The right side is summable in `n` for every `q>0`. Borel–Cantelli therefore yields, almost surely, for every fixed rational `epsilon>0`, eventually every `J_{n,k}` has oscillation at most `epsilon sqrt(2^n)`. Using (6.3), every admissible pair in (6.1) for every `T in [2^n,2^{n+1}]` lies in one of these intervals. Letting rational `epsilon downarrow0` proves (6.2). `square`

Consequently, for each `c>0`, if

\[
G_R(c):=
\left\{\exists T\ge R:\Omega_{C,q}(T)\ge c\sqrt T\right\},
\tag{6.7}
\]

then

\[
\boxed{\mathbb P(G_R(c))\longrightarrow0\qquad(R\to\infty).}
\tag{6.8}
\]

This path-only event is what permits a dependence-safe transfer to random FBM witness times.

## 7. Chirp geometry: every large scale contains a fast opposite-extremum transition

Fix `T` large and set

\[
a_T=\log(T/2),
\qquad
b_T=\log(3T/4).
\tag{7.1}
\]

The logarithmic width is the positive constant

\[
b_T-a_T=\log(3/2).
\]

Since `p>1`,

\[
b_T^p-a_T^p
\sim p\log(3/2)(\log T)^{p-1}
\longrightarrow\infty.
\tag{7.2}
\]

Hence, for all sufficiently large `T`, the phase interval `[a_T^p,b_T^p]` contains two consecutive opposite extrema of the sine: there are `r_+,r_- in [a_T,b_T]` such that

\[
\sin(r_+^p)=1,
\qquad
\sin(r_-^p)=-1,
\tag{7.3}
\]

and

\[
|r_+^p-r_-^p|=\pi.
\tag{7.4}
\]

By the mean value theorem,

\[
|r_+-r_-|
=
\frac{\pi}{p\xi^{p-1}}
\le
\frac{\pi}{p(\log(T/2))^{p-1}}
\tag{7.5}
\]

for some `xi` between `r_+` and `r_-`. Put

\[
u_+=e^{r_+},\qquad u_-=e^{r_-}.
\]

Then

\[
\frac T2\le u_+,u_-\le\frac{3T}{4}.
\tag{7.6}
\]

For sufficiently large `T`, (7.5) is at most one, and therefore

\[
|u_+-u_-|
\le e^{\max(r_+,r_-)}e^{|r_+-r_-|}|r_+-r_-|
\le
\frac{C_pT}{(\log T)^{p-1}}
\tag{7.7}
\]

for a deterministic constant `C_p<infinity` depending only on `p`.

Thus a fixed multiplicative annulus always contains an opposite pair whose **relative physical-time separation tends to zero**.

## 8. I0077-R07-T32 — accelerating log-chirp phase theorem

**Status of theorem: PROVED below. Overall source status remains PARTIAL.**

Let `C_{p,A,h}` be (4.3), with `p>1` and `A,h>0`.

### T32(i): separated chirp is universally impossible

If

\[
\boxed{A>h,}
\tag{8.1}
\]

then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\left|
\frac{X_{-u}}{\sqrt u}
-A\sin((\log u)^p)
\right|\le h
\quad\forall u\ge R
\right)=0.
}
\tag{T32.i}
\]

(The displayed event is in the `u>1` regime, where `phi_p(log u)=(log u)^p`.) In particular no FBM is pointwise confined to `C_{p,A,h}` for every negative time.

### T32(ii): wide-overlap chirp admits a decomposable FBM

If

\[
\boxed{h-A>1,}
\tag{8.2}
\]

then there exists a decomposable FBM `X` satisfying

\[
\boxed{
(-u,X_{-u})\in\mathcal C_{p,A,h}
\qquad\forall u>0
}
\tag{T32.ii}
\]

almost surely.

No claim is made for the intermediate regime

\[
A\le h\le A+1.
\tag{8.3}
\]

The theorem is complete as stated; (8.3) is a deliberately open sharp-classification question, not a hidden gap in either implication.

## 9. Proof of T32(i): a chirp forces a forbidden Brownian increment at every large witness scale

Assume `A>h` and put

\[
d:=A-h>0.
\tag{9.1}
\]

At the positive extremum `u_+` from Section 7, confinement gives

\[
X_{-u_+}\ge d\sqrt{u_+}.
\tag{9.2}
\]

At the negative extremum `u_-`, confinement gives

\[
X_{-u_-}\le-d\sqrt{u_-}.
\tag{9.3}
\]

Therefore, using (7.6),

\[
\begin{aligned}
|X_{-u_+}-X_{-u_-}|
&\ge d(\sqrt{u_+}+\sqrt{u_-})\\
&\ge \sqrt2\,d\sqrt T.
\end{aligned}
\tag{9.4}
\]

while (7.7) gives

\[
|u_+-u_-|
\le \frac{C_pT}{(\log T)^{p-1}}.
\tag{9.5}
\]

Now suppose, toward contradiction, that the eventual-confinement event in T32(i) has positive probability. Since it is a countable union over deterministic integer starting radii, there is an integer `R_0` such that

\[
E_{R_0}:=
\left\{
\left|
\frac{X_{-u}}{\sqrt u}-A\sin((\log u)^p)
\right|\le h
\quad\forall u\ge R_0
\right\}
\tag{9.6}
\]

has probability

\[
q_0:=\mathbb P(E_{R_0})>0.
\tag{9.7}
\]

Let `S_j -> -infinity` be an FBM witness sequence, put

\[
T_j=-S_j,
\qquad
W_j(t)=X_{S_j+t}-X_{S_j},\quad t\ge0.
\tag{9.8}
\]

For every **deterministic** index `j`, `W_j` is standard Brownian motion.

Apply Lemma 6.1 with `q=p-1`, `C=C_p`, and, say,

\[
c=d.
\tag{9.9}
\]

Choose deterministic `R_*` so large that:

1. the opposite-extremum construction of Section 7 works for every `T>=R_*`;
2. `T/2>=R_0` whenever `T>=R_*`;
3. for standard Brownian motion,
   \[
   \mathbb P(G_{R_*}(d))<q_0/2.
   \tag{9.10}
   \]

Because `T_j -> infinity` almost surely, choose a **deterministic witness index** `j` such that

\[
\mathbb P(T_j<R_*)<q_0/4.
\tag{9.11}
\]

On

\[
E_{R_0}\cap\{T_j\ge R_*\},
\tag{9.12}
\]

apply Section 7 at the random numerical value `T=T_j`. The resulting `u_+,u_-` lie in `[T_j/2,3T_j/4]`, so they are both at least `R_0`; hence (9.4)–(9.5) apply. In Brownian-witness time,

\[
t_+=T_j-u_+,
\qquad
t_-=T_j-u_-
\tag{9.13}
\]

belong to `[T_j/4,T_j/2] subset [0,T_j]`, and

\[
W_j(t_+)-W_j(t_-)
=X_{-u_+}-X_{-u_-}.
\tag{9.14}
\]

Thus

\[
|t_+-t_-|
\le\frac{C_pT_j}{(\log T_j)^{p-1}}
\tag{9.15}
\]

but

\[
|W_j(t_+)-W_j(t_-)|
\ge\sqrt2\,d\sqrt{T_j}
>d\sqrt{T_j}.
\tag{9.16}
\]

Therefore the **entire Brownian path** `W_j` lies in the path-only event `G_{R_*}(d)`. Consequently,

\[
\begin{aligned}
\mathbb P(G_{R_*}(d;W_j))
&\ge
\mathbb P(E_{R_0}\cap\{T_j\ge R_*\})\\
&\ge q_0-\mathbb P(T_j<R_*)\\
&>3q_0/4.
\end{aligned}
\tag{9.17}
\]

But `W_j` is standard Brownian motion for deterministic `j`, so by (9.10) the left side is `<q_0/2`. Contradiction.

No conditioning on the random witness time `T_j` occurred, and no independence between `T_j` and `W_j` was assumed. This proves T32(i). `square`

## 10. Proof of T32(ii): a common static substrip survives every chirp phase

Assume

\[
a:=h-A>1.
\tag{10.1}
\]

Because `|m_{p,A}(r)|<=A` for every `r`, every normalized chirp interval contains the fixed centered interval

\[
[-a,a]=[A-h,h-A].
\tag{10.2}
\]

Indeed for every `m in [-A,A]`,

\[
[-a,a]
\subset[m-h,m+h].
\tag{10.3}
\]

By the source identity `lambda_0(-1,1)=1` and strict domain monotonicity,

\[
\lambda_0(-a,a)<1.
\tag{10.4}
\]

Source Theorem 4.3(iii) therefore supplies a decomposable FBM with

\[
|X_t|\le a\sqrt{|t|}
\qquad\forall t\le0
\tag{10.5}
\]

almost surely. By (10.3), this process lies in the chirp tube at every negative time. This proves T32(ii). `square`

## 11. Canonical concrete instances

A thin impossible example is

\[
p=2,\qquad A=2,\qquad h=\frac12.
\tag{11.1}
\]

Then

\[
\boxed{
\left|
\frac{X_{-u}}{\sqrt u}-2\sin((\log u)^2)
\right|\le\frac12
\quad\text{eventually}
}
\]

has probability zero for every FBM.

A wide feasible example in the same chirp family is

\[
p=2,\qquad A=\frac12,\qquad h=2.
\tag{11.2}
\]

Every normalized slice contains `[-3/2,3/2]`, whose killed-OU exponent is strictly below one, so a decomposable FBM exists that stays in this chirp tube for every negative time.

The thin example also sits inside the wide static outer parabola

\[
|x|\le\frac52\sqrt u,
\tag{11.3}
\]

for which source Theorem 4.3(iii) gives a decomposable pointwise-confined FBM. Thus being contained in a source-subcritical outer parabolic envelope does not itself make a bounded normalized deformation trackable. The obstruction is the accelerating transport requirement.

## 12. What the theorem falsifies — and what it does not

A plausible extension heuristic is:

> a bounded normalized deformation of a source-feasible parabolic envelope should remain harmless if the tube itself stays Brownian-scale at every time.

T32(i), together with (11.3), shows this is false: the width remains exactly proportional to `sqrt(u)` and the normalized center remains bounded, yet the increasing temporal frequency forces macroscopic `sqrt(T)` displacement over `o(T)` Brownian time windows at every sufficiently large scale.

This is a refutation of that **proposed extension mechanism**, not a refutation of Problem 7.8. Problem 7.8 remains an open-ended request for generalizations.

## 13. Why the proof is not merely run 19 again

Run 19 uses a fixed period `P` and obtains an exponential survival cost by multiplying one Gaussian transport penalty per period. The number of compulsory transports per fixed-ratio annulus is `O(1)`.

Here there is no period and no product-of-probabilities argument at all. The number of oscillations in `[T,cT]` tends to infinity, but the proof deliberately discards almost all of them. One opposite pair already lies in a Brownian time window of length

\[
O\left(\frac{T}{(\log T)^{p-1}}\right)=o(T),
\]

and the pathwise shrinking-window modulus alone kills confinement. This is a scale-local regularity obstruction rather than a persistence exponent.

The new family also differs from run 17's power-sheared tube: there the normalized center is monotone and diverges at one compactified end; here it remains bounded forever and instead acquires unbounded temporal frequency.

## 14. Finite core / checking

There is no finite combinatorial or exact-enumeration core in T32. The new claim is analytic and its proof is written in full above. I therefore did **not** manufacture a checker merely to create an artifact. The elementary canonical parameter comparisons are exact on the page.

Self-check status: proof reread for quantifiers, arbitrary terminal times, and the `T_j` dependence issue. This is still a **self-check**, not an independent audit.

Independent OTHER-track audits for T32: **0/2**.

Therefore no closure claim and no `paper_<name>/` package is created.

## 15. Status and next route

The fixed metric moves

\[
\boxed{30\longrightarrow31}.
\]

Overall source status remains

\[
\boxed{\text{PARTIAL}.}
\]

`unchanged_count = 0`.

The strongest next mathematical question is the intermediate chirp regime `A<=h<=A+1`. In particular, when opposite extreme slices overlap but there is no common source-subcritical centered core, neither the shrinking-window obstruction nor the static common-core construction decides feasibility. A natural next route is to formulate a high-frequency adiabatic/averaging limit for the killed OU process and determine whether the fast chirp behaves like killing outside the **intersection** of its phase fibers, like an averaged killing potential, or by a genuinely different effective operator.

## 16. Model / scheduler control check requested by the owner

The control limitation is still present in the interface exposed to this worker. The available task-control schema offers prompt/title, schedule or start offset, enabled state, and timing mode; it exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable setting here, and I do not claim it ran.

The repository policy records historical modification probes for P26/P01/P03 that returned `You cannot modify this task`; later repository evidence records that P26 could be updated from another authorized context. The legitimate remedy is therefore the owning/authorized account or workspace surface, or platform support exposing/persisting model and reasoning fields and returning authenticated execution metadata. A repository edit is not a scheduler repair, and a worker-level bypass or duplicate task is not appropriate. No scheduler or permission mutation was attempted in this run.

## 17. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  lane: CLOSABLE_OUTSIDE
  source: I0077
  source_citation: "Burdzy--Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic regions"
  source_status: PARTIAL
  claim_owner: R07
  shared_claim_status: "PENDING_ADMISSION, not READY (preserved)"
  metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 30
  after: 31
  movement: true
  unchanged_count: 0
  methods: [7, 13, 30]
  new_family: "accelerating logarithmic chirp tubes"
  theorem: I0077-R07-T32
  theorem_status: PROVED_ON_PAGE_SELF_CHECKED
  thin_regime: "A>h => universal impossibility of eventual confinement for every FBM"
  wide_regime: "h-A>1 => decomposable FBM confined pointwise for all negative time"
  unclassified_regime: "A<=h<=A+1"
  finite_core: none
  checker: NOT_APPLICABLE_NO_FINITE_CORE
  independent_audits: []
  closure: false
  prior_art_status: "bounded current search; no explicit resolution located; novelty UNVERIFIED"
  next_obligation: "intermediate chirp regime via high-frequency killed-OU averaging/effective operator"
```
