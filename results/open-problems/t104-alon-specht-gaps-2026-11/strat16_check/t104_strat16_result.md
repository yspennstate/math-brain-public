# T104 (Alon Conj. 1.5): split 2+5 and 3+4 carriers, and lower components for the small classes — STRAT16 result

13 Nov 2026, 15:5x +04. an agent. Run on Mac mini 1, ~/agent_run/STRAT16 (Codex pid 71330, normal speed, exited).

## What is proved

PROVED (STRAT16/replay_all.py, 17 exact stages, all PASS; Codex's final replay 59.2 s, peak child RSS 86 MB):
1. Split 2+5 (an edge and a connected five-vertex component, each carrying one top eigenvalue) plus isolated vertices:
   T > 0 for every N >= 7 and in the limit N -> infinity.
2. Split 3+4 plus isolated vertices: the same.
3. On the auxiliary closures of both classes T >= 0, with equality only at two equal edges plus isolates. The
   balanced-triangle limit cannot occur (the external edge keeps normalized weight >= 1/5).
4. Split 2+3, 2+4, 3+3 and the four-vertex double carrier now allow arbitrary lower components (increment lemmas plus
   convex reductions, lower_components.py).
5. Hence the disconnected D = 2 statement with every component of at most three vertices is closed for N >= 7.

Method (2+5): fix the selected top vector u of the five-vertex part; T* is concave on
K_u = {A sym PSD, A >= 0 entrywise, A1 = 1, Au = 0} (252 coefficient matrices, exactly PSD on all 24 gap-ordering cones,
every real k >= 5 and infinity); extreme points classified by rank (rank two: J5/5 + g vv^T at its endpoint; rank three:
concavity in the scale of S reduces to S = 0 and the zero-edge endpoint, padding monotonicity F'(z) <= -3I/50 makes k = 5
hardest, and an exact rational SOS with 22 PD Gram matrices gives T*_7 >= 1/400000); disconnected extremes go to STRAT7's
padded statements. 3+4 follows the same pattern with the four-part's top vector fixed.

## My independent checks (all PASS)

1. my_replay3 / my_replay4: replay_all.py rerun by me from frozen source copies (hash lists replay3_sources.sha256,
   replay4_sources.sha256): 15/15 and then 17/17 PASS (69.5 s, 86 MB). After Codex exited, all 26 live .py files and
   rational_sos_2.json are byte-identical to my replay4 freeze; only output JSONs differ, which the replay rewrites.
2. my_F_identity_check.py: Codex's u^T F(1/k) u equals my own formula-(1) T*, max relative error 2.2e-15 over 8000 cases.
3. my_padding_check.py: the largest eigenvalue of F'(z) found is -4.33, inside the claimed bound -0.06.
4. my_min_search.py and my_concavity_sample.py (float corroboration written from RESULT.md, not from Codex's code):
   no negative T and no positive concavity direction found.
The B_lower identity in lower_components.py was checked by hand. Audit record: strat16_check/strat16_audit_on_proved.md.

## Caveats

- The first line of RESULT.md says "the complete 2+5 and 3+4 split classes". That means with isolates only; its own OPEN
  section keeps 2+5 and 3+4 with extra components open.
- Operational: two dense SOS discovery attempts peaked at about 3.29 GB each, above the 2.5 GB limit in the prompt
  (Codex recorded this itself; a workspace lock now prevents overlap). No proof depends on those attempts.

## What is NOT proved (OPEN)

- Five-vertex double carriers with any nontrivial lower component.
- Split 2+5 and 3+4 with extra nontrivial lower components.
- Split 3+5, 4+4, 4+5, 5+5, with or without lower components.

## Files

Tarball STRAT16_final.tgz (1,078,315 bytes, sha256 bc47e675ac910891b98d79b5879905eb4df00b5c76103e6955bf4f449a0926ae,
copied STRAT7 excluded) on Mac mini 1 at ~/agent_run/. Its 77 top-level files are pushed under strat16/; my checks
under strat16_check/.

## Next for T104

STRAT17: 4+4 (two four-vertex parts, both top vectors to fix) or 2+5 / 3+4 with lower components via the increment
lemmas that closed the small classes.
