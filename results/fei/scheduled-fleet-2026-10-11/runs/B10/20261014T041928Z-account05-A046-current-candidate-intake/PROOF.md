# Actual-row filtering closes the width-dependent separator debit

All laws are physical uniform cube laws. Entropy is in bits. Put c=1/ln2.
Let S,W,U,V be independent compatible point indicators on disjoint blocks
of positive widths s,L,R,T, and let g be any independent balanced Boolean
sign. Define B=WUV, C=U OR V, D=C-B, A=B+S D, F=1+A(g-1).
The physical stopping policy exposes S until failure or completion, then
resolves B or C and stops at a constant or at the actual unchanged g.

Set q=2^-R, r=2^-T, eta=2^{-(L+R+T)}, beta=q+r-qr, e=beta-eta.
The two branches of the fresh point switch are G=1+B(g-1) and
H=1+C(g-1), with EG=1-eta, EH=1-beta and Pr(G!=H)=e/2.
Every live point-selector layer uses these same underlying branches.

## 1. The scalar inequalities and exact row split

For masses a,b>=0, the binary erasure kernel obeys
Psi(a,b)<=b log2(euler(a+b)/b), by -(1-t)ln(1-t)<=t.
Log-sum yields sum Psi(a_T,b_T)<=b_* log2(euler q_*/b_*)
where b_*=sum b_T and q_*=sum(a_T+b_T); zero masses use limits.

At a live query with j separator bits remaining, put rho=2^{-(j-1)}
and d=rho e/2. Parseval gives sum Delta_T^2=2e for
Delta_T=Hhat(T)-Ghat(T). The nonempty residual-selector frequency rows
contribute exactly 2(1-rho)d to B_j, as in the independently accepted
paired-row argument in stage 4. The remaining rows have coefficients
u_T=Ghat(T)+rho Delta_T/2 and v_T=-rho Delta_T/2.

Separate the full empty DATA frequency T=empty from those remaining rows.
Its coefficients are u_0=1-eta-d, v_0=d. Thus b_0=d^2 and q_0<=1.
Its erasure contribution divided by d is at most

    d log2(euler/d^2).                                   (1)

On all nonconstant DATA frequencies, including every nonempty controller
or core frequency, exact Boolean identities give

    sum Ghat(T)^2=2eta-eta^2,
    sum Ghat(T)Delta_T=-eta e,
    sum Delta_T^2=2e-e^2.

Indeed E[G(H-G)]=EGH-1=-e; the empty-frequency contribution is
-(1-eta)e. Subtract it to obtain -eta e. The other two identities follow
from G^2=1 and the full Parseval identity after removing Delta_0^2=e^2.
Consequently the exact masses on these rows are

    q_*=2eta-eta^2-rho eta e+rho^2(e-e^2/2),
    b_*=rho^2 e(2-e)/4,
    q_*<=2eta+rho^2 e.                                  (2)

This is a full constant-row split. It does not replace a Fourier reference
or use a marginal entropy estimate for the whole coordinate. It holds for
every balanced independent g, including non-flat or high-entropy cores.

## 2. Small event density forces every layer to be K=4-good

Let theta=eta/e. With t=sqrt(qr)<=1/2, eta<=qr/2 and

    e>=q+r-(3/2)qr>=2t-(3/2)t^2>=(5/4)t.

It follows that eta<=8e^2/25 and theta<=8e/25. Assume 0<e<=1/8.
Using log-sum in (2), dividing by d and enlarging its positive coefficient
rho(1-e/2) to rho, the nonconstant-row contribution is at most

    rho log2[(4euler/(2-e))(1+2theta/rho^2)].

Combined with the exact nonempty residual-selector contribution and (1),

    B_j/d <= 2+rho log2(euler/(2-e))
                 +rho log2(1+2theta/rho^2)
                 +d log2(euler/d^2).                    (3)

The following elementary bounds make (3) uniform in rho and all widths.
First c<3/2 because ln2>2/3, the first positive atanh term for ln2.
Also euler<11/4: its exponential sum through degree four is 65/24,
and the remaining tail is at most (1/120)/(1-1/6)=1/100.
Thus euler/(2-e)<=22/15<3/2<2^{2/3}, and the first variable term
in (3) is less than 2/3 since rho<=1.

For x>=0, ln(1+x^2)<=x; the derivative of x-ln(1+x^2) is
(x-1)^2/(1+x^2)>=0 and the value at zero is zero. Therefore

    rho log2(1+2theta/rho^2)<=c sqrt(2theta)
          <(6/5)sqrt(e)<=6/(5sqrt(8))<9/20.

