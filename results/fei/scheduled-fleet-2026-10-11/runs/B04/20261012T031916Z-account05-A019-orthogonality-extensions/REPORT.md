# A019 stage 2: one shared selector bit, exact collision and a good-node tree

Run 20261012T031916Z-account05-A019-orthogonality-extensions, B04/A019. Full FEI remains OPEN. This report continues the already reviewed translation mechanism under the stream lead's direction. It proves an arbitrary-activation transfer, extends it to unbounded star overlap through one shared physical selector, and gives a terminal-inclusive selector-first tree with zero localized bad-node boundary bill at threshold 3 for point modules. New extension review is pending; no literature priority claim is made.

## exact target, quantifiers, hypotheses and units

All cubes are uniform and physical; inputs are written in F_2, entropy uses bits, and influence of Boolean signs is edge disagreement. Dirichlet energy of a real derivative D is I(D)=sum_U |U| Dhat(U)^2, not a trinary edge-disagreement probability.

Let g:F_2^n->{-1,1} be arbitrary, x a fresh physical bit, and Z_1,...,Z_r mutually disjoint fresh private blocks, independent of the data y and x. For arbitrary Boolean activations A_j:Z_j->{0,1}, vectors v_j in F_2^n, and orientations s_j in {0,1}, set

F(x,z,y)=g(y+sum_j v_j 1{x=s_j} A_j(z_j)).

There is no bound on r, n, private block dimensions, or overlap/dependence between the vectors v_j. Define h_j=(-1)^A_j, m_j=E h_j, rho_j=Pr[g(y)!=g(y+v_j)], and p_T=ghat(T)^2. For each T let J_T={j:T dot v_j=1},

alpha_T=product_{j in J_T:s_j=0}m_j, beta_T=product_{j in J_T:s_j=1}m_j,
d_T=(1-alpha_T beta_T)/2,
I_priv=(1/2)sum_j rho_j I(h_j), I_x=sum_T p_T d_T.

Empty products equal one; zero p_T rows are omitted. The full selector block is W={x} union all private coordinates. Exact identities and bounds are

M_W=0, I_W=I_priv+I_x, I_data=I(g),
B_W=H(F)-H(g)=(1/2)sum_j rho_j H(h_j)+sum_T p_T kappa(alpha_T,beta_T),
B_W <= (1/2)sum_j rho_j H(h_j)+I_priv+(3/ln2)I_x,
B_x(F) <=3 I_x,
2 I(D_x F)=I_priv+2 sum_T p_T |T| d_T.

The kappa function is defined explicitly below. Applying the boundary lemma to Boolean selector phases, instead of to F as a whole, removes the final data-core term from the entropy-decrement upper bound. This is an exact removal of that term, not an assumption that g's entropy is already paid.

If H(h_j)<=C_act I(h_j) for all j, then

B_W<=max(C_act+1,3/ln2) I_W,
H(F)<=max(C_core,C_act+1,3/ln2) I(F)

provided separately that H(g)<=C_core I(g). For private point activations A_j=1{z_j=z_j*}, C_act=4 is the inherited module bound, so B_W<=5 I_W, irrespective of r and how small neighboring disagreement becomes.

For those point modules, query x first, then private selector bits, stopping at a translate of g. Every queried selector node satisfies exact B_i<=3 Inf_i, including all restrictions and zero-influence nodes. Thus the lead's localized boundary bill over selector nodes with B_i>3 Inf_i is exactly ZERO, without reusing any influence. Terminal entropy remains H(g) and terminal influence I(g). A majority core and arbitrary finite fresh nesting give unbounded terminal-certified examples. Constant 5 is a proved upper bound, not an optimality assertion.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-12 03:24 UTC, B04/STREAM_NOTES.md v2 (2026-10-11 23:25 UTC), own STATUS.md and prior stage REPORT.md mechanism. The lead independently re-derived A019 stage 1 plus 400 exact cases, verdict HOLDS. Its A019 direction is arbitrary Boolean activations on disjoint blocks, an overlapping-block test, then a two-level tree on majority-of-translations. This stage follows that direction and resumes the saved one-shared-selector calculation.

EXECUTION_PROTOCOL.json was re-read in full, revision 2026-10-11-execution-v2. Earlier campaign/paper/supplement sources remain as pinned in stage 1; none of their percolation or biased-threshold claims is a new dependency. Threshold 38-page Proposition 8.6 and Section 8's regular/threshold closure provide the baseline and majority terminal certificate. The stage-1 general module identity already covers arbitrary activations algebraically; stating its transfer is inherited, not a second discovery.

