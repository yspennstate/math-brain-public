# Exact finite-leak Schur identity for the partner rank-one latent endpoint

This note sharpens Section 6-7 of `REPORT.md`. It uses the latent normal form in account02/B01 `QFORM-RANK1-LATENT-TRANSVERSE-WEDGE-v1` and performs only a literal ORIGINAL-coordinate Schur completion.

Let

`H=D+U C U^T`, `C=[[alpha,beta],[beta,gamma]]`, `delta=det C !=0`,

and let `I|J` be an exact-rank-one physical cut. In the partner's latent basis,

`U_I=[u,0]`, `U_J=[v,w]`.

Put

`r=alpha v+beta w`, `s=beta v+gamma w`.

Then

`H[I,J]=u r^T`.                                                  (1)

Fix one literal coordinate `j in J` and write

`d_j=H_jj=D_j+v_j r_j+w_j s_j`.                                 (2)

Assume `d_j!=0` and take the exact scalar Schur complement `H^(j)=H/j`.

## Theorem — `QFORM-FINITELEAK-SCHUR-CROSS-IDENTITY-v1`

The post-completion cross remains exact rank at most one:

`H^(j)[I,J\{j}] = u (r^(j))^T`,                                 (3)

where

`r^(j)_k = r_k - (r_j/d_j)(v_j r_k+w_j s_k)`.                  (4)

For every coordinate `k` with `w_k=0`, this simplifies exactly to

`boxed:
 r^(j)_k = [(alpha d_j-r_j^2)/d_j] v_k
           = [(alpha D_j+delta w_j^2)/d_j] v_k.}`               (5)

### Proof

Since `D` is diagonal, for `k!=j`

`H_jk=v_j r_k+w_j s_k`,

while `H[I,j]=u r_j`. The Schur formula gives (3)-(4). If `w_k=0`, then `r_k=alpha v_k` and `s_k=beta v_k`, so

`r^(j)_k
 =v_k[alpha-(r_j/d_j)(alpha v_j+beta w_j)]
 =v_k(alpha d_j-r_j^2)/d_j`.

Finally

`alpha d_j-r_j^2
 =alpha D_j+alpha(v_jr_j+w_js_j)-r_j^2
 =alpha D_j+w_j(alpha s_j-beta r_j)
 =alpha D_j+(alpha gamma-beta^2)w_j^2`,

which is (5). QED.

## Consequences when the partner's triple currency vanishes

The partner proves that if `rank U_J=2` and its latent triple currency `Zeta_3(v,w)=0`, then the transverse vector `w` is supported on at most two literal coordinates. Write `S=supp(w)`, so `|S|<=2`.

For `j in S` with `d_j!=0`, (5) gives the physical lower bound

`||H^(j)[I,J\{j}]||_op
 >= ||u|| * |alpha d_j-r_j^2|/|d_j| * ||v_(J\S)||`.             (6)

Thus, if the right-hand side is nonzero, the post-completion residual is exactly a nonzero rank-one packet, and the two-square theorem in the sibling `REPORT.md` applies immediately. At `beta=1/4`, with an outer scalar square coefficient `a`,

`||p_Q||_infinity
 <=13.1843165864 |a|^(-1/2)|d_j|^(-1/3)
   ||H^(j)[I,J\{j}]||_op^(-1/6)`.                              (7)

Combining (6)-(7) gives the explicit representation-level estimate

`||p_Q||_infinity
 <=13.1843165864 |a|^(-1/2)
   [ |d_j| ||u|| |alpha d_j-r_j^2| ||v_(J\S)|| ]^(-1/6)`.      (8)

No tiny second singular value has been discarded; the completion preserves rank one exactly.

If instead

`alpha d_j-r_j^2=0`,                                            (9)

then all post-completion cross coefficients from `I` to the diffuse complement `J\S` vanish **exactly**. Hence a failure of the two-square receiver is localized to the at-most-one remaining transverse support coordinate, rather than to a diffuse bank.

There is an especially rigid support-one endpoint. If `S={j}` and (9) holds, then the entire Schur residual is diagonal:

`boxed: H/j = D_(J union I)\{j}.}`                              (10)

Indeed every remaining low-rank row has latent form `(v_k,0)` (or `(u_i,0)` on `I`), so its low-rank bilinear coefficient is `alpha z_k z_l`. The Schur subtraction is

`(r_j z_k)(r_j z_l)/d_j`,

and (9) says `r_j^2/d_j=alpha`; the rank-one low-rank part cancels identically, leaving only the diagonal `D`.

Therefore the exact `Zeta_3=0`, support-one partner endpoint has only three possibilities: zero scalar pivot `d_j=0`; a nonzero rank-one residual paid by the two-square lift; or an exactly diagonal Schur residual. For support two, the same identity removes every diffuse cross direction whenever (9) occurs, leaving only one literal transverse coordinate. This narrows the remaining routing problem to a bounded-coordinate zero-pivot/cancellation core plus the quantitative near-rank-one collar.