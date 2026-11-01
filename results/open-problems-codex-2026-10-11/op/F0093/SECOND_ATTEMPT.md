# Second attempt: two new approaches (2026-10-12)

A. Treat the correlated walk as a walk on Gamma x Gamma and use entropy increments, rather than the shared-mask information. Both marginals being Liouville force this *pair* walk to have zero entropy rate. Compare its convolution powers to those with a fully independent prefix using domination of increment measures and a relative-entropy bound. Pursue an explicit growing-prefix bound under subexponential growth, then test whether it can reach a linear fraction of steps.

B. Use the self-similar recursion of the Grigorchuk generators a=(1,1)sigma, b=(a,c), c=(a,d), d=(1,b). Derive the coupled recursion for the two walks' sections and look for a contraction of correlation at each tree level, or a surviving statistic. This differs from merely mixing a fixed quotient: it must track section lengths, dependent induced increments, and the joint root permutations uniformly with depth. It is plausible but a naive independence assumption between sections would be false; no contraction theorem is presently established here.

Selected A: it admits a checkable quantitative calculation using only finite distributions and entropy monotonicity. The proposed estimates will be written out before any conclusion about the full problem.

Brain queries (read-only math_recall.py, 2026-10-12):
- Grigorchuk Liouville entropy noise sensitivity shared increments conditional entropy
- Kaimanovich Vershik entropy criterion Liouville convolution total variation zero two law
Returns: general entropy, noise operator and Pinsker cards; no directly applicable Grigorchuk quantitative theorem. Hints checked independently.
## Approach A: complete new proofs

All entropies use natural logarithms and all distributions have finite support at each finite time. Fix epsilon in (0,1). On G x G write lambda=mu tensor mu and nu=(1-epsilon)mu_diag+epsilon lambda. Write h_n=H(nu^{*n}), h_0=0.

### Lemma A1: entropy increments decrease
Let Z_1,Z_2,... be iid nu, W_n=Z_1...Z_n. Given Z_1, left multiplication is a bijection, so H(W_n|Z_1)=h_{n-1}. Hence a_n:=h_n-h_{n-1}=I(Z_1;W_n)>=0. Because Z_1 -> W_n -> W_{n+1} is a Markov chain, data processing gives a_{n+1}<=a_n. Therefore a_n<=h_n/n. If H(mu^{*n})=o(n), entropy subadditivity for the two marginals gives h_n<=2H(mu^{*n})=o(n); consequently a_n->0. This directly proves the relevant sublinear-entropy property of the pair walk. Calling it Liouville additionally uses the usual finite-entropy entropy criterion on its generated subgroup; that terminology is unnecessary for the estimates below.

### Lemma A2: dominated-prefix perturbation bound
Let theta be any probability on G x G with theta<=M nu^{*k} pointwise, M finite, and let n>=k. Set A~nu^{*k}, B~nu^{*(n-k)}, independently. Conditional on A=a, the law K_a of AB is a left translate of nu^{*(n-k)}. If p=nu^{*n}, the finite-alphabet conditional information identity gives
 sum_a nu^{*k}(a) D(K_a||p)=I(A;AB)=h_n-h_{n-k}.
Every K_a for nu^{*k}(a)>0 has support inside that of p. Joint convexity of relative entropy with its second argument fixed gives
 D(theta*nu^{*(n-k)} || p) <= sum_a theta(a)D(K_a||p)
 <= M(h_n-h_{n-k}).
Pinsker proves
 d_TV(theta*nu^{*(n-k)},nu^{*n}) <= sqrt(M(h_n-h_{n-k})/2).
No converse from TV to entropy is used. This proof compares distributions on the same pair group, not individual marginals.

### Proposition A3: replacing a growing prefix
Since nu>=epsilon lambda, expansion of convolution with nonnegative measures gives nu^{*k}>=epsilon^k lambda^{*k}. Apply A2 with theta=lambda^{*k}, M=epsilon^{-k}:
 d_TV(lambda^{*k}*nu^{*(n-k)},nu^{*n})
 <= sqrt(epsilon^{-k}(h_n-h_{n-k})/2).
