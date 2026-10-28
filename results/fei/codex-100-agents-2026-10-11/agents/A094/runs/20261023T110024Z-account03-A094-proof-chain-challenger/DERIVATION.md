# Full source-bank audit and a larger nonvanishing allowance

All costs are ideal bits, physical influences are uniform-cube influences, and complete divergence against a subprobability Q means D(P||Q)=CE(P,Q)-H(P), retaining the penalty -log2(sum Q). Full FEI remains OPEN.

## 1. Named target and original models

Target A086-NONVANISHING-ALL-FRONTIER-OLD-BOOKING-ALLOWANCE@1. Its dependency is the quantitative A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@2 source-prefix proof, its v1 padding proof, and A011-POINT-EDIT-GENERAL-ENVELOPE-ONE-USE-HISTORY@1 only at the general-envelope interface. All of these proof texts were read. A011 v3 is a distinct TWO-edit operation statement and is not blanket accepted by this audit. No source reference, rate, policy or old debit is replaced in the target theorem.

Let g be any nonconstant Boolean function on a>=1 source bits, with source subprobability R of mass s in(0,1], positive on true support, finite c=CE(P_g,R)<=C0 I_g, C0>=0. Add b>=2 padding bits and r>=1 point controls. Write n=a+b, p=2^-r,t=2^-n, rho=pt, q=b+r>=3, e=2^-q<=1/8 and w=2^-b<=1/4. Translate the edit point to0 and set F=g-2g(0)1_(all data and controls zero). The original rate is K=4C0+15, chosen ONCE. The prescribed data reference is

 Qdata=(Rpad+6rho U_n)/(1+6rho),

lifted by the TRUE conditional control-frequency distribution. Its full mass is(s+6rho)/(1+6rho). At each matching padding prefix use the same formula based on ORIGINAL R and residual data dimension. Unmatched padding branches keep original R embedded at zero unused frequencies. Once all padding is fixed, generate source models by the actual mass-preserving source inheritance from ORIGINAL R; matching source leaves receive their prescribed fresh floor and nonmatching siblings retain the inherited source model. Controls stay unqueried.

## 2. General envelope: no omitted control-entropy premise

For source coefficient A and edited-point phase z in{+-1}, the true data marginal after point edit is A^2-4rho z A+4pt^2. Young gives -4rho z A<=A^2+4p^2t^2, so qdata<=2P_g+6rho U_n. All data fibers are positive by completing the square: (A-2rho z)^2+4p(1-p)t^2>0. Thus the true conditional control kernel is defined everywhere, including source-zero masks.

Put beta=6rho. All log losses under the prescribed subprobability floor are nonnegative. Direct domination gives data CE<=2c+beta[2n+r-log2(6)+7], using log2(1+beta)<=2beta and beta<=3/2. The nonempty control-frequency mass is v=4p(1-p)t, uniformly distributed over2^r-1 nonempty labels. Its conditional entropy is no greater than its marginal entropy h2(v)+v log2(2^r-1). Using h2(v)<=v[log2(1/v)+log2(euler)], the log(1-p) terms cancel, since log2(1/v)+log2(2^r-1)=n+2r-2. Therefore this entropy is<=4rho n+8rho r. Combining and using log2(6)>=2 yields

 CE(F,Qfloor)<=2c+30rho(n+r).                 (1)

The auxiliary choice R=P_g gives ONLY the scalar entropy bound H(F)<=2H(g)+30rho(n+r). It is not substituted for any actual reference. Formula(1) requires only finite c for a residual positive-dimensional source, even when that residual function is constant.

## 3. Physical edges, source inheritance and full signed ledger

If d is the original pivotal degree at the edited source point, set E=2rho d and G=2rho(n-d+r). Literal edge counting gives I(F)=I_g+G-E. The incident source edges are distinct, hence I_g>=2d2^-a and E<=e I_g<=I_g/8. The minimum nonzero edge boundary of the a-cube is a, so I_g>=2a2^-a; induction by two sections proves this also when g does not depend on every coordinate. Consequently I(F)>=(7/8)I_g+G.

For a source reference Q of mass s and one physical source query, let m=(P0+P1)/2 and r_marg be Q with queried Fourier membership deleted. Set raw_j=r_marg*Pj/m on positive m fibers; choose the fair normalized posterior on true-zero fibers, retaining their entire reference mass. If Z_j=sum raw_j, define Qj=s raw_j/Z_j. Then Z0+Z1=2s, each Qj has mass s, and both Z_j>0. Direct likelihood disintegration gives

 Dparent-average Dchild=conditional spectral KL-average log2(Z_j/s)>=0.       (2)

The entropy decrement of a Boolean physical restriction is membership conditional entropy plus JS of the child spectra and is nonnegative. Thus every finite active source stopping tree, including every stopped sibling, obeys sum alpha_v D_v<=D and active alpha H_h<=H. Finite source cost ensures all needed true-positive ratios are finite. All source normalizers use the actual original s, not an implicitly normalized source.

For any actual prescribed models at physical nodes define lambda_v=average Dchild-Dparent. Its exact signed history ledger is

 L=CEroot+sum_internal reach(v) lambda_v
  =sum_internal reach(v) DeltaH_v+sum_terminal reach(v) CE_v
  =H(F)+sum_terminal reach(v) D_v.             (3)

This retains every previous signed charge and all complementary terminal CE/KL. Negative credits are part of this signed ledger; the theorem does not separately bound a history that discards all credits and sums only positive charges.

