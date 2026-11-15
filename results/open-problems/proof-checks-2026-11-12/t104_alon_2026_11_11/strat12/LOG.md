OPEN: STRAT12 started 2026-11-13 10:26 +04. Task: close the 13,368 OPEN leaves of T104 5+1 region (11), N=6, by constrained Bernstein certificates.

OPEN: Read STRAT10/RESULT.md and STRAT11/RESULT.md. Shared mesh hello/digest/assert and checklist registration are denied by the sandbox (read-only shared databases). No live claim conflict was reported. All task writes are confined to the isolated STRAT12 workspace.

OPEN: os.nice(5) is denied with PermissionError by this sandbox. Four multiprocessing workers and single-thread numerical libraries will be used; nice 5 cannot truthfully be claimed.

OPEN: The supplied STRAT11 snapshot contains only RESULT.md, LOG.md, remaining_open_boxes.json and replay_all.py. All nine verification scripts named by its replay_all.py are absent. A complete inherited replay cannot run from this snapshot.

OPEN: Strict Bernstein exclusion/positivity may be impossible on leaves containing the disconnected equality limit. Exact obstruction replay is being implemented.

OPEN: discovery checkpoint 40/13368; original {'exclusion': 35, 'positivity': 4, 'open': 1}; leaves {'exclusion': 35, 'positivity': 4, 'open': 1}; max depth 0; remaining chart volume 3327993/32768. NUMERICAL elapsed 1.45 seconds.

OPEN: discovery checkpoint 500/13368; original {'exclusion': 363, 'positivity': 126, 'closed_after_splitting': 9, 'open': 2}; leaves {'exclusion': 378, 'positivity': 148, 'open': 4}; max depth 4; remaining chart volume 3262635/32768. NUMERICAL elapsed 14.10 seconds.

OPEN: discovery checkpoint 500/13368; original {'exclusion': 363, 'positivity': 126, 'closed_after_splitting': 9, 'open': 2}; leaves {'exclusion': 378, 'positivity': 148, 'open': 4}; max depth 4; remaining chart volume 3262635/32768. NUMERICAL elapsed 14.38 seconds.

OPEN: discovery checkpoint 1000/13368; original {'exclusion': 690, 'positivity': 292, 'closed_after_splitting': 16, 'open': 2}; leaves {'exclusion': 713, 'positivity': 330, 'open': 4}; max depth 4; remaining chart volume 6385797/65536. NUMERICAL elapsed 16.15 seconds.

OPEN: discovery checkpoint 1500/13368; original {'exclusion': 1055, 'positivity': 414, 'closed_after_splitting': 29, 'open': 2}; leaves {'exclusion': 1091, 'positivity': 477, 'open': 4}; max depth 4; remaining chart volume 1565163/16384. NUMERICAL elapsed 28.22 seconds.

OPEN: discovery checkpoint 2000/13368; original {'exclusion': 1268, 'positivity': 698, 'closed_after_splitting': 32, 'open': 2}; leaves {'exclusion': 1307, 'positivity': 767, 'open': 4}; max depth 4; remaining chart volume 1531503/16384. NUMERICAL elapsed 49.47 seconds.

OPEN: discovery checkpoint 2500/13368; original {'exclusion': 1444, 'positivity': 1016, 'closed_after_splitting': 38, 'open': 2}; leaves {'exclusion': 1483, 'positivity': 1101, 'open': 4}; max depth 4; remaining chart volume 11986605/131072. NUMERICAL elapsed 72.65 seconds.

PROVED (verify_obstruction.py, obstructions.json): five input nodes 15773, 21550, 14175, 20736 and 12091 contain Q(sqrt(5)) points with T=0, every weak chart constraint nonnegative, connected=0 and a=b=1. Neither requested strictly signed Bernstein form, even with products, can close boxes containing these points. Every finite subdivision retains a descendant containing each point. These disconnected points are not feasible counterexamples. Replay uses rational pairs, not floating square roots.

