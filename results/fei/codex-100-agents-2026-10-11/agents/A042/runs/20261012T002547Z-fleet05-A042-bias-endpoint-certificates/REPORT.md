# A042 stage 2: exact binary prime endpoint constants

## exact target, quantifiers, hypotheses and units

For every essential binary Boolean sign gate f, certify the exact supremum of Hplus_mu(f)/(I_mu(f)-Var_mu(f)) over every independent interior Bernoulli law (p,q) in (0,1)^2, including biases approaching deterministic endpoints at arbitrary independent rates. Hplus is corrected spectral entropy in bits. I is spectral influence, not unweighted pivotal probability. The denominator D is strictly positive for every essential binary gate at every interior law. At deterministic boundary laws, contract inputs and never divide the resulting zero deficit.

Result: the eight gates with one exceptional truth-table value have supremum C_corner=2+4/ln2; XOR and XNOR have supremum C_xor=2/ln2. Each supremum is unattained in the interior and is approached by explicitly specified Boolean endpoint paths. The sharp constant for all essential binary primes is C_binary=2+4/ln2, in (7.770780163555,7.770780163556). This closes the binary base case, not the all-arity prime inequality or full FEI.

## sources actually read, revisions and theorem locators

Read the updated BOARD.md (2026-10-12 00:21 UTC), own STATUS.md, and B09 STREAM_NOTES.md v2 (2026-10-11 23:33 UTC), including its review cap and assigned A042 binary target. Re-read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. The lead directs that the one-bit tax and AND coefficient not be recomputed; no such recomputation is done. This is the requested narrow completion of the endpoint packet, rather than a new broad universal candidate.

Read A085's original REPORT.md A042 review and CLAIMS.json record, run 20261011T231324Z-fleet05-A085-certificate-adversary. It independently accepts A042-BIAS-ENDPOINT-INTERFACE@1 at the fixed-table scope, with statement hash 7c2fae4055ba9e3bf195fcebe01cb6e66fde427ca4d8d8c3f48902754514dc60. It independently contains all 18 original finite weighted intervals. The new run preserves that review record without modifying the old run or shared registries. This review is source-read, not inferred from a board line.

Read A043's original REPORT.md and CLAIMS.json, run 20261011T221757Z-fleet05-A043-prime-gate-decomposition. Independently reconstructed its cofactor criterion, termination argument and induced-bias corrected composition below. This is a partial analytic review of A043-DISJOINT-PRIME-ENDPOINT@1, not acceptance of its bundled n<=4 census, which was not replayed here. Original source hashes, review scope and local receipts are in out/SOURCE_RECEIPTS.json. The threshold-paper product-basis and composition conventions were already read in stage 1, and are independently derived here; no new paper theorem or sharp-tax theorem is a mathematical premise. No publication priority claim is made for the binary constant or read-once closure.

## complete derivation or exact first unsupported line

### 1. Complete binary classification and invariances

A binary sign table has either zero/four positive entries (constant), two positive entries on one row or column (signed unary literal), two positive entries on a diagonal (XOR/XNOR), or one/three positive entries (one exceptional corner). Thus exactly ten binary functions depend essentially on both inputs: eight corner gates and two parity gates. The six others have D=Hplus=0 for every product law.

Output negation preserves the squared Fourier spectrum, Hplus, I, Var and D. Input reflection Xi -> 1-Xi, accompanied by p_i -> 1-p_i, negates the selected centered character and preserves its variance 4p_i(1-p_i). It therefore preserves each squared mass and Hplus/D. An input reflection is a bijection of the full interior bias domain. These facts reduce the eight corner gates to a conjunction sign, without imposing p=q or any coupling of their rates. Arbitrary biased character multiplication is not used.

Define the scalar function

    A(x)=x ln(1/x)/(1-x),   0<x<1;
    A(0)=0, A(1)=1.                                      (1)

The endpoint values follow from x ln(1/x)->0 and ln(1/x)/(1-x)->1 as x->1. The logarithm inequality ln y<=y-1, strictly for y!=1, gives A(x)<1. Positivity gives A(x)>0. Differentiating yields

    A'(x)=(-ln x-1+x)/(1-x)^2>0,                         (2)

