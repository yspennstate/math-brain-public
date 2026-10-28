# Calibrated floors, query refunds, and the first hereditary obstruction

All entropies and divergences are in bits. Boolean functions take values in {-1,1}; every cube is finite and uniform. Full FEI remains open.

## 1. Independent reconstruction of A029@5

For F=(1-c)G+cH with independent CONTROL and DATA blocks, write a=1-2c, V=Var(a), gamma=Pr(G!=H), and eta=V gamma. At DATA frequency t let q_t be its true marginal and k_t the conditional probability of a nonempty CONTROL frequency. Parseval gives sum_t q_t k_t=eta. If V>0 the conditional nonempty CONTROL shape is the squared spectrum of a, conditioned nonempty, and does not depend on t. Zero-mass true rows contribute zero.

Keep the supplied reference row marginal and nonempty shape, and replace k by ell=(1-epsilon)k+epsilon eta, with 0<=epsilon<=1/16. The excess divergence over the canonical reference is

    C=sum_t q_t D_Bern(k_t || (1-epsilon)k_t+epsilon eta).

This cancellation needs the true q weights, not the reference row weights. Joint convexity of KL gives, by mixing the pairs (0,epsilon eta) and (1,1-epsilon(1-eta)),

    D(k||ell) <= (1-k)[-log2(1-epsilon eta)]
                 +k[-log2(1-epsilon(1-eta))].

Averaging uses the SAME eta=sum q k. Since 1-epsilon eta>0 and 1-epsilon(1-eta)>0, -ln(1-x)<=x/(1-x) yields

    C <= eta[epsilon-ln(1-epsilon)]/ln 2
      <= eta(1/16+1/15)/(2/3) = 31 eta/160.

Here ln(16/15)<1/15 and ln 2>2/3 (the first term of the positive atanh series is 2/3). At eta=0 or 1 all occupied k equal that endpoint and C=0; no cancelled denominator is needed. If V=0 the nonempty CONTROL shape is undefined but eta=0 and no new nonempty mass is requested. These are essential endpoint conventions.

Eta is harmonic under DATA restrictions. On a CONTROL query j it releases exactly gamma*ahat({j})^2, by the variance decomposition of a. Poincare gives eta<=gamma I(a)=I_CONTROL(F). Thus the already supplied eta/2 allowance pays this endpoint excess without an additional grant. This reconstructs A029's scalar and endpoint-account claims; it does not supply the initial H+T account.

## 2. The two distinct physical ledgers

At a node v let P_v be the true spectrum, Q_v the current reference, and Q^inh_vb the actual inherited references after a physical query. Let D_v=D(P_v||Q_v) and D^inh_vb=D(P_vb||Q^inh_vb). For normalized finite covering references inherited through the actual phase channel,

    L_v=D_v-(D^inh_v0+D^inh_v1)/2 >=0.

Indeed data processing for the channel to (physical outcome, erased spectral index), followed by the outcome/conditional chain rule, gives this inequality, including the actual outcome normalizers. Reference-only atoms require a declared stochastic completion; the fair completion is used here. The same finite identities apply under the source subprobability conventions when scalar mass penalties are retained.

Explicitly, if alpha_t and beta_t are the two parent Fourier coefficients over erased index t, send either input bit to outcome s and index t with probability (alpha_t+(-1)^s beta_t)^2/[2(alpha_t^2+beta_t^2)]. The two probabilities sum to1 whenever their denominator is nonzero. At a zero pair use1/2,1/2. Acting on P gives the true child joint law P_child(s,t)/2. Acting on Q gives the actual inherited joint law, whose outcome masses must be normalized separately. Cover guarantees those normalizers are positive because both true physical outcomes have probability1/2. The formulas include any reference mass on true-zero pairs.

If R_vb is the prescribed post-query model, the signed reset is D(P_vb||R_vb)-D^inh_vb. With actual global reaches w_v, finite telescoping gives

    CE(P_root,Q_root)+sum_resets w reset
       = H_root + E_leaf D(P_leaf||R_leaf) + sum_internal w_v L_v.       (A)

In contrast,

    sum_internal w_v Delta_v H + E_leaf CE(P_leaf,R_leaf)
       = H_root + E_leaf D(P_leaf||R_leaf).                             (B)

Thus (B) equals the initial CE plus signed resets MINUS the complete physical-query KL refund. A nonnegative terminal potential bounds (B); it does not, without another estimate, bound the raw left side of (A) by the same number.

The A026@6 endpoint bound retains this refund explicitly. Its saved code/check.py lines67-74 explicitly computes `refund`, proves `payment = incoming CE + raw - refund`, and bounds that payment. Therefore the existing A026 theorem is coherent with (B). The words "full payment" must retain its explicit refund convention. No claim that its numerical reserve fails to cover (A) is made. The same distinction applies to A029 equation(6): it is valid as its explicitly defined entropy-path/full-terminal functional; an unrefunded transaction interpretation needs sum w L paid from an actual unused account.

## 3. Two admissible strict-loss witnesses

More generally, for a SINGLE dictator controller with exact source references, ANY covering odds target preserving the true DATA marginal has Q-pair marginal equal to P-pair marginal on every erased controller pair. The explicit phase channel above depends only on that pair marginal. Querying the controller therefore sends Q to the exact true joint law: both inherited divergences vanish and both outcome normalizers equal their true values. Thus L=C for EVERY such target. This conclusion includes arbitrary Boolean source pairs and all their DATA restrictions, including the examples below. Zero true rows have zero target row mass and cause no denominator issue. Consequently outcome-normalizer refunds alone cannot account for the loss: the erased spectral bit carries the entire positive divergence in a nontrivial target.

