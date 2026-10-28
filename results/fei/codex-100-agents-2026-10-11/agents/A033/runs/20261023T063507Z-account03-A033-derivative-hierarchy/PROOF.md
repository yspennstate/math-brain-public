# Full-Boolean, FEI-hard zero-refund windows

Entropy, CE and KL are in bits. Physical cubes are uniform and independent.
This is an obstruction to a specified local refund/reset supplier, NOT a
disproof of FEI. No universal initially influence-priced source is assumed.

## 1. Arbitrary core and exact complete hierarchy

For ANY Boolean g on n>=1 bits and an integer L>=2, introduce n disjoint
blocks X_j of L fresh physical bits and define

  h_L(x)=g(y_1,...,y_n), y_j=product_{v in X_j} x_v.       (1)

This is an actual Boolean function, with ALL signed-convolution identities
sum_S hhat(S)hhat(S xor U)=1{U=empty}. Every physical restriction is
Boolean and hence satisfies the complete split hierarchy AB=0,A^2+B^2=1.
The full alternating derivative averages therefore have their true grids
2^(1-|T|)Z intersect [-1,1] for every nonempty T; no grid is substituted
for Booleanity. Fixed-order/dyadic/atom-cap/square-defect controls are
imported no-go routes, not new admission hypotheses here.

For J subset [n], let phi(J)=union_{j in J}X_j. The COMPLETE Fourier
expansion is

  hhat_L(phi(J))=ghat(J), hhat_L(T)=0 off this image.      (2)

Thus H(h_L)=H(g) and I(h_L)=L I(g). For every FIXED L, FEI on the entire
class (1) is equivalent up to the fixed factor L to full FEI: a uniform
C bound on (1) implies H(g)<=CL I(g) for EVERY Boolean g; full FEI of
course bounds this subclass. This is a hardness statement, not an
unbounded-ratio family. No benign special class of cores is selected.

## 2. Arbitrary adaptive physical prefixes before a block is completed

Allow any adaptive physical restriction history at which EVERY block
still has at least one unqueried bit. Let r_j be its remaining sizes,
eta_j the product of already exposed values, and phi_s(J) the union of
remaining bits in J. Then exactly

  h_s=g(eta_j product_{v remaining in X_j}x_v : j in[n]),
  hhat_s(phi_s(J))=ghat(J) product_{j in J}eta_j.          (3)

Consequently its FULL squared spectrum is a relabeling of ghat^2; its
mean stays ghat(empty), H(h_s)=H(g), and

  I(h_s)=sum_j r_j Inf_j(g),
  Inf_v(h_s)=Inf_j(g) for a remaining v in block j.       (4)

Consider a query in a block with at least TWO bits remaining. Each
frequency fiber {T,T+v} contains at most ONE image atom, because all
remaining bits of that block occur together. The two actual child
squared spectra are identical to the marginalized parent law. Thus

  B_v(h_s)=0, JS_v(h_s)=0, H(parent)-mean H(child)=0.      (5)

Nonzero physical influence does not force any of these refunds to be
positive. In particular EVERY adaptive tree of depth at most D has this
property at all of its queries whenever L>D. The leaves still retain
the arbitrary original core's ENTIRE entropy, not an empty terminal.

## 3. Arbitrary nonflat inherited source; coherent wrapper also stalls

Let p=ghat^2, mu=E g, r=mu^2. Supply ANY normalized core reference R
with R(empty)=r and finite CE(p,R), including reference-only atoms and
arbitrary nonflat conditional nonempty profile. Push R forward by
phi_s to obtain R_s, never removing old reference-only atoms. Both
children use exactly the current frequency marginal. The same at-most-
one-atom fiber property holds for R, including its reference-only atoms.
Therefore physical conditional occupancy KL rho is EXACTLY zero, and

  CE(h_s,R_s)=CE(g,R), D(p_s||R_s)=D(p||R).              (6)

This is not a claim that R was cheap: its full arbitrary core liability
survives unchanged. Taking R=p is an allowed, particularly strong boundary.

For disjoint complementary controller rows A,B, AB=0,A^2+B^2=1, put
beta=E B^2 and G_sigma=A+sigma B h_s (both actual tag children). Use
the admitted CURRENT coherent reference

  Q_sigma(U,empty)=(Ahat(U)+sigma mu Bhat(U))^2,
  Q_sigma(U,phi_s(J))=Bhat(U)^2 R(J), J nonempty.         (7)

