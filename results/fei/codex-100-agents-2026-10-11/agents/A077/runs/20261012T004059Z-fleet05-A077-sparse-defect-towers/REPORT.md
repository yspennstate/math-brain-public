# A077 stage 2 — majority's scalar child-defect surcharge diverges

## exact target, quantifiers, hypotheses and units

For odd n, f=Maj_n(x)=sign(sum_i x_i), with independent uniform physical signs. At a queried node v with actual Boolean children g,h, let j_v=min(Pr(g!=h),Pr(g=h)), kappa(g)=1-max_S ghat(S)^2 and kappa_min=min(kappa(g),kappa(h)). In bits define the LOG_ALLOCATION Section 5 scalar bill

\[
\Lambda_{\mathcal T}=\sum_{v\text{ internal}}w_vj_v\log_2(1+\kappa_{\min,v}/(2j_v)),
\]

with zero-j summands zero. T is any complete, deterministic adaptive single-coordinate physical restriction tree, querying only unfixed coordinates and stopping when constant. Randomized orders satisfy the same result by averaging. Define Lambda_noniso by deleting the bill of every node whose two child squared Fourier laws agree, while still continuing the complete restrictions.

For every odd n>=511 and every such tree,

\[
\frac{\Lambda}{I}\ge\frac{n+1}{4n}\log_2\left(1+\frac{\sqrt{3n+1}}{20}\right)
\ge\frac18\log_2n-1,
\]

\[
\frac{\Lambda_{\rm noniso}}{I}\ge\frac{n+1}{8n}\log_2\left(1+\frac{\sqrt{3n+1}}{20}\right)
\ge\frac1{16}\log_2n-\frac12.
\]

For every odd n>=3,

\[
\Lambda_{\rm noniso}\le\Lambda\le I\frac{n-1}{n}\log_2(1/a_n)
\le\frac I2\log_2(2(n-1)),\qquad
a_n=2^{-(n-1)}\binom{n-1}{(n-1)/2},\ I=na_n.
\]

Thus both complete-tree scalar bills are Theta(I log n). This is an exact all-dimensional failure of the proposed scalar **complete-tree** linear payment, including the proposed isospectral deletion repair. The true H/I is bounded for majority by the supplied threshold theorem. Stopping at a majority leaf with an external threshold certificate is permitted and is not refuted; complete-tree failure is not a failure of all stopping schemes. The sharper numerical leading coefficient 1/2 remains unproved by this lower bound. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

At stage start read BOARD.md, supervisor snapshot 2026-10-12 00:39 UTC, B16 STREAM_NOTES.md v2 (2026-10-11 23:25Z), and own STATUS.md. The stream lead directs A077 to drop bounded-H/I retained-KL tests and prove the explicit good-node mass and kappa bounds for B16-MAJORITY-LAMBDA-DIVERGENCE@1. This stage follows that direction; it supersedes our previous NEXT about bent-surgery Q/I tests.

Read the lead's full CLAIMS.json in claude/B16/runs/20261011T225600Z-claude-B16-retained-kl-sandwich. Its majority claim is EVIDENCE and names the first unsupported line; this report supplies an analytic proof, not acceptance of its floating constants. Its retained-KL sandwich follows independently from the already read node bounds and entropy/influence telescopes; here it is used only to explain the redirection, not to prove the new majority result.

Read A076's new report runs/20261011T233829Z-fleet05-A076-threshold-and-tribes-controls/REPORT.md: its majority-of-tribes canonical-shuffle obstruction has different scope. Our result concerns ordinary majority and every complete adaptive coordinate tree, with the exact isospectral deletion included. We do not repeat its mixed-family schedule enumeration or arbitrary-core transport.

Prior-stage sources retained: EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2; LOG_ALLOCATION_CURATED Sections 2 and 5 for the candidate definition and stopping/terminal scope; ISOSPECTRAL_SPLICING_CURATED for the distinction between scalar and exact retained-profile charges. The supplied 38-page threshold paper Theorem A (C001) implies H(Maj_n)<=C_reg I, C_reg<8.937; that existing result is cited only to distinguish the scalar failure from FEI. No external research theorem or local-limit estimate enters the new lower bound. out/SOURCE_RECEIPTS.json pins the local source bytes actually used. Brain and web queries were unnecessary.

