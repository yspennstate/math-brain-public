# Independent audit: two prescribed narrow resets

Verdict: HOLDS at the entire named scope. The exact replay passes and the analytic chain below reconstructs the entire named A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1 and its A094 one-reset dependency without repair. All costs are ideal bits. These are structural prescribed-reference statements, not arbitrary-core FEI.

## 1. Exact objects and the changed numerical bound

Let w>=4,m>=0, h_j=1-2 indicator(all j inputs zero), h_0=-1, and start from the fair-selector point edit of padded h_w*h_2 at zero. The incoming complete reference is exactly the support-completed source-spectrum reference accepted in A081 stage7. Put q=2^(1-w), delta=2^(-w-2-m). For source entropy c, direct physical edge counting and the signed profile give

    I_root=1+wq+delta(m-w-1),
    CE_root<c+delta[4m-2w+15+(4w+2)q],
    c<2+(4w-1)q-(2w-2)q^2.

Subtracting the last two bounds from FOUR TIMES THE ORIGINAL ROOT influence gives the unused original account

    S0=4I_root-CE_root
      >2+q+(2w-2)q^2-delta[2w+19+(4w+2)q].

At w=4, retain the positive terms q+6q^2=7/32: with delta<=1/64 this is 451/256. At w>=5, dropping only positive terms yields 2-243/1024=1805/1024, strictly above 451/256. The two subtracted sequences decrease because their next-to-current ratios are respectively (2w+21)/(4w+38) and (4w+6)/(4(4w+2)), both below one. Extra padding further decreases the subtraction. Thus S0>451/256 uniformly.

This is a sharper lower bound for the SAME original-root account previously bounded by A094 at 395/256; the improvement comes from retaining q,q^2 at w=4 and separating w>=5. It is NOT a change in the earlier 3/256 surviving-terminal margin. Those quantities name different accounts. No executed bill is removed to obtain the sharper estimate.

## 2. First prescribed reset, true support and real eta

An arbitrary finite wide-only adaptive tree has one leaf containing zero. Its depth is d, original reach rho=2^-d and remaining wide dimension t=w-d. Query one narrow coordinate there. Only its zero-child, reach lambda1=rho/2, resets to Q1=(1-eta)Qcan(h_t*h_1)+eta U, for a prescribed REAL eta in [0,1/4]. U is uniform on every residual Fourier mask. Every sibling and off-path terminal keeps its complete inherited reference.

For t>=2 write u=2^(1-t),b=1-u. Multiplication by the h_1 character gives source support of size 2^t and signed profiles

    c_t=-2b^2 log2 b+(2u-u^2)(2t-2),
    A_t=2b log2 b+(2-u)(2t-2),
    B_t=-2log2 b+(2^t-1)(2t-2).

The point value is +1. With epsilon=2^(-t-1-m), old coefficients shift by -epsilon; old reference masses are (1-W) times their actual source squares, W=2epsilon-2^t epsilon^2. EVERY complementary atom has reference epsilon^2. Therefore the full cost, including its normalizer and all complementary atoms, is

    c_t-2epsilon A_t+epsilon^2 B_t
       -(1-W)log2(1-W)+2(t+1+m)W.

Using ln2>2/3, -ln(1-u)<=u/(1-u), and -(1-W)ln(1-W)<=W gives A_t>=4t-4-(2t+1)u, B_t/2^t<=2t-2 and

    CEcan<c_t+epsilon[4m-3t+14+(4t+2)u].

