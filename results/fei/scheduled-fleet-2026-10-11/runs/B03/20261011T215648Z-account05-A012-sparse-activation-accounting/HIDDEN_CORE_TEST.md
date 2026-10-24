# Hidden-core admission test

All functions below are Boolean signs on uniform cubes. Entropy is in bits.

## Exact activation, including the selector cost

Let g have mean mu, let A_r be the indicator of one point on r fresh controls, and put p=2^-r and F=1+A_r(g-1). Write a=1-mu, v=1-mu^2 and L(q)=q log2(1/q), with L(0)=0. With the selected control point all positive, the Fourier coefficients are

* Fhat(empty,empty)=1-pa;
* Fhat(U,empty)=-pa for U nonempty;
* Fhat(U,T)=p ghat(T) for T nonempty and every U.

At other control points these last two expressions acquire character signs. Therefore the complete entropy ledger is

H(F)=L((1-pa)^2)+(p-p^2)a^2 log2(1/(p^2 a^2))
     +p[H(g)-L(mu^2)]+2rpv.                                      (1)

Terms containing a=0 are interpreted by continuity. Physical edge counting gives

I(F)=p I(g)+rp(1-mu).                                           (2)

Indeed every data influence is multiplied by p. A control is pivotal when its other r-1 controls match and g=-1, with probability 2p Pr(g=-1)=p(1-mu). The mean is 1-p(1-mu), the minority probability is p Pr(g=-1), and the dimension is n+r before deleting dummy inputs.

For balanced g these specialize, without suppressing the selector cost, to

H(F)=pH(g)+2rp(2-p)+L((1-p)^2),  I(F)=p[I(g)+r].                 (3)

The last two entropy terms are nonnegative. For fixed g, taking r to infinity mostly measures the outer point event; this is NOT the ratio-preserving regime for an arbitrary core.

For an arbitrary nonconstant seed f, instead let g_t=z product_(j=1)^t f(x^(j)), r_t=ceil(2 log2(t+1)), p_t=2^-r_t. Then H(g_t)=tH(f), I(g_t)=tI(f)+1, E g_t=0, and the dimension of F_t is tn+1+r_t. From (3),

H(F_t)/I(F_t)
 = [tH(f)+2r_t(2-p_t)+L((1-p_t)^2)/p_t]/[tI(f)+1+r_t]
 -> H(f)/I(f).                                                 (4)

Here I(F_t)->0 and Pr(F_t=-1)->0. The bound L((1-p)^2)<=2p log2(e) follows from -(1-p)ln(1-p)<=p. Thus the remainder in the numerator is at most 4r_t+2log2(e), explicitly o(t). This reconstructs Proposition 8.9/Corollary 8.10 of the 38-page paper; it is a recovered baseline, not a newly discovered hardness reduction.

## A hereditary admission theorem

Let C be any class containing constants and literals, closed under sign reversal and physical coordinate restrictions. Suppose it is also closed under point activation on fresh controls and disjoint Boolean products. These are precisely the operations used in (4). Then, for every f and every integer t>=1,r>=1,

f belongs to C iff z product_(j=1)^t f(x^(j)) belongs to C
               iff 1+A_r[z product_(j=1)^t f(x^(j))-1] belongs to C. (5)

Forward implications use the stated closures. For the converse activation implication, fix the controls to the selected point. To extract f from the balanced tensor, fix the other t-1 blocks arbitrarily. Their product is a sign c, and fixing z=c recovers f on the remaining block. Restriction closure proves the converse, exactly, with no entropy limit.

In particular a proper class with these closures cannot admit every hidden amplified core. Checking only the rare outer gate is insufficient. Any admission certificate for F_t must, after physical restrictions, certify the original seed. This theorem does NOT claim that all restriction-closed classes satisfy the forward closures, nor that failing one certificate proves a function is outside a larger class.

## An explicit proved admission class