Read the B04 lead run 20261011T224500Z CLAIMS.json, especially B04-NODE-BOUNDARY@1, and A018 stage-2 run 20261012T010436Z REPORT.md in full through its proof/validation sections. A018 independently accepts the node-boundary statement and gives a complete proof from indicator entropy tensorization, even though the lead's cited REPORT.md was absent. This stage consumes that accepted local tool; it does not repeat the universal selector-log or bent-asymptotic census.

Read A016 stage-2 run 20261011T232501Z REPORT's tensor spectator discussion and exact family normalization. Its warning motivates the explicit extra data-core term derived here. Read A023 stage-2 run 20261012T010933Z scope/ownership sections: its activation is 1+A_shared(A_r OR A_t)(g-1), with terminal weighting and a bias hypothesis. Our construction instead translates g, preserving its entire squared spectrum at every selector leaf, uses XOR of arbitrary translated vectors, allows incompatible shared orientations, and requires no core bias hypothesis. A023 is a scope comparison, not a premise or duplicated theorem. No whole campaign board claim is accepted merely from a status line. Source receipts record exact byte hashes and read scope.

## complete derivation or exact first unsupported line

### 1. Inherited arbitrary-activation disjoint transfer

Without x, let F_0(z,y)=g(y+sum_j v_j A_j(z_j)) on disjoint Z_j. Translation gives the data coefficient row

c_T(z)=ghat(T) product_{j:T dot v_j=1} h_j(z_j).

Its squared magnitude is p_T at every z. Conditional selector Fourier spectra tensorize across disjoint private blocks. Consequently, exactly

B_W=sum_j rho_j H(h_j), M_W=0,
I_W=sum_j rho_j I(h_j), I_data=I(g).

Thus certified constants C_core and C_act transfer at max(C_core,C_act). The coefficient proof and empty-row conventions are already in A019 stage 1, section 1; arbitrary activation does not supply a certificate H(h_j)<=C_act I(h_j) automatically. Taking g a dictator, r=1 and unrestricted A_1 recovers arbitrary Boolean selector phases, so that missing certificate is full-FEI strength. This paragraph completes the lead's requested transfer statement without claiming a new general theorem about those phases.

### 2. One shared bit: exact phase coefficients and empty-sector correction

For the star-overlap F in the target, the row phase h_T is Boolean. Its x=0 child is

u_(0,T)=product_{j in J_T:s_j=0} h_j(z_j),

and its x=1 child is u_(1,T) with s_j=1. The two children depend on disjoint private coordinates. Their means are alpha_T,beta_T, their entropies sum to sum_(j in J_T) H(h_j), and their influences sum to sum_(j in J_T) I(h_j).

For a nonempty private frequency belonging to child b, the two parent x coefficients are +c_U/2 and +/-c_U/2. Frequencies from different children cannot collide except at the empty private frequency. There the two amplitudes are

a=(alpha+beta)/2, b=(alpha-beta)/2.

Let eta(t)=-t log2 t, with eta(0)=0, and write

kappa(alpha,beta)=2-alpha^2-beta^2+eta(a^2)+eta(b^2)
                         -(eta(alpha^2)+eta(beta^2))/2.

Then H(h_T)=(H(u_0)+H(u_1))/2+kappa(alpha,beta). The term 2-alpha^2-beta^2 comes from splitting the nonempty private masses into two parent atoms of one-quarter child mass. This identity uses the actual signed coefficients before squaring; it is not an incoherent mixture assertion. The exact parent spectrum is ghat(T) times the selector phase transform. Hence M_W=0, H(F)=H(g)+sum_T p_T H(h_T), and the target collision identity follows.

The conditional selector x influence is d_T=(1-alpha beta)/2, because the product of the child means is their correlation. Private influence sums at the parent are half the sums of the child's private influences. Averaging over T gives I_x and I_priv as stated; data influence remains I(g). This proves every influence normalizer directly in physical coordinates.

### 3. Boundary payment with the data-core term removed

B04-NODE-BOUNDARY@1, independently reconstructed by A018, says for any genuine Boolean h and split i,

Delta_i H(h)<=(3/ln2)Inf_i(h)+2 I((h_0-h_1)/2).

For the Boolean phase h_T above, the two children have disjoint private Fourier supports apart from the empty frequency. That frequency has zero weight in Dirichlet energy. Therefore

I((u_0-u_1)/2)=(I(u_0)+I(u_1))/4.

Apply the local lemma to h_T, then average with the fixed p_T. This gives

