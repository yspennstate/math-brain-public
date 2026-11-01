# Exact sharpness and ledger audit

Uniform Boolean sign functions throughout. H and B are in bits; Lambda and
the repeated log charge D below are in nats. Write phi(u,v)=(u+v)h2(v/(u+v)),
with zero conventions. These are finite-dimensional analytic proofs; no
floating entropy comparison is used.

## 1. Rare-switch chain: exact H, I, B and the redundant root charge

Let A_r be the origin indicator on r independent binary controls, p=2^-r,
q=1-p, F_0=x_0, and F_t=(1-A_r(z_t))F_(t-1)+A_r(z_t)y_t, with all
physical inputs fresh. Every F_t is balanced. The two switch branches have
correlation zero, and E[F_t F_(t-1)]=q. Its dimension is 1+t(r+1).

For an arbitrary balanced G, the G-sector of (1-A)G+Ay has coefficients
q Ghat(S) at empty control frequency and -p Ghat(S) at each nonempty
control frequency; the y-sector has coefficient p at every control frequency.
The G and y sectors have disjoint data Fourier supports. Consequently

    I(F_t)=q I(F_(t-1))+p+rp,
    H(F_t)=q H(F_(t-1))+Q_r,
    Q_r=q^2 log2(1/q^2)+2rp(2-p).

For one control coordinate, G-sector erasure has one exceptional pair
(q^2,p^2) and 2^(r-1)-1 equal pairs (p^2,p^2). The y-sector contributes p.
Thus b_r=phi(q^2,p^2)+2p-2p^2 is its exact erasure. For an old data
coordinate i, summing over control frequencies multiplies its erasure by q;
the singleton/empty residual sector is disjoint because the other outer
branch contains y. The new y erasure is zero. Therefore

    B(F_t)=q B(F_(t-1))+r b_r,
    I(F_d)=1+r(1-q^d),
    H(F_d)=Q_r(1-q^d)/p,
    B(F_d)=r b_r(1-q^d)/p.                         (1)

The singleton coefficients are q^d at x_0 and p q^(d-s) at y_s, s=1,...,d;
control singletons vanish. In particular

    Lambda(F_t)=2t q^(2t) ln(1/q)
      + sum_(j=0)^(t-1) p^2 q^(2j)[2ln(1/p)+2j ln(1/q)]. (2)

At the root of G_r(G,y,z), A057's concavity estimate inserts
q Lambda(G): outer x has influence q, outer x erasure B_x(G_r)=0,
and the real coherent L_x is exactly zero (the outer a-sector contains y,
the b-sector does not). Controls are literals with alpha=1, so their
root charge is exact r b_r; y is a literal and incurs no extra charge.
Thus the selectively applied root ledger T_t satisfies

    T_0=0, T_t=q T_(t-1)+r b_r ln2+q Lambda(F_(t-1)),
    T_d=B_nat(F_d)+D_d,
    D_d=sum_(t=1)^(d-1) q^(d-t) Lambda(F_t).       (3)

Here T and B_nat are nats (multiply r b_r by ln2 in the recurrence).
This is a SPECIFIC concavity relaxation of the exact erasure identity,
not the still coarser constant-(2/e)I root bound. It repeats a charge even
though the relevant residual is zero at every level.

The dominant singleton alone yields

    D_d >= p d(d-1) q^(2d) >= p d(d-1)(1-2dp).    (4)

Indeed ln(1/q)>=p and d+t<=2d, so each term is at least 2tp q^(2d).
For an upper estimate use ln(1/q)<=p/q and discard all q powers:

    D_d <= p d(d-1)/q
          +p^2 d(d-1)ln(1/p)
          +(p^3/q)d(d-1)(d-2)/3.                 (5)

If dp->0, p ln(1/p)->0, then (4)-(5) imply D_d~p d(d-1), provided d->infinity.
Also Q_r~4rp as r->infinity, b_r~2p, and (1-q^d)/p~d. Thus

    H(F_d)~4rpd bits, B(F_d)~2rpd bits,
    I(F_d)-1~rpd, D_d~p d^2 nats.              (6)

Set r=3k, d=2^(2k), k>=2. Then I<=1+3k 2^-k<=5/2,
H~12k 2^-k, B~6k 2^-k, but D>=2^(k-1)(1-2^(-2k))->infinity.
The ratio D/H grows as (ln-unit conversion aside) d/(4r).
For every r,d, Q_r<=6rp (use -ln q<=p/q and ln2>1/2), hence
H<=6(I-1): this is not an FEI counterexample.

Notation correction to the informal lead diagnostic: if epsilon means
SWITCH PROBABILITY p, H=Theta(r d epsilon) and D=Theta(epsilon d^2).
If epsilon means GATE INFLUENCE DEFICIT rp, H=Theta(d epsilon) and
D=Theta(epsilon d^2/r). Both cannot be written with the same epsilon
without retaining r. A059 already proved the essential divergence; (1),(3)
and the explicit factor-r correction are the additional sharpness ledger here.

## 2. An a-bit selector cell containing a bent point defect

