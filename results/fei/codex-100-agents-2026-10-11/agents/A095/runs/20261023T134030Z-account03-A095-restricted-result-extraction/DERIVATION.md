# Two unqueried padding bits suffice for supplied-owner source-first floor paths

Author proof, independent review pending. Uniform Boolean cubes, normalized
Walsh coefficients, base2 complete-reference costs. Full FEI remains OPEN.

## 1. A dimension-uniform floor-divergence bound without quantization

Let g be ANY Boolean function on a>=0 source bits, with m>=2 padding bits
and one fair selector. Translate/output-negate to make the edited point0 and
g(0)=1. Put n=a+m, epsilon=2^-n, u=2^-m. Reverse g at the full zero point
of all n+1 inputs. If A_S is its padded source Fourier coefficient, the
actual data-frequency marginal is

 q_S=(A_S-epsilon)^2+epsilon^2.

Prescribe the normalized exact-source floor

 R_S=(A_S^2+3epsilon^2)/(1+3epsilon),

lifted by the TRUE conditional selector-frequency law. Call the full model
Qfloor. Its complete divergence is EXACTLY Dfloor=D(q||R), since the true
conditional kernel cancels in the likelihood ratio. All data fibers are
positive. There are M=1/epsilon data masks; at most N<=2^a=u/epsilon have
nonzero A. Also sum A^2=1. Constants and a=0 are included directly.

For EVERY data mask, including A=0,

 (q-R)/sqrt(R)=
 [3epsilon A^2-2epsilon(1+3epsilon)A
       -epsilon^2(1-6epsilon)] /
 [sqrt(1+3epsilon)*sqrt(A^2+3epsilon^2)].

Use (x+y+z)^2<=3(x^2+y^2+z^2), then sum ALL masks. The three denominator
sums are bounded respectively by1, N and M/(3epsilon^2). Consequently

 chi2(q,R) <= epsilon *
  [27epsilon+12u(1+3epsilon)^2+(1-6epsilon)^2]/(1+3epsilon).

Since u<=1/4 and epsilon<=u, the bracket quotient is at most

 [4+33epsilon+63epsilon^2]/(1+3epsilon)
 =4+21epsilon <=37/4.

Normalized KL obeys D2<=log2(e)*chi2, from ln x<=x-1. As ln2>2/3,

             Dfloor < (111/8)epsilon.                 (1)

If chi2=0 the strict positive right side still applies. This bound uses no
minimum nonzero Fourier coefficient and no influence bound. It therefore
avoids A086's quantization-dependent m>=8 admission argument. It is coarser,
and does not assert A086's strictly positive canonical-to-floor lower bound
at m2. The true conditional selector cost is retained, not discarded.

## 2. Actual incoming models and the stronger complete-query-release bill

Let Qincoming be ANY actual finite-cost subprobability model of this SAME
Boolean residual, covering its true support. Complete divergence includes
the mass penalty and is nonnegative: D(P||Q)>=-log2(sum Q)>=0.
At ORIGINAL physical reach lambda, the actual signed replacement charge is

 e=lambda[Dfloor-D(P||Qincoming)],
 p=max(e,0)<(111/8)lambda*epsilon.                     (2)

No source model, Boolean target, old model mass or sibling is renamed.
In particular (2) applies after actual mass-preserving physical inheritance,
not only to a canonical incoming reference. The signed charge can be negative;
we do not reclaim it as credit.

At each physical query retain its FULL complete CE release, computed from the
current parent and actual inherited children before child resets. Such releases
are nonnegative: entropy contracts, and full divergence contracts by likelihood
disintegration with both actual normalizers. For normalized parent mass1,
raw_b=r_marg P_b/p_marg on true-positive fibers, raw_b=r_marg on true-zero
fibers, Z0+Z1=2, child=raw_b/Z_b. More generally preserve parent mass s by
child=s raw_b/Z_b, Z0+Z1=2s and log normalizer Z_b/s.

On true fibers P_b/Q_b=(p_marg/r_marg)(Z_b/s). Thus parent complete D minus
average child complete D equals conditional spectral KL minus the average
log2(Z_b/s), which is nonnegative by Z0+Z1=2s and log concavity. Parent
entropy minus average child entropy equals queried-membership conditional
entropy plus JS(P0,P1), also nonnegative. These two identities prove the
claimed complete-release sign, retaining every true-zero reference fiber.

