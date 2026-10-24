# A095: ordered pivotal-height criterion and the rank/KL frontier

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This stage extracts two complete statements, with independent acceptance pending for the new statements. It also independently reconstructs B19-RANKCODE-REDUCTION v1 and B19-RANKCODE-GLOBAL-ORDER-NOGO v1. No novelty or priority claim is made.

Let f:{-1,1}^n -> {-1,1} have the uniform Fourier law P(S)=fhat(S)^2. H is in bits, I=sum_i Inf_i=E|S|, and ln and all KL quantities explicitly marked D_nat use natural logarithms. A coordinate order sigma has positions 1,...,n; pi below denotes the numerical circle constant, never a coordinate order. Put

    R_sigma(f)=E_P sum_{j=1}^{|S|} ln(i_j/j),

where i_1<...<i_|S| are the positions in sigma of S. Empty sets contribute zero. Write A=log2(4+e)+log2(pi^2/4).

Statement 1 (physical criterion). For each coordinate i at position p, let U_i be its p-1 predecessors. Fixing the remaining coordinates of the derivative cube gives a fiber of supp(d_i f) on U_i. Suppose EACH such fiber admits an orientation of U_i in which its longest strictly increasing chain has at most r_i points, for specified integers r_i>=1. Orientations may vary between coordinates AND between fixed-future fibers. Then

    H(f) <= A I(f) + (2/ln2) sum_i Inf_i(f) L(r_i),
    L(r)=min{r(1+ln2), 2+gamma+2 ln r}.

In particular r_i<=r gives a dimension-independent FEI constant A+(2/ln2)L(r); r=1 recovers C_reg exactly. More generally sum_i Inf_i ln r_i <= K I gives

    H(f) <= [A+(2/ln2)(2+gamma+2K)] I(f).

For fixed uniform r the class is closed under arbitrary physical restrictions, using the induced coordinate order. This is an intrinsic pivotal-support condition; it assumes neither unateness nor a representation as a Boolean combination of regular gates. It is a sufficient class criterion, not a characterization of all FEI functions or a claim to have found a maximal natural class. Its overlap with existing representation theorems has not been classified.

Statement 2 (exact equivalence with reference credit). For a fixed sigma, let

    Z_(n,k)=sum_{|S|=k} prod_{i in positions(S)} i^(-2),
    Q_(sigma,k)(S)=Z_(n,k)^(-1) prod_{i in positions(S)} i^(-2),
    beta_(n,k)=ln(Z_(n,k)(k!)^2),
    D_sigma(f)=sum_k P(|S|=k) D_nat(P(S | |S|=k) || Q_(sigma,k)),
    T_sigma(f)=2 R_sigma(f)-D_sigma(f).

At k=0, Q assigns mass one to the empty set, Z=1 and beta=0; zero-mass levels are omitted. For every Boolean f and EVERY order sigma,

    (ln2) H(f) = H_nat(|S|)+T_sigma(f)+E beta_(n,|S|),
    0 <= beta_(n,k) <= k ln(pi^2/4).

Let C_FEI=sup_f H(f)/I(f), over nonconstant Boolean functions in all dimensions, and let K_T=sup_f inf_sigma T_sigma(f)/I(f). In the extended real sense,

    K_T/ln2 <= C_FEI <= A+K_T/ln2.

Thus finiteness of K_T is equivalent to FEI. The exact missing universal statement is T_sigma<=K I for some order at each f, with the complete normalized KL credit retained. This equivalence does not bound K_T.

## sources actually read, revisions and theorem locators

Execution protocol fei-execution-protocol/2, revision 2026-10-11-execution-v2, was read in full. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, stream next actions, plan .tex, CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted. BOARD snapshot 2026-10-11 23:09 UTC and B19 STREAM_NOTES v1 (22:41 UTC) supplied the target and duplication guard. Full large plan/index reads exceeded terminal output limits; this report does not pretend that every unrelated packet was substantively audited.

