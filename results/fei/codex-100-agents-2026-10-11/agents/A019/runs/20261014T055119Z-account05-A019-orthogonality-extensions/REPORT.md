# A019 stage5: private-query empty-row transport, sharp curvature and zero-row repair

Full FEI remains OPEN. This stage consumes A018/A020's independent full-scope acceptance of A019's previous theorem and A020's warning that positive raw W is not necessarily a localized debt. It closes an explicit low-disagreement reference-transport case: after a genuine private-core query with two balanced children, an absent-frequency convention on zero true rows makes the net activation-reference surcharge nonpositive, with arbitrary supplied complete child references retained. Without that convention an essential sparse query has fixed positive surcharge as disagreement tends to zero. A sharp bound also prices the scalar empty-row curvature when an inherited core and a nonlinear two-bit mask both have nonzero means. The remaining general signed refund is stated, not discarded.

## exact target, quantifiers, hypotheses and units

All physical bits are independent and uniform, outputs Boolean signs, and entropy, KL and complete reference CE use bits. Let s be a nonlinear Boolean sign mask on two shared bits, so sigma=E s is plus or minus1/2. Let h(q,u) be any Boolean private core, with actual children h_0,h_1, means beta_0,beta_1, mean beta=(beta_0+beta_1)/2 and physical query disagreement d=Pr[h_0!=h_1]. Set F=1 at gate x0 and h*s at x1; both child fallbacks h_b*s stay nonconstant when h_b is balanced. The same supplied finite normalized mask reference Q_s and supplied normalized finite-cost core references are carried throughout.

Define eta(t)=-t log2(t), Psi(a)=eta((1+a)^2/4)+eta((1-a)^2/4)+1-a^2-eta(a^2)/2, and A=(9/8)log2(3)-1. Then the actual private-query profile curvature is sharply bounded by

0 <= Psi(beta*sigma)-[Psi(beta_0*sigma)+Psi(beta_1*sigma)]/2 <= A*d.

For the physical-label mixture reference introduced by A018, let c_v be its supplied core cost, c_s the fixed mask cost, and D_v its exact nonnegative posterior-label KL refund at a core-tree node v. The full cost is CE_v=c_v/2+c_s/2+Psi(beta_v*sigma)-D_v. If the parent core reference is the actual queried-frequency conditional lift of the average child references, define D_core=average_child KL_core-KL_parent_core>=0. The exact net reference insertion is

CE_parent-average_child CE = Delta H_core/2 + curvature + Lambda,
Lambda=average_child D_child-D_parent-D_core/2.

If beta_0=beta_1=0 and the parent reference conditional on every zero true data row assigns the queried frequency absent, then Lambda<=0. Hence CE_parent-average_child CE<=Delta H_core/2, uniformly as d tends to zero. Supplied terminal costs are not removed. The equal-split convention on zero rows does NOT satisfy any universal Lambda<=K*d: an actual rate4-certified core family below has Lambda=(1/2)log2(18/17)>0 and d=2^-k for every k>=1. This is a no-go for an explicit reference transport rule, not FEI.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot2026-10-14 05:41UTC; B04 STREAM_NOTES.md v2, unchanged2026-10-11 23:25UTC; own STATUS, previous-stage report and finalizer; and the complete EXECUTION_PROTOCOL.json, revision2026-10-11-execution-v2. Earlier required campaign and paper readings remain context, not new proof dependencies.

New source-bound reads: A018 run20261014T051305Z-account05-A018-shared-data-collision-law REPORT.md and CLAIMS.json, sections1-2,4-6 for one physical-label mixture, exact empty-row posterior refund, eligible negative prior-change witness and independent A019 acceptance; A020 run20261014T032122Z-account05-A020-selector-boundary-tests REPORT.md and CLAIMS.json, balanced gate, arbitrary-core parity, positive W/zero bad bill and its A019 acceptance. The unchanged A019-INTERNAL-PIVOTAL-EDIT-ACCOUNT@1 receives two full-scope independent reviews; this stage records their sources without rewriting the earlier immutable run.

