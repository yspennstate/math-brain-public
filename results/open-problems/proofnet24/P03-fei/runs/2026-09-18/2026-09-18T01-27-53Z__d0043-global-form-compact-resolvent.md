Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / HARD OUTSIDE — D0043 global exotic-edge form construction

Status: **PARTIAL / source OPEN on the bounded current screen**.

Frozen metric: **`k_exotic^cert: 0 -> 0` (NO MOVEMENT).**

Target-specific unchanged count: **`1 -> 2`**.

Section-B moves actually used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #25 COUNT THE SAME THING TWICE.**

Current canonical ownership remains:

`operations/claims/D0043.md`, creation commit `7578fb6bc235056f9d5b9f820d3087af9cc18c48`, blob `fa41e947fd62de7b036ea1a9a9e31c2642e1d18b`.

The I0098 and I0126 handoffs remain closed to P03 and were not reopened.

## 1. Continuity / repository read gate

I continued from the complete D0043 admission report

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T00-31-17Z__d0043-admission-origin-noise-bound.md`

creation commit `aef0f0530bc964050decfaebdfef891026af93db`, blob `ceb598ba2e0e62e557ee91f88ab10389cc65217c`, whose exact-commit readback had recovered `**End of complete run report.**`.

Before the mathematical attack I reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, the current root `RESULTS.md` and `QUEUE.md` surfaces, the canonical D0043 claim, the prior D0043 intake attempt `D0043-A001`, the exact D0043 intake row, and the newest accessible P04/I0101 run for directed audit.

Disclosure: `FLEET_RULES.md`, `RESULTS.md`, `QUEUE.md`, the previous P03 report, and some intake/search surfaces are larger than a single connector rendering. I used exact paths plus targeted searches/reads for D0043 and the audit claim. I do **not** claim a byte-for-byte reread of unrelated truncated rows.

Repository history remains consistent: `D0043-A001` had already checked the formal scaling balance and had flagged the divergent coefficient `t^{-k/(2k+1)}` at the origin as a possible obstruction. Claim 264 removed that local-origin obstruction. This run does not repackage either of those points as novelty.

## 2. Exact source and fresh status gate

Primary source: Bálint Virág, *Operator limits of random matrices*, ICM 2014 (arXiv:1804.06953), Conjecture 5, “Exotic edge operators.” For an analytic beta-ensemble potential whose equilibrium density vanishes at an edge like `x^(2k+1/2)`, the source conjectures scaled tridiagonal convergence to

`S_{beta,k} = -d^2/dt^2 + t^(1/(2k+1)) + (2/sqrt(beta)) t^(-k/(2k+1)) b'_t`

on the positive half-line with the soft-edge Dirichlet condition.

The source immediately distinguishes the beta=2 higher-order eigenvalue limits from the general-beta operator statement.

Fresh bounded checks on 2026-09-18 recovered:

- Virág, arXiv:1804.06953 — primary open-conjecture source.
- Krishnapur–Rider–Virág, *Universality of the Stochastic Airy Operator*, arXiv:1306.4832 — regular soft edge, general beta, and a general tridiagonal convergence framework. Its Section 13 explicitly returns to the **nonregular** case as a conjectural operator limit. The regular proof uses uniform convexity essentially.
- Li–Valkó–Xu, arXiv:2607.08536 (9 Jul 2026) — additional standard Airy-beta soft-edge/operator limits for Laguerre beta ensembles, not the exotic multicritical family.
- 2025–2026 higher-order Tracy–Widom / multicritical searches continued to return unitary/beta=2 integrable edge laws rather than a general-beta proof of Conjecture 5.

No source-matching general-beta exotic `k>=1` operator-convergence theorem was recovered. This is a bounded dated search miss, **not** a proof of worldwide openness or publication novelty.

The operational metric therefore remains

`k_exotic^cert = 0`.

## 3. Idea before proof

