# Round 257

Round 257 repackages adjacent stacked prefix pairs as two-level outward
staircases.

An adjacent stack has a lower record run \([a,b]\) at level \(u\) and an
upper record run \([a',b']\) at level \(u+1\).  Round 256 forced
\(a'=b+1\), so the two runs and the intervening upward edge form one outward
staircase segment.  If both runs are \(L\)-short, then
\[
  b'-a=(b-a)+1+(b'-a')\le 2L+1.
\]
Thus
\[
  P^{\rm pre,adj,sh}_{j,K,L}
  \le
  P^{\rm pre,stair,sh}_{j,K,2L+1}.
\]

The finite ladder now uses
\[
  P^{\rm pre,stair,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_iB_i,2L_i+1}^{
    G\to H,{\rm rad,tan,pre,out,per,stair,short}},
\]
together with the confined fixed-gap bridge profiles for \(2\le h\le B_i\).

No external open-status search was refreshed in this round.
