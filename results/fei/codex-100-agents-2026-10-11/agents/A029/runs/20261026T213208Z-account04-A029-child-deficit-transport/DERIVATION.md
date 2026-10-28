# Occupancy-calibrated odds floors use the existing child reserve

Units are bits. Full FEI remains OPEN. The statements below are supplied-reference results; they do not supply a cheap initial reference for an arbitrary Boolean core.

## 1. Target and conditions

At a physical restriction of a binary mux F=(1-c)G+cH on independent controller and DATA cubes, write a=1-2c, V=Var(a), gamma=Pr(G!=H), and eta=V gamma. Let q_t be the actual DATA spectral marginal and k_t the true conditional probability of a nonempty controller frequency. Then sum q_t k_t=eta. These identities hold also with fully shared DATA variables. Supply the original support-positive source/controller references of A029@4, inherited through their OWN physical channels. Retain their canonical account T and slack S, so canonical reference divergence is T-S. Its row marginal r and nonempty controller shape B are fixed during each odds conversion. Reference-only rows retain their full mass; none are deleted.

For ANY adaptive real epsilon in [0,1/16], prescribe

    ell_t=(1-epsilon) k_t + epsilon eta.                 (1)

Only occupied true DATA rows are changed. Zero-true rows retain the declared canonical completion. If eta=0 or eta=1, all occupied k_t equal that endpoint and the law is unchanged. When B is undefined, eta=0 and no new nonempty mass is requested. For eta in (0,1), (1) preserves the TRUE-weighted mean sum q ell=eta and gives the declared regularity bounds epsilon eta <= ell_t <= 1-epsilon(1-eta). This is true-weighted calibration, not preservation of reference-weighted mass sum r ell. No such latter assertion is used.

The extra divergence over the canonical reference is exactly

    C=sum_t q_t D(Bern(k_t)||Bern(ell_t)).                (2)

The cancellation in (2) uses unchanged r and B. It remains valid for arbitrary supplied references, not only exact ones.

## 2. A price for all rows, including the vacuum

Fix eta and epsilon. Joint convexity of Bernoulli KL, applied to the affine pair (k,(1-epsilon)k+epsilon eta), gives the endpoint chord

    D(k||(1-epsilon)k+epsilon eta)
    <= (1-k) log2(1/(1-epsilon eta))
       + k log2(1/(1-epsilon(1-eta))).                   (3)

This can also be proved by the two-atom log-sum inequality with mixture weights (1-k,k). Averaging (3) gives C<=F_epsilon(eta), where

    F_epsilon(eta)=(1-eta) log2(1/(1-epsilon eta))
                  +eta log2(1/(1-epsilon(1-eta))).       (4)

The endpoint conventions in (4) are continuous and yield zero at eta=0,1. All logarithm arguments are positive: epsilon<=1/16. Using -ln(1-x)<=x/(1-x),

    (1-eta)[-ln(1-epsilon eta)] <= epsilon eta,
    eta[-ln(1-epsilon(1-eta))] <= eta[-ln(1-epsilon)].

The first inequality uses (1-eta)/(1-epsilon eta)<=1; the second uses monotonicity. Therefore

    C <= [epsilon-ln(1-epsilon)] eta / ln(2)
      <= [1/16+ln(16/15)] eta / ln(2)
      < (31/160) eta <= eta/2.                          (5)

The strict coefficient uses ln(16/15)<1/15 and ln(2)>2/3. Write the non-strict bound C<=31 eta/160 so it also covers eta=0. No fixed additive floor on the vacuum is imposed: its floor vanishes with actual controller occupancy.

## 3. Same original allowance, both physical deficits

Under DATA queries gamma is harmonic and V is fixed, hence eta is harmonic. Under a CONTROL query j, gamma is fixed and

    eta_parent - mean eta_children = gamma * ahat({j})^2 >=0.

Also eta<=gamma I(a)=I_controls(F). Thus eta is the same physical supermartingale already used by A029@4. The new pooled target class and the old relative-odds class can be chosen in ANY adaptive order at every reached node. Both obey C<=eta/2. Consequently use exactly the OLD allowance

    Tbar=T+eta/2, Sbar=S+eta/2-C >=0,
    D_target=Tbar-Sbar.

No second allowance is allocated for (1). If R=U-b-Hroot-Tbar_root, the exact full payment to any finite frontier is

    Hroot+Tbar_root - sum_internal w*(Tbar-mean Tbar_child)
                       - E_frontier Sbar.              (6)

Every weight is the global physical reach. The complete entropy path telescopes to Hroot-E Hleaf; full terminal cross-entropies supply E(Hleaf+D_target). This proves (6). When a changed reference is physically queried first, raw reconstruction charges include the actual erasure and outcome KL refunds; only the signed net change belongs in (6). Those refunds are not booked twice. An arbitrary subsequent no-reset physical continuation only reduces payment.

