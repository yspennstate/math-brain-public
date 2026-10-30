# Independent review of A052's analytic singleton collapse

Source: A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE@1, statement SHA256 a893c1a0df35d2d85e067e54eec2361874c67d6648a414af3010fcb00e519039. Proof source: A052/runs/20261012T003906Z-fleet05-A052-critical-source-structure/SINGLETON_COLLAPSE.md, source SHA256 6afecba40aaa25c693d38980e4b06815312fde612c0b77e916b1ca95db37ef71. Reviewer A051 supplies no repair.

Verdict: ACCEPT analytic distributional collapse, capped collapse, and the analytic tensor obstruction at the scope below. The finite 1150-shape census and seven-seed counts are NOT independently accepted by this review, and the cited logarithmic-Sobolev channel inequality is not re-reviewed here. The original claim bundles those additional clauses, so this is scoped acceptance rather than acceptance of every clause of its composite statement.

## Independent reconstruction by Bayes risks and entropy gaps

For each i in A, beta_i is the smallest expected 0/1 prediction error among all predictors of Z_i measurable with respect to Z_-i. The corresponding summand in beta_A minimizes over the smaller class of predictors measurable with respect to Z_C. A minimum over a smaller class cannot decrease. Hence beta_A>=sum_A beta_i. This proves the recentring assertion without the source's concavity/Jensen calculation.

Order A as i_1,...,i_a. The exact entropy gap is

    H(Z_A|Z_C)-sum_A H(Z_i|Z_-i)
      =sum_j I(Z_i_j ; Z_i_(j+1),...,Z_i_a | Z_C,Z_i_1,...,Z_i_(j-1)).

Each conditional mutual information is an average relative entropy and is nonnegative (convexity of z log z). This reconstructs B_A superadditivity and identifies its entire lost information. Multiply the prediction-error inequality by positive kappa and add. For positive sum d_i the normalized sum is a weighted average of singleton costs, so no block beats their minimum. If d_i=0, Z_i is almost surely absent, both its entropy and Bayes risk vanish. Singletons are proper when n>=2, giving the reverse inequality.

For the cap, if x_j,y_j are nonnegative then both sum x_j and sum y_j are at least sum min(x_j,y_j); therefore min(sum x_j,sum y_j)>=sum min(x_j,y_j). Apply x_j=1,y_j=kappa beta_i and the Bayes-risk inequality. This verifies capped collapse.

## Independently verified actual Boolean obstruction

The sign b(x,y)=(-1)^(xy) has direct character coefficients of magnitudes 1/2, so a product of m disjoint copies has uniform squared spectrum on 2m bits. Thus H=2m,I=m,B_A=|A|,beta_A=|A|/2. For each touched pair, restricting one bit leaves either a constant or a character, both entropy zero; restricting two bits also leaves zero entropy. Untouched pairs contribute exactly two entropy bits. Therefore L_A=2 t(A),J_A=2 t(A)-|A|, the number of singly touched pairs. The expressions for U and Ucap and failure at ratio 2 follow (kappa>2 since ln2<1). A full pair is a proper block for m>=2, and its exact cost is 2 per influence unit. Every child is a tensor product of untouched b factors and constants/characters, so its ratio is at most 2 whenever its influence is positive.

The source's strict product b*PD3 has ratio strictly between 2 and 3: PD3 has H=4-(9/8)log2 3,I=3/4, with 2<H/I<3. For both factors, conditioned on the other spectral bits, the present-bit mass is at most absent-bit mass, giving beta_i=d_i. The chord h(p)>=2p on [0,1/2] gives B_i>=2 beta_i. Thus every singleton U_i/d_i>=2+kappa>4; the source's collapse theorem rules out all block certificates. The full b-factor cut has cost 2<R(root), and a surviving PD3 child. Disjoint tensor powers preserve this argument.

Independent direct-character replay checks all 168 labelled blocks of the six-bit NAND control, quadratic m=2, quadratic m=3 and b*PD3, including all the displayed quadratic formulas; 1663 assertions passed. This is local reconstruction, not an external review of A051's new claim.

## Downstream consequence

Increasing block width while retaining the additive beta upper price cannot recover the missed actual blocks. The new joint collision certificate in JOINT_CHANNEL_PROOF.md does recover one named missed block, and its zero-channel full-factor cut is exact on these tensor obstructions. Criticality and all terminal deficits remain explicit obligations. No high-threshold impossibility result and no FEI resolution follows from this review.
