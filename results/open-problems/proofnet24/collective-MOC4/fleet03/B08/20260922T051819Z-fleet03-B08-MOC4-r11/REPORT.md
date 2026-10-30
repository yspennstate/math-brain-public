# MOC4 fleet03/B08 — dense Cayley facet adversary and exact pair-Bloch envelope

Status: **AUXILIARY_ONLY; parent MOC4 remains OPEN / not proved / not disproved.**  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Assignment and inherited results

This run executes the exact fleet03/B08 assignment: construct exact or rigorously enclosed candidates from **true unitary matrices and complex spectra**, and test separation from **all 24 target vertices in one common real-linear direction**. Assigned partner: fleet04/B09.

Consumed assigned-partner source: fleet04/B09 `MOC4-STANDARD-CHANNEL-CEILING-v1`, handoff `20260922T041453Z-fleet04-B09-MOC4-standard-channel-ceiling.md`, whose source report blob is `faaf77b4fcebb8fed6a6c9763251acc1042105ac`. It proves that a genuine support violation of size `gamma` must obey `gamma <= Kstd-Delta`, with the same-unitary standard channel bounded by endpoint data. I also consumed fleet01/B09 `MOC4` handoff `20260922T044740Z-b09-moc4-r11`, report blob `9b496cd2cb18df7a577ab0997de1117a8c144c98`, which proves the entire flat complex-Hadamard phase fiber has a positive common-permutation lift and therefore directs adversary work away from the flat unistochastic center.

## 1. Exact pair-Bloch envelope for a true-unitary row-pair orbit

Let

`A=diag(a_1,...,a_4)`, `C=U diag(b_1,...,b_4) U*`, `D(U)=det(A+C)`.

Fix a row pair `r<s` and left-multiply `U` by an arbitrary embedded `V in SU(2)` on `span(e_r,e_s)`. By unitary conjugation,

`det(A + V C V*) = det(V* A V + C)`.

On this two-dimensional block write

`diag(a_r,a_s) = m I + d sigma_z`,  `m=(a_r+a_s)/2`, `d=(a_r-a_s)/2`.

For `V in SU(2)`,

`V* sigma_z V = n_x sigma_x + n_y sigma_y + n_z sigma_z`,  `n in S^2`.

**Lemma (PAIR-BLOCH-ENVELOPE-v1).** There are complex numbers `alpha,beta_x,beta_y,beta_z`, depending on the spectra, `U`, and the chosen pair but not on `n`, such that

`D(n)=alpha + beta_x n_x + beta_y n_y + beta_z n_z`.

Hence for every real-linear support functional `L`,

`h(n)=L(D(n)) = A0 + c_x n_x + c_y n_y + c_z n_z`,

and the exact maximum over the full genuine `SU(2)` pair orbit is

`max h = A0 + sqrt(c_x^2+c_y^2+c_z^2)`.

At the current point `n=e_z`, the pair-orbit improvement is

`Delta_pair = sqrt(c_x^2+c_y^2+c_z^2)-c_z >= 0`.

Therefore every genuine global support maximizer must, for all six row pairs, satisfy `c_x=c_y=0` and `c_z>=0`.

**Proof.** Only the chosen 2-by-2 block of `V* A V` changes. Write it as `m I+d S(n)` where `S(n)=n_x sigma_x+n_y sigma_y+n_z sigma_z`. In the determinant expansion of `M_0+d E(S(n))`, terms involving the perturbation have degree at most two because it is supported on two rows and columns. The degree-one term is linear in the entries of `S(n)`, hence linear in `n`. The degree-two term is the complementary principal minor times `det S(n)=-1`, independent of `n`. The degree-zero term is also independent of `n`. Thus `D(n)` is affine in `n`. Applying `L` makes the coefficients real, and maximizing an affine function over the unit sphere gives the stated Euclidean norm. No invertibility, simple-spectrum assumption, or nonzero determinant is used. QED.

For exact computation one needs only the six axis values. With `h_{+x},h_{-x},...`,

`c_x=(h_{+x}-h_{-x})/2`, `c_y=(h_{+y}-h_{-y})/2`, `c_z=(h_{+z}-h_{-z})/2`.

This gives a source-valid stationarity filter for true-unitary adversary searches and avoids inverse-matrix stationarity formulas at singular points.

## 2. Exact rational Cayley adversary

Use the simple complex spectra

`a=(18-17i, -20+2i, 15-22i, -21+2i)`,

`b=(-19+4i, 25-5i, 18-i, -18+i)`.