Read A092 LEARNED.md stage5 and run20261014T045641Z-account05-A092-counterexample-referee REPORT.md. Its four-bit conditional-product reset obstruction concerns entropy drift versus conditional KL and has its own repaired net price. The present obstruction uses a different, specified physical-activation/core-lift reference, with essential disagreement tending to zero, and the failure occurs on reference-only empty core rows. It is not an independent discovery of A092's generic reset warning. Our remedy directly specifies those zero-row reference masses.

The existing A019-RARE-TRANSLATION-COLLISION@1 point-phase bound H<=4I is consumed only for eligibility of the sparse family's supplied core bank; its analytic formula was already independently accepted by the stream lead. We do not rederive the constant-correlation corollary, activation closure Gamma, bent-splice lower bound, or the refuted paired-row scalar proposal. The bent-splice falsifier remains a required restriction: equal Fourier magnitudes are never presumed for arbitrary core surgery. Sources/read scopes and current byte hashes are saved in out/SOURCE_RECEIPTS.json. No web or external paper fact is needed.

## complete derivation or exact first unsupported line

### 1. Reconstruct A018's exact physical-label reference at the needed scope

For G=h*s, disjoint physical blocks give mean mu=beta*sigma, spectrum P_G=P_h tensor P_s, and supplied reference Q_G=Q_h tensor Q_s, cost c_h+c_s. With F=1 at x0 and G at x1, its nonempty G rows have two x coefficients Ghat(T)/2; the empty row has coefficients(1+mu)/2 and(1-mu)/2. Thus H(F)=H(G)/2+Psi(mu), I(F)=I(G)/2+(1-mu)/2. The data law is R=(P_G+delta_empty)/2. Use the SAME physical mixture q=(Q_G+delta_empty)/2 and lift it by F's actual conditional x-frequency law, including an arbitrary normalized conditional on zero true rows. This is a normalized finite-cost complete reference.

The tagged physical-branch KL is KL(P_G||Q_G)/2. Marginalizing its tag yields KL(R||q), and their difference is posterior-tag KL D>=0. Only the empty G row has tag ambiguity, so exactly

D=(1+mu^2)/2 KL_Ber(mu^2/(1+mu^2) || Q_h(empty)Q_s(empty)/(1+Q_h(empty)Q_s(empty))).

Consequently CE_F=(c_h+c_s)/2+Psi(mu)-D. Finite CE excludes unsupported positive true atoms; if mu=0, the binary formula simply becomes D=(1/2)log2(1+Q_h(empty)Q_s(empty)). This independently reconstructs A018's normalized reference identity and posterior-refund clause, with no author checker imported. Review scope does not include A060's sharp Gamma optimization or A018's entire negative-prior-change claim.

### 2. Sharp biased empty-row curvature after an actual core exposure

Set phi(b)=Psi(b/2). Evenness of Psi makes the sign of sigma immaterial. For b!=0,

phi''(b)=(1/4)log2[b^2/(4-b^2)].

Thus K(b)=-phi''(b) is nonnegative, even, and decreasing in |b| on[-1,1], with an integrable logarithmic singularity at zero. Extend K by zero outside that interval. For child-mean midpoint t and radius r=|beta_0-beta_1|/2, the Jensen gap is exactly

(1/2) integral_-r^r (r-|u|) K(t+u) du.

This is maximized at t=0. To verify rather than assume rearrangement, write the triangular weight as an integral of centered interval indicators. An even decreasing nonnegative function integrates most over a centered interval of prescribed length: moving such an interval away from zero replaces its nearer endpoint segment by a farther segment. Integrate that inequality over the layer lengths. Truncation and monotone convergence handle the integrable singularity. The derivative is absolutely continuous, so the displayed second-derivative integral identity remains valid across zero.

The gap is therefore <=phi(0)-phi(r). That function of r is convex, vanishes at0, and lies below its endpoint chord r[phi(0)-phi(1)]. Exactly Psi(0)=2, Psi(1/2)=3-(9/8)log2(3), giving A=phi(0)-phi(1). Actual Boolean child disagreement satisfies |beta_0-beta_1|<=2d by averaging pointwise differences. Hence curvature<=A*d. Positivity is concavity. A is positive and below1, as 2^8<3^9<2^16.

