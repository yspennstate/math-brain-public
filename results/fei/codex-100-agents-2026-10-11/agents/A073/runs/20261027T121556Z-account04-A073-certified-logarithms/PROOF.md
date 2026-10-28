# A signed invoice with a rational separation bound

Full FEI remains OPEN. Units are bits. This result certifies the actual price of the fixed AND2 admission used in A085's sign-boundary control; it supplies neither an original reference for arbitrary Boolean cores nor a necessary stopping policy. The earlier A073 count28/reserve11/400 and tensor count15/reserve3/4 are unchanged.

## 1. Independently reconstruct the Boolean invoice

Take f=(-1,1,1,1) on the uniform two-bit cube. Its four Walsh coefficients have absolute value1/2, so its squared law p is uniform on four spectral labels. Direct spectral degree weighting gives I=1 and H=2. A calibrated current reference is

    q_b=(1/4,(3/4-b)/2,(3/4-b)/2,b), 0<b<1/3.

The event A is the final nonempty label; t=3/4, p(A)=1/4, and the required floor is ell=1/3. Preserving the CURRENT conditional profiles on A and on the other two nonempty labels gives a target with event mass z. The cost derivative is t(z-a)/(z(t-z)ln2). Thus its unique minimizer under z>=ell is z=ell, and

    q*=(1/4,5/24,5/24,1/3).

Every reference entry is positive on the interval used below; the vacuum agrees, the profiles are unchanged, and no ghost atom or mass is deleted. Direct subtraction of full cross-entropies, not a conditioned-only KL, gives

    Delta(b) = CE(p,q*)-CE(p,q_b)
             = (1/4) log2 G(b),
    G(b)=product_s q_b(s)/q*(s)
        =432b(3/4-b)^2/25.

The factorization

    432b(3/4-b)^2-25
      =432(b-1/3)(b^2-7b/6+25/144)

gives the zero bcrit=(7-2sqrt6)/12 in (1/8,1/4). The other two roots are1/3 and a number greater than3/4. In the source's strict interval0<b<1/3, the invoice is negative below bcrit and positive above. On zero or one Boolean bit, every squared spectrum is a point mass; a nonempty event cannot satisfy0<p(A)<t. This reconstructs A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY@1 unchanged, including its dimension-minimal scope. The first binary64 coincidence in its declared m=4..160 adjacent-dyadic sequence is independently reproduced at m=58; no global smallest floating-point failure is asserted.

## 2. New uniform rational margin, with every side condition

Let b=k/d in [1/8,1/4], with integers d>0 and k>0. Reduction to lowest terms is unnecessary. Put

    N=27k(3d-4k)^2-25d^3
     =(3k-d)(144k^2-168kd+25d^2).

Then G-1=N/(25d^3), so the sign is exactly the sign of this INTEGER N. On this interval3k-d<=-d/4, so its magnitude is at least d/4. The second integer factor is NONZERO: if it vanished, (12k-7d)^2=24d^2. The power of2 dividing a nonzero integer square is even, whereas the right side has exponent3+2v2(d), which is odd. This is impossible. It follows that

    |N| >=d/4,
    |G-1| >=1/(100d^2).                              (1)

The likelihood G is positive. Its derivative is(432/25)(3/4-b)(3/4-3b), nonnegative on[1/8,1/4]; hence G<=G(1/4)=27/25. No positive denominator or discarded endpoint is hidden here.

For EVERY real g>0, integrating1/x between1 andg gives

    (g-1)/g <= ln g <=g-1,
    |ln g| >= |g-1|/max(1,g).                        (2)

The positive atanh series at z=1/3 gives a fixed rational bound

    2/3 < ln2 < 2/3 + 2(1/3)^3/[3(1-1/9)] =25/36.

The lower inequality uses the first positive term. For the upper inequality, replace every denominator2j+1 in the positive tail j>=1 by3 and sum the geometric series; strictness follows from j>=2. All sums converge absolutely, with ratio1/9, so the displayed tail bound justifies the operation. There is no precision refinement.

Combining(1)--(2) with max(1,G)<=27/25 yields the new quantitative bound

    |Delta(k/d)| >=1/(300d^2).                       (3)

For a SUPPLIED disjoint full-terminal seed weight beta=3/8, the actual full cost has magnitude at least1/(800d^2). At an actual reach rho>0 its reached magnitude is at least rho/(800d^2). A zero reach or zero seed weight gives EXACTLY zero; no division by that weight is permitted. The beta=3/8 decomposition is an explicit supplied-interface hypothesis, not a newly asserted Boolean realization. For beta=1 the invoice is the full actual AND2 cross-entropy change itself.

For A085's adjacent dyadic brackets, d=2^m, m>=4, both endpoints belong to[1/8,1/4]. Thus at weight3/8 and unit reach the magnitude exceeds2^(-2m-10). An approximation with guaranteed absolute error at most2^(-2m-11) therefore has the correct sign. This gives a representation-dependent sufficient precision; it does not contradict the absence of a FIXED precision ceiling as m grows. The integer sign test itself needs no logarithmic approximation, and its integer operands have O(m) bits (a constant number of degree-three products). No such per-term margin is claimed for a sum in which opposite prices can cancel.