Let Bfull be all these reached COMPLETE query releases plus ALL current
terminal CE, including every complementary sibling. Exactly

 Bfull=CE_original+sum actual signed reset e
       <=CE_original+sum positive bookings p.          (3)

The entropy-release ledger H(root)+E terminal complete D is <=Bfull.
Neither negative reset charges nor physical divergence releases are needed
to pay the claim below. Independent untouched terminal references retain
their entire additive cost and do not finance this account.

## 3. Whole source path, including the constant endpoint

At root source dimension a, install the exact-source floor and then query
distinct SOURCE coordinates only along the edited zero path, in any adaptive
order. All m>=2 padding bits and the SAME fair selector stay unqueried.
Every unmatched sibling keeps its actual inherited complete model (it may
undergo further inherited-only queries). After each matching query prescribe
the exact-source floor of its ACTUAL remaining source. If d<=a source bits
are queried, depth k has reach lambda*2^-k and epsilon_k=2^k epsilon.
Equation(2) gives, BEFORE taking any later credit,

 sum_(k=0)^d p_k <(111/8)(d+1)lambda*epsilon.          (4)

At k=a the source is a zero-dimensional constant, but m padding bits and the
selector remain; section1 covers it directly. For a nonconstant original
source, the cube edge cut has at least a edges, so I_g>=2a2^-a. A short
induction proves the cut bound: two nonconstant sections have at least
2(a-1)>=a edges; one nonconstant section contributes a-1 plus a cross edge;
two opposite constant sections have2^(a-1)>=a cross edges. The a1 case is
immediate. Thus for a>=1,

 sum p_k <(111/8)lambda*2^-m I_g
          <=(111/32)lambda I_g.                       (5)

This spends ORIGINAL I_g once. No positive descendant influence is assumed.
For constant original sources (4) remains valid; (5) is not asserted.

## 4. Same actual original owner, full old U, m>=2

Supply any nonconstant original source g and a reference R0 of mass s in(0,1],
finite c=CE(P_g,R0)<=C0 I_g, C0>=0. Fix K=4C0+15 ONCE. The initial model
is A011's ACTUAL supplied-source floor

 M0=(R0 padded+3epsilon U_n)/(1+3epsilon),

lifted by the true selector kernel. It is not equated with the new exact-source
floor. The entry in (4) pays its actual conversion, including its mass change.

For completeness its full root cost obeys CE0<=2c+15epsilon(n+1).
Indeed q<=2P_g+3epsilon^2 pointwise and all M0 log losses are nonnegative.
M0>=R0/(1+3epsilon) and M0>=3epsilon^2/(1+3epsilon) yield data CE at most
2c+(2+3epsilon)log2(1+3epsilon)+3epsilon(2n-log2 3).
Here n>=3 and epsilon<=1/8, so the middle term is <11epsilon. The true
selector-frequency mass is epsilon, and its conditional entropy is at most
h2(epsilon)<=epsilon(n+3/2). Therefore full CE0 is at most
2c+(7n+25/2)epsilon<2c+15epsilon(n+1).

Let d0 be g's ORIGINAL pivotal degree at0, E=epsilon*d0 and
G=epsilon(n+1-d0). Literal edge counting gives I(F)=I_g+G-E.
The d0 incident cut edges imply I_g>=2d0*2^-a, hence E<=2^-m I_g/2<=I_g/8.
It follows, with the actual original root still in force, that

 K I(F)-CE0 >=[(3/2)C0+45/4]I_g+4C0 G.

Retain ANY compatible old debit0<=U<=(C0+37/8)I_g. After this ENTIRE old
booking, root unused quota is at least[(1/2)C0+53/8]I_g+4C0G. Perform the
new source-FIRST policy of section3 at this actual root, without undoing any
previous padding-first history. By (3),(5), at EVERY intermediate frontier,

 K I(F)-U-Bfull >[(1/2)C0+101/32]I_g+4C0 G>0.          (6)

The same bound holds for the smaller entropy-release ledger. Every complete
query release, old positive booking and BOTH full terminals remain charged.
The original R0,C0,K are unchanged; no exact-source descendant certificate
is issued. Later inherited-only queries preserve the price.

## 5. Honest scope and universal gap

