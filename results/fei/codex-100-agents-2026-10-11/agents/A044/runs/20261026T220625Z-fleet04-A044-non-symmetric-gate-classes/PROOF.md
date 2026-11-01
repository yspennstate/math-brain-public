# The sharp singleton reserve can be empty while the prime bill is positive

All logarithms are natural. The physical law is an independent interior product
law unless the uniform law is stated. Contract deterministic coordinates and
constant children. Write P(S)=v_S c_S^2, Delta=I-Var, and
R=sum_{|S|>=3}(|S|-2)P(S). Upper dyadic rounding means
1/2<u_S=2^{j_S}|c_S|<=1. Put J_1=ln4 sum_i P(i)j_i,
L_1=sum_i P(i)ln(1/u_i^2), and

    B_*(f)=ln4(2Delta-R)-J_1-ln2 L_1.

## 1. Independent review of the A041 and A045 source

For the actual physical Boolean derivative D_i=(f_+-f_-)/2 in {-1,0,1},
t_i=|E D_i| and d_i=E D_i^2 satisfy d_i>=t_i. At t>0, set x=1/t.
For its unique cell x in [2^j,2^{j+1}),

    x-1-j-ln(x/2^j)>=0.

The derivative in x is 1-1/x>=0, and the value at the left endpoint is
2^j-1-j>=0. Multiplication by t^2 gives
t^2[j+ln(1/u)]<=t(1-t). Thus, exactly,

    B_*/ln4=sum_i v_i[(d_i-t_i)
                  +t_i(1-t_i)-t_i^2(j_i+ln(1/u_i))]>=0.       (1)

At t=0 the summand is v_i d_i. The dyadic endpoints are included on the
correct side. For alpha>=0 this scalar argument gives A041's sharp bound
J_1+alpha L_1<=max(ln4,2alpha)(2Delta-R). Fair AND2 forces ln4;
AND2 at equal p increasing to1 forces 2alpha. Neither endpoint uses a
zero child variance before its limit.

At a genuine disjoint boundary, the occupied physical blocks give the UNIQUE
label S=(A,(T_i)); c_F=c_g(A)product c_i(T_i). A singleton is exactly
A={i} and singleton T_i. This reconstructs A045's singleton equations

    J_1(F)=J_1(g)+sum a_i J_1(f_i)-T+ln4 C_1,
    L_1(F)+V+ln4 C_1=L_1(g)+sum a_i L_1(f_i).

Here a_i=I_i(g)/Var(f_i); T and V are the actual scale and mantissa imports,
and C_1 is rounding on FINAL singleton labels. Weighted finite telescoping
and the same physical Delta identity give A041's entire tradeoff

 T_tot+J_1(F)+alpha[L_1(F)+V_tot]+B_alpha,tree
   =max(ln4,2alpha)(2Delta_F-R_tree)+(1-alpha)ln4 C_1,tot. (2)

The alpha=0 and alpha=1 specializations recover A045 and A044 respectively.
These are different views of ONE source, not additive new capacity.
High-carry conversion remains
K_flat-K_tree=ln4 C_hi,tot-V_tot+n_F-sum omega n_g. This follows by
substituting K=n-L_hi into the separately partitioned high-mantissa identity.
Both ordinary full terminal laws remain; changing reference replaces its KL.
Verdict: HOLDS at the stated conditional scope; no universal prime payment
is accepted. This review reconstructs mathematics, not the peers' test counts.

## 2. Exact equality in the sharp joint reserve

For every actual finite Boolean f at an interior product law, B_*(f)=0 if
and only if each coordinate is either irrelevant, a literal coordinate
(t_i=d_i=1), or has t_i=d_i=1/2. A nonconstant function with a literal
coordinate is that literal, so every other coordinate is irrelevant.

Indeed every term of (1) is nonnegative and v_i>0. The scalar term can
vanish only at x=1 or x=2: on each cell its derivative is strictly positive
away from x=1, and 2^j-1-j=0 only for j=0,1. Thus t=1 or1/2. At t=0
zero forces d=0. Equality d=|E D| forces the derivative to have one sign
almost surely, since d-|E D|=2min(Pr(D=1),Pr(D=-1)). Interior support
turns this into pointwise unateness. The converse is substitution in (1).
This characterization includes every product bias, not just fair inputs.

## 3. Complete uniform-law classification in every dimension

On the fair cube, after deleting irrelevant coordinates and applying input
and output sign changes, B_*=0 gates are exactly: a constant, a literal,
AND2, and Maj3. The word AND2 denotes a Boolean SIGN gate with one exceptional
corner; its complement includes OR2.

Proof. For a nonliteral gate orient every relevant coordinate positively.
Section2 gives c_i=1/2. Parseval then gives r/4<=1, where r is the number
of relevant coordinates. If r=4, equality forces f=(x1+x2+x3+x4)/2,
which is not Boolean (its value at all-positive inputs is2). Thus r<=3.
One relevant coordinate is a literal. For r=2, monotonicity and relevance
leave the one-corner AND/OR gates; both have derivatives1/2.
For r=3 let A be the upward-closed set of positive vertices. In each
coordinate exactly two of four physical edges cross its boundary.
Consequently the integer Walsh singleton numerators are all4. Let w=|A|.
For each coordinate, the number of vertices of A with xi=+1 minus the
number with xi=-1 is2; hence w is even. Neither w=2 nor w=6 can have
three relevant coordinates: an upward set of size2 is the top vertex
and one neighbor and ignores their differing coordinate; complement and
bit reversal handle size6. With w=4, an upward set either contains a
weight-one vertex, in which case its four supersets form a literal, or
contains exactly the three weight-two vertices and the top vertex. The
latter is Maj3. Sizes0,8 are constant. This completes the all-dimensional
argument; finite enumeration below only checks it.

