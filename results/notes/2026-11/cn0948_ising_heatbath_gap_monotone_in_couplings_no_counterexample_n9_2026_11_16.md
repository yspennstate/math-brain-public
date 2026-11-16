---
name: cn0948_ising_heatbath_gap_monotone_in_couplings_no_counterexample_n9_2026_11_16
description: "[PROVISIONAL] CN0948 (Levin-Peres 2nd ed. 26.1 Q2, p.359): is the heat-bath Ising Glauber spectral gap nonincreasing in each J_e? No counterexample in ~250k exact small cases (n<=9) plus hill-climb; evidence only, no paper"
metadata:
  type: project
status: provisional
---
CN0948 asks whether the spectral gap of continuous-time rate-1 heat-bath Glauber dynamics for the zero-field ferromagnetic
Ising model is nonincreasing in each coupling J_uv. The catalogue says cycles and mean field are proved.

Search, 16 Nov 2026, (work folder; scripts gapmono.py and climb.py): exact symmetrised generator (off-diagonal
-sqrt(q(x,y)q(y,x)), eigvalsh), central difference d=1e-4 per edge, cases with lambda2-lambda1 < 1e-6 skipped.
- Random graphs and J: s11 200k trials n<=7, s12 40k trials n<=8, s13 8k trials n<=9. Max d gap/dJ_e: 1.45e-10, 1.94e-10, 2.83e-10.
- Hill-climb c21 maximising max_e d gap/dJ_e over every connected labelled graph with n<=5 plus 300 random n=6 graphs,
  60 steps per restart: max 6.4e-10 after 900 of 6000 restarts.
- Every top row has J_e = 0 on the maximising edge (gap_plus = gap_minus to 12 digits): the derivative vanishes there by
  symmetry, so the maxima are finite-difference noise at a flat point. No interior point with a positive derivative was found.

Verdict: consistent with monotonicity on all small graphs tried. Evidence only, not a proof; nothing posted.
Column scar: in the s1*.tsv files deriv is column 9 ($(NF-2) is gap_minus; counting rows >1e-7 on it gave false hits).
Companion question CN0949 (distance, not gap) is NOT monotone: [[cn0949_ising_glauber_distance_not_monotone_in_couplings_certified_2026_11_16]].
Before attacking a catalogue row, search the web for it: [[open_problem_check_must_search_the_web_not_only_arxiv_titles_2026_11_16]].
What would change this: an interior point with derivative above 1e-7 that survives recomputation at d=1e-3 and in mpmath.
