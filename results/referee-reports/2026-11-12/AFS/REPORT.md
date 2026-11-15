Verdict: SOUND WITH GAPS

The stated fixed-point sets, examples, pivot matrix, and spectral radii are correct. The odd-ray argument is correct, including its normalization and its reconstruction of the underlying tree. The reduction to two states is valid. I found no counterexample to the assertion that every point of the nontrivial simplex is rogue, even without an offspring moment assumption.

The qualification in the verdict concerns the presentation of the new argument at PAPER.tex:142–148. Its essential finite-exploration branching property is asserted without a precise definition of the filtration or a proof that selecting the spine preserves that property. This is a repairable proof gap, not a false theorem. A complete repair is supplied below. The criticism of the cited JPS proof is justified: the cited arXiv source really does apply an off-spine conditional-law statement to a spine vertex, conditional on the entire spine. The repair must preserve the distinction between the finite exploration used for spine estimates and the whole-spine conditioning used for off-spine martingales.

There are no wrong JPS section, theorem, proposition, or lemma numbers among the citations requested in the brief. The Rozikov–Zada attribution and parameter substitution are correct for the fixed-point assertion actually used. Minor issues below concern precision, exceptional indices, and omitted justifications. They should not be promoted into counterexamples to the main result.

Scope: I read PAPER.tex and references.bib, all of JPS Section 4, its required definitions and results from Sections 1–2 and 6, and the relevant Rozikov–Zada definitions, theorem, and equations. All source references below are to the supplied TeX files. No browsing, external writes, git operations, agents, or visible windows were used. The shared checklist/mesh/recall commands were not run because they write outside this folder, contrary to the specific instructions for this audit. Programs and outputs are saved here.

## Line-numbered findings and corrected text

### F1 — gap — PAPER.tex:142–148: specify and prove the new exploration property

The proposed repair is mathematically valid, but “information revealed by exploring the spine” is not a definition of a sigma-field. In particular, specify the original four-state labels, the selected vertex V_i, and the auxiliary choices that select the spine. Merely enlarging JPS's sigma-fields does not preserve a conditional-law assertion automatically. The statement that Lemma 4.12 “goes through” needs the branching/selection argument below. This is the load-bearing new step in the removal of the moment assumption.

JPS Proposition 4.1(c), source lines 1619–1691, proves that the original tree with labels 0d, 0s, 1d, 1s is multitype Galton–Watson. Proposition 4.9(d), lines 2048–2050 and 2071–2077, gives the corresponding law of a spine subtree conditional on the **finite** spine sigma-field G_n. Neither statement, as stated, is a conditional-law theorem for the newly introduced H_i. It follows from Proposition 4.1(c) and the manner of selecting the next child, but that implication should be proved.

Replace the filtration portion of line 142 by the following, with the notation of JPS retained:

> Work with the original, unswitched four-type tree under RST^{0s}. Choose the next spine vertex uniformly among the pivotal s-labeled children, using fresh independent uniform random variables U_0, U_1, … . Let H_0 record the root label and position. At step i reveal the complete ordered list of children of V_i and their original four-type labels, then U_i and the selected child V_{i+1}. Let H_{i+1} be the information revealed through this step. No descendants of an unexpanded child are revealed. Conditional on H_i, the unswitched labeled subtree rooted at V_i has law RST^{ell_i}, where ell_i is its original label, in {0s,1s}. Indeed, the multitype branching property of JPS Proposition 4.1(c) makes the child subtrees independent conditional on their labels, and selection using only these labels and the independent U_i reveals no further information about the selected subtree. Induction proves this assertion for every i.
>
> By the identity W_i = 1/N(V_i,T^{0s},omega_*^{0s}), proved at the start of JPS Lemma 4.12, the product A_i = W_0 … W_{i-1} is H_i-measurable. The same two-step argument as in that lemma, now using the preceding conditional branching property, gives E[W_i W_{i+1} | H_i] <= c < 1. Consequently E A_i <= c^{floor(i/2)}. Also E[deg(V_i) | H_i] <= L.

The tower-property calculation at lines 144–146 then follows by Tonelli, and proves that the series is finite almost surely. The fact that W_{i-1} is measurable before expanding V_i is essential; the displayed identity for W_i explains it.

Add the following bridge after line 148:

> Retain JPS's whole-spine sigma-field G for the off-spine subtrees in Proposition 4.9(b,c) and Lemma 4.11. Only the spine estimate has been changed. The series just proved finite is exactly the hypothesis supplied by Lemma 4.14 to the conditional submartingale argument in Lemma 4.15. Thus Lemma 4.15 and then Lemmas 4.5 and 4.3 give RST^{0s->1s} << RST^{1s}. The final argument of JPS Section 4 contradicts an interpretation, since switching the spine leaves the underlying tree unchanged and reverses its root colour.

