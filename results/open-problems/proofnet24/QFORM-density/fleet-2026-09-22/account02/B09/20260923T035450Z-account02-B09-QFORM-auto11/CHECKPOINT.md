# Early substantive checkpoint — strict-N3 clique alignment cannot survive

Programme `QFORM-DENSITY-3EIG-20260922`; account02/B09; run `20260923T035450Z-account02-B09-QFORM-auto11`.


## First calculation

Consider the exact global clique-factor geometry left open by account03/B09 r22. Write the physical coordinates as `{h} union I`, with

`A_II = D + sigma u u^T`, `sigma in {+1,-1}`,

where `D` is diagonal, and let the outer-hub row be `c=A[I,h]`. Assume strict `N3(tau)`:

` s_3(A)>=1`, `|A_kk|<tau`, and `|det A[{k,l},{k,l}]|<tau` for all `k!=l`.

Put `q=sqrt(tau+tau^2)`. Then every physical edge has modulus `<q`, hence `|u_i u_j|<q` for `i!=j`.

If the mixed frame is exactly aligned, `c=gamma u`, then

`A = E + sigma z z^T`,

with `z=(sigma gamma,u)` and diagonal

`E_h=A_hh-sigma gamma^2`, `E_i=A_ii-sigma u_i^2`.

Since the update has rank one, singular-value interlacing gives

`1 <= s_3(A) <= s_2(E)`.

Thus at least two diagonal entries of `E` have modulus at least one. Two leaf entries cannot both do so when `tau<1/3`, because each would force `u_i^2>1-tau` and hence `|u_i u_j|^2>(1-tau)^2>tau+tau^2=q^2`. Therefore one large entry is the hub entry and one is a leaf entry. They imply

`gamma^2>1-tau`, `u_i^2>1-tau`,

so the physical hub-leaf edge obeys

`|c_i|^2=gamma^2u_i^2>(1-tau)^2>tau+tau^2`,

contradicting strict N3. Hence exact alignment is impossible for every `tau<1/3`.

A quantitative version is also available. Let `gamma=<u,c>/||u||^2`, `e=c-gamma u`, `delta=||e||`, and `mu=1-tau-q`. Replacing `c` by `gamma u` changes `A` by a symmetric star of operator norm `delta`. If `delta<mu`, the same rank-one argument at spectral threshold `1-delta` forces

`gamma^2 >= 1-delta-tau`, `u_i^2 >= 1-delta-tau`.

Since `|c_i|<q` and `c_i=gamma u_i+e_i`,

`1-delta-tau <= q+delta`,

so in all cases

`delta >= mu/2`.

Moreover subtracting the physical hub star (rank at most two) gives

`1=s_3(A) <= tau+||u||^2`,

because the hollow rank-one leaf operator `sigma(uu^T-diag(u_i^2))` has operator norm at most `||u||^2`. Therefore `||u||^2>=1-tau`, and the scaling-invariant mixed determinant obeys

`R=det Gram(u,c)=||u||^2 dist(c,span u)^2 >= (1-tau)mu^2/4`.

At `tau=1/128`, `mu=(127-sqrt(129))/128=0.903454557...` and

`R>=0.2024633346...`.

Thus the account03/B09 r22 remaining clique branch is not allowed to approach exact alignment; if its row leverages are diffuse, the already-completed mixed-hub theorem immediately gives a universal bound. The only exact cut-rank-one clique survivor is now row-concentrated transversality.

The final report will record the heavy-row survivor family and the exact source/partner applications.
