# Round 421 nineteenth bounded-gap pairs split into fixed-gap profiles

Round 421 decomposes the nineteenth bounded-gap prefix-pair family left by
Round 420 into a finite fixed-gap family at the same current marker depth.

Round 420 left, for every finite \(i,j\), the bounded-gap prefix-pair
contribution
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
\]
under coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The bounded-gap profile uses scale
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and finite cutoff
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\Theta_i}
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1.
\]

Let
\[
  K_i^{\rm src}=K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
denote the inherited Round 420 source scale.  Define the new fixed
successor-gap scale by
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch;{\rm fix}}
  =
  8K_i^{\rm src}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
After this replacement the scale is relabeled as
\(K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\) in the fixed-gap profiles, matching
the surrounding ladder notation.  Thus the new fixed-gap scale is the Round
420 bounded-gap scale multiplied by the finite bounded-successor budget.  The
superscript marker depth is unchanged; only the local gap resolution has been
refined.

The bounded-gap-to-fixed-gap reduction gives, for every finite \(i,j\),
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The added \(h\)-sum is finite for each fixed \(i\) and introduces no
\(p\)-dependent loss.

Substitution into the Round 420 finite ladder replaces
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
\]
by
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
is unchanged, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
\]
is unchanged from Round 418.

The adjacent nineteenth return-spread family from Round 419 remains at radius
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the nineteenth bridge-return spread family from Round 417 is retained, and
the eighteenth bridge-return and adjacent return-spread families, seventeenth
retained spread families, older retained families, enlarged spread-return
profiles, exact-level return terms, and all finite cutoffs carry forward.

The radial-tail and subdivision criteria now use the nineteenth fixed-gap
prefix-pair formulation.  The next unresolved issue is to project these
fixed-gap prefix-pair profiles to confined bridge profiles at the same marker
depth, paralleling the previous fixed-gap-to-confined-bridge reductions.
