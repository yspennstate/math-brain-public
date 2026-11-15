Overall verdict: SOUND

I found no error or missing load-bearing step in the theorem or its proof. In particular, the spanning-tree representation is valid for the reversed trajectory used here; the harmonic-sum martingale is exact; and the argument excluding boundary limits does not assume the conclusion it needs to prove. The coefficient of the rung limit is exactly $1-1/\ell$. Independent rational calculations and simulations support these conclusions. Two orientation conventions should be clarified, as specified in the corrections below.

This audit concerns the supplied `PAPER.tex`, with line numbers referring to that unmodified file. I use the result numbers in the request and give the source labels to identify them unambiguously. The source actually uses one shared theorem counter without a section reset: the quoted conjecture is numbered 1, the main theorem 2, the corollaries 3–4, the lemmas 5–12, and the remark 13.

No browsing, external writes, pushes, other agents, or visible windows were used. The authors' programs were read but neither run nor imported. External source papers are absent from the folder, so the accuracy of their quotations and theorem numbers cannot be independently authenticated in this audit. The uses of the classical spanning-tree and martingale results can nevertheless be checked mathematically, and are correct.

## Quoted Conjecture (`conj`, lines 56–59)

**ERROR as a universal mathematical assertion; this is the assertion the paper intentionally refutes.** On $G_2$, the theorem proved below gives $\chi_{uv}=\rho(1-\rho)/2>0$ almost surely, although every geodesic avoids $uv$. This is a counterexample even to the direction of the quoted conjecture that forbids linear growth on non-geodesic edges. It does not depend on how the other direction is interpreted. Whether these lines reproduce Kious–Mailler–Schapira's exact original wording is a separate citation question, discussed below.

## Theorem 1.1 (`thm:main`, lines 88–100; Section 4.5, lines 416–423) — SOUND

The path has exactly one nest edge and exactly one complete leg. Therefore $A_n+B_n=C_n+D_n=S_n=n+2$, and all the edges within each leg have identical weights at every time. Lemmas 4.1–4.3 give $a_n,c_n\to\rho\in(0,1)$; Lemma 4.5 gives the stated rung limit. Multiplication by $S_n/n\to1$ proves every edge limit in the theorem, including the zero rung limit when $\ell=1$.

The automorphism exchanging the legs preserves the initial weights and all transition probabilities. It exchanges the limiting variables $\rho$ and $1-\rho$, proving their equality in law.

The non-degeneracy argument uses more than a nonzero early fluctuation, and the additional step is valid. Lemma 4.2 implies that $A_n,B_n,C_n,D_n\to\infty$. Thus the four harmonic-number corrections in $M_n-r_n$ tend to Euler's constant with coefficients $1,-1,\ell,-\ell$, which cancel. Consequently $r_\infty=M_\infty$. The $L^2$ convergence gives $\mathbb E r_\infty=0$, and orthogonality of martingale increments gives

\[
\operatorname{Var}(r_\infty)=\mathbb E M_\infty^2
\ge \mathbb E(M_1-M_0)^2
=\frac{3\ell^3+3\ell^2+5\ell+1}{3\ell+1}>0.
\]

The displayed variance was computed independently from the four first-ant probabilities. Since $\rho$ is a strictly increasing function of $r_\infty$, it is not constant. No identification of its full distribution is claimed or needed.

## Corollary 1.2 (`cor:fail`, lines 102–109; proof 425–430) — SOUND

The distances are $d(N,F)=\ell+1$, while a simple path using the rung has $\ell+2$ edges. There are precisely two such non-geodesic paths, $\pi_3,\pi_4$. Since the rung starts at weight 1, the number of non-geodesic reinforced paths among the first $n$ ants is exactly $R_n-1$, not $R_n$. The proof uses the correct count.

For $\ell\ge2$, the limiting proportion is strictly positive almost surely because $\rho\in(0,1)$. For the probability concerning a single ant, the proof correctly checks convergence of the conditional probability, rather than inferring it from convergence of empirical proportions:

\[
\mathbb P(\gamma_{n+1}\text{ uses }uv\mid\mathcal F_n)
=h_n+\ell h_n(g_n-h_n)/Q_n\longrightarrow g^*.
\]

