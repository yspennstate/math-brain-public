# C0017: an independent conditional-observable route

Saved 2026-10-10 before reading w411's approach or proof. This is a conditional reduction with a concrete counterexample to a weaker premise. C0017 is not proved. w413 independently kept the conditional lemma and deterministic counterexample; served-model/different-model integration evidence remains unavailable. No novelty claim is made.

## Target and distinct method

The exact intake statement is: "Prove that critical bond percolation on Z^2 at p = 1/2 is conformally invariant in the scaling limit (Cardy's formula and convergence of interfaces to SLE(6)), as is known on the triangular lattice by Smirnov." Primary source recovered: Garban–Steif, arXiv:1102.5761v3, Chapter II Section 4, printed p.24 / PDF page 26. This is a historical conjecture; current openness is UNKNOWN because the bounded primary search found unassessed square-lattice proof claims.

The recorded C0017-A001 route seeks a square-lattice discrete holomorphic observable and stops at missing strong regularity. This attempt instead asks for conditional crossing martingales in one filtration and derives the Loewner identification exactly. It neither constructs that missing lattice input nor assumes conformal invariance as an established premise.

## Conditional proposition: two Cardy martingales identify the driver

Work on a filtered probability space satisfying the usual conditions. Let W be a real, continuous adapted process with deterministic W(0), and let g solve the chordal Loewner ODE dg_t(z)=2/(g_t(z)-W_t) dt. Choose deterministic W(0)<x1<x2<x3. Up to a stopping time T before swallowing, write G_i=g_t(x_i), X_i=G_i-W_t, and assume 0<X1<X2<X3. All arguments are localized: stop also when a denominator, 1-u, or a marked-point separation approaches zero, or any relevant process becomes unbounded. The conclusions hold on [0,T) by exhaustion.

Set

C(u) = (integral_0^1 [s(1-s)]^(-2/3) ds)^(-1) * integral_0^u [s(1-s)]^(-2/3) ds,  0<u<1.

Assume BOTH M12=C(X1/X2) and M13=C(X1/X3) are continuous local martingales in this SAME filtration. Then W-W(0) is a continuous local martingale with quadratic variation 6t on [0,T). Equivalently it is locally a sqrt(6)-Brownian Loewner driver, up to the specified lifetime. This conclusion identifies the driving process; it does not by itself prove that a discrete interface has a trace limit or satisfies these observable assumptions.

### Derivation without assuming a semimartingale driver

For u=X1/X2, C'(u)>0 and C is smooth on (0,1). Its inverse is smooth on compact subsets of (0,1). Thus u=C^(-1)(M12) is a continuous semimartingale by Itô's formula after localization. G1 and G2 have absolutely continuous finite variation since their distances from W stay positive locally. The identity

W = (G1-u*G2)/(1-u)

therefore proves that W is a continuous semimartingale. Write W=W(0)+A+N, where A starts at zero and has continuous predictable finite variation and N is a continuous local martingale starting at zero. Write V=<N>. Do not assume that dV or dA has a density with respect to dt.

For a pair i<j, put X=Xi, Y=Xj, u=X/Y. Since dX=2/X dt-dW and dY=2/Y dt-dW, Itô's quotient rule gives

du = 2/Y^2*(1/u-u) dt + (u-1)/Y dW + (u-1)/Y^2 dV.

Also d<u>=(1-u)^2/Y^2 dV and C''/C'=(2/3)*(2u-1)/(u(1-u)). Hence the finite-variation part of C(u) equals

C'(u)/Y^2 * [(1/u-u)*(2 dt-dV/3) + Y*(u-1) dA].

A continuous local martingale has zero predictable finite-variation part. Since C'>0 and 0<u<1, this is equivalent, as an equality of signed random measures, to

dA = (1/X+1/Y)*(2 dt-dV/3).                              (1)

Apply (1) to (1,2) and (1,3) and subtract. This gives

(1/X2-1/X3)*(2 dt-dV/3)=0.

The prefactor is strictly positive before swallowing and has a locally bounded reciprocal after localization. Thus dV=6 dt; substitution into (1) gives dA=0. Lévy's characterization, or Dambis–Dubins–Schwarz with extension after the lifetime if needed, identifies the local Brownian driver. This subtraction does not multiply conditional expectations or use independence of the two observables.

The argument extends globally only if the martingale premise is supplied throughout a localizing exhaustion of the interface lifetime. Proving it only up to a fixed stop identifies only that stopped segment.

## Exact counterexample: one observable is insufficient

Take W(0)=0, x1=1 and x2=2. For 0<=t<1/2 set Y(t)=sqrt(4-8t), X(t)=Y(t)/2 and

W(t)=3-(3/2)*Y(t), G1(t)=3-Y(t), G2(t)=3-Y(t)/2.

Then G1(0)=1 and G2(0)=2. Direct differentiation gives G1'=4/Y=2/X and G2'=2/Y, so these are exactly the two real Loewner trajectories driven by W. Throughout this interval X/Y=1/2 and C(X/Y)=1/2. This observable is a constant martingale in the deterministic filtration, while W is a nonconstant deterministic finite-variation driver with zero quadratic variation. It cannot be a sqrt(6)-Brownian driver. This refutes the general one-observable inference, not any assertion about actual critical square-lattice percolation.

For a third starting point x3=3, at t=0 equation (1) would require W'=2*(1+1/3)=8/3, whereas the displayed driver has W'=3. The second Cardy observable therefore has nonzero initial drift. The two-observable premise detects the counterexample.

## The single hardest lattice gap

One must identify TWO appropriately defined discrete crossing or boundary-order events, including their induced primal/dual boundary conditions after exploration, whose Doob martingales converge jointly to the displayed C ratios in the SAME limiting exploration filtration on random slit domains. Merely writing an exact Doob martingale does not identify its limit. A fixed-domain Cardy assertion, RSW tightness, large-scale rotation invariance, or one marginal martingale is not this random-domain conditional identification.

For a sufficient passage-to-the-limit premise, it is enough after localization to have joint convergence of the curve/driver/marked-point processes and bounded discrete Doob observables, plus convergence of their joint expectations against a convergence-determining class of bounded continuous functions of the past. Then the identity E[(M_t-M_s)H(past up to s)]=0 passes to the limit, and a monotone-class argument gives the martingale property in the natural limiting filtration. If an enlarged filtration is claimed, this must be checked for that enlarged past as well. Curves reaching boundary marks and discontinuous stopping-time functionals require their own convergence treatment.

This sufficient premise remains unproved for the square-lattice model in this packet. It contains the hard conformal observable identification rather than solving it by notation.

## Independent review receipt

w413 independently reproduced the inverse-observable semimartingale step, quotient-Itô identity, signed-measure subtraction and deterministic counterexample, and kept L1 and X1 at their conditional/finite scope. See INDEPENDENT_REVIEW_RECEIPT.json. A successful finite arithmetic check only verifies the displayed algebra, not the lattice premise or the full stochastic theorem.

NEXT: Establish joint conditional Cardy limits for actual square-lattice observables in random slit domains; w411's route separately needs a specified cell comparison with vanishing signed defect.
