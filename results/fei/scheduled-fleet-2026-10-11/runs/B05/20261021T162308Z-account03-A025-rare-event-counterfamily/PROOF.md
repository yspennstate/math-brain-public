# A paid second data query and the return of the rare-query obstruction

All entropies are in bits. All probabilities below are physical cube probabilities.
Let m>=4 be even, delta=2^-m, b(y)=(-1)^(y0*y1+...+y_(m-2)*y_(m-1)).
Use A025's original cores g0=zb, g1=zb(1-2 1_{x=0,y=0}),
g2=zb(1-2 1_{x=0,y=e0}), with independent balancing sign z.
Two fair controller bits select the three cores with ORIGINAL weights
pi=(1/2,1/4,1/4). Optionally activate every core with the SAME fresh
width-t point event, p=2^-t, t>=0. Inactive output is +1.

The policy queries x and, ONLY in its x=0 child, queries y0. It then
resolves the controls and stops at the actual conditioned cores. There
are three data-history leaves, of weights 1/2,1/4,1/4. Neither controller
weights nor the x=1 sibling are discarded. The bank at a history h is
R_h=2 sum_{j<k} pi_j pi_k I(g_j|h * g_k|h), with activation included.

## What is inherited, and what is checked here

A021 run20261014T075029Z, DERIVATION.md, final owner section supplies:
the control-only bill at any x child is at most R_h+10 IC_h; after the
x query its remaining bank is

    R_old=p(3m-1+3t)delta/4.

The positive x-query excess U=max(D_x-10d_x,0) has the independent bound
U<=p m delta/2. A021 books R_old and U against, respectively, delta/4
and delta/6 fractions of ONE actual surplus S8=8 IT-HT. Its x-query
entropy estimate follows from h2(delta/2)+2(log2 e)delta/2; it is not
an assumed terminal FEI inequality. The earlier all-constant local
release-price counterexample is unchanged.

Here both bounds are carried into the NEW leaf partition. There is no
second issue of those fractions, and no claim that S8 stays constant.

## The second query is paid without a terminal debit

Work first without common activation, in the x=0 child. The y0 edge
between 0 and e0 is nonpivotal in b. It becomes pivotal in either edited
core; the altered labels have total weight1/2. This edge occupies a
2delta fraction of oriented cube edges. All other y0 edges retain the
bent seed's pivotal status. Consequently

    d_y0=1/2+delta.

For every Boolean query, its true entropy decrement satisfies
D_i=B_i+JS_i, B_i<=h2(d_i)<=1, JS_i<=2(log2 e)d_i. The latter follows
from the two-amplitude Jensen inequality and Parseval; it is valid for
signed amplitudes by (|a|-|b|)^2<=(a-b)^2. Thus here

    D_y0 <= [2+2 log2(e)]d_y0 <5d_y0.

Each original conditioned sign and each actual child is balanced by z.
Balanced point activation scales both d_y0 and D_y0 by p, so the same
bound holds at every t. The second query consumes no additional part
of the terminal owner at rate10. This estimate is for this query; a
query of a seed-dummy coordinate need not satisfy its d>=1/2 admission.

For bank release, all terminal pivotal indicators agree except on the
single exceptional y0 edge. There q=sum pi_j pivotal_j=1/2. The exact
data release identity is 2 E q(1-q). Its value is delta, or p delta
with activation. Since the child has reach1/2, the NEW remaining bank is

    R_new=R_old-p delta/2=p(3m-3+3t)delta/4>=0.             (1)

The activation-direction bank remains present. Its value3pt delta/4
is in both R_old and R_new; none is counted as a y0 release.

## The same old debits fit the new complete terminal surplus

Let IT_new,HT_new be the weighted influence and entropy of ALL three
data-history leaves and ALL original controller labels. Write
S_new=8 IT_new-HT_new. Without activation, the x=1 leaf has I=1+m/2,
H=m. In x=0, the original weighted terminal influence is
1+m/2+(m-1)delta: the flip at0 adds2m delta and the flip at e0 adds
2(m-2)delta, each with weight1/4. The y0 query removes1/2+delta.
Therefore the average remaining terminal influence there is

    (m+1)/2+(m-2)delta.

Every terminal at that child is z times a sign on m-1 remaining data
bits. Its entropy is at most m-1 (z shifts the spectral labels).
Keeping the x=1 sibling gives the rigorous aggregate bound

    S_new,unactivated >=3m+13/2+4(m-2)delta.             (2)

For any balanced h, its activated entropy is p H(h)+A(t), and its
influence is p(I(h)+t), with A(t)<=p(4t+2 log2 e). All terminal reaches
sum to one, so (2), log2 e<3/2 give

    S_new >=p[3m+7/2+4t+4(m-2)delta]
          >=p(3m+1+4t)>0.                              (3)

