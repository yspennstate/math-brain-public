# MOC4 fleet04/B07 — P-coupled spinor augmentation and two-rook boundary rigidity

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T054300Z-fleet04-B07-MOC4-r12`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Role:** representation-theoretic / exterior-algebra mixed-minor constraint  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and source state used

The target remains: for every pair of complex normal `4 x 4` matrices with spectra
`a_0,...,a_3` and `b_0,...,b_3`,
\[
\det(A+B)\in\operatorname{conv}\left\{
 \prod_{i=0}^3(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\},
\]
including repeated spectra and singular sums.

This run read the current owner controls and then the newest complete campaign-lead result available:
fleet03/B07 run `20260922T043708Z-fleet03-B07-MOC4-r11`,
`MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`, canonical report
`proofnet24/collective-MOC4/fleet03/B07/20260922T043708Z-fleet03-B07-MOC4-r11/REPORT.md`,
report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`.
It gives exact true-unitary subgroup roofs and leaves the strict-interior
same-unitary stationarity residual.

The required named OTHER-account result used directly is the latest complete assigned-partner
fleet01/B08 run `20260922T044241Z-b08-moc4-r12`, canonical report
`proofnet24/collective-MOC4/fleet01/B08/20260922T044241Z-b08-moc4-r12/REPORT.md`,
report blob `f7391a0c2fdeaef6c5fac2bdfbca4513245e5abf`.
It proves `MOC4-V4-BIRKHOFF-GLUE-v1`, the exact common lift on the order-four
complex-Hadamard locus, and the interior certificate
\[
8\min_{ij}P_{ij}+\min_{\alpha\beta}R_{\alpha\beta}\ge2
\Longrightarrow\text{MOC4 holds at that true unitary}.
\]
The present theorem supplies a different nonlinear same-unitary constraint on the complementary
interior and does not assume that the partner's projected V4 gluing is always feasible.

The immediate predecessor used below is fleet04/B07
`20260922T050458Z-fleet04-B07-MOC4-r11`,
`MOC4-SPINOR-TWO-ROOK-v1`, report blob
`0e64ed2b868fbee674c65fc6e3789e8bbbd7867d`.
Its dependency `MOC4-SPINOR-SINGULAR-VALUE-v1` gives the exact singular values in every
even-even Spin(6) gauge.  I also read fleet04/B09
`MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1` and fleet04/B08
`MOC4-CUBATURE-ROOF-RIGIDITY-v1` to keep this boundary result aligned with the current
maximizer-local route.

## 2. Compact conditional end-to-end route

If MOC4 fails, support separation and compactness produce a real support direction and a
true-unitary global maximizer with positive gap above all 24 permutation endpoints.

The current campaign has three complementary restrictions on such a maximizer:

1. the lead's subgroup/V4 roofs confine its scalar support value;
2. the exact Spin(6) stationarity equations and pair-circle Hessian inequalities constrain the
   actual same-unitary point;
3. fleet04/B07's predecessor gives, in every one of sixteen even-even gauges, a sharp
   two-rook convex description of the squared anti-linear block.

The predecessor intentionally discarded the phases and retained only the sharp one-gauge linear
hull.  The first missing representation-theoretic implication is therefore not another linear
mass inequality.  It is to recover the nonlinear same-unitary information which couples the
two-rook block to the *same* unistochastic `P=|U|^2`.

This run proves that coupling exactly.  It also proves that equality at a uniquely exposed
two-rook support roof forces a proper coordinate block decomposition, and is therefore MOC4-safe.
Thus a hypothetical violator is strictly interior to every uniquely exposed two-rook roof, just
as fleet04/B08 proved for uniquely exposed subgroup roofs.

## 3. Spin(6) setup

Use the established real exterior-square model `R^6=C^3`.  In an even-even gauge indexed by
tetrahedral sign rows `i,j in {0,1,2,3}`, write
\[
T_{ij}(z)=M_{ij}z+N_{ij}\bar z.
\]
Put
\[
P=(|u_{ij}|^2),\qquad p=P_{ij},\qquad t^2=1-p,
\]
and let
\[
B_{\alpha\beta}=|(N_{ij})_{\alpha\beta}|^2.
\]

The predecessor singular-value theorem gives
\[
\operatorname{sv}(N_{ij})=(t,t,0).
\tag{1}
\]
For `p<1`, therefore
\[
A:=N_{ij}/t
\]
is a rank-two partial isometry with singular values `(1,1,0)`.

The predecessor also gives the exact channel relation
\[
B_{\alpha\beta}
=\frac12\left(R_{\alpha\beta}
-s_i(\alpha)s_j(\beta)D_{\alpha\beta}\right),
\qquad
D=\frac14 E^TPE,
\tag{2}
\]
where
\[
E=
\begin{pmatrix}
1&1&1\\
1&-1&-1\\
-1&1&-1\\
-1&-1&1
\end{pmatrix},
\tag{3}
\]
and `s_i` is row `i` of `E`.

