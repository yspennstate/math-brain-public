# MOC4 fleet03/B07 — V4 fiber roof and pair-gap ceiling

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus-de Oliveira target  
**Worker:** fleet03/B07, campaign lead  
**Candidate:** `MOC4-V4-PAIR-GAP-CEILING-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; an endpoint-only closure shortcut is also exactly refuted. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Source-exact target and newest compatible state

For every complex normal `4 x 4` pair, after diagonalizing one matrix and writing the relative eigenbasis as a true unitary `U`, prove for every support direction `eta`

\[
h(U):=\Re\!\left(\eta\det(D_a+UD_bU^*)\right)
\le M:=\max_{\sigma\in S_4} H_\sigma,
\qquad
H_\sigma:=\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\tag{1}
\]

The owner-controlled target includes singular and repeated spectra and forbids replacing the common unitary by arbitrary bistochastic data.

The newest compatible campaign state used here is:

1. **Named OTHER-account partner consumed: fleet04/B08**, run `20260922T031434Z-fleet04-B08-MOC4-r11`, theorem `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`, report blob `0c611698463f4f00abe78c96a10308759d3cb716`. For every true `U` and every column transposition `tau`,
   \[
   \frac{h(U)+h(UP_\tau)}2\le
   R_\tau:=\max_\sigma\frac{H_\sigma+H_{\tau\circ\sigma}}2.
   \tag{2}
   \]
   If `g_tau:=2M-2R_tau`, a support violator of gap `gamma` pays the exact pair drop `2 gamma+g_tau`. This result is based on a genuine pair-symmetrized common lift, not an individual-unitary lift.
2. **fleet01/B07**, `MOC4-CARTAN-HESSIAN-PACKING-v1`, converts the true-unitary one-entry Cartan polarization into a quantitative Hessian payment on the branch where all zero-entry endpoints are safe.
3. **fleet03/B08**, `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, gives an exact filled-ellipse formula on a genuine one-cycle `SU(2)` closing orbit and a sharp payment condition `C^2<=delta_0 delta_1`.
4. **fleet03/B09**, newest exact compatibility identity `D=(1/4)E^TPE` plus imported odd-Weyl inequalities, shows that the oriented complementary-minor channel is determined by the same unistochastic `P` as levels 1 and 3.

Earlier B07 work compressed the exact support to the six `S_3` fibers of the standard representation. The present run changes mechanism: instead of trying to prove the parity-slack sufficient condition directly, it uses exact `S_4` subgroup/neighbor averaging to derive a quantitative obstruction for any support violation.

## 2. Four-point Klein fiber roof

Let `V_4` be the Klein four subgroup of `S_4`, the kernel of the action on the three complementary-pair classes. Define

\[
B_\rho:=\frac14\sum_{\sigma:\rho_\sigma=\rho}H_\sigma,
\qquad Q:=\max_{\rho\in S_3}B_\rho,
\tag{3}
\]

and

\[
m:=\frac1{24}\sum_{\sigma\in S_4}H_\sigma.
\tag{4}
\]

For a true unitary `U`, define

\[
A_V(U):=\frac14\sum_{v\in V_4}h(UP_v).
\tag{5}
\]

### Theorem 1 — exact `V_4` fiber roof

For every true unitary `U`,

\[
\boxed{A_V(U)\le Q.}
\tag{6}
\]

### Proof

In the exact 3-by-3 standard/complementary-pair reduction, right multiplication by `v in V_4` acts on the standard block by the tetrahedral signed matrix `S_v` and acts trivially on the three complementary-pair classes. The exact identities are

\[
\sum_{v\in V_4}S_v=0,
\qquad
\rho_v=e\quad(v\in V_4).
\tag{7}
\]

Thus the four-point twirl kills the oriented standard block `D` while leaving the same genuine doubly stochastic pair transport `R`. Choose a Birkhoff decomposition `R=sum_rho lambda_rho R_rho`. For each `rho`, distribute `lambda_rho` uniformly over the four permutations in its `V_4` fiber. The four even sign patterns average to zero, so this is an exact common endpoint lift of the twirled data. Therefore

\[
A_V(U)=\sum_\rho\lambda_\rho B_\rho\le Q.
\]

No common lift for the original individual `U` is asserted. ∎

Define

\[
d:=M-m,
\qquad
\Delta:=M-Q\ge0.
\tag{8}
\]

## 3. Six-transposition identity

Write the centered support at `U` as

\[
h(U)-m=k+y,
\tag{9}
\]

where `k` is the standard/oriented contribution and `y` the centered complementary-pair contribution. The Klein twirl removes precisely `k`, hence

\[
A_V(U)=m+y,
\qquad
k=h(U)-A_V(U).
\tag{10}
\]

For the six column transpositions `T_6`, the exact standard matrices and pair-class permutation matrices satisfy

\[
\sum_{\tau\in T_6}S_\tau=2I_3,
\qquad
\sum_{\tau\in T_6}R_{\rho_\tau}=2J_3.
\tag{11}
\]

Because the centered pair coefficient annihilates `J_3`,

\[
\boxed{\sum_{\tau\in T_6}h(UP_\tau)=6m+2k.}
\tag{12}
\]

Equivalently, the transposition Cayley Laplacian at `U` is `4k+6y`. This is the group-algebra form of the `[4]\oplus[31]\oplus[22]` low-frequency structure implicit in the exterior-power expansion.

## 4. Quantitative ceiling on every genuine support violation

Suppose a true unitary, not necessarily already selected by a variational argument, violates the endpoint hull:

\[
h(U)=M+\gamma,
\qquad \gamma>0.
\tag{13}
\]

From (6),

\[
k=h(U)-A_V(U)\ge M+\gamma-Q=\boxed{\gamma+\Delta}.
\tag{14}
\]