OPEN: Pilot at depth 4 processed 500 original boxes; 363 direct exclusions, 126 direct positivity certificates, nine originals fully closed after splitting and two originals still open. Exact acceptance occurred in discovery; independent bank replay pending. NUMERICAL pilot elapsed 14.38 seconds, largest observed worker peak RSS 314507264 bytes. The full four-worker depth-4 run resumed from this checkpoint.

OPEN: discovery checkpoint 3000/13368; original {'exclusion': 1685, 'positivity': 1257, 'closed_after_splitting': 56, 'open': 2}; leaves {'exclusion': 1724, 'positivity': 1396, 'open': 4}; max depth 4; remaining chart volume 11711331/131072. NUMERICAL elapsed 93.47 seconds.

OPEN: discovery checkpoint 3500/13368; original {'exclusion': 2018, 'positivity': 1411, 'closed_after_splitting': 67, 'open': 4}; leaves {'exclusion': 2068, 'positivity': 1580, 'open': 6}; max depth 4; remaining chart volume 5729157/65536. NUMERICAL elapsed 108.19 seconds.

OPEN: discovery checkpoint 4000/13368; original {'exclusion': 2287, 'positivity': 1641, 'closed_after_splitting': 68, 'open': 4}; leaves {'exclusion': 2338, 'positivity': 1812, 'open': 6}; max depth 4; remaining chart volume 11216061/131072. NUMERICAL elapsed 123.86 seconds.

OPEN: discovery checkpoint 4500/13368; original {'exclusion': 2576, 'positivity': 1835, 'closed_after_splitting': 84, 'open': 5}; leaves {'exclusion': 2645, 'positivity': 2034, 'open': 9}; max depth 4; remaining chart volume 10977129/131072. NUMERICAL elapsed 140.00 seconds.

OPEN: discovery checkpoint 5000/13368; original {'exclusion': 2796, 'positivity': 2101, 'closed_after_splitting': 93, 'open': 10}; leaves {'exclusion': 2874, 'positivity': 2350, 'open': 15}; max depth 4; remaining chart volume 42872067/524288. NUMERICAL elapsed 162.89 seconds.

OPEN: discovery checkpoint 5500/13368; original {'exclusion': 3084, 'positivity': 2302, 'closed_after_splitting': 99, 'open': 15}; leaves {'exclusion': 3169, 'positivity': 2586, 'open': 24}; max depth 4; remaining chart volume 41900751/524288. NUMERICAL elapsed 179.37 seconds.

OPEN: discovery checkpoint 6000/13368; original {'exclusion': 3253, 'positivity': 2605, 'closed_after_splitting': 124, 'open': 18}; leaves {'exclusion': 3351, 'positivity': 2977, 'open': 28}; max depth 4; remaining chart volume 41052357/524288. NUMERICAL elapsed 204.47 seconds.

OPEN: discovery checkpoint 6500/13368; original {'exclusion': 3420, 'positivity': 2923, 'closed_after_splitting': 137, 'open': 20}; leaves {'exclusion': 3524, 'positivity': 3356, 'open': 32}; max depth 4; remaining chart volume 40046157/524288. NUMERICAL elapsed 229.07 seconds.

OPEN: discovery checkpoint 7000/13368; original {'exclusion': 3757, 'positivity': 3075, 'closed_after_splitting': 148, 'open': 20}; leaves {'exclusion': 3862, 'positivity': 3543, 'open': 32}; max depth 4; remaining chart volume 38906541/524288. NUMERICAL elapsed 242.38 seconds.

OPEN: discovery checkpoint 7500/13368; original {'exclusion': 3957, 'positivity': 3367, 'closed_after_splitting': 156, 'open': 20}; leaves {'exclusion': 4062, 'positivity': 3865, 'open': 32}; max depth 4; remaining chart volume 37807533/524288. NUMERICAL elapsed 263.59 seconds.

OPEN: discovery checkpoint 8000/13368; original {'exclusion': 4267, 'positivity': 3553, 'closed_after_splitting': 159, 'open': 21}; leaves {'exclusion': 4374, 'positivity': 4062, 'open': 33}; max depth 4; remaining chart volume 9196209/131072. NUMERICAL elapsed 278.22 seconds.