Let `K` be the skew-Hermitian matrix encoded by the 16 rational Cayley coordinates

`(483/50, -63/25, -72/25, -163/50, 33/50, 23/5, -139/25, 9/25, -187/50, 6/5, 147/50, 3/10, 31/10, -14/25, 1/50, -7/2)`:

the first four are the imaginary diagonal entries of `K`; each subsequent consecutive pair is the real and imaginary part of the upper-triangular entries in lexicographic order `(12),(13),(14),(23),(24),(34)`, with `K_{ji}=-conj(K_{ij})`.

Define the exact true unitary

`U=(I+K)^{-1}(I-K)`.

The verifier checks `U U*=I` exactly over rational complex arithmetic. All 16 entries are nonzero and

`min_{ij}|U_ij|^2 = 4297768791625000 / 431850208768934029 > 99/10000`.

Thus this is not a formal bistochastic surrogate and it is not supported on a sparse Givens graph.

The exact determinant is

`D = 1079532813472946700976/431850208768934029`

`    - i 1212083384688988632932/431850208768934029`.

Take the single common support functional

`L(z) = -5782 Re(z) + 19099 Im(z)`.

Exact enumeration of **all 24** target vertices

`v_sigma=prod_i(a_i+b_{sigma(i)})`

gives

`M=max_sigma L(v_sigma) = -61633500`, uniquely at `sigma=1234`,

`m=min_sigma L(v_sigma) = -59822291610`.

For the true-unitary determinant,

`M-L(D) = 2774999449515476249040000 / 431850208768934029 > 0`.

Normalized by the full endpoint support width,

`(M-L(D))/(M-m)`

`= 92499981650515874968000 / 860255089365746349873794173`

`≈ 1.0752622424903614e-4`.

So this genuine, all-entry-nonzero Cayley unitary lies only about **0.01075% of the full support width** inside the exposed endpoint support line. It is still not a counterexample.

## 3. Exact target-hull rescue

The candidate is rigorously inside the actual target hull, not merely below the one tested support line. Let the vertices use one-line permutations. Then

`D = lambda_0 v_1234 + lambda_1 v_1243 + lambda_2 v_1342`,

with common denominator

`Q=132146163883293812874`

and numerators

`1697634460488463499`,
`22235572512143239175`,
`108212956910662110200`.

All are nonnegative and sum exactly to `Q`. The verifier checks the complex identity exactly.

## 4. Pair-orbit stationarity stress

Applying the pair-Bloch envelope to this same exact candidate and the same common `L`, the pair `(2,3)` has nonzero transverse coefficients. Let

`Delta_23 = sqrt(c_x^2+c_y^2+c_z^2)-c_z`.

Without evaluating a square root, exact rational squaring verifies

`Delta_23 > (M-m)/100000`

and simultaneously

`Delta_23 < M-L(D)`.

Thus an actual embedded `SU(2)` row-pair rotation can improve this already near-facet candidate by more than `10^{-5}` of the full endpoint width, but even the exact pair-orbit optimum still remains below the target support maximum. This supplies a rigorous next-stage adversary mechanism rather than a negative formal coefficient.

## 5. Use of the named partner result

For this endpoint datum the six Klein-four fiber means give

`Delta = 132071462`, `Kstd = 29871989917`.

Hence fleet04/B09's standard-channel ceiling leaves a large positive reserve `Kstd-Delta=29739918455`; it does not certify this instance globally. Its companion escape estimate, together with fleet01/B09's flat-phase lift, says any residual violator must move far enough from the flat unistochastic center. This candidate does exactly that (`p_min≈0.009952`) while keeping every unitary entry nonzero, so it probes the intended pair-strict residual rather than a ruled-out flat or arbitrary-bistochastic mechanism.

## 6. Next exact obligation

`MOC4-PAIR-BLOCH-DESCENT-v1`: use the exact six pair envelopes as a coordinate-wise ascent map on true unitaries. Either (i) prove that every pair-stationary point satisfies the 24-vertex support bound by combining the six conditions with the partner's `Kstd/Delta` reserve and subgroup roofs, or (ii) construct an exact/algebraically enclosed pair-stationary true unitary with a strict common-direction gap `L(D)>M`, which would be a genuine MOC4 counterexample. Preserve the current Cayley datum as a calibration point.

The parent MOC4 target remains OPEN. Negative formal coefficients, arbitrary bistochastic matrices, and failure of a sufficient lift are not treated as target counterexamples.
