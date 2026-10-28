# No universal full-source price for this canonical reference

For every integer r>=2 set m=2^(r+2), and take the ACTUAL Boolean function F_{h_{m,r}} defined in PROOF.md. Its dimension is3+r 2^(r+2). Use exactly the same matched-empty/marginal canonical occupancy reference Q. Then

    CE(P,Q)/I(F) > r-1,       H(F)<=4I(F).             (7)

Therefore no finite dimension-independent K bounds this prescribed full reference price by K I, even inside an elementary FEI-certified Boolean family. The full conjecture remains open; this is not a Boolean unbounded-H/I family. It rules out an unqualified complete canonical source payment for any fixed rate, not merely rate4. A selected transaction or different reference may avoid the full bill.

Here delta=2^-r, t=(1-(1-2delta)^m)/2 lies in(0,1/2), v=1-(1-t)^2/4 lies in(3/4,15/16). Data marginals of F are delta/2, repeated mr times. Put K_data=mr delta/2=2r. At c=1/2, ignore the control factors, which are<=1. The product in the normalizer equation is at most

    (1-delta/(4v))^(mr) <=1/(1+mr delta/(4v))
                         <=1/(1+r) <=1/3<1/2.

The middle inequality follows from (1-u)^(-k)>=(1+u)^k>=1+ku for0<u<1 and integer k>=1. All denominators are positive; u=delta/(4v)<1. The decreasing telescoping-product function from PROOF section1 therefore places the unique positive canonical c above1/2. In particular log2 c>-1 and c<1.

In the exact cross-entropy formula(1), every term except -v log(v/c) is nonnegative. That exceptional term is v log c-v log v>-v>=-1. The repeated data-selected contribution alone is

    -(mr delta/2) log(c delta/(2v))
      = K_data log(2v/(c delta)) > K_data r = 2r^2,

because2v/c>1. Thus CE>2r^2-1. On the other side I0=1+t/2+K_data<5/4+2r. Since2r^2-1>0,

    CE/I0 > (2r^2-1)/(2r+5/4) > r-1.

The final strict rational inequality has numerator difference3r/4+1/4>0. This is an all-integer-r proof with explicit dimension; no limit interchange or enormous table is used.

For the actual entropy, formula(3) implies H0<=4+Hh/4: p0,t^2/4 lie in[0,1/4], so each -p log2 p<=1/2 (the function increases there, since ln4>1); the two doubled control contributions total<=2. Also mu^2 log(mu^2)<=0 and1-mu^2<=1. The two a-atoms contribute1. Finally tensor additivity and the elementary point-factor certificate give Hh<=4Ih, with Ih=2mr delta. Hence

    H0 <=4+Ih <=4(1+t/2+Ih/4)=4I0.

The same point certificates hold for every data restriction; the b0 terminal and all queried data terminals retain their full entropy. For any proposed fixed rate C>=4 they have nonnegative S_C. Its sharp signed full-source payment is possible only if CE<=C I0 by the exact ledger identity. Choose integer r>C+1 in(7); this fails with no earlier booking or reference reset. This is a genuine complete-price obstruction, not conservative-only overpayment.

The precise universal step now known false is: the complete coordinate-product canonical occupancy law of every supplied core can be paid by K times its root influence for some absolute K. The surviving task is to preserve core correlations in a normalized reference or bound only an explicitly selected inherited transaction. A036 already reports qualitatively that rare-core canonical prices can diverge; (7) supplies an explicit disjoint-block FEI-certified family, a quantitative all-r bound and exact full-owner consequences. No priority over that qualitative observation is claimed.
