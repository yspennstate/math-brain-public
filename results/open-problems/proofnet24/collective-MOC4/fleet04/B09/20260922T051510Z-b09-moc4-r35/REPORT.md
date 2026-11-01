# MOC4 fleet04/B09 — full continuous Spin(6) stationarity behind the bi-orientation gates

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** Marcus–de Oliveira, complex normal `4 x 4` case (`MOC4`)  
**Worker/run:** fleet04/B09, `20260922T051510Z-b09-moc4-r35`  
**Assignment:** integrate the valid algebraic/geometric pieces and prove the exact remaining unitary-orbit step, including limit cases  
**Outcome:** `ESSENTIAL_STEP_APPLIED`. The parent MOC4 statement remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact source state consumed

I used the latest complete campaign-lead version available at run start, fleet03/B07
`MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`,
`proofnet24/collective-MOC4/fleet03/B07/20260922T043708Z-fleet03-B07-MOC4-r11/REPORT.md`.
For a fixed support normal it gives exact subgroup-cubature and bidirectional V4/pair ceilings for any hypothetical positive support gap, and identifies the remaining task as excluding a genuine global support maximizer in the positive-reserve branch using same-unitary geometry/stationarity.

The required named OTHER-account result actually consumed and applied is the assigned partner fleet01/B07
`MOC4-BIORIENTATION-PAIR-GATE-v1`,
`proofnet24/collective-MOC4/fleet01/B07/20260922T040155Z-a01-b07-moc4-r12/REPORT.md`.
In the real exterior-square model
`O=Lambda^2 U in SO(6)`, written as a `3 x 3` array of real `2 x 2` blocks `B_{alpha beta}`, it defines

\[
 D_{\alpha\beta}=\det B_{\alpha\beta},\qquad
 R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2
\]

and, for the structured spectral coefficients `(K,X)`, the support is

\[
 s(O)=\sum_{\alpha,\beta}
 \left(K_{\alpha\beta}D_{\alpha\beta}
 +\frac12X_{\alpha\beta}R_{\alpha\beta}\right). \tag{1}
\]

That partner proved the discrete row-pair and column-pair gates
`T^L_{alpha gamma} >= |C^L_{alpha gamma}|` and
`T^R_{beta delta} >= |C^R_{beta delta}|`
at every global support maximizer.

I also use fleet03/B09 `MOC4-CYCLE-SEPARATOR-NOGO-v1`,
`proofnet24/collective-MOC4/fleet03/B09/20260922T035131Z-fleet03-B09-moc4-r11/REPORT.md`,
only as an exact negative-control datum. It gives a genuine `SO(6)` point outside the 24-even-endpoint coefficient hull for an *unstructured* pair `(K_cycle,X_cycle)`. Fleet01/B07's late dependency note checked that this point nevertheless passes all six discrete bi-orientation gates. It is not an MOC4 counterexample.

A compatible same-account dependency published during this invocation was also consumed before finalization: fleet04/B08
`MOC4-CUBATURE-ROOF-RIGIDITY-v1` / `MOC4-CUBATURE-BOUNDARY-DEGENERACY-v1`,
`proofnet24/collective-MOC4/fleet04/B08/20260922T051237Z-fleet04-B08-MOC4-r11/REPORT.md`.
It proves that a violator saturating the lead's seven-subgroup cubature ceiling must lie on a highly degenerate simultaneous endpoint-roof tie; if any active subgroup roof is uniquely exposed, saturation forces a proper coordinate block and is MOC4-safe. Thus on the generic branch the remaining maximizer is genuinely strict-interior, exactly where the continuous stationarity theorem below is the relevant next orbit condition.

## 2. New theorem: `MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1`

Let `O in SO(6)` be a local, hence in particular a global, maximizer of (1) for fixed real `3 x 3` coefficient matrices `(K,X)`. No spectral genericity, invertibility, nonzero-entry, or nonzero-minor assumption is made.

Fix two distinct row planes `alpha<gamma`. For each block column `beta`, write

\[
 A_\beta=B_{\alpha\beta},\qquad G_\beta=B_{\gamma\beta}.
\]

For real `2 x 2` matrices define the determinant polarization

\[
 q(A,Y):=
 A_{11}Y_{22}+A_{22}Y_{11}
 -A_{12}Y_{21}-A_{21}Y_{12},
 \tag{2}
\]
so that
`det(A+tY)=det A+t q(A,Y)+t^2 det Y`.

Then for **every** real `2 x 2` matrix `Z` a maximizing point satisfies the exact linear stationarity identity

\[
\boxed{
\sum_\beta\left[
 K_{\alpha\beta}q(A_\beta,ZG_\beta)
 -K_{\gamma\beta}q(G_\beta,Z^TA_\beta)
 +\frac12(X_{\alpha\beta}-X_{\gamma\beta})
   \langle A_\beta,ZG_\beta\rangle_F
\right]=0.}
\tag{3}
\]

