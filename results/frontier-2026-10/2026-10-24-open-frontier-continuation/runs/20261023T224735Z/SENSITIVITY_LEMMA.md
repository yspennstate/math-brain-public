# Generic switching for finitely many irreversible diagonal losses

**PROVED (internal), independently audited in reviews/d04_sensitivity_review.md and used in the independently audited full k-input theorem.** The point of this lemma is to pay the later-switch genericity gap. A first-stage exponential calculation alone does not do so.

Fix k<infinity, a symmetric positive-definite C, a positive diagonal vector P, and a fixed initial sign orthant O. All environmental coefficients remain fixed while the initial residual b varies in O. Initially J(0)=0 and every population is alive. In a phase with alive set S, define Q_S=C+diag(P_j 1{j in S}) and

J'=b-Q_S J, r=J'.

Delete an alive coordinate j permanently at its first positive return J_j=0 after initially moving in sign(b_j). On a history of isolated transverse returns this prescription is unambiguous. The lemma shows that initial b for which the prescription first becomes ambiguous through a grazing or simultaneous return form a Lebesgue-null set. Thus at most k distinct transverse deletions define a unique global piecewise-exponential residual for almost every b in O.

## Conservation law and event derivative

Equivalently write r'=-Q_S r, J'=r, r(0)=b. On every phase r+Q_S J is constant. At deletion j, Q changes to Q-P_j e_j e_j^T, and J_j=0, so Q_after J=Q_before J. Consequently

r(t)+Q_S J(t)=b

holds globally through every regular history. The vector field for J is continuous at a deletion: its change there is P_j e_j J_j=0. Although the derivative r' can jump, J itself is continuously differentiable.

Fix an open parameter chart in which a specified finite sequence of earlier deletions has occurred at distinct transverse times. Implicit-function differentiation of each event equation makes those times smooth (indeed analytic) functions of b locally. For t after that history and before any new deletion, J(t;b) is smooth in (t,b). At a past event tau(b), differentiate the composition of the two flow maps: the term involving d tau/db is multiplied by the difference of the pre-event and post-event vector fields. That difference vanishes on the event surface. Hence the fixed-time sensitivity

Z(t)=D_b J(t;b)

is continuous across the event and satisfies

Z'=I-Q_S(t) Z, Z(0)=0.

These statements also hold for the smooth continuation with the current matrix held fixed beyond the next candidate event, which is the function used in the zero-set argument below. No differentiability through an already-grazing past event is assumed.

## An energy argument makes Z invertible

For a fixed nonzero vector v, put z=Zv. Then z'=v-Q_S z and z(0)=0. Consider

E(t)=one_half z(t)^T Q_S(t) z(t)-v^T z(t).

Between deletions Q_S is constant, so

E'=(Q_S z-v)^T z'=-||z'||^2.

At deletion j, z is continuous and

E(t+)-E(t-)=-one_half P_j z_j(t)^2<=0.

There is a positive interval before the first deletion because every b_j is nonzero. Since z'(0)=v, E becomes strictly negative on that interval and remains strictly negative for all later t>0. If Z(t)v=0, then E(t)=0, a contradiction. Thus Z(t) is nonsingular for every positive t on every regular-history chart and its constant-phase continuation. This conclusion uses the downward positive-semidefinite changes in Q; it is not a claim about arbitrary time-dependent positive-definite coefficient paths.

## Null grazing and simultaneous sets on a regular-history chart

Let j be an alive coordinate and define F_j(t,b)=J_j(t;b) on a smooth continuation chart with t after the last past event. Its parameter derivative is e_j^T Z(t), which is nonzero. The zero set M_j={F_j=0} is therefore a smooth k-dimensional manifold in the (k+1)-dimensional (t,b) space. Project it to b.

The differential of this projection has full rank precisely when partial_t F_j=r_j is nonzero. Indeed tangent vectors satisfy F_t delta t+F_b delta b=0. If F_t is nonzero, every delta b can be lifted by choosing delta t; if F_t=0, the image is confined to the proper hyperplane F_b delta b=0. Therefore grazing parameters are critical values of the smooth projection M_j -> R^k. Sard's theorem makes their set Lebesgue-null. Smoothness is more than sufficient for Sard's regularity requirement; one is not taking an uncountable union of fixed-time null sets without justification.

For two distinct alive coordinates j,l, the parameter gradients e_j^T Z and e_l^T Z are independent. Thus {J_j=J_l=0} is a smooth submanifold of dimension k-1 in (t,b) space. Its projection to b has Lebesgue measure zero by countable local charts and the fact that locally Lipschitz images from dimension k-1 into k have zero k-dimensional volume.

The actual next-event bad set is a subset of these continuation bad sets: one simply restricts to times at which neither coordinate had previously been deleted and no earlier new event occurred. Removing that restriction for the null-set bound does not alter the dynamics being asserted.

## Countable charts and induction

On each compact time interval, initial residuals with a specified already-regular finite history admit local smooth charts: old event derivatives remain nonzero, event gaps remain positive, and surviving signed cumulative coordinates have positive minima away from the event neighborhoods and time zero. The parameter-time domain is second countable, so these local charts can be reduced to a countable cover. Restricting unbounded times and parameters to a countable exhaustion causes no measure issue.

At the initial stage there is no earlier history and the sensitivity argument applies directly. Discard the null sets of grazing and simultaneous first events. If a first event exists, it is unique and transverse. Repeat the chart argument on the regular one-event domains to discard null sets for the second event, and so on. There are only finitely many ordered deletion histories (each coordinate can be deleted once), and at most k deletion stages. A finite union of countable unions of null sets remains null. A remaining trajectory with no next finite return simply continues under its fixed matrix forever. At an actual first return from a strictly positive signed clock, the derivative has the negative signed direction; hence the event is an absorbing crossing, not an arbitrary zero selection.

For b outside the resulting null set, this constructs a unique complete history with at most k transverse, nonsimultaneous deletions. On every finite horizon the matrices remain bounded and the residual is continuous. Since Q_S>=C, ||r(t)||<=exp[-lambda_min(C)t]||b||. This is decay of the limiting hybrid system; it does not interchange width and infinite-time limits.

## Random sign-selected environments and remaining network step

Suppose the initialized output F is independent of an environment E=(C,N), has a full-dimensional density, and P_j=P_j(sigma,E) is fixed once sigma=sign(y-F) is fixed. Condition on E and partition into the finitely many sign orthants. In each orthant b=y-F has a density and the preceding deterministic result applies to its fixed coefficients. Thus almost surely every hybrid deletion is regular, even though the selected Q is not unconditionally independent of b.

To obtain a neural-network theorem one still needs the actual joint stable initialization and a convergence proof through a finite regular sequence of deletion events. The finite-ray initialization and the localized/compactness gate argument are supplied in agents/d01_k_input_extension.md. This sensitivity lemma by itself is a deterministic genericity result; it does not apply to nonorthogonal-input projected dynamics, gates that reactivate, or arbitrary deep networks.

Primary source for the standard critical-value theorem: Arthur Sard, The measure of the critical values of differentiable maps, Bull. Amer. Math. Soc. 48 (1942), 883–890, https://webhomes.maths.ed.ac.uk/~v1ranick/papers/sard.pdf .
