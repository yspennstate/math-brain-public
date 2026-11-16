---
name: t104_five_vertex_classes_lowers_proved_strat17_2026_11_13
description: "[VERIFIED] T104 split 2+5, 3+4 and five-vertex double carrier proved with ARBITRARY lower components, every N>=7 (STRAT17, my replay 24/24); open 3+5, 4+4, 4+5, 5+5"
metadata:
  node_type: memory
  status: verified
  type: project
  modified: 2026-11-13T12:32:49.500Z
---

T104 (Alon Conj 1.5), 13 Nov 2026: Codex STRAT17 on Mac mini 1 (~/agent_run/STRAT17, STRAT17_final.tgz sha256 365f57a7...)
PROVED by replay_all.py (24 exact stages):
- split 2+5 and 3+4 with any number of lower components of any size: T>=0 every N>=7 and infinity; positive lower trace gives T>0.
- five-vertex double carrier with arbitrary lower components (STRAT15 isolate theorem used as black box at zero lower trace).
- equality: two equal edges + isolates; double-carrier closure also balanced triangle + isolates.
Method (reusable): lower blocks only shift M by s/2 and add 2 sum mu(1-mu)>=0; the increment is concave in the whole lower
matrix, so the exact trace interpolation F(s)=(1-s/S)F(0)+(s/S)F(S)+s(S-s)/k reduces ALL lower collections at once to s=0
and s=S. Adding one lower edge CAN lower T* (exact fixtures) - one-at-a-time increment arguments are wrong here.
Double carrier tau<=1: two weighted Cauchy inequalities give margin >=1/270 at s=k-4, k=5 hardest.

My checks: replay 24/24 from a freeze taken after Codex exited (live==freeze); own float searches for 2+5+lowers and
five-double+lowers found no negative T (tight spot: K5 top at max lower trace); hand audit of the graph-to-scalar steps.
Scar: my first freeze, taken while Codex was still editing, failed on a since-fixed assert - freeze only after exit.
Caveat: rests on STRAT15's 9,370-box cover (not rerun).
OPEN: 3+5, 4+4, 4+5, 5+5 (4+4 convex frame set up). Brain repo: 06_math_research/t104_alon_agent_2026_11_11/strat17/ (push 149).
Related: [[t104_split25_34_lowers_proved_strat16_2026_11_13]], [[t104_5plus1_class_all_n_proved_strat15_2026_11_13]], [[audit_certificate_read_the_assert_not_the_printout_2026_11_13]].
