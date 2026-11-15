# T063 work log

Task received: 14 November 2026, approximately 20:49 Asia/Tbilisi (16:49 UTC).

## 1. Orientation and literature check (begun 16:49 UTC)

Read the startup memory index and compute state. The latter reports `status: ok`, `mode: owner_away_open`. No subagents, git, or external writes will be used. The task-specific instruction to write only here supersedes the global checklist, mesh, recall-log, and brain-write routines, which mutate files elsewhere. Durable findings will remain here for the coordinator.

The shell launcher `OMP_NUM_THREADS=1 nice -n 15 python3 ...` emitted `nice: setpriority: Operation not permitted` but ran the small read-only script. Process inspection with `ps` is also denied by the sandbox. Further computations will use the requested nice launcher; this restriction will be documented rather than hidden. No heavy computation has run.

Web queries:

- `six vertex height Gaussian free field Averous Duminil-Copin He Lammers Manolescu 2026 2610.07454`
- `six vertex model Gaussian free field convergence 2026 full disordered regime`

Opened https://arxiv.org/abs/2610.07454. Its abstract matches the supplied partial-range domain theorem. Search also returned the March 2026 full-plane partial-range result arXiv:2603.06268, and a September 2026 OpenAI manuscript claiming the entire balanced regime. The latter needs examination before it can be called a solution.

Opened https://arxiv.org/abs/2603.06268: Hugo Duminil-Copin, Karol Kajetan Kozlowski, Piet Lammers, Ioan Manolescu; submitted 6 March 2026. Abstract proves full-plane convergence for Delta in [-1,-1/2], with anisotropic extensions. This is within the ranges already covered by the supplied status, not a resolution of its remaining range.

The GitHub directory for the OpenAI manuscript failed to fetch. Opened the community mirror landing page (https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/), which links the manuscript and labels its collected notes unreviewed. Its abstract alone is not sufficient to certify the claim. Following its PDF link next.

Opened the 93-page manuscript PDF via that mirror and the HTML of arXiv:2603.06268. Follow-up queries `"The Gaussian free field limit of the balanced" gap proof` and `six vertex Gaussian free field November 2026 full range c` returned a November item, `Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2`, at https://hexagonmath.org/2611.00291v1. The search snippet says an audit located an identification gap in the September claim. Opening this primary source now; a search snippet is not evidence of a theorem.

Opened the Hexagon record. It is dated 11 November 2026 (history says initial deposit 10 November), contributed by Yan Ru Pei, and explicitly unrefereed in its discussion of the OpenAI manuscript. It states zero-slope uniqueness for 1 < c <= 2 and a conditional repair of the state identification. Its provenance expressly says that the two required properties of the auxiliary OpenAI state were not checked. This is a substantial post-status claimed advance, with a specific remaining dependency; it is not evidence that the full GFF problem has an audited proof.

Read Theorem 1.1 and Proposition 4.3 of the OpenAI PDF. Theorem 1.1 claims the balanced-torus plane limit for all 0 < c <= 2 with squared GFF multiplier 2/arccos(Delta) = 1/arcsin(c/2). Proposition 4.3 uses zero-slope equilibrium uniqueness to identify a near-balanced auxiliary state for c >= 1. The November paper addresses exactly this issue. Following the user's early-stop instruction, the deliverable will be a literature handoff, not a new proof or a finite calculation. Opening the November PDF to check its precise theorem and conditions before writing the final report.

## 2. Checks and handoff

Opened https://hexagonmath.org/pdf/2611.00291v1 and checked Theorem 1.2, Corollaries 1.3 and 1.6, and the proof of Corollary 1.6 (printed p. 28). This is a Hexagon identifier, not an arXiv identifier. The exact unverified conditions are auxiliary-state existence (O1) and global free-energy minimality (O2). The printed author is Yan Ru Pei. Also read the September manuscript's title page, which gives author OpenAI and date 23 September 2026.

Independent algebra audit (no numerical fitting):

1. Forward substitution gives c = 1, sqrt(2), sqrt(3), 2 corresponding to Delta = 1/2, 0, -1/2, -1. In reverse, solving c = sqrt(2(1-Delta)) reproduces all four. The map is strictly decreasing since dDelta/dc = -c. Thus 1 < c <= 2 corresponds to -1 <= Delta < 1/2; sqrt(2) <= c < sqrt(3) corresponds to -1/2 < Delta <= 0. Endpoint directions matter.
2. Let theta = arcsin(c/2), so 0 < theta <= pi/2. Then cos(2 theta) = 1-c²/2 = Delta and 2 theta lies in (0,pi]; hence arccos(Delta) = 2 theta on the principal branches. Therefore 2/arccos(Delta) = 1/arcsin(c/2). Checking each expression separately at the four preceding points gives respectively 6/pi, 4/pi, 3/pi, 2/pi. Positivity and decreasing roughness with increasing c pass this elementary check. This only checks normalization arithmetic; it does not prove the claimed asymptotics.

Niceness diagnosis, exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY'
import os
print('OMP_NUM_THREADS=' + os.environ['OMP_NUM_THREADS'])
print('effective_nice=' + str(os.getpriority(os.PRIO_PROCESS, 0)))
PY
```

Output:

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1
effective_nice=20
```

The inherited process is already at nice 20, lower priority than requested; the failed relative increment did not launch high-priority compute. Only tiny read-only Python processes ran; no numerical experiment, array allocation, GPU, or extra worker was used.

Saved SOLVED_ELSEWHERE.md and REPORT.md. The verdict is deliberately PARTIAL: a substantial claimed literature advance was found, while full GFF convergence was not verified. No new PROOF.md is appropriate under the requested early-stop branch. All mutations used the workspace patch tool. Final file consistency check follows.

Final check: ran a small `OMP_NUM_THREADS=1 nice -n 15 python3` script reading the three deliverables, asserting the report's `VERDICT: PARTIAL` prefix, the Hexagon identifier in the reference note, and absence of a new PROOF.md. Output: `PASS: required literature-handoff files and verdict; no new proof claimed`. Literature check and handoff completed at approximately 16:52 UTC (20:52 Asia/Tbilisi), under three minutes after the first search.