This supplies the missing justification without making any stronger conditional-law assertion about a spine subtree given G.

There is also a shorter way to verify the contraction specifically for B. Every b vertex has a unique b child, which is pivotal; following these children proves survival from b with probability one. An a vertex with exactly two b children has two surviving pivotal children and occurs with positive probability, so survival from a also has positive probability. Conditional on 0s, the event of two b children has positive probability. Conditional on 1s, an a sibling with a surviving pivot tree occurs with positive probability. Thus for both surviving types, the original number R of surviving pivotal children is at least one and exceeds one with positive probability. Hence max_ell E[R^{-1} | ell] < 1. With the explicitly defined H_i this gives even the one-step bound E[W_i | H_i] <= c < 1. This provides a separate check of the proposed repair, independent of the difficult case in JPS Lemma 4.12.

### F2 — imprecision — PAPER.tex:129: make the passage to a tail event explicit

The conclusion is correct. Equality almost surely to an event in each decreasing sigma-field must be handled modulo null sets; it is not literal membership of the original event in every uncompleted sigma-field. There is no extra probabilistic assumption needed.

Replace the last tail-field transition by:

> For each r choose the tail-measurable reconstruction of T_r from (xi_r,xi_{r+1},…). Let E_r be the event that its interpretation is b_i. All E_r agree almost surely under P(. | T in O), after intersecting countably many probability-one events. The event E = liminf_{r->infinity} E_r belongs to every sigma(xi_j : j >= h), and agrees almost surely with {iota(T)=b_i}. Kolmogorov's zero-one law therefore gives P(iota(T)=b_i | T in O) in {0,1}.

This is a precision repair, not a failure of the odd-ray proof.

### F3 — imprecision — PAPER.tex:137–140: handle degree zero before using the polynomial bound

The two displayed conditional probability bounds are correct. Their first right-hand side is positive at n=0 when chi(0)>0, whereas C n^2 s^{n-2} is zero there. Thus the proposed polynomial bound does not follow by bounding that displayed numerator at n=0. The actual conditional probabilities at n=0 are zero: a surviving pivot tree has a child. For n>=1 the claimed bounds hold.

Replace the transition at line 140 by:

> For n >= 1 both conditional probabilities are bounded by C n^2 s^{n-2}, since chi(n) <= 1. Both vanish at n=0 because a root with a surviving pivot tree cannot be a leaf. Hence the two conditional root degrees have finite exponential moments for every exponent alpha with e^alpha s < 1, and in particular have all polynomial moments.

The original conclusion “all moments” is correct. It does not assert existence of exponential moments at every positive exponent.

### F4 — imprecision — PAPER.tex:164: write the logarithmic-moment extension as an actual bound

The parenthetical Borel–Cantelli argument is valid, and requires no independence of the degrees along the spine. Its justification should be recorded because it is a further generalization of the theorem, rather than a direct application of the finite-mean calculation at lines 144–146.

Replace the parenthetical by:

> To see this with only logarithmic moments, write A_i = W_0 … W_{i-1}. The estimate E A_i <= c^{floor(i/2)} implies by Markov's inequality and Borel–Cantelli that A_i <= b^i eventually almost surely for any sqrt(c) < b < 1. For epsilon > 0, the finite-exploration property gives
> P(deg V_i > e^{epsilon i}) <= P(D_{0s} > e^{epsilon i}) + P(D_{1s} > e^{epsilon i}).
> Finite E log(1+D_{ell}) makes the sum of these bounds over i finite. Choose epsilon so that b e^epsilon < 1. Then deg V_i <= e^{epsilon i} eventually almost surely, and sum_i A_i deg V_i is finite. This proves the needed series estimate without independence of the degrees.

The other hypotheses, including two states, full support, and the standing offspring assumption, must remain as stated. This does not establish the general multistate analogue of JPS's criterion.

### F5 — citation — PAPER.tex:142: identify the exact defect in the source

The criticism is correct, but “the end of the proof in JPS” is unnecessarily vague.

Replace that clause by:

> In the proof of Lemma 4.14 in the cited arXiv version, Proposition 4.9(c) is invoked for the spine vertex V_i conditional on the whole-spine sigma-field G. Proposition 4.9(c) concerns the off-spine vertices V_{i,j}; it does not give the asserted conditional law at V_i. We instead use a finite exploration of the original labeled spine.

