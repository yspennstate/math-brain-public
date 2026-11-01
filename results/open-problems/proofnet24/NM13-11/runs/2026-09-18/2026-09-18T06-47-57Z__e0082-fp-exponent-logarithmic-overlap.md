Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT after admission: `gamma_FP in [1,5/4] -> gamma_FP = 1`; status `PARTIAL`. Section-B methods actually tried: #2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY, #8 DISCRETIZE.

# NM13-11 — E0082 first-passage-pattern exponent via reversed matching matrices

## 1. Continuity, controlling policy, and admission

I re-read the controlling fleet/new-methods directives, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, the newest NM13-11 report, neighboring NM13-10/NM13-12 reports, intake/source/attempt material, and canonical claims before selecting a successor. The previous NM13-11 state was `ADMISSION_PENDING` after the H0003 handoff; D and I residue-10 exclusions were preserved rather than reopened.

This run completed the remaining canonical residue-10 screen of intake F through EOF and intake E through EOF. The F residue-10 hits after the previous cursor were `F0045`, `F0061`, `F0062`, `F0070`, `F0072`, `F0106`, `F0113`, `F0130`: the first, Janson pair, F0113 and F0130 are settled/resolved in current repository history; F0106 has the live canonical R7-04 claim; F0070 and F0072 are source-wide asymptotic problems without a realistic finite/source-relevant milestone for this worker. The E residue-10 hits were `E0036`, `E0054`, `E0082`, `E0107`: E0036 is the global Newman–Piza/FPP exponent problem, E0054 is the global SBM detection threshold, and E0107 asks for a general stationary-measure theory for sparse-graph interacting-particle local equations. None of those three has the concrete movable milestone required here. `E0082` does.

Selected source: Jim Pitman and Wenpin Tang, *Patterns in random walks and Brownian motion*, Open problem 2.3 / the exponent-gap discussion in Section 2.5. Canonical key `pitman_tang::op_2_3` has SHA256 `1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a`, whose integer value is `10 mod 13`, so it belongs to NM13-11's exclusive shard. Repository searches for `E0082`, the canonical key, and the exact title found the intake/campaign record and the old substantive attempt `E0082-A001`, but no ownership record, handoff, or canonical claim. `operations/claims/E0082.md` was absent before creation. The older attempt identified the matching-matrix/correlation obstruction but proved neither an improved exponent nor an exact asymptotic; I preserve that continuity and do not count it as a new method.

A bounded 2026-09-18 literature check used the exact source title together with `first passage`, `waiting time`, `exact asymptotics`, `Pitman Tang`, and `n log n`, plus the authors' later-publication trail. It recovered the original Pitman–Tang source, Tang's 2017 thesis version of the same argument, and later related Pitman–Tang random-walk papers, but no later paper claiming the exact Open-problem-2.3 asymptotics or the bound proved below. This is bounded negative evidence, not proof of worldwide openness. Direct source text is authoritative over one intake-summary sentence: for first-passage patterns the source proves `c_lambda n <= E T <= C_lambda n^(5/4)`, not an `O(n)` upper bound.

The canonical claim `operations/claims/E0082.md` was then created with create-only semantics and read back at its creation commit `84922e0f873072e7b346b21142dba7de681410d5` (blob `482f32998ffe4234cf436390bdb2bdf58faee795`). Only after that readback did substantive work begin.

## 2. Frozen source model and metric

Fix `lambda=-1`. Let `m=m_n:=|lambda_n|`, where `lambda_n<0` is the parity-correct integer used by Pitman–Tang, so `m=sqrt(n)+O(1)` and `m` has the same parity as `n`. Let

\[
\mathcal F_n:=\mathcal{FP}^{-1,n}
\]

be the family of sign strings `a=(a_1,...,a_n) in {+1,-1}^n` whose partial sums `S_t(a)` satisfy

\[
S_t(a)>-m\quad(0\le t<n),\qquad S_n(a)=-m.
\]

Let `T(F_n)` be the first waiting time until one member of this family appears as a consecutive length-`n` increment block in an infinite fair sign sequence.

