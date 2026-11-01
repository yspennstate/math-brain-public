# A079: sharp quadratic two-phase collision

Author proof; independent review pending. Entropy is in bits. All coordinates
below are uniform physical bits, with no change of coordinates in the influence.

## Statement and scope

Let q0,q1 be arbitrary polynomials of degree at most two over F2 on n bits y,
let gj(y)=(-1)^qj(y), and let G(z,y)=gz(y). Set
a=(I(g0)+I(g1))/2, mu=E(g0 g1), d=(1-mu)/2=Inf_z(G), and
L=H(G)-(H(g0)+H(g1))/2. Then, for every n including n=0,

    L <= kappa d,       kappa=12-(9/2)log2(3),
    H(G) <= Cstar I(G), Cstar=16/3-(3/2)log2(3)=(4+kappa)/3.

Both constants are sharp, attained by q0=0, q1=y0*y1. This treats a single
collision of two quadratic phases on the SAME full data cube. It does not assert
closure for unequal affine supports or for repeated collisions. Adding unused
coordinates preserves the equality example.

## Quadratic Fourier facts, with physical energy retained

For a quadratic q, let B be its polar bilinear form and let r=rank(B), an even
integer. The law of the squared normalized Walsh coefficients of (-1)^q is
uniform on an affine subspace of dimension r. Here is a proof of the fact used:
the autocorrelation at translation t is zero unless t is in ker(B); on ker(B)
it is a character determined by q(t)+q(0). Fourier inversion of this
autocorrelation gives mass 2^-r on an affine coset of ker(B)^perp and zero
elsewhere. Thus H(g)=r. In that affine support, each varying physical coordinate
is fair and each fixed coordinate is deterministic. At least r coordinates
vary, so I(g)>=r/2. This inequality uses physical coordinate weight, not a
coordinate-invariant substitute.

Put rj=rank(Bj), rD=rank(B0+B1). Matrix rank gives
|r0-r1|<=rD<=r0+r1. The preceding fact applied to g0*g1 gives
mu=0 or |mu|=2^(-rD/2). Consequently positive nontrivial mu has the values
1/2,1/4,1/8,..., and r0+r1>=rD.

## Exact overlap formula

Let Msmall<=Mlarge be the sizes of the two affine Fourier supports,
R=Mlarge/Msmall (a power of four), and u be the fraction of the smaller support
in their intersection. Parseval gives |mu|<=u/sqrt(R). The two selector
Fourier coefficients at a data frequency v are (g0hat(v)+g1hat(v))/2 and
(g0hat(v)-g1hat(v))/2. Their sign choices only permute their squared masses.
Frequencies outside the intersection contribute a new fair selector bit;
frequencies in the intersection have fixed amplitudes 1/sqrt(Msmall) and
1/sqrt(Mlarge). Directly summing -p log2 p therefore gives

    L=2-u gamma_R,
    gamma_1=2,
    gamma_4=(9/8)log2(3)-1,
    gamma_16=(25/32)log2(5)+(9/32)log2(3)-2.

For completeness, with t=R^-1/2 the formula at any R is

    gamma_R = 1+1/R
       + ((1+t)^2/4) log2((1+t)^2/4)
       + ((1-t)^2/4) log2((1-t)^2/4)
       + (log2 R)/(2R),

where 0 log 0=0. This follows by comparing the two intersection masses with
their two separate child contributions; the support information lost by mixing
is included. In particular L<=2 independently of R: the data marginal is the
average of the child laws, whose Jensen-Shannon increment is at most one bit,
and the conditional spectral-selector entropy is at most one bit. No
conditional auxiliary entropy has been dropped.

Write L4=2-gamma_4=kappa/4 and
L16=2-gamma_16=4-(25/32)log2(5)-(9/32)log2(3).
The following exact integer comparisons are sufficient for all inequalities:

    3^5<2^8,  3^12>2^19,  5^10>2^23.

They imply 24/5<kappa<39/8, Cstar>44/15, and L16<225/128.
Also 32/7<24/5, 75/16<24/5, 80/31<44/15,
and 481/176<44/15. These are rational or integer certificates.

## Sharp selector decrement

If mu<=0 then d>=1/2 and L<=2<=4d<kappa d.
If mu=1 the children agree, d=L=0. Otherwise:

* mu=1/2 forces rD=2 and R=1 or 4. When R=1,
  L=2(1-u)<=2(1-mu)=4d. When R=4, u>=mu sqrt(R)=1,
  hence u=1 and L=L4=kappa/4=kappa d.
* mu=1/4 forces rD=4 and R=1,4,16. The R=1 argument is unchanged.
  For R=4, u>=1/2, gamma_4>0, and L<=1+L4/2;
  hence L/d<=(8+kappa)/3<kappa because kappa>4.
  For R=16, u=1 and L/d=(8/3)L16<75/16<kappa.
