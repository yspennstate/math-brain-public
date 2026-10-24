# A self-contained proof of the deterministic input

2026-10-12. This proves the version of Zerner (2002), Lemma 3, used in FRESH_HYPERPLANE_PROOF.md. The proof follows its nested-set counting mechanism, with simpler constants. It uses no probability assumptions.

Let x_0=0,x_1,... be a nearest-neighbor path in Z^d, and let h_n=x_n dot e for a signed unit coordinate vector e. Assume limsup h_n/n>0. For integers m>=0, L>=1 put T_m=inf{n:h_n=m}, S_{m,L}={n:T_m<=n<T_{m+L},h_n=m}, d_{m,L}=diameter(S_{m,L}), and F_{M,L}(c)=(M+1)^{-1} sum_{m=0}^M 1{d_{m,L}<=c}. All T_m are finite: the assumed limsup makes h_n unbounded above and steps change h by at most one. Each S_{m,L} is a nonempty finite set with minimum T_m. As L increases, these sets are nested.

We prove sup_{c>=0} inf_{L>=1} limsup_M F_{M,L}(c)>0.

Choose a real delta>0 and times n_k increasing to infinity with h_{n_k}>=delta n_k. Necessarily delta<=1. Let M_k=floor(delta n_k/2); these tend to infinity (a strictly increasing subsequence can be taken). Put C=2/delta. For every fixed L and all sufficiently large k, M_k+L<=delta n_k, so the nearest-neighbor property gives T_{M_k+L}<=n_k<C(M_k+1). Distinct sets S_{m,L}, m=0,...,M_k, contain times spent in distinct planes, and all their elements are integers less than T_{M_k+L}. Therefore

sum_{m=0}^{M_k} #S_{m,L} <= T_{M_k+L} < C(M_k+1).       (A)

Also d_{m,L}<=T_{m+L}-T_m. Split the sum of the latter differences into residues modulo L. In each residue it telescopes, with terminal hitting time at most T_{M_k+L} and initial hitting time nonnegative. There are at most L residues, giving

sum_{m=0}^{M_k} d_{m,L} <= L T_{M_k+L} < C L(M_k+1).   (B)

Suppose the claimed supremum were zero. Since all quantities are nonnegative, for EVERY fixed c we would have inf_L limsup_M F_{M,L}(c)=0. Set L_0=1. Given L_i, put c_i=6 C L_i. Choose L_{i+1}>L_i with limsup_M F_{M,L_{i+1}}(c_i)<1/3. This is possible by the zero infimum and monotonicity of F in L.

For fixed i, (B) with L_i shows that along M_k, eventually the fraction of m with d_{m,L_i}>=c_i is at most 1/6. The choice of L_{i+1} shows that eventually the fraction with d_{m,L_{i+1}}<=c_i is less than 1/3. For every m at least one of the following is true:

- d_{m,L_i}>=c_i;
- d_{m,L_{i+1}}<=c_i;
- d_{m,L_i}<d_{m,L_{i+1}}.

Indeed if the first two are false the third follows from d_{m,L_i}<c_i<d_{m,L_{i+1}}. Consequently the fraction of strict diameter increases is eventually greater than 1/2, and in particular at least 1/3.

Choose an integer I>3C. All preceding eventual bounds for i=0,...,I-1 hold simultaneously for sufficiently large k. Nested finite sets with a strict increase in diameter have a strict increase in cardinality. For each m, the number of these I strict diameter increases is therefore at most #S_{m,L_I} (in fact at most #S_{m,L_I}-1). Sum over m and apply (A) at the fixed L_I:

I/3 <= (M_k+1)^{-1} sum_{m=0}^{M_k} sum_{i=0}^{I-1}
            1{d_{m,L_i}<d_{m,L_{i+1}}}
     <= (M_k+1)^{-1} sum_{m=0}^{M_k} #S_{m,L_I}
     < C.

This contradicts I>3C. The desired positive supremum follows. No bounds uniform in L or exchange of L and k were used: each of the finitely many L's is fixed before k tends to infinity.

Referee checks: (i) all hitting times are finite before diameters are used; (ii) the count bound (A) counts time instants, not distinct spatial sites; (iii) residue sums telescope because first-hit times are increasing in level; (iv) M_k need only tend to infinity to inherit a limsup_M upper bound; (v) strict set growth is necessary for strict diameter growth; (vi) all limit statements are applied to a finite list before the final contradiction.
