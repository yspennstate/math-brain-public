Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no model selector or reasoning-effort selector; I do not claim otherwise. **NO MOVEMENT: certified interval width `0.033614007999972411... -> 0.033614007999972411...`. Section-B moves tried: 22 (read the failures), 27 (swap the quantifiers), 16 (compute every small case / inspect the exact discrete outputs).**

Problem/source: Václav Chvátal and David Sankoff, “Longest common subsequences of two random sequences,” *Journal of Applied Probability* 12(2) (1975), 306–315. Target: determine exactly
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid fair binary strings.

Run ID: `20260916_2114Z_lowerprecision_6b2e`.

Status of outside problem: **OPEN**. Status of this run: **PARTIAL / NO METRIC MOVEMENT**.

## 1. Metric

Retain the previous R17-C010 interval
\[
L=0.792665992,
\qquad
U=\frac{173228576586520}{209648759000007}
=0.826279999999972411\ldots.
\]
Thus
\[
W=U-L
=\frac{880891882776315417257}{26206094875000875000000}
=0.033614007999972411\ldots.
\]

This run does **not** alter either endpoint. The lower-endpoint investigation below identifies an artifact-reproducibility obligation, not a refutation of the published theorem. Until the actual production-run integer/scale is recovered or the source claim is independently invalidated, the published `0.792665992` remains the retained source-certified lower endpoint.

## 2. Continuity / repository / source pass

Before research I read the required private-repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R17 report `runs/R17/20260916_2015Z_slackopt_51ac.md`, the current R18 folder/newest closure report, and the historical intake entry for the binary-LCS target.

Fresh dated source checks on 2026-09-16/17 confirm:

- Tiskin, arXiv:2212.01582v2, still treats the exact binary constant as unresolved;
- Heineman--Miller--Reichman--Salls--Sárközy--Soiffer, arXiv:2407.10925 / ISIT 2025, still states the lower bound `0.792665992` and the exact constants as open;
- Lember--Sova, *Scandinavian Journal of Statistics* 53 (2026), DOI `10.1111/sjos.70086`, studies a pairwise-Markov model and calls the iid Chvátal--Sankoff constant unknown.

No independent-Bernoulli matching substitution is used anywhere in this run.

## 3. Move 22 — read the failures: audit the lower-bound artifact, not just the decimal

The public repository `Statistics-of-Subsequences/PaperMaterials` is the code repository linked from Heineman et al. Its binary code computes an integer `min_change`, sets

`min_change_d = min_change / FIXED_POINT_SCALE`,

and prints the binary lower bound
\[
B=\frac{2\,\texttt{min\_change\_d}}{1+\texttt{min\_change\_d}}.
\]
Therefore, if `m=min_change` and `S=FIXED_POINT_SCALE`, the exact rational value represented by this formula is
\[
\boxed{B(m,S)=\frac{2m}{S+m}.}
\tag{C011.1}
\]

The current public source comments that for string length at least 19 the preferred fixed-point scale is `2^24=16,777,216` to avoid overflow, while for consistency with Lueker the checked-in default remains `25,000,000`. The public result tables are described as rounded **down** to six decimal places; however, the headline/abstract lower endpoint is reported to nine decimals as `0.792665992`, and I found no public production-run log storing the actual length-21 `min_change` and scale that generated those nine digits.

The public repository currently exposes one `main` branch and no release artifact containing such a run log. The external-memory source history also leaves the checked-in length parameter at 13 rather than preserving a length-21 production configuration. This is a reproducibility gap, not proof that the mathematical result is wrong.

### R17-C011 — exact conditional inverse-output reconstruction

**STATUS: PROVED as a finite conditional statement. It does not assert which production-run scale the authors actually used.**

Let
\[
d=\frac{792665992}{10^9}
\]
and let
\[
I_d=\left[d-\frac1{2\cdot10^9},\ d+\frac1{2\cdot10^9}\right)
\]
be its nine-decimal round-to-nearest cell. Since `B(m,S)` is strictly increasing in integer `m`, the possible `m` values are determined exactly by
\[
\frac{d_-S}{2-d_-}\le m<\frac{d_+S}{2-d_+}.
\]

The exact checker proves:

1. For `S=2^24`, the **unique** integer whose exact bound lies in `I_d` is
   \[
   m=11,014,954.
   \]

2. For `S=2^25`, the unique integer is
   \[
   m=22,029,908,
   \]
   giving the same exact rational bound.

