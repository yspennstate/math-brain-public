# Biased rare-row goodness and the first core-data query

All inputs are uniform physical bits, entropies are in bits, and
c=1/ln2. Let B=WUV, C=U OR V, D=C-B, where W,U,V are disjoint
compatible point events of positive widths L,R,T. Let S be a fresh
j-bit point event and g any independent Boolean sign, with no balance
assumption. Put

    F=1+[B+S D](g-1), a=1-Eg in [0,2],
    eta=2^{-(L+R+T)}, q=2^-R, r=2^-T,
    e=q+r-qr-eta, rho=2^{-(j-1)}, d=rho a e/2.

If e<=1/8, then every live S query with d>0 satisfies

    B_i(F)/Inf_i(F) < 10063/2520 <4.                    (1)

If d=0 then F is constant 1, since a=0; its erasure is zero. In
particular (1) holds in every width whenever min(R,T)>=4, for every
biased independent core and every remaining separator length.

This is a narrow continuation of A046's reviewed balanced rare-row
lemma, not a new universal FEI candidate. Its constant is deliberately
loose but has a strict exact margin 17/2520 below 4.

## Exact moments with arbitrary core bias

Write G=1+B(g-1), H=1+C(g-1), Delta=Hhat-Ghat. The full data labels
here include W,U,V and all core labels, but exclude the fresh separator.
Then

    EG=1-a eta, EH=1-a(eta+e), Pr(G!=H)=a e/2,
    Delta_empty=-a e.

For nonempty data frequencies, Boolean Parseval gives exactly

    sum Ghat^2 = 2a eta-a^2 eta^2,
    sum Ghat Delta = -a^2 eta e,
    sum Delta^2 = 2a e-a^2 e^2.                          (2)

For example, the full cross product sum equals E[G(H-G)]=-a e;
subtracting (1-a eta)(-a e) gives the middle identity. Nothing in
(2) assumes spectral flatness, unbiased rows, or core independence
within its own coordinates.

Nonempty remaining-separator Fourier labels contribute exactly
2(1-rho)d to erasure, by their equal parent masses. In the empty
remaining-separator label, the paired amplitudes are
u=Ghat+rho Delta/2 and v=-rho Delta/2. The FULL constant data row has

    u_empty=1-a eta-d, v_empty=d.

On the nonconstant rows, (2) gives

    q_star=2a eta-a^2 eta^2-rho a^2 eta e
             +rho^2(a e-a^2 e^2/2),
    b_star=rho^2 a e(2-a e)/4,
    q_star<=2a eta+rho^2 a e.                            (3)

Thus the coefficients change after a data query; reusing the balanced
moments verbatim would be invalid. Equations (2)-(3) are their exact
conditional replacement.

## A uniform strict K4 bound

For masses x,y the erasure kernel obeys
Psi(x,y)<=y log2(euler(x+y)/y), by -(1-t)ln(1-t)<=t.
Use log-sum on (3), and the same bound on the constant row whose
derivative mass is d^2 and total mass at most one. Put theta=eta/e.
After dividing by d>0 this gives

    B_i/d <=2+rho log2(euler/(2-a e))
                +rho log2(1+2theta/rho^2)
                +d log2(euler/d^2).                    (4)

The passage from the exact coefficient rho(1-a e/2) to rho only
enlarges a positive logarithmic term. Compatible event geometry gives

    eta<=8e^2/25, theta<=8e/25.

Indeed t=sqrt(qr)<=1/2, eta<=t^2/2 and
e>=2t-(3/2)t^2>=(5/4)t. This geometric estimate survives arbitrary
core-data restrictions because the controls are unexposed and fresh.

For e<=1/8 and 0<a<=2, we have a e<=1/4, d<=1/8 and theta<=1/25.
Each term in (4) now has an exact elementary bound:

1. c<13/9: the first three positive atanh terms give
   ln2>2/3+2/81+2/1215=842/1215>9/13.
2. euler<87/32: its degree-four exponential sum is 65/24 and
   the remaining positive tail is at most 1/100. Consequently
   euler/(2-a e)<87/56, whose log2 is <13/20 because
   87^20<2^13*56^20. Multiplication by rho<=1 preserves this bound.
3. ln(1+x^2)<=x for x>=0, since the derivative of
   x-ln(1+x^2) is (x-1)^2/(1+x^2)>=0. Therefore the middle term
   is at most c sqrt(2theta)<(13/9)(sqrt2/5)<26/63,
   using sqrt2<10/7.
4. x log2(euler/x^2) increases on (0,1/8], its derivative being
   2log2(1/x)-c>0 there. The final term is therefore
   <(6+13/9)/8=67/72.

Adding gives

    B_i/d < 2+13/20+26/63+67/72=10063/2520<4.

All constant comparisons are checked by rational or integer arithmetic
in out/RATIONAL_SUMMARY.json. The analytic proof covers every positive
width, every j and all Boolean cores; the finite physical checks are
corroboration, not a bias continuum argument.

## First actual core-data reveal and exact owned influence

With alpha=2^-j, JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC,
and pi=eta+alpha e, direct physical edges give

    I(F)=a[j alpha e+(1-alpha)JB+alpha JC]+pi I(g),
    c_j(F)=I(F0 F1)/2
          =alpha[a(JD+(j-1)e)+e I(g)].                 (5)

The control part is scaled by a; the core part is not. These factors
are essential under a biased conditional core.

At any actual core query i, let g0,g1 be its two physical restrictions,
a0,a1 their deficits, and t_i=Inf_i(g). Then

    (a0+a1)/2=a,
    I(g)-(I(g0)+I(g1))/2=t_i,
    Inf_i(F)=pi t_i.

Applying (5) to BOTH children, with the original controls and reaches,
proves the exact face-price contraction

    c_j(F)-[c_j(F|i=0)+c_j(F|i=1)]/2=alpha e t_i
          <=pi t_i=Inf_i(F).                            (6)

The difference between these two quantities is eta t_i. This is an
identity about actual face costs, not an additional refundable credit
to spend alongside an already-used data influence account.

After the reveal, each child remains in the same e<=1/8 geometry and
(1) applies even if a0 or a1 is near 0 or 2. More generally, along ANY
finite adaptive history querying only S bits and core-data coordinates,
with W,U,V still unexposed, every queried live S bit is strictly K4-good.
Upon S failure its remaining S bits are irrelevant. Thus the actual
S-query bad-face bill is zero through these histories. No separator
reserve must be replenished at core-data reveals in this rare regime.

The core query itself has its full entropy decrement and both terminal
laws. We prove no bound for its erasure by its influence, and no payment
for data-query reference resets, minority KL or terminal entropy. When
W,U,V are later exposed the small-e geometry may change, and arbitrary
biased union descendants are outside (1). The first unsupported line is
payment of that actual data-query or later-controller residual from a
genuinely unused inherited child/core bank, with all terminal laws and
prescribed reference costs kept on the same account.
