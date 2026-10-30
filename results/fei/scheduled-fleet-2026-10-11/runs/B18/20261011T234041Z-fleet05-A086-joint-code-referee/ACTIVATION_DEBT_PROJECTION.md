# Activation projects a complete-reference debt onto the core

All entropy/divergence units are bits. Let g be any balanced finite Boolean sign with squared spectrum P_g, so P_g(empty)=0 and sum_{T nonempty}P_g(T)=1. Let r>=1, p=2^-r, and F=1+A_r(g-1), on fresh point controls and the original data cube. The selected control point may be fixed all-positive by input sign changes. Let (U,T) denote its control/data spectral set.

For every T nonempty and every control subset U,

    P_F(U,T)=p^2 P_g(T).

For T empty and U nonempty, P_F(U,empty)=p^2. The empty atom is (1-p)^2. Therefore v=Var(F)=p(2-p), and the conditional nonempty law P^+ has

    beta=P^+(T nonempty)=1/(2-p),
    P^+(T | T nonempty)=P_g(T).

Conditional on nonempty T, controls are uniform over all 2^r subsets. Conditional on empty T, controls are uniform over the 2^r-1 nonempty subsets. No arbitrary core entropy is discarded by these facts.

Now let Q be ANY complete subprobability on nonempty (U,T), positive on the support of P^+. Let M=sum Q in (0,1], and q=Q/M. Put

    gamma=q(T nonempty),
    q_g(T)=q(T)/(gamma) for T nonempty.

Finite debt requires 0<gamma<1 and support for every required conditional sector. If positivity fails, the debt is infinite and all lower inequalities hold in the extended sense. Standard finite conditional disintegration gives the exact identity

    v D(P^+||Q)
      = -v log2 M
        + v D_Ber(beta||gamma)
        + p D(P_g||q_g)
        + v(1-beta) D(Unif(nonempty control subsets)||q(U | T=empty))
        + p sum_{T nonempty} P_g(T)
              D(Unif(all control subsets)||q(U | T)).             (1)

Proof: first write D(P^+||Q)=D(P^+||q)-log2 M. Apply the KL chain rule first to J=1[T nonempty], then to the data label within J=1, and then to U given T. The target coefficient of core-data divergence is v beta=p; the J=0 data label is deterministic. The two control conditionals are precisely the uniform laws established above. This proves every term with the original unconditioned weight; there is no replacement of p by v or conditional probability beta.

All terms on the right of (1) are nonnegative. Thus

    v D(P^+||Q) >= p D(P_g||q_g).                               (2)

This is valid for the optimized forest envelope U in A003 whenever it covers this activation, and for A008's complete output dictionary Q whenever its supports cover it. It never treats one generator as the other. For the forest envelope, substitute (1) into A003's exact identity to locate which part of its coding slack lies in data shape, versus normalization, binary-sector and control-shape slack.

A007's paid root-rarity component does not establish payment of the core term in (2); it does not automatically establish bounds on the other chain-rule terms either. Nor does (2) lower-bound seed entropy by itself: a reference with q_g=P_g makes the data divergence zero. The unresolved statement is existence of an admissible structural reference paying all the displayed terms, not an impossibility assertion for arbitrary references.

The shortest subsequent stress test uses arbitrary balanced tensor cores g_t=z product_{j=1}^t f(x^(j)) and r_t=ceil(2log2(t+1)). Core entropy is tH(f), core influence is tI(f)+1, and activation influence is p_t(tI(f)+1+r_t). A candidate complete reference must exhibit its induced q_{g_t}; proposed payment of (1) can then be checked with the core factor and actual p_t retained. Easy-core rarity bounds cannot substitute for this test. No finite universal K is claimed here.

Exact validation: code/projection.py, frozen out/BRIDGE_SPEC.json, exhausts all 78 balanced labelled cores in dimensions 1..3, controls r=1..3, and two fixed structural references: uniform-nonempty and a product of spectral coordinate biases 1/3,2/3 conditioned on nonempty output. The main identity and the generalized-reference normalization penalty at Q/2 are checked as exact rational linear combinations of log2 primes. The control terms vanish exactly for the uniform-nonempty reference. Results are in out/BRIDGE_RESULTS.json. These finite cases validate the implementation; the all-dimensional proof is the conditional KL chain rule above. Independent review is pending for this derived interface.
