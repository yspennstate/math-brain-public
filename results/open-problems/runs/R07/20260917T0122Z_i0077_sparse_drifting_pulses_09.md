Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **METRIC MOVEMENT: 8 -> 9 genuinely distinct nonparabolic shape families; Section-B moves tried: #4 PROVE SOMETHING WEAKER, COMPLETELY, #8 GO THE OTHER WAY AND DISCRETIZE, #26 HUNT THE SPORADIC CASE.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958v4), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the open-ended source problem is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 9: zero-density drifting pulses and a weighted OU spectral-mass obstruction

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric is the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260917T0024Z_i0077_nonsyndetic_density_pulses_08.md`.

It records metric `8`. Family 8 is the bounded-profile, fixed-severity pulse class: the narrow pulses may have unbounded gaps but have **positive lower logarithmic density**, and a fixed killed-OU cost `lambda_*` per unit pulse time gives the obstruction `p tau lambda_*>1`.

This run proves a qualitatively different regime: the pulse set has **zero logarithmic-time density**, but the allowed normalized corridor makes increasingly large off-center excursions, so the killed-OU spectral cost of the sporadic pulses tends to infinity. The relevant invariant is a weighted spectral mass, not pulse density. A canonical example has pulse starts at `m^2`, hence pulse-time density zero, while the per-pulse spectral cost is order `m^2`; its cumulative spectral mass is order `S^(3/2)` on a logarithmic horizon of length `S`.

Therefore

\[
\boxed{8\longrightarrow 9.}
\]

`unchanged_count` resets to `0`.

The old R07 KPZ/FPP route remains retired from this slot exactly as preserved in the run-1 handoff; no historical file was changed or deleted.

## 2. Required repository/source/current-status recovery

Before new mathematics I reread or directly rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and the current `RANKING.md` scope;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report plus the preceding I0077 chain recovered by exact repository search;
- newest neighboring R15 report `runs/R15/20260917_0058Z_rotation_scope_i0074_a21.md`; R15 has retired distinct Problem 7.2 / I0076 after its six-run handoff and has not claimed I0077;
- targeted repository/intake searches for I0077, `1302.6958`, Problem 7.8, duplicate attempts, and the old C29 collision.

`INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` still lists I0077 as the Burdzy–Scheutzow shape problem. The canonical claim still reserves I0077 exclusively to R07, although its shared text remains `PENDING_ADMISSION, not READY`; run 1 performed the source/status/ownership admission and the owner has repeatedly assigned this exact R07 target. I do not mutate shared operational files.

The large `probability_1000_intake_*/problems.jsonl` resources are connector-truncated when rendered wholesale. The whole-intake reread is therefore **PARTIAL / targeted due connector limits**, not falsely claimed complete. The exact I0077 source, ownership, exclusions, and prior attempts were recovered directly.

### Primary source recheck

I reopened the authors' PDF `https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf` and visually rechecked the relevant pages. Definition 2.1 is the FBM witness-time definition; Definition 2.2 is decomposable concatenation. Theorem 4.3 states the three parabolic-strip clauses controlled by `lambda_0(c1,c2)`: universal obstruction for `lambda_0>=1`, decomposable asymptotic existence for `lambda_0<=1`, and decomposable pointwise confinement when `c1<=0<=c2` and `lambda_0<1`. Problem 7.8 is exactly the one-sentence question above; the forward-Lévy text is separately Problem 7.9.

### Dated current-literature search: 2026-09-17

Fresh bounded searches included:

- exact phrase `"Can one generalize Theorem 4.3 from parabolas to other space-time shapes"`;
- `"Forward Brownian Motion" Burdzy Scheutzow Problem 7.8` and later-author/citation variants;
- `Ornstein-Uhlenbeck killed interval principal eigenvalue moving boundary survival`;
- `Brownian motion sparse moving boundary survival Ornstein Uhlenbeck`;
- `principal eigenvalue Ornstein Uhlenbeck interval Dirichlet`.

The source article is still the identifiable primary Problem-7.8 statement. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the FBM theorem below. This is **negative bounded evidence only, not a novelty certificate**. Principal-eigenvalue/absorption analysis for killed OU is classical; for example Iscoe–McDonald (1993) explicitly studies OU absorption through a harmonic-oscillator Dirichlet eigenvalue. The harmonic-oscillator transform used below is therefore treated as standard machinery, not as a novelty claim.

## 3. Why the previous suggested converse route was not forced

The end of run 8 suggested attacking the converse regime `p tau lambda < 1` by constructing a phase-aware decomposable FBM. I tested that direction first. The source construction for `lambda_0<1` ultimately needs a positive-probability Brownian **terminal-time** event (Perkins slow points plus support/scaling) from which almost-sure finite stopping pieces can be selected. A mere upper bound on an average killed-OU exponent below one does not supply such a terminal-time lower bound in a nonstationary, nonsyndetic corridor. In particular, sparse wide deserts can destroy any naive block-by-block uniform success probability.

I therefore used method #4: prove a weaker but complete theorem in the opposite sparse regime rather than manufacture a gap-filled converse. The new regime is not covered by T9 because its pulse density is zero and its normalized profile is unbounded on the pulses.

## 4. General weighted spectral-mass theorem

Let `L,U:R->R` be continuous with `L(r)<U(r)` for every `r`, and define the backward tube

\[
D_{L,U}
=
\{(t,x):t<0,\ \sqrt{|t|}L(\log|t|)\le x\le \sqrt{|t|}U(\log|t|)\}\cup\{(0,0)\}.
\tag{4.1}
\]

Fix `eta>0`. Let

\[
P_j=[a_j,a_j+\tau_j],\qquad \tau_j>0,
\]

be pairwise disjoint logarithmic-time pulse intervals. For each `j`, suppose there is a bounded open interval

\[
I_j=(\ell_j,u_j)
\]

such that throughout the pulse

\[
[L(r)-2\eta,\ U(r)+2\eta]\subset I_j,
\qquad r\in P_j.
\tag{4.2}
\]

Let `lambda_j` be the principal Dirichlet eigenvalue on `I_j` for the stationary Ornstein–Uhlenbeck generator

\[
\mathcal A f=\frac12f''-\frac12x f'.
\tag{4.3}
\]

For `r<s`, define the spectral mass of complete pulses by

\[
\mathfrak M(r,s)
:=
\sum_{j:P_j\subset[r,s]}\tau_j\lambda_j.
\tag{4.4}
\]

Put

\[
R_n=\left\lceil\frac{256}{\eta^2}\log n\right\rceil,
\qquad
r_n=\log R_n,
\qquad
s_n=\log n.
\tag{4.5}
\]

### Theorem I0077-R07-T10 — weighted sparse-pulse obstruction

If

\[
\boxed{
\underline\Lambda_\eta
:=
\liminf_{n\to\infty}
\frac{\mathfrak M(r_n,s_n)}{s_n-r_n}>1,
}
\tag{T10.cond}
\]

then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\!\left(
\exists R<\infty:
\sqrt uL(\log u)\le X_{-u}\le\sqrt uU(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T10}
\]

No positive pulse-density, bounded-gap, periodicity, almost-periodicity, bounded-profile, symmetry, decomposability, or stochastic-environment assumption is made. In particular, `T10.cond` can hold when the total pulse-time density tends to zero.

This is a source-appropriate analogue of the universal-obstruction clause of Theorem 4.3(i), but for a nonparabolic moving tube.

## 5. Proof of T10

### 5.1 Lamperti/OU survival and spectral mass

Let `Z` be standard Brownian motion and set

\[
Y_r=e^{-r/2}Z_{e^r}.
\]

Then `Y` is stationary OU with invariant Gaussian probability measure `gamma`. Consider the twice-padded moving interval

\[
J(r)=(L(r)-2\eta,U(r)+2\eta).
\]

Let `Q_{r,s}` be the positive sub-Markov evolution obtained by killing OU on leaving `J(v)` at time `v`. Unconstrained OU evolution and killing are contractions on `L^2(gamma)`.

On a complete pulse `P_j`, condition (4.2) makes the moving survival event a subset of survival in the fixed interval `I_j`. The killed OU semigroup on `I_j` has `L^2(gamma)` norm `exp(-lambda_j tau_j)`. Factoring the nonautonomous evolution at pulse endpoints and using submultiplicativity therefore gives

\[
\|Q_{r,s}\|_{2\to2}
\le
\exp\{-\mathfrak M(r,s)\}.
\tag{5.1}
\]

Because the Lamperti transform of Brownian motion starts every log time in `gamma`, Cauchy–Schwarz yields

\[
\mathbb P\!\left(
\sqrt v[L(\log v)-2\eta]\le Z_v\le
\sqrt v[U(\log v)+2\eta]
\ \forall v\in[R_n,n]
\right)
\le
\exp\{-\mathfrak M(r_n,s_n)\}.
\tag{5.2}
\]

Choose `kappa` with

\[
1<\kappa<\underline\Lambda_\eta.
\]

Then for all sufficiently large `n`,

\[
\mathbb P(\text{twice-padded survival on }[R_n,n])
\le
\exp\{-\kappa(s_n-r_n)\}
=
(n/R_n)^{-\kappa}.
\tag{5.3}
\]

### 5.2 Discretizing arbitrary terminal times — method #8

For a standard Brownian motion `B`, define a once-padded good terminal `t` (above a fixed lower lag `R_0`) by

\[
G(t;R_0):
\quad
\sqrt s[L(\log s)-\eta]
\le B_{t-s}-B_t\le
\sqrt s[U(\log s)+\eta]
\quad\forall s\in[R_0,t].
\tag{5.4}
\]

For integers `n>=3`, let

\[
M_n=\max_{0\le k\le n}\operatorname{osc}_{[k,k+2]}B.
\]

Reflection plus a Gaussian tail gives

\[
\mathbb P(M_n>8\sqrt{\log n})\le 8n^{-3}
\tag{5.5}
\]

for all sufficiently large `n`; the right side is summable.

Suppose `t\in[n,n+1]` is once-padded good and `M_n\le8\sqrt{\log n}`. For every `s\in[R_n,n]`,

\[
\left|
(B_{t-s}-B_t)-(B_{n-s}-B_n)
\right|
\le2M_n
\le16\sqrt{\log n}
\le\eta\sqrt s,
\tag{5.6}
\]

where the last inequality is exactly why `R_n` was chosen as in (4.5). Hence the integer terminal `n` is good in the **twice-padded** corridor on `[R_n,n]`.

The reversed process

\[
\{B_{n-s}-B_n:0\le s\le n\}
\]

is itself standard Brownian motion in the lag variable `s`. Therefore (5.3) and (5.5) imply

\[
\mathbb P\{\exists t\in[n,n+1]:G(t;R_0)\}
\le
8n^{-3}+(n/R_n)^{-\kappa}.
\tag{5.7}
\]

Since `R_n=O(\log n)` and `kappa>1`, the right side is summable. Borel–Cantelli gives

\[
\boxed{
\sup\{t:G(t;R_0)\}<\infty
\quad\text{a.s.}
}
\tag{5.8}
\]

(with the empty-set convention). In particular, if

\[
H_A:=\{\exists t\ge A:G(t;R_0)\},
\]

then

\[
\mathbb P(H_A)\downarrow0
\qquad(A\to\infty).
\tag{5.9}
\]

This tail-probability formulation is the dependence-safe statement needed for an arbitrary FBM witness time.

### 5.3 FBM transfer with no independence assumption

Assume, for contradiction, that an FBM `X` has positive probability `q>0` of eventual confinement in the unpadded tube. Since the event is an increasing union over deterministic lower horizons and `X_0` is finite a.s., there exist deterministic `R_0,K<\infty` such that

\[
E_0:=
\left\{
\sqrt uL(\log u)\le X_{-u}\le\sqrt uU(\log u)
\ \forall u\ge R_0,
\ |X_0|\le K
\right\}
\]

has probability `q_0>0`. Increase `R_0` if necessary so that

\[
K\le\eta\sqrt{R_0}.
\tag{5.10}
\]

Choose `A` so large that the standard-Brownian probability in (5.9) is less than `q_0/4`.

By the FBM definition there is a witness sequence `S_j->-infinity` a.s. such that

\[
B^{(j)}_r:=X_{S_j+r}-X_{S_j},\qquad r\ge0,
\]

is standard Brownian motion for each fixed `j`. Choose one deterministic index `j` so far down the witness sequence that

\[
\mathbb P(-S_j<A)<q_0/4.
\tag{5.11}
\]

Set `T=-S_j`. On `E_0\cap\{T\ge A\}`, for every `s\in[R_0,T]`,

\[
B^{(j)}_{T-s}-B^{(j)}_T
=X_{-s}-X_0.
\tag{5.12}
\]

By confinement and (5.10), (5.12) lies in the once-padded corridor. Thus `T` is a good terminal for the **single standard Brownian motion** `B^{(j)}`, so

\[
E_0\cap\{T\ge A\}\subseteq H_A(B^{(j)}).
\tag{5.13}
\]

No independence between `T`, `E_0`, and `B^{(j)}` is used. From (5.11),

\[
\mathbb P(E_0\cap\{T\ge A\})
\ge q_0-q_0/4=3q_0/4,
\]

whereas `B^{(j)}` is standard Brownian motion and the choice of `A` gives

\[
\mathbb P(H_A(B^{(j)}))<q_0/4.
\]

This contradicts (5.13), proving T10. `QED`

**Dependence audit note.** The proof is deliberately phrased with one deterministic witness index after choosing `A`. One does *not* compare the random terminals `-S_j` across different Brownian witness processes or assume a witness time is independent of its Brownian future. This is the same structural lesson as the source proof of Theorem 4.3(i), which bounds an existence-of-terminal event for one Brownian witness rather than conditioning on the witness time.

## 6. A new explicit family: zero-density pulses whose centers escape

Set

\[
\eta=\frac1{16}.
\]

For every integer `m>=3`, define the logarithmic pulse

\[
P_m=[m^2,m^2+1/4].
\tag{6.1}
\]

On `P_m`, set

\[
L(r)=m-\frac18,
\qquad
U(r)=m+\frac18.
\tag{6.2}
\]

On `[m^2-1/4,m^2]`, interpolate `L,U` linearly from the base corridor `(-2,2)` to the values in (6.2); on `[m^2+1/4,m^2+1/2]`, interpolate linearly back to `(-2,2)`; elsewhere set `(L,U)=(-2,2)`. The transition blocks are disjoint for `m>=3`, and convex interpolation preserves `L<U`, so this defines continuous walls.

The pulses occupy only

\[
\frac14\#\{m:m^2\le S\}=O(\sqrt S)
\]

units of logarithmic time up to horizon `S`; hence their logarithmic-time density is **zero**.

During pulse `m`, the twice-padded corridor is exactly contained in

\[
I_m=
\left(m-\frac14,m+\frac14\right).
\tag{6.3}
\]

### 6.1 Off-center killed-OU eigenvalue bound

For a bounded interval `I`, the OU principal Dirichlet eigenvalue has Rayleigh quotient

\[
\lambda(I)
=
\inf_{f\in H^1_0(I),f\ne0}
\frac{\frac12\int_I|f'|^2e^{-x^2/2}\,dx}
{\int_I f^2e^{-x^2/2}\,dx}.
\tag{6.4}
\]

Put `g(x)=f(x)e^{-x^2/4}`. Integration by parts (the Dirichlet boundary term vanishes) gives the exact harmonic-oscillator form

\[
\frac12\int_I|f'|^2e^{-x^2/2}dx
=
\int_I
\left[
\frac12|g'|^2+\left(\frac{x^2}{8}-\frac14\right)g^2
\right]dx.
\tag{6.5}
\]

Hence if `I\subset[a,\infty)` with `a>0`,

\[
\lambda(I)\ge\frac{a^2}{8}-\frac14.
\tag{6.6}
\]

For (6.3) and `m>=3`,

\[
\lambda_m
\ge
\frac{(m-1/4)^2}{8}-\frac14
\ge
\frac{m^2}{16},
\tag{6.7}
\]

because the difference between the two right sides is

\[
\frac{8m^2-8m-31}{128}>0
\qquad(m\ge3).
\]

### 6.2 Spectral mass diverges faster than the log horizon

Let `S=s_n=\log n` and `r=r_n=\log R_n`. Complete pulses with

\[
\lceil\sqrt r\rceil+1\le m\le\lfloor\sqrt{S-1}\rfloor
\]

lie inside `[r,S]` for all large `n`. By (6.7),

\[
\mathfrak M(r,S)
\ge
\frac1{64}
\sum_{m=\lceil\sqrt r\rceil+1}^{\lfloor\sqrt{S-1}\rfloor}m^2.
\tag{6.8}
\]

Here

\[
r=\log\!\left(\frac{256}{\eta^2}\log n+O(1)\right)=O(\log S),
\]

so the omitted lower-end contribution is only `O((log S)^(3/2))`, while the upper sum is asymptotic to `S^(3/2)/3`. Therefore

\[
\boxed{
\frac{\mathfrak M(r_n,s_n)}{s_n-r_n}\longrightarrow\infty.
}
\tag{6.9}
\]

In particular `T10.cond` holds with enormous room (eventually with any prescribed `kappa>1`). T10 yields:

### Corollary I0077-R07-C10.1 — sparse drifting-pulse tube excludes every FBM

For the continuous tube defined by (6.1)–(6.2) and the stated interpolation,

\[
\boxed{
\mathbb P\!\left(
\exists R<\infty:
(t,X_t)\in D_{L,U}
\quad\forall t\le-R
\right)=0
}
\]

for every forward Brownian motion `X`.

The obstruction is genuinely sporadic: the constraining pulse-time fraction tends to zero, yet the cumulative killed-OU cost is superlinear in logarithmic time.

## 7. Why this is a ninth family rather than another parameter of family 8

Family 8 (T9) has bounded normalized walls and gains its exponent from a fixed positive-density set of fixed-severity narrow pulses. The present canonical family has two qualitative invariants preserved by Brownian rescaling (which merely translates logarithmic time):

1. the pulse-time density is `0`, not positive;
2. the pulse centers satisfy `m->infinity`, so the normalized walls are unbounded on a sparse set and the individual OU killing rates diverge.

No logarithmic translation, Brownian scaling, reflection, or coefficient change converts zero pulse density into positive density or an unbounded normalized pulse center into a bounded one. T9's hypothesis `p>0` fails here, while T10 succeeds through weighted spectral mass. This is a structurally new source-level regime, not a second parameter value of T9.

Hence the frozen metric legitimately moves

\[
\boxed{8\to9.}
\]

## 8. Section-B method outcomes

### #4 — PROVE SOMETHING WEAKER, COMPLETELY

**Attempt.** The run-8 suggested target was a converse/existence theorem below the average killed-OU threshold. I tried to identify the missing source-style terminal-time lower bound. The nonstationary nonsyndetic setting provides no uniform positive success probability from a mere average exponent `<1`; sparse wide deserts break the naive block recursion.

**Outcome: success after narrowing the claim.** Instead of pretending that gap closed, I proved the complete weighted-obstruction theorem T10 and an explicit zero-density family. This moves the metric while leaving the true converse honestly open.

### #8 — GO THE OTHER WAY AND DISCRETIZE

**Attempt.** Discretize arbitrary Brownian terminal times into unit cells `[n,n+1]` and logarithmic motion into isolated pulse blocks. The Brownian modulus transfers a real good terminal to an integer terminal with one extra `eta` padding; the pulse blocks then multiply their exact `L^2(gamma)` spectral costs.

**Outcome: success.** It produced the summable terminal bound (5.7) and removed every independence ambiguity from the FBM transfer.

### #26 — HUNT THE SPORADIC CASE

**Attempt.** Force pulses to occur at `m^2`, so their time density is zero, and compensate by moving the allowed normalized interval out to height `m`. The harmonic-oscillator transform shows the OU Dirichlet eigenvalue grows at least quadratically in `m`.

**Outcome: success.** Sparse pulses contribute total cost `Theta(S^(3/2))` on horizon `S`, proving a universal obstruction in a regime where the positive-density theorem T9 is silent.

## 9. Prior-art qualification

The mathematical ingredients are classical individually:

- Brownian/Lamperti correspondence with stationary OU;
- killed-diffusion `L^2` semigroup contraction;
- the OU-to-harmonic-oscillator conjugation;
- reflection/Gaussian modulus bounds and Borel–Cantelli.

The dated bounded search found literature on OU absorption/principal eigenvalues and on nonautonomous parabolic principal exponents, but no accessible later paper explicitly resolving Burdzy–Scheutzow Problem 7.8 or stating this zero-density drifting-pulse FBM consequence. I therefore record **prior-art search performed / publication novelty UNVERIFIED**. Negative search is not a novelty certificate.

## 10. Closure/audits

Problem 7.8 remains **PARTIAL**, not closed. T10/C10.1 have no independent OTHER-track audit yet, including no P26 audit, so the owner's closure standard is not met and no `paper_*` folder is created.

There is no finite combinatorial core in T10. The only numerical threshold used for the canonical family is the exact symbolic inequality (6.7), proved on the page. I therefore did not spend the run manufacturing a checker whose sole purpose would be to restate elementary rational algebra.

## 11. Model/scheduler interface and permission status

The limitation remains real. The exposed scheduler interface offers task title/prompt, schedule, enablement, and timing-mode controls. It exposes **no model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` remains a prompt request, not a verified runtime setting, from this surface.

