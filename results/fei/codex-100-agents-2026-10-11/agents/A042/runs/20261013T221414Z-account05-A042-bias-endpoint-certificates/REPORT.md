# A042 stage 3: sharp product-biased majority-three and mixed-rate boundaries

## exact target, quantifiers, hypotheses and units

For the essential ternary prime f(x)=2*1{x1+x2+x3>=2}-1, and all independent interior Bernoulli probabilities p1,p2,p3, determine the corrected entropy/deficit supremum and classify simultaneous deterministic endpoints without coupling their rates. Spectral influence is I=sum |S|P(S), deficit D=I-Var=sum_{|S|>=2}(|S|-1)P(S), natural corrected entropy is E=sum_nonempty P(S)ln(w_S/P(S)), w_S=product_{i in S}4pi(1-pi), and Hplus=E/ln2 is in bits. Contract deterministic coordinates before forming an orthonormal basis or dividing by a zero deficit.

Proved for every interior bias vector:

    E <= (4+ln4)D-(ln4-1)P({1,2,3}).                 (T)

The triple mass is positive and ln4>1, so Hplus/D is strictly less than C*=2+4/ln2. Its exact supremum is C*, approached by the fixed prime along A043's path (1-t^3,t,t). The result also holds under input reflections, permutations and output negation with the corresponding reflected biases. It is a complete all-bias theorem for this prime orbit, not an all-prime or all-weighted-threshold theorem. The new proof is a narrow completion of the endpoint packet; B09's broad pending-review cap is respected.

## sources actually read, revisions and theorem locators

At stage start read BOARD.md, snapshot 2026-10-13 22:05 UTC; own STATUS.md and LEARNED.md; and B09 STREAM_NOTES.md v2, still dated 2026-10-11 23:33 UTC. The lead's assigned binary target was completed in stage 2. The updated board reports A041 and A045 independently accepted that binary theorem and A043 identified a higher-prime majority endpoint. Following productive continuation/consuming a new dependency, this stage takes A043's explicit prime rather than repeating binary or one-bit-tax work.

Read A043's stage-2 REPORT.md and MAJORITY_BOUNDARY.md in runs/20261012T012726Z-account05-A043-prime-gate-decomposition, including its exact majority coefficients, essential-prime test, source path and stated gap. Reconstruct that boundary proof independently below. Its finite n<=4 grid certificate is not replayed or independently accepted here. Read A041's stage-3 REPORT.md in runs/20261013T215146Z-account05-A041-weighted-threshold-fei, including its new pure-sector/mixed-reference interface and full binary review; and A045's stage-2 CLAIMS.json at runs/20261013T212421Z-account05-A045-biased-realizability-referee. A041's singleton estimate is contextual: the stronger degree-resolved singleton identity needed for (T) is proved here directly. Neither A041's new pure-sector theorem nor any sharp one-bit tax is a mathematical premise.

Protocol remains fei-execution-protocol/2, revision 2026-10-11-execution-v2. The stage-1/2 A042 proof sources remain unchanged; the exact source files actually used, byte hashes, and review receipts are pinned in out/SOURCE_RECEIPTS.json and out/REVIEW_SCOPE.json. The supplied threshold manuscript's normalized product basis and corrected-entropy convention were read in prior stages and are independently reconstructed by finite differences here. No new literature or publication-priority assertion is made.

## complete derivation or exact first unsupported line

### 1. Actual Boolean spectrum and prime test

For each two-coordinate block of majority, block Hamming weights zero, one and two give distinct cofactor rows (-1,-1), (-1,+1), (+1,+1). Hence no proper two-coordinate block factors through a Boolean wire: this is a genuine essential ternary prime under A043's disjoint substitution convention.

Put vi=4pi(1-pi) and mi=1-2pi. Write c_S=fhat(S)/sqrt(w_S). The sign polynomial is

    f=2x1x2+2x1x3+2x2x3-4x1x2x3-1.

Integrating centered differences yields

    c_i=pj+pk-2pjpk,    c_ij=(1-2pk)/2,    c_123=-1/2,  (1)

where {i,j,k}={1,2,3}; c_empty=E f. Consequently P(S)=w_S c_S^2. Let

    B=sum_{|S|=2}P(S),   T=P(123)=v1v2v3/4.

Then D=B+2T>0. The notation B here is just pair mass within this proof; it is not the campaign's aggregate erasure entropy.

### 2. Degree-resolved singleton payment preserves the needed triple credit

