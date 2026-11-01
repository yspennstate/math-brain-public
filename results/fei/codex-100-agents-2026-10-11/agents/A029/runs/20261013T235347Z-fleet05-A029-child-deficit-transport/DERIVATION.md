# Priority bent-carrier transport with an owned terminal seed

Let g be any Boolean sign on m>=1 fair bits, p=2^-m, and
F_g(x,y)=(-1)^(x dot y)g(y). Fourier summation gives
Fhat(A,B)=2^-m g(A)(-1)^(A dot B), so H(F)=2m, I(F)=m, r1(F)=4.
Use the stage-2 definition of D_K=KI-H and the established B06 R2.

Define a PRIORITY PHYSICAL TREE: query x_1,x_2,... until the first 1
occurs, say at i. Then query y_1,...,y_i and stop. If all x are 0,
stop at g without querying any y. No coordinate is queried twice on
any physical path. Every off-seed terminal is a paired carrier on
m-i remaining pairs, with an actual restricted seed g; its spectrum
is flat and H=2(m-i), I=m-i. Previously fixed pairs contribute only
a global output sign. These terminal statements are proved, not an
assumed FEI induction hypothesis. The one seed leaf has weight p.

The first-1 event has probability 2^-i. The exact sum
sum_{i=1}^m 2^-i(m-i)=m-2+2p gives

  E I(leaf)=m-2+2p+p I(g),
  E H(leaf)=2(m-2+2p)+p H(g),
  Pi_I=2-p(2+I(g)), Pi_H=4-p(4+H(g)).

Pi_I>0: the actual first query has influence1/2, or directly use
I(g)<=m in the formula. The priority paid ratio is

  Pi_H/Pi_I=2-p[H(g)-2I(g)]/[2-p(2+I(g))].

For EVERY real K, retain both terms with their signs:

  E D_K(leaf)=(K-2)(m-2+2p)+p D_K(g),
  K Pi_I-Pi_H=2(K-2)-p[2(K-2)+D_K(g)].

Their sum is exactly (K-2)m=D_K(F). At K=2 the query credit is
-p D_2(g), and the sole seed deficit is p D_2(g). A negative seed
cannot be omitted, called free slack, or reused as descendant credit.

This is an arbitrary-seed priority interface, not an entropy estimate
requiring g to be already FEI-certified. It shows that the apparent
gain above2 is exactly terminal debt conversion. If H(g)>2I(g), it
breaks the unrestricted gain<=2 helper, even though F itself has H/I=2.

For g=-1 iff y=000, H(g)=4-(9/8)log2 3 and I(g)=3/4. A smaller
MAXIMUM-DEPTH-FOUR TREE (binary labels; variable indices here 1-based):
query x1. If x1=1, query y1 and stop. If x1=0, query x2.
If x2=1, query y2; stop at y2=1, and at y2=0 query y1 then stop.
If x2=0, query x3; stop at x3=0, and at x3=1 query y3 then stop.
It has seven internal nodes and eight leaves. The leaves are one
g leaf of weight1/8, two bent four-bit leaves of weight1/4 each,
four bent two-bit leaves of total weight5/16, and one constant of
weight1/16. All other leaves have D2=0.

  E I(leaf)=45/32, E H(leaf)=21/8+H(g)/8,
  Pi_I=51/32, Pi_H=23/8+(9/64)log2 3,
  Pi_H/Pi_I=(184+9log2 3)/102.

Thus r1-r_all >= (224-9log2 3)/102 > 524/255 > 2.05,
using only 3^5<2^8. This is an attained ratio, not a claim that this
tree globally minimizes the ratio. All actual terminal entropy remains.
The primary stage-2 finite DP certifies no negative expected D2 cut
through depth3 for this witness and a negative cut at depth4; the
new exact checker reconstructs the compact depth4 tree.

For disjoint t-fold tensors of this six-variable bent root, run this
tree only in one factor. Other factors contribute the same root and
terminal H and I and cancel from Pi_H,Pi_I. They have D2=0, so the
same helper violation holds uniformly in dimensions6t, with H/I=2.

Depth-two gain exactly2 survives for every paired carrier and every
seed, by the stage-2 unmatched-pair restriction proof. Quadratic bent
roots also have arbitrary-tree gain2. The lead's all-bent parenthetical
must be restricted to quadratic bent functions if "best tree" has
arbitrary depth. There is no correction to the finite n<=4 claim.