For n labelled physical coordinates, the exact number of zero-reserve
tables is 2+2n+8 binom(n,2)+8 binom(n,3). AND2 has eight signed variants
on any pair, and Maj3 has eight on any triple.

The corrected high scale satisfies J_hi<=ln4 Delta on this zero-reserve
uniform class, sharply at AND2. AND2 has Delta=1/4,J_hi=ln4/4;
Maj3 has Delta=1/2,J_hi=ln4/4. Constants and literals contribute zero.
The sharper entropy ratios E/Delta are3ln4 for AND2 and2ln4 for Maj3.
This is a restricted classification, not a new universal high-scale bound.

Composition corollary. Suppose every nonconstant gate of a finite disjoint
literal-leaf formula has fair actual induced inputs and B_*=0. Then
E(F)<=3ln4 Delta(F), uniformly in depth and physical dimension: apply the
local bounds above and telescope the genuine Delta composition identity.
On fair physical inputs this gives H_bits(F)<=6 I(F), since
H_nat=E+P(empty)ln(1/P(empty))<=E+Var and 3ln4>1. There is no
per-level factor or fan-in factor. The classification says the essential
local fan-in is at most3; constants and dummies contract. In a reduced
connected formula a non-root AND2 output has mean +/-1/2 and cannot feed
a gate whose actual inputs are fair, so it can appear only at the root.
This explicitly describes the scope; the result says nothing about
arbitrary biased prime gates. It is a consequence of the classification,
not a claim of a new optimal formula constant.

## 4. The unpaid supplier cannot be just the sharp singleton slack

There is NO finite K such that J_hi(f)<=K B_*(f) for all Boolean f, even
on fair two-input threshold gates. Fair AND2 has four masses1/4,
all nonempty c=1/2, J_1=ln4/2, L_1=0 and B_*=0, but J_hi=ln4/4>0.
It also has R=0 and singleton entropy slack
S=4Delta-2R-E_1=1-ln4/2. Thus the remaining original entropy slack is
positive; the counterexample does not refute payment using that larger
account. The stronger shortcut J_hi<=K(B_*+ln4 R) fails on the SAME gate.
Its complete flat reference is P, with n=KL=0; no terminal KL rescues
either proposed shortcut. No existing registered theorem asserting these
shortcuts is refuted here; they are explicit candidate supplier mechanisms.
The quantifier is ALL gates. AND2 is an already understood base gate;
AND_n is decomposable; the Maj3 tower is also decomposable. These witnesses
do not refute a supplier that pays those known components separately and
uses B_* only on the remaining unknown prime gates. The uniform equality
classification actually excludes an exactly zero B_* on any larger
uniform prime, but supplies no dimension-uniform positive margin or
bound for its J_hi/B_*. No obstruction for that exception-aware supplier
is claimed.

The obstruction persists at arbitrary dimension without rounding or KL noise.
In a genuine fair Maj3 tower of depth d, every local B_* is zero, every
coefficient is a signed dyadic power, and C_1=C_hi=V=n=KL=0 at every
boundary and at both full terminals. Let D=(3/2)^d-1. The total original
prime high bill is (ln4/2)D; import is ln4[(3/2)D-d(3/4)^d]; final
J_hi=ln4[2D-d(3/4)^d]. All these identities follow from local
Delta=1/2,J_hi=ln4/4 and total gate weight2D. Hence zero joint slack
does not mean zero original prime obligation, even after all imports and
carries have been accounted for. This family is not a FEI counterexample.

## 5. Exact first unsupported line and next mechanism

An original prime payer must retain capacity beyond B_* (and beyond
B_*+ln4 R). At general product laws, even the zero-reserve class must be
handled using its actual unate pivotal-half structure, or another original
high-sector source. Uniform classification does not extend to arbitrary
biases: the SIGN AND_n at equal p=2^{-1/(n-1)}, n>=2, has every
d_i=t_i=p^{n-1}=1/2 and therefore B_*=0 for arbitrary n. Its normalized
mixed coefficients are c_S=2^{1-|S|}p^{n-|S|}; the factor2^{1-|S|}
is essential. For |S|>=2, its upper dyadic scale is exactly |S|-1,
since 1/2<p^{n-|S|}<=1. Consequently J_hi=ln4 Delta>0 in EVERY arity.
The equality-family obstruction therefore persists for an explicit
non-symmetric product law even without the Maj3 construction. This is a
failure of a proposed source account, not a divergent H/I family.
The next useful step is to determine whether pivotal-half product gates
with positive high scale admit an arity-independent original high-sector
payment, keeping S_tree and both full terminals. Full FEI remains OPEN.
