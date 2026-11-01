Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but authenticated runtime metadata does not establish GPT-6/maximum, so this artifact does not claim it.

# PROB10-08 artifact — a source-admissible affine Cayley stress test that defeats the Sarnak–Xue / collision route

Status: **PROVED auxiliary obstruction / source remains OPEN / cutoff for the stress-test family NOT proved / independent audit pending / worldwide novelty UNVERIFIED**.

This artifact is for Salez, arXiv:2508.21055, Problem 2.3, under the rate-one continuous-time SRW convention. It does **not** concern the posted Abelian-Cayley/product-condition target.

The point of this iteration is deliberately different from the preceding three PROB10-08 runs. Those runs weakened Altschuler's long-range-expansion hypothesis, transferred entropy through a large LRE quotient, and truncated LRE at the pre-entropic scale. The present run instead looks for a source-admissible family on which the most obvious transitivity-based Green-function replacement of Altschuler's entropy argument provably fails.

## 1. Inputs and current literature boundary

Primary source: Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.3: every bounded-degree vertex-transitive expander sequence should exhibit total-variation cutoff.

Current primary lead: Dylan J. Altschuler, *Long-range expanders: construction and cutoff*, arXiv:2609.14945v1, submitted 14 September 2026. A fresh bounded check in this run found the arXiv record still at v1 and found no correction/erratum. The proof uses LRE first to obtain tree-rate growth on the oriented-edge NBRW state space (Lemma 3.2), then a forest argument to obtain near-maximal Shannon entropy for the NBRW endpoint (Lemma 3.3 / Proposition 3.1), and then spectral entropy cleanup.

Comparison source: Konstantin Golubev and Amitay Kamber, *Cutoff on Graphs and the Sarnak-Xue Density of Eigenvalues*, arXiv:1905.11165v3. Their parameter-A=1 Sarnak-Xue density condition, together with expansion, yields cutoff; for a `(Q+1)`-regular graph it requires, for every `p>2` and `epsilon>0`,

`#{i : p(lambda_i)>=p} << n^(2/p+epsilon)`.

Here `p(lambda)` is defined by the larger nonbacktracking root `theta`, with

`theta = Q^(1-1/p(lambda))`.

Stress-test source: Milan Haiman, Carl Schildkraut, Shengtong Zhang and Yufei Zhao, *Graphs with high second eigenvalue multiplicity*, BLMS 54 (2022), arXiv:2109.13131. Their Theorem 1.4 constructs infinitely many 18-regular Cayley graphs on

`Gamma_q = SL(2,q) semidirect F_q^2`

with second-eigenvalue multiplicity at least `q^2-1`, hence at least `n_q^(2/5)-1`, where

`n_q = q^3(q^2-1)`.

The paper uses a 16-element symmetric set `S subset Pi=SL(2,q)` whose Cayley graph has adjacency spectral gap at least 4, and adds `t,t^{-1}` outside `Pi`. For the argument below, specialize along an infinite odd-q LPS subfamily and take `t=(I,e)` for one nonzero `e in F_q^2`; then `t != t^{-1}`.

A bounded current search found no paper asserting cutoff for this exact affine Haiman family and no source explicitly recording the uniform spectral-gap estimate proved below. This is only negative search evidence, not a novelty certificate.

## 2. New theorem A: the affine Haiman family is source-admissible

Let `Q=q^2`, `Pi=SL(2,q)`, `V=F_q^2`, and `Gamma=Pi semidirect V`. Let `S subset Pi` be the lifted LPS generating set from Haiman et al., so `|S|=16` and the adjacency operator of `Cay(Pi,S)` has top eigenvalue 16 and every other eigenvalue at most 12. Let `e in V\{0}`, let `t=(I,e)`, and define

`G_q = Cay(Gamma, S union {t,t^{-1}})`.

Then `G_q` is 18-regular and vertex-transitive.

### Theorem A

For every odd `q` in the above family,

`lambda_2(A_Gq) <= 15 + sqrt(3)`.

Consequently the normalized one-sided spectral gap satisfies

`1-lambda_2(P_Gq) >= (3-sqrt(3))/18 > 0`.

Thus `(G_q)` is a bounded-degree vertex-transitive expander sequence and is admissible for Salez Problem 2.3.

