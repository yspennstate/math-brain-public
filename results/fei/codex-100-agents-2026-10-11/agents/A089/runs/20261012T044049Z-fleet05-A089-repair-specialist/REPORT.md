# A089 stage 2: lexicographic limits and the raw composition repair

## exact target, quantifiers, hypotheses and units

Following B18 STREAM_NOTES v2, compute the relevant-coordinate minimum
E(f)=min_i B_i(f)/Inf_i(f) for lexicographic signs near minority measure
1/10, and decide whether raw recursive compositions of the five-bit
t=3 sign can produce growing E(f). All inputs are independent uniform
physical bits, output signs are Boolean, and entropy is in bits.
Write Phi(a,b)=(a+b)h2(b/(a+b)), with continuous zero conventions,
d_i=Inf_i, and B_i=H(S_i|S_without_i) for the squared Fourier law.

Three results are proved locally, pending independent review:

1. For f_n=-1 exactly on numerical indices <floor(2^n/10), every n>=5
has its E(f_n) attained exactly at the three most significant coordinates:

       E(f_n)=psi(2 floor(2^n/10)/2^n),
       psi(d)=2-2d+Phi((1-d)^2,d^2)/d.

   The exact limit is (17 log2 17-56)/5, enclosed numerically as
   2.697373660251154... by the rigorous saved interval.
2. The unqualified limit assertion using only t/2^n ->1/10 is false.
For m>=5, L=m^2, n=m+L and t=2^L floor(2^m/10)+1, the minimum is
attained at the newly relevant terminal coordinates and tends to 2.
Both sequences are actual lexicographic Boolean signs with the same
limiting minority measure.
3. Let F_0=x and F_d=f_5(F_{d-1}^{(0)},...,F_{d-1}^{(4)}), with five
disjoint copies and f_5=-1 on indices 0,1,2. Encode a +1 child as
physical bit 0 and a -1 child as bit 1 at each outer gate. Then
E(F_d)<3 for every d>=1, in physical dimension 5^d. An explicit leaf
path T,B,T,B,... certifies the bound, where T is one of the three high
gate coordinates and B one of the two low coordinates. The complete
finite profiles at depths 1..4 give minima respectively about
2.695887520153101, 2.187135307982910, 2.195676865035359,
2.190922624841381. These decimals are displays; interval endpoints are
the certificates. Raw recursion cannot cross 3.39 or give unbounded E.

Balanced lifts or complemented variants at selected levels are different
families; no conclusion about all such variants is asserted. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-12 04:39 UTC, including the omitted
middle portion in a separate read, B18 STREAM_NOTES.md v2 of
2026-10-11 23:34 UTC, own STATUS.md and LEARNED.md, and the complete
EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Previous
campaign/source/paper reads remain pinned in the first-stage source
inventory; no new whole-manuscript audit is claimed this stage.

Read B18 lead code/lex_check.py for its exact numerical-index convention
and the fact its broad search was float evidence. Read A071 stage-2
REPORT.md, run 20261011T233808Z-fleet05-A071-search-space-design,
which identifies mask 7 and the certified five-bit seed constant.
Read A075 REPORT.md and CLAIMS.json, run
20261011T231030Z-fleet05-A075-search-to-theorem-bridge, for its
balanced-composition scope and singleton correction. This stage
reconstructs the unequal-mean coefficient formula; it does not assume
balanced inner gates after the first recursive level. Read A001 claim
records for its independent acceptance of the r=2k part of A089 stage 1;
the r>2k and A062 portions remain pending review and are not used here.

The scalar Phi calculus, Parseval, and elementary finite-product
expansions below are proved directly. No unverified literature FEI
lower bound is a mathematical premise. The lead's 3.39 suggestion is
only a threshold to compare against. Source paths/hashes are saved in
out/SOURCES.json; full-FEI indices and other agents' trees are read-only.

## complete derivation or exact first unsupported line

### 1. Failed statements and original counterexamples remain visible

The earlier failed every-coordinate helper was

    B_i <= K d_i + A V_post,i + B M_inf,i at every Boolean split.

On the original B05 selector, d_i=2^(-3k), B_i/d_i=k+log2(e)+o(1),
V_post,i/d_i<=4*2^(-k), and M_inf,i/d_i=12k*2^(-3k). Thus all fixed
finite prices fail there. Stage 1 repaired only the existential family
selection, and A001 has independently accepted its r=2k B05 subclaim.
This stage follows the lead's new target rather than repeating that
refutation or converting its root result into a hereditary theorem.

