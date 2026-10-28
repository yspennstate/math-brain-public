# Mismatched inherited means: exact fine-invoice test and a false positive debit

All KL, CE and entropy units are bits. This is generic finite probability
geometry applied to an ACTUAL Boolean physical split; it is not a new Booleanity
admission inequality. Full-mean compatibility below is an explicit additional
route obligation, not a consequence of being Boolean.

## 1. Exact criterion for an arbitrary inherited mean

Let p_+,p_- be complete laws on finite Omega. Supply a complete normalized
inherited mean m with p_+,p_- absolutely continuous with respect to m. For a
partition B of Omega prescribe normalized coarse laws r_+,r_- satisfying
r_+(B)+r_-(B)=2m(B). Require finite coarse KL: r_tau(B)>0 if a_tau(B)>0,
where a_tau(B)=p_tau(B). The admissible fine references obey

 q_+(i)+q_-(i)=2m(i), q_tau(B)=r_tau(B).

The class is nonempty with finite objective: on m(B)>0 set
q_tau(i)=r_tau(B)m(i)/m(B). Empty m blocks are identically zero. This also
retains ALL reference-only atoms. Let L=(D(a_+||r_+)+D(a_-||r_-))/2 and let M
be the minimum of (D(p_+||q_+)+D(p_-||q_-))/2 over this compatible class.
The chain rule gives M>=L. Equality holds IFF all the following block tests hold:

* If BOTH a_+,a_->0, at every i in B,
  r_+ p_+(i)/a_+ + r_- p_-(i)/a_- = 2m(i).
* If ONLY a_tau>0, at every i in B,
  r_tau p_tau(i)/a_tau <= 2m(i).
* If BOTH a_tau=0, there is no additional obstruction.

Proof: equality in each conditional KL forces the ENTIRE reference conditional
to equal the actual conditional on every occupied child block, including its
true-zero atoms. In a doubly occupied block both fine references are thereby
fixed, giving the equality test. In a singly occupied block the occupied
reference is fixed; the other child's reference is the componentwise residual
2m-q_tau, nonnegative precisely under the displayed inequality. Its total is
automatically the prescribed other mass. In a doubly empty block use the finite
candidate above. These constructions prove sufficiency and necessity. The
compact compatible class and lower semicontinuous extended KL have a finite
minimum. If any test fails, that minimum is STRICTLY greater than L. No numerical
lower bound on that strict gap is inferred merely from compactness.

The original A033 actual-midpoint theorem follows when 2m=p_++p_-: the double
test reduces to (r_+-a_+)(p_+/a_+-p_-/a_-)=0. The single test is then automatic.
For a mismatched inherited m, neither simplification is valid. A033 explicitly
excludes that case, so the new test extends its scope and does not refute it.

## 2. Actual Boolean witness and rational global optimum

Use f(x,y)=g(y) if x=+1 and f(x,y)=y1 if x=-1, with g=-1 only when y1=y2=+1.
On labels(empty,{1},{2},{1,2}), the ACTUAL child laws are

 p_+=(1/4,1/4,1/4,1/4), p_-=(0,1,0,0).

Take inherited m=(1/4,1/4,1/4,1/4), blocks {0,1},{2,3}, and prescribe
r_+=r_-=(1/2,1/2). There is NO plus coarse shift in the doubly occupied block,
but the predicted equality references sum to (1/4,3/4) there, whereas 2m=(1/2,1/2).
Thus using the old simplified test outside its hypothesis would incorrectly
declare the coarse invoice attainable. The true coarse invoice is L=1/2.

An exact optimizer is
 q_+*=(5/12,1/12,1/4,1/4), q_-*=(1/12,5/12,1/4,1/4).

Write q_+(i)=x_i and q_-(i)=1/2-x_i. The objective is convex on the box with
fixed block sums. Apart from its positive common factor 1/(2 ln2), its gradient
at the proposed optimizer is

 -p_+/q_+* + p_-/q_-* = (-3/5,-3/5,-1,-1).

It is constant on each block. Its scalar product with every feasible displacement
is therefore zero. The convex supporting-plane inequality proves GLOBAL
optimality, including boundary candidates by lower semicontinuity. This is a
rational KKT certificate, not a floating-point optimizer.

 M=(1/8)log2(186624/3125)>1/2, since186624>16*3125.

## 3. The apparent positive obstruction disappears when old mismatch is retained

The true child midpoint is pbar=(1/8,5/8,1/8,1/8), and
JS=2-(5/8)log2(5), D(pbar||m)=(5/8)log2(5)-1.
Hence JS+D(pbar||m)=1 exactly. If one keeps JS but loses the inherited
mismatch term, the apparent debit is

 M-JS=(1/8)log2(729/256)>0.

But the COMPLETE transaction relative to the incoming marginal reference m is

 E_tau CE(p_tau,q_tau*)-CE(pbar,m)
   =M-JS-D(pbar||m)=M-1<0,

certified by186624<256*3125. Thus this actual Boolean example simultaneously
has a genuine fine-compatibility gap and a SPURIOUS positive net obstruction
if a sign/refund is lost. It does not challenge FEI or A097's payment theorem.

For explicit full-parent bookkeeping, let P be the actual parent squared law,
and take Q(S)=m(T)P(S)/pbar(T), where T removes the queried frequency. Its
conditional query-frequency law matches P; its marginal is m. Every witness
pbar(T)>0, Q is complete and normalized, and its conditional refund is zero.
CE(P,Q)=B_x(P)+CE(pbar,m). Consequently the reached erasure B_x plus both full
child CE invoices minus the full incoming CE is exactly the negative expression
above. No initial influence price for this Q is asserted. For another incoming
conditional law its ACTUAL refund must be measured, not set to zero by analogy.

## 4. Scope and validation

Frozen pilot uses16 labelled Boolean3-bit tables; primary uses ALL256, all15
partitions, three strictly positive inherited means (uniform and two mixtures
of the true midpoint with uniform), and two normalized fine-target templates.
There are23040 primary cases. Integer FWHT is independently compared to direct
character sums; all parent convolution shifts and all signed physical-collapse
identities are checked. Exact rational tests are compared with independently
assembled whole equality candidates, including singly occupied blocks and
reference-only atoms. The finite enumeration validates implementations; the
proof in section1 establishes arbitrary finite dimensions.

This theorem is explicitly generic. An initial source inequality that used only
it would still fail the normalized equal-singleton nonBoolean control; no
Booleanity admission, universal B<=KI helper, or full-FEI proof is asserted.
Optional incompatible targets do not become necessary merely because their
minimum is positive. First unsupported universal line: identify an ACTUALLY
REQUIRED compatible class, specify its incoming full reference and unused
original allowance, and pay its reached minimum minus JS and old mismatch/refund;
or influence-price the arbitrary-core initial complete reference. Keep all
complementary siblings and old bookings. Full FEI remains OPEN.
