# A090 stage 3: the terminal refund cannot be compressed to degree

## exact target, quantifiers, hypotheses and units

The live A099/A096 frontier is a signed-Boolean terminal-core KL lower bound paying the same complete conditional-edge bill with one physical influence reserve. Its normalized refund identity is already independently reconstructed by A073 and A099, so this stage does not repeat that baseline or the retired five-bit census/half-tax audit. It audits a new downstream compression mechanism: replacing each full derivative/reference row divergence by its divergence after retaining only the residual Fourier degree.

New result A090-DEGREE-COARSENED-REFUND-OBSTRUCTION v1, author-proved and pending independent review: this compression cannot yield a dimension-independent retained-price bound, even for actual Boolean tribes whose full retained price is at most six times influence.

For every integer w>=4 let m=2^w, p=1/m, beta=1-p, n=mw, and take

    f_w=1-2 product_(b=1..m)(1-A_w(x_b)),

where all width-w blocks are disjoint and A_w is the all-zero point conjunction. The sign is +1 on the OR of the conjunctions. For a relevant coordinate i set

    epsilon_i=Inf_i(f), mu_i(T)=p_(T+i)/epsilon_i,
    r_i(T)=p_T+p_(T+i),
    bar_mu_i(t)=sum_(|T|=t)mu_i(T),
    bar_r_i(t)=sum_(|T|=t)r_i(T).

Both mu_i and r_i are normalized row probability laws. Every entropy and KL below is in bits; p_S=fhat(S)^2, ordinary physical influence is I=sum epsilon_i. Define

    M=sum_i epsilon_i[log2(1/epsilon_i)-D2(mu_i||r_i)],
    M_degree=sum_i epsilon_i[log2(1/epsilon_i)-D2(bar_mu_i||bar_r_i)].

For the actual family, every epsilon_i=epsilon=2p beta^(m-1), I=2w beta^(m-1), and

    0<=D_degree<=3+log2(w+1/2),
    M_degree/I>=w-4-log2(w+1/2).

In particular M_degree/I>=w/2 for all w>=32, while 0<=M<=B<=H<=6I for all w>=4. The discarded within-degree KL refund per influence is at least w/2-6 for w>=32 and diverges. This is a mechanism obstruction, not a disproof of FEI and not a no-go for full function-specific conditional-edge references.

## sources actually read, revisions and theorem locators

Stage start: BOARD.md dated 2026-10-14 01:00 UTC, B18 STREAM_NOTES v2 (dated 2026-10-11 23:34 UTC), own STATUS.md. The lead's earlier N5/half-tax targets remain superseded by completed reviewed baselines, as recorded in stage 2; no disagreement with their mathematical statements is inferred. The current board directs A096/A001/A073 toward terminal-core KL payment.

Read source statement records, before new derivation: A096 run 20261013T220343Z-account05-A096-live-gap-ledger/CLAIMS.json, especially A096-TERMINAL-KL-REFUND-AUDIT v1; A099 run 20261014T001305Z-account05-A099-candidate-assembly/CLAIMS.json, including the inherited refund and parity-tail review records; A001 run 20261013T213937Z-account05-A001-quantifier-audit/CLAIMS.json for the already known influence-only and all-degree-majorant scope. A targeted rg of BOARD/A096/A045/A046/A073 located the existing reviews and found no degree-coarsening claim in those inputs. This is not a global novelty search.

The agent's stage-2 exact parity-tail statement has received A096 and A099 substantive reconstructions in the source records, and A081's independent reconstruction is reported on the board. That prior result is not rechecked here. The protocol field contract is EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. The original ERASURE_REDUCTION.md sections 1,3,5 define B, its entropy domination and the one-sided edge charge; those definitions are rederived below. Neither the threshold nor percolation paper is needed for the new theorem.

DERIVATION_CHECKPOINT.md was saved before computation, then DERIVATION_REFINEMENT.md saved the exact mean simplification and improved constants. No candidate author proof or checker is copied. The source statements do NOT assert that degree coarsening suffices; this stage tests a proposed shortcut to their open lower bound. Source byte hashes and local receipts appear in out/SOURCE_MANIFEST.json and out/RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. The normalized identity and exactly what coarsening loses

For any actual Boolean f and relevant i, sum_T r_i(T)=1 and sum_T mu_i(T)=1. Direct expansion of KL gives

    epsilon_i[log2(1/epsilon_i)-D2(mu_i||r_i)]
      =sum_T p_(T+i) log2((p_T+p_(T+i))/p_(T+i)).     (1)

