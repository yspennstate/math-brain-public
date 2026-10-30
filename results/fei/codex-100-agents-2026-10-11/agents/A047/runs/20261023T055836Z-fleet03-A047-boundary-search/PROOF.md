# A same-support obstruction to Boolean-factor refresh

All inputs are uniform Boolean signs; entropy and KL are in bits. Full FEI remains OPEN. This refutes an extension of the point-factor reference rule, not A036's point-factor theorem.

## Exact actual Boolean witness

Write cube inputs as bits a,b,c. Set g(a,b,c)=-1 exactly when a+b+c=1, and +1 otherwise. Its truth table in little-endian order is (1,-1,-1,1,-1,1,1,1). Its Walsh coefficients are 1/4 at empty, -1/4 at singletons, +1/4 at pairs, and 3/4 at full. Thus p(empty)=1/16, p(full)=9/16, and p(T)=1/16 at the six other sets. In particular EVERY spectral atom has positive mass. Direct physical edges give I_a=I_b=I_c=3/4 and I=9/4.

For 0<alpha<1 use exactly the full-essential-block spike rule

    q_alpha(empty)=p(empty),
    q_alpha(T)=(1-alpha)p(T)+alpha(1-p(empty))1[T=full], T nonempty.

Constants and characters use their exact spectral laws. This law is normalized and has exactly the source support. Query a, transport q_alpha by the ACTUAL coherent kernel, and normalize by its OWN branch probability. Reset each child to the SAME-alpha rule. Both children remain.

The a=0 child is parity2, with exact reference. The a=1 child is the width2 point defect negative only at (b,c)=(0,0), with uniform four-atom squared spectrum. The erased source probabilities are (1/8,1/8,1/8,5/8); the erased reference probabilities are ((2-alpha)/16,(1-alpha)/8,(1-alpha)/8,5(2+alpha)/16). The actual coherent kernel sends the first three rows entirely to the point child; it sends the full row to parity/point with probabilities 4/5 and1/5. Therefore the reference outcome law is

    r(parity)=(2+alpha)/4, r(point)=(2-alpha)/4.

The inherited parity reference is exact. The inherited point reference, in empty/two singleton/full order, is

    (1/4, (1-alpha)/(2(2-alpha)), (1-alpha)/(2(2-alpha)),
       (2+alpha)/(4(2-alpha))).

The fresh point reference is (1/4,(1-alpha)/4,(1-alpha)/4,(1+2alpha)/4). Both are positive on ALL four source atoms. Consequently the COMPLETE physically averaged new-minus-inherited KL is

    sigma_alpha = (1/8)log2[4(2+alpha)/((2-alpha)^3(1+2alpha))].       (1)

The ratio exceeds1 because its numerator minus denominator is exactly

    alpha^2(18-11alpha+2alpha^2)>0, 0<alpha<1.

Indeed 18-11alpha+2alpha^2>7. This proves strict positivity for EVERY allowed alpha, using actual branch normalization, without any discarded reference-only support. At alpha=1/6,

    sigma = (1/8)log2(1404/1331)>0.                            (2)

The integer sign1404>1331 certifies it exactly. Near alpha=0, sigma_alpha=9alpha^2/(32 ln2)+O(alpha^3), so even the same-support near-exact regime incurs a positive second-order cost. No claim that every arbitrary-core reset has this asymptotic order is made.

The mechanism is a profile change forced by the actual query: its inherited point reference is exactly q_point^(alpha/(2-alpha)), rather than q_point^alpha. For0<alpha<1 the inherited parameter alpha/(2-alpha) is smaller than alpha. For the uniform four-atom point spectrum,

    D(p_point||q_point^a)=-(1/4)log2[(1-a)^2(1+2a)],
    dD/da=3a/[2 ln2(1-a)(1+2a)]>0.

Thus the reset strengthens the spike and costs positively. At the requested alpha1/6 it converts an actual inherited1/11 profile to fresh1/6; it is not a change made to the declared OLD parent profile. This supplies a second analytic view of the sign and identifies the conditional profile that a positive-reset payment must track.

## Coherent activation with the same actual reference

For G_epsilon(x,a,b,c)=epsilon at x=0 and g(a,b,c) at x=1, use A050's normalized two-sector lift: copy the actual two zero-data masses and put q_alpha(T)/4 at each of the two control copies for T nonempty. Query a. BOTH physical activation children are retained. Their fresh references are the corresponding lifts of the parity and point references above. This is the same-profile outer rule, not a guessed product at coherent rows.

Put A=1-alpha/26, B=1-alpha/10, C=1+alpha/2, D=1+2alpha, z=14alpha/65. The erased likelihood ratio old reference/source equals A and B at the two zero-data rows, 1-alpha at the four singleton-data rows, and C at the two full-data rows. The actual reference outcomes are (1+z)/2 and (1-z)/2. Swapping epsilon swaps the two zero-data rows and leaves the answer unchanged. Direct source weighting gives

    sigma_activation = (13/32)log2 A+(5/32)log2 B
                    +(5/16)log2 C-(1/16)log2 D
                    -(1/2)log2(1-z^2).                      (3)

At alpha1/6 this is (1/32)log2 K, where

    K=(155/156)^13(59/60)^5(13/12)^10
       /[(4/3)^2(1-(7/195)^2)^16].                           (4)

The checker independently establishes K>1 by integer cross multiplication. Thus even the normalized coherent activation costs positively, with ALL source and child supports unchanged. This statement at alpha1/6 is finite/exact; no all-alpha activation sign is inferred from the core formula.

## Scope and incoming review

The original small-cube specification exhausts every2bit and3bit sign up to global output negation, every essential queried coordinate, and pure core plus four activation modes (epsilon+/-1, constant or character spectator), at alpha1/6. A global sign changes no core spectrum or query kernel; both controller signs restore the activation scope. Cases with dummy variables use the FULL ESSENTIAL block and constants/characters use exact laws. No coordinate symmetry quotient is used. There are1860 paired queries,1292 strictly negative,328 zero,240 strictly positive; every positive case has exactly matching old/new source support. The95-case pilot had no positive sign because it covered a strict initial subset, not the full domain. Dimension1 endpoints are exact characters/constants; dimension2 has no positive case in this prescribed domain. Thus3 is minimal input dimension for a pure-core counterexample to this SAME-alpha1/6 rule, not a globally minimal FEI falsifier or a theorem for other reference suppliers.

FIRST UNSUPPORTED UNIVERSAL LINE: charge positive arbitrary-Boolean hereditary reference resets to the SAME unused original influence/source budget, keeping old debits, both terminals and all normalization/erasure terms; then supply an influence-priced initial reference for arbitrary cores. Equations(1)-(4) forbid treating these resets as nonpositive merely from matching empty mass and support. There is no FEI counterexample here and no universal constant improvement.
