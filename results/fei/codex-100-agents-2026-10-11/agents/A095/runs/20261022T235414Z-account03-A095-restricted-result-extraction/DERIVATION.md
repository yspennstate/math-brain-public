# Two prescribed narrow resets from one diminished rate-four bank

All costs are ideal bits, influences are physical uniform-cube influences, and h_L=1-2 indicator(all L bits zero), with h_0=-1. Fix every w>=4,m>=0. The original point-selector M and incoming complete Q are exactly A095 stage16, source h_w h_2. Execute ANY finite adaptive wide-only tree, with all its actual references and complete releases retained. Let d be its all-zero path depth, t=w-d, rho=2^-d.

At that leaf query the first narrow coordinate. Reset ONLY child0, reach lambda1=rho/2, to A094's prescribed Q1=(1-eta)Qcan(h_t h_1)+eta U, for ANY eta in[0,1/4]. Keep every sibling and off-path terminal with its entire inherited reference cost. Query the remaining narrow coordinate INSIDE that reset child0. Transport Q1 by the actual normalized posterior; retain child1, and reset ONLY child00, original reach lambda2=rho/4, to Q2=Qcan(-h_t). Selector, padding and any independent terminal are unqueried. No original quota or old debit is renewed.

**Theorem (analytic author proof, independent review pending).** This complete two-query/two-reset ledger, including all prior complete query releases, first reset signed excess, second reset signed excess and every final H+KL terminal, is strictly below 4 I(M)-3/256 for ALL w,m,d and all the allowed wide-only adaptive policies and eta. This is a scoped structural source-bank theorem, not a universal FEI proof or a per-leaf influence price.

## 1. Sharper original bank; account names kept distinct

Put q=2^(1-w), delta=2^(-w-2-m), c=H(h_w h_2). The accepted signed-profile source derivation gives

    CEroot<c+delta[4m-2w+15+(4w+2)q],
    c<2+(4w-1)q-(2w-2)q^2,
    Iroot=1+wq+delta(m-w-1).

Consequently the ORIGINAL unused quota S0=4Iroot-CEroot satisfies

    S0>2+q+(2w-2)q^2-delta[2w+19+(4w+2)q].   (1)

At w=4, use q=1/8,delta<=1/64, retaining the POSITIVE source terms: the lower bound is 451/256. At w>=5, discard only these positive terms. Both (2w+19)2^(-w-2) and (4w+2)2^(-2w-1) decrease with w. At w=5 their sum is243/1024. Thus S0>1805/1024>451/256. Extra padding only decreases this subtraction. We have uniformly

    S0>451/256=7/4+3/256.                     (2)

This improves A094's looser395/256 estimate for the SAME original-root account by retaining q,q^2 at w=4 and splitting off w>=5. It is not a replacement for A095's3/256 surviving-terminal margin: that margin refers to a different account.

## 2. First reset: independent reconstruction at named scope

For t>=2 put u=2^(1-t),b=1-u. The sparse h_t h_1 source has true support2^t, signed sum1, entropy c_t, signed profile A_t and log-sum B_t:

    c_t=-2b^2 log2 b+(2u-u^2)(2t-2),
    A_t=2b log2 b+(2-u)(2t-2),
    B_t=-2log2 b+(2^t-1)(2t-2).

With epsilon=2^(-t-1-m), the canonical reference puts (1-W)P_source on its TRUE old support and epsilon^2 on every other mask, W=2epsilon-2^t epsilon^2. Thus its old-sector cost is c_t-2epsilon A_t+epsilon^2 B_t; adding -(1-W)log2(1-W)+2(t+1+m)W retains the full new sector and normalization. As in A094,

    CEcan<c_t+epsilon[4m-3t+14+(4t+2)u].       (3)

