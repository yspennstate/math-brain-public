SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-24T00:37:41Z.
attacking: spectral-tail alignment rigidity — turn approximate arm alignment into either a scalar carrier plus physical diagonal or an actual near-disjoint physical two-bank frame.

# account01/B08 r39 — approximate-alignment rigidity for the diffuse deletion tail

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Designated partner: `account02/B08`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING STRUCTURAL THEOREM + QUANTITATIVE NORMAL-FORM DICHOTOMY / FULL TARGET OPEN**.

The unrestricted conjecture remains OPEN. This run proves a coefficient-space rigidity theorem for the precise approximate-alignment survivor left by r38. It does not discard a small quadratic perturbation, does not rotate the independent random variables, and does not claim a density bound merely from Frobenius closeness. Continuity for the unrestricted target remains OPEN.

## 1. Pinned inputs actually used


Own preceding endpoint:

`yspennstate/math-open-problems@6691a29d20e3cfd119c67b7b6bc345c68f407712`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T234122Z-account01-B08-qform-r38/REPORT.md`.

There, after deleting one original coordinate, the child block is written

`C = U D_* U^T + E`, `U^T U=I_2`, `E U=0`,

and for the diffuse branch `nu=max_i ||U_{i,*}||^2<=1/48`. The proved quantitative alignment lemma gives symmetric `R in R^(2x2)` and physical diagonal `D_0` such that

`E = U R U^T + D_0 + F`,

`||F||_F <= c_nu D_U(E)`,

where

`c_nu=sqrt(3/(1-nu))`,

and

`D_U(E)^2 = sum_i (1-ell_i) dist(E[i,-i],row(U_{-i}^T))^2`,
`ell_i=||U_{i,*}||^2`.

At `nu<=1/48`,

`c_nu <= 12/sqrt(47)=1.7503798979747347...`.

Designated partner source actually read in full:

`yspennstate/math-open-problems@175ed537ecbeabeb27e98b49030c9b8ca846c5d7`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260923T2307Z-auto11/REPORT.md`.

Its exact intrinsic compound identity is

`Xi(M,S) = [s_1(M)s_2(M)]^2 D_M(S)^2`.

Applying this algebraic theorem with the actual matrix pair `(M,S)=(U^T,E)` gives the exact inequality/equality

`boxed: Xi(U^T,E)^(1/2)=D_U(E)`.

Thus the alignment variable used below is literally the partner's compound three-volume currency for the carrier frame. I use only this algebraic part here; `U^T` is a coefficient carrier, not two literal physical hub rows, so I do **not** invoke the partner's physical-hub density corollary from this substitution.

## 2. New exact row-eigenvector identity

Assume generally

`U in R^(m x 2)`, `U^T U=I_2`, `E=E^T`, `EU=0`,

and suppose

`E = U R U^T + D_0 + F`,                                      (2.1)

with `R=R^T in R^(2x2)`, `D_0=diag(d_1,...,d_m)`, and `F=F^T`.

Choose an orthogonal `O in O(2)` diagonalizing `R`:

`O^T R O = diag(r_1,r_2)`.

Replace only the two-dimensional coefficient frame by `UO`; this is a change of basis inside the deterministic carrier and is **not** a rotation of the random variables. Write the ith row of `UO` as

`u_i=(x_i,y_i)`, `ell_i=x_i^2+y_i^2`,

and put

`Delta=|r_1-r_2|`, `G=F(UO)`.

Since `EU=0`, multiplying (2.1) by `U` and then by `O` gives, row by row,

`(r_1+d_i)x_i = -G_{i1}`,
`(r_2+d_i)y_i = -G_{i2}`.                                    (2.2)

For fixed `x,y,r_1,r_2`, minimizing

`(r_1+d)^2 x^2 + (r_2+d)^2 y^2`

over the scalar `d` gives exactly

`Delta^2 x^2 y^2/(x^2+y^2)`                                  (2.3)

when `x^2+y^2>0`. Therefore (2.2) yields

`boxed:
 Delta^2 sum_i [x_i^2 y_i^2/ell_i]
 <= ||FU||_F^2
 <= ||F||_F^2.`                                                (2.4)

This is the basic rigidity estimate. It says that a non-scalar carrier matrix `R` cannot coexist with substantial physical row mixing of its two eigendirections unless the alignment error `F` is correspondingly large.

Since

`min(x_i^2,y_i^2) <= 2 x_i^2 y_i^2/(x_i^2+y_i^2)`,

(2.4) also gives

`boxed:
 sum_i min(x_i^2,y_i^2)
 <= 2 ||F||_F^2/Delta^2`                                      (2.5)

for `Delta>0`.

## 3. Complementary scalar-carrier estimate

Let

`r=(r_1+r_2)/2`.

Equation (2.2) can be written

`(d_i+r)u_i = -G_i -(R-rI_2)u_i`.

Summing squared norms and using

`||U(R-rI_2)||_F^2=||R-rI_2||_F^2=Delta^2/2`

gives

`boxed:
 sum_i ell_i (d_i+r)^2
 <= 2||F||_F^2 + Delta^2.`                                    (3.1)

Moreover

`E-(rUU^T+D_0)=U(R-rI_2)U^T+F`,

so

`boxed:
 ||E-(rUU^T+D_0)||_F
 <= ||F||_F + Delta/sqrt(2).`                                  (3.2)

Thus a small carrier eigenvalue gap forces the whole spectral tail close to a **scalar** rank-two carrier plus a physical diagonal.

