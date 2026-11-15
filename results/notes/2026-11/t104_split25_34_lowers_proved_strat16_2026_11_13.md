---
name: t104_split25_34_lowers_proved_strat16_2026_11_13
description: "[PROVISIONAL] T104 split 2+5 and 3+4 with isolates proved for every N>=7 (STRAT16, my replay 17/17); small classes now take any lower components; D=2 with components <=3 closed"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-e0b7-4033-8e68-650ac991b0b4
  modified: 2026-11-13T11:57:52.264Z
---

T104 (Alon Conj 1.5), 13 Nov 2026: Codex STRAT16 on Mac mini 1 (~/agent_run/STRAT16, tarball STRAT16_final.tgz sha256 bc47e675...)
PROVED by replay_all.py (17 exact stages):
- split 2+5 and split 3+4 (each carrier connected, simple at the top) plus isolates: T>0 for every N>=7 and N->inf;
  closures T>=0, equality only at two equal edges plus isolates.
- split 2+3, 2+4, 3+3 and the four-vertex double carrier with ARBITRARY lower components (lower_components.py increment lemmas).
- so disconnected D=2 with every component <=3 vertices is closed for N>=7.
Method: fix the five-part's top vector u; T* concave on K_u (252 coefficient matrices PSD on 24 gap cones); extreme points by
rank; rank three via scale concavity + padding monotonicity F'(z)<=-3I/50 (k=5 hardest) + exact SOS (22 Gram matrices, T*_7>=1/400000).

My checks: replayed 17/17 myself from a hash-frozen copy; all 26 final .py and rational_sos_2.json byte-identical to it after Codex
exited; formula-(1) identity check 2.2e-15; padding eigenvalue check; float min searches found nothing negative.

Caveat: RESULT.md line 1 says "complete 2+5 and 3+4 split classes" but means with isolates; its OPEN section keeps lower components
open. Codex breached the 2.5 GB memory limit with two 3.3 GB dense SOS attempts (no proof depends on them).

OPEN: five-vertex double carrier + lower components; 2+5 / 3+4 + lower components; 3+5, 4+4, 4+5, 5+5.
STRAT17 launched 13 Nov on mini1 for 2+5/3+4 with lowers, then the five-vertex double carrier, then 4+4 (1.5 GB cap).
Brain repo: 06_math_research/t104_alon_agent_2026_11_11/strat16/ and strat16_check/ (push 148).
What would change this: a mismatch found in a later replay, or a counterexample from STRAT17.
Related: [[t104_5plus1_class_all_n_proved_strat15_2026_11_13]], [[audit_certificate_read_the_assert_not_the_printout_2026_11_13]].
