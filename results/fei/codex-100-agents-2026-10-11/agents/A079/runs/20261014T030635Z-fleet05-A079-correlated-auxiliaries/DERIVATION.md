# Cubic row collision with unequal affine inverse supports

Author proof, independent review pending. All entropy is in bits; all influence
is measured in the original physical coordinates. Fourier-sign polynomials here
are polynomials on frequency variables, not physical input phases.

## Exact statement

Let F on two uniform physical address bits X and arbitrarily many independent
uniform data bits Y be Boolean. Define h_J(y)=2 E_X F(X,y) chi_J(X),
w_J=E_Y h_J^2/4, and p_J(S)=h_Jhat(S)^2/(4w_J) for nonzero rows.
Suppose each p_J is a coordinate-product law with AT MOST ONE nonfair varying
frequency coordinate. All other varying coordinates are fair. The nonfair
marginal can be arbitrary; its primitive rational magnitude ratio is not
bounded. Fixed frequency coordinates are allowed. Fourier signs are arbitrary;
no phase-degree hypothesis is imposed.

Put b=h2(1/10), Kcond=3/2+(5/2)b, Kall=6+2log2(65/64),
and Kjoint=10-3log2(3). Then in every data
dimension,

    H(S_Y|S_X) <= Kcond I_Y(F),
    H(F) <= Kall I(F).

If all nonfair primitive ratios belong to {2,3,4}, the sharper bound
H(F)<=Kjoint I(F) holds.

The conditional constant is sharp, attained by the actual three-bit point
defect with two address bits and one data bit. The joint constants are upper
bounds, not claimed sharp. This admitted class includes A032's actual 64-sign
cubic heavy-row witness, whose row ratios are 4,3,3,2.

## Universal two-address row ledger

For EVERY two-address Boolean F, without product or phase hypotheses, let
R_J=H_{1/2}(p_J)=2 log2(sum_S sqrt(p_J(S))). Then

    H(w) <= sum_J w_J R_J + 2 I_X(F),
    H(F) <= sum_J w_J [H(p_J)+R_J] + 2 I_X(F).       (1)

Proof: at every y the four integer rows are either one entry of magnitude two
and three zeros (pure), or all four entries of magnitude one (mixed). This
follows by taking the Walsh transform of the four signs F(x,y). Let M be the
common mixed set, delta=Pr(M). Its contribution to I_X is delta, since
sum_J |J|/4=1. Thus delta<=I_X.

Fourier inversion gives max|h_J|<=2 sqrt(w_J) sum sqrt(p_J). If row J has a
pure point, max|h_J|=2, and log2(1/w_J)<=R_J. Otherwise max|h_J|=1 and
log2(1/w_J)<=R_J+2. Such a mixed-only row is supported exactly on M, so
w_J=delta/4. The total weight of mixed-only rows is at most delta. Multiplying
the row bounds by w_J and summing proves (1). The complete conditional spectrum
and address entropy are both retained. This is a universal ledger, not a
universal FEI bound: R_J can be large compared with physical row influence.

## Exact phase-realization geometry

Consider one nonfair row, remove its deterministic spectral character, and let
m be its number of fair free frequency coordinates. Its two quadratic Fourier
sign branches have normalized inverse Walsh functions g0,g1. If their polar
ranks are r0,r1, their inverse supports L0,L1 are affine spaces of dimensions
r0,r1; these ranks are even. Their nonzero magnitudes are 2^(-r0/2),
2^(-r1/2). For completeness, a quadratic sign sigma has autocorrelation
E_v sigma(v)sigma(v+t)=(-1)^(q(t)+q(0)) on its polar kernel and zero off it.
On the kernel this sign is a character. Fourier inversion of that
autocorrelation gives g(x)^2=2^-r on one affine coset of the kernel annihilator,
and zero elsewhere. This proves the flatness and dimension assertion directly.
Consequently the physical row has the form

    h(z,x)=c [R g0(x)+(-1)^z g1(x)],
    A=c R 2^(-r0/2),  B=c 2^(-r1/2),
    R=(A/B) 2^((r0-r1)/2),                        (2)

for c>0, after orienting the heavy frequency half as zero. All nonzero physical
values are integers of magnitude at most two. Branch signs on an intersection
only swap which physical z value has magnitude A+B or |A-B|; there is no free
phase choice that removes either value.

* If L0=L1, their ranks agree. The positive amplitudes must be half-integers
  with A+B and |A-B| integers at most two. The possibilities are
  (1/2,1/2), (1,1), (3/2,1/2), or (1/2,3/2). For a nonfair ratio in {2,3,4},
  only R=3 occurs, with amplitudes (3/2,1/2).
