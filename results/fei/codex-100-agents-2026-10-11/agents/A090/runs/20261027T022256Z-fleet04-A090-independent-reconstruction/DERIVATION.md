# Independent reconstruction of the exact flexible-floor price

Verdict: A004-EXACT-FLEXIBLE-FLOOR-SIGNED-PRICE@1 HOLDS at its stated supplied-source scope, without a repair. Full FEI remains OPEN.

The reconstruction in RECONSTRUCTION_BEFORE_SOURCE.md was saved before opening the producer's DERIVATION.md. Neither producer checker was read or imported. The original statement is used unchanged; the independent checker uses monotone active-set growth, a separate exhaustive active-set enumerator, and exact certificates of the tangent inequality at every vertex of the feasible simplex.

## 1. Quantifiers and admissible references

Let P be any probability on a finite label set with empty label 0, and put a=1-P(0)>0. Let R be a covering finite-cross-entropy subprobability, of mass s in (0,1], and tail mass w=s-R(0)>0. Set pi_j=P(j)/a and M_j=R(j)/w for j nonempty. Thus pi and M are probabilities and M is positive wherever pi is positive. Fix any probability T on ALL nonempty labels and any real c in (0,1). A permitted replacement changes only M to a probability x satisfying x_j>=c T_j. It preserves the actual empty-label reference R(0), tail mass w, and total mass s. Information is in bits. These hypotheses describe a supplied reference; they do not price its initial construction by influence.

## 2. Existence, uniqueness, and all zero cases

Write l_j=c T_j and F(k)=sum_j max(l_j,k pi_j). F is continuous, F(0)=c<1, and F(k)>=k. Therefore some positive k has F(k)=1. At any k1 with F(k1)>c, at least one summand strictly exceeds its floor, and that summand increases strictly for every k2>k1. Consequently the root at level 1 is unique. The inequalities F(k)<=c+k and F(k)>=k give 1-c<=k<=1.

Define x*_j=max(l_j,k pi_j). For pi_j>0, x*_j>0. For a ghost pi_j=0, x*_j=l_j, which may be zero if also T_j=0. No expression divides by such a zero: define g_j=pi_j/x*_j on positive true support, and g_j=0 on ghosts. At a free coordinate x*_j>l_j, g_j=1/k. At every floor coordinate g_j<=1/k. For any feasible y, its displacement on a floor coordinate is y_j-x*_j=y_j-l_j>=0. Mass conservation now gives the exact finite identity and inequality

    sum_j g_j(y_j-x*_j)
      = sum_floor (g_j-1/k)(y_j-l_j) <= 0.                 (A)

This identity includes ghost floors. If y is zero at a true-positive atom, CE(y) is infinite, so it cannot improve the finite value at x*. Otherwise apply ln u<=u-1 with u=y_j/x*_j only on positive true support. The scalar inequality is strict except at 1: u-1-ln(u) decreases on (0,1), increases on (1,infinity), and equals zero at 1, since its derivative is 1-1/u. It follows that

    D_2(pi||y)-D_2(pi||x*)
      = -sum_{pi_j>0} pi_j ln(y_j/x*_j)/ln2
      >= -sum_j g_j(y_j-x*_j)/ln2 >= 0.                  (B)

Equality in (B) requires y_j=x*_j on every positive true atom by strictness of ln u<=u-1 away from u=1. All ghosts in x* already equal their floors. Their displacements in y are nonnegative and sum to zero after equality on true support, so they too agree atom by atom. The minimizer is unique even when targets or true atoms vanish or a coordinate ties exactly at its floor.

The source theorem excludes a=0, w=0, c=0, and c=1. The limits are consistent but require separate statements: a=0 makes every tail change free; c=0 permits x=pi; c=1 forces x=T, possibly with infinite CE. No excluded boundary is used in the proof.

## 3. Exact signed full cost

For any admissible finite-cost x, the complete reference is R_x(0)=R(0), R_x(j)=w x_j. Subtract its full cross entropy from the old full cross entropy directly. Empty-label and tail-mass terms cancel because they are identical, giving

    CE(P,R_x)-CE(P,R)
      = a sum_{pi_j>0} pi_j log2(M_j/x_j)
      = a[D_2(pi||x)-D_2(pi||M)].                        (C)

The subprobability mass penalty is present in both terms before subtraction. It is not discarded or renewed. In particular the minimum signed price is obtained by x=x*. It can be positive, zero, or negative. The previous A090 free corridor pi>=cT is recovered by x*=pi, with exact price -a D_2(pi||M).

The bound x*>=k pi>=(1-c)pi also gives D_2(pi||x*)<=log2(1/(1-c)). This is a bound on a supplied-reference reset, not a universal sum over histories. Its all-parameter endpoint is sharp on disjoint true and target supports, where x*=(1-c)pi+cT. No such sum or unpaid policy is imported into the acceptance verdict.

## 4. Both policy classes on an actual Boolean source

Take the two-bit sign f=(1,-1,-1,-1). Its four direct character sums are (-2,2,2,2), hence its squared Fourier law is (1/4,1/4,1/4,1/4). Use the full supplied reference R=(1/4,3/16,15/32,3/32). Thus a=w=3/4, pi=(1/3,1/3,1/3), M=(1/4,5/8,1/8). The target floor is x_1>=1/2, with c=1/2 and T=(1,0,0).

