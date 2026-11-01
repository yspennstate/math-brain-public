# Exact boundary credits and the bad-node question

Use Eplus for corrected entropy in bits, e(u)=u log2(1/u), v=1-m^2 and the notation of BIAS_TRANSPORT.tex. Fair physical restriction never biases an untouched physical coordinate. The outer Y_j law is a distribution of a Boolean output, not a replacement physical measure.

For a nonconstant uniform physical child,

    H(f)=e(m^2)+Eplus(f)=h2(v)+v H(nonempty spectrum),
    Eplus(f)=v H(nonempty spectrum)+v log2(1/v).

The output-empty reserve e(m^2), conditional-nonempty entropy and corrected entropy must not be interchanged. Corrected outer entropy includes the exact subtraction sum_i Inf_i^mu(g) log2(1/v_i) from its nonempty Shannon entropy. In disjoint substitution that subtraction is canceled by the inner Eplus terms. There is no extra output-variance numerator in the corrected definition.

At a deterministic child, contract its output coordinate before using a normalized basis. The apparently singular multiplier Inf_j^mu(g)/v_j is actually the bounded physical pivotal probability t=E(D_jg)^2, independent of m_j. For a fixed finite outer gate and fixed interior other biases, a coefficient containing j has P=v_j c^2 and its corrected logarithm is log2(w_other/c^2): the log(1/v_j) cancels exactly. Coefficients avoiding j are affine in m_j; if such a coefficient vanishes at the endpoint its squared mass is O(v_j^2), with a possible O(v_j^2 log(1/v_j)) term. Therefore outer corrected entropy converges to its contracted value, with O(v_j) drift for this fixed slice. This is a consumed A042 boundary fact, not an arity-uniform continuity modulus.

The erasure correction is

    R=sum_Z L(Ahat_Z+m Bhat_Z,beta Bhat_Z)-t L(m,beta),
    L(a,c)=(a^2+c^2) h2(c^2/(a^2+c^2)).

Its last term is a genuine negative credit. For fixed m!=0 and beta->0,

    L(m,beta)=beta^2[log2(1/beta^2)+log2(m^2)+log2(e)]+O(beta^4).

Let Z(m)=sum_{Ahat_Z+m Bhat_Z=0} Bhat_Z^2. Each nonzero first argument contributes the same beta^2 log(1/beta^2) leading factor multiplied by Bhat_Z^2; a zero first argument contributes zero. Hence

    R=-Z(m) beta^2 log2(1/beta^2)+O_{A,B,m}(beta^2),  m!=0.

There is no positive leading rare-beta logarithm at fixed nonzero mean. At m=0, the subtraction vanishes and instead

    R=kappa beta^2 log2(1/beta^2)+O_{A,B}(beta^2),
    kappa=sum_{Ahat_Z!=0} Bhat_Z^2 <= t.

For sufficiently small nonzero m away from the finitely many cancellation roots and with beta=o(|m|), the coefficient of beta^2 in the iterated expansion contains kappa log2(1/m^2)+O_{A,B}(1). The log(1/mean) is thus a crossover in the signed erasure residual, not bias of the surviving physical cube. The two limits m->0 and beta->0 cannot be exchanged in the fixed-m O(beta^2) term. The exact scalar subtraction covers the crossover.

This specific logarithmic component is linearly affordable: |beta|<=d by physical child disagreement, and for 0<|beta|<=1,

    t beta^2 log2(1/beta^2) <= [2/(e ln2)] t |beta| <= [2/(e ln2)] t d.

The maximum of u log(1/u) is 1/e. This consumes A057's already identified logarithmic-bank mechanism; it is not a new universal payment. In the regime beta=o(|m|), log(1/m^2)<=log(1/beta^2) eventually. The remaining outer spectral constants, outer-rarity t log(1/t) in equation (5), signed JS transport, and inner mismatch/KL logarithm are not thereby paid. No claim that every such node is good follows. A node is bad only after comparing its full B_x(F), including t B_x(f_j) and R, to K t d. The lead's localized odd-face estimate is not assumed.

Near-dictator calibration: let h_r(z)=1-2 1_{z=0}, r>=2, f_j(x,z)=x h_r(z), and F=1-2 1_{f_j=+1,y=+1} with a disjoint fair literal y. Query x. The two inner spectra are identical, so eta_inner=0 and delta H(f_j)=0, yet t=1/2 and delta I(F)=1/2. As r->infinity the physical functions converge in probability to the corresponding literal/AND functions; to justify entropy convergence despite growing dimension, use the explicit point-defect nonempty masses 4*2^(-2r), whose total entropy is O(r 2^(-r)). Thus delta H(F)->2 bits, and T->2 bits. Equivalently R tends to 1 bit and the outer JS term tends to 1 bit, as follows from the four nonzero Fourier masses of the limiting AND. A vanishing INNER mismatch charge alone does not authorize free splicing of F. This family is near a dictator, not a rare-influence bad-node obstruction: delta I(F) stays 1/2, and the limiting B/delta I is 2.

If the outer gate is itself a signed dictator, T=0 exactly even at deterministic child endpoints. If beta=0, T=R=0 for every outer gate: restrictions with stationary child means transport the full inner decrement by t. These two limits are exact and dimension-independent, unlike the fixed-spectrum asymptotic constants above.