### Proof

Write the full adjacency operator as

`A = A_S + B`,  `B = R_t + R_(t^{-1})`.

As in Haiman et al., the regular representation decomposes into irreducible representations of `Gamma`. Their Mackey/Frobenius argument shows that

`Ind_Pi^Gamma(1) = 1 direct-sum phi`,

where `phi` is irreducible of dimension `Q-1`, and these are exactly the irreducibles whose restriction to `Pi` contains a trivial vector.

If an irreducible `rho` is neither `1` nor `phi`, then `rho|_Pi` has no trivial component. The adjacency-gap-4 hypothesis on `Cay(Pi,S)` therefore gives

`lambda_max(A_(S,rho)) <= 12`.

Since `||B_rho||<=2`,

`lambda_max(A_rho) <= 14`.                                      (2.1)

It remains to bound the `phi` block.

Realize `1 direct-sum phi` as the permutation representation of `Gamma` on `Gamma/Pi`, identified with the affine space `V`. The `Pi`-action has exactly two orbits, `{0}` and `V\{0}`. Hence the 16-eigenspace of `A_S` on this permutation representation consists exactly of the functions constant on those two orbits. One direction is the global constant (the trivial representation); the orthogonal direction lies in `phi`.

Use the probability inner product

`<f,g> = Q^(-1) sum_(x in V) f(x) conjugate(g(x))`.

A normalized generator of this one-dimensional top space in `phi` is

`u(0)=sqrt(Q-1)`,

`u(x)=-1/sqrt(Q-1)` for `x!=0`.

Thus, if `w perpendicular u` lies in `phi`, then the gap-4 hypothesis gives

`<w,A_S w> <= 12 ||w||^2`.                                     (2.2)

In the affine action, `t` is translation by `e`. Because `q` is odd, `e` and `-e` are distinct. A direct count gives

`<u, B u> = -2/(Q-1) =: b_Q`,                                  (2.3)

and

`||B u||^2 = 2(Q-2)/(Q-1) < 2`.                                (2.4)

Therefore the component of `Bu` perpendicular to `u` has norm at most `sqrt(2)`.

Take a unit vector `f=alpha u+w` in `phi`, with `w perpendicular u`, `||w||=s`, and `alpha^2+s^2=1`. From (2.2), `||B||<=2`, (2.3), and (2.4),

`<f,Af>`

` <= (16+b_Q) alpha^2 + 14 s^2 + 2 sqrt(2)|alpha|s`.

The largest possible value is bounded by the top eigenvalue of

`[[16, sqrt(2)], [sqrt(2), 14]]`,

which is

`15+sqrt(3)`.

Together with (2.1), every nontrivial adjacency eigenvalue is at most `15+sqrt(3)`. Since the degree is 18, the normalized one-sided gap is at least `(3-sqrt(3))/18`. QED.

### Remarks on assumptions

1. This is a one-sided gap, exactly what Salez's continuous-time expander definition needs. No absolute-gap claim is made.
2. The specialization to pure translation `t=(I,e)` is allowed by Haiman et al.'s construction; restricting to an infinite odd-q LPS subfamily avoids the order-two translation degeneracy in characteristic two.
3. Haiman et al. prove connectedness and the large second-eigenvalue multiplicity. The argument above adds a uniform upper bound on that second eigenvalue for this specialized family.

## 3. New theorem B: this source-admissible family violates Sarnak-Xue density at A=1

Haiman et al. prove that the second adjacency eigenvalue `mu_q` of `G_q` satisfies

`mu_q >= |S|-2 = 14`

and has multiplicity at least

`m_q >= q^2-1 >= n_q^(2/5)-1`.                                 (3.1)

Normalize by degree 18. Thus the corresponding normalized eigenvalue satisfies

`lambda_q = mu_q/18 >= 7/9`.                                    (3.2)

For an 18-regular graph, the nonbacktracking branching parameter in Golubev-Kamber is `17`. At `lambda=7/9`, the larger nonbacktracking root is

`theta_0 = (18 lambda + sqrt((18lambda)^2-4*17))/2`

`        = 7+4sqrt(2)`.

Its p-value `p_0` is defined by