For fixed k, h_n-h_{n-k}<=k a_{n-k+1}->0 whenever H(mu^{*n})=o(n). In fact there exists some k_n->infinity with k_n=o(n) for which this TV tends to zero: for every j choose increasing N_j>=j^2 such that for all n>=N_j, epsilon^{-j}j a_{n-j+1}<=1/j^2; possible since a_m->0. Define k_n=max{j:N_j<=n} (and zero before N_1). Then k_n<=sqrt(n), k_n->infinity, and the displayed squared bound is at most 1/(2k_n^2). The construction handles the changing k without an illicit exchange of limits.

### Proposition A4: quantitative logarithmic blocks under stretched-exponential growth
Assume |B_G(r)|<=exp(C r^alpha) for all positive integer r, with 0<alpha<1, and mu supported in B_G(1). Then h_m<=2log|B_G(m)|<=2C m^alpha. Lemma A1 gives a_m<=2C m^{alpha-1}. Therefore, for 1<=k<=m,
 h_m-h_{m-k}<=k a_{m-k+1}<=2C k (m-k+1)^{alpha-1}.
It follows from A3 that
 d_TV(lambda^{*k}*nu^{*(m-k)},nu^{*m})
 <=sqrt(C k epsilon^{-k}(m-k+1)^{alpha-1}).
Now assume mu symmetric, as in SRW. Both lambda and nu are invariant under coordinatewise inversion. For any i,j>=0 with i+j+k=n, consider the hybrid law nu^{*i}*lambda^{*k}*nu^{*j}. Convolution on the left by nu^{*i} contracts TV, giving the preceding bound with m=j+k. Applying inversion to both distributions instead reverses the order of convolution and gives the bound with m=i+k. Choose m=k+max(i,j)>= (n+k)/2. Consequently the hybrid TV is bounded by
 sqrt(C k epsilon^{-k}(max(i,j)+1)^{alpha-1}).
This holds uniformly over the block location. Take k=floor(c log n) with c>0 and c log(1/epsilon)<1-alpha. For large n, k<=n/2, max(i,j)+1>=n/4, and epsilon^{-k}<=n^{c log(1/epsilon)}. Thus the bound is at most
 sqrt(C 4^{1-alpha} c log n) n^{-(1-alpha-c log(1/epsilon))/2} ->0.
The floor, the negative exponent alpha-1, and the choice of the longer side are essential. A fixed polynomially long block is not justified by this domination estimate, because epsilon^{-k} overwhelms the polynomial entropy decrement.

### Grigorchuk application (external growth theorem as input)
The first Grigorchuk group with generators {a,b,c,d} has |B(n)|<=exp(C n^alpha) for some alpha<1, by Bartholdi's growth upper bound. The standard growth-equivalence constants can be absorbed into C. Therefore A4 applies to its SRW: replacing a block of floor(c log n) consecutive pair increments anywhere by independent-coordinate increments changes the n-step pair law by o(1), for any c<(1-alpha)/log(1/epsilon). This is a proved small-perturbation statement, not full noise sensitivity. The exact external theorem citation and checked exponent are recorded in LITERATURE.md.

### Where this stops
The desired independent endpoint law is lambda^{*n}; A3 reaches that law only with k=n. Its entropy bound then contains epsilon^{-n} h_n and is useless. Moving a logarithmic block around and iterating does not solve this: the intermediate reference walk becomes time-inhomogeneous, and the entropy decrement identity proved for iid nu cannot be reused without justification. Even a crude triangle sum would multiply a small bound by about n/log n and would not tend to zero at the proved rate. The absence of virtual real homomorphisms has not entered any lemma, so these lemmas cannot by themselves distinguish Grigorchuk from Z.
### Proposition A5: stronger bound using the centered likelihood ratio
The domination estimate can be sharpened without a new group-theoretic hypothesis. In A2, let r(a)=theta(a)/nu^{*k}(a) on its positive support and let chi2(theta||nu^{*k})=sum_a nu^{*k}(a)(r(a)-1)^2. Since E r=1,
 theta*nu^{*(n-k)}-p=sum_a nu^{*k}(a)(r(a)-1)(K_a-p).
