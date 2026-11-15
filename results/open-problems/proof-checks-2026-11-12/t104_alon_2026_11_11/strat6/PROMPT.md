You are working on one open case of a graph inequality. Work in this folder only and write as you go.

FILES HERE
- PREVIOUS_RESULT.md: the STRAT5 result (notation, formula (3), the radial polynomial T(a,b) = a L_u + b L_w + a^2 P + ab Q0 + b^2 R_w, the moment polytope (13), the regions already proved, and the section "What remains").
- PREVIOUS_RESULT_STRAT4.md: the STRAT4 result (closed form (1), the disconnected theorem, the rank-one certificate).
- STRAT5/: STRAT5's scripts and certificates (stratum.py evaluates T exactly; verify_cells.py, weight_moment_cells.py, quartic_ratio_certificate.py, etc.).

TASK
Prove T >= 0 on the rest of the connected n = 5, D = 2 stratum, i.e. on the region described in "What remains" of PREVIOUS_RESULT.md:
3/25 < r = b/a <= 1, a > max(443/1000, A1(r), W(r)), a < 2/(3-r), some weight w_ij < (lambda-a)/5. If you cannot close all of it, enlarge the proved region as much as you can and state exactly what is left.

ROUTE TO TRY FIRST (check it before relying on it)
For a fixed frame (u, w) and fixed r, T(a, ar)/a is affine in a and positive at a = 0+. So T >= 0 on the whole admissible ray iff T >= 0 at the ray's far end a_end(u, w, r). At a_end either a = lambda (the disconnected endpoint, already proved) or some weight w_ij becomes 0. Hence it suffices to prove T >= 0 for frames on the stratum with at least one zero weight, which is a codimension-one set. Choose coordinates on that face (for example fix the zero edge as {4,5}, which is a polynomial equation in u, w, a, r) and repeat: decompose the face by which further weights vanish, and use exact cells in (r, moments) with interval or rational arithmetic as in weight_moment_cells.py. Report whether this reduction is correct, and if so how much of the region it closes.
Other tools available: the sharpened weight constraint (15), the quartic SOS endpoint method (it worked to r = 3/25 and failed at r = 1/8 with 5 of 286 forms), and finer cells.

RULES
- Mark every statement PROVED or NUMERICAL. A floating SDP, optimizer or sampler never proves anything; a proof needs exact rational or interval arithmetic, or a written argument.
- Write a replay script for every exact certificate and run it. Use one thread for any solver.
- Keep LOG.md current every 15 minutes or so (what you tried, what worked, what failed).
- Finish with RESULT.md: the theorems, the full derivations, the certificate construction and replay commands, and the explicit remaining region. Plain text, no bold.
- Do not use language-model workers or the network. Do not write outside this folder.
