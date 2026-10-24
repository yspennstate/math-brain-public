# ATTEMPT: F0093

Date: 2026-10-12. This is a partial investigation, not a solution.

## Statement and scope
Let Gamma be infinite and finitely generated, S a finite symmetric generating set, and mu uniform on S. Let s_i be independent mu increments. Independently mark each index refreshed with probability epsilon in (0,1); replace marked increments by independent mu samples t_i and retain unmarked ones. Set X_n=s_1...s_n and Y_n=t_1...t_n. The target is d_TV(Law(X_n,Y_n),mu^{*n} tensor mu^{*n})->0 for every fixed epsilon, assuming (Gamma,mu) is Liouville and no finite-index subgroup has a nonzero homomorphism to R. The Grigorchuk instance is also unresolved here. TV means half the l1 norm.

Kalai Section 3.3.4, PDF page 22, matches the supplied statement. Note a distinction: the existential question and the general conjecture are different. Recent special-case results answer the former but do not prove the latter. Also the source's assertion that *any* virtual real homomorphism obstructs sensitivity is too broad for arbitrary measures: lazy dihedral walks are sensitive. This does not refute the stated sufficient condition.

## 1. A valid shared-information sufficient condition
Let C record the refresh mask R and all increments at indices outside R. Given C, X_n and Y_n are independent with the same conditional law K_C: each unrecorded increment in each word is independently sampled from mu. Set p=mu^{*n}; hence E K_C=p and P=E(K_C tensor K_C).
For every realization C,
K_C tensor K_C-p tensor p=(K_C-p) tensor K_C+p tensor(K_C-p).
The l1 norm of a tensor product with a probability is the l1 norm of its other factor. The triangle inequality and averaging give
 d_TV(P,p tensor p) <= 2 E d_TV(K_C,p).
Pinsker followed by Cauchy-Schwarz gives
 d_TV(P,p tensor p) <= sqrt(2 I(X_n;C)).
All spaces here are finite at each n, so conditional laws and entropies exist without integrability issues. Thus I(X_n;C)->0 is sufficient. Data processing also gives I(X_n;Y_n)<=I(X_n;C), but it does not make the right side a necessary condition.

The earlier ledger F0093-A001 incorrectly inferred both necessity and that TV independence implies vanishing mutual information. Here is a full counterexample to the latter inference (a general probabilistic example, not a group counterexample): let X be uniform on M=2^k values; independently take B Bernoulli(delta) with delta=1/k, and let Y=X if B=1 and an independent uniform sample otherwise. Both marginals are uniform. Its TV distance from product is delta(1-1/M)->0. In natural logarithms,
 I(X;Y,B)=I(X;B)+I(X;Y|B)=delta log M=log 2.
By the chain rule I(X;Y)=log 2-I(X;B|Y), and 0<=I(X;B|Y)<=h(delta). Therefore I(X;Y)->log 2, not zero. Finite-alphabet entropy identities justify every equality. This counterexample explains why an entropy proof must establish the stronger estimate rather than assume it.

## 2. Exact endpoint matrix criterion
For p(g)>0 define f_g(s_1,...,s_n)=1_{s_1...s_n=g}/sqrt(p(g)), on the finite product probability space mu^n. These functions are orthonormal. Let T be the coordinate refresh operator: for one coordinate T_i=(1-epsilon)Id+epsilon E_i, and T is their product. Each E_i is an orthogonal projection; using tensor products of the constant function and any orthonormal basis of its perpendicular complement gives eigenvalues (1-epsilon)^j, j=0,...,n. Hence T is self-adjoint and positive semidefinite.
Let u_g=sqrt(p(g)). The normalized joint-law matrix A has entries
 A_gh=P(g,h)/sqrt(p(g)p(h))=<f_g,T f_h>.
Put B=A-u u^t. To see B is positive semidefinite, for any real vector v set f=sum_g v_g f_g. Then
 v^t B v=<f,T f>-(E f)^2=<f-E f,T(f-E f)> >=0,
since T fixes constants and preserves the constant-orthogonal subspace.
Direct substitution into the definition gives the exact identity
 chi^2(P || p tensor p)=sum_gh B_gh^2=trace(B^2).
Cauchy-Schwarz against the probability p tensor p yields
 d_TV(P,p tensor p)<= (1/2)sqrt(trace(B^2)).
Thus trace(B_n^2)->0 is another valid sufficient criterion. This is not claimed necessary for TV convergence. Also, for each bounded real endpoint test f,
 Cov(f(X_n),f(Y_n))=Var(E[f(X_n)|C])>=0
by conditional independence. Pointwise covariance convergence for individual tests does not control the supremum over n-dependent joint events required by TV.