3. In either power-of-two case the exact bound is
   \[
   \boxed{
   B_*=\frac{11014954}{13896085}
   =0.7926659918962787\ldots
   }
   \]
   and hence
   \[
   d-B_*
   =\frac{36033}{347402125000000}
   \approx1.0372130\times10^{-10}>0.
   \]
   Thus **if** the nine-digit headline came from direct round-to-nearest of a power-of-two-scale program value, the displayed decimal would be rounded upward by about `1.0e-10` relative to that exact rational program value.

4. For the checked-in default scale `S=25,000,000`, **no integer `m`** gives an exact `B(m,S)` in the nine-decimal rounding cell of `0.792665992`. The neighboring exact values are
   \[
   B(16,413,560,25,000,000)=\frac{820678}{1035339}
   =0.792665977037\ldots,
   \]
   \[
   B(16,413,561,25,000,000)=\frac{32827122}{41413561}
   =0.792666006190\ldots.
   \]

This exhausts the inverse problem for the three fixed-point scales explicitly mentioned by the public code.

**Interpretation restriction.** C011 is not a counterexample to Heineman et al. The actual production-run scale, `min_change`, and any additional conservative post-processing are not preserved in the artifacts I found. A paper theorem cannot be invalidated merely because a public code snapshot does not reproduce its displayed rounding convention. The correct next obligation is to recover the exact production certificate.

## 4. Move 27 — swap the quantifiers

Instead of asking “does the public code approximately reproduce `0.792665992`?”, I asked the discrete inverse question:

> For each explicitly documented fixed-point scale `S`, **which integer `m`, if any, can produce a bound that rounds to the reported nine-digit decimal?**

Because `m` is integral and `B(m,S)` is monotone, this turns a vague numerical-reproducibility question into a finite exact arithmetic problem. C011 is the complete answer for the documented scales.

This route did not move the metric, but it identifies precisely what data would settle the lower endpoint independently: a production log or certificate containing the actual `(S,m)` pair for the length-21 run, together with the source theorem mapping that pair to a lower bound.

### R17-O012 — lower-endpoint certificate recovery

**STATUS: OPEN.** Recover one of:

- the original length-21 run's exact `FIXED_POINT_SCALE` and final `min_change`;
- a preserved vector/certificate from which they can be recomputed;
- or an independent exact rerun at the same parameters.

Until then, C011 remains a conditional reproducibility warning only.

## 5. Move 16 — compute the exact discrete outputs and inspect the sequence

The checker enumerates the only integer candidates in the nine-decimal inverse cells rather than evaluating floating-point approximations. This exposes a useful scale diagnostic:

- the two recommended power-of-two scales are perfectly compatible with the reported **rounded** nine-digit number, but their underlying exact rational is slightly smaller;
- the checked-in default scale `25,000,000` is incompatible with the reported nine-digit number under direct round-to-nearest.

This means the nine-digit headline cannot be independently certified merely by reading the current default constants and `printf` format. That is the precise failure mode found in this route.

## 6. 2026 extremal-alignment theorem: exact iid-binary reduction

I also tested whether the 2026 Lember--Sova extremal-alignment/entropy route could improve the current iid-binary endpoint.

A 2026 University of Tartu thesis by William Undrits, supervised by Joonas Sova, explicitly says that its proof structure follows the Lember--Sova article but that it corrected some inaccuracies in the original article; it identifies the main correction as proving its Theorem 1, which is needed in the proof of Theorem 2. I therefore used the corrected theorem statement rather than importing the journal mechanism uncritically.

The corrected Theorem 2 states
\[
H\le2h(\gamma)+\gamma h(\alpha^*)+
\bigl(2-\gamma-((\alpha\gamma)\vee0)\bigr)\log_2(K-1).
\tag{E}
\]
For independent iid fair binary strings,
\[
K=2,\quad H=2,\quad q_x=q_y=\frac12.
\]
For every `gamma` in `(1/2,1)`, its two auxiliary proportions are
\[
\alpha_1=1-\frac1{2\gamma}<\frac12,
\qquad
\alpha_2=\frac1{2\gamma}>\frac12,
\]
so by the theorem's piecewise definition
\[
\alpha^*=\frac12.
\]
Also `log_2(K-1)=log_2(1)=0` and `h(1/2)=1`. Therefore (E) reduces exactly to
\[
\boxed{2\le2h(\gamma)+\gamma.}
\tag{C013}
\]

That is the classical entropy inequality whose upper root gives the original Chvátal--Sankoff-scale bound near `0.866595`, far weaker than Lueker/R17's current `0.8262799999999724...`. Thus the 2026 extremal-alignment theorem does not improve the fixed iid-binary metric in its symmetric specialization.

