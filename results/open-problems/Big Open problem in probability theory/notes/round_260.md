# Round 260

Round 260 refines the fixed-gap locally short staircase-pair residual.

For a fixed-gap pair of locally short two-level staircases:

\[
  h=1
\]
forces the upper staircase's lower run to be the same record run as the lower
staircase's upper run.  Thus the witness is a three-level locally short
outward staircase chain.

\[
  h=2
\]
forces the upper staircase's lower run to begin immediately after the lower
staircase's upper run exits outward.  Thus the witness is a four-level locally
short outward staircase chain.

For
\[
  h\ge3,
\]
the connector between the two staircases is confined:
\[
  u+1<d(x,v_t)<u+h
  \qquad(b'<t<c),
\]
where \([b+1,b']\) is the upper run of the lower staircase and \([c,d]\) is
the lower run of the upper staircase.

The live residual is now
\[
  P^{\rm pre,stair,loc,chain,sh}_{i,j,q}
  \quad(q=3,4),
  \qquad
  P^{\rm pre,stair,loc,brdg,sh}_{i,j,h}
  \quad(3\le h\le C_i),
\]
plus the previous confined fixed-gap bridge, terminal far-tail, long-run,
enlarged spread-return, ordinary exact-level return, finite-defect, and
near-tail terms.

No external open-status search was refreshed in this round.