Thus M is the one-sided downward edge charge, not a new unpriced information term. Each summand is nonnegative. Its complementary upward term gives the binary edge entropy, so M<=B. Conditioning reduces entropy and the entropy chain rule give B<=H. No independence of spectral bits is assumed.

Applying the KL chain rule to the deterministic map T->|T| gives

    D2(mu_i||r_i)=D2(bar_mu_i||bar_r_i)
      +sum_t bar_mu_i(t)
          D2(mu_i(.|t)||r_i(.|t)).                  (2)

Consequently

    M_degree-M=sum_i epsilon_i sum_t bar_mu_i(t)
                              D2(mu_i(.|t)||r_i(.|t))>=0.  (3)

This is also an honest complete normalized row reference: on positive bar_mu degrees define tilde_r_i(T)=bar_r_i(t)mu_i(T)/bar_mu_i(t); on zero bar_mu degrees choose any normalized conditional law. Its degree marginal is bar_r_i, total mass is one, it is positive wherever mu_i is positive, and D2(mu_i||tilde_r_i)=D2(bar_mu_i||bar_r_i). It is function-dependent, so the existing influence-only reference obstruction does not by itself settle this case. Equation (3) identifies its actual lost conditional refund.

### 2. Actual Boolean spectra and exact degree laws

Each factor b=1-A_w has Fourier coefficient beta at the empty set and -p at every nonempty set, with squared norm beta. Its normalized squared spectrum has probability beta at the empty set and p/(m-1) at each nonempty set. Equivalently a block is active with probability p; conditional on activity its subset is uniform nonempty. Write xi_w for that active block's degree distribution:

    xi_w(t)=binom(w,t)/(2^w-1), 1<=t<=w.

Let nu be the degree law of the product of m normalized factor spectra. Its PGF is

    [beta+p*((1+z)^w-1)/(2^w-1)]^m.                 (4)

The number L of active blocks is Bin(m,p), with E L=mp=1, and given L its degree is the sum of L independent xi_w variables. For the Boolean OR sign, its squared degree masses W_t are

    W_0=(1-2beta^m)^2,
    W_t=4beta^m nu_t for t>=1.                       (5)

This Fourier formula is an exact product expansion of an actual sign-valued function, not a relaxed spectral vector. Each coordinate's pivotal event requires the other w-1 bits in its block to activate and all other blocks to be inactive, so

    epsilon=2p beta^(m-1), I=n epsilon=2w beta^(m-1). (6)

The group of within-block and block permutations is transitive on coordinates and preserves degree. It does not act transitively on every fixed-degree subset. Coordinate transitivity alone yields

    bar_mu(t)=(t+1)W_(t+1)/I,
    bar_r(t)=(1-t/n)W_t+((t+1)/n)W_(t+1),
       0<=t<=n-1.                                  (7)

In particular, for t>=1,

    bar_r(t)>=4beta^m(1-t/n)nu_t.                    (8)

The derivative degree law has another independent representation. Conditioning a selected coordinate to be in the squared spectrum forces its block and makes the other w-1 coordinates of that block uniform independent Fourier bits. Other blocks retain their normalized b spectra. Thus

    T_mu=U+sum_(b=1..m-1) V_b,
    U~Bin(w-1,1/2),
    P(V_b=0)=beta;  P(V_b=t)=p xi_w(t), t>=1.

All variables in this representation are independent. It gives exactly

    bar_mu(0)=2p beta^(m-1)=epsilon,
    E T_mu=(w-1)/2+(m-1)p*w/(2beta)=w-1/2.           (9)

### 3. A pointwise domination that retains the true degree marginals

For t>=1, the nonzero U masses obey

    P(U=t)/xi_w(t)=2beta*(w-t)/w<=2beta.

The zero U mass is 2p. If U=0, the active-block count from the other m-1 blocks is Bin(m-1,p). Its likelihood ratio against Bin(m,p) at count j is (m-j)/(m beta)<=1/beta. This component of bar_mu is bounded pointwise by (2p/beta)nu.

For the U>0 component, replace U's subprobability by 2beta times xi_w and force one active block. The resulting total count L'=1+Bin(m-1,p) has likelihood ratio j/(mp)=j against Bin(m,p). Every active block has degree at least one; on total degree t its count j is at most t. Therefore

    bar_mu(t)<=(2p/beta+2beta t)nu_t, t>=1.           (10)

