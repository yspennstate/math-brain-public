---
title: "Full FEI: A Research Strategy for 100 Codex Agents"
subtitle: "Building on the threshold manuscript, joint descriptions, and the Brain's counterexamples"
author: "Research planning report"
date: "11 October 2026"
lang: en-US
toc: true
toc-depth: 2
numbersections: true
---

# Purpose and recommendation

The central recommendation is to spend the computation on **a small number of precise, competing mechanisms for paying the entire Fourier entropy with one influence budget**. One hundred agents repeatedly attempting a generic proof would produce correlated guesses and repeated mistakes. A useful allocation gives each group a different mathematical obligation, a falsifier, and a clear interface to the other groups.

The completed threshold paper provides a substantial structured starting point. Its most useful contribution to a full-FEI campaign is the combination of a valid reference distribution, complete joint witness costs, strong composition statements with explicit hypotheses, and exact reductions showing where the general problem is still present. The campaign should build outward from these interfaces. Further small improvements to the threshold constant are a low priority unless they reveal a mechanism that removes a structural restriction.

The objective is the full uniform-cube Fourier entropy-influence conjecture: find a finite constant $C$, independent of the dimension and the function, such that

$$
H(f)\le C I(f)
\qquad\text{for every }f:\{-1,1\}^n\longrightarrow\{-1,1\}.
$$

A rigorous Boolean family with $H(f_n)/I(f_n)\to\infty$ would instead disprove it. Refuting one proposed lemma or one numerical constant does neither. **Full FEI remains open in the work recovered and checked for this report.** No claim below assumes a universal estimate that has not been proved.

The proposed allocation is twenty research groups with five roles each. The twenty live B-stream assignments were installed concurrently and are preserved; `NATIVE_MAPPING.md` maps this report's F-groups to those streams. These are **100 logical roles and a design for using 100 workers if that capacity is actually available**. The operating campaign uses the twenty existing scheduled jobs in this environment, with their already installed B01-B20 assignments. Listing five roles in a prompt does not create five simultaneous agents. Each job uses the roles within its permitted capacity or performs them in sequence; the installed tasks' restrictions on launching additional workers remain in force. The coordinator is included in the five; there is no uncounted management layer.

The fixed campaign window is **11 October 2026 at 19:15:57 UTC through 21 October 2026 at 19:15:57 UTC**, equivalent to 22:15:57 Asia/Jerusalem on both dates. The ten-day period is a deadline for concentrated work and a useful handoff, not a prediction that an open conjecture will be solved. The operating assignments, deployment receipts, immutable research runs, and private mirrors make the distinction between a proposed plan, installed tasks, executed research, and accepted mathematics explicit.

# The mathematical starting point

## Conventions and the universal obstruction

Write

$$
f(x)=\sum_{S\subseteq[n]}a_S\chi_S(x),\quad
p_S=a_S^2,\quad
H(f)=\sum_Sp_S\log_2(1/p_S),\quad
I(f)=\sum_S|S|p_S.
$$

Parseval gives $\sum_Sp_S=1$. Terms with zero mass contribute zero. Ordinary influence is the expected number of occupied coordinates in a random Fourier set. The challenge is to show that this expected size pays for describing the set, even though its coordinates may have complicated dependence.

An arbitrary distribution on subsets does not satisfy the conjectured inequality. Uniform mass on the $n$ singleton sets has entropy $\log_2 n$ and expected size one. The inverse Walsh expansion of its positive square roots is generally not Boolean. Every route must use a consequence of Booleanity that excludes such examples. The complete signed constraint is

$$
\sum_S a_Sa_{S\triangle U}=\mathbf 1_{\{U=\varnothing\}}
\qquad\text{for every }U\subseteq[n],
$$

which is precisely the Fourier form of $f^2=1$. Replacing these identities by only nonnegativity, Parseval, or a few low-order constraints can discard the essential information.

All entropies are in bits except the continuous-time correlation subsection, which explicitly uses natural logarithms. The character-centered quantity in the paper is

$$
D(f)=\sum_i\min\{I_i(f),1-I_i(f)\}
=\min_U I(\chi_U f).
$$

It is distinct from ordinary influence and from $I(f)-\operatorname{Var}(f)$. Neither a biased normalization nor a change of physical coordinates may be silently substituted. In particular, arbitrary invertible linear changes of cube coordinates preserve some spectral algebra but do not preserve the cardinality $|S|$ that defines physical influence.

## What the completed paper supplies

The recovered 36-page version of *Fourier entropy of threshold functions and their compositions* is archived as `baseline/threshold-paper.tex`, source SHA256 `3a395e98153f826fa9160c348e45779f204d3ea77376f40cd71ee57440ba8193`. During this work, a concurrent agent completed a 38-page edition with a shared-data multiplexer extension. That newer source is archived as `baseline/current-threshold-paper.tex`, SHA256 `5cff9d1b91c92883a6d35ec7674ff5953365cadc85299747e4047d9deb150dac`; its public-package PDF has SHA256 `182eba4219e14b7f87200a7d99d2755acc81d41198e4990902986909c19504bc`. The older source pin remains available for exact historical dependency checks.

The principal uniform-cube theorem is

$$
H(f)\le C_{\rm reg}D(f),\qquad
C_{\rm reg}=\log_2(4+e)+2\log_2(e\pi)<8.937
$$

for the paper's regular functions, including every deterministic linear threshold function. Here regularity means a total desirability order after orienting the variables; it does not mean that the threshold weights must be small. Character multiples inherit an ordinary-influence estimate and a strong estimate with coefficient $4C_{\rm reg}<35.746$ against the variance deficit.

The paper also gives explicit logarithmic dependence for Boolean combinations, desirability width, and bounded-overlap gate constructions; corrected product-measure FEI-plus for symmetric thresholds; and a read-once threshold/parity closure with a constant below 744 independent of arity and depth. Arbitrarily weighted thresholds under arbitrary product biases remain a separate obligation.

The continuation repairs an important accounting loss. A finite queue and incidence forest can describe the gate choices used by an entire Fourier set together. The bound retains the number of gates actually used and the true allocation congestion, rather than charging a full gate label independently to every coordinate. This recovers a constant-order estimate for addressing functions. It does not establish that every Boolean function has a representation whose complete expected cost is $O(I)$.

The newer extension proves a useful closure for shared data. At a node with $a$ fresh uniform physical selector bits and Boolean branches $g_b$ on a common data cube, the exact collision analysis gives

$$H(F)\le 2a+2^{-a}\sum_b H(g_b).$$

If neighboring branch labels are orthogonal, the selector influence is $a/2$. The ordinary FEI coefficient therefore closes with $\max\{4,C\}$, and the centered version also closes under the stated orthogonality hypothesis. Repeating nodes with fresh selectors preserves $C_{\rm reg}$ for regular leaves even when the leaves reuse data. More generally, a uniform selector-energy lower bound $I_{\rm sel}\ge ca$ gives the ordinary coefficient $\max\{2/c,C\}$. These exact statements are in the new subsection `sec:shared-multiplexers`, independently checked during reconciliation. Their hypotheses are important: low-energy selectors and reuse of selector variables remain outside this argument.

