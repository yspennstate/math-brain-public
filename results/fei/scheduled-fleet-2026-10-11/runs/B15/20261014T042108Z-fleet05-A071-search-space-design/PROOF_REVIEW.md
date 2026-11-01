# Independent review of A075's output-entropy payment; price48 refinement

Verdict: A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET@1 HOLDS at its stated scope and unchanged statement hash329456072857a03fe4dfc64a015a86828e01fa2929c12c481e7b8d461f85c9de. No repair is needed. The proof below also establishes a scope-preserving quantitative refinement:48 replaces64,33 replaces the rare-start44 budget, and the existing actual g3 seed's whole admissible mixed orbit has H/I<10 rather than12. Acceptance of the original64 statement is distinct from independent review of this new48 corollary, which remains pending.

All entropies are bits. The gate h is negative exactly at {0,1,2,4,8,16,32,6,17,40}. Let J=-h(x xor1). The policy uses h on the minority-negative core when its minority probability p<=7/32 and on its complement otherwise; J is legal only when p<=1/16. Each step uses six identical cores on disjoint independent physical cubes, and the output may be complemented to orient its minority negative. Other sign patterns, gates, overlap, or physical restriction policies are outside this theorem.

## 1. An independent output-information proof of the potential

Let X_1,...,X_6 be independent input bits with negative probability a and let Y=k(X) for a deterministic Boolean gate k. The chain rule gives H(Y)=sum_j I(Y;X_j|X_<j). Independence and reduction of conditional entropy under extra conditioning imply

    I(Y;X_j|X_<j)
      =H(X_j)-H(X_j|Y,X_<j)
      <=H(X_j)-H(X_j|Y,X_-j)
      =H(Y|X_-j).

In a pivotal fiber H(Y|X_-j)=h2(a); otherwise it is zero. Consequently H(Y)<=Q h2(a), where Q=sum_j q_j is the sum of actual pivotal probabilities. In particular

    D_k(a)=Q h2(a)-h2(P(Y=-1))>=0.                      (1)

Applying the same inequality to a core g on its uniform physical inputs proves h2(p_min(g))<=I(g). Thus Psi(g)=h2(p_min(g))/I(g) lies in(0,1] for every actual nonconstant finite core.

