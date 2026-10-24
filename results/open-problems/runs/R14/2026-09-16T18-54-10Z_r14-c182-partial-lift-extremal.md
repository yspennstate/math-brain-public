Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated model selector or reasoning-effort selector, so I do not claim otherwise. **Metric movement:** `10.612411 -> 10.61241096216`. **Section-B moves actually tried:** **#24 FIND THE EXTREMAL OBJECT, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY**.

Problem/source: Elizabeth Gardner (1988), *The space of interactions in neural network models*, J. Phys. A 21, 257–270, DOI `10.1088/0305-4470/21/1/030`; modern negative-margin spherical-Gaussian formulation and scope in Stojnic arXiv:1306.3980, El Alaoui–Sellke arXiv:2010.15811, and Stojnic arXiv:2312.16531. Frozen target: rigorous SAT/UNSAT threshold bracket at `kappa=-1` for iid standard-Gaussian constraints on `S^{N-1}(sqrt(N))`.

Status: **PARTIAL**. This run does not determine the exact threshold. It does two things that materially change the research state:

1. it rigorously identifies the **global optimum of the entire one-parameter partially lifted Stojnic-2013 upper-bound family** at `kappa=-1`, reducing that optimization to one scalar root;
2. it proves that this whole family bottoms out in the tiny interval
   `12.78437096209 < alpha_PL^* < 12.78437096216`.

Consequently the frozen rigorous UNSAT endpoint may be set to the exact rational

`alpha_U = 1278437096216/10^11 = 12.78437096216`,

while the retained C178 SAT endpoint remains

`alpha_L = 54299/25000 = 2.17196`.

The tracked width is therefore

`alpha_U-alpha_L = 132655137027/12500000000 = 10.61241096216`.

The quantitative movement is intentionally tiny. The structural movement is large: the 2013 partial-lift route is now rigorously exhausted to about `7e-11` in alpha, so any material upper-bound improvement must use a genuinely higher lifting level or a different method.

# 1. Required repository continuation

Repository: `yspennstate/math-open-problems`, branch `master`.

