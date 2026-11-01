# Full four-coordinate QFORM theorem and a bound for every fixed dimension

**Status:** Proved. For every fixed n≥3, every real symmetric n×n matrix A with third singular value s3(A)≥1, every independent original-coordinate Xi with probability densities at most one, and arbitrary affine terms b·X+c, the quadratic Q=XᵀAX+b·X+c has an essentially bounded density. The bound obtained is C_n≤C n(1+G2), with the absolute archived rank-two half-Riesz constant G2. In particular n=4 is completely settled, for positive, negative, and mixed spectra and for rank three or four. C_n grows with n, so this does not establish the dimension-free conjecture.

The proof uses two verified lower-level results from `qform/structure.tex` and `qform/lower_levels.tex` in the research manuscript: (i) a principal k×k pivot B leaves a Schur complement S with N_S(1)≥N_A(1)−k; (ii) for an arbitrary independent cap-one quadratic with N(1)≥2 and arbitrary affine part, the truncated half potential H2=sup_s E[|Q−s|^−1/2; |Q−s|≤1] is at most an absolute G2. Also, N(1)≥1 implies the global logarithmic potential L=sup_s E log_+(1/|Q−s|)≤L0:=4+4log5. The rank-two half bound follows from the manuscript's pivot-half lemma or no-pivot lower:two theorem, with common threshold c*=10^−15 and G2=max(10^6,44c*^−1/2).

For clarity, the spectral Schur count can be checked directly for signed matrices, including singular A. Writing A in pivot blocks as [[B,C],[Cᵀ,D]] and S=D−CᵀB^−1C, the difference A−diag(0,S)=[[B,C],[Cᵀ,CᵀB^−1C]] has rank at most k. The singular-value rank-perturbation inequality therefore gives s_{j+k}(A)≤s_j(S) for every j≤n−k, proving N_S(1)≥N_A(1)−k. This is the rank-one step after a diagonal pivot and rank-two step after a saddle pivot; no positivity assumption is used.

## An original-product two-variable saddle estimate

Let X,Y be independent cap-one real inputs, B=[[a,b],[b,d]], and 0≤u<|b| with |a|,|d|≤u. The determinant ad−b²<0, so completing the square for arbitrary affine terms moves the critical point and target without affecting the two independent density caps. It is enough to consider q(x,y)=ax²+2bxy+dy² and t≠0. Put r=√(|t|/(4|b|)). On the level q=t, max(|x|,|y|)≥r, since |q(x,y)|≤(2|b|+2u)max(|x|,|y|)²≤4|b|max².

Split the level into |x|≥|y| and |y|>|x|. On the first sector, |∂_y q|=2|bx+dy|≥2(|b|−u)|x|. At fixed x, the allowed y interval has derivative of constant sign and therefore contains at most one root of q=t; alternatively, a two-root bound suffices. Coarea and f_Y≤1 bound its level density by [(|b|−u)|x|]^−1 f_X(x). The second sector gives the symmetric y expression. Since cap-one probability densities obey ∫_{|x|≥r} f_X(x)/|x|dx≤1+2log_+(1/r), the translated saddle satisfies

p_{q_B+linear}(t+t_crit)
≤ [2/(|b|−u)] [1+log_+(4|b|/|t|)].                   (1)

The inequality holds for an almost-everywhere density version and is uniform in affine shifts. It is intentionally generous by a factor two.

## A diagonal pivot or a robust saddle edge

Fix n≥3 and u=1/(4n). If some physical diagonal |a_hh|≥u, complete the square in the independent original X_h. The residual quadratic R in the other originals has Schur matrix S=A/a_hh and N_S(1)≥N_A(1)−1≥2. Conditioning on the other originals, the square-map density is at most |a_hh|^−1/2 |s−R|^−1/2. The archived rank-two half potential plus the tail |s−R|>1 give

||p_Q||∞≤2√n(1+G2).                                      (2)

Suppose instead every diagonal has modulus <u. Because N_A(1)≥3, ||A||_F²=Σ_j λ_j(A)²≥3. Subtract the diagonal Frobenius contribution <n u²=1/(16n), and average over n(n−1)/2 undirected off-diagonal edges. Some edge b=a_ij satisfies

|b|²≥[3−1/(16n)]/[n(n−1)]>2/n²,
so |b|>√2/n>u.                                         (3)

The principal two-variable block B on coordinates i,j is an invertible saddle. Complete the square in that original pair; conditional on the n−2 remaining independent originals, the 2D saddle receives a target s−R, where R is precisely a quadratic with Schur matrix S=A/B and an arbitrary affine part. The Schur count gives N_S(1)≥N_A(1)−2≥1. Apply (1), then the archived global logarithmic potential to R:

p_Q(s)≤ [2/(|b|−u)] [1+E log_+(4|b|/|s−R|)]
≤ C n (1+L0).                                              (4)

For the last inequality, if |b|≤1 then (|b|−u)^−1≤n/(√2−1/4) and log_+(4|b|)≤log4; if |b|>1 then (|b|−u)^−1 and log(4|b|)/(|b|−u) are absolute bounded. The event s=R has probability zero because its logarithmic potential is finite. Equations (2)–(4) prove the theorem with C_n≤C n(1+G2).

## Explicit four-coordinate constants and scope

For n=4 one can improve the convenient diagonal threshold to 1/4. If all four |a_ii|<1/4, then Σ_i a_ii²<1/4 and the six off-diagonal edges carry Σ_{i<j}a_ij²>11/8. Hence one edge obeys |b|²>11/48, while |ad|<1/16. This gives |b|>√(11/48)>1/4, det B<−1/6, and an absolute constant in (1). The Schur residual has N_S(1)≥1 and global logarithmic potential ≤L0. If a diagonal is at least 1/4, (2) improves to 2(1+G2). Thus the full four-original theorem holds with a universal bound independent of A, the source laws, and all affine terms. The same proof for general fixed n has a factor n and leaves the original dimension-free problem unresolved.
