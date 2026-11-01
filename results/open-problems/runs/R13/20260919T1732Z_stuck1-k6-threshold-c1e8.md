Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper metric** `B_R13(86)=728139/100000=7.28139`; fixed-upper unchanged count `2 -> 3`, so the owner-prescribed **STUCK1** protocol triggers. The explicit finite obstruction also has **no movement** this run and remains `K_86^* >= 452931/200000 = 2.264655`. Methods actually used: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #11 DUALIZE, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# R13 — Boolean Komlós STUCK1: isolate the six-column threshold

Run ID: `20260919T1732Z_stuck1-k6-threshold-c1e8`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, mandatory reads, source status, and ownership

I continued from the newest immutable R13 report

`runs/R13/20260919T1550Z_nonuniform-refinement-86-a6f2.md`

rather than restarting. Before new mathematics I reconciled `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the canonical intake row `I0091` in `probability_1000_intake_I_20260914/problems.jsonl`, the newest R13 report, the current R02 Komlós/Boolean-small-ball neighboring report, and the current R16 neighboring discrepancy state. `QUEUE.md` still identifies Boolean Komlós as an existing R13 hard assignment rather than an unassigned READY reserve target. I changed no shared root, peer-track file, ownership claim, email, Drive item, public post, permission, workflow, purchase, or scheduler state.

The intake row `I0091` is historically stale as an openness record: it says `open_per_source`, but it was recorded on 14 September without a later-resolution search. Fresh source checks on 19 September preserve the now-current separation:

- Shengtao Guo, Ethan X. Fang, and Junwei Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189, submitted 10 September 2026, prove the genuine real-Boolean Komlós theorem with bound `3 sqrt(2 pi)`.
- Emrullah Akbas and Suvrit Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 17 September 2026, recover Komlós through a Boolean small-ball theorem, but their main quantitative constants `nu_0,q_1,C_1` are universal rather than numerically instantiated at a scale competitive with R13's finite-`n` certificate.
- Sankeerth Rao Karingula and Shachar Lovett, ECCC TR26-188, posted 17 September 2026, give an elementary real-sign proof with constant `36`.
- Bansal--Jiang, arXiv:2508.03961v2, remains the earlier real-Boolean polylogarithmic source route.

Thus the **qualitative source status is KNOWN in current 2026 preprint / technical-report literature**. R13 remains only a quantitative finite-dimensional track. Complex phases, rank-two/vector colorings, and average-case bounds are not substituted for the real Boolean statement.

## 2. Fixed metric before / after — third unchanged upper run

The owner-tracked metric remains the complete rigorously certified pointwise upper envelope `B_R13(n)` for

\[
K_n^*:=\sup_{m\ge1}\sup_{A:\,\|A_{\cdot j}\|_2\le1}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty.
\]

Put

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The oldest retained DTV branch remains

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]
\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\]

The one-threshold branch remains

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]
\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]
\[
H(n)=\max\left\{\frac{148709}{20000},3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\]

For the retained three-threshold occupancy polynomial, with the exact predecessor coefficients `c_{ell,D}^{(3)}` and their unchanged threshold/failure conventions,

\[
\beta_D^{\uparrow,3}=\frac12\sum_{\ell=1}^D c_{\ell,D}^{(3)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]
\[
D_9(n)=\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]
\[
J(n)=\max\left\{\frac{740179}{100000},\frac{27\sqrt{10\pi}}{20}(1-\beta_{D_9(n)}^{\uparrow,3})\right\}.
\]

For every integer `D>=135`, the inherited conditional-tail branches remain

\[
C_D^-=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\qquad
L_-(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\]

and for `r=2,3,4`,

\[
C_D^{(r)}=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\qquad
L_r(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\]

Their exact conditional moments, truncation thresholds, and failed-threshold zero conventions are unchanged from the immutable predecessor chain.

The five-threshold branch remains

\[
A_{k,D}=\frac{5}{7(4437/5000)}\left(1-\frac{2k}{5D}\right)\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},
\qquad k=1,\ldots,5,
\]
with
\[
a_k=A_{k,D}/D,\quad a_0=0,\quad d_k=a_k-a_{k-1},
\]
\[
F_{1,0}=1,\qquad F_{k,r}=\sum_{s=0}^rF_{k-1,r-s}\frac{d_k^s}{s!},
\]
\[
C_{D,5}(x)=\sum_{r=0}^4\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r}.
\]
Writing
\[
1-C_{D,5}(x)=\sum_{\ell=1}^Dc_{\ell,D}^{(5)}x^\ell,
\]
\[
\beta_{D,5}^{\uparrow}=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(5)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]
and retaining exactly the predecessor's truncated `U=157/20`, four-shell Cantelli functional `beta_{D,5}^{downarrow}`,
\[
L_5(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{
\frac{27\sqrt{10\pi}}{20}(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\frac n{\sqrt{D+1}}\right\}.
\]

The transform branches remain

\[
L_{\rm LT}(n)=\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\},
\]
\[
L_{33/20}^{\rm shell}(n)=\max\left\{\frac{728139}{100000},\frac n{\sqrt{140}}\right\}.
\]

Therefore the complete fixed metric remains

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&5\le n\le85,\\
\min\{G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&n\ge86.
\end{cases}}
\]

In particular,

\[
\boxed{B_{R13}(86)=\frac{728139}{100000}=7.28139}
\]

before and after this run. The fixed-upper unchanged count is therefore `2 -> 3`. By owner policy this is a **stuck episode**, even though the preceding two runs moved lower obstructions.

The retained finite lower obstruction is also unchanged in this thinking run:

\[
\boxed{K_{86}^*\ge\frac{452931}{200000}=2.264655.}
\]

No checker was created because this run makes no new finite theorem claim.

## 3. Method #5 — ADD A PARAMETER: permutation-symmetrized heterogeneous cosine powers

The most plausible genuinely non-scalar continuation of the DTV route was to allow coordinate exponents `p_i>1`, then average the resulting product density over all coordinate permutations. This gives a nonproduct, permutation-invariant cube density rather than another homogeneous `p` retuning.

For one product component, if

\[
S_i\sim\chi^2_{p_i+1}
\]

independently, the same tangent/Gaussian calculation used in the retained homogeneous proof gives

\[
V_u\le\frac{\sqrt{\pi/2}}{C}
\mathbb E\sqrt{\sum_{i=1}^D u_i^2\frac{p_i^2}{S_i}}.
\]

After averaging over coordinate permutations, the right side is a symmetric concave function of the weights `u_i^2`. Hence its worst unit direction is the balanced direction, reducing this entire heterogeneous family to

\[
\boxed{
\kappa C\le\sqrt{\frac\pi2}\,
\mathbb E\sqrt{\frac1D\sum_{i=1}^D\frac{p_i^2}{S_i}}.}
\]

This is the useful reduction; it is not itself a metric improvement.

I then used high-precision numerical quadrature only as a **discovery screen**, not as proof evidence. Around `D=139`, the homogeneous family has its numerical minimum near `p≈1.65--1.655`; the retained exact branch at `p=33/20=1.65` is already within only a few `10^{-5}` of that numerical floor. Tested two-exponent mixtures around this neighborhood did not beat the homogeneous candidate. For example, splitting exponents between `1.64` and `1.66` gave numerical DTV constants above `7.28142` in the tested allocations, while the homogeneous `p=1.65` numerical value is about `7.281374`. These values are scouting only and are **not** certified inequalities.

**Failure reason:** heterogeneity did not reveal a structural drop. The remaining visible headroom in this family is only the small certification gap of the already-known homogeneous transform. Pursuing it would be another scalar/shell decimal squeeze, exactly the behavior the owner asked R13 not to substitute for a new method.

## 4. Method #11 — DUALIZE: why a one-row weighted cover cannot prove the needed six-column theorem

The higher-value finite route is an upper theorem for six columns. The existing block compiler would turn any

\[
K_6^*\le\frac{47}{25}=1.88
\]

into

\[
K_{86}^*\le\frac{47}{25}\sqrt{15}=7.281208690\ldots<7.28139,
\]

so `47/25` is a clean source-matching special-case target.

The exact threshold for merely tying the current `n=86` number is

\[
h_6^\dagger=\frac{728139}{100000\sqrt{15}}
=1.8800468138160815\ldots,
\]
with
\[
(h_6^\dagger)^2=\frac{176728801107}{50000000000}=3.53457602214.
\]

I dualized the simplest proposed cover proof. Suppose one tries to assign fixed nonnegative projective-sign weights `w_s` and fixed nonnegative coordinate prices `lambda_j` so that every row `r` obeys

\[
\sum_{[s]:\,|r\cdot s|>t}w_s
\le\sum_{j=1}^6\lambda_j r_j^2,
\tag{4.1}
\]

and then contradicts a complete cover by requiring `sum_s w_s > sum_j lambda_j`.

Averaging such a certificate over signed coordinate permutations preserves validity and the objective gap, so any successful certificate of this separable form has a symmetric version: all projective classes have one common weight `w` and all coordinates one common price `lambda`.

Now take the inherited equal-triple test row

\[
r=c(1,1,1,0,0,0),\qquad t/3<c<t.
\]

Exactly eight projective sign classes are bad. Sending `c downarrow t/3` in (4.1) forces

\[
8w\le\frac{t^2}{3}\lambda.
\]

Therefore

\[
32w\le\frac{4t^2}{3}\lambda.
\]

To contradict a cover one would need `32w>6lambda`, which is impossible whenever

\[
t\le\frac3{\sqrt2}.
\]

Thus the nonuniform-looking one-row LP collapses under symmetry to the already inherited `3/sqrt(2)` barrier. This is the dual-language form of the earlier R13-X03 obstruction, not a new upper theorem.

**Failure reason:** any proof that sums independent per-row charges loses exactly the information needed below `3/sqrt(2)`. A `1.88` theorem has to couple **intersections of bad families from different rows** with the six separate column-energy budgets. The missing object is a genuinely multirow certificate, not a better choice of static sign weights.

## 5. Method #22 — READ THE FAILURES: what the two September breakthroughs do not supply

The current primary papers clarify two different barriers.

### 5.1 Guo--Fang--Lu

Their Lemma 2.4 uses the cosine-squared product density and their Remark 2.5 proves that the coefficient `sqrt(2 pi)` is optimal uniformly in dimension **within that fixed product-density family**. They explicitly note that this does not prove optimality among all cube-supported densities. R13's finite-`D` `p<2` variants exploit a finite-dimensional Jensen defect and improve the `D=139` number, but the current homogeneous route is now numerically very close to its own finite optimum.

**What their proof has that R13 uses:** a stable DTV signing transform that converts a cube density into a real Boolean signing theorem.

**What it does not have for the present blocker:** a nonproduct cube density with a rigorously smaller worst-direction variation at `D=139`, or any six-column intersection theorem.

### 5.2 Akbas--Sra

Their Theorem 1.1 states the Boolean matrix small-ball theorem with universal constants `nu_0,q_1,C_1`; their Komlós corollary is obtained using the Guo--Fang--Lu signing theorem. The paper gives abundance/entropy information about good signings, but the displayed general constants are not numerically instantiated at a level that can be inserted to prove `K_86^*<7.28139` or `K_6^*<=1.88` without a new constant-tracking proof.

**Failure reason:** the new small-ball theorem changes the structure of the solution set, but its present universal constants do not furnish the required finite numerical inequality.

### 5.3 Karingula--Lovett

Their elementary proof gives constant `36`. It is valuable as a simplification of the qualitative theorem but is quantitatively far outside the present finite threshold.

**Outcome #22:** the closest current literature supplies either the DTV transform whose product-density numerical bottleneck R13 is already refining, or universal-constant small-ball/elementary arguments that do not reach the finite `7.28139` / `1.88` scale.

## 6. STUCK1 report required by policy

### (a) Exact blocking statement

I choose the six-column route as the recovery target. The exact clean statement whose proof would move the current `n=86` envelope is

\[
\boxed{K_6^*\le\frac{47}{25}.}
\tag{S1}
\]

The existing six-block compiler would then give

\[
K_{86}^*\le\frac{47}{25}\sqrt{15}<\frac{728139}{100000}.
\]

### (b) Routes already tried and their precise failure modes

1. **Pure one-row bad-cardinality / energy charging:** saturated at `3/sqrt(2)` by the equal-triple row; R13-X03 already proves this route cannot reach `1.88`.
2. **Static weighted fractional-cover dual:** after hyperoctahedral symmetrization it reduces to the same one-row barrier, as Section 4 shows.
3. **Intersection-aware six-cube cover:** identified repeatedly as the necessary finite route, but no exact multirow dual or exhaustive continuous reduction has yet been found. The obstruction is continuous row magnitude/orientation data coupled through six coordinate-energy budgets.
4. **Exact five-column compiler:** `K_5^*=T_5=1.792447...` is exact, but `T_5 sqrt(ceil(86/5))=T_5 sqrt(18)=7.6047...`, too large.
5. **Homogeneous cosine-power DTV:** successful down to the current `7.28139`, but numerical scouting shows only a few `10^{-5}` of room inside the present `D=139` scalar family; another shell/`c_*` tightening is not a new route.
6. **Permutation-symmetrized heterogeneous exponents:** reduces rigorously to a balanced mixed inverse-chi-square expectation, but tested mixtures near the finite optimum did not improve the homogeneous candidate.
7. **Boolean small-ball constants:** Akbas--Sra gives universal `q_1,C_1` rather than a presently extractable explicit constant below `7.28139`.
8. **Random-sign / Frobenius-energy union bounds:** complete but much too weak; they do not exploit the six-cube intersection geometry.
9. **Lower-obstruction refinement forests:** these have materially improved the secondary lower endpoint at `n=86`, but they do not constrain the universal upper envelope.

### (c) What a proof must contain that no current route contains

For the chosen recovery (S1), a successful proof needs an **intersection-aware multirow inequality**. Concretely, it must use that several threshold halfspaces on the 32 projective six-cube classes cannot cover all classes while their coefficient vectors simultaneously obey

\[
\sum_i r_{ij}^2\le1\qquad(j=1,\ldots,6),
\]

at threshold `47/25`. Any certificate that decomposes as an independent sum of one-row costs is ruled out by the equal-triple symmetry barrier. The missing information is the incompatibility between efficient bad-family shapes across different rows.

The alternative DTV route would instead need a genuinely nonproduct cube-supported density with a rigorously smaller worst-direction total variation; no current route supplies one.

### (d) Simplest special case still unproved

The simplest source-valid special case that directly moves the fixed metric is exactly (S1):

\[
\boxed{\text{every real matrix with six columns of Euclidean norm at most one has Boolean discrepancy at most }47/25.}
\]

The retained exact lower obstruction is

\[
K_6^*\ge T_6>1.84535465096,
\]

so the requested `1.88` upper theorem has only about `0.03465` absolute slack above the best R13 six-column obstruction.

### (e) Nearest solved problem in the literature and the ingredient it has that this lacks

The nearest current solved source problem is the unrestricted qualitative Komlós theorem of Guo--Fang--Lu. Their proof has a **global directional-total-variation stability theorem** that turns a cube density into a signing for arbitrary dimension. That machinery is strong enough for a universal constant, but its supplied product density does not encode the discrete overlap geometry of the 32 projective six-cube classes. Conversely, R13's exact `n=5` finite proof has the needed discrete exhaustive geometry but is internal campaign work, not the literature comparison requested here, and its finite core does not scale directly to 32 six-cube classes.

## 7. Recovery choice and next three moves

Per the stuck protocol I choose exactly one recovery action:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM (d): target `K_6^* <= 47/25`.**

The next run should be a fresh finite-geometry attack, not another DTV decimal refinement. The three planned Section-B moves are:

- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE:** enumerate the realizable threshold-downset / oriented bad-family types at `t=47/25`, modulo the signed-coordinate group, retaining the six-coordinate squared-load profile rather than only family size.
- **#20 FIND WHY THE ALGORITHM FAILS:** isolate which multirow cover types survive the coordinate-load relaxation and identify the exact configuration preventing a simple LP closure.
- **#30 DO ONE SCALE, ONE DIRECTION AT A TIME:** split row types by their minimal coordinate-energy profile and solve the cover/gluing obstruction class-by-class; only then attempt an exact global dual certificate.

If this recovery reaches the same blocker again, it will count as the second stuck recovery on this hard target. A third stuck episode must hand off/rotate under owner policy.

## 8. Model / scheduler-control truth

The available task-control surface still exposes prompt/title, schedule/timing, enabled state, and list/update operations, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. GPT-6 / maximum therefore remains prompt-only on this surface; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

Changing this would require an owner-authorized product/workspace/API scheduler surface whose schema includes persisted model-family and reasoning-effort fields and returns authenticated runtime telemetry. The historical P26 `You cannot modify this task` response is an authorization/context boundary; repository continuity records later P26 updates from another authorized context. The legitimate workaround is the task-owning/otherwise-authorized product or workspace surface, or platform support for that same task — not duplication, permission bypass, or a repository edit presented as a scheduler repair. No scheduler change was attempted in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  fixed_metric_name: complete rigorously certified upper envelope B_R13(n)
  fixed_metric_before: B_R13(86)=728139/100000
  fixed_metric_after: B_R13(86)=728139/100000
  fixed_metric_moved: false
  fixed_metric_unchanged_count_before: 2
  fixed_metric_unchanged_count_after: 3
  stuck_episode: STUCK1
  lower_obstruction_n86_before: 452931/200000
  lower_obstruction_n86_after: 452931/200000
  lower_obstruction_moved: false
  methods_this_run: [5, 11, 22]
  new_theorem_claims: 0
  exact_checkers_new: 0
  recovery_choice: PROVE_SIMPLEST_UNPROVED_SPECIAL_CASE
  recovery_target: K_6^* <= 47/25
  next_methods: [16, 20, 30]
  outside_audits_new_claim: 0/2
  novelty: NOT_APPLICABLE_NO_NEW_CLAIM
```
