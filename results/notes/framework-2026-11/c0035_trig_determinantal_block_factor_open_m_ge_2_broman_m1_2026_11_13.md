---
name: c0035_trig_determinantal_block_factor_open_m_ge_2_broman_m1_2026_11_13
description: "C0035 (Lyons ICM 2014 Question 5.4 / Duke 2003 Question 9.5: is the stationary determinantal process P_f on Z with f a degree-m trigonometric polynomial an (m+1)-block factor of an i.i.d. process?) still open for m >= 2 on 13 Nov 2026; m = 1 is Broman, AoP 33(2) 2005 (math/0503654); P_f is already known finitarily isomorphic to i.i.d., so only the explicit block-factor form is open"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T14:43:53.314Z
---

C0035, rank 28. f : T -> [0,1] is a trigonometric polynomial of degree m, so the determinantal process P_f on Z is
m-dependent. Is P_f an (m+1)-block factor of an i.i.d. process?
Source: Lyons, "Determinantal probability: basic properties and conjectures" (ICM 2014), Question 5.4. The same question is
Question 9.5 in Lyons, "Determinantal probability measures" (Publ. IHES 2003, math/0204324), where a higher-dimensional
version is also asked.

Status, checked 13 Nov 2026 (arXiv search plus an extended web search):
- m = 1: solved. E. Broman, "One-dependent trigonometric determinantal processes are two-block factors", Ann. Probab.
  33(2) 2005 (arXiv math/0503654), Theorem 1.3. The 2-block factor is explicit.
- m >= 2: no paper found that settles it. No higher-dimensional result found either.
- Context: when f is a trigonometric polynomial, P_f is already known to be finitarily isomorphic to an i.i.d. process
  (stated in Lyons math/0204324; the proof is attributed to Lyons-Steif, Duke 2003, not re-read). So the question is about the explicit (m+1)-block form, not about being a factor of i.i.d.
  Lyons notes that explicit block factors for trigonometric polynomials would give explicit i.i.d. factors for every P_f.
- Not every m-dependent process is an (m+1)-block factor (Burton-Goulet-Meester, AoP 1993, give, from memory and not re-read here, a 1-dependent process that is
  not a 2-block factor), so the determinantal structure has to be used.

Prior work: six runs between Sep and Oct, the last marked operationally retired, plus an unaudited sublattice-case attempt in
the ledger row. No verdict. A natural next step if picked up: check whether Broman's m = 1 construction (read it first; a
Fejer-Riesz factorization f = |g|^2 with deg g = m is the obvious handle) extends to m = 2. Test it numerically for m = 2 by matching the
3-point and 4-point correlations of a candidate 3-block map against det K_f.
Related: [[p0133_torus_ust_dual_homotopy_schramm_6_2_no_solution_found_leads_2026_11_13]] (same day's sweep).