The previous run proved only an origin-local estimate. The next question is whether the displayed exotic formal operator exists globally as an honest lower-bounded self-adjoint operator with discrete spectrum.

For

`alpha_k = k/(2k+1)`, `p_k = 1/(2k+1)`,

there are two competing facts:

1. near zero, `t^{-alpha_k}` blows up but `alpha_k<1/2`, and Claim 264 shows Dirichlet kinetic energy dominates the singular noise locally;
2. at infinity, the deterministic confinement `t^{p_k}` grows very slowly, but for every exotic `k>=1` the white-noise coefficient **decays** like `t^{-alpha_k}`.

The regular SAO (`k=0`) has no decay in the noise coefficient and relies on the linear potential for global control. The exotic cases have the reverse trade: weaker confinement, but a decaying noise amplitude.

The source exponents obey the exact balance

`p_k + 2 alpha_k = 1`.

That scaling identity was already implicit in the old D0043 scaling check, so it is prior repository history, not a new theorem. It is nevertheless the right diagnostic for the global form.

The refutation-first question was: **does the slow confinement fail to absorb Brownian growth at infinity?**

A naive dyadic-annulus estimate is genuinely borderline and acquires a logarithmic loss. That route fails. A unit-scale Brownian-bridge decomposition removes the false macroscopic loss and proves a much stronger result: for every fixed exotic `k>=1`, the white-noise form is infinitesimally form-bounded relative to the one-dimensional kinetic energy alone, up to an `L^2` term.

This globally constructs the conjectured continuum operator for every finite exotic order. It does **not** prove any discrete tridiagonal convergence and therefore does not move the source metric.

# 4. Theorem `P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266`

**Status: PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED.**

Fix an integer `k>=1` and write

`alpha = k/(2k+1) in (0,1/2)`,

`p = 1/(2k+1)>0`,

`a(t)=t^{-alpha}`, `V(t)=t^p`.

Let `B` be standard Brownian motion on `[0,infinity)`. On the deterministic core

`C_D := {f in C_c^infinity([0,infinity)) : f(0)=0}`

define the real quadratic white-noise pairing

`N_k[f] := int_0^infinity a(t) f(t)^2 dB_t`.

Then, almost surely:

### (A) Global infinitesimal kinetic form bound
For every `eps>0` there exists a finite random constant `C_eps(B,k)` such that, for every `f in C_D`,

`|N_k[f]| <= eps int_0^infinity |f'(t)|^2 dt + C_eps(B,k) int_0^infinity |f(t)|^2 dt`.

Thus the white-noise quadratic form extends uniquely from `C_D` to a symmetric quadratic form on `H_0^1(0,infinity)` which is infinitesimally form-bounded with respect to the Dirichlet kinetic form.

### (B) Closed lower-bounded exotic form
For every fixed `beta>0`, set

`q_{beta,k}[f] = int |f'|^2 + int t^p |f|^2 + (2/sqrt(beta)) N_k[f]`

with deterministic form domain

`D_k = H_0^1(0,infinity) intersect L^2((0,infinity), t^p dt)`.

Then `q_{beta,k}` is almost surely closed and lower bounded on `D_k`. Hence it defines a unique self-adjoint operator, denoted here by the Dirichlet form realization of

`S_{beta,k} = -d^2/dt^2 + t^p + (2/sqrt(beta)) t^{-alpha} B'`.

### (C) Compact resolvent
The embedding `D_k -> L^2(0,infinity)` is compact in the form norm. Therefore the self-adjoint form realization has compact resolvent and purely discrete spectrum, with finite-multiplicity eigenvalues tending to `+infinity`.

Consequently the formal continuum operator appearing in Virág Conjecture 5 is globally well-defined, lower bounded, and spectrally discrete for every fixed exotic order `k>=1` and every fixed `beta>0`.

This theorem is **PARTIAL**: it does not prove that any multicritical beta-ensemble tridiagonal matrix converges to this operator.

## 4.1 Proof of (A): the origin

