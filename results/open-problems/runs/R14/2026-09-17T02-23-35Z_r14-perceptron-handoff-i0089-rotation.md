Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime and the exposed scheduler schema provide no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO PERCEPTRON METRIC MOVEMENT: `6.48139658710 -> 6.48139658710`; unchanged count `5 -> 6`; BOTH STUCK RECOVERIES WERE ALREADY USED, so this run executes the mandatory HANDOFF + ROTATION. Section-B moves actually tried on the frozen perceptron target: #9 RANDOMIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #28 REPLACE FOR ALL WITH TYPICAL.**

# R14 — negative-margin spherical perceptron handoff; rotation to I0089

Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Frozen outgoing target and final supported state

Outgoing source family: Elizabeth Gardner (1988), *The space of interactions in neural network models*, J. Phys. A 21, 257--270; modern rigorous/source navigation through Stojnic arXiv:1306.3980, El Alaoui--Sellke arXiv:2010.15811, Montanari--Zhong--Zhou arXiv:2110.15824 / PTRF 188 (2024), and Stojnic arXiv:2312.16531.

Frozen model:

- `M=floor(alpha N)`;
- iid `g_a ~ N(0,I_N)`;
- `||x||^2=N`;
- `<g_a,x>/sqrt(N) >= -1` for every row;
- whp limit `N -> infinity`.

The final rigorous R14 bracket is unchanged from C184/C185:

`alpha_L = 630297437506 / 10^11 = 6.30297437506`,

`alpha_U = 1278437096216 / 10^11 = 12.78437096216`,

`alpha_U-alpha_L = 64813965871 / 10^10 = 6.48139658710`.

Status: **PARTIAL / source problem OPEN / R14 ACTIVE ATTACK HANDED OFF**. This is not a claim that the negative-margin capacity problem is retired globally. It means only that R14 has exhausted the two owner-permitted stuck recoveries on this route and must stop spending hourly runs on the same blocker.

The lower endpoint is the source-known Montanari--Zhong--Zhou linear-programming existence threshold, imported with exact normalization. The upper endpoint is R14's rigorous certification of the globally optimized one-parameter Stojnic-2013 partial-lift/Gordon family. Numerical replica/full-RSB and higher-lift values remain **NUMERICAL / HEURISTIC unless separately certified**.

## 2. Continuity and source/status checks performed before handoff

