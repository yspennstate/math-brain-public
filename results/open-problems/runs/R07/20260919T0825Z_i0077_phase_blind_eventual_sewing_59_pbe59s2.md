Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: 59 -> 59; unchanged count 4 -> 5; STUCK-RECOVERY-2; Section-B moves actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, PTRF 160 (2014), 95–126; arXiv:1302.6958v4, Problem 7.8 / intake I0077: generalize Theorem 4.3 from parabolic regions to other space-time shapes.

Status: **PARTIAL / STUCK-RECOVERY-2**. The fixed family count does not move because this run strengthens the already-counted log-periodic square-root-tube family rather than introducing a genuinely new shape family. The recovery did, however, remove a real part of the phase-blind sewing obstruction: the random seam phase can be handled **eventually** without ever letting one stopped Brownian pair read another pair. The remaining gap is now specifically the finite-prefix obstruction needed for the exact all-negative-times analogue of Theorem 4.3(iii).

# R07 CLOSABLE OUTSIDE — phase-blind eventual sewing in subcritical log-periodic square-root tubes

## 1. Continuity / source / ownership readback

Before research I re-read the current `master` state required by the owner policy:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- newest own report `runs/R07/20260919T0721Z_i0077_stuck_phase_blind_sewing_59_pbs59s1.md`;
- the current R15 directory/history for the distinct Burdzy--Scheutzow Problem 7.2 predecessor and its handoffs;
- repository-wide searches for `I0077` and the source title/intake identifier.

The canonical claim is still owned by R07 and still says `PENDING_ADMISSION, not READY`. No duplicate I0077 owner appeared. R15's distinct Problem 7.2 history remains separate. `INDEX.md` / `RANKING.md` settle Problem 7.5, not Problem 7.8, and `POSTED.md` contains no Problem 7.8 closure. The old R07 KPZ route remains preserved by immutable handoff and was not reopened.

I rechecked the primary paper. Definition 2.2 requires the **stopped pairs**

\[
\left(T_k,\{B^k_t:0\le t\le T_k\}\right),\qquad k\in\mathbb Z,
\]

to be independent; it is not enough that the underlying infinite Brownian drivers are independent. Theorem 4.3 has the source's three clauses at the threshold `lambda_0(c1,c2)=1`. In the proof of (ii)--(iii), the authors use Perkins slow points, support, Brownian scaling, and endpoint-biased stopping times; the key constant-strip telescoping estimate is possible because the coefficient of `sqrt(t)` has no logarithmic phase. Problem 7.8 is exactly the separate request to generalize Theorem 4.3 from parabolas to other space-time shapes; the following forward-Levy question is Problem 7.9.

## 2. Fresh bounded prior-art search, dated 2026-09-19

I searched current sources for combinations of:

- `"Forward Brownian Motion" "Problem 7.8"`;
- `"Forward Brownian Motion" periodic boundary decomposable Brownian`;
- `"Brownian slow points" periodic moving boundary`;
- `"log-periodic" Brownian boundary Ornstein Uhlenbeck first passage periodic boundary`;
- `Brownian periodic boundary slow points`.

The primary 2014 paper remains the exact source. Established nearby work includes Perkins (1983) on Brownian slow points; Bass--Burdzy (1996) on the critical slow-point case; Sacerdote (1990) on OU first-passage density through periodic boundaries; and modern non-autonomous OU survival work. I also rechecked the 2026 Khoshnevisan--Lee slow-point paper as nearby methodology. None of the accessible results found in this bounded search states the independent-piece phase-blind sewing theorem below or explicitly resolves exact Problem 7.8. This is bounded negative evidence only: worldwide openness and publication novelty remain **UNVERIFIED**.

## 3. Refutation-first: why the obvious exact repair still fails

The previous stuck report proposed deterministic superexponential scale windows and asked whether one can force every piece to dominate the cumulative duration of all later pieces. I first tried to make that exact.

