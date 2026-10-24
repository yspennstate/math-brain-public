# Boundary audit: child support and conditional likelihood transport

Bits throughout. All physical functions below are actual Boolean signs on uniform cubes. Queries are fresh physical singleton restrictions; all terminal spectral entropy and pivotal influence stay in the accounts.

## 1. Exact local criterion, with its support hypothesis

At one node write the parent spectral law as p(s_i,t,z), with complete normalized reference q dominating p. Erase i to obtain p_e(t,z),q_e(t,z). For this criterion assume the ERASED laws have identical support, including all reference-only rows: p_e(t,z)>0 iff q_e(t,z)>0. This is stronger than mere absolute continuity. The nonempty proof rows below all satisfy it; no zero-row fallback is claimed to remove a support mismatch.

The actual fair coherent kernel is K_b(t,z)=p_b(t,z)/(2p_e(t,z)). It sums to one on each supported erased row. Use this SAME kernel on q_e. Write q_joint(b,t,z)=q_e(t,z)K_b(t,z), q_B(b)=sum q_joint(b,t,z)>0, and q_Bayes,b=q_joint(b,.,.)/q_B(b). The actual branch is fair with p_joint=p_e K_b=p_b/2. Hence on every supported branch row,

    p_b(t,z)/q_Bayes,b(t,z)=2 q_B(b) L(t,z),
    L(t,z)=p_e(t,z)/q_e(t,z).                     (1)

For each fixed t, form a graph whose vertices are its supported z. Join two vertices whenever some physical branch b has K_b(t,z)>0 at both. Then the following are equivalent:

    every actual child and inherited Bayes child have the same
    conditional spectator law Z given T on all occupied child rows;

    L(t,z) is constant on every connected component of this graph.

Proof: equality of the conditional laws is exactly constancy in z of (1) on each branch support at fixed t. Each branch support is a clique. Constancy on each such clique is equivalent to constancy on their connected components. The common-support hypothesis guarantees the same occupied rows and no hidden reference-positive spectator atom.

For two branches there are at most two components. If one supported z has both K_0,K_1 positive, the two branch cliques meet, so the entire row is connected and L must depend only on t. If the branch supports are disjoint, L may take different constants on the two components; the likelihood condition of A050 remains sufficient but is no longer necessary. If a branch has no support on that t, there is just one nonempty clique. This is an exact criterion for the *inherited* children, not permission to introduce a freshly chosen mismatching reference for free.

## 2. Where the nonmatching conditional KL is owned

Let C_e=E_{p_e(T)} D_2(p_e(Z|T)||q_e(Z|T)). At fixed t apply KL chain rule to the two joint conditional laws P(B,Z|t) and Q(B,Z|t), both made with K. Their joint likelihood is the erased conditional Z likelihood. Thus exactly

    C_e = E_{p_e(T)} D_2(P(B|T)||Q(B|T))
          + sum_{b,t} P(b,t) D_2(P(Z|b,t)||Q(Z|b,t)).    (2)

The last term is the physical mean inherited-child conditional KL. It is nonnegative, at most C_e, and zero exactly at the criterion above. This is a once-only splitting of the existing erased conditional KL; it is not a new influence refund. Both terms in (2) can be strictly positive. Conditional Q(B|T) uses the ACTUAL transported full reference, not a new quotient channel built by discarding Z first.

The full source-reference ledger additionally retains queried-label conditional erasure:

    D(p||q)=E_erasure+D_2(fair||q_B)
                         +(D(p_0||q_Bayes,0)+D(p_1||q_Bayes,1))/2.

It follows by erasing i and then retaining (B,T,Z) under the same channel; retaining T,Z makes this channel embedding lossless for KL. Dropping or resetting any child reference requires its own signed correction.

## 3. Exact balanced exception

Take f(X0,X1)=1-2 X0 X1, query X0, and put Z=S_{X1}, with T empty. The root spectrum is uniform on its four sets. The children are constant and a character, so p_e(Z)=(1/2,1/2), K_b is deterministic with b=Z. Choose q_e(Z)=(1/4,3/4), and q(s_i,z)=p(s_i|z)q_e(z). This is positive and normalized.

The erased likelihood values are 2 and 2/3, not constant. Nevertheless both inherited child references are exactly the actual point-mass child spectra. Child conditional KL is zero; the full root KL is D_2(Ber(1/2)||Ber(1/4)), paid as outcome KL. There is no missing conditional correction. This is the smallest actual Boolean example: on zero/one residual-frequency vertex only one component is possible. The implementation also finds such exceptions by exhaustive two-tilt census, with no numerical equality tolerance.

## 4. Perturb a balanced seed: regular and extreme reference boundaries

For every r>=2 let h_r(x)=(-1)^{sum x_j}, except flip its value at the fixed vertex x=1 (integer bit mask1) from -1 to +1. Its mean is mu=2^(1-r), and every Fourier coefficient is nonzero: the original full-parity coefficient becomes 1-mu, while all others are plus/minus mu. Every physical coordinate remains essential, with I(h_r)=r(1-mu). Define f_r=+1 when selector B=0 and h_r when B=1. The selector is essential with influence (1-mu)/2. All root Fourier coefficients are nonzero as well.

Put a=mu^2. The erased empty-frequency mass is (1+a)/2; nonempty masses are hhat_r(z)^2/2. Let q_e(empty)=alpha, and distribute its remaining mass proportionally to those actual nonempty masses. Complete the parent reference with q(s_B,z)=p(s_B|z)q_e(z). For every 0<alpha<1 this is a normalized full-support reference and E_erasure=0.

