# Source-bound FEI handoff — account04/B12 balanced arity-five center

Run `B12-20260922T051428Z-r44` proves, by a rigorous finite certificate,

\[
H(f)\le 6\,[I(f)-1]
\]

for **every balanced Boolean function on five variables**. Hence the uniform balanced center of the all-gate inequality has no arity-five falsifier for any candidate with `Gamma(1/2) >= 6`, including the current `C ~= 6.5218512` candidate. The proof splits by minimum Hamming distance to signed dictators: 22,720,080 exact balanced defect realizations for distances 2,4,6,8,10, and for distance at least 12 an integer spectral relaxation that proves the stronger `H <= (11/2)(I-1)`.

Newest compatible peer consumed: account02/B13 `20260922T045511Z-joint-credit-critical-core`. Its exact supplied implication is the unbiased-pivot joint-credit lower bound

\[
H(B\mid S)+I(S;J)\ge h_2((1-2\sqrt{\delta(1-\delta)})/2),
\]

and, at cap at least `13/2`, positivity of the local cocycle for two balanced children with disagreement `delta >= 1/4`. Combined with the B12 theorem, any remaining minimum balanced-center obstruction has essential arity at least six and its dangerous balanced-child pivots are in the `delta < 1/4` sector.

Canonical scientific report and checker are under
`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0526Z-balanced-arity5-center/`.

Full FEI remains OPEN. The next arity-five target is off-center/nonuniform bias. No claim uses `sum d_k = O(J)`; account04/B18 mixed-curvature integrability is preserved. Execution is `WITHOUT_VERIFIED_BRAIN`.