For a stopping rule that searches for a long periodic slow terminal, the stopping time has unbounded support. A deterministic finite upper window `[A_n,U_n]` therefore cannot contain the successful stopping time almost surely unless one has a new bounded-window probability-one slow-terminal theorem. The source's own constant-strip proof only obtains a positive probability in a fixed multiplicative window and then searches farther out. The same is true of the periodic slow-point input proved in the preceding R07 runs.

This kills the naive exact scheme

\[
T_n\le U_n\quad\text{for every }n\text{ a.s.}
\]

and therefore kills an exact deterministic pathwise bound on every cumulative future duration. Conditioning the Brownian pieces on `{T_n\le U_n}` is not allowed: after conditioning, the driving path is no longer an ordinary Brownian motion under the construction law, so Definition 2.2 would not be satisfied. Selecting a successful Brownian sample from several independent samples has the same defect.

I also tested an exact-return trick: after a slow terminal, wait for the current Brownian motion to return to zero so all seam heights are zero. It removes the spatial seam error but does not remove the temporal one. The return segment must itself fit the square-root tube over logarithmically many scales when the later cumulative duration is small; this simply recreates the slow-point obstruction in the seam layer.

So this run did **not** prove the exact special case `(SC)` from the preceding report. Instead it found that deterministic upper windows are unnecessary for the **eventual** problem: summable tail bounds plus Borel--Cantelli are sufficient, and crucially they do not condition or couple the stopped pairs.

## 4. Setup for the successful recovery

Let `w:R->(0,infinity)` be nonconstant, `P`-periodic and Lipschitz. Put

\[
g(u)=\sqrt u\,w(\log u),\qquad u>0,
\]

and let `Lambda(w)` be the principal killed-OU Floquet exponent for the symmetric moving interval

\[
[-w(r),w(r)].
\]

Assume

\[
\boxed{\Lambda(w)<1.}
\tag{4.1}
\]

Write

\[
m=\min w>0,\qquad L=\operatorname{Lip}(w).
\]

The preceding R07 Floquet/Perkins runs proved the sharp periodic finite-cutoff and all-phase slow-point estimates at this threshold. The present construction uses them only as an input and does not adapt any stopping rule to a random seam phase.

Choose deterministic sequences

\[
\eta_n\downarrow0,\qquad
\delta_n\downarrow0,\qquad
\beta_n\downarrow0,
\]

so slowly that

\[
\Lambda(w-4\eta_n)<1,
\qquad 4\eta_n<m,
\tag{4.2}
\]

for every `n`. Choose `K_n\uparrow\infty` so fast that

\[
L\log(1+2/K_n)<\eta_n/8
\tag{4.3}
\]

and, later, the spatial seam error divided by `sqrt(K_n)` is also at most `eta_n/8`.

The construction is recursive in deterministic parameters only. This is the point that preserves Definition-2.2 independence.

## 5. Phase-blind finite-cutoff terminal lemma

### Lemma T90-A

Fix deterministic numbers

\[
A>r>0,\quad q>0,\quad \delta>0,
\]

and a positive periodic Lipschitz profile `v` whose Floquet exponent is `<1`. Then standard Brownian motion `B` admits an a.s.-finite stopping time `T>=A` such that

\[
|B_T|\le\delta\sqrt T,
\tag{5.1}
\]

\[
|B_{T-s}-B_T|\le \sqrt s\,v(\log s)
\qquad(r\le s\le T),
\tag{5.2}
\]

and

\[
\sup_{0\le s\le r}|B_{T-s}-B_T|\le q.
\tag{5.3}
\]

The stopping rule depends only on `(A,r,q,delta,v)` and the current Brownian path.

### Proof

The proof is the periodic analogue of the source's passage from its local slow-point statement to equations (4.10)--(4.13), with a terminal bridge added.

