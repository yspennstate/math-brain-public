# The fiber criterion selects a singleton

All entropies are in bits. Let n>=2, let g=1_U have mass p>0 on
the uniform physical cube, and put f=1-2g. Let L label the actual
connected component of X, where X is uniform on U. Write d_i=Inf_i(f),
I_A=sum_{i in A}d_i, and r=|A|. Original labels are retained in every
fiber; they are not recomputed after restriction. Define

    W_A = sum_l E_y m_ly log2(1/m_ly),
    m_ly = 2^(-r) |{x_A:(x_A,y) is in component l}|.

The previous stage proves payment at C=4+a, where
a=2/ln(2)+4/(e ln(2)), when W_A>=rp/2. That theorem remains valid.
Its existential admission condition has the following exact scope:

    max_{empty != A proper} W_A/(|A|p)
       = max_i d_i/(2p).                                      (1)

Thus some paid fiber block exists if and only if max_i d_i>=p.
Overlap credit can improve a prescribed block, but cannot enlarge this
existential admission class beyond a high-influence singleton.

## Proof of the exact admission identity

The physical fiber chain rule gives

    W_A=p[r-H(X_A|X_Ac,L)].                                   (2)

For every i, conditional on X_-i and L, a nonempty fiber has one or
two points. A two-point fiber has entropy one. Its endpoints have
the same label, because they are adjacent in U. A singleton fiber
has entropy zero. Counting the boundary endpoints therefore gives

    H(X_i|X_-i,L)=1-d_i/(2p).                                (3)

Here d_i counts both boundary endpoints with weight 2^-n; just one
endpoint lies in U. In particular W_{i}=d_i/2, exactly.
The chain rule and conditioning reduce entropy, so

    H(X_A|X_Ac,L)>=sum_{i in A}H(X_i|X_-i,L).

Combining with (2)-(3) yields

    2W_A<=I_A<=r max_i d_i.                                 (4)

Singletons are proper at n>=2 and attain the final maximum, proving
(1). There is no division by a zero mass and no asymptotic argument.
The conclusion holds for constant g=1 as well, with both sides zero.
For g=0, W and all influences are zero but the normalized ratios are
undefined, so that case is excluded from (1).

The component condition is used exactly in (3). It cannot be dropped:
on the full cube, parity labels split every edge, giving W_i=1 although
d_i=0. Arbitrary disjoint labels need not satisfy the theorem.

## Recovering the edge slack and the critical reserve

Let h=H(X|L)=sum_l(|U_l|/|U|)log2|U_l|, and define

    b=h-sum_i H(X_i|X_-i,L)
     =h-n+I(f)/(2p)>=0.                                    (5)

Nonnegativity follows by writing h in a chain and conditioning every
summand on the other coordinates. This is conditional dual total
correlation; it is physical entropy, not Fourier entropy. In particular

    h=n-I(f)/(2p)+b.                                        (6)

At block A the exact discarded isoperimetric slack is
R_A=I_A-2W_A>=0. A054's terminal-inclusive upper bound is

    L_A(f)<=4rp+a I_A.                                      (7)

Now fix K>a. Suppose f is a least-essential-dimension violation of
H(f)<=K I(f), with D=H(f)-K I(f)>0. Every actual child of a
nonempty physical restriction has smaller essential dimension and
satisfies that inequality. For a block A write
S_A=-E_children[H(child)-K I(child)]>=0. Then, exactly,

    D+S_A=L_A(f)-K I_A.

Consequently the previous necessary inequality strengthens to

    2(K-a)W_A+(K-a)R_A+D+S_A<=4rp.                         (8)

All child terminals remain in S_A. Neither S_A nor D is renewable.
For singleton blocks this gives (K-a)d_i+D+S_i<=4p. Summing once
over coordinates and using (6) gives

    h >= n-2n/(K-a)+b
         +(nD+sum_i S_i)/(2p(K-a)).                         (9)

This sums necessary constraints for alternative singleton queries.
The nD term is not permission to spend the root reserve n times;
the alternative S_i accounts are not one executable tree's bank.
Equation (9) is only a structural consequence of simultaneous criticality.

At K>=4+a, h>n/2+b. Hence each sign set of a hypothetical minimal
K-violation contains a component of size strictly greater than 2^(n/2).
This improves the previous 2^((n-1)/2) threshold. Apply the argument
separately to g=(1-f)/2 and g=(1+f)/2: Fourier entropy, influence,
D, and every actual S_A are unchanged by sign reversal; p and b need
not be the same. No component is used as a physical descendant.

For every fixed K>a the same argument implies

    max_i d_i < 4 min(p,1-p)/(K-a).                         (10)

At K>=4+a this is strictly below both sign masses. By (1), every
proper block fails the sufficient fiber threshold on both signs of
such a hypothetical critical source. This is an exact limitation of
that sufficient admission rule, not a counterexample to FEI, and not
a refutation of the paid-block theorem (a violation is hypothetical).

For comparison, the universal H(f)<=n also gives, on the same source,
h>=n-(n-D)/(2Kp)+b. It may strengthen (9) at nonrare p; no numerical
search is used to infer existence of a critical source.

## What remains unpaid

Equation (7) replaces the true signed drop by a coarse row bound.
To move beyond the exact barrier (1), one must retain a positive
improvement over 4rp+aI_A at a selected physical block and pay its
complete signed interface from the SAME D+S_A account. The fiber
criterion alone cannot select that block: it excludes precisely the
singleton high-influence class. The first unsupported line is a
dimension-independent payment of the actual signed pair interaction
for some proper pair/block on the remaining low-influence critical
source, with both complete child deficits retained. A051/A052's
affine-minimal pair constraints and A055's mixed refund are relevant
additional information; neither is asserted here to close this line.
