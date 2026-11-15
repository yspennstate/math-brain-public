# Bounded insertions: expansion, pattern comparison and ordered limits

This note checks the finite-insertion argument behind `reservoirInsertion_comparison` and `randomInsertion_comparison_tendsto`. It proves the logarithmic expansion and empirical-pattern estimate directly, and checks the change of reservoir law. The remaining regular-overlap concentration and depth-counting inputs are specified in Section 6. It does not prove the full Mézard–Parisi formula or certify a Lean build.

## 1. The positive tree expansion

Fix a finite conditional probability tower of depth d >= 1. At depth j its transition law is P_j(x | prefix), for j = 0,...,d-1. Allow zero transition probabilities. Let

\[
0=m_0<m_1\le\cdots\le m_d=1.
\]

Let f be a function of the complete path with |f| <= 1. For |t| < 1 define, backwards,

\[
A_d(t,y)=\log(1+t f(y)),\qquad
A_j(t,z)=\frac1{m_{j+1}}\log\sum_xP_j(x\mid z)
       e^{m_{j+1}A_{j+1}(t,zx)}.
\tag{1}
\]

All logarithm arguments are positive. These are finite sums and real analytic functions of t on (-1,1). Put

\[
K_j^t(x\mid z)=P_j(x\mid z)
 e^{m_{j+1}(A_{j+1}(t,zx)-A_j(t,z))},\qquad
g_t(y)=\frac{f(y)}{1+t f(y)}.
\]

The K_j^t are probability kernels. Differentiating the finite sums in (1) gives

\[
A'_j(t,z)=\sum_xK_j^t(x\mid z)A'_{j+1}(t,zx).
\tag{2}
\]

Thus A'_j is the conditional expectation of g_t along a fresh complete continuation from z.

A prescribed tree S has all leaves at depth d; every internal vertex has at least one child, and unary vertices are retained. Sample each child independently with the appropriate kernel K_j^t conditional on its ancestral prefix. For an internal vertex v at depth j with c_v children set

\[
\gamma_v=m_j-c_v m_{j+1}.
\]

Let U_S(t) be the expectation of the product of g_t at all leaves. Its derivative is

\[
U'_S(t)=\sum_{v\text{ internal}}\gamma_v U_{\operatorname{grow}(S,v)}(t),
\tag{3}
\]

where grow adds one independent unary continuation from v to depth d. In particular, it does not copy an existing sampled descendant.

To verify (3), for a nonzero-probability tree sample write its density as the product of K_j^t over its edges. An edge from depth j to j+1 contributes

\[
\partial_t\log K_j^t=m_{j+1}(A'_{j+1}-A'_j).
\]

At an internal vertex these terms collect into (m_j-c_vm_(j+1))A'_j. At the root the incoming term is absent, which agrees with m_0=0. At a terminal leaf the incoming contribution is m_d g_t=g_t. Differentiating its protected factor gives g'_t=-g_t^2. The incoming density contribution times that factor is +g_t^2, so they cancel, since m_d=1. This argument uses the product rule without dividing by g_t, so zero values of f cause no exception. What remains at v is the old leaf product times gamma_v A'_j. Equation (2) identifies that last conditional expectation with the added fresh branch, proving (3). Zero-probability transitions stay zero for all t and contribute zero to the finite derivative sum.

Write b for the number of leaves of S. Since m is nondecreasing, -gamma_v >= 0. Summing over vertices cancels the incoming and outgoing contributions at every internal vertex and leaves only the b terminal contributions and the root term. Consequently

\[
\sum_v(-\gamma_v)=b m_d-m_0=b.
\tag{4}
\]

Therefore adding a branch at v with probability -gamma_v/b defines a probability transition on trees. Start with a single unary path and make k such growth steps; call the resulting tree law Q_k. Every resulting tree has k+1 leaves. At t=0 all A_j vanish and the tilted kernels are the original P_j. Repeatedly applying (3), using the leaf counts 1,2,...,k, gives

\[
A_0^{(k+1)}(0)=(-1)^k k!\,
 \mathbb E_{Q_k}\mathbb E_S\prod_{b\in\operatorname{Leaf}(S)} f(y_b).
\tag{5}
\]

The first derivative is U_single by (2); the induction step multiplies the growth-law expectation by minus the current number of leaves, proving (5) including its factorial. Denote the last double expectation by c_k. Since |f| <= 1 and Q_k is a probability law, |c_k| <= 1. Also A_0(0)=0. Hence the Taylor series at zero is

