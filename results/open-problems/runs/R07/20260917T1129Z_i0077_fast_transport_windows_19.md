Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 18 -> 19 genuinely distinct nonparabolic shape families; Section-B moves tried: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #19 MAKE IT AN ALGORITHM.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the open-ended source request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 19: fast-transport log-periodic windows

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and frozen metric

The fixed R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative report is

`runs/R07/20260917T1022Z_i0077_infinite_parabolic_combs_18.md`,

which moved the metric `17 -> 18` and used Section-B moves `#7,#13,#21`. This run does not repeat that triple. All thirty moves have already appeared at least once somewhere in the I0077 sequence, so this is another second-cycle triple; I do not falsely label the numbers “never previously used on the problem.”

The new counted family is a **log-periodically shuttling parabolic window of constant normalized width**, with a transport obstruction that survives even when **every frozen-in-log-time interval is individually subcritical for the source OU exponent**. This is not a narrow-pulse theorem.

The metric moves

\[
\boxed{18\longrightarrow19}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains preserved and retired by its immutable handoff; no historical R07 file was modified or deleted.

## 2. Required repository / admission reread

Before new mathematics I reread or rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the owner-directive lineage it points to;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report and the searchable R07/I0077 history through run 18;
- newest visible R15 state, which preserves the retirement/handoff of distinct Burdzy–Scheutzow Problem 7.2 / I0076 and is now on another source;
- C29’s earlier I0077 duplicate-exclusion history;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` still lists I0077 separately. `operations/claims/I0077.md` still reserves I0077 to R07 and still literally says `PENDING_ADMISSION, not READY`; run 1 completed the mathematical/source admission checks, but this attacking worker does not mutate that shared claim file. The root `RESULTS.md` row is historically stale relative to the immutable R07 run chain and is not used to reset the metric.

The large `probability_1000_intake_*/problems.jsonl` files cannot be rendered literally row-by-row through the exposed connector without truncation. Intake reread is therefore recorded honestly as **PARTIAL / targeted due connector limits**, with the exact I0077 record, ownership, duplicate-attempt and adjacent-scope checks recovered.

## 3. Primary source benchmark recovered again

The primary source was rechecked directly, including Definitions 2.1–2.2, Remarks 4.1–4.2, Theorem 4.3, and the open-problem page.

An FBM is a continuous real-indexed process `X`, normalized in the paper by `X_0=0`, for which there are random times `S_j -> -infinity` such that each centered future

\[
(X_{S_j+t}-X_{S_j})_{t\ge0}
\]

is standard Brownian motion. A decomposable FBM is a concatenation of independent Brownian pieces stopped at finite stopping times.

For `-infinity <= c_1<c_2<=infinity`, the source uses `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the exact parabolic strip for every `t<=0`.

Remark 4.2 records the critical pairs `(-infinity,-1)`, `(-1,1)`, and `(1,infinity)`, all with `lambda_0=1`. Remark 4.1 records endpoint continuity and strict domain monotonicity.

Problem 7.8 is exactly the one-sentence question asking whether Theorem 4.3 can be generalized “from parabolas to other space-time shapes.” The forward-Lévy sentence following it is separately Problem 7.9 and is not part of I0077.

## 4. Fresh current-status / prior-art pass — 2026-09-17

Fresh bounded web searches included:

- the exact quoted text of Problem 7.8 and exact title/arXiv ID;
- `Forward Brownian Motion` with `other space-time shapes`, `moving interval`, `periodic window`, and `Ornstein-Uhlenbeck`;
- periodic and non-autonomous OU first-passage/survival;
- Brownian survival under step, affine and intermittent moving boundaries;
- later/citing material around Burdzy–Scheutzow.

The closest mechanisms located remain ordinary first-passage / survival theory, not an FBM resolution: Sacerdote (1990), *Asymptotic behaviour of Ornstein-Uhlenbeck first-passage-time density through periodic boundaries*; Giorgini–Moon–Wettlaufer (2024), *Analytical Survival Analysis of the Non-autonomous Ornstein–Uhlenbeck Process*; Guillaume’s 2015 and 2024 moving/intermittent Brownian-boundary calculations; and Burdzy–Kang–Ramanan’s time-dependent-interval Skorokhod problem (reflection rather than absorption/confinement).

I found no later paper in these bounded dated searches explicitly resolving exact Problem 7.8 or stating the FBM transport theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**. The Gaussian OU transition formula and first-passage viewpoint are classical and are not claimed new.

## 5. Move #2 — ATTACK THE NEGATION FIRST: falsify the frozen-eigenvalue extension

A very natural attempted generalization of Theorem 4.3 is:

> if a moving normalized interval is source-subcritical at every frozen log-time, i.e. `lambda_0(L(r),U(r))<1` for every `r`, then some decomposable FBM should be able to follow the moving tube.

This run attacks that statement first rather than trying to prove it. The attack succeeds: a wide interval can move so fast in logarithmic time that the OU image has to make a rare macroscopic transition once per period. Repeating those transport costs gives a survival exponent greater than one even though **no frozen slice has exponent at least one**.

This is a refutation of the proposed extension mechanism only. It is **not** a refutation of the source’s open-ended Problem 7.8.

## 6. Move #18 — SAY IT IN ANOTHER LANGUAGE: confinement becomes an OU tracking problem

Let `P>0`, `0<tau<P`, `a>0`, `eta>0`, `h>0`, and let `m:R->R` be bounded, `C^1`, and `P`-periodic. Define

\[
I(r)=[m(r)-a,m(r)+a]
\]

and the backward space-time tube

\[
\boxed{
\mathcal T_{m,a}
=
\left\{(-u,x):u>0,\ 
\sqrt u\,[m(\log u)-a]
\le x\le
\sqrt u\,[m(\log u)+a]
\right\}\cup\{(0,0)\}.
}
\tag{6.1}
\]

Assume there is a phase `r_0` such that the **twice-padded** endpoint windows satisfy

\[
m(r_0)+a+2\eta\le-h,
\qquad
m(r_0+\tau)-a-2\eta\ge h.
\tag{6.2}
\]

For a standard Brownian motion `B`, the Lamperti process

\[
Y_r=e^{-r/2}B_{e^r}
\tag{6.3}
\]

is stationary OU with generator

\[
\mathcal A=\frac12(\partial_{xx}-x\partial_x)
\]

and transition law

\[
Y_{r+\tau}
=e^{-\tau/2}Y_r+\sqrt{1-e^{-\tau}}\,Z,
\qquad Z\sim N(0,1).
\tag{6.4}
\]

Define

\[
z_*
:=
\frac{h(1+e^{-\tau/2})}{\sqrt{1-e^{-\tau}}},
\qquad
q_*:=\mathbb P(Z\ge z_*),
\qquad
\kappa_*:=-\frac1P\log q_*.
\tag{6.5}
\]

The key observation is transport, not killing in a narrow interval. If at phase `r_0+kP` the padded tube forces `Y<=-h` and at phase `r_0+kP+tau` it forces `Y>=h`, then conditional on every possible past and every `Y_{r_0+kP}<=-h`, (6.4) gives

\[
\mathbb P\!\left(
Y_{r_0+kP+\tau}\ge h
\mid\mathcal F_{r_0+kP}
ight)
\le q_*.
\tag{6.6}
\]

Indeed the required Gaussian innovation is at least

\[
\frac{h-e^{-\tau/2}(-h)}{\sqrt{1-e^{-\tau}}}=z_*.
\]

This changes the problem from a moving-boundary spectral problem into a repeated Gaussian tracking problem.

## 7. I0077-R07-T20 — fast-transport moving-window obstruction

**Theorem T20.** Under (6.2), if

\[
\boxed{\kappa_*>1,}
\tag{7.1}
\]

then every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
X_{-u}\in \sqrt u\,I(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T20}
\]