Before new mathematics this run read or queried:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R14/2026-09-16T17-52-00Z_r14-c180-concavity-alpha12784371.md`;
- its exact checker `artifacts/R14/2026-09-16T17-52-00Z_r14-c180-concavity-alpha12784371_checker.py`;
- newest visible neighboring/audit-target R15 report `runs/R15/20260916_1756Z_i0076_uniform_phase_a15.md`;
- current campaign exclusions and current R14 ownership;
- current arXiv pages for `2010.15811`, `2312.16531`, the recent full-RSB-ansatz work, and later algorithmic work.

The corpus-wide intake files remain too large for literal all-lines rendering through the connector; this run's intake read is therefore **ACCESS-LIMITED / INCOMPLETE**, not represented as a complete row-by-row audit.

The canonical R14 state recovered from C181 was:

- rigorous whp SAT endpoint `alpha_L=54299/25000=2.17196`;
- rigorous whp UNSAT endpoint `alpha_U=12784371/10^6=12.784371`;
- width `10.612411`;
- C180: corrected Stojnic partial-lift scalar functional and strict concavity in its scalar `s`;
- C181: exact UNSAT certificate at `alpha=12.784371`;
- X40: source sign typo identified and repaired by an independent derivation.

# 2. Model / scheduler interface status

The technical situation is unchanged. The exposed task interface has scheduling/prompt fields but no model field, no reasoning-effort field, and no authenticated runtime telemetry. `GPT-6 / maximum` is prompt text only. This run therefore reports the actual visible model, GPT-5.6 Sol, and reasoning as UNVERIFIED.

Repository policy also records that a historical P26 modification probe returned `You cannot modify this task`, while a later update succeeded in a different authorized context. The legitimate remedy is an authorized owning account/workspace context that exposes the task, or platform support. Duplicate-task creation, permission bypass, and repository-only imitation are not valid fixes. This run makes no scheduler change.

# 3. Source and current proof boundary — checked 2026-09-16

## Gardner locator

Gardner's 1988 paper is the original statistical-mechanics capacity locator. Its calculation is replica/saddle-point based; it is not a rigorous theorem establishing the negative-margin capacity.

## El Alaoui–Sellke candidate — exact normalization

For nondecreasing right-continuous `gamma:[0,1]->[0,1]`, equal to one strictly before one, define

`lambda_gamma(q)=int_q^1 gamma(t) dt`,

`qbar(gamma)=sup{q:gamma(q)<1}`.

Their PDE is

`partial_q Phi_gamma + (1/2)[gamma(q)(partial_x Phi_gamma)^2 + partial_xx Phi_gamma]=0`

with hard terminal value `0` on `x>=kappa` and `-infinity` on `x<kappa`. Their equation (2.3) is

`P_{alpha,kappa}(gamma)
 = alpha Phi_gamma(0,0)
 + (1/2) int_0^{qbar} dq/lambda_gamma(q)
 + (1/2) log(1-qbar)`.

Write `P_* = inf_gamma P`. Their all-negative-margin identification of capacity with the corresponding full-RSB variational transition is conjectural in this source. Their algorithmic theorem is conditional on the conjectured FRSB/no-overlap-gap sector and returns a feasible point near radius `sqrt(qbar N)`, `qbar<1`, not a full-radius point.

## Later primary claims

Stojnic 2023 says fully lifted RDT is used to characterize capacity but also says practical use requires substantial numerical work and reports rapid convergence of finite stationarized levels as an observation.

The source's numerical tables at `kappa=-1` display approximately:

- first full / Gardner level: `13.27`;
- second partial: `12.78`;
- second full: `12.32`;
- third full: `12.29`.

These are not silently promoted here. The same paper's modulo-m theorem gives an inequality and then says numerical evaluations found no failure of tightness; that observed equality is not itself an interval-certified theorem. The full second/third-level route therefore still needs exact stationarity and nested-expectation validation before a table entry can become this track's rigorous endpoint.

Annesi–Malatesta–Zamponi explicitly state that they compute the transition using a full-RSB ansatz. Recent Huang–Sellke–Sun work addresses an algorithmic class and explicitly distinguishes it from unrestricted feasible-projection geometry. No later primary theorem found in this bounded dated search supplies the requested rigorous full-radius SAT+UNSAT equality for every fixed negative margin.

# 4. Retained corrected 2013 partial-lift objective

C180 independently rederived the intended partial-lift scalar functional, avoiding the sign typo in the printed 2013 equations.

At `kappa=-1`, define

`L(s)=Phi(1)+s exp(-(1-s^2)/2) barPhi(s)`, `0<s<1`,

`ell(s)=log L(s)<0`,

`B(s)=s^2/[2(1-s^2)]`,

and

`A(c)=[sqrt(c^2+4)-c]/4 + asinh(c/2)/c`.

Then the comparison objective is

`F(c,alpha,s)=A(c)-c B(s)+(alpha/c) ell(s)`.

For each fixed `c,alpha>0`, C180 proved `s -> F(c,alpha,s)` is strictly concave on `(0,1)`.

For fixed `c`, let `U(c)` be the unique critical density satisfying

`max_{0<s<1} F(c,U(c),s)=0`.

Then any `alpha>U(c)` yields a strict negative comparison objective and hence whp UNSAT by the same Gaussian-comparison/concentration framework used in C181.

The question this run attacks is now exact and finite-dimensional:

`alpha_PL^* := inf_{c>0} U(c)`.

# 5. Move #29 — ADD THE POINTS AT INFINITY: the optimum cannot hide at c=0 or c=infinity

This compactifies the only remaining 2013 partial-lift parameter.

For `c -> infinity`, evaluate the threshold formula at `s=0`. Since

`F(c,alpha,0)=A(c)+(alpha/c) log Phi(1)`

and `c A(c) ~ log c`, any threshold satisfying `F<=0` obeys

`U(c) >= c A(c)/[-log Phi(1)] -> infinity`.

Thus the minimizing sequence cannot escape to infinity.

For `c -> 0`, choose the explicit deformation

`s_c = 1-c/2`.

Let

`d_1=L'(1)=2 barPhi(1)-phi(1)`.

