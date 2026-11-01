# A fixed padding influence cannot pay the upper-set discount

The absolute upper-set discount of an actual parity lift is not bounded by a universal constant times its added influence. This is a signed-drift obstruction, not a counterexample to FEI. Every physical influence remains in the calculation. Independent mathematical review is pending.

## 1. Actual Boolean family and exact physical costs

Let r>=1, n=2r+1, and let M_n(y) be majority on n uniform signs. Put

 g(a,y)=(1+a)/2+(1-a)M_n(y)/2,
 f(a,y)=a(prod_j y_j)g(a,y),
 F(a,y,z)=f(az,y_1z,...,y_nz).

These are Boolean functions, on n+1,n+1,n+2 actual physical bits respectively. Multiplication by the full character permutes Walsh coefficients and preserves their entropy. The last line is a systematic one-bit parity code, not a prescribed spectral law.

Write c=binom(2r,r)/4^r. Balance and the pivotal tie probability give

 I_a(g)=1/2, I_yj(g)=c/2, I(g)=(1+nc)/2.

Multiplication by the full character complements the pivotal event at EACH coordinate. Thus

 I(f)=n+1/2-nc/2.

All original-coordinate influences of F equal those of f. Since n is odd, M_n(-y)=-M_n(y). Direct evaluation gives f(-a,-y)=f(a,y) on exactly half the inputs (equivalently, g has odd spectral mass 1/2). Hence

 I_z(F)=1/2, I(F)=n+1-nc/2.                                      (1)

This counts the auxiliary bit. In particular I(f)>=n/2+1/2 and I(F)>=n/2+1, since c<=1. The entropy of f is at most n+1 bits, the logarithm of its number of possible Fourier rows. Entropy preservation therefore gives H(F)<2I(F), and H(f)<=2I(f). The family has a bounded full entropy/influence ratio despite its unbounded discount per added influence.

The complete spectrum of g has coefficients 1/2 at empty and {a}, and Mhat(S)/2,-Mhat(S)/2 at S,S+{a} for odd nonempty S. Therefore, with all means retained,

 H(f)=H(F)=H(g)=2+H(M_n)/2.                                      (2)

## 2. Exact discount and its logarithmic lower bound

For every Boolean h let p_h(S)=hhat(S)^2, pi_h(S)=sum_{T containing S}p_h(T), and

 U(h)=sum_{p_h(S)>0}p_h(S)log2(pi_h(S)/p_h(S)).

For a full parity lift Lh, occupied rows S acquire the tag |S| mod2. Its exact discount is

 d(h)=U(h)-U(Lh)
 =sum_{S odd,p_h(S)>0}p_h(S)log2[pi_h(S)/sum_{T containing S,T odd}p_h(T)] >=0.       (3)

Every denominator is at least p_h(S)>0; zero rows are omitted. This is the signed upper-set formula from A078's previous stage, directly obtained by tagged containment.

Here N=n+1 is even, and f has mass 1/4 at the full set [N]. For each y-coordinate j its immediate predecessor [N]\{y_j} has mass c^2/4 and odd size. Its only strict superset is [N], which has even size. Each such row contributes

 (c^2/4)log2(1+1/c^2)

to (3). The other immediate predecessor [N]\{a} has mass 1/4 and contributes exactly 1/4. All remaining terms in (3) are nonnegative. Consequently

 d(f)>=1/4+(nc^2/4)log2(1+1/c^2).                               (4)

The elementary central-binomial bounds

 1/(4r)<=c^2<=1/(r+1), r>=1,                                   (5)

give the useful explicit estimate

 d(f)>=1/4+(1/8)log2(r+2),
 d(f)/I_z(F)>=1/2+(1/4)log2(r+2) -> infinity.                    (6)

For completeness, c_1=1/2 and c_(r+1)/c_r=(2r+1)/(2r+2). Induction preserves the lower bound because (2r+1)^2>=4r(r+1); it preserves the upper bound because (2r+1)^2(r+2)<=4(r+1)^3. These differences are 1 and 3r+2 respectively. All denominators are positive. The lower coefficient nc^2/4>1/8 and log(1+1/c^2)>=log(r+2) yield (6). This proves divergence without a numerical fit, a limit exchange, or a CLT.

## 3. Both full padding children and the sign of the drift

At z=+1 and z=-1 the actual children are f and its physical input translation. Their complete squared spectra and U agree. Thus the exact signed query decrement is

 D_z U(F)=U(F)-(U(F_z+)+U(F_z-))/2=-d(f).                        (7)

