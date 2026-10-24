# Aldous–Fill Open Problem 4.49(ii): closure package

Source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 4, Open Problem 4.49(ii).

Source question: whether the multicommodity-flow estimate

`inf_f psi(f) <= K tau_2 log n`

can hold with graph diameter `D` in place of `log n` for some universal finite constant `K`.

Result packaged here: **negative**. For every `M>0` there is a finite connected simple unweighted graph `G` for which

`F(G)/(tau_rel(G) D(G)) > M`.

The proof uses cones over sufficiently large fixed-degree bipartite Ramanujan graphs supplied by Marcus–Spielman–Srivastava. It needs only a direct weak metric-duality inequality derived from the Aldous–Fill source flow normalization.

Files:

- `main.tex`: self-contained proof and exact normalization.
- `check.py`: exact `fractions.Fraction` checker for the finite algebraic core.
- `check.out`: archived output of the executed checker; ends `ALL_EXACT_CHECKS_PASS`.

Independent audit evidence already present in the repository:

- `P26-AUDIT-C31-AF449-DIRECT-DUALITY-02 = PASS` in `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_16-59-00__run-report.md`.
- `C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS` in `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T14-01-41Z__report.md`.

Author/source theorem report used for the audited claim:

- `proofnet24/C31-kemeny-constant/runs/2026-09-16/2026-09-16_14-54-31__run-report.md`, claim `C31-AF449-RAMANUJAN-CONE-1`.

Historical note: the older projective-plane cone certificate with ratio about `2.066512` refutes only the stronger constant-two assertion; it is not the source-level closure argument.

Literature status: bounded searches on 2026-09-16 found the original problem still stated on Aldous–Fill's live Chapter 4 page and found no prior published resolution of this exact question. This package makes no priority claim; no exhaustive MathSciNet/zbMATH audit was available.

`POSTED.md` is intentionally not edited by this task. Shared-ledger/posting reconciliation is left to the coordinator/owner.
