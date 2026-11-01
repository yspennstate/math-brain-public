# Independent audit: count hitting-time means and variances

12 October 2026.

**Result: PASS.** No blocking mathematical issue found in the audited hitting-time derivation.

## Exact scope

Read completely:

- polymer_extensions/tv/03_hitting_means.tex
- polymer_extensions/tv/04_hitting_variances.tex

Also read 02_count_theorem_and_stationarity.tex and 05_cutoff_conclusion.tex to confirm the definitions, fixed-b regime, stationary inputs, targets and claimed use of the moment estimates. This audit does not independently verify the cited external cutoff theorem or priority of the cutoff result.

The process has beta=b/n for fixed b>0, birth lambda_k=b(n-k)/n and death mu_k=k(k-1)/n. The positive zero a satisfies a^2+(b-1)a-bn=0, so n is comparable to a^2 with constants depending on fixed b.

## Hitting means

1. The flux/Poisson identities e_k=F_k/[p(k)lambda_k] and f_k=G_k/[p(k)mu_k] have the correct indexing. Their recurrence boundary values e_1=1/lambda_1 and f_n=1/mu_n are correct.
2. Monotonicity e_k increasing follows by subtracting consecutive recurrences and using decreasing lambda and increasing mu. The reflected argument gives decreasing f_k.
3. In the lower tail, delta_k=lambda_k-mu_k is positive and decreases. The exact difference h_k-h_{k-1}=(2k+b-2)/[n delta_k delta_{k-1}] for h=1/delta is correct and increasing.
4. The recurrence for h-e is exact. The increasing ratio q_k=mu_k/lambda_k bounds the products in its iteration by a geometric sequence, giving the displayed error at most mu_k(delta_{k-1}-delta_k)/delta_k^3.
5. The error estimate C_b a^2/(a-k)^3 uses delta_k bounded below by a constant times (a-k)/a. Its sum outside L sqrt(a) is O(a), as claimed.
6. The corresponding upper-tail recurrence, reverse iteration, and bound lambda_k(D_{k+1}-D_k)/D_k^3 are correct. D_{k+1}-D_k=(2k+b)/n has the right shift. The reciprocal drift is convex and decreasing above a; alternatively this follows immediately from its two-term partial fraction decomposition.
7. Both partial fractions have denominator 2a+b-1 and the correct signs. Each bracketed sum is (1/2)log(a)+O(1), the second by cancellation of its two large upper-endpoint logarithms.
8. Multiplying by n/(2a+b-1), and including central passages of total mean O(a), gives n log(a)/(4a)+O_b(a). Substituting a=sqrt(bn)+O_b(1) gives sqrt(n)log(n)/(8sqrt(b))+O_b(sqrt(n)).
9. Rounding u and v and the one-step endpoint differences change these sums by O(a) or less. Targets within a fixed multiple of sqrt(a) are handled by the same central estimate.

## Hitting variances

1. The Poisson equation for the second moment and summation against the stationary weights give
   E_k T_{k+1}^2 = 2/[p(k)lambda_k] sum_{ell<=k} e_ell F_ell.
   The displayed upper bound 2 e_k^2 sum F_ell/F_k follows from monotone e_ell. Replacing variance by the second moment is a valid upper bound.
2. The lower-tail ratio r_k=p(k-1)/p(k)=mu_k/lambda_{k-1} is increasing and at most mu_k/lambda_k. The index-shifting proof of F_ell <= r_k^{k-ell} F_k is valid.
3. Hence each lower-tail passage variance is at most 2lambda_k/delta_k^3, bounded by C_b a^3/(a-k)^3. The sum outside L sqrt(a) is O(a^2).
4. The reflected upper-tail estimates use s_k=lambda_k/mu_{k+1}, which is decreasing. They give 2mu_k/D_k^3. For k<=2a its sum is O(a^2); for k>2a, the bound C_b n^2/k^4 sums to O_b(a).
5. In the center, sum_{ell<=k}F_ell = E[(k-K+1)_+] and its reflected identity are exact. The stationary first moment bounds them by O(sqrt(a)). Central passage variance is therefore O(a^{3/2}), and O(sqrt(a)) passages contribute O(a^2).
6. Successive one-edge first-passage times are independent by the strong Markov property: each intervening first hitting level is a deterministic state. Excursions back across prior levels do not invalidate this independence. Thus the variances add.

The resulting variance bound O_b(a^2)=O_b(n) is correct, as is its extension to fixed-width central targets.

## Limits of this pass

The asymptotic estimates require fixed b>0. Constants may depend on b and, for off-median targets, on the fixed central-width parameter. This derivation alone does not prove a uniform theorem when b varies with n, a worst-case polymer upper bound, or an exact limiting cutoff profile.