Primary mathematical source: context/threshold_paper_38pp.txt, Lemma 2.1 (spectral-level entropy), Lemmas 3.2-3.4 (Sperner, signed relative noise, rank mean), Section 4.1 equations (18)-(19) (Euler reference), and Section 4.2/multi-rank Frullani argument. Earlier 29-page version was checked for its analogous locators and different one-order reference; the exact reduction uses the 38-page revision. The supplied percolation 30-page text, Theorems 1.1-1.2 and introduction, and theorem locators in its 31-page version, were inspected for scope only; no percolation theorem is a premise. No complete percolation proof audit is claimed.

B19 PAPER_AUDIT_38pp.md sections 1, 2, 4 and the lead's run CLAIMS.json were read. Their source pin is main.tex sha256 de36fcdab064333565b2f311db861df57b50955245d747ae7c03653d5e9bf28e, distinct from the published-source hash. That main.tex was not independently loaded here; this stage uses the supplied text and the exact lead statements. The lead run's REPORT.md was absent when requested, but PAPER_AUDIT_38pp.md and CLAIMS.json contain the pertinent proof descriptions. This is a provenance limitation, not a missing line in the proofs below.

Final source binding found declared statement SHA256 metadata inconsistent with the UTF-8 theorem strings in the imported lead claims. Local CLAIMS.json records both declared and recomputed values and corrects only local hash metadata, leaving the source and theorem strings untouched. This discrepancy needs supervisor reconciliation; it does not invalidate the independent analytic reconstructions.

The earlier B05/B19 accepted sparse-activation obstruction is read through the registry and campaign current status; it is not re-proved. The supplemental connected-component obstruction (Addendum 11.44) was read; no disjoint-physical-support entropy subadditivity is used. SEED_LEMMAS section 1 supplies a comparison point for the signed relative-noise/Frullani method; the proof below does not assume its effective-piece lemma. File hashes and exact paths are saved in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Universal rank reduction, independently reconstructed

For each k, Euler's product gives

    sum_{|S|=k} prod_{i in positions(S)} i^(-2)
       <= pi^(2k)/(2k+1)!.

This follows by comparing the coefficient of z^k in prod_{i>=1}(1+z/i^2)=sinh(pi sqrt(z))/(pi sqrt(z)); finite n only decreases the coefficient. Therefore the reference

    Q'_k(S)=((2k+1)!/pi^(2k)) prod_{i in positions(S)} i^(-2)

is a subprobability on k-sets. For S with ordered positions i_j,

    -ln Q'_k(S)=2 sum_j ln(i_j/j)
                   + ln(pi^(2k)(k!)^2/(2k+1)!).

The final logarithm is at most k ln(pi^2/4): (2k+1)!>=4^k(k!)^2, since its ratio to the right side starts at one and successive ratios are (2k+3)/(2k+2)>=1. Gibbs on each level gives

    H(S | |S|) <= (2/ln2) R_sigma + log2(pi^2/4) I.

For completeness, the Boolean spectral-level estimate is H(|S|)<=log2(4+e) I. Here is its full scalar reduction from cube edge-isoperimetry. Let p=min Pr(f=1),Pr(f=-1), v=4p(1-p)=Pr(|S|>0). Edge-isoperimetry gives I>=2p log2(1/p). This implies

    I >= v+(v/2) log2(1/v).

To verify the comparison put q=1-2p. The difference between its two sides is (1-q)/2 times

    phi(q)=(q-1)log2(1-q)+(1+q)log2(1+q)-2q.

phi(0)=phi(1)=0 and phi''(q)=-2q/((1-q^2)ln2)<=0, so phi>=0. Consequently

    h2(v)<=2I+(log2(e)-2)v.

The geometric reference (1-rho)rho^(k-1) on positive k, with rho=4/(4+e), gives

    v H(|S| | |S|>0) <= (I-v)log2(1/rho)+v log2(1/(1-rho)).

Its v coefficient cancels the one in the binary-entropy bound. The chain rule proves the asserted level estimate. v=0 is immediate and endpoints follow by continuity. Combining both bounds proves B19-RANKCODE-REDUCTION v1 with no regularity hypothesis. Cube edge-isoperimetry, Gibbs, and Euler's classical product are explicit standard premises; no unreviewed campaign claim is needed.

### 2. Bounded chain height pays the rank cost

