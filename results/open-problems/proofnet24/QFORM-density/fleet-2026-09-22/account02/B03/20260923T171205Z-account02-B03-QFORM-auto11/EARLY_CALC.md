# Early calculation — critical grouped crossing plus one square

Programme `QFORM-DENSITY-3EIG-20260922`, account02/B03.

Apply the completed grouped projected-crossing estimate `GC` from `interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` at its critical non-density exponent `k=1, ell=1`.  Write `F=sqrt(Z_1)=||C||_F`, let `S` be the one-dimensional singular-value product of the hub-partner row on `J`, and assume the one-volume row marginals `alpha_i=||c_i||^2/F^2` are all at most `1/2`.  If the one-dimensional hub projection has density cap `M_H`, then `GC` gives

`|phi_R(t)| <= min(1, K/|t|)`,

`K = 2*pi*M_H^(1/2)*(S*F)^(-1/2)`.

This is not L1, hence `GC` alone does not give a density.  But it is exactly enough for the half-Riesz receiver:

`int_R |t|^(-1/2)|phi_R(t)| dt <= 8 sqrt(K)`,

so using `int_R |t|^(-1/2)e^(itx)dt=sqrt(2*pi)|x|^(-1/2)`,

`sup_s E|R-s|^(-1/2) <= 8 M_H^(1/4)(S F)^(-1/4)`.

The dependence-safe independent-copy integral is even sharper:

`int_R |t|^(-1/2)|phi_R(t)|^2 dt <= (16/3)sqrt(K)`
` = (16/3)sqrt(2*pi) M_H^(1/4)(S F)^(-1/4)`.

Also `int |phi_R|^2 <= 4K`, hence

`||p_R||_2^2 <= 4 M_H^(1/2)(S F)^(-1/2)`

and therefore the collision law has the genuinely linear small-ball estimate

`P(|R-R'|<=eps) <= 8 M_H^(1/2)(S F)^(-1/2) eps`.

Finally, if an additional genuine original coordinate `Z` is independent of the residual background and exact physical completion gives

`Q=d[Z+h]^2+R`, `d!=0`,

then the conditional square kernel gives

`||p_Q||_infinity <= |d|^(-1/2) sup_s E|R-s|^(-1/2)`
` <= 8 M_H^(1/4) (|d|^2 S F)^(-1/4)`.

Thus the critical `k+ell=2` projected-crossing case, which is one exponent short of direct Fourier inversion, becomes a linear one-copy small-ball bound after one physical square.  No conjugate sum/difference variables are separated.