This inequality does not assert uniformity of spectra within degree. It arises from the exact conditional block-count distributions, and will be used only for the coarsened row.

### 4. Uniform analytic KL bound, without numerical entropy estimates

For w>=4, elementary logarithm inequalities give

    1/4<=beta^m<=e^-1<3/8,
    e^-1<=beta^(m-1)<=1/2.                           (11)

For the lower bound use ln(1-p)>=-p/(1-p), whence beta^m>=exp(-m/(m-1))>=exp(-4/3)>1/4. The last comparison follows from ln2>2/3. The upper bound uses ln(1-p)<=-p and e>8/3. For beta^(m-1)<=1/2, expand (1+1/(m-1))^(m-1)>=2; the lower bound follows from the same logarithm inequality. Both ln2>2/3 and e>8/3 follow from positive elementary series, not numerical approximations.

By (5), bar_r(0)>=W_0>=1/16. Equations (9),(11) give bar_mu(0)=epsilon<=p<=1/16. Therefore the zero-degree contribution bar_mu(0)log2(bar_mu(0)/bar_r(0)) is nonpositive.

On the head 1<=t<=n/2, combine (8),(10),(11). Since beta>=3/4 and p<=1/4,

    bar_mu(t)/bar_r(t)
      <=(2p/beta+2beta t)/(2beta^m)
      <=4/3+4t<=4(t+1).                             (12)

Thus the entire head contribution is at most

    2+E log2(T_mu+1)<=2+log2(w+1/2),                 (13)

by (9) and Jensen. Dropping negative terms was only done using valid upper bounds; no positive-only truncation is substituted for KL.

For the tail, (9) and Markov give P(T_mu>n/2)<=2/m. The actual row law always obeys r_i(T)>=epsilon mu_i(T), and therefore also bar_r(t)>=epsilon bar_mu(t). Hence its log ratio is bounded above by log2(1/epsilon). From (6),(11),

    w-1<=log2(1/epsilon)<=w-1+log2 e<w+1/2.

Here log2 e<3/2 follows from ln2>2/3. The tail contribution is at most

    2(w+1/2)/2^w<=9/16<1, w>=4,                    (14)

as (w+1/2)/2^w decreases for integer w>=1. Adding (13),(14) and the nonpositive zero term proves

    D_degree<=3+log2(w+1/2).                         (15)

Normalization proves D_degree>=0. Since every coordinate has the same row and influence,

    M_degree/I=log2(1/epsilon)-D_degree
                >=w-4-log2(w+1/2).                 (16)

For all real w>=32, log2(2w)<=w/4: it holds at32, and its right-minus-left derivative is 1/4-1/(w ln2)>0 thereafter. As w+1/2<=2w and 4<=w/4, (16) is at least w/2 for every integer w>=32. This is an all-w proof of divergence on actual Boolean functions, not extrapolation from the finite certificates.

### 5. The complete retained cost stays bounded

For a nonempty Fourier set hitting j blocks, its squared mass is 4p^(2j)beta^(2(m-j)). Under the normalized product law in (4), E j=mp=1. Expanding the atom entropies gives the exact formula

    H=h(W_0)+8w beta^m
      -8beta^m log2(beta)[m(1-beta^m)-1]
      -8beta^m(1-beta^m),                            (17)

where h(x)=-x log2 x. Since h(W_0)<=1, m(-log2 beta)<=[m/(m-1)]log2 e<8/5 for m>=16, and the last term is nonpositive,

    H<=8w beta^m+13beta^m+1.

Divide by I=2w beta^(m-1), use beta<=1 and beta^(m-1)>=e^-1>1/3, and obtain

    H/I<=4+8/w<=6, w>=4.                            (18)

Together with (1), M<=B<=H proves 0<=M<=6I. By (3),(16), for w>=32 the normalized discarded conditional refund satisfies

    (M_degree-M)/I>=w/2-6 ->infinity.                (19)

Thus the exact full conditional-edge KL contains a growing within-degree refund. The entire row degree distributions are function-specific and exact, yet retaining them alone still loses the payment. No influence-only or arbitrary-real-vector premise appears.

### 6. The first unsupported implication in the live universal bridge

The first universal line remains

    D2(P_joint||Q_joint)>=Gamma(f)-K,
    Gamma(f)=I(f)^-1 sum_i epsilon_i log2(1/epsilon_i),

with the actual normalized derivative/reference joint laws and an absolute K. It is equivalent to a universal M<=KI bound, hence FEI-strength through C018. The tempting replacement of the full divergence by its degree marginal is FALSE: (16) defeats every finite K.