Apply the named partner theorem (2) to all six transpositions. Each neighbor satisfies

\[
h(UP_\tau)\le M-\gamma-g_\tau.
\tag{15}
\]

Let `G=sum_tau g_tau`. Summing (15) and comparing with (12) gives

\[
\boxed{k\le3d-3\gamma-\frac G2.}
\tag{16}
\]

Combining (14) and (16) proves:

### Theorem 2 — `MOC4-V4-PAIR-GAP-CEILING-v1`

Every genuine true-unitary support violation obeys

\[
\boxed{0<\gamma\le\frac{3d-\Delta-G/2}{4}.}
\tag{17}
\]

Therefore

\[
\boxed{\Delta+\frac G2\ge3d
\quad\Longrightarrow\quad
h(U)\le M\text{ for every }U\in U(4).}
\tag{18}
\]

If the maximizing endpoint is unique with second-endpoint gap `delta`, the partner theorem gives `g_tau>=delta` for all six transpositions and hence

\[
\boxed{\gamma\le\frac{3d-\Delta-3\delta}{4}.}
\tag{19}
\]

No stationarity, inverse determinant matrix, or arbitrary-bistochastic relaxation is used in (17).

## 5. Exact falsification of the tempting endpoint-only closure

Condition (18) is useful but is not automatic, even for simple real spectra. The committed Fraction-only verifier uses

\[
a=(-1,2,1,0),\qquad b=(-1,1,-2,2),\qquad\eta=1.
\tag{20}
\]

All four entries of each spectrum are distinct. Exact endpoint arithmetic gives

\[
M=36,\qquad m=\frac{29}{6},\qquad Q=15,
\]

so

\[
d=\frac{187}{6},\qquad\Delta=21.
\]

The six pair gaps are

\[
36,\ 9,\ 36,\ 32,\ 4,\ 24,
\]

hence `G=141`. Therefore

\[
\Delta+\frac G2-3d=-2<0,
\]

and (17) leaves the exact residual allowance

\[
\gamma\le\frac12.
\tag{21}
\]

So a proof that merely tries to establish (18) for every endpoint configuration cannot close MOC4.

The verifier goes further. It constructs an explicit half-integer function `f:S_4->Q` with the same endpoint mean, a global maximum `f(e)=M+1/2`, all six transposition-pair roofs, every `V_4`-coset roof, and the exact low-frequency identity

\[
A(A-2I)(A-6I)f=0
\tag{22}
\]

for the central transposition adjacency operator `A`. Thus the bound `1/2` is sharp in this natural group/twirl relaxation. The witness is **not** claimed to arise from a unitary determinant orbit and is **not** a MOC4 counterexample. It proves that the remaining gap can only be removed by additional same-unitary compatibility, not by recycling the same pair/fiber roofs.

The exact terminal output is

```text
PASS MOC4-V4-PAIR-GAP-CEILING-v1
M = 36 m = 29/6 Q = 15 d = 187/6 Delta = 21 G = 141
abstract_low_frequency_ceiling = 1/2
endpoint_only_closure_slack = -2
```

## 6. Smallest conditional full deduction after this run

1. Use the campaign's generic reduction to isolate the simple-spectrum, irreducible, strict-support core; singular/repeated/common-block cases return through the established source-valid boundary/continuity reductions rather than being discarded.
2. For each support direction apply the exact `V_4` fiber roof and the fleet04/B08 pair-specific roofs.
3. If `Delta+G/2>=3d`, Theorem 2 closes that entire support direction for all true unitaries.
4. Otherwise any counterexample is confined to the explicit positive reserve
   \[
   \mathcal R:=3d-\Delta-G/2>0,
   \qquad 0<\gamma\le\mathcal R/4,
   \tag{23}
   \]
   and must simultaneously satisfy the exact same-unitary compatibility now available from fleet03/B09, including `D=(1/4)E^TPE`, `R>=|D|`, unistochastic `P`, the odd-Weyl overlap gates, plus the current stationarity/Cartan constraints at a maximizing representative.
5. Exclude that residual true-unitary branch. Then every support direction is bounded and the determinant lies in the 24-point convex hull; singular and repeated spectra follow through the already-established reductions.

The first essential missing implication is therefore:

> **`MOC4-RESIDUAL-PR-RESERVE-v1` (OPEN).** On a source-valid strict-support datum with positive reserve `mathcal R` in (23), prove that no genuine common-unitary pair `(P,R)` satisfying the exact fleet03/B09 compatibility and the existing maximizer stationarity/Cartan conditions can realize a positive support gap `gamma<=mathcal R/4`. Equivalently, find a genuine true-unitary/spectrum witness; a formal low-frequency, independent-bistochastic, or independently colored witness does not count.

The exact relaxation witness in Section 5 shows why this implication must genuinely use common-unitary compatibility.

## 7. Status and non-claims

- `MOC4-V4-FIBER-ROOF-v1`: **proved** for every true unitary.
- `MOC4-V4-PAIR-GAP-CEILING-v1`: **proved** for every true-unitary support violation.
- Endpoint certificate (18): **proved** as a sufficient condition for a whole spectra/direction instance.
- Universal endpoint-only closure by (18): **refuted** exactly; this does not refute MOC4.
- The abstract half-integer `S_4` witness is a relaxation witness only, not a unitary determinant orbit.
- `MOC4-RESIDUAL-PR-RESERVE-v1`: **open**.
- Full MOC4: **open**.

No benchmark material, held-out answers, credentials, scheduler identifiers, machine-local paths, unrelated private transcripts, email, Drive, public posting, paid model/API/Codex, remote workflow, or permission bypass was used. No arbitrary bistochastic data is promoted to a true-unitary claim.
