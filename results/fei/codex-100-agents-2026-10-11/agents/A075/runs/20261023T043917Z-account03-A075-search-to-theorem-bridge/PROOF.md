# Inherited credit at third-core admission

Full FEI remains OPEN. This is an exact finite-family continuation theorem and a generic real-credit transfer lemma. No all-dimensional Boolean theorem is inferred from the finite domain.

## 1. Family and retained owners

Use uniform physical bits and base-2 Fourier entropy. Let g be -1 exactly on {0,1,2} in six bits. Let h be -1 on {0,1,2,4,8,16,32,6,17,40}, and J(x)=-h(x xor1). The full retained function is Fplus=J(-1,+1,g,g,g,g). Put S=4I-H and A=-S(Fplus)>0. The original donor, its already spent outgoing subsidy and booked balance, all earlier stopped full terminals and parked2tau are retained unchanged. Only the supplied credit on this retained Fplus account is allocated below. Credit is nonnegative and mean-conserved; debit labels may be signed, but their total is nonnegative.

There are twelve literal inner profiles after deletion of pointwise dummy bits: P=constant+1; A_m=-1 only at0 for0<=m<=5; and L_m=-1 on {0,1,2} for2<=m<=6. A_0 is constant-1. An A_m query has children A_(m-1),P. A special-coordinate L_m query has children A_(m-2),A_(m-1), with the pair child's dummy deleted. A padding-coordinate L_m query has children L_(m-1),P. All729 labelled restrictions and1458 physical query rows are verified. Deleting a dummy does not query it, alter reach, or remove any full other-core function.

## 2. Spectra and finite Bellman hull

For fixed inner means mu_j and variances v_j, let q_j be the true pivotal probability of the outer gate over the OTHER inner signs. Occupied-set masses are

    P_T=prod_(j in T)v_j * [sum_(U containing T) Jhat(U) prod_(j in U\T)mu_j]^2.

Orthogonality and Shannon's finite chain rule give

    I(F)=sum q_j I(core_j),
    H(F)=H(P)+sum q_j[H(core_j)-h2(v_j)].

For a constant core, its occupied masks have mass0 and its H,I contributions vanish. It does not cause the remaining full entropy to vanish. Here fixing the first two outer signs reduces the outer table to sixteen entries K(z)=-h(z<<2). The source profile engine uses a multilinear centered transform and separately checks direct centered moments. The independent reviewer reconstructs the same masses by direct Walsh-subset sums from this sixteen-entry Boolean table and checks exact prime-log S identities.

For any allowed finite restriction DAG, define

    rho(s)=max(0,-S(s), max_query mean_b rho(child(s,b))).       (1)

This is the least nonnegative superharmonic majorant of (-S)_+. Backward induction proves it equals the largest expected (-S(terminal))_+ among all allowed adaptive stopping policies: either stop now or take one legal query and then optimize each child separately. This is finite dynamic programming, not a product of conditional estimates.

Given incoming a>=rho(s), allocate

    a_b=rho(child_b)+a-mean rho(children),
    d_b=S(child_b)+a_b.                                       (2)

Credits and net debits are nonnegative, mean a_b=a, and mean d_b=D+e, where D=S(s)+a and e=mean S(child)-S(s) is the SIGNED full query excess. For positive T=D+e, multiply each signed ancestor/new debit label by d_b/T. This preserves each label's conditional mean and their sum. If T=0, nonnegative outgoing debits both vanish; kernel1 preserves the signed labels whose sum is zero. If a>0, allocate each nonnegative credit-owner label using a_b/a; if a=0 all outgoing credits are zero, with no division. Thus old owners are conserved separately and no new donor flow appears.

Necessity follows without assuming arbitrary FEI: any feasible nonnegative credit process must dominate (-S)_+ at stopping, so its initial value must cover every stopping expectation. Hence (1) is sharp for this supplied-credit model. It does not establish that universal root credit is influence-paid.

## 3. Generic exact prefix-to-envelope transfer lemma

Let rho_old be a verified old envelope, and let its prescribed allocator be (2). Let the root credit be a0+D, with D any real>=0. For each reachable old state s, define a_min(s) as the least actual incoming credit over all old-policy paths at D=0. Finite acyclicity makes this a minimum, attained by a path. It is computed forward, taking minima over parents and the old allocator's TRUE child credit. Different histories reaching the same physical profile are not assumed to have the same credit.

Every child allocation is affine in incoming a with slope1. Inductively, adding D to the initial credit adds D to every descendant path's credit. Consequently the least credit at state s is EXACTLY a_min(s)+D. Given a proposed new envelope rho_new at a switch, the sharp extra initial-credit threshold for allowing that switch after EVERY old history is

    B=max_s (rho_new(s)-a_min(s))_+.                          (3)

