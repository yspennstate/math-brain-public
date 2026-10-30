# Source-scope supplement for fleet02/B03 r12

This supplement records one wording correction to Section 4 of `REPORT.md` and does not change any displayed bound.

The sentence beginning “Condition only on the original coordinates outside the right bank” should be read as follows:

> Take `Omega=(X_i,X_L,X_K)` to be the outside random state, independent of the active right-bank product variables.  Do **not** freeze `Omega` before applying Theorem 3.1.  The scalar `U=u.X_L` remains random with its genuine marginal density cap (`<=sqrt(2)`), while the square centre and outside scalar phase may depend arbitrarily on the same `Omega`.  The theorem itself disintegrates with respect to `U` only inside the Fourier integral, exactly as in (3.6)-(3.10).

Thus no conditional density cap for `U` is asserted or used.  In particular, the application does not condition on `U`, on any sum/difference variable, or on a dependent spectral projection.

With this reading the specialization is exactly

`X=X_r`,
`Y=X_{R\{r}}`,
`Omega=(X_i,X_L,X_K)`,
`U=u.X_L`,
`A=1/a`, `d=sigma`, `alpha=h_r`, `b=v_r`, `h=h_-`, `g=v_-`.

The deletion-plane Gram identity remains

`det G=m^2(1-eta_r)`,

and the final target-homogeneous bound remains

`||p_Q||_infinity
 < 7*2^(16/7)*3^(-4/7)
   s_3(A)^(-1)
   [(|h_r|/rho)(1-eta_r)]^(-2/7)`

under `h_r!=0`, `G>0`, and deletion-plane maximum leverage at most `3/4`.
