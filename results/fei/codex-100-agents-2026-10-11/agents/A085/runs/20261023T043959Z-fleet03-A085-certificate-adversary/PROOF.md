# Scope check and repeated profile changes from one retained refund

All costs are bits; reaches are physical uniform-cube probabilities. Full FEI remains OPEN.

## 1. Independent scope check of A079

Use the displayed controller row a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), b=1-a^2, F=a+z*b*h. Write A=ahat, B=bhat, beta=E b^2, m=E h and r=m^2. Since ab=0, sum A_U B_U=0. The supplied tagged reference has atoms A_U^2 at (z-frequency=0,U,seed-empty), and B_U^2 R(T) at (1,U,T). Its cost is supplied, not universally influence-priced.

After the tag query the true signed vacuum is (A_U+sigma*m*B_U)^2; the other atoms are B_U^2*p_h(T). A fresh signed reference uses the SAME vacuum and B_U^2*(1-r)*M(T) on nonempty seed labels. Both normalize by Parseval and orthogonality, including all reference-only labels. If M=(1-epsilon)R_tail+epsilon*S, its exact tag-query increment is

    -JS_z-beta*d(r||R(0))
      +beta*(1-r)*E_p_tail log2(R_tail/M).

For epsilon<1 the occupied likelihood bound M>=(1-epsilon)R_tail preserves support. A constant seed or beta=0 has no tail cost and requires no division. At the original root beta=3/8, r=1/4, R(0)=1/2 and epsilon=1/8, the increment is at most -rho, where

    rho=(9/32)*log2(21)-39/32 > 1/64.

The strict scalar sign follows from 21^18>2^79; discarded JS and other gains are nonnegative. This is an earned refund, not a renewed quota.

For any finite partition pi, block calibration Qnew(x)=P(E)*Q(x)/Q(E) for x in E gives CE(P,Q)-CE(P,Qnew)=D(pi P||pi Q). If P(E)=0 assign zero throughout E; Q(E)=0 then follows from finite CE only when P(E)=0. A physical query carried with the full marginalized reference has increment minus conditional occupancy KL. Applying block calibration separately to BOTH children therefore pays each coherent continuation. Seed queries use singleton vacuum atoms plus the whole tail; controller queries use singleton vacuum atoms plus one tail block per remaining controller frequency. After optional inherited-reference steps, use one tail block per U. The tail factors C(U)*N(T) survive physical marginalization, while vacuum atoms stay seed-empty. No independence of the entire signed spectrum is assumed.

This reconstructs A079-POST-TAG-SECOND-TAIL-RESET-SAME-REFUND at its exact scope without repair. Its second 1/64 mixture costs at most beta_v*(1-r_v)*log2(64/63). Beta is a physical martingale and its frontier sum is at most 3/8, so its published >1/256 reserve follows. Zero-beta, constant-seed, zero reference-block and optional-reset endpoints are covered above. The independent checker uses FWHT, exact logarithmic identities, complete references and explicit endpoint fixtures, not the author implementation.

## 2. Stronger physical mass available for repeated changes

Let tau_v=beta_v*(1-m_v^2) be the true total nonempty-seed mass in the signed node. At a controller query, mean beta_child=beta_parent and the seed mean stays fixed, so mean tau_child=tau_parent. At a seed query, write m=(m_0+m_1)/2. Then

    tau_parent-(tau_0+tau_1)/2
      =beta*(m_0-m_1)^2/4 >= 0.

Thus tau is a nonnegative physical supermartingale through every finite adaptive mixed query tree. Reference resets do not change it. In particular its initial value after deleting z is tau0=(3/8)*(3/4)=9/32, across both tag branches. This improves A079's beta-only 3/8 coefficient by a factor 3/4; its original bound remains valid.

At a prescribed profile change Mnew=(1-epsilon_v)Mcurrent+epsilon_v*S_v with 0<=epsilon_v<1, the exact added cost is

    tau_v*E_p_tail log2(Mcurrent/Mnew)
       <=tau_v*L_v,  L_v=-log2(1-epsilon_v).

Both old siblings and all previous erasures remain. Reference-only labels are retained by the displayed mixture. The target may be a point law or have occupied zeros; the retained current component supplies support. At epsilon=1 that guarantee disappears, so this endpoint is deliberately excluded.

Suppose EVERY realized root-to-leaf path spends sum L_v<=B, with possibly different targets, epsilon choices and numbers of changes on different paths. Give node v remaining scalar budget b_v=B-sum(previous L). Its potential is tau_v*b_v. A reset reduces the potential by tau_v*L_v, which covers its actual added cost. A query preserves b and decreases its mean potential because tau is a supermartingale. Terminal potential is nonnegative. Summing these local inequalities proves

    total added profile cost <= tau0*B.

This argument uses the joint physical tree, not a product of conditional event bounds. Adaptive choices are made at their reached node; the pathwise budget is mandatory. All intervening coherent calibrations and inherited-reference queries have nonpositive increments by Section 1. Old source costs, old debits, both tag branches and every full terminal appear exactly once in the telescoping account.

## 3. Two further genuine profile changes are paid

Choose B=2*log2(64/63). This permits two additional 1/64 changes on every path, at arbitrary two ordered stopping frontiers, or any finite adaptive allocation with product(1-epsilon_v)>=(63/64)^2. The SAME original earned tag refund leaves at least

    delta=rho-(9/16)*log2(64/63) > 3/1024.

Equivalently, the strict sign is the exact integer inequality

    21^288 * 63^576 > 2^1251 * 64^576.

This adds a THIRD genuine profile change counting the original 1/8 tag mixture. It does not reissue the published 1/256 reserve at descendants. The new >3/1024 reserve belongs to a larger admitted policy than A079's single later change; the different number is not a correction of its >1/256 result. Actual histories may earn further refunds, but none are assumed here.

The crude bound rho-3*(9/32)*log2(64/63) is negative, certified by 21^3*63^9 < 2^13*64^9. This is failure of THIS guaranteed budget for three further full rounds, not a Boolean counterexample and not an impossibility theorem about actual transactions.

## 4. Exact validation and the remaining universal line

The checker independently reconstructs all n<=2 labelled seeds in the frozen domain, controller endpoints and full marginal references, then explicitly realizes three target changes with the four-bit non-point seed negative at {0,1,2,4}. It queries physical seed bit0 between the first and second changes, keeps both nonconstant children, queries another seed coordinate before the third changes, and carries all full terminals. Later zero-tail nodes use explicit point formulas. Additional scalar checks include path-dependent budgets and tau supermartingale transitions.

The all-dimensional scope is proved by Sections 1--3, not extrapolated from finite cases. The first unsupported universal line remains an initially influence-priced reference for arbitrary seeds, or a physical-energy argument funding nonsummable new profile changes. The path budget is a finite refund allocation and supplies neither. Independent review of this new strengthening is pending; no formal verification is claimed.