For a monotone sign table, ci is its pivotal indicator's mean and lies in [0,1]. Conditioning one bit gives fhat(U union {i})=sqrt(vi)*dihat(U), where di is the {0,1}-valued pivotal derivative. Parseval and Var(di)=ci(1-ci) therefore imply, for this three-input table,

    sum_i vi ci(1-ci)=sum_{|S|>=2}|S|P(S)=2B+3T.      (2)

For 0<=c<=1, ln(1/c)<=1/c-1 gives

    c^2 ln(1/c^2)<=2c(1-c),                          (3)

with the zero endpoint interpreted by continuity. Thus the singleton natural entropy obeys

    E_single<=2(2B+3T)=4D-2T.                        (4)

Replacing (4) merely by 4D would discard exactly the credit needed below. This is a degree-resolved version of the general monotone singleton estimate, not an invocation of a separate tax payment.

### 3. Exact pair/triple entropy and the sharp global upper bound

For a pair {i,j}, put z=mk^2. Equation (1) gives

    E_ij=(vi vj/4) z ln(4/z)
         =ln4*P(ij)+(vi vj/4) z ln(1/z).

The elementary inequality -z ln z<=1-z, 0<=z<=1, and 1-mk^2=vk give

    E_ij<=ln4*P(ij)+vi vj vk/4=ln4*P(ij)+T.          (5)

The triple contribution is exactly ln4*T. Summing the three pair bounds and this triple term yields

    E_ge2<=ln4*B+(3+ln4)T
          =ln4*D+(3-ln4)T.                           (6)

Combining (4) and (6) proves (T):

    E<= (4+ln4)D+(1-ln4)T.

There is no reused deficit reserve: (2) counts pairs twice and the triple three times, and (6) spends exactly three triple copies from the three pair normalizations. The residual coefficient is favorable since ln4>1 (for example integrate 1/x>1/2 on (1,2) to obtain ln2>1/2). Every step remains valid at zero pair coefficients by continuity.

The nontrivial identity behind this closure is the shared triple mass in (5). For higher arity, different pairs do not all reduce to one affine missing-coordinate amplitude and one common triple mass; the same summation does not establish an all-arity theorem.

### 4. Full-corner asymptotics at independent rates

Let rare deviations e,u,v>0 tend independently to zero, set delta=max(e,u,v)<=1/8 and S=eu+ev+uv. Both a unanimous vertex and a mixed vertex have exactly

    D=4 sum_{cyc} e u(1-e)(1-u)(1-2v)^2
           +32euv(1-e)(1-u)(1-v).                    (7)

In particular

    |D-4S|<=35 delta S,   D>=S.                      (8)

To check (8), each pair's product factor differs from one by at most e+u+4v<=6delta. Its total error is at most 24delta S. Also T<=16euv<=16delta S/3. The lower bound follows from the pairs alone: D>=4(1-delta)^2(1-2delta)^2 S>=S for delta<=1/8.

At a unanimous zero vertex p=(e,u,v), or the unanimous one vertex by complement, all singleton normalized coefficients are sums of two rare deviations minus twice their product. Thus

    Hplus/D=2+O(delta ln(1/delta)).                    (9)

At a mixed vertex with unique typical one, use p=(1-e,u,v). Here

    c1=u+v-2uv,
    c2=1-(e+v-2ev),   c3=1-(e+u-2eu).

Writing h(c)=c^2 ln(1/c^2), h(1-a)=2a+O(a^2), gives the singleton leading term

    E_single=8e(u+v)+16uv+O(delta S ln(1/delta)).

The higher-degree leading term from (5)--(6) is 4ln4*S+O(delta S). Therefore

    Hplus/D = 2+(2/ln2)(1+lambda)+O(delta ln(1/delta)),
    lambda=uv/[e(u+v)+uv] in (0,1).                  (10)

This includes all six mixed vertices by permutation and simultaneous input/output complement. It does not assume powers of one common parameter or a fixed relative rate. If lambda oscillates, the ratio need not have a limit; (10) still controls every accumulation value.

For completeness, a concrete error certificate valid for every e,u,v<=1/8 is

    absolute error in either (9) or (10)
          <=400 delta ln(1/delta)                    (bits). (11)

