# Joint orientation/refund rigidity and the exact criticality failure

All cubes are finite and uniform, f takes values +-1, entropy is in bits.
For each coordinate i let beta_i be the sum of the smaller squared Fourier
coefficient in each i-pair and O_i=Inf_i-beta_i. For each pair i,j let R_ij
be the sum of the two A052 merging refunds over all retained Fourier rows.
Define the absolute structural defect

    T(f)=sum_i O_i + sum_{i<j} R_ij.

Every summand is nonnegative. This is a structural diagnostic, not an entropy
price and not a new name for the FEI target.

## 1. Local zero implication reconstructed from signed rows

In a quartet (a,b,c,d), let q=a^2+b^2+c^2+d^2. The exact refunds are

    M_i=4[ab(c^2+d^2)-cd(a^2+b^2)]^2
           /[q(a^2+b^2)(c^2+d^2)],
    M_j=4[ac(b^2+d^2)-bd(a^2+c^2)]^2
           /[q(a^2+c^2)(b^2+d^2)].

Zero denominators give their zero continuous extensions. These are just
weighted variances of two signed products. Subtracting the merged square
from the two separately conditioned squares independently proves A052's
identity C_ij=C_i+C_j+P_ij-M_i-M_j, P=4(ad+bc)^2/q.
The two numerators factor as -(ad-bc)(ac-bd) and -(ad-bc)(ab-cd).

If the quartet has no orientation excess in either direction, then
a^2>=b^2,c^2 and b^2,c^2>=d^2. If both refunds vanish, ad=bc.
Indeed if ad-bc!=0, all relevant variance denominators are positive and
ac=bd, ab=cd. If any coefficient is zero these equations force opposite
diagonal support, contradicted by the downward inequalities. Otherwise
d^2=a^2, c^2=b^2; downward ordering forces all four squared magnitudes
equal, giving ad-bc=0 by the same signed equations, a contradiction.
This implication uses the actual signed amplitudes, not their absolute sums.

## 2. Global Boolean rigidity, including spectral zeros

T(f)=0 implies O_i=0 for every i, so squared Fourier magnitudes are
nonincreasing on every upward cube edge. The empty coefficient a_empty is
therefore nonzero. Every pair refund in every row is zero. Section1 gives
the determinant identity a_S a_(S+i+j)=a_(S+i) a_(S+j) on every face.

Put r_i=a_{i}/a_empty. If r_i=0, downward monotonicity makes every
coefficient containing i zero. For the remaining coordinates, induct on
|S| using a face at S minus two elements; its lower coefficient is nonzero.
The determinant identity yields exactly

    a_S=a_empty product_{i in S} r_i.

Fourier inversion gives f(x)=a_empty product_i(1+r_i x_i). No factor can
vanish at any input because f is Boolean. Fix all other inputs; Booleanity
then forces |1+r_i|=|1-r_i|, hence r_i=0. Thus f is constant.
Conversely constants have T=0. This proves for every dimension:

    T(f)=0 if and only if f is constant.                 (1)

This strengthens the row zero classification only after *both* the global
orientation and refund conditions are imposed. Refund zeros alone do not
imply this conclusion; neither do orientation zeros alone (point defects
provide examples). No virtual component is assumed Boolean.

## 3. Exact finite-dimensional floor and its limitation

For n>=1 Boolean Fourier coefficients belong to h Z, h=2^(1-n).
A positive O_i is at least h^2. A nonzero refund numerator before squaring
belongs to h^4 Z. Its variance denominator is at most1, since q and both
two-coefficient masses are at most1. Hence a positive refund is at least
4h^8=2^(10-8n). For every nonconstant function on n>=2 named coordinates,

    T(f)>=2^(10-8n).                                   (2)

For n=1 a nonconstant sign is a character and T=1. Irrelevant coordinates
are allowed in (2); they merely weaken the floor. This is a proved rational
certificate, not a dimension-independent separation from zero.

An exact all-dimensional obstruction to such a separation already exists
with orientation identically zero. For the one-point defect on n>=2 bits,
let p=2^-n, u=1-2p, v=-2p. All Fourier coefficients except the empty one
equal v, so O_i=0. Every quartet not containing the empty index has zero
refund. In the unique remaining quartet, (u,v,v,v), u-v=1 and each refund
equals 2v^2/[(u^2+3v^2)(u^2+v^2)]. Thus exactly

    T(point_defect_n)=16 binom(n,2)p^2 /
                 [(1-4p+16p^2)(1-4p+8p^2)] ->0.       (2a)

These actual functions have full Fourier support, are all-essential and
prime (one negative vertex). Their H/I tends to4. This closes a positive
refund-floor mechanism even with exact zero orientation and dense support;
it makes no claim that large-threshold minimal witnesses are point defects.

## 4. Arbitrary hard cores enter every positive absolute neighborhood

Fix any nonconstant Boolean seed h on k essential bits. On mk core bits
let h_m=h tensor ... tensor h, and balance it by g_m=z h_m. Choose
r_m=ceil(4 log2(m+1)), p_m=2^-r_m and N_m=mk+1+r_m. Activate g_m only
when all r_m fresh control signs have a prescribed assignment, and output
+1 otherwise. Call this actual Boolean function F_m. Its exact identities are

    H(F_m)=p_m m H(h)+4r_m p_m+A(p_m),
    I(F_m)=p_m[m I(h)+1+r_m],
    A(p)=-(1-p)^2 log2((1-p)^2)+p^2 log2(p^2).