Let m>=2 be even, a>=1, delta=2^-m, p=2^-a, and
b(y)=(-1)^(y_1 y_2+...+y_(m-1)y_m). Let D(y)=1_(y=0), A(z)=1_(z=0),
and F(z,y)=b(y)-2A(z)D(y). This is Boolean because b(0)=1. Both data
branches are b and b'=b-2D, sharing every data Fourier frequency, and
E[bb']=1-2delta. Their means are sqrt(delta) and sqrt(delta)-2delta;
E[F]=sqrt(delta)-2p delta. Thus the two branches are neither balanced
nor orthogonal. Fresh selectors ARE present. A closure requiring branch
orthogonality/balance must not be tested as if this example met it.

All bhat(S) are sigma sqrt(delta), sigma=+1 or -1, with counts
N_sigma=(delta^-1+sigma delta^-1/2)/2. Put

    u=4p^2 delta^2,
    v_sigma=(sigma sqrt(delta)-2p delta)^2,
    M_sigma=v_sigma+(p^-1-1)u.

At empty selector frequency the coefficient is bhat(S)-2p delta; at
every nonempty selector frequency it is -2p delta. Thus

    H(F)=sum_sigma N_sigma v_sigma log2(1/v_sigma)
            +delta^-1(p^-1-1)u log2(1/u),
    B_W=sum_sigma N_sigma [v_sigma log2(M_sigma/v_sigma)
                       +(p^-1-1)u log2(M_sigma/u)],
    I_W=2a p delta,
    I_data=m(1/2+2p delta),
    I(F)=m/2+2(m+a)p delta.                      (7)

Zeros, for instance v_+=0 at a=1,m=2, contribute zero. Selector coordinates
change F only when y=0 and all other selector bits are zero, giving
Inf_z=2p delta. Each data origin edge changes from nonpivotal to pivotal
on the selector cell, adding 2p delta to the original influence 1/2.

There is an especially useful exact control on conditional entropy. Put
beta=4p(1-p)delta. The selector spectral law has mass 1-beta at empty
frequency and mass 4p^2 delta at each other frequency. Conditional on
any nonempty selector frequency the data spectrum is uniform. Therefore
the selector/data mutual information depends only on the indicator of a
nonempty selector frequency. Its exact chi-square divergence from the
product of marginals is

    chi2= beta/(1-beta) *
       16p^2 delta(1-delta)/[(1+4p delta)^2-16p^2 delta].      (8)

To derive (8), the uniform data law U has
sum_S U(S)^2/M(S)=[1+8p delta]/[(1+4p delta)^2-16p^2 delta].
For a binary mixture of weight beta with one conditional law U,
chi2=beta/(1-beta)*(sum U^2/M-1). This proves (8).
Since mutual information is between zero and log2(1+chi2)<=chi2/ln2,

    H(S_W)-chi2/ln2 <= B_W <= H(S_W),
    H(S_W)=h2(beta)+beta log2(p^-1-1).           (9)

For 0<=beta<1, h2(beta)=beta log2(1/beta)+beta/ln2+E,
where -beta^2/[(1-beta)ln2]<=E<=0 (integrate or expand -ln(1-beta)).
Here beta<=delta<=1/4 and the denominator in (8) is at least 1.
Using beta<=4p delta, p<=1/2 and beta/I_W<=2/a gives the uniform bound

    L(a,m)-32p delta/(a ln2) <= B_W/I_W <= L(a,m),
    L(a,m)=2(1-p)/a * [m+2a-2+1/ln2].          (10)

For clarity, the error bound follows by dividing beta^2/(1-beta)+chi2
by I_W ln2. The bracket after extracting beta is <=
(16/3)p delta+(64/3)p^2 delta <=16p delta.
Thus (10) is an all-parameter rigorous bound, not just a fixed-a expansion.

Consequences: for every FIXED a, B_W/I_W grows with slope
2(1-2^-a)/a in m; for a->infinity and m/a->lambda finite, the ratio tends
4+2lambda; if m/a->infinity, it diverges. Increasing the selector dimension
can therefore remove the apparent local divergence: quantify both parameters.
At a=1, (8) reduces exactly to 4delta^2/(1+4delta^2), reproducing X009.
For fixed a, B_W/I_data->0 despite B_W/I_W->infinity. The data budget is
large, and its reservation/transport remains a substantive obligation.
The selector's physical label carries only two distinct branch functions;
the rare-cell Boolean label has total influence 2a p. Cheap labels alone
do not provide a selector-only B_W payment.

## 3. Additive constants and tensorization

For disjoint products f tensor g, spectral laws are independent, so H, I,
aggregate B, and block B_W/I_W numerators and denominators add. For tensor
powers, H(f^tensor t)=tH(f), I=tI(f), B=tB(f). A class closed under these
powers and obeying H<=C I+D with FIXED D obeys H<=C I by division and
t->infinity. Likewise H<=C(I-1)+D has the SAME multiplicative coefficient
as H<=CI whenever the class is tensor closed. The additive shift may matter
for finite members or gate-deficit closure, but does not improve the optimal
universal coefficient. A per-factor D, growing with t, is not erased.

For the rare bent selector example tensoring independent selector/data
copies preserves B_W/I_W and does not turn its large local ratio into a
large H/I. The chain's repeated log D is an accounting cost, not an entropy;
it must not be tensorized as if it were Fourier entropy. The explicit
families themselves (a fixed chain or one bent perturbation) are not closed
under tensor powers, so no smaller coefficient for exactly those narrow
families is ruled out by the general tensor argument. Their tensor closures
are the classes to which the additive conclusion applies.

## 4. Exact remaining universal line

No universal payment of B_W by selector influence survives (10). No
depth-uniform payment of the repeated root log (3) by I survives (4).
The actual B in (1) is small: use the disjoint outer-sector zero or charge
new gate/edge logarithms once. What remains is mapping a physical query
tree's recentered, biased descendants and terminal entropy into a conserved
data-side/deficit budget; formula path weights q^(d-t) are not physical
reach probabilities. That transfer is unproved here. Full FEI is OPEN.
