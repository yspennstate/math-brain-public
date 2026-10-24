# P0297: sharp-boundary proof attempt

Author: w522. Date: 2026-10-10. Original problem unresolved by this packet; w524 independently kept C1 and L1-L4.

## Exact target and source

For every fixed gamma in (0,2), determine d_gamma = dim_H(C,D_h), almost surely, where h is a whole-plane GFF with its additive constant fixed and D_h is the gamma-LQG metric. The metric is unique up to deterministic positive scale. Fixed-gamma almost-sure statements do not by themselves give a simultaneous statement for all gamma.

Precise primary source: Gwynne--Miller, *Existence and uniqueness of the Liouville quantum gravity metric for gamma in (0,2)*, arXiv:1905.00383, Problem 7.1; https://arxiv.org/abs/1905.00383 . The original survey cited by P0297 is Rhodes--Vargas, *Two Decades of Probabilistic Approach to Liouville Conformal Field Theory*, arXiv:2509.21053, Section 3, PDF page 4; it asks the distance-dimension question for a GFF-based surface using the formal notation e^(gamma X_g)g. The whole-plane formulation above is the canonical P0297 statement. The question does not prescribe Watabiki's expression. Gamma=0 and gamma=2 require separate formulations. Current openness on 2026-10-10 remains UNKNOWN beyond the targeted archive and primary evidence. Bhatia--Gwynne--Harper, arXiv:2606.10496 (2026-06-09), Section 2.3, still describes the general precise value as unknown; that is the latest primary status statement checked here, not an exhaustive current-status certificate.

The related primary source is Gwynne--Pfeffer, *KPZ formulas for the Liouville quantum gravity metric*, arXiv:1905.11790v3, Theorems 1.4--1.5 and Corollary 1.7; https://arxiv.org/abs/1905.11790 . The notation is Q=2/gamma+gamma/2 and xi=gamma/d_gamma. The independent-set KPZ relation requires a deterministic Borel set, or a random Borel set independent of h. GFF thick sets require the dedicated thick-point result, not the independent-set theorem.

## Prior-attempt digest checkpoint

The dated intake ranking records tier 5 and unsolved, without an exact formula or proof. Team O's row 559 names P0297 with no claimant or kept bundle. Targeted filename/ID and title-based searches in the named H and I attempt directories and the Lean campaign found no P0297 proof artifact. These negative searches are not proof that no owner result exists.

The D intake contains the same mathematical question under D0049 and D0052, dedup_key `lqg_hausdorff_dimension_d_gamma`. They are related prior records, not a newly certified database alias. D0049-A001 (attempts.jsonl line 43) describes the normalization/time-constant obstruction, but contains the incorrect identity `d_gamma = 2Q/xi` in key_identity and `d_gamma = 2 Q / xi` in method. D0052-A001 (line 46) uses a quoted dimension window at gamma=sqrt(2) to reject affine interpolation, and explicitly does not claim a solution. Neither attempt lists an independent check. The narrow normalization error is corrected by C1 below; other statements in these archived records have not been promoted or certified by this packet.

The exact population-store P0297 attempt node was read using SQLite mode=ro and saved to EXISTING_P0297_CARDS.json. It correctly records xi*d=gamma, says it cannot calculate xi, and is marked unverified. Our lane analyzes the KPZ sharp optimization and quadratic critical boundary layer. The original target node is likewise unverified and unsolved in its dated metadata. These are source/status records, not independent proofs.

The specifically requested scar `perceptron_proof_open_gaps_fleet_2026_07_12` was read from its memory file, together with the matching MISTAKES.md line. Its relevant lesson is that passing computations and source checks cannot clear the hardest mathematical gap. No conditional row probabilities will be multiplied in this attempt.

## Route being stress-tested

Suppose one tries to determine the whole-space metric dimension by maximizing the thick-point expression

F_gamma,xi(alpha) = (2-alpha^2/2)/(xi*(Q-alpha)).

The expression already contains the metric normalization exponent xi. We examine whether optimization removes this unknown, and whether passing to the critical endpoint is uniform. The following results are deterministic algebraic lemmas. They do not construct additional LQG metrics.

## C1: concrete repair to the prior attempt's normalization

Assume 0<gamma<2, D>0, xi=gamma/D, and Q=2/gamma+gamma/2. Then

2*Q/xi = (1+4/gamma^2)*D > D,
whereas gamma/xi = D.

Consequently the archived identity D=2*Q/xi is inconsistent with the primary source's definitions for every parameter in this range. At gamma=sqrt(8/3) and D=4, it predicts 10 instead of 4.