* 0<mu<=1/8 gives d>=7/16 and L/d<=32/7<kappa.

This exhausts every quadratic pair in every dimension. The sharp case has
H(g0)=0, H(g1)=2, H(G)=4-(9/8)log2(3), d=1/4,
and L=3-(9/8)log2(3)=kappa/4.

## Sharp whole-function constant

The physical energy identity is I(G)=a+d, and H(G)<=2a+L.
Multiplication of G by the selector character (-1)^z preserves H and a,
while changing d to 1-d. Thus negative mu can be reduced to positive |mu|,
whose influence is smaller. The case |mu|=1 is a quadratic phase, possibly
times z, and has H/I<=2 whenever I>0. Constant functions have H=I=0.

For positive mu=1/2 and R=4, a>=(r0+r1)/4>=1/2.
Therefore (2a+L4)/(a+1/4) is at most its value at a=1/2,
which is (4+kappa)/3=Cstar. For R=1, the even equal ranks and
r0+r1>=2 force a>=1. Since L<=1, the ratio is at most 12/5.

For positive mu=1/4:

* R=1: a>=1, L<=3/2, ratio <=28/11<Cstar.
* R=4: equal-rank parity and rank difference two, with rank sum at least
  four, force rank sum at least six; a>=3/2. Since L<=1+kappa/8,
  the ratio is at most (32+kappa)/15<Cstar (equivalent to kappa>2).
* R=16: a>=1, L=L16<225/128, and the ratio is below
  (2+225/128)/(1+3/8)=481/176<Cstar.

For 0<mu<=1/8, r0+r1>=6, a>=3/2, d>=7/16, L<=2.
The ratio is at most 80/31<Cstar. Each displayed decreasing-ratio bound
is justified by differentiating (2a+b)/(a+d): its derivative has sign
2d-b; if nonnegative the supremum instead is its limit 2, also below Cstar.

It remains to handle mu=0, d=1/2.
If r0+r1>=4 then a>=1, L<=2, so the ratio is at most 8/3.
If r0=r1=0, the distinct children are characters. Their entropy is zero
and their disjoint spectra give H(G)=2. At least one character is nonconstant,
so a>=1/2 and H(G)/I(G)<=2.
If r0+r1=2, one support is a single character frequency v and the other is
an affine plane not containing v. Here H(G)=3 and a>=3/4, as follows.
If v is nonempty, its weight is at least one and the rank-two child's
influence is at least one, so a>=1. If v is empty, the affine plane excludes
the origin. A fixed-one physical coordinate gives plane mean weight at least
two. If there is no fixed-one coordinate, exactly two varying coordinates
would make the plane the full cube on those coordinates, containing the
origin. There must instead be at least three varying coordinates, so its
mean weight is at least 3/2. Thus a>=3/4 and H(G)/I(G)<=12/5.
All these constants are strictly below Cstar. This completes the proof.

## Conditional entropy, actual label collision, and terminal payment

At the sharp witness G=(-1)^(z*y0*y1), I_y=1/2 and I_z=1/4.
The spectral z marginal has masses 3/4,1/4. With X=z and Y=(y0,y1),

    H(S_Y|S_X)=2-(3/8)log2(3),
    H(S_Y|S_X)/I_Y=4-(3/4)log2(3)>2.

If instead X is empty and Y includes the selector, the conditional entropy is
the whole entropy, with sharp ratio Cstar>2. The loss of constant two is an
actual Boolean event, not a free choice of incompatible spectral phases.
Indeed f(x,z,y)=(-1)^(x*z+z*y0*y1) has distinct X labels empty and {x}
on the affine cells z=0 and z=1, with unit quadratic phases on each cell.
It satisfies the admission hypotheses of A034 v1. Restricting physical x=0
gives exactly the sharp collision G; the projected labels have merged.
This does not refute A034 v1, which explicitly requires injectivity of the
projected labels for its X-restriction closure statement.

For a selector-first stopping tree, L is the exact one-node entropy
decrement and d is its selector influence charge. The identity
H(G)=L+(r0+r1)/2 retains terminal entropy; the terminal influence is a.
Thus L<=kappa d and (r0+r1)/2<=2a provide a certified local C019 payment.
The sharper Cstar bound uses the rank/core slack once at this node; it must
not be recycled at descendants without a new argument.

## First unsupported universal line

The first unsupported extension is that arbitrary collisions of unit
quadratic phases on unequal affine partition cells obey a uniform decrement
bound using the available physical separator energy, with terminal costs
retained. Such rows do not have the two full-cube flat laws assumed here.
After repeated collisions the phase need not be quadratic, so the discrete
mu/rank classification also fails. No universal C018 or C019 bound, hereditary
closure theorem, unbounded-ratio Boolean family, or full FEI resolution is
claimed.
