# A096 stage 2: universal payment of the level-one-to-two erasure

## exact target, quantifiers, hypotheses and units

Following B20 STREAM_NOTES.md v2 (2026-10-11 23:39Z), this stage retires the singleton-tax topic and pays the next level of the C018 erasure functional. For every finite n>=0 and every Boolean sign f on the uniform cube, write a_S=hat f(S), epsilon_i=Inf_i(f), I=sum_i epsilon_i, and phi(x,y)=(x+y)h2(y/(x+y)), with phi(x,0)=phi(0,y)=0. All entropies are in bits. Define

    W2=sum_{i<j}a_{ij}^2,
    H2=sum_{i<j}a_{ij}^2 log2(1/a_{ij}^2),
    T12=sum_i sum_{j!=i}phi(a_i^2,a_{ij}^2).

The theorem proved here, uniformly in dimension and without any structural restriction on f, is

    H2 <= (155600/50301) I,
    T12 <= (16700/2187) I < 8 I   when I>0.

For constants I=H2=T12=0. The constants are explicit upper bounds, not claimed sharp. The proof uses the full Boolean constraint through its equivalent pointwise form f^2=1 and the resulting {0,+1,-1}-valued derivatives. A norm-one real Fourier vector alone is insufficient. This closes the precise level-one-to-two target issued to A096. It does not bound all higher erasure levels or solve full FEI.

## sources actually read, revisions and theorem locators

Read the updated BOARD.md, supervisor snapshot 2026-10-11 23:39 UTC; B20 STREAM_NOTES.md v2; B20 SYNTHESIS.md (five ranked routes and the level-one-to-two target); own STATUS.md and prior saved proof. Re-read execution protocol 2026-10-11-execution-v2. The canonical report/claim/obstruction/packet files remain read-only. The stage's out/SOURCE_LEDGER.json records local SHA256 receipts, all 100 packet observations and source records from 125 saved reports; out/REPORT_SOURCE_BUNDLE.txt preserves the complete report texts used for intake. This is source-bound navigation and correction tracking, not 125 independent mathematical audits.

Critical complete originals read: B20 lead run 20261011T225100Z-claude-B20-erasure-activation-transfer REPORT.md sections 2-4 (activation erasure, root payment and low-influence completeness); A090 run 20261011T231429Z-fleet05-A090-independent-reconstruction REPORT.md and CLAIMS.json (independent singleton-tax proof and explicit review scope); A021 run 20261011T232653Z-fleet05-A021-rare-core-asymptotics REPORT.md correction section and CLAIMS.json v2. B20's exact root claim is B20-ROOT-BIAS-ERASURE-PAID@1. The new theorem here does not use that claim as a proof premise; it is used only to describe the combined remaining bridge.

CORRIGENDUM.md fixes the old report's explanatory sign without changing the correct final claim: J<=h2(r)-h2(delta)+M, not minus M. Immutable old artifacts are preserved. A090 independently accepted A096-UNIFORM-SINGLETON-HALF-TAX@1 only, and explicitly did not independently accept the general fixed-pair theorem. B20's hand re-derivation of both is a separate source record. The distinction is carried in the adoption delta rather than upgrading both claims from board shorthand.

A021-UNIFORM-RARE-CORE-EXPANSION@1 has an erroneous nonpositive remainder interval. Its version 2 has a positive entropy remainder and negative control-decrement remainder. The source-bound correction identifies eight associated source claim records. A023/A087 acceptance of the old remainder must be narrowed; exact Fourier spectra and the separate control-first KL identity remain unaffected. No consumer file was changed and no downstream substitution is presumed.

## complete derivation or exact first unsupported line

### 1. Full Booleanity supplies a sparse derivative

The complete signed identities sum_S a_S a_(S xor U)=0 for U!=empty, together with sum_S a_S^2=1, are equivalent to f(x)^2=1 at every input. We use that pointwise conclusion. Let

    h_i(x_-i)=[f(+1,x_-i)-f(-1,x_-i)]/2.

Then h_i belongs to {0,+1,-1}; Pr(h_i!=0)=E h_i^2=epsilon_i. Its Fourier coefficient at {j}, j!=i, is a_{ij}. Set

    L_i=sum_{j!=i}a_{ij} x_j,
    d_i=E L_i^2=sum_{j!=i}a_{ij}^2=E[h_i L_i].

For a Rademacher linear form, independence and cosh(u)<=exp(u^2/2) give E exp(t L_i)<=exp(t^2 d_i/2). To verify the scalar inequality, (log cosh u)'=tanh u<=u for u>=0 because (tanh u)'<=1 and tanh 0=0; integrate and use evenness. Thus

    E exp(t|L_i|)<=2 exp(t^2 d_i/2), t>0.

For epsilon_i>0, conditional Jensen on A_i={h_i!=0} yields

    E[|L_i| | A_i] <= ln(2/epsilon_i)/t+t d_i/2.