The paper's selector and rare-activation identities are equally important. They provide positive closure results under precise support conditions and show that dropping those conditions can recover full FEI itself. These identities are a boundary map for the campaign, not evidence that the boundary has already been crossed.

The manuscript has analytic reviews and finite checks for the stated identities and constructions. Those checks do not constitute external peer review or a formal proof of every analytic argument. Future claims must cite the exact lemma and hypotheses they use, rather than treating an entire manuscript as an unchecked black box.

## What is already known in the literature

Whole-set coding is an established FEI framework. Wan, Wright and Wu connect expected description length with influence and develop decision-tree and protocol bounds [1]. The campaign's prospective contribution is an effective new code or cost estimate, not the observation that coding can prove FEI. Shalev obtains an $O(\sqrt{k})$ coefficient for read-$k$ decision trees and proves powerful low-influence reductions [2]. The read-parameter target below must be compared with that bound.

O'Donnell and Tan supply a strong composition framework and examples requiring a universal FEI constant of at least 6.278 [3]. Arunachalam and coauthors prove min-entropy and parity-certificate results [4]; min-entropy controls the largest Fourier coefficient and is weaker than the Shannon entropy required here. Recent restriction and stopping-tree work is also relevant [5]. These sources should be read before a team describes a familiar reduction or coding language as new.

The original marginal-influence entropy estimate belongs to Keller, Mossel and Schlank [6]. A later arXiv submission with a related claim was withdrawn and points to that earlier result [8]. Spectral concentration results such as [7] are valuable, but concentration on many coefficients and a Shannon entropy estimate require distinct tail accounting. A literature summary must preserve those distinctions.

# Counterexamples as research constraints

The detailed seed ledger is `COUNTEREXAMPLES.md`. Its role is to rule out invalid proof steps before they consume many runs. Each team must state which hypotheses its candidate retains and which obstruction it overcomes.

**Addressing exposes repeated label charges.** For $m$ control bits and $2^m$ independent data bits, $f(a,y)=y_a$ has

$$H(f)=2m,\qquad I(f)=1+m/2.$$

The address should be described once. A scheme charging its $m$-bit label to order $m$ separate control coordinates can spend order $m^2$. The repaired queue gives a bound below $10I$; the exact spectrum gives $H=4(I-1)$. Every proposal to remove overlap logarithms should first explain this family.

**Zero local erasure entropy does not imply an easy spectrum.** If a fresh sign $z$ is used to replace $g(x)$ by $g(x_1z,\ldots,x_nz)$, every Fourier set has even cardinality. Each occupancy bit is determined by the other bits, so the sum of one-coordinate conditional entropies is zero. Yet the Fourier entropy is unchanged and the influence grows by at most a factor two. The class therefore retains full-FEI difficulty. A small local entropy cannot be used as a proxy for a small total entropy.

**Restriction can create synergy.** Recovered parity-mixture constructions have children with zero erasure entropy and a parent with erasure entropy growing with dimension. The selector influence is bounded. Consequently, a fixed convex blend of total and erasure entropy does not automatically admit a constant-cost one-coordinate induction. A repair must keep the created dependence or remove it through a proved global payment.

**Rare restrictions can require logarithms.** The Brain's sparse bent perturbations have child influences tending to zero while the ratio of the relevant local entropy cost to the proposed local payment diverges. Spectator tensor factors also defeat scalar proxies that depend on irrelevant child complexity. These examples do not disprove FEI. They disprove particular attempts to pay each bad split by a bounded local quantity.

**Two-cell selectors can encode any balanced core.** For a balanced Boolean $g$,

$$
M_g=\frac{1+g}{2}y_1+\frac{1-g}{2}y_2,
\qquad
H(M_g)=2+\tfrac12H(g),\quad I(M_g)=1+\tfrac12I(g).
$$

Tensor powers balanced by one fresh sign remove the additive constants. A universal FEI theorem for this unrestricted two-cell class yields the full conjecture with the same constant. The number of cells alone is therefore not a simplification.

**Small total influence and rarity alone also retain the optimal constant.** Let $A_r$ be the conjunction of $r$ fresh activation bits, $p=2^{-r}$, and let $g$ be balanced. For $F=1+A_r(g-1)$,

$$
I(F)=p[I(g)+r],
$$

$$
H(F)=pH(g)+2rp(2-p)+(1-p)^2\log_2\frac1{(1-p)^2}.
$$

For every nonconstant $f$, taking $g_t=z\prod_{s=1}^t f(x^{(s)})$ and $r_t=\lceil2\log_2t\rceil$ sends the influence and minority probability to zero while $H(F_t)/I(F_t)\to H(f)/I(f)$. The exact identity is useful; the broad low-influence equivalence already has prior art [2]. A promising sparse class needs another structural hypothesis that does not simply hide an arbitrary balanced core.

**Shared leaves can hide the full problem.** Partition the control cube into points and put the leaf $f(z)y$ at point $z$. All cells are affine and every leaf is a signed dictator, but the leaf Fourier supports coincide. The resulting function is $f(z)y$, with $H(fy)=H(f)$ and $I(fy)-1=I(f)$. An unrestricted strong closure with a universal constant would prove full FEI. Keeping the sharp constant four of the separated-support class would be false by [3]. Similarly, entropy subadditivity for Fourier products with shared variables cannot be assumed.

# Main route I: complete joint descriptions

## The precise missing theorem

Let $\mathcal S$ have law $p_A=\widehat f(A)^2$ and put $v=\Pr(\mathcal S\ne\varnothing)=\operatorname{Var}(f)$. A distribution or subdistribution $Q$ on nonempty Fourier sets provides a valid description bound

$$
H(f)\le h_2(v)+\sum_{A\ne\varnothing}p_A\log_2\frac1{Q(A)}.
$$

The queue construction instantiates $Q$. For a global root-odds parameter $\lambda$, it supplies

$$
H(f)\le h_2(v)+v\Lambda_\lambda+
\sum_{A\ne\varnothing}p_A\min_{\tau,\mathcal T}
\mathcal C_\lambda(A;\tau,\mathcal T).
$$

Here $\Lambda_\lambda=\sum_l\log_2(1+\lambda\pi_l)$ is the root normalizer, $\tau$ assigns coordinates jointly to gate supports, and $\mathcal T$ is the incidence forest. The cost includes roots, local subsets, their sizes, attachments, child labels, rank costs and overlap congestion. No one term can be silently omitted when a representation changes.

