# Deterministic checks — fleet01/B09 20260924T005202Z

These checks are regression aids; the report contains the exact proofs.

## 1. Symbolic anchored-compound identity

For

`B=[[b11,b12],[b12,b22]]`, `g=(g1,g2)^T`, and leaf entries `r_i,r_j,D_ij`, direct symbolic expansion of

`det [[B,g r_j],[r_i g^T,D_ij]]`

gives

`b11*b22*D_ij-b12^2*D_ij
 -b11*g2^2*r_i*r_j
 +2*b12*g1*g2*r_i*r_j
 -b22*g1^2*r_i*r_j`,

which equals identically

`det(B) D_ij - (g^T adj(B)g) r_i r_j`.

A SymPy subtraction and factorization returned exactly `0`.

## 2. Singular-pair ledger

If `det B=0`, then `N_H=-kappa rr^T`, so

`sum_i N_ii^2 = kappa^2 sum_i r_i^4`,

`sum_(i!=j) N_ij^2
 =kappa^2[(sum_i r_i^2)^2-sum_i r_i^4]`,

and the sum is `kappa^2||r||_2^4`.

No entry of the leaf matrix `D` remains. This is algebraic, not numerical.

## 3. Concentration constant

At `omega=1/4`, `eta=1/16`, the principal determinant lower bound is

`eta*sqrt(omega)=1/32`.

The completed physical-triple theorem therefore gives

`216*(1/32)^(-1/3)
 =216*32^(1/3)
 =685.7572544502622... <686`.

## 4. Flat-star stress family

Take `m=64`, `r_i=1/8`. Then

`||r||_2^2=64/64=1`,
`q=max_i r_i^2/||r||^2=1/64`,
`P_H=sum_i r_i^4=64/4096=1/64`,
`Omega_(2,H)=1-P_H=63/64`.

Every principal anchored triple determinant has magnitude `r_i^2=1/64<1/32`.

If `v perpendicular to r` is unit and `D=t vv^T`, the invariant subspaces are:

- first hub: eigenvalue `1`;
- span(second hub, `r`): matrix `[[0,1],[1,0]]`, eigenvalues `+1,-1`;
- span(`v`): eigenvalue `t`;
- remaining leaf orthocomplement: eigenvalue `0`.

So the target hypothesis holds for every real `t`, while the anchored compound matrix remains `-rr^T` for every `t`.

## 5. Partner application

At `t=0`, `m=64`, the designated fleet02/B09 r15 theorem has

`tau=1`, `||A[I,H]k||_2=||r||_2=1`,

so its bound is exactly

`6*1^(-1/3)*1^(-2/3)=6`.

The spectrum is `{1,+1,-1}` plus zeros.