These follow directly by expanding F=1+1_active(g-1): every control
coefficient has magnitude p, core nonempty coefficients have magnitude
p times the core coefficient, and the empty coefficient is 1-p. For
balanced g, sum squared coefficients of g-1 is2, giving the displayed
4r p term and the exceptional empty-row correction. Since A(p)=O(p),
r_m=O(log m), and p_m<=(m+1)^-4,

    H(F_m)/I(F_m) -> H(h)/I(h),  I(F_m)->0.

Each singleton collision obeys C_i<=4 Inf_i because
4a^2b^2/(a^2+b^2)<=4b^2. Nonnegative refunds satisfy
R_ij<=C_i+C_j. Therefore the same physical influence account gives

    0<T(F_m)<=(4N_m-3)I(F_m)->0.                       (3)

Consequently, for every epsilon>0, an absolute FEI(C) bound on all
nonconstant Boolean functions with 0<T<epsilon implies FEI(C) for every
Boolean seed, at the SAME constant, by taking the above limit. Conversely
FEI obviously bounds that neighborhood. This is hardness admission, not a
disproof or admission into the genuinely dimension-minimal critical class.
It rules out any positive absolute floor replacing the dimension-dependent
floor (2), even when hardness must be retained.

## 5. The precise extremality test lost in the embedding

Let K>=0 and suppose D_K(h)>0. Then F_m eventually violates K by its
ratio limit. Query the proper physical block A consisting of all controls
and the balancing bit z. With probability p_m its children are +/-h_m;
all other children are constant. No terminal entropy is dropped:

    E H(child)=p_m m H(h), E I(child)=p_m m I(h),
    S_A=-E D_K(child)=-p_m m D_K(h)<0,
    D_K(F_m)+S_A=L_A-K I_A.

Thus the exact failed condition is physical-child eligibility, specifically
the nonnegative reserve S_A required by least essential dimension. Even a
vanishing absolute joint defect cannot make this embedding critical.
At least one actual smaller-dimensional child violates K. The block is
proper because mk>=1 remains unqueried. This is the original hard terminal,
now explicitly carried into the new orientation-plus-refund diagnostic.

## 6. Dense full-support prime admission with the same hard core

Add two dummy physical bits to F_m, then flip one vertex whose controls
are inactive; take any balancing/core/dummy assignment there. Write G_m
and d_m=N_m+2. Before the flip the integer Walsh sums are divisible by4
because of the dummy duplication; afterwards every sum is2 modulo4.
Therefore G_m has full Fourier support, so every variable is essential.
Its negative truth count is odd: F_m has 2^(mk) negatives, and dummy
duplication multiplies this by4 before the inactive +1 is flipped to -1.
A nontrivial coordinate product always has even negative count, because
both coordinate factors have even-sized truth cubes. Thus G_m is prime
across every nontrivial coordinate partition.

Let s_m=2^-d_m. Each influence changes by at most2s_m. The squared Fourier
law changes by TV<=2sqrt(s_m(1-s_m)); maximal coupling bounds the entropy
change by h2(TV)+TV*d_m=O(d_m sqrt(s_m)). Since I(F_m) is polynomially
small, while these surgery errors are exponentially small,

    H(G_m)/I(G_m)->H(h)/I(h), I(G_m)->0,
    T(G_m)<=(4d_m-3)I(G_m)->0.                        (4)

In particular every positive T-neighborhood, even restricted to prime,
all-essential, full-Fourier-support Boolean functions with arbitrarily
small total influence, admits every hard core at the same limiting ratio.
This complements the sparse-support surgery case: qualitative density of
the *support* does not distinguish the remaining critical regime. It is
not a claim that Fourier mass is evenly distributed or that relative
orientation/refund errors vanish.

Retain the full proper physical cut B of the controls, balancing bit and
both dummy bits. Active children still give +/-h_m with total probability
p_m. One inactive child becomes a point defect v_m on mk core bits, with
weight w_m=2^-(r_m+3); all other inactive children are constant. Exactly,

    E D_K(child)=p_m m D_K(h)+w_m D_K(v_m),
    S_B=-p_m m D_K(h)-w_m D_K(v_m).

The point defect has I(v_m)=2mk*2^-mk and H(v_m)=O(mk*2^-mk).
For any fixed K and seed D_K(h)>0 the second term is exponentially
small compared to p_m m D_K(h), so S_B<0 eventually. Active physical
children also remain explicit smaller-dimensional K-violators. Thus prime
full support does not repair the lost child eligibility. The finite named
K=2 controls certify positive root deficit and negative S_B exactly.

## 7. Source-bound review and the first unsupported line

A052-SIGNED-PAIR-ORIENTATION-REFUND@1: independently reconstructed new
signed-row identity, variance nonnegativity, P<=2(Inf_i+Inf_j), minority
split, and orientation-corrected comparison. Its guarded substitution uses
the unchanged, already reviewed A055 scalar reserve. A051's two-bit bank
is reconstructed from constant/nonconstant phase classes, Fourier TV,
the Gibbs bound, and weighted child accounting. Verdict HOLDS for A052's
new algebra/application; A055 authored the scalar premise and does NOT
count as an independent reviewer of that premise or of the entire chain.
No repair is supplied. Source finite assertion counts are not adopted.

First unsupported line: a *relative*, critical-source estimate paying signed
pair collision/phase error from the actual D+S_pair bank with one influence
owner. Neither exact rigidity (1), exponentially deteriorating floor (2),
nor arbitrary-core neighborhood admission (3) supplies it. A raw positive
orientation/refund floor is now closed as a mechanism; NEXT must retain
critical child signs and normalize the defect against the same live reserve.