The erroneous invocation is at JPS source lines 2300–2313, especially 2300–2302. Proposition 4.9(c) is at 2045–2047. The appropriate finite-spine statement is part (d), at 2048–2050. The presence of the defect does not make the theorem of JPS false: the finite-exploration argument repairs the use needed here and also repairs their logarithmic-moment estimate.

No other mathematical error or misattribution was established. The clarifications in the remaining sections are verification details, not additional allegations of defects.

## Claim-by-claim verification

### 1. Fixed points, including infinite mean and leaves

For s<1 and n>=1, a b_i root requires exactly one b_i child and n-1 a children. Its probability conditional on N=n is n x(b_i) s^{n-1}. The n=0 case is handled separately. Therefore

    Psi(x)(b_i) = x(b_i) G'(s),
    Psi(x)(a)   = 1 - (1-s) G'(s).

For s=0 the n=1 term uses s^0=1; higher degrees contribute zero. At s=1 the root is deterministically a. In particular one must not use 0 times G'(1) when the mean is infinite. The paper correctly restricts its displayed derivative formula to s<1 and treats delta_a separately at lines 105–107.

Positive offspring mass at some n>=2 implies chi(1)<1 and G' is strictly increasing on [0,1). Its value at zero is chi(1); its limit at one is m by monotone convergence. Thus when m>1, even m=infinity, there is exactly one root s_* in (0,1) of G'(s)=1. When m<=1 there is none below one. There are no additional boundary fixed points with s=0. Leaves cause no difficulty. The dimension and the description of relative interior/full support are correct.

### 2. Examples

The unary/binary mixture gives G'(s)=r+2(1-r)s and s_*=1/2 for every 0<=r<1. The excluded r=1 is essential: pure unary branching would give the identity on the entire state simplex and violates the standing assumption.

For Poisson(lambda), G'(s)=lambda exp(lambda(s-1)); s_*=1-log(lambda)/lambda, for lambda>1. The binary k=2 map at lines 110–114 is correct; its fixed points are (1,0,0) and the entire stated closed segment, with no additional points.

### 3. Rozikov–Zada and the JPS question

Rozikov–Zada source lines 664–671 give equation (17) and the admissible parameters. The choice a=b=0,c=1 is allowed, and satisfies a=2b and c>1/2. Theorem 2(iv), lines 702–705, gives the fixed segment

    x+y = (2c-1)/(2(c-b)) = 1/2.

Equation (21), lines 838–845, specializes to x'=2xz, y'=2yz, and z'=1-2(x+y)+2(x+y)^2. On x+y+z=1 its third coordinate equals z^2+(x+y)^2. The homogeneous quadratic heredity coefficients are indeed zero or one: pairs (x,z) and (y,z) produce x and y, respectively; all other unordered pairs produce z. Relabel z=a,x=b_1,y=b_2. This is precisely A_2 under binary branching. The source also has the isolated fixed point (x,y,z)=(0,0,1); the paper says “fixed segment,” not “entire fixed set,” and includes the isolated point in its own theorem.

There are errors in the source that the paper does **not** import. In the proof of Theorem 2(iv), RZ line 821 reverses the denominator sign relative to its correct theorem statement. Also the global convergence clause of that theorem fails at this boundary parameter for initial x+y=1: such a point maps to (0,0,1) in one step. Neither fact invalidates the fixed-point statement cited here. Attribution should continue to be restricted to that statement.

JPS Section 6, lines 2907–2914, asks whether there can be infinitely many fixed points for 3<=|Sigma|<infinity and says that analyticity rules this out for two states. PAPER.tex:56 reports that question and remark accurately. Its counterexample in Remark two correctly shows that the unrestricted two-state remark is false, even under the logarithmic-moment hypothesis of JPS Theorem 1.7. JPS's remark is a further-questions observation, not a proved extra hypothesis of Theorem 1.7. The paper does not misquote it as a theorem.

The statement at PAPER.tex:58 that JPS treats general offspring laws and that most of its examples are Poisson is supported by JPS's general setup and its Section 5 examples, including source lines 2543–2549, 2637–2642, 2716–2720, and 2776–2777.

### 4. Binary proposition and odd-ray theorem: line-by-line audit

The binary proposition at lines 116–118 is correct. Under delta_2 the ordered rooted tree is a single deterministic tree and each descendant subtree is the same rooted ordered tree. An interpretation is a function of this tree, without auxiliary vertex labels or randomness. It must assign the same c to every vertex. Only c=a satisfies g(c,c)=c. JPS Section 1.4, source lines 401–406, is exactly the definition needed. There is no nonconstant measurable interpretation hidden by the ordering.