Sufficiency: D>=B implies every actual incoming credit covers rho_new, so (2) pays any new allowed stopping policy. Necessity: if D<B, a minimizing old path to a maximizing switch state arrives below its sharp new hull; some new stopping policy therefore fails. Such a witness has its actual physical query path and true dyadic reach. The lemma is valid for arbitrary supplied real credit and finite DAGs; it does not assume any independence between different history rows.

This is the all-real parameter in this stage's analytic bridge. It is a credit parameter, NOT a new parameterized Boolean family, and must not be presented as settling the packet's all-dimensional construction goal.

## 4. Exact declared application and symmetry

For each triple of distinct remaining physical core indices, allow every adaptive physical query/stopping policy within those three cores after admission. Its full hull has12^3=1728 states. The outer Boolean table is invariant under literal swaps2<->4 and3<->5, checked on all16 inputs. Since the four inner cores start identically, these physical block permutations preserve full spectra, query labels, allocations and credits; no averaging of a basepoint-dependent section is used. Two representatives, triples(2,3,4) and(2,3,5), cover all four possible triples.

For each representative and each of its three source pairs, compute the OLD EXACT TWO-CORE hull (not the triple hull) and propagate actual minimum incoming source credit over all two-core histories from a0=A. At every one of144 pair states compare the full triple hull with that carried credit. The six representative source-pair/triple combinations give864 cuts. Literal outer symmetry covers the twelve labelled pair-plus-third choices.

The saved exact certificates determine whether B in (3) is zero or positive for each of these six cases. The final REPORT and TRIPLE files state the actual result. Root equality alone is insufficient: every source-prefix cut is checked, and the inherited source allocation is never retrospectively replaced by a new root optimum. An original debit D>=0 simply shifts every true carried credit by D, as proved in section3.

The source policy here is A084's exact-pair-hull allocator with a fixed admitted pair before the switch. This stage does not identify it with A089's differently rounded or adaptive pre-choice allocator, and does not silently certify every previously saved financial account. After a switch, all three admitted cores may be queried in any adaptive order; the fourth stays unqueried. An observation-dependent choice of third core is covered because each legal choice passes its own cut comparison.

Executed result: both root hulls equal A EXACTLY and all864 fixed-pair source cuts have B=0. An additional frozen phase amendment tests prefixes that first used the one-core allocator before choosing their pair. The independent replay seeds each pair-state credit minimum by all actual one-core prefix arrivals, then propagates pair allocations. Every one of these864 stronger cuts also has B=0. Its saved paths record the single/pair phase, original physical coordinates, answers and true dyadic reaches. Thus one may start with any first core, choose a second after observations using the original one-core credit, and subsequently choose a third after any such pair history. Once the triple is admitted, any adaptive policy within it is paid. No past allocation is replaced. The source phase policy is the specified exact-hull allocator, not every conceivable sufficient prior allocator.

For all real D>=0 already supplied at the root, initial credit A+D and initial total debit D remain sufficient. Equation(3) proves this continuum statement algebraically: D shifts every actual path arrival by D; all six extra thresholds are exactly zero. It is not inferred from a numerical grid. Generic section2 also permits any normalized nonnegative real outcome weights; all zero-weight outcomes are omitted and all means/kernels are interpreted with those weights. The actual physical applications here use halves.

## 5. Independent review and certificate audit

code/independent_review.py imports no peer executable. Its only shared primitive is A075's previously checked rational logarithm enclosure. It reconstructs the432 A084 pair-state instances using its own direct Walsh-subset masses, checks exact prime-log S and hull equality, and repropagates all72 original one-core prefix cuts. The finite real-credit/label proof above is reconstructed independently. A successful result supplies independent acceptance of A084's unchanged scoped theorem; it is not independent reviewer acceptance of this stage's new triple theorem.

The new triple application additionally receives an independent bottom-up replay from saved S profiles, using named literal profile transitions, and explicit original-coordinate replay of every source witness path. Exact comparisons use rational intervals with proved error; floats do not decide any sign or equality. Raw check counts are execution predicates, not distinct mathematical propositions.

## 6. Exact first unsupported universal line

Even if every declared cut has B=0, no Boolean parameter n or arbitrary remaining-core count has been settled by this finite domain. The next unpaid step is fourth-core admission against the credit ACTUALLY allocated by this three-core policy, preserving all old owners and the original donor's spent flow. More generally, one needs a dimension-independent signed-component superharmonic envelope funded by influence rather than by unknown full entropy. Stating that such an envelope exists, or inserting the already computed full S as a fresh bank, would restate the FEI gap. This run archives the complete bounded domain and makes no absence-of-failures claim beyond its exact certificates. Full FEI remains OPEN.
