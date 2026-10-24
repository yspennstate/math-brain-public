Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated applied-model / reasoning-effort receipt is available to this run, so I do not claim otherwise.

# NM13-12 progress-universality — quantitative radial-margin universality for the negative spherical perceptron

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12`  
Progress root: `proofnet24/NM13-12/progress-universality/`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Concrete application: T03, negative spherical perceptron at `kappa=-1`  
Status: **PARTIAL / NEW THEOREM PROVED / T03 SOURCE STILL OPEN**

## 1. Compact handoff and exact difference from the old assignment

The later `PROGRESS20_2026-09-20.md` owner directive replaces NM13-12's preceding intake/admission loop with a shared-theory assignment: recover the actual P12 universality state, prove an unposted quantitative universality extension, and demonstrate it on a concrete unresolved probability claim. I preserve the older NM13-12 admission-screen history but do not continue it here. There was no earlier report under the new `progress-universality/` root on current `master` when this run began.

This run does **not** reopen or repackage any posted row-submatrix, kernel, ReLU, or zero-margin Ising-perceptron result. `POSTED.md` explicitly excludes those subjects from fresh assignments. The theorem below concerns a different object: hard feasibility of a spherical perceptron under row-radius perturbations, with an explicit finite-`N` probability comparison and `O(sqrt(log N/N))` margin distortion. No least-singular-value minimum over row subsets appears in the theorem.

## 2. Recovered P12/universality proof state and unresolved successor

The newest retained P12 report is

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T06-25-12Z__run-report.md`.

Its frozen theorem is mathematically supported but protocol-open because one required independent full-package audit remained missing. The theorem's exact mathematical assumptions are:

- `F in {R,C}`, with `d_R=1`, `d_C=2`;
- iid centered variance-one entries with densities `f_m`;
- one fixed integer `q>=1` and one fixed finite `M` with
  `sup_m ||f_m^{*q}||_infinity <= M`;
- `N_m/m -> gamma>1`;
- moderate-surplus condition `k_m log m=o(m)`.

Under those hypotheses the package proves

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`.

There is **no fourth-moment assumption** in that frozen theorem and no positive-moment assumption beyond variance normalization. The old bounded-fourth-moment/RLogLCD program is an incomplete historical route, not a hidden hypothesis.

The nearest explicitly recorded unresolved successor is broader triangular iid-entry universality under smooth/bounded-fourth-moment assumptions **without a uniform microscopic finite-convolution smoothing bound**. P12 itself correctly left that outside the frozen theorem rather than claiming it.

A separate already-written spherical-row theorem in `paper19/parts/rotinv_universality.tex` transfers the **exponential least-singular-value base** through diagonal radial weights when the maximum logarithmic radius distortion is `o_P(m)`. That result is useful conceptual ancestry, but it is still a row-submatrix singular-value theorem. The theorem below is different in both scale and event: it transfers a hard margin-feasibility probability, needs only relative radius error `o(1)`, and gives an explicit finite-size coupling error.

## 3. T03 source-exact state and coordination

The T03 source model is frozen as follows. Let

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, and seek `sigma` with

`||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)`, `1<=a<=M`.

Writing `x=sigma/sqrt(N)`, this is exactly

`x in S^{N-1}`, `Gx >= -1`.

The strongest repository-supported rigorous bracket entering this run is

`alpha_L = 630297437506/10^11 = 6.30297437506`,

`alpha_U = 1278437096216/10^11 = 12.78437096216`,

with width

`W = 64813965871/10^10 = 6.48139658710`.

The lower endpoint is Montanari--Zhong--Zhou's rigorous LP success theorem after exact model matching, using `delta_lin(kappa)=1/Phi(kappa)`. The upper endpoint is the rigorously optimized Stojnic-2013 partially lifted Gaussian-comparison family recovered in the R14 chain.

### Coordination with NM13-07

The current NM13-07 report

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-full2-two-scalar-reduction.md`