Neither A096 nor A099 asserts this false replacement. Their existing identities and scoped acceptances remain valid, and the actual full divergence is not refuted by this family. The required contribution is a single owned bound retaining the conditional within-degree term in (2) together with terminal entropy. Paying each degree independently or keeping only its scalar mass is not licensed by data processing.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded all computation. The family is exactly the Boolean OR above; fixed w=4,5,6,7, four functions with n=64,160,384,896, and all 1,504 residual degree packets. Symmetry is the proved coordinate-transitivity reduction only. No 2^n truth table enumeration, arbitrary spectral vector, numerical entropy sign, automatic dimension increase, or job over 300 MB was used. Memory estimate <80 MB; both commands have a 60-second computation guard.

Commands from A090:

    python -X utf8 runs/20261014T010003Z-account05-A090-independent-reconstruction/code/check_degree.py --pilot
    python -X utf8 runs/20261014T010003Z-account05-A090-independent-reconstruction/code/check_degree.py

Pilot w=4: PASS 557 exact assertions, 64 packets, 0.0146902 seconds. Full frozen domain: PASS 12,836 exact assertions, four functions, 1,504 packets, 2.1690046 seconds. Integer polynomial convolution and Fraction verify the two independent degree-law representations, all normalizations, I=n epsilon, exact derivative mean, pointwise mu/r and nu domination, the head bound, tail probability bound, and all vacuum inequalities. out/PILOT.json and out/CHECK.json preserve results. The checker computes the full generating functions, not a truncated tail or a floating spectrum. The analytic logarithmic estimates (11)-(19) establish all widths and the infinite-ratio obstruction.

## proof dependencies and changed downstream conclusions

New A090-DEGREE-COARSENED-REFUND-OBSTRUCTION v1 is author-proved and pending independent review; A090 does not independently accept its own new theorem. The proof is self-contained from the actual Boolean factor Fourier expansion, elementary probability/KL chain rules, rational binomial identities and scalar logarithm inequalities. It does not depend on an unproved A096 lower bound, FEI, or the prior parity-tail theorem. A096's row definitions are adopted as the audited target and equation (1) is rederived directly.

The source claims retain their reviewed scope. The prior A090 parity-tail claim now has substantive independent acceptance records from A096 and A099, which are consumed as completion evidence and not reopened. A073's normalized terminal audit is also recognized rather than repeated. The new downstream exclusion adds a function-dependent boundary beyond A001's influence-only reference scope: even exact degree marginals of the function-dependent derivative and reference laws do not recover the necessary refund. It excludes neither full conditional-edge references nor paid global stopping trees.

## one next mathematical action and independent reviewer

Next: A096/A001/A073 should audit a proposed reference that explicitly retains or pays the within-degree conditional KL in (2), and evaluate it on these actual tribes rows and the parity-tensor activation rows using one physical influence ledger and complete terminal core entropy. A094/A085 should independently reconstruct the block-count likelihood domination (10), the head/tail KL estimate and the distinction between full-subset exchangeability and coordinate transitivity. This directly tests the missing universal refund, not another fixed-level theorem or a completed class bound.

## actual persistence receipts or precise save blocker

The assigned run contains the four protocol files, DERIVATION_CHECKPOINT.md, DERIVATION_REFINEMENT.md, DEGREE_REFUND_PROOF.tex, FROZEN_SPEC.json, code/check_degree.py, exact pilot/main outputs, source manifest, schema validation and receipt hashes. STATUS.md has exactly two lines, WORKLOG.md is appended with the stage and outcomes, and LEARNED.md records the durable conditional-refund distinction. All writes are confined to A090. No shared ledger, other-agent output, brain, mail, git or external application was modified. Supervisor copy, remote mirror, canonical adoption and independent review of the new obstruction remain outstanding.

## Universal bridge

This stage moves C018's terminal-KL refund audit by proving on actual tribes that degree coarsening leaves a retained cost/I at least w/2 while the full retained cost/I is at most6, so the discarded within-degree refund/I grows at least w/2-6. It supplies no FEI constant and refutes no full conditional-edge theorem; the dimension-independent signed-Boolean lower bound on the complete terminal divergence remains unpaid. The shortest NEXT is one source-complete conditional reference retaining the within-degree term on the same tribes and arbitrary-core activation rows, because the exact no-go identifies the information that the live universal mechanism must preserve rather than adding another isolated class result.
