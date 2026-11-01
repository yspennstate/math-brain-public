# PROB10-02 / R17 — idea fixed before code: canonical greedy-embedding frontiers

Target remains the genuine Chvatal--Sankoff constant for two independent iid fair binary strings. No independent Bernoulli match array is introduced.

## Continuity and nonduplication

Controlling directive: `operations/PROB10_2026-09-20.md`.

Newest completed R17 report entering this run is `runs/prob10_2026-09-20/PROB10-02/20260920T1223Z_r17_symmetric_single_debt_run_macro_71e4.md`. It leaves the source interval unchanged while proving a stronger lower-bound information process and a separate run-macro recurrence. The H0021 handoff remains exactly as recorded in `operations/claims/H0021.md`: H0021 is released/unassigned, `Delta_near=2`, R16's six-run stagnation and two consumed recoveries are preserved, R17's H0021 unchanged streak is one, and navigation commit `c8891869a1335d67bada83f23f63f2ce09603565` remains the historical pointer.

Current same-source division is respected. P02 owns the covering/cone stationary upper dual and has a newer completed `2026-09-20T13-10-25Z__padic-type01-dual-report.md`; P13 owns the strip/boundary recursion and has a newer completed `2026-09-20T13-12-00Z__cesaro-block-transfer-and-carry-quotient.md`. This R17 attack uses neither covering labels nor strip gradients. It works instead with canonical greedy embeddings of candidate common words.

## New representation

For an infinite binary string `X`, define the greedy embedding endpoint `T_X(w)` of a finite word `w`: `T_X(empty)=0`, and `T_X(wc)` is the first index strictly after `T_X(w)` at which `X` equals `c`. For independent strings `(X,Y)`, attach to every word `w` the point

`P(w)=(T_X(w),T_Y(w))`.

Then `LCS(X_1^n,Y_1^n)>=k` iff some binary word `w` of length `k` has `P(w)<=(n,n)` coordinatewise.

At a fixed block depth `r`, delete every word whose point is coordinatewise dominated by another word of the same length, with a deterministic tie rule for identical points. The key proposed lemma is subtree domination: if `P(v)<=P(w)`, then for every suffix `z`, `P(vz)<=P(wz)`. Hence Pareto pruning is lossless for the existence question.

The second key point to prove before computation is a stopping-line property. For fixed `w`, the event that `w` survives Pareto pruning at depth `r` is measurable from the two prefixes through `T_X(w)` and `T_Y(w)`. Therefore, conditional on that event and those endpoints, the two residual tails are still independent iid fair binary strings. This should make the expected weighted population multiplicative across `r`-letter macro generations despite sibling dependence.

For `0<z<1`, define

`m_r(z)=E sum_{w in F_r} z^(T_X(w)+T_Y(w))`,

where `F_r` is the Pareto-minimal depth-`r` frontier. If the stopping-line lemma is correct, then for every integer `q>=1`, the recursively pruned macro tree has expected weighted population `m_r(z)^q` at depth `qr`. Consequently

`P(LCS_n >= qr) <= z^(-2n) m_r(z)^q`,

and whenever `m_r(z)<1`,

`gamma_2 <= U_r(z):=2 r log(1/z)/(-log m_r(z))`.

This is an exact finite-to-infinite transfer in the genuine two-source model; the only finite numerical task is to upper-certify `m_r(z)`.

## Three attacks for this run

1. **Attack A — prove the greedy-frontier stopping-line theorem and exact upper transfer.** Falsification target: check that Pareto-survival of a word really is measurable before either residual tail is used.
2. **Attack B — solve `r=1` analytically.** Immediate sibling pruning should give `m_1(z)=z^2/2+z^3/(2-z)`, strictly improving the unpruned Chvatal--Sankoff first-moment tree but still likely weaker than the current source upper endpoint.
3. **Attack C — exact `r=2` macro certificate.** Parameterize all four greedy endpoints by the start bit and the first three geometric run lengths. At a rational `z` (planned `z=1/3`), enumerate run lengths up to `M`, sum the retained Pareto weights exactly, and add a proved geometric tail bound. A useful mechanism target is to certify `m_2(z)<m_1(z)^2` and a rational upper such as `U_2(z)<0.857`. If this remains above the P02 source endpoint, record it only as auxiliary mechanism progress, not source movement.

A fourth falsification check will test the tempting but false finite-profile Markov shortcut: finite extension signatures can have spurious closed high-reward cycles because hidden deeper extension capacity is forgotten. Any explicit self-loop witness will be preserved rather than used as a Markov proof.
