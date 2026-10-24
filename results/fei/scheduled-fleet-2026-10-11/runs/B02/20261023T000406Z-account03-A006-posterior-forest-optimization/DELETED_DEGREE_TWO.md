# Complete posterior cost after overlapping degree-two deletions

All costs use base-two logarithms. Let 2<=a<=b, and let H be ANY simple
bipartite graph on these two labelled sides with maximum degree at most two.
Let G=K_(a,b) minus H and f=2 OR_(ij in G)(x_i y_j)-1 on the uniform physical
cube. For G nonempty use precisely its surviving positive width-two primes,
both endpoint orders, rarity pi=1/4 and the single fixed vector lambda_e=1/b.
Let Q be the original nonempty-conditioned all-partitions reference, with
D=(1+1/(4b))^|G|-1. Every packing row holds. The complete cost satisfies

    C=sum_(A nonempty) fhat(A)^2 log2(1/Q(A)) < 42 I(f).

If a>=4 the stronger bound C<(283/8)I<36I holds. This includes all growing
deleted paths and cycles and their disjoint unions, with arbitrary side
imbalance. If G is empty, f is constant and is handled separately with zero
entropy and no nonempty reference. This is a SAME-prime complete-cost upper
bound, hence also an upper bound for the joint weight/actual-posterior
infimum containing this reference. It is not full FEI.

## 1. Actual queue mass and the root term

A010-GENERIC-WIDTH-TWO-FOREST-MASS@1 gives, for every nonempty A on incident
vertices, a distinct actual source-SCC-rooted event of mass at least
(lambda/72)^|A|/D. The whole construction and all queue factors are
reconstructed in REVIEW_A010.md; this is a lower mass bound, so it transfers
to an upper complete cost even when more actual events are included.

For A on one side, every gate owns exactly one selected vertex. All used
gates are roots, with no children. Their singleton block, root and zero-child
factors give the EXACT summed numerator

    product_(i in A) deg_G(i)/(32b).

Choices of incident gates are distinct actual root sets because different
selected vertices on one side belong to different edge gates. Each root
order is fixed. There is neither an extra factorial nor an identification
of duplicate descriptions as distinct runs. This sum legitimately retains
the posterior refund over all such choices.

Write L,R,M for the degree-weighted squared Fourier masses on left-only,
right-only and mixed nonempty sets, so I=L+R+M. If b>=4, every left degree
is at least b-2>=b/2. If also a>=4, every right degree is at least a/2.
Thus the same normalizer and weights give

    C <= v log D + (log72)I + R log(b/a) + M log b,          (1)

for a>=4. If a=2 or3 and b>=4, keep the one-sided left bound, and use the
generic event on every remaining positive-spectral set instead:

    C <= v log D + (log72)I + (R+M) log b.                 (2)

An isolated vertex has zero influence and zero spectral occurrence, so it
causes no division by its degree in (2). For b<=3 use the generic bound on
all sets: C<=v log D+(log72+log b)I.

The signed root payment applies to this SAME reference. The implicant-fiber
cube cut bound gives sum_(i in e)Inf_i>=4q/3 for every surviving edge,
where q=Pr(f=-1)>0. Multiply by lambda_e and use physical packing to get
S=sum_e lambda_e/4<=3I/(16q). Since ln D<=S and v=4q(1-q),

    v log2 D <=3(1-q)I/(4 ln2)<9I/8.                    (3)

This uses ln2>2/3, and remains valid for D<1; its negative sign has not
been replaced by an absolute value. Also log72<25/4 since72^4<2^25.

For completeness, the fiber cut bound needs only a four-vertex square.
Fix all coordinates outside a surviving edge. The vertex with both edge
bits one is positive, so there are k<=3 negative vertices in this square.
For k=0,1,2,3 the number of crossing edges is at least 0,2,2,2 respectively,
in each case at least 2k/3. The conditional sum of the two flip influences
is the crossing-edge count divided by two, at least k/3=(4/3)(k/4).
Averaging the outside coordinates proves the asserted bound, with no
monotonicity assumption beyond this positive edge being an implicant.

## 2. The exact exceptional Boolean configurations

Put u=2^-a, t=2^-b, n=a+b, and let f0 be the complete bipartite DNF.
Define E as the set of assignments with both sides nonempty but no G edge
active. Then f=f0-2*1_E exactly. For an assignment in E, its active sets
X,Y satisfy X cross Y subset H. Since every H degree is at most two,
1<=|X|,|Y|<=2. If h=|H|, w_L,w_R count its degree-two vertices on the two
sides, and c4 counts its four-cycle components, the exact number of E points is

    e = h+w_L+w_R+c4 <= (9/4)h <= (9/2)a.                (4)

The four terms count respectively (|X|,|Y|)=(1,1),(1,2),(2,1),(2,2).
Every K22 in H is an isolated four-cycle component, because all four
vertices already have degree two; distinct such components share no vertex.
Therefore w_L,w_R<=h/2 and c4<=h/4. These are counts of PHYSICAL Boolean
assignments, not arbitrary nonnegative spectral laws.