The random lower bound for $Q_n$ is positive on each sample path by Lemma 4.2. The conditional probabilities lie in $[0,1]$, so bounded convergence gives the unconditional probability limit. The shift from $n+1$ to $n$ has no effect. A bounded random variable positive almost surely has positive expectation, which supplies the strict final inequality.

## Corollary 1.3 (`cor:losange`, lines 111–114) — SOUND

Setting $\ell=1$ in the theorem gives the claimed paired geodesic limits and $\chi_{uv}=0$. The auxiliary identity $g=(a-c)^2$, used in discussing this case, is exact. The proof of the rung limit includes $g^*=0$, so the losange case is not being obtained by applying an argument that requires a positive limiting rung weight. The interpretation of this result as filling a particular gap in prior literature is conditional on the external citations being accurately described.

## Lemma 2.1 (`lem:ust`, lines 139–154) — SOUND

This is the critical step, and it uses the right direction. For each visited vertex $x\ne N$, let $\sigma_x$ be its first visit in the original walk. Its last occurrence in the reversed trajectory is at $K-\sigma_x$; its successor there is $X_{\sigma_x-1}=p(x)$. Moreover $\sigma_{p(x)}<\sigma_x$. Chronological loop erasure of the reversed trajectory therefore follows the first-entrance ancestry $F,p(F),p^2(F),\ldots,N$, without a cycle.

Continuing the original walk to cover the finite connected graph does not change any entrance edge of a previously visited vertex. The weighted Aldous–Broder construction gives a tree rooted at the original starting vertex $N$, with undirected tree probability proportional to the product of its conductances. No stationary initial distribution is required for this reversible weighted walk. Stopping originally at $F$ causes no conditioning of the completed tree: every trajectory is simply continued. The branch already exposed is the branch needed in the lemma.

The weights are positive and frozen during the ant, as required. Finite connectedness ensures almost sure hitting and cover times. These checks remove possible failures from zero weights, directed walks, or reinforcement during a walk; none occur in the stated process.

Independently of the spanning-tree theorem, I integrated all stopped-walk excursions exactly using rational linear algebra on visited subsets, keeping the first-entrance parents. For four fixed integer weight vectors on each of $G_1,G_2,G_3$, the resulting reversed-erasure law equals the separately enumerated tree law and Lemma 2.2. Two additional tests use unequal edge weights within the legs, outside the special hypothesis of Lemma 2.2, and also agree with the tree law. Details and every rational output appear below and in `independent_exact.out`.

The forward-erased walk has the same **distribution of edge sets**, by Wilson's algorithm rooted at $F$. I also calculated its probabilities independently by summing erased loops with killed Green functions; they agree exactly in all the tests. The two erasures need not coincide for a given trajectory. For example, on $G_1$, the walk

\[
N,u,v,N,v,u,F
\]

has forward loop erasure $N,v,u,F$, whereas reversal of its reverse-erased path is $N,u,F$. Thus time reversal matters pathwise, but does not change the weight-process transition law on the undirected weighted graphs in this paper. The transfer to the forward-loop-erased weight process in lines 156–163 is valid.

## Lemma 2.2 (`lem:law`, lines 181–202) — SOUND

The graph is a theta graph with three $u$-to-$v$ paths of lengths $1,2,2\ell$. A spanning tree is obtained by cutting two different paths once each. Cutting twice on the same path would leave a cycle in the other two paths and disconnect an intervening segment. The tree count is

\[
1\cdot2+1\cdot2\ell+2\cdot2\ell=2+6\ell.
\]

All eight deletion classes in lines 196–200 have the stated path and weight after division by $C^{\ell-1}D^{\ell-1}$. Collecting their contributions gives

\[
(m_1,m_2,m_3,m_4)=
(ACD+\ell ABC+\ell ARC,\ BCD+\ell ABD+\ell BRD,\ \ell ARD,\ \ell BRC).
\]

