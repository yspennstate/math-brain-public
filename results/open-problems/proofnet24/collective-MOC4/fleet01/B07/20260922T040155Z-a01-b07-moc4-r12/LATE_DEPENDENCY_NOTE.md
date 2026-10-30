# Late dependency note — interaction with fleet03/B09 cycle separator

After the immutable main report was written, the same invocation consumed fleet03/B09 `MOC4-CYCLE-SEPARATOR-NOGO-v1`, shared handoff `20260922T040531Z-fleet03-B09-cycle-separator-nogo.md`, whose exact true-`SO(6)` datum satisfies all 16 earlier odd-twist mass cuts but violates an even-endpoint hull inequality for the **unstructured** coefficient pair

`K_cycle = 3 diag(1,1,-1)`

and

`X_cycle = 2 [[0,-1,1],[1,0,-1],[-1,1,0]]`.

This does not contradict MOC4 because that coefficient pair has not been shown to arise from spectra `(a,b,eta)`.

I checked the new `MOC4-BIORIENTATION-PAIR-GATE-v1` on that exact B09 datum, using its exact

`t=R=[[337/625,0,288/625],[127008/525625,1241/1682,21609/1051250],[4608/21025,441/1682,21809/42050]]`

and

`y=D=diag(7/25,20/29,28/145)`.

Because both `K_cycle` and `D` are diagonal, every orientation-swap cross term `C^L_ag` and `C^R_bd` vanishes. The six gate slacks are nevertheless strictly positive:

- row `(0,1)`: `4446471/1051250`;
- row `(0,2)`: `44037/42050`;
- row `(1,2)`: `818424/525625`;
- column `(0,1)`: `127749/42050`;
- column `(0,2)`: `971271/1051250`;
- column `(1,2)`: `52056/18125`.

Thus the B09 true-`SO(6)` separator **passes all six new bi-orientation gates**. This is an important negative control: the new gate is a genuine maximizer restriction and expels the earlier parity-slack hard datum, but it is not by itself a coefficientwise characterization of the even endpoint hull.

The surviving shared implication should therefore be stated with the **structured spectral coefficient image** explicit. A proof must use the special formulas

`X_ab=Re(eta A+_a B+_b)`

and

`K=(H W H^T)_(1-perp)+Y/2`, `Y_ab=Re(eta A-_a B-_b)`,

in addition to the true-unitary `(P,D,R)` constraints and the new bi-orientation gates. Conversely, a disproof route must produce actual spectra and one support direction realizing a separator, not merely an `SO(6)` point with arbitrary `(K,X)`.

This note changes no claim in the main report: full MOC4 remains open.