OPEN: discovery checkpoint 8500/13368; original {'exclusion': 4517, 'positivity': 3787, 'closed_after_splitting': 174, 'open': 22}; leaves {'exclusion': 4637, 'positivity': 4335, 'open': 34}; max depth 4; remaining chart volume 8932113/131072. NUMERICAL elapsed 298.67 seconds.

OPEN: discovery checkpoint 9000/13368; original {'exclusion': 4863, 'positivity': 3911, 'closed_after_splitting': 204, 'open': 22}; leaves {'exclusion': 5010, 'positivity': 4528, 'open': 34}; max depth 4; remaining chart volume 8566641/131072. NUMERICAL elapsed 316.18 seconds.

OPEN: discovery checkpoint 9500/13368; original {'exclusion': 5214, 'positivity': 4030, 'closed_after_splitting': 230, 'open': 26}; leaves {'exclusion': 5397, 'positivity': 4719, 'open': 39}; max depth 4; remaining chart volume 8032473/131072. NUMERICAL elapsed 332.22 seconds.

OPEN: discovery checkpoint 10000/13368; original {'exclusion': 5492, 'positivity': 4223, 'closed_after_splitting': 253, 'open': 32}; leaves {'exclusion': 5697, 'positivity': 4998, 'open': 49}; max depth 4; remaining chart volume 14470119/262144. NUMERICAL elapsed 353.37 seconds.

OPEN: discovery checkpoint 10500/13368; original {'exclusion': 5733, 'positivity': 4417, 'closed_after_splitting': 304, 'open': 46}; leaves {'exclusion': 5979, 'positivity': 5451, 'open': 78}; max depth 4; remaining chart volume 6304725/131072. NUMERICAL elapsed 390.85 seconds.

OPEN: discovery checkpoint 11000/13368; original {'exclusion': 5940, 'positivity': 4662, 'closed_after_splitting': 349, 'open': 49}; leaves {'exclusion': 6200, 'positivity': 5864, 'open': 89}; max depth 4; remaining chart volume 5203683/131072. NUMERICAL elapsed 422.47 seconds.

OPEN: discovery checkpoint 11500/13368; original {'exclusion': 6253, 'positivity': 4805, 'closed_after_splitting': 386, 'open': 56}; leaves {'exclusion': 6543, 'positivity': 6097, 'open': 104}; max depth 4; remaining chart volume 2069739/65536. NUMERICAL elapsed 441.91 seconds.

OPEN: discovery checkpoint 12000/13368; original {'exclusion': 6596, 'positivity': 4905, 'closed_after_splitting': 428, 'open': 71}; leaves {'exclusion': 6945, 'positivity': 6315, 'open': 136}; max depth 4; remaining chart volume 190629/8192. NUMERICAL elapsed 462.99 seconds.

OPEN: discovery checkpoint 12500/13368; original {'exclusion': 6848, 'positivity': 5077, 'closed_after_splitting': 496, 'open': 79}; leaves {'exclusion': 7267, 'positivity': 6796, 'open': 149}; max depth 4; remaining chart volume 119925/8192. NUMERICAL elapsed 502.15 seconds.