Their sum is exactly $CD(A+B)+\ell AB(C+D)+\ell R(A+B)(C+D)$. Independent symbolic enumeration confirms all four polynomials for $\ell=1,2,3,4,5$, with respectively $8,14,20,26,32$ trees. The combinatorial argument establishes the formula for every $\ell\ge1$; finite enumeration is a check, not the proof of the general claim.

The surrounding identities also hold: there are only four simple $N$-$F$ paths, each contains exactly one whole leg, and $S_n=n+2$. Substituting $A=aS,B=bS,C=cS,D=dS,R=hS$ in the denominator gives $S^3Q$, because $a+b=c+d=1$. There is no missing length factor in $Q$.

## Lemma 3.1 (`lem:drift`, lines 221–238) — SOUND

I independently obtained the five edge probabilities by summing the four path probabilities. After subtraction of the normalized weights, the three different drift coordinates are exactly

\[
f_a=\frac{\ell ab(c-a)}Q,\qquad
f_c=\frac{cd(a-c)}Q,\qquad
f_h=\frac{\ell h}{Q}\left(ad+bc-ab-\frac{cd}{\ell}-h\right).
\]

The complementary nest-edge and leg identities follow from probabilities summing to one. Every algebraic line in the proof has the correct sign and factor. Symbolic simplification gives zero residual for all five identities and for $q_1+q_2+q_3+q_4=1$.

The normalization bounds preceding the lemma are valid: $R_n\le n+1<S_n$, so $0<h_n<1$; $ab,cd\le1/4$; and

\[
\ell ab+cd\le Q\le\ell/4+1/4+\ell=(5\ell+1)/4.
\]

At $a=c=p$, $g=(1-1/\ell)p(1-p)$. For $a,c\in(0,1)$ and $h>0$, vanishing of $f_a,f_c$ forces $a=c$, and vanishing of $f_h$ then gives precisely the claimed equilibrium curve for $\ell\ge2$. Boundary zeros with $h=0$ are not being included in that assertion. At $\ell=1$, direct expansion gives $g=(a-c)^2$.

## Lemma 4.1 (`lem:mart`, lines 267–294) — SOUND

The preparatory harmonic-number statements in lines 246–257 are correct. With $\psi(k)=H_{k-1}$,

\[
0\le\psi(k)-\log k\le1,
\quad [\psi(k+1)-\log(k+1)]-[\psi(k)-\log k]
=1/k-\log(1+1/k)>0.
\]

The limit is Euler's constant. For a nondecreasing integer sequence with increments 0 or 1, each value $j$ contributes $1/j^2$ at most once at an increment, giving the stated $\pi^2/6$ bound even when the sequence has long holding times or eventually stops increasing.

The four possible exact increments of $M$, in path order, are

\[
\frac1A+\frac\ell C,\quad -\frac1B-\frac\ell D,\quad
\frac1A-\frac\ell D,\quad -\frac1B+\frac\ell C.
\]

Their conditional mean under the four probabilities is identically zero. This was checked symbolically as a rational identity; it is not a Taylor approximation to a logarithmic martingale. The four conditional harmonic increments displayed in lines 275–279 and their cancellation in line 283 are correct.

The square bound is also valid. Applied separately to $A,B$, the increment-counting bound gives $\sum U_n^2\le2\zeta(2)=\pi^2/3$, and similarly for $V_n$. Using $(U+\ell V)^2\le2U^2+2\ell^2V^2$ yields the deterministic bound $2(1+\ell^2)\pi^2/3$. At each finite $n$, martingale increments are square integrable and orthogonal, so

\[
\mathbb E M_n^2=\sum_{k<n}\mathbb E(\Delta M_k)^2
\le2(1+\ell^2)\pi^2/3.
\]

This justifies both almost sure and $L^2$ convergence. It does not merely appeal to pathwise square summability, which by itself would be inadequate.

Each harmonic correction in $M_n-r_n$ converges because its integer argument is nondecreasing, whether bounded or unbounded. Pairing the two corrections with coefficients $+1,-1$ gives a bound 1; pairing those with coefficients $+\ell,-\ell$ gives a bound $\ell$. Thus $|M_n-r_n|\le1+\ell$, not the looser bound obtained by treating four signs independently. This proves finite convergence of $r_n$ and the almost sure finiteness of $r^*$.