\[
A_0(t)=\sum_{k\ge0}\frac{(-1)^k}{k+1}c_k t^{k+1},\qquad |t|<1.
\tag{6}
\]

Here equality on the whole interval needs justification. The coefficient bound gives convergence and real analyticity of the series on (-1,1). The finite recursion (1) is real analytic there and agrees with its Taylor series on a neighborhood of zero. The identity theorem for real analytic functions on an interval extends the equality throughout (-1,1). Thus this argument does not assume an unspecified Taylor neighborhood contains the eventual insertion radius.

The absolute remainder after K terms is at most

\[
T_K(t)=\sum_{k\ge0}\frac{|t|^{k+K+1}}{k+K+1}
\le\frac{|t|^{K+1}}{(K+1)(1-|t|)}.
\tag{7}
\]

The inequality follows by bounding each denominator below by K+1 and summing a geometric series. It proves summability and decay explicitly. The bound is independent of d, the positive exponents, the conditional kernels and the size of their finite alphabets.

## 2. Normalizing an arbitrary bounded insertion

Let |F| <= D with D >= 0. Set

\[
\rho=1-e^{-2D-1},\qquad f=\frac{e^{F-D}-1}{\rho}.
\]

Then 0 < rho < 1, and e^(F-D) lies in [e^(-2D),1]. Therefore |f| <= (1-e^(-2D))/rho <= 1 and

\[
F=D+\log(1+\rho f).
\tag{8}
\]

Positive power means commute with adding constants. Equations (6)-(8) consequently expand the tower insertion of F as D plus the series in (6) at t=rho. The radius, normalized insertion and coefficients agree with `QTopologyBound.lean`, `TreeSampling.lean` and `FiniteLogExpansion.lean`. D=0 is harmless: rho=1-e^(-1)>0 but f=0. The terminal exponent 1 is essential to (3); no assertion is made with a different terminal exponent.

## 3. The factor a in empirical-pattern replacement

Fix a tree with b leaves. After all its reservoir spin configurations have been sampled, let pi(e) be the empirical probability of the pattern e in {-1,1}^b at a uniform site. Set

\[
R_A=\sum_e\pi(e)\prod_{r\in A}e_r,
\qquad \bar\pi=\mathbb E\pi.
\]

Expectation includes both root disorder and tree samples. Walsh inversion follows by expanding the product of indicators:

\[
\pi(e)=2^{-b}\sum_{A\subseteq[b]}R_A\prod_{r\in A}e_r.
\]

Indeed, the kernel 2^(-b) sum_A product_(r in A)(e_r e'_r) equals product_r(1+e_r e'_r)/2, which is one when e=e' and zero otherwise. Subtract the formula for bar-pi. The empty-set coefficient cancels because both probabilities have mass one. Summing the triangle inequality over all 2^b patterns gives

\[
\sum_e|\pi(e)-\bar\pi(e)|
\le\sum_{\varnothing\ne A\subseteq[b]}|R_A-\mathbb E R_A|.
\tag{9}
\]

For a independent uniform site labels sampled with replacement, the conditional pattern law is pi tensor a. Expanding the difference of two product measures one coordinate at a time, and summing its absolute mass, gives

\[
\|\pi^{\otimes a}-\bar\pi^{\otimes a}\|_1
\le a\|\pi-\bar\pi\|_1.
\tag{10}
\]

Each term of the telescoping sum has one signed coordinate and a-1 probability coordinates; the latter have total mass one. Testing by any observable bounded by one costs at most the left side of (10). Averaging (9)-(10) proves the coefficient comparison

\[
|C_S^{\rm same}-C_S^{\rm independent}|
\le a\,\Delta(S),\qquad
\Delta(S)=\sum_{A\ne\varnothing}\mathbb E|R_A-\mathbb E R_A|.
\tag{11}
\]

There is no extra factor two: these formulas use absolute mass, which is twice the usual total variation distance. Independent insertion disorder can be conditioned on first because (11) is uniform in every observable bounded by one. Dependence on the reservoir would not permit that step. Coincidences among independently sampled site labels already occur in pi tensor a and require no collision correction.

Apply (11) with the observable product over the b leaves of f applied to the a spins. It is bounded by one. The independent-label tree law must have pattern mass bar-pi for every prescribed tree; that is the encoding input, not a consequence of (9). Using this input, (6) for both insertions, and (7) for their two remainders gives

