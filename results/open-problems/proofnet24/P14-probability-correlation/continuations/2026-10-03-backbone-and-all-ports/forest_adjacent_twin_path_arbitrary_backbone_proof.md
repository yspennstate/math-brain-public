# Adjacent twin-path edges attached to three ports of an arbitrary backbone

2 October 2026. Complete analytic proof using seven explicit positive
polynomials. This strengthens the earlier three-core adjacent theorem.
The arbitrary-backbone reduction uses elementary partition counts and
AMGM; it does not invoke matroid log-concavity or assume correlation
inequalities for the backbone. A separate independent audit is pending.
Historical novelty remains unverified.

## Theorem and exact scope

Let G be ANY finite weighted graph with arbitrary nonnegative activities
and three specified port vertices. Add three new vertices v_a,v_b,v_c.
Their spoke activities to the three ports are respectively a b_i,b b_i,
c b_i, where a,b,c>=0 and b_i>=0. Add marked edges e=v_a v_b and f=v_b v_c
with arbitrary positive activities. The new vertices have no other edges.
Then e and f are negatively correlated in the weighted forest measure.
The inequality is strict if a,c>0 and B=b_1+b_2+b_3>0. The middle row b
may be zero.

The conclusion remains true after conditioning arbitrary BACKBONE edge
indicators to states of positive conditional probability, and under
arbitrary positive fields on backbone edges and the two marked edges.
Common row or column changes of the spoke activities are already allowed.
Arbitrary independent fields on individual spokes are not asserted.
This does not establish negative association of all indicators, or a
correlation inequality for arbitrary marked positions within G. The
full forest conjecture remains unresolved by this proof.

## 1. Integrating an arbitrary backbone into five port partitions

For each backbone forest H, record which of the three ports are connected
by H. There are five possible partitions. Let v be the row of total forest
weights for these partitions. Its entries are nonnegative. All backbone
topology, vertex count, cycles, weights, and nonuniform attachment patterns
are absorbed in this row. Put F=v1>0, its ordinary forest partition sum.

Adding one new terminal with row x has exact transfer

    T(x)=d(x) I+x^2 P+x^3 Q,
    d(x)=1+Bx,
    B=b_1+b_2+b_3.

Here P joins two distinct port blocks with coefficients b_i b_j, and Q
joins three distinct port blocks with coefficient J_0=b_1b_2b_3. Two spokes
to ports already connected by H make a cycle and are rejected. Spokes to
different port blocks merge those blocks. Define

    M=vP1,
    D_sep=v_(all three ports separated),
    J=vQ1=D_sep J_0.

The operators satisfy

    P^2=2B Q,  PQ=QP=Q^2=0.                          (1)

To verify the first identity, start with three separate ports. Each first
unordered pair can be followed by either pair joining the third port.
The six ordered products sum to 2(b_1+b_2+b_3)b_1b_2b_3=2B J_0.
Starting with only two blocks, the first P join connects all ports and
the second join is zero. The other identities are immediate. Thus (1)
is an elementary connectivity identity independent of the backbone law.

## 2. Four exact marked-edge coefficients

For cluster row weights x_1,...,x_k define

    C(x_1,...,x_k)
       =F product_i d(x_i)
        +M sum_i x_i^2 product_(j!=i)d(x_j)
        +J sum_i x_i^3 product_(j!=i)d(x_j)
        +2BJ sum_(i<j)x_i^2 x_j^2 product_(l!=i,j)d(x_l). (2)

This expands v product_i T(x_i) 1 using (1). Deletion/contraction of
the marked edges gives the four coefficients in their multi-affine
partition polynomial:

    A=C(a,b,c),
    B_e=C(a+b,c),
    B_f=C(a,b+c),
    C_ef=C(a+b+c).                                    (3)

The marked two-edge path is acyclic. Its contractions sum row weights;
parallel spokes aggregate their activities exactly. Its Rayleigh
difference is therefore

    R=B_e B_f-A C_ef
      =C(a+b,c) C(a,b+c)-C(a,b,c) C(a+b+c).            (4)

The marked activity values cancel from this difference. Its sign controls
negative correlation for every positive choice of those activities.

## 3. Two elementary scalar bounds for EVERY backbone

Put e_2=b_1b_2+b_1b_3+b_2b_3. Each backbone forest permits only some
unordered two-spoke choices. Consequently

    0<=M<=e_2 F<=B^2 F/3.                            (5)

The last inequality follows from b_1^2+b_2^2+b_3^2>=e_2. Conversely every
backbone forest with all ports separated permits EVERY two-spoke choice,
so

    M>=D_sep e_2,
    BM>=B D_sep e_2>=9D_sep J_0=9J.                  (6)

Indeed B e_2 is 3J_0 plus the six symmetric monomials b_i^2 b_j. Their
sum is at least 6J_0 by AMGM. The bound extends to zero column factors
by continuity. For B>0, (5) gives B^2F-2M>=B^2F/3>0.