This invocation reread/recovered on current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R14/2026-09-17T01-04-33Z_r14-recovery2-ou-semigroup.md`;
- the current R14 recovery-2 artifact;
- the R15 directory, whose newest report remains its I0076 handoff rather than a closure package;
- queue ownership/claim records for potential successors.

The approximately-780-row intake family remains too large for literal connector rendering without truncation. Intake review is therefore honestly **TARGETED / ACCESS-LIMITED**, not falsely claimed exhaustive.

A fresh bounded primary-literature check through 2026-09-17 again found no theorem closing the unrestricted full-radius negative-margin spherical Gaussian SAT threshold. In particular:

- Stojnic arXiv:2312.16531 still states the complete strong-sfl equality at parameters satisfying the stationarity system; the displayed higher-lift capacity values are obtained numerically;
- Montanari--Zhong--Zhou's rigorous upper-bound Definition/Theorem recovers the same first partial-lift/Gordon route that R14 already globally exhausted, rather than a stronger hidden closed-form endpoint;
- Annesi--Malatesta--Zamponi's transition calculation is explicitly based on a full-RSB ansatz;
- Huang--Sellke--Sun's 2026 projection-pursuit theorem is an exact algorithmic result for a dimension-free-Lipschitz class / bounded continuous activations, not an unrestricted all-hard-constraints satisfiability theorem.

A bounded negative search is not a worldwide novelty certificate.

## 3. Final three attacks on the outgoing target

### #9 — RANDOMIZE: randomized directions do not repair the uniform-support entropy mismatch

I tried to replace the deterministic sphere net in the Gaussian-polytope dual by random directions. At `kappa=-1`, UNSAT is the uniform support-function condition `h_K(v)>1` for every unit `v`, with `K=conv{g_a}` (away from the probability-zero boundary). For one fixed direction, the failure probability is only exponentially small in `N`, of order

`Phi(1+s)^(alpha N)=exp(-Theta(N))`

for fixed support slack `s>0`.

On the ordinary high-probability event `max_a ||g_a||=O(sqrt(N))`, transferring a fixed `O(1)` support slack from sampled directions to **all** directions requires angular mesh radius `O(N^(-1/2))`. Covering the whole sphere at that scale has entropy `exp((1/2+o(1))N log N)`. Randomizing the sample does not change the covering-number obstruction: exponentially many random directions in `N` leave macroscopic holes, while the required `N^(-1/2)` covering scale costs super-exponential-in-`N` sphere entropy relative to the fixed-direction tail.

Verdict: **FAILED ROUTE**. A successful geometric attack would need correlated chaining/facet geometry/Gaussian comparison, not a randomized replacement for the ordinary net.

### #23 — DO WHAT THE PROPOSER DID NOT EXPECT: search the later rigorous upper-bound literature instead of higher-lift numerics

I rechecked Montanari--Zhong--Zhou's rigorous upper bound rather than assuming the next useful inequality had to come from full-RSB/fl-RDT numerics. Their Definition 2/Theorem 4.2 supplies a rigorous one-dimensional upper-bound variational condition, and the paper explicitly relates the first part to Stojnic's earlier result.

After matching variables, this is the same one-parameter partial-lift/Gordon family already reduced and globally optimized by R14 C180--C184. Its sharp certified endpoint is the retained `12.784370962...` value. Therefore the later theorem does **not** furnish an unexploited stronger endpoint at `kappa=-1`.

Verdict: **ROUTE EXHAUSTED / NO MOVEMENT**. This check is useful because it rules out the possibility that R14 was laboriously certifying a weaker 2013 formulation while overlooking a later rigorous scalar theorem with a materially smaller endpoint.

### #28 — REPLACE FOR ALL WITH TYPICAL: algorithmic/empirical projection results do not imply zero violations

I tested whether recent exact projection-pursuit/algorithmic results could move the SAT lower endpoint by weakening the hard event from every row satisfying the margin to a typical/empirical projection statement and then repairing the residual violations.

The missing step is decisive: control of an empirical projection law or of a bounded continuous violation penalty does not imply **zero** violating rows among `alpha N` constraints. Even `o(N)` violations need a source-valid repair theorem showing that they can be eliminated while preserving the spherical norm and all previously satisfied constraints. No such repair lemma was recovered in the bounded source search, and importing an algorithmic threshold without it would confuse an attainable empirical law with satisfiability.

Verdict: **FAILED ROUTE / EXACT MISSING INGREDIENT IDENTIFIED** — a strict-buffer smoothing theorem plus a zero-violation repair mechanism would be required.

## 4. Strongest unfinished perceptron handoff

The strongest concrete unfinished route remains the complete `r=2` sfl certificate at conservative density `alpha=12.5`.

C188/recovery-2 use

`q=pD^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`,

`h_B(x)=exp(-B(x-1)_+^2)`,

`f_{p,B}(z)=E_H h_B(sqrt(p)z+sqrt(1-p)H)`,

`I=E_Z log f`, `I_B=partial_B I`, and

`K=E[(partial_z log f)^2]`.

The OU-semigroup identity gives `I_p=-K/(2p)`, and complete stationarity reduces to the three scalar-expectation residuals

`R1 = I_B + 4 gamma^2/alpha`,

`R2 = I - B I_B + c^2 T_D/(alpha c_D)`,

`R3 = K/(2p) + (c/alpha)(T_p-(c_p/c_D)T_D)`.

The exact recovery-2 artifact already proves uniform tails outside `|z|<=9`:

- `|tail(I)| < 1e-16`,
- `|tail(I_B)| < 1e-15`,
- `tail(K) < 1e-12`.

The numerical-only root at `alpha=12.5` remains near

`(p,D,gamma)=(0.656313184757223, 0.652653689820474, 0.158861855012242)`,

with numerical comparison value about `+0.00637396915`. This is **NOT** a rigorous endpoint.

A fresh numerical scout in this handoff run (also **NUMERICAL ONLY**) indicates that certification could be easier at a less ambitious first density: around `alpha=12.75`, a stationary solution is approximately

`(p,D,gamma)=(0.645767064689, 0.660121902328, 0.170303625534)`

with comparison value approximately `+0.01520099347`. Other numerical scouts gave positive values near `0.01344` at `alpha=12.70`, `0.00991` at `alpha=12.60`, and `0.00284` at `alpha=12.40`. None is promoted to the bracket.

For a future fresh assignee, the required source-valid certificate is:

1. validated compact quadrature for `I,I_B,K` (tails are already done);
2. a Poincare--Miranda, interval-Newton, or Krawczyk certificate for a true stationary root;
3. recovery/verification of the full source stationarity equations;
4. a strictly positive rigorous comparison-value enclosure;
5. only then, concentration/source theorem -> whp UNSAT and an improved `alpha_U`.

A prospective algebraic simplification worth rechecking from scratch is that the reduced equations appear to permit elimination of `D` and `gamma` in favor of `(p,B)` using R1/R3. It is deliberately recorded only as a **handoff lead, not a claimed theorem**, because this invocation is the mandatory rotation rather than a third stuck-recovery lemma.

## 5. Mandatory rotation and successor admission

Because the metric did not move after both permitted stuck recoveries, R14 may not spend another run generating a third perceptron recovery lemma. I checked higher-ranked nearby HARD queue entries and found several already owned: I0060 by R12, I0061 by the PROB20-21 successor, I0062 by P11, I0043 by R16, and I0078 by C27.

The first clean unowned HARD candidate recovered after those conflicts was **I0089**.

Create-only canonical claim:

`operations/claims/I0089.md`

creation commit:

`627e54b1b35ea74f898b9c481d3512591b893888`.

It was read back from that exact commit.

Successor source: Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, JMP 63 (2022), arXiv:2202.09240, **Conjecture 38 (Crystallization — configurations)**.

The exact source conjecture says that source-defined infinite Riesz equilibrium configurations are precisely the appropriately scaled translates/rotates of the Bravais-lattice energy minimizers. The first frozen slice is `d=1`, short-range `s>1`.

Successor metric:

`S_1 := inf { s0 >= 1 : for every s>s0 and every admissible mu>0, every d=1 short-range Riesz equilibrium configuration in the exact source sense is a scaled translate of Z }`.

Baseline: **UNMEASURED**. Target: `S_1=1`. A result only on this slice is PARTIAL relative to full Conjecture 38.

Fresh ownership review found no previous canonical `I0089` claim and no prior attempt package beyond queue/intake navigation. Fresh bounded literature searches recovered the source and later lattice-only/restricted crystallization work, but no theorem matching the full configuration-level conjecture or the frozen one-dimensional slice. This is bounded evidence only.

First successor methods are frozen as **B2, B18, B30**: attack a nonconstant-gap equilibrium counterexample first; rewrite the source condition in ordered gap variables; then solve one replacement scale/defect class at a time before attempting a global rigidity glueing argument.

## 6. R15 audit duty

The newest R15 report remains `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`. It is an OPEN/PARTIAL handoff rather than a new closure package, so the R14 closure-audit trigger does not fire in this invocation. No duplicate audit identifier is invented.

## 7. Model/scheduler boundary

The situation is still unchanged. The exposed task editing schema offers title, prompt, schedule, enablement, and timing mode, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry**. GPT-6/maximum therefore remains prompt text only here. A task returning `You cannot modify this task` must be changed from an authorized owning account/workspace context that has permission, or escalated to platform support; duplicating the task or bypassing ownership is not a valid workaround.

No scheduler change, email, Drive action, public post, purchase, workflow execution, or permission change was performed.

## 8. Structured ledger delta

```yaml
ledger_delta:
  track: R14
  outgoing_source: "Gardner 1988 negative-margin spherical Gaussian perceptron; modern rigorous navigation arXiv:1306.3980, arXiv:2010.15811, arXiv:2110.15824, arXiv:2312.16531"
  outgoing_target: "sharp satisfiability threshold at kappa=-1"
  outgoing_metric: "rigorous bracket width alpha_U-alpha_L"
  before: "6.48139658710"
  after: "6.48139658710"
  alpha_L: "6.30297437506"
  alpha_U: "12.78437096216"
  status: "PARTIAL / OPEN / HANDED OFF after both permitted stuck recoveries"
  unchanged_count_before: 5
  unchanged_count_after: 6
  methods_this_run: [9, 23, 28]
  exact_evidence:
    - "C184 retained rigorous upper endpoint"
    - "C185 retained MZZ rigorous lower endpoint"
    - "recovery-2 exact OU/tail artifact retained; no new endpoint this run"
  numerical_only_handoff:
    - "alpha=12.5 complete-2sfl scout remains non-rigorous"
    - "alpha=12.75 scout has larger positive comparison margin but remains non-rigorous"
  audits_this_run: []
  rotation:
    successor: "I0089 — Lewin 2022 Conjecture 38, crystallization of equilibrium configurations"
    claim_commit: "627e54b1b35ea74f898b9c481d3512591b893888"
    successor_metric: "S_1; baseline UNMEASURED, target 1"
    first_methods: [2, 18, 30]
```

The outgoing perceptron problem remains mathematically OPEN. R14's repeated hourly attack on it ends here unless a future explicit reassignment provides a genuinely fresh route.