Indeed, the conditional exponential moment is at most the unconditional moment divided by epsilon_i. Since |h_i|=1 on A_i,

    d_i=E[h_i L_i] <= epsilon_i E[|L_i| | A_i].

If d_i>0, choose t=sqrt(2 ln(2/epsilon_i)/d_i), divide by sqrt(d_i), and square:

    d_i <= 2 epsilon_i^2 ln(2/epsilon_i).          (1)

When epsilon_i=0, h_i is identically zero and d_i=0. When d_i=0 the inequality is immediate. No small-influence assumption is required. The quadratic suppression in (1) is the actual new payment mechanism.

### 2. A normalized influence reference pays the level-two entropy

Assume I>0 and W2>0. For unordered pairs define

    Q({i,j})=2 epsilon_i epsilon_j/I^2,
    P({i,j})=a_{ij}^2/W2.

The reference has total mass 1-sum_i epsilon_i^2/I^2<=1. Every occupied pair has both influences positive, so Q is positive on the support of P. Normalizing Q and applying nonnegative relative entropy gives H(P)<=E_P log2(1/Q). Multiplying by W2 and retaining the level mass entropy yields

    H2 <= sum_i d_i log2(1/epsilon_i)
          + W2 log2(I^2/(2W2)).                  (2)

This step includes the reference normalization; it does not treat the pair masses as a probability law of total mass one. Zero influences contribute zero.

With t=-ln epsilon_i>=0, equation (1) implies

    d_i log2(1/epsilon_i)
      <= epsilon_i * [2 exp(-t)(t^2+t ln2)/ln2].

Calculus gives sup_{t>=0} t^2 exp(-t)=4/e^2 and sup_{t>=0} t exp(-t)=1/e. Therefore

    sum_i d_i log2(1/epsilon_i)
      <= [8/(e^2 ln2)+2/e] I.                    (3)

For every z>0, ln z<=2 sqrt(z)/e: the maximum of ln(z)/sqrt(z) occurs at z=e^2 and is 2/e. Apply this with z=I^2/(2W2). Parseval gives W2<=1, so

    W2 log2(I^2/(2W2))
      <= [sqrt(2)/(e ln2)] I sqrt(W2)
      <= [sqrt(2)/(e ln2)] I.                    (4)

This remains valid even when the logarithm on the left is negative. Combining (2)-(4), and treating W2=0 separately,

    H2 <= K2 I,
    K2=8/(e^2 ln2)+2/e+sqrt(2)/(e ln2).          (5)

### 3. Convert the entropy bill into the requested erasure bill

Every edge has x=a_i^2,y=a_{ij}^2 and x+y<=1 by Parseval. For x,y>0, x ln(1+y/x)<=y and log2((x+y)/y)<=log2(1/y). Hence, with zero cases obtained directly,

    phi(x,y)<=y log2(1/y)+y/ln2.

Each unordered pair appears twice in T12. Also 2W2<=I. Consequently

    T12 <= 2H2+2W2/ln2 <= [2K2+1/ln2] I.        (6)

The following completely rational comparison certifies the constants: e>27/10 since the exponential series through degree five is 163/60; ln2>69/100 since the first two positive atanh terms at 1/3 sum to 56/81; sqrt(2)<71/50 by squaring. Thus

    K2 < 8/[(27/10)^2*(69/100)] + 2/(27/10)
           +(71/50)/[(27/10)*(69/100)]
       =155600/50301,
    2K2+1/ln2 <16700/2187<8.                    (7)

Equations (1)-(7) prove the theorem in all dimensions. No finite census or unknown external theorem is used to extrapolate it.

### 4. Controls identify exactly where Booleanity matters

For the lead's normalized real linear control g=n^(-1/2)sum_i x_i, the spectral derivative energy is 1/n, but the derivative is the nonzero constant 1/sqrt(n): its support probability is one. It violates |ghat(i)|<=spectral influence_i and the support/energy identification in step 1. This control has T12=0, so it tests the mechanism, rather than being a counterexample to the final T12 inequality.

A stronger actual real norm-one control with both levels is

    g_n=(1/sqrt(2n))sum_i x_i
          +(1/sqrt(n(n-1)))sum_{i<j}x_i x_j.

Its first- and second-level masses are both 1/2, so its spectral energy is 3/2. There are n(n-1) oriented edges, each with x=1/(2n), y=1/[n(n-1)]. Since phi(x,y)>=y log2(x/y),

    T12(g_n)>=[log2((n-1)/2)],
    T12(g_n)/I_spectral(g_n)>=(2/3)log2((n-1)/2)->infinity.

This is not a Boolean counterfamily. For U={i}, its signed convolution is 2(n-1)/(sqrt(2n)*sqrt(n(n-1)))>0, violating full Booleanity. It proves that arbitrary norm-one spectra cannot satisfy the proposed universal level-one-to-two payment. The exact constraint, rather than mere normalization, is indispensable.

