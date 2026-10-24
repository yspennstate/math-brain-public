# Main scalar-pivot branch

Assume s_5(A)>=1 and |a_ii|>=eta. The parent square-root kernel contributes eta^(-1/2), while its Schur complement has at least four unit-scale eigenvalues. Unfold the three half-potential branches from 02_NOPIVOT_HALF.md instead of multiplying by the coarse bound 73.

If the Schur complement has no pivot,

eta^(-1/2)*(12200/467)
<199714/2335
=85.530620985....

If it has a pair pivot,

eta^(-1/2)*(1648/25)
<674444/3125
=215.82208.

If it has another scalar pivot, the nested square-kernel estimate is

eta^(-1/2)*(1+eta^(-1/2)B)
=eta^(-1/2)+eta^(-1)B
<5776163/24500
=235.7617551020...<236.

Thus every parent scalar-pivot branch is below 236. This uses exactly the published Schur-complement and square-kernel arguments; only eta,zeta and the numerical bookkeeping changed.
