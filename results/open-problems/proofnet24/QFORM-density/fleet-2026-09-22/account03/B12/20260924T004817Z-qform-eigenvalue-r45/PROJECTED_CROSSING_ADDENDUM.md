# r45 addendum — required application of the checked arbitrary-rank projected-crossing theorem

This addendum consumes the later owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, which specifically asks B09--B12 workers to apply `NEW_PROJECTED_CROSSING.md` to an actual surviving physical partition and check the rank, projected volume and all row-marginal gates.

Source theorem: `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

## Actual original-coordinate partition

Use fourteen ORIGINAL coordinates and split them as

- hub set `K={1,2}`;
- light set `I={3,4,5,6,7,8}`;
- light set `J={9,10,11,12,13,14}`.

The hub variables are exactly `(X_1,X_2)`, so their joint density is at most one: `M_H<=1`.

Let the final coefficient matrix have the following physical blocks:

1. the `K x K` hub block is arbitrary symmetric (so arbitrarily large positive or negative additional hub spectrum is allowed);
2. `A[K,J]=M_J=2[I_2,0_(2x4)]` and `A[K,I]=0`;
3. `A[I,J]=2 I_6 + E`, with `||E||_op<=1/100`;
4. every block internal to `I` or internal to `J`, every diagonal and every linear term after outside conditioning is arbitrary.

This is a concrete subfamily of the additional-eigenvalue setting. The arbitrary hub block is absorbed by the theorem's arbitrary measurable hub function `F`; it is not treated as an independent quadratic remainder. The small crossing perturbation is deterministic coefficient error, not a random-noise approximation.

## Check every projected-crossing hypothesis

Take `k=2`, `ell=1`. The matrix `M_J` has rank two and singular values `(2,2)`, hence

`S=s_1(M_J)s_2(M_J)=4`.

The row-space projection of `M_J` in the six `J` coordinates is

`Pi=diag(1,1,0,0,0,0)`.

The projected light crossing is

`C=(2I_6+E)(I-Pi)`.

For `E=0`,

`C_0=2 diag(0,0,1,1,1,1)`,

so `||C_0||_F=4`. Since `||E(I-Pi)||_F<=sqrt(6)/100`,

`F:=||C||_F >= 4-sqrt(6)/100 = 3.975505102572168...`.

For `ell=1`, the volume is exactly

`Z_1=e_1(CC^T)=||C||_F^2`,

hence

`Z_1 >= (4-sqrt(6)/100)^2`.

Every row of `E(I-Pi)` has Euclidean norm at most `1/100`. Consequently every row of `C` has squared norm at most

`(2+1/100)^2`.

The `ell=1` volume row marginals therefore obey

`alpha_i = ||C_{i,*}||_2^2/Z_1
          <= (2.01)^2/(4-sqrt(6)/100)^2
          = 0.25562744803031934... < 1/2`.

Thus the rank, nonzero projected volume, and every row-marginal gate are verified on the actual physical partition.

## Density inequality

The grouped projected-crossing theorem (GC) with `k=2`, `ell=1`, `d=3` and `M_H<=1` gives, with the `ell=1` exponential factor omitted,

`||p_Q||_infinity
 <= 3 * 2^(5/6) * S^(-1/3) * Z_1^(-1/6)`.

Using `S=4` and the lower bound on `Z_1`,

`boxed( ||p_Q||_infinity <= 2.125668232876967... ).`

At `E=0` this specializes to the clean value

`boxed( ||p_Q||_infinity <= 3/sqrt(2) = 2.1213203435596424... ).`

Because the theorem supplies an integrable characteristic-function envelope (`d=3>2`), this branch has a continuous `C_0` density.

This calculation is independent of the six-mode compiler in the main r45 report and is much sharper on this concrete surviving partition. It also verifies the later owner request at an equation rather than merely citing the projected-crossing theorem.

## Scope

This does not solve full QFORM. The bare hypothesis `s_3(A)>=1` still does not force every matrix into this quantitative partition: one must still produce rank-two hub crossing product `S`, nontrivial projected light volume `Z_1`, and the row-marginal gate, or route failure to another paid mechanism. The unrestricted target remains OPEN.