The bound is sharp: h is the actual queried character, with means1 and-1 and d=1. Both children can instead remain nonconstant by taking h_0 a rare point-defect sign and h_1=-h_0: their means tend to plus/minus1 while d stays1 and the ratio tends to A. This is an all-dimensional proof; finite tests are not a continuum bridge. In physical F-query units the scalar charge is 2A*Inf_q(F), since Inf_q(F)=d/2.

### 3. Exact signed insertion with one carried core hierarchy

Let P_b be the two child core spectra on unqueried rows, and Q_b their supplied complete references. On the parent core's positive unqueried row U use its actual conditional queried-frequency law nu_h(L|U). Set Q_h(L,U)=nu_h(L|U)(Q_0(U)+Q_1(U))/2; on zero true rows choose a specified normalized conditional. Marginal log-sum gives

KL(P_h||Q_h)<=average_b KL(P_b||Q_b),
D_core=average_b KL(P_b||Q_b)-KL(P_h||Q_h)>=0,
c_h=average_b c_b+Delta H_core-D_core.

Substitute this identity into the three exact activation CE identities from section1. It gives the stated CE insertion with Lambda=average D_b-D_parent-D_core/2. Every supplied child CE, the fixed mask reference and the posterior refunds remain. This is the precise correction to treating the A018 refund as hereditary available credit. No separate bound on raw W is required. The reference tree carries its existing sources; it is not reset to unknown exact terminal spectra. Consistency of the incoming parent core reference with the displayed child lift is an explicit hypothesis, not a license to replace an arbitrary previously fixed incoming reference after a query.

For any finite core-only stopping tree, the profile curvatures telescope as phi(beta_root)-sum_leaf pi phi(beta_leaf). Their local bounds sum to <=A sum_internal pi d_v=A[I(h_root)-sum_leaf pi I(h_leaf)]. The D and D_core terms must also telescope as signed potentials; a nonnegative D at each individual node does NOT permit deleting the positive average child D in the parent insertion. The bound is a single physical reserve for the profile term, not a new allowance per depth.

### 4. Uniform zero-row repair when both children remain balanced

Suppose beta_0=beta_1=0. Then the entire parent core empty unqueried row has zero true mass, not merely one Fourier coefficient. Specify nu_h on zero true rows by putting all its mass on the queried frequency ABSENT, as a fixed convention in the incoming reference construction before sampling. This gives Q_h(empty)=[Q_0(empty)+Q_1(empty)]/2. This allowed convention preserves normalization and every positive true core cost; changing it may nonetheless affect activation CE because the constant physical branch puts true mass on the empty row.

With t=Q_s(empty) fixed, all three activation refunds reduce to D_v=(1/2)log2(1+t Q_v(empty)). Concavity of log(1+t a) yields average D_b<=D_parent. Therefore Lambda<=-D_core/2<=0. The profile curvature vanishes, and CE_parent-average CE_child<=Delta H_core/2, as claimed. This holds for arbitrary finite-cost supplied child references, arbitrary nonlinear mask reference, every private dimension and arbitrary small query disagreement. The fallback h_b*s remains nonconstant because h_b is balanced and s is nonconstant. No entropy/I bound for h itself is supplied by this reference identity.

### 5. Essential rare-query obstruction under the equally split zero-row convention

For every k>=1, let u be one private bit and v a disjoint k-bit cube. Put h_0=chi_u and h_1=chi_u*(-1)^1_(v=0). Expose one physical query q choosing these children. Both children are balanced and nonconstant; q is essential with d=2^-k. The parent's and children's true empty core coefficients vanish. Supply Q_b=(P_b+delta_empty)/2. Each child core KL is exactly1. On every positive true parent row the conditional lift gives Q_h=P_h/2. The empty unqueried row has reference mass1/2 and true mass0. If its conditional splits equally between queried frequency absent/present, then Q_h(empty)=1/4. Parent core KL is also1, so D_core=0.