Define R as the functions with a finite formula certificate whose internal gates are AND, OR, parity and negation, whose leaves are original literals or constants, and in which each original variable occurs at most once globally. Every node's child variable blocks must be disjoint; no arbitrary Boolean function is accepted as an opaque leaf. Gate fan-in and depth are unbounded. The global distinct-label check is essential.

R is closed under restrictions (simplify fixed leaves), sign reversal, disjoint substitution, and disjoint product (a parity root). Its activation closure is the explicit formula

F=OR(-ell_1,...,-ell_r,g),

where ell_i is the fresh control literal matching the selected point. Balancing adds a fresh parity input z. These operations keep distinct global labels. Consequently (5) applies to R.

For completeness the known AND/OR/parity gate bound is reconstructed here. Under a product input law with coordinate variances v_i, define corrected entropy

E(f)=sum_(S nonempty) fhat(S)^2 log2(product_(i in S) v_i / fhat(S)^2),
Delta(f)=I(f)-Var(f),   I(f)=sum_S |S| fhat(S)^2.

Biased I here is spectral mean size, not unweighted physical pivotal count. For disjoint substitution F=b(f_1,...,f_m), write V_i=Var(f_i)>0 and c_i=I_i(b)/V_i. Expanding each centered child and using the unique decomposition into disjoint blocks gives exactly

E(F)=E(b)+sum_i c_i E(f_i),
Delta(F)=Delta(b)+sum_i c_i Delta(f_i).                         (6)

Constant children are removed first. The coefficients c_i and all deficits are nonnegative. For a nonempty union S of child sets T_i, the coefficient is bhat(A) product_(i in A) fhat_i(T_i)/sqrt(V_i); squaring this coefficient and splitting the corrected logarithm proves (6).

For a_i in (0,1], put Z=product a_i,
R0=sum_i(1-a_i)-1+Z,
Theta=sum_i(a_i-Z)ln(1/a_i).
The elementary inequality Theta<=2R0 has a complete induction: initially both sides vanish. Appending b changes R0 by (1-b)(1-Z) and changes Theta by

(1-b)Z ln(1/Z)+b(1-Z)ln(1/b)<=2(1-b)(1-Z),

using s ln(1/s)<=1-s. For an OR sign gate set a_i=Pr(input_i=-1). Its nonempty spectral probabilities are

P_S=4 product_(i in S) a_i(1-a_i) product_(i not in S) a_i^2.

Consequently Delta=4ZR0 and, in natural units, E_nat=(ln4)Delta+8ZTheta. This proves E<=C0 Delta with C0=2+4/ln2. Input/output negation handles AND. For parity set a_i=(E input_i)^2. The product spectrum gives Delta=R0 and E_nat=Theta, hence E<=2 Delta/ln2. Zero/boundary parameters follow by continuity or removal of deterministic inputs. Literals have zero corrected entropy and deficit. Equation (6) proves E(f)<=C0 Delta(f) for every R certificate under every product law. This is Lemma 7.5 and its composition consequence from the source, reproduced with no reliance on an unreviewed external claim.

For uniform original inputs E(f)=H_nonempty(f). Also L((Ef)^2)<=log2(e) Var(f), since x ln(1/x)<=1-x. Therefore

H(f)<=C0[I(f)-Var(f)]+log2(e)Var(f)<=C0 I(f),
C0=2+4/ln2<8.                                                  (7)

The last strict bound follows from ln2>2/3, for example the positive series ln2=2[1/3+(1/3)^3/3+...]. Neither this gate constant nor the read-once class FEI theorem is claimed as new. The packet increment is the exact hereditary admission/reflection interface and a concrete exclusion certificate; it replaces an informal root-level rarity test.

## Actual excluded core and why overlap is still unpaid

Let M(x,y,z)=(1+x)y/2+(1-x)z/2. Its Fourier coefficients are 1/2 on {y},{z},{x,y} and -1/2 on {x,z}. Thus H(M)=2, I_x=I_y=I_z=1/2 and I(M)=3/2. This is an easy FEI function, used only to prove R is a proper class.