These inequalities hold for ANY nonnegative five-partition row v. No
log-concavity, negative correlation, or special representation of the
backbone distribution is used.

## 4. Seven positive polynomials give the adjacent Rayleigh inequality

This section proves a general scalar lemma: the expression in brackets
in (4), with C given by (2), is nonnegative whenever `F>0,B>0,M,J>=0`,
`B^2F>=2M`, and `BM>=9J`.

Normalize the rows and parameters by

    x=Ba, y=Bb, z=Bc,
    u=2M/(B^2F),  v=9J/(BM),
    s=x+z, t=xz.                                      (7)

When M=0, the second hypothesis forces J=0; set u=v=0. Otherwise both
u and v belong to [0,1]. Define the degree-two Bernstein basis

    beta_0(w)=(1-w)^2,
    beta_1(w)=2w(1-w),
    beta_2(w)=w^2.

Let R denote the bracket in (4). The exact polynomial identity is

    R=F^2 xz sum_(i,j=0)^2 beta_i(u) beta_j(v) Q_ij(s,t,y).   (8)

Here the nine Q polynomials have only seven distinct values. The following
is the complete list, grouped by powers of y. Every displayed coefficient
is nonnegative:

    Q_00=Q_01=Q_02=1+s+t.

    4 Q_10
      =2+3s+2s^2+2st
       +2y(1+s+t).

    72 Q_11
      =36+51s+34s^2+30st+2s^3+2s^2t
       +y(30+34s+4s^2+30t+4st)
       +2y^2(s+t).

    18 Q_12
      =9+12s+8s^2+6st+s^3+s^2t
       +y(6+8s+2s^2+6t+2st)
       +y^2(s+t).

    4 Q_20
      =2s+2s^2+s^3+s^2t
       +y(4+4s+2s^2+2st)
       +y^2(2+s+t).

    72 Q_21
      =30s+32s^2+17s^3+2s^4+12s^2t+2s^3t
       +y(60+68s+38s^2+6s^3+24st+6s^2t)
       +y^2(36+25s+6s^2+12t+6st)
       +y^3(4+2s+2t).

    324 Q_22
      =108s+126s^2+72s^3+15s^4+s^5+36s^2t+12s^3t+s^4t
       +y(216+288s+180s^2+48s^3+4s^4+72st+36s^2t+4s^3t)
       +y^2(162+144s+54s^2+6s^3+36t+36st+6s^2t)
       +y^3(36+24s+4s^2+12t+4st)
       +y^4(3+s+t).

For an elementary check of (8), divide each C expression by F and replace
`B a,B b,B c` by x,y,z. Each factor d becomes `1+x`, the normalized M
coefficient becomes `u/2`, and the normalized J coefficient becomes
`uv/18`. Form the four C expressions in (4) and expand their two products.
Since the result has degree at most two in each of u,v, its tensor-product
Bernstein coefficients are determined by these products. They are exactly
the seven displayed Q polynomials after the substitutions `s=x+z,t=xz`.
This is an identity of polynomials, with no inequality or numerical
approximation in the calculation.

All beta and Q factors on the right of (8) are nonnegative, proving the
scalar lemma. In the forest application (5) gives u<=2/3<1. Since
`sum_j beta_j(v)=1`, the i=0 terms alone contribute

    F^2 xz (1-u)^2 (1+s+t).

This is strictly positive when a,c>0. If B=0, all spokes vanish, the marked
two-edge path is a separate acyclic component, and its two edge indicators
are independent. If either outer row vanishes, its marked edge is a bridge
and independent; the inequality is again equality. Equations (1)-(8)
prove the theorem for all allowed cases.

## 5. Conditioning, fields, exact checks, and scope

Conditioning backbone indicators replaces v by the nonnegative row of
weights of the allowed backbone forests. Positive-probability conditioning
gives F>0. The argument permits D_sep=0, as when required present edges
connect two ports, so it does not presume three distinct ports survive a
contraction. Positive backbone fields likewise change only v. The two
marked activities do not change (4). This proves the stated closure.

The unchanged seven-polynomial identity is verified exactly, as a
polynomial in x,y,z,u,v, by
forest_adjacent_terminal_core3_bernstein_exact.py and its results JSON.
The new original-graph checker is
forest_adjacent_twin_path_arbitrary_backbone_exact.py. It enumerates the
UNCONTRACTED full graph including arbitrary backbone vertices and
non-rank-one backbone edge weights, computes all four coefficients by
union-find cycle tests, independently calculates the five backbone port
weights, and compares (2)-(4). Its report includes required present
backbone edges connecting ports, zero middle rows, and zero column
factors. These finite checks support a complete analytic proof rather
than extrapolating it to larger backbones.

The result covers a special proportional-neighborhood configuration of
the marked path, with at most three common port neighbors. It does not
cover nonproportional new-vertex spoke profiles or extra edges incident
to the three new vertices. It does not imply negative association of all
forest indicators. Historical priority and overlap with known small-
graph or series-parallel results remain unverified.
