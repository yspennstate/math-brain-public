# Representation-free five-control payment and the six-control odd lattice

Uniform Boolean signs; entropy in bits. Put K=4+2/ln2. This is a continuation of A017's existing signed quadratic/shared-address ledger and stopping claim. We prove (i) every nonconstant Boolean phase on at most five physical controls has a relevant K4-good coordinate; (ii) every Boolean six-control coordinate of influence5/32 has B<639/1024<4Inf; and (iii) every quadratic phase with at most eleven coherent edits in one linear-address fiber has zero localized bad-boundary bill and H(F)<=K(I(F)-1). These are restricted results. Full FEI remains open.

## 1. Inherited exact interfaces

INHERITED_CRITICAL_PROOF.md reproduces the six-edit proof, generic four-control coordinate certificate, five-control two-edge certificate, complete sparse/dense terminal lemma, signed crossing ledger and exact phase/fiber identities. DERIVATION.md reproduces the scalar JS proof. INHERITED_STAGE5_PROOF.md preserves the rank-two seven-edit collapse, eight-edit result and the actual fixed-order3/8 obstruction.

For the current actual Boolean F=b(x)(1-2 1_E(x))y_(Mx), b=(-1)^q, a data label is one independent physical coordinate regardless of how often it appears. Coefficients update coherently by -2*2^-n sum_(w in E)b(w)chi_S(w) in its named data row. Active address controls have influence1/2. An inactive polar coordinate has

    Inf_i=1/2+2^(1-n) sum_(w in E,w+e_i notin E)(-1)^(ell_i+(Qw)_i).

Internal edited edges cause no change. The data influence totals1. Entropy decrements along a query are B_i+JS_i, with JS_i<=2Inf_i/ln2. The exact boundary cost is C_i=2 sum_(S,z,i in S)|S|p_(S,z). The tree below never spends it: every queried node has B_i<=4Inf_i.

The complete inherited certificates establish that EVERY coordinate on D<=4 is K4-good; on D=5 every coordinate of influence1/8 is K4-good. Influence0 has B=0. Concavity gives B_i<=h2(Inf_i), and h2(t)/t decreases. The exact integer inequality3^3*13^13>2^52 proves h2(3/16)<3/4. Thus coordinates of influence>=3/16 are also good in every dimension. critical.py and ternary.py rerun all128/2187 normalized certificate cases in this run.

## 2. Every five-control phase has a good coordinate

For every physical Boolean coordinate on five bits, influence is a multiple of1/16. Select a coordinate of maximum influence. If it has influence>=3/16, use section1. If it has influence1/8, use the two-edge certificate.

The remaining nonconstant case has maximum influence1/16. No coordinate can be irrelevant: otherwise the function is a junta on at most four physical variables, whose positive influences are multiples of1/8. Thus all five coordinates have influence1/16. The total influence is5/16, so its negative set has exactly five undirected boundary edges.

For a set of s vertices in a five-cube, edge isoperimetry gives boundary>=s(5-log2 s). Its proof by dimension split is reproduced in INHERITED_CRITICAL_PROOF section4: the internal edge count is at most(s/2)log2 s, using the concave entropy chord. Replace the negative set by its complement if necessary, making s<=16. For each2<=s<=16, the exact integer inequality

    s^s < 2^(5s-5)

shows s(5-log2 s)>5. All15 positive integer slacks are saved by five.py. Therefore s=1, and the actual phase is a point defect or its global negative. Its Fourier entropy is at most4I by the sparse terminal lemma with s=1. Coordinate permutation symmetry makes all five erasures equal; entropy's chain rule gives sum_i B_i<=H. Consequently each B_i<=H/5<=4I/5=4Inf_i. This proves the maximum-influence physical policy is K4-good for EVERY nonconstant five-control Boolean function.

Restrictions have at most four controls, so this policy followed by generic four-control queries gives a finite zero-bad-bill tree and

    H(g)<=K I(g)  for every Boolean g on at most five controls.

No quadratic representation, edit-count hypothesis or fair selector is used in this lemma. The full lemma is analytic plus the complete critical certificates; there is no claim to enumerate all2^32 five-bit truth tables. five.py independently enumerates all32768 normalized four-bit child a with a(0)=1 and b=a flipped only at0. That exhausts the normalized one-pivotal-edge coordinate family. It constructs actual five-bit parents, checks direct edges against its own integer Walsh implementation, chooses maximum physical influence and proves the selected B<=4Inf with an integer-product comparison. The two low-maximum cases are exactly the normalized point defect and its opposite minority sign. A global sign and translation normalize any specified one-edge parent without changing its physical coordinate influences or erasures.

## 3. Six controls, five pivotal edges: integrality pays the concavity gap

Let g be ANY Boolean phase on six controls with Inf_i=5/32. Its selected coordinate has exactly five pivotal undirected edges. The negative-vertex count has the same parity as this edge count (partition the vertices into the32 selected pairs), so it is odd. For every Walsh sum W_s=sum_x g(x)chi_s(x),

    W_s/2 is an odd integer.