proves a complementary exact reduction of the second-full lifted stationarity equations to two scalars `(p,B)`. Its `alpha=12.75` point has a strong positive numerical comparison margin, but the compact Gaussian quadrature/root enclosure is not yet rigorous, so NM13-07 correctly claims no source-bracket movement.

I do **not** duplicate that root-certification route. The theorem below is orthogonal: it shows that any strict Gaussian SAT or UNSAT theorem at a nearby margin transfers to the row-normalized/fixed-radius disorder, with an explicit radius-concentration loss. Consequently, if NM13-07 later rigorously certifies its `12.75` Gaussian witness, the same density transfers automatically to the normalized-row model without a second high-dimensional proof.

### Coordination with NM13-03

The intended new root `proofnet24/NM13-03/progress-perceptron-theory/` was still absent from current `master` when checked in this run; repository search returned no post-LIVE20 report there. I therefore did not wait for an unavailable peer result and did not edit NM13-03 files. The theorem below is left as a self-contained reusable comparison lemma for that worker's future Gaussian-comparison route.

## 4. First falsification: blanket iid-entry universality is false at kappa=-1

Before proving a transfer theorem, test the strongest tempting statement: does the T03 satisfiability threshold at `kappa=-1` depend only on mean zero and variance one of iid entries?

No.

Let `B` be any `M x N` iid Rademacher matrix, `B_ai in {+1,-1}`. Pick any coordinate vector `x=e_j`. Then `||x||_2=1` and for every row

`(Bx)_a = B_aj in {-1,+1} >= -1`.

Therefore

`SAT(B,-1)` holds **deterministically for every M,N**.

So there cannot be unrestricted Lindeberg universality from Gaussian rows to all centered variance-one iid entries for this exact hard-margin event. The obstruction is a localized coordinate witness and survives arbitrarily large aspect ratio. This also explains why an informal statement that Gaussian randomness can be replaced by broad iid randomness cannot be used here without an anti-localization or atom-exclusion hypothesis.

This falsification materially narrows the correct universality class: preserve the Gaussian angular law and perturb only radii, or impose enough geometry to exclude coordinate witnesses.

## 5. New mechanism theorem: deterministic radial-margin sandwich

For a real `M x N` matrix `A` and `kappa<0`, define

`SAT(A,kappa) := { exists x in S^{N-1} such that (Ax)_a >= kappa for every a }`.

### Theorem NM12-RMU-1 (pathwise radial-margin comparison)

Let `Y` be any `M x N` matrix and let

`X = S Y`, `S=diag(s_1,...,s_M)`,

with

`1-delta <= s_a <= 1+delta`, `0<delta<1`.

Then for every `kappa<0`, pathwise,

`SAT(Y, kappa/(1+delta))`
`  subset SAT(X,kappa)`
`  subset SAT(Y, kappa/(1-delta))`.

#### Proof

Fix `x in S^{N-1}` and a row value `y=(Yx)_a`.

For the left inclusion, suppose `y >= kappa/(1+delta)`. If `y>=0`, then `s_a y>=0>kappa`. If `y<0`, multiplication by a larger positive number makes it more negative, so the worst permitted multiplier is `1+delta`; hence

`s_a y >= (1+delta)y >= kappa`.

This holds for every row, so any witness for `SAT(Y,kappa/(1+delta))` is a witness for `SAT(X,kappa)`.

For the right inclusion, suppose `s_a y>=kappa`. Then

`y >= kappa/s_a`.

Because `kappa<0` and `s_a>=1-delta`,

`kappa/s_a >= kappa/(1-delta)`.

Thus every witness for `SAT(X,kappa)` also witnesses `SAT(Y,kappa/(1-delta))`. QED.

### Why this is a genuine extension rather than a restatement

The old row-weight theorem for submatrix singular values uses the coarse multiplicative bound

`min s_a * smin(Y_T) <= smin((SY)_T) <= max s_a * smin(Y_T)`