\[
|I-J|\le 2T_K(\rho)+a\sum_{k<K}\frac{\rho^{k+1}}{k+1}
          \mathbb E_{Q_k}\Delta(S).
\tag{12}
\]

This is the displayed bound in `reservoirInsertion_comparison`, with b=k+1 in its k-th summand. The independent encoding uses a product tower with the same exponent vector, so the Q_k law in the two expansions is identical. Integrating independent physical disorder preserves (12), since its right side is independent of that disorder. Also |I|,|J| <= D by monotonicity of each normalized log mean, so their difference is at most 2D.

## 4. Changing the physical root to the reservoir root

The physical and reservoir root laws in `FiniteTowerPi.lean` differ only in the Poisson clause intensity:

\[
\lambda=\alpha N,\qquad r_N=\alpha N\left(\frac N{N+1}\right)^q,
\quad q=p-1.
\]

For N >= 1 and alpha > 0, r_N>0. Bernoulli's inequality gives

\[
0\le\lambda-r_N\le\alpha q,\qquad r_N\longrightarrow\infty.
\tag{13}
\]

For completeness, put x=1/(N+1); then (1-x)^q >= 1-qx, so lambda-r_N <= alpha N q/(N+1) <= alpha q. In particular r_N >= alpha(N-q), proving divergence.

For a bounded measurable test function |G| <= B of a marked Poisson sample, average all marks and other root variables conditional on the clause count. This gives a sequence G_n with |G_n| <= B independent of the Poisson parameter. For s>0 the derivative of its expectation is

\[
\frac d{ds}\sum_nG_n e^{-s}\frac{s^n}{n!}
=\mathbb E_s[G_X(X/s-1)].
\]

Termwise differentiation is justified on each compact positive s interval by the factorial tails, even after multiplication by n. Since E_s(X-s)^2=s, Cauchy–Schwarz bounds the derivative in absolute value by B/sqrt(s). Integrating from r_N to lambda yields

\[
|\mathbb E_\lambda G-\mathbb E_{r_N}G|
\le B d_N,\qquad d_N=\frac{\lambda-r_N}{\sqrt{r_N}}\longrightarrow0.
\tag{14}
\]

This checks the constant in `reservoirDistance` without invoking a coupling that would leave an O(1) edit error.

There is a separate check of (14). The affinity of Pois(lambda) and Pois(r_N) is the explicitly summed series

\[
A=\sum_{n\ge0}\sqrt{p_\lambda(n)p_{r_N}(n)}
 =\exp\left(-\frac{(\sqrt\lambda-\sqrt{r_N})^2}{2}\right).
\]

Cauchy–Schwarz applied to (sqrt(p)-sqrt(q))(sqrt(p)+sqrt(q)) gives absolute mass distance at most 2 sqrt(1-A^2). Since 1-e^(-x)<=x for x>=0, this is at most 2|sqrt(lambda)-sqrt(r_N)| = 2(lambda-r_N)/(sqrt(lambda)+sqrt(r_N)) <= d_N. Passing through the common conditional law of marks and other root variables does not increase this distance. Bounded tests therefore satisfy (14) with exactly the same constant.

Let X be any tree overlap in [-1,1], with its conditional tree law held fixed as a function of the root. Its means under the two root laws differ by at most d_N. The function E_tree |X-c| is bounded by two when |c|<=1. Changing the root law with the center fixed therefore costs at most 2d_N by (14); changing the center costs at most d_N by the reverse triangle inequality. Hence the two mean absolute deviations differ by at most 3d_N. There are 2^b-1 nonempty subsets of b leaves. Consequently

\[
|\Delta_\lambda(S)-\Delta_{r_N}(S)|
\le 3(2^b-1)d_N\le3\,2^b d_N.
\tag{15}
\]

Q_k is supported on b=k+1 leaves, so its averaged error is at most 3*2^(k+1)d_N. This tends to zero for each fixed k and each fixed depth as N tends to infinity. The estimate is uniform in perturbation parameters and the root-dependent tower, because (14) applies to arbitrary bounded test functions of the root. Thus size-dependent perturbation parameters cause no exception. This independently verifies the transfer in `reservoirShape_qExpect_difference_tendsto`.

## 5. Shape MAD and the ordered-limit step

Every subset overlap is in [-1,1], so each mean absolute deviation is at most two. Thus

\[
0\le\mathbb E_{Q_k}\Delta(S)\le 2(2^{k+1}-1)\le2^{k+2}.
\tag{16}
\]