### 5. Honest remaining line

Let R_ge2(f)=sum_{|S|>=2}sum_{i notin S}phi(a_S^2,a_(S+i)^2). Then

    B(f)=B_root(f)+T12(f)+R_ge2(f).

B20 already pays B_root by [2/(sqrt(e) ln2)]I. This stage pays T12 by (16700/2187)I. The first unsupported universal line is R_ge2(f)<=K I(f) with one dimension-independent K. Repeating a fixed-layer bound with the same whole I at every layer would reuse the budget and does not close this line.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before execution. No symmetry reduction or dimension escalation was used. Commands from A096:

    python -X utf8 runs/20261011T234252Z-fleet05-A096-live-gap-ledger/code/check_level12.py --mode pilot
    python -X utf8 runs/20261011T234252Z-fleet05-A096-live-gap-ledger/code/check_level12.py --mode full

The pilot covers all 278 sign functions at n=0,1,2,3. The full job covers all 65,536 functions at n=4. The initial pilot passed 3,259 assertions in 0.0132 seconds. After adding one explicit rational-constant assertion, the pilot was rerun with the final helper; the final output in out/PILOT.json is authoritative. The full job passed 1,048,593 assertions in 4.9037 seconds. Integer Walsh transforms are cross-checked against direct physical flip counts. Each derivative support identity and (1) is certified; H2 and T12 are bounded using exact integer fixed-point outward enclosures for rational logarithms. out/FULL.json records the witness and bounds. No floating entropy sign is accepted.

The log kernel range-reduces to [1,2), uses 18 positive atanh terms with geometric remainder, takes all four division endpoints for ln2, and rounds outward to a denominator 2^50. The 17 exact powers-of-two regression cases include negative logarithms. The rational comparison (7) is checked directly. The census certifies only its frozen finite domain; the proof above covers every dimension. Estimated memory is 60 MB, below the memok trigger, and no job exceeding 300 MB was started.

## proof dependencies and changed downstream conclusions

The new bundled claim A096-UNIVERSAL-LEVEL12-ERASURE@1 is self-contained, with no pending external proof dependency. It includes the supporting level-two entropy estimate. It uses full Booleanity through sparse derivatives, a proved linear-form exponential bound, and a normalized pair reference. The source-bound C018 decomposition is an application context, not a premise of the new inequality.

Ledger intake: 125 saved reports, 236 source claim records, and all 100 packet observations at the recorded cutoff. Source presence is not acceptance. The current delta carries the A096 sign repair, the precise A090 review scope, and A021 v1 remainder invalidation with the v2 substitution. It does not withdraw unrelated exact KL identities or turn the control-first class ledger into a universal tree payment. Existing shared indices, other agents' folders and remote repositories were not modified.

Changed mathematical frontier: the universal erasure remainder starts at level two rather than level one. The lead's proposed possibility that T12/I might diverge for actual Boolean signs is ruled out by (6)-(7). The divergent real-vector control remains a guard against discarding Booleanity. Claims, hypotheses, proof sources, unchanged prior versions and the correction destinations are saved as a proposed adoption delta for the supervisor.

## one next mathematical action and independent reviewer

Next: construct a single influence-weighted reference for all levels >=3 using the actual sparse-derivative spectral measures, retaining its total normalizer and the sharing of one influence budget across levels. Start from the exact row identity in (1); determine what replaces its level-one linear-form moment when the row has arbitrary degree. An unsummable sequence of fixed-level constants is not sufficient. A090 is the primary independent reviewer of this new fragment, A094 alternate; A088 can audit where full Booleanity enters. Named consumers: B20, A031/A033, A057, A064 and A099. Half-tax review is retired as directed; A090's saved review is consumed rather than rerun.

## actual persistence receipts or precise save blocker

Saved inside the assigned stage run: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, CORRIGENDUM.md, DERIVATION.md, frozen spec, code and out/. STATUS.md is two lines. WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPT.json records file sizes/SHA256 and checks the exact protocol fields, progress-copy identity and final Universal bridge paragraph. No git, Brain write, other-agent write, external message, independent acceptance of the new claim, supervisor copy or mirror verification is claimed.

## Universal bridge

This stage moves C018, directly on all Boolean functions: after B20's paid root pairs, the next complete erasure layer now costs at most (16700/2187)I<8I, so B<=([2/(sqrt(e)ln2)]+16700/2187)I+R_ge2. A uniform bound R_ge2<=K I would imply full FEI with constant K+2/(sqrt(e)ln2)+16700/2187+2/ln2; that bound remains unproved. NEXT targets one normalized reference for the whole remaining higher-level bill from actual sparse derivatives, with a single conserved influence budget, because repeating this universal fixed-level proof separately spends I again at every level. It therefore attacks the precise remaining universal bridge rather than adding an isolated structural class result.