H(F)-average_x H(F_x)
<= (3/ln2)I_x+I_priv.

The branch-average entropy is H(g)+(1/2)sum_j rho_j H(h_j); adding gives the complete B_W bound. If each module certificate uses C_act, this becomes (C_act+1)I_priv+(3/ln2)I_x. Since I(F)=I(g)+I_priv+I_x, the full closure follows with the certified core constant.

For comparison, the actual derivative D_x F has coefficient energy

I(D_x F)=sum_T p_T[I(D_x h_T)+|T| d_T].

Thus the raw node-boundary charge on F includes the additional nonnegative 2sum_T p_T |T|d_T. Our conditional-row proof does not charge that term. It is allowed because h_T is genuinely Boolean in this translation class, unlike a general arbitrary coefficient row. For arbitrary shared-data branches, normalizing a row need not produce a Boolean phase, and this substitution cannot be assumed. The terminal H(g) has not been converted into a spendable influence bank.

For self-contained dependency reconstruction, the local lemma follows from Delta<=h2(d)+(2/ln2)d, h2(d)<=d log2(1/d)+d/ln2, and d log2(1/d)<=2I(D). The last inequality comes from entropy tensorization for the indicator of supp(D); on a boundary edge D has squared change at least that of the indicator. This is the accepted A018 proof, not a new boundary result.

### 4. Exact root erasure, including the initially missed term

Define Phi(A,B)=(A+B)h2(B/(A+B)), zero when A+B=0. The exact x erasure in a row is

b(alpha,beta)=1-(alpha^2+beta^2)/2+Phi((alpha+beta)^2/4,(alpha-beta)^2/4).

The first term is essential: all nonempty private frequencies carry an equiprobable x-frequency bit. The initial helper omitted this term and failed its exact identity assertion. A dictator core with one one-bit point activation gated by x already has B_x=1, whereas the incomplete formula returns 1/2. No published claim used that incomplete formula; out/PILOT_FAILURE.json and code/failed_star_v1.py preserve it. The proposed B_x<=2I_x was also false: alpha=1,beta=1/2 gives B_x=(5/8)h2(1/10)+3/8>2*(1/4). The repaired uniform bound is 3, proved next.

### 5. Scalar root bound b(alpha,beta)<=3(1-alpha beta)/2

This holds for all alpha,beta in [-1,1], not just dyadic means. Replacing beta by -beta interchanges the two empty-sector masses and leaves b invariant. It suffices to prove the bound for d=(1-|alpha beta|)/2 in [0,1/2]; the original d is at least this value. Put e=(alpha-beta)^2/4 after choosing same signs, q=(alpha^2+beta^2)/2=1-2d+2e. The identity

(1-alpha beta)^2-(alpha-beta)^2=(1-alpha^2)(1-beta^2)>=0

gives e<=d^2. At fixed d, b=2d-2e+Phi(q-e,e) is increasing in e, because its derivative is log2(q^2/[4e(q-e)])>=0 (extend zero endpoints by continuity). Thus

b<=2d(1-d)+Phi((1-d)^2,d^2).

Use the elementary binary bound h2(t)<=2sqrt(t(1-t)). For completeness, write t=(1+u)/2. The difference sqrt(1-u^2)-h2((1+u)/2) is zero at u=0,1; its derivative changes sign once, because R(u)=sqrt(1-u^2)atanh(u)/u decreases from 1 to 0. Indeed R'/R=[u/atanh(u)-1]/[u(1-u^2)]<0. Hence the difference is nonnegative. For d>=1/4 this yields b<=4d(1-d)<=3d.

For 0<d<=1/4, use Phi(A,e)<=e log2((A+e)/e)+e/ln2 and q<=1. The displayed upper bound divided by d is at most

U(d)=2(1-d)+d[2 log2(1/d)+1/ln2].

Its derivative is 2log2(1/d)-2-1/ln2>0 on this interval because ln2>1/2. Therefore U(d)<=U(1/4)=5/2+1/(4ln2)<3. The case d=0 has b=0. Averaging the scalar bound over p_T proves B_x(F)<=3I_x. No bound on core influence, bias or dimension was used.

### 6. Point-module hereditary singleton payment and the two-level tree

After fixing x, active modules have disjoint private blocks, and inactive modules are irrelevant. If A_j is a point indicator, any private restriction either kills that event, makes its translation fixed, or leaves a point indicator on fewer free coordinates. Earlier fixed translations preserve every p_T. Thus the disjoint phase identity applies at every such descendant, and each private node's B_i and Inf_i are the same rho-weighted scalar point-module quantities.