## 3. Every fixed finite quotient loses correlation, including periodic quotients
We prove a special case valid for every finite group Q and symmetric finitely supported mu whose support S generates Q as a semigroup. Repeated projected generators may carry unequal weights; assume only mu(s)>0 on S. This includes every finite quotient of the SRW above.
Let H be the set of group elements representable by an even-length S-word. It is a subgroup: concatenate even words and reverse/invert even words. Every s in S has square in H, and s t^{-1} is in H for all s,t in S. Consequently all elements outside H, if any, lie in the same coset aH, and [Q:H]<=2. If H=Q both parity classes are Q; if index two, even and odd endpoints are confined to H and aH respectively.
Because Q is finite, choose one even word for each h in H and let L be a positive even number at least their maximum length. Append inverse pairs s s^{-1} to obtain length exactly L for every h. Therefore mu^{*L}(h)>0 for every h in H. For nu_epsilon=(1-epsilon)mu_diag+epsilon(mu tensor mu), each length-L independent-coordinate path has positive weight at least epsilon^L times its independent weight. It follows nu_epsilon^{*L}(h,k)>0 for every (h,k) in H tensor H; its support is contained there. The same support conclusion holds for nu_1=mu tensor mu. No assertion that the one-step pair support generates Q tensor Q is needed; for bipartite walks that assertion would be false.
Let U be uniform on H tensor H, and choose a common delta in (0,1] such that nu_epsilon^{*L}>=delta U and nu_1^{*L}>=delta U pointwise. For example delta=min(1,|H|^2 min_{h,k}(nu_epsilon^{*L}(h,k),nu_1^{*L}(h,k))). Each block kernel is delta U+(1-delta)R on H tensor H. Uniformity is invariant under right convolution by any distribution on that finite group. Expanding independent blocks, or inducting on their number, shows that either block walk starting from the identity has TV distance at most (1-delta)^m from U after m blocks. When delta=1, both are already uniform after one block.
Write n=mL+r, 0<=r<L. TV contracts under convolution, so each n-step law is within (1-delta)^m of its U convolved with its r-step law. These latter two distributions agree: when index two, every r-step coordinate lies in the same parity coset, and translating uniform H independently in each coordinate gives the uniform product on that coset; when H=Q the result is simply U. (Index-two subgroups are normal, so left/right cosets agree.) Therefore
 d_TV(nu_epsilon^{*n},mu^{*n} tensor mu^{*n}) <= 2(1-delta)^{floor(n/L)} ->0.
This proves fixed finite quotient sensitivity without adding laziness. It does not prove the infinite-group conjecture: the quotient and its mixing constant are fixed before n tends to infinity. Quotients large enough to resolve the n-step endpoints may have mixing times larger than n.

## Remaining gap
No proof or counterexample is obtained for infinite Liouville Cayley graphs with no virtual real homomorphism, including the first Grigorchuk group. Liouville gives sublinear endpoint entropy and trivial bounded harmonic functions, but neither the shared-information estimate in Section 1 nor the matrix estimate in Section 2 has been deduced from it. Section 3 shows that fixed finite quotients cannot supply an obstruction; it gives no uniform control as quotient size grows. The bounded literature search found no theorem asserting the full conjecture.

## Computations and hostile-referee checks

`experiments.py` performs deterministic forward probability recursion, not Monte Carlo, with epsilon=1/4 and n up to 80. Groups use the semidirect-product rule (x,o)(t,s)=(x+o*t,o*s), o,s in {+1,-1}. Nonlazy dihedral generators are (0,-1),(1,-1); the four-generator aperiodic SRW adds (1,+1),(-1,+1). For the line, use (1,+1),(-1,+1). Finite cyclic tests reduce x modulo 5 or 6. Infinite-walk arrays use the full range [-80,80]; each step changes x by at most one, so no mass wraps before or at step 80 despite using array roll. Only orientation +1 is reached in the cyclic and line models. Pair-step weights are epsilon/d^2+(1-epsilon)1_{i=j}/d. State arrays are below 1 MB each and jobs finish in seconds once Python starts. Outputs are in `experiments.json`.

At n=80 the total variation distances were:
- Z SRW: 0.341441224838.
- D_infinity nonlazy: 0.341441224838.
- D_infinity aperiodic SRW: 0.0215473354134.
- C5 SRW: 0.000470507036867.
- C6 SRW bipartite: 4.07172381645e-08.

Normalization and joint symmetry were maintained within floating-point error; the endpoint matrices had minimum eigenvalues no smaller than about -3e-16. These are numerical consistency checks, not proofs of asymptotic results. The line and nonlazy dihedral outputs coincide, the four-generator dihedral distances decrease, and both cyclic models decay, including the periodic cycle of length 6. The four-generator example is covered by the 2025 virtually abelian theorem; it has a virtual real homomorphism and is outside the conjecture's sufficient-condition hypothesis.

