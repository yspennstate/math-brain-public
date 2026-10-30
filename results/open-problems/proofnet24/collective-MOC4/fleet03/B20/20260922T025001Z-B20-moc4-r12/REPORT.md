# MOC4 fleet03/B20 — pair-twirl two-point bound and quantitative curvature collar

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker:** fleet03/B20  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and current inputs

For complex normal `4 x 4` matrices `A,B` with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

\[
\det(A+B)\in \operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

Fix a support direction `eta` and diagonalize one matrix, so the support value at a true unitary `U` is

\[
h(U)=\Re\!\left(\eta\det(D_a+UD_bU^*)\right),
\]

and let

\[
M=\max_{\sigma\in S_4}\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\]

This run directly consumes and combines the following completed inputs.

1. **Assigned partner fleet04/B09, `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`**, report blob `1ec092caac4aa78fb3998199849f632387a0c18f`. For every true unitary and every embedded row-pair `SU(2)` orbit, the Haar-averaged *complete exterior-minor data* admit an exact probability lift to the 24 permutation endpoints. The same holds for column pairs. Consequently the Haar-averaged support is at most `M`. This is a true-unitary theorem, not a bistochastic relaxation.
2. **fleet04/B08, `MOC4-PAIR-FLAT-BOUNDARY-v1`**, report blob `3c71dc6a046f699b3248957d660b2c02fe968efb`. On any row-pair sphere the support is exactly affine in the Bloch vector:
   \[
   h(GU)=\alpha+c\cdot n.
   \]
   The identity and opposite/transposition endpoints are the two antipodal poles, hence have values `alpha+c_z` and `alpha-c_z` after relabelling axes.
3. **fleet02/B07, `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` and pair-Hessian trace**, report commit `3abc17877e43f8e374a4565db8bf708811c12042`. In exact Spin(6) coordinates, with nonconstant support `s=k+x`,
   \[
   k=\langle D,K\rangle,\qquad x=\tfrac12\langle R,X\rangle,\qquad c=\tfrac16\langle \mathbf 1,X\rangle,
   \]
   the six column-transposition class sum is
   \[
   \sum_{\tau\text{ transposition}}s(UP_\tau)=2k+6c,
   \]
   and at a pair-stationary point the exact pair-Hessian trace is
   \[
   \operatorname{Tr}H_{\rm pair}=-8\{2k+3(x-c)\}.
   \]
   It also proves that every support violator of gap `gamma>0` is quantitatively separated from every odd-Weyl equality face.
4. **fleet02/B09, `MOC4-CARTAN-POLARIZATION-v1`**, handoff blob `89877a13a6c65243cc0c701c5fb634ef495a19f9`. If the Cartan zero endpoint for each entry is support-safe, a gap-positive global maximizer is quantitatively separated from zero and common-block entry faces.

The previous B20 endpoint parity-payment certificate remains a sufficient gate, but this run changes mechanism and uses exact pair-orbit averaging rather than another Birkhoff/slack optimization.

## 2. New theorem — exact pair-twirl two-point support inequality

### `MOC4-PAIR-TWIRL-TWO-POINT-v1`

For **every** true unitary `U`, every row transposition `tau`, and every column transposition `tau`,

\[
\boxed{h(U)+h(\tau U)\le 2M}
\qquad\text{and}\qquad
\boxed{h(U)+h(U\tau)\le 2M}.
\tag{1}
\]

No maximizing, stationarity, genericity, nonsingularity, or simple-spectrum assumption is needed.

### Proof

Fix a row pair. By `MOC4-PAIR-FLAT-BOUNDARY-v1`, throughout its embedded `SU(2)` orbit the support has the exact form

\[
h(GU)=\alpha+c\cdot n,\qquad n\in S^2.
\tag{2}
\]

Choose the polar axis so `G=I` corresponds to `n=e_z`. The opposite pole has the same determinant/support value as the row-transposed endpoint, so

\[
h(U)=\alpha+c_z,\qquad h(\tau U)=\alpha-c_z.
\tag{3}
\]

Haar measure on the pair orbit has `\int_{S^2}n\,dn=0`, hence

\[
\int h(GU)\,dG=\alpha=\frac{h(U)+h(\tau U)}2.
\tag{4}
\]

Now apply the assigned partner's `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`: the Haar-averaged complete exterior-minor data are a convex combination of the 24 true permutation endpoint data. Since the support functional is linear in those data,

\[
\int h(GU)\,dG\le M.
\tag{5}
\]

Combining (4)-(5) proves the row inequality. Applying the same argument to `U*` (equivalently exchanging row/column action) proves the column inequality. QED.

This is stronger than the earlier flat-pair corollary: the partner result was invoked there only when a pair orbit was flat at a global maximizer. Equation (1) is an unconditional two-point inequality for every true unitary and every pair orbit.

## 3. Quantitative consequence for any hypothetical violator

Suppose `U_*` is a global support maximizer with positive target gap

\[
\gamma=h(U_*)-M>0.
\tag{6}
\]

Equation (1) immediately gives, for **each** of the six row and six column transpositions,

\[
\boxed{h(U_*\tau)\le M-\gamma},\qquad
\boxed{h(U_*)-h(U_*\tau)\ge2\gamma}.
\tag{7}
\]

Thus a target violator is not merely pair-strict: every one of its twelve pair-swap gaps is at least twice the target support gap.

On the exact Bloch sphere (2), at a global maximum the transverse components vanish and `c_z>=0`; equation (3) shows

\[
c_z=\frac{h(U_*)-h(U_*\tau)}2\ge\gamma.
\tag{8}
\]

So every genuine pair sphere has a uniform positive north-pole coefficient at least `gamma`. This is a quantitative interior collar in the actual unitary geometry.

## 4. New global Spin(6) scalar bound

Subtract the `U`-independent scalar term from the support and write, in the fleet02/B07 notation,

\[
s(U)=k+x,
\quad k=\langle D,K\rangle,
\quad x=\tfrac12\langle R,X\rangle,
\quad c=\tfrac16\langle\mathbf1,X\rangle,
\]

with corresponding endpoint maximum `M_even` in the same normalization.

Apply (1) to the six column transpositions and sum:

\[
6s(U)+\sum_{\tau\text{ transposition}}s(UP_\tau)\le12M_{\rm even}.
\tag{9}
\]

Using the exact class-sum identity

\[
\sum_{\tau}s(UP_\tau)=2k+6c
\tag{10}
\]

gives the universal true-unitary inequality

\[
\boxed{4k+3x+3c\le6M_{\rm even}.}
\tag{11}
\]

Equivalently,

\[
\boxed{s(U)-M_{\rm even}\le\frac{2k+3(x-c)}6.}
\tag{12}
\]

This holds for every actual unitary datum in the exact mixed-minor representation; no stationarity assumption is needed for (11)-(12).

At a pair-stationary point, fleet02/B07's exact Hessian trace identity converts (12) into

\[
\boxed{s(U)-M_{\rm even}\le-\frac1{48}\operatorname{Tr}H_{\rm pair}.}
\tag{13}
\]

In particular, a stationary point with zero pair-Hessian trace is automatically target-safe. At a gap-positive global maximizer,

\[
\boxed{2k+3(x-c)\ge6\gamma},
\qquad
\boxed{\operatorname{Tr}H_{\rm pair}\le-48\gamma}.
\tag{14}
\]

This strictly strengthens the previously known necessary condition `2k+3(x-c)>=0`: a positive target gap forces a proportionally negative aggregate pair curvature.

For consistency, summing the six pair-swap gaps yields

\[
\sum_\tau[s(U)-s(UP_\tau)]
=2\{2k+3(x-c)\},
\tag{15}
\]

and (7) gives the same lower bound `>=12 gamma`.

## 5. Combined exact collar for the surviving counterexample branch

The new pair-twirl theorem combines cleanly with the newest cross-account results.

- **Pair collar (this run):** all 12 row/column swap gaps are at least `2 gamma`.
- **Odd-orientation collar (fleet02/B07):** for every odd coloured matching `J`, if `W=max |K+X/2|,|-K+X/2|`,
  \[
  \delta_J\ge\gamma^2/(24W^2).
  \]
- **Cartan entry collar (fleet02/B09):** for each unitary entry, either its true-unitary zero endpoint is itself support-violating, or
  \[
  \sqrt{\gamma/(4W)}\le |u_{ij}|\le1-\sqrt{\gamma/(4W)}.
  \]
- **Flat pairs are already harmless (assigned partner fleet04/B09):** a flat pair orbit Haar-averages exactly into the target endpoint hull.

Therefore any hypothetical MOC4 counterexample can be pushed to a global maximizer which is quantitatively separated from every pair-flat boundary and every odd-Weyl equality face; on the branch where all Cartan zero endpoints are support-safe it is also separated from all zero/common-block entry faces. It must simultaneously obey the full true-unitary/Spin(6) stationarity equations.

This is a substantially smaller and more rigid interior than the earlier generic `pair-strict` statement.

## 6. Interaction with current no-go results

The new inequality does **not** assert a global 24-state positive lift for an individual unitary. That stronger representation was refuted exactly by fleet01/B08 on a dense true orthogonal point. Nor does it resurrect the refuted common `(P,R)` permutation lift or unconditional parity-roof gate. The lift is used only after Haar averaging on one genuine `SU(2)` pair orbit, exactly where fleet04/B09 proved it.

Likewise, fleet03/B08's one-cycle chord result shows that even a very small cyclic Givens family can consume more than 90% of the forest-endpoint support margin, so a proof cannot replace the remaining compact interior by a naive gate-by-gate convex interpolation.

## 7. First unpaid universal implication

The updated first target-level obligation is:

> **`MOC4-STRICT-COMPACT-INTERIOR-v1`.** Exclude a structured-support global maximizer `U_*` with gap `gamma>0` satisfying simultaneously:
> 1. the exact Spin(6) block orthogonality and stationarity equations;
> 2. all twelve pair-swap gaps at least `2 gamma` (equivalently the curvature bound (14));
> 3. every odd-Weyl deficit at least `gamma^2/(24W^2)`;
> 4. and, on the zero-endpoint-safe branch, the two-sided Cartan entry collar.
>
> If a Cartan zero endpoint is itself support-violating, the remaining obligation is instead the genuine zero-entry support branch; an arbitrary common-minor permutation lift is unavailable there.

The most concrete next attack is to combine the structured spectral `K,X` identities with (11)/(14) and the full complex stationarity balances, rather than seeking another unconditional positive representation.

Full MOC4 remains **OPEN**.

## 8. Verification and non-claims

The new proof is exact algebra from the cited true-unitary pair-orbit and Haar-lift theorems. The accompanying verifier checks only the arithmetic/class-sum consequences (11)-(15) on exact rational symbolic placeholders; it is not substituted for the peer theorems themselves.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive material, public posting, paid model/API, Codex, or remote workflow was used.
