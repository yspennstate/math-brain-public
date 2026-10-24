# The remaining payment target concerns nonempty shape

This stage's absorption identity says pure vacuum calibration and coordinate deletion carry no extra repeated-original-source-reset obligation. The following exact local decomposition isolates the first operation genuinely beyond that identity.

Let a queried parent have actual spectrum P, complete normalized reference Q, marginal V=M_j Q, child actual laws P_b, and nonnegative conditional-occupancy KL refund rho. Put p_b=P_b(0). For a selected child b, supply a complete source law S_b of finite CE and use its vacuum calibration C_(p_b)(S_b) as the fresh full child reference. All unselected children keep V. For p_b<1, let A_b be the actual spectrum conditioned on being nonempty, and V_b^+,S_b^+ the normalized nonempty parts of V,S_b. Define the signed transport bill

    T_b=(1-p_b) E_(A_b) log2(V_b^+/S_b^+).

At p_b=1 put T_b=0. Finite-support hypotheses ensure every logged denominator on actual support is positive. Then exactly

    CE(P_b,C_(p_b)(S_b))-CE(P_b,V)
      = T_b-D_Bern(p_b || V(0)).                      (1)

This follows by first calibrating V: its vacuum mass agrees with P_b and its nonempty shape is V_b^+, so the remaining CE difference has no vacuum term. Binary KL pays the first calibration. Terms at unoccupied vacuum atoms use the standard continuous convention; finite CE excludes a zero reference on occupied atoms.

With physical child weights 1/2 and reset subset J,

    Z= (1/2) sum_(b in J) [T_b-D_Bern(p_b||V(0))].   (2)

For a global original quota M0, already booked erasures d, and all complete frontier costs, let U=M0-d-frontier_CE be the CURRENT unused bank before this local query at reach w. The exact full-ledger update is

    U_new=U+w[rho+(1/2)sum_(b in J)D_Bern
                       -(1/2)sum_(b in J)T_b].       (3)

No complementary terminal is discarded. Thus the weakest necessary-and-sufficient local affordability statement, for this fixed query/reset policy and existing original bank, is

    (w/2) sum_(b in J)T_b
       <= U+w rho+(w/2)sum_(b in J)D_Bern.           (4)

Equation (4) is an exact reformulation, not a proved universal construction. The smallest genuinely stronger lemma for the reference-transfer route is a SELECTION/CONSTRUCTION statement guaranteeing (4) for useful nonempty-shape-changing source transports from one admitted original influence bank. Merely assuming a cheap source or bounding each positive reset by edit mass does not prove it. A003's previous stage refutes the latter stronger shortcut.

If each fresh source's nonempty part is proportional to the complete currently inherited law, then T_b=0 exactly and (4) holds for U>=0. Section 1 of DERIVATION.md proves that this proportionality survives every intervening physical marginal when all earlier changes were pure vacuum calibrations of one fixed source. This proves the repeated-return closure with zero new charge. It does not imply that arbitrary Boolean edit floors preserve the nonempty ray.

## Constant-preserving implication diagram

The older route definitions and constants are preserved in IMPLICATIONS_BASELINE.md. The new reference-transport edge is:

    finite source comparison c + supplied occupied floor gamma
        ==> first-reset stopping-frontier payment c+(1-m^2)log2(1/gamma)
        ==[vacuum absorption; zero surcharge]=> arbitrary repeated returns to SAME source
        ==[supplied negative-cell creating/live algebra]=> original rate K=2C0+10,
                                                        K=18 if C0=4,
                                                        reserve >=7e_root.

The last edge remains conditional on its stated source/creating hypotheses. Writing c_*=2/ln(2), the baseline good-coordinate erasure rule B_i<=K Inf_i implies FEI(K+c_*); the all-coordinate C018 bound implies this rule with the same K. The baseline signed-downward rule L_i<=K Inf_i implies FEI(K+3/ln(2)), whereas a physical entropy-deficit rule Delta_i<=C Inf_i implies FEI(C). The baseline posterior witness residual R_*<=K I implies FEI(2+Kref+K), with its explicitly admitted reference family and Kref specified in IMPLICATIONS_BASELINE.md. This stage changes none of those constants. Its contribution to C019/C024 is eliminating the repeated-pure-calibration detour and replacing that proposed gap by the signed, full-ledger nonempty-transport condition (4). The global source admission/selection line remains open for arbitrary Boolean functions.