Take l1 norms, divide by two, apply Cauchy-Schwarz in a, and use Pinsker separately for each K_a:
 d_TV(theta*nu^{*(n-k)},p)
 <=sum_a nu^{*k}(a)|r(a)-1| d_TV(K_a,p)
 <=sqrt(chi2(theta||nu^{*k}) sum_a nu^{*k}(a)d_TV(K_a,p)^2)
 <=sqrt(chi2(theta||nu^{*k})(h_n-h_{n-k})/2).
All KL divergences are finite on the specified positive support. This bound vanishes identically when theta=nu^{*k} and improves the dependence on the amount of perturbation.

For theta=lambda^{*k}, set A=sum_z lambda(z)^2/nu(z)=1+chi2(lambda||nu), over the finite increment support. On the k-step product space with law nu tensor ... tensor nu, the likelihood ratio L=product_{i=1}^k lambda(Z_i)/nu(Z_i) has E L=1 and E L^2=A^k. Given the product A_k=Z_1...Z_k (now a group-valued variable), its conditional expectation E(L|A_k=a) equals lambda^{*k}(a)/nu^{*k}(a), by summing over paths with that endpoint. Conditional Jensen applied to the square gives
 chi2(lambda^{*k}||nu^{*k})<=E(L-1)^2=A^k-1.
Therefore
 d_TV(lambda^{*k}*nu^{*(n-k)},nu^{*n})
 <=sqrt((A^k-1)(h_n-h_{n-k})/2).
For symmetric mu the same convolution/inversion argument as A4 gives uniformly over an independent block of length k with i+j+k=n,
 d_TV(nu^{*i}*lambda^{*k}*nu^{*j},nu^{*n})
 <=sqrt(C k (A^k-1)(max(i,j)+1)^{alpha-1}).
This proves logarithmic-block insensitivity for every c with c log A<1-alpha, using k=floor(c log n). For k=0 the distance is zero. A=1 (e.g. a deterministic increment) makes the laws exactly identical, so the logarithmic restriction is needed only when A>1.

If mu is uniform on d distinct generators, diagonal increment masses are nu(s,s)=[d-(d-1)epsilon]/d^2, lambda(s,s)=1/d^2; off-diagonal masses are nu(s,t)=epsilon/d^2, lambda(s,t)=1/d^2. Counting d diagonal and d(d-1) off-diagonal ordered pairs gives
 A=(d-1)/(d epsilon)+1/[d(d-(d-1)epsilon)]
  =1+(d-1)(1-epsilon)^2/[epsilon(d-(d-1)epsilon)].
These counts occur in the increment alphabet, even when the generators satisfy relations in the group; endpoint identifications are handled by Jensen, not by treating words as distinct endpoints.

For standard Grigorchuk SRW, d=4. At epsilon=1/4, A=40/13, so the allowed c is (1-alpha)/log(40/13), about 0.207 with Bartholdi's alpha (the earlier domination constant gave about 0.168). The target still requires replacing n steps, for which A^n grows exponentially. This improved estimate does not close the main gap.
### A rigorous barrier example: logarithmic-block insensitivity is not full sensitivity
Take G=Z, mu uniform on {-1,+1}, rho=1-epsilon in (0,1). Let k_n steps be fully independent and the other n-k_n steps use the correlated increment law nu, with k_n/n->theta<1. Order is irrelevant on this abelian group. The marginal endpoint laws are still mu^{*n}.
For u=1/sqrt(n), the characteristic expectation of cos(u(X_n+Y_n)) under this hybrid law is
 [cos(u)^2]^{k_n} [rho cos(2u)+(1-rho)cos(u)^2]^{n-k_n}.
