You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/, sources/ of another run):
open problem I0071, Problem 7 of A. Agresti and M. Veraar's survey on nonlinear SPDEs and (stochastic) maximal regularity
(arXiv:2501.18561v5; NoDEA 2025, DOI 10.1007/s00030-025-01090-2): global well-posedness of the reaction-diffusion system (8.14)
with transport noise under conditions (1)-(6) (nonnegative data, globally Lipschitz g_i vanishing on the face y_i = 0,
quasi-positivity, local Lipschitz growth of order h, mass control, and the triangular condition R f(y) <= (1 + sum y_i) r with R
invertible lower triangular with nonnegative entries), on T^d or R^d, l >= 2, plus the follow-up on superlinear noise.

The claim is PARTIAL: on the torus T^d, d >= 2 (d = 1 by a dummy variable), with uniform stochastic parabolicity (P)
nu_i I - (1/2) sum_n b_{n,i} (x) b_{n,i} >= (mu/2) I, Holder transport coefficients that may differ between species, need not be
divergence free or small, conditions (1)-(6), any finite h admitted by the local theory, and nonnegative data in the local-theory
class, the maximal solution is global (P(sigma = infinity) = 1). The proof (REPORT section 2): a polynomial energy Phi_m with mixed
monomials compatible with the triangular cone (2.1), a Hessian estimate controlling the leading transport Ito correction (the
"mixed-Hessian estimate (11)", 2.2), zero-order noise and the full Ito formula (2.3), a tail bound without martingale absorption
(2.4), and closing the survey's blow-up criterion (2.5). Not claimed: R^d, boundary conditions, superlinear noise.

Break it if it is wrong.
1. Get the survey and the Agresti-Veraar papers the report relies on (reaction-diffusion with transport noise I and II, the global
   well-posedness paper whose Theorem 5.2 it cites, and any triangular-structure deterministic sources such as Fellner-Morgan-Tang
   or Fitzgibbon-Morgan-Tang, and Milesis-Salins 2026) into sources/ as plain text from arXiv, independently of claim_files/sources.
   State exactly Problem 7, (8.14), Assumption 8.4 (with the correct sign of the parabolicity condition), the local theorem
   (Theorem 8.6 or the paper's version), the blow-up criterion used, and check that REPORT restates them correctly.
2. Check the proof line by line. In particular: (a) the energy Phi_m: is it positive definite on the cone, and does the triangular
   condition (T) really give grad Phi_m . f <= C(1 + Phi_m) with constants independent of the solution? Check the construction of
   the mixed weights for l = 2 and l = 3 by hand. (b) the transport Ito term: with species-dependent b_{n,i}, the Ito correction
   contains mixed terms sum_n (b_{n,i}.grad u_i)(b_{n,j}.grad u_j) d_ij Phi_m; is it really dominated by the dissipation
   sum_i nu_i d_ii Phi_m |grad u_i|^2 under (P) alone, uniformly in m? This is the step most likely to fail: if the species
   transports differ and Phi_m has mixed second derivatives, the matrix of quadratic forms need not be positive. Try to build a
   counterexample to estimate (11) for l = 2 with b_{.,1} != b_{.,2}. (c) zero-order noise: globally Lipschitz g with g_i = 0 on
   the face y_i = 0; does the Hessian trace grow at most like Phi_m? (d) the tail bound and its stopping times; integrability of
   the stochastic integral; (e) does the obtained L^m bound for large m satisfy the survey's blow-up criterion in the critical
   space used, for every admissible (p, q, delta, kappa)? (f) positivity of the solution, which the energy argument needs.
3. Ask the hard question: is this already in the literature (Agresti-Veraar reaction-diffusion with transport noise II treats
   mass control and some triangular/entropy structures; check what exactly their theorems cover and whether species-dependent
   transport is excluded there)? If the mixed-energy argument works this simply, why did the authors pose Problem 7?
4. Check every citation in REPORT against sources.
5. Verdict: correct or not, novel or not, exactly what is proved, and how much of Problem 7 it answers.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Small numerical
checks in code/ are allowed (evidence only). Source texts may go in sources/ as plain text only; no PDFs kept, no page images.
Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
