# Independent obstruction, saved before reading w378

2026-10-10. This is an auxiliary bridge counterexample, not a solution or refutation of P0110. Author: w379. Independent reviewer: w380, KEEP C1/C2; receipts in REFEREE_VERDICTS.jsonl. The derivation below was saved before the paired proof was read.

Let iid nonnegative finite edge weights live on nearest-neighbor Z^2. Let T be the infimum of path sums and D the infimum restricted to coordinatewise nondecreasing paths. Suppose the law is nonconstant. Select finite 0 < l < h with p_l=P(tau<=l)>0 and p_h=P(tau>=h)>0. Choose integer n>2l/(h-l). Between 0 and n e_1 there is only one nondecreasing path: the n horizontal axis edges. The path going up, n steps right, and down uses n+2 different edges, disjoint from that path.

On the event that all n direct edges have weight >=h and all n+2 detour edges have weight <=l, D>=nh>(n+2)l>=T. The event has probability p_h^n p_l^(n+2)>0. Translates with disjoint edge sets occur infinitely often almost surely. Thus even an arbitrarily narrow bounded nondegenerate weight law cannot make undirected FPP equal to monotone FPP at all endpoints. Constant laws do admit a monotone minimizing path for every comparable pair, so this boundary is exact for the universal endpoint equality claim.

For the explicit iid two-point law P(tau=a)=p, P(tau=b)=1-p, 0<a<b, 0<p<1, take n=floor(2a/(b-a))+1. The strict saving is delta=n(b-a)-2a and its event probability is q=(1-p)^n p^(n+2).

## Linear axial gap (independent derivation)

Put delta=n(h-l)-2l>0, q=p_h^n p_l^(n+2)>0, and L=n+2. Block k starts at k L e_1: its direct segment ends at (k L+n)e_1; its detour goes through height 1. Distinct blocks use disjoint edges, including their two vertical connectors. Let E_k be the heavy-direct/light-detour event above. Then the indicators 1_{E_k} are iid Bernoulli(q), without conditioning on a selected geodesic.

For any integer N, take K=floor(N/L). Follow the direct axis path from 0 to N e_1, replacing a block's n direct edges with its n+2 detour edges whenever E_k holds, for 0<=k<K. This is a valid nearest-neighbor path. Each replacement saves at least delta, so

    D(0,N e_1)-T(0,N e_1) >= delta sum_{k=0}^{K-1} 1_{E_k}.

The strong law and K/N -> 1/L give, almost surely,

    liminf_{N->infinity} (D(0,N e_1)-T(0,N e_1))/N >= delta q/L > 0.

No moment assumption or attainment of T is needed for this gap statement: all finite path sums are finite, and an explicit candidate bounds the infimum. If E tau=m<infinity, the axis-edge strong law further gives limsup T(0,N e_1)/N <= m-delta q/L. Thus any existing axial FPP time constant is strictly below the monotone axial constant m.

For weights 1 and 2 with equal probabilities, n=3, L=5, delta=1, q=1/256, and the rigorous gap bound is 1/1280. For weights in {1,1+epsilon}, any epsilon>0, choose n=floor(2/epsilon)+1: delta=n epsilon-2>0. There is no positive support-width threshold that makes the raw axial restriction error sublinear for all nonconstant iid laws.

Scope: this refutes raw equality or an o(N) uncentered approximation by the monotone axial model. It does not refute a comparison after different deterministic centerings, a bridge in interior directions, or the original existential KPZ target. It is an elementary independently derived result; novelty is not claimed.
