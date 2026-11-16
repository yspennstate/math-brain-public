# STRAT15 work log

2026-11-13 12:44 +04. Task received: close the T104 5+1 class for every N >= 7. Read the STRAT14, STRAT13, STRAT12, STRAT11 and STRAT10 results and STRAT10 FINALIZE. Source tree is read-only for this task. No subagents. Shared mesh registration, digest, claim and assert failed with a read-only database; checklist registration was denied by the filesystem sandbox. New artifacts stay in the isolated STRAT15 workspace. NUMERICAL compute state: owner_away_open, warn CPU saturation; use single-thread libraries and no more than two discovery processes initially.

OPEN: exact quadratic extraction, inventory and a possible padding comparison are being investigated. No inherited N=6 positivity certificate is yet asserted for N>=7.

PROVED (inventory.py): exact structural inventory has 8,366 non-all-N positive leaves, 17 collar leaves, the independent corner ball and 24,559 inherited all-N positive leaves. A separate exclusion audit identified the N-dependent premise issue.

PROVED (verify_target.py, verify_padding.py): exact q coefficients, degree-two compactification on the closed interval u in [0,1/2], infinity normalization and physical padding identity all passed coefficientwise checks.

PROVED (local_uniform.py): uniform physical local bounds hold through infinity with matrix coefficient 1/24, radii 1/4000 (edges) and 1/12900 (triangle). A multinomial coefficient envelope gives remainder constants 8 and 25. All 17 inherited collar boxes pull back into the new charts. Independent full partition replay is pending.

PROVED (domain_audit.py): 19,273 exclusions transfer and 1,004 require new sign checks. Discovery now has 9,370 input boxes and two single-thread workers. Full inherited replays started in byte-identical temporary copies, sequentially, with a runtime pool cap of two. Supplied sources remain pinned and untouched.

PROVED (unchanged STRAT14/replay_all.py, invoked by replay_all.py): the complete connected n=5 proof replay passed in a byte-identical temporary copy. NUMERICAL elapsed 698.689172 seconds. The unchanged STRAT13 full replay is now running. A separate exact traversal independently re-derived the full extended input-frontier volume as 1152.

OPEN: The first discovery pass has five unresolved boxes so far; the others have exact positive controls or exact exclusions. A refinement driver is ready. Some stored control checks are exclusions, so the final ledger will classify boxes by their actual proof, rather than calling every accepted box positive.

PROVED partial (refine.py; independent verify_new.py replay pending): the first eight unresolved input boxes closed using exact constraint-product certificates and five bisections, producing thirteen certificate leaves. No OPEN refinement leaf remains at this checkpoint. The separate two-worker first pass continues over the rest of the 9,370 boxes.

PROVED partial (discover.py, refine.py; independent replay pending): the complete 9,370-box first pass finished; all thirteen failures closed with five bisections and eighteen refinement positivity leaves. READY.json freezes both banks. NUMERICAL first-pass time 1973.8 seconds and conservative process-memory bound 993,910,784 bytes; recorded refinement peak 431,964,160 bytes.

PROVED (replay_all.py): the unchanged STRAT13 full replay passed in its byte-identical temporary copy. NUMERICAL elapsed 1364.214888 seconds. Both inherited complete replays and all four added all-N premise checks passed; verify_target.py and verify_padding.py passed again. The independent new partition replay is now running against 21 pinned new proof inputs.

OPEN / replay correction: the first new-stage worker check stopped because spawned children inherited STRAT12 at the front of sys.path and imported its identically named N=6 exact_bernstein module. This produced a positive recomputed margin for the wrong target, which disagreed with the saved new margin. The guard correctly rejected it. No certificate or mathematical input changed. verify_new.py now restores STRAT15 at the front before spawning and asserts the exact module path. PROVED (check_spawn.py): a spawned process replayed all twelve controls of four actual records with the correct extended target.

NUMERICAL / operational: failed_replay_1.json and failed_replay_1.out preserve the first attempt. replay_all.py --resume retains the six completed inherited PASS stages only after checking the unchanged source manifest and both full replay receipts, then reruns the target identities, spawn regression and complete new stage. A fresh replay_all.py without --resume always runs the full inherited copies again.

