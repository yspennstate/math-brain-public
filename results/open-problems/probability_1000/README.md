# Probability open problems — 1,000-problem campaign

Work on open problems in probability carried out on the owner's machine between 2026-08-09 and
2026-09-14. It was previously held only in the brain repository
(`<private-repo>`, under `06_math_research/`) and is mirrored here so that
every open-problem effort lives in one place alongside the `paper*/` and `proofnet24/` tracks.

## Layout

| Directory | What it holds |
|---|---|
| `probability_1000_intake_claude_20260907` … `_I_20260914` | Intake ledgers: sources surveyed, problems extracted, dedup keys, exclusion decisions with the reason and the citation each was checked against. |
| `probability_1000_attempts_H_20260912`, `_I_20260914` | Attempt records and written arguments, one file per problem or problem group. |
| `prob1000_lean_20260908` | Lean formalisation of the arithmetic cores that admit one, plus the settled-problem write-ups. |
| `bernoulli_convolution_two_thirds_2026_09_07` | Bernoulli convolution at ratio 2/3: information summability and normality. |
| `sharp_rademacher_campaign_2026_08_18` | Sharp Rademacher singularity campaign. |

## Reading the status fields

Labels are recorded as the original worker wrote them and were not upgraded when mirroring. Treat
`settled` as "a written argument exists and was checked by hand", not as refereed. Specifically:

- Results carry their own verification wording verbatim — "Lean file P0208.lean, nine theorems, no sorry",
  "not formalised", "Prior art not cleared", "NOVELTY IS THE WEAK POINT".
- Prior art is the weakest link across the whole campaign, and it is an absence claim about the
  literature, not a property of the mathematics. Three problems were found already solved after being
  worked: one by the owner's own earlier paper, one whose 2022 solution the corpus missed, and one whose
  prior art an audit caught late. A citation check — pull the papers citing the source and search for the
  problem number — precedes any claim of novelty.
- The intake ledgers' exclusion decisions were audited: of eight literature exclusions checked, seven held
  and one was wrong and re-admitted as open.

## Provenance

Mirrored 2026-09-14 from the brain repository at its then-current commit, using the tracked file list
(`git archive HEAD <path>`) rather than the working directory, so that agent scratch directories and tool
caches that sit beside the campaign on disk are excluded by construction.
