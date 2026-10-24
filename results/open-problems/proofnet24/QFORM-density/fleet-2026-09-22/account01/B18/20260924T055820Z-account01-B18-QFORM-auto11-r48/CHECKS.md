# Deterministic / constant checks for account01 B18 r48

Full QFORM remains OPEN. These checks concern only the scoped source-factorized null-pivot transfer.

## 1. General determinant identity

For

`H=[[0,r1,r2],[r1,c,d],[r2,d,a]]`,

direct expansion gives

`det H = -a r1^2 - c r2^2 + 2 d r1 r2`.

If `r=(r1,r2)` and an orthogonal pair change sends `r` to `(beta,0)`, `beta=||r||_2`, the transformed matrix is

`H'=[[0,beta,0],[beta,alpha,delta],[0,delta,gamma]]`.

The pair change has determinant modulus one, so

`det H'=det H=-beta^2 gamma`.

Thus the account02/B18 receiver currency `|beta^2 gamma|` is exactly `|det H|`; no lower-bound loss occurs in the deterministic reduction.

## 2. Source-cap arithmetic

Account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1` gives

`||p_Q||_infinity <=3(2 M K)^(2/3)|det H|^(-1/3)`.

For one literal original scalar `S`, one unit product-bank projection `Y`, and a second literal original scalar `W`,

`K=1`, `M<=||p_Y||_infinity ||p_W||_infinity<=sqrt(2)`.

Therefore

`3(2 M K)^(2/3) <=3(2 sqrt(2))^(2/3)=6`.

If both non-pivot pair coordinates are literal original scalars, this improves to

`3*2^(2/3)=4.762203155904598...`.

If the pivot and both pair coordinates are arbitrary unit projections of three disjoint product banks, the universal LPP caps give

`K<=sqrt(2)`, `M<=2`,

hence `3*2^(5/3)=9.524406311809198...`.

## 3. Householder target family

Set

`n=(1/sqrt(2),1/2,1/2)`, `H=I-2 n n^T`.

Then exactly

`H=[[0,-1/sqrt(2),-1/sqrt(2)],
    [-1/sqrt(2),1/2,-1/2],
    [-1/sqrt(2),-1/2,1/2]]`.

Since `H` is a Householder reflection,

`H^2=I`, `spec(H)={-1,1,1}`, `det H=-1`.

The 45-degree pair rotation

`O=(1/sqrt(2))*[[1,1],[1,-1]]`

puts the full core into

`diag(1,O)^T H diag(1,O)
 =[[0,-1,0],[-1,0,0],[0,0,1]]`.

Thus the form is exactly a null-pivot hyperbolic product plus one square after a determinant-one change of the JOINT pair; no probabilistic independence after that rotation is asserted.

For a flat bank `Y_m=m^(-1/2) sum_{j=1}^m X_j`, the literal principal block on `{S,X_j,W}` equals

`D H D`, `D=diag(1,m^(-1/2),1)`,

so

`det(D H D)=det(D)^2 det(H)=-1/m`.

Hence literal single-triple determinant payment deteriorates as `m^(1/3)`, while the grouped source-factorized bound stays at `6`.

## 4. Coefficient-sensitive primary-source sharpening

For `Y=v^T X_J`, Juškevičius--Lee Theorem 1 implies

`||p_Y||_infinity <= R(v)`,

where `R(v)` is the maximum density of the sum of independent centered uniforms with interval lengths `|v_j|` (zero coefficients omitted). LPP/Ball gives `R(v)<=sqrt(2)` for `||v||_2=1`.

Thus the same receiver yields the coefficient-sensitive version

`||p_Q||_infinity <=3(2 R(v))^(2/3)|det H|^(-1/3)`

when the pivot and third coordinate are literal cap-one originals.

For the flat vector `v_j=1/sqrt(m)`, this gives `R_2=sqrt(2)` and constant exactly `6`; for `m=3`, `R_3=3sqrt(3)/4` and the constant is `5.6696447245...`. The universal statement remains `<=6`.