The new candidate statement being corrected is:

    t_n/2^n ->1/10 forces E(lex(n,t_n)) ->2.6974... .

It is correct for canonical dyadic truncations, with the exact constant
below, but false with only that hypothesis. Section 5 gives the actual
Boolean countersequence and its different limit. This was a question
from the lead, not a claim that the lead had already proved.

For composition, the unsupported shortcut would be substituting
f_5 recursively into a balanced-composition identity. The seed has
mean 13/16; at level two its inner gates are biased, so the first
balanced assumption already fails. Section 6 retains that bias exactly.

### 2. Scalar estimates and an exact coefficient ledger

Let c=log2(e). The elementary estimates used are

    Phi(a,b)<=b log2(e(a+b)/b),
    Phi(a,b)>=b[log2(a/b)+c],                        (1)

for positive a,b. The upper estimate is the binary-entropy upper
bound. For the lower estimate write Phi=b log2(a/b)+(a+b)log2(1+b/a)
and use ln(1+x)>=x/(1+x). Also 7/5<c<3/2: the positive atanh series
at 1/3 gives 2/3<ln2<=25/36<5/7. Joint concavity and homogeneity
of Phi give sum_r Phi(a_r,b_r)<=Phi(sum a_r,sum b_r) by log-sum.

For an inner Boolean g with mean mu and singleton coefficient c_i,
define the nonconstant spectral-edge reserve

    R_i(g)=B_i(g)-Phi(mu^2,c_i^2)>=0.

