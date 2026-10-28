# Quantitative fine-compatibility invoice, with its old-KL cancellation retained

All laws below are finite complete probabilities; logs in bits unless marked ln.
This is generic reference geometry applied to actual Boolean spectra, NOT a new
Booleanity-admission inequality. Full FEI is OPEN. A required reference class and
an original unused supplier must still be supplied by a universal construction.

## 1. Independent reconstruction of the new frontier

A033 20261023T123045Z DERIVATION sections1-2 considers the ACTUAL midpoint m
of actual child laws p+,p-, and a full-mean compatible pair R++R-=2m with declared
block masses r+,r-. The KL chain rule gives coarse L=mean D(a_tau||r_tau),
a_tau(z)=p_tau(z). Equality forces the ENTIRE conditional reference to equal
the true conditional in every occupied block. Thus on a doubly occupied block
the actual-midpoint criterion is (r+-a+)(kappa+-kappa-)=0 at every atom.
Singly occupied blocks are automatically feasible at this actual midpoint.
The stated 3-bit witness and its boundary minimizer reconstruct without repair.

A035 20261023T132111Z DERIVATION sections1-3 correctly extends the theorem to an
ARBITRARY supplied inherited mean m. On a doubly occupied block equality requires

  r+ kappa+(i)+r- kappa-(i)=2m(i) at every fine atom;             (1)

on a singly occupied block it requires r_tau kappa_tau(i)<=2m(i).
These tests include actual-zero reference-only atoms. The all-m proportional
candidate proves finite feasibility whenever coarse KL is finite. Compactness
and lower semicontinuity justify STRICT separation if a test fails, but do not
alone give a quantitative price. Both statements explicitly declare the mean
constraint; neither asserts that Booleanity or A097 calibration imposes it.

A035's witness p+=(1/4,1/4,1/4,1/4),p-=(0,1,0,0),m=uniform4,
blocks{0,1},{2,3},r+=r-=(1/2,1/2), has global minimizer
R+=(5/12,1/12,1/4,1/4),R-=(1/12,5/12,1/4,1/4). Its gradient is
constant in each block, so the convex supporting plane proves optimality on
the whole compatible class. M=ln(186624/3125)/(8 ln2), L=1/2.
Its actual JS=2-(5/8)log2(5), old marginal mismatch Dold=(5/8)log2(5)-1,
so M-JS>0 but FULL M-JS-Dold=M-1<0. Exact integer comparisons establish both.
This is a genuine fine gap and a false positive debit if old mismatch is lost.

A097 20261023T121505Z PROOF sections2-4 has a DIFFERENT admissible class: a fixed
vacuum and an event floor, with no pointwise full-mean-preservation condition.
Its sharp t*binary-KL floor price follows by log-sum and monotonicity in event
mass. Its all-L controller payment keeps one original35/4 account and the full
old booking. A098 already reviews that payment. We consume its declared-class
scope, not claim another independent review of the whole inherited chain.

## 2. An explicit dimension-free quantitative separation

Assume A035's hypotheses: p+,p- absolutely continuous w.r.t. complete m;
partition z; normalized nonnegative profiles r++r-=2*pi(m); finite coarse KL.
Let M be the minimum mean fine KL over complete pairs with those profiles and
pointwise mean m, and L the coarse lower invoice. In a doubly occupied block set

 e_z(i)=r+ kappa+(i)+r- kappa-(i)-2m(i),
 W_z=r+^2/a+ + r-^2/a-.

In a singly occupied block (occupied sign tau) set

 o_z=sum_i (r_tau*kappa_tau(i)-2m(i))_+.

Then the quantitative bound is

 (M-L)*ln2 >= Phi := sum_double ||e_z||_1^2/(4 W_z)
                       +sum_single a_tau*o_z^2/r_tau^2.        (2)

Zero actual blocks contribute0. Finite coarse KL makes every displayed occupied
denominator positive. All reference-only atoms remain in e, o and normalization.
In particular Phi>0 EXACTLY when one of A035's fine equality tests fails.

Proof: for any feasible pair write E_tau=R_tau-r_tau*kappa_tau in an occupied
block. The KL chain rule subtracts L exactly and leaves mean a_tau times the
conditional KL. Pinsker in nats gives the block excess at least

 (1/4) sum_occupied a_tau*||E_tau||_1^2/r_tau^2.                (3)

For two occupied signs E++E-=-e. The triangle inequality and weighted
Cauchy-Schwarz give ||e||_1^2 <= W_z * sum a_tau||E_tau||_1^2/r_tau^2.
For one occupied sign feasibility R_tau<=2m forces removal of at least o_z
from its ideal law. Since E_tau has zero total in the block, ||E_tau||_1>=2o_z.
These prove (2) for EVERY feasible pair and hence its minimum.

