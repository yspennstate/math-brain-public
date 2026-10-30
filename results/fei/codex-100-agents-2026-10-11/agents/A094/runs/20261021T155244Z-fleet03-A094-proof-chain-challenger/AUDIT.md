# Independent reconstruction of the carried-reference history chain

All Fourier transforms use the uniform probability measure. Entropy, cross entropy (CE) and divergence are in bits. A physical restriction fixes input coordinates; it is not conditioning the Fourier set. Statements below concern ideal CE; integer code rounding is separate.

## 1. Source chain and exact review scope

The source-complete A086 run is `20261014T093519Z`, not its later timestamp-only `.final` folders. Its RECONSTRUCTION sections 1–5 and REPORT have been read in full. The arbitrary-core envelope source `A011/20261014T074949Z/GENERAL_ENVELOPE.md` has also been read. The new dependency is A095's `20261014T074829Z/DERIVATION.md` sections 1–6, with its root construction reconstructed from `20261014T034647Z/DERIVATION.md` sections 1–6. Only the support-completion and finite core-query history clauses of the long A095-RANK-KL-EQUIVALENCE@5 claim receive a verdict here. Rank, shared-block and fresh-activation clauses are outside this review. The predecessor A094 shock/floor review is consumed as a recorded earlier result, not credited again.

## 2. A086 arbitrary-core envelope

For original coefficients a_T and point signs b_T, point-control probability p=2^-r and data point probability t=2^-n, the true data marginal is

q_T=a_T²-4pt b_T a_T+4pt²=(a_T-2pt b_T)²+4p(1-p)t²>0.

Young's inequality gives q_T≤2a_T²+6pt² because p≤1/2. This is a pointwise bound, not a normalized law. With β=6pt, the subprobability reference R†=(R+βU)/(1+β) has mass M=(s+β)/(1+β), and lifting by the actual conditional control law preserves that mass. All log costs are nonnegative. Consequently

CE(q,R†)≤2c+(2+β)log₂(1+β)+β[n+log₂(1/β)].

Here β≤3/2, log₂(1+β)≤2β and log₂(1/β)=n+r-log₂6. The conditional control entropy is at most 4p(1-p)tn+8rpt: designate the nonzero-frequency event of probability w=4p(1-p)t, use h₂(w)≤w log₂(1/w)+2w, and use log₂(2^r-1)=r+log₂(1-p) for its conditional cardinality. The log₂(1-p) terms cancel. These estimates yield CE≤2c+15(C+E+J), where C=2pt(n-d), E=2ptd, J=2rpt.

Physical edge counting gives I(F)=I(g)+C-E+J and E≤pI(g)≤I(g)/2 (each erased edge is an original incident pivotal edge). Thus c≤C₀I(g) is paid at rate 4C₀+15. If I(g)=0 the hypothesis requires c=0. Positive-cost constant references cannot be silently substituted. This establishes the general envelope portion of A086's chain at its stated scope. It does not preserve the rate under recursion.

## 3. A095 support-completed incoming reference

Let g have k≥1 coordinates, append m≥0 dummies, n=k+m and δ=2^-n. Select g and its full-vertex flip with a fresh fair bit. If S is the old Fourier support and s=|S|, old-sector coefficients are a_T-δη_T and every complementary coefficient has magnitude δ. Fourier inversion gives Σ_S a_Tη_T=1, hence old-sector mass 1-w=1-2δ+sδ². Boolean coefficient granularity gives |a_T|≥2^(1-k)>δ on S, so there is no cancellation, 1-w>0, and the actual root has full support even at k=1,m=0.

Calibrate a supplied normalized R to S, retaining the exact saving log₂R(S); call the result R_S and its cost c_S≤c. Define Q=(1-w)R_S on old atoms, δ² on every complementary atom. Atom counting gives total reference mass one. No true old conditional divergence is deleted:

CE(root)=Σ_S(a_T-δη_T)²ℓ_T -(1-w)log₂(1-w)+2nw,

D(root||Q)=(1-w)D(P_old/(1-w)||R_S), where ℓ_T=log₂(1/R_S(T))≥0.

Granularity gives Σ|a_T|ℓ_T≤2^(k-1)c_S and Σℓ_T≤2^(2k-2)c_S. Expanding the square, using δ≤2^-k, w≤2δ and 2/ln2<3, proves

CE(root)≤c+δ[(5/4)2^k c+4n+3].

The reference has completed support, but the source-dependent shock remains explicit. An arbitrary supplied reference is not replaced by the edited spectrum.

## 4. Actual inherited child models and complete terminals