## complete derivation or exact first unsupported line

### 1. Exact monotone coefficient maximum

For any monotone Boolean g, in physical sign coordinates,

\[
\widehat g(S)=\mathbb E[ D_i g\,\chi_{S\setminus\{i\}}],\quad
D_i g=(g(x_i=1)-g(x_i=-1))/2\in\{0,1\},\quad i\in S.
\]

Consequently |ghat(S)|<=Inf_i(g), while ghat({i})=Inf_i(g). Thus

\[
\max_{S\ne\varnothing}|\widehat g(S)|=\max_i\operatorname{Inf}_i(g),\quad
\kappa(g)=1-\max\{(\mathbb Eg)^2,\max_i\operatorname{Inf}_i(g)^2\}.
\]

Input sign changes give the same statement for unate functions with absolute singleton coefficients. This sharpens the lead's weaker inequality ghat(S)^2<=Inf_i(g). It needs no Krawtchouk maximum search.

### 2. Elementary central-binomial bounds

Put c_k=2^-k binom(k,floor(k/2)). For r>=1,

\[
\frac1{2\sqrt r}\le c_{2r}\le\frac1{\sqrt{3r+1}}.
\]

The upper bound starts at c_0=1 and the recurrence c_(2r+2)/c_(2r)=(2r+1)/(2r+2) preserves it because

\[
\frac{(2r+1)^2}{(2r+2)^2}\le\frac{3r+1}{3r+4}.
\]

After cross multiplication the right minus left numerator is r. The lower bound starts at r=1 and is preserved since the same ratio squared is >=r/(r+1), with positive cross-multiplied numerator 1. Also c_(2r+1)=c_(2r+2). Hence for k>=1,

\[
c_k^2\le\frac2{3k+2},\qquad c_k\le\frac1{\sqrt{k+1}}.
\]

For even N>=2, c_N>=1/sqrt(2N). These are inequalities of rational squares; no unproved numerical constant is used.

### 3. Physical states and pivotal-bridge mass

After d reveals, set m=n-d and let s be their sum. The residual function is sign(s+X_1+...+X_m). Any adaptive fresh coordinate order has the same distribution of the first d revealed signs: independent fair signs. At d<=(n-1)/2 all nodes are still nonconstant, since |s|<=d<m. The queried disagreement is

\[
q_d(s)=\Pr(X_1+\cdots+X_{m-1}=-s)
=2^{-(m-1)}\binom{m-1}{(m-1-s)/2}.
\]

For m>=2, q<=c_(m-1)<=1/2, so j=q. Summing over s gives E j=a_n by Vandermonde. Weighting a node by its j instead of merely its history probability conditions the total of N=n-1 signs to zero. The first d signs then form an exchangeable balanced sampling bridge. Symmetry gives E X_i=0; expanding (sum_(i=1)^N X_i)^2=0 gives E X_iX_j=-1/(N-1) for i!=j. Therefore

\[
\mathbb E[S_d^2\mid S_N=0]=\frac{d(N-d)}{N-1}.
\]

For d<=N/2 and m=N+1-d this variance is <=m/2: the ratio d(N-d)/[(N-1)(N+1-d)] is increasing up to d=N/2, where the desired inequality reduces to N^2<=(N-1)(N+2), valid for N>=2. Chebyshev yields

\[
\mathbb E_s[j_d(s)\mathbf1_{\{s^2\le m\}}]\ge a_n/2.
\]

There are L=(n+1)/2 depths d=0,...,(n-1)/2, so the probability-weighted good-node mass is at least L a_n/2=(n+1)a_n/4>=I/4. All history probabilities and all queried influence are included. No improbable branch is used without its weight.

### 4. Uniform kappa on good nodes

At a good node s^2<=m, either child has k=m-1 remaining signs and shift t=s+/-1, hence |t|<=sqrt(m)+1. There are no ties, since k+t is odd. By symmetry, the absolute child mean equals the probability that its Rademacher sum lies strictly between -|t| and |t|, an interval containing |t| support atoms. Each atom has probability at most c_k. Thus