The universal research target is a representation and a normalized law for which the **entire right-hand side**, including its variance term, is at most $CI(f)$ with dimension-independent $C$. This is a sufficient route to full FEI. FEI itself does not automatically imply that this particular queue representation is efficient. A proved bound for a broad proper class is also a meaningful result.

F01 owns normalization and global coding. F02 owns correlated assignments. F03 owns rare roots and non-reuse of budgets. F04 owns references that escape total-order or width dependence. They should work separately enough to expose mistakes, but combine estimates only through this same complete cost expression.

## Three concrete improvements to try first

**Use the whole family of valid witnesses.** Distinct finite runs of a probability process are disjoint outcomes. If $\mathcal W(A)$ is an explicitly specified family of distinct runs producing $A$, then $Q(A)\ge\sum_{w\in\mathcal W(A)}\Pr(w)$. Counting many witnesses can yield an entropy credit that a minimum-cost witness misses. The difficulty is to count genuinely distinct runs, including repeated visits and termination, and then control the expectation analytically.

**Optimize correlations before coordinatewise bounds.** The useful quantities include the number of used gates and

$$
L(A,\tau)=\sum_{l:|A_l|>0}|A_l|\log_2\frac{|A\cap R_l|}{|A_l|}.
$$

F02 should seek correlated assignment rules and combinatorial dual certificates that bound their spectral expectation on an explicitly named class. A pointwise optimum discovered by an integer program is diagnostic until it yields a mathematical rule and an expectation bound. The same gate label should not reappear under a new name in the rank or attachment cost.

**Pay for choosing the scale.** A separate root parameter chosen freely for each Fourier set is invalid. A legitimate repair is a mixture of normalized laws. For weights $w_j\ge0$ with $\sum_jw_j\le1$,

$$
Q_{\rm mix}(A)=\sum_jw_jQ_{\lambda_j}(A)
$$

gives

$$
H(f)\le h_2(v)+\sum_{A\ne\varnothing}p_A
\min_j\left\{\Lambda_{\lambda_j}+
\min_{\tau,\mathcal T}\mathcal C_{\lambda_j}(A;\tau,\mathcal T)
+\log_2\frac1{w_j}\right\}.
$$

This is a direct consequence of the proved reference interface and Gibbs' inequality. A dyadic scale prior may make the selector cost small, but it never makes it free. F03 must show that the resulting scale and sparse-root residuals are summable against one available influence budget. Choosing the unknown spectral law itself as an ideal reference is circular.

## A modest seed lemma: effective piece count

The rank method offers an immediately testable refinement. Suppose the signed derivative pieces $d_l$ have disjoint physical supports and satisfy the same piecewise Laplace estimate as in the manuscript. Let

$$
a_l=\frac{\|d_l\|_2^2}{\|\sum_jd_j\|_2^2},\qquad
K_{\rm eff}=\left(\sum_l\sqrt{a_l}\right)^2\le m.
$$

For the paper's multi-order rank variable $G$, write $Z=e^{-G}$. The positive Fourier multiplier $e^{-tZ}$ and the triangle inequality give

$$
\mathbb E e^{-tZ}\le
\frac{(\sum_l\|d_l\|_2t^{-1/4})^2}{\|\sum_ld_l\|_2^2}
=K_{\rm eff}t^{-1/2}.
$$

Combining this with the bound by one and the manuscript's Frullani integral yields

$$\mathbb E G\le2+\gamma+2\ln K_{\rm eff}.$$

The complete hypotheses and derivation are in `SEED_LEMMAS.md`; this is a derived refinement for review, separate from the already completed paper. It can help when pivotal masses are concentrated. Equal masses give $K_{\rm eff}=m$, so it does not solve addressing or remove every normalizer. Its first success criterion is an application where the full final theorem improves, rather than just a renamed parameter.

# Main route II: restriction histories and global information payments

## Exact physical restriction identities

Let $g=f|_{x_i=1}$ and $h=f|_{x_i=-1}$. For the actual restrictions of a Boolean function, the entropy decrement is

$$
\Delta_iH=H(f)-\tfrac12[H(g)+H(h)]
=H(\mathcal S_i\mid\mathcal S_{-i})+
\operatorname{JS}(\widehat g^2,\widehat h^2).
$$

The Jensen-Shannon term obeys

$$
\operatorname{JS}(\widehat g^2,\widehat h^2)
\le\frac2{\ln2}\min\{I_i(f),1-I_i(f)\}.
$$

Influence has the exact decrement

$$I(f)-\tfrac12[I(g)+I(h)]=I_i(f).$$

Thus a terminating adaptive restriction tree has two matching telescoping formulas. The expected sum of its physical-coordinate influence payments plus its expected leaf influence is exactly the original influence. The analogous entropy sum includes the actual entropy drops and the leaf entropies. F05's goal is to exploit a choice of tree and a sharper entropy charge, with all bad splits and leaf terms included.

A useful recovered refinement measures actual amplitude mismatch. Put $a_T=\widehat g(T)$, $b_T=\widehat h(T)$,

$$
q_T=(a_T^2+b_T^2)/2,\quad
m_T=(|a_T|-|b_T|)^2/4,\quad M=\sum_Tm_T,\quad\nu_T=m_T/M.
$$

When $M>0$, the recovered bound is

$$
\Delta_iH\le M\left[\log_2(1/M)-D_2(\nu\Vert q)+\frac3{\ln2}\right].
$$

Here $D_2(\nu\Vert q)=\sum_T\nu_T\log_2(\nu_T/q_T)$ means Kullback-Leibler divergence measured in bits, not Renyi divergence of order two. For $M=0$, the entropy drop is zero and $\nu$ need not be defined. This estimate keeps more information than a bound based only on child influences. It is still a local inequality. The new obligation is a cumulative bound along an actual tree, not a second assertion that the local logarithm is harmless.

An informative first result would be a restriction-closed class beyond the baseline for which a rule selects coordinates, a potential pays every decrement, and the leaves have a proved FEI bound. The candidate should be tested on the rare bent examples, parity synergy, and irrelevant tensor factors before its proof is expanded.

## Proper blocks and stopping rules

For a physical block $A$ with complement $C$, let $X$ denote its uniform assignment, and conditionally on $X=x$ sample $Y$ from the squared Fourier coefficients of the restricted function $f_x$ on $C$. The block identity splits the entropy decrement into

$$
H(\mathcal S_A\mid\mathcal S_C)+I(X;Y).
$$

The information-channel term is at most $(2/\ln2)I_A(f)$. The conditional spectrum term is the main issue. F06 should use proper blocks chosen from a proved dependence structure, then stop at thresholds, affine leaves, or another certified family. Both outcomes of every restriction must remain in the accounting.

Taking the block to be all coordinates leaves $H(f)$ itself and restates FEI. Taking only singleton blocks can repeat the known synergy failure. A useful block theorem therefore needs a selection rule, termination, a leaf theorem and an influence identity that prevents spending one pivotal event several times.

## Erasure entropy and the signed downward-edge functional

