# Independent audit of w591's two-observable statement

2026-10-10. Scope: STATEMENT_FOR_ADVERSARY.md, read only after my ATTEMPT.md was saved. The paired ATTEMPT.md was then a placeholder, so this is a separately derived proof of the precise statement, with a sharp one-observable counterexample. Mathematical verdict: KEEP on the stated localized interval. No global FK convergence conclusion is justified. Independent referee w593 must check this derivation; served author/referee model identities remain unverified.

Assume W is adapted and continuous, W_0=0, and g_t solves the capacity-normalized chordal Loewner equation. Choose 0<x_1<x_2<y. Stop before swallowing, and localize on compact subsets with 0<U_i<1, Y=g_t(y)-W_t>0, X_i=g_t(x_i)-W_t>0 and all inverses bounded. Let U_i=X_i/Y and fix kappa>0. Let H'(u)=u^(-4/kappa)*(1-u)^(8/kappa-2), with H(1/2)=0. Assume both H(U_i) are continuous local martingales in the same filtration as W.

1. A semimartingale assumption on W is unnecessary. H is smooth with H'>0 on (0,1). On each compact localization, U_1=H^{-1}(H(U_1)) is a continuous semimartingale by Ito's formula. Both g_t(x_1) and g_t(y) are continuous finite-variation adapted processes, and

W_t=(g_t(x_1)-U_1*g_t(y))/(1-U_1).

Thus W is a continuous semimartingale there. Localize further to write W=N+A with N a continuous local martingale and A a continuous predictable finite-variation process, both starting at zero. Let Q=[N]=[W]. Do not assume Q is absolutely continuous.

2. Direct Ito differentiation gives

dU_i=(U_i-1)/Y*dW + 2*(1/U_i-U_i)/Y^2*dt + (U_i-1)/Y^2*dQ,

d[U_i]=(U_i-1)^2/Y^2*dQ,

H''(u)/H'(u)=-4/(kappa*u)-(8/kappa-2)/(1-u).

The finite-variation part of dH(U_i) is therefore

H'(U_i)*[(U_i-1)/Y*dA + 2*(1/U_i-U_i)/Y^2*(dt-dQ/kappa)].

Because H(U_i) is a local martingale, this signed measure vanishes. Dividing by the nonzero factor H'(U_i)*(U_i-1)/Y yields

dA=2*(1/X_i+1/Y)*(dt-dQ/kappa),  i=1,2.

3. Subtract these two measure identities. Before swallowing, X_2-X_1=(x_2-x_1)*exp(-integral_0^t 2/(X_1*X_2) ds)>0. Hence 2*(1/X_1-1/X_2)>0, and on a further compact localization its inverse is bounded. Thus dt-dQ/kappa=0 and dA=0. Consequently W is a continuous local martingale and Q_t=kappa*(t stopped at tau). This proves precisely the localized conclusion, including the recovery of the semimartingale structure. It does not extend it past tau.

Sharp counterexample if the second observable is removed: fix 0<x<y and, for 0<=t<xy/4, set

W_t=(x+y)*(1-sqrt(1-4*t/(x*y))),

Y_t=y*sqrt(1-4*t/(x*y)), X_t=x*sqrt(1-4*t/(x*y)).

Then define g_t(x)=W_t+X_t and g_t(y)=W_t+Y_t. Differentiation gives d g_t(x)/dt=2/X_t and d g_t(y)/dt=2/Y_t, so these agree with the Loewner solutions for the displayed smooth deterministic driver. U_t=X_t/Y_t=x/y is constant. H(U_t) is therefore a local martingale for every kappa, yet W has nonzero finite variation and Q=0. This refutes one-observable identification even on a compact unswallowed interval.

Parent-problem missing premises:

- Construct two actual FK exploration-filtration event observables and prove their common stopped limit is H(U_i), with the same deterministic normalization and correct filtration. Finite posterior martingales alone do not identify that function.
- Establish stability uniformly for the random slit domains encountered before the localizing times, joint convergence with the driver, and a valid passage of martingale identities to the limiting filtration. Bounded probabilities help integrability, but not the conformal profile.
- Justify extension over arbitrary finite capacity times: the fixed marked points can be swallowed. One needs a sufficiently rich family of marked points or another argument covering the driver's full interval.
- At q=1, a wiring density is constant. At kappa=4, H(u)=log(2*u) is unbounded as u approaches zero. Bounded event probabilities require a separately justified normalization/localization rather than a global bounded-profile claim.

NEXT: w593 independently checks the signed-measure argument and the explicit counterexample; w591 supplies the missing FK profile theorem or retains it as an open premise.

Follow-up after the actual paired proof became available: read w591's completed ATTEMPT.md. L4's inversion, two Ito equations and signed-measure elimination agree with the independent derivation above. Its global corollary now explicitly assumes the observable property for every deterministic triple n<n+1<n+2. That additional quantifier covers each finite horizon: for any path and T, n>sup_[0,T] W ensures the positive Loewner images stay to the right of the driver, so the triple is not swallowed on [0,T]. The countable family and localization are essential; this is not a consequence of one fixed triple.

The paired L3 also correctly separates a different q=1 observable: for fixed finite graph, p and history atom, differentiating R_n(q)=1/q+(1-1/q)*P_q(A|F_n) at q=1 gives P_1(A|F_n)=1+R_n'(1). This repairs the finite q=1 loss of the plain ratio without proving uniform differentiation in the mesh or identifying a continuum conformal profile. Our O1 obstruction is specifically to the undifferentiated wiring density, and does not refute L3.

One required precision in the finite partial-conditioning formula: e must still be unrevealed, and the history on that atom must be measurable using the other queried edges. If the phrase "partial exploration filtration" included a history that already revealed the single free-boundary edge open at q=4,p=2/3, its actual conditional probability would be 1, while the stated mixture with C_e false would give 1/3. Add the unrevealed-edge premise when serving this formula. The intended next-edge application already has that premise.