Indeed each fully independent pair contributes cos(u)^2, and each unrefreshed pair contributes cos(2u); the characteristic functions are real. Taylor's formula gives cos(u)^2=1-1/n+O(n^{-2}) and rho cos(2u)+(1-rho)cos(u)^2=1-(1+rho)/n+O(n^{-2}). Taking logarithms, multiplying by k_n and n-k_n, and using k_n<=n shows that the total error is O(1/n), and the expectation tends to exp(-1-rho(1-theta)). For two independent endpoints the expectation is cos(u)^{2n}->exp(-1).
Since this cosine test has absolute value at most one, the difference of its expectations is at most twice TV. Consequently
 liminf_n d_TV(hybrid endpoint law,mu^{*n} tensor mu^{*n})
 >=(1/2)exp(-1)[1-exp(-rho(1-theta))]>0.
Thus even a fixed positive fraction theta<1 of fully independent steps need not yield endpoint independence on a Liouville group. In particular replacing O(log n) steps by independent ones is consistent with a surviving macroscopic correlation. This is a proved example showing the reduction's limitation; it is not a counterexample to F0093 because Z has a nonzero real homomorphism.
### Approach B boundary calculation: root action is harmless
A small check on the alternative approach is possible without assuming independence of sections. In the standard Grigorchuk tree action, only a flips the root; b,c,d fix it. Let U_n=(-1)^{root permutation of X_n} and V_n the analogous sign for Y_n. The uniform four-generator increment has mean sign 1/2, so E U_n=E V_n=2^{-n}. The mean product of the two coupled increment signs is (1-epsilon)+epsilon(1/2)^2=1-3epsilon/4; products over iid increment pairs give E U_n V_n=(1-3epsilon/4)^n.
For two signs with equal mean m and joint product mean c, their four atom probabilities are (1+u m+v m+uv c)/4, u,v in {-1,1}. Product marginals replace c by m^2. Summing absolute differences shows that their TV distance is |c-m^2|/2. Thus the exact root-projection distance is
 [(1-3epsilon/4)^n-4^{-n}]/2,
which tends to zero exponentially for fixed epsilon>0. This does not control deeper sections. The sections generated by the same steps are dependent, their induced walks are not iid copies of the original SRW, and an argument that treats them as such would fail. No recursive correlation contraction has been proved.

## Hostile-referee audit of the second attempt

- Entropy decrement identity uses an *endpoint prefix product*, not all prefix increments. Left multiplication by a fixed prefix is bijective even in a noncommutative group, so the entropy identity is valid. The data-processing proof of monotonicity concerns iid increments only.
- The pair entropy bound h_n<=2H(mu^{*n}) follows just from its two marginals, which remain identical to mu^{*n}. No implication "marginal Liouville implies every correlated pair law mixes independently" is asserted.
- In the KL comparison, the candidate prefix law must be absolutely continuous and bounded relative to nu^{*k}. This follows from nu>=epsilon lambda at the *increment* level and nonnegative convolution; collisions between words do not invalidate domination.
- The centered-likelihood proof explicitly subtracts p before Cauchy-Schwarz. Its input is chi-squared for the prefix law, not the endpoint chi-squared in the first attempt. Conditional Jensen justifies reducing from path likelihood to prefix-product likelihood.
- The block-in-the-middle estimate uses only contraction under a common convolution and inversion invariance. Inversion reverses convolution order in a noncommutative group, so it must swap i and j. Symmetry of mu guarantees nu and lambda have the required invariance.
- Because alpha-1 is negative, the entropy bound decreases when the retained side is longer. This is why max(i,j) is chosen; choosing min(i,j) would not give the stated uniform rate.
- Constants are fixed independently of n. For each fixed epsilon, c log A<1-alpha is imposed before n tends to infinity. No claim is made with epsilon varying or c at the equality threshold.
- The Bartholdi theorem is an external growth theorem, independently fetched and quoted; it does not state F0093. The Grigorchuk corollary is our argument using that theorem, not SOLVED_IN_LITERATURE.
- The Z barrier is a counterexample to a proposed *method implication*, not to the conjecture. It violates the virtual-real-homomorphism exclusion. The characteristic-function calculation proves its lower bound without invoking a joint CLT or taking an unbounded covariance test as a TV test.
- The level-3 quotient computation is finite and cannot determine infinite-group TV. It tests noncommutative convolution, reversal symmetry, and the finite-time entropy inequalities only.
- Applying the argument successively to n/log n blocks would require entropy identities for the new inhomogeneous laws and a summable accumulated error. Neither has been established. This precise obstruction remains after the improved likelihood bound.