For any centered real random variable Y and t>0, (|Y|-t)^2>=0 gives

\[
\mathbb E|Y|\le\frac{\mathbb EY^2}{2t}+\frac t2.
\tag{17}
\]

If a tree S has b leaves, each nonempty subset of its leaves induces a tree U with at most b leaves. Its overlap has exactly the same marginal law as that subset overlap: integrate out unselected branches in the product of conditional probability kernels; each removed branch has integral one. A nonnegative potential summing the variances of all depth assignments of all reduced trees with at most b leaves therefore dominates each such induced variance. Call this potential P_b(S). Summing (17) over subsets gives

\[
\mathbb E_{Q_k}\Delta(S)\le 2^{k+1}
 \left(\frac{\mathbb E_{Q_k}P_{k+1}(S)}{2t}+\frac t2\right).
\tag{18}
\]

This checks `physicalShapeDeviation_qExpect_le`. The coarse factor 2^(k+1) includes the empty subset with a nonnegative upper bound and is valid. At every fixed depth the potential is a finite sum of variances in [0,1], so it is bounded in system size.

Suppose its ordered limit vanishes, as asserted by the remaining input in Section 6. Take the fixed-depth size limsup in (18), then let depth tend to infinity with t fixed. The resulting upper bound is 2^(k+1)t/2. Finally let t decrease to zero. Equations (15)-(16) transfer the conclusion to reservoir shape errors:

\[
\lim_{L\to\infty}\limsup_n f_{k,L,n}=0,
\quad f_{k,L,n}=\mathbb E_{Q_k}\Delta_{\rm reservoir}(S).
\tag{19}
\]

Now put a_(L,n)=|I_(L,n)-J_(L,n)|, including the independent physical-disorder integrals if present. Equation (12), finite-sum limsup subadditivity and the boundedness in (16) give, for every fixed K,

\[
0\le\limsup_n a_{L,n}\le2T_K(\rho)+
 a\sum_{k<K}\frac{\rho^{k+1}}{k+1}\limsup_n f_{k,L,n}.
\tag{20}
\]

There are finitely many terms in this sum. With K fixed, let L tend to infinity using (19). The resulting limsup is at most 2T_K(rho). Finally let K tend to infinity and use (7). This proves the ordered-limit insertion conclusion conditional on (19). It never sums the exponentially growing bound (16) over all k: that would be invalid when 2rho >= 1. Instead K is fixed before the depth limit; this distinction is necessary at large D.

## 6. What remains assumed

The mathematical comparison just proved requires the independent-label encoding to match every prescribed-tree pattern law. `PhysicalInsertionComparison.lean` invokes `integral_independentInsertion_trialLog` for this fact, together with terminal interiority. This note uses the encoding as an input; it does not audit its complete construction.

For (19), `PhysicalSubtreeConcentration.lean` invokes `qSubtree_limsup_tendsto` in `TopologyDecay.lean`. Its hypotheses assert vanishing regular-depth averages of every fixed reduced-topology overlap variance. Its proof uses the finite-depth counting estimate

\[
\mathbb E_{Q_k}P_K(S)\le\sum_{U\in\mathcal T_K}c_{k,U}
 \left(\mathcal A_{L,\eta}\operatorname{Var}(R_U)
             +b_U(2\eta+4/L)\right),
\tag{21}
\]

where the topology set is finite and the nonnegative constants are independent of depth and system size. Given (21) and regular-variance decay, its limiting argument is valid: take the size limsup, then the depth limit with eta fixed, then eta down to zero. The ceiling estimate used there is valid because ceil(eta L)<=eta L+1 implies 2(ceil(eta L)+1)/L<=2eta+4/L. The combinatorial estimate (21) itself and the regular-variance decay are not proved in this note.

`PhysicalOverlapLimit.lean` obtains that regular-variance decay from `physicalShapeLimsup_tendsto`, the marker-defect identities in `FullShapeControl`, and `physicalOverlapAverage_le_marker`. Their source-level combination has the correct order of limits, but those concentration and marker estimates remain the next substantive boundary. In particular no conclusion here certifies that the selector establishes all these inputs for the physical model.

No gap was found in the finite logarithmic comparison, pattern replacement, Poisson-root transfer or ordered-limit passage checked above. These checks extend the earlier conditional outer reduction; they do not establish the unchecked concentration inputs or the whole theorem.