The final strict inequality uses sqrt(8)>8/3. Finally d<=1/16,
and x log2(euler/x^2) increases on (0,1/16] (its derivative is
2log2(1/x)-c>0). Hence the last term in (3) is less than
(8+3/2)/16=19/32. Combining proves

    B_j/d < 2+2/3+9/20+19/32=1781/480<4                  (4)

for EVERY live layer j. There is no lower bound on e or on d.
In particular min(R,T)>=4 implies e<=q+r<=1/8, so all separator queries
are strictly K=4-good regardless of s,L or the core dimension.

## 3. Modified reserve and an absolute localized price

Retain the accepted exact physical accounts from A046 v1 (independently
accepted by A040 without repair). Write alpha=2^-s,
JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC, pi=eta+alpha e.
Then

    I_sep=s alpha e,
    I_other=(1-alpha)JB+alpha JC,
    I_terminal=pi I(g), I(F)=I_sep+I_other+I_terminal,
    E H(terminal)=pi H(g).                              (5)

The actual child-product face cost at a live layer is
c_j=2^-j[JD+(j-1)e+e I(g)]. It is never billed when that node is good.
Define a fixed root parameter

    m_*=0 if min(R,T)>=4;
    m_*=ceil(log2(min(R,T)+2))+2 otherwise.

Then m_*<=5. In the second regime the already accepted paired-row cutoff
proves layers j>m_* good. In the first regime (4) proves EVERY layer good.
At live state j put M_j=min(j,m_*) and

    W_j=2^-j[M_j JD+e M_j(M_j-1)/2+M_j e I(g)], W_0=0.

Set W to zero on separator failure. The fair success child has W_{j-1}.
The exact drift is c_j if j<=m_* and zero otherwise. Thus the actual
bad-layer cost is at most that drift. This transports one declared
reserve, with no root budget reopened at later layers. Finite summation
gives Q_bad,separator<=W_s and no leftover terminal separator reserve.

For M=min(s,m_*), alpha JD<=I_other and alpha e I(g)<=I_terminal.
Therefore, treating M=0 separately,

    Q_bad,separator<=W_s
      <=M I_other+max(M-1,0)I_sep/2+M I_terminal
      <=5 I_other+2 I_sep+5 I_terminal<=5I(F).           (6)

The point-conjunction and U OR V descendants are strictly K=4-good by the
previous reconstructed descendant argument, so (6) is the entire control
prefix localized bad bill. Arbitrary terminal g may have its own bad
nodes if queried; those are not included, and its entropy is not erased.

In the rare regime min(R,T)>=4 the prefix bill is exactly zero, not just
bounded above by an envelope. In particular A040's envelope-obstruction
family w=2^h-2 has actual prefix bill zero for every h>=3. Its original
cutoff envelope still has V/I~log2(w); that obstruction remains true.
The modified reserve simply does not purchase these already-good faces.

## 4. Terminal-inclusive entropy, scope and the next unsupported line

Using B+JS entropy telescope and JS<=2d/ln2,

    H(F)<=(4+2/ln2)(I_sep+I_other)+W_s+pi H(g)
       <=(6+2/ln2)I_sep+(9+2/ln2)I_other+5pi I(g)+pi H(g).

If H(g)<=C0 I(g) is independently certified, then
H(F)<=max(9+2/ln2,C0+5)I(F). At min(R,T)>=4 the stronger zero-bill
bound is H(F)<=(4+2/ln2)(I_sep+I_other)+pi H(g).
These are certificates for this chosen physical prefix. They do not
improve A021's existing family-wide entropy constant at threshold 7;
the advance here closes its previously open threshold-4 price interface.

The signed root-spectral/output correction from stage 4 remains
C_T=J_tree-[h2(pi/2)-pi], under the declared coherent root-compatible
coupling. No new conditioning bank is supplied by (6), and no prescribed
witness, extra side information or reset is identified with that coupling.

First unsupported universal line: obtain such an owned debit for a general
shared-data point switch without the nested compatible-event geometry,
using genuinely unspent child/terminal surplus, and transport it through
nested selectors while retaining all original terminal spectra. The small
e proof crucially uses eta<=8e^2/25. At a bent/point-flip large-contrast
switch that inequality fails and a logarithmic local price can be real.
An unconditional replacement of q_* by O(e^2+rho^2 e) is therefore invalid.
