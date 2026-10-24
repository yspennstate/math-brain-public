# account02/B02 early calculation — two hyperbolic pairs versus cross-volume certificates

Run: `20260924T041549Z-account02-B02-QFORM-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.

For independent cap-one real variables U,V,

`phi_a(t)=E exp(2 i a t U V)=int f_U(u) psi_V(2 a t u) du`.

Minkowski, Plancherel, `||f_V||_2<=1`, and the one-dimensional bathtub bound

`int f_U(u)|u|^(-1/2)du <= int_(-1/2)^(1/2)|u|^(-1/2)du=2sqrt(2)`

give

`||phi_a||_2 <= 2 sqrt(2 pi) |a|^(-1/2)`.

Hence for two independent hyperbolic pairs and any independent remainder R,

`Q=R+2a U1 V1+2b U2 V2`

satisfies

`int |phi_Q(t)|dt <= 8 pi / sqrt(|ab|)`.

A direct conditional-density argument is sharper: given `(U1,U2)=u`, convolution in V1,V2 has height at most

`[2 max(|a u1|,|b u2|)]^(-1)`.

After `(x1,x2)=(a u1,b u2)`, the joint density is at most `K=1/|ab|`. The sup-norm bathtub inequality

`int g(x)/||x||_infinity dx <= 4 sqrt(K)`

therefore gives `||p_Q||_infinity <= 2/sqrt(|ab|)`. Fourier L1 additionally gives a continuous C0 representative.

Exact-target stress family:

`A_eps=[1] direct_sum [[0,D_eps],[D_eps,0]],  D_eps=diag(1,1,eps), 0<=|eps|<=1.`

Its spectrum is `{1,+/-1,+/-1,+/-|eps|}` and thus has at least five eigenvalues of modulus >=1. Every disjoint physical cross cut has rank <=3, `E5=0`, and `sup E3=eps^2`; on the full matching block all third-volume row marginals equal one, so D' fails its `h<3/4` gate. The reviewed marginal-free E3 compiler can only give a certificate proportional to `|eps|^(-1/3)`, while the two-pair receiver gives uniformly

`int |phi_Q| <= 8 pi`, `||p_Q||_infinity <=2`.

For the full partition `L={x0,y1,y2,y3}`, `R={z1,z2,z3}`, the account03/B02 r45 mixed `2+1` volume quantity has `x1 x2=1`, transverse same-side energy one, and is entirely overlap-one: the minor on rows `{x0,y1,y2}`, columns `{x0,z1,z2}` has determinant one. Thus the r45 diagonal/hub endpoint can be real while all physical E3/D5 currencies degenerate as eps->0.

Status: supporting theorem/obstruction to a D'/D5-only structural closure, not a QFORM counterexample. Next step is to extend the two-pair L2xL2 receiver from this direct-sum source geometry to the overlap-one grouped-pivot packet with arbitrary same-bank twists/couplings, without post-rotation independence.