| PAPER.tex step | Assessment and exact comparison |
| --- | --- |
| 121: the law of iota(T) is fixed | Correct. JPS Lemma 1.4 in Section 1.5, source lines 415–423, states and proves exactly this. The paper's Theorem main then gives s=s_* unless the law is delta_a. |
| 121: compatibility at every vertex almost surely | Correct. This is part of JPS's interpretation definition, source lines 401–406, not just compatibility at a typical root. Equivalently, countability of vertex addresses permits a common full-measure event. |
| 121: an odd vertex has a unique odd child with the same b_i | Correct directly from A_k. This is a new automaton-specific fact, not a claim supplied by JPS. It also proves that an odd tree has an infinite ray on the compatibility event. |
| 123: define theta and xi | Correct almost surely. The sets of odd/even trees are Borel because iota is measurable. Child-subtree extraction and the unique odd-child index are measurable on the root-compatible odd set. The decoration space is the countable disjoint union over n,j of spaces of ordered (n-1)-tuples of even trees. Define the maps arbitrarily on the null exceptional set. This uses JPS's tree space and Borel structure, source lines 339–353, and its interpretation definition. |
| 125: factorization | Correct, with no missing factor of 1-s. For fixed n,j, put the jth child in B intersect O, and each sibling in O^c. Independence of GW child subtrees factors off P(T in B intersect O); summing the sibling contributions produces nu(C). Root compatibility makes this event equivalent, modulo a null set, to the event on the left. The branching independence is the same fact used in JPS Lemma 1.4, line 423. |
| 127: nu is a probability measure | Correct. It is a countable sum of positive finite measures and its total mass is sum_n chi(n)n s^{n-1}=G'(s)=1. For n=0 the inner sum is empty. No moment at s=1 is used. |
| 127: conditional independence | Correct. Dividing by P(O)=1-s gives P(theta T in B,xi in C | O)=P(T in B | O) nu(C). This proves the claimed distributional regeneration. It is a new argument, not an invocation of JPS's pivotal spine. |
| 129: iteration | Correct. Apply the preceding kernel identity repeatedly to Borel functions of the remaining odd subtree. This proves finite-dimensional independence of the xi_r and their common distribution nu. It also proves independence of the first r decorations from T_r. |
| 129: reconstruction and measurability of T_r | Correct. Each decoration includes complete even sibling trees, the total degree, and the position of the next ray vertex. The next h decorations determine the first h generations. These finite truncations generate the tree's Borel sigma-field (JPS lines 340–353). No extra “terminal tree at infinity” remains to be specified. |
| 129: invariance of iota along the ray | Correct on one probability-one event for all r, by compatibility and the unique-child rule. |
| 129: tail zero-one conclusion | Correct with the explicit null-set argument in F2. The independent sequence is considered under the conditional probability P(. | O). Each odd colour has conditional probability zero or one; finitely many such colours partition O, so exactly one has probability one. |

Thus Theorem interp really excludes every nonvertex point of the simplex without any moment assumption. It does not by itself exclude the vertices. That exclusion is the role of Theorem only.

### 5. Theorem only: line-by-line comparison with JPS

