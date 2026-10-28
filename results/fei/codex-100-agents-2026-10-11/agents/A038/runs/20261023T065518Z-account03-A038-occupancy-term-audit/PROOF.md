# All positive query debits, including queries after the second reset

Uniform Boolean inputs; all entropy/KL in bits and rate4. Retain the root, source definition and hypotheses of A038-BALANCED-CANONICAL-ADMISSION@3. Thus h_m=chi_z d_m, d_m=1-2*1[y=0], m>=3; F=chi_a on x0, h_m on x=b=1, and +1 otherwise. M is the ORIGINAL completed canonical occupancy reference, A=KL(P_F||M)=(15/16)K_occ. Query b first, keep b0 untouched and never query a. Inside b1 use any finite adaptive fresh data/x tree with x eventually exposed on each terminal path. Two prescribed canonical reset frontiers may occur after x exposure. Preserve all references and all physical complementary terminals.

Fix ANY prior paid all-x-exposed frontier and its ACTUAL booking L0=A+[Dpre-4Rpre]_+. Keep every conservative previous extra booking in 0<=omega<=11/32. Preserve each already booked post-prefix physical debit U_j, with each U_j the positive part of the signed query deficit in one disjoint leg of the subsequent history. Arbitrarily many further disjoint data-query legs, including legs AFTER the second reset, are allowed. One may instead charge individual reached nodes by their weighted positive query deficits, or use any disjoint partition of queries into groups. No physical query is charged in two groups; overlapping conservative duplicate charges require a separate explicit booking and are not silently discarded.

Let P_future be the SUM of all these old and new post-prefix positive leg debits, and B0,B1 the FULL new terminal KL bills for at most two named canonical reset frontiers (each at most7/32). The current references are always transported by the actual coherent common kernels, fair on source-zero rows; reference-only mass and reference outcome normalizers remain. No reset credit is renewed. Let Sfinal be the actual complete final mean4I-H.

THEOREM. For every m and every stated finite adaptive history,

    L0+P_future <= A+[H(d_m)-8(m-1)2^-m]/4
                 <=G_m-1-2(m-1)2^-m <155/128,
    Sfinal-(L0+P_future+B0+B1+omega)>1/128.      (T)

Thus ALL further data queries after the second reset remain paid, with EVERY old L0,B0,B1,omega and old physical debit retained. This extends version3's one-whole-post-leg payment to cumulative positive debits under arbitrary finite disjoint leg partitions. It is not a theorem for arbitrary Boolean cores, third resets, a exposure or b0 exposure.

## 1. Exact local signed query deficit

Write s_k=4I(d_k)-H(d_k). An active point-bit query at k>=2 has signed surplus increment

    delta_k = s_(k-1)/2-s_k
            =H(d_k)-H(d_(k-1))/2-8*2^-k.

Set epsilon=2^-k and F(q)=-(1-q)^2 log2((1-q)^2). The explicit point-defect spectrum gives

    delta_k=8(k-3)epsilon^2+F(2epsilon)-(1/2)F(4epsilon),   (1)

For k>=3, q=2epsilon<=1/4, and

    F''(q)=-2[2 ln(1-q)+3]/ln2 <0 on[0,1/2].

Indeed ln(1-q)>=-ln2 and ln2<3/4, so the bracket is positive. Strict concavity and F(0)=0 yield F(q)>F(2q)/2 for q>0. Therefore delta_k>0 for k>=3. The boundary k=2 has delta_2=0 exactly; k=1 has two constant children and signed increment -4. A query of the independent z character has signed increment -4, a dummy data query0, and x exposure is exactly rate4-neutral. Adding or removing the surviving character does not change a point-bit delta_k.


## 2. Positive variation is finite and paid once

The maximum total EXPECTED positive point-query increments starting at d_m or chi_z d_m is

    Q_m = sum_(k=3)^m 2^(-(m-k))*delta_k
        = 8*2^-m-s_m
        = H(d_m)-8(m-1)2^-m.                  (2)

This is an exact finite Bellman induction, not a product of adaptive conditional bounds. Define Q_1=Q_2=0. At k>=3, querying an active point bit charges delta_k>0 and retains an active (k-1)-bit defect with probability1/2; the other child is constant. Thus its total remaining optimum is delta_k+Q_(k-1)/2. Stopping yields0, so full continuation to k=2 attains this maximum. A z query has no positive charge and only removes the independent character; its two sign outcomes retain the same point-defect state, so cannot increase the maximum. Signs and dummy coordinates have no effect. These facts prove the recurrence for EVERY adaptive policy, with arbitrary divergent stopping choices. Telescoping s_(k-1)/2-s_k gives (2), because s_2=2 and its final survival weight is2^(-(m-2)).

At the priority-root level, a data query before x exposure acts on selector chi_a/g, whose surplus is2+s_g/2; its signed increment is half the corresponding core increment. The b1 reach weight is1/2. After x exposure only b1x1 carries core increments, at total weight1/4; b1x0 is the retained a character. Thus the full rooted sum of weighted positive query increments is at most Q_m/4, whether data queries precede or follow x. More formally, simulate the b1 policy with x fixed to1 to obtain an adaptive core policy, and apply the preceding finite Bellman bound. The original b query is rate4-neutral at this balanced core; x is neutral at every restricted core. Only point-bit increments k>=3 can be positive.

For the prior prefix, L0-A=[sum signed prefix deficits]_+ is at most the prefix sum of positive deficits. For each subsequent DISJOINT query group, its positive signed deficit is at most that group's sum of positive node deficits. Adding the prefix and all subsequent groups therefore gives

    L0-A+P_future <=Q_m/4.                    (3)

This retains all already booked old leg debits and bounds genuinely new ones without shrinking any previous booking. It does not add a coarse group AND its individual nodes: that would double charge physical queries and needs a separate explicit liability.

## 3. Original source and both reset bills stay owned

Version3 proves the exact canonical source bound A<=G_m-1-H(d_m)/4, G_m=2h2(1/4)+m h2(2^(-m-1)). Combining with (2)-(3) yields L0+P_future<=G_m-1-2(m-1)2^-m. The three exact bounds from version3 are37/32 at m3,17/16 at m4, and155/128 for m>=5; all are strictly below155/128. Thus the SAME constant now bounds the cumulative source-plus-all-positive-query package, rather than L0 alone.

Every final restricted core has H<=4I. Untouched b0 contributes1 and b1x0 contributes1 to the complete final surplus, so Sfinal>=2. Every canonical reset frontier has full new KL bill at most(1/4)*(7/8)=7/32: constants/point defects cost zero, surviving character-point-defect cores cost at most7/8, and total actual core weight is1/4. Both original reset bills are retained, including every old reference-only row and full inherited terminal KL. Each bill decomposes along its own actual subsequent common-channel erasure/outcome/terminal tree until the next reset or final frontier. No such release is added to spendable credit or charged twice. The positive actual conversion at a reset is dominated by the full new bill charged for that reset.

Hence final remaining owner exceeds2-155/128-2*(7/32)-11/32=1/128. This proves (T), including arbitrarily many queries after the second reference change and any disjoint temporal partition of the physical query charges.

## 4. First unsupported line

Data-only iteration with two canonical reset bills is now closed at the stated scope. A THIRD prescribed reset from the actual remaining account, or one a exposure that spends the supporting character, remains unpaid. Arbitrary Boolean cores still lack both affordable original canonical admission and an analogue of the positive-variation Bellman bound; those are the universal supplier gaps. Full FEI remains OPEN. All new claims are author proofs with passing exact checks; independent external review remains pending.