Let $B(f)=\sum_iH(\mathcal S_i\mid\mathcal S_{-i})$. The recovered erasure reduction compares optimal class constants for a universal $B/I$ bound and a universal $H/I$ bound, within an explicit additive constant. It does **not** supply a pointwise inequality $H(f)\le B(f)+O(I(f))$ for each individual function. The parity lift above is the reason that distinction matters.

The downward-edge functional

$$
L(f)=\sum_Sp_S\sum_{i\in S}\log_2\left(1+\frac{p_{S\setminus\{i\}}}{p_S}\right)
$$

satisfies $L\le B\le L+I/\ln2$. Generic Jensen bounds lose a dimension-dependent logarithm. F07 and F09 should attempt a sign-sensitive inequality using the full Boolean convolution equations. A new nonlinear potential is worthwhile only if it is tensor-stable, survives parity lifts, and has a verified global change formula. Renaming $L$ does not bound it.

## Correlation lifetime under a specified reveal policy

The Brain's current route map contains a more differentiated target for F08. In this subsection entropy is in natural units. For a finite law $P$ on occupancy sets define

$$
\operatorname{TC}(P)=\sum_iH(S_i)-H(S),\qquad
\operatorname{DTC}(P)=H(S)-\sum_iH(S_i\mid S_{-i}).
$$

Use the source's rate-one observation dynamics for occupied coordinates and its forced reveal/removal when a posterior marginal reaches $\varepsilon e^{-2t}$. Both forced outcomes, instantaneous cascades, and the original forward time are part of the policy. Let $P_t$ be its active posterior and $J_0=\mathbb E|S_0|$. The target is

$$
\int_0^\infty e^t\mathbb E\operatorname{TC}(P_t)\,dt
\le A_\varepsilon[\operatorname{DTC}(P_0)+J_0]
$$

for a fixed admissible $\varepsilon$, uniformly over the source's stated class of laws. The exact balance includes a **negative information refund at forced reveals**. Dropping that refund asks for a stronger estimate that is not justified by the balance. A one-hot law with a logarithmic lifetime is not a counterexample when its initial dual total correlation is already logarithmic.

F08 must first reconstruct the finite-horizon identity and every definition from the source pin, then prove this estimate or give a finite-law counterexample to its exact scope. Even a proof requires a separate entropy-transfer theorem to imply FEI. The Brain's actual-source path functional is already comparable to Fourier entropy up to $O(I)$; proving a uniform bound for that functional merely relocates the full problem unless a new source-specific estimate controls it. Actual Boolean ancestry is potentially useful structure. Arbitrary wavefunctions or posterior laws cannot be substituted for physical Boolean restrictions without proof.

# Main route III: Boolean algebra, interference and new classes

## Two spectral addresses and collective row constraints

This target conditions a genuine Boolean Fourier spectrum on a set of address coordinates $A$. For each positive-probability value of $\mathcal S_A$, require the remaining coordinates $\mathcal S_C$ to have a product distribution. This is a property of the spectral law, not an ordinary decision-tree selector representation.

The Brain has solved the zero- and one-address endpoints with constant two. A six-variable two-address example has $H=5$ and $I=17/8$, hence $H/I=40/17>2$. F12 should settle the correctly stated two-address class with a valid constant or find an asymptotic obstruction. A theorem for fixed two-address complexity is a proper-class advance; no equivalence with full FEI is asserted. Allowing arbitrarily many addresses without a uniform cost eventually makes the condition vacuous.

One possible algebraic route takes the partial Walsh rows $g_T(x_C)=\mathbb E_{z_A}[f(z_A,x_C)\chi_T(z_A)]$, indexed by $T\subseteq A$ and defined on the complementary cube $C$. These rows are usually real-valued, not Boolean. They obey the coupled pointwise relations

$$
\sum_Tg_T(x)g_{T\triangle U}(x)=\mathbf1_{\{U=\varnothing\}}.
$$

F09 should exploit the coupled system. Applying a Boolean rigidity lemma to each row separately would be invalid. F12 and F18 can verify conditional-product hypotheses by exact rank-one tests on probability arrays, search the genuine Boolean feasible set, and return small exact witnesses to the algebra team.

## Decision-tree covariance

For a decision tree in which each physical variable labels at most $k$ nodes, the relevant known coefficient is $O(\sqrt{k})$ [2]. A concrete improvement target from the coding literature is a logarithmic bound for the signed covariance sum

$$
\operatorname{Cov}[T]=\sum_v2^{-d(v)}\operatorname{Cov}(g_v,h_v)
\le A\log_2(k+1)I(f),
$$

with the tree conventions and resulting coding implication checked from [1]. Here $g_v,h_v$ are the two subfunctions at node $v$ and $d(v)$ is its depth. The proposed logarithmic target is not claimed as a new conjecture.

F10 should begin with laminar repeated-variable patterns or a single cycle of overlap, where the covariance structure may be explicit. Taking absolute values prematurely can discard the cancellation the bound needs. A leaf-count theorem and a read-count theorem have different parameters; they should be compared only after specifying a representation. Improving the read dependence would be significant, but a representation with enormous $k$ does not by itself give full FEI.

## Selector interference and repeated-variable composition

The completed selector theorem applies to balanced leaves on a data cube disjoint from the control coordinates, with pairwise disjoint nonempty leaf Fourier supports. The leaves' physical variable supports may overlap with one another. For selector probabilities $p_j$ and normalized cell spectra $q_j$ it gives

$$
H(F)=H(p)+\sum_jp_j[H(q_j)+H(g_j)],
$$

$$
I(F)=\sum_jp_j[\mathbb E_{q_j}|T|+I(g_j)].
$$

Strong cell and leaf bounds close with the maximum of their constants and four. The support condition is what makes the spectral pieces separate. The 38-page extension now handles fresh-selector recursive multiplexers with orthogonal neighboring branches, and more generally ordinary FEI under a uniform selector-energy fraction. F11 should move beyond these solved cases: derive sharper collision credits for low-energy selectors, or control overlap in nonuniform affine-cell partitions and structures without fresh independent selectors. Orthogonality in one averaged sense need not imply coefficientwise separation.

A useful new target is an interference penalty outside those already proved hypotheses that composes without accumulating a growing depth factor. F14 works on the corresponding shared-variable Fourier convolution and a stable compositional invariant. The signed-dictator encoding in the obstruction ledger must accompany every proposed unrestricted closure. A condition that permits arbitrary point cells and arbitrary reuse of the same signed leaf already contains full FEI.

## Weighted thresholds under product bias

The symmetric biased-threshold theorem leaves a concrete extension for F13. If $q_i\in(0,1)$ are independent input probabilities, $\sigma_i^2=4q_i(1-q_i)$, and $P(S)$ denotes squared coefficients in the orthonormal biased basis, the corrected entropy is