First take f(y,z)=-1 only at (0,0), with y CONTROL. Its four true Fourier masses are all1/4. Keep the DATA marginal q(z-frequency)=1/2. Change only the empty-DATA-row relative odds by factor2, so its conditional CONTROL mass becomes2/3. The reference, ordered DATA bit first, is

    Q=(1/6,1/4,1/3,1/4).

This lies in A026@6's exact stated class: lambda_empty=2; epsilon_nonempty=0. The current source/controller references can be exact and the nonempty CONTROL shape is the singleton dictator. Query y. Since this phase channel depends only on the erased pair marginal, Q and P have exactly the SAME inherited children and true outcome normalizers. Hence both child divergences vanish, while

    L=D(P||Q)=(1/4)log2(9/8)>0.

Both children have entropy0; Delta H=2; the entropy-path terminal bill is2, whereas initial CE with no resets is2+L. This refutes only identification of (A) and (B) without the refund.

For a witness also INSIDE A029's new calibrated class, let a=y, G=1, H=AND2 on two DATA bits, epsilon=1/16. This is the three-bit point defect. Eta=1/4. The true DATA marginal is q0=5/8 and q_t=1/8 on the other three rows; k0=1/10 and k_t=1/2. The calibrated ell values are7/64 and31/64. In DATA-first order Q has empty-CONTROL masses285/512,33/512,33/512,33/512 and nonempty-CONTROL masses35/512,31/512,31/512,31/512. Querying the sole controller again gives exact true children, no terminal divergence, and

    16 L=log2[2^80*3^6/(5^10*7*11^3*19^9*31^3)]>0.

The last strict sign is an integer comparison in the checker. The costs obey the existing envelopes; neither example refutes those inequalities, FEI, or existential coordinate selection.

## 4. A root good-coordinate theorem on a full-FEI-hard class

The following identities refine A029's calibrated-carrier reduction by following the actual erasures and arbitrary physical interleavings. Let h be ANY Boolean function, m>=1, and use disjoint blocks:

    F_m=AND2(y,z) product_{r=1}^m h(x^(r)).

The gate Fourier law is uniform on four points. Therefore its controller odds k are1/2 in EVERY occupied DATA row, eta=1/2, and every calibrated target equals the true spectrum. The conversion cost is0. Exact disjoint tensor identities give

    H(F_m)=2+m H(h),       I(F_m)=1+m I(h).

For EACH gate coordinate, B_i(F_m)=1 and I_i(F_m)=1/2. Thus EVERY member of this class has a root relevant coordinate with B_i/I_i=2, independently of the unknown core. For each original core coordinate j, the tensor law gives B_j(F_m)=B_j(h) and I_j(F_m)=I_j(h). The gate does not improve those core ratios.

Query a gate coordinate. Both child squared spectra have entropy mH(h), so the exact entropy decrement is2, decomposed as B_i=1 and JS_i=1. One child is the unchanged product core (with a dummy remaining gate bit); the other is that core multiplied by the remaining dictator. That dictator has B=0 and can be removed, leaving the original core. With m=1, the restriction closure contains every Boolean h (up to sign and a removable dummy). Hence the root theorem at K=2 does not furnish a hereditary good-coordinate theorem.

For an arbitrary finite adaptive mixed restriction tree, every reached function still factors into the restricted gate and restricted cores. Nodewise tensor additivity and finite telescoping imply, component by component,

    Pi_H(F)=2-E H(gate_leaf) + sum_r [H(h)-E H(h_r,leaf)],
    Pi_I(F)=1-E I(gate_leaf) + sum_r [I(h)-E I(h_r,leaf)].

The adaptive choice can depend on all earlier outcomes; conditional at a fixed node the remaining disjoint cubes are uniform and independent, so factorization still applies. No probabilistic independence of different leaf components is asserted or needed. Gate entropy remains2 until its first query and becomes0 thereafter. Consequently its entropy contribution is exactly2 times the probability of reaching a first gate query; its erasure contribution is exactly that probability (subsequent gate erasures are0). This accounts for the carrier once across all branches, not once per leaf.

For a complete gate-only peel the gate spends exactly1 influence and2 entropy, leaving signed rate-K surplus K-2; the terminal core retains mH(h) and mI(h). No repeated grant of K-2 is licensed. A universal FEI bound on these calibrated terminals implies full FEI by dividing 2+mH(h)<=K(1+mI(h)) by m and taking m->infinity. Conversely full FEI bounds the subclass. This is a reduction, not a divergent-ratio family.

## 5. Checks that could fail; first unpaid line

Checks target: nonnegative/zero eta endpoints, constant controllers, relevant-coordinate denominators, ghost support, actual branch normalizers, true versus reference calibration, signed reset orientation, both physical query blocks, and all output signs. Main finite validation includes ALL labelled two-bit controllers and two-bit source pairs, with no symmetry reduction. It certifies exact algebra and scalar inequalities on that domain, not the all-dimensional theorem. A separate direct-character/physical-edge implementation verifies the carrier identities, gate ratios and arbitrary adaptive nodewise decompositions for all h on0..2 bits and m1,2. The continuum and arbitrary-tree assertions follow from sections1-4.

The review rung is a mathematical proof with exact finite validation; independent acceptance of this review's consequences remains pending. Any Lean result concerns only its separately stated real-algebra accounting identity. It cannot certify the entropy/channel/carrier arguments.

The first universal unpaid line remains an ORIGINAL influence-priced covering source and a required hereditary stopping policy for arbitrary h. If a consumer instead charges raw transactions, it must additionally pay sum w L from its SAME actual unused original account or explicitly authorize and retain the refunds. The root K=2 carrier theorem shows why proving more affordable root conversions cannot replace the hereditary core step.