`exact_checks.py` checks the conditional-mixture identity using Fraction arithmetic on S_3 at n=3, with the three transpositions (period two) and all five nonidentity elements (aperiodic). It verifies P=E(K tensor K), exact normalization, equality of marginals, and symmetry. The exact TV values are 9/32 and 1143/3125. These finite checks test the conditional-law construction and noncommutative product convention.

Potential failure points and their disposition:
1. Conditioning on the noisy endpoint is not conditioning on shared increments. The proof explicitly conditions on the mask plus retained values. The original and fresh values at marked sites remain independent. Checked exactly on two nonabelian finite examples.
2. Relative entropy cannot be recovered from small TV on growing alphabets. The displayed rare-diagonal example disproves this inference, with an exact information bound; `information_counterexample.json` records its values.
3. The endpoint matrix requires strictly positive p(g). It is defined only on the finite support of p, where divisions are legitimate. The claimed chi-squared criterion is sufficient only.
4. Positivity of the endpoint kernel uses a positive noise operator. This holds for independent refresh with epsilon in [0,1]; it is not asserted for arbitrary couplings. Numerical eigenvalue audits agree, and the finite scalar covariance algebra is formalized separately.
5. Finite-quotient support may be a proper subgroup of Q tensor Q. The even-word subgroup proof handles this; one must not invoke irreducibility on the full product for a bipartite walk. C6 and the transposition walk test this issue.
6. Uniformity on the residual parity coset must agree for the correlated and independent walks. Every coordinate has the same deterministic word parity at a fixed time; uniform convolution on the index-two subgroup gives the identical product-coset distribution in both cases.
7. The block minorization is uniform only within a fixed finite quotient. No exchange of quotient-size and time limits is used. This remains the main barrier to applying the finite proof to Grigorchuk.
8. A special case with virtually abelian groups is not the Liouville conjecture. The modern theorem has additional structure and aperiodicity assumptions, and its infinite groups do have virtual real homomorphisms.

Formal verification scope: `FiniteCovariance.lean` proves the two-point conditional covariance identity and its nonnegativity, together with the scalar entry identity behind the tensor difference bound. It imports only real-number basics and the ring tactic, uses no sorry or native_decide, and checks only these finite algebraic steps, not the full probability or finite-group arguments. The initial run failed because PowerShell wrote a UTF-8 BOM, blocking import parsing; the file was rewritten without BOM and checked again. Final success/failure is recorded in `lean_check.txt`.

Final formal verification: `lake env lean ~/brain_workers/TRIO_1011/op/F0093/FiniteCovariance.lean` ran from `~/lean_verify` and exited 0 in 102.984 seconds. All three named algebraic theorems passed Lean kernel checking. No sorry, axiom declarations, native_decide, or whole-Mathlib import occur in the checked file. The failed first run is retained separately in `lean_initial_error.txt`.


## Requested second serious attempt (2026-10-12)

The two new approaches, complete new proofs, experiments, formal verification and hostile-referee audit are in SECOND_ATTEMPT.md. Approach A uses entropy increments of the correlated *pair* walk and dominated convolution-prefix perturbations; Approach B uses Grigorchuk's self-similar tree sections. Approach A was pursued in full; a root-action boundary calculation was also proved for B.

New result: if |B(n)|<=exp(C n^alpha), alpha<1, a block of k=floor(c log n) coupled increments can be replaced anywhere by independent-coordinate increments with o(1) change in endpoint-pair TV. The sharper sufficient condition is c log A<1-alpha, where A=1+chi2(mu tensor mu || (1-epsilon)mu_diag+epsilon mu tensor mu). For uniform SRW on d generators, A=1+(d-1)(1-epsilon)^2/[epsilon(d-(d-1)epsilon)]. Applied to standard Grigorchuk SRW, d=4 and Bartholdi's alpha approximately 0.7674; at epsilon=1/4 any c<0.2069266754 works. This is insensitivity to a small change in the refresh mechanism, not endpoint noise sensitivity.

The full comparison with independent endpoints would require replacing n steps. The likelihood cost A^k is exponential, and iid entropy decrement identities cannot be silently applied to time-inhomogeneous laws after repeated replacements. A complete characteristic-function calculation on Z proves that even replacing a fixed fraction theta<1 of steps can leave positive endpoint TV from product; this illustrates the method's limitation and is not a counterexample to F0093. The virtual-real-homomorphism exclusion remains unused.

Second-attempt status: PARTIAL. Numerical finite-time bounds and exact S3 checks passed; PrefixDomination.lean passed with exit 0. The general conjecture and Grigorchuk full endpoint independence remain unproved and no counterexample in the stated class was found.
