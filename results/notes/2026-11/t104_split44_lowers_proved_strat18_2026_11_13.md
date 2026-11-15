---
name: t104_split44_lowers_proved_strat18_2026_11_13
description: "T104 split 4+4 proved with arbitrary lower components, every N>=8 (STRAT18, my replay 32/32 from freeze); open 3+5, 4+5, 5+5"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:05:05+02:00
  status: verified
  evidence: "my replay_all.py rerun 32/32 PASS from STRAT18_freeze on Mac mini 1 (strat18_myreplay.out), live==freeze hash diff; push 150 commit 1a3f83d5 verified 33/33"
---

T104 (Alon Conj 1.5), 13 Nov 2026: Codex STRAT18 on Mac mini 1 (~/agent_run/STRAT18, freeze STRAT18_freeze, 70 hashed files strat18_freeze.sha256)
PROVED by replay_all.py (32 exact stages, 24 inherited + 8 new):
- split 4+4 (two connected four-vertex top carriers) with isolates OR arbitrary lower components of any size: T>=0 every N>=8 and infinity; two connected simple tops give T>0; positive lower trace gives T>0.
- equality only at two equal edges + isolates.
- 3+5 setup (triangle corner reduction, K_u concavity) done; 3+5 signs OPEN.
Method: fix both top vectors, separate concavity on K_u x K_v; four-vertex extremes = star/path trees or rank<=2;
tree pairs by flux parametrisation (numerators 4,536-6,075 coefficients, all positive at k=6+z); rank boundary by
coefficientwise PSD (margin 1/100); inverse-padding derivative PSD so k=6 hardest; max lower trace
F_k(k-7)>=F_6(0)+3/10 by twelve Bernstein controls; disconnected extremes go to 3+4/2+4/smaller.

My checks: replay 32/32 from the freeze taken after Codex exited (127 s, 105 MB), live==freeze; read the exact LDL PSD test
in boundary44/padding44 by hand (rejects negative pivot and zero pivot with nonzero row; each script asserts zero failures);
own float search my_44_search.py found no negative T - tight spot with lowers is K4+K4 at max lower trace, T* about 1.7 at
k=1e6, so no uniform margin in T as N grows, only through 1/M^2.
Caveat: inherited stages still rest on STRAT15's 9,370-box cover (not rerun).
OPEN: 3+5, 4+5, 5+5. Brain repo: 06_math_research/t104_alon_agent_2026_11_11/strat18/ and strat18_check/ (push 150, commit 1a3f83d5).
Related: [[t104_five_vertex_classes_lowers_proved_strat17_2026_11_13]], [[t104_split25_34_lowers_proved_strat16_2026_11_13]], [[audit_certificate_read_the_assert_not_the_printout_2026_11_13]].

