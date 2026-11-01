# R11 I0054 — idea before code: equal-weight sparse translation compiler

Date: 2026-09-19 UTC.

Target: strengthen U053/C074 by forbidding tuned Caratheodory weights. Retained translations must all carry the same weight.

Methods for this run: #9 RANDOMIZE, #19 MAKE IT AN ALGORITHM, #26 HUNT THE SPORADIC CASE.

## Candidate U054

Keep the full-translation C072 power-permutation architecture. For a cutoff K, let G_t be the vector of all specified split rates contributed by translation t, normalized so the full C072 generator vector is p^{-1} sum_t G_t.

For a coordinate A|B and any cross-pair a in A, b in B, the translation contribution g_t(A|B) is bounded by the pair-separation contribution r_t(a,b). If x=phi(t+a), y=phi(t+b), then

r_t(a,b) = (1/2) |L_p(y)-L_p(x)|,
L_p(r)=H_r-H_{p-1-r}.

Because t -> phi(t+a) and t -> phi(t+b) are permutations of F_p,

p^{-1} sum_t r_t(a,b)^2 <= p^{-1} sum_{r=0}^{p-1} L_p(r)^2.

The latter is uniformly bounded: symmetry, H_n^2 <= 2n, and the integral bound for log^2(1/x) give a universal constant (8 is enough).

Therefore every generator coordinate has population second moment <=8. If S is a uniformly random L-subset of translations, sampling without replacement gives

Var( |S|^{-1} sum_{t in S} g_t(c) ) <= 8/L.

A union bound over D_K=(3^K-2^{K+1}+1)/2 coordinates gives

P(max_c |q_S(c)-q_full(c)| > eps) <= 8 D_K/(L eps^2).

Hence, for every L -> infinity, choose eps=L^{-1/8} and K -> infinity slowly enough that 16 D_K <= L^{3/4}. Then some equal-weight L-subset approximates every split rate on every subset of [K] within eps. Lexicographically choose the first such subset. This should imply generator convergence, path-TV convergence on each fixed restriction, and the same CTCS(infinity) projective limit.

This removes the tuned positive rational weights from U053. The support threshold should remain sharp: L_N -> infinity is necessary by the same order-cut counting obstruction and sufficient even with equal weights.

## Candidate C075

Use a very slowly divergent equal-weight budget B_N=max(2,ceil(log log(N+e^e))) and ell_N=min(B_N,p_N). Define eps_N=ell_N^{-1/8}; define K_N as the largest k with 16 D_k <= ell_N^{3/4}, or K_N=1 if none. Among ell_N-subsets satisfying the split-test tolerance on [K_N], choose lexicographically first; if ell_N=p_N use all translations. Each retained (t,u) clock has rate p_N/[2 ell_N u(p_N-u)].

At N=4 the rule has p=5,d=3,ell=2,K=1, so the chosen support should be {0,1}. This gives an immediate finite non-equivalence witness; exact arithmetic will be checked only after this note is committed.

## Method #26 target

Search the p=5,d=3 small case for proper equal-weight subsets that exactly reproduce the full generator on K=2 or K=3. A sporadic exact design would improve the construction. If none exists, record that failure rather than force a certificate into the theorem.