For one split let A=Tbar_parent-mean Tbar_children, with actual child deficits d_s=C_s-S_s-eta_s/2=-Sbar_s. The exact criterion is (d_0+d_1)/2<=R+A. If a smaller candidate allocation is being tested, replace eta_s/2 by its ACTUAL inherited allocation, not a fresh grant. Refining a leaf replaces its bill by its expanded children and release. It never adds the old leaf slack to that expansion. Signed returns and arbitrarily many conversions at the same node telescope. Positive parts can grow without bound, as the prior dummy-coordinate witness shows.

In particular every literal prefix and quota covered by A029@4 remains paid, at the SAME original 4I, old debit1/8, and reserve>121/128 for the prior m>=1 family. Only the admitted continuation class grows; the proof imports that old prefix without claiming new finite reproduction of its numerical margin here.

## 4. Actual Boolean separation from bounded relative odds

Let a(y)=y, G=1, and H be negative only at the origin of n DATA bits. Set delta=2^-n. The mux is an actual point defect on n+1 variables, I=(n+1)delta, gamma=eta=delta. Its empty DATA row has q0=1-2delta+2delta^2 and k0=delta^2/q0. With epsilon=1/16, the pooled target has

    ell0=(15/16)k0+delta/16,
    ell0/k0=15/16+q0/(16delta).

For n>=6 this exceeds 2. Hence the RELATIVE ODDS factor ell0(1-k0)/(k0(1-ell0)) is also >2. It diverges as n grows. This is outside A029@4's [1/2,2] target class, including at the vacuum, yet its ENTIRE all-row cost is <=31delta/160, from the existing eta/2 allowance. Fixed-strength vacuum mixing instead has the earlier nonvanishing cost obstruction. No lower bound on a fixed vacuum mass survives here.

When epsilon>0 and eta>0, the declared floor ell0>=epsilon eta itself is necessary for membership in this chosen floor class. For n>=7, epsilon eta/k0=q0/(16delta)>2, so ANY member of that class is outside the upper-relative-factor-2 class at the vacuum. This is necessity for the explicitly declared compatible class, NOT necessity for every FEI proof or every useful stopping rule. Both descriptions are essential.

## 5. Source reviews and first unsupported universal line

A028's latest exact admission C<=Z+gamma Cvac follows directly from chain-rule cancellation T-Dtarget=S-C. Its dummy-DATA witness can be reconstructed with exact Walsh arithmetic; outside a posterior-channel image does not imply an unaffordable child. A026@6's nonempty floor price J/8 and eta/2 sum is a different envelope: fixed nonempty floors do not provide the occupancy-calibrated vacuum floor (1). This stage does not revise either source.

The first unsupported universal line is still an influence-priced ORIGINAL complete source/controller allowance Hroot+Troot with enough real unused capacity and a stopping/terminal policy that implies FEI. Formula (1) provides a compatible arbitrary-core target prescription with a paid, vanishing vacuum floor, but it is not proved sufficient for that policy. Exact original-reference inheritance and cheap target changes cannot alone upper-bound Hroot. Full FEI has not advanced to a proved dimension-independent constant.

The following reduction settles the simplest version of that next question negatively: occupancy calibration alone does not give a simpler terminal class.

## 6. Even the nondegenerate calibrated terminal class retains full FEI

Let h be ANY Boolean function. For each integer m>=1 form the actual Boolean function

    F_m(y,z,x^(1),...,x^(m)) = AND2(y,z) product_j h(x^(j)),

where the sign gate AND2 is negative only at the origin of its two-bit cube. All blocks are disjoint. Take y as the sole controller and z plus all x blocks as DATA. The AND2 spectrum is uniform on its four frequencies. If P_m is the product spectrum of the m h-blocks, the full law is P_F(U,v,S)=P_m(S)/4 for U,v in{0,1}. Thus q(v,S)=P_m(S)/2 and EVERY occupied conditional k(v,S)=1/2. Moreover eta=1/2 exactly, since the two DATA sources differ on precisely half their inputs. These are nondegenerate examples: eta is neither0 nor1; controller and both physical gate inputs are relevant.

Every pooled target (1) equals the TRUE spectrum. It satisfies the declared floor and ceiling, exact calibration, and even the stronger condition that every conditional k is the SAME interior constant. The conversion cost is zero. Nevertheless

    H(F_m)=m H(h)+2,  I(F_m)=m I(h)+1.                  (7)

Consequently a dimension-independent FEI bound with constant K just for this calibrated terminal class implies H(h)<=K I(h) for every h: apply the bound to F_m, divide by m, and let m grow. Conversely full FEI trivially bounds the class. This is a reduction, NOT a counterexample to FEI or to the paid floor theorem. It strengthens the earlier AND2-carrier warning by putting all carriers INSIDE the new fully calibrated, fixed-occupancy, zero-conversion terminal class. No stronger tensor entropy claim is assumed; (7) follows from disjoint spectral products and exact influence additivity.

Thus no further floor-only enumeration addresses the universal gap. NEXT must consume a concrete proposed ORIGINAL supplier or stopping certificate that uses DATA-spectrum structure beyond these row odds, challenge it on F_m while retaining its actual mH(h) terminal debt, and identify its first unpaid original-core line. This exact obstruction and the paid enlargement can be used immediately by A028/A096/A097 without inventing a mandatory floor policy.