PROVED (verify_new.py, replay_all.py): the corrected independent replay passed every new residual, all local bounds and collars, the exact complete partition and the disconnected radial endpoint premises. Final counts: 33,848 positive, 19,359 excluded, 17 collars, 53,223 splits and zero OPEN leaves. The root volume is exactly 1152. All 789 supplied files and 22 new pinned proof inputs are unchanged. The theorem holds for every integer N>=7 and the continuous formal target for real q>=1, including the N=infinity limit. No counterexample exists in this class.

NUMERICAL: all ten final stages passed. Total recorded replay execution 3452.320961 seconds, including the rejected import attempt and full successful new retry; successful new stage 1309.644491 seconds. New exact replay conservative process-memory bound 814,129,152 bytes. First-pass discovery bound 993,910,784 bytes; largest recorded refinement-process peak 431,964,160 bytes. Per-phase bounds are recorded; sandbox denial of ps prevented an independent whole-session aggregate RSS sample.

OPEN: This closes the requested 5+1 class, not every disconnected graph whose components have at most five vertices. RESULT.md lists the remaining component combinations outside this theorem, STRAT7 padding and the S5=0 class.

PROVED (replay_all.py manifest audit), 2026-11-13 14:00 +04: final SHA-256 audit confirmed all 789 supplied files and 22 new pinned proof inputs unchanged. All ten final replay stages are PASS, the remaining-box list is empty, and the terminal-count identity is 33,848+19,359+17=53,223+1. RESULT.md now states the completed theorem, exact coefficients and local constants, replay timing and the separate broader OPEN component families.

Task: “STRAT15: close the T104 5+1 class for every N >= 7” — received 2026-11-13 12:44 +04; completed 2026-11-13 14:00 +04.

OPEN: discovery 100/9370; {'positive': 100}; NUMERICAL seconds 15.1, conservative memory 666378240 bytes

OPEN: discovery 200/9370; {'positive': 200}; NUMERICAL seconds 27.6, conservative memory 666378240 bytes

OPEN: discovery 300/9370; {'positive': 300}; NUMERICAL seconds 41.5, conservative memory 666378240 bytes

OPEN: discovery 400/9370; {'positive': 400}; NUMERICAL seconds 61.1, conservative memory 666378240 bytes

OPEN: discovery 500/9370; {'positive': 500}; NUMERICAL seconds 79.8, conservative memory 666378240 bytes

OPEN: discovery 600/9370; {'positive': 600}; NUMERICAL seconds 94.8, conservative memory 666378240 bytes

OPEN: discovery 700/9370; {'positive': 700}; NUMERICAL seconds 111.2, conservative memory 666378240 bytes

OPEN: discovery 800/9370; {'positive': 800}; NUMERICAL seconds 126.9, conservative memory 666378240 bytes

OPEN: discovery 900/9370; {'positive': 900}; NUMERICAL seconds 143.9, conservative memory 666378240 bytes

OPEN: discovery 1000/9370; {'positive': 1000}; NUMERICAL seconds 162.7, conservative memory 666378240 bytes

OPEN: discovery 1100/9370; {'positive': 1100}; NUMERICAL seconds 184.1, conservative memory 666378240 bytes

OPEN: discovery 1200/9370; {'positive': 1200}; NUMERICAL seconds 199.7, conservative memory 666378240 bytes

OPEN: discovery 1300/9370; {'positive': 1300}; NUMERICAL seconds 217.3, conservative memory 666378240 bytes

OPEN: discovery 1400/9370; {'positive': 1400}; NUMERICAL seconds 238.5, conservative memory 706912256 bytes

OPEN: discovery 1500/9370; {'positive': 1500}; NUMERICAL seconds 254.3, conservative memory 707174400 bytes

OPEN: discovery 1600/9370; {'positive': 1598, 'open': 2}; NUMERICAL seconds 274.1, conservative memory 708812800 bytes

OPEN: discovery 1700/9370; {'positive': 1696, 'open': 4}; NUMERICAL seconds 293.3, conservative memory 708812800 bytes

