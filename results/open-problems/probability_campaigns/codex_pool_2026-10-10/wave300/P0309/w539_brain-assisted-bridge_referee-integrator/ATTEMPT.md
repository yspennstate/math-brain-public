# P0309: bridge audit and near-collision obstruction

The intake's most specific recovered statement is the existing math-brain concept card `claim_894df26aac73717c54f790f08423c9c5e20c7eeea63ca049b11cab1e5c280c09`: existence of a crystalline Gibbs phase at sufficiently low positive temperature for a three-dimensional Coulomb or Riesz gas in the regimes predicted by Lewin's 2022 review. It does not specify an exponent range, ensemble, boundary condition, or order parameter. Current openness remains UNKNOWN. Lewin p.65 treats the BCC/FCC phase diagram as numerical/expected, and Theorem 46 addresses a unique fluid only when `s>d` and the activity is sufficiently small.

## The retrieved theorem and its proof obligation

The read-only math-brain query (command in `REPORT.md`) returned Theorem 3.13 of arXiv:2405.06616 as a concept card. Its exact primary-source hypothesis is a probability density proportional to `exp(-V)` on all of `R^n`, with a fixed positive-definite matrix `Gamma` such that `D^2 V(z) >= Gamma` uniformly in `z`; its conclusion is `Cov <= Gamma^{-1}`. For w538's conditional lattice model, `V=beta H_D`, `Gamma=beta kappa(L_D tensor I_3)` is positive definite for each finite Dirichlet set `D`; the assumption is supplied explicitly, so the inference is sound. The theorem does not itself supply that assumption for a Riesz gas.

## New obstruction O2 (own derivation; w542 audit requested)

Let `n>=2`, `s>0`, and `H(x_1,...,x_n)=sum_{i<j}|x_i-x_j|^{-s}+W(x_1,...,x_n)` on collision-free configurations in an open subset of `(R^3)^n`. Assume there is an interior point `c` and a neighborhood where `W` is `C^2` with bounded Hessian, while `x_3,...,x_n` can be fixed mutually distinct and separated from `c`. Set `x_1=c+(epsilon/2)e_1`, `x_2=c-(epsilon/2)e_1`, and choose the direction `v_1=e_2`, `v_2=-e_2`, `v_j=0` for `j>=3`. Then

`v^T D^2H(x) v = -4s epsilon^{-s-2} + O(1)` as `epsilon` decreases to zero.

Indeed, the pair separation is `epsilon e_1` and changes by `2t e_2`; differentiating `(epsilon^2+4t^2)^(-s/2)` twice at zero gives `-4s epsilon^{-s-2}`. Other pair distances stay bounded away from zero, and `D^2W` is bounded. Hence no fixed matrix lower bound `D^2H >= Gamma` can hold throughout the collision-free configuration space, for any finite positive-definite `Gamma`. The singularity also prevents a `C^2` extension to all of `(R^3)^n`. This eliminates a direct global Brascamp-Lieb transfer from w538's conditional displacement lemma to the actual continuum pair Hamiltonian. It does not rule out localized convexity inside a defect-free tube or a different argument.

For `0<s<3` and a uniform finite-volume jellium background, the one-body background convolution is locally smooth away from the domain boundary, so the same local near-collision mechanism applies. The formal claim above uses the explicit `C^2` assumption on `W` and does not need a boundary regularity assertion.

## Single hardest open piece

Prove an unconditioned, uniform-in-volume lower bound on a reciprocal-lattice Bragg observable (or equivalent order parameter) for a correctly defined continuum Riesz Gibbs specification, while controlling vacancies, dislocations, unlabeled particles, and the complement of any locally convex tube. Then pass it to a DLR limit and deduce a symmetry-broken phase. The Gaussian/phonon finite Green function and w538's conditional lemma do not control that complement.

## Retrieval measurement and bounded repair proposal

Command run: `python -X utf8 ~/.claude/dreaming/brain.py recall "P0309 probability Riesz crystalline proof mistakes"`. The top three returned slugs were a Bernoulli-convolution Riesz-product memory, a general proof-citation memory, and a martingale joint-structure memory: **0/3 directly relevant** to Riesz-gas crystallization. The response also reported P0309 absent. This is one manual relevance check, not a benchmark. Proposed repair: when query contains an explicit `Riesz gas` or `P0309` scope, down-rank results whose matched text is only `Riesz product`, and report an unresolved target if no on-scope theorem remains. Keep ordinary Riesz-product queries unchanged. This is a bounded proposal; no live recall control was changed or improvement claimed.

NEXT: Obtain w542's independent check of O2; check w537's first proof artifact and focus on its single hardest premise.
