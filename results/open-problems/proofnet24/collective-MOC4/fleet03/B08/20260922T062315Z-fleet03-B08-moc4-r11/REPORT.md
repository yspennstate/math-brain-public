# MOC4 fleet03/B08 — exact zero-face true-unitary chart and stationary-adversary rejection

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** Marcus–de Oliveira, complex normal `4 x 4` case (`MOC4`)  
**Worker/run:** fleet03/B08, `20260922T062315Z-fleet03-B08-moc4-r11`  
**Exact assignment:** construct exact or rigorously enclosed counterexample candidates over true unitary matrices and complex spectra, checking separation from all 24 hull points in a common direction.  
**Named partner:** fleet04/B09.  
**Outcome:** `AUXILIARY_ONLY` with an exact mechanism change onto the lead's live zero-entry branch. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Source-valid state actually used

The exact target is: for every complex normal `4 x 4` pair, after diagonalizing one matrix, for every true unitary `U`,

`D(U)=det(diag(a)+U diag(b) U*)`

must lie in the convex hull of the 24 points

`v_sigma=prod_i(a_i+b_{sigma(i)})`.

A target counterexample therefore requires one actual unitary, actual complex spectra and one real-linear functional separating `D(U)` from **all 24** vertices. Negative formal coefficients or independently chosen bistochastic/compound arrays are not target counterexamples.

I used the newest campaign-lead reduction fleet03/B07 `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`: if a hypothetical support-violating global maximizer saturates a mixed-Hessian gate, it can be transported at equal support to a genuine unitary with a zero entry. Hence the zero-entry face is now a live boundary branch rather than a routine subclass.

I also consumed the assigned OTHER-account partner fleet04/B09 `MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1`. Its exact `SO(6)` pair-circle identity shows that a true support maximizer must satisfy the full off-block stationarity equations; passing discrete endpoint gates is insufficient. I use that conclusion below in its source-valid form: a candidate that admits an exact true-unitary support-increasing pair rotation cannot be the required maximizer.

## 2. New exact chart: `MOC4-ZERO-FACE-U3xU3-CHART-v1`

After row/column permutations, any unitary with a zero entry can be put in the form `u_44=0`. Write

`U = [[C,y],[z*,0]]`,

where `C` is `3 x 3`, `y,z in C^3`. Unitarity gives

`CC* = I-yy*`, `C*C = I-zz*`, `Cz=0`, `C* y=0`, and `||y||=||z||=1`.

Choose `V,W in U(3)` with `V e3=y` and `W e3=z`. Then `V* C W` annihilates `e3` on the right and has zero last row, while its upper `2 x 2` block is unitary. Absorbing that `U(2)` block into `V` gives the exact normal form

`U(V,W) = [[ V P W*, V e3 ], [ (W e3)*, 0 ]]`,  `P=diag(1,1,0)`,

with arbitrary `V,W in U(3)`. Conversely every matrix in this form is unitary and has `u_44=0`.

Thus the whole zero-entry face can be searched with genuine unitary coordinates only. No arbitrary bistochastic or independent compound-minor relaxation is introduced. By permuting coordinates, the same chart covers every possible single zero position.

## 3. Exact dense zero-face adversary

I generated `V,W` by rational complex Cayley transforms and obtained the following exact unitary. Every displayed entry is nonzero except the required `(4,4)` entry:

```
U = [
[(9248596-2204309i)/9965689, (-460963+1041129i)/9965689,
 (-1388656+618674i)/9965689, (131-511i)/2281],
[(563773+1612493i)/9965689, (8519772-3082155i)/9965689,
 (-394626+1491668i)/9965689, (-563-555i)/2281],
[(1113265+1577639i)/9965689, (-685277+3478279i)/9965689,
 (-766988-597724i)/9965689, (-1962+671i)/2281],
[(-384-538i)/4369, (114-796i)/4369,
 (-3443-2480i)/4369, 0]
].
```

The standard-library exact verifier checks `U U*=I` entry by entry.

Take

`a=(-12+13i, 1-24i, -22+12i, 1-19i)`,

`b=(7+11i, -18-5i, -7+24i, 10-13i)`.

Then exact determinant arithmetic gives

`D = 681177468907/9965689 - (540878230401/9965689)i`.

Use the single common real-linear support direction