Physical edge counting through independent disjoint blocks gives I(g')=Q I(g). Input/output complements preserve h2(p_min) and I. Therefore

    Psi(g)-Psi(g')=D_k(a)/(Q I(g)).                     (2)

This derivation uses ordinary output information. It never substitutes output entropy for spectral entropy.

## 2. Retain the complete spectral terminal

Write v=4a(1-a). Let s_T be the normalized biased squared outer Fourier law and rho the core's normalized nonempty squared Fourier law. A physical Fourier set determines its occupied blocks and the nonempty inner set inside each. These alternatives are disjoint. The expected number of occupied blocks is vQ. The exact Shannon chain rule on this hierarchical law yields

    H(g')=H_a(k)+vQ H(rho)=Q H(g)+C_k(a),
    C_k(a)=H_a(k)-Q h2(v),
    H(g')/I(g')-H(g)/I(g)=C_k(a)/(Q I(g)).              (3)

For later bounds, write the biased sign expansion as coefficients A_T times products of(y_j-Ey_j). Each A_T is an average of a normalized mixed Boolean derivative and hence |A_T|<=1. Its normalized squared mass is v^|T| A_T^2. Since expected degree is vQ, H_a(k)>=vQ log2(1/v). Defining ell(x)=x log2(1/x), this gives

    C_k(a)>=-Q ell(1-v)>=-Q v log2(e).                 (4)

Spectral-bit subadditivity and the concavity in q of

    q h2(v)+v h2(q)-h2(vq)

give the upper envelope C_k(a)<=v sum_j h2(q_j). Indeed this difference vanishes at q=0,1 and its second derivative is -v(1-v)/[ln2(1-q)(1-vq)]<=0. The weaker lower envelope -C_k<=Q h2(v) follows directly from H_a(k)>=0. These bounds do not presume coordinate transitivity for J.

## 3. Rare common-gate endpoint, every real0<p<=1/16

Direct gate counting gives

    Q_h=24p-84p²+108p³-60p⁴+12p⁵,
    tau=P_p(h=+1)=12p²-28p³+27p⁴-12p⁵+2p⁶.

The positive event requires one of twelve unmatched negative pairs, so tau<=12p². Also Q_h>=24p-84p² and every q_j=Q_h/6 lies in[3p,4p]. For L=log2(1/p), e2=log2(e), use

    pL+e2(p-p²)<=h2(p),
    h2(tau)<=12p² log2(e/(12p²)).

Combining gives D_h>=p²[12log2(12)-84pL+e2(12-108p+84p²)]>(105/4)p². To check the constants, log2(12)>7/2 follows from144>128; pL<=1/4 on this whole interval;1<e2<3/2; and12-108p>=21/4. The monotonicity of pL on this interval follows from its derivative L-e2>0.

The exact variance-log terms cancel in C_h, leaving

    C_h=ell(s_empty)+sum_(T nonempty) v^|T| ell(A_T²)-Q_h ell(1-v).

Here1-s_empty<=48p², so ell(s_empty)<=72p². Singletons have A_{j}=-q_j and contribute at most96p²: bound v<=4p,q_j<=4p, and p(2L-4)<=1/4 (the latter increasing up to1/16). For degrees>=2, ell(A_T²)<=1/(e ln2)<9/16 and sum_(r>=2)binom(6,r)v^r<=(5385/256)v², giving at most(48465/256)p². These estimates are quantitative and their sum is less than360p². Equation(4),Q_h<=24p and v<=4p supply C_h>=-144p². Thus

    |C_h|/D_h < 360/(105/4) <14.                       (5)

The inequalities1/(e ln2)<9/16 and1<e2<3/2 require only e>8/3 and2/3<ln2<1. They follow from the first four terms and a geometric upper tail of e's factorial series, and from ln2's positive atanh series. This endpoint is analytic, not inferred from rational profiles.

## 4. Rare one-flip endpoint; six pivotal types kept

The actual gate J has negative counts by Hamming weight[0,4,10,18,15,6,1], yielding

    sigma(p)=4p-10p²+18p³-19p⁴+10p⁵-2p⁶.

On0<p<=1/16,3p<sigma(p)<4p<=1/4. Its derivative is at least4-20p: the remaining quadratic-and-higher part is positive, since54-76/16-12/16³>0. Differentiating the product law counts signed pivotal events, so Q_J>=sigma'(p)>=4-20p. Using the previous binary-entropy estimates gives

    D_J>=p[8-20pL-e2(24p-20p²)]>(3/4)p.               (6)

For any selected direction the other five bits are all zero with probability at least1-5p. Pivotal status there is a fixed zero or one. Therefore min(q_j,1-q_j)<=5p for EVERY j, irrespective of unequal pivotal probabilities. The upper envelope from Section2 gives

    C_J<=6v h2(5p)<=120p² log2(e/(5p)).

The function p log2(e/(5p)) increases here and is below1/4, so C_J/D_J<40. Conversely(4) with Q_J<=6,v<=4p,e2<3/2 gives C_J>=-36p, so -C_J/D_J<48. Hence

    |C_J|<48D_J.                                      (7)

This48 estimate is already present in the source's endpoint analysis. Using it is a numerical tightening of the existing proof, not a repair of the valid64 theorem.

## 5. Compact common-gate domain reconstructed without Bernstein bounds

The remaining chosen h input biases lie in[1/16,7/32] or[1/2,25/32]. Each is partitioned into128 equal closed intervals[a,b], matching the exact endpoints in the source certificate. Our independent ranges use positive factorizations, not the source power-to-Bernstein conversion:

    Q_lower=12a(1-b)^3(2-b), Q_upper=12b(1-a)^3(2-a),
    alpha_lower=(1-b)^4(1+4a-2a²),
    alpha_upper=(1-a)^4(1+4b-2b²).

Each factor has its stated monotonicity and is nonnegative. Bound v=4p(1-p) at its endpoints, adding its exact maximum1 if a box crosses1/2. Enclose h2 by endpoint values and maximum1 if its argument interval crosses1/2. For every box the checker independently obtains

    D_lower=Q_lower h2(p)_lower-h2(alpha)_upper>0,
    C_upper=6v_upper h2([Q_lower/6,Q_upper/6])_upper,
    (-C)_upper=Q_upper h2(v)_upper.

All256 recorded max(C_upper,minus_C_upper)/D_lower are below20, with maximum approximately19.41842713345, hence strictly below48. The boxes cover both complete closed intervals. This and(5),(7) prove |C|<=48D on EVERY allowed gate/bias pair, independently of inner core dimension. The preserved source64 claim follows a fortiori.

The96-bit log enclosure is independently implemented: positive48-term series for ln r after binary range reduction1<=r<2, with z=(r-1)/(r+1)<=1/3, explicit tail2z^97/[97(1-z²)], and outward fixed-point rounding at natural scale2^128. Divide by a similarly enclosed positive ln2, add exact binary exponents, and subtract integer-log intervals to handle rationals. Signed coefficients reverse interval endpoints. Only rational endpoints make decisions. The tail is included even if it is below the working scale.

## 6. All finite words; rare-start and fixed-seed bounds

At each legal step, equations(2),(3) and the48 price give

    |H(g')/I(g')-H(g)/I(g)|<=48[Psi(g)-Psi(g')].

The right side is nonnegative. Summing over ANY finite legal word telescopes once, proving total absolute variation<=48(Psi_start-Psi_end)<=48. There is no new account at a return or escape, and no uniform length or eventual exit assumption is needed.

Edge isoperimetry I>=2p log2(1/p) follows from product entropy tensorization applied to the minority indicator: Ent(1_A)=p log2(1/p), while a crossing uniform two-point fiber contributes1/2 and other fibers zero. Tensorization is proved by the log-sum inequality/convexity of Ent under averaging, iterated over coordinates. Combining with h2(p)<=p[L+e2] gives Psi<=1/2+e2/(2L)<11/16 for p<=1/16. Thus the rare-start budget is at most33. This sharpens the source44 budget while retaining the full initial H/I.

The already checked own-stage4 exact g3 state gives R(g3)+48Psi(g3)=9.9481922336...<10 by rational interval endpoints. Therefore ALL finite admissible descendants of that fixed actual core have H/I<10. No further recursion or sign enumeration is needed. Since E I<=sum_i B_i<=H (condition on all other bits in each summand and compare with any entropy chain), their E is also bounded. This is a closure of a fixed-seed mechanism, not a universal bound on unknown starting cores.

## 7. Physical falsification family and scope controls

The28 tagged actual12-bit truth tables include h and J on every nonconstant two-bit core, with the orientations frozen in the spec. For h the common policy is enforced. The J two-bit controls have minority1/4 or1/2 and are OUTSIDE its permitted rare domain; they test the generic signed coefficient/terminal/potential identities only. No price theorem is extended to those inputs. Every4096-entry integer Fourier spectrum is checked coefficient by coefficient against the biased expansion, and all12 physical edge influences are checked separately, including dummy core coordinates. The exact coefficient identity plus the analytic Shannon decomposition proves the entropy identity; a numerical interval containing zero alone is not presented as such a proof.

The six rare compressed controls include nontransitive, non-flat core negative set{0,1,2} on six bits, as well as the4- and5-bit point defects, with both gates. Their physical-coordinate influences are all retained. These do not replace the continuum/word proof; they target the places a missed signed row, omitted coordinate type, or terminal term could have falsified it. Finally, all48 actual matching automorphisms are checked on all64 truth inputs, and all six one-flip locations are explicitly matched.

## 8. First unsupported universal line

The entire arbitrary starting H(g)/I(g) remains in the ledger. A finite bound on the corrections does not bound that starting ratio. The next missing assertion is a noncircular payment for an arbitrary retained rare core, from its actual signed spectral rows and an exclusively allocated surplus such as I-h2(p). This surplus has an exact physical-information meaning: for independent physical inputs X and output Y=g(X),

    I(g)-H(Y)=H(X|Y)-sum_i H(X_i|Y,X_-i)>=0.

Indeed each I(Y;X_i|X_-i)=Inf_i(g), and independence gives H(X)=sum_i H(X_i). This conditional dependence identity explains what the proposed source reserve measures; it does not compare it to Fourier entropy. Proving H(g)<=K[I(g)-h2(p)] on the rare band would already be FEI-equivalent up to constants because h2(p)<=11I/16 there. We do not rename that missing line as a theorem or infer it from the reserve's positivity.

The audit supplies no physical restriction-tree payment, no universal E/H bound, no assertion about other sign/gate libraries, and no FEI disproof. No substantive repair to the accepted original source version was made. The48 corollary's independent review remains pending.
