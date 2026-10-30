# Notation correction for REPORT.md

The theorem and estimates in `REPORT.md` are unchanged. There is one coordinate-identification shorthand in Sections 2 and 4 that should be read as follows.

The invariant shear vector is the **three-dimensional** vector

`p_phys=(I-n n^T)P n in n^perp subset R^3`.

After choosing the orthonormal frame `E` of `n^perp`, its two-dimensional coordinate vector is

`p_E=E^T P n in R^2`.

Thus `p_phys=E p_E` and `||p_phys||=||p_E||`. In the block matrix of `P` in the basis `(n,E)`, the off-diagonal block is `p_E`, and equation (4.2) should read

`k=C_0^(-1) p_E`.

Likewise equations (4.3), (6.4), and all linear-frequency calculations use `p_E` inside two-dimensional dot products, while every displayed norm `||p||` in the final bounds is the invariant common norm `||p_E||=||p_phys||`.

With this identification, all dimensions match and the physical invariant identity remains

`P w=Delta p_phys`, hence `Delta^2 ||p_E||=||w|| ||P w||` at `n^T P n=0`.

This is only a notation clarification; no hypothesis, constant, proof step, or status changes.
