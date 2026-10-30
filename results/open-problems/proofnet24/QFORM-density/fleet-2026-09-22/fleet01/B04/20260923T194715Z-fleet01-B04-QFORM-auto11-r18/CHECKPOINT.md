SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T19:47:15Z.
attacking: extract a target-scale product-Fourier packet from aggregate third compound volume, without a row-marginal gate.

# Early substantive checkpoint

Let a physical partition of the original independent coordinates be `I sqcup J=[n]`, and write `B=A[I,J]`. Define

`E3(B)=e_3(BB^T)=sum_{|R|=|T|=3} det(B[R,T])^2`.

The preceding fleet01/B04 compound-promotion theorem applies with no initial hub (`k=0`), compound order `ell=3`, and `Z_3=E3(B)`. Therefore every full quadratic form

`Q=F(X_I)+2 X_I^T B X_J+G(X_J)`

with arbitrary same-bank quadratic terms satisfies, whenever `E3(B)>0`,

`||p_Q||_infinity <= 6^(4/3) E3(B)^(-1/6)`,

and `p_Q in C_0(R)`.

The constant follows exactly from

`3 * 2^(9/6) * (3^3/3!)^(1/6) = 6^(4/3)`.

For symmetric `A`, define the disjoint third-compound energy

`Delta_3^disj(A)=sum_{|R|=|T|=3, R intersect T=empty} det(A[R,T])^2`.

Under a uniformly random labelled half-partition `I,J`, each fixed ordered disjoint pair `(R,T)` lands with `R subset I, T subset J` with probability `2^-6`. Hence

`E_partition E3(A[I,J]) = Delta_3^disj(A)/64`.

Consequently some original-coordinate partition has `E3(A[I,J])>=Delta_3^disj(A)/64`, and therefore

`||p_(X^TAX)||_infinity <= 2*6^(4/3) [Delta_3^disj(A)]^(-1/6)`

whenever `Delta_3^disj(A)>0`; the density is continuous and vanishes at infinity.

This does not solve the full target: `e_3(A^2)>=1` follows from three singular values >=1, but disjoint compound energy can vanish (e.g. a diagonal target). The new exact structural debt is the overlap-dominated third-compound branch.