For each `i` and coordinate `alpha`, define `tau_alpha(i)` to be the unique label different
from `i` having the same sign as `i` in coordinate `alpha`.  For example,
`tau_1(0)=1`, `tau_2(0)=2`, `tau_3(0)=3`.

## 4. New theorem: the normalized anti-linear block has a P-coupled unistochastic augmentation

### Theorem 1 — `MOC4-SPINOR-P-COUPLED-UNISTOCHASTIC-v1`

For every true unitary, every even-even gauge `(i,j)`, and `p=P_ij<1`, define
\[
S_{\alpha\beta}=\frac{B_{\alpha\beta}}{1-p},
\]
\[
a_\alpha=\frac{P_{\tau_\alpha(i),j}}{1-p},
\qquad
b_\beta=\frac{P_{i,\tau_\beta(j)}}{1-p}.
\tag{4}
\]
Then the `4 x 4` doubly stochastic matrix
\[
\boxed{
\mathcal J^{ij}=
\begin{pmatrix}
S&a\\
b^T&0
\end{pmatrix}
}
\tag{5}
\]
is in fact **unistochastic**.  More precisely there are phases such that
\[
\mathcal J^{ij}=|W^{ij}|^{\circ2}
\quad\text{for a genuine }W^{ij}\in U(4).
\tag{6}
\]

This is a necessary same-unitary mixed-minor constraint.  It is not a positive lift to the
24 MOC4 endpoint permutations and does not assert any new positivity representation of
`det(A+B)`.

### Proof

Because `A=N_{ij}/t` has singular values `(1,1,0)`, choose unit vectors `ell,r` spanning,
respectively, `ker A^*` and `ker A`.  Then
\[
AA^*=I-\ell\ell^*,\qquad A^*A=I-rr^*.
\tag{7}
\]
Consequently
\[
W=
\begin{pmatrix}
A&\ell\\
r^*&0
\end{pmatrix}
\tag{8}
\]
is unitary: both `WW^*` and `W^*W` are the identity by (7), `Ar=0`, and
`A^*\ell=0`.

It remains to identify the last column and row moduli with the same `P`.
From (2), using that every row of `R` sums to one,
\[
\sum_\beta B_{\alpha\beta}
=\frac12\left(1-s_i(\alpha)(Ds_j)_\alpha\right).
\tag{9}
\]
The tetrahedral identities `E^TE=4I` and
\[
Es_j^T=4e_j-\mathbf1
\]
give
\[
(Ds_j)_\alpha
=\sum_{k=0}^3 E_{k\alpha}P_{kj}.
\tag{10}
\]
Among the three labels `k != i`, exactly `tau_alpha(i)` has the same sign as `i` in coordinate
`alpha`; the other two have the opposite sign.  Hence
\[
s_i(\alpha)(Ds_j)_\alpha
=2\left(P_{ij}+P_{\tau_\alpha(i),j}\right)-1.
\tag{11}
\]
Substitution into (9) yields
\[
\sum_\beta B_{\alpha\beta}
=1-P_{ij}-P_{\tau_\alpha(i),j}.
\tag{12}
\]
Therefore
\[
|\ell_\alpha|^2
=1-\sum_\beta |A_{\alpha\beta}|^2
=\frac{P_{\tau_\alpha(i),j}}{1-p}=a_\alpha.
\tag{13}
\]
The column calculation is identical:
\[
|r_\beta|^2
=\frac{P_{i,\tau_\beta(j)}}{1-p}=b_\beta.
\tag{14}
\]
Thus the entrywise squared moduli of (8) are exactly (5), proving (6). `QED`

### Phase-free overlap consequences

Orthogonality of two distinct rows of `W` gives, for every `alpha != gamma`,
\[
\boxed{
\sqrt{P_{\tau_\alpha(i),j}P_{\tau_\gamma(i),j}}
\le
\sum_{\beta=1}^3
\sqrt{B_{\alpha\beta}B_{\gamma\beta}}.
}
\tag{15}
\]
Similarly, for every `beta != delta`,
\[
\boxed{
\sqrt{P_{i,\tau_\beta(j)}P_{i,\tau_\delta(j)}}
\le
\sum_{\alpha=1}^3
\sqrt{B_{\alpha\beta}B_{\alpha\delta}}.
}
\tag{16}
\]
These are explicit nonlinear payments from the same spinor `P` into anti-linear mixed-minor
overlap.  In particular, if all entries of the distinguished row or column of `P` are bounded
below, an anti-linear gauge block cannot concentrate arbitrarily close to disjoint two-rook
supports without paying overlap.