It is normalized because sum_U Ahat(U)Bhat(U)=0. When the queried block
has at least two remaining bits, the true seed singleton coefficient
AND its reference mass vanish. The parent and both child vacuum atoms
are identical. Tail masses beta(1-r) are also identical. Hence the FULL
controller-vacuum-plus-tail coarse laws of A033 are IDENTICAL, not just
equal in scalar occupancy. The complete coarse calibration refund is0.
The full wrapper query erasure, JS and conditional occupancy KL also
vanish; CE(G_sigma,Q_sigma) is unchanged at BOTH full children. Its
physical influence in that query is beta Inf_j(g).

These conclusions hold for arbitrary supplied nonflat R, not merely a
true-spectrum reference or the parity example. They include A079's
actual four-controller mask. Nothing refutes A096's phase-funded rule:
its singleton d is0 and it correctly authorizes epsilon0. The theorem
rules out upgrading that current-query rule by claiming a hidden
uniform positive refund on arbitrary Boolean cores or bounded lookahead.

## 4. A necessary profile change may have positive exact local cost

Take nonconstant g, beta>0, and at a query retain at least TWO bits in
one block AFTER the query; e.g. L>D+1 for a depth-D window. A singleton
remaining frequency in such a block lies outside the image phi_s. Use
that point as a prescribed new conditional nonempty target S. With
0<epsilon<1, form N=(1-epsilon)(R_child)_tail+epsilon S.
This genuinely changes the profile; all old reference-only atoms retain
their weight1-epsilon. Since S is disjoint from EVERY occupied actual
tail atom, the exact FULL CE increment of this reset is

  beta(1-r) log2(1/(1-epsilon)) >0.                     (8)

Equation(8) retains all signed vacuum atoms and both complete child
terminals. Every current-query refund in sections2--3 is zero. A prior
ancestor bank may still pay this bill; the present theorem does not
discard or refute such a bank. It says that a prescribed conversion
cannot be called a free calibration of the CURRENT inherited reference.

## 5. No fixed-strength local physical-influence repair

More strongly, for EVERY finite K>=0, a uniform epsilon=1/64 conversion
of the kind (8) is NOT paid by K times that query's ORIGINAL influence,
even after adding ALL of its zero current refunds. Choose g=majority
of 2m+1 independent bits, encoded by (1), and query any one encoded
physical bit before its block is completed. The majority core is
balanced, nonconstant and genuinely nonlinear for m>=1. Thus r=0 and

  Inf_j(g)=a_m=binom(2m,m)/4^m,
  reset cost=beta log2(64/63), query influence=beta a_m.  (9)

The EXACT elementary bound a_m^2<=1/(3m+1) follows by induction from
a_0=1 and a_(m+1)/a_m=(2m+1)/(2m+2): the required polynomial identity is

 (3m+1)(2m+2)^2-(3m+4)(2m+1)^2=m>=0.                 (10)

Also log2(64/63)>1/64: integrate 1/x>1/64 over(63,64)
and use ln2<1. Choose any integer m>=1 with 3m+1>4096K^2.
Then K a_m<1/64<log2(64/63), proving the strict underpayment.
Both physical children, both tag signs, full actual Fourier laws, the
same inherited reference and all prior debits are retained. In particular
K=2,m=8192 and K=4,m=32768 have exact rational sufficient certificates.
This is an actual Boolean route counterfamily for a FIXED reset strength
per query, not an FEI counterexample. The arbitrary target is prescribed,
not proved necessary for every potential universal strategy. An adaptive
strategy can choose no reset or a smaller strength, or use unused ancestor
surplus. The honest universal gap is to show which conversions are
necessary and price them globally, rather than postulate a positive
current refund or universal constant-strength local replacement.

## Boundary and first unsupported line

Completing a block is a real boundary: at a last-bit query the corresponding
core variable is exposed, the image need not have one atom per fiber, and
entropy/phase refunds can appear. This is verified explicitly by a
two-bit point-defect core. No theorem extends the zero-window condition
past that boundary. L is frozen for each family; no dimension escalation
is hidden in a search. The all-D result is analytic, not finite extrapolation.

The first unsupported line of a proposed universal repair is: every
required profile conversion has a dimension-free price from UNUSED
original physical influence across a block-completion/selection tree,
with all old debits and retained arbitrary core entropy included.
No such global selection/payment theorem is proved here. Full FEI stays
OPEN. These fully Boolean examples meet the COMPLETE hierarchy, so
increasing any fixed Booleanity prefix cannot eliminate this obstruction.
