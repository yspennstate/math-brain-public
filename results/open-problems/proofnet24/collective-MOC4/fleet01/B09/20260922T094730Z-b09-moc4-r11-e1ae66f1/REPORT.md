# fleet01/B09 MOC4 — double-half exterior-energy equality is target-safe

Run: `20260922T094730Z-b09-moc4-r11-e1ae66f1`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Candidate: **`MOC4-DOUBLE-HALF-ENERGY-SAFETY-v1`**  
Parent MOC4 target: **OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-bound inputs actually consumed

The target is the complex-normal `4 x 4` Marcus--de Oliveira inclusion

\[
\det(D_a+UD_bU^*)\in
\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every `a,b in C^4` and every true unitary `U`, including singular sums and repeated spectra.

The latest complete campaign-lead result actually consumed is fleet03/B07 run
`20260922T074824Z-fleet03-B07-MOC4-r13`, report blob
`7724d19f793eb934c5fcc2b469bb9d0a108da4eb`, candidates

- `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1`,
- `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.

On the mixed-Schur branch (`MSQR`) a pair-kernel vector at a true global support maximizer is a full-Hessian kernel vector, and the exact fourth-order gate is

\[
q+3R_{\rm pair}+3R_{\rm cross}\le0,
\qquad R_{\rm cross}\ge0. \tag{1}
\]

The assigned partner's newest complete result was also consumed after it appeared: fleet02/B07 run
`20260922T093424Z-b07-c8697991`, report blob
`52c8681b4b72cbdb5655c9668ed36d87376ceec9`, candidate
`MOC4-MSQR-BILATERAL-EQUALITY-CIRCLE-v1`.
At exact simple pair-LS saturation it gives bilateral equality circles, six exact finite coefficient identities, and the full-`Z` axis-transport / repeated-singular-value dichotomy. Combined with (1), a positive-gap exact-saturation survivor must also satisfy full-Hessian cross annihilation and `R_cross=0`.

The decisive OTHER-account input for the new theorem is fleet04/B08 run
`20260922T091158Z-fleet04-B08-MOC4-r12`, report blob
`a51e9a09e68c9d2c5f04f6a73f4a919f95ebb1df`, candidate
`MOC4-EXTERIOR-BLOCKROW-HALF-ENERGY-v1`.
For the real exterior matrix `O=Lambda^2 U in SO(6)`, partitioned into `3 x 3` real `2 x 2` blocks `B_{alpha beta}`, define

\[
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2,
\qquad D_{\alpha\beta}=\det B_{\alpha\beta},
\]
\[
E_\alpha=\sum_{\beta=1}^3
\left(R_{\alpha\beta}^2-D_{\alpha\beta}^2\right).
\tag{2}
\]

B08 proves sharply

\[
0\le E_\alpha\le\frac12, \tag{3}
\]

and equality holds iff exactly two blocks in that row are rank-one unit partial isometries with complementary row-side range projections, while the third block is zero.

I also use the exact fleet01/B07 mixed-minor identity

\[
D_{\alpha\beta}=\frac14h_\alpha^T P h_\beta,
\qquad P=|U|^2, \tag{4}
\]

where the three `h_alpha` form a basis of `1^perp` in `R^4`, together with the already-established safety of true common reducing blocks. Finally I apply my earlier exact source-valid theorem
`MOC4-HADAMARD-FIBER-LIFT-v1`, run `20260922T044740Z-b09-moc4-r11`, report blob
`9b496cd2cb18df7a577ab0997de1117a8c144c98`, which supplies an explicit positive `S_4` lift for the canonical `4 x 4` complex-Hadamard family.

No arbitrary bistochastic or independent compound-minor surrogate is used below.

## 2. Compact conditional end-to-end argument

Assume a strict MOC4 support counterexample and take the genuine positive-gap global maximizer supplied by the campaign genericization. On an `MSQR` edge `{alpha,gamma}`, fleet01/B07 covariance reconstruction and fleet04/B08 give

\[
4Qh_e\le E_\alpha+E_\gamma\le1,
\qquad
Q=4(\gamma+r_\tau)(\gamma+r_{\tau^c}). \tag{5}
\]

The previously open issue was the equality stratum `E_alpha+E_gamma=1`. The theorem below proves that **every true unitary on this stratum is already MOC4-safe for all spectra**. Hence any genuine positive-gap counterexample must satisfy the strict inequality

\[
E_\alpha+E_\gamma<1, \tag{6}
\]

and therefore

\[
\boxed{16h_e(\gamma+r_\tau)(\gamma+r_{\tau^c})<1.} \tag{7}
\]

Thus the sharp conditioning ceiling is not merely non-strict: its complete equality locus is removed from the counterexample search.

When the partner's pair-LS equality also occurs, its bilateral identities / axis transport and the lead's `R_cross=0` must now coexist with the **strict** exterior-conditioning inequality (7). This removes one boundary component from `MOC4-MSQR-AXIS-CROSSSPLIT-RIGIDITY-v1`.

## 3. Main theorem

### `MOC4-DOUBLE-HALF-ENERGY-SAFETY-v1`

Let `U in U(4)` be a true unitary and let `O=Lambda^2U in SO(6)` be its standard real exterior representative, decomposed into the three complementary-pair row planes and three complementary-pair column planes. If two distinct block rows satisfy

\[
E_\alpha=E_\gamma=\frac12, \tag{8}
\]

then the MOC4 inclusion holds at `U` for **every** complex spectra `a,b`.

More precisely, exactly one of the following two geometric alternatives occurs.

1. **Common missing block column.** The two saturated rows have their zero `2 x 2` block in the same block column. Then `U` has a proper `2+2` common reducing block after row/column permutations and phases; hence MOC4 is target-safe.

2. **Distinct missing block columns.** The two zero columns are different. Then all three block rows and all three block columns saturate (3); the zero blocks form a block-level permutation matrix and every other block is rank one with singular value one. Consequently `D_{alpha beta}=0` for all nine blocks, hence (4) forces

\[
P=|U|^2=\frac14J. \tag{9}
\]

Thus `U` is a `4 x 4` complex Hadamard matrix. Every such `U` is monomially equivalent to the canonical one-parameter family from `MOC4-HADAMARD-FIBER-LIFT-v1`, so the explicit positive lift from that theorem proves MOC4.

The same statement holds with rows and columns interchanged.

## 4. Proof: the two-row equality combinatorics

Assume (8). By B08's equality characterization, each saturated row contains exactly one zero block and two rank-one singular-value-one blocks.

For a rank-one singular-value-one block write

\[
B=xv^T,
\qquad \|x\|=\|v\|=1. \tag{10}
\]

Then

\[
BB^T=xx^T,
\qquad B^TB=vv^T. \tag{11}
\]

Let `z_alpha,z_gamma` denote the missing block columns of rows `alpha,gamma`.

### Case A: `z_alpha=z_gamma=z`

Let `delta` be the third block row. Column orthogonality of `O` gives

\[
\sum_rB_{rz}^TB_{rz}=I_2. \tag{12}
\]

The first two terms vanish, so

\[
B_{\delta z}^TB_{\delta z}=I_2. \tag{13}
\]

Thus `B_{delta z}` is orthogonal. Row orthogonality for row `delta` then gives

\[
\sum_jB_{\delta j}B_{\delta j}^T=I_2. \tag{14}
\]

The `j=z` term already equals `I_2`, so every other term is zero. Hence

\[
B_{\delta j}=0\quad(j\ne z). \tag{15}
\]

Therefore `O` maps the complementary-pair real plane indexed by `z` exactly onto the complementary-pair plane indexed by `delta`, and maps its orthogonal four-dimensional complement onto the corresponding complement.

Normalize the irrelevant global phase of `U` so `U in SU(4)` and complexify this statement. The complementary-pair real plane associated with a split `J|J^c` complexifies to

\[
W_J=\operatorname{span}_C\{e_J,e_{J^c}\}\subset\Lambda^2C^4. \tag{16}
\]

Inside `W_J`, a vector `xe_J+ye_{J^c}` is decomposable iff

\[
(xe_J+ye_{J^c})\wedge(xe_J+ye_{J^c})
=2xy\,e_{1234}=0, \tag{17}
\]

i.e. iff `xy=0`. Thus the only decomposable projective lines in `W_J` are `Ce_J` and `Ce_{J^c}`.

Because `Lambda^2U` preserves decomposability and bijectively maps one such `W_J` onto another, it permutes those two decomposable lines. Therefore `U` maps the coordinate two-plane `E_J` onto one coordinate two-plane and `E_{J^c}` onto its complement. After row/column permutations,

\[
U=\begin{pmatrix}V&0\\0&W\end{pmatrix},
\qquad V,W\in U(2). \tag{18}
\]

For a `2 x 2` true unitary `V`, Cauchy--Binet gives for arbitrary complex two-vectors `x,y`

\[
\det(D_x+VD_yV^*)
=t(x_1+y_1)(x_2+y_2)
+(1-t)(x_1+y_2)(x_2+y_1) \tag{19}
\]

for one `t in [0,1]` (up to swapping the two labels). Applying (19) to both diagonal blocks in (18) and multiplying the two convex combinations produces a convex combination of four of the 24 MOC4 permutation products. Hence Case A is target-safe for all complex spectra, including singular and repeated data.

## 5. Proof: distinct missing columns force a six-cycle exterior boundary

Now assume `z_alpha!=z_gamma`. Relabel block columns so

\[
z_\alpha=1,\qquad z_\gamma=2. \tag{20}
\]

The only block column in which the two saturated rows are simultaneously nonzero is column `3`. Write

\[
B_{\alpha3}=xv^T,
\qquad B_{\gamma3}=yw^T, \tag{21}
\]

with all four vectors unit. Cross-row orthogonality gives

\[
0=\sum_jB_{\alpha j}B_{\gamma j}^T
=B_{\alpha3}B_{\gamma3}^T
=(v^Tw)xy^T. \tag{22}
\]

Therefore

\[
v\perp w. \tag{23}
\]

Column-3 orthogonality now yields

\[
I_2
=\sum_rB_{r3}^TB_{r3}
=vv^T+ww^T+B_{\delta3}^TB_{\delta3}, \tag{24}
\]

and (23) makes the first two terms equal `I_2`; hence

\[
B_{\delta3}=0. \tag{25}
\]

In column `1`, row `alpha` is zero and row `gamma` contributes a rank-one projection. Thus

\[
B_{\delta1}^TB_{\delta1}=I_2-\text{(rank-one projection)}, \tag{26}
\]

so `B_{delta1}` is itself rank one with singular value one. The same argument in column `2` gives the same conclusion for `B_{delta2}`. Therefore row `delta` also saturates (3), with missing column `3`.

The symmetric column statement follows immediately: every block column contains exactly one zero block and two rank-one singular-value-one blocks. The three zeros form a block-level permutation matrix. The six active block positions form

\[
K_{3,3}\setminus\text{(perfect matching)}, \tag{27}
\]

i.e. one six-cycle.

This already gives a useful exact normal form: by choosing orthonormal bases independently in the three row planes and three column planes, every active rank-one block becomes a single signed matrix unit and `O` becomes a signed scalar `6 x 6` permutation supported on that block-level six-cycle. No claim about the lift is needed for the target argument below.

## 6. Six-cycle exterior boundary implies flat one-point data

Every block in Case B has rank at most one. Hence

\[
D_{\alpha\beta}=\det B_{\alpha\beta}=0
\qquad\text{for all }\alpha,\beta. \tag{28}
\]

Apply the exact same-unitary identity (4):

\[
h_\alpha^TPh_\beta=0
\qquad\text{for all }\alpha,\beta. \tag{29}
\]

The three vectors `h_alpha` span `1^perp`. Since `P=|U|^2` is doubly stochastic,

\[
P\mathbf1=\mathbf1,
\qquad P^T\mathbf1=\mathbf1, \tag{30}
\]

so `P` preserves `1^perp`. Equation (29) says the restriction of `P` to `1^perp` is zero. Therefore

\[
\boxed{P=\frac14J.} \tag{31}
\]

Thus every entry of `U` has modulus `1/2`: `2U` is a complex Hadamard matrix.

This implication is source-valid: it uses the determinant blocks of the actual `Lambda^2U` and the exact actual-unitary identity (4), not an independently chosen `R,D,P` tuple.

## 7. Self-contained `4 x 4` complex-Hadamard normalization

For completeness, here is the elementary classification needed to invoke the previous B09 lift.

Multiplying rows and columns by phases and permuting them does not change MOC4 safety: diagonal phases commute with the diagonal spectral matrices, and permutations only relabel `a,b` while the target ranges over all `S_4`.

Dephase `2U` so its first row and first column are all `1`. A basic lemma is:

> If four unit complex numbers have sum zero, they split into two antipodal pairs.

Indeed, if their roots are `z_1,...,z_4`, then `e_1=0`; taking conjugates and using `|z_j|=1` gives `e_3=(z_1z_2z_3z_4)\sum_jz_j^{-1}=0`. Hence their monic polynomial is `t^4+e_2t^2+e_4`, invariant under `t->-t`, so the multiset of roots is antipodally paired.

Apply the lemma to the second row and permute the last three columns:

\[
r_2=(1,-1,z,-z),\qquad |z|=1. \tag{32}
\]

For a remaining dephased row `r=(1,a,b,c)`, the same lemma says one of `a,b,c` is `-1` and the other two are `w,-w`.

- If `a=-1`, orthogonality to (32) forces `w=-z`, so `r=(1,-1,-z,z)`.
- If `b=-1`, orthogonality gives `(1-\bar z)(1-w)=0`; unless `z=1`, this forces `w=1` and `r=(1,1,-1,-1)`.
- If `c=-1`, orthogonality gives `(1+\bar z)(1-w)=0`; unless `z=-1`, again `w=1` after the evident last-column relabeling.
- In the exceptional cases `z=1` or `z=-1`, one column permutation turns the free remaining phase into the new parameter and again yields the same normal form.

The fourth row is then forced by orthogonality. Thus every `4 x 4` complex Hadamard is monomially equivalent to

\[
U(z)=\frac12
\begin{pmatrix}
1&1&1&1\\
1&-1&z&-z\\
1&1&-1&-1\\
1&-1&-z&z
\end{pmatrix},
\qquad |z|=1, \tag{33}
\]

which is row/column equivalent to the canonical family used in `MOC4-HADAMARD-FIBER-LIFT-v1`.

That theorem supplies, with `c=Re z`, an explicit probability law `mu_c` on `S_4` matching every singleton and two-subset compound-minor marginal, and therefore

\[
\det(D_a+U(z)D_bU(z)^*)
=\sum_{\sigma\in S_4}\mu_c(\sigma)
\prod_i(a_i+b_{\sigma(i)}), \tag{34}
\]

with `mu_c>=0` and total mass one. This proves target safety in Case B.

Together with Case A, the theorem is proved. `QED`

## 8. Strict conditioning corollary

B08's universal half-energy bound gives for every distinct pair

\[
E_\alpha+E_\gamma\le1. \tag{35}
\]

If equality holds, both individual energies equal `1/2`, so the theorem proves the true unitary target-safe. Therefore **at any genuine positive-gap MOC4 counterexample**,

\[
\boxed{E_\alpha+E_\gamma<1\quad\text{for every distinct }\alpha,\gamma.} \tag{36}
\]

On a mixed-Schur edge, combine (36) with the exact covariance-reconstruction lower bound

\[
E_\alpha+E_\gamma\ge4Qh_e \tag{37}
\]

and the partner roof identity

\[
Q=4(\gamma+r_\tau)(\gamma+r_{\tau^c}). \tag{38}
\]

Then every genuine positive-gap `MSQR` survivor satisfies the **strict** ceiling

\[
\boxed{
16h_e(\gamma+r_\tau)(\gamma+r_{\tau^c})<1.
} \tag{39}
\]

In particular, no counterexample can live on the equality boundary of fleet04/B08's sharp conditioning ceiling.

There need not be a uniform numerical margin in (39): a sequence of irreducible unitaries could in principle approach one of the now-classified safe boundary strata. The result is an exact exclusion of equality, not an unproved compactness gap.

## 9. Application to the newest partner / lead residual

The newest fleet02/B07 theorem says exact simple pair-LS saturation creates bilateral equality circles and forces either

- generic full-`Z` singular-axis transport, or
- multiplicity at least two of the mixed singular value in the full `3 x 3` coupling.

The lead simultaneously forces full-Hessian kernel annihilation and `R_cross=0` at an actual global maximum.

The present theorem removes one additional boundary possibility from that system: such a positive-gap survivor **cannot** also saturate the exterior covariance ceiling. Therefore the exact-saturation residual now obeys all of

1. the partner's bilateral identities and axis-transport / degeneracy dichotomy;
2. the lead's full-Hessian cross annihilation and `R_cross=0`;
3. the strict same-unitary conditioning inequality (39).

The first essential unpaid implication remains the genuine determinant-specific cross-split rigidity problem, but it is now strictly interior with respect to the exterior half-energy ceiling. Equivalently, any attempt to build a source-valid counterexample by forcing covariance reconstruction all the way to the two-row half-energy boundary is impossible: the common-zero branch is a `2+2` common-block safe point, and the distinct-zero branch is a complex-Hadamard safe point with an explicit positive permutation lift.

The separate all-pair-negative-definite (`NDI`) branch remains open.

## 10. Verdict

**ESSENTIAL_STEP_APPLIED.**  
`MOC4-DOUBLE-HALF-ENERGY-SAFETY-v1` classifies the complete equality locus of the two-row exterior half-energy bound into two source-valid MOC4-safe strata and upgrades the mixed-Schur spectral-conditioning ceiling from non-strict to strict at every genuine positive-gap counterexample.

Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.
