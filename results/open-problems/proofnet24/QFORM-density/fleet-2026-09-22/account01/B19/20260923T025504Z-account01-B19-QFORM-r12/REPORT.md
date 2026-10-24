# B19 r12 — co-heavy single-row extraction fails; exact three-bank aggregate endpoint is paid

Status: `ESSENTIAL_STEP_APPLIED / SOURCE-VALID INTERMEDIATE COUNTEREXAMPLE / FULL TARGET OPEN`.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Target and scope

The global target remains: for independent real coordinates with densities at most one and real symmetric `A` having at least three eigenvalues of modulus at least one, prove one dimension-free finite `L^infinity` bound for the density of `X^T A X`. Continuity is separate.

This report attacks the current account02/B19 r22 residual `QFORM-O3-TWO-RANK2-COHEAVY-AGGREGATE-ROUTING-v1`. It does two things:

1. proves a sharp geometric alignment inequality for a co-heavy row whose grouped 2+1 determinant is small;
2. constructs an exact target-class family showing that fixed transverse frame mass plus co-heavy rows does **not** force any single grouped physical row of fixed determinant size. The family has every physical diagonal equal to zero, so the failure is not repaired by a scalar diagonal pivot. It is nevertheless uniformly paid by a genuinely aggregate three-bank smoothing theorem.

The family is **not** a counterexample to QFORM. It is a counterexample only to a single-row extraction mechanism.

## Peer inputs actually used

### account02/B19 r22

Source-pinned handoff: `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B19/20260923T020950Z-account02-B19-QFORM-r22.md`; canonical mathematics `yspennstate/math-open-problems@3a8e3494dac898f3b7180d5b80a8c5eb974a8412`.

For a rank-two bank `G` with covariance `S_G`, unit normal `n_G`, and a physical row `u_i` outside `G`, r22 proves

`delta_i = pdet(S_G) (n_G . u_i)^2`,

and for a second transverse rank-two bank `H`,

`sum_{i in H} delta_i = pdet(S_G) n_G^T S_H n_G >= g^2 h eta`,

where `g,h` are the least positive eigenvalues of `S_G,S_H` and `eta=1-(n_G.n_H)^2`.

It also proves a direct grouped-row density payment `<105 delta_i^{-1/2}` and the diffuse two-bank theorem when all internal normalized leverages are at most `1/2`.

### account02/B06 weighted affine-fiber Brascamp--Lieb theorem