and asks only for logarithmic errors `o(m)` because its observable is itself exponentially small. Here the observable is a **fixed hard margin**, so exponential radial control is useless. The new theorem works at the much finer relative-radius scale `delta=o(1)` and converts it into an additive margin perturbation of size `|kappa| delta`. It is a feasibility comparison, not a singular-value comparison.

## 6. Quantitative Gaussian-to-spherical coupling

Let `g_a iid N(0,I_N)`. Write the polar decomposition

`g_a = R_a theta_a`,

where `R_a=||g_a||_2` and `theta_a` is uniform on `S^{N-1}`; for Gaussian rows, `R_a` and `theta_a` are independent. Define fixed-radius rows

`Y_a = sqrt(N) theta_a`.

Then

`G = S Y`, `s_a=R_a/sqrt(N)`.

Let

`E_delta = { max_{a<=M} |R_a/sqrt(N)-1| <= delta }`.

Applying NM12-RMU-1 with `X=G` gives, on `E_delta`,

`SAT(G,(1-delta)kappa)`
`  subset SAT(Y,kappa)`
`  subset SAT(G,(1+delta)kappa)`.

Hence

`P_G[SAT((1-delta)kappa)] - P(E_delta^c)`
` <= P_Y[SAT(kappa)]`
` <= P_G[SAT((1+delta)kappa)] + P(E_delta^c)`.

This is an exact finite-`N` probability comparison.

### Proposition NM12-RMU-2 (explicit radius error)

For `0<delta<=1`,

`P(E_delta^c) <= 2 M exp(-N delta^2/4)`.

#### Proof

For `R^2 ~ chi_N^2`, Laurent--Massart gives, for `t>0`,

`P(R^2-N >= 2 sqrt(Nt)+2t) <= exp(-t)`,

`P(N-R^2 >= 2 sqrt(Nt)) <= exp(-t)`.

Take `t=N delta^2/4`.

If `R >= sqrt(N)(1+delta)`, then

`R^2-N >= N(2delta+delta^2)`

and

`N(2delta+delta^2) >= N delta + N delta^2/2`
` = 2 sqrt(Nt)+2t`.

If `R <= sqrt(N)(1-delta)`, then

`N-R^2 >= N(2delta-delta^2) >= N delta = 2 sqrt(Nt)`

for `0<delta<=1`. Each tail is therefore at most `exp(-N delta^2/4)`. A union bound over `M` rows proves the claim. QED.

For `M=O(N)`, choose

`delta_N = sqrt(12 log N / N)`.

Then, once `delta_N<1`,

`P(E_delta_N^c) <= 2 M N^{-3} = O(N^{-2})`,

and the induced margin perturbation at `kappa=-1` is exactly

`delta_N = O(sqrt(log N/N))`.

This gives a quantitative, summable finite-size universality error rather than only a qualitative `o_P(1)` radial statement.

## 7. General radial-disorder corollary

The argument never used independence of the radii from the directions after the pathwise sandwich.

### Corollary NM12-RMU-3

Let

`A_a = r_a theta_a`,

where `theta_a` are iid uniform on `S^{N-1}`, the positive radii `r_a` may be dependent on the directions and on one another, and

`epsilon_N := max_{a<=M} |r_a/sqrt(N)-1| ->_P 0`.

For each fixed `kappa<0`, any Gaussian SAT theorem that holds uniformly at one fixed **harder** margin `kappa+eta` and any Gaussian UNSAT theorem that holds at one fixed **easier** margin `kappa-eta` transfer to `A` at margin `kappa`.

More explicitly, if for some fixed `eta>0`,

`P[SAT(G,kappa+eta)] -> 1`,

then `P[SAT(A,kappa)] -> 1`; and if

`P[SAT(G,kappa-eta)] -> 0`,

then `P[SAT(A,kappa)] -> 0`.

#### Proof

On `{epsilon_N <= delta}`, rescale by `sqrt(N)` and apply NM12-RMU-1. For all sufficiently large `N`, choose `delta<eta/|kappa|` (or simply use the exact factors `(1+-delta)kappa`), so the Gaussian comparison margin lies between `kappa` and the fixed margin supplied by the hypothesis. Monotonicity of `SAT(A,kappa)` in `kappa` completes the two implications; the probability of the complement event tends to zero. QED.

