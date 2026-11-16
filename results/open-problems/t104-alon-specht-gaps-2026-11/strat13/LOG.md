# STRAT13 work log

2026-11-13 11:07 +04. OPEN: task received at workspace launch, 11:05 +04: “close the last 9 OPEN leaves of T104 5+1 region (11), N=6, by local collar bounds at the disconnected equality limits”. Read STRAT12/RESULT.md and STRAT11/RESULT.md, the exact obstruction bank, and the corner proof. The two-edge local theorem can be reused; a triangle local theorem is required. Shared mesh/checklist writes are denied by the sandbox. A read-only mesh query found no live claims; a snapshot at /private/tmp/strat13-mesh.sqlite3 holds the local claim. This snapshot does not publish coordination to other sessions. All new files stay in STRAT13; inherited files are read-only. No subagents. One process initially; at most four workers, below 3 GB.

2026-11-13 11:10 +04. OPEN (independent replay pending): rational physical charts computed for both types. Triangle active edge Jacobian has rank seven, with multipliers (21/4,31/18,31/18,31/18,31/18,31/18,31/18). Both charts admit c=1/6 tangent coercivity. Exact coefficient envelopes give combined quadratic remainder bounds 32 and 54; proposed l1 collar radii are 1/384 and 1/648, with T6 >= ||h||_1/12. Discovery now uses these collars plus the unmodified STRAT12 LP/Bernstein machinery.

2026-11-13 11:15 +04. PROVED (verify_collars.py): the independent exact replay closed all nine leaves: 271 positive Bernstein leaves, 178 exclusions, 12 collar leaves, 452 splits, maximum additional depth 55. All nine original-coordinate degree-two Taylor jets and both rational physical chart proofs replayed. NUMERICAL: this replay took 11.785881 seconds. OPEN: full inherited replay and the original STRAT10 accepted leaves are still being audited before stating the global theorem. An old STRAT10/replay_all.out records an unrelated pressure-family verification failure; this run does not rely on that optional family theorem. The original canonical-root cover uses only the moment ceilings and direct polynomial signs, whose exact premises are explicitly replayed by the new driver.

2026-11-13 11:17 +04. PROVED (verify_collars.py): added a second universal polynomial derivation of both local targets, directly from the six-vertex matrix definitions. It agrees identically with the invariant expression; this is independent of the Taylor and Farkas construction. NUMERICAL: discovery used two workers, largest worker peak RSS 222,756,864 bytes. The governor reported the four inherited exact replay workers at approximately 102–106 MB each at 11:16; shared machine state was ok. Process enumeration is sandbox-denied, so these snapshots are operational measurements, not an exhaustive simultaneous RSS trace.

2026-11-13 11:24 +04. PROVED (verify_collars.py): an independent polynomial-cancellation remainder argument gives M<=1533221743435914585899/50000000000000000000<32 for the two-edge chart and M<=5891344851651791485819/112500000000000000000<54 for the triangle chart. This audits the Hessian-based constants without using quotient differentiation. OPEN: physical-ball discovery is complete with no candidate OPEN leaves; final independent replay pending. PROVED (replay_all.py, inherited stage): the complete unmodified STRAT12 replay passed all 15 checks, including its 15,748 accepted certificates. NUMERICAL elapsed 290.390579 seconds. All original-cover scale premises also passed; its full leaf replay is in progress.

OPEN: candidate partition node 19750: {'positivity': 26, 'exclusion': 24, 'collar': 2}. NUMERICAL elapsed 5.058419417007826 seconds; exact replay pending.

OPEN: candidate partition node 15773: {'positivity': 20, 'exclusion': 24, 'collar': 1}. NUMERICAL elapsed 5.50024204197689 seconds; exact replay pending.

OPEN: candidate partition node 21058: {'positivity': 28, 'exclusion': 24, 'collar': 2}. NUMERICAL elapsed 5.489451665984234 seconds; exact replay pending.

OPEN: candidate partition node 20736: {'positivity': 46, 'exclusion': 5, 'collar': 1}. NUMERICAL elapsed 6.552147708978737 seconds; exact replay pending.

OPEN: candidate partition node 21550: {'positivity': 20, 'exclusion': 24, 'collar': 1}. NUMERICAL elapsed 4.823408833995927 seconds; exact replay pending.

OPEN: candidate partition node 12091: {'positivity': 48, 'exclusion': 5, 'collar': 1}. NUMERICAL elapsed 6.286250208009733 seconds; exact replay pending.

OPEN: candidate partition node 12407: {'positivity': 31, 'exclusion': 23, 'collar': 2}. NUMERICAL elapsed 5.7690686249989085 seconds; exact replay pending.

OPEN: candidate partition node 14175: {'positivity': 22, 'exclusion': 24, 'collar': 1}. NUMERICAL elapsed 4.604155250010081 seconds; exact replay pending.

OPEN: candidate partition node 15603: {'positivity': 30, 'collar': 1, 'exclusion': 25}. NUMERICAL elapsed 6.577256541000679 seconds; exact replay pending.

PROVED (verify_collars.py): all nine collar partitions replayed; zero OPEN leaves. NUMERICAL elapsed 11.785880999988876 seconds.

