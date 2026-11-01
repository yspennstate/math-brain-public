# A decreasing output-entropy budget pays arbitrary return/escape words

All entropies and logarithms are in bits. All inner cores are actual nonconstant Boolean signs on arbitrary finite uniform cubes. Let b(g)=min(P(g=-1),P(g=+1)) and R(g)=H(g)/I(g), where H is the entropy of the complete squared Fourier law and I total physical influence.

The six-bit gate h is negative exactly at indices {0,1,2,4,8,16,32,6,17,40}; a one bit denotes a negative input. Write J(x)=-h(x xor1). Every substitution uses six identical independent copies on disjoint physical supports, and its output is reoriented to its minority. At each step permit either:

* the common policy: feed the minority-negative core to h when b<=7/32, and its complement when b>7/32;
* the escape policy: feed the minority-negative core to J when b<=1/16.

No restriction is imposed on how often these operations alternate or on the finite word length. The result below does not require erasure monotonicity, finite moderate escape, or any FEI hypothesis.

The single flipped block can be any of the six: matching-pair swaps and pair permutations act transitively on h's inputs, and the six identical disjoint cores permit the induced physical block permutation. This preserves all scalar entropy/influence quantities used below. J itself is not transitive; its six pivotal probabilities are kept separate.

## Theorem

Define Psi(g)=h2(b(g))/I(g). For every starting core g0 and every finite admissible word producing g_d,

    0<=Psi(g_d)<=Psi(g0)<=1,
    sum_(s<d) |R(g_(s+1))-R(g_s)|
               <=64[Psi(g0)-Psi(g_d)]<=64.             (T)

In particular R(g0)-64<=R(g_d)<=R(g0)+64, with the complete initial R(g0) retained. Thus repeated legal escape/return cycles from a fixed finite seed cannot yield unbounded H/I, or unbounded E=min_i B_i/Inf_i. The theorem is a composition ledger, not a physical restriction-tree payment and not an absolute bound on an arbitrary starting core.

If g0 is already rare, b(g0)<=1/16, its absolute variation budget is at most44. Indeed edge isoperimetry gives I>=2p log2(1/p), while h2(p)<=p log2(1/p)+p log2(e). Thus Psi<1/2+3/[4log2(1/p)]<=11/16, and64 Psi<=44. This only sharpens the relative bill; the starting R remains present.

## 1. The potential comes from output entropy, not spectral entropy