OPEN: discovery 1800/9370; {'positive': 1796, 'open': 4}; NUMERICAL seconds 309.4, conservative memory 708812800 bytes

OPEN: discovery 1900/9370; {'positive': 1896, 'open': 4}; NUMERICAL seconds 325.4, conservative memory 709730304 bytes

OPEN: discovery 2000/9370; {'positive': 1996, 'open': 4}; NUMERICAL seconds 340.5, conservative memory 709730304 bytes

OPEN: discovery 2100/9370; {'positive': 2096, 'open': 4}; NUMERICAL seconds 353.7, conservative memory 709730304 bytes

OPEN: discovery 2200/9370; {'positive': 2196, 'open': 4}; NUMERICAL seconds 370.9, conservative memory 714907648 bytes

OPEN: discovery 2300/9370; {'positive': 2296, 'open': 4}; NUMERICAL seconds 387.6, conservative memory 715005952 bytes

OPEN: discovery 2400/9370; {'positive': 2396, 'open': 4}; NUMERICAL seconds 412.4, conservative memory 718446592 bytes

OPEN: discovery 2500/9370; {'positive': 2496, 'open': 4}; NUMERICAL seconds 430.2, conservative memory 718446592 bytes

OPEN: discovery 2600/9370; {'positive': 2596, 'open': 4}; NUMERICAL seconds 455.3, conservative memory 720314368 bytes

OPEN: discovery 2700/9370; {'positive': 2696, 'open': 4}; NUMERICAL seconds 478.2, conservative memory 723722240 bytes

OPEN: discovery 2800/9370; {'positive': 2796, 'open': 4}; NUMERICAL seconds 498.9, conservative memory 728834048 bytes

OPEN: discovery 2900/9370; {'positive': 2896, 'open': 4}; NUMERICAL seconds 520.8, conservative memory 728834048 bytes

OPEN: discovery 3000/9370; {'positive': 2996, 'open': 4}; NUMERICAL seconds 533.5, conservative memory 728834048 bytes

OPEN: discovery 3100/9370; {'positive': 3096, 'open': 4}; NUMERICAL seconds 545.7, conservative memory 728834048 bytes

OPEN: discovery 3200/9370; {'positive': 3196, 'open': 4}; NUMERICAL seconds 570.1, conservative memory 729423872 bytes

OPEN: discovery 3300/9370; {'positive': 3296, 'open': 4}; NUMERICAL seconds 597.7, conservative memory 729423872 bytes

OPEN: discovery 3400/9370; {'positive': 3396, 'open': 4}; NUMERICAL seconds 617.2, conservative memory 757538816 bytes

OPEN: discovery 3500/9370; {'positive': 3496, 'open': 4}; NUMERICAL seconds 636.0, conservative memory 757538816 bytes

OPEN: discovery 3600/9370; {'positive': 3596, 'open': 4}; NUMERICAL seconds 664.4, conservative memory 757538816 bytes

OPEN: discovery 3700/9370; {'positive': 3696, 'open': 4}; NUMERICAL seconds 683.5, conservative memory 759177216 bytes

OPEN: discovery 3800/9370; {'positive': 3796, 'open': 4}; NUMERICAL seconds 703.2, conservative memory 759177216 bytes

OPEN: discovery 3900/9370; {'positive': 3895, 'open': 5}; NUMERICAL seconds 729.9, conservative memory 759177216 bytes

OPEN: discovery 4000/9370; {'positive': 3995, 'open': 5}; NUMERICAL seconds 748.3, conservative memory 760832000 bytes

OPEN: discovery 4100/9370; {'positive': 4095, 'open': 5}; NUMERICAL seconds 770.6, conservative memory 765616128 bytes

OPEN: discovery 4200/9370; {'positive': 4195, 'open': 5}; NUMERICAL seconds 792.6, conservative memory 778608640 bytes

OPEN: discovery 4300/9370; {'positive': 4295, 'open': 5}; NUMERICAL seconds 807.8, conservative memory 783523840 bytes

OPEN: discovery 4400/9370; {'positive': 4395, 'open': 5}; NUMERICAL seconds 822.3, conservative memory 788504576 bytes