M cannot be in R. Remove constants and unary gates from a putative certificate. A root on three essential leaves either has three singleton children or has a singleton child and a two-variable child. A three-input AND/OR gate, with any literal orientations/output negation, is unbalanced; a parity gate gives every singleton influence one. At a binary AND/OR root the singleton child is fair. Balance forces the other child to be constant, contradicting essentiality. At a binary parity root the singleton coordinate again has influence one. These exhaust all root possibilities and contradict M's balance and influence vector.

Therefore every point activation of M, and every activated balanced tensor of M, lies outside R by (5). Conversely activations of every admitted core stay in R with the same bound (7). This excludes an arbitrary hidden-core admission rule while retaining arbitrarily rare functions in the class.

Overlap is NOT an allowed closure. In fact M=OR(AND(x,y),AND(-x,z)) in sign-gate notation. Both child formulas are in R, while their OR shares x and produces M outside R. Thus this certificate cannot serve as a universal overlap representation. A011 still needs a quantitative rule that pays the reuse of x, and then the amplified arbitrary-core test must be rerun. No universal FEI conclusion follows.

## New dependency consumed: A011 control-first transcript obstruction

A011's newly completed report was read during finalization (20261011T213831Z-account05-A011-representation-existence, A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT@1, still unreviewed). Its general transcript cost is 2D plus weighted terminal cost and its admission requires I_sel>=gamma D. The following source-independent calculation identifies the admission failure on our precise activation family.

Take the easiest balanced core g=y, and query r fresh point controls sequentially until a mismatch; all stopping leaves are +1, and only the final matching leaf is y. At query j the reach probability is 2^-(j-1). Thus

D=sum_(j=1)^r 2^-(j-1)=2(1-p),
I_sel=rp, I_data=p, I(F)=p(r+1).

All leaf spectral codes have zero cost. A code paying one physical-path bit and one spectral membership bit per reached query therefore has exact expected cost 2D=4(1-p), and

(2D)/I(F)=4(2^r-1)/(r+1)->infinity.                             (8)

The boundary admission ratio is I_sel/D=rp/[2(1-p)]->0. This is an actual Boolean family already admitted by R and is NOT a lower bound on optimal spectral coding cost. Indeed (3) with H(y)=0 gives H(F)=2rp(2-p)+L((1-p)^2)<=4rp+2p log2(e).

There is also a lower bound on the posterior term that any exact witness retaining the full physical leaf label must erase. Let J be that leaf label. Leaf probabilities are 2^-j for mismatch j=1,...,r and p for the terminal leaf, so H(J)=D. If W contains J and exactly decodes S, then

H(W|S)=H(W)-H(S)>=D-H(F)
 >=2(1-p)-4rp-2p log2(e)->2 bits.                              (9)

Thus neither a full latent transcript entropy nor its uncompressed physical-label charge is influence-paid, even for a literal core. Posterior erasure is quantitatively necessary here. The unbounded ratio in (8) diagnoses that specific transcript, not every tree policy or every code. Control-first is explicit; reordering, marginalizing unused physical branches or using a new subprobability reference remains possible. This consumes A011's low-boundary continuation without redoing its transcript proof. It is bundled with the admission theorem as one review package, keeping the current B03 queue at A011 plus A012, subject to reconciliation of any additional live outputs.

## Exact finite certificate

The frozen search evaluates all 256 labelled three-bit truth tables and their 768 activations with r=1,2,3. Integer FWHT and Fraction arithmetic verify every activation coefficient, exact spectrum mass, entropy atom histogram, and physical/spectral influence. The complete read-once class is enumerated by disjoint-support dynamic programming, reducing arbitrary AND/OR/parity fan-ins to associative binary gates. It contains exactly 152 of the 256 functions; all 912 one-coordinate restrictions stay in the class. M is absent. Execution: 5,268 assertions, 0 failures, 0.601 seconds reported by the helper. No floating-point entropy is used as proof. The analytic arguments above supply all-dimensional closure, exclusion and bounds.