For independent input bits with common negative probability a, let k be any Boolean outer gate, p'=P_a(k=-1), q_j its physical pivotal probabilities and Q=sum q_j. Entropy tensorization of the indicator of its negative set, and separately of its complement, yields

    h2(p')<=Q h2(a).                                  (1)

Indeed in a fiber where the selected coordinate is not pivotal, both conditional indicator entropies vanish. In a pivotal fiber their sum is h2(a), independently of which endpoint is negative. Summing gives (1). Tensorization follows by induction from the log-sum inequality (convexity of Ent under averaging); zero fibers follow by continuity. The same argument applied to the actual uniform input bits of g gives h2(b(g))<=I(g), because each pivotal two-point fiber has output entropy one. Hence 0<Psi(g)<=1 for every nonconstant actual core.

For the selected actual gate define the nonnegative scalar deficit

    D_k(a)=Q h2(a)-h2(p').                              (2)

Physical edge counting gives I(g')=Q I(g), since each inner coordinate changes the gate precisely on pivotal configurations of the independent other blocks. Input/output complementation preserves h2(b) and I. Therefore

    Psi(g)-Psi(g')=D_k(a)/(Q I(g))>=0.                 (3)

Q>0 for the gates here at every interior bias, so every relevant inner coordinate stays relevant. These facts involve output randomness; no independence assumption is made on the inner squared Fourier law.

## 2. Complete spectral terminal identity

Put m=1-2a, v=4a(1-a), let H_a(k) be the entropy of its normalized biased Fourier law, and let rho be the core's normalized nonempty spectral law. Every physical spectral set uniquely specifies its occupied blocks and the nonempty inner spectral set in each. The expected number of occupied blocks is vQ. Thus

    H(g)=h2(v)+v H(rho),
    H(g')=H_a(k)+vQ H(rho)=Q H(g)+C_k(a),
    C_k(a)=H_a(k)-Q h2(v).                             (4)

In particular

    R(g')-R(g)=C_k(a)/(Q I(g)).                        (5)

This retains the entire starting core entropy and the signed correction. Formula (4) is not derived by dropping a signed empty coefficient. In the raw biased multilinear expansion each coefficient a_T is an average of a mixed Boolean derivative and satisfies |a_T|<=1. The normalized mass is v^|T| a_T^2; hence

    H_a(k)>=vQ log2(1/v),
    C_k(a)>=-Q[-(1-v)log2(1-v)]>=-Q v log2(e).         (6)

For upper bounds, spectral-bit marginals are vq_j. Subadditivity and

    h2(vq)<=q h2(v)+v h2(q), 0<=v,q<=1,

give C_k(a)<=v sum_j h2(q_j). The scalar inequality follows because the difference vanishes at q=0,1 and has second derivative -v(1-v)/[ln2(1-q)(1-vq)]<=0. The weaker lower bound C_k>=-Q h2(v) follows simply from H_a(k)>=0.

It now suffices to prove, on every permitted gate/bias pair,

    |C_k(a)|<=64 D_k(a).                              (7)

Then (3),(5) pay the absolute cost of every level by one nonnegative potential drop, and summation proves (T). No fixed constant is charged anew for each excursion.

## 3. Rare endpoint for the common gate

For a=p in (0,1/16], exact pivotal counting and output enumeration give

    Q_h(p)=12p(1-p)^3(2-p)
           =24p-84p^2+108p^3-60p^4+12p^5,
    tau(p)=P_p(h=+1)=12p^2-28p^3+27p^4-12p^5+2p^6.

The event h=+1 requires some unmatched negative pair; there are twelve. Hence 0<tau<=12p^2. Q_h>=24p-84p^2>0, since its remaining polynomial is positive on this band. Write L=log2(1/p) and ell_e=log2(e), with 1<ell_e<3/2. Since

    h2(p)>=pL+ell_e(p-p^2),
    h2(tau)<=12p^2 log2(e/(12p^2)),

the deficit obeys

    D_h(p)>=p^2[12log2(12)-84pL
                      +ell_e(12-108p+84p^2)]
             >(105/4)p^2.                             (8)

For the last bound, log2(12)>7/2, pL<=1/4, and the last parenthesis is at least12-108/16=21/4>0. Use ell_e>1 and drop the positive84p^2. The entropy upper bound used here is h2(x)<=x log2(e/x); x log2(e/x) increases for x<=1. Both arguments lie below one. The lower bound for h2(p) uses -ln(1-p)>=p.

Here is an independent rare spectral envelope. The raw singleton coefficient of the monotone decreasing sign h is -q, where q=Q_h/6 and 3p<=q<=4p. With ell(x)=x log2(1/x), expansion of (4) cancels every log(v) term exactly:

    C_h=ell(P_empty)+sum_(T nonempty) v^|T| ell(a_T^2)
                                     -Q_h ell(1-v),
    P_empty=(1-2tau)^2.                                (9)

All raw coefficients obey |a_T|<=1. Since1-P_empty<=48p^2, its entropy is <=72p^2. For singletons, ell is increasing on[0,1/16], q^2<=(4p)^2, v<=4p, and p(2L-4)<=1/4; their sum is <=96p^2. For |T|>=2 use ell(a_T^2)<=1/(e ln2)<9/16 and sum_(k=2)^6 binom(6,k)v^k<=(5385/256)v^2, giving <=(48465/256)p^2. The last term has magnitude <=Q_h v ell_e<=144p^2. Consequently

    -144p^2<=C_h(p)<=360p^2.

Together with (8), |C_h|/D_h<360/(105/4)<14<64. The argument applies to all real p in the rare interval, not just the rational fixtures. Elementary constants follow from e's factorial series and ln2's positive atanh series.

## 4. Rare endpoint for the one-flip escape

Direct enumeration of the actual J gate gives negative counts by weight [0,4,10,18,15,6,1], and therefore

    sigma(p)=P_p(J=-1)=4p-10p^2+18p^3-19p^4+10p^5-2p^6.

For0<p<=1/16, 3p<sigma(p)<4p<=1/4. Also

    sigma'(p)=4-20p+54p^2-76p^3+50p^4-12p^5
                  >=4-20p>0.

Differentiating the product measure shows sigma' is the sum of SIGNED pivotal contributions, so sigma'<=Q_J. No transitivity is asserted for J; all six pivotal polynomials are independently enumerated. Using the same entropy inequalities as above,

    D_J(p)>= (4-20p)[pL+ell_e(p-p^2)]
                         -4p log2(e/(4p))
             =p[8-20pL-ell_e(24p-20p^2)]
             >(3/4)p.                                 (10)

Here pL<=1/4 and ell_e<3/2 give8-5-9/4=3/4, after dropping the favorable20p^2 term.

At the dominant all-zero assignment of the other five outputs, any selected direction has a fixed pivotal status. The probability of any nonzero assignment is <=5p, so min(q_j,1-q_j)<=5p. The entropy upper bound from Section2 yields

    C_J(p)<=6v h2(5p)<=120p^2 log2(e/(5p)).

The function p log2(e/(5p)) increases for p<1/5 and at p=1/16 is below1/4, since16e/5<48/5<16. Thus C_J/D_J<40. For the negative side, (6), Q_J<=6, v<=4p and ell_e<3/2 give C_J>=-36p, whence -C_J/D_J<48. This proves (7) for every permitted escape bias and handles a nontransitive gate's entire physical-coordinate spectrum. It does not assume nonnegative erasure admission.

## 5. Compact common-gate biases: an exact real-domain certificate

The remaining chosen common-gate input probabilities are a in[1/16,7/32] or[1/2,25/32]. Matching transitivity gives q_j=Q_h/6. The actual output probability polynomial is alpha(a)=1-tau(a). On each of128 fixed adjacent rational intervals in each band, the checker computes exact Bernstein bounds on Q_h, alpha and v=4a(1-a). It evaluates binary entropy endpoints with192-bit outward logarithms; if a binary-entropy interval crosses1/2 its upper bound is exactly one. Binary entropy's monotonicity on either side of1/2 justifies these interval enclosures.

For each interval the recorded deficit lower bound is

    D_lower=Q_lower h2(a)_lower-h2(alpha)_upper>0.

The recorded positive/negative C envelopes are respectively

    C_upper=6v_upper h2(Q/6)_upper,
    (-C)_upper=Q_upper h2(v)_upper.

Every one is <=64 D_lower. The largest certified envelope-to-deficit quotient is approximately19.195542; every exact rational quotient, D interval and envelope is stored in out/COMPACT_PAYMENT_CERTIFICATE.json. The pre-frozen threshold was64. Adjacent equal subdivisions cover BOTH complete closed bands, including boundary input biases and the balanced point. These are continuum certificates, not point samples. Combined with Sections3-4 they prove (7) on every allowed operation.

## 6. One normalized ledger, all words and complete terminals

At every legal step, the exact identities and certified bound imply

    |C_s|/(Q_s I_s)<=64[Psi(g_s)-Psi(g_(s+1))].

The right side is nonnegative. Summing over ANY finite word telescopes once to64(Psi(g0)-Psi(g_d)). The signed correction is still the exact sum C_s/(Q_s I_s); its absolute variation is bounded by the same single budget. Complements change no quantity in this formula. An arbitrarily small output probability, arbitrarily many visits to the moderate bands, or extremely long residence near the irrational fixed bias cannot create a new source account.

Since E(g) I(g)<=sum_i B_i(g)<=H(g), the bounded H/I orbit also bounds E from a fixed seed. This does not turn a seed's finite high erasure into a universal E bound. Nor does replacing the starting seed by arbitrary unknown g remove its retained ratio from (T).

The existing A080 actual rare core provides a source-bound check. Reconstruct g0=h, g1=h(g0^6), g2=h((-g1)^6), g3=h(g2^6), including the exact bias, influence and retained H/I at every step. For its1296-bit g3, minority probability is approximately0.02227493483. The actual7776-bit child J(g3^6) has negative probability approximately0.08433232901, hence it escapes the rare band in one step. Its signed normalized entropy increment is approximately0.006438799895, bounded in both directions by64 times the independently computed potential decrease. The initial available total mixed-word budget64 Psi(g3) is approximately6.584285156. An exact outward interval proves R(g3)+64 Psi(g3)<12, so EVERY finite admissible mixed descendant of this fixed rare seed has H/I<12. This is an analytic all-word corollary of(T) after an exact seed certificate, not a depth extrapolation. No new erasure-value or admission claim is made for the child. The exact endpoints and regenerated recursive circuit are in out/EXISTING_HIGH_E_CORE_ONEFLIP_PAYMENT.json.

## 7. Independent acceptance of A089's fixed-policy bill

A089-PAID-MODERATE-PREFIX-AND-COMPLETE-TERMINAL-LEDGER@1 is independently accepted at its unchanged scope, without repair. Its exact gate identities and probability/pivotal polynomials are reconstructed here. The critical payment and constants can be checked without importing its code:

On the ordinary moderate band, q'(p)=2(1-p)^2(2-10p+5p^2)>0, whose last factor at7/32 is53/1024. Therefore Q>=Q(1/16)=313875/262144>19/16; v/q<=65536/35625<2. Section2's entropy envelopes give -1<=C/Q<=2. The reciprocal-influence drop Delta=(1-1/Q)/I then pays signed increments between -(19/3)Delta and(38/3)Delta. Edge isoperimetry I>=2b log2(1/b) gives I>=1/2 on the moderate band, so every ordinary segment costs between -38/3 and76/3.

The policy has at most one ordinary segment and two complemented steps: b(p)=p^4(3-2p^2)<=5/32 from an initial p>7/32; the only subsequent upcrossing is below tau(7/32)<3/8 and b(3/8)=7047/131072<1/16. Rarity is then absorbing. At complemented inputs a=1-p, Q=12p^3(1-p^2)>=1003275/8388608>1/9, so C/Q<8 and C/Q>=-1; I>=1/2 bounds each complemented bill in[-2,16]. This yields the source prefix interval[-50/3,172/3]. Its dyadic fixed-point escape follows from the same irrational quintic root previously reconstructed by A075; the entropy bound itself covers every partial prefix without requiring termination.

The edge-isoperimetric estimate used here has a direct tensorization proof: for the minority indicator1_A, Ent(1_A)=p log2(1/p). In a uniform two-point fiber, Ent_i(1_A)=1/2 exactly when that fiber crosses A, and is zero otherwise. Therefore Ent(1_A)<=sum_i E Ent_i(1_A)=I/2. Concavity of2p log2(1/p) gives the claimed lower1/2 over the entire moderate minority band. This introduces no FEI premise.

For the improved rare upper envelope in that source, w=Var_a(h)<=48p^2 and at most63 nonempty atoms give H_p(h)<=48p^2 log2(63e/(48p^2)). Also Qv=48p^2(1-p)^4(2-p)>=96p^2-432p^3 and h2(v)>=v log2(1/v). Subtraction gives

    C_h<=p^2[48log2(63e/48)+192+432p(log2(1/p)-2)]
          <342p^2,

since63e/48<4 and p(log2(1/p)-2)<=1/8. Equation(6) supplies the source's negative envelope without incorrectly bounding the entire h2(v) by v log(e). With r=I/p, q>=3p and tau<=12p^2 give r_next>=3r/2; Poincare gives r_start>=15/4. The signed tail costs lie between -6/r and19/r, summing to[-24/5,76/5]. Adding the prefix yields[-322/15,1088/15]. Every displayed source constant is independently checked rationally, and the rare envelope is checked on the frozen rational profiles. No substantive repair is supplied, so this is an independent review rather than contributor acceptance.

## Exact first unsupported universal line

The missing full-FEI line remains a dimension-independent bound on the arbitrary starting actual core's E or H/I, or an independently certified operation that funds that starting bill. This stage closes the repeated-excursion ENTROPY budget for the named two-gate strategy; it does not prove repeated erasure reserves are nonnegative, and does not bound the rare-core supremum from the localization theorem. Arbitrary shared-data substitutions, gates outside the frozen library/domain, and physical stopping-tree queries require different ownership proofs. A finite seed's entire admissible mixed orbit is now analytically ruled out as an unbounded-ratio family; finite search nonfailures play no role in that conclusion.