First fix one logarithmic phase. The finite-cutoff second-moment theorem from the preceding R07 run gives a positive lower bound for finding, in a multiplicative time block, a terminal whose reversed increments survive in an inward-eroded periodic interval from scale `r` up to the terminal scale. The killed-OU Floquet kernel is strongly positive. Conditional on long survival, its endpoint distribution at the coarse end has a positive density on every compact subinterval strictly inside the moving interval, uniformly in phase. Therefore imposing the additional normalized endpoint condition `|B_T|<=delta sqrt(T)` costs a strictly positive factor, not an additional power of the scale ratio.

At the fine end, require the state at lag `r` to lie in a sufficiently small compact interval around zero. Strong positivity again gives positive conditional probability. Conditional on that state, an ordinary Brownian bridge on the last deterministic interval of length `r` has strictly positive probability to remain in `[-q,q]`; this is exactly (5.3). Thus, for the fixed deterministic quadruple `(r,q,delta,v)`, one obtains a positive success probability in each sufficiently large multiplicative trial block. The success probability may be extremely small when `q/sqrt(r)` is small, but it is strictly positive and that is all that is needed for a single piece.

To turn positive probability into an a.s.-finite stopping time without conditioning the Brownian path, take disjoint trial blocks whose lengths grow superexponentially and, using the period `P`, choose the trial scales on the lattice `exp(P Z)` so that the moving profile has the same logarithmic phase after scaling. Brownian increments on the trial blocks are independent. The prefix before the successful block is negligible relative to the successful block by the Brownian law of the iterated logarithm, exactly as in the source's triple-exponential argument around (4.11)--(4.13). Because `v` is Lipschitz and the successful block is overwhelmingly longer than the prefix, the small phase error at the oldest lags is absorbed by the inward margin used in the first step. The same prefix estimate turns the block-endpoint restriction into (5.1) relative to the original Brownian origin.

Hence every fixed trial has a positive lower success probability, independent trials continue forever, and the first global terminal satisfying (5.1)--(5.3) is finite almost surely. The defining conditions involve only the path observed up to the candidate terminal, so the first such terminal is a stopping time. QED.

The purpose of the flat bridge (5.3) is important: it avoids asking Brownian motion to satisfy a `c sqrt(s)` bound all the way to `s=0` at an ordinary seam. The global tube at a seam a positive distance from the final origin has radius of order `sqrt(R)`, so a flat `O(sqrt(R))` bridge is the correct local object.

## 6. Move #19 — make the sewing algorithm deterministic before sampling

Let `B^1,B^2,...` be independent standard Brownian motions. These will be the negative-time pieces, indexed from the origin toward `-infinity`.

The deterministic parameters are chosen recursively.

After `U_1,...,U_{n-1}` have been fixed, set

\[
H_n=1+\sum_{j<n}U_j,
\qquad
r_n=K_n H_n.
\tag{6.1}
\]

Choose the deterministic lower search scale `A_n` so large that

\[
A_n\ge n^4r_n,
\tag{6.2}
\]

and also so large that the deterministic endpoint envelope from all pieces strictly earlier than `n-1` is negligible at scale `sqrt(A_{n-1})`; concretely, when choosing `A_n` all the quantities `U_j`, `j<n`, are already known, so we may impose

\[
\frac{1+\sum_{j<n}\delta_j\sqrt{U_j}}{\sqrt{A_n}}\le n^{-2}.
\tag{6.3}
\]

Apply Lemma T90-A to `B^n` with