## Lemma 4.2 (`lem:away`, lines 298–335) — SOUND

The implication in lines 302–306 has the right direction. If $a>c$, then $r<(1+\ell)\logit a$. Combining this with $r\ge-r^*$ forces $a>\kappa$, where $\logit\kappa=-r^*/(1+\ell)$. Hence $a<\kappa$ implies $a\le c$.

For the centered increments of the $A$-harmonic process, conditional variance is at most $\mathbb E[I_{Nu}/A_n^2\mid\mathcal F_n]$. Tonelli and the pathwise increment-counting bound give a total unconditional variance at most $\pi^2/6$. Orthogonality then proves $L^2$ boundedness and convergence of $\mathcal N_n$, and a convergent real sequence has finite supremum of its absolute values.

Both $Y_n-1\le\log a_n\le Y_n$ and the inequality for $Y_{n+1}-Y_n$ are correct. In an excursion below $\kappa$, its drift term is nonnegative. Summing between the last exit $m$ and $n$ costs at most $2\mathcal N^*$ from the martingale. The single initial crossing costs at most $\log(1+1/S_m)\le\log(3/2)$, since $S_m\ge2$. Therefore the proof supplies the explicit positive pathwise bound

\[
a_n\ge\kappa\exp[-\log(3/2)-1-2\mathcal N^*]\quad\text{for every }n.
\]

The last exit need not be a stopping time. The proof uses only a pathwise bound on differences of a convergent martingale, not optional stopping. Likewise $\kappa$ may depend on the entire trajectory; it is only used in this pathwise excursion argument. Neither feature creates an anticipative martingale argument.

Symmetry gives a positive lower bound for $b_n$ on another event of probability one; intersecting these events is legitimate. With both $a_n,b_n$ bounded below, $\logit a_n$ is bounded. The identity $\ell\logit c_n=r_n-\logit a_n$ bounds $\logit c_n$ in both directions and hence bounds $c_n,d_n$ below. Taking the minimum of the four random bounds gives the common $\kappa_0>0$. No deterministic uniform lower bound, and no bound away from zero for the rung in this lemma, is claimed.

## Lemma 4.3 (`lem:delta`, lines 339–361) — SOUND

The normalized increment denominator is $S_n+1=n+3$, as written. Since $\xi=I_{Nu}-I_{u\text{-leg}}$, the exact drift calculation gives

\[
\mathbb E[\xi-\delta\mid\mathcal F_n]
=-\frac{\ell ab+cd}{Q}\delta=-\lambda_n\delta.
\]

The term $-\delta$ coming from normalization has been included. The bound $|\xi-\delta|\le2$ gives the second-moment remainder $4/(S_n+1)^2$. Robbins–Siegmund applies to the nonnegative adapted bounded sequence $\delta_n^2$, with zero multiplicative error, the nonnegative decrement $2\lambda_n\delta_n^2/(S_n+1)$, and a deterministic summable remainder. This proves convergence of $\delta_n^2$ and summability of the decrement.

Since $ab,cd\ge\kappa_0^2$ and $Q\le(5\ell+1)/4$, the stated lower bound

\[
\lambda_n\ge\frac{4(\ell+1)\kappa_0^2}{5\ell+1}>0
\]

is correct. A positive limiting value of $\delta_n^2$ would contradict the divergent harmonic sum. The limit is therefore zero. The compact interval obtained in Lemma 4.2 makes logit uniformly continuous; combining $a-c\to0$ with convergence of $\logit a+\ell\logit c$ yields the displayed logistic formula for $\rho$, including strict exclusion of 0 and 1.

## Lemma 4.4 (`lem:det`, lines 365–388) — SOUND

This is a deterministic convergence lemma. For any $\theta>g^*$, eventually $g_n\le(g^*+\theta)/2$, so while $x_n>\log\theta$, $u_n$ decreases by at least $\beta_n(\theta-g^*)/2$. If the process never returned below that threshold, divergence of $\sum\beta_n$ and boundedness of $\eta_n$ would force $x_n\to-\infty$, a contradiction.

