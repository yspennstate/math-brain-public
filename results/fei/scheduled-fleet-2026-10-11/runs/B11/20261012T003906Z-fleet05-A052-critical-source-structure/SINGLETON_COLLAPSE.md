# Optimal recentring collapses this block certificate to singletons

Let Z be any binary random vector, d_i=P(Z_i=1), and kappa=2/ln2. For a nonempty block A with C=A^c define

    B_A=H(Z_A|Z_C),
    beta_A=sum_(i in A) E min(P(Z_i=1|Z_C),P(Z_i=0|Z_C)),
    U_A=B_A+kappa beta_A.

For i write B_i=H(Z_i|Z_-i), beta_i=E min(P(Z_i=1|Z_-i),P(Z_i=0|Z_-i)), U_i=B_i+kappa beta_i. Zero-probability conditioning fibers contribute zero. Entropy is in bits. For every block,

    U_A >= sum_(i in A) U_i.                                      (1)

Proof: order the coordinates in A. The entropy chain rule expresses B_A as a sum of terms H(Z_i|Z_C, earlier coordinates). Each is at least H(Z_i|Z_-i), since its conditioning set is smaller. For the mismatch term put q_i=P(Z_i=1|Z_-i). Its conditional expectation given Z_C is P(Z_i=1|Z_C). Concavity of q -> min(q,1-q) and conditional Jensen give

    E min(P(Z_i=1|Z_C),P(Z_i=0|Z_C)) >= E min(q_i,1-q_i).

Sum and multiply by the positive kappa to prove (1). This is a distributional statement; no Booleanity or full FEI assumption enters.

If n>=2 and some d_i>0, every relevant singleton is a proper physical block. Irrelevant coordinates have U_i=0. Therefore

    min_(nonempty proper A, sum_A d_i>0) U_A/(sum_A d_i)
       = min_(i:d_i>0) U_i/d_i.                                 (2)

The >= direction follows by (1) and the weighted average; singletons give <=. The same argument applies when restricting blocks to |A|<=w for any w>=1. This does not identify the minimum of the exact physical decrement L_A, only the recentered logarithmic-Sobolev upper certificate.

For an actual Boolean sign the lead's independently reconstructed channel lemma proves J_A<=kappa beta_A and L_A=B_A+J_A<=U_A. For a ratio-critical source, R(f)I_A<=L_A<=U_A; for a dimension-critical K-witness, KI_A+D_K(f)<=U_A. If a singleton satisfies U_i<R(f)d_i, the physical-child deficit identity guarantees some child of larger ratio. Equality only forces a nonnegative child deficit on average; it is not a strict descent assertion. If U_i>R(f)d_i at every relevant i, (2) proves every proper block fails this upper certificate, regardless of its actual decrement or child deficits.

In particular, replacing A052's affine predictor by the fully optimal recentring sharpens the metric but does not allow block size to rescue this upper-bound mechanism. The exact nonnegative loss of the block surrogate relative to singleton addition is

    [B_A-sum_A B_i]+kappa[beta_A-sum_A beta_i].

This is a loss in the certificate. It is not the entropy/channel interface of connected physical components and is not asserted to be a paid Boolean invariant. Actual multi-coordinate channels J_A can capture information once that the coordinatewise upper bound pays several times. Thus the surviving next mechanism is a sharper joint-channel estimate or exact J_A with child/terminal deficits retained, not a larger-block search using the same U_A.

The elementary information cap does not repair the mechanism. Since X_A is uniform on |A| bits, J_A<=|A|. Put Ucap_A=B_A+min(|A|,kappa beta_A). Both |A| and beta_A are superadditive under block assembly, and min(sum a_i,sum b_i)>=sum min(a_i,b_i). Therefore

    Ucap_A>=sum_(i in A)[B_i+min(1,kappa beta_i)],

and its minimum normalized block cost also occurs at a singleton. This analytic extension does not require another search or an entropic uncertainty theorem.

## Exact all-dimensional mechanism obstruction

Let b(x,y)=(-1)^(xy) on two fair 0/1 bits and F_m=product_(j=1)^m b(x_j,y_j), m>=2. The one-factor Walsh coefficients all have magnitude 1/2. Hence the full squared spectrum is uniform on every subset of 2m coordinates, H(F_m)=2m, I(F_m)=m, and R(F_m)=2. Every spectral bit is independent and fair, so for every nonempty proper block A,

    B_A=|A|, beta_A=|A|/2, I_A=|A|/2,
    U_A/I_A=2+2/ln2>R(F_m).

Thus even the fully optimized recentring certificate cannot discover the exact tensor block descent already proved in the lead's R6. If t(A) is the number of pairs intersecting A, every touched pair loses its two entropy bits under restriction, giving L_A=2t(A). The actual joint channel is

    J_A=2t(A)-|A|,

the number of pairs hit exactly once. Revealing a full pair gives J_A=0 and L_A/I_A=2=R(F_m). Every physical restriction has ratio at most 2: untouched pairs retain (H,I)=(2,1), partly queried pairs become characters or constants, and fully queried pairs become constants. F_m is therefore non-strict all-physical-descendant ratio-critical, despite the available exact full-factor block. It is not dimension-minimal or tensor-indecomposable, and this low-ratio example does not refute any proposed high-threshold critical theorem.

For this same family Ucap_A/I_A=4>2, because kappa>2 and beta_A=|A|/2. Thus merely clipping the optimized channel payment by its actual |A|-bit information ceiling also fails every block.

There is also a strict-descending example. Take b times the three-bit point defect g=1-2 indicator(all three bits zero), and arbitrary disjoint tensor powers of this five-bit product. For g, H=4-(9/8)log2(3), I=3/4, and 2<R(g)<3; the upper comparison follows from 3^9>2^14, and the lower from log2(3)<2. The product ratio lies strictly between 2 and 3. Every coordinate in either factor has beta_i=d_i, because in its spectral pair the mass on the coordinate-present side is no larger than on the absent side. Binary entropy's endpoint chord gives B_i>=2 beta_i, so U_i/d_i>=2+2/ln2>4. Equation (2) rules out every proper block certificate at the product's own ratio. Yet revealing one entire b factor gives L_A/I_A=2<R(root); a physical child retains the higher-ratio g factor and the actual deficit comparison certifies strict improvement. These are all-dimensional route obstructions with bounded ratios, not FEI counterexamples.