Because (3) is linear in `Z`, it is equivalent to the four equations obtained from the orthogonal basis

\[
 I,\quad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
 S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 T=\begin{pmatrix}0&1\\1&0\end{pmatrix}. \tag{4}
\]

For an orthogonal `Z`, write `epsilon=det Z in {+1,-1}`. Then
\[
q(G,Z^TA)=\epsilon\,q(A,ZG), \tag{5}
\]
and (3) becomes
\[
\boxed{
B^{L,\epsilon}_{\alpha\gamma}(Z):=
\sum_\beta\left[
 (K_{\alpha\beta}-\epsilon K_{\gamma\beta})
 q(A_\beta,ZG_\beta)
 +\frac12(X_{\alpha\beta}-X_{\gamma\beta})
 \langle A_\beta,ZG_\beta\rangle_F
\right]=0.}
\tag{6}
\]

Thus there are twelve exact scalar off-block stationarity equations, four for each of the three row-plane pairs.

### Proof

Let `L_Z` be the real `6 x 6` skew-symmetric matrix which is zero outside row-plane blocks `(alpha,gamma)` and has
\[
(L_Z)_{\alpha\gamma}=Z,\qquad
(L_Z)_{\gamma\alpha}=-Z^T. \tag{7}
\]
Then
\[
O(\theta)=\exp(\theta L_Z)O\in SO(6). \tag{8}
\]
Since the `Spin(6)=SU(4)` exterior-square map is onto `SO(6)`, this is a genuine unitary-orbit variation, not an independent-block relaxation.

At `theta=0`,
\[
A_\beta'=ZG_\beta,\qquad
G_\beta'=-Z^TA_\beta. \tag{9}
\]
Since `R(B)=||B||_F^2/2`,
\[
R(A_\beta)'=\langle A_\beta,ZG_\beta\rangle_F,\qquad
R(G_\beta)'=-\langle A_\beta,ZG_\beta\rangle_F. \tag{10}
\]
Since `D(B)=det B`,
\[
D(A_\beta)'=q(A_\beta,ZG_\beta),\qquad
D(G_\beta)'=-q(G_\beta,Z^TA_\beta). \tag{11}
\]
Differentiating (1) gives exactly the left side of (3). A local maximizer has zero derivative for every `Z`, proving (3). Equation (5) follows by polarizing
`det(ZG)=det(Z)det(G)` for orthogonal `Z`; substituting it gives (6). QED.

## 3. Exact continuous closure of the partner's discrete gate

When `Z in O(2)`, the path (8) has the closed form on the selected four-dimensional row subspace

\[
W_Z(\theta)=
\begin{pmatrix}
\cos\theta\,I_2&\sin\theta\,Z\\
-\sin\theta\,Z^T&\cos\theta\,I_2
\end{pmatrix}. \tag{12}
\]

A direct determinant/Frobenius expansion gives

\[
\boxed{
s(W_Z(\theta)O)-s(O)
=
-\sin^2\theta\,
\bigl(T^L_{\alpha\gamma}-\epsilon C^L_{\alpha\gamma}\bigr)
+
\sin\theta\cos\theta\,
B^{L,\epsilon}_{\alpha\gamma}(Z).}
\tag{13}
\]

Therefore, at a stationary point satisfying (6), fleet01/B07's discrete inequality
`T^L>=|C^L|` is **exactly enough to control the whole circle**, not only the `theta=pi/2` swap:
\[
s(W_Z(\theta)O)\le s(O)\quad\text{for every }\theta. \tag{14}
\]

This identifies what the discrete partner theorem was missing: a point can pass all endpoint swaps while still have a nonzero first derivative and hence fail even local maximality.

There is also a useful completeness statement. The tangent algebra `so(6)` decomposes into:
- three block-diagonal `so(2)` directions; and
- the twelve off-block directions (7), four for each unordered row-plane pair.

The block-diagonal directions leave every `D_{alpha beta}` and `R_{alpha beta}` invariant, hence leave (1) invariant identically. Consequently the twelve equations (3) are the **full first-order `SO(6)` stationarity system modulo this exact three-dimensional gauge invariance**. No additional first-order unitary-orbit directions are unpaid.

The same construction can of course be written on column planes by right multiplication. Those equations are necessary too, but the left system already spans the non-gauge tangent directions.

## 4. Decisive exact application: the current cycle separator is not a maximizer