At t>=4, c_t<57/32: substitute the source entropy bound at t=4 and check the positive upper bound decreases thereafter. Also (4t+2)u<=9/4. Induction on 16m+17<=17*2^m bounds the correction by 17/128, so CEcan<245/128<2. The induction step adds 16 to a quantity already at least 17. At t=2,3 the same expression is bounded by 29/8 and 97/32; the relevant padded correction sequences decrease from m=0. At t=0,1 the source is a character, the canonical reference equals its actual point-edit spectrum, and its entropy is at most epsilon(4n'+3)<=7/2, n'=t+1+m>=1. Thus CEcan<4 for all boundary cases without an influence division.

For every allowed real eta, Q1>=(3/4)Qcan. Since log2(4/3)<1/2 (16<18), C1<CEcan+1/2. If d=0, t=w>=4 and lambda1=1/2; otherwise lambda1<=1/4. Hence the COMPLETE fresh reached cost lambda1 C1<5/4. This reconstructs A094's one-reset price and retains its normalized finite-cost arbitrary independent terminal hypothesis. Sampling three eta values is validation only; the pointwise domination proves the full real interval.

## 3. Second prescribed reset and the zero-reference endpoint

Inside the reset child, query the other narrow coordinate using the CURRENT Q1. Retain its one-child. Its zero-child has original reach lambda2=rho/4 and actual unedited source -h_t, with the same padding and selector. Reset it to Q2=Qcan(-h_t). The old reference for this second substitution is the one inherited FROM Q1, not the pre-first-reset reference.

For t>=2 the signed source coefficients and nonzero squared coefficients have exactly the c_t,A_t,B_t above: the h_1 factor in the first child is a character and has value -1 at zero. Now epsilon=2^(-t-m), n'=t+m, so

    C2=c_t-2epsilon A_t+epsilon^2 B_t
       -(1-W)log2(1-W)+2n'W.

At t>=4,m=0, epsilon B_t<=2t-2 gives C2<c_t+2^-t[-2t+9+(4t+2)u]<=57/32+13/64=127/64<2. At t>=4,m>=1, epsilon B_t<=t-1 gives C2<c_t+epsilon[4m-3t+10+(4t+2)u]<=57/32+17/128<2. The padded sequence (4m+1/4)2^-m decreases for integers m>=1 because 4<=4m+1/4; its maximum is at one.

At t=2 the exact triple is (c,A,B)=(2,2,8), yielding C2<2+epsilon(4n'-1)+epsilon^2(2-8n'). For n'=2 this is 23/8; for n'>=3 it is below 27/8. At t=3, c<5/2,A>25/4,B<29 give C2<5/2+epsilon(4n'-19/2)+epsilon^2(17-16n')<4; use n'>=3 and 4n'2^-n'<=3/2. At t=0,1 the reference is the actual point-edit spectrum; for n'>=1 its entropy is at most 7/2. The exceptional t=0,m=0 has n'=0,epsilon=1,W=1: the actual child is a selector dictator with spectrum (0,1), and Q2=(0,1), cost zero. The old atom has zero true mass AND zero reference mass. Retain it as a zero atom and never evaluate its logarithm. No assertion 1-W>0 is used there.

Thus C2<2 for t>=4 and C2<4 otherwise. If d=0 use lambda2=1/4,t=w>=4; if d>=1 use lambda2<=1/8. In either case lambda2 C2<1/2, including the zero-reference boundary.

## 4. Exact conserved ledger; positive bookings are cumulative

Let G be the reached sum of complete CE releases at all executed physical queries, and T the reached complete terminal CE. Before any reset G+T=CE_root. This is the exact normalized phase-aware physical reference identity; it includes membership KL, branch normalizers and reference-only zero true fibers, not merely erasure entropy.

The first reset changes the ledger by e1=lambda1(C1-Cold,0). The next query uses Q1 and only disintegrates that current bill. The second reset changes it by e2=lambda2(C2-Cold,00-from-Q1). Hence exactly

    G_final+T_final=CE_root+e1+e2.

The complete old siblings and old releases remain on the left. Since a complete normalized reference has nonnegative CE, p1=max(e1,0)<5/4 and p2=max(e2,0)<1/2. Their CONSERVATIVE cumulative booking is paid from S0, without reclaiming negative reset credits:

    S0-p1-p2>451/256-320/256-128/256=3/256.

The second booking is paid from S0-p1, never a fresh bank. A reset changes no physical function, influence or reach. A no-reset continuation below any final leaf only disintegrates that existing complete bill. Independent untouched prescribed terminals remain fully CE/KL-additive with product-compatible zero-fiber kernels; their cost is excluded from S0,p1,p2. There is no individual-child 4I guarantee.

## 5. Acceptance scope and remaining line

The all-parameter argument uses explicit finite inductions, rational inequalities and actual sparse boundary profiles; no asymptotic extrapolation or exchange of limits is needed. The replay must still check signs, actual child references after the first reset, both terminal siblings, old reaches/releases, normalizer positivity and W=1. A094's one-reset claim and A095's two-reset claim have no repair in this reconstruction. Their exact source versions are preserved.

The unpaid next source-specific line is a further actual wide-coordinate exposure and SPECIFIED reset after BOTH p1 and p2 are booked, keeping the complementary terminal and the same original quota. The broader universal leaf remains arbitrary incoming-reference/source construction and hereditary selected reset payment. These class resets do not discharge that universal leaf or close full FEI.
