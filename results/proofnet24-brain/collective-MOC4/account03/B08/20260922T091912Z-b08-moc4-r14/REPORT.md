# account03/B08 MOC4 research report — r14

Outcome: **AUXILIARY_ONLY**. Parent MOC4 remains **OPEN / not proved / not disproved**. Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. Fresh assignment and source-valid scope

This run follows owner control revision `2026-09-22.2` and directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B08 assignment is to construct exact or rigorously enclosed candidates over **true unitary matrices and complex spectra**, and test one common separating direction against all 24 spectral permutation products. Old installation/benchmark duties remain superseded.

The source target is only the complex-normal `4 x 4` Marcus-de Oliveira scope:

`det(diag(a)+U diag(b) U*) in conv{ prod_i(a_i+b_sigma(i)) : sigma in S_4 }`

for every unitary `U`, including singular/repeated spectra by the target's full statement. No bistochastic surrogate or negative formal coefficient is treated as a target counterexample.

Required named OTHER-account partner consumed and applied: account04/B09, run `20260922T084040Z-b09-moc4-r38`, result `MOC4-ZERO-FACE-ALIGNED-EXTERNAL-ONE-THIRD-CAP-v1`. That theorem proves that on a genuine zero-entry face, each aligned Drury external coefficient is at most `1/3`, sharply, using the same-unitary factorization `q^+=p s^T`. The present run deliberately attacks the complementary **dense interior** regime: the exact unitary below has no zero entries and no zero `2 x 2` minors, so the zero-face cap does not directly apply. Its limit is nevertheless a Weyl/permutation trap, which makes the relation to the partner result precise in Section 7.

## 2. New result: `MOC4-DENSE-IN-HULL-PAIR-TRAP-v1`

Use the same simple, nonzero spectra found in the previous exact pair-trap run:

\[
a=(23+19i,\ 1+17i,\ 25-26i,\ -35+19i),
\]
\[
b=(-21+13i,\ -1+23i,\ 26-27i,\ 32-21i).
\]

All 16 sums `a_i+b_j` are nonzero. For `v_sigma=prod_i(a_i+b_sigma(i))`, let

- `p=4321`, with `v_p=-1262976+2125032 i`;
- `q=3412`, with `v_q=929730+823140 i`.

Take the exact common real-linear support direction

\[
L(z)=216964043\,\Re z+365420756\,\Im z.
\]

Exact enumeration of all 24 permutation products gives **24 distinct support values**, with

\[
L(v_q)=502510420792230,
\qquad
L(v_p)=502510420792224.
\]

Thus `q` is the unique global target-support vertex, `p` is uniquely second, and their exact gap is only `6`.

Now define

\[
S=\begin{pmatrix}
0&1&2&3\\
-1&0&4&5\\
-2&-4&0&6\\
-3&-5&-6&0
\end{pmatrix},
\qquad t=10^{-10},
\]

\[
Q(t)=(I-tS)(I+tS)^{-1},
\qquad U(t)=Q(t)P_{4321}.
\]

Because `S^T=-S`, `Q(t)` is exactly real orthogonal; the verifier also checks `det U=1`. Since `t` is rational, every entry of `U` is rational. For this exact `t`, all 16 entries of `U` and all 36 of its `2 x 2` minors are nonzero. Hence this is a genuine dense orthogonal, therefore unitary, witness rather than a monomial or zero-face point.

Let

\[
D=\det(\operatorname{diag}(a)+U\operatorname{diag}(b)U^T).
\]

The exact standard-library verifier obtains

\[
M-L(D)
=
\frac{146559639035124021415276996805890043231942837950575743396618750000000000000006}
{24414062500000000044433593750000000020529785156250000000284375000000000000001}
\]

where `M=L(v_q)`. Numerically this is

\[
6.00308281487868\ldots>0.
\]

The candidate lies only

\[
0.0030828148786799063\ldots
\]