For a query, let P_b be the actual physical-child spectra, m=(P_0+P_1)/2 and r the incoming Q marginalized over queried spectral membership. On m>0 set π_b=P_b/(2m), and on m=0 choose any fixed normalized pair retaining all r mass. Raw child models are 2rπ_b; their positive normalizers satisfy Z_0+Z_1=2. Normalize Q_b=2rπ_b/Z_b. On every positive child atom P_b/Q_b=(m/r)Z_b.

Disintegrating the original divergence, rather than changing its reference, gives

D_parent-average D_child=L-average log₂Z_b≥0,

CE_parent-average CE_child=Δ+L-average log₂Z_b≥0.

Here L is the actual queried-membership conditional KL, and Δ=H_parent-average H_child=B+JS(P_0,P_1)≥0. Positivity of normalizers follows from positive reference on true support; Jensen uses their exact sum two. All sums are finite; no limit interchange occurs. At a finite adaptive tree the same original reaches telescope to E CE_leaf=CE_root-Γ, Γ≥0. Individual leaf prices are not implied by this average identity.

Tensor an arbitrary independent terminal spectrum P_q and its prescribed normalized reference R_q, including reference-only zero true fibers. Choose zero-fiber posteriors depending only on the retained core. The raw models then factor, so Z_product=Z_core and Q_b=Q_core,b⊗R_q. Therefore both CE and divergence of the terminal remain fully additive through every core query. The terminal is never used as a bank for the core.

## 5. Adaptive physical edge debit

Run the same finite core-only policy on g and on the edited selector root. The policy queries no coordinate twice along a path and leaves padding, selector and independent terminals unqueried. Let Π_g be cumulative original queried influence. There is a unique path containing the edited vertex a. Let t_a count its queried coordinates and j_a count originally pivotal edges among them, with j_rem=j-j_a. At depth d the point mass increases by 2^d, cancelling its physical reach 2^-d. Each queried original point edge therefore contributes exactly δ(1-2p_i), with its original pivotal indicator p_i. All off-path branches are unchanged. Hence

Π_M=Π_g+δ(t_a-2j_a),

E I_leaf=I(g)-Π_g+δ[n+1-t_a-2j_rem].

This argument handles branch-dependent orders and stopping without creating a new bank at a child. Incident edges in distinct queried directions are distinct, and j_rem≤k-t_a at the point where that bound is used.

## 6. One-bank admission and its quantifiers

At K≥4 put S_K=KI(g)-c. Combining the last equations with the root bound gives

K E I_leaf-E CE_leaf ≥ S_K-KΠ_g+Γ
 -δ[(5/4)2^k c+(4-K)n+K(t_a+2j_rem-1)+3].

For nonconstant g, I(g)≥2^(1-k)>0, so β=Π_g/I(g) is defined. If c≤K₀I(g), K₀≥0, K>K₀, the remaining bracket is bounded using j_rem≤k-t_a, K≥4, and the positive quantity K(2k-1)+3. Dividing by I(g) produces the sufficient condition

2^-m[(5/4)K₀+kK+(3-K)/2]≤K-K₀-Kβ.

Under this condition E CE_leaf≤K E I_leaf, with the full same incoming reference. The right side of the admission must be nonnegative. For K₀=4,K=6, β≤1/6 and 2^m≥6k+7/2 suffice. Constants are a separate case: support calibration makes R_S a point mass and Q equals the actual point-defect spectrum; the admission division is not used. The point-defect H<4I calculation then pays each surviving point-defect leaf, while unaffected constant leaves have zero cost.

For g=h₃h₂ at the all-zero edit, I(g)=7/4, first queried original influence 1/4, and a second query on the matching first branch adds 1/4 with original reach retained. Thus β=1/7 and 2/7 respectively; the m=6 and m=7 admissions quoted by A095 are arithmetically valid. All original incident point edges are pivotal, so the edit subtracts δ per queried path edge. Both first children, and every second-history terminal core, remain nonconstant.

## 7. Verdict and first unsupported line

The A095 support-completion and finite core-only history clauses hold by the reconstructed chain above; this is a scoped acceptance of those clauses only. The A086 arbitrary-core envelope is also reconstructed without a repair. Neither conclusion changes full FEI's status. Exact validation and any formally checked algebra are reported separately; finite results do not supply the all-parameter proof.

The first unsupported universal line remains: for every Boolean core with its actual incoming reference, choose a useful continuation and pay KΠ_g beyond the explicit admission from measured Γ and genuinely unused original surplus, retaining both complete terminal references and erased edges at one fixed absolute K. The general envelope instead inflates 4C₀+15, and the history admission is conditional on a supplied core cost. A new point-floor or a zero-cost descendant reset does not close this line.