* If the supports intersect but are unequal, at least one support has an
  exclusive point. Its amplitude is a positive integer. Integrality at the
  intersection makes the other amplitude an integer too, and A+B<=2 forces
  A=B=1. Thus R=2 or 4, and r0-r1=2 log2(R).
* If they are disjoint, A and B are each one or two. Equation (2) excludes
  R=3. For R=2, the rank difference is 0,2,4; for R=4 it is 2,4,6, according
  to the amplitude pair. The larger affine support is proper, hence its
  dimension is at most m-1.

These are exhaustive. In particular R=2 requires m>=1, while R=4 requires
m>=3. R=3 may have m=0; that endpoint will be paid using the actual common
mixed mask, not omitted. A 4:1 row also has w<=17/32. In the intersecting case
its amplitudes are one, its support dimensions differ by four, and
w=(2^r0+2^r1)/(4*2^m)<=17/64. In the disjoint cases use the amplitudes from
{1,2}, r0<=m-1, and (2); the largest result is 17/32. A032's cubic witness
attains this latter bound with a height-two affine plane disjoint from a
height-one point, r0-r1=2 and m=3.

The classification above assumes quadratic branch signs. The dimension costs
needed for the entropy theorem hold for ARBITRARY signs: if a 4:1 row had m<3,
each branch would be a sign on at most two frequency bits and therefore would
automatically have degree at most two. The classification rules it out.
Similarly a 2:1 row with m=0 is excluded. Thus arbitrary-sign rows satisfy
m>=3 for R=4 and m>=1 for R=2. No large-dimensional phase assumption remains.

There is also an arbitrary-sign proof of the weight caps. Let s be the common
positive integer magnitude of the raw Walsh coefficients on the light half.
An odd divisor of s would divide every raw coefficient and, by integer Walsh
inversion, every h value. Height two excludes any odd divisor greater than one.
Hence s is a power of two. Parseval gives w=(R^2+1) times a power of two, with
the even factor removed when R=3. Since w<=1, w<=5/8 for R=2 or 3 and
w<=17/32 for R=4. The actual cubic heavy row attains the latter bound.

Thus unequal-support phase realization supplies the low-dimensional exclusion
needed for arbitrary signs: at least three fair coordinates for the 4:1 case. Its
normalized row influence is at least m/2+1/17, and its conditional row entropy
is exactly m+h2(1/17). Fixed-one frequency coordinates only add influence.

## Regular row payment, with both entropy terms

For a ratio R, q=1/(R^2+1). Either orientation has the same entropy and
normalized physical row influence at least m/2+q. Direct product evaluation gives

    H(p)=m+h2(q),
    H_{1/2}(p)=m+2log2(R+1)-log2(R^2+1),
    H(p)+H_{1/2}(p)=2m+2log2(R+1)-2(1-q)log2(R).   (3)

Fair rows have H=H_{1/2}<=2 I(row). For R=2 use m>=1, for R=4 use m>=3,
and for R=3 with m>=1 use that endpoint. The ratio of the last line of (3)
to m/2+q is decreasing to four; alternatively its supremum is the larger
of its endpoint and four. The respective endpoints are

    R=2: (4+20log2(3))/7,
    R=3: 10-3log2(3)=Kjoint,
    R=4: (76+68log2(5))/53.

The first and third are strictly below Kjoint. Integer certificates
3^5<2^8 and 5^3<2^7 suffice: the first comparison reduces to
41log2(3)<66; the third is below 704/159<9/2<Kjoint.
Applying (1) proves H(F)<=Kjoint I_Y+2 I_X<=Kjoint I whenever no R=3,m=0
row is present. This proof allocates address entropy once, not from a second
independent copy of physical influence.

For conditional entropy alone the regular row endpoint ratios are
(1+h2(1/5))/(7/10), (1+b)/(3/5), and
(3+h2(1/17))/(53/34). They are below 52/21, 89/36, and 237/106,
respectively. To check these inequalities exactly use

    5^3<2^7, 3^12>2^19, 17^4<2^17.

Since 5^10>2^23 and 3^5<2^8 give b>21/50, Kcond>51/20,
which exceeds all three rational bounds and two. Thus every regular row pays
its entire conditional entropy at rate Kcond.

## The exceptional m=0 ratio-three row

Such a row has physical magnitudes two and one on the two halves of a SINGLE
physical data coordinate z, up to a deterministic physical character on other
data coordinates. Hence the common mixed mask is a half cube, w_heavy=5/8,
and every other row has magnitude one exactly on that half cube and zero
elsewhere. The other row weights are each 1/8.

