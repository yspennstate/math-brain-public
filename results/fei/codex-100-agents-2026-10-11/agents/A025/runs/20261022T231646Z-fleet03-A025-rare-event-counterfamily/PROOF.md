# One ancestor account pays every mixed cut of the rare-event family

All signs are Boolean on uniform cubes. Entropy is in bits. Fix even
m>=4, delta=2^-m, common activation width t>=0 and p=2^-t. Use exactly
the A025/A021 family: b(y)=(-1)^(y0*y1+...+y_(m-2)*y_(m-1)),
g0=zb, g1=g0 flipped at x=0,y=0, and g2=g0 flipped at x=0,y=e0.
Two independent fair controller bits choose labels with probabilities
(1/2,1/4,1/4). Every core has the same fresh point activation, with
inactive value+1. Query x first. Let the two resulting actual physical
histories be the root partition of the following account.

After x, permit ANY finite adaptive restriction tree on the m y bits
and the two controller bits, querying a coordinate at most once on a
path. Trees may stop at any leaves; their queries and stopping rules
may depend on all previously observed physical outcomes. Keep z and
activation coordinates unqueried. Each leaf may finish its remaining
controller queries and stop at its actual conditioned core. No leaf
is discarded. All expectations below include the x-root probabilities.

## The general accounting identity

At a cut T, let IT_T,HT_T be the full physical averages of the original
cores' remaining data influence and entropy, with controller labels
conditioned on the ACTUAL revealed controller outcomes. Repeated labels
retain their weights; a label with zero conditional probability contributes
zero. Let H_T be the average entropy of the actual mixed node functions.
Write L_T=H_T-HT_T. Revealing the remaining controller bits telescopes
nonnegative one-bit entropy decrements, so L_T>=0. Define

    S_T=8 IT_T-HT_T,
    E_T=10(Pi_D+Pi_C)-(H_0-H_T),
    A_T=S_T+E_T.                                      (1)

Pi_D and Pi_C are reached queried influences on y and controllers,
respectively, AFTER the x query. E_T is SIGNED; no negative query bill
is thrown away, and it is not a fresh allocation. Subscript0 means the
post-x root partition, including both siblings.

For a data query, its actual pivot mass equals the label-weighted core
pivot mass, since the remaining controllers are still uniform physical
coordinates independent of the unqueried data. For a controller query,
conditioning changes the label weights but preserves IT and HT in
expectation. Therefore IT_0-IT_T=Pi_D exactly. Expanding definitions gives

    A_T = S_0+2Pi_D+10Pi_C-L_0+L_T.                   (2)

This identity is valid for arbitrary finite shared-data cores and a
finite physical controller under the stated separation of coordinates.
It does not prove any universal source admission. It handles adaptive
trees by conditional expectation at each actual node, not by multiplying
independent per-row estimates. No leaf entropy or reference is erased.
Since Pi_D,Pi_C,L_T>=0, A_T>=S_0-L_0 for EVERY allowed adaptive cut.

## The original bank never increases

At a node with actual conditional label weights pi_j and actual
restricted cores h_j, use R=2 sum_{j<k} pi_j pi_k I(h_j h_k), on the
remaining data coordinates (including z and activation). At a data
query, ordinary influence telescoping for EACH product h_j h_k gives
R_parent=average R_child+2 E q(1-q), where q is the label-weighted
terminal pivotal indicator in the queried coordinate. All other product
directions retain their actual conditional capacities.

At a controller query, fix any remaining data edge and write P_j for
its terminal pivotal indicator. Its bank contribution is
2 Var(P_label)=2q(1-q). Conditional variance decomposition gives
average child bank <= parent bank, direction by direction. Thus the
physical average R_T<=R_0 at every mixed cut. This directly reconstructs
the source bank-contraction clause; it is not assumed to pay entropy.

## Root source admission, once

The inherited x-query excess is U_x=max(D_x-10d_x,0), with

    U_x<=p m delta/2,
    R_0=p(3m-1+3t)delta/4,
    IC_0=p delta,
    S_0>=p(3m+1+4t).                                 (3)

These are A021's explicit x-owner subclause and A025's checked bank.
For completeness the S_0 bound follows from H(core)<=m and
I(core)>=1+m/2-2m delta before activation. Balanced activation has
H=pH_unactivated+A(t), I=p(I_unactivated+t),
A(t)<=p(4t+2 log2 e). Since m delta<=1/4 and log2 e<3/2, (3) follows.
The x-bound follows from D_x<=h2(delta/2)+2(log2 e)delta/2 before
activation. All x children are balanced by z, so its offset cancels.

The complete ORIGINAL controller bill obeys

    0<=L_0<=R_0+10 IC_0.                             (4)

The x=0 core family has two adjacent point edits; A021's ANY-seed
two-edit theorem, on the m-bit seed with fair controls, supplies (4).
The x=1 cores coincide and have zero bill. The common activation
scales the bills and controller influence, and its extra bank capacity
is nonnegative. This use includes the original full terminal entropy.