For a point sign h_m on m>=2 remaining coordinates, let delta=2^-m. On the queried coordinate's empty residual frequency the masses are (1-2delta)^2 and 4delta^2; on each other residual frequency they are both 4delta^2. Hence

B_i(h_m)=4delta-8delta^2+Phi((1-2delta)^2,4delta^2), Inf_i(h_m)=2delta.

Since the empty pair's total is at most 1,

B_i/Inf_i <=2+delta[4m-8+2/ln2]<3.

The last line uses ln2>1/2 and m-1<=2^(m-2), valid for all m>=2 by induction. For m=1 the point sign is a character and B_i=0. Killed or fixed events give zero. Tensor products of disjoint phases show that conditioning on other module Fourier labels leaves this same module law, so the weighted B_i<=3Inf_i transfers to the physical parent without a core charge.

Query the shared bit first, then the private selector coordinates; stop before querying any core coordinate. This is the lead's two-level organization: shared-bit split, followed by private-module subtrees, with each complete-module query also available as a block. Root B_x<=3I_x and every subsequent selector node has B_i<=3Inf_i. Consequently

sum_(selector nodes with B_i>3Inf_i) pi_v 2I(D_v)=0,
sum_selector pi_v Inf_i=I_W(F), E_leaf H=H(g), E_leaf I=I(g).

It is important that the zero statement uses exact B, not h2(Inf), and that it is restricted to the queried selector portion with certified terminal core required for full closure. The full entropy is independently paid at H(g)+5I_W by section 3. No descendant or terminal influence is spent twice.

### 7. Majority cores, low disagreement, and nesting

For odd n, take g(y)=sgn(sum_i(-1)^(y_i)). If a vector v flips t coordinates, the exact translation disagreement is

rho(v)=2^-n sum_(i=0..t,j=0..n-t) binom(t,i)binom(n-t,j)
                      1{|t-2i|>|n-t-2j|}.

The two compared sums are A+B and -A+B; odd n excludes ties, proving the formula. Therefore all star influences and exact entropy expressions can be computed with finite integer sums without enumerating all selector branches. Threshold Theorem A certifies H(g)<=C_reg I(g), C_reg<8.937 and >5, so the star extension preserves C_reg uniformly in n,r and widths. This uses a baseline certified leaf, not a new proof of majority FEI.

For any nonconstant core and v with rho(v)>0, one private point module of width k with the extra common x is just a point-triggered translation on k+1 controls. Its neighboring disagreement tends to zero, while the exact phase spectrum still applies. Multiple compatible and incompatible orientations share x, and the result holds for unbounded r; no lower disagreement bound is assumed.

Each finite fresh nesting level gives H(g_l)<=H(g_(l-1))+5[I(g_l)-I(g_(l-1))], so constants remain max(C_base,5). An input translation of a lower-level star changes point targets and shared orientations but preserves this allowed class. Consequently, for point modules the same outer-to-inner selector-first singleton tree has zero bad-selector bill at threshold 3 at every level, ending at the certified base core.

### 8. Exact first unsupported universal line

The derived star theorem is complete. The universal extension is unproved: for arbitrary Boolean F, there need not be a proper-selector block with common squared data spectra whose normalized rows are Boolean phases, nor a physical separator after which those phases have disjoint private supports. The exact row-wise removal of the data-core term fails at this unproved Boolean-phase admission line. Arbitrary activation phases also need their own FEI/hereditary certificate, and arbitrary g remains a full terminal obligation. The bent splice changes branch magnitudes and therefore still excludes a universal selector-only payment. We import that existing falsifier; its lower-bound computation is not repeated this stage.

## executed validation with domain, arithmetic, commands and outputs

The initial helper's missing root-erasure term failed an exact identity check and is retained with an explicit witness. Corrected helper A019-star-v2 has separately frozen pilot/full domains; the parameter domain is unchanged by the correction. The pilot uses two specified core masks, all module/vector/orientation cases and the majority fixtures, at most 60 seconds. The full bounded job uses all 16 two-bit Boolean cores, point private sizes (1,1),(1,2),(2,2), all 16 ordered vector pairs, both shared orientations; all 16 ordered one-bit arbitrary activation pairs with the same vectors/cores/orientations; plus odd-majority n=1,3,5 fixtures. Case count 9,764; no random sampling or growing n. The only symmetry reduction fixes s_1=0 by translating x.