Thus the distributional class is strictly broader than Gaussian rows: coordinates within a row may be highly dependent, and no iid-entry density or finite-convolution assumption is needed. What is preserved is the spherical angular law plus vanishing relative radius distortion.

## 8. Concrete unresolved probability application: fixed-radius negative spherical perceptron

Define the **row-normalized / fixed-radius negative spherical perceptron** by iid rows

`Y_a = sqrt(N) theta_a`, `theta_a ~ Unif(S^{N-1})`,

and ask for `x in S^{N-1}` with

`Y_a . x >= -1`, `a<=floor(alpha N)`.

This is not the original T03 Gaussian source, so it does not close T03. It is, however, a concrete non-Gaussian hard-feasibility model at the exact same sphere radius and margin, and it was not supplied by the posted zero-margin Ising or row-submatrix results.

### Theorem NM12-T03-RADIAL (same current rigorous bracket for fixed-radius disorder)

Let `alpha_c^sph(-1)` denote the fixed-radius model's asymptotic SAT threshold in the usual lower/upper threshold sense. Then the currently certified Gaussian T03 endpoints transfer unchanged:

`6.30297437506 <= alpha_c^sph(-1) <= 12.78437096216`.

Equivalently:

- for every `alpha < 1/Phi(-1)`, the fixed-radius model is SAT with probability tending to one;
- for every `alpha > 12.78437096216`, it is UNSAT with probability tending to one.

The theorem does not assert existence of a sharp threshold or equality of the two endpoints.

### Proof: lower endpoint

Fix

`alpha < 1/Phi(-1)`.

By continuity of `Phi`, choose `eta>0` so small that

`alpha < 1/Phi(-1+eta)`.

Montanari--Zhong--Zhou's rigorous LP theorem applies to the exact Gaussian spherical perceptron and yields Gaussian SAT with probability tending to one at the **harder** fixed margin `-1+eta`.

Take `delta_N=sqrt(12 log N/N)`. Then `delta_N->0` and `P(E_delta_N^c)=O(N^-2)`. For all large `N`, `delta_N<eta`. Since a witness at `-1+eta` is also a witness at `-1+delta_N`,

`P[SAT(G,-1+delta_N)] -> 1`.

The Gaussian-to-spherical inclusion on `E_delta_N` is

`SAT(G,-1+delta_N) subset SAT(Y,-1)`.

Therefore

`P[SAT(Y,-1)] -> 1`.

Taking `alpha` arbitrarily below `1/Phi(-1)` gives the lower threshold statement, and in particular the fleet's exact rational endpoint `6.30297437506`. QED for the lower side.

### Proof: upper endpoint

Let

`U_* = 12.78437096216`

be the retained rigorous upper endpoint from the globally optimized Stojnic-2013 partially lifted family, and fix `alpha>U_*`.

The R14 C180--C184 chain gives more than a pointwise statement at `kappa=-1`: because `alpha` is strictly above the global partial-lift threshold, there exists a **fixed finite comparison parameter** `c>0` for which the corrected Stojnic Gaussian-comparison objective has a strictly negative maximum at `kappa=-1`.

For fixed `c`, the C180 derivation writes the `kappa`-dependent scalar term as

`J_{kappa}(gamma)`
` = -gamma + (alpha/c) log E exp{ -c (Z+kappa)_+^2/(4 gamma) }`,

`gamma>0`, `Z~N(0,1)`,

plus a spherical term independent of `kappa`. We need only show that a strict negative maximum persists for a small change of `kappa`.

For every compact `kappa`-interval around `-1` and every compact `gamma`-interval bounded away from zero, the integrand is continuous and bounded by one, so dominated convergence gives uniform continuity of the expectation and hence of `J_kappa(gamma)`.

The two `gamma` boundaries cannot hide a new maximizer under a small `kappa` perturbation:

- as `gamma->infinity`, `J_kappa(gamma)->-infinity` uniformly on a compact `kappa`-interval because the logarithmic term is nonpositive;
- as `gamma downarrow 0`, dominated convergence gives
  `E exp{-c(Z+kappa)_+^2/(4gamma)} -> P(Z+kappa<=0)=Phi(-kappa)`.
  At the chosen strict UNSAT witness the compactified source objective is already strictly negative at this boundary as part of the globally certified `max<0`; continuity of `Phi(-kappa)` preserves a negative gap nearby.

Hence the full compactified maximum is continuous in `kappa` at `-1`. There is therefore some `eta>0` such that the same fixed comparison witness remains strictly negative at the **easier** margin

`kappa=-1-eta`.

The same Stojnic Gaussian comparison/concentration theorem used in C180--C184 then yields

`P[SAT(G,-1-eta)] -> 0`.

Again take `delta_N=sqrt(12 log N/N)`. For all large `N`, `delta_N<eta`, and

`-1-delta_N > -1-eta`.

A harder-margin SAT event is contained in an easier-margin SAT event, so

`SAT(G,-1-delta_N) subset SAT(G,-1-eta)`.

On `E_delta_N`, NM12-RMU-1 gives

`SAT(Y,-1) subset SAT(G,-1-delta_N)`.

Therefore

`P[SAT(Y,-1)]`
` <= P[SAT(G,-1-eta)] + P(E_delta_N^c)`
` -> 0`.

This proves the upper threshold statement for every `alpha>U_*`. QED.

### A useful automatic transfer for NM13-07

NM13-07's current `12.75` second-full point is numerical only, so it is not inserted into any bracket here. But if that worker later certifies a strict Gaussian comparison witness at `alpha=12.75`, the same compact-margin argument above immediately gives fixed-radius UNSAT at `12.75` as well. No new `N`-dimensional random-matrix proof is then needed; only the already-proved `O(sqrt(log N/N))` radial coupling is used.

## 9. Parent metric versus demonstrated theory gain

### Applied parent claim (T03 Gaussian source)

Before:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

After:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**NO SOURCE-LEVEL MOVEMENT is claimed.** The original T03 source is Gaussian and its exact threshold remains open.

### Demonstrated theory gain

The new theorem expands a rigorously controlled hard-margin feasibility result from Gaussian rows to:

1. iid fixed-radius spherical rows `sqrt(N) theta_a` with the **same current rigorous T03 bracket**;
2. more generally, spherical directions with arbitrary positive radii satisfying
   `max_a |r_a/sqrt(N)-1|=o_P(1)`, even when radii depend on directions;
3. an explicit Gaussian-to-fixed-radius comparison with margin distortion
   `delta_N=sqrt(12 log N/N)` and coupling failure `O(N^-2)` for `M=O(N)`.

This is a strict distributional-class extension and a quantitative rate statement. It is not a source-level T03 bracket improvement.

The Rademacher construction simultaneously proves an exact boundary: the extension cannot be promoted to all centered variance-one iid entries at `kappa=-1` without additional anti-localization/anti-atom hypotheses.

## 10. Essential executed checker/output

Created and executed:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_radial_margin_check.py`

Archived output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_radial_margin_check.out`

The code checks exact rational bracket arithmetic, evaluates the explicit `delta_N`/union-bound rate at three dimensions, and verifies the Rademacher coordinate-witness obstruction. The archived output ends

`RADEMACHER_KAPPA_MINUS1_COORDINATE_WITNESS_PASS`

and

`ALL_CHECKS_PASS`.

This checker is only a sanity certificate for finite arithmetic. The main radial sandwich and T03 transfer are proved analytically above.

## 11. Current source / prior-art boundary

Primary/current references checked in the transition and this run include:

- El Alaoui--Sellke, arXiv:2010.15811: exact Gaussian disorder, exact sphere radius `sqrt(N)`, negative-margin algorithmic pure states on radius `sqrt(qbar N)` rather than source closure at full radius;
- Stojnic, arXiv:1306.3980: negative spherical perceptron and rigorous Gaussian-comparison upper-bound machinery;
- Stojnic, arXiv:2312.16531: fully lifted RDT and numerical finite-level capacity calculations;
- Montanari--Zhong--Zhou, arXiv:2110.15824 / PTRF 2024: rigorous exact-model LP lower bound used for the retained Gaussian endpoint;
- Gerace--Krzakala--Loureiro--Stephan--Zdeborova, arXiv:2205.13303: a different perceptron universality theorem for random-label classification, proved for mixtures of homogeneous Gaussian clouds / minimum training loss, not this fixed-radius hard negative-margin satisfiability transfer.

A bounded search did not locate a theorem matching the exact finite-`N` radial hard-margin sandwich and the fixed-radius `kappa=-1` bracket application above. That search failure is **not** a novelty certificate.

## 12. Residual obstruction and next attack

The parent T03 bracket has not moved. The cleanest next use of this theory is not another generic universality lemma: it is to make the current Gaussian second-full improvement rigorous. The nonduplicating role for NM13-12 is to quantify **margin stability of a certified lifted comparison witness**—an explicit Lipschitz/modulus bound in `kappa` for the compactified Gaussian expectation—so that NM13-07's eventual interval root certificate automatically comes with a finite-`N` radial robustness window. If the Gaussian `12.75` certificate stalls, a second concrete route is to exploit fixed-radius angular geometry directly for a stronger comparison inequality and then transfer it back to Gaussian rows using the same radial sandwich in the opposite direction with an explicit margin buffer.

No claim of a Gaussian threshold improvement, exact fixed-radius threshold, or unrestricted iid universality is made.

```yaml
ledger_delta:
  worker: "NM13-12"
  assignment: "shared quantitative universality with concrete T03 application"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
    requested: "GPT-6 maximum"
  p12_state:
    theorem: "frozen finite-convolution submatrix universality"
    hypotheses: "centered variance-one iid densities; fixed q,M with sup ||f_m^{*q}||_infinity<=M; N_m/m->gamma>1; k_m log m=o(m)"
    unresolved_successor: "triangular smooth/B4 universality without uniform microscopic smoothing"
  parent:
    id: "T03"
    target: "Gaussian negative spherical perceptron, kappa=-1, exact radius sqrt(N)"
    metric: "certified bracket width"
    before:
      lower: "6.30297437506"
      upper: "12.78437096216"
      width: "6.48139658710"
    after:
      lower: "6.30297437506"
      upper: "12.78437096216"
      width: "6.48139658710"
    movement: "NO"
    status: "OPEN"
  theory_gain:
    theorem_id: "NM12-RMU-1/2/3 + NM12-T03-RADIAL"
    status: "PROVED / self-checked, pending later independent review"
    distribution_extension: "Gaussian -> fixed-radius spherical and o_P(1) relative radial perturbations with spherical directions"
    quantitative_rate: "delta_N=sqrt(12 log N/N), failure <=2 M N^-3=O(N^-2) for M=O(N)"
    application: "fixed-radius kappa=-1 perceptron inherits [6.30297437506,12.78437096216]"
    boundary: "blanket centered variance-one iid-entry universality is false: Rademacher coordinate witness"
  coordination:
    NM13-07: "complementary; consumes its exact two-scalar reduction only as future Gaussian witness source, does not duplicate root certification"
    NM13-03: "no post-LIVE20 progress-root report found on current master; reusable lemma recorded here, no peer edit"
  artifacts:
    checker: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_radial_margin_check.py"
    output: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_radial_margin_check.out"
  rejected_route:
    - "unrestricted iid-entry Lindeberg universality at kappa=-1; exactly refuted by Rademacher coordinate witness"
  next_attack: "explicit kappa-stability modulus for a certified second-full Gaussian witness, or angular comparison yielding a stronger fixed-radius bound transferable back with margin buffer"
```