`theta_0 = 17^(1-1/p_0)`.

Since `theta_0>12` and

`12^6 = 2,985,984 > 17^5 = 1,419,857`,

we have `theta_0>17^(5/6)`, hence

`p_0>6`.                                                        (3.3)

The p-value is increasing with a positive eigenvalue above the Ramanujan interval, so each of the `m_q` copies in (3.1) has p-value greater than 6.

If this family satisfied the Sarnak-Xue density property with parameter `A=1`, then taking `p=6` and, say, `epsilon=1/30` would give

`m_q << n_q^(1/3+1/30) = n_q^(11/30)`.

But (3.1) gives `m_q >= n_q^(2/5)-1 = n_q^(12/30)-1`, a contradiction for large `q`.

### Theorem B

The source-admissible affine family `(G_q)` does **not** satisfy the Sarnak-Xue density property with parameter `A=1`.

This means the Golubev-Kamber `A=1` cutoff theorem cannot settle Salez Problem 2.3 by proving that transitivity plus a fixed spectral gap automatically implies Sarnak-Xue density.

This does **not** show that `(G_q)` fails cutoff. It only gives a concrete source-admissible family outside that sufficient mechanism.

## 4. New theorem C: exact endpoint Green-function / collision obstruction at the ambient tree radius

The preceding result can be stated directly in the language suggested by the current PROB10 priority.

Let `K_k` denote the length-k nonbacktracking endpoint kernel on an undirected 18-regular graph. Because path reversal is a bijection, `K_k` is symmetric; equivalently it is a polynomial in the adjacency operator. If the graph is vertex-transitive, the diagonal of `K_k^2` is constant, and therefore for every vertex `x`,

`sum_y K_k(x,y)^2 = (1/n) sum_i kappa_k(lambda_i)^2`,            (4.1)

where `kappa_k(lambda_i)` is the eigenvalue of `K_k` corresponding to the normalized adjacency eigenvalue `lambda_i`.

For a positive eigenvalue with nonbacktracking root `theta>sqrt(17)`, the exact Golubev-Kamber formula has only nonnegative terms, so

`kappa_k(lambda) >= [theta^k]/[18*17^(k-1)]`

`                  = (17/18)(theta/17)^k`.                      (4.2)

For the high-multiplicity eigenvalue of `G_q`, (3.3) gives `theta/17 > 17^(-1/6)`. Hence

`kappa_k(lambda_q) >= (17/18) 17^(-k/6)`.                       (4.3)

Take

`k_q = floor(log_17 n_q)`.

Then `17^(-k_q/6) >= n_q^(-1/6)`. Combining (4.1), (4.3), and `m_q >= n_q^(2/5)-1`, for all large q,

`sum_y K_(k_q)(x,y)^2`

` >= (m_q/n_q) (17/18)^2 n_q^(-1/3)`

` >= c n_q^(-14/15)`                                            (4.4)

for an absolute `c>0`, uniformly in `x`.

The uniform distribution has collision probability `1/n_q`. Thus the collision excess satisfies

`n_q * sum_y K_(k_q)(x,y)^2 >= c n_q^(1/15)`.                   (4.5)

### Theorem C

There is a bounded-degree vertex-transitive spectral-expander sequence, admissible for Salez Problem 2.3, for which the NBRW endpoint at the ambient tree-entropic radius `floor(log_17 n)` is polynomially far from uniform in chi-square / collision scale.

Consequently, a proof strategy that tries to replace Altschuler's LRE hypothesis by a universal transitivity-plus-gap estimate of the form

`sum_y K_(floor(log_(d-1)n))(x,y)^2 <= n^(-1+o(1))`

cannot work.

Again, this is **not** a TV lower bound and is **not** a failure of Shannon near-maximal entropy. Shannon entropy can be much larger than Renyi-2 entropy. The conclusion is deliberately limited to the Green-function/collision route.

## 5. Why this is genuinely different from the exhausted R16 routes

The old R16/I0112 sequence already exhausted:

- fixed product/varentropy constructions;
- synchronous tensor products;
- moving-window/local-Poincare attempts;
- Hecke/information-curvature attempts;
- the global subcommutation recovery, including the regular-tree harmonic obstruction.