below the non-global pair-trap vertex `p`. The full target support width in this same direction is

\[
3516399730246630,
\]

so the candidate's normalized gap to the unique target maximum is only

\[
1.707167351664437\times10^{-15}.
\]

This is an exact all-24 common-direction computation.

## 3. Exact target-hull certificate: this is not an MOC4 counterexample

The determinant has an exact three-vertex Caratheodory representation

\[
D=\lambda_1v_{1234}+\lambda_2v_{1342}+\lambda_3v_{4321},
\]

with one common positive denominator

`910584953393554689157264615176269532015710887308640136729356493537128125000037297559691`

and corresponding nonnegative numerators

- `2550683187709637288381932044084057229756679314392876562500000000000000`,
- `2240297798370834692485897855498769059672512066842028125000000000000000`,
- `910584953393554684366283629095797551147880987725813847300165112302223437500037297559691`.

They sum exactly to the common denominator and reconstruct both real and imaginary parts of `D` exactly. Therefore the dense candidate is rigorously inside the actual 24-point target hull.

## 4. Full elementary `SU(2)` pair envelopes are almost stationary

For any row pair `(r,s)`, vary `U` through the **full embedded `SU(2)` orbit** on that row pair. Conjugating the two diagonal `a`-entries by the corresponding `2 x 2` gate writes the determinant support exactly as

\[
h(n)=A_0+c_xn_x+c_yn_y+c_zn_z,
\qquad n\in S^2,
\]

with the current unitary at `n=(0,0,1)`. Hence the exact improvement available anywhere on that complete pair orbit is

\[
\Delta_{rs}=\sqrt{c_x^2+c_y^2+c_z^2}-c_z.
\]

The verifier computes all coefficients with rational arithmetic. In every one of the six pairs, `c_z>0`, and uses the exact bound

\[
\Delta_{rs}
\le \frac{c_x^2+c_y^2}{2c_z}
<\frac1{400}.
\]

The six numerical values of these rigorous rational upper bounds are

| pair | upper bound for full-`SU(2)` improvement |
|---|---:|
| `(1,2)` | `3.4544903933e-6` |
| `(1,3)` | `1.0723075831e-4` |
| `(1,4)` | `1.9119042503e-4` |
| `(2,3)` | `2.2504958246e-3` |
| `(2,4)` | `4.7336422995e-4` |
| `(3,4)` | `5.7079145422e-5` |

Thus every complete elementary pair orbit can improve this dense true-unitary point by **less than `1/400`**, while the unique target vertex `q` beats it by **more than `6`**. In particular the ratio of the common-direction global deficit to the largest single-pair improvement is rigorously greater than `2400`.

This is stronger than checking six endpoint transpositions: it uses the entire continuous `SU(2)` pair sphere in each root direction.

## 5. Why this is not an isolated numerical accident

The Cayley curve gives an exact local explanation. Since

\[
Q(t)=I-2tS+2t^2S^2+O(t^3),
\]

direct determinant expansion gives

\[
D(t)
=v_{4321}
+(-99534232-784537096i)t^2
+O(t^3),
\]

with **zero linear term**. The standard-library verifier checks these coefficients by truncated exact polynomial arithmetic.

More importantly, the second-order displacement points strictly into a target-hull cone:

\[
-99534232-784537096i
=\alpha\,(v_{1234}-v_{4321})
+\beta\,(v_{1342}-v_{4321}),
\]

where

\[
\alpha=\frac{497504682718}{1776074271}>0,
\qquad
\beta=\frac{1310894256442}{5328222813}>0.
\]

The barycentric coordinate functions are analytic near `t=0`. Therefore for every sufficiently small positive `t`, the Cayley determinant lies in

\[
\operatorname{conv}\{v_{1234},v_{1342},v_{4321}\},
\]

while `U(t)` is dense for all sufficiently small nonzero `t` because every off-diagonal Cayley entry has a nonzero first-order coefficient `-2S_ij t` and the diagonal entries remain near one.