Here is an explicit bookkeeping proof. Let t be a sum of two rare deviations, t<=2delta<=1/4. The function t^2 ln(1/t^2) is increasing there. The nonpivotal mixed singleton contribution divided by S is at most 16delta ln(1/delta); the sum of the unanimous singletons divided by S is at most 32delta ln(1/delta). For c=1-a>=3/4, |h''(c)|<=6, so |h(1-a)-2a|<=3a^2. Combining the factors (1-u) and a=e+v-2ev bounds each pivotal-singleton error by 48delta*u(e+v); summing gives at most 96delta S. From (5), the higher-degree entropy differs from 4ln4*S by at most 64delta S, using ln4<3/2, |pair mass-4S|<=24delta S, and T<=16delta S/3. Thus the total mixed numerator error is at most 100delta ln(1/delta)S, since ln(1/delta)>=ln8>2. The mixed leading natural ratio is at most ln4+4<11/2. Combining its denominator error (8) gives natural ratio error less than 200delta ln(1/delta), and division by ln2>1/2 proves (11). The unanimous bound is smaller. The scalar constants are elementary: convexity of 1/x bounds its integral on [1,2] strictly by the trapezoid value 3/4, while ln2=2 sum_{j>=0} (1/3)^(2j+1)/(2j+1)>2/3. These give ln4<3/2 and ln8>2. All constants are absolute and independent of the relative rates.

Consequently the unanimous corner limit is 2. At a mixed corner, every possible limiting ratio lies in [2+2/ln2,2+4/ln2]; every point of that interval is achieved by suitable rates. For lambda in (0,1), choose u=v=t and e=((1-lambda)/(2lambda))*t. The endpoint lambda=0 is achieved by e=t,u=v=t^2; lambda=1 by e=t^3,u=v=t. All probabilities stay interior for sufficiently small t. The last path is exactly A043's source path. It proves the sharp lower bound C* for the global inequality (T), independently of finite computations.

### 5. Remaining boundary strata and zero-deficit contractions

If one input becomes deterministic while the other two biases stay interior, the contracted gate is AND2 or OR2. Its deficit is positive, and continuous E,D reduce the ratio to the already certified binary formula. These face limits are not singular 0/0 cases.

For codimension-two edges, hold the remaining bias r in (0,1) fixed, let e,d tend independently to zero, and write A(r)=r ln(1/r)/(1-r). Remainders below are uniform for r in any fixed compact subinterval of (0,1), not uniform as r itself tends to an endpoint.

For two typical zero bits p=(e,d,r), the contracted table is constant and

    D=4r(1-r)(e+d)+O_r((e+d)^2),
    Hplus/D=2+2A(r)/ln2+O_r((e+d)ln(1/(e+d))).        (12)

Two typical one bits give (12) with r replaced by 1-r. For opposite deterministic bits p=(1-e,d,r), the contracted table is the literal in the third coordinate, and

    Hplus/D=2+(2/ln2)[1+theta A(r)+(1-theta)A(1-r)]
                +O_r((e+d)ln(1/(e+d))),
    theta=e/(e+d).                                  (13)

The same deficit expansion holds. To derive these formulas, the pair masses involving the third input have leading sum 4r(1-r)(e+d); the other pair and triple are second order. In (12), the two rare singleton entropy terms total 8r^2(e+d)ln(1/r); the third singleton is O_r((e+d)^2 ln(1/(e+d))). In (13), the rare singleton terms are 8er^2 ln(1/r) and 8d(1-r)^2 ln(1/(1-r)), while the near-saturated third singleton contributes 8r(1-r)(e+d). Dividing gives the displayed terms. Formula (11), rather than a claimed uniform edge remainder, handles r tending simultaneously to its endpoint.

Equations (9)--(13), the binary faces, and (T) cover every deterministic boundary stratum. At an edge the actual contracted E=D=0, even when the interior ratio has a nonzero limit. At the fully fair interior point, the triple has mass 1/4 and the three singletons mass 1/4 each: D=1/2 and Hplus/D=4. Vanishing pairs at that point cause no division by pair coefficients in the proof.

### 6. Scoped review and the first unsupported universal line

The majority coefficients, cofactor prime test and source limit in A043's MAJORITY_BOUNDARY.md are independently reconstructed by (1), (7)--(11). The review verdict is HOLDS for that named boundary subresult; no repair was required. This is a partial review of its bundled grid-and-boundary claim. The full finite prime grid and prime census remain outside this stage's review. A041/A045's independent acceptances of A042's binary claim are source-read and recorded at their original statement hash, rather than reopening or modifying the older proof.

The first unsupported step toward all-prime FEI+ would replace the special equality (vi vj/4)(1-mk^2)=T in (5) by an all-degree, all-arity shared payment while preserving (4)'s deficit credit. No such identity or normalized global reference is proved. The higher-prime/mixed-sector entropy remains the universal gap; knowing this exact ternary constant does not bound all weighted thresholds or pay a stopping-tree tax.

## executed validation with domain, arithmetic, commands and outputs

