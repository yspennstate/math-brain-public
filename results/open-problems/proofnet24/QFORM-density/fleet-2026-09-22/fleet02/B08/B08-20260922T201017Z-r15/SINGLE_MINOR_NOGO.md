# Source-valid obstruction to single-minor payment inside the bicolloop geometry

This is a supplement to `QFORM-REGULARIZED-BICOLOOP-SCHUR-STAR-v1`. It refutes only a possible **intermediate payment mechanism**: a dimension-free lower bound on one incident physical `2x2` minor. It is not a counterexample to QFORM.

Fix `d>=1` and `gamma>0`. Let the physical cross block have one distinguished row `j`, one distinguished column `r`, and `d` other rows/columns. Put

`alpha=(gamma/sqrt(d)) 1_d`, `beta=(gamma/sqrt(d)) 1_d`,

and

`H_d = [[0, alpha^T],[beta,0_{dxd}]]`.                         (1)

The two nonzero singular values of `H_d` are exactly `gamma,gamma`. Therefore with the partner scale `g=gamma/16`,

`rho = gamma^2/(g^2+gamma^2)=256/257`,                         (2)

and

`Z_d=H_d(g^2I+H_d^T H_d)^(-1/2)`
`   =[[0,a^T],[b,0]]`,                                        (3)

where every entry of `a,b` equals `sqrt(rho/d)`. Hence

`ell=(K_L)_{jj}=rho=256/257>99/100`,
`m=(K_R)_{rr}=rho=256/257>99/100`,                             (4)

and

`theta=||Z_d||_F^2=2rho=512/257=1.992217898...<201/100`.       (5)

The lower threshold from the designated partner also holds:

`512/257 > 256/129`.                                          (6)

At the original scale, the partner transverse variables are `x_1=x_2=1`, so

`e_2(x)=1>=2/3`.                                               (7)

Thus this is genuinely inside the quantitative two-sided near-coloop branch, not merely a formal matrix resembling it.

For every remaining row `k` and column `s`, the incident normalized minor is

`det Z_d[{j,k},{r,s}] = -rho/d`.                               (8)

Therefore

`sum_{k,s} det Z_d[{j,k},{r,s}]^2 = rho^2=(256/257)^2`,        (9)

while

`max_{k,s}|det Z_d[{j,k},{r,s}]|=rho/d ->0`.                  (10)

The same phenomenon is already present before regularization:

`det H_d[{j,k},{r,s}] = -gamma^2/d`,                           (11)

so the complete physical incident bank has squared mass exactly

`sum_{k,s} det H_d[{j,k},{r,s}]^2 = gamma^4`,                 (12)

but every individual physical minor has magnitude only `gamma^2/d`.

Consequently no deduction of the form

`aggregate incident determinant mass >= c gamma^4`
`  => some incident |det physical minor| >= c' gamma^2`

with universal `c'>0` can be valid without a dimension/cardinality factor. The determinant bank must be consumed **before reciprocal inversion**, exactly as required by the current proof-first programme.

For a target-valid symmetric quadratic-form example, set `gamma=1` and

`A_d=diag(1, [[0,H_d],[H_d^T,0]])`.                            (13)

Its nonzero spectrum contains `1,+1,+1,-1,-1`, so it has at least three eigenvalues of modulus at least one. The input coordinates may be any independent cap-one densities. This construction still does not assert a large output density; it only proves the single-minor structural reduction false inside an admissible target matrix.