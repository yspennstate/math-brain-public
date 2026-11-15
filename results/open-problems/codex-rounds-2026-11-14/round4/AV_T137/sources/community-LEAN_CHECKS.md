# Comparator run on OpenAI's Lean challenges (October 2026)

OpenAI's release states each formalized result in a file `lean/ComparatorChallenges/X.lean`, whose proof is left as `sorry` on purpose, and names the module that proves it in `X.json`. Lean's [comparator](https://github.com/leanprover/comparator) checks that this module proves exactly the theorems stated there, that it uses no axioms beyond those the `.json` permits (`propext`, `Quot.sound`, `Classical.choice` for all 416), and that the Lean kernel accepts the proof.

The maintainers ran the comparator on all 416 challenges of the version checked (419 after OpenAI's update of 26 October). Results per challenge: [`checks/comparator-2026-10-26/results.tsv`](../checks/comparator-2026-10-26/results.tsv), with one log per run in [`checks/comparator-2026-10-26/logs/`](../checks/comparator-2026-10-26/logs/). The paper pages show the result next to each statement in their "Lean formalization" section.

## Result

- **414 accepted**, 9 of them with the limitation described below. One of them, `UniversalTensorSquares`, only on a retry that took about 4 hours.
- **2 not finished:** `PlanarPacking` (stopped by a 12-hour limit) and `MUBSix` (retry stopped after about 3 hours to free the server). Both are very large computational certificates (about 0.9 and 2.8 million lines of Lean). For both, the maintainers checked outside the comparator that the proof module builds without errors, that `#print axioms` on the proved theorem lists only the three standard axioms, and that the proved theorem's statement is word for word the challenge's (`logs/PlanarPacking.axioms.txt`, `logs/MUBSix.axioms.txt`). The comparator itself gave no verdict.
- **None rejected.**

## What this shows, and what it does not

An accepted run means: the proof module proves the statement written in the challenge file, using only the standard axioms, and the Lean kernel accepts it (with the exception for 9 challenges described below).

It does not mean that the challenge statement says what the paper claims. The definitions and the theorem in the challenge file can differ from the paper's (special cases, weaker conclusions, non-standard definitions). OpenAI's scope notes in `lean/docs/` describe some of these differences. Whether a statement matches the paper needs a person who knows the subject; on this site nobody has checked that unless a paper's notes say so.

**A limitation for 9 challenges.** A configuration can list definitions under `definition_names`. For those, the comparator checks only that the proof's definition has the same name and type as in the statement file, not that its body is the same, even when the statement file spells the body out. In the version checked here, 9 configurations list definitions that the statement file spells out: `Brenier`, `DefocusingNLS`, `EuclideanFiveColor`, `KServer`, `LogspaceEquality`, `Naimark`, `OccupiedOverlap`, `Rokhlin` and `SpinAngle`. For them, an accepted run does not show that the proof uses the statement file's definitions. A tenth, `ElementaryPositivity`, names no theorem; its result is stated as the type of a definition (`elementaryPositivityWitness`) whose fields include the claimed expansion, and the comparator checks that the proof supplies a definition of exactly that type. OpenAI changed all 10 configurations on 26 October 2026 (see below); the results here are for the earlier versions.

## How it was run

- Repository commit `f1be4a4`, whose `lean/` folder is identical to openai/math at commit `fd4aeeb` (OpenAI's update of 8 October 2026), Lean `v4.34.1`, Mathlib and the other dependencies as pinned by `lean/lake-manifest.json`, with the compatibility patches the lakefile applies (the logs' "has local changes" warnings refer to them).
- comparator `v4.34.0` (commit `d03acab`) and lean4export `v4.34.0` (commit `076e8e5`), both built with Lean `v4.34.1`; landrun 0.1.18 (commit `ec104f6`) as the sandbox, on Linux 7.2 with Landlock. The second kernel (nanoda) ran only for the two challenges whose configuration enables it, `ArtinParabolicIntersections` and `TraceIdealTransportSupport`; it accepted both.
- On a university server, 25–26 October 2026. To save time, the proof modules were compiled in the same workspace before the comparator ran on them. The comparator's documentation advises against this when a proof might be adversarial; nothing here suggests that, but it is a deviation from its strictest setting. For one challenge, `CHObstruction`, the comparator was also run in a fresh workspace before anything had been compiled, with the same result (`logs/CHObstruction.fresh.log`, the summary lines of that run).
- Each run had a 2-hour limit; the three that exceeded it were retried with longer limits as described above. Server paths in the logs are replaced by `<workspace>`.

The run was set up and monitored by an AI agent (Claude Code) for the maintainers. The logs are the comparator's own output.

## Later changes

OpenAI updated its repository on 26 October 2026 ("Some Comparator configurations were fixed, and some Lean formalizations were improved"), changing 11 of the checked challenges or their configurations: the 10 above (the nine configurations now list no definitions; `ElementaryPositivity` now names its theorem, `OAI.elementaryPositivityExpansion`, and keeps the definition) and `HarmonicGrowth` and adding new ones. `results.tsv` records the git hashes of each challenge's `.lean` and `.json` as checked, and of the repository files a challenge imports (two challenges import library modules); the site shows a result only while all these files are unchanged, and otherwise says that the challenge has changed since the run. Challenges added later have no result here.

## Other runs

[MathVet](https://math.vet), an independent project, reports running the comparator on all 416 challenges in October 2026 with all accepted, 401 of them in the landrun sandbox, including `PlanarPacking` and `MUBSix` ([table](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/challenge-status.csv)).