\[
|\mathbb Eg|^2\le(\sqrt m+1)^2c_{m-1}^2
\le\frac{2(m+2\sqrt m+1)}{3m-1}\le\frac45\quad(m\ge256).
\]

The last inequality is equivalent to m-10sqrt(m)-7>=0, which is positive at 256 and increasing thereafter. Each child influence is at most c_(m-2)<=1/2 when k>=2; its squared nonempty Fourier maximum is therefore <=1/4 by Section 1. Consequently kappa(g),kappa(h)>=1/5. If n>=511, every first-half residual m is >=256, so this holds at every good node.

The queried j also satisfies j<=c_(m-1)<=sqrt(2/(3m-1)). Therefore each good node logarithm is at least

\[
\log_2(1+\tfrac1{10}\sqrt{(3m-1)/2})
\ge\log_2(1+\sqrt{3n+1}/20).
\]

Multiply by the good mass from Section 3 to obtain the first claimed lower bound. Since sqrt(3n+1)/20>=sqrt(n)/16, the convenient bound (1/8)log2(n)-1 follows. No child entropy or independent tensor spectator is paying this bill.

### 5. Removing every exact isospectral split

At a nonconstant majority state with j>0, child means satisfy mu_+-mu_-=2j>0. Equality of their squared means requires mu_++mu_-=0, equivalently zero parent mean. For a nonconstant majority threshold with the allowed parity this occurs exactly when s=0. Conversely at s=0 the children satisfy g_-(x)=-g_+(-x), so their squared Fourier laws agree. Hence the active exactly isospectral nodes are precisely s=0. Zero-j nodes contribute nothing anyway.

For d even, the pivotal-bridge probability of s=0 is

\[
\Pr(S_d=0\mid S_N=0)=c_d c_{N-d}/c_N\le2/\sqrt{d+1}\quad(0\le d\le N/2).
\]

For odd d it is zero. The displayed bound follows from Section 2 and N-d>=N/2, and remains valid at d=0. Summing over all these depths, even if we overcount odd ones,

\[
\sum_{d=0}^{L-1}\mathbb E[j_d\mathbf1_{s=0}]\le4a_n\sqrt L,
\]

because sum_(u=1)^L u^-1/2<=2sqrt(L), by integration on each interval [u-1,u]. For n>=511 we have L>=256, hence 4sqrt(L)<=L/4. Subtracting this from the good mass L a_n/2 leaves at least L a_n/4=(n+1)a_n/8>=I/8 at good **nonisospectral** nodes. The same logarithm lower bound proves the second theorem. This deletes summands only; it does not grant free arbitrary leaf certificates.

### 6. Matching logarithmic upper order

At every depth with m>=2, j<=1/2 and kappa_min<=1, so

\[
j\log_2(1+\kappa_{\min}/(2j))\le j\log_2(1/j).
\]

After padding constant branches by ignored zero-cost queries, E j=a_n at each depth d=0,...,n-2. Concavity of x log2(1/x) gives expected cost <=a_n log2(1/a_n) at each depth. At residual dimension one, the possible nonconstant threshold is a character and j=0. Thus Lambda<=(n-1)a_n log2(1/a_n). The lower central-binomial bound a_n>=1/sqrt(2(n-1)) proves the asserted upper bound. Complete adaptive coordinate choice changes neither the pivotal distribution nor these bounds.

The first unsupported universal line remains a hereditary retained-profile or actual-erasure transport rule that pays both physical descendants and terminal entropy on arbitrary Boolean cores. This report refutes replacing that transport with the scalar Lambda bill on complete trees, even after its isospectral deletion. It does not claim the exact asymptotic coefficient, a failure for every certified stopping rule, or any unbounded H/I.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation. Pilot: odd majority roots n=3,5,9,17,33,65; 33 full Walsh child-threshold cases k=1..6; exact binomial-induction checks through r=1025. **4,583 assertions passed**, Python runtime 0.1881 seconds. The full fixed domain additionally contains n=129,257,511,513,1025, and verifies every first-half pivotal-bridge state, every good child kappa for n>=511, and both mass lower bounds. Integer FWHT verifies the monotone maximum identity independently on the 33 child truth tables. Integer binomial counts independently verify E j=a_n, the bridge variance, the Chebyshev mass and center-state bounds. No floating ratios establish a sign.