Indeed W_s/2=32*1_(s=0)-sum_(g(x)=-1)chi_s(x), whose second sum has odd parity. Write v_s=W_s/2; the actual amplitude is v_s/32. Parseval gives total squared integer mass1024, selected present mass160, and absent mass864. There are32 spectral rows, each with odd integer pair(a,b). At least16 rows have |b|=1: every other row has b^2>=9, while sum b^2=160 and the baseline32 ones leaves only128 extra units. odd5.py enumerates all17 possible magnitude histograms and checks this arithmetic, although the argument itself proves it without a census.

For t=a^2,u=b^2, let Phi(t,u)=(t+u)log2(t+u)-tlog2t-ulog2u. Then

    1024 B_i=sum_rows Phi(t,u).

Joint concavity has the tangent upper bound at present proportion5/32:

    Phi(t,u)<=t log2(32/27)+u log2(32/5).

The sum of these tangents is

    5120-2592log2 3-160log2 5 < 641.

The strict integer certificate is5^160*3^2592>2^4479. In a row with u=1, its tangent deficit is

    L(t)=t log2(32/27)+log2(32/5)-Phi(t,1).

Its derivative is log2[32t/(27(t+1))], negative below27/5 and positive above it. Since t is an odd integer square, the minimum over allowable t occurs at t=1 or9. Exactly

    L(1)=8-log2 135>1/8,
    L(9)=40-9log2 3-11log2 5>1/8.

Their certificates are2^63>135^8 and2^319>3^72*5^88. Every other row has nonnegative tangent deficit. The at least16 magnitude-one rows therefore save more than2, while the tangent exceeds640 by less than1. It follows that

    1024B_i < 641-2=639,
    B_i < 639/1024 < 640/1024=4*(5/32).

This is a generic physical-coordinate theorem. It uses Boolean truth-table parity, not a heuristic spectral flatness or a tolerance on h2(5/32). The analytic monotonicity and exact three integer signs give a checked proof. actual5edge.py additionally constructs4096 actual six-control parents: four quadratic five-control child cores, all32 linear characters and all32 translations of five changed child points. Direct physical influences agree with Walsh masses, at least16 present coefficients have magnitude1, and every parent satisfies the stricter integer comparison for B<639/1024. The finite sample is not the generic proof.

## 4. All-dimensional eleven-edit physical tree

Query address-active physical controls first; their influence1/2 is good. After the address is fixed, stop unedited branches at the actual quadratic phase. On edited branches with D>=6, stop when the restricted polar form vanishes, retaining the character times edit mask. Otherwise query any nonzero physical polar row. For s=|E|<=11,

    Inf_i>=1/2-2s/2^D.

At D>=7 this exceeds1/4. At D=6 it is at least5/32, with all influences multiples of1/32. Influence5/32 is covered by section3; larger values are at least3/16 and covered by section1. Hence these polar queries are K4-good. At D<=5 use the maximum-influence policy of section2, even if its selected coordinate is nonpolar in the old representation. A constant phase can stop immediately. Alternatively one may stop at D<=5 with its complete H<=KI certificate; either convention preserves the terminal ledger.

Each actual query removes one physical coordinate; no branch renews a data reference or charges a reused gate label again. Restrictions preserve the edit-count bound until the representation-free terminal policy is invoked. All queries are good, so the localized bill sum_(B_i>4Inf_i) weight_i C_i is exactly ZERO.

## 5. Complete terminal payment at the same K

Clean quadratic phase leaves have H<=2I_phase. For an affine phase times an s-point mask, with D>=6 and s<=11, put u=s2^-D and L=log2(1/u). Then u<=11/64<1/4, so character multiplication only increases influence. The retained sparse proof gives

    H/I_phase <= 4+2[log2 s+log2 e-log2 3]/L
               <= 4+2log2 s/(D-log2 s).

The second inequality uses e<3; if the bracket correction is negative the ratio is even smaller. Since11^2<2^7, log2 s<=log2 11<7/2 and D-log2 s>5/2. Thus this terminal ratio is below4+14/5=34/5. This sharper dimension-aware payment replaces the older coarse4+log2 s bound; it is why increasing the edit count here does not increase the final K.

The positive factorial series gives exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6=12013/6000>2. Therefore ln2<7/10 and K>4+20/7=48/7>34/5. Every large affine terminal is paid below the access coefficient. Every actual phase terminal on D<=5 has the full certificate H<=KI from section2. No entropy is erased by using a different representation.

Finally, actual influence and entropy telescope along the finite tree. Let A be the weighted queried influence and T the weighted remaining phase influence. The complete named data influence is1, even when many leaves share the same y_z. Therefore

    I(F)-1=A+T,
    H(F)<=K A+K T=K(I(F)-1).

This includes empty through eleven same-fiber edits, arbitrary quadratic linear terms, arbitrary linear address maps and every dimension. Signed Fourier/fiber ledgers from earlier versions remain valid. Earlier seven-edit minimum-index root badness and its3/8 full-tree bill are preserved; this theorem does not claim all polar choices are good on D<=5.

