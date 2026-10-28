# A fixed nonfair product branch leaves full FEI in the complement

All entropies are in bits. All physical coordinates below are independent
uniform signs (indexed by binary strings); influence uses those original
coordinates. Let u range over a four-bit cube and put

    a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1],
    b=1-a^2=[0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0].

The bit of weight one varies fastest. For EVERY Boolean h on a fresh cube x,

    F_h(z,u,x)=a(u)+z b(u) h(x)

is Boolean, since a and b have disjoint supports partitioning the cube and
a has value +/-1 on its support. This uses a seed only in the complementary
branch, rather than tensoring the entire gate by a seed. It preserves the
original nonfair product branch exactly, in arbitrary dimension.

## Exact spectrum, entropy and phase energy

Raw Walsh arrays for a and b, on 16 points, are

    A=[2,2,2,2,2,2,2,2,4,-4,-4,-4,-4,4,4,4],
    B=[6,-2,-2,-2,6,-2,-2,-2,0,0,0,0,0,0,0,0].

The normalized squared coefficients of F are, for z-frequency j and
u,x-frequencies s,t,

    p_F(0,s,t)=A_s^2/256 * 1{t=empty},
    p_F(1,s,t)=B_s^2/256 * hhat(t)^2.

There is no cross term between the z-frequency branches. Their masses are
q_0=5/8 and q_1=3/8. The first normalized branch is coordinate product,
with three fair marginals and last-bit probability 4/5; fresh seed
frequencies are deterministically empty. Its entropy is

    H_a=3+h2(1/5)=7/5+log2(5).

The second conditional law is p_b tensor p_h, where p_b has two atoms 3/8
and six atoms 1/24. Thus H_b=3-(1/2)log2(3). It is nonproduct for EVERY
seed: a product law would have product u-marginal, contradicting this p_b.
In addition, A032's norm congruence excludes any ternary product row of
mass 3/8 in every dimension, irrespective of signs.

The complete identities, with no dropped branch or terminal entropy, are

    H(F_h)=5-(9/16)log2(3)+(3/8)H(h),
    H(S_(u,x)|S_z)=(5/8)H_a+(3/8)H_b+(3/8)H(h),
    I_z(F_h)=3/8,
    I_u(F_h)=23/16+5/16=7/4,
    I_x(F_h)=(3/8)I(h),
    I(F_h)=17/8+(3/8)I(h).

The u-energy equality follows either from Walsh degrees or physical edges:
averaging over z kills the cross term between differences of a and b, even
when h is biased. The x-energy is supported precisely where b=1. Therefore
the construction includes all sign-realization costs. In particular seed
entropy cannot be paid from the fixed address influence 3/8.

## Genuine dependence and the tensor guard

Given ANY nonconstant Boolean seed f, use

    h_t(ell,x_1,...,x_t)=ell product_{i=1}^t f(x_i), t>=1.

This is balanced even if f is biased. H(h_t)=tH(f) and I(h_t)=1+tI(f).
The balancing coordinate costs exactly 3/8 in F and is never omitted.
Since h_t has zero empty Fourier coefficient, z-frequency is exactly the
indicator that the seed-frequency set is nonempty. Hence

    I_mutual(S_z;S_(ell,x_1,...,x_t))=h2(3/8)>0

for every t. Dependence does not vanish under scaling. The auxiliary physical
inputs remain independent; it is their squared spectral labels that correlate.
The full ratio is exactly

    [5-(9/16)log2(3)+(3/8)tH(f)] / [5/2+(3/8)tI(f)],

and tends to H(f)/I(f). For nonconstant f, I(f)>0 since a connected cube
with no disagreeing edges would make f constant. Constants have H=I=0 and
need no ratio. The analogous conditional/data-influence ratio tends to the
same seed ratio, with denominator 17/8+(3/8)tI(f).

Consequently a dimension-independent FEI theorem for this very fixed-mask
one-product-branch subclass is equivalent to full FEI, with the SAME constant
in the reverse implication. A universal full-FEI bound restricts to the
subclass. A finite conditional bound H(S_(u,x)|S_z)<=K I_(u,x) on this
subclass also implies full FEI at K by the same limit. In the forward
direction full FEI implies a finite such conditional constant, since
I(F_h)/I_(u,x)(F_h)<=17/14. The family is not a disproof: no seed with
unbounded H/I is supplied. It is a certificate that this admission condition
still contains the complete unpaid problem.

## Signed address/Renyi gap retained exactly

Add a second unused physical address d if the two-address interface is
required, and set X=(z,d), Y=(u,x). This changes no spectrum, entropy or
influence; the positive address masses remain 5/8,3/8. Write R for order-1/2
Renyi entropy. Direct sums of absolute Walsh coefficients give

    R_a=log2(72/5), R_b=log2(6), R_(b tensor h)=R_b+R(h).

The signed address gap is

    G=H(S_X)-(5/8)R_a-(3/8)[R_b+R(h)]
     =3/4-2log2(3)-(3/8)R(h).

The identity H(F)=sum_j q_j[H(p_j)+R(p_j)]+G cancels the full seed Renyi
term and retains the full seed Shannon term. For h_t, R(h_t)=tR(f).
Discarding G would invent an extra (3/8)tR(f) bill. Replacing G by a
universal Renyi/influence estimate is unjustified. There is only one
physical data reserve, 7/4+(3/8)I(h); the fixed 7/4 overhead vanishes after
division by t and cannot hide a payment of arbitrary seed entropy.

## First unsupported line and change of mechanism

The exact unsupported line is a universal estimate of the complementary
normalized seed Shannon term from its surviving physical seed energy.
Under this fixed-mask admission that line is full FEI itself. Two product
branches are already closed by mass rigidity; one product branch alone
cannot supply an easier terminal theorem. A next universal transfer must
transport a measured incoming reference or unused ancestor budget through
the nonproduct complementary branch, retaining its complete seed terminal,
rather than declaring the presence of a product sibling sufficient payment.