$$
H_\mu^+(f)=\sum_{S\ne\varnothing}P(S)
\log_2\frac{\prod_{i\in S}\sigma_i^2}{P(S)}.
$$

The desired strong bound uses $I_\mu(f)-\operatorname{Var}_\mu(f)$. Uncorrected biased Shannon entropy divided by $I_\mu$ is already unbounded for a biased dictator; using the correction is essential.

Begin with a bounded number of distinct weights or a controlled weight ratio, but preserve uniformity in the biases, near-dictator limits and deterministic-input reductions. A successful weighted gate theorem would feed the existing read-once composition framework immediately. It would extend the paper materially. It would still require a new overlap or representation mechanism to imply full FEI.

# Computation that can change the mathematics

## Search candidates, not just the conjecture's ratio

F16 should receive exact candidate inequalities from the proof teams. A search for a violated intermediate statement is often more informative than another search for large $H/I$, because the former can eliminate a whole proof architecture with a small certificate. Search outputs must preserve the hypotheses, including Booleanity, physical influence, source ancestry, and any stopping-rule conditions.

Use exact integer Walsh transforms. A Boolean table has coefficients $W_S/2^n$, so squared masses and influence are rational. Entropy comparisons involve logarithms and require outward interval bounds or an analytic comparison for a certificate. Floating-point exploration is useful for finding a witness; it should not be described as exact proof.

The complete four-variable space has $2^{16}=65{,}536$ sign tables. Five variables already have $2^{32}$ tables. Do not promise an unperformed exhaustive five-variable search without a runtime analysis and a proved symmetry reduction. Input permutations, sign flips and output sign changes have clear invariance properties. More aggressive linear coordinate transformations require a fresh influence calculation.

Each returned witness should contain a truth table or exact symbolic construction, the full tested statement, coefficient convention, rational influence, certified logarithmic comparison, and a minimal replay program. A maximizer from a sampled family is not a proven global maximizer. A certificate of one inequality is not a certificate of the surrounding analytic proof.

## Asymptotic stress families and a failed strengthening

F17 converts finite warnings into all-dimensional tests: addressing, tribes, parity lifts, bent perturbations, recursive selectors, point defects and tensor products. The output should specify which ratio diverges. The witness-cost ratio may diverge while $H/I$ stays bounded; that refutes a proposed code bound and can suggest a better code.

One direct diagnostic rules out an attractive moment strengthening. Let $f_r$ equal $-1$ at one point of an $r$-cube and $+1$ elsewhere, with $p=2^{-r}$. Then

$$
I(f_r)=2rp,\quad P(\varnothing)=(1-2p)^2,\quad
P(S)=4p^2\quad(S\ne\varnothing).
$$

For fixed $0<\alpha<1$, the Renyi moment is

$$
Z_\alpha=(1-2p)^{2\alpha}+(p^{-1}-1)(4p^2)^\alpha.
$$

When $1/2<\alpha<1$, its entropy satisfies

$$
H_\alpha(f_r)\sim
\frac{4^\alpha p^{2\alpha-1}}{(1-\alpha)\ln2},
\qquad H_\alpha(f_r)/I(f_r)\longrightarrow\infty.
$$

At $\alpha=1/2$ the Renyi entropy tends to a positive constant, and for $\alpha<1/2$ it grows on the scale $r$, so their ratios also diverge. Meanwhile the Shannon ratio tends to four. Thus a dimension-free fixed-$\alpha<1$ Renyi bound of the form $H_\alpha\le C_\alpha I$ is false, even on these simple Boolean functions. A moment or semigroup approach must work at the Shannon derivative or pay a scale-dependent tail correction. This calculation is a diagnostic, not a novelty claim.

## Optimization and formal work

F18 should fit a potential or solve a finite assignment problem only when the resulting dual certificate could bound a named unpaid term. Good outputs include a symbolic inequality valid on an entire parameter region, a rational dual solution with an independent checker, or an exact counterexample separating two candidate potentials. Increasing a sample size without changing the mathematical conclusion is a poor use of the budget.

F19 should reconstruct pivotal proofs from definitions and independently design adversarial examples. Formalization is most useful for reusable identities or delicate discrete steps: Parseval, restriction coefficients, tensorization, Boolean autocorrelation, exact queue normalization, and termination of a finite construction. For a continuous-time argument, a checked finite generator does not settle integration, cascades or the terminal limit. Formalize those obligations explicitly if that route becomes competitive.

# Allocation, decision gates and standards of progress

## Why this allocation

F01-F09 attack universal mechanisms directly: whole-set descriptions, conserved restriction budgets and signed Boolean constraints. F10-F14 pursue structurally meaningful bridges that can yield substantial results while testing those mechanisms. F15-F18 supply extremal reductions, exact falsification, asymptotics and proof-directed optimization. F19 reconstructs candidate arguments, and F20 works on a complete synthesis with an explicit list of unpaid obligations.

These boundaries are starting responsibilities, not permanent silos. If F03 proves a multiscale estimate, F05 should test whether it pays the actual restriction log; if F09 discovers a signed cancellation identity, F01 should test whether it improves a reference distribution. Sharing a theorem with a precise interface is more useful than sharing a long speculative transcript.

Every team has five roles, listed in the allocation appendix. Across a team, roughly three roles construct or analyze arguments, one attempts independent falsification, and one integrates evidence or checks a complementary formulation. These assignments are tailored to each problem. F19 does not relieve the other teams of their own checks. For a candidate full proof, reviewers must come from other teams and reconstruct the argument independently.

## Ten-day decision schedule

| Period | Work to prioritize | Required decision |
|---|---|---|
| Days 1-2 | Reconstruct only essential dependencies; state exact lemmas; attack shortcuts with known obstructions. | Retire known, duplicated or already refuted targets. Every live route has a measurable unpaid term. |
| Days 3-4 | Prove the most promising intermediate statements; seek exact small counterexamples. | Continue a route because a bound improved or an obstruction was overcome, not because it produced more pages. |
| Days 5-6 | Join compatible mechanisms; resolve normalization and budget reuse; reallocate stalled work within FEI. | Identify a plausible universal bridge or finish a worthwhile proper-class theorem. |
| Days 7-8 | Attempt a complete dimension-independent argument; stress it asymptotically; repair the sharpest new class result. | Every claimed universal step has a proof and explicit dependencies. |
| Days 9-10 | Independent reconstruction, source audit, certificate replay, writing and continuation handoff. | Accept only what survives review; preserve the exact remaining gap and strongest counterexamples. |

After three consecutive runs with the same unpaid obligation and no substantive advance, the team writes a brief stuck analysis and changes method. After six such runs, the installed B20 synthesis stream reallocates the research effort within FEI, using input from the proposed F20 synthesis roles. Neither rule retires the conjecture or redirects a job to unrelated work. A serious new obstruction may justify a pivot immediately. A promising proof may justify sustained work when the ledger shows actual movement.