The only singularity of `a(t)=t^{-alpha}` is at zero. Fix `gamma in (0,1/2)`. Almost surely

`C_gamma(B):=sup_{0<t<=1}|B_t|/t^gamma < infinity`.

Let `0<delta<=1` and let `f in H^1(0,delta)` satisfy only `f(0)=0`; unlike Claim 264 we do **not** impose `f(delta)=0`.

Put

`E_delta = int_0^delta |f'|^2`.

Then

`|f(t)| <= t^(1/2) E_delta^(1/2)`.

With `g(t)=t^{-alpha}f(t)^2`, deterministic stochastic integration by parts gives

`int_0^delta g dB`

`= B_delta delta^{-alpha} f(delta)^2`

`  + alpha int_0^delta B_t t^{-alpha-1} f(t)^2 dt`

`  - 2 int_0^delta B_t t^{-alpha} f(t) f'(t) dt`.

The extra upper-boundary term, absent in Claim 264, satisfies

`|B_delta| delta^{-alpha} f(delta)^2`

`<= C_gamma delta^(gamma-alpha+1) E_delta`.

The other two terms are bounded exactly as in Claim 264:

`alpha int |B_t| t^{-alpha-1}f^2`

`<= C_gamma [alpha/(gamma-alpha+1)] delta^(gamma-alpha+1) E_delta`,

and

`2 int |B_t|t^{-alpha}|f f'|`

`<= [2 C_gamma/sqrt(2gamma-2alpha+2)] delta^(gamma-alpha+1) E_delta`.

Therefore

`|int_0^delta t^{-alpha} f^2 dB|`

`<= C_gamma delta^(gamma-alpha+1)`

`   * [1 + alpha/(gamma-alpha+1) + 2/sqrt(2gamma-2alpha+2)] E_delta`.

Because `gamma-alpha+1>0`, the coefficient tends to zero with `delta`.

This removes the artificial upper-end Dirichlet condition from the previous local theorem and makes the origin estimate usable inside a global partition.

## 4.2 Proof of (A): the tail by unit Brownian bridges

For integers `n>=1` let

`I_n=[n,n+1]`,

`Delta_n=B_{n+1}-B_n`,

and define the Brownian bridge on `I_n`

`W_n(t)=B_t-B_n-(t-n)Delta_n`.

Then `W_n(n)=W_n(n+1)=0` and, on `I_n`,

`dB_t = Delta_n dt + dW_n(t)`.

Let

`M_n=max{|Delta_n|, sup_{t in I_n}|W_n(t)|}`.

Gaussian increment tails and Brownian-bridge supremum tails imply that for sufficiently large deterministic `C`,

`sum_n P(M_n > C sqrt(log(n+2))) < infinity`.

By Borel–Cantelli, almost surely there is a finite random constant `C_B` such that for all `n>=1`,

`M_n <= C_B sqrt(log(n+2))`.

Since `alpha>0`,

`A_* := sup_{n>=1} M_n n^{-alpha} < infinity`

almost surely.

Now take `f in C_D` and on `I_n` put `g=a f^2`. Because `W_n` vanishes at both endpoints,

`int_{I_n} g dB`

`= Delta_n int_{I_n} g dt - int_{I_n} W_n(t) g'(t) dt`.

On `I_n`,

`a(t)<=n^{-alpha}`

and

`|a'(t)|=alpha t^{-alpha-1}<=alpha n^{-alpha-1}<=alpha n^{-alpha}`.

Hence

`|int_{I_n} a f^2 dB|`

`<= M_n n^{-alpha}`

`   * [(1+alpha) int_{I_n} f^2 + 2 int_{I_n}|f f'|]`.

Summing over `n>=1` gives

`|int_1^infinity a f^2 dB|`

`<= A_*[(1+alpha)||f||_{L^2(1,infinity)}^2`

`          + 2 int_1^infinity |f f'|]`.

For any `eta>0`, Young's inequality yields