After a last crossing from below, the first step increases $u$ by at most $2\beta_m\le\varepsilon$; subsequent steps above the threshold do not increase it. The difference between any two sufficiently late $\eta$'s is at most $\varepsilon$. These are exactly the two errors producing $2\varepsilon$ in line 380. The argument also covers indices that are already below the threshold. Taking limsup and then $\varepsilon\downarrow0,\theta\downarrow g^*$ gives the upper bound. If $g^*=0$, taking positive $\theta\downarrow0$ proves convergence of $e^{x_n}$ to zero without any lower bound for $x_n$.

For $g^*>0$, the threshold $0<\theta<g^*$ gives a strictly positive drift below $\log\theta$. The reversed last-exit argument has the same two errors and proves the lower bound. No monotonicity of $\eta_n$, summability of its increments, or monotonicity of $\beta_n$ is needed; convergence of $\eta_n$ is sufficient. The hypotheses in the statement cover every estimate in the proof.

## Lemma 4.5 (`lem:rung`, lines 390–414) — SOUND

The proof works with the harmonic logarithm of $R_n$ to avoid incorrectly inferring persistence from a positive interior drift. Dividing the rung inclusion probability by $R_n=h_nS_n$ gives exactly $1/S_n+\beta_n(g_n-h_n)$, with $\beta_n=\ell/(Q_nS_n)$. Its centered increment martingale has total expected squared increments at most $\zeta(2)$, by the same increment-counting argument used for $A_n$. This is valid even if $R_n$ were to remain bounded.

For $t\ge0$, $0\le t-\log(1+t)\le t^2/2$, so the $e_n$ sequence is nonnegative and summable. The harmonic correction $\varepsilon_n$ converges since $R_n$ is nondecreasing. The definitions in line 408 have the correct initial constant: telescoping gives $Y'_n=u_n+\mathcal N'_n+\sum_{k<n}e_k$, and hence $u_n+\eta_n=\log h_n$.

The rough bound $-1/2\le g_n\le1$ follows from $0\le ad+bc\le1$ and $0\le ab+cd/\ell\le1/2$. Together with $0<h_n<1$, it implies the required bound $|g_n-h_n|\le2$. Furthermore

\[
\frac{4\ell}{5\ell+1}\frac1{S_n}
\le\beta_n\le
\frac{\ell}{(\ell+1)\kappa_0^2}\frac1{S_n}.
\]

Thus $\beta_n\to0$ and $\sum\beta_n=\infty$. Lemma 4.3 gives $g_n\to(1-1/\ell)\rho(1-\rho)\ge0$. All hypotheses of Lemma 4.4 hold pathwise. This proves the rung limit for both $\ell=1$ and $\ell\ge2$, without assuming beforehand that $h_n$ stays away from zero.

## Section 5: numerical claims (lines 433–480) — SOUND within the stated numerical/heuristic scope

All 13 table rows agree with the corresponding supplied text outputs. Independently recomputing the prediction from each printed $a_n$ agrees within its rounding precision. The largest printed $|a_n-c_n|$ is $0.00021<0.0003$. The fixed-weight probability vectors agree with exact rational calculations; every quoted empirical coordinate is within 1.07 marginal standard errors of its exact probability at two million ants.

The local rung derivative at an interior equilibrium is indeed

\[
\left.\partial_h f_h\right|_{a=c=p,\ h=(1-1/\ell)p(1-p)}
=-\frac{1-1/\ell}{2},
\quad Q^*=2\ell p(1-p).
\]

The full Jacobian has a zero eigenvalue tangent to the equilibrium curve, a geodesic-difference eigenvalue $-(\ell+1)/(2\ell)$, and this rung eigenvalue: the first two drift coordinates have zero $h$-derivative on the diagonal, so the off-diagonal coupling into the rung does not change those eigenvalues. The paper calls the power law a suggestion from linearization, rather than a proved stochastic rate theorem. That qualification is appropriate; neither these simulations nor the proof establish a general asymptotic rate or distribution for the error.

