# MOC4 fleet04/B07 — spinor Hessian moments and generic triple-flat closure

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T061043Z-fleet04-B07-moc4-r13`  
**Target:** Marcus–de Oliveira for complex normal `4 x 4` pairs  
**Role:** representation-theoretic / exterior-algebra mixed-minor constraint  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact current state consumed

The source-exact target is
\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]
for every pair of complex normal `4 x 4` matrices, with eigenvalues counted with
multiplicity. Singular matrices and repeated spectra are part of the target.

The latest complete team-lead result consumed is fleet03/B07,
run `20260922T055130Z-fleet03-B07-MOC4-r11`,
`MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`,
canonical report
`proofnet24/collective-MOC4/fleet03/B07/20260922T055130Z-fleet03-B07-MOC4-r11/REPORT.md`,
report blob `055492abce4a340ed49b4dbc44787461454c2b71`.
For the genuine exterior-square point
\[
O=\Lambda^2U\in SO(6)
\]
written as a `3 x 3` array of real `2 x 2` blocks `B_{\alpha\beta}`, it proves the
full pair Hessian bound
\[
\|M_{\alpha\gamma}\|_{\rm op}^2
 \le 4(T_{\alpha\gamma}^2-C_{\alpha\gamma}^2),
\tag{1}
\]
and, when `T=|C|`, separate vanishing of the two weighted traceless Gram sums.

The newest complete assigned-partner result consumed is fleet01/B08,
run `20260922T060423Z-fleet01-B08-MOC4-r11`,
`MOC4-PR-JOINT-LIFT-FACET-v1`,
canonical report
`proofnet24/collective-MOC4/fleet01/B08/20260922T060423Z-fleet01-B08-MOC4-r11/REPORT.md`,
report blob `5a93eb14d686499625085947cf3fcc4612597863`.
It gives an exact dense rational true-unitary point for which the necessary
joint `(P,R)` common-lift facet
\[
T(R)\le 3S(P)
\]
fails strictly. Thus the unconditional positive common-compound lift is
rigorously unavailable even in the dense interior. I apply that no-go here by
not introducing any common positive permutation law: all new statements below
are identities or consequences on the same genuine `O=\Lambda^2U`.

The preceding fleet04/B07 spinor work used below is
`MOC4-SPINOR-P-COUPLED-UNISTOCHASTIC-v1` and
`MOC4-TWO-ROOK-ROOF-RIGIDITY-v1`,
report
`proofnet24/collective-MOC4/fleet04/B07/20260922T054300Z-fleet04-B07-MOC4-r12/REPORT.md`.
In every even-even coordinate-conjugation gauge `(i,j)`, if
\[
T(z)=Mz+N\bar z,
\]
then
\[
\operatorname{sv}(N)=
(\sqrt{1-P_{ij}},\sqrt{1-P_{ij}},0).
\tag{2}
\]
This exact same-unitary singular-value identity is the final step in the new
rigidity theorem below.

## 2. Compact conditional end-to-end route

If MOC4 fails, support separation and compactness give a real support direction
and a genuine global support maximizer with positive gap over all 24 permutation
endpoints. The lead's theorem forces the full first- and second-order
`Spin(6)` conditions at that maximizer. The newest partner result rules out
closing the proof by an unconditional positive common-minor law.

The first representation-theoretic gap is therefore:

> convert the lead's traceless-Gram Hessian constraint into the natural
> complex spinor variables `(m,n)`, then determine what exact pair-flatness
> forces on one genuine exterior-square point.

This run does that. It proves that generic simultaneous flatness of the three
row-pair Hessian gates is not a surviving interior branch: it forces a
coordinate `1+3` block and is already MOC4-safe. It also gives a quantitative
collar measuring distance from that pure-orientation locus.

## 3. Complex block coordinates and an exact Gram identity

Represent each real block as the real-linear complex map
\[
B_{\alpha\beta}:\quad z\longmapsto
m_{\alpha\beta}z+n_{\alpha\beta}\bar z.
\tag{3}
\]
Then
\[
R_{\alpha\beta}=|m_{\alpha\beta}|^2+|n_{\alpha\beta}|^2,
\qquad
D_{\alpha\beta}=|m_{\alpha\beta}|^2-|n_{\alpha\beta}|^2.
\tag{4}
\]

For a real symmetric matrix
\[
S=\begin{pmatrix}s_{11}&s_{12}\\s_{12}&s_{22}\end{pmatrix},
\]
put
\[
\chi(S)=\frac{s_{11}-s_{22}}2+i\,s_{12}.
\tag{5}
\]
If `B` is the real matrix of `z -> mz+n zbar`, direct expansion gives
\[
\boxed{\chi(BB^T)=2mn.}
\tag{6}
\]
Consequently the anisotropy norm used by the lead is
\[
\rho(S)=|\chi(S)|.
\tag{7}
\]

There is also a universal row identity. Writing the full real orthogonal map
as
\[
T(z)=Mz+N\bar z,
\]
orthogonality gives
\[
MM^*+NN^*=I,\qquad MN^T+NM^T=0.
\tag{8}
\]
The diagonal of the second identity is
\[
\boxed{\sum_{\beta=1}^3m_{\alpha\beta}n_{\alpha\beta}=0
\quad(\alpha=1,2,3).}
\tag{9}
\]

## 4. The lead's Hessian gate in spinor-moment form

Fix a row pair `alpha<gamma` and write
\[
\delta X_\beta=X_{\alpha\beta}-X_{\gamma\beta},
\qquad
z_{\alpha\beta}=m_{\alpha\beta}n_{\alpha\beta}.
\tag{10}
\]
The lead defines
\[
\mathsf A=\sum_\beta\delta X_\beta
 B_{\alpha\beta}B_{\alpha\beta}^T,\qquad
\mathsf G=\sum_\beta\delta X_\beta
 B_{\gamma\beta}B_{\gamma\beta}^T.
\]
By (6),
\[
\rho(\mathsf A)=
2\left|\sum_\beta\delta X_\beta z_{\alpha\beta}\right|,
\quad
\rho(\mathsf G)=
2\left|\sum_\beta\delta X_\beta z_{\gamma\beta}\right|.
\tag{11}
\]
Thus (1) is exactly:

### Theorem 1 — `MOC4-SPINOR-HESSIAN-MOMENT-v1`

At every local support maximizer,
\[
\boxed{
\left(
\left|\sum_\beta\delta X_\beta z_{\alpha\beta}\right|
+
\left|\sum_\beta\delta X_\beta z_{\gamma\beta}\right|
\right)^2
\le T_{\alpha\gamma}^2-C_{\alpha\gamma}^2.
}
\tag{12}
\]

In particular, if the pair is flat,
\[
T_{\alpha\gamma}=|C_{\alpha\gamma}|,
\]
then
\[
\boxed{
\sum_\beta
(X_{\alpha\beta}-X_{\gamma\beta})
m_{\alpha\beta}n_{\alpha\beta}=0,
}
\tag{13a}
\]
\[
\boxed{
\sum_\beta
(X_{\alpha\beta}-X_{\gamma\beta})
m_{\gamma\beta}n_{\gamma\beta}=0.
}
\tag{13b}
\]

This is the lead's flat traceless-Gram cancellation expressed directly in the
two spinor channels of the same mixed minors.

### Quantitative collar

For fixed `alpha`, let `gamma,delta` be the other two row indices and set
\[
L_\alpha=
\begin{pmatrix}
1&1&1\\
X_{\alpha1}-X_{\gamma1}&
X_{\alpha2}-X_{\gamma2}&
X_{\alpha3}-X_{\gamma3}\\
X_{\alpha1}-X_{\delta1}&
X_{\alpha2}-X_{\delta2}&
X_{\alpha3}-X_{\delta3}
\end{pmatrix}.
\tag{14}
\]
Put
\[
r_{\alpha\gamma}=T_{\alpha\gamma}^2-C_{\alpha\gamma}^2\ge0.
\]
If `L_alpha` is invertible, (9) and (12) give
\[
\boxed{
\|z_\alpha\|_2
\le
\|L_\alpha^{-1}\|_2
\sqrt{r_{\alpha\gamma}+r_{\alpha\delta}}.
}
\tag{15}
\]
The blockwise orientation impurity
\[
\varepsilon_\alpha=
\sum_\beta
\min\{|m_{\alpha\beta}|^2,|n_{\alpha\beta}|^2\}
\]
therefore satisfies
\[
\boxed{
\varepsilon_\alpha
\le
\sqrt3\,\|L_\alpha^{-1}\|_2
\sqrt{r_{\alpha\gamma}+r_{\alpha\delta}}.
}
\tag{16}
\]
Indeed `min(x^2,y^2)<=xy` for nonnegative `x,y`, so
`\varepsilon_alpha<=sum |z_{alpha beta}|<=sqrt(3)||z_alpha||_2`.

This is a genuine same-unitary distance-to-pure-orientation estimate. It uses
no convex lift.

## 5. Pure block orientations force a `1+3` unitary

The exact zero-reserve endpoint of (16) can be classified.

### Theorem 2 — `MOC4-PURE-BLOCK-SPINOR-RIGIDITY-v1`

Let `O in SO(6)` be in the exterior-square image and write its nine blocks as
in (3). If
\[
\boxed{m_{\alpha\beta}n_{\alpha\beta}=0
\quad\text{for every }\alpha,\beta,}
\tag{17}
\]
then, after an even number of output-coordinate conjugations and an even
number of input-coordinate conjugations, the map is complex-linear:
\[
N=0.
\tag{18}
\]
Consequently, by the exact singular-value identity (2), some entry of the
original `4 x 4` unitary has modulus one. Hence that unitary is
permutation/phase equivalent to
\[
1\oplus V_3,
\]
and the MOC4 inclusion holds for it for all complex spectra, including
singular and repeated cases.

#### Proof

Make the bipartite support graph with row vertices `alpha`, column vertices
`beta`, and an edge for every nonzero block. Give an edge sign `+` when its
block is conformal (`n=0`) and `-` when it is anticonformal (`m=0`).

For two distinct block rows `alpha,gamma`, row orthogonality is
\[
\sum_\beta B_{\alpha\beta}B_{\gamma\beta}^T=0.
\]
In complex coordinates it splits into the two independent equations
\[
\sum_\beta
(m_{\alpha\beta}\overline{m_{\gamma\beta}}
+n_{\alpha\beta}\overline{n_{\gamma\beta}})=0,
\tag{19}
\]
\[
\sum_\beta
(m_{\alpha\beta}n_{\gamma\beta}
+n_{\alpha\beta}m_{\gamma\beta})=0.
\tag{20}
\]
Under (17), a common neighbor of the two rows contributes a nonzero term to
exactly one of (19),(20), according as the two incident edge signs agree or
disagree. Therefore neither the number of same-sign common neighbors nor the
number of opposite-sign common neighbors can equal one.

It follows that every support `4`-cycle has positive edge-sign product:
with its two common columns, mixed relative signs would give one term in
each of (19),(20). A chordless `6`-cycle is impossible, because a pair of
its row vertices would have exactly one common neighbor. Any `6`-cycle with
a chord is the symmetric difference of two `4`-cycles. Since a bipartite
graph on `3+3` vertices has no longer simple cycle, every cycle has positive
sign product.

Hence each connected support component is a balanced signed bipartite graph.
There exist row signs `r_alpha` and column signs `c_beta` such that on every
edge
\[
\operatorname{sign}(\alpha,\beta)=r_\alpha c_\beta.
\tag{21}
\]
Conjugate output complex coordinate `alpha` when `r_alpha=-1` and input
coordinate `beta` when `c_beta=-1`. Each such conjugation swaps the conformal
and anticonformal channel, so (21) makes every nonzero block conformal.
Thus the transformed map is complex-linear.

It remains to ensure this is one of the even-even gauges to which (2)
applies. First, every support component has equally many row and column
vertices. If a component contains `r` row planes and `c` column planes,
orthonormal rows supported there give `2r<=2c`, while orthonormal columns
give `2c<=2r`; hence `r=c`.

Let `k_r,k_c` be the numbers of output and input conjugations in the gauge
just constructed. The transformed map is complex-linear orthogonal and
therefore has real determinant `+1`. Since the original `O` lies in `SO(6)`,
\[
(-1)^{k_r+k_c}=1.
\tag{22}
\]
Thus `k_r,k_c` have the same parity. If both are odd, the support-component
sizes sum to three, so at least one component has odd row/column size.
Multiplying all row and column signs in that one component by `-1` leaves
(21) unchanged and flips both parities. Hence an even-even gauge exists.

In that even-even gauge `N=0`. Equation (2) then forces
`1-P_{ij}=0` for the gauge labels `(i,j)`, so `P_{ij}=1`. A unitary with a
modulus-one entry splits as `1+3` after row/column permutations and phases.
The determinant factor is the fixed one-dimensional factor times the
three-dimensional determinant. The known `n<=3` Marcus-de Oliveira theorem
then gives a convex combination of the corresponding `S_4` endpoints.
No division by a spectral quantity occurs, so singular and repeated spectra
are included. `QED`

## 6. Generic triple-flat Hessian closure

Define the affine row nondegeneracy determinant
\[
\Omega_X=
\det\begin{pmatrix}
1&1&1\\
X_{11}-X_{21}&X_{12}-X_{22}&X_{13}-X_{23}\\
X_{11}-X_{31}&X_{12}-X_{32}&X_{13}-X_{33}
\end{pmatrix}.
\tag{23}
\]
The condition is not vacuous on structured spectral data: for the exact
structured campaign example
\[
X=
\begin{pmatrix}
-284&-294&-148\\
-624&-430&-376\\
1110&1100&590
\end{pmatrix},
\]
one has exactly
\[
\Omega_X=-133824.
\tag{24}
\]

### Theorem 3 — `MOC4-GENERIC-TRIPLE-FLAT-CLOSURE-v1`

At a genuine support maximizer, assume
\[
\Omega_X\ne0
\tag{25}
\]
and all three row-pair Hessian gates are flat:
\[
T_{12}=|C_{12}|,\qquad
T_{13}=|C_{13}|,\qquad
T_{23}=|C_{23}|.
\tag{26}
\]
Then the underlying unitary is `1+3` block-safe, hence satisfies MOC4.

#### Proof

For row `alpha=1`, equations (9), (13) for pairs `(1,2)` and `(1,3)` form
the linear system
\[
L_1 z_1=0.
\]
Condition (25) says `L_1` is invertible, hence `z_1=0`. The same argument
using the two flat pair equations incident to rows `2` and `3` gives
`z_2=z_3=0`. Thus every `m_{\alpha\beta}n_{\alpha\beta}=0`, and Theorem 2
applies. `QED`

A column-transposed version holds with the analogous affine determinant of
the column coefficient profiles.

Therefore a genuine positive-gap maximizer on the affine-generic branch
cannot have all three row-pair gates flat. At least one pair has a strict
Hessian reserve
\[
T_{\alpha\gamma}^2-C_{\alpha\gamma}^2>0.
\tag{27}
\]

## 7. Direct use of the newest partner no-go

The latest fleet01/B08 run proves that the attractive universal
same-unitary common-positive lift already fails at a dense rational unitary,
before any spectral coefficients are chosen. This run does not weaken that
counterexample and does not try to repair the refuted lift.

Instead, Theorems 1--3 constrain a *support maximizer* using exact
`Spin(6)` geometry. They therefore remain applicable precisely on the
source-valid route that survives the partner's no-go. Together with the
partner lineage's still-valid interior certificate
\[
8\min_{ij}P_{ij}+\min_{\alpha\beta}R_{\alpha\beta}\ge2
\quad\Longrightarrow\quad \text{MOC4 holds at that unitary},
\tag{28}
\]
a hypothetical counterexample may be confined simultaneously to the
complementary low-floor branch and, when `Omega_X != 0`, away from complete
row-pair Hessian flatness.

This is a target-facing narrowing, not a new positivity claim.

## 8. First essential missing implication after this run

The smallest remaining same-mechanism implication is:

> **`MOC4-ONE-FLAT-SPINOR-PROPAGATION-v1` (OPEN).**  
> For a structured spectral support pair `(K,X)` and a genuine positive-gap
> global maximizer, assume `Omega_X != 0` and one row-pair Hessian gate is
> saturated. Use its exact spinor profile (9),(13), the full first-order
> stationarity equations, the other row/column Hessian gates, and the
> same-unitary `P/R/D` constraints to prove either:
> (i) a second compatible saturation propagates to the triple-flat/block-safe
> locus above; or
> (ii) the remaining positive Hessian reserve pays the spectral support gap.
> The affine-degenerate branch `Omega_X=0` must be handled separately rather
> than assumed away.

This is strictly more specific than “use stationarity” and does not replace
the missing step by another unsupported positive representation.

## 9. Exact verifier

`verify_pure_block_rigidity.py` is a standard-library finite verifier for
the signed-support combinatorics used in Theorem 2 and an exact algebraic
sanity check of (6). It enumerates all `3^9` zero/conformal/anticonformal
support patterns, keeps the necessary orthogonality support conditions,
checks sign-gauge separability, imposes the determinant parity required by
an actual `SO(6)` realization, and verifies that an even-even gauge is then
always available.

Captured exact output:
```
spinor_gram_identity_samples=81
admissible_support_sign_patterns=512
gauge_balance_failures=0
det_compatible_patterns=256
even_even_gauge_failures=0
structured_example_Omega_X=-133824
```

The finite enumeration is a check of the short graph argument, not a
substitute for the proof above.

## 10. Honest status

**Outcome: `ESSENTIAL_STEP_APPLIED`.**

Proved this run:
- exact spinor-moment form of the lead's full Hessian anisotropy gate;
- a quantitative same-unitary collar from two pair reserves to orientation
  impurity;
- pure block-orientation rigidity to a `1+3` MOC4-safe unitary;
- generic simultaneous triple-flat Hessian closure.

Not proved:
- `MOC4-ONE-FLAT-SPINOR-PROPAGATION-v1`;
- the affine-degenerate `Omega_X=0` branch;
- full MOC4.

No benchmark material, answer key, credential, unrelated private data,
email/Drive material, paid model/API/Codex call, remote workflow, scheduler
mutation, permission change, or public release was used.
