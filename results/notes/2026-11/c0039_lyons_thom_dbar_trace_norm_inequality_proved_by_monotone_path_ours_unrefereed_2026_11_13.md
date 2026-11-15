---
name: c0039_lyons_thom_dbar_trace_norm_inequality_proved_by_monotone_path_ours_unrefereed_2026_11_13
description: "PAPER POSTED 14 Nov 2026 (github yspennstate/dbar-determinantal-trace-norm b116900, Zenodo doi 10.5281/zenodo.24209165, three independent audits). C0039 (Lyons ICM 2014 arXiv 1406.2707 Sec 5.2 p.23 = Lyons-Thom ETDS 2016 arXiv 1402.0969 after Lemma 7.8: is dbar(P_Q, P_Q') <= ||Q - Q'||_1 for all equivariant positive contractions, not only commuting ones? 'We do not know whether this inequality always holds.') ANSWERED YES by us on 13 Nov 2026, unrefereed: chop the segment into n steps, each step = a down-move by D_-/n then an up-move by D_+/n (D = Q'-Q), after shrinking both kernels into [delta/2, 1-delta/2]; every move is monotone, so Lyons-Thom Lemma 7.2 + their invariant monotone coupling theorem price it at its trace, and the triangle inequality sums to tau|D|. Holds wherever invariant monotone couplings exist (sofic groups; finite groups and finite sets unconditionally via Lyons Thm 2.9 + Strassen + averaging). Sharp: equality when Q <= Q'. Numerics: W1/tr-norm max exactly 1.0 on 3-6 points, never above"
metadata:
  node_type: memory
  status: verified
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T19:46:47.649Z
---

C0039 on the 200 list. Source: Russell Lyons, "Determinantal probability: basic properties and conjectures", ICM 2014,
arXiv 1406.2707, Sec 5.2 p.23; the question is from Lyons and Thom, "Invariant coupling of determinantal measures on
sofic groups", Ergodic Theory Dynam. Systems 36 (2016) 574-607, arXiv 1402.0969 v2 (final), text after Lemma 7.8, p.25:
"When Q and Q' commute, one can improve the bound in Lemma 7.8 by replacing the norm ... with the Schatten 1-norm ...
We do not know whether this inequality always holds". They prove dbar <= 6||Q-Q'|| (operator norm, Lemma 7.8) and
dbar <= 6 * 3^{2/3} ||Q-Q'||_1^{1/3} (Lemma 7.9, Powers-Stormer).

Status 13 Nov 2026: ANSWERED YES, by our own argument, UNREFEREED. Literature: arXiv searches and the 16 papers citing
1402.0969 (Semantic Scholar) give no answer; nearest are Austin 2412.13751 and Meszaros 1905.11459, about other things.