To change the runtime for real, the product must expose model/reasoning controls to the task owner, or an authorized owner/admin/platform-support context must change the task's underlying runtime configuration. A repository edit cannot do this.

The earlier `You cannot modify this task` result for one P26 context is not a universal P26 immutability result: current `RESULTS.md` records that a later full P26 prompt update succeeded from another authorized context, while another deployment context denied edits. The legitimate workaround for a denied task is therefore its authorized owning/admin context (or platform support), not a worker-level bypass and not a duplicate schedule.

No scheduler modification was attempted in this run, per the current owner instruction.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source: "Burdzy--Scheutzow (2014), Forward Brownian Motion, Problem 7.8 / I0077"
  target: "Generalize Theorem 4.3 to genuinely distinct nonparabolic space-time shape families"
  metric: "number of distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 8
  after: 9
  status: PARTIAL
  unchanged_count: 0
  methods: [4, 8, 26]
  new_claims:
    - "I0077-R07-T10 weighted sparse-pulse universal FBM obstruction"
    - "I0077-R07-C10.1 zero-density drifting-pulse explicit family"
  exact_evidence:
    - "runs/R07/20260917T0122Z_i0077_sparse_drifting_pulses_09.md"
  audits: []
  prior_art: "bounded dated search performed 2026-09-17; exact Problem 7.8 resolution not found; novelty UNVERIFIED"
  access_limits:
    - "large intake JSONL corpus connector-truncated; exact I0077/ownership/prior-attempt searches recovered directly"
  scheduler_model_selector: "not exposed"
  scheduler_reasoning_selector: "not exposed"
```

## 13. Next high-value direction

The weighted spectral-mass theorem now separates three obstruction mechanisms at parabolic scale: positive-density fixed killing, zero-density increasing killing, and persistent periodic killing. The genuinely missing complementary direction is existence when the nonautonomous survival cost is below one **and** terminal slow points recur with enough uniformity to define stopping pieces.

The next run should not add another easy pulse example. The unused-method triple recorded for the next attack is **#10 DERANDOMIZE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #22 READ THE FAILURES, NOT THE SUCCESSES**. The concrete target is a finite-state/step-boundary killed-OU transfer matrix that can expose whether a subcritical product exponent `<1` is enough to recover a source-style terminal-point construction, and if not, exactly which local phase obstruction breaks it.