From the printed $G_2$, seed 1 data I obtain residuals $0.0401398,0.0187023,0.0090083,0.0049874,0.0027934$, with final decade ratios $0.55365,0.56009$, close to $10^{-1/4}=0.56234$. The early ratios are smaller, so there is no exact power law throughout the displayed range. On $G_1$, seed 1, the reciprocal-rung increments per decade are $4.36354,4.36829,4.11999,4.42635$, consistent with the stated rounded range. The corresponding $\log(10)/Q_n$ values range from $4.20730$ to $4.39115$, approaching 4.4. The $\ell=1$ identity $f_h=h(\delta^2-h)/Q$ is exact; the reciprocal growth discussion neglects small/transient terms and is properly a heuristic.

My independent actual-walk simulations also agree with the asserted behavior; their endpoints and comparisons are given below. Positive finite-time rung fractions alone would not establish survival, and a small rung on $G_1$ would not establish extinction. The theorem is supported by the proof, not by those observations.

## Section 6: numbered remark (`remark`, lines 484–492) — SOUND

The two trees containing both complete legs have the rung deleted and one of $Nu,Nv$ deleted. Their total weight after removing the common leg factor is exactly $CD(A+B)$. The $\ell$ factors in the other deletion classes are correct. At $a=c=p\in(0,1)$,

\[
\lim_{h\downarrow0}\frac{q_3+q_4}{h}
=\frac{2\ell}{\ell+1}.
\]

This exceeds 1 precisely when $\ell\ge2$, as claimed. For $\ell=1$, it equals 1, and the nonlinear dilution term is essential. General weighted-tree path probabilities do give the mean drift for this process on any finite undirected graph. The open questions about general graphs are not used in any proof here.

## Citation audit

The mathematical use of Aldous–Broder is correct: first-entrance edges of a reversible conductance walk, continued to cover the graph, have the weighted tree law. The use of Wilson is correct: forward chronological loop erasure is its first branch rooted at $F$. The application of Robbins–Siegmund has the requisite nonnegativity, adaptedness, and summable error, as checked above. Nothing in this argument requires a general stochastic-approximation theorem or Borel–Cantelli; neither is invoked in the supplied proof.

The claims attributed to Kious–Mailler–Schapira, Armfield–Mailler, and the survey are internally consistent with the graph and the conclusions proved here. In particular, $G_1$ has distance 2 and a vanishing rung, whereas the counterexample $G_2$ has distance 3. Equal transition laws for the two erasure rules justify transferring a theorem that concerns the weights. The distinction between the uniform-geodesic, trace-reinforced, and loop-erased rules is maintained in the text. The other reinforced-walk papers are cited as background, not as supplying an omitted step of this proof.

However, those papers' contents are not supplied. I cannot certify the exact statement/number of Conjecture 1.1$1$, Theorems 1.3–1.4 of KMS, Theorem 1.1 of AM, the current status of an open problem, or bibliographic details of recent preprints from this folder alone. No such external-source verification is claimed. If the KMS conjecture is as quoted, its refutation follows from the checked mathematics. This limitation is not a gap in the supplied proof of the weight limits.

## Independent programs and exact outputs

All programs written and run for this audit are retained here:

| Program | Output | Purpose |
|---|---|---|
| `independent_exact.py` | `independent_exact.out` | Rational stopped-walk calculations, forward-erasure calculations, tree enumeration, symbolic drifts and martingale |
| `independent_sim.c` | `independent_sim.out`, `independent_sim_1e8.out` | Actual random walks, reversed-erasure reinforcement, two seeds for each of $G_2,G_3$ |
| `independent_data_audit.py` | `independent_data_audit.out` | All table rows, arithmetic predictions, frozen-weight numbers, decade increments, independent endpoints |
| `format_report.py` | `format_report.out` | Report math formatting and structural checks; no mathematical computation |

Reproduction commands, from this folder:

```sh
python3 independent_exact.py > independent_exact.out
cc -O2 -std=c11 independent_sim.c -o independent_sim
./independent_sim 10000000 > independent_sim.out
./independent_sim 100000000 > independent_sim_1e8.out
python3 independent_data_audit.py > independent_data_audit.out
```