The initial full run passed **103,510 assertions**, Python runtime 12.2470 seconds. The final run additionally encloses the logarithmic upper bound and checks its compatibility with each lower certificate; final counts, runtime and hashes are in out/full.json and out/ARTIFACT_MANIFEST.json. No test domain was enlarged. Estimated memory is under 60 MB, below the 300 MB memok trigger; no observed peak measurement is claimed. No GPU or background process was used.

Commands from the agent root:

```
python -X utf8 runs\20261012T004059Z-fleet05-A077-sparse-defect-towers\code\check.py pilot
python -X utf8 runs\20261012T004059Z-fleet05-A077-sparse-defect-towers\code\check.py full
```

Log2 certificates use dyadic reduction, a positive 32-term atanh series, proved tail 2z^65/[65(1-z^2)], positive ln2 interval division and outward rounding to denominator 2^120. For the radical lower bound, replace sqrt(3n+1) by floor(sqrt(3n+1)); the bound is then a rational-log certificate with the correct inequality direction. All probability and influence checks use exact integers/Fraction. The infinite-family statement is proved analytically in Sections 1-6, not extrapolated from n<=1025.

## proof dependencies and changed downstream conclusions

The analytic majority theorem uses only the explicit Boolean threshold, elementary Walsh differentiation, elementary central-binomial recurrence, exact sampling variance, Chebyshev and concavity. The lead's numerical majority claim is the target being completed, not a proof premise. No unreviewed claim is required for the result. The existing threshold FEI bound is background for its scope distinction; it is not used in proving the scalar divergence.

This closes the lead's first unsupported line with constants good mass >=I/4 and kappa_min>=1/5 (odd n>=511), and strengthens the warning to all complete adaptive orders with isospectral deletion: good nonisospectral mass >=I/8. The broader exact leading coefficient 1/2 conjecture remains open. A076's mixed-family claim is complementary and is not adopted or independently accepted here. The stage completes an existing lead candidate rather than opening another unrelated broad conjecture after the stream's review cap.

## one next mathematical action and independent reviewer

Independent reviewers: A092, alternate A088. Reconstruct the sampling-bridge variance, uniform child-mean bound and center-state removal argument. Next mathematical action: derive a hereditary node majorant from the actual monotone derivative packet profile, using the exact maximum-coefficient identity above, that recognizes low true-erasure majority nodes without discarding arbitrary terminal-core entropy in the shifted majority/core family from A076. A078 receives the constants and ordinary-majority fixture for its requested profile-based replacement. No external messages or other-agent writes were used.

## actual persistence receipts or precise save blocker

All four protocol files, FROZEN_SPEC.json, code/check.py, code/persist.py, exact output certificates, MULTISCALE_COST_LEDGER.json and proof TeX are saved in this assigned run directory. The agent root STATUS.md and LEARNED.md are updated and WORKLOG.md is appended. out/ARTIFACT_MANIFEST.json records local hashes and sizes; out/SOURCE_RECEIPTS.json identifies read source bytes. Schema validation interprets the protocol's parenthetical annotation of packet_ids as the compatibility key packet_ids. Supervisor copying, mirror verification and independent acceptance are not claimed.

## Universal bridge

This stage moves **C019 stopping-tree payment** by completing B16's majority scalar-overcharge warning with an all-dimensional, all-complete-adaptive-order proof: good pivotal mass >=I/4, child defect >=1/5, and even after exact-isospectral deletion the bill/I grows at least (log2 n)/16-1/2, while majority's H/I is already bounded. The scalar replacement is therefore rigorously unusable as a universal complete-tree payment; the retained-profile and paid-terminal stopping obligations remain open. NEXT targets the actual derivative-packet majorant through A076's shifted arbitrary-core child because it must repair precisely this demonstrated loss while retaining full-FEI terminal difficulty, rather than spend another stage improving a known class constant.
