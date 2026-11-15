---
name: p0245_uniform_kn_strict_local_min_with_holds_n4_to_16_2026_11_10
description: "P0245 holding walk: is uniform K_n a local minimum of E_pi C? Yes, strict modulo scale for n=4..16 (S_n-symmetry Hessian; soft mode (n-2,2), lambda 0.047 at n=16, ~ (log n)^2/n^2); global proof still open"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T11:25:05+02:00
  status: provisional
  evidence: ""
---

P0245 (Aldous-Fill Open Problem 6.30, the holding walk: is E_pi C >= (n-1)H_(n-1) for every reversible chain on n states,
holding allowed?). Uniform K_n attains (n-1)H_(n-1) exactly, and it is a STRICT LOCAL MINIMUM modulo scale for n = 4..16
(10 Nov 2026, an agent).

How it was checked:
- Coordinates: log edge conductances plus hold conductances h_s >= 0. The one-sided derivative in every hold is H_(n-1)/n > 0,
  so adding holding only raises E_pi C to first order. The edge gradient vanishes (1e-8).
- n = 4..8: the full dense Hessian (kn_local_min_check.py), one zero eigenvalue (scale), the rest positive.
- n = 6..16: by symmetry. The Hessian commutes with S_n on edges, so it has three eigenvalues: 0 on scale, lambda(n-1,1) on
  vertex potentials x_ij = a_i + a_j, and lambda(n-2,2) on the rest. kn_irrep_eigs.py takes one second directional
  derivative per part and solves E_pi C exactly by a dynamic programme over visited sets. It agrees with the dense check at
  n = 6, 7, 8 to six digits.
- The soft direction is always (n-2,2): reweighting edges without changing any vertex's total. lambda(n-2,2) is
  0.375, 0.279, 0.2154, 0.1720, 0.1408, 0.1177, 0.0999, 0.0861, 0.0750, 0.0660, 0.0586, 0.0524, 0.0472 for n = 4..16.
  lambda n^2/H_(n-1) rises slowly (3.27 at n=4 to 3.64 at n=16, the steps shrinking like 0.22/n). So the margin decays
  polynomially, roughly like (log n)^2/n^2, and never reaches zero at a finite n checked.
- A forecast made before the n = 9 and 10 runs (0.117 and 0.099) held: 0.1177 and 0.0999.

What it does NOT settle: the global inequality. Searches on Mac mini 1 (n = 6, 7, about 300 restarts) found no
counterexample (best gap >= -1.1e-15), but a local minimum plus a search is not a proof. A proof for all n would compute
lambda(n-2,2) in closed form and then needs a global argument.

Files: brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OPEN3/independent_check_agent/
(HOLDING_REDUCTION.md, kn_local_min_check.py, kn_irrep_eigs.py, kn_irrep_eigs_n9_12.out); GitHub commits 683d9749 (n=8)
and d4715b97 (n=9..16). What would change this: a closed form for lambda(n-2,2) going to zero, or a global counterexample.


UPDATE 10 Nov 12:0x (an agent): exact rational Hessian eigenvalues at K_n by a reduced DP (4 special vertices + an
exchangeable rest; kn_irrep_reduced.py, checked against the full DP at n = 5..13), n = 5..80: the soft eigenvalue
lambda(n-2,2) stays positive (0.0029944 at n = 80) and behaves like 4 H_{n-1}/n^2 (fit coefficient 4.04 on n >= 40;
lambda n^2 - 4H rises -1.37 -> -0.65 over n = 5..80; no closed form found, a 32-term exact ansatz failed). At finite
amplitude the bound holds on both K_n test lines (t in [-6, 6], n = 5..20; kn_softline.py) and on the whole soft x vertex
plane (25 x 25 grid, n = 5, 8, 12; kn_plane.py), smallest gap always next to the origin on the soft axis. Mini 1's ~70,000
random descents at n = 5, 6 found nothing below the bound (smallest gap -1.2e-14, float noise). Commits 97c1064d,
52269053, 57b5d37b. Still evidence, not a proof: directions touching more than four vertices are untested at finite amplitude.