Thus no FBM can be pointwise confined to `mathcal T_{m,a}` on the whole negative half-line either.

No assumption is made that any frozen interval has `lambda_0>=1`. In Section 11 below I construct a profile for which **every** frozen interval has `lambda_0<1` while T20 still applies.

## 8. Move #19 — MAKE IT AN ALGORITHM: one forced transition per period

Consider stationary OU survival in the twice-padded moving corridor

\[
I^{+2\eta}(r)
=[m(r)-a-2\eta,m(r)+a+2\eta]
\tag{8.1}
\]

on a log-time interval `[r,s]` of length `H=s-r`.

Inside every full period there is one ordered pair of phases

\[
a_k=r_0+kP,
\qquad
b_k=a_k+\tau
\]

for which survival implies

\[
Y_{a_k}\le-h,
\qquad
Y_{b_k}\ge h.
\tag{8.2}
\]

The number `N(r,s)` of complete such ordered pairs in `[r,s]` obeys

\[
N(r,s)\ge \frac{H}{P}-3.
\tag{8.3}
\]

By the OU Markov property, tower property, and (6.6), each required transition costs conditional probability at most `q_*`, regardless of what happened between earlier periods. Hence

\[
\mathbb P\left(
Y_v\in I^{+2\eta}(v)
\ \forall v\in[r,s]
\right)
\le q_*^{N(r,s)}
\le q_*^{-3}e^{-\kappa_*H}.
\tag{8.4}
\]