The proof (Gamma sofic, Q, Q' positive contractions in R(Gamma); same for R(Gamma, S)):
- Ingredients, both in Lyons-Thom: (a) Q1 <= Q2 gives a Gamma-invariant monotone coupling (their main theorem, survey
  Thm 5.6); (b) Lemma 7.2: under a monotone joining dbar = sum over a section of |P[X1(w)=0] - P[X2(w)=0]|, i.e.
  dbar(P_Q1, P_Q2) = tau(Q2 - Q1) when Q1 <= Q2. (c) dbar is a metric (relatively independent joining).
- Shrink: Q^delta := (1-delta)Q + (delta/2)I lies in [delta/2, 1-delta/2]. Q >= (1-delta)Q <= Q^delta, so
  dbar(P_Q, P_{Q^delta}) <= delta tau(Q) + delta/2 <= 3 delta/2. Same for Q'.
- Path: D := (1-delta)(Q'-Q) = D_+ - D_-, R_k := Q^delta + (k/n) D, S_k := R_k - D_-/n. For n >= 2/delta, S_k >= 0
  (R_k >= delta/2 and ||D_-/n|| <= 1/n); S_k <= R_k and S_k <= S_k + D_+/n = R_{k+1}, all contractions. So
  dbar(P_{R_k}, P_{R_{k+1}}) <= tau(D_-)/n + tau(D_+)/n = tau|D|/n.
- Sum: dbar(P_Q, P_Q') <= 3 delta + (1-delta)||Q-Q'||_1; let delta -> 0. Sharp: equality whenever Q <= Q' (Lemma 7.2).
- Finite groups, no soficity needed: Lyons survey Thm 2.9 (0 <= Q1 <= Q2 <= I gives P_Q1 dominated by P_Q2, Naimark
  dilation) + Strassen give a monotone coupling; averaging it over Gamma keeps it monotone and invariant. On any finite set
  E the same chain gives W1_Hamming(P_Q, P_Q') <= tr|Q - Q'|.
- Why Lyons-Thom missed it: Lemma 7.8 chains three monotone steps but prices each by operator norm; pricing by trace and
  cutting the segment into many comparable steps is the whole difference.

Numerics (scratchpad c0039, w1test.py, transport LP with Hamming cost, random complex Hermitian contractions, small
non-commuting perturbations, 40-step hill-climb): worst W1/tr|Q-Q'| exactly 1.000000 at N = 3, 4, 5, 6 (hundreds of
trials), never above; the hill-climb lands on comparable pairs. mono.py: for non-commuting Q1 <= Q2 a coupling supported
on {A subset of B} exists in every trial (N = 3, 4, 5; 460 trials), cost = tr(Q2 - Q1) to 1e-15.

Scar on the way: a hung child process (exited but pinned by a handle) wedged a chained background shell for 13 min, and
the transport LP called rounding-mismatched marginals infeasible; drop the redundant last row.

Posted 14 Nov 2026, single author (the author): public repo https://github.com/yspennstate/dbar-determinantal-trace-norm
(main b116900924db, README + LICENSE CC BY 4.0 + paper/main.tex + main.pdf, 7 pages, no code), Zenodo record 24209165,
doi 10.5281/zenodo.24209165, PDF md5 76581030901c6a6f0e88ef84a27674b1 checked on the record. Three independent audits
(audits/reports/2026/11/13/paper_audit_repo_paper_main_72ace5/, last MINOR EDIT 4 must / 17 should, all applied): the
math held each time (Remark determinant -s(1-s)/2 for the two rank-one projections, corollary LP check <= 2e-15). What
the audits made the paper say: the LT16 Lemma 7.8 route gives 6t >= 2||Q-Q'||, never the trace norm; the one-step
operator M = Q-(Q'-Q)_- would finish it if it were positive, and it is not (Remark); the commuting case is LS03; BPT26
and DM21 are cited after the corollary (finite-set optimal transport for DPPs). Paper sources kept at scratchpad
c0039/repo (session agent); a Codex referee (C0039R, commit 2498cd2d) was asked of an agent.
Still open beyond it: the d-bar distance for non-sofic Gamma (no invariant monotone coupling theorem there).

Related: [[c0034_lyons_orthogonal_union_coupling_open_rank_one_lyons_2003_codex_288_certs_2026_11_13]] (previous item,
same survey); [[c0033_lyons_determinantal_entropy_concavity_open_two_point_posted_codex_abc_partial_2026_11_13]];
[[c0035_trig_determinantal_block_factor_open_m_ge_2_broman_m1_2026_11_13]].

Next: independent referee pass on the proof (the step most worth attacking: Lemma 7.2 and the monotone-coupling theorem
are used for R(Gamma, S) with several orbits; check the normalisation of dbar and ||.||_1 agree there), then a short note
"The dbar distance between determinantal measures is bounded by the trace norm" for GitHub/Zenodo citing Lyons-Thom.
Consequence worth stating: Lemma 7.9's SOT-continuity statement follows with a linear rate.
