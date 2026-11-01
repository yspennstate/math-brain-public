# P0104 review packet — w368, 2026-10-10

## Verdicts

KEEP w366-C1 through C5 and w367-C001 through C003 within their stated scopes. KEEP w367-scope-001 as a source-status caution. w366-C3/C4 duplicate w367's independent boundary calculations, so the brain bundle uses one copy of each statement. The machine-readable verdicts and step checks are in `REVIEW.jsonl`; detailed independent proofs are in `ATTEMPT.md`.

## Reproduction

`python -X utf8 ~/brain_workers/w368/reproduce.py`

Observed: `PASS: 32 four-route checks; sharp examples 6=6 and 5<6; ratio=10.000000`.

The code checks finite route geometry, explicit threshold witnesses and one numerical ratio. The all-n statements are checked by the written proofs in `ATTEMPT.md`, not by finite enumeration. No formal prover or admitted placeholder is involved.

## Source and current status

Question 13 in Auffinger--Damron--Hanson, arXiv:1511.03262v2, is the primary source behind P0104. See `SOURCE_STATUS.json`. The survey explicitly leaves the conditions on F and the meaning of the variance scaling symbol open. Damron--Hanson--Sosoe arXiv:1306.1197 gives the logarithmic variance improvement; Basu--Sidoravicius--Sly arXiv:2604.01214 gives a power saving for a rotationally invariant Riemannian model. Local August 2026 brain records say lattice chi=1/3 was open. Present October 2026 openness is UNKNOWN pending exhaustive owner-work and literature check; no peer result is a solution to Question 13.

## Boundary and next handoff

The Pareto fixed-endpoint example has finite mean and infinite variance at tail index alpha=1/2, so a theorem phrased for all finite iid edge weights has an immediate moment defect. The Uniform[1,1+epsilon] example rules out one overly uniform auxiliary variance estimate even for continuous bounded positive weights. The hardest gap is fixed-law large-n control of detours, with polynomial upper saving and matching lower scale. A subsequent proof attempt should choose a precise chi definition and a fixed F class before claiming progress on the source question.

No new referee-authored lemma is submitted here; w371 independent review is therefore not required for these KEEP verdicts. The reviewed source results are still unclaimed as novel.
