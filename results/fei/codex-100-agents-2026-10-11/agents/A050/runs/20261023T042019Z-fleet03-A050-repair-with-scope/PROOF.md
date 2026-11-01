# Two full correlated resets from one original source account

All cubes are finite and uniform, functions are signs, and entropy/KL units are bits. Full FEI remains OPEN. This extends a supplied-reference transaction; it does not supply a reference for an arbitrary Boolean core.

## 1. Source and allowed histories

Let h be the product of disjoint point signs H_j of widths r_j>=2. Put d_j=2^-r_j, v_j=4d_j(1-d_j), and t=Pr(h=-1). Use precisely the INITIAL A050 correlated lift Q for F_h: on x0 it is the fresh a-character, on x1b0 it is +1, and on x1b1 it is h. Each original factor reference is q_j(0)=p_j(0), q_j(s)=(7/8)p_j(s)+(v_j/8)1_full(s) for s nonempty. The full lifted Q copies the actual six control atoms and has q(s)/16 on each of four nonempty-data control copies. It is normalized and dominates the source. No incoming canonical reference is converted to Q for free.

Query b and retain b0. In b1 allow any finite adaptive data-only prefix. At selected frontier leaves expose a once (retain BOTH signs) or x once (retain its character partner). After a reset both activation children to the full lifts specified below; after x reset its core child only. These are the FIRST resets. In every reset descendant allow separate finite adaptive DATA-only histories; keep x unqueried in activation children. At any selected stopping frontier make a SECOND reset to the prescribed full law, at most once along each path. Retain every complementary leaf. Further finite data-only queries without another reset are allowed. The policies of the two a-sign branches may differ. All choices depend on physical history, never on the encoded Fourier set.

For a current restricted core g and0<=alpha<1, define r_g^alpha as the tensor of its conditional factor references. A surviving width k>=2 point factor uses r_k^alpha(0)=p_k(0) and r_k^alpha(s)=(1-alpha)p_k(s)+alpha Var(point_k)1_full(s). A character or constant uses its exact spectral law, including any irrelevant physical coordinates with zero frequency. Signs do not change squared spectra. Thus r_g^alpha is normalized, dominates p_g, and matches its empty mass. A pure-core reset uses r_g^alpha itself. An activation J_s(x,z)=s on x0,g(z) on x1 copies its actual two zero-data masses (s+Eg)^2/4,(s-Eg)^2/4 and uses r_g^alpha(T)/4 on each of the two x copies for T nonempty. This is a FULL replacement law, not a mixture with the incoming reference. Direct summation gives D(P_J||R_J^alpha)=D(p_g||r_g^alpha)/2. Constant/character degeneracies require no division.

## 2. Sharpen the original supplier margin before spending it

The original lift gives CE(F,Q)<=3+CE(h,q)/4 and I(F)=1+t/2+I(h)/4. Write l0=log2(8/7). For a width-r point of defect d, I=2rd, nonempty entropy is exactly 8(r-1)d(1-d), empty entropy is at most 4d(1-d)/ln2, and its original factor KL is at most 4d(1-d)l0. Therefore

    (4I(point)-CE(point,q))/4
      >= d(1-d)(2-1/ln2-l0)+2r d^2 =: B_r.

Tensor additivity implies the ORIGINAL margin

    M0=4I(F)-CE(F,Q) >= 1+2t+sum_j B_rj.       (1)

This improves the earlier coarse m*d/4 bound by retaining the actual empty-entropy estimate and the positive 2r*d^2 term. It is unused margin of the SAME original source, not new influence or a renewed reference account. The empty-entropy estimate follows from -(1-v)ln(1-v)<=v. Also ln2>56/81, from the first two positive terms of 2*atanh(1/3). Hence a rationally certified lower bound replaces 2-1/ln2 by 31/56.

## 3. One variance budget per reset generation

For a finite data stopping partition L, E Var(H_j|L)=Var(H_j)-Var(E[H_j|L])<=v_j. This is the finite total-variance identity. Adaptive interleavings among factors and unequal stopping depths do not affect it. At a physical leaf the data cylinder still leaves all unqueried bits independent and fair; the core is still a signed tensor of restricted point factors.

A full fresh factor obeys D(p_k||r_k^alpha)<=Var(point_k)*l(alpha), where l(alpha)=log2(1/(1-alpha)). Add over factors. At a reset generation the reach-weighted fresh KL T_n is at most

    T_n <= (1/4) sum_j v_j*l(alpha_n)
         = sum_j d_j(1-d_j)*l(alpha_n).          (2)

The factor 1/4 includes b1's reach1/2 and either the pure x1 reach1/2, or the activation KL factor1/2 averaged over its fair a pair. The second generation may use different data policies in the two a branches. Apply total variance separately to those sign-conditioned partitions and average. Selection of only some leaves decreases the nonnegative gross fresh-KL sum. A prefix or first-reset frontier also partitions into cylinders; applying total variance within its cells and then summing gives the same ORIGINAL v_j bound. Consequently (2) is valid at both generations, without restarting a conditional variance reserve. It also permits later no-reset data continuations.

This estimate bounds gross fresh KL, not the actual reset increment. Let sigma_n be the sum over that generation of reach times [D(P_leaf||R_leaf)-D(P_leaf||Q_inherited_leaf)]. The complete inherited KL is nonnegative, so sigma_n<=T_n. The actual signed sigma_n, including its normalization and reference-only rows, is nevertheless the amount retained in the ledger.

More generally, for any finite prescribed number of reset generations the same argument gives a sufficient cumulative condition

    sum_j d_j(1-d_j)*sum_n l(alpha_n) <= 2t+sum_j B_rj.  (3)

