# Rigor check — account03/B15 auto34

Claim checked: `QFORM-OPNORM-RANKCOLLAPSE-TV-HEIGHT-BARRIER-v1`.

1. **Target-valid matrices.**  
`A_0=diag(1,1,1,0)` has eigenvalues `1,1,1,0`.  
`A_e=diag(1,1,1,e)` with `0<e<1` has eigenvalues `1,1,1,e`.  
Both satisfy the owner hypothesis; `||A_e-A_0||_op=e` exactly.

2. **Common product law.**  
`X_1,X_2,X_3~Unif[-1/2,1/2]`, `X_4~Unif[R,R+1]`, mutually independent. Every marginal density equals one on a unit interval and zero elsewhere, hence is an admissible cap-one probability density. The *same* four-dimensional law is used for both matrices.

3. **Base support and height lower bound.**  
`S=sum_{i=1}^3 X_i^2` is supported in `[0,3/4]`. Since its density has total mass one on a set of Lebesgue length at most `3/4`, every density representative has essential supremum at least `4/3`.

4. **Perturbing-variable density.**  
For `Y=eX_4^2`, with `R>0`, the map `x->ex^2` is strictly increasing on `[R,R+1]`; its inverse derivative is
`dx/dy=1/(2e x)=1/(2 sqrt(e y))`.
Thus
`g_Y(y)=1/(2 sqrt(e y)) 1_[eR^2,e(R+1)^2](y)`
and `||g_Y||_infinity=1/(2eR)`. Taking `R=L/(2e)` gives exactly `||g_Y||_infinity=1/L`.

5. **Interval bound.**  
`Q_e=S+Y`, with `S independent of Y`. For any interval `I`,
`P(S+Y in I)=E[P(Y in I-S | S)]<=|I|/L`.
No pointwise version of the density of `S` is used here.

6. **Partner application.**  
Account04/B15 r8 Theorem 6.1 applies because `rank(A_e)=4>=3`. The interval bound in item 5 therefore yields a canonical `p_e in C_0(R)` with `||p_e||_infinity<=1/L` and no constant loss. Likewise the diagonal `pi` interval bound for `A_0` plus `rank(A_0)=3` gives canonical `p_0 in C_0`.

7. **Translation-robust TV lower bound.**  
Let `E=[0,3/4]`. For every `c`, the translated law `tau_c mu_e` has the same density cap `1/L`, so `(tau_c mu_e)(E)<=3/(4L)`. Since `mu_0(E)=1`, under the convention `d_TV(mu,nu)=sup_B |mu(B)-nu(B)|`,
`d_TV(mu_0,tau_c mu_e)>=1-3/(4L)`.
Taking `L>=3/(4eta)` gives `>=1-eta`.

8. **Density-height gap.**  
The same choice yields `||p_e||_infinity<=1/L<=4eta/3`, while `||p_0||_infinity>=4/3`, so
`||p_0||_infinity-||p_e||_infinity >= (4/3)(1-eta)`.
No claim is made that `p_0-p_e` is positive pointwise.

9. **Affine amplification identity.**  
With `X_4=R+U`,
`eX_4^2=eR^2+2eRU+eU^2=eR^2+LU+eU^2` because `2eR=L`. This verifies that small quadratic curvature can generate an arbitrarily large random affine scale under remote cap-one supports.

10. **Numerical check quoted in the report.**  
For `eta=0.01`, `L=75`, `e=10^-6`, `R=L/(2e)=37,500,000`; `3/(4L)=0.01`; `1/L=0.013333333333...`; hence the stated TV and density-height inequalities follow.

Boundary: this is a regularity/stability obstruction, not a QFORM counterexample. The full universal upper bound remains open.
