# STRAT16 audit on PROVED (an agent, 13 Nov 2026 ~15:25 +04)

Codex (mini1 ~/agent_run/STRAT16, pid 71330) reports: PROVED (replay_all.py), all 15 exact stages PASS, 56.5 s,
child peak 85 MB: split 2+5 AND 3+4 with isolates, T>0 for connected simple carriers, every N>=7 and infinity; closure
equality only at two equal edges + isolates. Also 2+3 now with arbitrary lower components (increment lemma).

## My checks so far
1. Frozen-hash diff (replay2/sources.sha256 vs live): algebra, concavity, rank_two SAME. tree_certificate.py CHANGED:
   adds three forest families (four-star+isolate, four-path+isolate, three-path+two isolates), signs 0 on isolated
   vertices; the old three tree families unchanged. disconnected_certificate.py CHANGED: adds lower-edge X1*=2t(1-t) term
   and the general lower-component bracket 7/3+z/3+(53/3+11z/3)g+(10+2z)q (coefficients asserted positive). Both widen
   scope; nothing previously checked was altered.
2. Independent numbers agree with my earlier searches: T*_7(J/5)=63/250 -> T=0.04032 (my min search 0.04032);
   T_inf(J/5)=3/6.25=0.48 (mine 0.48).
3. my_F_identity_check.py: Codex's rank<=3 reduction u^T F(1/k) u equals my own formula-(1) T* at 8000 random
   (u, S rank<=2, k) cases, max relative error 2.2e-15. PASS (NUMERICAL).
4. my_padding_check.py: F'(z) <= -3I/50 claim; largest eigenvalue found over feasible S, z in {0,.1,.2}: -4.33. PASS (NUMERICAL).

## Rank-three route as written (for the record)
Concavity in the scale of S from J/5 reduces all rank<=3 A to S=0 and the first zero-edge endpoint; padding monotonicity
makes k=5 hardest; the zero-edge endpoint chart S=VV^T/(5t) on a proved root box is certified by an exact rational SOS
(22 PD Gram matrices, rational_sos_2.json) giving T*_7 >= 1/400000. Small margin, but exact.

## Still to do
- Run replay_all.py from a frozen copy (replay3) when mini1 memory free >= 25% (24% at 15:2x, so not started).
- Then write-up + push strat16_check and Codex STRAT16 sources to the brain repo.
- Open beyond this: split pairs with lower components (2+4,3+3,2+5,3+4), 3+5,4+4,4+5,5+5, double carriers with lower comps.

## My frozen replay (15:27-15:29 +04, mini1 at 70% free)
replay3 = rsync of STRAT16 at 15:26 (codex.log excluded), sources hashed in strat16_mycheck/replay3_sources.sha256 (35 files).
First launch used /usr/bin/python3 (no sympy) and failed at stage 1 on ModuleNotFoundError; relaunched with
/usr/local/bin/python3 (sympy 1.13.1): replay_all.py 15 of 15 stages PASS, label "PROVED (replay_all.py): split 2+5 and
3+4 with isolates, every real k>=5 and infinity", 69.2 s, max RSS 82.7 MB. After the run every frozen .py still matches;
only the four output JSONs it rewrites differ (concavity_coefficients, rank_two_checks, tree_checks, replay_summary).
Codex is still working: live lower_components.py and replay_all.py changed after my freeze (a lower-components stage is
being added). That newer version needs its own replay before it is pushed as proved.

## 17-stage version (lower-component extensions), my replay4 at ~15:3x +04
Codex added lower_components.py (+ byte-identical prior_four.py from STRAT7): four-vertex double carriers and split
2+4, 3+3 allow arbitrary lower components; with 2+3 already, the disconnected D=2 statement with every component of
size <=3 is closed for N>=7 (and the four-vertex classes above). Hand check: substituting s=k-n0+1-q into the 2+3
bracket 2(k+1)(k-2)-4k(2M+s/2-1)+2(k+2)h gives exactly B_lower=2k(n0-4M+h)+4(h-1)+2kq (Codex's general form). 
replay4 (frozen, hashes replay4_sources.sha256): rc=0, 17 of 17 PASS, label "PROVED (replay_all.py): split 2+5 and 3+4
with isolates; smaller carrier classes with arbitrary lowers; every real k>=5 and infinity", 69.5 s, 85.9 MB; no .py changed.
OPEN per RESULT.md: five-vertex double carriers with lower components; 2+5, 3+4 with lower components; 3+5,4+4,4+5,5+5.
