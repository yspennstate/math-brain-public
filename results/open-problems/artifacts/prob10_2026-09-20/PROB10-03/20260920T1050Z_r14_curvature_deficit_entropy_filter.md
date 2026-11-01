# PROB10-03 / R14 — curvature-deficit entropy filter for complete-third stationarity

Status: **proved auxiliary theorem / source endpoint unchanged**.

This note is a create-only companion artifact to the R14 PROB10-03 run. It uses the exact full-radius `kappa=-1` source convention and does not promote any floating-point third-full root to a source endpoint.

## 1. A sharp one-dimensional information lemma

Let `gamma=N(0,1)` and let

`d nu/d gamma = exp(phi)/Z`,

where `phi` is smooth and concave. Put

`r=phi'`, `t=-r'`,

and assume `0 <= t <= K` with `K>0`. Write

`mu=E_nu X`, `v=Var_nu(X)`, `R=Var_nu(r)`, `D=KL(nu||gamma)`.

Define

`psi(z)=-z-log(1-z)`, `0<=z<1`.

### Lemma 1 (curvature-deficit KL lower bound)

Under the hypotheses above,

`z:=1-v >= R/K`,

and therefore

`D >= mu^2/2 + psi(R/K)/2`.                                  (1.1)

More generally, for a family `(nu_y)` with the same curvature cap `K`,

`E_y D_y >= (1/2)E_y mu_y^2 + (1/2)psi(E_y R_y/K)`.          (1.2)

The result is sharp within the class described only by these statistics: equality in `z>=R/K` and in the entropy lower bound is attained by quadratic Gaussian tilts.

### Proof

For `d nu proportional exp(phi)d gamma`, integration by parts gives, for smooth `F`,

`E_nu F' = E_nu[(X-r)F]`.

Taking `F=1` yields `E r=E X=mu`. Taking `F=X` and then `F=r` gives

`1=E X^2-E[Xr]`,

`E r'=E[Xr]-E r^2`.

Eliminating `E[Xr]` and using `I:=E r^2=mu^2+R` gives the exact identity

`1-v = -E r' - R = E t - R`.                                (1.3)

The potential of `nu` is `W(x)=x^2/2-phi(x)`, so

`W''=1+t >=1`.

Brascamp--Lieb with the test function `r` gives

`R=Var_nu(r) <= E_nu[(r')^2/W'']`
`             = E_nu[t^2/(1+t)]`
`             <= [K/(1+K)] E_nu t`.                         (1.4)

Since `E t=(1-v)+R` by (1.3), (1.4) rearranges to

`R <= K(1-v)`, i.e. `z=1-v>=R/K`.                            (1.5)

The variance-matched Gaussian information projection gives

`D >= G(mu,v)`
`  = (1/2)[mu^2+v-1-log v]`
`  = mu^2/2 + psi(1-v)/2`.                                  (1.6)

The function `psi` is increasing and convex on `[0,1)`. Combining (1.5) and (1.6) proves (1.1); averaging and Jensen prove (1.2).

For sharpness, take `phi(x)=-a x^2/2+b x`, `a>0`. Then `nu` is Gaussian with variance `v=(1+a)^(-1)`, `K=a`, and

`R=a^2/(1+a)`, `1-v=a/(1+a)=R/K`.

Because `nu` itself is the matched Gaussian, (1.6) is equality. Thus no universal strengthening depending only on `(mu,R,K)` can replace (1.1) by a strictly larger lower bound at every point. QED.

The smoothness assumption can be removed by standard smooth approximation whenever the displayed expectations are finite. In the perceptron application the Gaussian convolution already makes the relevant outer potential smooth; the inner hinge tilt is handled directly or by approximation.

## 2. Application to the complete-third outer U tilt

Use the current source-matched notation

`m=c3/c2`, `d^2=p2-p3`, `s^2=1-p2`,