Source-pinned handoff: `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B06/b06-20260922T155426Z-9fd56fa68a65.md`; canonical mathematics `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

For a normalized one-dimensional physical projection `Y=sum c_i X_i`, `sum c_i^2=1`, of independent cap-one inputs,

`||p_Y||_infinity <= exp(1/2)=sqrt(e)`.

This is used below on actual disjoint original-coordinate banks.

### account01/B19 prior linear-square smoother

From `yspennstate/math-open-problems@09bb706f11ea00995a61f0c7323bf67997c65932`, if `X` is independent of `(Y,Z)`, `p_X<=1`, `p_(Y,Z)<=H`, and

`T=2sXY+aY^2+fZ^2`,

then

`||p_T||_infinity <= 6 H^(2/3) |s^2 f|^(-1/3)`.

By scaling `X`, the cap-`K` form is

`||p_T||_infinity <= 6 (K H)^(2/3) |s^2 f|^(-1/3)`.

True independence of the scalar bank from the pair is retained below; no conditional-cap substitute is used.

---

## 1. Co-heavy alignment inequality

Let `P_G=n_G^perp` and `P_H=n_H^perp` be two distinct planes in `R^3`. Let

`S_G=sum_{i in G} u_i u_i^T`, `S_H=sum_{j in H} u_j u_j^T`

have rank two, with least positive eigenvalues `g,h>0`. Put

`eta=1-(n_G.n_H)^2>0`.

For `i in G`, define its normalized internal leverage

`ell_i=u_i^T S_G^+ u_i`,

and its grouped determinant against `H`

`delta_i=pdet(S_H)(n_H.u_i)^2`.

Let `L=P_G intersect P_H`, choose a unit vector `l` on `L`, and a unit `m in P_G` perpendicular to `l`. Then `|n_H.m|=sqrt(eta)`. Write

`u_i=alpha_i l + beta_i m`.

Because `S_G^+ <= g^{-1} I` on `P_G`,

`ell_i <= ||u_i||^2/g`,

hence

`||u_i||^2 >= g ell_i`.

Also `pdet(S_H)>=h^2`, so

`delta_i >= h^2 eta beta_i^2`.

Therefore

`boxed: dist(u_i,L)^2=beta_i^2 <= delta_i/(h^2 eta)`,

and

`boxed: |alpha_i|^2 >= g ell_i - delta_i/(h^2 eta)`.

In particular, if `ell_i>1/2` and `delta_i` is small, the co-heavy row is forced close to the common intersection line while retaining a quantitatively nontrivial longitudinal norm. This conclusion is purely frame-geometric; it makes no coefficient-perturbation claim about `u_i^T M u_i`, so it does not violate the known correction against deleting small spectral-coordinate errors for unrestricted `M`.

---

## 2. Exact target family saturating the aggregate identity while every row atom vanishes

Fix an integer `m>=2` and the standard basis `e1,e2,e3` of `R^3`.

Define bank `G` by the rows

- `g0=(1/2)e1`,
- `g1=(1/sqrt(12))e1`,
- `m` rows `g_r=(1/sqrt(3m))e2`.

Then

`S_G=diag(1/3,1/3,0)`, `g=1/3`, `n_G=e3`.

The heavy row has

`ell(g0)=(1/4)/(1/3)=3/4>1/2`.

Define bank `H` symmetrically by

- `h0=(1/2)e1`,
- `h1=(1/sqrt(12))e1`,
- `m` rows `h_r=(1/sqrt(3m))e3`.

Then

`S_H=diag(1/3,0,1/3)`, `h=1/3`, `n_H=e2`,

and `ell(h0)=3/4`. Since `n_G.n_H=0`,

`eta=1`.

Add a remainder bank `K` containing

- `m` rows `(1/sqrt(3m))e1`,
- `m` rows `sqrt(2/(3m))e2`,
- `m` rows `sqrt(2/(3m))e3`.

The sum of all row outer products is exactly

`S_G+S_H+S_K=I_3`.

Thus the matrix `R` whose rows are all these vectors has orthonormal columns: `R^T R=I_3`.

Take

`M = [[0,1,1],[1,0,1],[1,1,0]]`.

Its eigenvalues are `2,-1,-1`. Hence

`A=R M R^T`

is a valid exact-rank-three QFORM target with nonzero spectrum exactly `{2,-1,-1}`.

Every row of `R` lies on one coordinate axis and the diagonal of `M` is zero, so

`boxed: A_ii=u_i^T M u_i=0 for every physical coordinate i.`

Thus no nonzero physical scalar diagonal pivot exists anywhere in this family.

Now apply account02/B19 r22's exact grouped identity. Relative to bank `H`,

`pdet(S_H)=1/9`, `n_H=e2`.

For the two `e1` rows in `G`, `delta_i=0`. For each of the `m` transverse `e2` rows,

`delta_i=(1/9)(1/(3m))=1/(27m)`.

Therefore

`boxed: max_{i in G} delta_i=1/(27m) -> 0`,

while

`boxed: sum_{i in G} delta_i=1/27=g^2 h eta`.

The symmetric statement holds from `H` toward `G`. For `m>=22`, every grouped row has `delta_i<1/576`, so the r22 single-row `<2520` trigger does not fire, even though the aggregate lower bound is attained exactly and both banks contain leverage-`3/4` rows.

Consequently there is no positive function `c(g,h,eta)` such that, under the co-heavy hypotheses alone,

`max_i delta_i >= c(g,h,eta)`.

This gives the correction

`QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1`.

It is a target-class, source-valid obstruction to reciprocal single-row selection, not a QFORM counterexample.

---

## 3. The same family is uniformly paid by an aggregate three-bank theorem

The obstruction above is constructive: it identifies the correct currency as whole-bank aggregation.

### Theorem: zero-diagonal three independent scalar banks

Let `Y1,Y2,Y3` be mutually independent real random variables with density caps `K1,K2,K3`. Let

`q=2(a Y1 Y2+b Y1 Y3+c Y2 Y3)`

with `abc != 0`. Equivalently, the coefficient matrix is

`M0=[[0,a,b],[a,0,c],[b,c,0]]`,

so `det M0=2abc`. Then

`boxed: ||p_q||_infinity <= 6 (K1 K2 K3)^(2/3) |det M0|^(-1/3).`

#### Proof

Set

`X=Y2`, `Y=aY1+cY3`, `Z=aY1-cY3`.

Since `Y1,Y3` are independent and the determinant of `(Y1,Y3)->(Y,Z)` has modulus `2|ac|`,

`||p_(Y,Z)||_infinity <= K1 K3/(2|ac|)`.

Also `X` remains genuinely independent of `(Y,Z)` and has density cap `K2`. Since

`Y1Y3=(Y^2-Z^2)/(4ac)`,

we have the exact identity

`q=2XY + (b/(2ac))(Y^2-Z^2)`.

Apply the cap-`K2` linear-square smoothing theorem with

`s=1`, `f=-b/(2ac)`, `H=K1K3/(2|ac|)`.

It gives

`||p_q||_infinity`
`<=6 [K1K2K3/(2|ac|)]^(2/3) [|b|/(2|ac|)]^(-1/3)`
`=6 (K1K2K3)^(2/3) |2abc|^(-1/3)`
`=6 (K1K2K3)^(2/3) |det M0|^(-1/3)`.

All signs are allowed. Nondegeneracy of the zero-diagonal `3x3` form is exactly `abc!=0`. No post-rotation independence is asserted.

### Apply it to the exact co-heavy family

Partition all original coordinates by their row direction `e1,e2,e3`. Define the three spectral aggregates

`Y_j=sum_{i: u_i parallel e_j} ||u_i|| X_i`.

These use disjoint original-coordinate banks, hence are mutually independent. Because `R^T R=I_3`, each coefficient vector has Euclidean norm one.

Apply account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at `k=1` to each actual bank:

`K_j=||p_(Y_j)||_infinity <= sqrt(e)`.

For the chosen `M`, `a=b=c=1` and `|det M|=2`. Therefore

`boxed: ||p_(X^T A X)||_infinity <= 6 e 2^(-1/3) = 12.9450103021... < 12.946.`

Thus the family is uniformly safe for **all** independent cap-one original-coordinate laws and every `m`, despite

- fixed `g=h=1/3`, `eta=1`,
- two leverage-`3/4` co-heavy rows,
- every physical diagonal equal to zero,
- `max_i delta_i -> 0`.

This is an explicit proof that the missing co-heavy branch requires aggregate product structure rather than a hidden constant-size row atom.

---

## 4. Conditional end-to-end splice and first remaining implication

The completed account02/B19 r22 theorem pays the transverse two-rank-two state when both banks have internal normalized leverages at most `1/2`; it also pays any single row with a large grouped determinant. The present alignment lemma says that a surviving co-heavy row with small grouped determinant is nearly forced onto the common intersection line. The exact family above shows that this behavior can coexist with a fixed aggregate transverse determinant mass spread over arbitrarily many weak rows and with no physical diagonal pivot.

Therefore the first honest residual is not a single-row selector. It is

`QFORM-COHEAVY-INTERSECTION-LINE-AGGREGATE-ROUTING-v1`:

> Starting from fixed positive `g,h,eta`, use the forced intersection-line concentration of all co-heavy/small-delta rows together with the exact aggregate mass `sum delta >= g^2 h eta` to construct a product-preserving **bank-level** payment (three-bank, ridge, or exact Schur/grouped-coordinate) before any reciprocal individual minor is selected, uniformly with arbitrary same-bank curvature, signs and extra spectrum.

The zero-diagonal three-scalar-bank theorem above pays one exact generated-span endpoint of this residual. What remains is the non-axis, arbitrary-self-curvature and arbitrary-extra-spectrum passage from the geometric alignment/aggregate identities to such a bank-level normal form.

## Corrections preserved

No step uses post-rotation independence, the false arbitrary-joint coarea bound, a conditional-density cap as independence, law-uniform pointwise quadratic-phase decay, reciprocal single-good-minor extraction, or perturbative deletion of small matrix coefficients. The only rotation-like map `(Y1,Y3)->(Y,Z)` occurs *inside one already grouped independent pair* and its exact Jacobian is carried in the pair density bound; the scalar `Y2` remains an independent original-coordinate bank.

## Outcome

`ESSENTIAL_STEP_APPLIED`.

Full QFORM target: `OPEN_NOT_PROVED`.

Continuity: not established by this report.
