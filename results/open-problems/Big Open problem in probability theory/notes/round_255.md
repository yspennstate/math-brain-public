# Round 255

Round 255 repackages the fixed-gap prefix-pair residual as a confined
fixed-gap bridge residual.

For a fixed-gap pair at levels \(u\) and \(u+h\), with lower witness
\([a,b]\) and upper witness \([a',b']\), lower persistence gives
\(d(x,v_t)>u\) for \(b<t<a'\).  The upper witness is record at level \(u+h\),
and graph distance changes by at most one along the path, so the connector
cannot pass above \(u+h\) before first visiting \(u+h\).  Thus
\[
  u<d(x,v_t)<u+h
  \qquad(b<t<a').
\]
Consequently,
\[
  P^{\rm pre,gap,sh}_{j,K,L,h}
  \le
  P^{\rm pre,br,sh}_{j,K,L,h}.
\]

When \(h=1\), the confinement interval contains no integer radial level, so
the upper record run starts immediately after the lower run exits upward:
\(a'=b+1\).

In the finite ladder, the live residual is now
\[
  P^{\rm pre,br,sh}_{i,j,h}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_iB_i,L_i,h}^{
    G\to H,{\rm rad,tan,pre,out,per,bridge,short}},
  \qquad 1\le h\le B_i.
\]

Round 255 did not refresh the external open-status search.  It keeps the
Round 254 external assessment and only changes the internal conditional
endpoint.
