SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T10:49:01Z.
attacking: convert the newest partner's strict-row Fourier envelope into a genuinely decoupled positive-weight whole-copy time integral which by itself recovers L1 Fourier integrability, then remove the artificial deletion-leverage 3/4 gate by choosing the partner exponent adaptively.

# SUBSTANTIVE CHECKPOINT

Full QFORM remains OPEN.

## New integrated transducer
If a real random variable Z has characteristic function phi and, for some theta>1,

J_theta(Z):=int_R |t|^theta |phi(t)|^2 dt < infinity,

then phi is in L1 and Z has a continuous bounded density with

||p_Z||_infinity <= [(theta+1)/(pi(theta-1))] * [((theta-1)J_theta)/8]^(1/(theta+1)).

Proof: for T>0, split int|phi| at |t|=T. The low part is <=2T. Cauchy-Schwarz on the tail gives <=[2J_theta/(theta-1)]^(1/2) T^(-(theta-1)/2). Optimize at T=[(theta-1)J_theta/8]^(1/(theta+1)).

For an independent copy Z', |phi_Z(t)|^2=phi_{Z-Z'}(t), so J_theta is literally a whole-copy decoupled time integral; no coordinate sum/difference pair is split or declared independent.

## Partner envelope -> positive-weight collision
Latest designated partner account02/B03, canonical source
math-open-problems@0feb5b58d53a266b5df517982780448aa9b6daf5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T101024Z-account02-B03-QFORM-r12/REPORT.md,
proves for 1<q<2, beta=1/2+1/q>1, under deletion-plane leverage max ell_j<=q/2,
|phi_Z(t)|<=min(1,K_q |t|^-beta).
Hence, for every -1<theta<2beta-1,
J_theta <=2 K_q^((theta+1)/beta)[1/(theta+1)+1/(2beta-theta-1)].
In particular theta=beta gives
J_beta <=[4beta/(beta^2-1)] K_q^(1+1/beta),
which satisfies theta>1 and therefore recovers linear small-ball scaling from the decoupled integral alone.

## Adaptive nested-leverage consequence
In the current one-sided packet, let e=ell_* be the largest leverage in the deletion plane, zeta=1-eta_r, delta=|h_r|/rho, and s=s_3(A). For any strict deletion plane e<1 with e>1/2, choose q=2e in the partner theorem (the endpoint q/e=2 is legal by the newest-Claude/e5 L^p estimate). Using L<=sqrt(2), y>1/sqrt(2), and the exact spectral inequalities gamma|sigma|>=s^2 and gamma sigma^2>=s^3 gives

||p_Q||_infinity <= C(e) s^-1 [delta^(2(2e-1)) zeta]^(-1/(2(1+e))),
C(e)=((1+e)/(1-e))*(4/e)^(1/(1+e)).

At e=3/4 this is exactly 18.2190565794 s^-1[delta zeta]^(-2/7), matching the partner q=3/2 specialization. Thus `ell_*>3/4` is not a separate qualitative obstruction: every strict e<1 has a continuous-density receiver; only the quantitative second-order collar e->1 together with delta,zeta->0 remains.
