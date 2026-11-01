# The signed data debit after booking true future erasure

All entropies are in bits. G,H are Boolean signs on the same uniform data cube. An independent balanced Boolean sign h remains unqueried. Write F=(G+H)/2+h(G-H)/2, delta=Pr(G!=H), T=(H(G)+H(H))/2, J=JS(P_G,P_H), and B=H(S_z|S_data) for the uniform one-bit shadow. Let e be any fixed real booked inherited encoder allowance per unit disagreement.

## 1. Exact debit, at arbitrary data histories

The empty encoder sector has squared coefficients ((Ghat+Hhat)/2)^2. Every nonempty encoder frequency U has squared coefficient hhat(U)^2((Ghat-Hhat)/2)^2. Since h is balanced and Parseval gives sum_U hhat(U)^2=1, the conditional nonempty encoder spectrum is exactly P_h, independent of the data frequency. Its mass is delta. Therefore

    H(F)=T+J+B+delta H(h).                         (1)

No division is made at zero delta; the sector contributes zero there. At a data query i, delta is harmonic under its two physical restrictions. Write child average with E_i. From (1),

    [Delta_i H(F)+E_i B-B-Delta_i T] = J-E_i J.   (2)

Adding the harmonic booked term e delta changes neither side. For every finite adaptive DATA-ONLY stopping tree, with physical reaches w_v,

    sum_v w_v signed_debit_v = J_root-E J_leaf.  (3)

In particular this entire signed debit is at most 1 bit, regardless of the number of queries, since 0<=J<=1. Individual positive parts need not obey this bound; signed refunds and the same root account must be retained. The result is structural transfer, not an influence bound or a universal choice of a good coordinate. Querying inside h invalidates the fixed balanced-encoder hypothesis.

## 2. No fixed local influence price for this booked debit

For even m>=4 put t=2^-m and q_m(r)=(-1)^(r1*r2+...+r_(m-1)*r_m). Its Fourier squares are all t, by multiplying the four-coefficient two-bit quadratic spectra. On (j,r) set G=1-2*1_{j=0,r=0}, H=q_m(r). Take h=Maj3. These are actual signs; G,H and both actual j-children of F are nonconstant. Their full spectra include the empty atoms. If every one of the four ORIGINAL branch restrictions after j must also be nonconstant, multiply G and H by the same fresh dictator. This shifts all Fourier labels bijectively, preserving H,J,B,delta and every j charge, while adding one to each branch influence. All conclusions survive and the terminal surplus increases by four.

Set Phi(x,y)=(x+y)h2(x/(x+y)), continuously zero for a zero argument. For normalized P,Q,

    JS(P,Q)=1-(1/2)sum Phi(P_s,Q_s).

The dummy-j bent branch has mass t at each j-free frequency and zero otherwise. The point branch has empty mass a=(1-t)^2 and every other mass t^2. After querying j its branches are 1 and the m-bit point sign, whose empty mass is b=(1-2t)^2 and other masses 4t^2. Thus the ACTUAL signed debit D=J-E_j J is

    D=Phi(1,t)/4+Phi(b,t)/4-Phi(a,t)/2
       +(t^-1-1)[Phi(4t^2,t)/4-Phi(t^2,t)/2].    (4)

We prove D>=t(m/2-3). Let beta=1/ln(2)<3/2 (ln(2)>2/3, from its atanh series). For f(s)=Phi(s,t), f'>=0 and -f''=beta*t/[s(s+t)]<=16 beta t on [b,1], because b>=1/4. The midpoint is (1+b)/2=a+t^2. Taylor's inequality for a twice differentiable function with f''>=-L gives its midpoint Jensen gap at most L(1-b)^2/8. Consequently the first three terms of (4), which equal half the endpoint average minus f(a)/2, are at least

    -16 beta t^3 >= -24t^3.                     (5)

Here 1-b<=4t, and moving from a to a+t^2 only increases f. The endpoints are positive for m>=4, so differentiation is legitimate throughout.

For x>0, Phi(x,t)=x log2(t/x)+(x+t)log2(1+x/t). The second summand lies between zero and beta*x*(1+x/t), by ln(1+u)<=u. Thus the nonempty-row term of (4) is at least

    (1-t)t[m/2-2-(3/4)(1+t)].                   (6)

Since m t/2<=1/8 for integers m>=4 (equality at4 and the ratio of successive terms is (m+1)/(2m)<=1), t<=1/16, and (1-t)[2+(3/4)(1+t)]<=11/4,

    D/t >= m/2-1/8-11/4-24/256
         = m/2-95/32 > m/2-3.                  (7)

The physical queried influence of F is d=t/2, since only G depends on j and h selects it with probability1/2. A028's same boundary bank R=I(GH)/2 releases t/2=d on this query. Therefore D/d>=m-6, and NO finite C makes

    signed booked debit <= C*d + release_R

hold at all actual data queries, even with this fixed non-point Maj3 encoder and independently price-four-certified nonconstant terminals. This sharpens the finite lower-price guard for a DIFFERENT bill: the future true B has already been booked. It does not refute A028's control-only theorem, any existential coordinate selection, or FEI.

## 3. The same original terminal owner nevertheless pays this history

Bent H has H(H)=m and I(H)=m/2, hence price-four surplus m. G is a point sign and H(G)<=4I(G): for a point of density p<=1/4, its exact entropy is eta((1-2p)^2)+8p(1-p)(n-1); eta((1-2p)^2)<=4 beta p(1-2p)<=8p; its influence is 2np. This proves the stated inequality including its empty atom.

Let S=4[I(G)+I(H)]/2-T be the single original terminal surplus. S>=m/2. For h=Maj3, H(h)=2, and the inherited allowance used in A026 stage6 is e=1. At the root book B+delta (the present disagreement probability is not the small point density t). Here E q_m=2^(-m/2), q_m(0)=1, so

    delta=(1-2^(-m/2)+t)/2 < 1/2.

It is essential NOT to confuse delta with t. The estimates B<=1, delta<1/2 give an initial booked margin greater than m/2-3/2. After any data-only stopping history, (3) leaves booked margin greater than m/2-5/2. The remaining ACTUAL encoder correction is E J_leaf + E delta_leaf[H(h)-e] = E J_leaf+delta_root. Adding it back gives the exact complete margin

    S-B_root-J_root-2delta_root
       >= m/2-3+2^(-m/2)-2^-m.                 (8)

For every even m>=6 this is at least7/64 bit: at m=6 the lower bound is7/64, while m>=8 gives a bound greater than1. This holds for every adaptive data-only history, keeping every full branch terminal entropy and the same original surplus. No local-price rule and no new root reserve is issued. The queried physical DATA influence is partitioned exactly into the path's queried influence and expected remaining data influence; S uses their sum once, not an extra copy at descendants.

This bound is deliberately dimension independent in its treatment of the actual controller correction; the growing bent surplus is a supplied terminal certificate, not a universal spare bank. Finite actual fixtures m=2,4,6 check exact margins separately; only m>=6 is admitted by the all-dimensional bank theorem.

## 4. First unpaid universal step

For arbitrary G,H the signed debit still telescopes as (3), but one bit can be enormous relative to an arbitrarily small original influence. The above family proves a local fixed-price repair is impossible for this booked bill. The missing universal line is to select a physical history and charge its signed J loss, future true erasure, inherited encoder entropy and BOTH full terminals to genuinely unused influence/terminal surplus, without presuming a bent-like bank or dividing by zero. Fixed data-only encoder balance is explicit; no mixed encoder/data theorem is asserted.