Returning to Brownian physical time gives the fixed-terminal survival estimate

\[
\boxed{
\mathbb P\left(
B_v\in\sqrt v\,I^{+2\eta}(\log v)
\ \forall v\in[R,T]
\right)
\le C(T/R)^{-\kappa_*},
}
\tag{8.5}
\]

with `C=q_*^{-3}`. The proof used only endpoint transition probabilities; it did not need a Floquet eigenvalue, a narrow interval, or a principal-eigenvalue lower bound.

## 9. Continuum terminal times — full dependence-safe compiler

The FBM witness time is random and need not be independent of its Brownian future. Therefore a fixed deterministic-terminal estimate is not enough. We prove the continuum-terminal statement needed for the FBM transfer.

Fix `R_0>0`. A time `t` is called **good** for a standard Brownian motion `B` if

\[
B_{t-u}-B_t
\in
\sqrt u\,I(\log u)
\qquad\forall u\in[R_0,t].
\tag{9.1}
\]

I claim that, almost surely, the set of good terminal times is bounded.

For integer `n`, define

\[
M_n:=\max_{0\le k\le n}\operatorname{osc}_{[k,k+2]}B.
\tag{9.2}
\]

If `M_n>8\sqrt{\log n}`, then for some `k<=n` a Brownian interval of length two has oscillation exceeding that amount. Since `osc<=2 sup|W|`, reflection plus the Gaussian Chernoff bound gives, for all sufficiently large `n`,

\[
\mathbb P(M_n>8\sqrt{\log n})\le 8n^{-3}.
\tag{9.3}
\]

Set

\[
R_n:=\left\lceil256\eta^{-2}\log n\right\rceil.
\tag{9.4}
\]

Write

\[
F_\pm(u)=\sqrt u\,[m(\log u)\pm a].
\]

Because `m` is bounded `C^1`, there is a deterministic `K<infinity` with

\[
|F_\pm'(u)|\le K/\sqrt u\qquad(u>0).
\tag{9.5}
\]

Suppose a good `t` lies in `[n,n+1]`, put `delta=t-n`, and fix `v in [R_n,n]`. Set `u=v+delta`; then `t-u=n-v`. Therefore

\[
B_{n-v}-B_n
=
[B_{t-u}-B_t]+[B_t-B_n].
\tag{9.6}
\]

