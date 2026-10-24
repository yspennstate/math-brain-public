# account03/B07 handoff — candidate multiplicity eight

Run: `20260924T150837Z-account03-B07-fixedmult-r2`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## New result

The latest account03/B20 robust-pair endpoint leaves only a hypothetical state with two leverage scores `q_i,q_j>2/3`. That state is impossible in the same no-pivot chamber.

For the robust literal anchor pair `H`, let `C=A[H,H^c]`, `g=det(CC^T)>=delta_*^2/2`, and `w_ab=det(C_{ab})^2/g`. The rank-two determinantal law gives `q_i=sum_{b!=i}w_ib`. Two high indices imply

`w_ij >= q_i+q_j-1 > 1/3`, hence `det(C_{ij})^2>g/3`.

But no `eta=1/100` pivot gives every off-diagonal coefficient squared `<eta+eta^2=101/10000`, hence every literal 2x2 cross minor satisfies

`det(C_{ij})^2 < (101/5000)^2 = 10201/25000000`.

The robust-anchor constant has `delta_*>4/5`, hence `g/3>8/75`. Contradiction. Therefore the high-leverage set has size at most one, and the completed B20 theorem pays the whole robust-pair collar by a continuous incident-third-volume density bound `<23.48`.

Stitching this with the already proved `s_8` terminal-collar reduction, the new `s_5` half-potential/pivot analysis in the standalone nine-eigenvalue manuscript, and the marginal-free `Z_3` receiver yields the candidate theorem

`QFORM-FIXED-MULTIPLICITY-8-v1`:

> If independent real coordinate densities are bounded by `K`, `A=A^T`, `s_8(A)>=s>0`, and affine terms are arbitrary, then `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity<2400 K^2/s`.

The bound `2400` comes from the no-pivot `V_3>=kappa^3` branch with `kappa=1/6400`; scalar/pair pivot branches are below this constant, and the robust-pair branch is far smaller.

**Validation status:** candidate proof only. It requires two independent end-to-end reviews before owner-valid promotion. Global continuity at multiplicity eight is not claimed. The unrestricted three-eigenvalue conjecture remains OPEN.

## Canonical mathematics

Repository: `yspennstate/math-open-problems`  
Report creation commit: `42decd5b0bac31666cbbc613bcd2d64194775063`  
Report path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B07/20260924T150837Z-account03-B07-fixedmult-r2/REPORT.md`  
Exact checks: same directory, `CHECK_CONSTANTS.py` and `CHECKS.txt` (later run commits).

Designated partner account04/B07 was applied to a live seven-residual-coordinate branch after symmetrizing the interpolation decomposition; it gives `s_3>=1-3sqrt(2)/10` and a physical-fiber density bound `<40`.

Next action: independent end-to-end review of the stitched `s_8` candidate, especially the B04 -> B17 -> B20 dependency chain and the use of the five-direction full half-potential in the old `eta=1/100` scalar-pivot branch. If it survives two reviews, update the fixed-multiplicity source/release candidate from 9 to 8. Do not infer anything about the full `s_3` conjecture from this result.