The frozen metric is

\[
\gamma_{FP}:=\inf\{\gamma:\ \mathbb E T(\mathcal F_n)=O(n^\gamma)\}.
\]

Pitman–Tang give a linear lower bound and an `n^(5/4)` upper bound, hence the certified baseline before this run is

\[
1\le \gamma_{FP}\le 5/4.
\]

No normalization or metric was changed after admission.

## 3. New idea before bookkeeping

The source bounds **column sums** of the matching matrix and obtains the `n^(1/4)` loss. The new route is to look at **row sums instead**, where the first-passage constraint has a hidden ladder-time structure, and then transpose the matching matrix by reversing every pattern. Reversal is crucial: it turns positivity for the matching system of the reversed family into positivity for `M^{-T} 1`, which is exactly what is needed to convert a row-sum bound into an upper bound for the original waiting time.

This route is different from `E0082-A001`: it does not assume or seek asymptotic uniformity of the first-hit weights and does not try to invert the full exponentially large matrix.

## 4. Complete theorem

### Theorem

For every fixed `lambda<0`, with `F_n=FP^{lambda,n}` in the exact Pitman–Tang model,

\[
\mathbb E T(\mathcal F_n)=O_\lambda(n\log n).
\]

Consequently, for the frozen `lambda=-1` metric,

\[
\boxed{\gamma_{FP}=1}.
\]

This is `PARTIAL` for source problem E0082: it closes the power-law exponent gap but does **not** prove `Theta(n)`, an asymptotic equivalent, or the bridge half of Open problem 2.3.

### Proof

Write the terminal level as `-m`, with `m=|lambda_n|`. Enumerate `F_n={A_1,...,A_k}`. For two length-`n` patterns define the Pitman–Tang matching matrix

\[
M_{ij}=\sum_{\ell=0}^{n-1}2^{-\ell}\,\epsilon_\ell(A_i,A_j),
\]

where `epsilon_l(A_i,A_j)=1` exactly when the prefix of `A_i` of length `n-l` equals the suffix of `A_j` of that length. Their renewal/matching theorem gives

\[
\frac1{\mathbb E T(\mathcal F_n)}
=2^{-n}\mathbf 1^T M^{-1}\mathbf 1. \tag{1}
\]

We first bound every row sum of `M`.

Fix `A=A_i` and write its partial sums as `s_t`. For a shift `ell>=1`, put `t=n-ell` and `q=s_t`. Suppose a pattern `B in F_n` contributes to this shift, i.e. its suffix of length `t` equals the prefix `A_1...A_t`. Since `B` ends at `-m`, its first `ell` increments must sum to

\[
-m-q=-d,
\]

where the first-passage condition at time `ell<n` forces `1<=d<=m-1`. During the copied suffix, the partial sum of `B` after another `u<t` steps is `-d+s_u`; this must be strictly larger than `-m`. Hence

\[
s_u> d-m=q\qquad(0\le u<t),\qquad s_t=q.
\]

Thus `t` is the first time `A` hits the level `q=-(m-d)`. If `tau_r(A)` denotes the first hitting time of `-r` by `A`, the only possible shift for this `d` is therefore

\[
\ell_d=n-\tau_{m-d}(A).
\]

Conversely, once this first-hitting condition holds, every length-`ell_d` prefix `b` that ends at `-d` and stays strictly above `-m` can be followed by `A_1...A_{n-ell_d}` to form a valid member of `F_n`. Therefore the row sum has the exact representation

\[
\sum_j M_{ij}
=1+\sum_{d=1}^{m-1}
\mathbb P\!\left(S_{\ell_d}=-d,\ \min_{1\le r\le \ell_d}S_r>-m\right), \tag{2}
\]

where on the right `S` is an independent simple symmetric random walk. In particular,

\[
\sum_j M_{ij}
\le 1+\sum_{d=1}^{m-1}\sup_{\ell\ge d,\ \ell\equiv d\ (2)}
\mathbb P(S_\ell=-d). \tag{3}
\]

