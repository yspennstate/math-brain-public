# Separately derived posterior law: narrow manuscript audit

The September 24 manuscript's Lemma 7.2 is mathematically valid under its stated conditioning. This check is independent of its global bigeodesic argument. The source is sources/no_bigeodesics_20260924.pdf, pages 29-30, SHA-256 f97d87dc82bcee0cd11725e3261df8ddf51c34442c8305873c27107074d3b5ae. This is a partial audit, not a certificate of its Theorem 1.1. Independent reviewer w389 has now kept this derivation after symbolic rederivation (R07, announced05:16 UTC).

Take independent triples (X_e,U_e,Z_e), also independent across edges, with X_e~G, U_e uniform[0,1], and Z_e~G conditioned on [b,infinity). Let a<b, p_a=G([0,a])>0, p_b=G([b,infinity))>0, and deterministic 0<=delta_e<p_a. Set xi_e=1{X_e<=a,U_e<=delta_e/p_a}, and Y_e=Z_e if xi_e=1, otherwise X_e. Modify a deterministic finite set F; outside F, Y_e=X_e.

For any measurable output set D,

    P(xi_e=1,Y_e in D)=(delta_e/p_b) G(D intersect [b,infinity));
    P(xi_e=0,Y_e in D)=integral_D [1-(delta_e/p_a)1_[0,a](t)] dG(t).

Their sum has density lambda_e(t)=1-(delta_e/p_a)1_[0,a](t)+(delta_e/p_b)1_[b,infinity)(t). Since a<b and delta_e<p_a this density is positive G-almost everywhere. Divide the first density by lambda_e to obtain

    P(xi_e=1 | Y_e)=1_[b,infinity)(Y_e) delta_e/(p_b+delta_e).

The pairs (xi_e,Y_e) are independent across F, so their regular conditional kernel given the finite output vector is the product of these Bernoulli kernels. The unchanged exterior is independent of every inside pair, hence conditioning also on all exterior outputs preserves that product, first for finite-coordinate functions and then by a monotone class argument. This proves independence conditional on the ENTIRE individual output.

If a finite simple path prefix is a measurable function of that output alone, its edge list is fixed after conditioning and consists of distinct edges. Restricting the product kernel to that list is legitimate. Completion-measurable selections admit Borel versions under the output law; equivalently partition by the countably many finite possible prefixes. Conditioning on other sites' outputs or on success of the subsequent mark is a different conditioning and is not licensed by this argument. The manuscript explicitly avoids that extension.

Consequently the conditional count variance is sum theta_e(1-theta_e)<=sum theta_e. The conditional gain estimates in Lemma 7.3 may use this variance once the stated usable-prefix lower bound and cone inclusion are established. This derivation does not audit those geometric premises, the no-fork argument, or the final label budget.

Exact control in check_obstructions.py: uniform G, a=1/4,b=3/4,delta=1/16. The posterior on high output is 1/5. Nine pairs of output regions test all four flag combinations (36 products) and an output-measurable choice of one of two edges (nine selections). No numerical approximation or conditional-independence assumption is hidden in those controls.