OPEN: discovery checkpoint 13000/13368; original {'exclusion': 7125, 'positivity': 5248, 'closed_after_splitting': 546, 'open': 81}; leaves {'exclusion': 7586, 'positivity': 7064, 'open': 152}; max depth 4; remaining chart volume 205695/32768. NUMERICAL elapsed 521.78 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 581, 'open': 89}; leaves {'exclusion': 7894, 'positivity': 7222, 'open': 166}; max depth 4; remaining chart volume 1233/8192. NUMERICAL elapsed 531.87 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 593, 'open': 77}; leaves {'exclusion': 7934, 'positivity': 7291, 'open': 144}; max depth 10; remaining chart volume 301275/2097152. NUMERICAL elapsed 6.09 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 607, 'open': 63}; leaves {'exclusion': 7956, 'positivity': 7372, 'open': 124}; max depth 10; remaining chart volume 267417/2097152. NUMERICAL elapsed 13.13 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 619, 'open': 51}; leaves {'exclusion': 7973, 'positivity': 7453, 'open': 100}; max depth 10; remaining chart volume 209853/2097152. NUMERICAL elapsed 18.27 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 627, 'open': 43}; leaves {'exclusion': 7983, 'positivity': 7526, 'open': 75}; max depth 10; remaining chart volume 152253/2097152. NUMERICAL elapsed 23.41 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 639, 'open': 31}; leaves {'exclusion': 7992, 'positivity': 7577, 'open': 50}; max depth 10; remaining chart volume 94653/2097152. NUMERICAL elapsed 26.92 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 652, 'open': 18}; leaves {'exclusion': 8011, 'positivity': 7626, 'open': 26}; max depth 10; remaining chart volume 37089/2097152. NUMERICAL elapsed 30.54 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 661, 'open': 9}; leaves {'exclusion': 8025, 'positivity': 7664, 'open': 11}; max depth 10; remaining chart volume 261/2097152. NUMERICAL elapsed 34.33 seconds.

OPEN: refinement complete; exact acceptance performed per certificate, independent replay pending. NUMERICAL additional elapsed 34.65862708300119 seconds.

OPEN: discovery checkpoint 13368/13368; original {'exclusion': 7384, 'positivity': 5314, 'closed_after_splitting': 661, 'open': 9}; leaves {'exclusion': 8046, 'positivity': 7702, 'open': 9}; max depth 16; remaining chart volume 189/134217728. NUMERICAL elapsed 3.77 seconds.

OPEN: refinement complete; exact acceptance performed per certificate, independent replay pending. NUMERICAL additional elapsed 4.10021366699948 seconds.

PROVED (verify_sources.py): the full copied STRAT11 proof dependencies appeared before the source snapshot was pinned; all 483 inherited files match that snapshot. The original provenance bank additionally names two absent transient PID files, STRAT9/codex.pid and STRAT10/codex.pid. inherited_replay.py checks every mathematical input and explicitly records those two operational omissions. Its overlay entry point is called without the source-writing main block.

OPEN: all 13,368 originals processed at depth 4, then retained leaves refined to depth 10 with products, then depth 16. Discovery accepted 8,046 exclusion and 7,702 positivity leaf certificates, with 9 OPEN leaves. Independent exact replay pending.

PROVED (verify_obstruction.py): the four additional OPEN roots 19750, 21058, 12407 and 15603 contain Q(sqrt(15)) equality limits, a triangle with weights 1/3 and two isolated vertices. Together with the five Q(sqrt(5)) two-edge limits, every one of the nine final OPEN leaves contains a point forbidding both requested strict certificate forms. Their connected constraint is zero, so none is a feasible counterexample.

NUMERICAL: largest recorded worker peak RSS across discovery/refinement was 717275136 bytes; final refinement parent peak was 264929280 bytes. The conservative bound 4*largest worker peak+parent peak is 3134029824 bytes (2.919 GiB); individual peaks need not coincide. The tensor LP implementation now allocates its constraint matrix once and reduces only active multiplier rows, avoiding the earlier large temporary copies. nice 5 remains sandbox-denied.

PROVED (verify_certificates.py): all retained new certificates and subdivision volumes replayed. NUMERICAL elapsed 239.0643102080212 seconds.

PROVED: all exact partial claims replayed; OPEN: global sign. NUMERICAL full replay elapsed 267.36866495900904 seconds.

PROVED (replay_all.py): all 15 exact checks passed. The independent certificate replay took 239.0643102080212 seconds; full replay took 267.36866495900904 seconds (NUMERICAL timings). Final original classification: 7384 direct exclusions, 5314 direct positivity, 661 fully closed after splitting, 9 OPEN. Final leaves: 8046 exclusion, 7702 positivity, 9 OPEN; split nodes 2389; maximum additional depth 16. Exact OPEN volume 3333609/32768 -> 189/134217728. Every remaining leaf has an exact strict-certificate obstruction. RESULT.md is final; all source fingerprints matched after replay.