| PAPER.tex step | Assessment and exact comparison |
| --- | --- |
| 133: merge all b_i into b | Correct. If q is the merge, q(A_k(children)) = B(q(children)) for every finite child configuration, including leaves and unary vertices. Therefore q composed with an interpretation is measurable and compatible at all vertices on the same full-measure event. This is the homomorphism calculation required by the definition in JPS Section 1.4. It is stronger than merely observing that the root distribution merges correctly. |
| 133: merged fixed point | Correct: the merged law is (s_*,1-s_*). Both entries are strictly positive. JPS assumes full support immediately before Theorem 1.7, source lines 528–532. Boundary points of the original larger simplex are therefore no obstacle. |
| 133: applicability of Theorem 1.7 with a log moment | Correct. JPS lines 538–542 state: for two states and finite logarithmic offspring moment, a full-support fixed point is interpretable iff its pivot tree is subcritical or critical. The standing chi({2,3,…})>0 is at lines 347–348. All hypotheses other than the moment condition hold here; one cannot directly cite the theorem to dispense with that condition. The paper instead adapts its proof. |
| 135: where the moment enters | Correct. I read Section 4, source lines 1557–2420, in full. Lemma 4.13 is the logarithmic-tail summability lemma. Lemma 4.14 uses it to control the number of offspring along the spine after proving exponential decay of weight products. Lemma 4.15 inherits the assumption through Lemma 4.14. There is no earlier hidden use of the offspring logarithmic moment in this direction of the proof. In particular, the finite-level likelihood comparison in Lemma 4.5 and the two-step contraction in Lemma 4.12 do not use it. |
| 135: meanings of 0s,1s | Correct. JPS lines 1603–1614 define the survival label using the pivot tree of the descendant subtree. A surviving pivot tree starts an infinite pivotal path because the tree is locally finite. |
| 135: root b probability | Correct: P(N=n,root b)=chi(n)n p s^{n-1}. This follows from JPS's random-state-tree definition, lines 441–451, or its offspring law in Proposition 2.1, lines 718–729. |
| 135–138: root 0s probability bound | Correct. An a root with a surviving pivot tree has at least one pivotal child. Under B it can therefore have zero or exactly two b children. The bound includes configurations whose pivot tree dies, which is harmless for an upper bound. |
| 135: positive denominators | Correct under supercriticality by JPS Proposition 2.6(c), source lines 1175–1176 and 1216–1236. Supercriticality is verified later; this is a conditional argument followed by its hypothesis check, not circular reasoning. For this B, positivity can also be proved directly using the immortal b ray and the event of two b children. |
| 140: exponential tails and finite L | Correct after the n=0 clarification in F3. Since 0<s<1, sum_{n>=1} n^{r+2}s^{n-2}<infinity for every finite r. This works even for offspring laws having infinite mean and infinite logarithmic moment. |
| 142: criticism of JPS | Correct; see F5 and the countercheck below. The source invokes part (c) for V_i, although part (c) is expressly about V_{i,j}. The whole spine contains information about descendants of V_i. |
| 142: new H_i and contraction | Correct once the filtration and its conditional branching property are supplied as in F1. The relevant source statements are Proposition 4.1(c), Proposition 4.9(d), and Lemma 4.12, source lines 2143–2240. Changing the sigma-field requires an argument; a citation alone would not justify it. |
| 144–146: expectation bound | Correct. A_i is nonnegative and H_i-measurable, E[deg V_i | H_i]<=L, and N in the switched tree is at most the actual degree. Tonelli and the tower property give E sum_i A_i N_i <= L sum_i c^{floor(i/2)}<infinity. |
| 148: almost sure series finiteness | Correct. A nonnegative extended random variable with finite expectation is finite almost surely. This supplies precisely the conclusion of JPS Lemma 4.14. |
| 148: rest of JPS proof | Valid with the bridge in F1. Lemma 4.11 gives conditional mean-one off-spine likelihood-ratio martingales. Lemma 4.15 uses their conditional submartingale sum and the finite spine series to bound limsup f_n. Lemma 4.5 transfers this to the likelihood ratios r_n. Lemma 4.3 gives absolute continuity, and the last proof of Section 4, lines 2385–2405, contradicts root measurability for an interpretation. No remaining offspring moment enters these steps. |
| 150–154: verify supercriticality | Correct; the independent matrix calculation appears below. |

The proof uses the supercritical-to-rogue direction only. It does not need a new proof of the critical or subcritical directions of JPS Theorem 1.7.

For completeness, two typographical defects in the source do not obstruct this adaptation. JPS's proof of Lemma 4.13 at line 2266 uses X_n <= (2c)^{-n} eventually, which is not true for arbitrary c in (0,1). The valid argument is X_n <= e^{epsilon n} eventually, with c e^epsilon<1. Also JPS's displayed expectation bound for Y_n at line 2367 drops its fixed factor C from the definition at line 2338. Restore that factor; finiteness is unchanged. The present paper's finite-L argument does not use the faulty constant in the proof of Lemma 4.13.

### 6. Pivot children, mean matrix, and JPS's definition of supercritical

The children described in PAPER.tex:150 are pivotal **relative to a pivotal parent**, or equivalently relative to the root of the parent's subtree. For two states, local pivotality then propagates to the original root. A nonpivotal vertex does not contribute children to the original pivot tree; the paragraph is correctly read in the pivot-tree context.

Under B:

* A b parent has exactly one b child. Flipping any child changes the count to zero or two, so every child is pivotal.
* An a parent with no b children has all children pivotal, all of type a.
* An a parent with two b children has precisely those two children pivotal.
* An a parent with at least three b children has no pivotal children.

The a parent cannot have exactly one b child. For a leaf the first case for a gives zero pivotal children.

Divide unconditioned pivotal-child counts by the parent probabilities p and s. In order (b,a),

    M_bb = sum chi(n)n p s^{n-1}/p = 1,
    M_ba = sum chi(n)n p s^{n-1}(n-1)/p = s G''(s),
    M_ab = sum chi(n)n(n-1)p^2 s^{n-2}/s = p^2 G''(s)/s,
    M_aa = sum chi(n)n s^n/s = 1.