Pinsker itself needs no unverified outside theorem: group the positive part of
P-Q using log-sum. The resulting binary KL d(x||y) has second derivative in x
1/[x(1-x)]>=4; Taylor's integral about x=y gives d(x||y)>=2(x-y)^2.
Since ||P-Q||_1=2|x-y| after grouping, D_nat>=||P-Q||_1^2/2.
Endpoints follow by limits, or infinite KL. This proves the exact constant used.

At the actual midpoint, e=(r+-a+)(kappa+-kappa-), making the signed child
conditional discrepancy explicit. It is essential to form p_tau=(u+tau*v)^2
FIRST; their difference is4uv and Boolean convolution supplies sum uv=0.
Replacing u,v by absolute values before forming the children changes the laws
and can invalidate every price and refund. The bound (2) itself is generic;
it supplies no new F^4=1 admission bound and excludes no normalized real control.

## 3. Optimal universal constant, on an actual positive-influence Boolean query

Take h(y1,y2)=-1 only at the all-plus point, and +1 otherwise. Its four squared
coefficients are uniform1/4. Put f(x,y)=x*h(y), and query x. Both actual child
spectra are that uniform law p, and Inf_x=1. Let 0<s<1/2 and prescribe the
inherited mean m=((1+2s)/4,(1+2s)/4,(1-2s)/4,(1-2s)/4).
Use ONE block, so r+=r-=1 and L=0. Jensen convexity gives M=D(p||m), attained
by both references equal to m. Thus

 M*ln2=-(1/2)ln(1-4s^2), Phi=2s^2,
 (M*ln2)/Phi ->1 as s->0.                                  (4)

The elementary integral bounds z<=-ln(1-z)<=z/(1-z) prove this limit with
z=4s^2. Consequently no multiplier greater than1 can replace the RHS of(2)
uniformly, even restricted to actual Boolean physical child spectra. This
sharpness uses inherited mismatched means and does not claim sharpness if the
mean is required to be the actual midpoint.

The COMPLETE transaction here is ZERO, not M>0: choose parent Q(x-present,T)=m(T),
zero on x-absent. Query occupancy matches deterministically, so refund rho=0;
JS=0, old marginal Dold=M, and B_x=0. Both child references already equal the
carried m, so M-JS-Dold=0. No reset is necessary and no new source is priced.
This sharpness example is a guard against falsely turning a fine invoice into
an unpaid local obligation by omitting the original KL.

## 4. Full transaction and exact first unsupported universal line

Let P be the actual full parent squared law, Q its supplied complete incoming
reference, m its frequency marginal, and a=(p++p-)/2 the actual marginal.
Exact entropy and KL chains give, for a minimum-cost compatible conversion,

 min [B_i+mean CE(p_tau,R_tau)-CE(P,Q)]
       =M-JS-D(P||Q)
       =M-JS-D(a||m)-rho,                                 (5)

where rho is the actual conditional queried-frequency KL, not a fair-bit credit.
Thus(2) quantifies the fine part of M, but pays NO transaction on its own. Every
old debit, physical reach and complementary full terminal must remain. At a
tree, reached full increments telescope against one original owner; no reserve
is renewed by counting another positive fine gap.

First unsupported universal line: specify a model/policy-required admissible
class and prove its full minimum minus JS, old mismatch and actual occupancy
is paid by a genuinely unused influence-priced original source for every core.
Alternatively supply such an original complete reference for every Boolean core.
The fixed-mean class here and A097's floor class are explicit DIFFERENT choices;
neither becomes universally necessary merely from this variational calculation.

For a declared finite adaptive tree, (2) and (5) give a usable same-owner dual
test. At each node put T=L+Phi/ln2-JS-D(a||m)-rho using its CURRENT incoming
reference and actual signed children. Define A=W-U-CE(P_root,Q_root), the
original owner W less all old debits U and the supplied incoming CE. If that
same owner pays every erasure and complete terminal, necessarily
sum_v reach(v)*T_v<=A.
Indeed the reached complete increments telescope to the full terminal bill
plus all reached erasures minus the original incoming CE. Summing the pointwise
lower bounds proves the test. Negative T values are retained; replacing them
by positive parts is not valid. This is a necessary test for that declared
tree/class, not an assertion that FEI requires it.

A useful free-class guard: when BOTH prescribed profiles equal pi(m), the
complete pair R+=R-=m is already admissible, so the minimum net increment is
at most -rho. This applies to BOTH reviewed positive-fine-gap witnesses.
Their strict extra fine KL therefore cannot establish necessary positive
transaction expenditure for that class. It is not necessary to solve the
fine optimizer to see that inherited continuation is admissible.
