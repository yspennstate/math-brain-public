# MOC4 fleet03/B07 — transposition-subgroup cubature and a stronger true-unitary residual ceiling

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T043708Z-fleet03-B07-MOC4-r11`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Role:** fleet03/B07, campaign lead  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Source-exact target and recovered state

For complex normal `4 x 4` matrices with spectra `a_0,...,a_3` and `b_0,...,b_3`, after diagonalizing one matrix the target is, for every true `U in U(4)`,

\[
\det(D_a+UD_bU^*)\in \operatorname{conv}\left\{
 z_\sigma:=\prod_{i=0}^3(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\]

Equivalently, for every real support direction `eta`,

\[
h_\eta(U):=\Re\!\left(\eta\det(D_a+UD_bU^*)\right)
\le M_\eta:=\max_{\sigma\in S_4}H_\sigma,\qquad
H_\sigma:=\Re(\eta z_\sigma).
\tag{1}
\]


The newest complete assigned-partner result consumed is **fleet04/B08**, run
`20260922T041159Z-fleet04-B08-moc4-r11`, report blob
`30448cadc8902a3b38f080fd1923392393e997ed`,
`MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1` and
`MOC4-ZERO-RESERVE-ENDPOINT-STAR-RIGIDITY-v1`.
It applies the earlier lead theorem after swapping `(A,B)` and proves that any support violation
`h(U)=M+gamma` obeys

\[
0<\gamma\le \frac{\mathcal R_{\rm bi}}4,\qquad
\mathcal R_{\rm bi}
=3(M-m)-(M-Q)-\frac12\max(G_{\rm out},G_{\rm in}),
\tag{2}
\]

where `m` is the 24-endpoint mean, `Q` is the best Klein-`V_4` fiber average, and `G_out,G_in` are the two six-transposition pair-gap sums. It also gives an exact endpoint-star characterization of the zero-reserve case. This run uses that result as the current residual baseline.

A second exact dependency used in the proof below is the same worker's earlier
`MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`, report blob
`ccc5358d81a9432f3764a9a89be9a01c6bb54e26`.
For every true unitary and every row or column transposition, the average of the two genuine-unitary compound-minor data admits one positive common lift to the 24 permutation endpoints. This is an averaged theorem; no positive lift of an individual unitary is assumed.

## 2. Smallest conditional full deduction before the new step

A source-valid failure of MOC4 has a separating support direction `eta`, and compactness of `U(4)` supplies a true-unitary global maximizer `U_*` with

\[
h_\eta(U_*)=M_\eta+\gamma,\qquad \gamma>0.
\]

The current end-to-end route is:

1. impose the exact true-unitary pair-symmetrized roofs on both row and column relabeling orbits;
2. impose the lead `V_4` roof and the partner's bidirectional ceiling (2);
3. use the exact low-frequency exterior-power structure of the entire `S_4` relabeling orbit, not merely six pair neighbors;
4. if these true-unitary orbit constraints already force `h(U_*)<=M`, the support direction is closed;
5. on the remaining positive residual, use only the same-unitary `P-R-D` compatibility, pair-Rayleigh stationarity and Cartan/Hessian constraints at the actual global maximizer.

Thus the first missing implication is maximizer-local. A universal individual-unitary common-permutation lift is already refuted and is not part of this route.

The present run directly attacks Step 3 by extending the valid two-point lift to whole transposition-containing subgroups and then deriving an exact cubature identity for the `n=4` exterior-power orbit.

## 3. Transposition-subgroup roof

Fix one of the two genuine relabeling actions, row or column. For a true `U`, let

\[
F_U(g)=h_\eta(P_gU)\quad\text{or}\quad F_U(g)=h_\eta(UP_g),
\qquad g\in S_4,
\tag{3}
\]

with the corresponding choice fixed throughout.

### Theorem 1 — `MOC4-TRANSPOSE-SUBGROUP-ROOF-v1`

Let `H<=S_4` contain a transposition. Then the uniform `H`-orbit average of the genuine data in (3) admits a positive common lift to the 24 permutation endpoints. After symmetrizing that lift by `H`, it is `H`-invariant. Consequently,

\[
\boxed{
 \min_C\,\frac1{|H|}\sum_{\sigma\in C}H_\sigma
 \ \le\ 
 \frac1{|H|}\sum_{g\in H}F_U(g)
 \ \le\
 \max_C\,\frac1{|H|}\sum_{\sigma\in C}H_\sigma ,
}
\tag{4}
\]

where `C` ranges over the corresponding left or right `H`-cosets in `S_4`. The opposite physical relabeling action gives the opposite coset orientation.

#### Proof

Choose a transposition `tau in H`. Right multiplication by `tau` partitions `H` into disjoint two-element pairs `{g,g tau}` (or use the left version for the opposite action). For each pair, apply fleet04/B08
`MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`
to the genuine unitary reached at `g`. It gives a positive 24-endpoint lift of that pair average. Averaging these pair lifts gives a positive lift of the full uniform `H`-orbit average.

That averaged genuine data is invariant under the same `H` relabeling action. Push the lift through each element of `H` and average the resulting lifts. Equivariance of the endpoint data leaves a positive lift of the same averaged genuine data, now invariant under `H`. Because determinant support is a linear functional of the exact lifted `P,R,D` data, this symmetrization leaves the support value unchanged.

An `H`-invariant probability law on `S_4` is a convex combination of uniform laws on the corresponding `H`-cosets. Its expectation of `H_sigma` therefore lies between the minimum and maximum coset averages, proving (4). No arbitrary bistochastic array or individual-unitary positive lift is introduced. ∎

For `H=S_4` there is only one coset, so (4) also gives the exact identity

\[
\frac1{24}\sum_{g\in S_4}F_U(g)
=\frac1{24}\sum_{\sigma\in S_4}H_\sigma=:m.
\tag{5}
\]

## 4. Exact `n=4` cubature identity

The principal-minor/Cauchy--Binet expansion is

\[
\det(D_a+UD_bU^*)
=
\sum_{k=0}^4
\ \sum_{\substack{|I|=|J|=k}}
 a_{I^c} b_J\,|\det U[I,J]|^2.
\tag{6}
\]

Under either row or column permutation of `U`, the `k=0,4` terms are constant; the `k=1,3` terms lie in the singleton assignment permutation module; and the `k=2` terms lie in the unordered two-subset assignment module. Hence every real support orbit `F_U:S_4->R` belongs to the linear span

\[
\mathcal L
=\operatorname{span}\left(
1,\ 
{\bf 1}_{g(i)=j},\
{\bf 1}_{g(I)=J}\ (|I|=|J|=2)
\right).
\tag{7}
\]

Use zero-based labels and define the seven transposition-containing subgroups

\[
\begin{array}{lll}
H_1=\langle(03),(12)\rangle, & |H_1|=4,\\
H_2=\langle(01),(0213)\rangle, & |H_2|=8,\\
H_3=\langle(12),(13)\rangle, & |H_3|=6,\\
H_4=\langle(01),(23)\rangle, & |H_4|=4,\\
H_5=\langle(02)\rangle, & |H_5|=2,\\
H_6=\langle(03),(0132)\rangle, & |H_6|=8,\\
H_7=\langle(01),(03)\rangle, & |H_7|=6 .
\end{array}
\tag{8}
\]

For `A_H f=|H|^{-1}\sum_{h\in H}f(h)`, the following identity is exact on all of `mathcal L`:

\[
\boxed{
f(e)=
\frac13A_{H_1}f+\frac13A_{H_2}f+\frac12A_{H_3}f
+\frac13A_{H_4}f+\frac23A_{H_5}f
+\frac13A_{H_6}f+\frac12A_{H_7}f
-2A_{S_4}f .
}
\tag{9}
\]

### Exact finite certificate

The companion standard-library verifier checks (9) with `Fraction` arithmetic on a spanning generating family:
one constant function, all `16` singleton-assignment indicators, and all `36` two-subset-assignment indicators, `53` generators total. Since both sides of (9) are linear, that finite exact check proves (9) on `mathcal L`, hence for every orbit function (3) coming from (6).

Combining (4), (5) and (9) gives a new support bound valid for **every true unitary**, with no stationarity hypothesis:

\[
\boxed{
h_\eta(U)\le
\Lambda_\pm(H):=
\frac13\rho_1+\frac13\rho_2+\frac12\rho_3
+\frac13\rho_4+\frac23\rho_5
+\frac13\rho_6+\frac12\rho_7
-2m ,
}
\tag{10}
\]

where `rho_j` is the maximum `H_j`-coset endpoint average in the coset orientation corresponding to the chosen physical relabeling side. Both physical sides are available, so one may take the smaller of the two valid bounds obtained from the two orientations.

This is `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`.

## 5. Exact application to the partner's hard positive-reserve datum

Use the exact simple complex spectra retained by fleet04/B08,

\[
a=(-4+4i,-i,-3+2i,-4-4i),\qquad
b=(-4-4i,2-i,2-4i,4-i),\qquad \eta=1.
\tag{11}
\]

The endpoint data are

\[
M=256,\qquad m=-\frac{217}{2}.
\tag{12}
\]

For the stronger coset orientation in (10), the seven exact roofs are

\[
\left(
-\frac{47}{2},\ -\frac72,\ 32,\ 58,\ 231,\ -68,\ -\frac{134}{3}
\right).
\tag{13}
\]

Substitution into (10) yields

\[
\boxed{\Lambda=\frac{1057}{3}},
\qquad
\boxed{h_\eta(U)-M\le\frac{289}{3}}
\quad\text{for every true }U.
\tag{14}
\]

The assigned partner's newest bidirectional `V_4`/pair ceiling on exactly this endpoint datum was

\[
\gamma\le\frac{529}{4}.
\tag{15}
\]

The present genuine-unitary subgroup bound therefore strictly improves that residual to

\[
\boxed{\gamma\le\frac{289}{3}},
\tag{16}
\]

an exact reduction by

\[
\frac{529}{4}-\frac{289}{3}=\frac{431}{12}.
\tag{17}
\]

This does not close the hard datum, but it removes a substantial part of the partner's positive-reserve branch without using stationarity.

### Previous lead negative control

For the earlier lead datum

\[
a=(-1,2,1,0),\qquad b=(-1,1,-2,2),\qquad\eta=1,
\tag{18}
\]

the opposite coset orientation has roofs

\[
\left(
\frac{119}{4},\ 9,\ \frac{44}{3},\ 12,\ 18,\ \frac{59}{4},\ 9
\right)
\]

and (10) gives exactly

\[
\boxed{\Lambda=36=M}.
\tag{19}
\]

Thus the new subgroup-cubature mechanism independently closes the exact real direction that the assigned partner had already closed by the bidirectional pair-gap theorem. The two mechanisms agree on the conclusion but use different exact information.

## 6. Updated smallest conditional full deduction

For arbitrary spectra and support direction, compute:

1. the two subgroup-cubature bounds `Lambda_left,Lambda_right` from (10);
2. the assigned partner's bidirectional `V_4`/pair bound;
3. the endpoint maximum `M`.

Every source-valid counterexample must therefore satisfy

\[
0<\gamma
\le
\Gamma(a,b,\eta):=
\min\left\{
\Lambda_{\rm left}-M,\ 
\Lambda_{\rm right}-M,\ 
\frac{\mathcal R_{\rm bi}}4
\right\},
\tag{20}
\]

on a datum where the right side is positive. If any of the three entries is nonpositive, that entire support direction is closed for every true unitary.

Hence one remaining implication suffices for full MOC4:

> **`MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1` (OPEN).**  
> For every structured spectral support datum with `Gamma(a,b,eta)>0`, no genuine common-unitary global support maximizer satisfying the exact `P-R-D` compatibility, all pair-Rayleigh stationarity conditions and the current Cartan/Hessian constraints can realize a positive support gap `0<gamma<=Gamma(a,b,eta)`.

A proof of this implication for every structured datum closes every support direction and therefore the full `4 x 4` convex-hull statement. The algebraic subgroup theorem itself does not exclude singular sums or repeated spectra: (6), the genuine-unitary relabeling orbit, and the positive pair-symmetrized lift remain meaningful there. Where a later maximizer argument invokes a generic reduction, the existing source-valid continuity treatment returns those boundary cases.

The present run directly attacked this missing implication by deriving additional exact constraints that every putative maximizer must satisfy and by shrinking its canonical hard residual from `529/4` to `289/3`. The remaining work must now use nonlinear same-unitary/maximizer structure; another unconstrained low-frequency or transport-only relaxation is not enough.

## 7. Verification, failure controls and non-claims

`verify_transpose_subgroup_cubature.py` uses only the Python standard library (`itertools`, `fractions`). It verifies:

1. the seven exact subgroups and that each contains a transposition;
2. the cubature identity (9) on all 53 spanning generators;
3. all exact endpoint values and the seven roofs in (13);
4. the hard bound `1057/3` and residual `289/3`;
5. the exact closure `Lambda=M=36` of the preceding real datum.

Observed terminal output:

```text
PASS MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1
basis_generators = 53
subgroup_sizes = [4, 8, 6, 4, 2, 8, 6]
hard_left_coset_roofs = ['-47/2', '-7/2', '32', '58', '231', '-68', '-134/3']
hard_endpoint_M = 256
hard_endpoint_mean = -217/2
hard_support_upper_bound = 1057/3
hard_gap_upper_bound = 289/3
real_right_coset_roofs = ['119/4', '9', '44/3', '12', '18', '59/4', '9']
real_support_upper_bound = 36
```

A discarded exploratory LP temporarily mixed row-orbit and column-orbit constraints as if they were one group-orbit function. That is invalid because they are two different genuine-unitary orbit functions. The error was caught before promotion. The theorem and verifier above use one physical relabeling side at a time and only combine the two resulting scalar upper bounds by taking their minimum.

Full MOC4 remains **OPEN**. No arbitrary bistochastic surrogate, individual-unitary common lift, benchmark material, held-out answer, credential, scheduler identifier, machine path, unrelated private transcript, email/Drive material, paid model/API/Codex call, remote workflow, permission bypass, or public release was used.
