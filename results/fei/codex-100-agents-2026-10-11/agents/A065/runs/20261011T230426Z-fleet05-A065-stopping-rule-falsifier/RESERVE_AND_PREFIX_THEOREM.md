# Exact reserve and unpaid-prefix statements

All entropies are in bits. A physical fair restriction tree has actual Boolean nodes g_v, query i_v, d_v=Inf_i(g_v), D_v=H(g_v)-[H(g_0)+H(g_1)]/2>=0, and constant leaves. Fix C>=0. Define

    Q*_v=max(0,D_v-Cd_v+(Q*_0+Q*_1)/2),   Q*_constant=0.

This is the least nonnegative adapted reserve obeying D_v<=Cd_v+Q_v-E[Q_child|v]. Indeed the inequality and nonnegativity force precisely this lower bound at each node; backward induction proves minimality and feasibility. No undisplayed terminal reserve is allowed.

The same recursion proves the finite-tree stopping representation

    Q*_v = sup_tau E_v sum_{v<=t<tau}(D_t-Cd_t)
         = H(g_v)-C I(g_v) + sup_tau E_v[C I(g_tau)-H(g_tau)].

The supremum is over bounded stopping times on this fixed tree, including stopping immediately. This follows by choosing at each node between stopping for zero and continuing for the displayed increment plus optimal children. The second equality uses both exact telescopes on that stopping tree, including the actual terminal entropy and influence. This is a Snell envelope, not the positive part of a complete-path total.

For every node and every rule,

    max(0,H(g_v)-C I(g_v)) <= Q*_v <= H(g_v).

The first bound chooses complete continuation; the second is backward induction: Q*_children<=H(children), hence the untruncated right side is <=H(g_v)-Cd_v<=H(g_v), and H(g_v)>=0. Consequently a uniform Q*_root<=K I(f) for ANY prescribed complete rule gives FEI(C+K); conversely FEI(K) gives that reserve bound for EVERY complete rule. Changing the rule does not turn this universal initial bound into a weaker problem. One may still prove it for a proper class or use terminal certificates with an exclusive queried budget.

## Addressing prefix with growing expected unpaid cost

Let A_a(x,y)=y_x, with a address bits and 2^a distinct data bits. Its exact spectrum has 4^a atoms of mass 4^-a, so H(A_a)=2a. Each data influence is 2^-a; each address influence is 1/2, so I(A_a)=1+a/2.

Use the complete rule that reveals every data bit first, then the remaining address bits. Stop at the end of the data phase. The queried budget is exactly 1, by the block influence identity. Every terminal restriction h_y is a sign on a address bits, so H(h_y)<=a. Thus

    E sum_{data phase}(D_t-Cd_t) = 2a-E_y H(h_y)-C >= a-C.

For every fixed C this expected unpaid prefix cost tends to infinity, and Q*_root>=max(0,a-C). This refutes a bound by a fixed multiple of the prefix's exclusive queried influence. It does not refute a bound by root influence: Q*_root<=2a and I(A_a)=1+a/2. The retained terminal influence is exactly E_y I(h_y)=a/2, because a uniformly random truth table disagrees across every address edge with probability 1/2.

This is an explicitly data-first rule. No claim is made that the adaptive min-influence rule remains data-first in all dimensions; after partial data revelations some address influences can fall below the remaining data influences. The five lead-prescribed adaptive rules are separately certified on the frozen finite domains.

## Rare activation preserves the unpaid prefix

For r>=1 let p=2^-r and F_{a,r}=1+A_r(A_a-1), with fresh point controls. Reveal controls first, stopping immediately on failure; on survival reveal every addressing data bit, then stop. The exact queried budget is B=p(r+1). The terminal law is constant with probability 1-p and h_y with probability p. The balanced activation identity gives

    H(F)=2ap+2rp(2-p)+(1-p)^2 log2[1/(1-p)^2],
    I(F)=p(1+a/2+r).

Therefore the unpaid stopped prefix is at least

    p[a+2r(2-p)-C(r+1)]

after dropping a nonnegative constant-coefficient entropy term. In particular its ratio to B is at least a/(r+1)-C. For fixed r its absolute expectation grows without bound in a. With r=ceil(log2(a))+s, fixed s>=0, root influence stays bounded, B tends to zero, and the unpaid-prefix/B ratio diverges; terminal influence p a/2 remains visible. Rarity does not repair exclusive prefix payment.

## Coded restriction plateau calibration

Let P_a(x,z,y)=y_{x*z}, where x*z denotes coordinatewise product of two fresh a-bit address blocks. Each original address Fourier character is lifted to the same support in x and z. Hence H(P_a)=2a and I(P_a)=1+a. Revealing every mask bit z produces an address-translated copy of A_a on every branch: entropy remains exactly 2a, terminal influence is 1+a/2, and the mask phase spends a/2 influence with ZERO entropy decrement at every node. After this plateau, the conditional data-first reserve is still >=max(0,a-C) on every mask branch.

This quantifies the already known zero-erasure plateau phenomenon; it is not a new zero-erasure terminal refutation. The whole prefix including masks has extra paid influence a/2, so its debt is >=a-C(1+a/2), which need not grow positively for C>=2. The conditional reserve statement must not be substituted for that whole-prefix inequality.

## All-k bound for the B05 tests

For even k>=4, r=2k, delta=2^-k, let b be the quadratic bent sign, b'=b-2*1_0, and g its fair selector splice. Its mean is m=sqrt(delta)-delta, a=1-m, and ordinary influence is i=k/2+(k+1)delta. The activated B05 parent has I=p(i+ra), p=2^-r. Its core entropy h<=k+1 and i>=k/2, so h<=3i.

For a general Boolean core of mean m, activation overhead R=H(1+A_r(g-1))-pH(g) is exactly

    R=2rpa(2-pa)+p m^2 log2(m^2)
      -(p-p^2)a^2 log2(a^2)-(1-pa)^2 log2[(1-pa)^2].

The m term is <=0. The last term is <=2pa/ln2. When a>=1 the a term is <=0; for 0<a<1 it is <=2pa/(e ln2). Thus R <= [4+2(1+1/e)/ln2] rpa <8rpa. The strict constant can be certified using ln2>56/81 and e>65/24. Consequently H(B05)<=8I(B05) and Q*_root/I(B05)<=8 for every rule, every C>=0 and every even k>=4. This reconstructs the simple entropy bound used in A064; it does not import an unreviewed universal claim.

At the actual selector root, d=pdelta and the accepted B05 packet bound gives D/d >= (1-delta)(k-2). Hence selector-first Q*_root/d >= max(0,(1-delta)(k-2)-C). The local reserve price is unbounded with k, even though Q*_root/I is bounded. Its root-budget lower bound is delta*max(0,(1-delta)(k-2)-C)/(i+ra), which tends to zero. The finite Q*/I values must not be extrapolated as an unbounded-ratio family.

First unsupported universal line: for arbitrary Boolean roots, obtain a dimension-independent upper bound on the stopping surplus (equivalently Q*) while retaining all terminal costs. The addressing and rare-prefix examples specifically forbid financing it only from the prefix's exclusive queried influence.
