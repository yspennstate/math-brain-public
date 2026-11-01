SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T15:20:23Z.
attacking: the exact-rank-three indefinite collision collar: relate determinantal-triple disjointness, pair-area energy, and the partner overlap-two star identity, then isolate the near-coloop survivor.

# Early substantive checkpoint

Let `A=R M R^T`, `R^T R=I_3`, with `M` invertible of signature `(2,1)` or `(1,2)`. Put

- `v_K=det(R_K)^2` for physical triples `K`;
- `c_i=||r_i||^2=sum_{K contains i} v_K`;
- `g_{ij}=||r_i wedge r_j||^2=sum_{K contains {i,j}}v_K`;
- `C2=sum_i c_i^2`, `G2=sum_{i<j}g_{ij}^2`, `V2=sum_K v_K^2`;
- `D=sum_{K cap L=empty}v_Kv_L` for two independent determinantal triples.

A direct inclusion-exclusion calculation gives the exact collision identity

`D = 1 - C2 + G2 - V2`.                                                (C1)

The designated partner fleet04/B11 r6 proves, for each physical pair `S`,

`W2(S)=|det M|^2[g_S^2-sum_{K contains S}v_K^2]`.

Summing over all pairs therefore gives the new global partner application

`Wtot/|det M|^2 = G2 - 3V2`,                                           (C2)

and hence

`D = 1-C2 + Wtot/|det M|^2 + 2V2`.                                   (C3)

Thus the determinantal-triple collision has exactly three currencies: leverage deficit, overlap-two star energy, and triple concentration.

Immediate paid wings, with `s=min |lambda(M)|`:

1. If `C2<=1-delta`, then `D>=delta`. The preceding fleet03/B11 r34 random-cut theorem and grouped rank-three cross compiler yield

`||p_Q||_inf <= 6e/[s delta^(1/6)]`, with a continuous density.

2. If `C2>=1+delta`, then from (C1), `G2>=delta`. Since `sum g_ij=3`, some pair has `g_ij>=delta/3`. The completed area compiler recorded in fleet04/B11 r6 gives

`||p_Q||_inf <= 128 sqrt(6)/[s sqrt(delta)]`.

For `delta=1/4`, the two constants are respectively `6e 2^(1/3)<20.549` and `256 sqrt(6)<627.070`.

The only exact-rank-three collision state not paid by these two wings is therefore the collar `|C2-1|<delta`; after also using r34, its genuinely new part has `max_i c_i>=1/3`.

A sharpness family for the structural reduction is the exact coloop frame `r_0=e_1` and `r_j=sqrt(2/m)(0,cos(2pi j/m),sin(2pi j/m))`. It has `C2=1+4/m`, `D=0`, and `max g_ij=2/m`. Thus collision/pair-area currencies really can vanish while the frame tends to a coloop; this is not a QFORM counterexample because the exact-coloop density branch is already paid by a different theorem.

Full target remains open. The next calculation is to formalize (C1)-(C3), verify the coloop family, and state precisely how the third direction appears in the two paid wings without invoking post-rotation independence.
