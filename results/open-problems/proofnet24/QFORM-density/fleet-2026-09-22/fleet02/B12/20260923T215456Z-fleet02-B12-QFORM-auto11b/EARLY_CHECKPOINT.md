# fleet02/B12 early checkpoint — rank-one-self retention inside the rank-two common-plane tube

Status: substantive derivation in progress; full QFORM remains OPEN.

The incoming completed partner theorem is fleet03/B12 r42, `QFORM-THREE-MODE-HUB-PAIR-OR-R2-TUBE-v1`, canonical bundle `9f2faf96ddefc42383b5ea509451b4e667798629`. Its only surviving branch is a quantitatively nondegenerate rank-two common cross plane with arbitrarily small transverse Frobenius residual. I attack the endpoint from the nearly-rank-one self side.

Let `H` be an ORIGINAL-coordinate set, `|H|=m>=3`, write `C=A[H,H]`, `B=A[H,H^c]`, and assume

`lambda_3(C^2+B B^T)>=g^2`.

Write the top absolute-eigenvalue decomposition

`C=lambda u u^T+E`, `||E||op=b=s_2(C)`, `|lambda|=s_1(C)>=c`,

and assume `c>m b`. Choose a literal coordinate `i` with `|u_i|>=m^{-1/2}`, put `K=H\{i}`, `a=C_ii`, `r=C[K,i]`, `h=||B[i,H^c]||_2`, and

`alpha=c/m-b>0`.

Then `|a|>=alpha`. Define the actual scalar-Schur cross block

`B#=B[K,H^c]-(r/a)B[i,H^c]`.

The new deterministic estimate is

`boxed: s_2(B#) >= Delta_new := g-b-(sqrt(2m)b/alpha) h.`

Proof skeleton:

1. Put `W=[C,B]`. Since `W W^T=C^2+B B^T`, `s_3(W)>=g`.
2. Put `W0=[lambda u u^T,B]`. Singular-value Weyl gives `s_3(W0)>=g-b`.
3. Compress `W0 W0^T=lambda^2 u u^T+B B^T` to `u^perp`. Cauchy interlacing yields
   `s_2((I-u u^T)B)>=g-b`.
4. Define the physical coordinate quotient map `T_i z=z_K-(u_K/u_i)z_i`. Its kernel is `span{u}` and
   `T_i T_i^T=I+u_Ku_K^T/u_i^2`, so the least nonzero singular value of `T_i` is exactly one. Hence
   `s_2(T_iB)>=g-b`.
5. The actual Schur coefficient satisfies
   `r/a-u_K/u_i=(u_i E[K,i]-E_ii u_K)/(a u_i)`, so
   `||r/a-u_K/u_i|| <= sqrt(2m)b/alpha`.
   Therefore `B#=T_iB-(r/a-u_K/u_i)B_i`, and Weyl gives the boxed estimate.

If `Delta_new>0`, the completed fleet03/B12 r41 scalar-square/rank-two-cross receiver applies exactly to the actual ORIGINAL-coordinate Schur residual and gives

`||p_(X^T A X)||_(infinity,ess) <= 2^(11/4) binom(m-1,2)^(1/8) / sqrt(alpha Delta_new)`.

In particular, at the exact rank-one endpoint `b=0`, one has `Delta_new=g` independently of the size of the pivot cross row. Thus the exact rank-one-self / exact-or-near-rank-two-common-plane endpoint is already paid; any remaining partner-r42 tube survivor must have `b>0` and, if this new exit fails,

`h >= alpha(g-b)/(sqrt(2m)b)`,

so the physical hub norm must diverge at least like `1/b` as the self block approaches rank one.

This argument is deterministic on the final matrix. It neither removes a small dense tail from the random quadratic form nor rotates the product inputs.