At the same time, for each row pair the transverse Bloch coefficients satisfy `c_x,c_y=O(t)` while the positive `c_z` tends to the strict permutation-pair reserve. Consequently

\[
\max_{r<s}\Delta_{rs}(t)=O(t^2)\to0,
\]

but

\[
L(v_{3412})-L(D(t))\to6.
\]

So even **inside the true target hull and away from every zero entry**, dense true-unitary points can be arbitrarily close to stationary on every elementary pair orbit while retaining a fixed nonzero common-direction deficit to the global target-support vertex.

### Consequence for proof strategy

Any proposed implication of the form

> dense true-unitary + sufficiently small residual on every elementary pair orbit => approximately globally support-maximizing

is false without an additional genuinely multi-root/global hypothesis. Excluding monomial matrices or zero entries does not repair it. A proof must retain the cross-root/mixed interaction or another global comparison.

This is a proof-method obstruction, not a target counterexample.

## 6. Exact relation to the previous pair trap

The previous run exhibited the permutation `p=4321` as a strict maximizer on each of its six complete elementary pair orbits even though `q=3412` is globally better by `6`. The new result pushes that phenomenon off the monomial locus into an exact dense true-unitary family and, at the explicit rational point, certifies actual target-hull containment.

Thus the earlier objection cannot be dismissed as a permutation-boundary artifact. Approximate rootwise stationarity remains insufficient in the generic interior.

## 7. Application of the named account04/B09 zero-face result

The partner theorem gives a sharp nonlinear restriction exactly **on** a genuine zero-entry face: an aligned external coefficient is at most `1/3`, using `q^+=ps^T`. The present unitary has no zero entries and no zero `2 x 2` minors, so it lies outside that theorem's hypothesis. As `t->0`, however, it converges to the Weyl permutation `P_4321`, where the aligned-external coefficient is zero and the partner cap is trivially satisfied.

This supplies a precise compatibility lesson for the collective proof:

1. the account04/B09 theorem genuinely constrains the exact zero-face branch;
2. it cannot by itself control dense interior points that approach a safe zero-face Weyl point while remaining globally nonoptimal in the same support direction;
3. therefore any generic-to-zero-face reduction must carry a **quantitative global support payment**, not merely pairwise near-stationarity or proximity to the zero face.

That is directly aligned with the lead's remaining mixed-root/MSQR-NDI obligation.

## 8. Next exact B08 obligation

`MOC4-EXACT-INTERIOR-STATIONARY-ADVERSARY-v1`:

Move from **approximate** pair stationarity to an exact nonmonomial interior stationary point for one common support functional, while keeping simple complex spectra and true-unitary compatibility. Then either:

1. find an exact/all-24 positive separating gap, which would be a genuine MOC4 counterexample and must be independently reproduced; or
2. prove that the exact stationarity equations force the additional mixed-root payment needed by the lead's MSQR/NDI split.

The present run shows that reducing pair residuals alone cannot be the missing theorem.

## 9. Verification and integrity

`verify_dense_pair_trap.py` uses only the Python standard library `fractions.Fraction` and exact Gaussian-rational arithmetic. It checks:

- exact orthogonality and determinant-one status of the Cayley unitary;
- all 16 unitary entries and all 36 `2 x 2` minors nonzero;
- all 24 target support values and the unique `3412` maximum;
- exact candidate determinant and common-direction gap;
- exact nonnegative three-vertex hull certificate;
- all six full-`SU(2)` Bloch-envelope bounds;
- exact second-order determinant series and positive tangent-cone coefficients.

A narrow changed-content review found no credentials, signed URLs, scheduler IDs, machine paths, benchmark material, unrelated private transcripts, email/Drive data or public-dispatch instructions. No paid model/API/Codex, remote workflow, scheduler repair, cross-account native action or notification mutation was used. Settings not genuinely exposed remain `UNKNOWN`/`UNVERIFIED`.