For the fleet03/B09 exact genuine `SO(6)` datum
\[
O=
\begin{pmatrix}
1&0&0&0&0&0\\
0&7/25&0&0&0&-24/25\\
0&0&1&0&0&0\\
0&-504/725&0&20/29&0&-147/725\\
0&0&0&0&1&0\\
0&96/145&0&21/29&0&28/145
\end{pmatrix}, \tag{15}
\]
and its separating unstructured coefficients
\[
K_{\rm cyc}=3\,\mathrm{diag}(1,1,-1),\qquad
X_{\rm cyc}=2
\begin{pmatrix}
0&-1&1\\
1&0&-1\\
-1&1&0
\end{pmatrix}, \tag{16}
\]
fleet01/B07's late note had already found all three row discrete gate slacks strictly positive:
\[
\frac{4446471}{1051250},\qquad
\frac{44037}{42050},\qquad
\frac{818424}{525625}. \tag{17}
\]

Nevertheless the new stationarity equations fail. For pair `(alpha,gamma)=(0,1)` and `Z=I`,
\[
B^{L,+}_{01}(I)=-\frac{27216}{18125}\ne0. \tag{18}
\]
Other exact nonzero derivatives are
\[
B^{L,+}_{02}(I)=-\frac{648}{725},\qquad
B^{L,+}_{12}(I)=\frac{19278}{105125}. \tag{19}
\]
The reflection basis gives the corresponding opposite signs; the `J,T` derivatives vanish for this sparse datum.

This is not merely infinitesimal. Take the exact rational row-plane rotation on planes `(0,1)` with `Z=I` and half-angle parameter `t=-1/100`, so
\[
c=\frac{9999}{10001},\qquad s=-\frac{200}{10001}. \tag{20}
\]
The resulting matrix is again exactly in `SO(6)`, and the support increases from
\[
s(O)=\frac{1605549}{525625} \tag{21}
\]
by
\[
\boxed{
s(O')-s(O)=
\frac{59577629088}{2102920521025}>0.}
\tag{22}
\]
Hence the exact cycle-separator point is **not even a local maximizer** for its own separating normal. It remains a valid refutation of coefficientwise even-endpoint convexity, but it cannot inhabit the campaign's global-maximizer residual.

The companion verifier `verify_continuous_biorientation.py` uses only `fractions.Fraction`; it checks (15) is in `SO(6)`, reconstructs the exact `(R,D)` arrays, rechecks the discrete slacks, evaluates all twelve basis derivatives, constructs the exact rational improving rotation, and verifies (22) without tolerance. Captured output is `VERIFY_OUTPUT.txt`.

## 5. Compact conditional end-to-end argument after this run

Assume MOC4 fails in some support direction. By compactness of the unitary orbit, there is a genuine global support maximizer with positive gap over all 24 endpoint products.

The current campaign lead's subgroup-cubature/V4/pair ceilings and inherited boundary reductions constrain that maximizer to the positive-reserve residual. Fleet04/B08's cubature-roof rigidity removes generic equality on the cubature boundary, leaving a strict-interior maximizer except for an explicit simultaneous endpoint-roof degeneracy. The assigned partner fleet01/B07 forces all discrete bi-orientation gates. The present theorem now forces the complete twelve-equation first-order `Spin(6)` stationarity system and, together with those gates, closes every orthogonal row-pair great circle exactly by (13).

Therefore the first essential remaining implication can now be stated without an unpaid generic phrase such as "use stationarity":

> **`MOC4-STRUCTURED-SPIN6-STATIONARY-RIGIDITY-v1` (OPEN).**  
> For coefficient matrices `(K,X)` that actually arise from complex spectra `(a,b)` and a support direction, no genuine `O=Lambda^2 U in SO(6)` with positive support gap over the 24 permutation endpoints can simultaneously satisfy:
> 1. the twelve exact stationarity equations (3);
> 2. the six fleet01/B07 bi-orientation gates;
> 3. the same-unitary identities linking `(P,D,R)`;
> 4. the lead's subgroup-cubature and bidirectional V4/pair positive-reserve ceilings; and
> 5. on the generic cubature branch, the strict-interior condition supplied by fleet04/B08 (with its explicit all-roofs-tied degeneracy treated separately).

Proving this implication, together with the already-isolated endpoint-roof tie branch, closes the remaining genuine unitary-orbit step. A target-level disproof must instead produce actual spectra, a support direction, and a true unitary satisfying all of these conditions while retaining a positive gap.

The theorem in this run itself has **no simple-spectrum, invertibility, nonzero-minor, or nonsingularity hypothesis**; degeneracies merely make some of the equations vanish. Thus it introduces no new limit-case debt. I do not claim here to have independently reproved every inherited repeated-spectrum/boundary reduction.

## 6. Honest status

Primary status: **`ESSENTIAL_STEP_APPLIED`**.

A specific intermediate candidate is refuted: the fleet03/B09 exact cycle-separator datum, despite passing all six discrete bi-orientation gates, cannot be a local/global support maximizer because it violates the exact continuous stationarity equations and admits the rational improving rotation (20)-(22).

Full MOC4 remains open. No benchmark material, sealed answer, credential, email/Drive content, paid API/model, Codex, remote workflow, or public release was used.