Both full terminals remain present. Equation (6) refutes EVERY finite K in

 |D_z U(Lh)|<=K I_z(Lh), or d(h)<=K I_z(Lh), for all Boolean h.

It does NOT refute a one-sided inequality D_z U<=K I_z: this particular decrement is negative. Replacing it by an absolute value or renewing this discount as independent credit would change the problem. All occupied rows of F have even cardinality, so all physical queries have zero erasure and nonpositive D_i U. The actual first nonzero-erasure positive-correction witness from the previous stage remains a separate result.

This family sharpens the previous tensor example: disjoint repetition there accumulated a constant correction per added influence; here ONE padding bit has fixed influence and an unbounded discount. The cause is concentration of supersets at a full-set coefficient after multiplication by a character. No FEI bound is disproved; the original core influence in (1) is essential.

## 4. Exact finite-sum H,U,G formulas for all parameters

The following formulas specify the full metrics, including mean rows; (4)-(6) use only their top layer. For odd k define

 m_k=(-1)^((k-1)/2)c binom(r,(k-1)/2)/binom(2r,k-1).

This is the Fourier coefficient of majority at every k-set. To see this, choose j in the set and differentiate majority in y_j. The derivative is the indicator of the balanced slice on 2r coordinates. On that slice the average product over a fixed 2t-set is (-1)^t binom(r,t)/binom(2r,2t): expand (1-z)^r(1+z)^r=(1-z^2)^r and average over the chosen subset. Multiplying by the slice probability c gives the formula. Even coefficients vanish by oddness.

For even l=0,2,...,n-1 put b_l=m_(n-l)^2 and

 A_l=sum_{t even,l<=t<=n-1}binom(n-l,t-l)b_t.

All b_l,A_l are strictly positive. Then

 H(M_n)=-sum_{k odd}binom(n,k)m_k^2 log2(m_k^2),
 U(f)=1/2+(1/2)sum_{l even}binom(n,l)b_l log2((1+A_l)/b_l),
 d(f)=1/4+(1/4)sum_{l even}binom(n,l)b_l log2(1+1/A_l),
 U(F)=U(f)-d(f).                                                (8)

Indeed f has mass 1/4 at each (a-bit,all-y), and mass b_l/4 at each (a-bit,R) with |R|=l even. The a-bit is an independent fair spectral coordinate. Counting its full upper sets proves (8) and includes every row.

For the complete G, set t_s=b_(s+(s mod2))/4 for 0<=s<=n-1, and

 W_s=sum_{t=s}^{n-1}binom(n-1-s,t-s)t_t.

After deleting one y-coordinate from F, BOTH children have the same squared spectrum. At each remaining y-set S of size s the auxiliary pair (a,z) has occupied diagonal rows (0,0),(1,1), each of mass t_s. At the full remaining y-set there are also the two off-diagonal rows, each of mass 1/4. Their upper-set masses are 2W_s+1/2 for (0,0), W_s for (1,1), and W_s+1/4 for either off-diagonal row. Therefore their common complete potential is

 U_y=sum_s binom(n-1,s)t_s[log2((2W_s+1/2)/t_s)+log2(W_s/t_s)]
      +(1/2)log2(1+c^2).

Swapping the a and z spectral coordinates preserves the full parent law. Since these queries have zero erasure, their child laws are the injective projections and depend only on that law. Thus D_a U=D_z U=-d(f). Permutation symmetry of y gives the EXACT formula

 G(F)=-2d(f)+n[U(F)-U_y]<=-2d(f).                              (9)

The inequality follows from upper-set mass increasing under an injective zero-erasure projection. It is not an empirical sign. Equations (1),(2),(8),(9) specify analytic I,H,U,G for every r>=1. The r=0 boundary is also valid for these finite formulas, but the lower bound (5) is stated only for r>=1.

## 5. Universal gap and failure checks

The proof is checked against the following possible failures: parity of N; which full-set row survives multiplication by a character; every physical influence, including z; positive denominators in (3),(5),(8); both full child potentials; top-layer containment; exact majority coefficients; r=0 and r=1; and the distinction between an absolute charge and signed GU. Finite certificates check all complete spectra and metrics for fixed r=0..4; they do not supply the all-r argument, which is above.

The first unpaid universal line is to price a NECESSARY selected nonzero-erasure query using UNUSED ORIGINAL core and padding capacities, retaining the old signed discount and BOTH full terminal U. A076's shared-only selector obstruction and A077's arbitrary-event source equivalence concern related but different bills. None permits spending d(f) as a new influence source. An independent review of A077's event-source reduction is recorded separately; it is not assumed to prove this family.