Take s a positive-mean two-bit point defect with its exact flat squared spectrum Q_s, Q_s(empty)=1/4 and c_s=2. The child activation refunds are (1/2)log2(9/8), while the parent refund is (1/2)log2(17/16). Thus

Lambda=(1/2)log2(18/17)>0,
Lambda/d=2^(k-1)log2(18/17) -> infinity.

The decisive sign is the integer comparison18>17. This refutes only the stated universal query-price inequality for the equal-split reference transport, including any attempt to cancel it by D_core/2. These references are not pathological unsupported costs: every parent and child core reference is rate4 eligible. A character contributes I1,H0. The other phase is respectively a point defect on k or k+1 fresh bits, and the previously proved H_phase<=4I_phase gives H_core+1<=4I_core-3. Thus at least3 bits of certified core slack remain; its half-branch reserve exceeds the constant debt, which is below1/2. No FEI or owned-child-bank theorem is refuted.

Under the absent-query convention instead, Q_h(empty)=1/2, D_parent equals the child refunds, and Lambda=0 for this same essential rare-query family. The full branch references and all terminal costs are kept; only a reference-only row assignment changes. This provides an exact low-disagreement repair on an unbounded structured class, not a new positive-correlation result or new activation constant.

### 6. Changed universal gap and exact first unsupported line

The profile curvature for biased cores and nonlinear two-bit masks is now paid sharply by one query reserve. The remaining term Lambda is quantified and controlled nonpositively for two balanced child cores under a specified zero-row convention. For general children of nonzero means, the empty row has true mass and its parent conditional can no longer be chosen freely. The first unsupported universal line is a support-aware policy and unused certified child slack that pay the positive part of Lambda while retaining the same Q_s, the full c_b costs, the core-query refund and later descendants. Neither the bounded scalar curvature nor the false paired-row subadditivity supplies that bank. The successful balanced-child repair identifies the exact hypothesis to remove next; enlarging the sparse-family dimension is unnecessary.

## executed validation with domain, arithmetic, commands and outputs

Every specification preceded its job; pilots preceded the larger new Boolean domains. All jobs estimated100MB or less and had a60second cap, so no >300MB memok gate was needed. Actual peak memory was not measured. Runs were sequential with no randomization, GPU, automatic domain growth, background helper or window. Reported times measure checker work; shared-machine shell overhead is not included.

