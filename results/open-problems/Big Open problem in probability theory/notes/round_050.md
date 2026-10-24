# Round 050 log

## Goal

Turn the critical shell summability condition from Round 049 into a compact
exponential criterion that can be targeted directly.

## Critical shell exponents

Added Corollary `cor:critical-shell-exponent`.  For a bounded-degree graph with
\(p_c(G)<1\), define
\[
  \rho_{\mathrm{sph},2}(G)
  =
  \limsup_{n\to\infty}\|S_n^G\|_{2\to2}^{1/n}
\]
and
\[
  \alpha_c^{\max}(G)
  =
  \limsup_{n\to\infty}\tau_{p_c}^{\max}(n)^{1/n}.
\]
If
\[
  \alpha_c^{\max}(G)\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof is immediate but useful: choose exponential upper bounds
\(\tau_{p_c}^{\max}(n)\le C\alpha^n\) and
\(\|S_n^G\|_{2\to2}\le C'\rho^n\) with \(\alpha\rho<1\).  This makes the
critical shell sum finite, so the Round 049 openness corollary applies.

## Check case

For the \(d\)-regular tree,
\[
  \rho_{\mathrm{sph},2}(T_d)=\sqrt{d-1},
  \qquad
  \alpha_c^{\max}(T_d)=p_c(T_d)=\frac{1}{d-1},
\]
so the product is \(1/\sqrt{d-1}<1\).  The criterion recovers the strict
\(L^2\) gap in this model.

## Updated target

The next proof target can now be stated as
\[
  \alpha_c^{\max}(G)<\rho_{\mathrm{sph},2}(G)^{-1}.
\]
This formulation separates graph geometry, encoded by sphere-kernel
\(L^2\)-growth, from actual critical two-point decay.