Let epsilon=e*ut and let J=sum_i Pr[1_E(x)!=1_E(x^i)]. Counting boundary
edges of E gives

    J <= 2n epsilon <=9an ut.                            (5)

The exact Dirichlet identity for delta=-2*1_E is

    sum_A |A| deltahat(A)^2 = J.                         (6)

Indeed half the coordinate difference of delta is plus/minus one on a
crossing edge and zero elsewhere. The factor two in (5) and the factor four
in delta squared must not be dropped.

For each left coordinate, the event that every other left bit is zero and
at least one surviving right neighbor is one forces that coordinate to be
pivotal. Thus for b>=4,

    I >= a 2^(1-a)(1-2^(-(b-2))) >= (3/2) a u >0.       (7)

Consequently, using n<=2b, log b<=b and b^2 2^-b<=1 for b>=4,

    J log b / I <=6n 2^-b log b <=12.                   (8)

The scalar sequence bound follows from its value one at b=4 and adjacent
ratio (b+1)^2/(2b^2)<=25/32 for b>=4.

## 3. Sector perturbations pay overlap without a quadratic deletion loss

Let R0,M0 be the corresponding Fourier sector moments for f0. Direct
expansion of f0=1-2 A_empty-2 B_empty+2 A_empty B_empty gives

    R0=2bt(1-u)^2,
    M0=2ut[a(1-t)+b(1-u)] <=2ut n.                     (9)

Let J_R,J_M be delta's degree-weighted energies in the two disjoint sectors.
The scalar inequality (r+s)^2<=2r^2+2s^2 gives

    R<=2R0+2J_R, M<=2M0+2J_M, J_R+J_M<=J.             (10)

This retains their JOINT energy budget. Two separate copies of J are
unnecessary. No independence of Fourier coefficients is assumed, and no
coefficientwise absolute sum over e exceptional points is squared.

If a>=4, put d=b-a and r=b/a. Using (7), log r<=r, and
r<=1+d/4 gives

    R0 log r / I <=(4/3)r 2^-d log r
                 <=(4/3)(1+d/4)^2 2^-d <=4/3.           (11)

For the last step the sequence at d=0 is one and its adjacent ratio is
((d+5)/(d+4))^2/2<=25/32. Also n/a<=b/2 when a,b>=4, so

    M0 log b / I <=(4/3)(n/a)t log b <=2/3.             (12)

Since 0<=log(b/a)<=log b, (8),(10)--(12) yield

    [R log(b/a)+M log b]/I <=8/3+4/3+24=28.             (13)

If a=2 or3, use log b<=b and 2^a/a<=8/3. Equations (7),(9) give

    R0 log b/I <=(4/3)(2^a/a)b^2 2^-b <=32/9,
    M0 log b/I <=(4/3)(n/a)b2^-b <=4/3,                (14)

where n/a<=b. The SAME disjoint-sector energy budget then gives

    (R+M) log b/I <=64/9+8/3+24=304/9.                 (15)

## 4. A reusable complete-cost transfer before imposing degree two

For ANY bipartite G on4<=a<=b with every left degree at least b/2 and
every right degree at least a/2, define E and its physical boundary J exactly
as above. The SAME original prime reference has the conditional transfer

    C < (91/8)I(f)+2J log2 b.                            (16)

Indeed (1),(3),(9),(10) apply without a degree bound on H. The pivotal
event now uses min left degree>=b/2>=2 to give I>=(3/2)au. Thus (11),(12)
still pay the complete-bipartite sector contribution by4I; the single joint
perturbation budget pays the remaining bill by2J log b. Adding25/4+9/8+4
gives91/8. Degree two is used only to further pay J log b by12I through the
physical count (4). This transfer is not an assertion that J log b is always
influence-paid for arbitrary dense graphs. It exposes that exact remaining
bill within one original prime table and one global reference.

## 5. Complete constants, posterior meaning, and the remaining bridge

For a>=4, (1),(3),(13) give
C<[25/4+9/8+28]I=(283/8)I<36I.
For a=2 or3,b>=4, (2),(3),(15) give
C<[25/4+9/8+304/9]I=(2963/72)I<42I.
For b<=3, the generic bound gives C<(75/8)I<42I.

All root exclusions, rarities, counts, subsets, attachment choices and labels
are included in the legal-event lower mass. The optimal posterior on actual
partition runs is q(run)/Q(A); its complete expected code length minus its
witness entropy equals -log Q(A). Thus this is a bound on the requested
complete posterior cost, not on a deterministic label cost or merely an
optimization gap. The selected mass upper-bounds the full-family cost; it
does not give a variational lower bound for a larger family.

The first unsupported universal line is the analogous influence-paid
spectral occupation budget when H has unbounded degree or for arbitrary
Boolean prime tables. The proof uses the degree-two hypothesis in the
physical exception count, the one-sided degree bounds, and the pivotal
event; it cannot simply be dropped. Cubic and growing-degree overlap need a
replacement for (4),(7),(8), rather than a reference reset or another root
normalizer estimate. Full FEI remains OPEN.
