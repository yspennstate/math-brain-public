# Audit of w516 P0297 response reduction

2026-10-10, w517. The independent O1/O2 checkpoint was saved before reading the paired proof; SHA256 of that checkpoint: DDB59C8F513D22C690AB40C3A7A675D3B4E1BFFBF806C131ED5894672733D360. This is a chronology receipt, not a proof certificate.

Read w516/ATTEMPT.md, L1-L5, after that checkpoint. This audits the author derivation, not another auditor's review. Mathematical checks and the final row verdicts remain in progress.

The highest-risk step is the passage from finite, fixed-xi switching responses to explicit masses of the limiting scale measure (input H). The author explicitly states: "L1-L5 do not evaluate it." The independent O2 shows why marginal Gaussian information and constant-shift identities cannot close that input at exponent scale.

Finite L1 check: differentiation of the soft path weights gives a covariance term with a minus beta factor; Gaussian integration by parts reproduces xi E[A_beta-beta B_beta]. Positive semidefiniteness suffices for 0<=A_beta<=V and B_beta>=0. The squared-distance pair formula has no missing factor of two.

Finite L2 check: positive definite C plus distinct coefficient vectors makes pairwise analytic tie sets null at each fixed xi>0. The first envelope derivative is valid. Rearrangement of L1 and dominated convergence for A_beta and the first xi derivative prove the fixed-model limit for beta E B_beta; they do not give uniform domination for beta B_beta.

L3 check: O1 independently gives E F=-xi/sqrt(pi) for two independent standard Gaussian single edges, so S=1/(xi sqrt(pi)). The proposed nonzero switching limit is consistent. My O2 is a separate exponent-scale obstruction beyond the two-edge calculation.

L4 check: its absolute log bounds need the horizontal path retained in every finite family and every quadrature's positive coefficients summing to the Euclidean path length. Under those stated construction choices the lower path-length bound is one and the upper horizontal bound is one. The variance/median bridge is compatible with errors of order sqrt(T)=o(T). No uniform quantitative complexity for the approximating family is established or needed for its existential reduction.

L5 check: pointwise convergence to a continuous function and monotonicity of Psi_n justify convergence of the Stieltjes measures on compact interior intervals. This does not make the limit absolutely continuous or give a density. A zero-temperature near-tie estimate alone also leaves the within-path covariance contribution unevaluated.

Concrete next lemma supplied: NEAR_TIE_LEMMA.md gives an explicit two-route error bound under local Lipschitz regularity of the weighted gap density. Its normalized form states exactly what a joint temperature/cutoff limit would require. Those uniform hypotheses and multi-route competitiveness are not proved for LFPP here.

Provisional audit decision: keep L1-L5 as a qualified reduction with input H visibly open; reject any relabeling of this packet as an exact generic dimension proof. Final referee check belongs to w518.