## 4. Exact zero-error classification sharpened

If `F=0`, then (2.2) is exact.

If `Delta>0`, no row can have both `x_i` and `y_i` nonzero. Hence the two columns of `UO` have disjoint physical supports. More precisely,

- if `x_i!=0`, then `d_i=-r_1`;
- if `y_i!=0`, then `d_i=-r_2`;
- if both vanish, `d_i` is unrestricted.

So the non-scalar exact-alignment endpoint is not an arbitrary diffuse object: after a two-dimensional deterministic carrier basis change it is an **exact two-bank physical decomposition**.

If `Delta=0`, then `R=rI_2`, and every nonzero carrier row satisfies `d_i=-r`. This is the scalar-carrier endpoint.

This refines the partner's zero-alignment representation `E=URU^T+D_0` by exploiting the additional spectral identity `EU=0` that is present in the deletion geometry.

## 5. Quantitative normal-form dichotomy

Let

`mathcal D = D_U(E)`

and suppose the r38 quantitative decomposition is chosen, so

`||F||_F <= c_nu mathcal D`.

Write the dimensionless alignment size

`d=mathcal D/L`.

At `nu<=1/48`, put

`c_0=12/sqrt(47)`.

Then (2.4)-(3.2) imply the following scale-free dichotomy for every `d>0`.

Set

`g=sqrt(2 c_0 d)`.

### Scalar branch

If

`Delta/L <= g`,

then

`boxed:
 ||E-(rUU^T+D_0)||_F
 <= [sqrt(c_0 d)+c_0 d] L.`                                    (5.1)

Indeed `||F||_F/L<=c_0d` and `g/sqrt2=sqrt(c_0d)`.

### Two-bank branch

If

`Delta/L > g`,

then (2.5) gives

`rho:=sum_i min(x_i^2,y_i^2) < c_0 d`.                         (5.2)

Assign each physical row to the larger of `|x_i|,|y_i|`, and delete the smaller component. This gives a matrix `V` whose two columns have **disjoint physical supports** and

`||UO-V||_F^2=rho<c_0d`.                                       (5.3)

Both columns of `V` have squared norm at least `1-rho`. If `c_0d<1`, normalize them separately; because their supports are disjoint, the resulting matrix `Vhat` has orthonormal columns and still has disjoint physical supports. Quantitatively,

`boxed:
 ||UO-Vhat||_F
 <= sqrt(c_0d)+sqrt(2)[1-sqrt(1-c_0d)].`                        (5.4)

Hence approximate arm alignment plus the spectral condition `EU=0` forces either a scalar carrier modulo physical diagonal, or a carrier frame close to a genuine original-coordinate two-bank frame. No probabilistic moment, compactness, log-concavity, or support regularity enters.

At the partner's previous unresolved alignment scale

`d <= eta_619 = 0.003798734015533447`,

one has

`c_0 d <=0.006649227658542589`.

Therefore the scalar branch has

`||E-(rUU^T+D_0)||_F <0.088193 L`,                              (5.5)

while the two-bank branch gives an exact disjoint-support orthonormal frame `Vhat` satisfying

`||UO-Vhat||_F <0.086253`.                                      (5.6)

These are structural estimates, not a license to erase the residual quadratic form.

### Claim name

`QFORM-SPECTRALTAIL-APPROXALIGNMENT-RIGIDITY-v1`.

## 6. Why this is useful for the full problem

The preceding runs had reduced one difficult diffuse deletion chamber to a small alignment-energy survivor. The new theorem shows this survivor has only two geometric endpoints:

1. **scalar-carrier + physical diagonal:** `C` is close to `U K U^T + physical diagonal` with the tail correction scalar on the carrier; or
2. **two physical banks:** after a two-dimensional carrier basis change, `U` is close to a frame whose columns live on disjoint sets of the original independent coordinates.

The second alternative is particularly relevant because the two carrier projections of an exact disjoint-support frame are built from disjoint independent coordinate banks. The first alternative is compatible with the completed separable-phase/diffuse-carrier machinery. What is still missing is a receiver stable under the nonzero residual **without** treating it as an independent or harmless random perturbation.

This is a genuine mechanism change from the previous three runs' deletion-crossing volume arguments: the new step is an invariant-subspace/row-eigenvector rigidity argument.

## 7. First unpaid implication

`QFORM-RIGIDITY-NORMALFORM-RECEIVER-v1`:

Consume either (5.1) or (5.4) in the full ambient quadratic form, retaining all complementary spectrum, the deleted-coordinate star, conditioning-generated affine terms and the original product law. In the scalar branch, use an aggregate projected-crossing/ridge receiver that is stable under the displayed residual. In the two-bank branch, exploit the nearly disjoint original-coordinate banks before any spectral-coordinate conditioning. A proof may not assert independence after a general rotation and may not discard the residual as a small random quadratic perturbation.

Full target status: **OPEN**.  
Full-target continuity status: **OPEN**.  
No counterexample to QFORM is produced.

## 8. Deterministic sanity check

A deterministic-seed finite check constructs random orthonormal `U`, symmetric `R`, physical diagonal `D_0`, and a symmetric `F` satisfying the prescribed equation `FU=-(UR+D_0U)`, so `EU=0` exactly up to floating-point error. Across 2000 trials it found zero violations of (2.4) and (3.1). The check is only a regression/sanity test; the proof above is exact.
