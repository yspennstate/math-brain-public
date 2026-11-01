# P0321 referee proof route and stopping point

2026-10-10. The dated P0321 title is qualitative. I use w540's precise provisional subtarget: classical density-one two-dimensional Riesz jellium with potential 1/|x|, neutralizing background, and a nonempty interval of positive inverse temperatures. The phase observables must be defined on the actual limiting point process. Lewin 2022 §VI.2 describes the desired hexatic by fast translational and slow sixfold orientational correlations but does not fix quantitative thresholds. Present openness remains UNKNOWN.

## Single hardest missing input

For that microscopic Gibbs model, prove on one nonempty beta interval a volume-uniform coarse-graining that controls dislocation and disclination sectors, constructs an equilibrium limit, and yields actual particle-bond and positional correlation estimates. In a w540-style angle route, the load-bearing subpart is an anchored connected-cumulant bound, a log-variance coefficient, a nonzero projection of the physical bond observable, and an insertion error asymptotically below the angular vertex correlation. These statements must hold for the *same* Gibbs state in which positional quasi-long-range order is absent. This is unproved.

## Attempted route

1. Start from an infinite-volume neutralized s=1 Gibbs state, if it exists under a specified limiting procedure, and define a bounded local sixfold bond observable using a precise neighbor rule. Choose a microscopic positional observable that tests reciprocal-lattice order rather than demanding exponential decay of the entire density correlation; the long-range potential may leave a noncrystalline tail.
2. Construct a scale decomposition of a **lifted pair angle**. Lifting is required for cumulants; angles modulo 2π alone do not have canonical real differences when disclinations occur. Establish a logarithmic second cumulant and summable anchored connected higher cumulants, including all defect sectors. w540 L1 and L2 would then give an algebraic vertex magnitude without assuming independent increments.
3. Prove a nonzero, volume-uniform microscopic bond projection and error o(r^-η). w540 L3 would transfer the algebraic law to the actual bond observable. Independently prove positional disorder in the same state. A phase conclusion follows only after all of these steps and an equilibrium thermodynamic limit.

## Direct test of the route

I independently reproduced w541's Gaussian elastic surrogate. It has algebraic positional correlation r^-aT|q|²/(4π) and a positive orientational plateau. Therefore the harmonic field gives the quasi-solid pattern, not the desired hexatic separation. Adding only a log-variance estimate does not repair this: w540 C1 has the same log-variance scaling but zero vertex correlation. Nor can a fixed or same-order approximation error be ignored: w540 C2 erases a wrapped Gaussian vertex correlation with total-variation perturbation 2r^-η/π. The next mathematical step would be a microscopic connected-defect expansion with enough strength to establish w540's stated hypotheses; none has been derived here.

## Source-scope check

Lewin's Theorem 47 has the hypothesis s>d. Its later invocation in the 2D phase discussion cannot establish translation invariance for s=1,d=2. w545 independently recorded the same scope correction in its SOURCE_STATUS.json. A claim about the s=1 Gibbs state's symmetry needs its own argument.

No complete P0321 proof, formal certificate, or current-open status claim is asserted.

NEXT: Obtain an independent audit of any new mathematical lemma; here only source correction and peer-claim verdicts are contributed. The unresolved step is a microscopic defect-sector estimate at s=1.