We first prove a signed derivative lemma. Let d:{-1,1}^N->{0,+1,-1}, alpha=E d^2>0, and U have M coordinates. Suppose each U-fiber of supp(d) has increasing-chain height at most r in some orientation of that fiber. A finite poset of height at most r partitions into r antichains: assign each point the length of the longest chain ending there; comparable distinct points have strictly different labels. Every restriction to a subcube retains this property. Sperner therefore bounds support density in every q-dimensional subcube by

    min{1,r c_q}, c_q=2^(-q) binom(q,floor(q/2)) <= (q+1)^(-1/2).

Resample each U-coordinate at rate t. Given X and the mask, Y is uniform in a subcube of dimension B~Bin(M,t). Its orientation is inherited from the fixed outside-U fiber; it may depend on that fiber. Since |d|=d^2 and the mask is independent of X,

    E[d(X)d(Y)] <= E[|d(X)||d(Y)|]
                    <= alpha E min{1,r c_B}.

Parseval and the resampling identity give, for nu(T)=dhat(T)^2/alpha and kappa=|T intersect U|,

    E_nu (1-t)^kappa <= E min{1,r c_B}
                      <= r/sqrt((M+1)t).

The final step uses Cauchy-Schwarz and

    E[1/(B+1)]=(1-(1-t)^(M+1))/((M+1)t).

This argument allows arbitrary signs of d and independent fiber orientations. It never replaces a coherent signed spectrum by an incoherent mixture.

Set p=M+1, Z=(kappa+1)/p and G=-ln Z. Substituting t=1-exp(-a/p) gives

    E_nu exp(-a Z) <= min{1,r a^(-1/2)}, a>0,

because 1-exp(-s)>=s exp(-s). Frullani and 0<Z<=1 then imply

    E G = integral_0^infinity [E exp(-aZ)-exp(-a)] da/a
        <= integral_0^(r^2) (1-exp(-a)) da/a
           + integral_(r^2)^infinity (r a^(-1/2)-exp(-a)) da/a
         = 2 ln r+gamma+2.

The integral identity follows from integral_0^A(1-exp(-a))da/a - integral_A^infinity exp(-a)da/a = ln A+gamma. Nonnegative integration justifies averaging Frullani; all variables are finite here.

An alternative exact-density argument improves small r. Let h_k=sum_{j=1}^k 1/j. The harmonic integral yields

    E h_kappa >= sum_{q=1}^M (1-r c_q)/q,
    E G <= h_M-E h_kappa <= r sum_{q=1}^M c_q/q <= r(1+ln2).

The first inequality may have negative summands, which is harmless: it comes from the valid upper bound E(1-t)^kappa<=r E c_B. The beta integrals are binom(M,q) integral_0^1 t^(q-1)(1-t)^(M-q)dt=1/q. Pointwise ln((M+1)/(k+1))<=h_M-h_k proves the middle step. Finally c_(2j-1)=c_(2j)=b_j=4^(-j)binom(2j,j), and sum_j b_j/(2j-1)=1, sum_j b_j/(2j)=ln2. These follow by integrating the binomial generating functions: sum b_j z^j/(2j-1)=1-sqrt(1-z), and integral_0^1((1-z)^(-1/2)-1)dz/(2z)=ln2. M=0 gives G=0 directly. This proves E G<=L(r).

For d=d_i f and U=U_i, its normalized squared spectrum is the law of S minus i conditioned on i in S. Hence

    R_sigma(f)=sum_i Inf_i(f) E_(nu_i) ln(position(i)/(1+|T intersect U_i|))
                <=sum_i Inf_i(f) L(r_i).

Combining with Section 1 proves Statement 1. For fixed r, physical restrictions only intersect original pivotal supports with faces and remove fixed coordinates from the order; chain height and the allowed fiber-dependent orientations survive. Thus the restricted class is hereditary.

An explicit unbounded dimension family satisfying r<=2 is

    F(z,y)=g_a(y) when z=+1, and -g_b(y) when z=-1,
    g_t(y)=+1 iff the number of positive y_j is at least t,

