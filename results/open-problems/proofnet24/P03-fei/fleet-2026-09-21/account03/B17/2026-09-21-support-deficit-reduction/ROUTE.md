# Route 15 — minority-set support-deficit reduction

**Status:** proposed full-FEI mechanism; full FEI remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.  
**Parent role:** account03/B17, FEI new proof mechanisms.

This route was opened after the first Approach 1 local-charge candidate was refuted by an exact Boolean function.

For a nonempty set `A` in the `n`-cube, let `g=1_A`, `delta=E g`, and let

`mu_A(S)=ghat(S)^2/delta`

be the normalized Fourier-energy law of the indicator. Put

`L(A)=log2(1/delta)`, `H_A=H(mu_A)`, `J_A=E_{S~mu_A}|S|`,

and define the two classical deficits

`U(A)=H_A-L(A)`,

`E(A)=J_A-L(A)/2`.

The proposed universal inequality is

`U(A) <= C E(A)`                                                    (SD_C)

for every nonempty cube set `A`, with a dimension-independent constant `C` (ideally Hod's `beta(1/2)`).  `U` is the spectral-entropy excess over the finite Fourier uncertainty floor, while `E` is the normalized edge-isoperimetric / log-Sobolev excess. Both vanish on subcubes and both add exactly under Cartesian products.

The first target is not to assume compression monotonicity. Prove the exact transfer from `(SD_C)` to ordinary FEI, stress-test `(SD_C)` on all set indicators through dimension four and on recursive dyadic staircase sets, and explicitly attack the tempting claim that one-coordinate compressions monotonically increase the deficit ratio.

No novelty or publication-priority claim is made by this route declaration.