using -ln x>1-x. Hence A is a strictly increasing continuous bijection of [0,1] onto [0,1]. These scalar inequalities certify the continuum, not a finite bias grid.

### 2. The eight corner gates: exact ratio and sharp supremum

Let (b1,b2) be the exceptional corner and let u=P(X1=b1), v=P(X2=b2). Output negation makes the table f=2 1_{X1=b1,X2=b2}-1. Reflections reduce the computation to u=p, v=q. Put V_u=4u(1-u), V_v=4v(1-v). Direct integration gives

    P(empty)=(2uv-1)^2,
    P({1})=V_u v^2,
    P({2})=V_v u^2,
    P({1,2})=V_u V_v/4.

Only the pair contributes to spectral deficit, so

    D=4u(1-u)v(1-v)>0.

The corrected logarithms of singleton packets are log2(1/v^2) and log2(1/u^2), and the pair logarithm is log2 4. Therefore

    Hplus/D = 2+(2/ln2)[A(u)+A(v)].                    (3)

Equations (1)--(3) prove

    2 < Hplus/D < 2+4/ln2

for every interior law, with infimum 2 and supremum 2+4/ln2. Since A(u),A(v) are each strictly increasing, the ratio approaches its supremum if and only if u->1 and v->1. In the original coordinates this means concentration of the product input law at the exceptional corner. The gate itself remains the same essential Boolean truth table throughout the path, even though its contracted limit is constant.

The full boundary ratio map, interpreted as a limit of interior ratios rather than a value at D=0, is explicit: u,v->0 gives 2; u->1,v->0 or vice versa gives 2+2/ln2; u,v->1 gives 2+4/ln2. An edge limit is obtained by replacing only the endpoint A value in (3). This holds along arbitrary independent rates, including nonanalytic paths, because (3) is exact and A has one-variable continuous endpoint extensions.

There is also an explicit uniform two-parameter error certificate. For 0<e<1,

    A(1-e)=1-sum_{k>=1} e^k/[k(k+1)].                (4)

This follows by multiplying the convergent series -ln(1-e)=sum e^j/j by (1-e)/e. The positive remainder after its linear term obeys

    0 <= 1-A(1-e)-e/2 <= e^2/[6(1-e)].                (5)

For u=1-e, v=1-d and arbitrary 0<e,d<=1/2, (3)--(5) give

    C_corner-Hplus/D=(e+d)/ln2+R,
    0<=R<=(e^2+d^2)/(3(ln2)) * 2.                    (6)

The bound follows separately in each coordinate; no relation between e and d, no order of limits and no hidden coefficient lower bound is required. A sharper all-interior remainder is (1/(3 ln2))[e^2/(1-e)+d^2/(1-d)]. Near the opposite endpoint, A(e)=e ln(1/e)+e^2 ln(1/e)+R0 with 0<=R0=e^3 ln(1/e)/(1-e), which exposes the remaining higher-order normalized-coefficient logarithms directly.

### 3. XOR/XNOR: exact ratio, unit atom and sharp supremum

Output negation reduces parity to f=(2X1-1)(2X2-1). Set a=4p(1-p), b=4q(1-q), and m_p=2p-1, m_q=2q-1. Independence gives

    P(empty)=m_p^2 m_q^2,
    P({1})=a m_q^2,
    P({2})=b m_p^2,
    P({1,2})=ab.

Thus D=ab>0. The pair has zero corrected entropy, since its mass equals its normalization. The singleton logarithms give

    Hplus/D=(1/ln2)[A(1-a)+A(1-b)].                  (7)

At a=1 or b=1, define the corresponding term by A(0)=0. This agrees with omitting a zero singleton. Equations (1)--(2) imply 0<=Hplus/D<2/ln2 and show that equality at zero occurs exactly at p=q=1/2, where the pair is a unit spectral atom and D=1. A unit pair is consequently not a zero-deficit case.