Taylor expansion at `(c,s)=(0,1)` gives

`A(c)=1+O(c)`,

`c B(1-c/2)=1/2+O(c)`,

`-ell(1-c/2)=d_1 c/2+O(c^2)`.

Therefore the density required to make this one test point nonpositive satisfies

`liminf_{c downarrow 0} U(c) >= 1/d_1`.

But `1/d_1` is exactly the old Gardner/Stojnic first-level upper endpoint at `kappa=-1`, about `13.2732`, strictly above C181's `12.784371`.

Hence the global minimizer of `U(c)` exists at an interior `c_*>0`.

This is not just topological bookkeeping: once the boundary is excluded, the envelope derivative at the minimizing `c_*` is a legitimate stationarity equation rather than an unjustified optimization heuristic.

# 6. Move #24 — FIND THE EXTREMAL OBJECT: exact saddle equations collapse to one scalar root

At the interior global minimizer, strict concavity gives a unique contact point `s_* in (0,1)` such that

`F(c_*,alpha_*,s_*)=0`,
`partial_s F(c_*,alpha_*,s_*)=0`,
`partial_c F(c_*,alpha_*,s_*)=0`,

where `alpha_* = alpha_PL^*`.

The last condition is an envelope-theorem consequence, not an interchange of min and max.

From

`F/c = A/c - B + alpha ell/c^2 = 0`

and

`F_c = A' - B - alpha ell/c^2 = 0`,

adding gives

`A/c + A' - 2B = 0`.

Direct differentiation of `A` gives the exact identity

`A/c + A' = [sqrt(c^2+4)-c]/(2c)`.

Therefore

`B(s)=[sqrt(c^2+4)-c]/(4c)`.

With `B(s)=s^2/[2(1-s^2)]`, this solves exactly as

**(C182.1)**

`c_* = (1-s_*^2)/s_*`.

Then

`sqrt(c_*^2+4)=(1+s_*^2)/s_*`

and

`asinh(c_*/2)=-log s_*`.

Consequently

`A(c_*)-c_*B(s_*) = -log(s_*)/c_*`.

The equation `F=0` becomes

`alpha_* = log(s_*)/ell(s_*)`.

Meanwhile

`B'(s)=s/(1-s^2)^2`

and C182.1 gives

`c_*^2 B'(s_*)=1/s_*`.

Thus `F_s=0` gives

`alpha_*=1/[s_* ell'(s_*)]`.

Combining the two representations yields the single scalar equation

**(C182.2)**

`ell(s_*) = s_* log(s_*) ell'(s_*)`.

Equivalently, if

`h(s)=ell(s)/log(s)`,

then `s_*` is a critical point of `h`, and

**(C182.3)**

`alpha_PL^* = 1/max_{0<s<1} h(s)`.

This turns the full one-parameter partial-lift optimization into a one-dimensional extremal problem independent of `c`.

# 7. Move #13 — FIND WHAT ONLY INCREASES: the scalar extremum is unique

Define

`k(s)=s ell'(s)`.

Because `ell(1)=0`,

`h(s)
 = [int_s^1 k(t) dt/t] / [int_s^1 dt/t]`.

So `h(s)` is the logarithmic right-tail average of `k`.

The exact finite core studies

`K(s)=L(s)^2 k'(s)`.

Writing derivatives of `L` explicitly, one obtains

`K = L L' + s L L'' - s (L')^2`

and

`K' = 2 L L'' + s L L''' - s L' L''`.

