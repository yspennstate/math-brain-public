# Fine compatibility can make a coarse conversion invoice unattainable

All laws are complete normalized probabilities on a finite remaining Fourier-label set. All entropy/CE/KL are bits. Both physical children and all old accounts remain. This is a generic variational theorem applied to actual Boolean splits, not a new Booleanity admission inequality or an initial-source theorem.

## 1. The exact class and the missing fine constraint

Let p+,p- be the squared spectra of the two actual Boolean children of one physical query, and q=(p++p-)/2 its actual spectral marginal. Fix a finite partition into blocks z. Write a_tau(z)=p_tau(z), q(z)=(a_+(z)+a_-(z))/2. Prescribe nonnegative block reference masses r_tau with (r_++r_-)/2=q at block level. The ADMISSIBLE CLASS in this theorem requires BOTH full laws R_tau to have those block masses and (R_++R_-)/2=q AT EVERY FINE LABEL. This full-mean compatibility is an explicit additional route requirement, not a consequence of Booleanity or A097's calibration rule.

Restrict to finite coarse KL, namely r_tau(z)>0 whenever a_tau(z)>0. The class is nonempty: distribute each requested plus block mass over q in that block, R_+(S)=r_+(z)q(S)/q(z), and set R_-=2q-R_+. These are nonnegative because 0<=r_+(z)<=2q(z); both normalize. This construction alone need not have finite fine CE at boundary r_tau(z)=0, but finite coarse KL ensures each zero child reference block has zero true child block. On positive-reference blocks the construction covers every occupied fine atom.

The KL chain rule gives the coarse lower invoice

 L=average_tau D(a_tau||r_tau),
 average_tau D(p_tau||R_tau)>=L.                       (1)

For a block with a_tau(z)>0, put kappa_tau(S)=p_tau(S)/a_tau(z). Equality in (1) requires R_tau(S)=r_tau(z)kappa_tau(S) on the ENTIRE block, including true-zero labels. Indeed equality in Gibbs for the normalized conditional laws forces equality of the full conditionals, not only occupied ratios. When both a_+,a_->0, full compatibility then reads

 (r_+-a_+)kappa_+ +(r_--a_-)kappa_-=0.

Since the two shifts are opposite, this is exactly

 (r_+(z)-a_+(z))*(kappa_+(S)-kappa_-(S))=0 for EVERY S in z. (2)

Therefore the coarse lower invoice is attained IFF each block occupied by BOTH actual children either has no prescribed coarse shift, r_+=a_+, or the two child conditional spectra in that block are identical. A block occupied by only one child causes no extra obstruction: set its occupied child's reference proportional to its true conditional, and allocate the remaining nonnegative 2q mass to the true-zero child. Its prescribed occupied reference mass cannot exceed the actual occupied child block mass because the other prescribed reference is nonnegative. A zero midpoint block has zero prescribed masses and both full references zero there.

This also proves sufficiency by constructing all blocks and combining them; their prescribed masses already normalize each full law. If (2) fails, the exact infimum is STRICTLY above L, not merely unattained. The compatible class is compact, extended KL is lower semicontinuous, and the explicit finite candidate above ensures a finite minimum. If its minimum equaled L, nonnegativity of every within-block KL would force (2), a contradiction. No unproved quantitative separation is inferred from compactness.

An equivalent all-rational test on a doubly occupied block is

 (r_+-a_+)*(a_- p_+(S)-a_+ p_-(S))=0 at every fine S.    (3)

At the ACTUAL midpoint q=(p++p-)/2, isospectrality gives q=p+=p- and kappa_+=kappa_-, recovering A031's matched-conditional special case. A031's more general arbitrary incoming q need not equal the actual midpoint and retains its separate ghost-capacity optimizer; that general case is not solved by this simpler criterion. A097's outcome-specific calibrations do NOT impose full-mean compatibility and are not refuted here.

## 2. An actual Boolean positive-gap witness and exact minimum

Take f(x0,y)=g(y) when x0=+1 and f(x0,y)=y1 when x0=-1, where g=-1 only at y1=y2=+1 and +1 otherwise. On remaining labels (empty,{1},{2},{1,2}), actual child spectra are

 p+=(1/4,1/4,1/4,1/4), p-=(0,1,0,0),
 q=(1/8,5/8,1/8,1/8).

Use blocks z0={empty,{1}}, z1={{2},{1,2}}, and REQUIRE both reference block profiles r+=r-=(3/4,1/4). These preserve the inherited coarse midpoint. The actual child profiles are a+=(1/2,1/2),a-=(1,0). In z0 both children occupy, the requested shift is1/4 and their conditionals differ. Thus the coarse invoice cannot be attained.

Full compatibility parameterizes the first block as R+=(x,3/4-x), R-=(1/4-x,1/2+x), 0<x<=1/4. Its objective's derivative, after multiplication by a positive factor, has the sign of

 -[3/8+(11/4)x-6x^2].

On0<=x<=1/4 this polynomial is positive: 3/8+(11/4)x-6x^2 >=3/8+(5/4)x>0, using6x<=3/2. Hence the objective strictly decreases, and the exact minimum is x=1/4. The second block has true mass only in the plus child and is minimized by uniform conditionals. A complete optimizer is

 R+*=(1/4,1/2,1/8,1/8), R-*=(0,3/4,1/8,1/8).

Both full laws normalize, their average is exactly q, and zero R-*(empty) covers no true-minus mass. The exact minimum and coarse lower invoice are

 M=1/8+(1/2)log2(4/3), L=(3/4)log2(4/3),
 M-L=1/8-(1/4)log2(4/3)>0,                         (4)

because log2(4/3)<1/2 is equivalent to16<18. This is an exact analytic optimum and strict rational-log certificate, not a floating optimizer.

For incoming actual full parent reference Q=P_f, the inherited marginal is q. The exact complete signed query-plus-conversion increment is M-J_i(f), with B_i included, because H(parent)=B_i+average H(children)+J_i. Here it equals (1/8)log2[5^5/(2^7*3^4)]<0, certified by3125<10368. Thus (4) is an extra COMPATIBILITY price over the coarse surrogate, but the actual JS pays the full price in this example. It is NOT an unpaid transaction or FEI obstruction. The checker reconstructs the entire parent and both children and verifies this identity as a prime-log linear form. Any available JS, occupancy refund or actual unused ancestor reserve must still be credited exactly once.

## 3. Universal limitation and the Booleanity hierarchy

The full Boolean hierarchy is sum_S fhat(S)fhat(S xor U)=1{U=empty} for EVERY shift U, equivalently f^2=1, and the same identities at EVERY physical restriction. Our witness is an actual truth table, so it satisfies the complete hierarchy. The proof of the compatibility criterion itself is a probability fact and is not represented as a further full-Booleanity inequality. Previously imported dyadic fixed-order signed-convolution and small-defect controls remain ruled out as admission replacements; the separate original cyclic atom-cap-prefix family/checker is still absent locally, so no missing import is fabricated.

First unsupported universal line: a universal construction/policy must actually require a specified compatible class, and its exact minimum (including the extra fine price) must be paid from SAME unused original influence after all old debits and full terminals. A011's new edit stages CHANGE the target function and do not automatically preserve a fixed inherited mean; this theorem is NOT a claimed application to those stages without an explicit compatibility requirement. A011/A001 retain an unpaid arbitrary-core source. The next useful step is to test a truly required target against (3), not append optional marker cycles or increase a fixed Booleanity prefix. Full FEI OPEN.