On the complement of the event in (9.3), the second bracket has magnitude at most `8 sqrt(log n)`. By (9.4) this is at most `(eta/2)sqrt(v)` after harmlessly increasing the numerical constant if necessary. By (9.5), uniformly for `0<=delta<=1` and `v>=R_n`, the difference between each `F_\pm(v+delta)` and `F_\pm(v)` is also at most `(eta/2)sqrt(v)` for all sufficiently large `n`. Hence existence of a good `t in [n,n+1]` implies, except on the modulus event,

\[
B_{n-v}-B_n
\in
\sqrt v\,I^{+2\eta}(\log v)
\qquad\forall v\in[R_n,n].
\tag{9.7}
\]

For fixed integer `n`, the reversed increment process `(B_{n-v}-B_n)_{0<=v<=n}` is standard Brownian motion. Applying (8.5),

\[
\mathbb P\{\exists\text{ good }t\in[n,n+1]\}
\le
8n^{-3}+C(n/R_n)^{-\kappa_*}.
\tag{9.8}
\]

Since `R_n=O(log n)` and `kappa_*>1`, the right side is summable. Borel–Cantelli proves that only finitely many unit intervals contain a good terminal time. This establishes the claim.

## 10. Proof of the FBM statement T20

Assume contrary to T20 that eventual confinement has probability `q_0>0`. Since

\[
E_N:=\{X_{-u}\in\sqrt u I(\log u)\ \forall u\ge N\}
\]

increases to the eventual-confinement event, choose deterministic `R_0` with `P(E_{R_0})>3q_0/4`.

By Section 9, for a standard Brownian motion the probability of having any good terminal beyond `A` tends to zero as `A->infinity`. Choose deterministic `A` so large that this probability is `<q_0/8`.

Let `(S_j)` be the FBM witness sequence. Since `S_j->-infinity` a.s., choose one deterministic index `j` such that

\[
\mathbb P(-S_j<A)<q_0/8.
\tag{10.1}
\]

The single process

\[
B^{(j)}_r=X_{S_j+r}-X_{S_j},\qquad r\ge0,
\]

is standard Brownian motion. Put `t_j=-S_j`. Because the paper normalizes `X_0=0`, for every `u<=t_j`,

\[
B^{(j)}_{t_j-u}-B^{(j)}_{t_j}=X_{-u}.
\tag{10.2}
\]

Hence on `E_{R_0}\cap\{t_j\ge A\}`, the Brownian path `B^{(j)}` has a good terminal `t_j>=A`. The probability of this event is larger than

\[
3q_0/4-q_0/8=5q_0/8,
\]

contradicting the `<q_0/8` Brownian bound. No conditioning on `S_j` and no independence between `S_j` and `B^{(j)}` was used.

This proves T20.

## 11. Strong canonical example: every frozen slice is subcritical, but the moving tube is impossible

This is the substantive payoff of move #2.

Set

\[
\varepsilon=\frac12,
\qquad
\eta=\frac18,
\qquad
h=\varepsilon-2\eta=\frac14,
\qquad
P=1,
\qquad
\tau=\frac1{64}.
\tag{11.1}
\]

The source gives

\[
\lambda_0(1,\infty)=1.
\]

Strict monotonicity in the left endpoint therefore yields

\[
\lambda_0(1/2,\infty)<1.
\tag{11.2}
\]

By endpoint continuity, choose finite `R_*>1/2` such that

\[
\lambda_0(1/2,R_*)<1.
\tag{11.3}
\]

Also, since `lambda_0(-1,1)=1` and `(-1,1)` is strictly contained in `(-2,2)`,

\[
\lambda_0(-2,2)<1.
\tag{11.4}
\]

Choose

\[
K\ge \max\{9/2,\ R_*+5/2\},
\quad
a=\frac{K-1/2}{2},
\quad
M=\frac{K+1/2}{2}.
\tag{11.5}
\]

Let `m` be any `C^1`, period-one profile with values in `[-M,M]` satisfying

