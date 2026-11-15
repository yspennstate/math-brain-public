Open research problem. In this folder REPORT_P0347.md proves, for the discrete-time critical beta-splitting tree DTCS(n)
(a clade of size m splits into (i, m-i) with probability m/(2 h_{m-1} i(m-i))), that the Sackin index S_n and the Colless
index C_n satisfy Var ~ kappa n^2 log^2 n with kappa = (2 zeta(3) - zeta(2))/zeta(2)^2, are asymptotically equivalent at
scale n log n, and have non-Gaussian limiting third and fourth moments. Its §9 conjectures a limit law and gives an
infinitesimal fixed-point equation consistent with those moments. Its §7-8 prove the analogous full result for quadratic
Colless (all moments, determinacy, Laplace fixed point).

Goal: prove that (S_n - E S_n)/(n log n) converges in distribution, identify the limit (as the unique solution of a
fixed-point/Laplace equation, or by its moments), and prove convergence of all moments. Natural routes: (a) extend the
§6 central moment recursions to every order k by induction, find the recurrence for the limiting central moments a_k,
and bound a_k <= C^k k! for determinacy; (b) a contraction/infinitesimal-splitting argument. Check the literature in the
two supplied overview texts first and state precisely what is new.
Every claimed step must be verified numerically with your own code: exact central moment recursions to n >= 8000 for
k <= 6, compared with your limiting constants (expect slow 1/log n convergence; fit in powers of 1/log n).
If the full result is out of reach, prove the most you can (e.g. all moments converge, or tightness plus moment
identification) and say exactly what remains. Write REPORT.md (status line first: PROVED / PARTIAL / FAILED), LOG.md with
timestamped progress, and your scripts. Size memory before any large array; stay under 4 GB.