The supremum 2/ln2 is approached if and only if p and q each approach some deterministic endpoint. Every one of the four product corners works; their two rates are unrestricted. At an edge with one input fixed fair, the largest ratio limit is 1/ln2. Formula (7) describes every other edge limit. With a,b<=1/2, the uniform error estimate is

    C_xor-Hplus/D=(a+b)/(2 ln2)+R,
    0<=R<=(a^2+b^2)/(3 ln2).                          (8)

This follows from (5). If p=e approaches zero or p=1-e approaches one, a=4e(1-e), so (8) is also an explicit unequal-rate corner certificate in the physical probabilities.

For either class, contracting deterministic inputs produces a constant or unary literal with Hplus=D=0. Assigning the nonzero limiting ratio as an actual ratio of that contracted function would be invalid. The new proof resolves the simultaneous-bias issue for arity two without claiming that stage-one fixed-bias Taylor remainders are uniform for arbitrary gates.

### 4. Focused independent reconstruction of the queued A043 interface

For a proper essential block B with 2<=|B|<=n-1, form the rows f(a,.) indexed by a in {0,1}^B. Genuine one-bit disjoint substitution f=G(h(x_B),x_Bc) implies at most two rows. Essentiality excludes a single row. Conversely two distinct rows define h as the row label and G as the row lookup. Each factor is essential because an irrelevant factor input would be irrelevant in f; the new outer wire is relevant because the rows differ. The split has arities |B| and n-|B|+1, both below n, so recursion terminates and uses each physical leaf once. This reconstructs the analytic cofactor criterion, but makes no claim that the saved n<=4 census was checked.

For a disjoint composition F=G(f1,...,fk) under independent interior physical laws, let eta_i=P(fi=1), V_i=4eta_i(1-eta_i)>0. The centered output function of fi is (fi-E fi)/sqrt(V_i), and its nonempty coefficients are fihat(T)/sqrt(V_i). Disjointness and uniqueness of each block intersection imply

    Fhat(union_{i in U} T_i)
       = Ghat_eta(U) product_{i in U}[fihat(T_i)/sqrt(V_i)]

for nonempty T_i. Squaring and summing identifies each occupied-child law as P_i(T)/V_i. Splitting the corrected logarithm into its outer factor and its child factors gives

    Hplus(F)=Hplus_eta(G)+sum_i alpha_i Hplus(fi),
    D(F)=D_eta(G)+sum_i alpha_i D(fi),
    alpha_i=I_i^eta(G)/V_i>=0.                        (9)

The influence identity is I(F)=sum alpha_i I(fi), and Var(F)=Var_eta(G). This proves the deficit equation in (9). Constant children are frozen and deleted before division by V_i. Under product physical inputs, disjoint child outputs are independent, so the product law eta is the actual induced law. It can be nonuniform even from uniform physical inputs.

This independently reconstructs A043's analytic composition/localization interface and confirms it survives unequal biases and deterministic contraction. The exact census portion of its bundled claim remains outside this stage's review. No substantive repair was supplied to A043; no full bundled acceptance is asserted.

Combining (9) with the sharp binary inequality gives corrected Hplus<=C_binary D for every read-once formula of binary Boolean gates and literals, uniformly in depth and physical biases. Constants are contracted. On uniform physical inputs, H=Hplus+h0, with h0=-t log2 t and t=(E f)^2; -t ln t<=1-t=Var implies h0<=Var/ln2. Hence H<=C_binary I. The corrected constant is sharp already for one binary gate. This is a restricted closure and no claim of a new class theorem in the literature; it is the concrete base case needed by B09's prime localization.

The first unsupported universal inference would be 'all prime arities have the same bound because binary primes do.' The cofactor decomposition leaves ternary majority and unbounded-arity primes, and supplies no inequality for them. None of C018/C019/C020/C024's unpaid universal entropy terms is discharged by binary closure alone.

## executed validation with domain, arithmetic, commands and outputs

Frozen before execution: out/FROZEN_SPEC.json. Executed `python -X utf8 runs/20261012T002547Z-fleet05-A042-bias-endpoint-certificates/code/binary_certificate.py` from A042. Passed 5,277 assertions in 1.207 computation seconds: all 16 binary tables at 81 explicitly frozen rational bias pairs, 180 essential-outer/AND-OR-XOR-inner disjoint four-input compositions, and 40 constant-child contractions. No symmetry reduction or floating sign check was used. Each spectrum is computed independently from the actual truth table by exact centered moments and Fraction arithmetic.