with z first, then any data order, and 1<=a,b<=d. For a data derivative its support at each selector value is a Hamming level on the remaining prefix data. Each of the two selector layers is an antichain, so a chain has at most two pivotal assignments. For the first selector derivative the predecessor cube is empty. This covers growing, biased, signed examples, although it also overlaps existing regular-gate composition results. The 54 saved exact examples verify this physical hypothesis directly. No novelty is inferred from those examples.

### 3. Exact boundary: XOR of AND blocks

Let g_L=1-2*1_{x=x0} on L bits (a sign convention of AND or its negation) and f_(m,L)=prod_{b=1}^m g_L on disjoint blocks. Put p=2^(-L), q=2p. Its one-block squared spectrum is

    P(empty)=(1-2p)^2, P(S)=4p^2 for nonempty S,
    Inf_i=q, I(g_L)=Lq.

Tensor spectra imply H(f)=m H(g_L), I(f)=m Lq. For L>=2,

    H(g_L)=-(1-2p)^2 log2((1-2p)^2)
             +8p(1-p)(L-1).

Using -a ln a<=1-a=4p(1-p) gives

    H(g_L)/I(g_L)
       <= (1-p)[4(L-1)/L+2/(L ln2)] < 4.

The strict final comparison follows from 2/ln2<4. Thus this entire obstruction family itself satisfies FEI with constant 4.

Fix ANY order. Given that coordinate c at position u is in S, other coordinates in its own block are independently present with probability 1/2, and other blocks retain their unconditional law. If b preceding coordinates share its block, and N_u is the number of occupied positions at most u, then

    E[N_u | c in S]=1+b/2+q(u-1-b)
       <= (L+1)/2+q(u-1), for L>=2.

Convexity of -ln and N_u<=u yield

    R_sigma(f) >= q sum_(u=1)^(mL)
        max{0,ln u-ln((L+1)/2+q(u-1))}.

This is exactly the quantitative bound in B19-RANKCODE-GLOBAL-ORDER-NOGO v1. For fixed L, the summand tends to ln(1/q), so its Cesaro average gives

    liminf_(m->infinity) inf_sigma R_sigma(f)/(mLq)
         >= ln(1/q)=(L-1)ln2.

As a direct diagonal bound, E N_u<=L+q u. For u>=2^L L, this is at most 3*2^(-L)u. For m>2^L and L>=2,

    R_sigma(f)/I(f) >= (1-2^L/m)(L ln2-ln3).

Taking m=2^(2L) proves divergence uniformly over all orders, while H/I<4. This refutes only a universal estimate R_sigma<=K I with one global order. It does not refute FEI, adaptive references, normalized mixtures of orders with paid selection, or reference-KL credit. Sections 1 and 3 independently accept both lead v1 claims at their stated scope; the report supplies its own all-parameter reconstruction rather than relying on the lead's absent REPORT.md.

### 4. The exact KL credit and equivalence

Normalize the finite Euler weight on each level as in Statement 2. It is strictly positive on every k-set. Its surprisal is exactly

    -ln Q_(sigma,k)(S)=2 sum_j ln(i_j/j)+beta_(n,k).

The k-set consisting of the first k positions contributes 1/(k!)^2 to Z_(n,k), giving beta>=0. The Euler coefficient bound and factorial comparison from Section 1 give beta<=k ln(pi^2/4). Since cross-entropy equals entropy plus KL,

    H_nat(S | |S|)=2R_sigma+E beta-D_sigma.

The chain rule proves Statement 2's exact identity. In particular T_sigma<=H_nat(S) for every order. FEI(C) implies T_sigma<=C ln2 I. Conversely, if each f has an order with T_sigma<=K I, the level-entropy estimate and beta upper bound give H<= [A+K/ln2] I. There are finitely many orders at every n, so the infimum is a minimum. Taking suprema proves the stated two-sided comparison. K_T>=0 since every nonconstant character has H=T=0; no issue arises from negative T at some functions.

On the obstruction family, 2R_sigma/I diverges but the identity and H/I<4 force

    D_sigma >= 2R_sigma-4 ln2 I,
    T_sigma <= 4 ln2 I.

Thus discarding KL removes exactly the compensation needed on the cleanest product obstruction. Bounding T for arbitrary Boolean functions is still FEI-equivalent; using this identity alone is not progress on its universal value. What is new in this stage's extraction is the source-complete physical class criterion and the explicit retained-credit target, not a universal estimate.