From the A019 directory, all commands use `python -X utf8` and the prefix `runs\20261014T055119Z-account05-A019-orthogonality-extensions\code\`:

- `check_exposure.py --pilot`:16 cases,450 exact assertions,0.009693seconds. Full `check_exposure.py`:3216 reference cases,149254 exact assertions,7.076236seconds. It exhausts every core in dimensions1,2,3 and every private query, using two fixed nonlinear mask signs and exact/uniform supplied child references with the equal-split zero-row lift. There are128 nonflat core tables and596 actual queries with both children nonconstant before mask/reference choices. Direct actual Boolean spectra, physical query influence, every normalized parent/child reference atom, complete CE, exact posterior refunds and sharp curvature inequality are checked.
- `check_refund.py`:804 fixed core-query cases,2.013374seconds. Exact sign census:54 positive,544 negative and206 zero net Lambda cases for uniform child references. It records both sign witnesses, not an all-dimensional sign claim. The positive two-bit example has two nonconstant children and exact Lambda=(1/2)log2(18/17); it motivated the essential sparse extension. Negative witness Lambda=-3/2+(9/8)log2(3)-(5/16)log2(5). These are exact prime-log certificates, not floating discoveries.
- `check_sparse.py --pilot`:one k1 case,101 assertions,0.004080seconds. Full `check_sparse.py`:eight frozen k1..8 actual Boolean parents up to13 total physical bits,15698 assertions,0.640094seconds. Every core/reference KL identity, essential query disagreement, both nonconstant children, constant net debt and all supplied rate4 core certificates pass. The infinite family follows section5, not escalation or finite extrapolation.
- `check_balanced_repair.py --pilot`:32 cases,610 assertions,0.018577seconds. Full:464 cases,17958 assertions,1.033120seconds. Every dimension2/3 core query with two balanced children and all four independently chosen exact/uniform child reference types passes the absent-query zero-row convention, posterior-refund monotonicity and full CE/core entropy-decrement comparison.

The principal exposure, sparse and repair jobs together have3688 cases and182910 exact assertions, excluding pilots. The additional804-case sign census is reported separately because its counter checks are internal helper calls rather than a fixed theorem-assertion count. All actual cases are enumerated without symmetry quotient. Exact algebra uses rational prime-log coefficient identities. Required signs use range-reduced36-term Fraction atanh series with positive tail bounded by2z^73/[73(1-z^2)] for0<=z<=1/3. Exact zero forms are canceled symbolically, not by tolerance. No precision escalation or assertion failure occurred. Every dimension or sparse parameter completion was saved immediately; first transport-sign witnesses were saved upon discovery.

## proof dependencies and changed downstream conclusions

The curvature proof, exact query insertion, balanced-child support repair and sparse no-go are proved analytically at stated scope. The activation reference identity is a scoped independent reconstruction of A018-JOINT-CONSTANT-BRANCH-REFERENCE@1, preserving its hypotheses. A019-RARE-TRANSLATION-COLLISION@1 is needed only for rate4 eligibility of the sparse reference bank, not for the no-go or support repair. No B04 node-boundary inequality or optional paired-row scalar claim is used in the new proofs.

A019-INTERNAL-PIVOTAL-EDIT-ACCOUNT@1's A018/A020 independent reviews are consumed unchanged, with exact original statement digest retained. The new source-complete application remains independently unreviewed. It is scoped work on an existing interface and a useful source review, not a new broad universal candidate under the stream cap. A018/A020/B04/A090/A091/A095/A097/A092 should keep exact localized B, specify zero true row reference conditionals, and retain the signed average child posterior refund. The sparse bank example shows why a debt cannot always be priced by removed influence alone even with eligible child certificates; its unused source slack, rather than its query influence, is the available owner.

## one next mathematical action and independent reviewer

Replace one balanced child in the support-aware query repair by a biased nonflat child, while both fallbacks remain nonconstant; keep Q_s and the same complete child references, derive the positive Lambda from the true empty-row likelihood, and test payment from a named unused core slack. Use the essential sparse equal-split/absent-query pair as a zero-row guard and A018's eleven-bit positive-excess case as a collision guard. A018/A020 review the sharp curvature, actual reference formulas and balanced-child repair; A090/A091/A092 challenge the signed refund and sparse all-dimensional no-go. This removes the repair's enabling hypothesis, rather than searching larger versions of an already settled rare-query family.

## actual persistence receipts or precise save blocker

The four protocol files, code/, out/ proof checkpoints, frozen specs, exact reference and sign certificates and source receipts are saved in this run. STATUS.md stays exactly two lines; WORKLOG.md and LEARNED.md receive dated updates. code/finalize.py verifies exact protocol schemas, all canonical statement hashes, unchanged reviewed-source statement identity, identical packet delta, report fields, JSON parsing,20MB size limits and local SHA256 receipts. New independent review, shared adoption, supervisor copying and remote mirror verification are separate and remain pending.

## Universal bridge

This stage moves C020/C024 and B04's C019 private-query interface by paying the biased nonlinear-mask profile curvature sharply atA=(9/8)log2(3)-1 per core disagreement and proving nonpositive net activation-reference surcharge for arbitrary supplied two-balanced-child cores under an explicit absent-query zero-row convention. It also sharply diagnoses the failed convention: an essential query of disagreement2^-k has fixed positive net reference debt(1/2)log2(18/17) despite rate4-certified terminal references, while the support-aware assignment repairs that same family exactly. No universal FEI constant improves; arbitrary biased-child posterior likelihood, unused terminal slack and its ownership through later restrictions remain open. NEXT removes balance in that exact signed reference insertion, the shortest route because it tests the one hypothesis that permits the zero-row refund rather than re-closing a class or paying irrelevant raw derivative surplus.
