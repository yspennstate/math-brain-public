SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T05:18:47Z.
attacking: pair-anchored E3 promotion, so the multicarrier volume obstruction collapses to the one-heavy-row branch.

# Early calculation — pair-anchored E3 promotion

Let M=A[I,J] be a literal original-coordinate crossing and fix physical rows a,b. Put D2=det Gram(m_a,m_b)>0 and project every other row orthogonally off span(m_a,m_b), obtaining rows c_r and matrix C. Define the pair-anchored third-volume mass

W_ab := sum_{r notin {a,b}} det Gram(m_a,m_b,m_r).

The Gram-Schur identity gives exactly

W_ab = D2 * E1(C),  E1(C)=sum_r ||c_r||^2.

Let alpha_r=||c_r||^2/E1(C).

If every alpha_r<=1/2, apply the checked grouped projected-crossing theorem (d2f970d..., NEW_PROJECTED_CROSSING.md) with k=2 literal hubs, ell=1 and d=3. The hub density cap is one, the hub-to-right singular product is sqrt(D2), and the ell=1 entropy term cancels. Hence

||p_Q||_inf <= 3*2^(5/6) D2^(-1/6) E1(C)^(-1/6)
             = 3*2^(5/6) W_ab^(-1/6).

If some alpha_c>1/2, then D3=det Gram(m_a,m_b,m_c)=alpha_c W_ab>W_ab/2. Condition the other left coordinates. The retained three literal rows have exact cross rank three. Account03/B04 r32 exact-cross-rank product Plancherel, with the three-coordinate side density cap one and the opposite three-dimensional product projection cap 2^(3/2), gives

||p_Q||_inf <= 3*sqrt(2) D3^(-1/6)
             < 3*2^(2/3) W_ab^(-1/6)
             < 3*2^(5/6) W_ab^(-1/6).

Thus pair-anchored E3 mass alone is a row-marginal-free receiver; no E4 packet is needed. Both branches have an integrable characteristic-function envelope and hence a continuous C0 density.

Immediate canonical-volume corollary: if z_S=det Gram(M_S), Z=sum_{|S|=3}z_S, and alpha_i=P(i in S), then for any two rows a,b with alpha_a+alpha_b>1,

W_ab/Z=P(a,b in S)>=alpha_a+alpha_b-1,

so

||p_Q||_inf <= 3*2^(5/6)[(alpha_a+alpha_b-1)Z]^(-1/6).

In particular two canonical E3 row marginals at least 3/4 imply

||p_Q||_inf <= 6 Z^(-1/6).

Therefore the D' obstruction cannot remain genuinely multicarrier: after this exit, a surviving max-marginal >=3/4 state has at most one such heavy row.
