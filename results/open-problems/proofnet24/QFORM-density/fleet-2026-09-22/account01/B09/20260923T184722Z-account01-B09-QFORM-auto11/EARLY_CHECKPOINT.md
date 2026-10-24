# Early checkpoint — two-bank diffuse rank-transition geometry

Run: `20260923T184722Z-account01-B09-QFORM-auto11`.
Status: supporting deterministic proof step; full QFORM open.

## Lemma A: rank-two frame has quantitative disjoint basis mass

Let `P` be an `m x 2` real matrix with `P^T P=I_2`, rows `p_i`, and leverages `l_i=||p_i||^2<=1/2`. Put

`w_{ij}=det(p_i,p_j)^2`, `i<j`.

Cauchy--Binet gives `sum_{i<j} w_{ij}=1`. For two iid bases `S,T` drawn with probabilities `w`, define

`rho_2=P(S cap T=empty)`.

Then

`rho_2 = 1-sum_i l_i^2 + sum_{i<j} w_{ij}^2 >= 1/10`.

Proof of the identity: `E|S cap T|=sum_i l_i^2`; also `P(S=T)=sum w_{ij}^2`. Since intersections of two 2-subsets have size 0,1,2,

`P(S cap T !=empty)=E|S cap T|-P(S=T)`.

For the lower bound order `l_1>=l_2>=...` and set `delta=sum_{i>=5}l_i`, so `sum_{i<=4}l_i=2-delta`. Because `l_i<=1/2`,

`sum_{i<=4}l_i^2 <= (1/2)(2-delta)=1-delta/2`.

For `i>=5`, `l_i<=l_4<=(2-delta)/4`, hence

`sum_{i>=5}l_i^2 <= delta(2-delta)/4`.

Therefore

`1-sum_i l_i^2 >= delta^2/4`.

If `delta<=1`, Cauchy--Binet on the first four rows gives

`W_4:=sum_{1<=i<j<=4}w_{ij}=det(I-R)`, `R=sum_{i>=5}p_i p_i^T`,

so `W_4=1-tr R+det R>=1-delta`. Hence by Cauchy--Schwarz over the six pairs,

`sum w_{ij}^2 >= W_4^2/6 >= (1-delta)^2/6`.

Thus for `0<=delta<=1`,

`rho_2 >= delta^2/4+(1-delta)^2/6 >= 1/10`,

with the minimum at `delta=2/5`. For `delta>=1`, the first term already gives `rho_2>=1/4`.

## Lemma B: every three-plane inside two diffuse two-frames has disjoint 3-basis mass >=1/40

Let `P,R` have orthonormal two-column frames on disjoint original-coordinate banks and assume every row of each has squared norm at most `1/2`. Put

`U=diag(P,R)`.

Let `O` be any `4 x 3` matrix with orthonormal columns and set `V=UO`. Let `z=(z_P,z_R)` be the unit vector orthogonal to `range(O)`, with the splitting `R^4=R^2_P direct_sum R^2_R`.

For a physical 3-subset `B`, let `W_B=det(V_B)^2`; these are Pluecker basis probabilities and sum to one. Define

`rho_3=sum_{B cap B'=empty}W_B W_B'`.

Then `rho_3>=1/40`.

Proof. By the Hodge-star identity `o_1 wedge o_2 wedge o_3 = +/- *z`, a triple with two rows from the P-bank and one row `i` from the R-bank has weight

`w^P_alpha * |<r_i,J z_R>|^2`,

where `alpha` is its P-row pair, `w^P_alpha=det(P_alpha)^2`, and `J` is the quarter-turn in `R^2` (the sign convention is irrelevant after squaring). The total mass of this channel is `a=||z_R||^2`. The opposite `1P+2R` channel has total mass `b=||z_P||^2`, with `a+b=1`.

Inside the first channel, conditional on being in that channel, the P-pair and the R-singleton are independent. Lemma A gives disjoint P-pairs with probability at least `1/10`. The normalized R-singleton weights are

`q_i=|<r_i,Jz_R>|^2/||z_R||^2`,

and satisfy `max_i q_i<=max_i||r_i||^2<=1/2`; therefore two iid such singletons are distinct with probability

`1-sum_i q_i^2 >= 1-max_i q_i >=1/2`.

So same-channel disjointness contributes at least `a^2/20`. The other channel contributes at least `b^2/20`. Cross-channel contributions are nonnegative. Hence

`rho_3 >= (a^2+b^2)/20 >=1/40`.

## Corollary C: stable disjoint third volume through a small fourth carrier direction

Let `K` be symmetric `4 x 4`, let `S=UKU^T`, and write singular values `s_1>=s_2>=s_3>=s_4>=0`. Assume `s_3>=a>0`, `s_4=sigma`, and the same row-leverage gate as above. If

`sigma/a <= 1/(4 sqrt(30))`,

then

`Z_3^disj(S):=sum_{|B|=|T|=3, B cap T=empty} det S[B,T]^2 >= a^6/160`.

Indeed let `S_3` be the top-three spectral truncation. If `L=s_1 s_2 s_3`, Lemma B gives

`Z_3^disj(S_3)>=L^2/40`.

In the spectral basis,

`|| wedge^3 S-wedge^3 S_3 ||_F^2
 = sigma^2(s_1^2s_2^2+s_1^2s_3^2+s_2^2s_3^2)
 <=3 L^2(sigma/a)^2`.

Projection onto the disjoint physical minor coordinates is contractive, so

`sqrt(Z_3^disj(S)) >= L/sqrt(40)-sqrt(3)L sigma/a >= L/(2sqrt(40))`.

Squaring gives `Z_3^disj(S)>=L^2/160>=a^6/160`.

Finally, for an iid fair physical-coordinate bipartition `I disjoint_union J`, each disjoint ordered pair `(B,T)` is captured as `B subset I`, `T subset J` with probability `2^-6`. Hence some literal original-coordinate cut satisfies

`e_3(S[I,J]S[I,J]^T) >= a^6/10240`.

If `A=D_0+S` with physical diagonal `D_0`, the same identity holds for `A[I,J]` because a physical diagonal has no cross-block entries.

This does not yet prove the unrestricted density bound: the arbitrary-rank projected-crossing receiver additionally requires its 3-volume row marginals to be at most `1/2` (or a valid heavy-row promotion). The result isolates that gate while retaining the nonzero fourth carrier direction exactly.