The same original upper bounds, without renewal, now satisfy

    R_old <= (delta/4) S_new,
    U <= (delta/6) S_new,
    R_new+U <=(5delta/12)S_new <=(5/192)S_new.           (4)

Indeed 3m-1+3t<=3m+1+4t and m/2<=(3m+1+4t)/6.
We prove (4) using S_new directly, not an unsupported transport of
S_old into S_new. The ACTUAL already booked U is no larger than its
inherited bound; R_new is smaller than its inherited bound.

Each y0 child has just one surviving edited vertex on n=m-1 bits;
the other edited label now equals the seed. A021's distinct-vertex
theorem cannot simply be cited for that degenerate case. Here is a
direct proof, valid for ANY Boolean seed on n bits, balanced by z.
Write eta=2^-n, and let C be the appropriate two-literal AND indicator
of the altered label, with alpha=P(C)=1/4. The controller Fourier
coefficients of C have absolute value1/4 at every one of its four
frequencies. At each data label the nonempty-controller amplitudes
therefore have magnitude eta/2. The variance row is constant,
v_T=4eta^2 alpha(1-alpha)=3eta^2/4, so V=sum v_T=3eta/4.
Their raw entropy is Hplus=V(2n+2). The boundary bank is R=nV;
the actual controller influence is IC=eta.

For clarity the signed row refund is proved as follows. Let q_T be
the mixture of terminal squared coefficients; sum q_T=1 and q_T>=v_T.
For E(s)=s log2(1/s), concavity gives
E(q_T-v_T)-E(q_T)<=v_T log2(q_T)+(log2 e)v_T.
Since v_T/V=eta, Jensen gives sum v_T log2(q_T)<=-nV.
The mixture entropy J<=2(log2 e)IC follows from the elementary
one-bit entropy inequality Ent_nat(X^2)<=(a-b)^2/2 and tensorization
on the two controller bits (A021 Section independently reconstructed
A028 mixture bound). Hence the complete controller bill satisfies

    D_controls<=R+(2+log2 e)V+2(log2 e)IC
               <R+6IC.                               (6)

No terminal coefficient is divided by, so zero and unequal rows are
allowed. Activation scales the bill and IC by p and adds a nonnegative
activation capacity to R. All three old labels remain in R, including
the now coincident pair. The x=1 controller bill is zero. Thus the
complete NEW controller continuation is paid by R_new+10 IC.
Using (1)--(4), the actual physical tree telescope gives

    10 I(F)-H(F) >=2 IT_new+S_new-R_new-U
                  >=2 IT_new+(1-5delta/12)S_new>=0.

Equation (6) closes the distinct-vertex side condition directly; no
unproved distinct-to-coincident extension is used in this telescope.

## The next partner query recreates an unbounded local ratio

At history x=0,y0=0 (reach1/4), keep ALL three labels. Set a=delta'=4delta,
and let c be the quadratic bent seed on the remaining m-2 paired bits.
The actual sign is

    z c -2z 1_{y1=0,remaining bits=0} C1,
    C1=1_{label=1}, P(C1)=1/4.

The bit y1 is a dummy in c, but pivotal in the point edit. Thus d_y1=a/4=delta.
For empty controller frequency its paired Fourier amplitudes are
u=sqrt(a)sigma-a/4, v=-a/4. Their total mass is >=a/4, so
v^2 log2((u^2+v^2)/v^2)>=a^2 m/16. There are1/a such rows;
their erasure is at least m delta/4. Nonempty-controller amplitudes
in the two y1 sectors are equal; their derivative mass is3delta/4,
giving erasure3delta/2. Hence

    B_y1/d_y1 >=3/2+m/4,
    released_R/d_y1=3/2.                               (5)

The release uses q=1/4 on the exceptional data edge, not q=1/2.
Common activation scales B,d and release by p, since z remains in
every old Fourier label. For every finite K,lambda, (5) again defeats
D_y1<=K d_y1+lambda released_R when even m>4K+6(lambda-1).
This is the return of the same LOCAL obstruction after one paid
intervening query, not a new refutation of FEI or an existential policy.

All denominators used above are positive: m>=4, p,delta,a>0; the
Fourier mass bound uses sqrt(a)>=2a/4 for a<=1/4. At m=4 the reduced
bent seed still has two bits. At t=0 take A(0)=0. No limits of sums
are used. Choosing m in (5) is allowed to depend on K,lambda.

The universal unpaid step is to pay this next rare partner query
from an explicitly unused portion of the SAME final owner while
retaining its complementary sibling, actual terminals and old debit U.