The characteristic polynomial is (t-1)^2-p^2 G''(s)^2. Thus rho(M)=1+pG''(s)>1; the other eigenvalue is 1-pG''(s), whose absolute value is smaller. G''(s) is finite at s<1 and positive because s>0 and chi gives positive mass to some n>=2. The matrix is strictly positive, hence positive regular, and cannot be singular because its spectral radius exceeds one. There is no need to infer survival from an arbitrary reducible multitype process.

JPS defines supercriticality by the spectral radius of this mean-offspring matrix at source lines 535–537 and 1043–1053. Proposition 2.4, lines 961–965, gives the multitype Galton–Watson property with augmented types. The paragraph immediately following its proof, lines 1025–1030, explicitly reduces these types to colours alone in the two-state pivot tree. The citation is correct.

For Poisson(lambda), G''(s_*)=lambda, p=log(lambda)/lambda, hence rho=1+log(lambda). This is the pivot-tree spectral radius, not necessarily the absolute derivative of the one-dimensional automaton map. Those quantities must not be confused; the paper does not confuse them.

### 7. Two-state example, moments, analyticity, and the general remark

The law chi(n)=1/[n(n-1)] for n>=2 is normalized by telescoping. Its mean is sum_{n>=2}1/(n-1)=infinity. Its logarithmic moment is finite because log(1+n)/[n(n-1)] is summable by comparison with 2 log(2n)/n^2.

For the “at most one zero” automaton, for every p in [0,1],

    Psi_K(p) = sum_{n=2}^K [p^n+n(1-p)p^{n-1}]/[n(n-1)]
             = p-p^K/K.

The remainder tends to zero even at p=1. Therefore Psi(p)=p on the entire closed interval, not merely in its interior. This proves the claimed counterexample to the blanket two-state remark.

If G is entire, the scalar map for any deterministic two-state automaton is entire as well. To justify the step at line 162, write its degree-n contribution as a Bernstein polynomial P_n(z) with coefficients in {0,1}; then

    |P_n(z)| <= (|z|+|1-z|)^n.

On every compact set the right side is at most R^n for some finite R, and sum chi(n)R^n=G(R)<infinity. Thus the series converges normally and defines an entire function. A leaf's deterministic output and chi(0)>0 imply either Psi(1)<1 or Psi(0)>0. Hence Psi-id is a nonzero analytic function on a neighborhood of [0,1], and has only finitely many zeros there. Compactness plus the identity theorem rules out accumulation at the endpoints too. The necessity of at least three states for infinitely many fixed points in this setting is correct. Under the paper's supercritical assumption A_2 supplies sufficiency. The leaf condition matters: entire G alone does not prevent identity maps.

The general logarithmic-moment remark is justified by F4 and the same JPS proof bridge. Conditional degree distributions may change with the spine type; no assertion that they are independent or identically distributed is required.

### 8. Abstract, introduction, and scope of claims

All mathematical sentences of the abstract agree with the established conclusions after F1 is made explicit:

* The JPS question is accurately stated.
* The three-state binary fixed segment is implicit in RZ, with the exact attribution checked above.
* A_k works for each supercritical offspring law, including Poisson laws, laws with leaves, and infinite-mean laws.
* The fixed set is the isolated delta_a plus the claimed simplex, for every k>=2.
* Every point of that simplex, including its vertices, is rogue by Theorem only. The odd-ray theorem alone proves this for its nonvertices.
* No offspring moment assumption beyond the stated extended mean m>1 is required by the repaired argument.

The same conclusions cover PAPER.tex:58 and 96. The title accurately describes the result. “No moment assumption” does not mean offspring may be infinite at a vertex: chi remains a probability law on N_0, so the trees are locally finite. That restriction is already in the paper.

The AB, HM, and GMR contextual sentences, funding, contribution history, and public repository availability cannot all be independently authenticated from the two supplied research sources. They are not consequences of the theorems proved here. I found no local evidence contradicting them and did not browse to verify them. In particular this audit does not authenticate the contribution and model-version declarations at lines 7 and 170–179.

## Citation and bibliography audit

The numbering was reconstructed from the actual TeX counters, including the shared counters for definitions and remarks; it was not inferred from where an item appeared on a page. See audit_citations.py and audit_citations.out.