The flexible solution is x*=(1/2,1/4,1/4), k=3/4. Since every full true tail atom has weight 1/4, its signed full price is (1/4)log2(product_j M_j/x*_j)=(1/4)log2(5/8)<0. Both the exact rational product and its sign are certified without evaluating a floating logarithm.

If the additional policy requires preserving the ratio 5:1 between labels 2 and 3, write x=(z,5(1-z)/6,(1-z)/6), z>=1/2. Differentiating the true conditional objective gives a positive multiple of z-1/3, so its minimum on this interval is at z=1/2. The optimizer is (1/2,5/12,1/12), and product_j M_j/x_j=9/8. Its full price is (1/4)log2(9/8)>0. The extra compatibility condition therefore costs (1/4)log2(9/5)>0. This verifies the stated sign reversal while holding the Boolean function, incoming reference, empty atom, tail mass, and required floor fixed. It does not establish which class any useful FEI policy permits.

## 5. Same original owner

At a finite stopping frontier let rho_v be actual physical reach, C=sum_v rho_v CE(P_v,R_v) the full CURRENT terminal cost, U all previously booked costs, and B the original capacity. References, old bills, reaches, and every complementary terminal are retained. Applying (C) at those terminals changes the remaining original capacity from B-U-C to

    B-U-C-sum_v rho_v Delta*_v.                         (D)

For a disjoint actual sector with full weight beta_v, its local conditional price is multiplied by beta_v exactly once. Equation (D) is a finite sum and contains both outcomes; it needs no independence assumption or limit interchange. Payment is equivalent to sum_v rho_v Delta*_v<=B-U-C. It neither creates a fresh bank nor substitutes a child's hypothetical influence budget for the actual current margin. A prior negative price may not be booked again as if still unspent.

## 6. Executed checks and their limits

The final v2 pilot passed 1,615 assertions on 22 Boolean tables and 94 projection cases in 0.060 seconds. The final v2 main run passed 28,957 assertions on all 278 Boolean tables through three variables, 1,483 projection cases, and 480 ghost-target cases in 1.300 seconds. For all 675 pairs of nonempty uniform-support laws on four labels and c in {1/4,1/2,3/4}, a second exhaustive active-set implementation gives the same unique profile. Exact tangent inequalities are certified at all vertices cT+(1-c)e_j, which proves the linear certificate over the entire feasible simplex for each tested input. Direct character sums and a separate Walsh transform agree; physical and spectral influences agree. Two incoming mixture weights and two subprobability masses test the atomwise full-CE ratio cancellation. These finite checks support the analytic proof; they do not establish the all-dimensional FEI conjecture.

The first full v1 run failed at assertion 9,939: empty Python sums allowed int/int division and produced a floating k. This was a checker defect, not a mathematical counterexample. FIRST_RUN_FAILURE.json records it. The v2 helper forces rational division and asserts Fraction types for every optimizer scalar; both pilot and main were rerun. The initial pilot is not retained as exact evidence.

A separate full-frontier implementation passed 16,297 exact assertions across 804 actual physical edges and 2,412 two-child frontiers in 1.178 seconds. Each actual child spectrum is reconstructed directly from its truth table. Incoming references are actual spectral marginals of a supplied positive root reference. The optimizer is obtained by exhaustive active masks, not by importing the main optimizer. Every full CE and its signed change is represented as a rational linear combination of logarithms of primes; exact identities (C) and (D) are then checked coefficient by coefficient. One-child transactions retain the literal full reference on the sibling. Both-child transactions retain both terminal contributions. Arbitrary old-debit log coefficients persist on both sides. The test does not price its supplied root by influence.

The bounded Lean attempt for the finite active-floor tangent step received memok exit 0, but timed out at 45.398 seconds with no compiler verdict. FORMAL.json and the helper receipt pin the submitted source, compiler, and declared Mathlib revision. Status is RUNTIME_UNVERIFIED, with target identity, theorem kind and axioms unverified. No Lean-checked claim is made. The submitted lemma covers positive reference atoms and the linear tangent step only; even a future pass would not certify logarithmic strictness, the complete optimization theorem, or prose fidelity automatically.

A090 authored the earlier free-corridor special case credited by A004. This stage supplies no repair to the new general theorem and reconstructs it before opening the producer proof; the prior related contribution is nevertheless disclosed. The stage is a scoped reconstruction, not an assertion of a second disinterested full-chain acceptance.

## 7. First unreconstructed implication

The supplied-source optimization theorem has no remaining unsupported implication at its named scope. The first unpaid universal line is: for every Boolean core, choose a required useful policy with an explicitly specified permissible reference class and provide an ORIGINAL complete reference plus its necessary reached repairs, all old bills, and both full terminal costs at one common influence price K I(f). Neither free profile flexibility nor a source-equal choice is an accepted universal supplier. A cheap initial complete reference by itself would imply FEI by Gibbs, and choosing the exact true spectrum as reference would require paying its still-unbounded entropy. This reconstruction changes a local candidate from pending review to independently reconstructed; it does not close that universal line.