The checker covers the compact interval `[0,1]` with exact rational interval arithmetic: cells of width `10^-2` up to `0.89`, then width `10^-3` through `1`. On every cell,

`K'(s)<0`.

It also proves

`K(0)>0`, `K(1)<0`.

Hence `K` crosses zero exactly once, so `k` is strictly increasing up to one point `s_0` and strictly decreasing afterwards.

This unimodality forces `h` to have exactly one critical point:

- as `s downarrow 0`, `k(s)=O(s)` while `h(s)~[-log Phi(1)]/|log s|`, so `h(s)>k(s)` for small `s`;
- at the unique maximum `s_0` of `k`, the right-tail average `h(s_0)` is strictly less than `k(s_0)`;
- on `(0,s_0)`, for `d=h-k`,
  `d'=d/[s(-log s)]-k'`; at any zero of `d`, `d'=-k'<0`, so there can be at most one crossing;
- after `s_0`, `k` is strictly decreasing, hence its right-tail average satisfies `h(s)<k(s)`.

Therefore `h` rises, has one global maximum, and falls. C182.2 has exactly one solution.

This proves that the partial-lift extremizer is globally unique, not merely a numerical stationary point.

# 8. R14-C182 — exact global characterization of the 2013 partial-lift optimum

**STATUS: PROVED.**

For `kappa=-1`, the globally best upper threshold obtainable from the corrected one-parameter partially lifted Stojnic-2013 comparison is attained at the unique `s_* in (0,1)` solving

`ell(s)=s log(s) ell'(s)`,

with

`c_*=(1-s_*^2)/s_*`

and

`alpha_PL^*=1/[s_* ell'(s_*)]=log(s_*)/ell(s_*)`.

No min-max exchange is used. Boundary escape is excluded by Section 5; the unique maximizer in `s` comes from C180 strict concavity; uniqueness of the global `c` extremum follows from the unique maximum of `h`.

# 9. R14-C183 — exact interval for the intrinsic partial-lift floor

**STATUS: PROVED by exact rational arithmetic.**

The checker uses Machin-series rational bounds for `pi`, alternating rational bounds for the Gaussian integrals/exponentials, and atanh-series rational bounds for logarithms.

It proves

`g(s):=ell(s)-s log(s) ell'(s) <0`

at

`s=0.58444642236`

and

`g(s)>0`

at

`s=0.58444642238`.

By C182 uniqueness,

`0.58444642236 < s_* < 0.58444642238`.

The checker also proves `K(0.7)>0`, so `k` is still increasing over this root bracket. Therefore

`1/k(0.58444642238) < alpha_PL^* < 1/k(0.58444642236)`.

Exact interval propagation yields the clean rational enclosure

**(C183.1)**

`12.78437096209 < alpha_PL^* < 12.78437096216`.

Thus the entire 2013 one-parameter partial-lift route cannot ever yield a rigorous upper endpoint below `12.78437096209`.

This is the main route-obstruction result of the run.

# 10. R14-C184 — new rigorous whp UNSAT endpoint and metric

**STATUS: PROVED.**

Take the exact rational

`alpha_U = 1278437096216/10^11 = 12.78437096216`.

C183 proves

`alpha_U > alpha_PL^*`.

At the genuine minimizer `c_*`, the maximum partial-lift comparison objective is exactly zero at `alpha_PL^*`. Increasing `alpha` strictly decreases `F(c_*,alpha,s)` for every `s in (0,1)` because `ell(s)<0`. The maximum is attained in the interior and therefore becomes strictly negative at `alpha_U`.

The same rigorous Stojnic Gaussian-comparison/concentration argument as in C181 therefore gives

`kappa=-1`, `alpha=12.78437096216`
`=> P(SAT)->0`.

Retaining C178,

`alpha_L=54299/25000=2.17196`.

Hence

**(C184.1)**

`2.17196 <= alpha_c(-1) <= 12.78437096216`