The preceding PROB10-08 runs then exhausted three variants of Altschuler's LRE architecture.

Theorems A-C above do not tensorize an already-known cutoff example and do not add another LRE weakening. They produce a source-admissible, explicitly represented Cayley family and prove that a natural spectral-density / NBRW collision replacement for LRE fails on it.

## 6. Third approach examined: semidirect Fourier/Feynman-Kac route toward cutoff of the stress test

The stress-test family is attractive because the full walk has an exact Markov-additive decomposition that does not appear in the earlier R16 routes.

Use semidirect multiplication

`(M,x)(N,y)=(MN, x+My)`.

For rate-one continuous-time SRW on the 18 generators, Poisson thinning gives:

- subgroup moves from `S` at total rate `16/18=8/9`;
- translation moves `t,t^{-1}` at total rate `2/18=1/9`;
- the subgroup coordinate `M_t` is therefore an `S`-walk on `Pi` run at rate `8/9`, independent of the translation clock;
- at a translation time `tau`, the additive coordinate changes by `+M_tau e` or `-M_tau e` with equal probability.

Let `chi_xi` be a nontrivial additive character of `V`. Conditional on the entire subgroup path `(M_s)_(0<=s<=t)`, the Poisson exponential formula gives the exact identity

`E[chi_xi(X_t) | (M_s)]`

` = exp{ (1/9) integral_0^t [ Re chi_xi(M_s e) - 1 ] ds }.       (6.1)

Under uniform `M`, the vector `Me` is uniform on `V\{0}`, and therefore

`E_uniform[Re chi_xi(Me)] = -1/(Q-1)`.                          (6.2)

Thus the stationary mean of the potential in (6.1) is `-Q/(Q-1)`, bounded away from zero. Formula (6.1) converts the remaining cutoff question for the growing affine extension into a Feynman-Kac / additive-functional problem over the lifted LPS walk.

I did **not** promote this to a cutoff theorem. A direct Parseval bound sums over `Q-1` characters and pays a logarithmic L2 cost which does not capture the TV effect of a single well-randomized translation; moreover the joint `(M_t,X_t)` law, rather than only the `X_t` marginal, must be controlled. The missing ingredient is a regeneration/entropy estimate showing that, during the subgroup entropic window, one translation direction is effectively uniform relative to the accumulated additive state without paying the full L2 character count.

This is the cleanest non-LRE next route found in this iteration.

## 7. Three approaches and outcomes

1. **Affine high-multiplicity stress test (representation theory): SUCCESS AS OBSTRUCTION.** Theorem A proves the Haiman affine Cayley family is a genuine bounded-degree vertex-transitive expander; Theorem B proves it violates Sarnak-Xue density at A=1.
2. **Endpoint NBRW Green function (self-adjoint polynomial instead of oriented-edge nonnormality): SUCCESS AS OBSTRUCTION.** Theorem C gives an exact polynomial collision excess at the ambient tree radius, so transitivity+gap cannot imply the naive near-uniform collision estimate.
3. **Semidirect Fourier / Feynman-Kac analysis: PARTIAL.** Formula (6.1) is exact and points to an adaptive information mechanism, but the required TV/entropy regeneration estimate is not yet proved.

## 8. Source before/after and metric accounting

**Source before:** Salez Problem 2.3 OPEN.

**Source after:** still OPEN. No cutoff theorem for the new affine stress-test family is claimed, so the PROB10 graph-class/window metric does not move this run.

**What did move:** the obstruction is now source-admissible rather than an abstract or nontransitive example. The family is proved to have a uniform one-sided gap, to lie outside Sarnak-Xue A=1, and to violate the ambient-radius near-uniform NBRW collision estimate by a polynomial factor.

**Historical `W_exp`:** unchanged at the prior provisional `1/2` floor; no attempt is made to relabel this obstruction as a better exponent.

**Remaining full-scope gap:** prove a TV/entropy estimate that survives this affine family and other local-product stress tests. The immediate delimited target is to exploit (6.1) to control the joint affine walk through a regeneration or conditional-entropy argument, not through L2 Fourier summation and not through ambient-degree tree growth.

No finite mixing plot was used, and no asymptotic claim was inferred from finite numerics.