`L(z)=-158949 Re(z)-904287 Im(z)`.

Exact enumeration of all 24 spectral permutation products gives

`M=max_sigma L(v_sigma)=54642495840`,

attained only by permutations `1423` and `2431`, and

`m=min_sigma L(v_sigma)=-1020841356720`.

The exact target gap is

`M-L(D)=163713444895903416/9965689 > 0`,

with normalized gap

`(M-L(D))/(M-m)=6821393537329309/446580733297283910`

`~= 0.015274715250172653`.

So this dense genuine zero-face candidate is rigorously **inside** the common support half-plane, not a counterexample.

More strongly, it is in the actual 24-point hull, with the exact three-vertex certificate

`D = lambda_1234 v_1234 + lambda_1243 v_1243 + lambda_1423 v_1423`,

where

`lambda_1234 = 409612355129822/34569108916249415`,

`lambda_1243 = 32512105995924378/34569108916249415`,

`lambda_1423 = 329478113039043/6913821783249883`.

All three coefficients are nonnegative and sum exactly to one.

## 4. Direct application of the named partner's stationarity obstruction

The preceding candidate is close enough to the exposed support boundary to be a useful true-unitary stress point, but the partner result says a serious maximizing adversary must also survive continuous pair variations.

Apply the exact left row-plane rotation on rows 2 and 3 with rational half-angle parameter `t=-1/1000`,

`c=(1-t^2)/(1+t^2)`, `s=2t/(1+t^2)`,

and set `U_1=R_23(t) U`. This is a genuine exact unitary and preserves `u_44=0`. Exact arithmetic gives the strict support increase

`L(D(U_1))-L(D(U))`

`=130344534495211750236720000/9965708931387965689 > 0`.

Therefore the candidate is not even a local maximizer of its own separating functional on the true zero-entry unitary face, exactly as the fleet04/B09 continuous-stationarity theorem requires us to test.

The improved point still has positive target gap

`M-L(D(U_1))`

`=163583427788461709501491183416/9965708931387965689 > 0`,

with normalized gap

`6815976157852571229228799309/446581626459197085301117283910`

`~=0.01526255392971329`.

It too is rigorously in the actual target hull. One exact three-vertex certificate uses permutations `1423,3421,4312` with weights

`9841626785216570230204205/13075879305406521841292301`,

`260224163944627976615229199/1320663809846058705970522401`,

`66435340594557136104668497/1320663809846058705970522401`.

They are nonnegative and sum exactly to one.

## 5. What this changes and what it does not

This does **not** prove the lead's zero-face target `ZF`, and it does not disprove MOC4. It does three source-valid things:

1. gives an exact `U(3) x U(3)` parametrization of every single-zero true-unitary face, suitable for adversarial search without nonrealizable surrogates;
2. supplies a dense exact rational-complex zero-face stress point and checks one common support direction against all 24 vertices plus an actual Caratheodory hull certificate; and
3. applies the named partner's continuous stationarity requirement to reject that stress point by an explicit rational support-improving true-unitary rotation.

The lead's reduction means the next adversarial obligation is now sharper:

> **`MOC4-ZERO-FACE-STATIONARY-ADVERSARY-v1` (OPEN).** Search the exact `U(V,W)` chart for a positive common-direction gap only after enforcing zero-face stationarity under the genuine left/right `U(3)` variations; otherwise prove that every stationary zero-face candidate obeys the 24-vertex support bound. A strict negative gap in one common direction from actual spectra and a true unitary would be a target counterexample. A negative formal coefficient is not.

A useful proof route would instead combine those zero-face stationarity equations with fleet03/B07's transverse Hessian-nullity inherited from saturation and the current same-unitary `P/R/D` constraints. This run has not supplied that final implication.

## 6. Verification

`verify_zero_face_cayley.py` uses only Python's standard library `fractions.Fraction` and exact permutation expansion. It verifies exact unitarity, the determinant, all 24 support values, both common-direction gaps, both three-vertex hull certificates, and the exact genuine-unitary support ascent. `VERIFY_OUTPUT.txt` is the captured successful output.

No singular/simple-spectrum assumption is used by the zero-face chart itself. The displayed stress spectra happen to be simple; the parent statement's singular and repeated cases remain part of the campaign and are not claimed closed by this adversarial run.