We now use an elementary local-binomial bound. There is an absolute constant `C_0` such that for every `d>=1`,

\[
\sup_{\ell\ge d,\ \ell\equiv d\ (2)}\mathbb P(S_\ell=-d)\le \frac{C_0}{d}. \tag{4}
\]

For completeness, here is a direct proof. If `ell=2N` and `d=2a`, compare the mass at `-d` with the central mass:

\[
\frac{\mathbb P(S_{2N}=-2a)}{\mathbb P(S_{2N}=0)}
=\prod_{j=0}^{a-1}\frac{N-j}{N+j+1}.
\]

Using `log(1-x)<=-x` and `N+j+1<=2N=ell`, the logarithm of this product is at most `-a^2/ell=-d^2/(4ell)`. Also the central-binomial estimate gives `P(S_ell=0)<=sqrt(2/ell)`. Hence

\[
\mathbb P(S_\ell=-d)\le \sqrt{2/\ell}\,e^{-d^2/(4\ell)}\le C/d,
\]

because the maximum over positive real `ell` of `ell^{-1/2}e^{-d^2/(4ell)}` is a constant times `1/d`. If `ell=2N+1` and `d=2a+1`, comparison with the modal mass at `-1` gives

\[
\frac{\mathbb P(S_{2N+1}=-(2a+1))}{\mathbb P(S_{2N+1}=-1)}
=\prod_{j=0}^{a-1}\frac{N-j}{N+j+2}
\le \exp\!\left(-\frac{a(a+1)}{\ell}\right),
\]

and the same modal-binomial bound yields `C/d`; `d=1` is immediate. This proves (4).

Combining (3) and (4), every row sum is at most

\[
R_n:=1+C_0\sum_{d=1}^{m-1}\frac1d
=O(1+\log m)=O_\lambda(\log n). \tag{5}
\]

It remains to explain why a row-sum bound is useful despite the non-symmetry of `M`. Reverse every sign string and let `F_n^R` be the reversed family. Directly from the overlap definition,

\[
M(\mathcal F_n^R)=M(\mathcal F_n)^T=M^T. \tag{6}
\]

Apply the same Pitman–Tang renewal theorem to the legitimate finite pattern family `F_n^R`. It says that

\[
y:=M^{-T}\mathbf 1
\]

has strictly positive coordinates (up to the positive factor `2^n`, these are reciprocal expected waiting quantities for the reversed patterns). Let

\[
S:=\mathbf 1^T M^{-1}\mathbf 1=\mathbf 1^T M^{-T}\mathbf 1=y^T\mathbf 1.
\]

Since `M 1 <= R_n 1` coordinatewise and `y>=0`,

\[
k=y^TM\mathbf 1\le R_n y^T\mathbf 1=R_n S.
\]

Thus

\[
S\ge \frac{k}{R_n}. \tag{7}
\]

Substitute (7) into (1):

\[
\mathbb E T(\mathcal F_n)\le \frac{2^nR_n}{k}. \tag{8}
\]

Finally the ballot/cycle lemma gives the exact family size

\[
k=\frac{m}{n}\binom{n}{(n-m)/2}. \tag{9}
\]

For fixed `lambda<0`, `m=|lambda|\sqrt n+O(1)`. Stirling's formula (equivalently the lattice local CLT) gives

\[
2^{-n}\binom{n}{(n-m)/2}=\Theta_\lambda(n^{-1/2}),
\]

so (9) implies `2^n/k=Theta_lambda(n)`. Together with (5) and (8),

\[
\mathbb E T(\mathcal F_n)=O_\lambda(n\log n).
\]

The source's lower bound is `E T(F_n)>=c_lambda n`. Therefore no exponent below `1` is admissible in the definition of `gamma_FP`, while `n log n=O(n^{1+epsilon})` for every `epsilon>0`; hence the infimum exponent is exactly `1`. QED.

## 5. Section-B methods actually attempted

