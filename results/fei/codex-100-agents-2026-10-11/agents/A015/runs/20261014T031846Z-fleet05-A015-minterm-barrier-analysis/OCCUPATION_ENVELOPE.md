# A sharp residual after distributed ownership erasure

Bits unless ln is written. This is a scoped continuation diagnostic for A007's SAME base posterior, not a new universal FEI candidate. Retain gamma=6/5 and all fixed-reference requirements.

## Exact envelope when all selected data supports coincide

Fix one data assignment tau using k>=1 gates, with positive owned sizes s_l and total s=sum s_l. Suppose kappa_l=|T intersect R_l|=s for every used gate. This includes the full satisfying-cell table of any Boolean function under common full-support orders, and the full prime table of parity. Let a_l=s_l/s. For every integer u>=1, A007's distributed ownership sum is

    Z_tau(u)=sum_(v_l>=0,sum v_l=u) [u!/prod v_l!]
       product_l [((s_l+v_l)/(s+u))^(gamma(s_l+v_l))
                                      /(s_l/s)^(gamma s_l)].

Then exactly

    Z_tau(u)>=2^(-(gamma-1)u H(a)) >= k^(-(gamma-1)u).

Proof: put a product probability q on labelled ownership maps alpha, giving each of the u coordinates owner l with probability a_l. Its entropy is u H(a), and its occupation means are E v_l=u a_l. The finite log-sum/relative-entropy variational inequality gives log Z>=H(q)+E_q log(weight). Convexity of x log x gives

    E sum_l (s_l+v_l)log(s_l+v_l)
      >=sum_l ((s+u)a_l)log((s+u)a_l).

Subtract the fixed denominator and old congestion. The expected log(weight) is at least -gamma u H(a), proving the first inequality. H(a)<=log k gives the second. Zero-size used gates are excluded by definition; q has full positive support on all maps. The q here is only a variational proof law on the actual ownership maps of one fixed reference, not a new freely selected output reference or a replacement of the base posterior.

## The coefficient gamma-1 is sharp

Take equal owned sizes s_l=L, fixed k,u, and let L tend to infinity. Write the weight as R(v)^gamma. Direct cancellation gives

    ln R(v)=-u ln k + Delta(v),
    Delta(v)=sum_l (L+v_l)ln(1+v_l/L)
                    -(kL+u)ln(1+u/(kL)).

Convexity of x->(L+x)ln(1+x/L) yields Delta>=0. The elementary bounds x<=(L+x)ln(1+x/L)<=x+x^2/L yield Delta<=sum v_l^2/L<=u^2/L. Thus

    k^(-(gamma-1)u) <= Z_tau(u)
          <= k^(-(gamma-1)u) exp(gamma u^2/L).

Equivalently the error in the limiting loss (gamma-1)u log k is at most gamma u^2/(L ln 2). Consequently the coefficient 1/5 in the first envelope cannot be reduced uniformly over fixed assignments; ownership-name erasure alone does not make this congestion factor >=1. This is an analytic limit with an explicit proved error, not a numerical extrapolation.

These assignments are realized by ACTUAL Boolean prime tables: let g be parity on m=kL coordinates, let T be its full spectral set, choose k distinct positive full-cell primes, and partition T into k sets of size L. Parity's positive implicants all require every coordinate, so every positive full cell is prime, and there are N=2^(m-1)>=k. Each used gate has kappa=s=m, the ownership graph is strongly connected and has exactly one source/root. Choose globally lambda_l=1/N, beta=1, and common orders on the table; all constraints hold. Root rarity is 2^-m, and fresh point activation retains a nonconstant parity core. These are positive-Fourier-mass assignment witnesses of the envelope's sharpness. They do NOT force this assignment in the optimized posterior, do NOT make the whole reference cost large relative to I, and do NOT disprove FEI.

## Retaining the actual base posterior and terminal cost

For full-support, equal-rarity tables the assignment graph has c=1. A007's added component factor is exactly one. With lambda=1/N and beta=1, L_0(T)=1 and, without changing eta_T,

    J_dist,U(T)=E_(tau|eta_T) Z_tau(u)
      >= E_eta 2^(-u H(a_tau)/5)
      >= 2^(-u E_eta H(a_tau)/5).