Keep the already booked delta/4 share for R_0 and delta/6 for U_x.
Allocate ONE additional LOSS BUFFER of the same ANCESTOR S_0 to L_0:

    R_0 <= (delta/4) S_0,
    U_x <= (delta/6) S_0,
    L_0 <= [delta/4+10delta/(3m+1+4t)] S_0.           (5)

These are three disjoint allocations issued ONCE at the post-x root.
Their total fraction is

    theta=2delta/3+10delta/(3m+1+4t)
          <=56delta/39 <=7/78.                      (6)

Here 3m+1+4t>=13 and delta<=1/16. The extra loss buffer is not another
copy of the bank: R_0 is an upper bound on the remaining controller
debt, while the distinct L_0 allocation bounds the worst decrease of
the SIGNED source-plus-query account in (2). The two uses are explicitly
paid from disjoint fractions. No term is charged once at every query.

Combining (2),(5),(6) and R_T<=R_0 gives

    A_T-R_T-U_x >=(71/78) S_0+2Pi_D+10Pi_C >0.       (7)

In particular every rare query's actual signed loss is already included
in E_T. The separately booked returning-query U_y from A021 can be
retained for an audit; adding it again to E_T would DOUBLE CHARGE that
query. The old x debit IS still outside E_T and remains explicitly paid.

## Remaining-controller admission at any cut

The completion at an arbitrary allowed node costs at most

    L_node<=R_node+10 IC_node.                       (8)

If both controllers remain, the possible actual profiles are identical
cores, one point edit with multiplicity, or two distinct point edits
of one common seed. The last case is A021's ANY-seed theorem. The
singleton case is independently reconstructed in A025 stage6: for
n remaining data bits and eta=2^-n, V=3eta/4,
Hplus=(2n+2)V, IC=eta and R=nV. Signed row Jensen refund gives
L<=R+(2+log2 e)V+2(log2 e)IC<R+6IC. This includes n=0; an edit then
flips the whole seed and R=0.

If one controller remains, its two equal-weight labels either coincide,
differ at one point, or are the two different point flips. In the
one-point case V=eta, Hplus=2nV, R=nV, IC=eta. The same signed refund
gives L<=R+3(log2 e)IC<R+5IC. For the two-point case, let e=1 if the
two vertices are adjacent and e=0 otherwise. Then V=2eta=IC, the
nonzero variance rows have v_T=4eta^2 and v_T/V=2eta,
Hplus=(2n-2)V, R=(n-e)V. The refund is at most
-(n-1)V+(log2 e)V. Including the mixture entropy<=2(log2 e)IC yields
L<=R+(e-1+3 log2 e)IC<R+5IC. This case needs n>=1, which follows from
two distinct vertices. These calculations allow arbitrary seed Fourier
coefficients, including zero rows. With no controller remaining L=0.
Balanced activation preserves all bills and IC by p and adds only
nonnegative actual bank capacity. Thus (8) holds on every allowed leaf.

The full influence and entropy telescopes, then (7),(8), prove for the
actual policy (x, arbitrary mixed tree, remaining controllers, cores)

    10 I(F)-H(F)
      >=2 IT_T+A_T-R_T-U_x
      >=2 IT_T+(71/78)S_0+2Pi_D+10Pi_C >=0.           (9)

The known stronger global H<6I is not new. The new conclusion is the
specific unchanged-source account at EVERY mixed cut, including a cut
after all y bits have been revealed. It does not assert that S_T alone
is large, or that a fixed fraction of S_T retains an old rare debit.

## The final collapse is crossed, not denied

At the cut exposing all y data in both x children and leaving the
controllers, every original terminal is activated +z or -z. Exactly

    S_final=8p(1+t)-A(t),
    L_final=2p delta,
    IT_0-IT_final=p[m/2+(m-1)delta/2].                (10)

Thus S_final is O(p(1+t)), as A021's obstruction requires. However the
actual signed query credit satisfies

    E_final >=4pm-L_0.                               (11)

Indeed HT_0<=pm+A(t), HT_final=A(t), so substitute (10) into (1).
This credit is earned by the ACTUAL physical data queries. It supplies
the missing source scale at the final cut; no old debit or sibling is
removed to make the fraction fit. A021's counterexample to a current-
terminal-only third fraction remains valid for 3m>134+32t.

## Boundaries and remaining universal gap

All statements include t=0, where p=1 and A(0)=0, m=4, n=0 singleton
cores, identical labels and partially exposed controllers. All canceled
denominators in (5),(6) are positive. The argument uses only finite
conditional expectations and finite sums; it makes no limit exchange.
The policy is chosen after m,t, as allowed by the quantifiers.

This is a conditional transfer identity with an explicitly certified
source admission on one parameterized Boolean family. It is NOT a
universal FEI proof or a refutation of an all-coordinate or stopping
route. The universal unpaid line is to supply an equally owned root
source satisfying S_0>L_0+R_0+U_x for arbitrary nonflat core profiles,
or replace that admission with a genuinely available signed reference
account. Queries of z or activation coordinates are outside this
family-level balanced-activation specialization.
