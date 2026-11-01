# r25 correction addendum — normalization notation only

The theorem and all quantitative bounds in `REPORT.md` are unchanged, but one displayed normalization sentence in Section 4 contains a reciprocal typo.

For a conjugate fiber with overlap `a=m_N(u)`, the conditional density cap is

`M=(2a)^(-1)`.

To normalize to density cap one, the correct definition is

`Y=M V = V/(2a)`,

so equivalently

`V=2a Y`.

The same applies to each right overlap `b`: `Y=V/(2b)`, equivalently `V=2bY`.

Therefore the scaled cross block used immediately afterwards is indeed

`M(u)=diag(2a_(g,r)) M0 diag(2b_g)`,

which is exactly the block used in equations (4.1) onward. Consequently the computations of `M(u)^T M(u)`, `Z(u)`, the row marginals, and the `Omega(N^2)` good-fiber lower bound are unaffected. Only the sentence defining `Y` in Section 4 should be read with this correction.