More completely, for each row pair (and likewise each column pair), the four numbers
\[
\sqrt{S_{\alpha1}S_{\gamma1}},\
\sqrt{S_{\alpha2}S_{\gamma2}},\
\sqrt{S_{\alpha3}S_{\gamma3}},\
\sqrt{a_\alpha a_\gamma}
\tag{17}
\]
are side lengths of a closed complex quadrilateral.  Hence no one exceeds the sum of the other
three.  This is stronger nonlinear information than the predecessor's sharp linear two-rook hull.

## 5. New target-facing rigidity: an exposed two-rook boundary is MOC4-safe

### Theorem 2 — `MOC4-TWO-ROOK-ROOF-RIGIDITY-v1`

Fix a true unitary and one even-even gauge `(i,j)`.  If `p<1` and
\[
\frac{B^{ij}}{1-p}
\]
is a vertex of the two-rook polytope (a size-two matching of `K_{3,3}`), then the original
`4 x 4` unitary is permutation/phase equivalent to a proper coordinate block unitary.
For `0<p<1` the block type is `2+2`; for `p=0` it degenerates to blocks of sizes at most two.
For `p=1` the distinguished row/column is monomial and the unitary is `1+3` block-safe.

Consequently, for every complex spectra and every support direction, such a unitary already
satisfies the MOC4 hull inclusion.

#### Proof

Suppose first `p<1` and the normalized block is the two-rook vertex with unmatched row
`alpha_0` and unmatched column `beta_0`.  Its row deficits are exactly the unit vector
`e_{alpha_0}` and its column deficits exactly `e_{beta_0}`.  Equations (13)-(14) therefore give
\[
P_{\tau_{\alpha_0}(i),j}=1-p,\quad
P_{\tau_\alpha(i),j}=0\quad(\alpha\ne\alpha_0),
\tag{18}
\]
and
\[
P_{i,\tau_{\beta_0}(j)}=1-p,\quad
P_{i,\tau_\beta(j)}=0\quad(\beta\ne\beta_0).
\tag{19}
\]
Thus the distinguished column `j` and row `i` of the actual unitary each have at most two
nonzero entries.

If `0<p<1`, write
\[
i'=\tau_{\alpha_0}(i),\qquad j'=\tau_{\beta_0}(j).
\]
Then row `i` is supported exactly on `{j,j'}` and column `j` exactly on `{i,i'}`, with both
displayed entries nonzero.  For any row `k` outside `{i,i'}`, orthogonality with row `i`
forces `u_{k j'}=0` because `u_{k j}=0` and `u_{i j'}!=0`.  Hence column `j'` is also supported
on `{i,i'}`.  Dually, orthogonality of column `j` with every column outside `{j,j'}` forces
row `i'` to vanish outside `{j,j'}`.  Therefore the two coordinate planes
`span{e_i,e_i'}` and `span{e_j,e_j'}` form a `2 x 2` unitary block and their complements form
the other `2 x 2` block.

If `p=0`, (18)-(19) make row `i` and column `j` monomial on off-distinguished indices; after
removing these one-dimensional blocks the remainder has size at most two.  If `p=1`, the row
and column containing `(i,j)` are monomial immediately, leaving a `3 x 3` unitary block.

MOC4 is known in dimensions at most three in the campaign source record.  For a proper block
unitary, the determinant factors into block determinants.  Taking the product of the blockwise
convex endpoint representations gives a convex representation by full `S_4` endpoints
respecting those blocks.  No invertibility or spectral-simplicity assumption is used. `QED`

### Corollary — strictness of a uniquely exposed two-rook roof at every violator

In predecessor notation,
\[
Q_{K,X}(O)
=
\left\langle R,\frac X2+C^{ij}\right\rangle
-2\langle B^{ij},C^{ij}\rangle
\tag{20}
\]
and
\[
\langle B^{ij},C^{ij}\rangle
\ge(1-p)\mu_2(C^{ij}),
\quad
\mu_2(C)=\min_{M\in\mathcal M_2}\langle C,M\rangle.
\tag{21}
\]
If the minimizing two-rook matching in (21) is unique, equality forces
`B^{ij}/(1-p)` to be exactly that vertex.  Theorem 2 then makes the unitary block-safe.
Therefore a genuine MOC4 support violator must satisfy the **strict** inequality
\[
\boxed{
\langle B^{ij},C^{ij}\rangle
>(1-p)\mu_2(C^{ij})
}
\tag{22}
\]
for every gauge whose two-rook minimum is uniquely exposed.

This removes the generic equality boundary of all sixteen predecessor roofs.  A surviving
violator can touch such a roof only on an explicit coefficient tie locus.

## 6. Strictness relative to the previous mass constraints