For a physical extension with one constant child c0 in {+1,-1} and
one child g, Fourier pairing gives

    mu'=(mu+c0)/2, c_i'=c_i/2, d_i'=d_i/2,
    R_i(g')=R_i(g)/2+Phi((mu-c0)^2,c_i^2)/4.          (2)

Every nonempty remainder pair duplicates with one-quarter mass.
The empty remainder pair creates the constant packet
Phi((mu+c0)^2,c_i^2)/4 and the nonempty new-coordinate packet
Phi((mu-c0)^2,c_i^2)/4. Removing the first proves (2).
No independence of spectral coordinates is assumed.

For an r-control activation 1+A_r(h-1), p=2^(-r), the same pairing
gives the grouped version

    R_i'=p R_i(h)+(p-p^2)Phi((1-mu_h)^2,c_i(h)^2).  (3)

The empty-core coefficient changes in every control fiber. This is
the correction that mattered in stage 1. Input reflections and output
negation leave the squared Fourier law and each physical influence
unchanged, so (3) applies when h=-g with reflected input variables.

All lex signs and all raw recursive signs here are unate. A derivative
in a fixed coordinate has one constant sign, hence |c_i|=d_i. Put
J_i=R_i/d_i. Equation (2) then becomes the exact nonnegative ledger

    J_i'=J_i+Phi((mu-c0)^2,d_i^2)/(2d_i).            (4)

Unateness here is used to identify the singleton coefficient with
influence, not to assume an FEI bound.

### 3. Closed form for every finite lexicographic coordinate

Let f=1-2*1{sum_i 2^i x_i<t} on n physical 0/1 bits.
For coordinate i, initialize

    alpha_i=(t mod 2^(i+1))/2^(i+1),
    u=1-2alpha_i, d=1-|u|, J=2-2d.

If d=0 the coordinate is irrelevant. Otherwise, for each j=i+1,...,n-1,
with c_j=1-2*(the j-th bit of t), update

    J <- J+Phi((u-c_j)^2,d^2)/(2d),
    u <- (u+c_j)/2, d <- d/2.                       (5)

At the end,

    Inf_i=d,
    B_i/Inf_i=J+Phi(u^2,d^2)/d.                    (6)

This finite sum is a closed expression in t,n and logarithms, requiring
no 2^n truth table. At its initial split, one child is constant and the
other is a residual threshold; the queried influence is d and its
erasure is 2d-2d^2+Phi((1-d)^2,d^2). Thus its nonconstant reserve
is exactly J=2-2d. Each higher bit gives (4), proving (5)-(6).

Integer Walsh transforms and direct physical edges independently
verify this formula on every one of the 120 threshold truth tables in
dimensions 1..6, including irrelevant coordinates and both threshold
orientations. The all-dimensional formula is established by the derivation.

### 4. Canonical truncations: determine the minimum for all n>=5

Define g_m^- as the lex sign with negative support size floor(2^m/5)
and g_m^+ with negative support size ceil(2^m/5). For m>=2, every
nonconstant such gate has mean mu in [1/2,3/4], except the constant
g_2^-, which has no relevant coordinates. The bounds follow from
1/8<=floor/ceil(2^m/5)/2^m<=1/4 in the nonconstant cases; the few
m=2,3,4,5 cases are exact and the general inequalities follow once
2^m/5-1>=2^m/8.

For m>=4, both gates have a leading zero run of length two and

    g_m^sigma = 1+A_2(-g_(m-2)^(-sigma)(reflected inputs)-1).

This follows because complementing the inner interval of size
floor/ceil(4*2^(m-2)/5), then reflecting its inputs, gives the opposite
rounding of 2^(m-2)/5. At a leading control, d=1-mu and J=2mu.

Claim: each relevant coordinate of every nonconstant g_m^sigma,
m>=2, either has d=1-mu and J=2mu, or has J>27/10.
The base m=2,3 gates are point defects on two or three relevant
variables, with possible dummies, and have only the first type.
For induction, a coordinate of the first type in the child has
d=1-mu_child in [1/4,1/2]. By (3), its new nonconstant ratio is

    W(d)=2-2d+(3/4)Phi((2-d)^2,d^2)/d.

Using (1) and c>7/5,

    W(d)>L(d)=2-(19/20)d+(3/2)d log2((2-d)/d).

The function d log((2-d)/d) has negative second derivative, so L is
concave. It is therefore bounded below by the smaller endpoint value:

    L(1/4)=141/80+(3/8)log2(7)>27/10,
    L(1/2)=61/40+(3/4)log2(3)>27/10.

The exact comparisons 7^2>2^5 and 3^12>2^19 prove those signs.
Coordinates whose J already exceeds 27/10 remain so because (3)
adds a nonnegative amount. New leading controls have the first type.
If the child is constant only the new controls are relevant. This
proves the claim. The balanced one-bit child arises only in the
separately checked m=3 point-defect base.

Now a_n=floor(2^n/10), n>=5, is supported only when its top three
bits are zero. Write p=1/8 and m=n-3. After input reflection,
the inner gate is -g_m^+. Its mean is -mu with mu in [1/2,3/4].
Every inner coordinate with J>27/10 retains that bound after activation.
Every coordinate of the other type receives (7/8)Phi((2-d)^2,d^2)/d,
which is larger than the (3/4) correction above. Thus all inner
coordinates have B_i/d_i>27/10 at the outer root.

The top three coordinates are interchangeable activation controls.
Their influence is d=2a_n/2^n, and their ratio is psi(d). For every
n>=5, d lies in [3/16,1/5]. The saved 256-box rational logarithm
certificate proves, on that entire CLOSED interval,

    13/5 < psi(d) < 27/10.                          (7)

Therefore exactly the three top controls minimize. Since d->1/5,
continuity gives the exact limit

    psi(1/5)=(17 log2 17-56)/5.                     (8)

The slight rise then fall in the saved finite profiles is real; the
rounded 2.6974 plateau is not an exact equality at finite n.

### 5. Same limiting measure, different limiting minimum

Let m>=5, L=m^2, a_m=floor(2^m/10), n=m+L, and

    t_m=2^L a_m+1.

Compare f_m on m bits, extended by L dummies, with the new lex sign
on n bits. The new sign flips precisely one vertex, of probability
delta=2^(-n). Thus t_m/2^n=a_m/2^m+delta ->1/10.
Let s=v2(a_m). All L+s previously irrelevant terminal coordinates
become relevant and are interchangeable in the single-point terminal
core of size L+s. Its starting influence is d0'=2^(1-(L+s)), and its
starting nonconstant ratio is 2-2d0'. Above that core there are m-s
extensions of the form (4).

For d<=1/2 and |u|<=1, (1) gives

    Phi((u-c0)^2,d^2)/d <= d[4+2log2(1/d)].

Indeed (u-c0)^2+d^2<=17/4, whose log is <5/2, and c<3/2.
At h extensions the influence is d0'/2^h. Dropping the factor 1/2
in (4), summing sum 2^(-h)=2 and sum h2^(-h)=2, and bounding the
final constant-packet term by d0'[2(L+s)] yields

    2-2d0' <= B_i/d_i <= 2+d0'[6(L+s)+8].

Both right-hand error factors decrease as L+s increases. With
d0=2^(1-L), every newly relevant terminal coordinate therefore obeys

    2-2d0 <= B_i/d_i <= 2+d0(6L+8).                (9)

These bounds tend to 2. It remains to verify that old relevant
coordinates do not become cheaper.

For probability laws on a binary X and arbitrary finite Y, total
variation epsilon gives

    |H_p(X|Y)-H_q(X|Y)|<=h2(epsilon)+epsilon.         (10)

To prove it, write p=(1-epsilon)r+epsilon s and
q=(1-epsilon)r+epsilon t using the common part. Conditional entropy
of each mixture lies between its component average and that average
plus h2(epsilon). The two residual conditional entropies lie in [0,1].
This proves (10) without a dimension-dependent Y factor.

For a one-point sign edit of probability delta, Parseval and
Cauchy-Schwarz give TV(fhat^2,ghat^2)<=||fhat-ghat||_2=2sqrt(delta).
Each coordinate influence changes by at most 2delta by edge counting.
Every originally relevant coordinate has d_i>=2^(1-m), and by (7)
its old ratio exceeds 13/5. Write epsilon=2sqrt(delta), then use
h2(epsilon)<=epsilon log2(e/epsilon). Its new ratio is bounded below
by 13/5 minus an error at most

    2^((m-m^2)/2)[(m+m^2)/2+2]+3*2^(-m^2).        (11)

Here we replaced (26/5)delta by 6delta for the denominator change.
At m=5 expression (11) is <=17/1024+3/2^25<1/10; it decreases
thereafter (the polynomial factor grows by less than a factor two,
whereas its exponential factor shrinks by 2^(-m)). Thus every old
relevant coordinate has new ratio >5/2. The upper bound in (9) is
<5/2 for L>=25. Consequently the exact minimum is attained at the
L+s new terminal coordinates, has the closed sum (5)-(6), and tends
to 2. This is a counterexample to the unqualified limit statement,
not to FEI. Vanishing influence is precisely why dividing a continuity
bound by every coordinate's influence is invalid without a cutoff.

### 6. Biased raw recursive composition: exact coordinate profiles

Let z_j denote a child output sign, and let h=f_5 on five signs with
the bit convention from the target. It is antimonotone and its negative
event is

    (z_2=z_3=z_4=+1) AND (z_0=+1 OR z_1=+1).

For common child mean mu, write p+=(1+mu)/2 and p-=(1-mu)/2.
The next mean and the two derivative probabilities are

    mu_next=1-2 p+^3(1-p-^2),
    q_B=p+^3 p-, q_T=p+^2(1-p-^2).                 (12)

These are actual product probabilities, not biased Fourier influences
on fictitious physical bits. F_d remains unate in its physical leaves,
with orientation (-1)^d, and its singleton coefficient magnitude equals
its physical influence.

Here is the full unequal-mean composition formula. For target outer
block j, write h(g_0,...,g_4)=A(other blocks)+g_j B(other blocks).
For T subset the other four outer coordinates, expand about the mean:

    a_T=sum_{U superset T, j notin U} hhat(U) mu^(|U|-|T|),
    b_T=sum_{U superset T, j notin U} hhat(U+j) mu^(|U|-|T|),
    w_T=(1-mu^2)^|T|, q=sum_T w_T b_T^2.

With an inner coordinate influence d_i and singleton magnitude d_i,

    d_i'=q d_i,
    R_i'=q R_i+sum_{T nonempty} w_T
                    Phi((a_T+mu b_T)^2,b_T^2 d_i^2).           (13)

To prove it, a nonempty spectral remainder within target block j has
both paired coefficients equal to its inner coefficients times Bhat;
their contribution is q R_i. If that block's remainder is empty,
the adjacent pair is (Ahat+mu Bhat,Bhat*c_i). Specifying exactly which
other blocks have nonempty spectra leaves coefficients proportional
to the products of inner nonempty Fourier coefficients. Their squared
mass sums to w_T, proving homogeneity and (13). The T=empty pair is
exactly the new constant packet, removed in R_i'. This is a coherent
coefficient identity; it assumes no balanced child and no disjoint
support within a shared data block. All copies here are physically disjoint.

Equation (13), the mean recursion (12), and

    B_i'/d_i'=R_i'/d_i'+Phi(mu_next^2,(q d_i)^2)/(q d_i)

give closed finite recurrences for all leaf paths. There are 2^d
coordinate orbits at depth d, covering all 5^d leaves. The checker
calculates every orbit for d=1..4. Generic (13), before using |c_i|=d_i,
is independently checked by exact Walsh on all sixteen two-bit
Boolean inner functions, including biased and non-unate inputs;
direct biased-product moments reconstruct all a_T+mu b_T and b_T
at eight separate means, including the actual first three recursive means.

### 7. All-depth bound: raw recursion has a bounded good-coordinate path

Choose the leaf path T at depth one, then B at even ancestor depths,
T at odd ancestor depths. At depth one its ratio is <3. At depth two,
the exact outward certificate gives its full ratio <11/5. Its influence
is exactly

    d_2=(3/16)*(29/32)^3*(3/32)
       =219501/16777216 <1/64.                      (14)

We prove its later accumulated reserve remains bounded. At positive
mean write the minority probability s=(1-mu)/2; initially s=3/32.
The next negative-mean gate has positive probability

    u=1-(1-s)^3(1-s^2) <=3s+s^2 <(25/8)s <3/10.

The next positive-mean minority is

    s_next=u^4(2-u)<=2(25/8)^4 s^4<=s,

where 2(25/8)^4(3/32)^3<1 is an exact rational comparison. Thus this
alternating mean invariant holds at every finite depth. On the selected
path, q_B<=s<=3/32<1/8 and q_T<=2u^3<1/8, so influences shrink
by at least a factor eight at each subsequent level.

For any Boolean coordinate, d_i<=2 times the minority probability:
each pivotal edge in that direction uses one minority vertex. At a
positive mean, q_B=(1-s)^3 s>=(2/3)s>=d_i/3; at a negative mean,
q_T=u^3(2-u)>=u^3>=d_i^3/8. Thus in either state

    q>=d_i^3/8.                                   (15)

The sum of the first mass arguments in (13), including T=empty, is
E(A+mu B)^2=1-(1-mu^2)q by Booleanity of A+gB. The sum of second
arguments is q d_i^2, and their combined mass is <=1 since
d_i^2=c_i^2<=1-mu^2 by Parseval. Log-sum and (1) give a bound on
the normalized reserve increment:

    J_i'-J_i <=d_i log2(e/(q d_i^2))
             <=d_i[5+5log2(1/d_i)].                (16)

This is the line using actual Boolean normalization; arbitrary real
coefficient arrays would not supply the unit budget or variance bound.

At level h>=2, d_h<=(1/64)8^(-(h-2)). The right side of (16)
increases with d in this range. Summing the infinite geometric majorant
therefore bounds every later J by

    J_h < 11/5 + (5/64)sum_{r>=0}8^(-r)(7+3r)
        =11/5+65/98.

For h>=3, d_h<=1/512. The final constant packet has normalized cost
<=d_h[c+2log2(1/d_h)]<=5/128. Consequently

    B_i(F_h)/d_i(F_h) <11/5+65/98+5/128<3           (17)

for h>=3. The exact depth-one and depth-two certificates cover the
remaining cases. All finite means are strictly interior, so the selected
coordinate remains relevant. This proves E(F_h)<3 for every h, with
no finite-to-infinite extrapolation and no use of a balanced-child shortcut.

### 8. Honest boundary of the repair

The canonical lex limit and the raw composition route are now resolved
at their stated all-dimensional scopes. The weaker measure-only limit
is explicitly refuted by a second Boolean lex family. The first
unsupported line toward universal C018 is a coordinate-selection bound
for arbitrary Boolean residuals, or a witness-preserving admission
mechanism controlling every newly relevant low-influence coordinate.
Neither the raw family nor the threshold limit supplies that bound.
The root estimates do not establish restriction closure and cannot
discard any terminal entropy in a C019 application.

## executed validation with domain, arithmetic, commands and outputs

Every job had its own frozen spec saved before execution, estimated
memory <=40 MB, and a 60-second pilot cap. No job required the >300 MB
memory gate; no GPU, automatic dimension escalation, background process,
or other-agent write occurred.

Commands from A089, all `python -X utf8`:

    runs\20261012T044049Z-fleet05-A089-repair-specialist\code\profiles.py
    runs\20261012T044049Z-fleet05-A089-repair-specialist\code\certify.py
    runs\20261012T044049Z-fleet05-A089-repair-specialist\code\validate.py
    runs\20261012T044049Z-fleet05-A089-repair-specialist\code\check_rare.py

Outputs respectively are PROFILES.json, SCALAR_CERTIFICATES.json,
VALIDATION.json, RARE_SEQUENCE_CHECK.json. Observed runtimes were
0.0382, about 0.02, 0.2163, and 0.0344 seconds. The independent small-cube
checker passed 2,991 exact assertions; the rare-family check passed 20;
the final scalar count is saved in SCALAR_CERTIFICATES.json and the
receipt. Finite profile coverage is n=5..24 at canonical truncation,
all 30 orbit paths over raw depths 1..4, and four rare sequences
m=5,6,7,8 (dimensions 30,42,56,72) via the proved recurrence.

Log certificates use 192-bit outward integer bounds. For positive
rational r, range-reduce r=2^e u with 1<=u<2 and z=(u-1)/(u+1)<=1/3.
Use 80 terms of ln u=2 sum z^(2j+1)/(2j+1), whose nonnegative
remainder is <=2*3^(-161)/(161*(1-1/9)). Each multiplication and
division is rounded outward. Separately enclosed positive ln2 converts
the positive unit log, then the exact integer e is added; no signed
denominator reversal is hidden. Phi is evaluated using its two positive
log terms, retaining exact rational weights. Displays converted to
floats are not used for signs. Scalar continuum boxes are bounds on
the whole box, not point samples. Exact prime-log coefficient equality
in the independent Walsh checker verifies identities without evaluating
logarithms or presuming algebraic independence.

## proof dependencies and changed downstream conclusions

One bundled repair claim is created. The derivation is self-contained;
A071 identifies the seed and A075 identifies the balanced-scope pitfall,
but their unreviewed claims are not premises. A089 is a contributor and
cannot independently accept its own repair. The stage follows the
lead-directed repair obligation, not a new broad candidate route.

For B18/A090/A075/B15, the canonical plateau is exactly (8), and raw
seed recursion is eliminated as a mechanism for growing E beyond 3.
For A002/A005/A053, a near-measure or point-edit admission cannot
preserve the minimum coordinate ratio without treating newly relevant
tiny-influence coordinates. Section 5 supplies the concrete missing
guard and section 5's continuity proof supplies the correct influence-
cutoff replacement for coordinates that already carry enough mass.
No existing class constant is promoted to a universal constant.

## one next mathematical action and independent reviewer

Audit a high-erasure witness admission proposed by A002/A005: split
old relevant coordinates from newly relevant coordinates and prove a
fixed-K bound for the latter before using entropy/influence continuity
to transfer an existential obstruction. Use the exact six-bit matching
seed as the initial witness, not a new large census. A090 should
independently reconstruct the lex all-n ordering and the pathwise
all-depth bound; A094 or A075 should challenge the biased Fourier
fiber identity and continuity denominator. No external message was sent.

## actual persistence receipts or precise save blocker

All four protocol files, RESULTS.md, code/, frozen specs and outputs
are saved in this run directory. STATUS.md has exactly STATE/NEXT
lines; WORKLOG.md and LEARNED.md are updated. code/finalize.py checks
required field sets (normalizing the protocol's explanatory annotation
on the actual packet_ids key), statement hash, delta equality and output
success, then writes out/RECEIPTS.json with hashes and sizes. No local
save blocker remains. Supervisor copy, independent acceptance, shared
index adoption and remote mirror verification remain unverified.

## Universal bridge

This stage moves the lead's C018 existential erasure-selection target
by closing the canonical lex plateau exactly, refuting its measure-only
extension with a second explicit Boolean limit, and proving the raw
five-bit recursive mechanism has a uniformly paid root coordinate below
3 at every depth. It establishes no universal B<=KI estimate and leaves
arbitrary-descendant selection and terminal payment open. NEXT attacks
the witness-preserving admission gap exposed by the rare-coordinate
countersequence, using an existing exact high-erasure seed and a fixed-K
test on every newly relevant coordinate; that is the shortest route here
to a valid universal obstruction or repair, rather than another isolated
class estimate or a larger finite census.
