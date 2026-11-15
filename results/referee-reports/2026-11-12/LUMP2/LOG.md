# Referee audit log

Task: “Find every error, gap, overclaim and misattribution” in `paper/`.
Started 12 November 2026, 23:17 +04 (first recorded local work).

Scope: offline review; no agents, pushes, visible windows, or writes outside this directory. The current task's write restriction overrides global brain/checklist/mesh commands, which persist outside this directory. Existing reports are leads, not proof certificates. Manuscript sources will remain unchanged. Programs are saved before execution, numerical libraries use one thread, and each audit computation has a 240-second alarm.

## Initial reading

- Read the complete main manuscript and its four inputs, both author check programs, and the relevant earlier reports.
- **Error identified:** `paper/lumping.tex:115` states `K(7) in {3,4}`. The arguments only establish `3 <= K(7) <= 4`. A supremum of real-valued ratios need not be integral; no integrality theorem is stated or proved. `K7P_REPORT.md` itself explicitly records the interval and an unresolved rank-two case. Exact fix: replace the set membership by the interval bounds.
- The stated single-merge proof has no immediate sign or loop-convention failure. Its potential, Schur-complement, minimum, and strictness steps require independent checks below.
- No cited primary source text (Aldous–Fill, Lovász–Winkler, Hermon–Peres, Lyons–Peres) is present in this directory. External theorem numbers and historical attributions must remain “to check”; no browsing will be used.

## Second reading: precise quotient hypothesis

- **Formal error identified:** `paper/lumping.tex:270` only requires `f(u)=f(v)` and injectivity on `J=I\{u,v}`. This still permits a third state in the fibre of the merged pair. The rank-one proposition is false for those maps. Theorem 2 itself explicitly excludes them. An exact four-state independent-sampling counterexample will be recorded in `audit_inventory.py`; fix by adding `f^{-1}(hat v)={u,v}`.

## Independent exact random audit

- `audit_random.py`: all checks passed, {'networks': 46, 'merges': 445, 'entries': 19357, 'minimum_checks': 11782, 'set_tests': 3472, 'roots': 225}; elapsed 6.907 s, peak RSS 17612800 bytes.
- Largest tested one-merge ratio: 1.184758162. Every entry checked against direct quotient hitting solves, with exact rank-one and strict minimum-potential inequalities. Grounded identities tested at every root; stopping occupation equations, exact spectral PSD inequality, arbitrary partitions, hitting sets, periodic chains and complete graphs also passed.

## Independent symbolic and exact comb audit

- `audit_comb.py`: symbolic identities from graph cut masses passed for N=0,...,4 with independent t,r,alpha,ell. Under the specified scaling, all stated limits and both O(t^-5) centerings were verified symbolically.
- Direct killed-transition hitting solves passed at 25 points, N=0,...,4 and t=2,5/2,3,10,1000. Both sufficient conditions, original maximizer (a,c), quotient maximizer (a,b), both mean hitting corrections, and set-hitting comparisons passed exactly. Elapsed 16.189 s; peak RSS 81838080 bytes.
- All four rounded rows of Table 2 agree. The comb therefore proves the lower bounds 2,3,4 on 4,6,8 states, respectively; these are limiting suprema, with no finite attainment needed.

## Bounds, counterexample, and attribution inventory

- `audit_inventory.py` enumerated U(n) for 2<=n<=20; every manuscript Table 1 entry agrees. U(6)=3 and U(8)=4, proving the two claimed small cases when combined with the verified comb. K(7) is only bounded by the interval [3,4].
- Confirmed exact counterexample to the literal setup of Proposition 8: w_ij=1 on four states; f merges {0,1,2}, keeps {3}; u=0,v=1,J={2,3}; f is injective on J. At i=j=2, beta_i=0, original F_22=-3, but lifted quotient F_AA=-1/3. The stated rank-one identity therefore fails unless the missing fibre condition is supplied.
- Author check counts 100 networks / 850 merges and 20 comb points match the source. The second program has exactly 400 trials. It returns Boolean failure flags rather than failing the process; this is a reproducibility improvement, not a refutation.
- Manuscript/code SHA-256 snapshot saved; elapsed 0.005 s, peak RSS 18317312 bytes.

## Bounds, counterexample, and attribution inventory

- `audit_inventory.py` enumerated U(n) for 2<=n<=20; every manuscript Table 1 entry agrees. U(6)=3 and U(8)=4, proving the two claimed small cases when combined with the verified comb. K(7) is only bounded by the interval [3,4].
- Confirmed exact counterexample to the literal setup of Proposition 8: w_ij=1 on four states; f merges {0,1,2}, keeps {3}; u=0,v=1,J={2,3}; f is injective on J. At i=j=2, beta_i=0, original F_22=-3, but lifted quotient F_AA=-1/3. The stated rank-one identity therefore fails unless the missing fibre condition is supplied.
- Author check counts 100 networks / 850 merges and 20 comb points match the source. The second program has exactly 400 trials. It returns Boolean failure flags rather than failing the process; this is a reproducibility improvement, not a refutation.
- Manuscript/code SHA-256 snapshot saved; elapsed 0.006 s, peak RSS 18907136 bytes.

## Final report

- `REPORT.md` completed with verdict MAJOR: two required mathematical corrections, separately identified suggestions, a full proof audit, U(n) through 20, and an explicit to-check list for every unavailable external source. No additional theorem counterexample was found.
- `audit_report_check.py` independently checked all source hashes, the four report numerical rows against exact data, proposition numbering, evidence files and report structure. Minor transcription/rounding and inline-formatting errors in the draft report were corrected before delivery.
- Final check passed in 0.0059 s, peak RSS 18038784 bytes. No original paper file was changed.

## Final report

- `REPORT.md` completed with verdict MAJOR: two required mathematical corrections, separately identified suggestions, a full proof audit, U(n) through 20, and an explicit to-check list for every unavailable external source. No additional theorem counterexample was found.
- `audit_report_check.py` independently checked all source hashes, the four report numerical rows against exact data, proposition numbering, evidence files and report structure. Minor transcription/rounding and inline-formatting errors in the draft report were corrected before delivery.
- Final check passed in 0.0087 s, peak RSS 19120128 bytes. No original paper file was changed.