The new augmented-unitary condition is not implied by the two-rook convex hull plus the
predecessor's determinant-hexagon **modulus** inequalities.

Consider
\[
S=
\begin{pmatrix}
7/20&7/15&1/15\\
7/30&0&31/60\\
7/60&1/30&13/60
\end{pmatrix}.
\tag{23}
\]
Its row sums are `(53/60,3/4,11/30)`, its column sums are `(7/10,1/2,4/5)`, and its total
mass is two.  The exact verifier gives an explicit convex combination of the 18 two-rook
vertices with denominator 60, so `S` belongs to the predecessor's sharp linear hull.

The six determinant-matching modulus radicands are
\[
0,\quad
217/36000,\quad
637/27000,\quad
1519/54000,\quad
7/13500,\quad
0.
\tag{24}
\]
The largest side obeys
\[
\sqrt{1519/54000}
\le
\sqrt{637/27000}+\sqrt{7/13500},
\tag{25}
\]
because after the standard exact radical comparison
\[
(217/54000)^2
=
47089/2916000000
<
4459/91125000
=
4(637/27000)(7/13500).
\]
Thus all predecessor determinant-hexagon polygon inequalities are satisfied.

But the augmentation has column deficits `(3/10,1/2,1/5)`.  Orthogonality of augmented columns
2 and 3 would require
\[
\sqrt{1/10}
\le
\sqrt7/15+\sqrt{26}/60,
\tag{26}
\]
where the omitted middle-row overlap is zero.  In fact the inequality is reversed:
\[
6\sqrt{10}>4\sqrt7+\sqrt{26}
\]
since
\[
(4\sqrt7+\sqrt{26})^2
=138+8\sqrt{182}<250<360=(6\sqrt{10})^2.
\tag{27}
\]
So (23) passes the old linear hull and all old modulus hexagon polygon tests but cannot be the
anti-linear squared block of any true Spin(6) gauge with the corresponding deficits.  This
confirms that Theorem 1 contributes genuinely new nonlinear compatibility rather than merely
renaming the predecessor constraints.

The witness is a relaxation witness only; it is **not** a counterexample to MOC4.

## 7. Application to the assigned partner result

On fleet01/B08's exact complex-Hadamard locus, `P=J_4/4`.  Therefore every gauge has
`p=1/4` and all three normalized row/column deficits in (4) equal `1/3`.  Theorem 1 says that
each normalized anti-linear channel is the upper-left corner of a genuine `4 x 4`
unistochastic matrix whose last row and column are uniformly `1/3` off the zero corner.

This is compatible with, but weaker than, the partner's explicit common 24-endpoint lift on
that special locus.  More importantly, it explains why the partner's `P/R` gluing problem on
the general interior cannot be reduced to choosing arbitrary two-rook decompositions
independently in the sixteen gauges: each decomposition must come from an augmented unitary
with its kernel deficits fixed by the *same row and column of P* through (4).

Thus the new theorem supplies exactly the sort of nonlinear same-unitary constraint demanded
by the partner's remaining maximizer-local branch, without replacing it by a stronger
untested global positivity claim.

## 8. Updated first missing implication

The exact generic residual is now:

**`MOC4-P-COUPLED-TWO-ROOK-STATIONARITY-v1` (OPEN).**  
For every structured spectral coefficient pair `(K,X)` and every true-unitary global support
maximizer which is not already block-safe, combine

1. the twelve exact Spin(6) first-order stationarity equations and pair-circle Hessian gates;
2. the lead's subgroup/V4 ceilings;
3. the sixteen two-rook roofs;
4. the sixteen P-coupled unistochastic augmentations (5), equivalently their exact phase
   orthogonality and overlap constraints (15)-(17); and
5. the partner's valid V4/interior gluing certificates,

to force the support gap nonpositive.

Theorem 2 pays the complete equality case whenever any active two-rook coefficient minimum is
unique.  Therefore the unpaid branch is strict-interior in both the lead cubature roofs and the
generic two-rook roofs.  A target-level disproof must still provide actual spectra, support
direction, and a true unitary/global maximizer satisfying all these same-unitary conditions;
an arbitrary `(P,R,D)` or independent collection of gauge decompositions does not qualify.

## 9. Verification and scope

`verify_p_coupled_unitary.py` is a standard-library exact verifier.  It checks:

- the tetrahedral P-coupled deficit identities exactly on all 24 permutation vertices of the
  doubly stochastic `P` polytope (the identities are affine in `P`);
- exact membership of (23) in the two-rook polytope via an explicit denominator-60 convex
  combination;
- exact satisfaction of the determinant-hexagon polygon inequality in (25);
- exact failure of the augmented-unitary bracelet in (26).

No benchmark gold, sealed answers, external compute, paid API/model, email, Drive, workflow
dispatch, or brain-on retrieval is used in this run.
