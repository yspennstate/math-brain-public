SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T19:16:57Z.
attacking: the still-unpaid diffuse near-coloop endpoint by replacing coordinatewise selector independence with a joint-density Plancherel compiler for an entire projected selector vector; first goal is a whole-copy |phi|^2 estimate and linear collision scale for the exact angular packet without splitting any sum/difference pair.

Early calculation. Let Z in R^k be independent of a background W, with joint density f_Z bounded by M_Z; let C(W) have a joint density bounded by M_C, with arbitrary dependence between its coordinates and the rest of W. For invertible B and arbitrary selector phase P,

Q=R(W)+P(Z)+2 Z^T B C(W).

Writing F_t(xi)=E_Z exp(i t P(Z)+i xi.Z), Cauchy--Schwarz over the whole background and Plancherel on the whole selector vector give

|phi_Q(t)|^2 <= M_C |det(2tB)|^{-1} int |F_t(xi)|^2 dxi
              <= M_Z M_C pi^k |det B|^{-1}|t|^{-k}.

This needs no independence among the coordinates of Z. The intended source-valid application takes Z=(v.X_R,q.X_R), an orthonormal two-dimensional projection of the original right product bank, whose joint density cap is <=2. In the exact packet Q=a^{-1}(H_0+beta Z_1+m Z_2)^2+2 sigma U Z_1, the background coefficient vector C=(beta H_0/a+sigma U, m H_0/a) has density cap <=sqrt(e)/(|sigma|m): the pair (H_0,U) has cap <=sqrt(e)/|a| because H_0 contains the independent physical term a X_i, and the determinant of (H_0,U)->C is |sigma m/a|. Thus a cancels before inversion.

If verified end-to-end, k=2 yields |phi_Q(t)|^2 <= min{1,2 pi^2 sqrt(e)(|sigma|m)^{-1}|t|^{-2}}, a finite weighted whole-copy half-Riesz integral and a linear collision small-ball estimate. This does not by itself claim the one-copy L-infinity endpoint.
