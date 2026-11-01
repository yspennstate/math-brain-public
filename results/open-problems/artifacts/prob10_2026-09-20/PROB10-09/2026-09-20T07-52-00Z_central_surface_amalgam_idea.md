# PROB10-09 idea before code — central amalgams of surface extensions

Parent remains the Benjamini–Schramm bond-percolation conjecture for every Cayley graph of every finitely generated nonamenable group. This note records the mathematical idea before any new checker.

## New route

The preceding R20 theorem treats one non-split infinite-cyclic central extension of a closed surface group, and then bounded arbitrary generator augmentation. A different extension is to glue several such central extensions along their common infinite cyclic centre.

For r>=2, genera g_i>=2 and nonzero Euler classes e_i, consider

E(g,e)=< z, a_{i,j}, b_{i,j} | z central, prod_{j=1}^{g_i}[a_{i,j},b_{i,j}]=z^{e_i} for i=1,...,r >.

Equivalently this is the iterated amalgamated free product of the individual central surface extensions over their common centre <z>. Killing z gives the free product Gamma_{g_1} * ... * Gamma_{g_r}.

Let S be the standard symmetric set consisting of every a_{i,j}^{+-1}, b_{i,j}^{+-1}, and z^{+-1}. Put

G=sum_i g_i,  Sroot=sum_i sqrt(g_i),  k=sum_i(2g_i-1)=2G-r.

Two mechanisms should combine:

1. Critical side: by Freiheitssatz in each surface factor, all but one standard surface generator in each factor generate F_{2g_i-1}; across the free product these combine to F_k. Together with z this should lift to F_k x Z. Hence the Cayley graph contains T_{2k} square Z. The full Z-fibre Galton–Watson calculation from the previous R20 report should give the strict bound p_c < 1/(2k), not merely <=1/(2k-1).

2. Operator side: Fourier transform along the common central Z. The horizontal operator splits as a sum of factor operators. On each coset, factor i is a magnetic surface adjacency and should have norm <=4 sqrt(g_i) by diamagnetic domination plus Zuk's ||M_{g_i}||<=g_i^{-1/2}. Therefore ||A|| <= R:=4 Sroot+2. With degree D=4G+2 and Q=D-1=4G+1, the nonbacktracking transfer gives p_u >= p_{2->2} >= 1/beta_D(R).

The key inequality to test is beta_D(R) < 2k = 4G-2r.

There is a simple uniform proof candidate. Since g_i>=2,

Sroot <= G/sqrt(2),    r <= G/2,

so x:=4G-2r >=3G and R<=2sqrt(2)G+2. For P(t)=t^2-Rt+(4G+1), x lies to the right of R/2. Hence

P(x) >= P_{R0}(3G)
     =(9-6sqrt(2))G^2-2G+1
     > (1/2)G^2-2G+1 >0

for G>=4, using 9-6sqrt(2)>1/2 (equivalent after squaring to 289>288). This should force x above the nonbacktracking growth root beta.

Thus the whole r>=2 central-amalgam family should have p_c<p_u for its standard Cayley graph.

## Tight smallest case and exact target

The smallest new graph is r=2, g_1=g_2=2. Then G=4, k=6, D=18, Q=17 and

R <= 8sqrt(2)+2.

The general proof gives p_c<1/12 and beta<12. For a clean rational quantitative certificate, try p_u>21/250. Setting z=250/21, it is enough to prove z^2>17 and z+17/z>2+8sqrt(2). The elementary bound sqrt(2)<99/70 gives

z+17/z = 69997/5250,
2+8sqrt(2) < 466/35 = 69900/5250,

leaving exact slack 97/5250. Therefore the intended frozen auxiliary metric is

p_u-p_c > 21/250 - 1/12 = 1/1500.

## Negation tests / distinct methods

A. Quotient-cover route: check whether strict monotonicity under the central covering alone would imply the result. It gives useful p_c information but no immediate general p_u monotonicity for infinite fibres, so it should not be promoted without an additional theorem.

B. Direct subgroup route: F_k x Z is an actual subgroup and gives the p_c witness, but subgroup inclusion alone does not transfer p_u upward. The operator estimate remains necessary.

C. Central-amalgam Fourier route: the proposed successful route above combines the subgroup p_c witness with a central direct-integral norm estimate and is structurally different from NM13-11's Rattaggi/free-augmentation lane.

No source-level closure or novelty claim is made in this idea note. The next step is to verify the algebra exactly and then write a full proof if the group-theoretic and operator decompositions survive scrutiny.
