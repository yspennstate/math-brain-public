# fleet02/B08 r35 early substantive calculation

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains open.

## Row-aware balanced cut

Let `U in R^{n x 3}` have orthonormal columns and assume

`mu := max_i ||U_{i,*}||_2^2 <= 1/48`.

Fix an ORIGINAL physical coordinate `k` and a deterministic row vector `a=(a_j)_{j!=k}`; in the QFORM application `a_j=A_{kj}`. Put `R^2=sum_{j!=k} a_j^2`.

Choose independent Bernoulli `delta_i in {0,1}` with mean `1/2`, set `S={i:delta_i=1}`, `T=S^c`, and

`G_S=U_S^T U_S`.

Because `E G_S=I_3/2`, independence and centering give

`E ||G_S-I_3/2||_F^2
 = (1/4) sum_i ||u_i u_i^T||_F^2
 = (1/4) sum_i ||u_i||^4
 <= (mu/4) sum_i ||u_i||^2
 = 3 mu/4 <= 1/64.`

Hence Markov gives

`P( ||G_S-I_3/2||_op > 1/5 )
 <= P( ||G_S-I_3/2||_F > 1/5 )
 <= 25/64.`

Thus with probability at least `39/64`, both physical-side Gramians satisfy

`G_S,G_T=I_3-G_S >= 3I_3/10`.

Now let

`Z=sum_{j!=k} a_j^2 1_{delta_j != delta_k}`.

Conditioning on `delta_k`, each other coordinate lies across the cut with probability `1/2`, so `E Z=R^2/2`, while always `0<=Z<=R^2`. If `p=P(Z>=R^2/6)`, then

`R^2/2 = E Z <= p R^2 +(1-p)R^2/6`,

so `p>=2/5`. Consequently

`P( balanced and Z>=R^2/6 ) >= 39/64+2/5-1 = 3/320 >0`.

Therefore there is one literal original-coordinate cut for which simultaneously

`G_S,G_T >= 3I_3/10`

and, after swapping side labels if necessary so `k in S`,

`||A[k,T]||_2 >= ||A[k,-k]||_2/sqrt(6)`.

This is the missing deterministic compatibility between the diffuse spectral cut and a pre-existing localized OFF-DIAGONAL row witness. A purely scalar witness `|A_kk|` is intentionally not forced into the crossing.

## Immediate spectral consequence

Let `A_3=U Lambda U^T` with `min_j |lambda_j|>=L`. On the cut above,

`B_0=A_3[S,T]=U_S Lambda U_T^T`

has

`s_3(B_0)>= (3/10)L`.

Using the already completed marginal-free physical third-compound receiver

`||p_Q||_infinity <= 6^(4/3) e_3(BB^T)^(-1/6)` for `B=A[S,T]`,

and the retained benchmark `C_*=197.7780678260685`, put

`theta=6^(4/3)/C_*=0.05512604949999305`.

If the `C_*/L` payment fails then

`e_3(BB^T)^(1/6)<theta L`, hence `s_3(B)<theta L` and

`||(A-A_3)[S,T]||_op > (3/10-theta)L
 =0.24487395050000695 L`.

This gives a row-aware version of the r34 rank-two cancellation tube. The remaining calculation is to delete the row `k` and combine the newest fleet03/B08 exterior-algebra star inequality with the reduced top-three Gram.