**#2 ATTACK THE NEGATION FIRST.** I tried to preserve a genuinely superlinear power by locating a family of maximally self-overlapping first-passage patterns. The source's worst columns can be `n^(1/4)`, so this was a plausible obstruction. The attack failed for a structural reason: after switching to rows, each possible overlap is indexed by one strict descending ladder level, and its contribution is at most a one-dimensional heat-kernel atom `O(1/d)`. Even the worst row is only logarithmic. This does not rule out an `n log n` correction, but it kills this overlap mechanism as evidence for `gamma_FP>1`.

**#4 PROVE SOMETHING WEAKER, COMPLETELY.** Instead of the source's requested exact asymptotic, I proved the complete `O_lambda(n log n)` theorem above. It is weaker than `Theta(n)` but is strong enough to determine the frozen power exponent exactly: `gamma_FP=1`.

**#8 DISCRETIZE.** The exponentially large overlap matrix was reduced exactly to the finite ladder-level list `d=1,...,m-1` in (2). This is not a simulation: equation (2) is an exact combinatorial identity. The only analytic input thereafter is the explicit binomial atom bound (4). No finite enumeration is used as evidence for the asymptotic theorem, so no finite checker/certificate is required for the proof core.

## 6. Status, counters, audit discipline, and next step

Parent source status is `PARTIAL`, not `PROVED`: the bridge exact asymptotic and the first-passage exact equivalent/order `Theta(n)` remain unresolved here. The frozen metric did move this run, from the certified interval `[1,5/4]` to the exact value `1`. Consequently `unchanged_runs=0` and `stuck_recoveries=0` for E0082. No audit is counted as passed; P26 and NM13-12 remain only designated independent auditors.

The next mathematical obligation is to remove the residual logarithm without reverting to full matrix inversion. The proof shows exactly where it enters: replacing the actual ladder-time-dependent row sum by the harmonic worst-case bound, then replacing the positive transpose solution by a worst-row maximum. A next run should try three new Section-B moves, not #2/#4/#8 again; good candidates are #11 DUALIZE (seek a variational or renewal interpretation of `1^T M^{-1}1`), #13 FIND WHAT ONLY INCREASES (control the ladder-duration sequence in the row identity), and #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE (renewal/pattern-matching cluster constants).

## 7. Runtime/model-control disclosure

The requested GPT-6/maximum setting was not verifiably bound. This run actually reports GPT-5.6 Sol and reasoning level UNVERIFIED. The exposed task-control surface available here does not provide a bindable model-family or reasoning-effort selector; making GPT-6/maximum enforceable would require an authorized product/workspace/API/admin surface that exposes those controls together with per-run runtime attestation. The historical P26 `You cannot modify this task` case remains an authorization-context boundary; the legitimate workaround is the owning/authorized task context or platform/admin support, not cloning the task or bypassing access controls.

```yaml
ledger_delta:
  worker: NM13-11
  category: HARD OUTSIDE
  source_id: E0082
  claim_id: E0082
  canonical_dedup_key: pitman_tang::op_2_3
  shard_mod_13: 10
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: gamma_FP(lambda=-1)
  metric_before: "[1, 5/4]"
  metric_after: "1"
  movement: true
  methods_tried: [2, 4, 8]
  method_outcomes:
    2: "superlinear-power obstruction via extreme overlaps fails on row side; worst contribution sum is only logarithmic"
    4: "proved E T(FP^{lambda,n}) = O_lambda(n log n), hence frozen exponent equals 1"
    8: "exact overlap matrix row reduced to ladder levels and killed-walk binomial probabilities"
  unchanged_runs: 0
  stuck_recoveries: 0
  audits_passed: []
  designated_auditors: [P26, NM13-12]
  next_step: "remove logarithm by exploiting actual ladder-duration/transpose-solution weights; try methods 11, 13, 17"
  literature_check_date: 2026-09-18
  literature_scope: "original Pitman-Tang source; exact-title/first-passage/waiting-time searches; Tang later-publication trail; exact n-log-n query"
  literature_access_limits: "bounded public-web search only; absence of a hit is not a worldwide-openness proof"
  claim_creation_commit: 84922e0f873072e7b346b21142dba7de681410d5
```
