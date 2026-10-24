# account02/B12 early checkpoint — rank-one tube transverse-spectrum hybrid

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

First unpaid implication after this checkpoint: in the near-rank-one physical carrier chamber, after the existing scalar-Schur retention branch and the account03/B12 r42 two-row common-plane receiver are combined, the only local tube not paid uniformly is one in which the Frobenius distance of the physical cross block to rank <=2 is `o(s2(C))`. In particular, the exact rank-two cross tube remains unpaid when `s2(C)>0`; the exact self-rank-one endpoint `s2(C)=0` was paid in the preceding account02/B12 run.

## New deterministic amplifier

Let `B` be an `m x n` real matrix with rows `r_1,...,r_m` and singular values `sigma_1>=sigma_2>=...`. For every fixed row `i`, with `h=||r_i||`,

`sum_{j!=i} ||r_i wedge r_j||^2 = h^2 ||B||_F^2 - ||B r_i^T||^2 >= h^2 sum_{k>=2} sigma_k^2.`

Proof: in a right-singular basis write `r_i=sum_k c_k v_k`. The left side equals

`sum_k c_k^2 (sum_l sigma_l^2-sigma_k^2)`,

and every parenthesis is at least `sum_{l>=2} sigma_l^2`. Hence some ORIGINAL row `j!=i` obeys

`||r_i wedge r_j|| >= h sigma_2(B)/sqrt(m-1)`.

Now write the actual final QFORM matrix on an ORIGINAL-coordinate carrier `H`, `|H|=m>=3`, as

`A=[[C,B],[B^T,D]]`

and assume `lambda_3(C^2+BB^T)>=g^2`. Write the top spectral truncation `C=lambda uu^T+E`, with `|lambda|=c=s1(C)`, `||E||op=b=s2(C)`, and assume `0<b<min(c/m,g)`. Since `C^2=c^2 uu^T+E^2`, rank-one interlacing plus Weyl gives

`g^2 <= s2(B)^2+b^2`, hence `s2(B)>=d:=sqrt(g^2-b^2)`.

Choose a literal pivot coordinate `i` with `|u_i|>=m^(-1/2)`, put `alpha=c/m-b`, `h=||B_i||`, and let

`Delta=g-b-((1+sqrt(m-1))b/alpha)h`.

The preceding account02/B12 retention theorem pays `Delta>0`. More quantitatively, for any `0<eta<g-b`, either `Delta>=eta`, or

`h > alpha(g-b-eta)/((1+sqrt(m-1))b)`.

In the latter branch the row-wedge identity forces an ORIGINAL pair `M=[B_i;B_j]` with singular product

`S_M=s1(M)s2(M)=||B_i wedge B_j||`

satisfying

`S_M >= alpha(g-b-eta)d / ((1+sqrt(m-1))sqrt(m-1)b)`.

Let

`rho_2(B)=dist_F(B,{rank<=2})=(sum_{k>=3}s_k(B)^2)^(1/2)`.

If `P_M` projects onto the row space of `M`, then `BP_M` has rank <=2, so by Eckart-Young

`F:=||B(I-P_M)||_F >= rho_2(B)`.

The account03/B12 r42 marginal-free two-row projected-crossing receiver therefore yields, whenever `rho_2(B)>0`,

`||p_Q||_infinity <= 3*2^(5/6) [ alpha(g-b-eta)d rho_2(B) / ((1+sqrt(m-1))sqrt(m-1)b) ]^(-1/3)`

in the `Delta<eta` branch. This keeps all randomness in original coordinates.

Taking `eta=(g-b)/2`, if `rho_2(B)>=theta b`, the two branches give a bound independent of `b` as `b->0`:

`||p_Q||_(infinity,ess) <= max{ 2^(13/4) binom(m-1,2)^(1/8)/sqrt(alpha(g-b)), 3*2^(5/6) [ theta alpha(g-b)sqrt(g^2-b^2)/(2(1+sqrt(m-1))sqrt(m-1)) ]^(-1/3) }.`

No small operator-norm matrix is interpreted as a uniformly small quadratic random variable; this is a final-matrix coefficient theorem.