Only the two-generation application is certified computationally here. Formula (3) is an analytic sufficient hypothesis, not a claim that an unlimited number of equal-size resets is free. Within this particular gross-variance bound it is the exact aggregate admissibility test; no globally weakest repair is claimed. A per-factor bound is convenient but stronger than (3).

## 4. Actual terminal eligibility survives divergent a histories

For any Boolean core g with mu=Eg, direct pivots give I(J_s(g))=(1-s*mu)/2+I(g)/2. Erasing x from its squared spectrum gives (delta_0+p_g)/2, whose entropy is at most 1+H(g)/2; the erased x contributes at most one more bit. Thus, with S4(g)=4I(g)-H(g),

    S4(J_s(g)) >= -2s*mu + S4(g)/2.             (4)

Each point-tensor restriction has H(g)<=4I(g), by the elementary point entropy estimate and additivity; constants and characters have zero entropy. Within either of the TWO complete sign-conditioned data partitions, E mu_leaf equals the same original core mean. Therefore the -2s*mu terms cancel after averaging the fair signs, even with different policies. The full activation pair has nonnegative average S4. This independently reconstructs A049's paired-mean proof; an individual activation terminal need not have nonnegative S4.

An x pair has a retained character with surplus4 and a data core with nonnegative surplus. Unexposed selectors have surplus>=2. The retained b0 terminal has reach1/2 and surplus2. Hence at every final frontier in section1, including further data continuations,

    S=E_terminal S4 >=1.                       (5)

References and resets do not change physical entropy or influence. No branch is dropped to establish (5).

## 5. Full signed payment, no renewed owner

Transport every current reference by the actual coherent physical query kernel, fair on erased source-zero rows, and normalize using the ACTUAL reference branch probability. Retain all reference-only rows. The atomwise erasure/outcome/child likelihood product gives, with A0=D(P_F||Q),

    A0+sigma1+sigma2 = all reached erasure/outcome KL
                        + complete final reference KL.   (6)

Here the references in later query releases are the already-reset incoming laws. No cumulative-erasure shortcut is used. Let e=H0-EHleaf-4(I0-EIleaf). Exact algebra gives

    S-[A0+e+sigma1+sigma2]_+
       = min(S,M0-sigma1-sigma2).               (7)

Combine (1)-(3),(5): the right side is at least1. Any one eligible old booking 0<=omega<=1/4 against this original account therefore leaves at least3/4. The first reset is already booked and remains explicitly present as sigma1. Bounding sigma1+sigma2 by T1+T2 charges each fresh law once; it neither renews the first bill nor replaces the signed account by separately clipped query/reset bills. All complementary terminal entropy and KL are retained in (6)-(7).

## 6. Concrete all-dimensional applications and the boundary

Fix first alpha1=1/7, as A046. For second alpha2=1/11,

    l0+l(alpha1)+l(alpha2)=log2(22/15)<31/56,

certified by 22^56 < 2^31*15^56. Hence (3) holds STRICTLY for every finite heterogeneous list of widths>=2, every number of factors, and every history in section1. This supplies the paid second FULL nonempty-profile change after a exposure, vacuum overlap and divergent data queries. It requires no assumption that sigma2 is nonpositive.

For the requested unchanged second alpha2=1/7, the combined logarithm is log2(14/9)<13/20, certified by14^20<2^13*9^20. First, for 2<=r<=7,

    31/56+2r/(2^r-1) >=31/56+14/127 >13/20.

The sequence r/(2^r-1) decreases, since (r-1)2^r+1>0. Thus (3) again holds strictly for any number of factors with widths2..7. This includes the original A047 m64,r2 and A049 m9,r3 canonical counterexamples, arbitrarily many such factors, and heterogeneous mixtures of these widths. A047's all-width m=2^(r+2) family is covered at every r by the second1/11 theorem, and at r<=7 by the second1/7 theorem.

Second, retain the ORIGINAL 2t allowance in (1). Let lambda=sum_j d_j. Since 1/(1-2d_j)>=1+2d_j and finite products have nonnegative cross terms, mu_h=product_j(1-2d_j)<=1/(1+2lambda). Consequently 2t>=2lambda/(1+2lambda). For two1/7 resets the combined logarithmic excess above31/56 is less than13/20-31/56=27/280. Ignoring only the nonnegative2r*d^2 terms, the excess gross cost is therefore less than27lambda/280. If lambda<=9, the same original2t is at least2lambda/19>27lambda/280, since560>513. Thus (3) pays TWO FULL1/7 resets at EVERY width whenever total defect load lambda<=9. This is an aggregate hypothesis on the initial core, not a fresh sign-branch reserve. In particular A047's entire all-width m=2^(r+2) family has lambda=4 and satisfies it. The earlier width<=7 application also covers large-load examples such as m64,r2, which has lambda16.

The deliberately coarser rational per-factor budget without2t does NOT certify second1/7 when r>=8: log2(14/9)>5/8 follows from14^8>2^5*9^8, whereas31/56+16/255<5/8. Monotonicity handles larger r. This is a failure of that sufficient bound, NOT a positive-reset counterexample or a refutation of A049's finite negative signs. The aggregate criterion including2t may admit further mixtures and larger loads, and actual negative inherited-KL refunds may pay more than this gross estimate. No universal all-width/all-load same1/7 sign conclusion is asserted.

## 7. First unpaid line

The all-width/all-load same1/7 second-refresh sign remains unproved here. The next narrow action is to price that actual conversion at a surviving width>=8 activation child outside the aggregate budget (in particular total defect load>9), preserving sigma1, both sign subtrees and the old quarter; extra gross budgets are inadequate without sharper inherited-KL control. Universally, the influence-priced complete correlated supplier for an arbitrary Boolean core remains missing. The repair closes a concrete two-reset history interface, not full FEI.