\[
m(0)=-M,
\qquad
m(1/64)=M.
\tag{11.6}
\]

Such a smooth periodic shuttling profile is elementary to construct by smoothing two monotone ramps with short plateaux at the extrema.

At the two distinguished phases the unpadded intervals are exactly

\[
I(0)=[-K,-1/2],
\qquad
I(1/64)=[1/2,K].
\tag{11.7}
\]

After twice-padding by `2eta=1/4`, they satisfy

\[
I^{+2\eta}(0)\subset(-\infty,-1/4],
\qquad
I^{+2\eta}(1/64)\subset[1/4,\infty),
\]

so (6.2) holds with `h=1/4`.

### Every frozen interval has exponent below one

For a center `c in [0,M]`, write `I_c=[c-a,c+a]`.

If `c<=a-2`, then `a>=2` and

\[
[-2,2]\subset I_c,
\]

so by (11.4) and domain monotonicity,

\[
\lambda_0(I_c)<1.
\]

If `c>a-2`, then

\[
c-a\le M-a=1/2,
\]

while

\[
c+a>2a-2=K-5/2\ge R_*.
\]

Thus

\[
[1/2,R_*]\subset I_c,
\]

and (11.3) again gives `lambda_0(I_c)<1`. Negative centers follow by reflection symmetry of the OU operator. Hence

\[
\boxed{
\lambda_0(m(r)-a,m(r)+a)<1
\quad\text{for every }r\in\mathbb R.
}
\tag{11.8}
\]

There is therefore **no supercritical frozen slice anywhere in the moving tube**.

### Yet transport gives exponent greater than one

From `1-e^{-tau}<=tau` and `1+e^{-tau/2}>=1`,

\[
z_*^2
\ge \frac{h^2}{\tau}
=
\frac{(1/4)^2}{1/64}
=4.
\tag{11.9}
\]

The Gaussian Chernoff bound gives

\[
q_*\le e^{-z_*^2/2}\le e^{-2}.
\]

Since `P=1`,

\[
\boxed{\kappa_*=-\log q_*\ge2>1.}
\tag{11.10}
\]

T20 therefore implies that **no FBM can even be eventually confined to this tube**, despite (11.8).

This is a clean failure of the proposed frozen-time criterion:

\[
\left[\forall r,\ \lambda_0(I(r))<1\right]
\not\Longrightarrow
\left[\exists\text{ FBM eventually following }I(\log u)\right].
\]

The obstruction is not local narrowness but the cost of repeatedly transporting an OU state from one side of the origin to the other faster than its transition variance permits.

## 12. Exact finite self-check

The substantive finite arithmetic in (11.1), (11.9), and (11.10) was checked with exact rational arithmetic and executed before archiving.

Artifacts:

- `artifacts/R07/20260917T1129Z_transport_window_check.py` — creation commit `111039dfed6c2b1ac0e996893795c9337813caf7`;
- `artifacts/R07/20260917T1129Z_transport_window_check.out` — creation commit `e9e12235d815f00537935ce9b086b50fc3bf3c0f`.

The archived output is

```text
epsilon = 1/2
eta = 1/8
h = epsilon - 2 eta = 1/4
tau = 1/64
z^2 lower bound = h^2/tau = 4
kappa lower bound = z^2/(2P) = 2
PASS
```

This is a **self-check**, not an independent audit. The source spectral comparisons in (11.2)–(11.4) are symbolic consequences of Remark 4.1/4.2 and are not being misrepresented as finite computation.

## 13. Why this is a new metric point rather than another pulse parameter

Runs 6–9 obtained obstruction from intervals that become narrow/high-eigenvalue on a positive-density or weighted family of logarithmic-time pulses. Run 15 used topology-changing disconnected gates. Run 16 used unbounded half-line slices. Run 17 moved the center by a non-Brownian physical power and run 18 used static infinitely disconnected combs.

The present family has all of the following invariant features:

1. every normalized time slice is one bounded **connected interval**;
2. its normalized width is **constant in log-time**;
3. its center remains **bounded and periodic**;
4. every frozen interval can be chosen with `lambda_0<1`;
5. impossibility comes entirely from **finite-time transport between separated subcritical windows**, not from narrow/static spectral killing.

Brownian rescaling merely translates the phase of `m(log u)` and cannot remove the recurring center shuttle or convert constant-width subcritical windows into the earlier narrow-pulse classes. The family is counted once, not once per speed, amplitude, or smooth profile.

Therefore the frozen metric moves

\[
\boxed{18\to19}.
\]

## 14. Section-B outcomes

- **#2 ATTACK THE NEGATION FIRST — SUCCESS.** The natural frozen-eigenvalue extension was falsified by the canonical profile: all `lambda_0(I(r))<1`, yet no FBM can eventually follow the tube.
- **#18 SAY IT IN ANOTHER LANGUAGE — SUCCESS.** Lamperti turns the moving space-time geometry into a stationary OU tracking problem, exposing a one-step Gaussian displacement cost invisible to frozen eigenvalues.
- **#19 MAKE IT AN ALGORITHM — SUCCESS.** Require one left-to-right OU transition per period, multiply the conditional transition bound, compile fixed terminals to arbitrary real terminals, then use one deterministic FBM witness index. This produces the complete proof of T20.

## 15. Status / closure discipline

The theorem-sized claim T20 and its canonical all-frozen-subcritical corollary are proved on this page. The exact finite arithmetic core is archived and passes its self-check. The prior-art pass is recorded above.

However, closure under the campaign protocol requires two independent OTHER-track end-to-end audits, one from P26 and one from a different track. T20 currently has neither. Therefore:

- theorem T20: **PROVED on the R07 page, unaudited externally**;
- source Problem 7.8: **PARTIAL**;
- no `paper_<name>/` folder is created;
- no public-posting or novelty claim is made.

## 16. Model / scheduler control issue

The situation remains unchanged at the actual exposed scheduler control surface used by this runtime. It offers task title/prompt, schedule, enablement, and timing-mode controls. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus `GPT-6 / maximum` can be requested in prompt text but cannot be verified or enforced here.

To change that honestly, the product/API would need to expose model and reasoning fields plus run metadata, or an authorized owning/admin product context would need to make the change through a surface that has those controls. Repository edits cannot substitute for native scheduler configuration.

The repository policy records earlier `You cannot modify this task` probes for P26/P01/P03 and instructs workers not to bypass them or create duplicates. The legitimate workaround is the authorized owning account/workspace context or platform support. No scheduler modification, permission bypass, duplicate task, or support request was attempted in this run.

## 17. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  intake: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic regions"
  metric_name: "genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  metric_before: 18
  metric_after: 19
  movement: "+1"
  new_family: "fast-transport log-periodic constant-width moving windows"
  theorem_id: "I0077-R07-T20"
  theorem_status: "PROVED_SELF_CHECKED_UNAUDITED"
  source_status: "PARTIAL"
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods: [2, 18, 19]
  finite_core: "PASS exact rational self-check"
  p26_audit: false
  second_other_track_audit: false
  novelty: "UNVERIFIED; bounded negative literature search only"
  rotation: false
  shared_root_edits: false
  scheduler_changes: false
  delivery: "private GitHub only"
```

## 18. Next research direction if R07 continues

The new obstruction suggests a genuinely different question from adding more narrow gates: determine the sharp **transport/Floquet threshold** for a periodic moving interval when every frozen exponent is below one. T20 gives the explicit sufficient criterion `-log q_*/P>1`, but not necessity. A useful next route would be to compare the true period operator with the simple endpoint-transition product and ask whether its principal Floquet exponent crosses one before any frozen slice becomes critical. That would turn the counterexample family into a quantitative moving-domain analogue of the source’s exact parabolic threshold rather than another sufficient obstruction.
