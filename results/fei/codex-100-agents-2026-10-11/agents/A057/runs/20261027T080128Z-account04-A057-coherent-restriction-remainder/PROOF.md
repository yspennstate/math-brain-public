# A whole-core restriction ticket at rate41/20

Entropy uses bits, and the physical input is uniform. For every finite Boolean sign g and every coordinate i, put p=Inf_i(g), I=I(g), and D=H(g)-[H(g_0)+H(g_1)]/2. The result is

    0 <= D <= (41/20) I.                                      (1)

This is a whole-core bound. It is not D<=(41/20)p, and it does not pay an unlimited number of queries by renewing the same owner.

## 1. An exact finite certificate for a dimension-independent boundary bound

Let d(x,Z) be the distance to the nearest integer and define the continuous piecewise affine function

    T(s)=sum_{k=0}^3 2^(-k) d(2^k s,Z),  0<=s<=1.

The key inequality is

    T((a+b)/2) <= [T(a)+T(b)+|a-b|]/2.                         (2)

Here is a complete finite rational certificate for all real a,b in[0,1]. The affine partition is cut by a=k/16, b=k/16, a+b=2k/16, and a=b, with integers0<=k<=16. Every vertex of the partition has both coordinates on the16-grid: this follows directly by intersecting each pair of these lines, including the diagonal. Thus its entire vertex set is exactly the289 grid pairs. On each closed cell the difference in(2) is affine. BOUNDARY_VERTICES.json supplies all289 nonnegative rational differences, independently reproduced in audit.py by an integer residue formula. An affine function on a compact polygon attains its minimum at a vertex. Therefore(2) holds everywhere, not merely on a grid. No untested continuum interval is left.

For a Boolean sign u with density s=Pr[u=-1], cube slicing gives

    I(u)/2 >= T(s).                                          (3)

Induct on dimension. Constants give zero on both sides. Let a,b be the two slice densities; let r be the fraction where the two slices differ. Then r>=|a-b|, while I(u)/2 is the average of the two slice half-influences plus r/2. Apply the inductive inequalities and(2). This proves(3) for every dimension using only the fixed finite certificate. All65536 four-variable signs verify(3); the minimum for each possible density agrees exactly with T on that grid. These finite checks are an audit of normalization, not the dimension induction itself.

The tempting shorter tent beta(s)=min(2min(s,1-s),max(s,1-s)) is NOT a valid slicing subsolution. At a=1/2,b=1/6 its difference in(2) would be-1/12. FAILED_TENT.json and FAILED_DRAFT.md preserve that rejected step. No conclusion here uses it, nor is optimality of T or rate41/20 asserted.

## 2. Apply the boundary to an actual physical derivative

Set u=g_0 g_1. It is negative on fraction p. A change of u requires a change of at least one child, so

    I(u) <= I(g_0)+I(g_1)=2(I-p).

Consequently I>=p+T(p). The ordinary cube edge-isoperimetric inequality also gives I>=p+delta log2(1/delta), delta=min(p,1-p), with0log(1/0)=0. These apply to arbitrary output bias. They do not extend here to a biased physical input measure.

The exact Fourier erasure identity and amplitude-pair Jensen-Shannon estimate, reconstructed in A091 PROOF Section1, give

    0<=D<=h2(p)+min(1,2delta/ln2).                            (4)

This input concerns both full child spectra; there is no terminal substitution.

## 3. A rational certificate of the entropy comparison

Write C=41/20. When p>=1/2, the ordinary isoperimetric bound and log2(1/delta)>=1 give I>=p+delta=1, and(4) gives D<=2<C I. This includes delta=0 and p=1. When p=0, the children agree, so D=0.

For0<p<=1/8, set

    F(p)=C p(1+log2(1/p))-h2(p)-2p/ln2.

It is continuous at0, with F(0)=0, and

    F''(p)=[1/(1-p)-(C-1)/p]/ln2<0.

Indeed p<=1/8 and C-1=21/20>1. The exact rational logarithm certificate gives F(1/8)>0. Concavity then gives F(p)>=0 on the entire interval. Divide only when p>0; the endpoint uses the elementary limit p log(1/p)->0. This proves(1) in this range.

It remains to certify1/8<=p<=1/2. Subdivide into the384 intervals[j/1024,(j+1)/1024],128<=j<=511. Every breakpoint k/16 of T is a subdivision endpoint, so p+T(p) is affine on every cell. Put m=(2j+1)/2048. The binary entropy tangent bound is

    h2(p)<=-p log2(m)-(1-p)log2(1-m).