OPEN: candidate partition node 19750: {'positivity': 35, 'exclusion': 30, 'collar': 2}. NUMERICAL elapsed 8.811021166999126 seconds; exact replay pending.

OPEN: candidate partition node 15773: {'positivity': 31, 'exclusion': 28, 'collar': 2}. NUMERICAL elapsed 9.930109459004598 seconds; exact replay pending.

OPEN: candidate partition node 21058: {'positivity': 35, 'exclusion': 30, 'collar': 2}. NUMERICAL elapsed 9.90836508301436 seconds; exact replay pending.

OPEN: candidate partition node 20736: {'positivity': 61, 'exclusion': 5, 'collar': 2}. NUMERICAL elapsed 12.258881416986696 seconds; exact replay pending.

OPEN: candidate partition node 21550: {'positivity': 31, 'exclusion': 28, 'collar': 2}. NUMERICAL elapsed 9.531033167004352 seconds; exact replay pending.

OPEN: candidate partition node 12091: {'positivity': 63, 'exclusion': 5, 'collar': 2}. NUMERICAL elapsed 12.008600999979535 seconds; exact replay pending.

OPEN: candidate partition node 12407: {'positivity': 38, 'exclusion': 29, 'collar': 2}. NUMERICAL elapsed 10.606993708002847 seconds; exact replay pending.

OPEN: candidate partition node 14175: {'positivity': 33, 'exclusion': 28, 'collar': 2}. NUMERICAL elapsed 8.918352584005333 seconds; exact replay pending.

OPEN: candidate partition node 15603: {'positivity': 39, 'collar': 1, 'exclusion': 33}. NUMERICAL elapsed 10.65724691702053 seconds; exact replay pending.

PROVED (verify_collars.py): all nine collar partitions replayed; zero OPEN leaves. NUMERICAL elapsed 17.793481832981342 seconds.

2026-11-13 11:26 +04. PROVED (verify_collars.py): final physical-ball partition replay passed: 366 positivity leaves, 216 exclusions, 17 matrix-ball leaves, 590 splits, max added depth 72, zero OPEN. Exact chart volume is 189/134217728. NUMERICAL independent replay 17.793482 seconds. OPEN: only the ongoing original-cover audit remains before the global statement.

2026-11-13 11:28 +04. PROVED (verify_collars.py; inherited verify_formulation.py/verify_domain.py): audited the link between chart and physical constraints. Physical kappa=4*connected/D^2, physical eigenvalue ratio is the chart eigenvalue ratio, and the certified polynomial is 20 D^2 Delta T6. Canonical t>=1 is obtained by orienting a zero edge toward its larger-norm endpoint, t<=4 follows from its nonnegative degree, and the other ROOT bounds follow from edge signs and row bounds. Every new proof module has no floating literals; rational field signs and both exact partition identities were independently checked. OPEN: original cover audit remains in progress.

2026-11-13 11:29 +04. NUMERICAL: final physical-ball discovery completed in 51.288279 seconds with two workers, largest worker peak RSS 224,952,320 bytes. PROVED (verify_collars.py): the 599-leaf refinement satisfies leaves=splits+9 and preserves the exact input volume. OPEN: the independent original-root cover audit has reached 36,000 nodes without failure. All nine local conclusions, the original-coordinate expansions, and both independent remainder arguments have passed.

2026-11-13 11:31 +04. PROVED (verify_collars.py): separately audited the rational radius chains 40/15360=1/384 and 43/27864=1/648, and M*rho=1/12 for M=32,54. The matrix-distance derivative factor is 2 in both charts, giving c=1/24. Every exact center and all nine original-chart linear terms are now printed in RESULT.md, with complete quadratic/active-constraint jets in local_certificates.json. OPEN: the original-cover audit has reached 56,000 of 80,355 nodes without failure.

2026-11-13 11:32 +04. PROVED (verify_collars.py, with inherited cell replay in replay_all.py): audited strictness separately. All moment/fine-cell scale margins and every original/STRAT11 positive-leaf margin are strictly positive rationals. The low-scale theorem is strict as well. Thus combining the original cover with the new balls supports T6>0, rather than only T6>=0, on the connected region. The final driver will recheck these strict margins when it invokes verify_collars.py. OPEN: original-cover replay still running.

PROVED (verify_collars.py): all nine collar partitions replayed; zero OPEN leaves. NUMERICAL elapsed 14.991478666983312 seconds.

PROVED (replay_all.py): region (11), N=6, closed; zero OPEN leaves. NUMERICAL total replay elapsed 1093.2311507500126 seconds. All inherited fingerprints unchanged.

2026-11-13 11:35 +04. PROVED (replay_all.py): complete replay passed all 18 stages. Region (11) at N=6 is closed with T6>0 under its named hypotheses; zero OPEN leaves. All 522 supplied inherited files are byte-identical to the initial fingerprints. Exact final combined root ledger: 32,925 positive, 20,277 excluded, 17 physical-ball leaves, 53,218 splits, total volume 1152. NUMERICAL total 1093.231151 seconds; final local replay 14.991479 seconds. RESULT.md now states the full theorem, all hypotheses, expansions, proof bounds, coverage and replay command. Shared brain/checklist publication remains sandbox-denied; the complete durable result is recorded locally.
