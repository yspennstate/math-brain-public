# Checks on the reduction

The following checks are algebraic. No simulation or numerical evidence is used in the proof.

1. **Independent check of the exponential constant.** The proof optimizes the exponential-moment bound at a = epsilon p/2 and obtains the denominator 8(1+epsilon/6) <= 28/3 < 10. As a separate check, use the unoptimized value t = epsilon/(3 delta) in (4). Since epsilon <= 1,

   \[
   -ta+\frac{t^2p\delta}{2(1-t\delta/3)}
   \leq-\frac{\epsilon^2p}{6\delta}
        +\frac{\epsilon^2p}{16\delta}
   =-\frac{5\epsilon^2p}{48\delta}
   \leq-\frac{\epsilon^2p}{10\delta}.
   \]

   The last comparison is 5/48 > 1/10. Thus a different exponential parameter recovers the same stated constant 10. Both checks include the factor 2 lost in passing from net quadratic forms to the operator norm.

2. **Sampling variance, first derivation.** For uniform T of size h, let I_i be its inclusion indicators and p = h/N. Then Var I_i = p(1-p), and for i != j,

   \[
   \operatorname{Cov}(I_i,I_j)=-\frac{p(1-p)}{N-1}.
   \]

   Using sum w_i = 1 gives

   \[
   \operatorname{Var}\left(\sum_{i\in T}w_i\right)
   =\frac{h(N-h)}{N(N-1)}
      \left(\sum_iw_i^2-\frac1N\right).
   \tag{A1}
   \]

   In particular, since sum w_i^2 <= L/N, the variance of the relative mass (N/h) sum_T w_i is at most

   \[
   \frac{(N-h)(L-1)}{h(N-1)}.
   \tag{A2}
   \]

   This checks the h/L effective sample size in the exponent. It also shows that the net argument introduces an additional dimension loss beyond a one-vector variance estimate.

3. **Sampling variance, second derivation.** Sample an ordered list of h distinct coordinates. The corresponding random weights Y_j have population mean 1/N and variance sigma^2 = (sum_i w_i^2)/N - 1/N^2. Two distinct draws have covariance -sigma^2/(N-1). Therefore

   \[
   \operatorname{Var}\left(\sum_{j=1}^hY_j\right)
   =h\sigma^2-\frac{h(h-1)}{N-1}\sigma^2
   =\frac{h(N-h)}{N-1}\sigma^2,
   \]

   which is (A1), derived without inclusion indicators.

4. **A finite exact check.** For N = 4, h = 2 and w = (1/2,1/4,1/4,0), the six unordered-subset masses are 3/4, 3/4, 1/2, 1/2, 1/4, 1/4. Their mean is 1/2 and their variance is 1/24. Formula (A1) gives (4/12)(3/8-1/4) = 1/24 independently. The conditioning probability at p = 1/2 is 6/16 = 3/8, exceeding 1/(N+1) = 1/5 as required. This is a hand enumeration, not a claimed computer experiment.

5. **Multiplicity and net cardinality.** The key hypothesis is complete delocalization of every vector in an eigenspace. Delocalization of a selected basis alone would not suffice: a Walsh orthonormal basis of R^N is flat, but linear combinations include coordinate vectors. Under the actual hypothesis the projection identity gives rank <= L. Alternatively, if e_1,...,e_m is an orthonormal basis of E, the maximal squared coordinate of a unit linear combination is sum_j e_j(i)^2. Summing these maxima over i gives m, again yielding m <= L. The volume ratio for a 1/4-net is (9/8)^m/(1/8)^m = 9^m. The quadratic-form approximation loses 1/(1-2*(1/4)) = 2, consistent with (8).

6. **Probability accounting.** A binomial mass at its mode is at least 1/(N+1), hence conditioning costs at most N+1. The upper and lower tails cost 2. There are at most N eigenspaces and M observables. Correlations between the permuted sets are irrelevant to the union bound. Conditioning on a fixed good matrix makes every net deterministic before sampling the permutation. The original and permuted matrices have the same law; the exceptional probability q is paid once.

7. **Endpoint and scale checks.** At h = N the mass is exactly 1 for every unit vector. At h = 1 no vanishing relative error is asserted. At L = 1 every weight vector satisfying the hypothesis is exactly uniform, so all masses are exact; the bound remains valid but is loose. At L = N the net bound may be entirely vacuous, as it should be. Substitution of epsilon_N from (11) cancels exactly the factor 2MN(N+1)9^floor(L), leaving N^{-r}. For M <= N^K and L = (log N)^C, sqrt(L(L+log N)/N^alpha) is bounded by a constant times the two terms in (15). Both vanish for fixed alpha > 0.

8. **Source and probability check.** Theorem 1.4 and equation (1.4) in Huang–Yau, arXiv:2102.00963v3, were read in the primary HTML. Their delocalization statement is about eigenvectors, not merely a randomly chosen basis. Its resolvent origin also gives bounds for every vector in a repeated eigenspace. The surrounding text separates overwhelming conditional probability on a locally tree-like event from the polynomial unconditional probability. The application retains this distinction; it does not upgrade q to N^{-r} for arbitrary r. The graph normalization does not change eigenvectors.

9. **Attempt to enlarge the claim, and its failure.** The random-permutation argument requires the observable to stay fixed when H is relabelled. A graph-dependent ball or an eigenvector-dependent support transforms along with H, so its inverse image is not a uniform independent subset conditional on H. The Walsh construction in PROOF.md gives an exact abstract counterexample to omitting this restriction. No statement about such observables, optimal logarithmic scales, Haar eigenvector fluctuations, or a full solution to the original unspecified QUE question follows from the proof.

10. **Nature of the contribution.** Deterministic-observable QUE was already known at sufficiently large fixed degree. The earlier all-degree delocalization result makes this elementary reduction available at every fixed d >= 3. The contribution recorded here is an explicit, basis-independent finite-N reduction with a relative mesoscopic-set statement. No assertion of a new literature theorem or priority is made.