| Citation in PAPER.tex | Local source location | Result |
| --- | --- | --- |
| Section 1.2 | JPS 339–362, Notation | Correct standing offspring assumption and tree space. |
| Section 1.4 | JPS 397–406, Interpretations | Correct definition. |
| Section 1.5 | JPS 408–439 | Correct distributional map, interpretation law, and rogue terminology. The particular fixed-law assertion is Lemma 1.4. |
| Section 1.6 | JPS 441–470 | Correct random-state-tree definition. |
| Theorem 1.7 | JPS 538–542, with 528–537 | Correct two-state criterion, full-support qualification, and log-moment assumption. |
| Proposition 2.4 | JPS 961–999, plus 1025–1030 | Correct pivot-tree branching property and two-colour specialization. |
| Proposition 2.6(c) | JPS 1175–1176, proof 1216–1236 | Correct positive survival probability from both colours. |
| Section 4 | JPS 1557–2420 | Correct location of the supercritical proof. |
| Proposition 4.9(c) | JPS 2045–2047 | Off-spine conditional law only. The paper's criticism of the invocation at 2300–2302 is accurate. |
| Lemma 4.12 | JPS 2143–2240 | Conditional two-step contraction. |
| Lemma 4.13 | JPS 2256–2267 | Logarithmic-moment summability; its statement is correct despite the proof's constant typo. |
| Lemma 4.14 | JPS 2270–2321 | Almost sure finiteness of the exact series replaced in the manuscript. |
| Lemma 4.15 | JPS 2327–2382 | Bounded limsup of f_n from the spine-series estimate and off-spine martingales. |
| Section 6 | JPS 2885–2921, especially 2907–2914 | Exact question and two-state remark. |
| RZ Theorem 2(iv) | RZ 702–714 | Correct fixed segment at the cited parameters. Its stronger convergence assertion is not used. |
| RZ equation (21) | RZ 838–845 | Correct operator, after imposing x+y+z=1. |

Bibliographic facts supported by the available files:

* references.bib:2–3: all three JPS author names and the title match JPS source lines 93–108 exactly.
* references.bib:11–12: the RZ author initials/surnames and title match RZ source lines 58–60. The local source prints initials only, so it does not independently establish the expanded given names.
* references.bib:40–45: AB authors, title, journal, volume, year, and pages agree with sources/jps/pivot_trees.bbl:10–13. That bibliography additionally gives issue 2; its omission here is harmless.
* The supplied JPS TeX has no embedded arXiv version identifier. All cited numbering agrees with this local source. The statement that it is v2 is provenance supplied by the task/bibliography, not something independently certified by the TeX. The RZ source likewise does not independently certify an arXiv version suffix.
* The published JPS and RZ journal years, volumes, pages, and DOIs, the AB DOI, and the HM/GMR metadata are not all independently checkable from these files. No corrections to them are justified on the available evidence. The JPS .bbl does not contain the HM article. Absence from an older bibliography is not evidence of a wrong citation.

For clarity only, references.bib:8 could read “All numbering refers to arXiv:1808.03019v2,” since the manuscript cites theorem and proposition numbers as well as sections. The existing wording is not a wrong citation. No bibliographic author/title mismatch was established.

## Programs, outputs, and independent checks

Programs saved and run:

1. audit_verify.py — exact Fraction enumeration, symbolic SymPy identities, deterministic series summation, pivot counts, merging, moment estimates, and explicit finite/full-spine conditioning checks. Full output: audit_verify.out.
2. audit_citations.py — parses the local JPS shared theorem counters and subsections and lists every JPS/RZ citation in PAPER.tex. Full output: audit_citations.out.

Commands, run sequentially in this folder:

    python3 audit_verify.py > audit_verify.out
    python3 audit_citations.py > audit_citations.out

Both completed with exit status zero. The mathematical verification program's final run used about 56.44 MiB peak RSS and 0.074 seconds after imports; total process time was about 0.33 seconds. Both programs have alarms well below five minutes. Numerical libraries were limited to one thread; no workers were created. An initial priority-setting call failed because raising niceness relatively on this already-low-priority process was disallowed; it was replaced by a check of the existing absolute priority. An initial spine check used an incorrect hand-computed survival constant in the audit program; it was corrected from the enumerated equation r=(1/2)(1-(1-r)^2)+1/8 to r=1/2 before the final successful run. Neither issue was a finding about the manuscript.

Principal outputs:

    30 exact maps PASS (k=2,3; s=0,1 included)
    511 binary configurations through degree 8 PASS
    9841 three-state merges PASS
    binary: s=1/2, M=[[1,1],[1,1]], rho=2
    unary_binary: s=1/2, M=[[1,3/5],[3/5,1]], rho=8/5
    leaf_supercritical: s=2/3, M=[[1,1],[1/4,1]], rho=3/2
    RZ substitution; fixed segment; r-mixture; Poisson; characteristic polynomial: PASS