This also explains why the new 2026 paper can be genuinely useful for pairwise-Markov/asymmetric models while leaving the hard iid-fair binary interval unchanged.

## 7. Exact checker / evidence

No Monte Carlo.

Executed checker:

- `artifacts/R17/20260916_2114Z_lowerprecision_6b2e_checker.py`
- executed output `artifacts/R17/20260916_2114Z_lowerprecision_6b2e_checker_output.txt`
- local output SHA-256 `bd13d4e693f8698e782b6d57cc4bad68a4032aa8b161053de9bd55d6cc7cf568`

The checker verifies C011 exactly and regression-checks the iid-binary `alpha* = 1/2` specialization. It ends `ALL_EXACT_CHECKS_PASS`.

## 8. R18 audit duty

The newest visible R18 package is the already closed/packaged source-matching I0080 result. It already records the distinct R17 audit and the independent P26 audit. No newer R18 mathematical package requiring a fresh R17 audit was present at this run's continuity pass, so I did not duplicate an audit merely to generate activity.

## 9. Model / scheduler interface

Unchanged: the exposed scheduler interface provides prompt/title, timing/schedule, enablement and timing mode, but no model selector or reasoning-effort field. `GPT-6 / maximum` therefore remains requested prompt text, not verified runtime configuration. Enforcing it would require product/API support for those fields or an owning workspace interface that exposes them.

The historical P26 `You cannot modify this task` failure is ownership/context-specific; the repository records a later authorized context in which P26 was modified successfully. The legitimate workaround is the owning account/workspace or platform support, not a permission bypass or duplicate task. No scheduler modification was attempted here.

## 10. Next attack

This run found an exact certificate-reproducibility obstruction rather than another asymptotic lemma. The next highest-value routes are now sharply separated:

1. **Lower side:** recover the actual Heineman length-21 `(scale,min_change)` production certificate before trying to claim any additional lower digit.
2. **Upper side:** regenerate Lueker's actual h=8 positive witness and certify its real `Rhat` margin with directed rounding; the previous C010 threshold-only amplification has already been essentially exhausted.
3. Do **not** spend another run on the symmetric 2026 entropy theorem; C013 shows it collapses to the old `0.866595`-scale inequality for iid fair binary strings.

Because the previous run moved the metric and this run does not, the visible unchanged streak after the reset is `1`.

## 11. Claim ledger

- R17-C001 through R17-C010: retained at prior audited scopes.
- **R17-C011:** exact conditional inverse-output reconstruction for the documented fixed-point scales — PROVED; does not identify the actual production-run scale.
- **R17-O012:** recover exact Heineman length-21 lower-bound certificate — OPEN.
- **R17-C013:** corrected extremal-alignment entropy theorem specializes to `2 <= 2 h(gamma)+gamma` in the iid fair-binary model — PROVED as a derivation from the cited theorem; no metric improvement.
- Exact `gamma_2`: OPEN.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R17
  source:
    authors: "Václav Chvátal; David Sankoff"
    year: 1975
    target: "exact binary Chvátal-Sankoff constant gamma_2"
  metric:
    name: "width U-L of the best rigorously certified interval containing gamma_2"
    before_exact: "880891882776315417257/26206094875000875000000"
    before_decimal: "0.033614007999972411..."
    after_exact: "880891882776315417257/26206094875000875000000"
    after_decimal: "0.033614007999972411..."
    movement: "none"
  endpoints:
    lower_retained: "0.792665992 (source-certified; exact production artifact not independently reconstructed)"
    upper: "173228576586520/209648759000007"
  status: PARTIAL
  source_problem_status: OPEN
  unchanged_count: 1
  methods_this_run: [22, 27, 16]
  exact_evidence:
    - "artifacts/R17/20260916_2114Z_lowerprecision_6b2e_checker.py @ 050babea42f04996d5b2a79343247272b36925a7"
    - "artifacts/R17/20260916_2114Z_lowerprecision_6b2e_checker_output.txt @ c496e4f91b1c0f6c75c8dd5324ae592ac2118290"
    - "local executed output sha256 bd13d4e693f8698e782b6d57cc4bad68a4032aa8b161053de9bd55d6cc7cf568"
  audit_ids:
    - "no new R18 package requiring an audit; retained completed R17/P26 audits"
  limitations:
    - "C011 is conditional on a documented fixed-point scale and does not identify the authors' actual l=21 production parameters."
    - "The published lower endpoint is retained; no refutation is claimed."
    - "C013 is a specialization of the corrected 2026 theorem, not a new iid upper bound."
```

No Gmail, Drive, email, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-file edit was made.
