# Deterministic checks for QFORM-FIXEDPAIR-AGGREGATE-THREEVOLUME-v1

Run: `20260923T164801Z-account01-B09-QFORM-auto11`.

These checks are supplementary only; the proof in `REPORT.md` is analytic.

## 1. Exact Gram/Cauchy--Binet identity: finite numerical regression

A fixed-seed symmetric `9 x 9` real matrix was generated (`numpy.random.default_rng(20260923)`), with physical pair `H={0,1}`, leaf split `I={2,3,4}`, `J={5,6,7,8}`.

For

`Delta=det(A[H,J] A[H,J]^T)=2.9375805508649564`,

and `C=A[I,J](I-Pi_row(A[H,J]))`, the three row identities

`Delta ||C_i||^2 = sum_{T subset J, |T|=3} det A[H union {i},T]^2`

returned respectively

- row 2: left `1.556542400646045`, right `1.5565424006460444`;
- row 3: left `0.26462152657367083`, right `0.26462152657367066`;
- row 4: left `2.492756010937104`, right `2.492756010937104`.

Maximum absolute discrepancy: `6.661338147750939e-16`.

The summed values were `4.31391993815682` and `4.313919938156819`.

## 2. Random-partition expectation: exhaustive finite regression

For the same matrix, all `2^7=128` literal partitions of the seven leaf coordinates were enumerated with independent inclusion probability `p=3/4` on the `J` side.

The global fixed-pair volume was

`V=52.81995349097337`.

The exact weighted partition average was

`E W=5.570854469751097`,

while

`(1-p)p^3 V = (27/256)V =5.570854469751097`.

Ratio: exactly `1.0` at displayed precision.

## 3. Constants

Using the safe source constant `5.35` from Claude Theorem 6.5:

`5.35*(256/27)^(1/6)=7.783348603264946`.

The promoted-third-hub branch gives

`3*sqrt(2)*(512/27)^(1/6)=6.92820323027551=4*sqrt(3)`.

Thus `7.784` covers both branches.

For the designated-partner family with `V>=1/4`:

`7.783348603264946*4^(1/6)=9.806404743923364 < 9.807`.

For the account03/B09 r35 compiler with `V>=27 G_*/400`:

`7.783348603264946*(400/27)^(1/6)=12.197828419627104 < 12.198`.

## 4. Homogeneity

Each `3 x 3` determinant is cubic in the coefficient matrix; its square has degree six. Therefore `V` has degree six and `V^(-1/6)` has degree minus one, exactly the scaling of an output density under `A -> sA`.

## 5. Scope checks

- Every determinant used in `V_i` has disjoint physical row/column sets: row set `H union {i}`, column set `T subset H^c\{i}`.
- `W>0` forces `det(M_JM_J^T)>0` and `F>0`; hence Theorem 6.5 is never invoked with a singular two-hub partner block.
- In the diffuse branch, `Delta ||c_i||^2=W_i<=V_i<=W/2=Delta F^2/2`, so the row-share condition is exactly verified.
- In the heavy branch, Cauchy--Binet identifies the complete three-hub cross Gram determinant with `V_i`, with no spectral rotation of the input law.
- No Monte Carlo/histogram evidence is used for the theorem.