## 4. Full prefix-price dependencies, independently reconstructed

At a padding prefix of length ell>=1 the stopped copies of g have total reach1-2^-ell. The active floor has reach2^-ell. Equation(1) gives terminal CE<=(1+2^-ell)c+30rho(n+r-ell). For the j-th matching padding query, its physical pivotal probability is d_j=2rho2^j. Entropy decrement is<=h2(d_j)+4d_j/ln2<=d_j[log2(1/d_j)+9]. For completeness, the pairwise JS bound follows from log x<=x-1:

 [u^2 ln(u^2/m)+v^2 ln(v^2/m)]/2
 <=(u^2-v^2)^2/[2(u^2+v^2)]<=(u-v)^2,

where m=(u^2+v^2)/2; zero pairs contribute zero. Summing gives sum(u-v)^2=4d_j. The membership term is<=h2(d_j) by concavity. Also ln2>2/3 from its atanh expansion. These are direct inequalities, not an assumed influence-priced entropy theorem.

Using(3), with s0=a+b+r,

 L_ell<=(1+2^-ell)c+2rho T,
 T=15(s0-ell)+ell(s0+8)-ell(ell-1)/2.

Write T=(15+ell)a+J, J=(15+ell)q-7ell-ell(ell-1)/2. Since q>=ell+1, J>0. Dividing this POSITIVE remainder by a>=1 justifies T/a<=q^2+15q+7; one must not divide its negative terms separately. The ratio (q^2+15q+7)/2^q decreases for integer q>=2, since twice its numerator minus the next numerator is q^2+13q-9>0. This proves the original41/4 overhead at q2 and, with q>=3 here, the STRONGER61/8 overhead. Thus

 L_padding<=(3/2)c+(61/8)I_g.                 (4)

At an intermediate source prefix of depth1<=k<a, active reach is w2^-k, and residual source dimension a-k>=1. Source divergence contraction(2), entropy contraction, the scalar root entropy bound and the active floor bound give the quantitative source price

 L_k<=2(1+w)c+15[Broot+w2^-k B_h],
 Broot=2rho(a+b+r), B_h=2p2^(-(a-k))(a-k+r).

Explicitly the terminal divergence is<=(1+w)D+2wH+15w2^-k B_h; adding scalar root entropy gives the displayed cost. All nonmatching source siblings remain. No conditional c_h<=C0 I(h) is used. Minimum source boundary gives

 [Broot+w2^-k B_h]/I_g<=2^-q[2+(b+2r-k)/a]
 <=(q+1)/2^q<=1/2,

using a>=2,k>=1, q>=3. Since w<=1/4,

 L_source<=(5/2)c+(15/2)I_g.                  (5)

At the root, L_root<=2c+15(G+E). At final source collapse the inherited source model is the single atom s, not a free normalized atom. Its prescribed scalar floor is(s+6p)/(1+6p)>=s, so edited-terminal divergence<=-log2(s)<=D. Consequently L_final<=H(F)+D<=2c+15(G+E) as well. This covers a1 (no intermediate source prefix) and all constant residuals without a dimension-zero application of(1).

An independent untouched finite-cost subprobability terminal remains fully additive, with masses multiplying. Product-compatible likelihoods on its true-zero labels ensure core normalizers remain unchanged. Its cost cannot pay any core booking.

## 5. Audit verdict and stronger all-frontier allowance

Using the original weaker41/4 padding and45/4 intermediate overheads recovers the complete A086 statement: KI(F)-L>=(C0+15/8)I_g and old U<=(C0+1)I_g leaves>=7I_g/8 at every old frontier. No repair to A086 or its source interface is supplied. The new conclusion below is separately authored.

Retain the stronger q>=3 overheads(4),(5), the SAME original K and the SAME physical I(F). The resulting unused margins before external U are:

 root and final: >=[(3/2)C0+45/4]I_g+4C0G;
 padding: >=[2C0+11/2]I_g+KG;
 intermediate source: >=[C0+45/8]I_g+KG.

For example, source coefficient7K/8-5C0/2-15/2=C0+45/8 and padding coefficient7K/8-3C0/2-61/8=2C0+11/2. All three margins are at least(C0+11/2)I_g for every real C0>=0,G>=0. Therefore EVERY old frontier admits the external booking

 0<=U<=(C0+37/8)I_g,

with remaining reserve>=7I_g/8>0. The allowance grows by29I_g/8 over A086's(C0+1)I_g, with exactly the SAME guaranteed residual. No reference, rate or original source supplier is renewed. This is an improved conditional payment theorem, not a universal initial supplier or an arbitrary-history positive-part bound.

## 6. Policy compatibility remains an actual unpaid step

A095's all-m>=8 rare-allowance obstruction concerns the actual canonical root and narrow-first policy. Its e1>1/10 is a physical complete-reference conversion charge, while its comparison cap U_star tends to zero. The present larger allowance removes that numerical sufficient-cap obstruction for compatible external U only. It does not identify A095's canonical history with these prescribed floor/padding-first models. A100's negative PROFILE/CALIBRATED charge likewise concerns a different ledger from A094's positive RAW canonical reset; it does not reverse the exact raw e3 sign1/128<e3<9/1024.

The next unpaid step is a genuine handoff between the actual incoming models and these prescribed models, including the reached signed conversion charge, previous bookings, source-entropy changes and both complete terminal costs, all against one original supplier. Arbitrary iteration at fixed padding/rate and the universal influence-priced source supplier remain unproved. Full FEI is OPEN.
