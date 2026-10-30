# fleet02/B03 r56 early calculation — two-slope completion of the square-collision slice

Programme `QFORM-DENSITY-3EIG-20260922`; full unrestricted theorem OPEN.

Let `(S,R)` with `R in R^2` have arbitrary joint probability density `g<=M`. Let `V in R^2` be independent of `(S,R)` with joint probability density `h<=N`. Let `a!=0`, `B` invertible `2x2`, and let `G,H,K` be arbitrary measurable real functions. For

`Q = a(S+G(R))^2 + 2 R^T B V + H(R)+K(V)`,

shearing `S` by `G(R)` preserves the joint density cap. For a.e. `r`, put

`A_r(t)=int g(s,r)e^{iat s^2} ds`, `F(t)=int |A_r(t)|^2 dr`.

The slice argument of fleet03/B03 r53 is dimension-free in the environment `r` and gives

`||F||_2 <= C0 M |a|^{-1/2}`, `C0=(3/2)sqrt(6pi)`.

Writing `q_t(r)=A_r(t)e^{itH(r)}` and `w_t(v)=h(v)e^{itK(v)}`, two-dimensional bilinear Plancherel gives

`|phi_Q(t)|^2 <= pi^2 N |det B|^{-1}|t|^{-2} F(t)`.

Hence for `T>0`, Holder with exponents `4/3,4` yields

`int |phi_Q| <= 2T + D T^{-1/4}`,

`D=pi*6^{3/4}*C0^{1/2} (MN)^{1/2}|a|^{-1/4}|det B|^{-1/2}`.

Optimising at `T^{5/4}=D/8` gives

`||p_Q||_infty <= (15/4) 3^{1/5} (MN)^{2/5}|a|^{-1/5}|det B|^{-2/5}`.

Equivalently with `J=|a||det B|^2`, the scale is `J^{-1/5}`. This is the first same-packet L1 Fourier closure obtained from the r53 slice resource: the second independent hyperbolic slope is exactly what makes the `t^{-1} F^{1/2}` tail integrable against `F^{1/2} in L^4`.

A separate direct weighted-time split gives

`int |t|^{-1/2}|phi_Q(t)|^2 dt <= (5/2)2^{4/5}3^{3/10}sqrt(pi) (MN)^{1/5}J^{-1/10}`,

hence for a whole independent copy `Q'`,

`E|Q-Q'|^{-1/2} <= (5/2)6^{3/10}(MN)^{1/5}J^{-1/10}`.

The exact constants and a strict original-product target application will be checked in the final report.
