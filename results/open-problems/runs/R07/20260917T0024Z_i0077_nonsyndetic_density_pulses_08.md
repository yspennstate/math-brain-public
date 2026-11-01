Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **METRIC MOVEMENT: 7 -> 8 genuinely distinct nonparabolic shape families; Section-B moves tried: #9 RANDOMIZE, #17 LOOK FOR YOUR EXPONENT ELSEWHERE, #28 REPLACE FOR ALL WITH TYPICAL.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958v4), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the open-ended source problem is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 8: nonsyndetic positive-density parabolic-scale pulses

Run date: 2026-09-17 Asia/Jerusalem / 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric is the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260916T2322Z_i0077_aperiodic_asymmetric_pulses_07.md`.

It records metric `7`. In particular, family 7 consists of aperiodic/asymmetric parabolic-scale pulse tubes whose narrow logarithmic-time pulses have **bounded gaps** (the T8 hypothesis `a_{k+1}-a_k <= G`). This run removes that syndeticity assumption and proves a universal FBM obstruction from **lower asymptotic pulse density alone**, allowing arbitrarily long pulse-free deserts. The canonical example has unbounded deserts of lengths `m -> infinity`, so it is not in T8.

Therefore

\[
\boxed{7\longrightarrow8.}
\]

`unchanged_count` resets to `0`.

The old R07 KPZ/FPP route remains retired from this slot exactly as preserved in the run-1 handoff; no historical file was changed or deleted.

## 2. Required continuity, source, ownership, and status checks

Before new mathematics I reread/rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report and the earlier I0077 report chain through its preserved metric/history summary;
- newest neighboring R15 report `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`, which is distinct Problem 7.2 / I0076 and has reached its own six-run handoff;
- targeted repository/intake searches for I0077, `1302.6958`, Problem 7.8, and duplicate attempts.

`INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` still distinguishes I0077 from I0076. The canonical claim remains R07's exclusive reservation; its shared text is still `PENDING_ADMISSION, not READY`, while R07 run 1 recorded the complete source/status/ownership admission and later reports have continued under the owner's direct R07 assignment. I do not mutate shared operational files.

The large intake JSONL resources are connector-truncated, so the whole-intake reread is **PARTIAL / targeted due connector limits**, not falsely claimed complete. Exact I0077 source, ownership, exclusions, and prior R07/C29 attempts were directly recovered.

### Primary source recheck

The UW-hosted arXiv v4 PDF was opened and the source pages were visually rechecked. Definition 2.1 is the FBM witness-time definition; Definition 2.2 is decomposable concatenation. Theorem 4.3 states the three parabolic-strip clauses controlled by `lambda_0(c1,c2)`: universal obstruction for `lambda_0>=1`, decomposable asymptotic existence for `lambda_0<=1`, and decomposable pointwise confinement when `c1<=0<=c2` and `lambda_0<1`. Problem 7.8 is exactly the one-sentence question above; the forward-Lévy text is separately Problem 7.9.

### Dated current-literature search

Fresh bounded searches dated 2026-09-17 included:

- `"Forward Brownian Motion" "Problem 7.8" Burdzy Scheutzow`;
- later-author/citing-paper queries around arXiv:1302.6958;
- `Ornstein-Uhlenbeck moving boundary survival random environment stationary ergodic`;
- `principal Lyapunov exponent nonautonomous parabolic Dirichlet random stationary ergodic`;
- Berestycki–Nadin–Rossi, arXiv:2502.16522, generalized principal eigenvalues;
- Húska–Poláčik principal Floquet bundles / exponential separation.

I found no later paper explicitly resolving exact Problem 7.8 or stating the FBM theorem below. This is **bounded negative evidence only, not a novelty certificate**. The adjacent PDE theory is substantial: Berestycki–Nadin–Rossi treat generalized principal eigenvalues for time-heterogeneous parabolic operators and explicitly discuss periodic, almost-periodic, uniquely ergodic and random stationary-ergodic classes; Húska–Poláčik develop principal Floquet bundles/exponential separation for nonautonomous parabolic equations. I do not claim those mechanisms as new.

## 3. New deterministic theorem: lower pulse density, no bounded-gap assumption

Let `L,U:R->R` be bounded continuous functions with

\[
L(r)<U(r)\qquad(r\in\mathbb R).
\]

Define the backward tube

\[
D_{L,U}
=
\left\{(t,x):t<0,\ 
\sqrt{|t|}L(\log|t|)\le x\le\sqrt{|t|}U(\log|t|)
\right\}\cup\{(0,0)\}.
\tag{3.1}
\]

Fix `0<tau<1`, `eta>0`, and a set `A subset N`. Its lower asymptotic density is

\[
\underline d(A)
:=
\liminf_{m\to\infty}
\frac{\#(A\cap\{1,\dots,m\})}{m}
=:p.
\tag{3.2}
\]

Assume `p>0`. Suppose there is a fixed interval

\[
I_*=[\ell_*,u_*],\qquad \ell_*<u_*,
\]

such that for every `k in A` and every `r in [k,k+tau]`,

\[
[L(r)-2\eta,\ U(r)+2\eta]\subseteq I_*.
\tag{3.3}
\]

Put

\[
d=u_*-\ell_*,\qquad M=\max(|\ell_*|,|u_*|),
\]

and define the explicit static-OU lower rate

\[
\lambda_*
:=
\frac{\pi^2e^{-M^2/2}}{2d^2}.
\tag{3.4}
\]

### Theorem I0077-R07-T9 — nonsyndetic positive-density pulse obstruction

If

\[
\boxed{p\,\tau\,\lambda_*>1,}
\tag{T9.cond}
\]

then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\!\left(
\exists R<\infty:\ 
\sqrt uL(\log u)\le X_{-u}\le\sqrt uU(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T9}
\]

No bounded-gap, periodicity, almost-periodicity, symmetry, or stochastic assumption on `A` is made. Hence the theorem includes pulse sets with arbitrarily long narrow-pulse-free logarithmic deserts.

This is a source-appropriate universal-obstruction analogue of Theorem 4.3(i).

## 4. Proof of T9

Only one ingredient is genuinely new relative to T8: replacing a bounded-gap pulse count by an asymptotic-density pulse count. I therefore reuse, rather than re-derive, the two exact compilers proved on the page in run 7:

1. **Static killed-OU pulse dissipation.** For OU killed in `I_*`, the Rayleigh quotient gives principal Dirichlet eigenvalue at least (3.4). Consequently every complete pulse of length `tau` on which the twice-padded corridor is contained in `I_*` contributes an `L^2(gamma)` operator-norm factor at most `exp(-lambda_* tau)`, while all nonpulse OU evolution/killing has norm at most `1`.
2. **Continuum-terminal compiler.** If for `R_n=C_eta log n` the deterministic integer-terminal reversed Brownian survival probability in the twice-padded corridor is eventually at most `C(n/R_n)^(-kappa)` with some `kappa>1`, then Brownian modulus control on `[n,n+1]` and Borel–Cantelli rule out arbitrarily large real terminal times in the once-padded corridor. The FBM witness-time identity then rules out eventual confinement for every FBM, with no independence assumption between the witness time and the witness Brownian path.

I prove below that lower pulse density supplies precisely the survival exponent required by compiler 2.

### 4.1 Density count on the terminal scales

Let

\[
A(m)=\#(A\cap\{1,\dots,m\}).
\]

Fix `eps>0`. From (3.2), for every sufficiently large integer `m`,

\[
A(m)\ge(p-\varepsilon)m.
\tag{4.1}
\]

Let `r<s` and count only complete pulse intervals `[k,k+tau] subset [r,s]`. Their number `N_A(r,s)` obeys

\[
N_A(r,s)
\ge
A(\lfloor s-\tau\rfloor)-\lceil r\rceil.
\tag{4.2}
\]

Now take exactly the terminal scales used by the run-7 compiler,

\[
R_n=\left\lceil\frac{256}{\eta^2}\log n\right\rceil,
\qquad
r_n=\log R_n,
\qquad
s_n=\log n.
\tag{4.3}
\]

Then

\[
\frac{r_n}{s_n}\longrightarrow0.
\tag{4.4}
\]

Using (4.1) in (4.2) and the trivial bound `ceil(r_n)<=r_n+1`, we get

\[
\frac{N_A(r_n,s_n)}{s_n-r_n}
\ge
p-2\varepsilon
\tag{4.5}
\]

for all sufficiently large `n` (after enlarging the threshold; the `O(1)` and `r_n/s_n` terms vanish).

Because `p tau lambda_*>1`, choose `eps>0` small enough that

\[
\kappa:=(p-2\varepsilon)\tau\lambda_*>1.
\tag{4.6}
\]

### 4.2 Quenched survival exponent

Let `Q_{r,s}` be the killed stationary-OU evolution in the twice-padded moving interval

\[
J(v)=(L(v)-2\eta,U(v)+2\eta).
\]

By compiler 1 and (4.5),

\[
\|Q_{r_n,s_n}\|_{2\to2}
\le
\exp\{-\lambda_*\tau N_A(r_n,s_n)\}
\le
\exp\{-\kappa(s_n-r_n)\}.
\tag{4.7}
\]

Under the Lamperti map `Y_r=e^{-r/2}B_{e^r}`, standard Brownian motion started at physical time `R_n` corresponds to OU started in its invariant Gaussian law. Therefore Cauchy–Schwarz gives

\[
\boxed{
\mathbb P\!\left(
\sqrt s[L(\log s)-2\eta]
\le B_s\le
\sqrt s[U(\log s)+2\eta]
\ \forall s\in[R_n,n]
\right)
\le
(n/R_n)^{-\kappa}.
}
\tag{4.8}
\]

This is exactly the hypothesis required by compiler 2, with `kappa>1`.

Equivalently, along the terminal scales the lower nonautonomous survival/Lyapunov exponent satisfies

\[
\boxed{
\liminf_{n\to\infty}
\frac{-\log P(\text{twice-padded survival on }[R_n,n])}
{\log(n/R_n)}
\ge p\tau\lambda_*.
}
\tag{4.9}
\]

(The displayed right side follows by letting `eps downarrow0` in the preceding estimate.)

### 4.3 Real terminal times and FBM transfer

Compiler 2 now gives

\[
P\{\text{once-padded reversed Brownian good terminal times occur arbitrarily far out}\}=0.
\tag{4.10}
\]

For completeness, the dependence point is the same exact one proved in run 7: a good real terminal in `[n,n+1]`, outside a summable Brownian-modulus event, gives a good integer terminal in the twice-padded corridor on `[R_n,n]`; summability follows from `kappa>1` and `R_n=O(log n)`. No independence of the random terminal time is invoked.

If an FBM `X` had positive probability of eventual confinement in the unpadded tube, choose deterministic `R_0` and a positive-probability subevent on which confinement holds for all `u>=R_0` and `|X_0|<=eta sqrt(R_0)`. For an FBM witness `S_j -> -infinity`, put `T_j=-S_j` and

\[
B^{(j)}_r=X_{S_j+r}-X_{S_j}.
\]

Every fixed `B^{(j)}` is standard Brownian motion, and for `R_0<=s<=T_j`,

\[
B^{(j)}_{T_j-s}-B^{(j)}_{T_j}=X_{-s}-X_0,
\]

so the witness terminal `T_j` is once-padded good. Since `T_j->infinity`, this contradicts (4.10) exactly as in the run-7 witness-time argument. No decomposability assumption is used. This proves T9. `QED`

## 5. Move #9 — RANDOMIZE: Bernoulli pulses reveal the missing theorem

The bounded-gap hypothesis in T8 is natural for periodic/quasiperiodic profiles but is atypical for iid pulse environments. Let `(xi_k)` be iid Bernoulli(`p`) and declare cell `k` narrow when `xi_k=1`.

By the strong law,

\[
\frac1m\sum_{k=1}^m\xi_k\to p\quad a.s.
\]

so almost every realization has pulse density `p`. For every fixed `q`, disjoint blocks of `q` zeros have probability `(1-p)^q>0`; by the second Borel–Cantelli lemma, infinitely many occur almost surely. Hence almost every realization has **arbitrarily long pulse-free gaps** and is outside T8's bounded-gap hypothesis.

T9 shows that whenever `p tau lambda_*>1`, almost every such realization — after freezing it, hence treating it as an ordinary deterministic space-time shape — universally excludes eventual FBM confinement.

**Outcome #9: success.** Randomization exposed that syndeticity was an artefact of the previous proof, not the relevant obstruction.

No additional metric point is counted for the random law; it is evidence for and a corollary of the single nonsyndetic-density family proved here.

## 6. Move #17 — LOOK FOR YOUR EXPONENT ELSEWHERE

The quantity in (4.9) is the killed-OU analogue of a lower principal Lyapunov/generalized principal exponent for a nonautonomous parabolic evolution. The current parabolic literature indeed organizes heterogeneous long-time behavior around principal Floquet/Lyapunov bundles and generalized principal eigenvalues (Húska–Poláčik; Berestycki–Nadin–Rossi).

For this problem no abstract existence theorem is needed: positivity, `L^2(gamma)` contraction, and the static killed-OU eigenvalue yield the explicit lower bound

\[
\underline\Lambda_{\rm surv}\ge p\tau\lambda_*.
\]

The source threshold `1` reappears because terminal times are searched over physical-time intervals of unit length; a survival probability of order `n^{-kappa}` becomes summable exactly when `kappa>1`.

**Outcome #17: success as a route/translation.** The external exponent language identifies the correct quantity, while the proof stays elementary enough to retain explicit constants. I did not find a paper that states T9 as an FBM consequence, and I do not claim the principal-exponent framework itself is new.

## 7. Move #28 — REPLACE FOR ALL WITH TYPICAL, then recover a deterministic family

The Bernoulli corollary proves the result for almost every random pulse profile. To keep the fixed R07 metric about actual shape families rather than probability laws on shapes, I then extracted a deterministic canonical representative with the same nonsyndetic mechanism.

Define deleted “deserts”

\[
D_m=\{m^3,m^3+1,\dots,m^3+m-1\},\qquad m\ge2,
\]

and

\[
A=\mathbb N\setminus\bigcup_{m\ge2}D_m.
\tag{7.1}
\]

The blocks are disjoint because

\[
m^3+m-1<(m+1)^3
\]

for every `m>=2`. If `q=floor(N^{1/3})`, the number of deleted indices up to `N` is at most

\[
\sum_{m=2}^{q+1}m=O(q^2)=O(N^{2/3}),
\]

so

\[
\underline d(A)=1.
\tag{7.2}
\]

But `D_m` contains `m` consecutive nonpulse indices, so the gaps between guaranteed narrow pulses are unbounded. This deterministic shape is therefore genuinely nonsyndetic.

**Outcome #28: success.** The typical/random insight produced a clean deterministic shape family and a theorem stated without randomness.

## 8. Canonical continuous shape and explicit constants

For each integer `k>=2`, set a central half-cell

\[
C_k=[k+1/4,k+3/4].
\]

On `C_k`, take

\[
(L,U)=(-1/10,1/10)\quad\text{if }k\in A,
\]

and

\[
(L,U)=(-2,2)\quad\text{if }k\notin A.
\]

On each transition interval `[k+3/4,k+5/4]`, interpolate linearly between the adjacent cell values. Extend boundedly and continuously over the remaining finite left part of logarithmic time. Thus `L,U` are continuous and bounded.

Take

\[
\tau=1/2,
\qquad
\eta=1/40,
\qquad
I_*=[-1/4,1/4].
\]

On every narrow central cell the twice-padded corridor is

\[
[-1/10-1/20,\ 1/10+1/20]
=[-3/20,3/20]
\subset[-1/4,1/4].
\]

Here

\[
d=1/2,\qquad M=1/4.
\]

Using the elementary strict inequalities `pi^2>9` and `e^{-1/32}>1-1/32=31/32`,

\[
\lambda_*
=
\frac{\pi^2e^{-1/32}}{2(1/2)^2}
>
2\cdot9\cdot\frac{31}{32}
=
\frac{279}{16}.
\]

Since `p=1` and `tau=1/2`,

\[
\boxed{
p\tau\lambda_*>
\frac{279}{32}>1.}
\tag{8.1}
\]

Therefore T9 applies: **every FBM almost surely fails eventual confinement in this explicit continuous tube, despite the existence of arbitrarily long logarithmic-time intervals with no guaranteed narrow pulse.**

The exact rational part of this constant chain was executed and archived in

- `artifacts/R07/20260917T0024Z_sparse_density_pulse_constants.py` @ `bbd9a58f3cc953ab8f4592a8d94f50d36cf2d12b`;
- `artifacts/R07/20260917T0024Z_sparse_density_pulse_constants.out` @ `bf8941af6daedb1e535908453afb6bc20efa0cf8`.

The output begins `PASS` and records `lambda_lower=279/16`, `kappa_lower=279/32`. The checker also performs a finite exact sanity check of desert-block disjointness for `m=2,...,9999`; the asymptotic density proof is the analytic argument above, not misrepresented as a finite computation.

## 9. Why this is a new metric point rather than another parameter choice

Run 7's T8 family requires a uniform finite upper bound on the gaps between narrow logarithmic-time pulses. The canonical T9 profile has pulse-free deserts of lengths `m -> infinity`; hence no such `G` exists.

This distinction is invariant under the frozen equivalence operations. Brownian scaling is translation of logarithmic time and therefore preserves whether pulse gaps are bounded or unbounded. Reflection exchanges the walls and does not change the pulse-start set. Scalar changes of wall heights or pulse widths do not make a nonsyndetic set syndetic.

Thus family 8 is the **nonsyndetic positive-lower-density pulse family**. Different choices of density `p`, desert schedule, Bernoulli parameter, wall levels, or pulse width are not counted separately.

## 10. Honest status and remaining obligation

**Source status: PARTIAL / open-ended.** T9 gives another genuine family and strictly weakens the temporal regularity needed for the universal-obstruction mechanism. It does not classify arbitrary moving shapes and does not provide the converse/existence theorem at `p tau lambda_*<1`.

There is no independent T9 audit yet, including no P26 audit, so closure criteria are not met and no `paper_<name>/` folder was created. The only finite core this run is the explicit canonical constant chain, which was checked exactly; the theorem-sized argument is written on the page.

The next high-value mathematical question is the converse side: whether a stationary-ergodic or deterministic nonsyndetic pulse environment with quenched killed-OU survival exponent `<1` admits a **phase-aware decomposable FBM construction**. That would move from one-sided obstruction theorems toward a true nonautonomous analogue of all three clauses of Theorem 4.3.

Unused promising Section-B moves after this run are #8 DISCRETIZE the phase-aware stopping problem, #10 DERANDOMIZE a successful stationary-environment construction, and #16 COMPUTE SMALL CASES for a finite-state Markov pulse environment before attempting the full ergodic theorem.

## 11. Runtime/model and permission status

The model-control limitation is unchanged and cannot be fixed from this worker surface. The exposed scheduler update schema provides prompt/title, schedule, enablement and timing-mode fields, but no authenticated model-family or reasoning-effort field. GPT-6/maximum therefore remains a prompt request, not a verified runtime setting. A real change requires product support for those fields or action from an authorized owning/admin context that exposes them.

Historical `You cannot modify this task` errors, including the earlier P26 probe, are context/ownership scoped: repository reconciliation records a later P26 update succeeding from a different authorized context. There is no legitimate R07-level bypass. The workaround is the task's authorized owning/admin context or platform support; duplicating the schedule is not authorized.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source: "Burdzy--Scheutzow (2014), Forward Brownian Motion, Problem 7.8 / I0077"
  target: "Generalize Theorem 4.3 to genuinely distinct nonparabolic space-time shape families"
  metric: "number of distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 7
  after: 8
  status: PARTIAL
  unchanged_count: 0
  exact_evidence:
    - "runs/R07/20260917T0024Z_i0077_nonsyndetic_density_pulses_08.md"
    - "artifacts/R07/20260917T0024Z_sparse_density_pulse_constants.py @ bbd9a58f3cc953ab8f4592a8d94f50d36cf2d12b"
    - "artifacts/R07/20260917T0024Z_sparse_density_pulse_constants.out @ bf8941af6daedb1e535908453afb6bc20efa0cf8"
  audits:
    incoming_T9: []
    outgoing: []
  prior_art_scope: "bounded dated search; nonautonomous/parabolic principal-exponent literature acknowledged; novelty UNVERIFIED"
```