ENTROPY_CELLS.json records outward lower enclosures of both logarithms. Their negatives therefore give an affine U_j(p) above this cross-entropy, hence above h2(p). On each cell the checker chooses either J_j(p)=2p/L or J_j(p)=1, where L is a proved positive lower bound for ln2. Both choices upper-bound the JS part of(4). It then verifies at BOTH endpoints that

    C[p+T(p)]-U_j(p)-J_j(p)>=0.

That difference is affine, so the endpoint certificates prove the inequality on the ENTIRE cell. There is no numerical sampling argument. The384 exact endpoint certificates cover the remaining interval completely. Together with Section2 they prove(1).

Logarithms are enclosed by scaling their argument into[1,2] and using

    ln y=2 sum_{k=0}^{69} z^(2k+1)/(2k+1)+remainder,
    z=(y-1)/(y+1),  0<=remainder<=2z^141/[141(1-z^2)].

All evaluations are Fraction arithmetic. Outward192-bit rounding is applied to log2 intervals, and ln2 is positive. Signs and divisions are checked explicitly; no floating sign supplies a premise. The initial pilot hit Python's integer-string limit when serializing a huge exact NAND expression; outward rounding fixed representation size without changing the domain or weakening a sign. PILOT_ERRATUM.md records this separately from the false tent.

## 4. Spend the SAME original owner only once

In A059's established coherent interface, let t be the actual current core density. Preallocate TWO labelled C t I(g) tickets plus(2/5)t I(g) reserve, since

    9/2 = 2(41/20)+2/5.

This split is made BEFORE expenditure. Through an already-paid core query, each pending ticket transports to C t I(g_a) in child a and releases C t p; the conditional average is its parent principal. At a selected new query consume exactly one pending ticket to pay tD<=C t I, retaining its nonnegative surplus, and close it. The second ticket is separately transported and later consumed. Expected-resource branch innovations remain explicit, and full child profiles remain literal. No previously consumed ticket is recreated. Compared with A059's two29/13 tickets, the same original owner now retains reserve2/5 instead of1/26. This improvement comes from(1), not a change of source budget.

The same substitution improves A091's actual-fee continuation. For ANY supplied original rate A>=C and remaining influence J=I-p>0, its exact formula q*=min(1,(AI-D)/(AJ)) remains valid. At A=9/2 it now guarantees q*>=1-C/A=49/90, versus the earlier59/117. The rule q*=1 iff D<=Ap is unchanged; it remains a condition, not a universal assertion. Fresh independent physical dyadic continuation q=17/32 is uniformly affordable with pending rate C/(1-q)=328/75, leaving19/150 of original rate9/2 unused. The same fixed-q law still retains extensive terminal entropy, as A060 proved. J=0 ends at constant children without dividing. Zero density has zero fee and zero principal.

Every already-booked exterior fee and exact coherent source profile remains as in the imported interface. In particular the alpha^2 log(1/alpha^2) contribution remains literal; it is not replaced by O(alpha^2), bounded a second time, or counted as fresh cash. This result changes only the core ticket price.

## 5. Source obstruction and the precise open line

The independent checker reconstructs A091's NAND depth5 mean, influence and entropy with a separately simplified recurrence. If m,H,I are a NAND subtree's data and v=1-m^2, a=(1+m)/2, then the next entropy is

    eta(((1-2m-m^2)/2)^2)+(1+m)[H-eta(m^2)]
      +2v eta(a^2)+v^2/2,

where eta(x)=-xlog2(x). The next mean is(1-2m-m^2)/2 and influence is(1+m)I. The entropy coefficient1+m follows by grouping A091's disjoint Fourier sectors:2a^2+v/2=1+m. At depth5, the independently computed intervals overlap A091's saved intervals, exact means/influences agree, and H-(9/2)I>1/10 is certified. Its2048-copy tagged wrapper therefore exceeds its generously enlarged complete budget by>883/160. The certificate independently HOLDS at that finite Boolean scope. It rules out universal full completion at fixed rate9/2, not the two-query result or FEI.

First unpaid line: provide a sufficiently large dimension-independent ORIGINAL arbitrary-core resource and a necessary continuation whose complete expected terminal entropy decays within that resource, with all old fees and both full terminals retained. Lowering the ticket price does not price the stopped child's entropy. Full FEI remains OPEN. The analytic theorem and its exact certificates await independent review by A091 or A087/A094. Formal receipts concern only their named finite vertex statement, if verified; they do not certify the entropy argument or all-dimensional translation.