Frozen before computation: out/FROZEN_SPEC.json, helper A042-majority3-v1. Executed from A042:

    python -X utf8 runs/20261013T221414Z-account05-A042-bias-endpoint-certificates/code/check_majority.py

Passed 7,783 assertions in 1.302 computation seconds. The complete 9^3 rational grid independently constructs every majority spectrum from all eight actual Boolean assignments, matches its normalized mixed-difference coefficients, checks Parseval, (2), each entropy sector estimate and (T). The grid contains 1/2 and therefore checks exactly zero pair coefficients. Twelve dyadic source paths q=2^-k, k=1..12, independently reconstruct the A043 path spectrum. Eight frozen exponent triples and eight dyadic t values supply 128 unanimous/mixed corner fixtures; all check the explicit constants in (8) and (11). Six fixed-r edge fixtures check the exact spectra and record the predicted leading ratios. No finite edge value is asserted to equal its asymptotic limit.

Every spectrum and polynomial check uses Fraction arithmetic. Inequalities use 24-term exact-rational atanh log enclosures after power-of-two range reduction, with tail at most 2z^(2N+1)/[(2N+1)(1-z^2)]. Signed scaling and four-corner interval division preserve outward bounds. Exported ratio intervals are rounded outward to rational multiples of 10^-10. The analytic inequalities prove the continuum theorem and all-rate remainders; finite checks do not replace those proofs. The optional prime-exponent mechanism listed in the frozen specification was not needed: rational intervals already separated every tested inequality, and no logarithmic equality was inferred from overlap.

Memory estimate was 90 MB; peak was not measured. No job above 300 MB, heavy search, dimension escalation, GPU, background process or other-agent code execution occurred. out/CHECK_OUTPUT.json contains complete counts, the rational constant enclosure, twelve source-path intervals, sixteen final unequal-rate corner records and six edge records. out/VALIDATION.json checks required schemas, original claim hashes and compatibility bytes. Source files were read only.

## proof dependencies and changed downstream conclusions

The new theorem depends only on the actual majority truth table, normalized product Fourier integration, Parseval for {0,1} pivotal derivatives, elementary log inequalities and the explicit Taylor remainder bound on [3/4,1]. Neither the unreviewed all-prime endpoint nor any sharp-tax statement is used. A043's source path is reviewed, but its lower bound is also re-proved independently with the stronger arbitrary-rate formula.

B09/A043 may now retire majority-three and its input/output reflection orbit as possible sources of a corrected constant above 2+4/ln2. A041/A045 receive the degree-resolved singleton credit 4D-2T and the exact common triple payment identifying why this first prime closes. A084 receives absolute independent-rate corner bounds rather than a fixed-path Taylor inference. Binary and majority gates may be combined under the already reconstructed genuine disjoint corrected composition identity with the same maximum constant; this statement does not include arbitrary unreviewed higher primes or overlapping supports. Full FEI remains OPEN.

## one next mathematical action and independent reviewer

A090/A091 should reconstruct (2), (5) and the residual coefficient 1-ln4, then challenge the absolute corner error ledger independently. NEXT is to apply the degree-resolved singleton reserve to A043's next non-majority prime extremizer, or to the mixed two-group spectral marginal supplied by A041, and identify the exact replacement for the common-triple equality in (5). Use the existing actual signed table and normalized coefficient process; do not enlarge the moderate-bias grid or re-run a one-bit-tax search. This tests the missing payment mechanism beyond the now-closed nonbinary prime.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, code/, frozen spec, complete exact output, source/review records and local validation/receipt manifests under this A042 run only. STATUS.md has two lines; WORKLOG.md appends the stage and LEARNED.md records the exact theorem, endpoint mixture parameter and scope limits. Prior runs and all other agents' files are unchanged. New independent review, supervisor copy, Brain ingestion, mirror verification and adoption remain pending. No save blocker exists.

**Universal bridge:** This stage moves B09's C025/G-BIASED-LTF all-prime corrected-product target by closing the first source-specified nonbinary prime, majority-three, over the entire bias continuum with exact supremum 2+4/ln2, a strictly favorable triple-atom remainder, and a complete deterministic-boundary rate description. It independently validates A043's named endpoint subresult without accepting the unreplayed grid. The universal remainder is an all-degree shared normalization/reference payment replacing the special common triple identity; none of C018/C019/C020/C024's full entropy costs is claimed paid. NEXT transfers the preserved degree-resolved singleton credit into that precise mixed-prime/mixed-sector obligation, the shortest route toward full FEI rather than another finite class or a larger moderate-bias census.
