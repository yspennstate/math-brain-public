# A complete event-spectrum bill for balanced defects

All entropies are in bits. Influence of a Boolean sign function is the sum of physical edge-disagreement probabilities. Let h be Boolean on d shared coordinates, A an event contained in {h=1}, and 0<p=Pr(A)<=1/2. Let V be a balanced Boolean function on independent private coordinates. Put F=h+1_A(V-1), e=1-2*1_A, and let J be the shared-coordinate influence of F. Write H_A for the entropy of the probability law a_S^2/p, where a is the Fourier transform of 1_A.

The quantitative transfer is

    H(F) <= p H(V) + 2 H(h) + (3/4) H(e) + (15/2) I(e).       (1)

Also I_private(F)=p I(V), I(h)<=2J, and I(e)<=2J. Consequently, if H(h)<=Ch I(h), H(e)<=Ce I(e), then

    H(F) <= p H(V) + [4Ch+(3/2)Ce+15] J.                    (2)

No shared dimension, event Fourier l1 norm, or rarity/dimension condition occurs. The event and carrier certificates in (2) are supplied hypotheses. Arbitrary events do not receive a free FEI certificate.

## Complete spectral partition

Let g=h-1_A and M=1-p. Physical disjointness of g and 1_A implies ||g||_2^2=M. The empty-private Fourier rows of F are ghat_S. Every nonempty-private row is a_S Vhat_T. Balance is used here: Vhat_empty=0, and all private spectral mass is in nonempty rows. Thus, with P=(ghat_S^2,p), a probability law with one additional symbol,

    H(F) = H(P) + p H_A + p H(V).                           (3)

In particular, the dummy row p must be retained. This identity includes all mean rows and all private terminal entropy.

## A normalized reference bounds coherent interference

Let b_S=hhat_S, r_S=b_S^2+a_S^2, and R_S=r_S/(1+p). Parseval makes R a probability law. Every row with ghat_S nonzero has R_S>0. Since ghat=b-a, ghat_S^2<=2r_S. Also log(1/R_S)>=0, including rows with r_S>1. Define the complete reference Q_S=R_S/(1+p), Q_dummy=p/(1+p). It sums to one. Gibbs' inequality and the preceding pointwise inequality give

    H(P) <= sum_S ghat_S^2 log(1/R_S) + log(1+p)+p log(1/p)
         <= 2 sum_S r_S log((1+p)/r_S)+log(1+p)+p log(1/p)
         <= 2H(h)+2p H_A+3p log(1/p)+(3+2p)log(1+p).       (4)

The last step uses r_S>=b_S^2 and r_S>=a_S^2 separately inside each nonnegative weighted sum; zeros are interpreted by continuity. There is no claim that the coherent spectrum equals an incoherent mixture. R is an upper-bound reference only.

Since p<=1/2 and ln 2>=2/3, (3+2p)log2(1+p)<=4p/ln2<=6p. Edge isoperimetry gives I(e)>=2p log2(1/p)>=2p. Consequently the last two terms of (4) together cost at most (9/2)I(e).

For completeness the required edge isoperimetry follows inductively from the two half-cubes. If their event densities are u,v, the cross-edge disagreement is at least |u-v|; applying induction on the two halves leaves the scalar inequality h2(t)>=2 min(t,1-t), for t=u/(u+v). This is concavity of h2 above the chords from 0 to 1/2 and from 1/2 to 1. Explicitly the required difference is (u+v)[h2(u/(u+v))-1]+|u-v|>=0. Empty half-cubes use the continuous zero convention.

The exact relation between the indicator law and the Boolean event spectrum is

    4p H_A = H(e)-phi((1-2p)^2)+8p(1-p)
                       -4p(1-2p)log2(1/p),                (5)

where phi(t)=-t log2 t. Both subtracted terms are nonnegative on 0<p<=1/2, so p H_A<=H(e)/4+2p<=H(e)/4+I(e). Combining (3)-(5) proves (1).

## Actual physical influence pays once

Let L be the total event-boundary edge probability on which h changes sign. An h-pivotal edge cannot lie inside A. Boundary edges of F disagree with probability 1/2 because V is balanced. Every other carrier pivotal edge remains pivotal. Therefore

    J=I(h)-L+I(e)/2,  0<=L<=min(I(h),I(e)).                (6)

It follows that J>=I(h)/2 and J>=I(e)/2. Both bounds hold even if all event-boundary edges were carrier pivots; no positivity of the event's neighbors is assumed. Equation (2) follows. For p=0, F=h and the transfer is immediate; p=1/2 is included. A nonempty event and balance imply J>0, so no zero denominator is used.

## Several scales and the honest universal gap

Suppose a finite acyclic tower uses fresh shared coordinates at each wrapper and balanced private children, with supplied uniform carrier/event FEI bounds Ch,Ce. If the child entropy has bound C0 times its influence, (2) yields a parent bound max(C0,4Ch+(3/2)Ce+15). The coefficient does not add across levels: the same probability p multiplies the complete child entropy and its actual private influence. Output balance is an additional requirement for any node reused as a balanced private child; closure of arbitrary wrappers under balance is NOT asserted. Multiplication by a fresh independent sign makes a wrapper balanced and preserves entropy, adding exactly one influence, so finite towers may use this explicitly accounted balancing step.

This is a repair/extension of A077's prior dimension-dependent continuity transfer, not an all-dimensional FEI proof. Its first unsupported universal line is a noncircular ORIGINAL influence-priced source for arbitrary event sign e and carrier h. Multiple correlated profiles and consumed-influence stopping-tree payment remain unproved. No prior FIRST, D0, terminal, or source account is reset.

## The unrestricted event bill contains full FEI, quantitatively

Take h=1 and V=y, an independent sign, and denote this wrapper by W_A. For every event of mass 0<p<=1/2 its full spectrum gives exactly

    H(W_A)=phi((1-p)^2)+phi(p^2)+2 sum_{S nonempty}phi(a_S^2),
    H(e)=phi((1-2p)^2)+4 sum_{S nonempty}phi(a_S^2)-8p(1-p),
    I(W_A)=p+I(e)/2,   J(W_A)=I(e)/2.                    (7)

For 0<=x<=1, phi(x)<= (1-x)/ln2 <=2(1-x). Hence phi((1-2p)^2)<=8p(1-p), including p=1/2 by continuity. Both remaining root terms of H(W_A) are nonnegative. Thus

    H(e)<=2H(W_A).                                      (8)

Let C* be the optimal universal Boolean FEI constant (possibly infinite). Let K* be the supremum of H(W_A)/J(W_A) over all finite-dimensional events with 0<p<=1/2. Then

    C* <= K* <= 2C*.                                   (9)

The left inequality follows from (8) and complementing the sign of any Boolean event function to make its minority probability at most 1/2; constants have zero entropy. The right follows from FEI applied to W_A and p<=I(e)/2, so I(W_A)<=I(e)=2J(W_A). The statement is also meaningful as finiteness equivalence if either supremum is infinite. These are explicit actual Boolean wrappers, with their private influence retained. A universal replacement paying this complete event-spectrum bill is therefore FEI-strength already for a constant carrier and a one-bit private profile. It is not enough to name an effective support cost and assume it is cheap.
