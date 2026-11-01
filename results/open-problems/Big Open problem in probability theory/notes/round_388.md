# Round 388

Round 388 absorbs the fourteenth inward-free bridge profiles from Round 387
into prefix-record profiles, while retaining the new fourteenth bridge-return
spread family.

Round 387 left the inward-free profiles
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
\]
and bridge-return profiles
\[
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}
\]
over the finite height range
\[
  1\le h\le
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Applying the inward-free bridge chain/long-run split and then the locally
short staircase-chain-to-prefix-record reduction gives a prefix-record
profile
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The profile uses threshold
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
so its superscript carries fourteen \({\rm recbr}\) markers.

The old carried coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
is multiplied by the finite height budget to define
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The long-run coefficient is updated by adding this new coefficient:
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  \leftarrow
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  +
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]

The finite-ladder, radial-tail, and subdivision criteria now use the
fourteenth prefix-record profiles and retain the fourteenth bridge-return
spread profiles, adjacent fourteenth return-spread family, thirteenth
bridge-return spread profiles, adjacent thirteenth return-spread family, and
older retained spread families.  The next internal move is to split the
fourteenth prefix-record profiles into persistent-prefix profiles and
the next adjacent return-spread terms, paralleling the previous prefix-record
split.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
