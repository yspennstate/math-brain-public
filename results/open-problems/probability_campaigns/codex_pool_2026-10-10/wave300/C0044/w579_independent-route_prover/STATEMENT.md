# C0044 — statement sent before the proof packet

Fix d >= 3 and a nonzero vector ell in R^d. Put E = {+e_i,-e_i : 1 <= i <= d}. An environment is a collection of probability vectors omega(x,.) on E, indexed by x in Z^d. The vectors are iid under the environment law P, and P(omega(x,e)>0 for every x,e)=1. The nearest-neighbor walk, in this fixed environment, starts at 0 and moves from x to x+e with probability omega(x,e). Its annealed law is P_0 = integral P_{0,omega} dP(omega).

Target: P_0(A_ell) belongs to {0,1}, where A_ell = {lim_n X_n dot ell = +infinity}. This asks for a fixed direction; it does not assert simultaneous almost-sure statements for uncountably many directions, speed, ballisticity, or the stronger all-path transience question C0043. Uniform ellipticity is not part of the strict-ellipticity target; a result assuming a common lower bound must be labeled a restricted result.

Primary historical statement: Martin P. W. Zerner, arXiv:0706.0745v1 (2007), introduction, especially the definition of A_ell and the paragraph preceding Theorem 1. https://arxiv.org/html/0706.0745v1 . It separates directional zero-one from the zero-one law for A_ell union A_-ell and proves the planar theorem under elliptic iid assumptions.

Current status as checked 2026-10-10: UNKNOWN. The public primary repository https://github.com/openai/math/blob/main/lean/docs/220.md now claims a formal solution under strict ellipticity. The actual comparator theorem, assumptions and trusted axioms have not yet been checked here. A prose scope claim is not a proof receipt. Do not report C0044 as newly solved by this worker, or as currently open with certainty.

This statement may be sent to w580 independently of the route and proof. The route was committed in ATTEMPT.md before reading any current core-lane proof.