First unsupported line for a universal extension: there exists an absolute K such that every Boolean f admits sigma with 2R_sigma(f)-D_sigma(f)<=K I(f). Neither the physical-height theorem nor tensor additivity proves this outside their stated hypotheses.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json, helper A095-rank-audit-v1. No search exceeds n=3 for arbitrary Boolean tables. Explicit selectors use 2..5 data bits, and explicit products use L=1..4, m=1..5 with L*m<=10. No symmetry quotient or automatic dimension increase was used. Integer FWHT and Fraction arithmetic check Parseval, direct/spectral influence, conditional prefix laws and relative-noise inequalities at t=1/4,1/2,1. Logarithms use rational atanh series with a proved remainder, 36 terms after reduction to [1,2). No floating entropy is accepted as proof.

Command from the A095 folder:

    python -X utf8 runs/20261011T231526Z-account05-A095-restricted-result-extraction/code/validate.py

First pilot: PASS, 20,449 exact assertions, 1.703 seconds. After freezing the added normalized-reference identity checks, the final bounded run: PASS, 27,177 assertions, 6.432 seconds; 1,572 all-table/order cases, 54 signed selector cases and 15 product parameter cases. Output is out/VALIDATION.json. Runtime is observational; all-dimensional proofs are in the preceding section. Rational interval overlap validates identities; the analytic algebra proves exact equality. The normalized finite-reference cross-entropy regression is tested instead of estimating e or pi numerically. Memory estimate 40 MB; no >300 MB job was started and no memok gate was needed. No long-lived job, GPU, external write, git command, or message to another agent was used.

## proof dependencies and changed downstream conclusions

The reduction depends on cube edge-isoperimetry, Gibbs' inequality and Euler's product. The pivotal-height theorem additionally uses Sperner and the elementary resampling Fourier identity. Its signed and fiber-dependent extension is fully proved above; it is not an appeal to a known unsigned mixture estimate. The KL equivalence depends on the normalized finite reference and the level-entropy estimate. It has no dependence on an unproved campaign target.

B19-RANKCODE-REDUCTION v1 and B19-RANKCODE-GLOBAL-ORDER-NOGO v1 are independently reconstructed at scope. New A095 class and KL statements remain author-proved pending independent review. Downstream B02/B03/B14 may use them conditionally with these statuses; B20 should retain the source pins and keep the universal residual open. No shared index was changed.

## one next mathematical action and independent reviewer

Next action: derive a normalized reference for two overlapping rank-local blocks, retaining its complete block-selection cost and KL credit, and compare its T/I with the product obstruction and an arbitrary terminal core. Begin with one identified shared physical coordinate; do not claim tensor additivity for the overlap. This tests the exact place where the product boundary requires a different code rather than extending the finite census.

Independent reviewer requested in saved artifacts: A090, alternate A085. Reconstruct the signed noise bound with fiber-dependent orientations and the normalized-reference identity; separately verify that the physical restriction heredity claim has the induced order. This is a handoff designation, not a tool-sent message or an assertion that review occurred.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/validate.py, out/FROZEN_SPEC.json, out/VALIDATION.json and rolling STATUS/WORKLOG/LEARNED are saved only inside A095. out/PERSISTENCE_RECEIPTS.json records SHA256 and byte size after schema validation. Source receipts identify the primary local texts. Local persistence is complete; supervisor copying, mirror verification, registry adoption and independent acceptance are unobserved and not claimed. All artifacts are under 20 MB.

## Universal bridge

This stage moves C020 (whole-set witness cost), the B19 lead's rank-code target: it independently pins the universal rank reduction and its order-independent Boolean product obstruction, closes a hereditary class under bounded (or influence-weighted logarithmic) pivotal chain height, and identifies the exact normalized KL credit that cancels the product rank debt. It gives no universal constant and leaves the rank-minus-KL payment FEI-equivalent. NEXT is the shortest identified route toward full FEI because a two-block overlap reference tests a mechanism that survives the already proved global-order failure while retaining all selection and terminal costs; another isolated regular-family theorem or a larger truth-table census would not address that obstruction.