Proof. Substitute xi=gamma/D. Then 2*Q/xi=2*(2/gamma+gamma/2)*D/gamma=(4/gamma^2+1)*D. Positivity of D and gamma gives the strict inequality. For the known anchor gamma^2=8/3, the multiplier is 5/2, so the value is 10. The corrected relation is the direct rearrangement of the primary source's equation xi=gamma/d_gamma (Gwynne--Pfeffer equation (1.5), and Gwynne--Miller Problem 7.1).

This is a source-backed statement correction with an author proof. It does not evaluate the unknown exponent. The proposed unified diff changes only the two erroneous identity strings and adds correction provenance; no live archive is changed by w522.

## L1: exact sharp maximum and deficit

Assume 0<gamma<2, xi>0, and -2<=alpha<=2. Then Q-alpha>0 and

gamma/xi - F_gamma,xi(alpha) = (alpha-gamma)^2/(2*xi*(Q-alpha)).

Consequently max_{alpha in [-2,2]} F_gamma,xi(alpha)=gamma/xi, uniquely attained at alpha=gamma. The same maximum is attained on the open interval (-2,2).

Proof. Q-2=(2-gamma)^2/(2*gamma)>0, so multiplication by the denominator preserves order. Multiply the claimed identity by xi*(Q-alpha). Its left side is gamma*(Q-alpha)-(2-alpha^2/2). Since gamma*Q=2+gamma^2/2, this equals (alpha-gamma)^2/2. The deficit is nonnegative, and vanishes exactly at alpha=gamma, which lies in (-2,2). This proves the formula, the sharp maximum, and uniqueness.

This is an proved deterministic special case, independently kept by w524. It contains no numerical approximation and assumes no independence.

## L2: critical boundary layer and every possible endpoint limit

Under the same algebraic assumptions, put delta=2-gamma and beta=2-alpha. Then

xi*F_gamma,xi(alpha) = (2*beta-beta^2/2)/(beta+delta^2/(2*gamma)).

For gamma approaching 2 from below and alpha approaching 2 from below, if beta/delta^2 tends to k in [0,infinity], the normalized expression tends to

8*k/(4*k+1) for finite k, and 2 for k=infinity.

Its possible joint limits are exactly [0,2]. Thus the expression has no unique continuous extension at (gamma,alpha)=(2,2), even after multiplying by xi.

Proof. Substitute Q-alpha=(Q-2)+beta=delta^2/(2*gamma)+beta and 2-alpha^2/2=2*beta-beta^2/2. For finite k divide numerator and denominator by delta^2, using gamma -> 2; for k=infinity divide by beta. By L1, 0<=xi*F<=gamma<2, so no other finite joint-limit values are possible. Every value in (0,2) is realized by beta=k*delta^2 with k>0. The value 0 is realized by beta=delta^3; the value 2 by beta=delta (indeed alpha=gamma). All these paths stay in the subcritical/open-alpha domain for sufficiently small delta.

For the algebraic endpoint alpha=2, F=0 for every gamma<2. If gamma is first set equal to 2 and alpha<2, cancellation gives xi*F=(2+alpha)/2, which tends to 2 as alpha -> 2. These endpoint evaluations illustrate the same noncommuting limits; they are not applications of a subcritical metric theorem at gamma=2.

This is an proved deterministic special case, independently kept by w524. The sharp scale is (2-gamma)^2, rather than (2-gamma).

## L3: all independent-set KPZ dimensions still leave the absolute scale free

For 0<=x<=2 define

A_x=sqrt(Q^2-2*x), alpha_x=Q-A_x, and T_gamma,xi(x)=alpha_x/xi.

Here 0<=alpha_x<=gamma<2. For x>0 the maximum, over -2<=alpha<=2, of

max{x-alpha^2/2,0}/(xi*(Q-alpha))

is uniquely T_gamma,xi(x), at alpha=alpha_x. At x=0 the expression is identically zero, so uniqueness is false. In the region x-alpha^2/2>=0, the exact deficit is

T_gamma,xi(x) - (x-alpha^2/2)/(xi*(Q-alpha))
  = (alpha-alpha_x)^2/(2*xi*(Q-alpha)).

Proof. The function a -> Q*a-a^2/2 is strictly increasing on [0,gamma], and takes values 0 and 2 at the endpoints. This gives the asserted range and x=Q*alpha_x-alpha_x^2/2. Substitute this last identity into the numerator of the deficit and complete the square. In the region with negative unclipped numerator the clipped expression is zero, strictly below the positive maximum for x>0. At alpha_x the unclipped numerator equals alpha_x*(Q-alpha_x)>0 for x>0. At x=0 every clipped numerator is zero.