The second inequality is Jensen for the exponential; all old ranks, gate labels, root choices and chronological traces remain in eta_T. Retaining log[D'/(pD)]<=0 only after writing the complete signed identity yields the scoped bound

    Psi_dist <= (p r/10) sum_(T nonempty) P_g(T) E_eta_T H(a_tau).

Here p=2^-r and E_uniform_U |U|=r/2; empty U has zero size and contributes log L_0=0. The new ingredient is the ownership-entropy expectation under the ORIGINAL whole-set posterior. A007's complete residual therefore obeys, for this scoped table,

    R_F <= p R_g+(7/2)p I(g)
           +[6/5+log2(e)/4] I_core(F)
           +(p r/10) sum_(T nonempty)P_g(T) E_eta_T H(a_tau).

R_g is retained, not set to zero or replaced by known entropy. The original entropy theorem still separately retains h_2(Var F)+K_ref I(F). Surrogate B mass is not claimed to be exact queue probability or arbitrary terminal-reference CE. A007's original accepted claim assumes its full PRIME table; a general full-cell table need not be prime. The preceding scoped extension to arbitrary full-cell AND covers follows directly by the same trace construction, root/rarity ratios, rank bounds and signed identity: activating each listed full cell gives a legal fixed cover, without requiring it to be the complete activated prime table. Primeness is used only to identify that source's chosen table, not in those calculations. This extension is a narrow diagnostic proved here, not an expansion of the upstream reviewed statement. The inherited complete source cost of an arbitrary nonconstant core remains unpaid unless separately bounded.

## Exact posterior owned-size law for full-cell covers

This law closes the derivation step before the proposed concentration question. Take N distinct positive full cells on m coordinates, each with rarity pi=2^-m, lambda=1/N, and the same full physical order. Fix nonempty T of size s. A used k-gate assignment has sizes s_l>=1. Write X=sum_(j in T)x_j. Every gate has incoming edges from every other used owner, with weight equal to that owner's sum of selected coordinate variables. The rarity-weighted sum of incoming minors is pi X^(k-1): for k>=2 a root minor is its owned-coordinate sum times X^(k-2), and summing roots gives X; for k=1 the empty determinant gives pi. Its factorial moment is pi(s)_(k-1), independent of the partition sizes, where (s)_0=1. The common rank factor is independent of assignment.

Therefore, after cancelling that common factor and pi, the exact posterior mass on k and an ordered positive size vector is proportional to

    W_(k,sizes) = binom(N,k) N^(-k) (s)_(k-1)
                         [s!/prod_l s_l!]
                         product_l (s_l/s)^(gamma s_l),
    1<=k<=min(N,s), sum_l s_l=s.

The ordering here is the fixed increasing order of the chosen k gate IDs; no extra k! is inserted. Choose the k IDs in binom(N,k) ways, assign the s labelled coordinates with the displayed multinomial count, and retain the exact determinant factorial moment. This is the SAME old surrogate posterior, including root/chronological counts and label factors. Old rank order does not disappear from the base output cost; it only cancels in this conditional size law. No claim of exact actual-queue posterior is made.

The quantity needed in the previous subsection is consequently obtained exactly by averaging H(sizes/s) under these W weights. It depends on s,N and gamma, not on which positive full cells were listed. A finite proof-of-interface check compares the law against independent chronological-event moments for actual parity tables m=1,2,3 and each s=1,...,m (six cases and 91 labelled assignments). This supplies an explicit target for a tail bound rather than inventing a uniform ownership prior.

## First unsupported line and next mechanism

The remaining line for this selected full-support mechanism is a dimension-independent control of sum_T P_g(T) E_eta_T H(a_tau), with the same table and posterior; the crude bound <=Var(g) log n is insufficient for the new controller payment at fixed core variance. No such uniform bound is proved here. In addition, the base physical-location/rank cost p R_g is still not universally influence-paid, as the previous stages demonstrated. For general prime tables kappa_l need not equal s, and this envelope does not apply unchanged; A007's unequal-width component weights also remain.

A uniform conditional bound E_eta_T H(a_tau)<=C under the explicit W law would pay this specific correction by Psi_dist<=(C/5) I_core(F), since Var(g)=4b(1-b) and I_core(F)=2rp b. This is a precise conditional implication, not an assertion that the tail bound or the inherited base payment is proved.

NEXT should prove a tail for H(a_tau) under the exact W law above, or find an exact counterexample to that proposed tail. This attacks the newly isolated controller debt while preserving the nonconstant terminal core and identifies whether posterior concentration, in addition to ownership erasure, is the missing compression feature. It does not propose a universal representation lemma on the strength of a fixed-assignment envelope.