and the fixed metric becomes exactly

**(C184.2)**

`alpha_U-alpha_L
 = 132655137027/12500000000
 = 10.61241096216`.

Previous width: `10.612411`.

New width: `10.61241096216`.

The movement is `3.784e-8`.

# 11. What the 2023 full-lift source says, and why it is not yet in the bracket

The numerical 2023 tables are now especially informative because C183 proves there is essentially nothing left to gain from the partial-lift family.

At `kappa=-1`, the source reports approximately

- `2-spl RDT`: `12.78`;
- `2-sfl RDT`: `12.32`;
- `3-sfl RDT`: `12.29`.

The second-full table gives numerical parameters near

`gamma_sq=0.1500`,
`gamma_sq^(p)=1.6660`,
`p_2=0.6649`,
`q_2=0.2780`,
`c_2=3.7194`.

However these table values remain numerical. The modulo-m theorem later gives a one-sided inequality, and the paper says numerical evaluation did not find a case where it was non-tight. That observed tightness is not the exact certificate required by this track.

Therefore the next material upper-bound route is sharply isolated:

> rigorously validate one second-full stationary point, including every nested Gaussian expectation and the correct inequality/equality direction, or derive a direct sufficient UNSAT inequality from the second-level construction that avoids assuming numerical stationarity.

C183 shows that spending another run optimizing the 2013 partial-lift scalar beyond its intrinsic floor would be scientifically negligible.

# 12. Independent R15 audit

Newest visible R15 package:
`runs/R15/20260916_1756Z_i0076_uniform_phase_a15.md`.

I independently audited its theorem `R15-PR1`.

**Audit ID:** `R14-AUDIT-R15-I0076-PR1-05 = PASS`.

The key point requiring care is that the seam `T` and the offset `A_n=T-S_n` may be fully anticipative. Let `U~Unif[0,1]` be independent of the original sigma-field and

`R_n={A_n+U}`.

Conditional on the entire original sigma-field, `A_n` is fixed and `R_n` is uniform. Therefore `R_n` is uniform and independent of the original sigma-field, hence independent of the Brownian witness path `B^(n)`.

On `E_n={S_n<T}` write

`A_n+U=M_n+R_n`, `M_n in Z_{>=0}`.

For a Wiener-null Borel set `N` and fixed integer `m`,

`{F^{T,U} in N, E_n, M_n=m}`
is contained in
`{theta^+_{m+R_n} B^(n) in N}`.

The right-hand event has probability zero: condition on `R_n=r`; deterministic Brownian increment-shifting by `m+r` preserves the one-sided Wiener law. Summing over the countable `m`, then over `n` with `union_n E_n` of probability one, gives

`Law(F^{T,U}) << W_+`.

The argument does not condition on `M_n` and therefore does not mistakenly assert independence of `M_n` from the path. This was the subtle point worth checking.

The backward analogue follows by time reversal. R15 correctly states that independently smoothing the two halves does **not** produce one physical re-rooting of `X`, so this partial theorem does not solve Burdzy–Scheutzow Problem 7.2. I audit PR1 only, not the full R15 target.

# 13. Cumulative R14 ledger

Retained:
- C175: rigorous baseline bracket at `kappa=-1`;
- C178: whp SAT at `alpha_L=2.17196`;
- C179/C181: rigorous partially lifted whp UNSAT route;
- X40: literal plus-sign continuation in the 2013 printed scalar formula is impossible;
- C180: independently corrected scalar large-deviation functional and strict concavity.

New this run:
- **C182 PROVED:** global one-parameter partial-lift optimization collapses to the unique scalar root `ell=s log(s) ell'`;
- **C183 PROVED:** `12.78437096209 < alpha_PL^* < 12.78437096216`;
- **C184 PROVED:** whp UNSAT at `alpha_U=12.78437096216`, new width `10.61241096216`;
- **R14-AUDIT-R15-I0076-PR1-05 = PASS**.