OPEN: discovery 4500/9370; {'positive': 4495, 'open': 5}; NUMERICAL seconds 839.1, conservative memory 788979712 bytes

OPEN: discovery 4600/9370; {'positive': 4595, 'open': 5}; NUMERICAL seconds 855.7, conservative memory 794157056 bytes

OPEN: discovery 4700/9370; {'positive': 4695, 'open': 5}; NUMERICAL seconds 877.3, conservative memory 804478976 bytes

OPEN: discovery 4800/9370; {'positive': 4795, 'open': 5}; NUMERICAL seconds 897.4, conservative memory 805052416 bytes

OPEN: discovery 4900/9370; {'positive': 4895, 'open': 5}; NUMERICAL seconds 919.8, conservative memory 816472064 bytes

OPEN: discovery 5000/9370; {'positive': 4995, 'open': 5}; NUMERICAL seconds 941.2, conservative memory 822190080 bytes

OPEN: discovery 5100/9370; {'positive': 5095, 'open': 5}; NUMERICAL seconds 969.4, conservative memory 828137472 bytes

OPEN: discovery 5200/9370; {'positive': 5195, 'open': 5}; NUMERICAL seconds 992.7, conservative memory 828809216 bytes

OPEN: discovery 5300/9370; {'positive': 5295, 'open': 5}; NUMERICAL seconds 1018.9, conservative memory 873750528 bytes

OPEN: discovery 5400/9370; {'positive': 5395, 'open': 5}; NUMERICAL seconds 1041.9, conservative memory 874405888 bytes

OPEN: discovery 5500/9370; {'positive': 5495, 'open': 5}; NUMERICAL seconds 1063.2, conservative memory 875569152 bytes

OPEN: discovery 5600/9370; {'positive': 5595, 'open': 5}; NUMERICAL seconds 1080.9, conservative memory 876175360 bytes

OPEN: discovery 5700/9370; {'positive': 5695, 'open': 5}; NUMERICAL seconds 1115.3, conservative memory 876978176 bytes

OPEN: discovery 5800/9370; {'positive': 5795, 'open': 5}; NUMERICAL seconds 1144.4, conservative memory 887087104 bytes

OPEN: discovery 5900/9370; {'positive': 5895, 'open': 5}; NUMERICAL seconds 1170.8, conservative memory 897982464 bytes

OPEN: discovery 6000/9370; {'positive': 5992, 'open': 8}; NUMERICAL seconds 1199.8, conservative memory 899588096 bytes

OPEN: discovery 6100/9370; {'positive': 6092, 'open': 8}; NUMERICAL seconds 1229.7, conservative memory 899588096 bytes

OPEN: discovery 6200/9370; {'positive': 6192, 'open': 8}; NUMERICAL seconds 1267.5, conservative memory 899588096 bytes

OPEN: discovery 6300/9370; {'positive': 6292, 'open': 8}; NUMERICAL seconds 1300.5, conservative memory 899588096 bytes

OPEN: discovery 6400/9370; {'positive': 6392, 'open': 8}; NUMERICAL seconds 1331.7, conservative memory 899588096 bytes

OPEN: discovery 6500/9370; {'positive': 6492, 'open': 8}; NUMERICAL seconds 1360.0, conservative memory 899588096 bytes

OPEN: discovery 6600/9370; {'positive': 6592, 'open': 8}; NUMERICAL seconds 1380.0, conservative memory 899588096 bytes

OPEN: discovery 6700/9370; {'positive': 6692, 'open': 8}; NUMERICAL seconds 1402.6, conservative memory 899588096 bytes

OPEN: discovery 6800/9370; {'positive': 6792, 'open': 8}; NUMERICAL seconds 1425.8, conservative memory 899588096 bytes

OPEN: discovery 6900/9370; {'positive': 6892, 'open': 8}; NUMERICAL seconds 1452.9, conservative memory 899588096 bytes

OPEN: discovery 7000/9370; {'positive': 6992, 'open': 8}; NUMERICAL seconds 1479.6, conservative memory 899588096 bytes

OPEN: discovery 7100/9370; {'positive': 7092, 'open': 8}; NUMERICAL seconds 1509.6, conservative memory 899588096 bytes

