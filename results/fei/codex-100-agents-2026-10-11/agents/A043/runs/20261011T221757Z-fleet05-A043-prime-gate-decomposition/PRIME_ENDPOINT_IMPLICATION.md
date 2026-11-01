# Exact prime endpoint and its consequence

Let P be the essential prime class in PRIME_GATE_DEFINITION.tex, including all essential binary gates. For an interior product law mu on sign inputs, put m_j=E X_j, sigma_j^2=1-m_j^2, psi_j=(X_j-m_j)/sigma_j, and a_S=E[f psi_S]. All entropies below use bits. Define

    Hplus_mu(f) = sum_{S nonempty} a_S^2 log2((product_{j in S} sigma_j^2)/a_S^2),
    I_mu(f) = sum_S |S| a_S^2,
    V_mu(f) = sum_{S nonempty} a_S^2 = Var_mu(f),
    delta_mu(f) = I_mu(f)-V_mu(f).

Zero summands are omitted. For signs, E|psi_j|=sigma_j, so |a_S|<=product sigma_j. Thus Hplus and delta are nonnegative. I_mu is spectral influence; it equals sigma_j^2 times the pivotal probability in coordinate j, summed over j, and must not be confused with unweighted pivotal probability at bias.

**Conditional theorem.** If a finite C>=0 satisfies Hplus_eta(g)<=C delta_eta(g) for every g in P of every arity and every interior product law eta, then Hplus_mu(f)<=C delta_mu(f) for every Boolean f under every interior product law mu. Conversely the universal product-biased corrected bound implies the same bound on P by inclusion. The two strong endpoints therefore have exactly the same optimal constant, allowing infinity. This is an equivalence of the corrected product-biased endpoints; no converse from ordinary uniform FEI is asserted.

The induced laws require no extra hypotheses. Use the disjoint prime formula. If its physical inputs have an interior product law, disjoint child outputs are independent. A nonconstant child is surjective and has both output probabilities positive, because every physical assignment has positive mass. Its output mean m_i and variance v_i=1-m_i^2 therefore define an interior product law eta at its parent. Constants are substituted and removed. Essentiality of a gate is a truth-table property and does not change when its interior law changes. Repeated induction carries precisely these means, rather than silently replacing the gate law by uniform input.

For completeness reconstruct the composition step from Proposition 7.1 of the 38-page threshold paper. Given F=g(f_1,...,f_r), disjoint physical blocks, child means m_i and variances v_i>0, let b_A be the eta-biased gate coefficients and w_i=sum_{A containing i} b_A^2; set alpha_i=w_i/v_i. For a physical set S, write T_i=S intersect B_i and A={i:T_i nonempty}. Centered child expansions have no empty coefficient, so

    Fhat_mu(S)=b_A product_{i in A}(fhat_mu_i(T_i)/sqrt(v_i)).

For S=empty this says Fhat(empty)=b_empty. Every S determines A and the T_i uniquely. Squaring gives a spectral experiment: sample A with mass b_A^2, then sample each nonempty T_i with law fhat(T_i)^2/v_i. Splitting the logarithm for nonempty S yields

    Hplus_mu(F)=Hplus_eta(g)+sum_i alpha_i Hplus_mu_i(f_i).

The gate entropy uses the variance factors v_i; these factors cancel the denominators from the child spectra. Expected cardinality and output distribution give

    I_mu(F)=sum_i alpha_i I_mu_i(f_i),   V_mu(F)=V_eta(g),
    delta_mu(F)=delta_eta(g)+sum_i alpha_i delta_mu_i(f_i).

The last equality uses sum_i alpha_i v_i=I_eta(g). Applying the prime hypothesis and induction on the finite formula gives the theorem, since all coefficients and deficits are nonnegative. Constants and unary literals have both corrected entropy and deficit zero. Unary negation preserves all squared coefficients and deficit. No depth penalty is incurred. These identities hold with unequal biases, not just equal bias or balanced children. Endpoint laws can be handled by first restricting deterministic physical coordinates and re-factoring the resulting truth table; no division by zero is performed.

**Uniform full FEI consequence.** On uniform physical inputs sigma_j^2=1, so H(f)=Hplus(f)+h0, where h0=m^2 log2(1/m^2). The elementary inequality -t ln t<=1-t for 0<=t<=1 gives h0<=log2(e) Var(f). Consequently

    H(f)<=C [I(f)-Var(f)]+log2(e) Var(f)
         <=max{C,log2(e)} I(f).

The all-prime corrected product-bound is still OPEN. The implication and the reduction are proved here, not its antecedent. No independent review is claimed.

**Precisely weaker variants.** A uniform-input corrected bound on prime gates suffices for a prime formula only when every internal gate encounters independent balanced nonconstant children (hence its actual eta is uniform). That condition is not guaranteed by the factorization theorem. An ordinary bound H(g)<=C I(g) even on uniformly driven gates does not provide the corrected deficit cancellation: it leaves the outer entropy as a new charge at every composition. Neither omission is repaired by declaring a gate prime.

An explicit prime-root bias witness is F=majority_3(AND_2(x_1,x_2),x_3,x_4), with all four physical inputs uniform. The root majority_3 is prime by the threshold argument. Its induced first output has mean -1/2 and P(+1)=1/4; the other two means are zero. Thus the first unsupported line of a uniform-only application would be applying the root's uniform-input estimate at eta=(1/4,1/2,1/2). This is a demonstrated failure of that proof step, not a disproof of any possible abstract implication between ordinary prime FEI and full FEI.

**Residual localization.** For a fixed C and a disjoint split define D_C=Hplus-C delta. The exact identity D_C(F)=D_C(g)+sum_i alpha_i D_C(f_i) shows that any positive universal corrected deficit has a positive prime descendant under its actual induced product law. Conversely a prime violation is already a universal corrected violation. This reduces a corrected-bound falsification search to prime gates with their biases, not necessarily to uniform prime gates and not to a counterexample to ordinary uniform FEI. It also shows why there is no mathematical payment yet: all the unpaid corrected deficit has been localized, rather than bounded.

Next consumer action: A044 should use the two-row criterion to identify which proposed gate families actually remain prime, and prove a bias-uniform quantitative estimate or a fully scoped obstruction. A059 can use the finite termination/depth bound and exact zero-overhead strong-entropy transport. A091/A090 should independently reconstruct the criterion and induced-law cancellation.