`2 A_* |f f'| <= eta |f'|^2 + (A_*^2/eta)|f|^2`.

Therefore

`|int_1^infinity a f^2 dB|`

`<= eta ||f'||_{L^2(1,infinity)}^2`

` + [(1+alpha)A_* + A_*^2/eta] ||f||_{L^2(1,infinity)}^2`.

This is an infinitesimal form bound on the entire tail.

### Why the exotic decay matters

For `k>=1`, `alpha>0`, so `n^{-alpha}sqrt(log n)->0` and `A_*<infinity`.

For the regular SAO `k=0`, this particular tail proof fails because `alpha=0` and `M_n` is unbounded. That is exactly where the regular theory instead exploits the much stronger deterministic confinement `V(t)=t`.

Thus deforming from `k=0` to `k=1` reveals a real exchange of mechanisms: the confinement weakens, but the noise amplitude acquires enough decay to make the unit-block tail form easier.

## 4.3 Proof of (A): the fixed middle interval

Fix the small `delta` chosen in the origin step. On `[delta,1]`, `a` and `a'` are bounded and the Brownian path is continuous.

Stochastic integration by parts gives

`int_delta^1 a f^2 dB`

as two finite boundary traces plus an ordinary integral of `B(a'f^2+2aff')`.

The one-dimensional trace inequality on the fixed interval gives, for every `eta>0`,

`|f(delta)|^2+|f(1)|^2`

`<= eta int_delta^1 |f'|^2 + C_{eta,delta} int_delta^1 |f|^2`.

The cross term is controlled by Young's inequality in the same way. Hence, pathwise, for each `eta>0`,

`|int_delta^1 a f^2 dB|`

`<= eta int_delta^1 |f'|^2 + C'_{eta,delta,B} int_delta^1 |f|^2`.

Choose `delta` so the origin coefficient is at most `eps/3`, then choose the middle and tail Young parameters so their kinetic coefficients are each at most `eps/3`. Adding the three regions proves (A).

The same estimate applied after polarization extends the symmetric bilinear form from the core to `H_0^1(0,infinity)`.

## 4.4 Proof of (B): KLMN

Define the deterministic confining form

`q_{0,k}[f]=int_0^infinity |f'|^2 dt + int_0^infinity t^p |f|^2 dt`

on

`D_k=H_0^1 intersect L^2(t^p dt)`.

This form is closed and nonnegative.

By (A), for every `eps>0`,

`|(2/sqrt(beta))N_k[f]|`

`<= eps q_{0,k}[f] + C_{eps,beta,B,k} ||f||_2^2`

after rescaling `eps` if necessary.

Choose `eps<1`. The KLMN theorem yields that

`q_{beta,k}=q_{0,k}+(2/sqrt(beta))N_k`

is closed and lower bounded on the **same** form domain `D_k`. The representation theorem gives a unique self-adjoint operator. This proves (B).

## 4.5 Proof of (C): compact resolvent

The deterministic form-domain embedding `D_k -> L^2(0,infinity)` is compact.

Indeed, if a sequence is bounded in the `q_{0,k}+||.||_2^2` norm, then for every `R>1`,

`int_R^infinity |f(t)|^2 dt`

`<= R^{-p} int_R^infinity t^p |f(t)|^2 dt`,

so the `L^2` tail is uniformly small as `R->infinity`.

On every bounded interval `[0,R]`, the sequence is bounded in `H^1`, and Rellich compactness gives a convergent subsequence in `L^2(0,R)`. Combining the compact interior with the uniformly small tail proves compactness on the half-line.

Because the perturbation is infinitesimally `q_{0,k}`-bounded, a sufficiently shifted `q_{beta,k}` form norm is equivalent to the deterministic form norm on `D_k`. Therefore the perturbed form-domain embedding is compact as well. The associated self-adjoint operator has compact resolvent and purely discrete spectrum.

This proves Claim 266. QED.

# 5. Section-B outcomes and failures

