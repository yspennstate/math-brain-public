Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — GPT-6 maximum was requested, but the exposed scheduler/runtime has no model selector, reasoning-effort selector, or applied-effort telemetry, so I do not claim GPT-6 maximum. **NO MOVEMENT:** certified interval width `0.033613183721596843 -> 0.033613183721596843`. Methods tried: **#1, #20, #25**.

# R17 C031 — deficiency-filter intersection route; third unchanged run

Status of the outside problem: **OPEN**. Status of R17: **PARTIAL**.

## 1. Recovered state before doing new work

I read the current campaign/index state, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the controlling owner directive, the current R17 report, the latest neighboring R18 package, and the current intake/ownership lineage for the binary-LCS target. I did not restart from an older recurrence.

The newest prior R17 report is

`runs/R17/20260917_1216Z_refined_domination_c030_2f6d.md`.

It leaves the rigorous interval at

\[
\boxed{0.792665992\le \gamma_2\le 0.826279175721596843},
\qquad
\boxed{W=U-L=0.033613183721596843}.
\]

C029 and C030 were both no-movement runs after C028, so the entering consecutive-unchanged count was `2`.

No posted exclusion or conflicting ownership entry was found for R17. The newest R18 work is already a closed/package state rather than a neighboring live theorem that needs an R17 audit.

## 2. Current source check

Fresh source checks this run still find the binary Chvátal–Sankoff constant unresolved:

- Alexander Tiskin, arXiv:2212.01582, *The Chvátal-Sankoff problem: Understanding random string comparison through stochastic processes*, explicitly describes the binary coefficient as unresolved.
- George Heineman et al., arXiv:2407.10925, *Improved Lower Bounds on the Expected Length of Longest Common Subsequences*, describes exact Chvátal–Sankoff constants as open and gives the rigorous binary lower bound `0.792665992`.
- Ray Li, William Ren, and Yiran Wen, arXiv:2504.10425, treats generalized many-string constants and does not resolve the exact `d=2,k=2` value.
- George S. Lueker, JACM 56(3), 2009, remains the primary finite-state/Perron upper-bound source used here.

A bounded search for later work around Lueker domination/canonicity, Conjecture 3.19, and the C029 witness found no accessible source that closes the binary constant or supplies the deficiency-filter construction below. This is not a priority certificate.

## 3. #1 CHANGE THE CATEGORY — from one covering automaton to an intersection of subshifts

C030's useful structural observation was the deficiency surplus

\[
\Delta(L)=\operatorname{LCS}(P(L))-|L|.
\]

A saturated LCS collation cannot contain a contiguous deficient factor: a longer common subsequence inside that factor can be concatenated with the matches before and after it. Instead of replacing Lueker's successful canonical machine by the much weaker standalone refined-domination machine, I therefore changed category and treated the new information as a **forbidden-factor subshift to intersect with the existing canonical language**.

The smallest deficient minimal-match factors at total size eight include, in Lueker's `(c,l)` hook notation,

\[
(c,+2)(c,-2),\qquad (c,-2)(c,+2),\qquad c\in\{0,1\}.
\]

This suggests a small-memory product automaton: retain the h=8 canonical boundary state and a finite memory indicating whether the preceding minimal-match pair was a `+2` or `-2` hook (and, if needed under the complement quotient, its terminal bit), and reject exactly when the opposite hook with the same terminal bit completes one of these deficient factors.

The attraction of this construction is that it does not throw away the 6,419,109-state h=8 canonical operator that already produces the best R17 upper certificate. It tries to remove only paths which cannot belong to a saturated LCS collation.

I did **not** claim an improved endpoint from this product without its Perron certificate.

## 4. #25 COUNT THE SAME THING TWICE — exact proof that the proposed filter is nontrivial

Before paying for a full product Perron computation, I checked whether the h=8 canonical language already forbids those deficient factors automatically. If it did, the intersection idea would be vacuous.

It does not.

The exact checker reconstructs Lueker's h=8 transition rule directly from the DP/backtracking recurrence and performs a BFS only until the first deficient two-letter factor is found. It finds the accepted canonical path

\[
(0,4),\ (0,2),\ (0,-2).
\]

The last two hook letters generate

\[
\binom{1100}{0110},
\]

have list order `2`, and have exact LCS length `3`. Thus the factor is deficient, yet both transitions occur on an accepted path of the canonical h=8 machine.

The checker output records:

- only 12 base states had been processed when the witness was found;
- the exact packed source/mid/destination states are `4292935710`, `4278845193`, `4178181650`;
- `block_order=2`, `block_lcs=3`;
- `CANONICAL_MACHINE_ACCEPTS_DEFICIENT_LENGTH2_BLOCK=PASS`;
- `EXACT_FINITE_RECOVERY_CHECK_PASS`.

Artifacts:

- `artifacts/R17/20260917_1314Z_deficiency_filter_c031_exact_probe.cpp`
- `artifacts/R17/20260917_1314Z_deficiency_filter_c031_exact_probe_output.txt`

The source was created at commit `fc982064a894d18c003a5bea124d48aa99106bb6` and read back there. The executed output was created at commit `580fd024e04776da7c1977d895a3ee52044bd7a7` and read back there.

This proves only a finite language fact: the deficiency filter makes the accepted language strictly smaller. It **does not** prove that the Perron root decreases, because deleting transient or nondominant paths can leave the spectral radius unchanged.

## 5. #20 FIND WHY THE ALGORITHM FAILS — standalone refined domination is too weak, and strict language shrinkage is not enough

I explored two numerical diagnostics, neither used as a theorem endpoint.

First, I implemented the C030 refined-domination language directly as a finite forbidden-factor automaton and pushed the scalar history through `h=16`. Even after optimizing `z` coarsely, the best observed scalar upper diagnostic was about `0.8468`, still far above the certified h=8 canonical value `0.826279175721596843`. This says the C030 repair is useful as a convergence mechanism but, at accessible small histories, is not competitive as a replacement for the canonical machine.

Second, on a smaller canonical history where the full product is cheap, I intersected the canonical automaton with the length-two deficiency filter. The floating Perron diagnostic did not move to displayed precision. That identifies the exact danger: the removed deficient paths can exist while lying outside the Perron-dominant recurrent structure.

Accordingly, a full h=8 intersection is worth doing only if we inspect the dominant SCC/Perron support, rather than assuming that a strictly smaller accepted language gives a strictly smaller spectral radius.

I attempted a full local regeneration of the h=8 transition table for that product computation. It did not finish within this run's execution ceiling; the partial table is excluded from all claims and was not committed. No bound in this report depends on it.

## 6. Exact blocking statement

The tracked metric moves only if we obtain a deterministic endpoint below the current one (or a lower endpoint above the current lower bound). On the upper side the missing object is, concretely, a finite covering operator and positive exact witness satisfying

\[
\boxed{
A_{\rm new}(x,y)v\le \lambda v
\quad\text{and}\quad
\frac{\log(4xy)}{\log\lambda}
<0.826279175721596843.
}
\]

The deficiency-filter route has not yet supplied that second inequality.

## 7. What the existing routes lack

The route history since the last numerical movement now has a clear separation.

1. **More rounding / Perron-vector polishing of the same h=8 operator:** exhausted. Earlier exact Collatz brackets showed only microscopic room inside the fixed operator.
2. **Bivariate fugacity optimization:** produced C028's real movement, but subsequent work did not expose another certified parameter improvement of useful size.
3. **Lueker's scalar domination conjecture:** C029 found an exact binary counterexample, so that route cannot be used as stated.
4. **C030 refined domination:** repairs convergence conceptually, but the small-history operator is search-diagnostically much too weak to beat the present canonical certificate.
5. **Deficiency-filter intersection:** this run proves the filter is genuinely nonvacuous on the h=8 canonical language, but strict language shrinkage alone does not show spectral-radius shrinkage.
6. **h=9 canonical history:** remains computationally expensive; no exact h=9 table/witness has been recovered in the repository.
7. **Alternative balanced canonicalizations:** previous work isolated the missing locality/padding lemma; no proof of that lemma is available.

What a successful route must contain that the present routes do not is **a coverage-preserving exclusion that removes positive Perron mass from the dominant recurrent component**, together with an exact finite cone certificate. Merely finding more rejected paths is insufficient.

## 8. Simplest special case still unproved

The cleanest finite question left by this run is:

\[
\boxed{
\rho\!\left(B^{\Delta}_8(x_{028},y_{028})\right)
<
\rho\!\left(A_8(x_{028},y_{028})\right)?
}
\]

Here `A_8` is the existing C028 h=8 canonical operator at

\[
x_{028}=513401/1600000,\qquad y_{028}=513467/1600000,
\]