OPEN: discovery 7200/9370; {'positive': 7187, 'open': 13}; NUMERICAL seconds 1543.5, conservative memory 899588096 bytes

OPEN: discovery 7300/9370; {'positive': 7287, 'open': 13}; NUMERICAL seconds 1569.6, conservative memory 899588096 bytes

OPEN: discovery 7400/9370; {'positive': 7387, 'open': 13}; NUMERICAL seconds 1592.6, conservative memory 899588096 bytes

PROVED partial (refine.py): exact accepted refinements; independent replay pending; {'certificates': 18, 'split': 5}.

OPEN: discovery 7500/9370; {'positive': 7487, 'open': 13}; NUMERICAL seconds 1618.3, conservative memory 900276224 bytes

OPEN: discovery 7600/9370; {'positive': 7587, 'open': 13}; NUMERICAL seconds 1646.7, conservative memory 908632064 bytes

OPEN: discovery 7700/9370; {'positive': 7687, 'open': 13}; NUMERICAL seconds 1668.1, conservative memory 911712256 bytes

OPEN: discovery 7800/9370; {'positive': 7787, 'open': 13}; NUMERICAL seconds 1691.3, conservative memory 912236544 bytes

OPEN: discovery 7900/9370; {'positive': 7887, 'open': 13}; NUMERICAL seconds 1714.1, conservative memory 912236544 bytes

OPEN: discovery 8000/9370; {'positive': 7987, 'open': 13}; NUMERICAL seconds 1743.7, conservative memory 923639808 bytes

OPEN: discovery 8100/9370; {'positive': 8087, 'open': 13}; NUMERICAL seconds 1752.5, conservative memory 923639808 bytes

OPEN: discovery 8200/9370; {'positive': 8187, 'open': 13}; NUMERICAL seconds 1764.7, conservative memory 923639808 bytes

OPEN: discovery 8300/9370; {'positive': 8287, 'open': 13}; NUMERICAL seconds 1773.0, conservative memory 924000256 bytes

OPEN: discovery 8400/9370; {'positive': 8387, 'open': 13}; NUMERICAL seconds 1788.2, conservative memory 926556160 bytes

OPEN: discovery 8500/9370; {'positive': 8487, 'open': 13}; NUMERICAL seconds 1806.8, conservative memory 926556160 bytes

OPEN: discovery 8600/9370; {'positive': 8587, 'open': 13}; NUMERICAL seconds 1825.0, conservative memory 926556160 bytes

OPEN: discovery 8700/9370; {'positive': 8687, 'open': 13}; NUMERICAL seconds 1842.5, conservative memory 926556160 bytes

OPEN: discovery 8800/9370; {'positive': 8787, 'open': 13}; NUMERICAL seconds 1861.7, conservative memory 926556160 bytes

OPEN: discovery 8900/9370; {'positive': 8887, 'open': 13}; NUMERICAL seconds 1879.9, conservative memory 926556160 bytes

OPEN: discovery 9000/9370; {'positive': 8987, 'open': 13}; NUMERICAL seconds 1898.6, conservative memory 937648128 bytes

OPEN: discovery 9100/9370; {'positive': 9087, 'open': 13}; NUMERICAL seconds 1917.3, conservative memory 948396032 bytes

OPEN: discovery 9200/9370; {'positive': 9187, 'open': 13}; NUMERICAL seconds 1936.8, conservative memory 959209472 bytes

OPEN: discovery 9300/9370; {'positive': 9287, 'open': 13}; NUMERICAL seconds 1958.9, conservative memory 972660736 bytes

OPEN: discovery 9370/9370; {'positive': 9357, 'open': 13}; NUMERICAL seconds 1973.8, conservative memory 993910784 bytes

PROVED partial (refine.py): exact accepted refinements; independent replay pending; {'certificates': 18, 'split': 5}.

PROVED (verify_new.py): complete canonical root for real q>=1 including infinity. All new exact controls and collar pullbacks passed. NUMERICAL seconds 1309.1322185409954.

PROVED (replay_all.py): all required exact replays passed. NUMERICAL seconds 3452.320960833982.
