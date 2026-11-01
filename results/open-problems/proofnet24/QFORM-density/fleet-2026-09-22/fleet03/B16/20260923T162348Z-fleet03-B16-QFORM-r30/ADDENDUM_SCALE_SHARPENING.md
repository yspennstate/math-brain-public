# r30 scale sharpening for the projected-crossing survivor

The projected-crossing addendum gives, for either balanced bank `B`,

`||p_Q||_infinity <9.4 [D^2 h det(G_other) nu_B]^(-1/6)
                     <=9.4 [D^2 h nu_B/16]^(-1/6)`,

where `D=|det Lambda|>=1`, `h>63/64`, and `nu_B=det H_B` is the full three-dimensional spectral volume of that bank.

The scale-sharp universal exit is therefore

`D^2 nu_B >=2^-12  =>  ||p_Q||_infinity <59.844 <60`,

with a continuous `C_0` density. Thus a genuinely unpaid bank must satisfy the stronger inequality

`D^2 nu_B <2^-12`.

Since `det G_B>=1/16`, its longitudinal least-squares innovation obeys

`t_B-v_B^T G_B^(-1)v_B
 =nu_B/det G_B
 <2^-8 D^-2`.

Equivalently, there is a deterministic `q_B in R^2` such that

`sum_(i in B)(alpha_i-q_B^Tz_i)^2 <2^-8 D^-2`,

so the source-coefficient innovation norm is `<1/(16D)`. Because `||Lambda||_op<=D` when all three singular values of `Lambda` are at least one, the corresponding **spectral-image coefficient error** has Euclidean norm `<1/16`. This is a coefficient-space statement only; no small random quadratic term is deleted or treated perturbatively.

Hence the final r30 survivor is two disjoint original-coordinate banks, both transverse-balanced and carrying diffuse order-one negative hub-pair determinant mass, whose longitudinal source rows are each within `1/(16D)` of a two-slope plane. The next analytic step must exploit, not discard, these two small innovations.