and `B_8^Delta` is the finite-memory product which additionally rejects the four deficient length-two factors above. This is a finite spectral question. A negative answer would kill the simplest deficiency-intersection route cleanly; a positive answer would justify an exact product Perron certificate and could move the primary endpoint.

## 9. Nearest solved literature problem and missing ingredient

The nearest solved framework remains Lueker's 2009 canonical finite-history construction. Its proof supplies exactly what a rigorous upper-bound route needs: a coverage argument, a finite state recurrence, and a Perron/Collatz transfer to an asymptotic upper bound. What it lacks is a tractable stronger accepted language at the same history size.

The independent Bernoulli matching model is not a substitute: its match array has different dependence and cannot certify the true two-string binary constant.

The deficiency-product proposal is deliberately staying inside Lueker's true dependent-string automaton. Its missing ingredient is not probability modeling; it is the finite dominant-SCC/Perron computation.

## 10. Stagnation and next-run rule

This is the third consecutive no-movement report after C028:

- C029: no movement;
- C030: no movement;
- C031: no movement.

Therefore the consecutive unchanged count is now

\[
\boxed{3}.
\]

Under the owner protocol, the **next R17 invocation is mandatory STUCK/thinking recovery episode 1 for this post-C028 stagnation cycle**. It must make no theorem-sized claim before completing the required stuck analysis and choosing exactly one recovery branch. If two recovery episodes fail on this cycle, the third stuck episode must rotate to an eligible outside target rather than continue polishing binary LCS.

Suggested next three method roles, deliberately different from this run's `#1,#20,#25`, are:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** solve the deficiency-product Perron question exactly at smaller canonical histories and track where the dominant SCC first feels the forbidden factors;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** port finite-type forbidden-word / Perron-perturbation tools from symbolic dynamics rather than treating the product as a brute-force table;
- **#28 REPLACE FOR ALL WITH FOR TYPICAL:** ask whether the deficient factors occur on Perron-supported recurrent states, not merely somewhere in the accepted language.

## 11. Model / scheduler control

The limitation is still real. The exposed scheduler schema offers task title, prompt, schedule or relative start offset, timing mode, and enabled state. It exposes **no model field and no reasoning-effort field**. Therefore GPT-6 maximum remains request text only and cannot be enforced or verified from this task surface.

Changing that requires a product/workspace/API surface which actually exposes model and reasoning controls, or a platform change to this scheduler schema. The historical P26 `You cannot modify this task` error is an ownership/context restriction; the repository records that a later authorized context could update P26. The legitimate workaround is to use that owning/authorized context or platform support, not to bypass permissions or clone around them.

No scheduler settings were changed in this run.

## 12. Prior-art / closure label

No closure claim is made. No paper folder is created. No independent audits are requested from other tracks because the source target is still open and this report contains only a finite recovery probe plus search diagnostics.

A bounded prior-art search checked Tiskin 2212.01582, Heineman et al. 2407.10925, Li–Ren–Wen 2504.10425, Lueker's JACM paper, Lueker's convergence paper, exact Conjecture 3.19 wording, and the C029 witness strings. Absence of a hit is not treated as proof of novelty.

```yaml
ledger_delta:
  worker: R17
  target: "binary Chvatal-Sankoff constant gamma_2"
  source_status: OPEN
  worker_status: PARTIAL
  metric: "rigorously certified interval width U-L"
  lower_before: "0.792665992"
  lower_after: "0.792665992"
  upper_before: "0.826279175721596843"
  upper_after: "0.826279175721596843"
  width_before: "0.033613183721596843"
  width_after: "0.033613183721596843"
  movement: false
  stagnation_before: 2
  stagnation_after: 3
  next_run_mandatory_stuck: true
  methods_actual: [1, 20, 25]
  exact_finite_probe:
    claim: "h=8 canonical machine accepts a path containing a length-two deficient factor"
    deficient_block: "(c=0,l=+2),(c=0,l=-2)"
    generated_pair: ["1100", "0110"]
    block_order: 2
    block_lcs: 3
    checker_commit: "fc982064a894d18c003a5bea124d48aa99106bb6"
    output_commit: "580fd024e04776da7c1977d895a3ee52044bd7a7"
  theorem_claim_this_run: false
  closure_claim: false
  publication_priority: UNVERIFIED
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  scheduler_model_selector: false
  scheduler_reasoning_selector: false
```
