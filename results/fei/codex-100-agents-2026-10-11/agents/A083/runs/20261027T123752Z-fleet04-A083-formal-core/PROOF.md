# Exact target and verdict

A097-HIGH-MOMENT-MATCHED-QUERY-LOSS@1 is reconstructed unchanged. The remaining tail coordinate also has large loss: for every even n>=4, its same explicit Boolean function and reference have

    n-1/2 < min_i L_i < n,
    2n-1 < min_i L_i/Inf_i < 2n.

Thus existential choice of the FIRST physical coordinate cannot give a dimension-independent local payment from these matching hypotheses. This is a scoped obstruction for a supplied reference, not a divergent Boolean H/I family. H/I=2 exactly. The universal original-source construction is still open.

# Construction and proper marginals

Put f=product_j h(x_(2j-1),x_(2j)), with h=-1 only at pair(+,+). Its four Walsh magnitudes are1/2, so P is uniform on2^n spectral sets, H=n, every Inf_i=1/2, and I=n/2. Write N=2^n and e=2^(-4n). On the face S={n} union V, V subset[n-1], let Q(S)=[1+(1-e)(-1)^|V|]/N; off the face Q(S)=1/N. The face has equal positive/negative parity classes, so Q is normalized and strictly positive. The vacuum is off the face and remains1/N.

Every marginal on at most n-2 coordinates agrees with P. Indeed at least one of the n-1 free coordinates is absent from the kept set, and summing that coordinate cancels the parity perturbation. This argument includes marginals that retain coordinate n, arbitrary assignments of the retained coordinates, and all inclusion moments of that order. No independence of physical query outcomes is assumed. Affine calibration using only these matched moments leaves Q unchanged: Q is feasible, has relative entropy0 from itself, and uniqueness of its information projection follows from strict convexity. Its calibration release is0.

# Root divergence and free-coordinate losses

Exactly N/4 reference atoms have mass e/N, N/4 have mass(2-e)/N, and N/2 have mass1/N. Therefore

    D=D(P||Q)=(1/4)log2[1/(e(2-e))]
              =n-(1/4)log2(2-e),
    n-1/4 < D < n.

For i<n the two signed perturbations cancel in every erasure fiber. Thus pi_i Q=pi_i P is uniform, and L_i=D. This independently reconstructs A097's statement at k=n-1. It also shows CE(P,Q)=n+D<2n=4I. No capacity additional to that original source is inferred.

# The omitted tail coordinate

Deleting coordinate n instead gives, for every V subset[n-1],

    (pi_n Q)(V)=[2+(1-e)(-1)^|V|]/N.

Its two mass classes are (3-e)/N and(1+e)/N, each on N/4 atoms; the true marginal has mass2/N. Hence

    d=D(pi_n P||pi_n Q)
      =(1/2)log2[4/((3-e)(1+e))],
    L_n=D-d.

Since 0<e<1, (3-e)(1+e)=4-(1-e)^2 is strictly between3 and4. Thus0<d<(1/2)log2(4/3)<1/4, where the last strict inequality is the exact rational inequality(4/3)^2=16/9<2. Combining with n-1/4<D<n gives n-1/2<L_n<D<n. Therefore the exact minimum over ALL coordinates is L_n; the claimed all-coordinate and influence-normalized inequalities follow. Unlike the free-coordinate erasures, this tail erasure leaves nonzero marginal divergence. Dropping it would be a real formula error, even though the weaker lower bound remains valid.

All formulas hold for every even n>=4. This is a finite-law proof for each n; no infinite sum, limit exchange or numerical logarithm estimate is used. At n2 the root face construction fails to match every required individual marginal (order n-2=0 no longer includes influences); the all-high-moment statement is intentionally not extended there.

# Actual children and the full account

For any physical query, the queried two-bit factor becomes either a constant or a dictator of its partner, and the other disjoint factors remain. Each child spectral law is uniform on2^(n-2) sets and H_child=n-2. The constant-factor child has influence(n-2)/2 and the dictator-factor child has influence n/2; their mean is(n-1)/2. Their average law is the uniform erased law, and physical influence conservation holds: I=1/2+average I_child. The two child supports are complementary according to whether the partner lies in the spectral set. Because n>=4, at least one other free coordinate remains, and the parity term is balanced on each child support.

Let d_i=0 for i<n, d_n=d. Direct summation then gives, for BOTH children,

    D(P_child||pi_i Q)=1+d_i,
    CE(P_child,pi_i Q)=n-1+d_i.

The exact full-child CE change is -1-L_i, because root CE=n+D and L_i=D-d_i. In the projection-history identity, J_i=1 and average child divergence=D+1-L_i. Consequently the large first loss is paid by already charged initial divergence D; it cannot be charged locally to Inf_i with a universal constant, nor released again as unused money. Old U, BOTH physical terminals and the original source CE remain in the ledger. This is consistent with A012/A097's complete history theorem and does not require a new source after querying.

# Proof status and first unsupported universal line

The all-dimensional derivation above is an analytic proof pending independent review. Exact certificates cover the frozen finite n4,6,8 domain. A separate Lean target, only if admitted, checks finite n4 rational fiber formulas and the rational16/9<2 bound, not real logarithms, entropy identities or the all-n theorem.

First unsupported universal line: produce a useful original full reference with CE<=C I for EVERY Boolean core, or a required productive interface whose full query-KL losses are paid by actual unused original influence after all old charges and both full terminals. The present source has ample initial divergence to pay its own loss and is not a counterexample to that global theorem. Selecting a coordinate on the basis of high matched moments alone is now ruled out even existentially.