| Offspring law | Computed s_* | Computed pivot rho | Largest map summation error |
| --- | ---: | ---: | ---: |
| (1/4)delta_0+(1/4)delta_1+(1/2)delta_3 | 0.707106781187 | 1.621320343560 | 1.11e-16 |
| Poisson(2) | 0.653426409720 | 1.693147180560 | 2.78e-17 |
| chi(n)=1/[n(n-1)], n>=2 | 0.632120558829 | 2.000000000000 | 1.39e-17 |
| (1/4)delta_0+(3/4)chi_heavy | 0.736402861884 | 1.750000000000 | 2.78e-17 |
| P(N=2^(2^j))=1/[j(j+1)], j>=1 | 0.777256783668 | 2.069070965232 | Tail bound below |

For the first four laws the map was checked at s=0.1,0.5,s_*,0.9, with the odd mass split in ratio 1:2. Their pivot means were also checked by direct degree/count summation. Exact enumeration separately checked critical and subcritical laws and configurations with three odd colours. The finite-law exact enumeration and symbolic characteristic-polynomial calculation provide checks independent of simply evaluating the manuscript's final formula.

For the heavy law, G(s)=s+(1-s)log(1-s), G'(s)=-log(1-s), and G''(s)=1/(1-s). These closed forms independently verify the numerical values and show that infinite mean is genuinely being tested. The sums were truncated at degree 2000; for s<=0.9 the omitted derivative tail is at most 0.9^2000/(1-0.9), since chi(n)n=1/(n-1)<=1. The omitted second-derivative tail is at most 0.9^1999/(1-0.9), since chi(n)n(n-1)=1. Both are below 1e-89. Poisson summation through degree 100 has a much smaller tail than floating-point rounding at the tested parameters.

The sparse-law test covers **infinite logarithmic moment**, not merely infinite mean. Its probabilities telescope to one, and E log N = log(2) sum_j 2^j/[j(j+1)] is infinite. The first four atoms suffice numerically near the reported root: all omitted degrees are at least 2^32. Monotonicity of n s^{n-1} beyond that degree bounds the omitted G' contribution by 10^(-470021793) at the computed root. This is a numerical stress check, not a computational proof of the general rogueness theorem.

The identity-map test checked exact rational p=0,1/4,1/2,9/10,1 and verified Psi_80(p)=p-p^80/80 exactly. The moment outputs were:

    partial mean through degree 100000 = 12.090136129863 (harmonic divergence)
    partial E log(1+N) = 1.553642244083
    remaining logarithmic moment <= 0.000264121453

The tail bound follows from the integral of 2 log(2x)/x^2 and is independent of the symbolic telescoping calculation.

The spine checks include two different laws:

* For (1/4)delta_0+(3/4)delta_2, exact child-configuration enumeration with the analytically derived survival probabilities gives P(survival | a)=1/2 and P(survival | b)=1. It gives E[W | as]=E[W | bs]=3/4 and E[W_i W_{i+1} | either original surviving type]=9/16<1.
* For delta_2, B is binary XOR. Under original root a, its children are aa or bb with equal probabilities. After switching a uniformly selected child, the root is b and the children are ba or ab. The whole-spine information already determines whether the first child is b, so its conditional probability is zero or one. Under RST^{bs} that probability is 1/2. This explicitly disproves the whole-spine conditional-law assertion at JPS lines 2300–2302. Enumerating depth two verifies that all four finite-exploration histories retain the correct unswitched conditional subtree law instead.

The numerical checks support the formulas; the branching, null-set, analyticity, and absolute-continuity arguments above are what establish the nonnumerical assertions.

Audited source SHA-256 digests, to identify the files to which these line numbers refer:

    PAPER.tex                       f8eff85cc16eefb783a9d1d3c6f7bb9b216d724dafbf987ec410e6b0b40d0ab7
    references.bib                  30d72642d8d1884763daa6d34bb41f9e9475e6c83633ec10e70b72ab1dbe5b51
    sources/jps/pivot_trees.tex      a5db1c79a7ecdf7c7126e551c201f156dac854f9ded819014f1541eb0be52477
    sources/jps/pivot_trees.bbl      68aca5108f17df9806dd1291b8b7616d3b42be1349df25f6b057be142f788c1b
    sources/rz/rz.tex               48d2857d70efa8b7883d4d8255125aec56cb19c68f14b0c25bd1b79a0b665308

Task: “find every error, gap, overclaim and misattribution before it is read by others” — 12 November 2026, 20:53 (Asia/Tbilisi; launch log).
