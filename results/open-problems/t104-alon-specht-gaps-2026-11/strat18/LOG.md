# STRAT18 work log

2026-11-13 16:34 +04: received task. Parent an agent owns workspace claim; no mesh writes required.

PROVED (source_hashes.json): copied inherited proof inputs byte for byte. Read STRAT17 RESULT.md in full and the 4+4 setup, trace interpolation, 3+4 tree and rank-boundary certificates. OPEN: three connected pair families and their lower-trace endpoints.

2026-11-13 16:41 +04:
PROVED (tree44.py): all six tree/tree isolate and maximal-lower-trace scalar polynomials have nonnegative rational coefficients (4,536–6,075 terms). Positive finite and leading-padding coefficients give strictness for positive fluxes.
PROVED (boundary44.py): seven mixed/rank boundary corner families pass exact rational 2x2 or 4x4 PSD coefficient checks, including a uniform T* margin 1/100.
PROVED (padding44.py, exploratory construction checked; full replay pending): at inverse-padding endpoints 0 and 1/6, every negative derivative coefficient matrix is PSD.
PROVED (lower44.py): twelve exact Bernstein controls show the universal 4+4 maximal lower-trace comparison F_k(k-7)>=F_6(0)+3/10, using all 0<=tau<=4. No isolate margin is spent. OPEN: final integrated replay and independent formula audit remain before the class theorem is finalized.

2026-11-13 16:47 +04:
PROVED (audit44.py): exact rational fixtures agree with the original centered normalized definition, including a feasible lower edge.
PROVED (symbolic44.py): twenty universal sparse polynomial identities identify the tensor numerators with a separate direct 8x8 construction. This audits every connected endpoint, including the lower-trace relaxation.
PROVED (padding44.py): all twenty inverse-padding derivative endpoint checks pass, so k=6 is hardest for every connected endpoint pair.
PROVED (symmetric44.py): two balanced squares have T*_8=4/3 and T*_infinity=5/2 (T_8=1/3, T_infinity=5/8); stars and selected K4 closures are also positive. Only two equal edges give zero among these fixtures.
PROVED (setup35.py): triangle corner reduction and five-part K_u concavity transfer to 3+5, including fixed lower trace. OPEN: connected 3+5 signs (both triangle corners against three trees, rank<=2, rank3) and maximal lower endpoints.
RESULT.md now records the complete 4+4 argument, equality reasoning, margins, and exact remaining disconnected scope. OPEN: final combined replay receipt is pending.

PROVED (replay_all.py): 32 stages PASS. NUMERICAL runtime 79.25257162502385 seconds; peak aggregate upper bound 119717888 bytes.

2026-11-13 16:49 +04 final audit:
PROVED (replay_all.py; replay_summary.json): all 32 stages PASS (24 inherited, 8 new). All 64 proof-input hashes and 6 generated receipt hashes were independently rechecked after replay. All 52 source files in ../STRAT17 remain byte-identical to their pinned copies, including all reused STRAT16 and STRAT15 inputs. No source-folder mutation occurred.
NUMERICAL: 79.252571625 seconds; child peak 99,418,112 bytes, parent peak 20,299,776 bytes, conservative aggregate 119,717,888 bytes. Total workspace files 1,233,798 bytes at the final audit, far below 500 MB. No solver, subagent, process pool, or accelerated mode was used.
PROVED (replay_all.py and RESULT.md): the requested 4+4 class is closed with arbitrary lower components for every N>=8 and fixed-graph infinity. Equality is exactly two equal edges and isolates. Boundary endpoint T* margin 1/100 and universal lower endpoint gain 3/10 are retained.
PROVED (setup35.py): requested optional 3+5 setup is complete. OPEN: 3+5 connected signs and lower endpoints; the full disconnected D=2 statement still requires 3+5, 4+5 and 5+5 outside inherited S5=0 cases.
Task: “STRAT18: T104 split 4+4” — received 2026-11-13 16:34 +04; completed 16:49 +04.

PROVED (replay_all.py): 32 stages PASS. NUMERICAL runtime 127.01633729200694 seconds; peak aggregate upper bound 125255680 bytes.