No other row can have ANY single nonfair ratio. Write its integer raw Walsh
magnitudes as a*s and b*s, with coprime positive integers a!=b, integer s,
and m' other fair coordinates. Its squared norm, and therefore its weight,
has odd numerator divisible by the odd part of a^2+b^2. This odd part exceeds
one: opposite parity gives an odd sum at least five; both odd give a sum
congruent to two modulo eight, and a^2+b^2=2 would require a=b=1. All Walsh
denominators and support sizes are powers of two. This is incompatible with
w=1/8. All other rows in the admitted class must be fair.
Their support on the half cube makes z a fair active frequency coordinate,
so each has fair spectral dimension d_J>=1.

The full address law is (5,1,1,1)/8. Its minimum address influence over label
permutations is 1/2. The heavy row has H=b and row influence at least 1/10;
the other rows have H=d_J and row influence at least d_J/2. Write
e=sum_other (d_J-1)/16>=0. Then

    I_Y >= 1/4+e,
    H(S_Y|S_X)= (5/8)b+3/8+2e
                 =Kcond/4+2e <=Kcond I_Y.

This proves the sharp conditional bound including the exceptional row. The
point defect F=1 except at one vertex of its three-bit cube attains equality
with two address bits and one data bit, I_Y=1/4 and e=0.

Retaining address entropy gives

    H(F)=4-(9/8)log2(3)+2e,
    I(F)>=3/4+e.

Thus H(F)<=Cstar I(F), Cstar=16/3-(3/2)log2(3), which is strictly below Kjoint.
The sharp full-collision constant from the previous stage is used here only as
an explicit algebraic number; the point-defect equality is evaluated directly,
and no pending prior theorem is a proof premise.

## Remove the magnitude-ratio restriction

For any nonfair row with m=0, remove the deterministic character. Its physical
values on the remaining one bit are integers in {0,+/-1,+/-2}. Their two
sums/differences show that the only nonfair nondeterministic Fourier magnitude
ratio is 3:1. The exceptional analysis above exhausts m=0 for ALL ratios.

When m=1, the two branch signs are affine and have rank-zero inverse supports,
each a point. Equal supports allow only nonfair ratio3; disjoint supports have
integer amplitudes one or two and allow only ratio2. Thus any row on at most
two varying data-frequency bits has nonfair ratio2 or3. The complete four-bit
Boolean validation therefore covers the arbitrary-ratio theorem there, even
though the implementation names the three fixed-ratio signatures explicitly.

For m>=1, let q<=1/2 be the smaller nonfair spectral probability. The
Gibbs/KL inequality gives h2(q)<=c q+log2(1+2^-c) for every c>0: subtract the
nonnegative divergence from Bernoulli(q) to the Bernoulli law with probability
1/(1+2^c). At c=5/2, log2(1+2^-5/2)<1/4. Squaring the equivalent positive
inequality reduces it to sqrt(2)>11/8, certified by 121<128. Hence

    m+h2(q)<=m+(5/2)q+1/4<=(5/2)(m/2+q).

Every regular arbitrary-ratio row pays conditional entropy at rate5/2<Kcond.
Together with the exceptional common-mask calculation this proves the SAME
sharp Kcond for arbitrary nonfair marginals and arbitrary phases.

For complete joint entropy put l=log2(65/64)>0. Take c=6 in the Gibbs bound
and use H_1/2(Ber(q))<=1. For m>=1,

    H(p)+H_1/2(p)<=2m+6q+1+l<=(6+2l)(m/2+q),

since the right side minus the preceding bound is
(1+l)(m-1)+2l q>=0. Fair rows pay this sum at rate4. Use the universal ledger
(1) and Kall=6+2l>2 to obtain H(F)<=Kall I(F). The exceptional case pays at
Cstar<Kall. This closes all single-nonfair-coordinate odds; no universal
Renyi/I bound is claimed, and the physical row height/common-mask endpoint
remains necessary.

## Boundaries and first unsupported universal line

The inverse-support classification is exhaustive for a single nonfair
coordinate with quadratic branch signs and integer height two. Its low-dimension
exclusion and the weight divisibility extend to arbitrary Fourier signs, so the
total theorem permits correlated spectra, arbitrary phases and the actual cubic witness. It does not
assert unrestricted tensor closure, more than two address bits,
multiple nonfair coordinates per row, nonproduct magnitudes,
or repeated cubic collision closure. The first unsupported extension is a
conditional complete-core reference transfer at a nonproduct or
multiple-nonfair-coordinate row, retaining the signed gap
H(w)-sum w H_{1/2}(p) and both actual terminal debts, paid by one unused physical
reserve. A universal bound on H_{1/2}/I alone is already excluded by the
campaign's fixed-Renyi obstruction, so (1) must not be turned into that known
failed route. The universal row ledger itself is proved; the conditional
reference transfer is not. Full FEI remains open.