Branch0 has only empty frequency. Branch1 has empty mass a and nonempty mass1-a. The empty row is now ambiguous, connecting the entire graph. The inherited branch1 empty probability and mean child conditional KL are

    beta=alpha*a/(1+a-alpha),
    C_child=(1/2) D_2(Ber(a)||Ber(beta)).                 (3)

Branch0's conditional KL is zero. Matching therefore holds exactly when alpha=(1+a)/2. This demonstrates why a tiny nonzero mean changes the exact admissibility boundary.

At regular alpha=1/4, beta=a/(3+4a), and expanding logarithms at a=0 gives

    C_child = a*(ln3-2/3)/(2 ln2)+O(a^2).

The coefficient is positive because ln3>2/3, for example integrating 1/t over [1,3] gives a strictly larger value than its right-endpoint rectangle 2/3. Thus the mismatch is quadratic in the small Boolean child mean. Its validity is analytic, not extrapolation from the frozen seven r values.

At alpha=1-a^2, the inherited beta is exactly1-a, giving

    C_child=((1-2a)/2) log2((1-a)/a)=r-1+o(1),
    q_B=(1-a,a), O=-(1/2)log2(4a(1-a))=r-2+o(1),
    D(p||q)=D_2(Ber((1+a)/2)||Ber(1-a^2))
            =O+C_child=2r-3+o(1).

Hence C_child divided by removed selector influence tends to infinity (asymptotic ratio2r). No absolute K can price this *unconditionally chosen inherited nonmatching conditional KL* by K times this query's influence, even with actual full-support Boolean functions, positive normalized references, same-kernel transport, and zero erasure KL. A source-specific floor or its retained KL bank is needed. This is not an objection to A050's explicitly scoped sufficient condition, which fails here. It also does not establish failure for any prescribed occupancy reference: these are exactly specified tilted references.

The frozen r=6 member is a seven-variable exact certificate: a=1/1024, selector influence31/64, alpha1048575/1048576. Since1023>512, C_child>(511/1024)*9=4599/1024>31/8=8 times the removed influence. The strict sign uses only integer comparisons, with no floating-point logarithm.

The exact terminal budgets are E I_leaf=r(1-mu)/2 and E H_leaf=H(h_r)/2. Root influence is (r+1)(1-mu)/2. Every local entropy telescope is checked. The growing root source KL is kept in the ledger, so the example is an obstruction to free or influence-only reference substitution, not to FEI.

## 5. Independent review of A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1

Source statement hash75e11f0efbb88117837b6072fcc99042198eb3c655744bf203b8b1dd7cab64ea. Accepted unchanged at its stated scope; the criterion/obstruction above are separately identified audit results.

Reconstruction: With p(c,u,z)=pbar(c,u)k(z|u) and q=qbar k, reference normalization follows by summing k. KL chain rule gives D(p||q)=D(pbar||qbar); cross entropy adds L=E H(k(.|U)), which remains part of every actual terminal bill. Controller erasure keeps u, so the common k cancels from the actual branch kernel p_b/(2p_e). Apply that same kernel to source and reference, with quotient-only fallback on source-zero rows. Both full Bayes children factor with the same k; hence erasure KL, outcome KL and each signed Bayes-to-chosen-child reset are exactly the quotient values. L averages to its parent value because the U spectral marginal is the physical child mixture, proving zero controller drift and inherited prefix transfer. No Boolean quotient is assumed.

For an arbitrary query outside Z, erasure removes spectral i while coherent branching changes the remaining law. Direct entropy chain rules give

    L_parent-average L_child=I(B;Z|T)-I(S_i;Z|T).

Its positive part is bounded by J_full, itself at most2 Inf_i/ln2. For completeness the natural fiber inequality is d(z)<=1-sqrt(1-z^2), where d'(z)=atanh(z); the derivative of z/sqrt(1-z^2)-atanh(z) is (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0. Integrate and use symmetry/endpoints. Multiplying by (G^2+H^2)/2 gives natural JS<= (|G|-|H|)^2/2 <= (G-H)^2/2, and Parseval gives the physical price. This price pays only that positive entropy drift; the signed negative term remains.

If p/q is a positive function of retained T on the entire common source/reference support, summing out i preserves that likelihood, and (1) gives inherited child likelihood independent of Z. Thus all extra conditional KL is zero. This proves the source sufficient condition; it is not claimed necessary by A050. The common independent-factor application follows by multiplying normalized references and retaining that factor entropy/influence once.

The h3 data-query witness has root L=2-(3/8)log2(3) and mean terminal L=1, so its drift is1-(3/8)log2(3)>0 by27<256. The arbitrary-controller-reference times independent h3 example has likelihood depending only on retained controllers, so both data children meet the condition. These exact clauses and their terminal scope are reconstructed without replaying A050's checker. The present direct Walsh census independently verifies the same-channel identity and the exact support boundary. A050's universal nonmatching-reference payment remains explicitly OPEN.

FIRST UNSUPPORTED LINE: at a specified mixed priority data/controller query, supply an unused certified source conditional-KL or signed child surplus that funds the nonmatching inherited conditional KL and the full signed quotient decrement, while retaining both actual terminal entropy/influence bills. Formula(2) identifies ownership but does not provide a uniform physical payment or justify fresh projection.