`X=d U + sqrt(p3)V - 1`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u=log f`.

The previously proved global curvature estimate is

`-L <= u_xx <= 0`,

`L=2B/(1+2Bs^2)`.                                           (2.1)

For fixed `V=v`, the outer U-tilt has

`phi_v(U)=m u(dU+sqrt(p3)v-1)`.

Its relative score is `r_U=md u_x`; hence

`0 <= -r_U' <= K_U:=m d^2 L`.                               (2.2)

At a strict complete-third stationary point define

`C:=4B^2 M_B=c2^2/alpha>0`.

The exact score-overlap identities give

`E mu_U^2 = m^2 d^2 C q3`,

`E R_U    = m^2 d^2 C (q2-q3)`.                             (2.3)

The exact entropy form of c3-stationarity gives

`D_U = m^2 C A_c3`.                                         (2.4)

Apply (1.2) with the common cap (2.2). Set

`t_U := m C(q2-q3)/L`.                                      (2.5)

The lemma itself implies `0<=t_U<1`. Combining (1.2)--(2.5) yields the new necessary condition

`A_c3 >= d^2 q3/2 + psi(t_U)/(2m^2 C)`.                     (2.6)

Since `psi(t)>=t^2/2`, a log-free corollary is

`boxed: A_c3 >= d^2 q3/2 + C(q2-q3)^2/(4L^2)`.             (2.7)

This strictly strengthens the old lower cage `A_c3>=d^2q3/2` whenever `q2>q3`.

## 3. Application to the inner H tilt

For fixed `x`, the H-tilt has relative log density

`phi_x(H)=-B(x+sH)_+^2`.

Thus

`r_H=-2Bs(x+sH)_+`,

`0 <= -r_H' <= K_H:=2Bs^2`.                                 (3.1)

At a strict stationary point, averaging over the outer nested law gives

`E mu_H^2 = s^2 C q2`,

`E R_H    = s^2 C(1-q2)`,                                   (3.2)

while c2-stationarity is

`E KL(rho_X||gamma_H)=C A_c2`.                              (3.3)

Set

`t_H := C(1-q2)/(2B)`.                                      (3.4)

Again `0<=t_H<1` follows from the lemma. Equations (1.2), (3.1)--(3.4) give

`A_c2 >= s^2 q2/2 + psi(t_H)/(2C)`.                         (3.5)

Using `psi(t)>=t^2/2` gives the simple polynomial filter

`boxed: A_c2 >= s^2 q2/2 + C(1-q2)^2/(16B^2)`.             (3.6)

This strictly strengthens the old lower cage `A_c2>=s^2q2/2` on the strict branch.

## 4. Why this is useful and why it does not close the root by itself

The older transport/LSI lower bounds were proved in the previous R14 run to be automatic throughout the strict projective cone. The new corrections (2.7) and (3.6) are not projective identities: they contain the score normalization `C` and the kernel curvature scale `L`. They can therefore serve as inexpensive prefilters in the four-overlap positive-gap Krawczyk/subdivision proof before evaluating the full nested KL integrals.

A numerical-only falsification check at the archived `delta=10^-3` waypoint (`alpha approximately 12.3164333569308`) gives

- outer old lower `0.0425472447026614`, refined lower `0.0436600703338475`, while `A_c3 approximately 0.0675450259449614`;
- inner old lower `0.0102732276266880`, refined lower `0.0103434424450167`, while `A_c2 approximately 0.0120159755148959`.

Thus the new theorem is nontrivial but **does not by itself certify or exclude** that candidate. This is the intended negation test: a full source-moving proof still needs outward control of the actual nested moment map (or a stronger model-specific curvature statistic).

The Gaussian quadratic equality case above is also a rigorous obstruction to trying to obtain an everywhere-stricter universal theorem from only `(mean, score variance, uniform curvature cap)`. The next gain must use the nonconstant perceptron curvature `u_xx`, exactly the quantity isolated by the complementary NM13-03 curvature-overlap theorem.
