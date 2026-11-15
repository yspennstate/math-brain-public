# Check 1 (part a), 13 Nov 11:02 - exclusions carried to all N without re-proof

domain_audit.json: 19,273 transferred, 1,004 need new certificates (9 STRAT10 'scale:71/125', 995 STRAT12 Farkas exclusions).
Transferred as 'unchanged-common-interval' (accepted for every N without re-proof): 11,997 boxes (STRAT10 10,208, STRAT11 1,789),
reasons g01 g02 g04 g12 g14 g24 order12 order23 orientation row0 row1 row2 spectral11 only.
STRAT10 cover_face.necessary() lines 36-45 define every one of these from the chart variables (t,v1,z1,v2,z2,z) alone:
orientation t^2-1-z^2, order v2-v1 / x3-v2, row 4t-x_i^2-y_i^2, g_ij t+x_i x_j+y_i y_j, spectral11 5t-M11. No N appears.
The N-dependent premises (ratio 529 delta-60 tau^2, the 14/25 scale ceiling) are NOT in that branch: those boxes went through
weaker-ratio (9) or the all-N ceiling scale_exclusion. So the unchanged branch is sound for N >= 7 given the shared chart.
Still to do (part b): exact resample of 'weaker-Farkas' (7,267) and scale transfers with own Fraction code.

## Part b, 13 Nov 11:13 - weaker-Farkas transfers, exact, own code (strat15_check/my_check1b.py, run on Mac mini 1 in ~/agent_run/strat15_check_claude)
Sample 80 of 7,267 (seed 11): PASS 80, FAIL 0, guard failures 0, 5.1 s.
Negative control (ctl_halflam.py: keep only the first multiplier, halved): 14 of 20 FAIL, so the check can fail; the 6 that still pass
plausibly hold on one constraint alone.
Full run over all 7,267 started (pid 16585, check1b_full.out).
FULL RESULT (11:19): all 7,267 weaker-Farkas transfers PASS exactly, 0 FAIL, 0 guard failures, 250 s (check1b_full.out).
