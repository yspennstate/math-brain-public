# T075 work log

Task received: “push this problem forward by one checkable piece.” Session date 2026-11-14; first recorded local clock 20:52:00 +04:00 (Asia/Tbilisi).

## Scope and startup

All writes are confined to this directory. No git, external messages, subagents, or shared-brain/mesh/checklist writes: the task-specific prohibition on writes elsewhere takes precedence over the global startup instructions. Read the startup memory index and compute_state.json. Compute state: warn / owner_away_open, CPU saturated. No heavy computation planned.

Shell commands use OMP_NUM_THREADS=1 nice -n 15 python3. The inherited process already has priority 20; nice emits “setpriority: Operation not permitted” while Python runs successfully at priority 20. Verified independently with os.getpriority(os.PRIO_PROCESS, 0). Read the existing memory card about stacked relative nice on macOS. Keep the inherited lower priority.

## Literature search, first pass

Used the web search tool with these queries:

- Bernoulli convolutions transcendental absolute continuity 2026 2025
- Kittle Kogler 2610.10511 Bernoulli
- 2610.12072 Salem Bernoulli

Opened https://arxiv.org/abs/2611.17277 and https://arxiv.org/html/2611.17277v1, and the already-listed https://arxiv.org/abs/2610.10511. The new paper's authors are Samuel Kittle and Constantin Kogler; submission timestamp is 2026-11-12 18:50:34 UTC. Its Theorem 1.1 supplies a higher-integrability implication for absolutely continuous self-similar measures. This is a substantial regularity advance beyond the supplied status, not a solution of T075.

## Choice before further work

Apply step 1's literature-update stopping branch. Check the precise hypotheses and distinguish an implication assuming absolute continuity from a criterion proving absolute continuity. Write SOLVED_ELSEWHERE.md (the filename requested by the stopping branch, with an explicit warning that T075 is not solved) and REPORT.md. Do not start a separate research project.

## Commands already run

Read-only startup: Python pathlib reads of MEMORY.md, compute_state.json, and the existing macOS priority memory card; local directory listing. Priority check command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY_CHECK'
import os
print(os.getpriority(os.PRIO_PROCESS, 0))
PY_CHECK
```

Observed output from the equivalent check in the startup command: `PRIORITY 20`. No numerical experiment has been performed.

## Follow-up search and source check

Second web queries: `Bernoulli convolution transcendental absolute continuity November 2026 solved` and `"2611.17277" "transcendental"`. No solution of the universal transcendental-parameter assertion was located. This is a bounded search, not a proof that none exists. Total literature work remains below ten minutes.

Opened the PDF independently at https://arxiv.org/pdf/2611.17277 and the HTML proof section. The abstract, HTML theorem, and PDF are consistent about the direction of the regularity implication. The new algebraic results in the introduction have an algebraicity hypothesis and cannot be substituted for a result about transcendental parameters.

Audit target: verify that the Bernoulli convolution in the prompt is the invariant measure for the two contracting similarities x -> lambda*x +/- 1, and check the converse from a density in L^p to absolute continuity. Also check the quantifiers: the exponent may depend on lambda; there is no uniform exponent asserted here. Do not mistake dimension one for the hypothesis of Theorem 1.1.

## Applicability audit and attempted failure cases

1. First-sign derivation: write X = xi_0 + lambda*Y, where Y = sum_{n>=0} xi_{n+1} lambda^n has the same law as X and is independent of xi_0. Thus the law is invariant under the balanced pair g_+(x)=lambda*x+1 and g_-(x)=lambda*x-1. Both maps have contraction ratio lambda in (0,1).
2. Independent finite-prefix check: if mu_N is the law of sum_{n=0}^{N-1} xi_n lambda^n, then mu_{N+1} = ((g_+)_*mu_N + (g_-)_*mu_N)/2. The uniform tail bound lambda^N/(1-lambda) tends to zero, so the limiting law satisfies the same fixed-point identity. The maps are precisely of the type in the cited theorem.
3. Normalization check: the series starts at n=0 in both the prompt and the source. Its support lies in [-1/(1-lambda),1/(1-lambda)]. No change from fair signs to biased digits is being made.
4. Converse check: having a density f means nu(A)=integral_A f dx for every Borel A. Hence a Lebesgue-null set has nu-mass zero. Higher integrability is not needed for this direction.
5. Attempted misuse: the forward implication starts from absolute continuity, not from dimension one. A hypothetical singular full-dimensional nu_lambda would not satisfy that hypothesis. Consequently the new theorem does not settle T075.
6. Quantifier check: “for some p>1” is applied separately to each measure. No p uniform over transcendental parameters follows. The introduction's algebraic parameter criteria retain their algebraicity hypothesis.
7. Source check: the PDF's page 1 Theorem 1.1 agrees with the HTML and abstract. No occurrence of “transcendental” was found in the HTML. This text search is only a scope check, not an argument for nonexistence of other results.

No load-bearing numerical bound was introduced. There is therefore no numerical re-derivation or computation data file. No PROOF.md is supplied because this is the explicitly requested literature-update stopping branch, not an original proof. The proof and formalization of the cited preprint were not fully audited.

## Deliverables

Wrote SOLVED_ELSEWHERE.md and REPORT.md. The former explicitly says that T075 is not solved. The report uses VERDICT: PARTIAL and records the gap, uncertainty, commands, and a next step. Stop under task step 1.

Final document check: verified the exact verdict line, nonempty deliverables, explicit unsolved qualification, and the statement that Lean was not run. Replaced an unverified HTML fragment with the opened paper URL. Output: LOG.md, SOLVED_ELSEWHERE.md, REPORT.md present; all assertions passed.