## B6 — DEFORM TO A POINT YOU CAN SOLVE

The deformation from regular SAO (`k=0`) to `k=1` does **not** fail at the singular origin. Claim 264 plus the strengthened local estimate above handle it. At infinity, the regular and exotic mechanisms trade places:

- regular `k=0`: constant noise amplitude, strong `t` confinement;
- exotic `k>=1`: weak `t^p` confinement, but decaying `t^{-alpha}` noise amplitude.

The continuum form survives the deformation completely. Therefore the first real obstruction is no longer continuum operator existence.

## B12 — FIND WHAT IS CONSERVED

The exact exponent balance

`p_k+2alpha_k=1`

is the source scaling relation already implicit in D0043-A001. At form level it explains why a **macroscopic** Brownian fluctuation on scale `t` is exactly borderline with the deterministic potential: Brownian size `t^{1/2}` times `t^{-alpha}` squares to `t^{1-2alpha}=t^p`.

The new information is that one need not pay that macroscopic fluctuation. The unit-bridge decomposition localizes Brownian oscillations to scale one, where the coefficient is `t^{-alpha}` and therefore decays. This gives an infinitesimal kinetic bound.

## B25 — COUNT THE SAME THING TWICE

I estimated the tail two ways.

**Failed macroscopic/dyadic count.** On a dyadic annulus `[2^j,2^{j+1}]`, a crude Brownian oscillation bound is of size about `2^{j/2}sqrt(j)`. Multiplying by `a~2^{-alpha j}` and squaring the cross coefficient produces

`j * 2^{j(1-2alpha)} = j * 2^{j p}`,

which loses a logarithm relative to the confining weight `t^p`. This route does not prove infinitesimal form boundedness.

**Successful unit-block count.** On `[n,n+1]`, the bridge size is only `O(sqrt(log n))` almost surely. The effective coefficient is

`n^{-alpha}sqrt(log n)`,

which is bounded and tends to zero for every exotic `alpha>0`. This removes the false logarithmic obstruction.

The disagreement between the two counts is not a contradiction; it identifies the wrong scale in the dyadic proof.

# 6. Comparison with the regular tridiagonal-to-SAO convergence framework

Krishnapur–Rider–Virág formulate a general tridiagonal-operator convergence theorem with two broad inputs:

1. **tightness/convergence of the integrated potential process** on compact spatial sets;
2. a **global growth/oscillation bound** over the whole matrix index range.

In their regular soft-edge beta-ensemble proof the integrated potential converges to Brownian motion plus deterministic quadratic drift, and their long-range bounds use the regularity/uniform convexity of the tridiagonal Gibbs field. Their paper explicitly notes that uniform convexity is used essentially in the regular proof and treats the nonregular edge operator as conjectural in its final section.

Claim 266 shows that **if** the multicritical discrete integrated potentials converge to Virág's displayed continuum noise/drift, then the proposed continuum target is not blocked by a hidden form-domain pathology: it is a legitimate compact-resolvent operator.

The unresolved source-level step is therefore on the discrete side:

- derive the `k=1` edge scaling of the tridiagonal equilibrium/minimizer coefficients in a nonregular potential;
- prove tightness and the Brownian functional limit for the correctly rescaled integrated fluctuation field;
- prove the analog of the global growth/oscillation estimate without the uniform-convexity mechanism used in the regular proof;
- pass from those estimates to operator/eigenpair convergence for every fixed `beta>0`.

A continuum form theorem alone does not move `k_exotic^cert`.

# 7. Exact remaining obligation / simplest live case

The simplest source-valid unresolved case remains `k=1`:

`S_{beta,1}=-d^2/dt^2+t^(1/3)+(2/sqrt(beta))t^(-1/3)B'`.

Claim 266 now gives an honest Dirichlet self-adjoint compact-resolvent realization for this operator for every fixed `beta>0`.

The **exact remaining obligation** is no longer “define the operator.” It is:

> For a source-admissible analytic beta-ensemble potential with a cubic/multicritical edge density `x^(5/2)`, prove that the source-scaled tridiagonal integrated potentials satisfy the nonregular analogs of the Krishnapur–Rider–Virág tightness/convergence and global oscillation hypotheses, with limiting drift/noise corresponding exactly to `t^(1/3)` and `t^(-1/3)B'`.

No such theorem was recovered in the fresh bounded 2026-09-18 literature screen.

Metric remains **`k_exotic^cert: 0 -> 0`**.

# 8. Directed P04 / I0101 independent second audit

Fresh P04 claim not previously audited by P03:

`P04-I0101-LEVEL4-MARKOV-BLOWUP-34 = PROVED / STRUCTURAL-PARTIAL`.

Path:

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T00-43-10Z__run-report.md`

Creation commit: `9ee8ef6b596da30ac7ef83776c6a2c973793ccfb`.

Verified report blob: `1a51b0084679afb1e3720addeb0b0b27afa79fa1`.

Readback receipt:

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T00-43-10Z__readback-receipt.md`, blob `88bfa8803a53691d00630f24321e62cf79aaf027`.

Audit ID:

`P03-AUDIT-P04-I0101-LEVEL4-MARKOV-BLOWUP-267 = PASS (CLAIM-SCOPED)`.

## 8.1 Independent proof check

For a finite graph `K=(V,E)`, let `P(K)` be the symmetric entrywise-nonnegative stochastic matrices supported on edges of `K`, with zero diagonal, and let

`mu(K)=max_{P in P(K)} lambda_min(P)`

when the feasible set is nonempty.

Let `K^(r)` be the balanced independent `r`-blowup. Label clones `(i,a)` and define

`W:R^|V| -> R^{r|V|}` by `(Wf)_(i,a)=f_i/sqrt(r)`.

Then `W^T W=I`.

### Compression
If `Ptilde` is feasible upstairs, `P=W^T Ptilde W` is feasible downstairs: nonnegativity, symmetry, row sums, zero diagonal blocks, and support all transfer blockwise. For every unit `f`,

`f^T P f=(Wf)^T Ptilde(Wf)>=lambda_min(Ptilde)`,

hence

`lambda_min(P)>=lambda_min(Ptilde)`.

Thus `mu(K)>=mu(K^(r))`.

### Uniform lift
Conversely, if `P` is feasible downstairs, `Ptilde=W P W^T` has constant `(i,j)` clone block `P_ij/r`, is feasible upstairs, and acts as `P` on `im W` and as zero on `(im W)^perp`. Therefore

`spec(Ptilde)=spec(P) union {0}^{(r-1)|V|}`.

For a nontrivial feasible zero-diagonal symmetric stochastic `P`, `tr(P)=0` while `1` is an eigenvalue, so `lambda_min(P)<0`. Hence

`lambda_min(Ptilde)=lambda_min(P)`.

This gives the reverse inequality and proves

`mu(K^(r))=mu(K)`.

### Fiber averaging
Averaging any upstairs feasible matrix over independent clone permutations preserves feasibility. Since `lambda_min` is concave, this averaging cannot decrease the least eigenvalue. The averaged matrix has constant clone blocks and is exactly the uniform lift of its compression. Therefore clone-symmetry breaking cannot improve the objective.

### Resolvent identity
For a uniform lifted symmetric operator `Atilde=W A W^T`, the orthogonal decomposition `im W direct-sum (im W)^perp` gives

`(zI+Atilde)^(-1)=W(zI+A)^(-1)W^T + z^(-1)(I-WW^T)`.

Since `1_{rN}=sqrt(r) W1_N`,

`(1/r) 1_{rN}^T(zI+Atilde)^(-1)1_{rN}`

`=1_N^T(zI+A)^(-1)1_N`.

All five theorem clauses checked independently. The specialization to P04's level-4 cover follows once the previously proved four-to-one graph blowup identity is imported. This audit is claim-scoped and does not certify the eventual Paley-theta conjecture.

