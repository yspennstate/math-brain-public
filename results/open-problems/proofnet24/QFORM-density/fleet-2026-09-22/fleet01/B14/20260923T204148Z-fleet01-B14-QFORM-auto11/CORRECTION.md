# Controlling correction to REPORT.md Section 5

This correction was written before the run handoff and supersedes one overbroad sentence in `REPORT.md` Section 5. The general probabilistic Theorem 4.1 is unchanged.

The sentence saying that homogeneous cross terms between `X` or `Y` and the driver bank `Z` are allowed in the **strict-target corollary** is not justified by the displayed direct-sum spectral argument and must be deleted from that corollary. If those cross terms are present, the active homogeneous matrix is no longer `diag(a,-b) direct_sum S`, so the three target eigenvalues do not follow from that direct-sum spectrum alone.

The correct strict-target statement is:

Let the selected active ORIGINAL-coordinate principal block be exactly

`A_* = diag(a,-b) direct_sum S`,

`S=[[H,c],[c^T,d]]`,

with `a,b>0`, `H=H^T`, and `R0=sqrt(d^2+||c||_2^2)`. No homogeneous cross terms from the two opposite-square coordinates `(X,Y)` to `(Z,W)` are included in this selected active principal block. Arbitrary additional **outside** original coordinates and arbitrary couplings between those outside coordinates and every active coordinate are permitted: after conditioning on the outside bank, they become affine terms in the active variables, while the active homogeneous principal block remains `A_*`.

If `a>=1`, `b>=1`, and `R0>=1`, then `S` has an eigenvalue of modulus at least `R0` because `||S||_op>=||S e_W||_2=R0`. Hence `A_*` has at least three eigenvalues of modulus at least one. Cauchy interlacing preserves that threshold count in the full ambient matrix. Conditional on the outside variables, Theorem 4.1 applies with `xi,eta` constant (depending on the outside value), `s(Z)` equal to the arbitrary quadratic-plus-affine `Z` contribution, and arbitrary receiver-linear shift `e`. Therefore

`||p_Q||_infinity <= 2^(19/6)(ab)^(-1/3)R0^(-1/3)`,

and in particular `<=2^(19/6)<8.980` under `a,b,R0>=1`.

The diffuse family used later in the report has exactly this corrected structure (`a=b=1`, `H=d=0`, `c_m=m^(-1/2)(1,...,1)`), so Sections 5's diffuse example and Section 6's random-center comparison remain valid without change.

Status after correction: supporting strict-target theorem proved in this corrected scope; full unrestricted QFORM remains OPEN.