Here A_t>=4t-4-(2t+1)u, B_t/2^t<=2t-2, epsilon*2^t<=1/2, and log2(e)<3/2. For t>=4,c_t<57/32 and (4t+2)u<=9/4. The induction16m+17<=17*2^m bounds (3) by245/128<2. For t=2,3 the same formula gives29/8 and97/32, respectively, both<4. For t=0,1 the source is a character and the canonical reference equals the actual point-edit spectrum; its entropy is at most epsilon(4n'+3), n'=t+1+m>=1, hence at most7/2<4. These boundary cases use true support, never a zero influence denominator.

Since Q1>=(3/4)Qcan, its FULL cost C1<CEcan+1/2. If d=0,t=w>=4,lambda1 C1<5/4. If d>=1,lambda1<=1/4 and C1<9/2, so lambda1 C1<9/8<5/4. This independently reconstructs A094's one-reset price, including its arbitrary finite-cost terminal and zero-fiber conditions; no repair is required.

## 3. Second prescribed reference and ALL boundary sources

On child00 both narrow inputs are fixed zero, so the ACTUAL unedited source is -h_t on its t remaining wide bits. It has value+1 at the edited point. Its selector/padding point edit is the actual residual Boolean child, not a surrogate spectrum. Define Q2 by the SAME canonical support-completion recipe on the true support of P_{-h_t}, with epsilon=2^(-t-m), n'=t+m and W=2epsilon-|support|epsilon^2.

For t>=2 the entropy c_t, signed profile A_t and B_t are EXACTLY the three quantities in section2: h_1 contributes a Fourier CHARACTER, which changes neither nonzero squared coefficients nor their signed values at the all-zero point. The difference is the doubled epsilon and the smaller n'. Therefore

    C2=c_t-2epsilon A_t+epsilon^2 B_t
       -(1-W)log2(1-W)+2(t+m)W.                (4)

For t>=4,m=0, epsilon B_t<=2t-2. The preceding inequalities give

    C2<c_t+2^-t[-2t+9+(4t+2)u]
       <=57/32+13/64=127/64<2.                (5)

For t>=4,m>=1, epsilon B_t<=t-1; hence

    C2<c_t+epsilon[4m-3t+10+(4t+2)u]
       <=57/32+(4m+1/4)2^(-t-m)
       <=57/32+17/128=245/128<2.              (6)

The last sequence decreases for integers m>=1, since4<=4m+1/4. In both (5),(6), u bounds decrease with t, so all growing widths are included analytically.

At t=2, the exact c_t=2,A_t=2,B_t=8 yield

    C2<2+epsilon(4n'-1)+epsilon^2(2-8n').

At n'=2 this is23/8; for n'>=3, discard only the negative quadratic term and use(4n'-1)2^-n'<=11/8 to get C2<27/8<4. At t=3, c_t<5/2,A_t>25/4,B_t<29 imply

    C2<5/2+epsilon(4n'-19/2)+epsilon^2(17-16n')<4.

Indeed n'>=3 and4n'2^-n'<=3/2, while the omitted terms are strictly negative. These are checks of the actual sparse boundary profiles.

At t=0,1, the source is a character and Q2=P_actual. For n'>=1 its entropy is at most epsilon(4n'+3)<=7/2<4. The exceptional t=0,m=0 has n'=0,epsilon=1,W=1: the selector child is a dictator and Q2 is its point spectrum, cost0. Its old reference atom has ZERO mass and ZERO true probability. It is retained as a zero atom; no log of zero, positive-mass cancellation or positive-normalizer assertion is made there. This is the only W=1 boundary and is expressly included.

We have proved C2<2 when t>=4 and C2<4 at every t>=0. Thus

    lambda2 C2<1/2,                           (7)

using t=w>=4,lambda2=1/4 when d=0; using lambda2<=1/8 when d>=1. Unlike section2 this bound includes an actual zero-reference boundary.

## 4. Both signed charges and all original releases

Let G be the reached sum of all complete reference releases from physical queries, and T the reached sum of complete current terminal CE. Before resets G+T=CEroot. A reset of a single reached leaf changes the full ledger by its SIGNED excess lambda(Cfresh-Cold). Denote the first actual signed excess by e1; after it the ledger is CEroot+e1. A physical query in that reset child uses the current Q1 and only disintegrates its existing full bill. Resetting child00 changes the ledger by e2=lambda2(C2-Cold,00), where Cold,00 is the complete reference inherited FROM Q1, not the pre-first-reset Q.

Exactly,

    G_final+T_final=CEroot+e1+e2.              (8)

The complete old siblings and all old releases are explicitly present in (8). The conservative booking p1=max(e1,0),p2=max(e2,0) satisfies p1<5/4,p2<1/2 because both old costs are nonnegative. Thus even WITHOUT reclaiming negative reset credits,

    S0-p1-p2>451/256-7/4=3/256.               (9)

In particular the second charge is paid from S0-p1, the diminished SAME original bank. An independent terminal remains tensor-additive in CE and KL by product-compatible zero-fiber posteriors; its complete cost is excluded from S0,p1,p2. Reset changes no physical function or influence. No query is assumed to have its own local4Inf price, and no terminal is promised an individual4I guarantee.

## First unsupported universal line

This pays the second prescribed narrow reset with cumulative conservative booking for the explicit family. It does not supply an arbitrary-core source reference or pay arbitrary repeated reset rules. The remaining source-specific root surplus and canonical profiles are structural hypotheses. NEXT exposes an actual remaining wide coordinate after both narrow resets and prices its prescribed reference with the same p1+p2 already booked, retaining the complementary full terminal; no further bare no-reset telescoping is needed. Full FEI remains OPEN.