For any positive number D put xi=gamma/D. Then

T_gamma,xi(x)/D = (Q-sqrt(Q^2-2*x))/gamma

is independent of D. Also x=xi*Q*T-xi^2*T^2/2 and T(2)=D hold for every D. Thus even the full algebraic independent-set KPZ spectrum does not identify D. This is a counterexample to that numerical inference, not a construction of multiple LQG metrics.

The known Brownian anchor and the limit D -> 2 as gamma -> 0 do not fix the deficiency. For example, the two purely numerical functions

D_A(gamma)=2+gamma/sqrt(6)+gamma^2/2,
D_B(gamma)=D_A(gamma)+gamma^2*(gamma^2-8/3)^2/100

are distinct, smooth, greater than 2 on (0,2), have limit 2 at zero, and both equal 4 at gamma=sqrt(8/3). Defining xi_i=gamma/D_i and T_i by the displayed formula makes each satisfy every algebraic KPZ equation and the thick-point maxima above. At gamma=1 their D values differ by exactly 1/36. These are chosen solely as explicit algebraic witnesses. No claim is made that either function satisfies all known LQG bounds or arises from a metric, and no novelty is claimed for the chosen expressions.

The source's Corollary 1.7 already proves that gamma-thick points have full metric dimension. We do not infer this by taking the dimension of an uncountable union. The source's statements are for each fixed parameter; this packet does not take an uncountable intersection of probability-one events or assume a common coupling across gamma.

## L4: sharp uniform inverse stability is square-root, not Lipschitz

Let Y_gamma(x)=xi*T_gamma,xi(x)=Q-sqrt(Q^2-2*x) on [0,2] and q_gamma=Q-gamma=(4-gamma^2)/(2*gamma)>0. Its optimal Lipschitz constant for fixed gamma is 1/q_gamma, which tends to infinity as gamma -> 2. Nevertheless, for every x,y in [0,2],

|Y_gamma(x)-Y_gamma(y)| <= sqrt(2*|x-y|),

uniformly over 0<gamma<2. The constant sqrt(2) and exponent 1/2 are sharp for this uniform family.

Proof. Differentiating gives Y'(x)=1/sqrt(Q^2-2*x), increasing to 1/q_gamma at x=2; endpoint difference quotients give optimality. The square-root inequality |sqrt(a)-sqrt(b)|<=sqrt(|a-b|) for a,b>=0 gives the uniform bound. More explicitly, for 0<=epsilon<=2,

gamma-Y_gamma(2-epsilon) = sqrt(q_gamma^2+2*epsilon)-q_gamma
  = 2*epsilon/(sqrt(q_gamma^2+2*epsilon)+q_gamma).

At fixed epsilon>0, sending gamma -> 2 makes the first expression tend to sqrt(2*epsilon), so the uniform constant cannot be smaller. A uniform bound with exponent p>1/2 would, after that limit, require sqrt(2*epsilon)<=C*epsilon^p for all small epsilon, which is impossible. This also rules out a uniform Lipschitz bound. The argument is solely for the numerical inverse map, not for a critical LQG metric theorem.

## Consequence and the single hardest remaining gap

Optimizing this expression yields gamma/xi. After substituting xi=gamma/d_gamma, it yields d_gamma itself. This is self-consistency, not an equation that evaluates the unknown exponent. Passing to gamma=2 does not supply the missing equation, because L2 gives a full interval of endpoint limits.

The single hardest missing piece is an independent evaluation of the actual LFPP distance-normalization exponent Q_LFPP(xi), equivalently an estimate of normalized metric crossing distances strong enough to determine xi from Q_LFPP(xi)=2/gamma+gamma/2. No estimate in this packet does that. This is the gap in the original-target attempt; L1 and L2 themselves have complete algebraic proofs.

NEXT: Run the bounded exact-arithmetic and endpoint measurements, complete source/archive records, and send the finished packet to w524.

Closeout: the canonical-repository lookup did not locate a current P0297 card or primary live-store path; discovered audit snapshots were not opened. Current owner-retirement status is unconfirmed. Both named peer deliveries failed due to unregistered recipients and are preserved as file handoffs. The bundle remains concept/draft material. On resumption, five claim-specific independent KEEP verdicts from w524 were recovered and saved in referee/w524_verdicts.jsonl. No formal receipt, ingestion or retrieval is certified.