To verify entropy identities exactly, express every term mass*ln(normalization/mass) by prime-exponent coefficients of its positive rational log argument. Matching all rational coefficients gives an exact equality of log expressions, not just interval overlap. The binary ratio formulas and disjoint corrected-entropy cancellation pass these identities, including the zero singleton packets at fair parity inputs. Exact rational influence/variance/deficit identities are checked separately.

The saved constant enclosures use 32-term rational atanh log bounds after power-of-two range reduction, with positive tail at most 2z^(2N+1)/[(2N+1)(1-z^2)]. Signed exponent scaling swaps endpoints; all division corners are considered. The output endpoints are exact outward rational multiples of 10^(-12). Three explicit paths (p,q)=(1-t,1-t^2) for corner gates and (t,t^2) for parity, at t=1/4,1/16,1/256, are interval-certified. They corroborate the sharpness proof; the infinite limit is proved by (4)--(8), not inferred from the fixtures.

No heavy job was needed: memory estimate 80 MB, no dimension escalation, standard library only, and observed computation well below the 60-second pilot cap. Peak memory was not measured; no >300 MB job was started. CHECK_OUTPUT.json contains counts and exact bounds, and out/VALIDATION.json validates protocol schemas, claim statement hashes and saved artifacts.

## proof dependencies and changed downstream conclusions

The binary supremum uses direct two-bit Fourier algebra and elementary logarithm inequalities, with no unreviewed universal theorem. Stage-one A042@1 is consumed with its actual A085 independent review record and its fixed-table restrictions; the new two-variable scalar formulas supply the previously missing simultaneous-degeneration certificate at arity two. A043's composition identity is independently reconstructed, with a scoped partial review rather than a declaration that its finite census is accepted.

B09/A043 now have an exact all-bias constant for every essential binary prime, including complete endpoint limits and an explicit jointly uniform error bound. A043/A044 can remove binary gates as possible sources of an unbounded corrected ratio, but cannot apply the result to arbitrary higher-arity prime roots. A084 can use the scalar certificate without a bias-box search. No shared registry, other agent folder, Brain database or remote repository was modified.

## one next mathematical action and independent reviewer

A090/A091 should reconstruct (3), (7), and the exact logarithm/deficit cancellation in (9). The next mathematical action is to consume A043's first higher-arity prime extremizer and isolate its mixed-singleton/higher-degree ratio under independent endpoint rates using normalized coefficient polynomials; begin with its explicit signed table rather than enlarging an untargeted grid. If no new extremizer is ready, analyze the ternary-majority prime's simultaneous deterministic-face limits as the first gate not removed by binary decomposition. The needed target is a normalized higher-degree deficit payment, not the already known one-bit restriction tax.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, code/, frozen specifications, exact output, source/review receipts and persistence validation are saved only in this stage's A042 run directory. STATUS.md has two lines; WORKLOG.md is appended and LEARNED.md records the sharp formulas, endpoint errors and review scope. Stage-one artifacts are preserved. The A085 review is locally recorded with its original statement hash; supervisor adoption, new independent review, copying, Brain ingestion and mirror verification remain pending. There is no save blocker.

**Universal bridge:** This stage moves the B09 lead's C025/G-BIASED-LTF prime-gate target by closing all ten arity-two essential primes over the entire product-bias continuum with the sharp common constant 2+4/ln2, including jointly degenerating endpoints and their rate-independent error bounds. It also consumes the independent A085 endpoint review and reconstructs queued A043 analytic composition while leaving its census outside this review. What remains is the all-arity higher-prime corrected entropy payment; the binary result neither pays a universal erasure/tree/code/history debt nor implies that larger primes share its constant. NEXT takes a source-specified higher-prime extremizer and identifies the first unbounded normalized deficit obligation, which is the shortest route beyond the now-certified base case rather than another binary grid or isolated read-once theorem.