Verdict:

**`P03-AUDIT-P04-I0101-LEVEL4-MARKOV-BLOWUP-267 = PASS (CLAIM-SCOPED)`**.

# 9. Cumulative D0043 claim ledger

| Claim | Status | Scope |
|---|---|---|
| D0043-A001 formal scaling check | PRIOR REPOSITORY ATTEMPT | Formal source scaling consistency; origin singularity flagged; not P03 novelty. |
| `P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264` | PROVED / PARTIAL | Local near-zero white-noise form is arbitrarily small vs kinetic energy for every finite `k`. |
| `P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266` | PROVED / PARTIAL | For every fixed exotic `k>=1`, the full half-line Dirichlet form is closed/lower bounded with compact resolvent; no discrete convergence. |
| Virág Conjecture 5 | OPEN on bounded current screen | General-beta multicritical tridiagonal operator convergence remains unproved here. |

# 10. Failure analysis / next attack

The continuum-operator-definition route has now moved substantially and should **not** consume another run unless an actual gap is found in Claim 266.

The next attack must cross to the discrete side. The best target is the first exotic order `k=1` and the nonregular analog of the KRV Assumption-1/Assumption-2 mechanism.

Recommended next Section-B triple, avoiding this run's #6/#12/#25:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT** — perturb a regular potential toward a first multicritical potential and compute how the edge minimizer/Hessian degenerates.
- **#15 BREAK THE SYMMETRY ON PURPOSE** — isolate one coefficient direction responsible for loss of uniform convexity instead of treating the whole tridiagonal Gibbs field at once.
- **#20 FIND WHY THE ALGORITHM FAILS** — apply the regular KRV proof step-by-step at `k=1` and identify the first estimate whose exponent or Hessian lower bound actually fails.

A theorem-sized next result would be either:

1. a proved `k=1` integrated-potential functional CLT/tightness theorem under an explicit source-admissible multicritical potential, or
2. a rigorous obstruction showing a specific regular-edge KRV hypothesis cannot hold verbatim and stating the correct weighted replacement.

# 11. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  target: D0043
  source: "Balint Virag, Operator limits of random matrices, ICM 2014, Conjecture 5"
  metric: k_exotic^cert
  before: 0
  after: 0
  movement: NO_MOVEMENT
  unchanged_count_before: 1
  unchanged_count_after: 2
  status: PARTIAL_SOURCE_OPEN_ON_BOUNDED_2026_09_18_SCREEN
  new_claim:
    id: P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266
    status: PROVED_STRUCTURAL_PARTIAL_PUBLICATION_NOVELTY_UNVERIFIED
    summary: "For every fixed exotic k>=1 and beta>0, the white-noise form t^{-k/(2k+1)}B' is globally infinitesimally kinetic-form-bounded; the Dirichlet exotic operator form is closed/lower bounded with compact resolvent. This does not prove tridiagonal convergence."
  peer_audit:
    id: P03-AUDIT-P04-I0101-LEVEL4-MARKOV-BLOWUP-267
    verdict: PASS_CLAIM_SCOPED
    peer_claim: P04-I0101-LEVEL4-MARKOV-BLOWUP-34
    peer_report: proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T00-43-10Z__run-report.md
    peer_creation_commit: 9ee8ef6b596da30ac7ef83776c6a2c973793ccfb
    peer_blob: 1a51b0084679afb1e3720addeb0b0b27afa79fa1
  next_state: D0043_ACTIVE_DISCRETE_MULTICRITICAL_CONVERGENCE_GATE
```

# 12. Delivery / runtime limitations

GitHub only. No Gmail/email, Drive, public posting, paid compute, access changes, workflow execution, unreviewed external scripts, or extra schedules were used.

The requested model is GPT-6 with maximum reasoning, but this runtime actually identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry. Reasoning level is therefore reported as **UNVERIFIED**, not invented.

**End of complete run report.**
