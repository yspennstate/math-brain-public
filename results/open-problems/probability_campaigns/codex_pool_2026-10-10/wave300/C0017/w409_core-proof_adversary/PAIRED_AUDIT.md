# Audit of w408's conditional route

Auditor w409, 2026-10-10. Independent contour work and its first three claims were saved before this proof was read. This is an audit of the original proof, not an audit of another review. The designated referee remains w410.

Verdict: KEEP L1-L3 as conditional reductions, with their stated assumptions. C0017 remains unproved in this packet. No concrete counterexample to L1 was found; the separately derived calculation below verifies its crucial coefficient and signed-measure step.

## Independent calculation of L1

Use dg_t(z)=2/(g_t(z)-W_t) dt. Set f(x,y)=C(x/y), r=x/y and C'(r)>0, where C is the normalized integral with density [r(1-r)]^(-2/3). Let D=partial_x+partial_y. Direct differentiation gives

C''/C'=-(2/3)(1/r-1/(1-r)),

Df=(1-r)C'/y,

D^2f=((1-r)^2 C''-2(1-r)C')/y^2,

[(2/x)partial_x+(2/y)partial_y]f=-3D^2f,

(D^2f)/(2Df)=-(1/3)(1/x+1/y).

For W=N+V, with N a continuous local martingale and V continuous finite variation, put Q=<N>. The martingale assumption for f_i means its finite variation measure is zero, so

dV=-(1/3)(1/X+1/Y_i)(dQ-6dt).

Subtract the two identities. Since Y_2-Y_1>=eta and Y_i<=L, the coefficient 1/Y_1-1/Y_2 is at least eta/L^2. Multiplication by its bounded inverse is legitimate on the localization. Hence dQ=6dt and dV=0. These are identities of measures, so the argument excludes singular finite variation and singular bracket measures as well as ordinary drift densities. Independence of the two martingales is neither used nor required.

The proof's preliminary recovery of the semimartingale property is sound: invert C on a compact ratio range and express W=(g_t(a)-U_t g_t(b))/(1-U_t). The positive separation assumptions keep the ratio and this inverse operation away from their endpoints. L1 therefore does not assume the conclusion's diffusion structure.

For the global result the countable localization condition matters. An explicit exhaustion can be obtained from triples (m,2m,3m), m>=4, and stops sigma_m=m wedge inf{t: |W_t|>=m/2}. On these intervals X>=m/2, Y_2<=3m+4, and each initially m-sized separation stays at least m exp(-8/m), using d(Y-X)=-2(Y-X)/(XY) dt. Thus eta=1/m and L=4m work for m>=4. The sigma_m increase to infinity for any continuous W on finite time intervals. This makes the global localization argument concrete without selecting a mark based on future information.

## L2 and L3

With dR_i=-(Df_i)dV+(D^2f_i/2)(dQ-6dt), divide by Df_i and solve the two linear equations. This independently gives the signs and coefficients printed in L2. Its total variation inequalities follow by bounded multiplication of measures and the triangle inequality. Uniform approximation alone does not imply those total variation premises.

L3's bounded cylinder-function argument is valid with JOINT convergence of the driver and the original martingales in synchronized time. Each cylinder is measurable in the prelimit filtration, and boundedness permits convergence of the expectations. A monotone-class argument supplies the natural limiting filtration. Actual stopping-time convergence and the marked-point convergence are explicitly separate assumptions. If a discrete martingale is replaced by an interpolation, its adaptedness/martingale property must still be established; the stated theorem does not automatically license that replacement.

## The minimal missing premise in the full-target application

The square-lattice Doob crossing or exit martingales must approximate the Cardy functions in the EXPLORATION'S RANDOM SLIT DOMAINS, on the nondegenerate stopped intervals, with joint driver/marked-point convergence in one limiting filtration. This is unproved in w408's route. A static quad limit, RSW, unconditional symmetry or independence of unrevealed bonds does not identify those conditional crossing probabilities.

For a quantifier check, let D_m be a family of domains and define an abstract error e_n(D_m)=1 when n=m and 0 otherwise. For every fixed D_m, e_n(D_m) tends to zero. Choosing D_n at stage n gives error 1 always. This is only a counterexample to interchanging pointwise-in-domain convergence with evaluation at a varying domain; it is not a percolation model. A uniform estimate on the encountered domains, or a separate transfer theorem with verified boundary/stopping hypotheses, is needed.

## Exact finite controls

Command: python -B -X utf8 verify_obstructions.py. It checks the normalized Cardy differential identities and nonzero determinants for three separated mark triples using rational arithmetic. Duplicated endpoints give determinant zero, and a variance coefficient 4 fails the Cardy differential identity. Together with the contour controls, 198 assertions pass. These are diagnostic controls supporting the written calculations, not a formal proof receipt or a proof of the lattice input.

NEXT: w410 independently check the deterministic contour reduction and retain the full target's stopped slit-domain Cardy approximation as OPEN.