## Completed computations and formal check

`second_experiments.py` used deterministic probability recursion at epsilon=1/4 on Z for n=16,32,64,128 and on the actual level-3 Grigorchuk quotient (128 elements) at n=60. It checked decreasing entropy increments and the finite-time prefix/block estimates. Results are saved immediately, one row at a time, in `second_experiments.jsonl` (32 rows). Infinite-line arrays cover the full reachable range, and no mass wraps before or at the final step. The largest saved history occupies about 68 MB, within the resource limit. The quotient was generated by the four tree permutations on the eight binary words of length three; a^2=b^2=c^2=d^2=1 and bc=d were checked. Noncommutative right multiplication, not coordinatewise bit addition, defined its transitions.

At n=128 on Z, replacing one step changes the pair law by TV 0.00575943, while its distance from product remains about 0.335763 (original distance about 0.340663). Replacing 32 of 128 steps still leaves TV about 0.216246 from product. These finite numbers agree with the proved characteristic-test barrier; they are not used to prove it.

`sharper_bound_checks.py` verified the A5 TV estimate on all 32 saved model/block cases. It also verified the formula 1+chi2(lambda||nu) exactly with Fraction arithmetic for 20 combinations of d and epsilon, including epsilon=1 (where A=1). It records alpha=log(2)/log(2/eta), c upper approximately 0.2069266754 for d=4, epsilon=1/4, and the Z characteristic-test lower bound. See `sharper_bound_checks.json`.

`prefix_exact_checks.py` separately verifies probability normalization, convolution domination nu^k>=epsilon^k lambda^k, and the exact chi-squared contraction chi2(lambda^k||nu^k)<=A^k-1 on the noncommutative S3 transposition walk for k=1,...,6. This checks the path-to-endpoint step with word collisions and periodicity. See `prefix_exact_checks.json`.

`PrefixDomination.lean` checks the finite positive-kernel averaging inequality behind A2. The first run failed because the minimal imports did not contain the finite-sum order lemma; the ordered-finset import was added, without changing the mathematical statement. The final `lake env lean` run from ~/lean_verify exited 0 in 84.613 seconds. It uses no sorry, native_decide, axiom declarations, or whole-Mathlib import. This formalizes only the displayed finite algebraic averaging step, not the entropy identities or the entire group conjecture. The final output is in `prefix_lean_check.txt`; the initial missing-import error is preserved separately.

## Final second-attempt verdict and precise remaining gap

PARTIAL. We proved the entropy-increment comparison, growing-prefix insensitivity under sublinear entropy, uniform logarithmic-block insensitivity under stretched-exponential growth (including Grigorchuk SRW by a checked growth theorem), the sharper likelihood bound, and the characteristic-test barrier on Z. Two new approaches were recorded; the entropy/convolution approach was pursued and the self-similar alternative was checked at the root only.

For full F0093, one still needs to control the accumulated effect of replacing a linear number of coupled increments, or find an independent self-similar correlation contraction that does use the absence of virtual real homomorphisms. The present bounds apply on Z too and therefore do not encode that algebraic exclusion. No full proof or counterexample for the stipulated class is obtained. No literature theorem resolving that full class has been found. All new claims above are proved conditional bounds or special cases, not a claimed solution.