This extends arbitrary-source positive-part floor-path payment from unqueried
padding>=8 to padding>=2. It is a SAME-owner supplied-reference theorem;
an arbitrary initial influence-paid reference remains an unproved hypothesis.
The source-path subtheorem does not undo an already executed padding-first
path, certify m0/m1, pay arbitrary off-path resets, or create new Boolean edits.
It does not supply A086's positive canonical-conversion lower bound at low m.
The prior A095 rate4 canonical chain and A011 fresh-control v4 construction
are not identified with this new root/history.

A011 v4's fresh-control summability and its fixed-ambient positive-sum parity
obstruction were read as context, not independently accepted by this result.
This stage changes the floor-divergence estimate, not the representation primitives.

## 6. One paid prescribed reset AFTER actual selector exposure

We can sharpen(4) enough to fund this structural change. Section1 actually
proves Dfloor<(6+(63/2)epsilon)epsilon. Summing at source depths0..d<=a gives
total positive source-floor bookings less than

 lambda*epsilon[6(d+1)+(63/2)epsilon(2^(d+1)-1)].

Use the full a-depth sum as an upper bound, epsilon=2^-a*u and
I_g>=2a2^-a. Because(a+1)/a<=2 and(2-2^-a)/a<=3/2 for a>=1,

 source-floor positive total / I_g
 <lambda[6u+(189/8)u^2] <=(381/128)lambda.            (7)

For the second ratio a1 is equality; at a>=2 the numerator is<2<=3a/2.
This is an analytic sum, not a sampled coefficient.

At ANY chosen source prefix d, query the SAME unqueried selector using its
CURRENT installed exact-source floor. The edited physical child0 has
data-only Boolean function h-2*1_(all remaining data zero), where h is the
actual residual source with h(0)=1. There is NO fair selector left in that
child. Its actual squared Fourier law is q'_S=(A_S-2epsilon_d)^2.
Prescribe the genuinely data-only normalized model

 R'_S=(A_S^2+4epsilon_d^2)/(1+4epsilon_d).

Keep the unedited selector child1 with its ENTIRE actual inherited model.
Do not apply the point-selector formula to the edited data-only child.

For clarity write e=epsilon_d and u=2^-m. The exact difference is

 (q'-R')/sqrt(R')=
 [4e A^2-4e(1+4e)A+16e^3]/
 [sqrt(1+4e)*sqrt(A^2+4e^2)].

The same three-term square bound, summed over ALL data masks, gives

 chi2(q',R')<=e[48e+48u(1+4e)^2+192e^2]/(1+4e)
            <=12e(1+8e)<=36e,

since u<=1/4 and e<=1/4. The factorization is
12+144e+384e^2=12(1+4e)(1+8e). Thus

 D(q'||R')<54e.                                    (8)

Both laws normalize by sum A=1,sum A^2=1; constants at a_residual0 are
included. Formula(8) does not assume this is still a point-selector law.
The incoming reference is the ACTUAL physical child inherited through the
selector query, and its complete D is nonnegative. Hence the actual positive
reset debit is <(lambda*2^-d/2)*54epsilon_d=27lambda*epsilon.
For nonconstant original g its ratio to I_g is <=27lambda*u/(2a)<=27lambda/8.

At original root lambda=1 the combined positive new charges, INCLUDING all
old source-floor entries AND the new selector-child reset, therefore total

 <(381/128+27/8)I_g=(813/128)I_g.

The ORIGINAL owner after FULL old U had at least[(1/2)C0+53/8]I_g+4C0G.
Since53/8-813/128=35/128, every intermediate frontier, including the final
post-selector reset, obeys the stronger complete-query-release reserve

 K I(F)-U-Bfull >[(1/2)C0+35/128]I_g+4C0G>0.          (9)

No old debit, complete release or full terminal has been refunded. No new
controller, Boolean construction edit or source certificate is issued.
An actual positive reset is not assumed: signed charges are computed from
current inherited models, and positive parts alone are conservatively paid.

## 7. First remaining universal line

This closes ONE explicitly prescribed data-only reset after selector exposure,
for arbitrary supplied source and m>=2, at the actual diminished original owner.
It does not certify arbitrary further data-only/padding resets, m0/m1,
new interacting Boolean edits, or an arbitrary-core influence-paid initial
reference. NEXT should retain this post-selector model and original account
and test the necessary next data-only conversion, or replace the initial
source premise by a noncircular whole-set supplier. Inherited-only queries
are already paid. Universal FEI remains OPEN.