## What would count as significant

The highest-value outcome is a complete proof of full FEI or a rigorous unbounded-ratio Boolean counterfamily. A full proof must give one dimension-independent constant and cover every finite Boolean function, including constants and limiting reductions. A counterfamily must establish unbounded ratios analytically, not merely exceed a previously guessed constant.

Several lesser outcomes would still justify concentrated computation: a complete universal correlation or signed-edge inequality with a noncircular transfer to FEI; a broad new FEI class outside the manuscript's current closure; a logarithmic read-$k$ decision-tree bound; product-biased strong FEI for genuinely weighted thresholds; the corrected two-address theorem; or a new asymptotic obstruction that eliminates a live approach and leaves a sharper surviving question.

A constant-preserving equivalence can be a useful structural result but is not a proof of its equivalent target. An independently checked repair of a pivotal lemma is more valuable than a large batch of unrelated tests. Counting accepted claims, removed hypotheses, controlled residuals and informative falsifiers gives a better view of progress than counting tokens, pages or agent-hours.

The plan does not assign a numerical probability of solving FEI in ten days. There is no evidence base here for such a prediction. Its purpose is to increase the chance that available computation produces mathematically decisive information and leaves reusable results even if the universal obstruction survives.

# Execution and repository contract

## Twenty schedules and one fixed scope

The user's latest instruction reassigns this environment's twenty currently enabled jobs to full FEI for the fixed window. Readback confirms the existing hourly offsets and Asia/Jerusalem timezone. The installed recurrences use finite `COUNT` values of 239 or 240, and their last occurrences precede the fixed endpoint; their schedules are preserved. The five previously disabled jobs are outside this change. The campaign does not create additional native schedules or assume additional paid compute.

The requested research model and reasoning preference can be written in the prompts. The exposed scheduler update interface has no model or reasoning selector, so prompt text must not be reported as verified model configuration. A run records the actual observed model and effort, or states that they are unavailable. Actual worker execution is also distinct from successful installation of a schedule.

The old Brain-maintenance, mixed-portfolio, movie and Primary Directive assignments are superseded for these twenty jobs during this window. Scoped coordination headers preserve the installed full-FEI B-stream assignments and prevent older controllers from restoring obsolete missions. Other accounts, access restrictions and source/privacy requirements retain their scope. At the deadline, the final natural run saves a continuation handoff; the campaign does not automatically extend or restore the old programme.

## Where the work goes

Both private research repositories receive this report and its operating files under:

`research_pushes/2026-10-11-full-fei-100-agents/`

The installed campaign's canonical editable state is `reports/fei-2026-10-11/` in `yspennstate/math-open-problems` on `master`. The existing Brain handoff root is `research_pushes/2026-10-11-full-fei-campaign/handoffs/account01/Bxx/` in `yspennstate/math-research-brain` on `main`. The present report and its source/obstruction supplement are saved under the common `research_pushes/2026-10-11-full-fei-100-agents/` path in both repositories. `NATIVE_MAPPING.md` connects this report's F-role groups to the live B-streams; it does not rename or replace those streams.

Each natural run preserves its existing immutable `runs/Bxx/<UTC_RUN_ID>/` record and Brain handoff. It reads the relevant supplementary targets and counterexamples, then saves complete mathematical work and necessary code or certificates through the installed private routes. B20 maintains the campaign synthesis. Shared indexes are reconciled from immutable deltas; concurrent proofs and peer-owned files are preserved. Every commit uses a fresh branch head. A failed mirror is recorded as a failed mirror, and native scheduler identifiers, credentials, signed URLs and unrelated account details stay outside this supplement's repository artifacts.

The public destination is separate: `yspennstate/fourier-entropy-threshold-functions`. The approved 38-page paper package is published at commit `cd27aa96a5bb670a5b3ae5451095b7020db8e9d4`. All twenty public files and all nineteen checksum entries match the checked package; the remote PDF bytes and source text also pass direct SHA256 checks. The existing publication was preserved without an additional public write. Only the approved threshold paper, LaTeX, declarations and reproducibility package belong there. **This report and the private campaign history do not belong in the public paper repository.** `PUBLICATION.json` records the verified release. The existing B20 synthesis job retains an idempotent check for that prepared package during its normal runs; no twenty-first schedule is needed. New campaign manuscripts need separate public-release authorization.

## A run's minimum mathematical record

Each substantive result records its exact statement and quantifiers, assumptions, ordinary or biased normalization, status, scope, proof or decisive failure, dependency pins, constants, tested domain, owner and reviewers. It names the single remaining obligation or states why the claim is complete. Statuses distinguish known literature, proved baseline, a derived lemma awaiting review, an open target, a conditional theorem, a refuted candidate and finite evidence only.

A candidate full solution requires two separate reconstructions by other teams and a source audit before the campaign treats it as accepted. Agreement among models is not itself a mathematical argument, and internal reviews are not external peer review. Routine no-progress runs can remain quiet, but the stored state must make the lack of progress clear. The final handoff should let a new researcher continue from the strongest exact statement without repeating the campaign.

# Sources and provenance

The complete threshold manuscript and its six verification programs/output files are retained in `baseline/`. These are the direct source for the paper-specific constants, queue construction, selector identities and activation formulas. The recovered Brain notes are archived in `sources/` with original paths and SHA256 hashes in `SOURCES.json`. Their status is recovered research evidence, not a claim that every historical checker was rerun during this planning task. Where a note points to a corrected or later source, the correction governs.

The agent strategy derivations that informed this report are retained in `supporting/`. Their alternative allocation tables are background proposals; `TEAMS.json` and the allocation appendix below define this report's proposed 100-role allocation; `NATIVE_MAPPING.md` preserves the live B-stream assignments and maps relevant roles to them. `SEED_LEMMAS.md` separates the new direct derivations from the completed manuscript. `DEPLOYMENT.json`, when present, records actual installation and readback; it is the operational evidence rather than a promise embedded in this narrative.

