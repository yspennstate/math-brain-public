# Free moment calibration and its exact witness cost

All logarithms are base two. The statements concern finite laws and finite uniform Boolean cubes. They do not establish FEI.

## 1. Source-bound repair intake

A050, run 20261027T005654Z, PROOF sections 1--3, correctly reconstructs A096 ghost transport and proves repeated vacuum calibration. Its formula is CE(p,q*)-CE(p,q)=-D(Bern(p0)||Bern(q0)). The true-law coefficient remains positive, nonempty witness slots are scaled, and one empty slot suffices. Both children and old bookings remain in the original account. This is an independent reconstruction of A050's new calibration result, not an independent review of our own earlier transport theorem.

A050's source-registration correction is accepted: its earlier exact claim already contains the occupied hereditary substatement, although that substatement has no separate native ID. A096 stage21's statement that it was unregistered was too broad. The separately adopted statement and proof remain valid.

A094's physical query objection and A011 version 6 distinguish Braw=CEroot+signed resets from Hroot+mean Dterminal. The difference is accumulated query contraction, Qloss. Inherited/vacuum-calibrated descendants pay it from the original root D. Locally reconstructed fresh floors still require their own payment. No new audit of A011's root numerical constants is asserted here.

## 2. Universal free vacuum-and-influence calibration

Let p be any law on subsets of [n] and let Q=s q be a covering subprobability reference, 0<s<=1, with q normalized. Put r=p(empty), t=E_p |S|. Among normalized laws u with u(empty)=r and E_u |S|=t, the information projection of q exists. If 0<=r<1, on nonempty sets it has the form

 u(S)=(1-r) q(S) x^{|S|}/Z(x),  Z(x)=sum_{S!=empty} q(S)x^{|S|},
 u(empty)=r,

where x>0 makes E_u|S|=t. Here the displayed formula uses the unnormalized nonempty masses q(S). The required conditional mean is t/(1-r). Its derivative with respect to log x is the conditional variance, so a unique tilted law exists when this mean is strictly between the smallest and largest q-supported nonempty cardinalities. If the support has only one cardinality, the conditional law is unchanged. At either boundary use q conditioned on that extreme cardinality. Covering ensures p has no mass outside that extreme when its mean is extreme. When r=1 use u=delta_empty. These conventions also cover q(empty)=0 when r=0.

On the positive support, log(u/q) is a constant on the empty cell and an affine function of |S| on the nonempty cell. Since p and u match those two moments,

 CE(p,su)-CE(p,sq) = -E_p log(u/q) = -D(u||q) <= 0.       (1)

At boundary projections the same identity follows by summing on the retained support, which covers p. There is no limit/sum interchange. The full scalar penalty -log s is retained. Equation (1) is the finite information-projection identity, derived here rather than invoked as an unchecked theorem.

For Boolean p=hat(f)^2, t=I(f). Thus matching BOTH the normalized vacuum mass and total spectral influence is free from a supplied reference. Arbitrary physical queries followed by this calibration obey the same full CE inequality as ghost transport, with an additional nonnegative release D(u||q) at every calibration. All finite adaptive histories, old bills and complete leaves stay within the same originally supplied CE. This does not construct or price that source. Re-expanding a covering u as beta p plus individual atoms is always possible on a finite cube, but can require exponentially many atoms.

## 3. An actual Boolean family forces exactly 2^n-n witnesses

For even n>=4 let f_n be the product of n/2 disjoint two-bit signs h(x,y)=1-2*1[x=y=+1]. Each h has four Walsh coefficients of magnitude 1/2. Therefore P=hat(f_n)^2 is uniform on M=2^n subsets, H=n, I=n/2. This is a Boolean family, not a relaxed spectrum. Supply

 q=(P+delta_[n])/2.

It has one witness atom, covers P by P/2, and CE(P,q)<=n+1<=(5/2)I. First vacuum-calibrate to qv. Write c=(M-1)/(2M-1). Then

 qv(empty)=1/M,
 qv(S)=c/M for 0<|S|<n,
 qv([n])=c(M+1)/M.

Its representation is c P+c delta_[n]+(1-c)delta_empty/M: only two witnesses. Its conditional nonempty size mean exceeds the true mean mu=nM/[2(M-1)] because M>2. Apply section 2, retaining vacuum mass. With

 Z_n(x)=(1+x)^n-1+M x^n,
 mu(x)=x Z_n'(x)/Z_n(x),

the unique solution of mu(x)=nM/[2(M-1)] lies in (0,1). Indeed mu(0+)=1<mu and mu(1)=3nM/[2(2M-1)]>mu. The derivative is a strictly positive variance on this support.

In fact x>1/(M+1). To check this without asymptotics put x0=1/(M+1), y=nx0<=4/17 (n/(2^n+1) decreases for n>=4). Since Z_n(x0)>=nx0 and binom(n,l)<=n^l,

 mu(x0) <= 1/(1-y)^2 + M x0^(n-1)
          <=289/169+1/256 <2 <=nM/[2(M-1)].             (2)

The geometric series used here converges since y<1. Also M x0^(n-1)<=M^{-(n-2)}<=1/256. Every denominator is strictly positive. Strict monotonicity gives the claimed root location.

For the calibrated law u the likelihood ratios relative to the TRUE uniform P are

 u(empty)/P(empty)=1,
 u(S)/P(S)=(M-1)x^{|S|}/Z_n(x) for 0<|S|<n,
 u([n])/P([n])=(M-1)(M+1)x^n/Z_n(x).

Because 0<x<1, among the intermediate levels the minimum is precisely |S|=n-1. Because (M+1)x>1, the full-set ratio is larger. The intermediate minimum must be <1: otherwise all ratios would be >=1 and some strictly >1, contradicting normalization against P. Consequently the global minimum is attained on exactly n atoms, the sets of size n-1.

Consider ANY representation u=b P+sum_{j=1}^k a_j delta_Wj, b>0, a_j>=0. Distinct witness locations, not duplicated labels, are counted. Nonnegativity forces b<=min_S u(S)/P(S). If the inequality is strict, every one of the M residual masses is positive. If equality holds, exactly those n minimizing atoms have zero residual. Every other location needs its own atom. Hence

             k_min = 2^n-n.                            (3)

Equality is realized by taking b equal to that minimum and using each positive residual mass. Equation (3) permits arbitrary witness relocation and arbitrary new b, so it is stronger than failure of a particular update rule. The endpoint n=2 is excluded: its tilted law is P, x=1/5, and k_min=0. Nonnegativity of residual weights is an essential hypothesis; signed residuals are a different interface.

## 4. Exact boundary of the advance

Vacuum-and-total-influence matching is a concrete, stronger compatible condition with nonpositive ACTUAL signed CE debit for every covering law. It is not asserted to be necessary for FEI. Even on a family with explicit original rate 5/2 source, it cannot preserve a dimension-independent number of moving atom witnesses. Vacuum matching alone does preserve that count (A050). This separates monetary payment from representation complexity without declaring either a universal obstruction to FEI.

FIRST UNPAID UNIVERSAL LINE: construct an original arbitrary-core complete source at O(I), with a useful noncircular stopping/terminal certificate. If fixed witness count plus moment matching is required, a richer representation than a single true-law component plus finitely many individual atoms is necessary; equation (3) rules out that conjunction in its present form. Permitting exponentially many atoms removes this particular obstruction but does not price H.
