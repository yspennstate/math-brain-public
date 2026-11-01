# Same-reference insertion and a connected compatibility correction

All logs are base2. All reference masses sum distinct actual partition-forest runs; the posterior witness entropy is retained. No descriptions of one run receive extra mass.

## General insertion inequality

Let a nonempty original table T with fixed feasible positive weights define Q0, D0. Enlarge it to T' with the same old weights and one or more new gates of fixed positive feasible weights, using original gate/order/subset/count rules, and let Q1,D1 denote the enlarged reference. Every old actual run embeds uniquely as a run with no new gate used. Root exclusions and the nonempty conditioning give exactly the same unnormalized numerator and the new denominator D1. Thus

    Q1(A)>=(D0/D1) Q0(A).

This is selected actual mass giving a full-reference COST UPPER bound; it is not a lower bound for a larger variational family. Suppose old Boolean f and new Boolean F have delta=F-f, and Q0 positive on the nonempty Fourier supports of both. Put

    E_delta(Q0)=sum_(A nonempty) deltahat(A)^2 log(1/Q0(A)).

For every theta>0, since Q0(A)<=1 and (x+y)^2<=(1+theta)x^2+(1+1/theta)y^2,

    C_F(Q1)<=(1+theta)C_f(Q0)+(1+1/theta)E_delta(Q0)
                 +v_F log(D1/D0).                         (1)

Here v_F=sum_(A nonempty) Fhat(A)^2. Weights do not depend on A. The full posterior entropy identity inf_eta[E(-log q(run))-H(eta)]=-log Q(A) remains in force on each table. This is a universal insertion inequality, conditional only on the stated support/feasibility assumptions; it does not assert universal payment of E_delta.

## A genuine connected graph

Take two disjoint K_mm components, m>=2, on left blocks L1,L2 and right blocks R1,R2. Let f be their edge OR and add one edge xy with x in L1, y in R2, obtaining connected F. Use exactly the surviving edge primes of F, both endpoint orders, pi=1/4 and lambda=1/(2m) at EVERY gate including xy. Vertex packing holds: maximum degree m+1<=2m. No table editing is performed after a Fourier set is sampled. Write t=2^-m and E0=2m^2,

    D0=(1+1/(8m))^E0-1, D1=(1+1/(8m))^(E0+1)-1.

A010 COMPONENT_FACTOR.md sections1--3 proves C_f(Q0)<71I0/8, with these exact weights. Its full component factorization and this corollary are independently reconstructed in REVIEW_SOURCES.md.

The positive change delta=F-f=2*1_Z occurs precisely when x=y=1, every R1 bit=0 and every L2 bit=0. Hence Z is an ACTUAL physical cylinder with w=2m+2 fixed coordinates and probability p=2^-w. Its coefficients have magnitude2p on every subset of those w coordinates and vanish otherwise. Therefore

    sum_A deltahat(A)^2=4p=t^2,
    sum_A |A|deltahat(A)^2=(m+1)t^2.                       (2)

## Encode the exceptional Fourier sets without a coordinatewise label loss

In block1, any relevant selected set is A subset R1 union {x}; the other block is symmetric. For a nonempty set solely on one side, the exact summed ALL-ROOT singleton numerator is64^-|A|, since every selected vertex has m distinct incident root choices, each mass lambda/32. No child is present and all root orders are fixed.

If x is selected and k>=1 right vertices are selected, choose the first selected right vertex j by a fixed coordinate ordering. Gate xj owns the two-element block {x,j}; all remaining selected right vertices own singleton blocks at independently chosen incident gates. These gates are distinct because their right endpoints are distinct. Every gate is a root with zero children; their owned blocks are disjoint, and the canonical root queue is valid even though several supports contain x. The two-element root has numerator lambda/48, and each other selected right vertex has summed numerator m lambda/32=1/64. Thus the EXACT selected-subfamily numerator is

    (lambda/48)64^(-(k-1))=(2/(3m))64^-k.                (3)

If A={x}, the one-sided singleton sum is1/64. The unique empty history has numerator1. Combining the two local subfamilies in the old global table uses its unique induced FIFO merge, not an arbitrary shuffle multiplier. For every nonempty A subset of the cylinder support W,

    Q0(A)>=64^-|A| (3m/2)^-2 / D0.

Using the exact sign of log D0 directly could sharpen this; for an upper bound simply use log D0<3m/8 (ln D0<S=m/4, ln2>2/3). Equations (2),(3) give

    E_delta(Q0)<t^2[3m/8+6(m+1)+2log(3m/2)]
                <=(91/8)m t^2,                         (4)

because m>=2 gives6(m+1)<=9m and3m/2<=2^m, the latter by induction from m=2. This pays the connector's actual Fourier perturbation; the coarse J log b is never used.

## Physical influence and the ONE normalizer

For either K_mm, q_B=2t-t^2 and I_B=4mt(1-t). Their disjoint OR has

    I0=2q_B I_B=8mt^2(1-t)(2-t).

At the cylinder Z, flipping either fixed one bit x,y creates a new boundary edge, while flipping any of the2m fixed zero bits removes an old boundary edge. All free-bit edges stay unchanged. Normalize physical undirected edges by2/2^(4m) to obtain

    I1=I0-(m-1)t^2 >=(19/2)m t^2,
    I0/I1<=21/19.                                      (5)

The inequality uses t<=1/4, so8(1-t)(2-t)>=21/2. This physical count independently fixes the sign and factor; it is not inferred from a generic perturbation norm.

Let s=1/(8m). Bernoulli gives D0>=E0s=m/4, and

    D1/D0=1+s+s/D0<=1+1/(8m)+1/(2m^2)<=1+3/16.

Thus log(D1/D0)<9/32 using ln(1+z)<=z and1/ln2<3/2. Since v_F<=I1 by Parseval, this NORMALIZER INCREMENT is <9I1/32. It is booked once and never replaced by a fresh local root payment.

Take theta=1 in (1). Equations (4),(5) and the source cost give

    C_F(Q1)/I1 < (71/4)(21/19)+(91/4)(2/19)+9/32
                =1491/76+91/38+9/32 <23.                (6)

This is a complete SAME original-prime posterior cost upper bound for every m>=2 on a connected graph of unbounded read. The old graph appears only as an analysis embedding; the final reference has all and only the connected graph's own original prime edges with one globally fixed vector.

## First unsupported universal line

For arbitrary insertions or connected overlap, no absolute influence payment for E_delta(Q0) in (1) has been established. The present cylinder has only one exceptional selected coordinate in each old component; encoding it by one double-owned root avoids paying log m per coordinate. Many interacting connectors may destroy that sparsity, and repeated use of the square inequality would also grow constants. The next target is a joint compatible-cover bound for all connector-induced cylinders, with posterior overlap and the original D retained. This is the precise remaining universal C020/PI-J obligation, not a disproof of FEI.