UPDATE 10 Nov 12:2x (an agent): the soft eigenvalue's form. Fitted on n=30..65 in 60-digit arithmetic and tested on held-out n=66..80 (kn_lambda_models.py/.out): n^2 lambda(n-2,2) = 4 H_{n-1} - c H_{n-1}^2/n + O(H/n) with NO constant term (free constant -0.0001, holdout 4e-11). The earlier "lambda n^2 - 4H tends to about -0.6" read was wrong: that drift is the H^2/n term dying. [SETTLED later the same day: c = 4 exactly, from the closed form in the UPDATE below] c is NOT settled: 3.9 from the joint fit, 4.25-4.33 from extrapolating d_n=(4H-y)n/H^2 in 1/H (kn_lambda_c.py), both on a short 1/H range (0.20-0.28) - do not quote c. Commits 4b114819, d7f710d9. Next: derive the 4H leading term from the reduced DP.

UPDATE 10 Nov 12:4x: both edge-Hessian eigenvalues at uniform K_n have closed forms that match every DP value exactly at n = 4..80 (fitted on 5..44, so 4 and 45..80 are held out); commit b2bb60e0, kn_lambda_closed_form.py. With H = H_{n-1}, H2 = sum_{k<n} 1/k^2: lambda(n-1,1) = [H^2 + H2 - 2(n+1)H/(n(n-1)) + 2/(n(n-1)^2)]/(n-2); lambda(n-2,2) = 4[(n^2-2n+3)H - (n-1)(1+H^2+H2)]/(n^2(n-2)(n-3)). Both are positive for all n >= 4, and the H^2/n coefficient is exactly 4, which supersedes the 'c not settled' caveat above. Still open: derive the forms from the DP (they are guessed from data); the hold block has no formula yet. Earlier the same day the six-vertex and all-edge random directions with holds were all positive (n=8, 12; n=6..9).

UPDATE 10 Nov 12:50: the hold direction is settled with a proof. dE_pi C/dh at a hold of one vertex = H_{n-1}/n exactly (jump chain unchanged, each visit adds h/(n-1) steps, visits split evenly over the n vertices; checked exact n=5..20, kn_hold_derivative.py). Strictly positive one-sided derivatives in the holds plus a positive definite edge Hessian give a strict local min, so the hold block needs no formula. Only remaining gap for local minimality: prove the two edge-Hessian closed forms (or their positivity) for all n.

UPDATE 10 Nov 13:0x: lambda(n-1,1) is PROVED for all n (kn_star_proof.py): the star chain's state times have closed forms to order t^2 (kn_star_forms.py), checked symbolically against its recursions, and assembly gives the closed form identically. Projection argument: K_n critical + scale invariance => Hess*1 = 0, so the star curve reads the (n-1,1) eigenvalue. Hold side proved earlier. Only lambda(n-2,2)'s closed form (exact n=4..80) is still unproved; try a two-star chain (scale edges at two vertices, or the single edge 01) the same way.

UPDATE 10 Nov 13:1x: lambda(n-2,2) PROVED too (kn_edge_proof.py: single-edge chain, five state families, symbolic recursion check + boundary + assembly). So uniform K_n is a strict local min of E_pi C over edge weights and holds for EVERY n >= 4. Local only; the global question stays open. Scar from this step: in assembly, the start state's j = n-2 means H_j = H_{n-1} - 1/(n-1) - one subtraction, not two (a wrong index gave a nonzero residual that looked like a failed proof).

Independent check (an agent, 10 Nov 19:21): a from-scratch visited-set solver (40-digit mpmath, own directions)
reproduces both closed forms to 20 digits at n = 4..7, the hold derivative H_{n-1}/n, and the K_n-minus-an-edge basin
(t and value) at n = 4, 5, 6. Numbers only; the symbolic proofs for general n were not re-checked. Note and code:
briefs/OPEN3/audit_agent/KN_LOCAL_MIN_REFEREE_2026_11_10.md, p0245_kn_referee.py/.json.
