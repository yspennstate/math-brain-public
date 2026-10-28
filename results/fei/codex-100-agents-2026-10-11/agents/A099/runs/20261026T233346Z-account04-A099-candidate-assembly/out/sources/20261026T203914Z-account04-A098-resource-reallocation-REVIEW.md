# A098 stage21 independent reconstruction

All entropies, cross-entropies and divergences are in bits. These reviews do not settle full FEI.

## A096 ghost-complete inherited references

Reviewed source: A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT@1, statement hash f56d45dca2a12323d1e4cffc916581d684014f5e8a5809d069cbb91cc1990cdb, DERIVATION sections2--5 in run20261023T140303Z-account03-A096-live-gap-ledger. The statement holds at its stated scope, without repair.

Supply Q=bP+sum c_j delta_Wj, b>0, c_j>=0 and b+sum c_j=1. For a physical query let R=M_i P and V=M_i Q. Actual Boolean restriction gives (P_0+P_1)/2=R. On R(u)>0 put K_t(u)=P_t(u)/(2R(u)); on R(u)=0 choose any single stochastic split shared by source and reference. Both actual child masses vanish there, so the true joint experiment remains P_t(u)/2. The reference experiment is V(u)K_t(u).

Its outcome mass is r_t=b/2+sum c_j K_t(M_i Wj)>=b/2>0. Hence Q_t=VK_t/r_t equals [b/(2r_t)]P_t plus the original witness atoms with coefficients c_j K_t(M_i Wj)/r_t and erased labels. This includes empty labels, repeated labels, zero weights, and ghosts that collide with true support. The complete coefficients sum to one. No ghost mass is discarded.

Define A=D(P||Q) and D_e=A-D(R||V). Disintegration along M_i gives D_e>=0. Applying the same K to R and V preserves their KL exactly: the factors K cancel wherever true joint mass is positive; zero rows contribute zero true mass, but remain in reference normalizers. Disintegration of the joint experiment by outcome therefore gives

    A = D_e + D(fair||r) + [D(P_0||Q_0)+D(P_1||Q_1)]/2.

Write B_i=H(P)-H(R) and J=H(R)-[H(P_0)+H(P_1)]/2>=0. Adding entropy and KL gives

    B_i + average CE(P_t,Q_t) - CE(P,Q) = -J-D_e-D(fair||r).

All denominators used above are positive where cancelled: R is used only on R>0, r_t>=b/2, and Q>=bP ensures finite true-support likelihoods. There is no exchange of an infinite sum or limit. Induction on the finite physical tree multiplies each identity by its actual reach and cancels internal terms; both full terminal costs remain. Also log(1/b_t)=log(1/b)+log(2r_t), so averaging gives the claimed envelope decrease D(fair||r). This proves arbitrary finite adaptivity, not just a fixed coordinate order.

For any normalized finite-CE reference Q, every Q(s)/P(s) on true support is positive. A positive b smaller than their finite minimum and than1 makes Q-bP a nonnegative residual of mass1-b. Decompose that residual into at most2^n atoms. This existence statement gives neither a compact description nor an influence price. In particular CE(P,Q)>=H(P); a universal complete-source CE<=K I would already imply FEI. The transport identity alone cannot pay that initial entropy.

Boundary/adversarial checks: constant and irrelevant queries; source-zero erased rows with fair and deterministic completions; biased reference outcomes; ghost-to-occupied collisions; both Boolean child spectra; complete adaptive histories. Exact prime-exponent identities, independently reconstructed from literal Walsh sums, verify KL disintegration, complete CE payment and the envelope. Standard finite log-sum inequalities establish nonnegative KL; entropy concavity establishes J>=0.

## A097 signed admission from the current reference

Reviewed source: A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER@1, statement hash8e3a5074a89063d0bb52d1a8ac5d9e3743fbbd167e47b159b86e4b760171e170, PROOF in run20261023T143952Z-account03-A097-cross-route-transfer. The registered statement and conclusions hold. A displayed derivative in the proof needs the factor t described below; no source file is modified.

Fix vacuum1-t, 0<a=p(A)<t and 0<b=q0(A)<ell<t. Retain the full q0 conditionals on A and its nonempty complement, including their ghosts. At mass z in[ell,t), direct cancellation of full atomwise CE gives

    F(z)=a log2(b/z)+(t-a)log2((t-b)/(t-z)).

The correct derivative is

    F'(z)=t(z-a)/[z(t-z) ln2].

The source omits the positive factor t. The sign, unique minimizer z*=max(a,ell), exact minimum, binary-KL difference and constant upper bound are unchanged. The source derivative is not reproduced as correct. All denominators are positive on the stated domain. Since a>0 and t-a>0, endpoints0 and t have divergent cost when approached; the feasible interior minimizer is unique. Finite CE makes the within-cell cancellation valid even with ghosts: their true weights are zero but they retain their share of each conditional profile. The derivative sign supplies the continuum proof; a rational grid is only an adversarial finite check.

For disjoint controller and seed parts of identical weights1-beta and beta in P and Q, the controller terms and seed log(beta) terms cancel. Thus the full signed CE change is beta F(z*). At a finite actual frontier, let C=sum rho_h CE(P_h,Q_h), old booked cost U, original capacity B and remaining M=B-C-U. The new cost is exactly C+U+sum rho_h beta_h F_h. Consequently payment from that same original account is equivalent to sum rho_h beta_h F_h<=M. This is an identity of full liabilities, not new capacity from revealing a variable. Negative F releases previously paid mismatch; crediting that release again would violate the identity. If a stricter recipe changes within-cell profiles, its further cost has not been priced by this theorem.

The actual three-bit sign negative only at000 and111 has expansion (1-y1y2-y1y3-y2y3)/2. Both y1 children have four equal squared Walsh coefficients. At their seed target q*=(1/4,5/24,5/24,1/3), current p=(1/4,1/4,1/4,1/4) costs (1/4)log2(27/25)>0. Current q0=(1/4,5/16,5/16,1/8) costs (1/4)log2(27/32)<0. The two numbers concern different already-paid current references, so their different signs are consistent. A disjoint seed of weight3/8 scales each by3/8. Complete frontier checks include reaches1/2,1/4,1/4, beta0, nonzero old booking and three remaining margins.

## Scope, rung and next unpaid line

Rung: analytic proof reconstruction plus exact finite validation. A096 holds unchanged. A097's statement holds with the derivative erratum above. Lean admission returned SETUP_UNVERIFIED due compute pressure and started no compiler; no Lean certification is claimed. These are reviews of existing source versions, not new broad candidates.

First unsupported universal line: exploit Booleanity to construct a well-founded influence-priced original-source/payment mechanism or a selected physical descent whose genuine child reserves pay its full initial and terminal liability. A further strict floor is useful only after specifying a necessary compatible policy. Ghost presence, optional resets, supplied capacity and a renamed CE<=K I target do not supply that mechanism.