Integer FWHT and Fraction probabilities reconstruct every full parent coefficient and each physical selector edge influence. Exact entropy identities use rational linear combinations of log2(prime). An independent conditional-phase computation checks the signed empty-sector collision formula, corrected root B, complete selector influence, and untouched data influence. The binary/ln2 estimates and B_W<=5I_W point cases use outward rational logarithms: 48-term atanh expansions reduced to [1,2), with positive geometric remainder and sign-aware interval arithmetic. Majority rho is checked against a separate combinatorial count. All-k scalar proof checks m=2,...,100 supplement, rather than supply, the all-dimensional analytic induction.

Commands from A019:

`python -X utf8 runs/20261012T031916Z-account05-A019-orthogonality-extensions/code/check_star.py --pilot`

`python -X utf8 runs/20261012T031916Z-account05-A019-orthogonality-extensions/code/check_star.py`

Pilot PASS: 1,252 cases, 86,731 exact assertions, 2.642 seconds. Full PASS: 9,764 cases, 608,203 exact assertions, 56.108 seconds. Independent selector-tree helper PASS: 4 majority fixtures, 204 internal nodes, 1,253 exact assertions, 0.519 seconds. out/TREE_SPEC.json froze this separate sub-60-second domain; code/check_tree.py reconstructs all descendants, exact entropy telescopes, point-module local rates, core translations at leaves and the raw boundary surplus. No other engine is imported. Its command is `python -X utf8 runs/20261012T031916Z-account05-A019-orthogonality-extensions/code/check_tree.py`. Planned memory 80 MB, not instrumented peak; no job expected above 300 MB, so memok preflight was not applicable. Full frozen timeout 300 seconds, checked at each case; no GPU, heavy search or background process. Rational certificate signs, not floating spectra, establish finite validation. The proof above supplies the unlimited r,n,width/depth bridge.

## proof dependencies and changed downstream conclusions

Dependencies: A019-RARE-TRANSLATION-COLLISION@1 for the inherited point-module H<=4I and disjoint identity, independently reconstructed by the B04 lead; B04-NODE-BOUNDARY@1 with independent acceptance in A018 stage 2; elementary finite Fourier/entropy identities. Majority closure alone uses threshold Theorem A as the certified terminal bound. New root-erasure and singleton bounds are proved self-contained here.

The general disjoint C_act transfer restates the stage-1 row identity. The new single bundled extension is unbounded star overlap, its exact kappa correction, conditional boundary payment removing the data-core term, and zero bad-selector stopping certificate for point modules. A018/A016 can substitute the row-wise boundary only after proving the same Boolean-phase/common-magnitude admission, not for the bent splice. A020 can test this narrower hypothesis. A027/A028/A064 receive a complete tree with terminal H and one-use influence explicitly retained. The shared-data universal gap is not marked closed.

## one next mathematical action and independent reviewer

Next: break exactly the Boolean-phase admission by letting one gate depend on one physical core coordinate, starting from a majority core and two point translation modules. Compute the actual common-frequency amplitude changes and the extra row normalization/posterior term, then ask whether a two-level selector/core query pays that correction with disjoint descendant reserves. This is the first coupling absent from the star proof and directly tests the lead's universal boundary bottleneck; adding further disjoint/star modules would repeat the solved mechanism. Independent reviewers requested: A090/A091; A018 can reconstruct the exact spectator correction and the repaired scalar root inequality. No external messages or other-agent edits occur.

## actual persistence receipts or precise save blocker

All four required protocol files, code/, out/, the exact overlap interface and failure record are local in the assigned run directory. STATUS.md stays two lines; WORKLOG.md is appended and LEARNED.md records both the corrected formulas and the failed erasure omission. Persistence receipts verify exact schema keys, statement hashes, identical PROGRESS/PACKET_DELTA, file hashes and size limits. Supervisor copying, independent extension acceptance and mirror verification remain pending. No shared report tree, other-agent folder, brain store, git, mail, trading or external publication was modified.

## Universal bridge

This stage moves the B04 lead's localized C019 boundary target: unbounded modules sharing one selector bit have complete collision payment at max(C_act+1,3/ln2), and point modules admit a physical selector-first tree with zero boundary charge at all nodes whose exact B exceeds 3Inf, while preserving the entire terminal core. The row proof also removes exactly 2sum_T p_T|T|d_T of inappropriate data-core derivative pricing. What remains is admitting Boolean conditional phases and paying the amplitude/normalization correction when selectors depend on the same coordinates as the core. The next one-core-coordinate coupling is the shortest route to test that missing universal step; another independent activation or additional star module would not move it.