1. **Andrew Wan, John Wright and Chenggang Wu**, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*, ITCS 2014; [arXiv:1312.3003](https://arxiv.org/abs/1312.3003), [author-hosted full text](https://www.cs.cmu.edu/~jswright/papers/readk.pdf).
2. **Guy Shalev**, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, revised 24 January 2019; [arXiv:1806.03646v2](https://arxiv.org/abs/1806.03646v2).
3. **Ryan O'Donnell and Li-Yang Tan**, *A composition theorem for the Fourier Entropy-Influence conjecture*; [arXiv:1304.1347](https://arxiv.org/abs/1304.1347), [author-hosted full text](https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf).
4. **Srinivasan Arunachalam, Sourav Chakraborty, Michal Koucký, Nitin Saurabh and Ronald de Wolf**, *Improved bounds on Fourier entropy and Min-entropy*; [arXiv:1809.09819](https://arxiv.org/abs/1809.09819).
5. **González, MacManus and Pereyra**, *Further evidence towards the Fourier Entropy-Influence conjecture*, 2026; [arXiv:2606.00246v2](https://arxiv.org/abs/2606.00246v2).
6. **Nathan Keller, Elchanan Mossel and Tomer Schlank**, *A Note on the Entropy/Influence Conjecture*; [arXiv:1105.2651](https://arxiv.org/abs/1105.2651).
7. **Kelman, Kindler, Lifshitz, Minzer and Safra**, *Towards a Proof of the Fourier-Entropy Conjecture?*; [arXiv:1911.10579v2](https://arxiv.org/abs/1911.10579v2).
8. The withdrawal and attribution notice for the later related submission is at [arXiv:2512.03117](https://arxiv.org/abs/2512.03117). It is not counted as an additional theorem.

# Allocation appendix: the complete 100-role roster

This is the proposed topical allocation from `TEAMS.json`: twenty groups, each with five research roles. The scheduled coordinator is included in its team's five roles. Role labels identify mathematical responsibilities; they do not certify separate workers, concurrent capacity, completed work, or installed schedules.

The target and tracked metric below are the team's research contract. The live B-stream mapping is in `NATIVE_MAPPING.md`; groups may change methods in response to evidence while preserving the full-FEI objective.

## F01: Joint witness coding

**Target.** Construct normalized distributions describing each whole Fourier set with a controlled expected root and gate-label cost.

**Tracked metric.** Best proved expected total witness cost divided by influence, with the class and all residual terms stated.

- **F01.A:** Construct finite queue and forest codes.
- **F01.B:** Compare globally normalized mixtures of root odds.
- **F01.C:** Find label-cost obstructions on addressing and tribes.
- **F01.D:** Reconstruct normalization and Gibbs proofs independently.
- **F01.E:** Transfer a successful code to F02 and F03.

## F02: Correlated gate assignment

**Target.** Choose coordinate-to-gate assignments jointly so used-gate and overlap-congestion charges improve on coordinatewise read-number bounds.

**Tracked metric.** Proved bound for E[used-gate cost + allocation congestion] divided by influence on an explicitly defined class.

- **F02.A:** Develop correlated assignment rules.
- **F02.B:** Seek combinatorial dual certificates.
- **F02.C:** Optimize small exact assignment instances.
- **F02.D:** Prove or refute dimension-independent congestion bounds.
- **F02.E:** Connect assignment bounds to complete F01 witnesses.

## F03: Rare-root amortization

**Target.** Pay sparse-root rarity and scale-selection costs without replacing a necessary logarithm by a bounded local constant.

**Tracked metric.** Smallest rigorously bounded global rare-root residual per unit of consumed influence.

- **F03.A:** Build multiscale root priors.
- **F03.B:** Analyze activation and point-flip asymptotics.
- **F03.C:** Find reusable-budget violations.
- **F03.D:** Prove a non-reuse charging identity.
- **F03.E:** Combine the root bound with F01 normalization.

## F04: Rank-free references

**Target.** Replace dependence on the number of coordinate orders by a global spectral reference that uses Boolean structure.

**Tracked metric.** Dependence of the proved entropy coefficient on order count, width, or another explicitly defined structural parameter.

- **F04.A:** Construct references beyond total desirability orders.
- **F04.B:** Explore adaptive order mixtures.
- **F04.C:** Search functions forcing large rank cost.
- **F04.D:** Audit every mixture and normalizer.
- **F04.E:** Identify a route from structured references to unrestricted functions.

## F05: Restriction charge

**Target.** Bound the total actual entropy cost of a genuine physical restriction tree with one conserved influence budget.

**Tracked metric.** Proved cumulative restriction cost divided by consumed ordinary influence, including the leaf term.

- **F05.A:** Derive exact entropy-drop identities.
- **F05.B:** Design adaptive coordinate choices.
- **F05.C:** Test bent and rare bad-split examples.
- **F05.D:** Audit the influence telescoping identity.
- **F05.E:** Find a new restriction-closed class beyond the baseline.

## F06: Block stopping rules

**Target.** Find useful proper blocks or stopping rules controlling conditional block spectrum entropy while ending at certified leaves.

**Tracked metric.** Largest explicit family admitting a terminating block rule with a uniform conditional-entropy charge.

- **F06.A:** Choose physical blocks from dependence structure.
- **F06.B:** Combine blocks with threshold or affine leaves.
- **F06.C:** Construct parity-synergy failures.
- **F06.D:** Prove termination and budget non-reuse.
- **F06.E:** Compare block and singleton policies.

## F07: Erasure and synergy

**Target.** Exploit signed Boolean constraints to control erasure entropy or its downward logarithmic residual; retain high-order parity dependence.

**Tracked metric.** A new valid bound for the downward spectral-edge log functional with every residual explicitly identified.

- **F07.A:** Use Boolean convolution on spectral edges.
- **F07.B:** Search tensor-stable nonlinear potentials.
- **F07.C:** Stress-test parity and pair lifts.
- **F07.D:** Prove exact sign-sensitive inequalities.
- **F07.E:** Transfer a bound through the known erasure reduction without calling the reduction new.

## F08: Reveal correlation budget

**Target.** Verify and attack the decaying-threshold reveal-policy correlation integral in the current Brain, retaining the forced-information refund and separating entropy transfer.

**Tracked metric.** Best valid bound or counterexample for the exact weighted total-correlation integral after its definitions and source are pinned.

- **F08.A:** Reconstruct the reveal dynamics and admissibility.
- **F08.B:** Prove a drift inequality with the refund.
- **F08.C:** Find multiscale or parity counterexamples.
- **F08.D:** Certify the integration and boundary terms.
- **F08.E:** Determine exactly what additional entropy-transfer theorem would imply FEI.

## F09: Boolean convolution

**Target.** Use the exact signed XOR autocorrelation identities of Boolean spectra in a dimension-independent entropy estimate.

**Tracked metric.** Strongest proved entropy or downward-edge inequality under the full Boolean constraints, and sharp counterexamples to relaxations.

- **F09.A:** Develop algebraic identities from f squared equals one.
- **F09.B:** Search operator or Gram formulations.
- **F09.C:** Test relaxed non-Boolean spectral laws.
- **F09.D:** Derive exact certificates for candidate inequalities.
- **F09.E:** Connect the signed estimate to F07 or F04.

## F10: Decision-tree covariance

**Target.** Improve the dependence on read count for decision trees by controlling covariance or whole-path costs beyond the known square-root bound.

**Tracked metric.** Proved dependence on k in the read-k decision-tree entropy coefficient, with prior-art comparison.

- **F10.A:** Reconstruct the best known read-k proof.
- **F10.B:** Analyze covariance of overlapping paths.
- **F10.C:** Find hard read-k families.
- **F10.D:** Prove a logarithmic or sharper intermediate estimate.
- **F10.E:** Test whether the mechanism can escape the representation parameter.

## F11: Selector interference

**Target.** Extend selector closure beyond the proved fresh-selector, orthogonal-neighbor or uniformly positive-selector-energy cases, paying coherent interference explicitly.

**Tracked metric.** Largest class and smallest explicit interference penalty for which a strong selector inequality is proved.

- **F11.A:** Derive coefficient-level cross terms.
- **F11.B:** Search sign or orthogonality conditions.
- **F11.C:** Build cancellation and reinforcement examples.
- **F11.D:** Audit entropy and normalization under overlap.
- **F11.E:** Connect a valid interference budget to F12 or F14.

## F12: Two spectral addresses

**Target.** Reconstruct the Brain's conditional-product spectral-address results and settle the next two-address case with a valid constant; do not reuse the already refuted constant two.

**Tracked metric.** Best proved constant or exact obstruction for the precisely sourced two-address class.

- **F12.A:** Pin the exact conditional-product definitions.
- **F12.B:** Develop the two-address entropy identity.
- **F12.C:** Find asymptotic extremizers.
- **F12.D:** Prove the corrected constant independently.
- **F12.E:** Map which larger selector classes the result would cover.

## F13: Biased weighted thresholds

**Target.** Extend the strong product-measure entropy inequality from symmetric thresholds to genuinely weighted thresholds, with constants uniform in biases and arity.

**Tracked metric.** Largest weight class with a uniform corrected FEI-plus coefficient and explicit composition consequence.

- **F13.A:** Identify the weighted pivotal concentration obstruction.
- **F13.B:** Prove controlled-weight or few-weight cases.
- **F13.C:** Test rare biases and near-dictators.
- **F13.D:** Audit deterministic inputs and corrected entropy.
- **F13.E:** Transfer a valid gate theorem to read-once weighted-threshold formulas.

## F14: Shared-variable composition

**Target.** Develop entropy transfer for repeated selector variables or low-energy shared-data compositions beyond the new multiplexer closure, without assuming false product entropy subadditivity.

**Tracked metric.** Proved loss per overlap/depth parameter, or a normalized representation theorem that removes one parameter.

- **F14.A:** Derive exact shared-variable Fourier products.
- **F14.B:** Search cancellation-sensitive bounds.
- **F14.C:** Test known product-subadditivity counterexamples.
- **F14.D:** Prove a compositional invariant.
- **F14.E:** Connect the result to full-scope gate representations.

## F15: Sparse extremal structure

**Target.** Use activation-preserving reductions to identify additional structural hypotheses that genuinely simplify FEI; rarity or small influence alone is insufficient.

**Tracked metric.** A proved structural theorem or a new exact asymptotic H/I family that changes a live route.

- **F15.A:** Study balanced-core activations.
- **F15.B:** Compare high-entropy and low-influence reductions.
- **F15.C:** Construct sparse bent perturbations.
- **F15.D:** Certify asymptotic entropy-to-influence ratios.
- **F15.E:** Identify a non-equivalent restricted core class worth proving.

## F16: Exact finite search

**Target.** Search Boolean truth tables and structured families for violations of new intermediate inequalities, preserving physical influence and using certified logarithmic comparisons.

**Tracked metric.** New certified extremizer, smallest counterexample, or explicitly exhaustive new domain for a live candidate claim.

- **F16.A:** Implement exact integer Walsh transforms.
- **F16.B:** Prove safe symmetry reductions.
- **F16.C:** Search structured or SAT-encoded families.
- **F16.D:** Certify entropy comparisons with intervals.
- **F16.E:** Return minimal counterexamples to the proposing team.

## F17: Asymptotic stress families

**Target.** Turn promising finite obstructions into all-dimensional families and determine whether they refute a route, a fixed constant, or full FEI.

**Tracked metric.** A rigorously proved growth law for the targeted cost-to-influence ratio.

- **F17.A:** Analyze addressing and recursive selectors.
- **F17.B:** Analyze tribes and sparse activation.
- **F17.C:** Analyze parity, bent, and tensor constructions.
- **F17.D:** Prove limiting ratios and quantify all parameters.
- **F17.E:** Give every live route a matched asymptotic stress test.

## F18: Certified optimization

**Target.** Convert useful numerical patterns into symbolic inequalities, exact witnesses, or rigorous optimization certificates rather than enlarging brute-force checks without a theorem target.

**Tracked metric.** New certified parameter region, dual bound, or exact inequality directly feeding a full-FEI route.

- **F18.A:** Optimize finite witness assignments.
- **F18.B:** Search analytic potential coefficients.
- **F18.C:** Generate rational or interval certificates.
- **F18.D:** Reconstruct a dimension-free symbolic proof.
- **F18.E:** Measure whether the certificate resolves a previously unpaid term.

## F19: Independent proof reconstruction

**Target.** Independently reconstruct the strongest new candidate arguments, identify hidden hypotheses, and prove or refute their missing bridges; formalize only the parts where it reduces concrete risk.

**Tracked metric.** A repaired or refuted pivotal lemma, independently reconstructed full proof, or faithful checked formal core.

- **F19.A:** Rebuild proofs without using their conclusion.
- **F19.B:** Audit quantifiers and normalization.
- **F19.C:** Seek adversarial Boolean instances.
- **F19.D:** Formalize critical finite or induction steps where feasible.
- **F19.E:** Issue source-pinned mathematical reviews to F20.

## F20: Full-FEI synthesis

**Target.** Combine compatible proved ingredients into a dimension-independent FEI proof or a rigorous unbounded-ratio Boolean family; maintain the exact remaining gap and reallocate stalled work within FEI.

**Tracked metric.** Number and strength of genuinely unpaid universal obligations in the best complete proof outline, with a precise dependency graph.

- **F20.A:** Construct the global proof from accepted lemmas.
- **F20.B:** Audit whether reductions only rename full FEI.
- **F20.C:** Join successful ideas across teams.
- **F20.D:** Verify theorem-sized candidates with independent teams.
- **F20.E:** Maintain the campaign summary and authorized publication routing.

# Deployment evidence and the limits of this document

This report specifies the research plan and allocation. Actual native updates and their readback, observed worker execution, repository commits, independent mathematical review, and a complete solution are separate facts. A roster or configured prompt establishes none of the later facts.

`DEPLOYMENT.json` is the separate operational receipt. It must distinguish completed and verified actions from pending actions or failed attempts. The campaign endpoint remains 21 October 2026 at 19:15:57 UTC; creating or rebuilding this report does not restart or extend the ten-day window.

**Receipt available at assembly:** `DEPLOYMENT.json`, with SHA256 `b6f85582d8a4c9887b69b7348fdb113c63cb8dc7d028ea59a83dd1555d49bd23`. This fingerprint identifies the accompanying receipt; it does not independently verify every claim inside it. Consult that receipt and its readback evidence for the actual installation and save status.