## 3. Sign-safe intervals and SAME original owner

Use the fixed bounds L=2/3,U=25/36 for ln2. Given exact g=G(b), put x=(g-1)/g and y=g-1. The interval for Delta is one quarter of the minimum and maximum of{x/L,x/U,y/L,y/U}. Multiplying by nonnegative rho beta preserves ordering. This explicitly handles negative numerators: dividing a negative bound as though it were positive would reverse the wrong endpoint. If g=1 or rho beta=0, return exact[0,0]. The polynomial decides a nonzero sign BEFORE any display interval is calculated. The interval endpoints retain that sign for every tested reference and analytically for every admissible rational b.

At a full actual terminal with a supplied disjoint controller/seed decomposition, the same controller and seed weight occur in both laws. The beta factor cancels inside each log, so its FULL CE change is beta Delta. Retain every terminal reach rho, every complement, and all previously charged U. Writing M=B-C-U for the CURRENT unused ORIGINAL account, payment is exactly

    sum_h rho_h beta_h Delta(b_h) <=M.

No negative invoice is discarded, no query erasure or physical-query KL is erased, and a decrease in CURRENT C is not also booked as a new credit. This is a fixed-terminal conversion test, not a theorem that obtains a free physical query. A097's new high-moment example emphasizes why such a query cost must stay in U if it was already incurred; its all-policy theorem is not newly accepted here.

For rational reaches, seed weights and M, let w_h=rho_h beta_h/4 and choose a positive common denominator L of all w_h and M. The exact integer-product test is

    product_h G(b_h)^(L w_h) <=2^(L M).

Clear the positive denominators of all G's and move any negative power of2 to the left. Equality is an admissible payment, and zero weights are omitted without evaluating invalid logarithms. This is code/paired.py's comparison, retaining BOTH reached prices before taking a verdict. A bit-size admission limit returns UNRESOLVED_RESOURCE_BOUND, never a sign or a rejection of the mathematics. Thus the implementation has a bounded safe run while the exact comparison defines the finite rational test without a universal precision cap. No global polynomial bit bound is claimed for arbitrary many terminal weights or their common denominator.

An irrational CURRENT C need not be rounded to use this compiler. When C and old U are finite rational-log expressions, put their terms on the LEFT as well, inverting a base if its coefficient is negative, and retain the ORIGINAL rational B on the right. For a concrete ACTUAL full AND2 account, take B=(5/2)I=5/2 and keep old U=1/4. The initial CE is(1/4)log2[6912/(25G)]. Since G>=27/32 on the full rational interval, this CE is at most(1/4)log2(8192/25)<17/8: squaring its equivalent positive rational comparison reduces exactly to512<625, integer margin113. The final q* has G=1, so its CE is also<17/8. Therefore this SAME original account has reserve>1/8 before and after the complete signed admission, including old U. The helper adds CURRENT CE terms and the signed price before comparison, and independently reconstructs the direct final CE. As a counterguard, matched q=p has CE=2; original B=9/4 with U=1/4 is a VALID zero-unused account, and its positive floor admission is exactly rejected. This is an end-to-end oracle/control certificate, not a new claim about the FEI difficulty of AND2 or a general source supplier.

## 4. What is actually checked

The frozen main domain is478 references: both neighbors in159 predeclared dyadic brackets m=4..160,512,1024, plus160 distinct rationals with denominators at most64 in[1/8,1/4]. It keeps Boolean dimension2. The primary helper uses integer bisection of the decreasing quadratic and the expanded cubic. The separate helper uses integer square roots, the direct FULL q_b/q* likelihood product and the paired invoice's combined product. It imports no primary helper. For each main reference it checks12 exact owner comparisons using beta in{1,3/8}, reach in{1,1/2}, and CURRENT margin in{-1/64,0,1/64}. Both reached terminal prices are separately combined in477 paired comparisons. Tests include exact equality, zero reach/weight, negative margins, the strict incoming endpoint b=1/3 used only as a boundary control, and an intentionally unresolved resource hold. All old U=1/4 in the paired receipt stays retained; it is not treated as extra unused margin.

The proof of(3) is uniform over all rational b in the stated interval. The tests establish finite identities, implementation consistency and the stated first alias sequence; they do not extend the class to arbitrary cores. Native core Lean fixtures check ONLY the two integer inequalities at m=58, with source/compiler and axioms receipts recorded separately on success. The uniform rational margin, all-m argument, complete census and original-account theorem are prose proofs with exact certificates, not full Lean formalizations.

## 5. First unsupported line

A universally required useful arbitrary-core compatible profile, an influence-priced original complete source, and enough genuinely UNUSED original margin after all physical-query KLs/old bills remain unconstructed. This stage closes A085's external sign-boundary review and supplies a quantitative certified invoice oracle for that obstruction. It does not pay an arbitrary source or improve a universal FEI constant. The next short route is to apply the exact aggregate test to ONE proposed necessary arbitrary-core admission using its actual depleted margin; without that proposal, more optional near-zero examples cannot close FEI.