The exact calculation took 0.409 seconds and recorded peak resident memory of 59,965,440 bytes. The full simulation took 57 seconds for all four $10^8$-ant runs combined, at nice priority 10, with a fixed 4,000,000-byte trajectory-validation buffer and small fixed graph arrays. The pilot took 6 seconds. Every mathematical computation ran in one worker with a timeout of at most 240 seconds; no calculation approached 1 GB. No author implementation was treated as an oracle.

### Exact walk probabilities

The exact reverse-walk calculation solves $(I-P_V)^Tz=e_s$ over the rationals for each visited set $V$ and current vertex $s$. Then $z_xP(x,y)$ is the probability that the next new vertex is reached through the entrance edge $x\to y$. Recursing through successive discoveries sums arbitrarily many steps inside the visited set without truncation. On first discovering $F$, the recorded ancestry gives the reverse-erased path. This computation never samples or assumes a spanning tree.

The forward calculation separately decomposes a walk according to the last departures at each vertex of a prescribed simple path. For $v_0=N,\ldots,v_k=F$, it multiplies $P(v_j,v_{j+1})G_{D_j}(v_j,v_j)$, where $D_j=V\setminus\{F,v_0,\ldots,v_{j-1}\}$. The diagonal killed Green function sums the loops before that last departure. These are rational linear solves, also independent of the tree law. A third calculation enumerates weighted spanning trees by edge subsets.

For every row below all four calculations—reverse walk, forward walk, tree enumeration, Lemma 2.2—agree exactly. Weight order is $(A,B,C,D,R)$; probability order is $(\pi_1,\pi_2,\pi_3,\pi_4)$.

| $\ell$ | Weights | Exact probability vector |
|---|---|---|
| 1 | $1,1,1,1,1$ | $3/8, 3/8, 1/8, 1/8$ |
| 1 | $2,3,1,4,2$ | $9/50, 3/5, 4/25, 3/50$ |
| 1 | $5,2,3,4,1$ | $15/29, 72/203, 20/203, 6/203$ |
| 1 | $1,17,13,2,9$ | $364/3153, 782/3153, 6/1051, 663/1051$ |
| 2 | $1,1,1,1,1$ | $5/14, 5/14, 1/7, 1/7$ |
| 2 | $2,3,1,4,2$ | $7/45, 3/5, 8/45, 1/15$ |
| 2 | $5,2,3,4,1$ | $75/161, 60/161, 20/161, 6/161$ |
| 2 | $1,17,13,2,9$ | $117/973, 187/973, 6/973, 663/973$ |
| 3 | $1,1,1,1,1$ | $7/20, 7/20, 3/20, 3/20$ |
| 3 | $2,3,1,4,2$ | $19/130, 3/5, 12/65, 9/130$ |
| 3 | $5,2,3,4,1$ | $65/147, 8/21, 20/147, 2/49$ |
| 3 | $1,17,13,2,9$ | $1040/8523, 1462/8523, 6/947, 663/947$ |

The heterogeneous-leg checks use nest weights $(2,3)$, rung weight 2, successive $u$-leg weights $(1,2)$ or $(1,2,3)$, and successive $v$-leg weights $(4,5)$ or $(4,5,6)$. The three applicable calculations agree at

\[
G_2:\ (65/362,105/181,30/181,27/362),
\qquad
G_3:\ (245/1326,125/221,110/663,37/442).
\]

Lemma 2.2 is not applied to these heterogeneous vectors. They test the more general statement of Lemma 2.1.

The symbolic output reports zero residuals for 16 identities, including all five drift identities, the exact martingale, the geodesic difference, the rung's harmonic drift, both diagonal identities, the equilibrium denominator, the rung derivative, and the small-rung amplification. All five symbolic spanning-tree enumerations pass. The output ends with `ALL EXACT CHECKS PASS`.

### Independent actual-walk simulations

The simulation generates individual steps with probabilities proportional to the integer edge weights, using a different pseudorandom generator from the supplied program and rejection sampling for bounded integers. It does not sample the four-path formula. During each walk it stores first-entrance parents, then increments the ancestor path from $F$ to $N$. As a separate implementation check, the first 10,000 ants in each run also store the full trajectory and literally loop-erase its reversal; all 40,000 comparisons pass. Forward and reverse erasures differ on respectively 1,052, 607, 283, and 1,275 of those same trajectories, demonstrating the pathwise distinction directly.

