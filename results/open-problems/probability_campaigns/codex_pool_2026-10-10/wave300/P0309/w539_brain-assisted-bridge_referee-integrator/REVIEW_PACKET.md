# P0309 referee checkpoint (2026-10-10)

## w538

**KEEP** w538-S1.2. Independent differentiation reproduces the Hessian and the two-particle transverse counterexample exactly. This refutes a termwise convexity route, not stability of a full lattice.

**KEEP as conditional lemma** w538-S1.3. The math-brain card `claim_25c5933eb4eeace1fc2a65fb1aba685df634054eba10e9f383b0eeb7c1ba32f7` states the Brascamp–Lieb covariance inequality for an everywhere-positive matrix lower bound. The source theorem, arXiv:2405.06616 Theorem 3.13 p.19, agrees. w538 supplies this assumption explicitly as `D^2H_D >= kappa L_D tensor I_3`; `L_D` is positive definite for finite Dirichlet D. The killed-walk Green diagonal is bounded by `C_3`, finite because its Fourier denominator is quadratic near zero in three dimensions. The stated loose bound `C_3 <= sqrt(3) pi/8` checks algebraically using `1-cos t >= 2t^2/pi^2` for `|t|<=pi` and a radius `sqrt(3)pi` ball. Evenness centers `G dot u_x`; cosine and Jensen finish the claim. This is a labeled finite-volume special case.

**DROP any inference to P0309.** No premise supplies global convexity, a defect-free labeling, an unconditional continuum Gibbs law, or a symmetry-broken DLR limit. Lewin's reviewed theorem for a fluid has `s>d` and small activity, which is a different regime and conclusion.

**KEEP** w538's O2 centering counterexample. With `D` nonadjacent, `L_D=6I`; the stated quadratic Hamiltonian has Hessian exactly `kappa L_D tensor I_3` and site covariance `I/(6 beta kappa)`. The two means yield reciprocal phases `+a` and `-a`, `a=exp(-|G|^2/(12 beta kappa))`. The exact second moment is `(1-a^2)/N`, so the fixed-mode lower bound fails without evenness or another coherent phase premise. This is a constructed surrogate, not a Riesz gas.

**KEEP** w538 O3. Along its one-particle transverse path, the close pair contributes `-s epsilon^(-s-2)` and all separated/smooth terms stay bounded; thus the full finite-particle Hessian is negative in an open near-collision region. My separately saved relative-motion O2 gets factor `-4s` and the same conclusion. No claim about a crystal-neighborhood or infinite-volume Hessian follows.

**KEEP** w538 O4. Its circular ordered branch carries probability `exp(-cN)`. The full second moment is `a^2 exp(-cN)` and the angular Laplace integral has rate `beta a |h|`; therefore the full pressure is `max(a|h|-c/beta,0)` and is flat near zero. This is the exact full-law versus branch distinction required by w537 C5.

**Bundle overlap:** w538 has already prepared `bundle_001.json` containing O1, B1, and O2 as DRAFT concepts. My independently checked local `draft_bundle/bundle_001.json` duplicates O1/B1 and will remain a reviewer artifact; submit w538's bundle after updating its pending-review labels instead of ingesting duplicate nodes.

## w537

**KEEP C1-C5 within their stated assumptions.** Exact per-claim reproductions and remaining gaps are in `review/W537_VERDICTS.jsonl`. The hardest claim C5 was rederived independently: a positive full-law second moment plus circular symmetry gives a fixed positive probability of a positive real Fourier response, then C2 forces a pressure cusp. C1 correctly keeps the thermodynamic limit before `h` decreases to zero. C2's result is strict away from the threshold `a=m`. C3 requires uniform integrability, a good cell boundary, and separate zero-field Gibbs closure. C4 correctly shows an exponentially rare ordered branch can disappear from the zero-field pressure slope.

**Parent verdict: still open/UNKNOWN current status.** The packet does not prove a full-law Bragg lower bound for a 3D Riesz Gibbs measure or the pressure limit. One nonzero reciprocal mode would show translation breaking if C3's inputs hold, but would not identify BCC/FCC or a full-rank crystal. The exact intake source is the `op-p0309` entry in `~/math-brain-inbox/claude-probability-1000-continue-0907/bundle_010.json`; its quantifiers are incomplete.

NEXT: Send the scoped C1-C5 referee verdict to the integration contact through the authorized shared progress path; keep O2 provisional until w542 audits it.

## w542 independent audit request

Please audit `w539-S1.4` in `ATTEMPT.md`, especially the `-4s epsilon^(-s-2)` factor, the bounded remainder, and whether the claim's configuration-space assumptions justify its global-convexity conclusion. The result is provisional until your verdict. This is a route obstruction only; it does not solve P0309.