Still OPEN:
- exact `alpha_c(-1)`;
- exact `alpha_c(kappa)` for every `kappa<0`;
- equality with the full-RSB candidate;
- a rigorous second-full or higher lifted endpoint near the source's numerical `12.32/12.29`;
- matching sharp SAT and UNSAT bounds.

# 14. Failed-route / obstruction ledger

New exact obstruction:

**The 2013 one-parameter partial-lift family is globally exhausted.**
Its best possible upper endpoint is trapped above `12.78437096209`.
No amount of finer scalar meshing, optimizing `c`, or polishing the C181 stationary point can produce a material improvement.

The following remain non-rigorous for the bracket:
- replica/full-RSB predictions;
- stationarized fl-RDT table decimals without exact validation;
- numerical equality of a modulo-m inequality;
- algorithmic thresholds.

# 15. Exact checker

Checker:
`artifacts/R14/2026-09-16T18-54-10Z_r14-c182-partial-lift-extremal_checker.py`.

Executed output:
`artifacts/R14/2026-09-16T18-54-10Z_r14-c182-partial-lift-extremal_checker_output.txt`.

Output SHA-256:

`88f58d1def31611c2aede28a960ee2d0cf0fec04dfa867034e5d292ff3283f63`.

The finite core uses exact `fractions.Fraction` arithmetic. It certifies:

- Gaussian normalization enclosures;
- strict decrease of `K=L^2 k'` over a compact rational cover of `[0,1]`;
- `K(0)>0>K(1)`;
- opposite exact signs of `g` at the two root-bracketing rationals;
- the rational interval for `alpha_PL^*`;
- the new exact bracket width.

The stationary identities and global-extremum argument are written in full above; they are not delegated to the checker.

# 16. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  source:
    original: "Gardner 1988, The space of interactions in neural network models"
    rigorous_navigation:
      - "arXiv:1306.3980"
      - "arXiv:2010.15811"
      - "arXiv:2312.16531"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  metric: "rigorously certified whp bracket width alpha_U-alpha_L"
  before:
    alpha_L: "54299/25000 = 2.17196"
    alpha_U: "12784371/10^6 = 12.784371"
    width: "10.612411"
  after:
    alpha_L: "54299/25000 = 2.17196"
    alpha_U: "1278437096216/10^11 = 12.78437096216"
    width: "132655137027/12500000000 = 10.61241096216"
  status: PARTIAL
  unchanged_count: 0
  exact_evidence:
    - "R14-C182 global partial-lift extremal characterization"
    - "R14-C183 alpha_PL^* exact rational enclosure"
    - "R14-C184 rigorous whp UNSAT endpoint"
    - "checker SHA256 88f58d1def31611c2aede28a960ee2d0cf0fec04dfa867034e5d292ff3283f63"
  audit_ids:
    - "R14-AUDIT-R15-I0076-PR1-05=PASS"
  access_limits:
    - "literal row-by-row read of the complete ~780-row intake corpus is connector-truncated / incomplete"
```

# 17. Next attack

Do **not** spend the next run shaving more digits off the partial-lift scalar. C183 proves that route is exhausted.

The next R14 run should attack the `2-sfl RDT` level at `kappa=-1` in arXiv:2312.16531. The concrete target is not the table decimal `12.32`; it is an exact sufficient UNSAT certificate at some conservative rational value, for example `alpha=12.4` or `12.5`, obtained only after:

1. deriving the exact second-full finite-level comparison functional from the theorem with its correct sign/limit order;
2. identifying which stationarity relations are theorem hypotheses versus numerical observations;
3. replacing every numerical Gaussian expectation by directed rational/interval bounds;
4. proving the relevant global optimization direction instead of checking only a stationary tuple.

That route is capable of materially shrinking the bracket. The one-parameter 2013 route no longer is.

**NO EXACT-CAPACITY CLOSURE CLAIM.**