At $n=10^8$, using the paper's normalization $S_n=n+2$:

| $\ell$ | Seed | $a_n$ | $c_n$ | $h_n$ | $(1-1/\ell)a_n(1-a_n)$ | Residual |
|---|---|---|---|---|---|---|
| 2 | 2026111201 | 0.310621444 | 0.310656424 | 0.107222728 | 0.107067881 | +0.000154847 |
| 2 | 2026111202 | 0.105422748 | 0.105372958 | 0.048865539 | 0.047154396 | +0.001711143 |
| 3 | 2026111201 | 0.952004521 | 0.951995831 | 0.030598479 | 0.030461275 | +0.000137204 |
| 3 | 2026111202 | 0.206590876 | 0.206607836 | 0.110091388 | 0.109274057 | +0.000817331 |

The theorem uses $W/n$, while this table follows the paper's $W/(n+2)$. At $10^8$ ants the coordinate difference between these normalizations is less than $2\times10^{-8}$. Reading $\rho$ from either has no material numerical effect here.

For the second $G_2$ seed, the residuals at $10^4,\ldots,10^8$ ants are $0.020563049,0.010393144,0.005669020,0.003113864,0.001711143$. Their late ratios are about 0.55, consistent with slow decay at the predicted exponent. For the second $G_3$ seed the corresponding residuals are $0.020456197,0.008238010,0.004534888,0.001819780,0.000817331$. These are trends rather than exact rate fits.

In the authors' $10^8$-ant runs, the six $G_2$ residuals from the printed table are $+0.00279,+0.00017,-0.00002,+0.00450,+0.00268,+0.00207$; the two $G_3$ residuals are $+0.00058,+0.00075$. The independent residuals have comparable scale and shrink over time. The different geodesic fractions are expected from the random limiting $\rho$, so reproducing the authors' particular values of $a_n$ with unrelated seeds is not a requirement. Every independent run passes the common-leg-weight, nest/leg-sum, and rung-count invariants.

## Corrections and limits to retain

1. **Lines 165–168 and 211, and later events written $\gamma=\pi_i$: make orientation explicit.** The definition makes $\gamma$ an ordered $F$-to-$N$ path, whereas each $\pi_i$ is ordered from $N$ to $F$. Literally these ordered paths cannot be equal. Add, before the four-path probabilities: “We identify a simple path with its undirected edge set when specifying reinforcement events.” Alternatively, write $\gamma^{\leftarrow}=\pi_i$. All calculations in the proof already use the intended edge sets; no probability or conclusion changes.

2. **Lines 75–78, especially “the same random spanning tree”: distinguish equality in distribution from a coupling.** Use “a weighted random spanning tree with the same distribution” and, if needed, state that the two erasures can differ on the same walk. The example in the Lemma 2.1 section above shows why a pathwise interpretation is false. Lines 156–163 already make the equality-in-law interpretation substantially clear; this is a clarification of that interpretation, not a missing proof step.

3. **Lines 474–480: retain the heuristic qualification.** The derivative and reported arithmetic are correct. A general almost sure rate or limiting error distribution has not been proved here, and these sentences should continue to be phrased as a suggestion/approximation. No correction to the exponent or constant is needed.

4. **Lines 56–79 and 116–127: external attribution remains unverified in this closed-folder audit.** The referee should compare the original conjecture and cited theorem hypotheses with these passages before certifying priority and bibliography. There is no inconsistency visible in the supplied text and no demonstrated citation error to correct. The mathematical theorem proved in this manuscript does not rely on those attributions being exact.

There are no required mathematical repairs to the numbered theorem, corollaries, or lemmas. The first two items address genuinely ambiguous notation/wording; the last two record the scope of claims and checks rather than mathematical faults.

Task: “You are refereeing a mathematical paper that has been posted.” Audit date: 12 November 2026, Asia/Tbilisi. The user message's clock time is not exposed in this session, so no request time is invented.
