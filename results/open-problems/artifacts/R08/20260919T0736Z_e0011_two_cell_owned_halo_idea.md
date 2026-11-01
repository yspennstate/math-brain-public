# R08 E0011 — two-cell owned-halo / backward-value idea

Methods this run: **B11 DUALIZE / B19 MAKE IT AN ALGORITHM / B27 SWAP THE QUANTIFIERS**.

Starting point: the certified `b16` terminal event uses the 18-cell patch `P18`, the maximal 17-label support-closed alphabet, owned hazard `D=214`, and a universal minimum over all stable entrance states with the six target vacancies frozen. The previous run proved that every remaining suppressed owned label is missing at least two support cells, so one-cell support closure is exhausted.

The new route is not to internalize an arbitrary larger halo or to rerun the full mixed-label Markov chain. First enumerate every two-cell support gap among the already-owned suppressed terminal clocks. Retain only pairs whose added cells are themselves already completely controlled by the old owned Harris family (their CO clocks and every incident O2 edge are already in the paid-for family), so adding the state coordinates does **not** enlarge the hazard or the distance-two dependency sigma-field.

For a retained pair, let `A_old(n,s)` be the exact backward successful-history weight for `n` remaining arrivals from the old 17-label alphabet. For the newly internalized labels `N`, define a disjoint additional language by requiring the **first** accepted arrival to be in `N` and every later accepted arrival to be old. Its exact weight at total length `m` is

`B_m(s) = sum_{ell in N} sum_t w(ell,s,t) A_old(m-1,t)`.

This is deliberately a one-new-mark language: it is disjoint from the old terminal event and can therefore be added without inclusion-exclusion.

B27 quantifier discipline: do **not** choose the new label or history after seeing the boundary. The event is fixed once and for all; then minimize its summed successful weight over **every** stable entrance state on the enlarged patch, including every legal value of the two newly exposed state cells. A positive minimum is a genuine universal certificate.

Research target for this run: find a fully old-owned two-cell pair for which the universal first-new-mark language has positive exact mass and improves the frozen terminal factor at the same rational Poisson mean `lambda=43/20`. Only after finding such a pair is an exact checker warranted.
