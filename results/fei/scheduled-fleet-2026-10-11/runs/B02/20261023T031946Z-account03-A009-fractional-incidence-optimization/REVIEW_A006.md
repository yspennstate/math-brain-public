# Independent reconstruction: A006 degree-two complete cost, version1

Reviewer A009; no substantive repair supplied. Verdict HOLDS for the ENTIRE
stated version, including the conditional half-density transfer. This is a
local review receipt; shared registry adoption remains B20's action.

Source: A006-DELETED-DEGREE-TWO-COMPLETE-POSTERIOR-COST@1,
statement SHA256 b7dcb04baef45b89177ea1012a9c5cfc5ca81f3525ff510b637dc7dbe25752c2.
Read DELETED_DEGREE_TWO.md and CLAIMS.json in A006's
20261023T000406Z-account03-A006-posterior-forest-optimization run. Reconstructed
the underlying A010-GENERIC-WIDTH-TWO-FOREST-MASS@1 from its original
GROWING_MATCHING.md, rather than relying on A006's review verdict.

## Queue factors reconstructed in a different representation

Assign each selected physical coordinate to an incident edge, merging coordinates
assigned to the same edge into an owned block. These blocks partition the output;
N used gates satisfy N<=|A| and have sizes s in{1,2}. Make an arc from a gate
to another when its owned block intersects the other's edge. Root one vertex in
each source strongly connected component; a multi-source search reaches all
gates. Choosing the first discovered incoming arc makes a directed forest.
Its attachment is a coordinate in the parent's owned block. Order children by
attachment slot, then edge index, yielding one original legal queue history.
Every owned block has an endpoint order with theta=1. For R roots and c children
at each gate the ORIGINAL numerator, before dividing by D, is exactly

 lambda^N 4^-R product_g
 [s(s+1) binom(2,s) (c+1)(c+2) binom(s+c-1,c)]^-1.

The subset denominator is4 or6. The weak composition denominator is at most
c+1. The elementary inequality (c+1)^2(c+2)<=2*6^c follows at c=0,1 directly
and thereafter by the adjacent ratio<6. Thus the product denominator is at
most12^N 6^(N-R), since sum c=N-R. The numerator is at least
(lambda/72)^N(3/2)^R >=(lambda/72)^|A| for0<lambda<=1.
The independent implementation uses transitive closure for SCCs and breadth
first discovery, then recomputes these exact factors for every selected set in
every small labelled graph. It checks17,951 actual legal forests, not just the
final scalar expression. This independently accepts the generic mass premise.

For a one-sided selected set, choose one incident gate per selected coordinate,
all as roots, all zero-child singleton blocks. Different choices are different
root sets; one edge cannot serve two selected coordinates on that same side.
Summing produces exactly product deg_G(i)/(32b), with no factorial or repeated
description. In all cases root absence and nonempty conditioning are the SAME
D=(1+1/(4b))^|G|-1. Dividing a selected event sum by D lower-bounds Q(A), so
its negative logarithm upper-bounds the complete posterior cost.

## Root and sector transfer, including signs

On any surviving edge's four-point fiber at most three vertices are negative.
For k negative vertices the crossing-edge count is at least2k/3. Conditional
sum of its two flip probabilities is half this count, hence at least k/3.
Averaging gives sum of the two physical influences>=4q/3. Packing implies
S=sum_e lambda_e/4<=3I/(16q). For v=4q(1-q), log D<=S/ln2 gives
v log D<9I/8, using ln2>2/3. This does not require log D to be positive.
The inequality ln2>2/3 follows by integrating1/x on[1,2], or the positive
atanh expansion ln2=2(1/3+1/(3^3*3)+...). Also log72<25/4 because72^4<2^25.

With u=2^-a,t=2^-b, complete-graph right-only and mixed degree moments are
R0=2bt(1-u)^2 and M0=2ut[a(1-t)+b(1-u)]. These follow by expanding the two
empty-side indicators. The actual perturbation is delta=-2*1_E. Its Dirichlet
energy is J, the physical flip influence of1_E, including its factor two per
undirected boundary edge. On the two DISJOINT sectors, (r+s)^2<=2r^2+2s^2
gives R<=2R0+2J_R and M<=2M0+2J_M with J_R+J_M<=J. One budget is used.

Under half-density and a>=4, sole-left activation gives I>=3au/2. Put h=b-a.
R0 log(b/a)/I <=(4/3)(1+h/4)^2 2^-h<=4/3; the adjacent ratio is<=25/32.
Also n/a<=b/2 and b^2 2^-b<=1 give M0 log b/I<=2/3.
The one-sided and generic event masses therefore bound C by
v log D+(log72)I+R log(b/a)+M log b
< (91/8)I+2J log b. This proves the entire general transfer clause.

## Entire degree-two conclusion and endpoints

If maxdeg H<=2, active exceptional sets have sizes1or2 on each side. Their
four exact counts are h,w_L,w_R,c4. Degree-two vertices on each side number
at most h/2; any K22 is an isolated four-cycle, so c4<=h/4. Therefore
e<=9h/4<=9a/2 and J<=9an2^(-a-b). For b>=4, surviving left degree>=b-2
implies I>=3a2^-a/2. Since n<=2b, log b<=b and b^2 2^-b<=1,
J log b/I<=12. For a>=4 the transfer gives C<(91/8+24)I=283I/8.

For a=2or3,b>=4 use the left-only sum and generic forests elsewhere:
C<=v log D+(log72)I+(R+M)log b. Here R0 log b/I<=32/9, since2^a/a<=8/3;
M0 log b/I<=4/3, since n/a<=b. Thus (R+M)log b/I<=304/9 and
C<(25/4+9/8+304/9)I=2963I/72<42I. If b<=3, use the generic forest on
all nonzero output sets: log b<2 yields C<75I/8. Isolated vertices never
occur spectrally; the empty G endpoint is constant and needs no reference.
The posterior identity is the exact cancellation of run entropy against
the conditional law q(run)/Q(A); no new law is optimized after A is seen.

## Validation scope and remaining limitation

The pilot independently checks all330 labelled max-degree-two deletion graphs
on2<=a<=b<=3, including the constant case, with integer Walsh transforms and
direct physical flips. Full execution also checks larger declared fixtures.
The proof above handles every dimension; enumeration is an audit, not the
finite-to-infinite bridge. No material amendment to the source was needed.
This acceptance says nothing about whether J log b is paid for arbitrary
half-dense G; the new obstruction explicitly shows it is not.
