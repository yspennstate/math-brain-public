SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T18:53:21Z.
attacking: six-mode destructive square-Gram stability with a physical-pair middle branch.

# Early substantive checkpoint

Full QFORM remains OPEN. This checkpoint records the first new implication before the final report.

Let H be m original coordinates and let a final symmetric matrix A be written across H and H^c as

A = [[C,B],[B^T,D]].

The exact identity

(A^2)[H,H] = C^2 + B B^T

combined with the latest account03/B12 Weyl profile gives, at k=6, p=2, q=5,

s_2(C)^2 + s_5(B)^2 >= lambda_6((A^2)[H,H]).                    (1)

Hence if lambda_6((A^2)[H,H]) >= g^2 and s_2(C)<b<g, then

s_5(B) >= sqrt(g^2-b^2).                                        (2)

The pinned e5f71d79... fifth-volume theorem applies to the ACTUAL final original-coordinate cross block B and has no marginal gate. Since

e_5(B^T B) >= s_5(B)^10,

it gives the real density inequality

||p_(X^T A X)||_infinity <= 5 sqrt(2e)/sqrt(g^2-b^2).           (3)

If instead s_2(C)>=b, choose 0<a<b/N with N=binom(m,2). If s_3(C)>=a, the finite physical-core projected-gradient theorem gives 2 sqrt(6 pi m)/a after conditioning outside H. If s_3(C)<a, the top-two Pluecker identity forces an ORIGINAL-coordinate pair I with

sigma_min(C[I,I]) >= b/N-a =: kappa.                            (4)

A definite pair gives pi/kappa. An indefinite pair, using the arbitrary-rank physical-pair theorem and the fact that lambda_6((A^2)[H,H])>=g^2 implies s_3(A)>=g, gives

||p||_infinity <= 3*400^(1/3) kappa^(-5/6) g^(-1/6).           (5)

Thus six physical square-energy modes already admit a complete original-coordinate receiver; no seventh mode is required.

For additional signed spectrum, use the account04/B12 destructive square-Gram theorem. With baseline A0, arbitrary symmetric addition S, G0=(A0^2)[H,H], G=((A0+S)^2)[H,H], N_H=[G0-G]_+ with eigenvalues nu_j, and any further dense symmetric T with ||T||op<=delta, it gives

sqrt(lambda_6(((A0+S+T)^2)[H,H]))
 >= [sqrt((lambda_(6+r)(G0)-nu_(r+1))_+) - delta]_+.           (6)

Combining (1)-(6) is the intended final stability theorem. Small ||T|| is used only in this coefficient-matrix inequality, never as a claim that X^T T X is uniformly small on unbounded inputs. No rotated random coordinates are declared independent.