\[
v_n=w-2\eta_n,
\quad A=A_n,
\quad r=r_n,
\quad q=\beta_n\sqrt{A_{n-1}}
\tag{6.4}

(with an arbitrary positive convention for `A_0`), and endpoint coefficient `delta_n`. Denote the resulting stopping time by `T_n` and the stopped endpoint by

\[
D_n=B^n_{T_n}.
\]

Thus

\[
|D_n|\le\delta_n\sqrt{T_n},
\tag{6.5}
\]

\[
|B^n_{T_n-s}-B^n_{T_n}|\le
\sqrt s\,[w(\log s)-2\eta_n]
\quad(r_n\le s\le T_n),
\tag{6.6}
\]

and

\[
\sup_{0\le s\le r_n}
|B^n_{T_n-s}-B^n_{T_n}|
\le\beta_n\sqrt{A_{n-1}}.
\tag{6.7}
\]

Since `T_n<infinity` a.s., choose a deterministic quantile `U_n` satisfying

\[
\mathbb P(T_n>U_n)\le2^{-n}.
\tag{6.8}
\]

Only after choosing this deterministic `U_n` do we define the deterministic parameters of piece `n+1`.

Every `T_n` is a stopping functional of `B^n` and deterministic data only. Therefore the stopped pairs are independent. No seam time, seam phase, endpoint of another piece, or future sigma-field is ever read by the rule for `T_n`.

## 7. Move #30 — one scale/direction at a time: seam layer versus bulk

Concatenate the stopped pairs as in Definition 2.2. For positive indices one may take deterministic unit Brownian pieces; only the negative tail matters here.

For piece `n`, let

\[
R_n=\sum_{j<n}T_j
\tag{7.1}

be the elapsed time from the right seam of piece `n` to the final origin, and let `Y_n` be the spatial value at that seam. A point `s` units backward into piece `n` occurs at total backward time

\[
u=R_n+s
\]

and has value

\[
Y_n+Z_n(s),
\qquad
Z_n(s)=B^n_{T_n-s}-B^n_{T_n}.
\tag{7.2}

### 7.1 Borel--Cantelli gives eventual deterministic domination without conditioning

From (6.8),

\[
\sum_n\mathbb P(T_n>U_n)<\infty.
\]

Hence, almost surely, only finitely many events `{T_n>U_n}` occur. Let their total excess in time be absorbed into a finite random constant `C_T(omega)`. Then

\[
R_n\le C_T+H_n
\tag{7.3}

for all sufficiently large `n`. Consequently

\[
\frac{R_n}{r_n}
\le
\frac{1+C_T/H_n}{K_n}\longrightarrow0.
\tag{7.4}

No conditioning has occurred; the stopped pairs retain their original independent Brownian construction laws.

### 7.2 Seam heights are asymptotically negligible

Since `Y_n` is the sum of the stopped endpoints of the later pieces,

\[
|Y_n|\le \sum_{j<n}|D_j|.
\]

Split off the immediately later piece `n-1`. By (6.5),

\[
|D_{n-1}|\le\delta_{n-1}\sqrt{T_{n-1}}
\le\delta_{n-1}\sqrt{R_n}.
\tag{7.5}

All earlier good endpoints are bounded using their deterministic `U_j`; finitely many exceptional ones contribute another finite random constant. Condition (6.3), applied one index earlier, and `R_n>=T_{n-1}>=A_{n-1}` therefore give

\[
\frac{|Y_n|}{\sqrt{R_n}}
\le
\delta_{n-1}+o(1)\longrightarrow0.
\tag{7.6}

This is the spatial analogue of (7.4).

### 7.3 Near-seam layer

For `0<=s<=r_n`, (6.7) and `R_n>=A_{n-1}` yield

\[
|Y_n+Z_n(s)|
\le
|Y_n|+\beta_n\sqrt{A_{n-1}}
\le
(\delta_{n-1}+\beta_n+o(1))\sqrt{R_n}.
\tag{7.7}

Since `w>=m>0` and `u=R_n+s>=R_n`, the right side is eventually strictly smaller than

\[
m\sqrt{R_n}\le \sqrt u\,w(\log u).
\tag{7.8}

Thus the entire seam layer is eventually inside the target tube. This is the missing role of the flat bridge: ordinary Brownian roughness at `s=0` is harmless because the global radius there is of order `sqrt(R_n)`, not `sqrt(s)`.

### 7.4 Bulk layer

Now let `s>=r_n`. By (7.4), `R_n/s=o(1)` uniformly over the bulk. Lipschitz continuity gives

\[
\begin{aligned}
\sqrt{R_n+s}\,w(\log(R_n+s))
&\ge \sqrt s\,w(\log s)
 -L\sqrt s\,\log(1+R_n/s)\\
&\ge \sqrt s\,[w(\log s)-\eta_n/4]
\end{aligned}
\tag{7.9}

for all sufficiently large `n`, using (4.3) and (7.4). Also, from (7.6) and `s>=K_nH_n` while `R_n<=H_n+O(1)`, we have

\[
\frac{|Y_n|}{\sqrt s}=o(\eta_n)
\tag{7.10}

provided `K_n` was chosen sufficiently fast, which is allowed because all choices are deterministic before `B^n` is sampled.

Combining (6.6), (7.9), and (7.10),

\[
|Y_n+Z_n(s)|
\le
\sqrt s\,[w(\log s)-2\eta_n]+|Y_n|
<
\sqrt{R_n+s}\,w(\log(R_n+s))
\tag{7.11}

uniformly for `r_n<=s<=T_n`, for all sufficiently large `n`.

The near-seam and bulk estimates together cover every point of piece `n`.

## 8. Theorem T90 — subcritical periodic tubes admit a phase-blind decomposable eventual confinement

Let `w:R->(0,infinity)` be nonconstant, positive, periodic and Lipschitz, and let `Lambda(w)` be the principal Floquet killing exponent of stationary OU motion in `[-w(r),w(r)]`. If

\[
\boxed{\Lambda(w)<1,}
\]

then there exists a **decomposable forward Brownian motion** `X` such that

\[
\boxed{
\mathbb P\left(
\exists U_0<\infty:\
|X_{-u}|\le\sqrt u\,w(\log u)
\quad\forall u\ge U_0
\right)=1.
}
\tag{T90}

The stopped Brownian pairs in the construction are independent in the exact sense of Definition 2.2. In particular, the proof never chooses a stopping time using the actual random seam phase `log R_n mod P`.

### Proof

Lemma T90-A supplies each stopping time from its own Brownian driver and deterministic parameters. Hence the pairs are independent and their negative-time durations diverge because `T_n>=A_n->infinity`; adding arbitrary independent unit pieces on the positive side gives a decomposable FBM by Definition 2.2. Equations (7.7)--(7.11) show that, almost surely, every sufficiently far negative piece lies pointwise inside the deterministic log-periodic tube. Since only finitely many pieces precede that random index, this is equivalent to (T90). QED.

T90 is stronger than merely obtaining the correct limsup/liminf inequalities in the strict subcritical regime: it gives pointwise confinement for **all sufficiently large backward times**.

## 9. What changed about the blocker

The preceding stuck report said that the near-seam bridge was the missing ingredient. T90 identifies the correct bridge and proves that it can be made phase-blind:

- use a **flat** bridge over a deterministic seam layer, not a `sqrt(s)` cone down to `s=0`;
- let deterministic quantile bounds fail with summable probabilities rather than condition on success;
- Borel--Cantelli makes scale domination eventual;
- endpoint coefficients tending to zero make seam heights negligible;
- an eroded periodic bulk absorbs the logarithmic phase error `log(R+s)-log s`.

Thus random seam phases are **not** an obstruction to the eventual/asymptotic Theorem-4.3 analogue.

The exact all-time special case `(SC)` is still open in this track. The remaining difference is finite-prefix, not asymptotic. T90 uses Borel--Cantelli, so a finite random number of quantile-window failures is allowed. Exact clause (iii) would require eliminating those failures without conditioning the Brownian pieces or allowing one stopping rule to read another piece. The direct bounded-window repair fails for the reason in Section 3.

This is now a much sharper obstruction than the one in the previous report:

\[
\boxed{
\text{eventual phase-blind sewing works; exact all-time sewing needs a Brownian-preserving finite-prefix repair.}
}
\tag{9.1}

A future proof of `(SC)` must contain such a repair. Another Floquet estimate, another all-phase slow-point theorem, or another summable-error argument will not by itself close clause (iii).

## 10. Method accounting

### #6 DEFORM TO A POINT YOU CAN SOLVE — succeeded

Instead of trying to sew the exact boundary immediately, each bulk piece uses a small inward erosion `w-2 eta_n`. The erosion tends to zero and its Floquet exponent stays below one. It supplies exactly the deterministic margin needed to absorb the small additive-time phase deformation.

### #19 MAKE IT AN ALGORITHM — succeeded

The proof is an explicit recursive construction: choose deterministic parameters, build one stopping functional from the current Brownian driver only, take a deterministic quantile of its law, then use that quantile only in the **next piece's deterministic design**. The actual value of the previous stopping time is never read. This is what makes independence auditable.

### #30 DO ONE SCALE / ONE DIRECTION AT A TIME — succeeded

The obstruction splits cleanly at `r_n=K_n H_n`: a flat bridge handles the near seam, while the eroded periodic slow path handles the bulk. Trying to use one inequality on both regions was the source of the earlier false obstruction.

### Mandatory refutation-first outcome

The attempted exact deterministic-window version failed: a slow-terminal stopping time has unbounded support, and conditioning/rejection would destroy the ordinary-Brownian law required by Definition 2.2. That failure forced the summable-quantile/Borel--Cantelli design and explains exactly why T90 is eventual rather than all-time.

## 11. Metric / closure / audit state

The frozen metric remains

\[
\boxed{59\to59.}
\]

The periodic square-root-tube family was already counted; T90 is a stronger theorem in that family, not family 60. The unchanged count is

\[
\boxed{4\to5.}
\]

T90 is a theorem-sized self-authored claim with a complete argument on this report page, but it has **0/2 independent OTHER-track audits**. There is no finite arithmetic/combinatorial core, so no checker was manufactured. Source status remains **PARTIAL**, not PROVED/REFUTED/KNOWN. Publication novelty remains **UNVERIFIED**.

Because this is the second recovery on the current stuck episode and the fifth unchanged run, the next R07 invocation has only two legitimate outcomes under the closable-target policy: (i) genuine fixed-metric movement / exact source-level closure, or (ii) if the metric remains unchanged for the sixth run, write the immutable handoff and rotate to the next eligible CLOSABLE OUTSIDE queue item. It must not manufacture family 60 by reparameterizing this periodic family.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  source: Burdzy-Scheutzow_2014_Problem_7.8
  intake: I0077
  lane: CLOSABLE_OUTSIDE
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: distinct_nonparabolic_shape_families_complete_source_appropriate_theorem_frozen_equivalence
  metric_before: 59
  metric_after: 59
  movement: none
  unchanged_count_before: 4
  unchanged_count_after: 5
  stuck_recovery_number: 2
  methods: [6, 19, 30]
  new_theorem_claims:
    - "T90: Lambda(w)<1 for a positive periodic Lipschitz symmetric sqrt tube implies existence of a decomposable FBM eventually pointwise confined to the tube, using phase-blind independent stopped pieces"
    - "T90-A: finite-cutoff terminal lemma with endpoint control, eroded periodic bulk, and deterministic flat terminal bridge"
  audits_other_tracks: "0/2"
  finite_core: "none; analytic proof, no checker manufactured"
  remaining_obligation: "exact all-negative-times confinement in the genuinely periodic regime, requiring a Brownian-preserving finite-prefix repair"
  next_run_protocol: "metric movement/closure or six-unchanged immutable handoff and rotation"
  source_status: PENDING_ADMISSION_not_READY
  publication_novelty: UNVERIFIED
```

## 13. Model / scheduler-control reality

The actual runtime model for this report is GPT-5.6 Sol. No authenticated reasoning-effort receipt is exposed, so the reasoning level is `UNVERIFIED`; I do not claim GPT-6 maximum.

The exposed scheduler schema still provides prompt/title, schedule or start offset, enablement, and timing mode, but no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run model receipt. The repository policy records the historical `You cannot modify this task` outcomes as authorization-context issues; a denied task must be handled through the owning/authorized workspace/account or platform support, not through a duplicate schedule or permission bypass. No scheduler, permission, email, Drive, public-posting, purchase, or workflow change was attempted in this run.