## 6. Honest frontier: twelve edits and even rows

At D=6, twelve edits can lower polar influence to1/8, i.e. four pivotal edges. The present odd-numerator lemma no longer applies: selected parity is even. Integer/Parseval/common-parity constraints ALONE do not pay the necessary row inequality. An abstract normalized row array with8 pairs(a,b)=(1,1) and24 pairs(3,1), denominator256, has present mass32, absent224, influence1/8, and

    B=[16+24*(10log2 10-9log2 9)]/256 >1/2.

The exact comparison is2^128*5^240>3^432. EVEN_RELAXATION_CERTIFICATE.json saves it. This is explicitly an abstract spectral-row relaxation, NOT an actual Boolean family or an FEI counterexample. No signed truth-table realization is supplied. The gap is the missing Boolean row compatibility, not inaccurate logarithms.

Two exact actual twelve-edit tests were run:140 affine-plane-complement edit sets in x0=x1=1 for q=x0x1+x1x2+x3x4, then1680 coupled point-toggle variants that preserve twelve total edits and four pivotal selector edges. Both found zero bad tested root pivots, and maximum-influence full physical trees were good on every tested node. They neither supply the universal four-edge certificate nor refute it. The next unsupported line is a six-control four-edge Boolean compatibility bound B<=4Inf, or an adaptive/owned-terminal repair if that local bound fails. Section7 closes one complete compatibility class. A universal point-count-independent representation and one conserved reserve still remain beyond this finite threshold.

## 7. Complete four-edge certificate for an affine disagreement plane with affine phase

Let a,b be ANY Boolean children on five controls differing at exactly four vertices that form an affine2-plane E. Suppose a restricted to E is an affine sign character. Translate E and make an invertible linear change ONLY of the unqueried controls to write E={(t,z):z=0}, t in F_2^2,z in F_2^3. A common unqueried character and a global sign make a(t,0)=1. These operations preserve selected B_i and Inf_i only. They are NOT used to carry other physical influences or derivative budgets.

Put h(z)=(1/4)sum_t a(t,z), H(z)=2h(z). Then H(0)=2 and every other H(z) is in{-2,-1,0,1,2}. The selector-present coefficients vanish on nonzero t-frequency; on t-frequency zero they are2/16, and the absent coefficients are(WH_s-2)/16, where WH is the eight-point integer Walsh transform of H. Thus selected influence is1/8 and

    256 B_i=sum_s Phi((WH_s-2)^2,4).

There are exactly5^7=78125 normalized quinary projections. Each can be realized by a Boolean child: in each t slice choose2+H(z) of its four signs positive. quinary.py exhausts all of them, computes integer spectra, and verifies

    product_s((WH_s-2)^2+4)^((WH_s-2)^2+4)
        <=2^128 product_s[((WH_s-2)^2)^((WH_s-2)^2) *4^4],

omitting zero exponents. This is exactly B_i<=1/2=4Inf_i, with zero failures. It compares all product ratios exactly to find a maximum; one maximizing profile is H=[2,-2,-2,0,-2,0,0,2] in low-bit-first order. quinary_actual_v2.py reconstructs its actual six-control truth table independently, reproduces the maximum product RATIO and its positive slack, and checks physical first/mixed derivatives against the named-data spectrum. Its influences are[1/8,0,3/8,1/2,1/2,1/2], selected boundaryC=5/8. The v1 checker incorrectly compared raw entropy products; off-selected-frequency rows multiply numerator and denominator by cancelling factors. The v2 cross-multiplication repair and v1 failure record are preserved. No mathematical inequality was changed by that implementation repair.

The remaining four-edge cases are affine-plane disagreement with a genuinely quadratic restriction of a to the plane, and affine-span-three disagreement sets. No generic four-edge bound or twelve-edit theorem is concluded from the closed affine-phase class.

## 8. Quadratic changed plane with all parallel slices bent

There is also a source-complete subcase of the first remaining class. Normalize the phase on E to a two-bit bent quadratic, whose four Walsh/2 signs are sigma_t. For every parallel plane z, assume its four-sign child slice is also bent. Define H_t(z)=sigma_t * Walsh_t[a(.,z)]/2. Then each of the four H_t is a Boolean three-bit sign function with H_t(0)=1. In its selected spectral row the present normalized coefficient is1 and the absent coefficient isWH_t(k)-1, after a harmless row-sign multiplication. Hence

    256B_i=sum_(t,k) Phi((WH_t(k)-1)^2,1).

The complete128-case three-bit child critical certificate says each sum over k is below32. Summing four such bounds gives B_i<128/256=1/2. This closes all parallel-bent slices analytically, without enumerating the2^21 coupled sign choices or pretending that arbitrary independent row words are Boolean. If an unqueried plane slice is affine instead, its four Walsh/2 entries are one signed2 and three zeros; the Boolean three-bit child certificate no longer applies to those four H_t. Those affine-column intrusions, and affine-span-three disagreement sets, remain the precise four-edge gap.
