Overall verdict: SOUND

This verdict concerns the mathematical conclusions of the main theorem under (E1)–(E3). I found no counterexample or substantive gap in those conclusions. In particular, the normalisation argument does justify stochastic approximation without monotonicity of the attachment function. The extension to unbounded weights supplies the moment estimates and continuity that this requires; it does more than apply the bounded-operator argument formally.

There is an **ERROR in the simulation commentary**: the largest discrepancy is approximately 1.77, rather than 1.3, of the stated iid standard deviations. The displayed theoretical limits and the actual data agree with my independent calculations. This numerical correction does not change the theorem.

I read every result and proof in the four section files, including their extension in `sec_sublinear.tex`, and checked the definitions and comparisons in `PAPER.tex`. Standard analytic steps that I expand below are not classified as gaps merely because the authors abbreviate them. All verdicts below refer to the assumptions applicable to the result: the first three section files assume bounded weights; the final section replaces that assumption.

The source uses one global theorem counter, without section numbering. Thus its main theorem is Theorem 1, although the request calls it Theorem 1.1. I give both source numbers and labels, so the results can be identified without compiling the manuscript. Remarks and the example are included because they also contain mathematical assertions.

No external reference texts were supplied, and I did not browse. The citation assessment therefore distinguishes internal scope checks from verification of the cited documents. The Lean file was inspected as source; no Lean executable or local Mathlib build was available for kernel checking.

## Result 1 — Main theorem (`thm:main`): SOUND

Location: `PAPER.tex:104–120`.

**(i)** Nonexplosion follows from the global affine majorants furnished by (E3). Exponential killing gives the stated product tail, and the renewal argument in the last section constructs a positive solution with mean exactly $m$. Each product is strictly decreasing in its scalar argument, so there cannot be a second solution. The factors start at $j=0$, as required for an in-degree kernel.

**(ii)** The stochastic approximation and renewal argument prove almost sure convergence in $\ell^1$, including for non-monotone, unbounded weights. The deterministic mean bound puts the empirical measures in a compact set. Sublinearity makes the weight functional continuous on that set, which is the additional fact needed to pass from $\ell^1$ convergence to convergence of $S_n/n$. The separate degree second-moment bound gives the maximum-degree assertion in probability.

**(iii)** The embedding calculation identifies the one-root probabilities. The disjoint two-root calculation supplies the second moment; it is this calculation, rather than the one-root expectation alone, that gives convergence in probability of empirical ball frequencies. Tightness prevents loss of mass among increasingly large shapes. The limit is a locally finite infinite simple directed tree, with out-degree $m$ at every vertex. Its root degree law follows from either the degree-count theorem or the radius-one probabilities.

The model is consistently the sequential, updated model. The new vertex is excluded from all $m$ endpoint denominators. Mid-batch changes are explicitly estimated in the recursion and the tagged-process comparison. None of the arguments needs independence of the actual endpoints within a batch.

The claim about answering the survey problem is properly restricted to (E1)–(E3). Its attribution and problem number remain externally unverified; see the citation checks below.

## Result 2 — Limiting-tree description (`rem:tree`): SOUND

Location: `PAPER.tex:131–141`.

Given a child age $x$, the parent-age density integrates to one because

$$
\int_0^x \frac{h_\lambda(\log(x/y))}{cx}\,dy
=\frac1c\int_0^\infty e^{-u}h_\lambda(u)\,du
=\frac{s(p(c))}{c}=1.
$$

Distinct parents become independent conditional on the vertex's age. Their degree histories have the Palm weight $f$ at the prescribed child time. For a vertex reached from an older parent, one outgoing slot has already been specified and the other $m-1$ slots remain. For a vertex reached from a younger child, the forced incoming jump changes subsequent birth rates through the updated state. This last point must be read in the sense of the explicit processes in `eq:Phi`, not as adding one to an otherwise unchanged trajectory after the prescribed time.

The statement that the density is uniform only for constant $f$ is also correct. If $h_\lambda$ were constant, its derivatives at zero successively imply $f(1)=f(0), f(2)=f(0),\ldots$; the coefficient of the next new value is a nonzero product of positive birth rates. This argument applies under (E1)–(E3) as well: the finite-order derivatives involved are integrable under the linear growth majorant.

## Result 3 — Joint edge bound (`lem:edges`): SOUND

Location: `sec_apriori.tex:7–24`.

Every eligible weight is at least $\alpha$, and every target weight is at most $\beta$, including after earlier slots of the same new vertex. Thus $C/(t-1)$ bounds each conditional slot probability for every past history. Assigning distinct slots to repeated prescribed edges is necessary and is done correctly. There are at most $m^e$ assignments; when a younger endpoint would need more than $m$ slots, the event is impossible. Iterated conditioning proves the product bound without assuming independence. The second inequality uses $t-1\ge t/2$ only for $t\ge2$, which holds for every edge.

## Result 4 — Schur bound (`lem:schur`): SOUND

Location: `sec_apriori.tex:26–35`.

The two sums with $w_i=i^{-1/2}$ are bounded by $2w_i$ each, using decreasing-function integral comparisons. The weighted inequality for $2|x_ix_j|$, symmetry, and the spectral theorem for the finite symmetric matrix give its operator norm at most 4. Positivity of the matrix as an operator is unnecessary; the absolute quadratic-form bound is sufficient. The constant is uniform in $n$.

## Result 5 — Ball bounds and old vertices (`prop:balls`): SOUND

Location: `sec_apriori.tex:40–56`.

Use a simple path to witness each vertex at a given distance. Extending the sum over simple paths to all label sequences gives an upper bound, and the unrestricted sum is precisely $\mathbf1^T H^l\mathbf1_A$. Cauchy–Schwarz and the Schur bound give $B^l\sqrt{|A|/n}$. Taking $A=[n]$ bounds the mean size and taking $A=[K]$ bounds the probability of meeting old vertices. A union bound over path lengths is valid even when there are many witnesses. The $l=0$ term and $n=1$ cause no exception.

These are first-moment statements. Their use later for random proportions is through Markov's inequality, not an unjustified almost sure bound.

## Result 6 — No short cycles (`prop:cycles`): SOUND

Location: `sec_apriori.tex:58–74`.

An extra edge in a breadth-first tree, together with the two root paths, yields a connected rooted multigraph with equally many vertices and edges. It has at most $2r+1$ vertices. A second copy of a tree edge gives the same witness for a parallel edge. For fixed $r$ there are finitely many shapes, each contributing $n^v/n$ possible rooted labelings times an $O_{r,\varepsilon}(n^{-v})$ edge probability. The resulting $O_{r,\varepsilon}(n^{-1})$ bound is uniform over labels outside the cutoff.

It is essential to take $n\to\infty$ first and then $\varepsilon\downarrow0$; the proof does so. The old-vertex bound supplies the remaining error. No assertion about the total number of cycles throughout the graph is needed.

## Result 7 — Tightness and properties of subsequential limits (`cor:tight`): SOUND

Location: `sec_apriori.tex:76–89`.

The mean ball bounds permit thresholds $M_r$ with a summable total probability of exceeding them. Bounded out-degree bounds the number of edges when the vertex count is bounded, so only finitely many directed multigraph balls occur for each threshold. This proves tightness in the locally finite rooted-graph space.

Every outgoing edge from a vertex in $B_r$ is visible in $B_{r+1}$. The exceptional initial vertex is avoided with probability tending to one. Applying these facts for countably many radii proves that every vertex of a limit has out-degree $m$, not merely that the root does. Simplicity follows from Result 6. A finite tree cannot have $mv$ edges, so the limit is infinite. Compatibility of the limiting balls comes from taking limits in this rooted-graph space.

## Result 8 — Degree moments (`lem:degrees`): SOUND

Location: `sec_apriori.tex:91–110`.

The factorial second moment uses ordered pairs of distinct slots. Their joint probabilities satisfy the product bound by successive conditioning, even when they belong to the same batch. With $N=n-1$, the exact unscaled identity is

$$
\sum_i\left(\sum_{s=i}^{n-1}s^{-1}\right)^2
=\sum_{s,t=1}^{N}\frac{\min(s,t)}{st}
=2N-H_N.
$$

Also $\sum_i L_i=mC(n-1)$. These identities give the stated uniform second moment. Markov's inequality applied to the sum of degree squares gives the maximum-degree bound $O((\delta^2 n)^{-1})$.

The final uniform-integrability assertion is justified: the expected root in-degree is exactly $m(n-1)/n$, while its second moments are bounded. Consequently the root degree of every subsequential local limit has mean $m$.

## Result 9 — Scalar equation (`lem:scalar`): SOUND

Location: `sec_normal.tex:15–32`.

Memorylessness of the exponential killing time gives both the product tails and the mass recurrence, including the $k=0$ term. Under bounded weights the geometric tail majorant justifies summation, differentiation on compact scalar intervals if desired, and the first-moment identity

$$
dM(d)=m\sum_k f(k)p_k(d).
$$

Strict decrease, local uniform convergence of the series, the limit at infinity, and the finite-product lower bound at zero establish existence and uniqueness. The comparisons at $d=\alpha,\beta$ give the stated bracket for bounded $f$. The unbounded extension does not retain an undefined upper $\beta$: `sec_sublinear.tex:122–135` replaces that part of the proof and constructs the solution using the Laplace transform of $h$.

For general (E1)–(E3), choose a growth majorant with slope less than $d/m$ to show $M(d)<\infty$. Tonelli applied to the birth-process compensator proves the first-moment identity without a questionable boundary term in a weighted infinite recurrence. Exponential killing and nonexplosion still give the same product formula. Uniqueness follows from the same strict decrease.

## Result 10 — Normalisation and empirical degree law (`thm:normal`): SOUND

Location: `sec_normal.tex:34–173`; unbounded extension at `sec_sublinear.tex:75–144`.

The eligible count vector has $n$ vertices throughout the next $m$ slots. Each slot has conditional drift $QN/S$, and the new vertex contributes $e_0$ only afterwards. This gives the claimed recursion with a bounded count-valued martingale difference. In the bounded case, the within-batch drift error is $O(n^{-1})$ before multiplication by the step size.

The compact set $\mathcal K$ is valid: total in-degree is $m(n-1)$, its tail masses are bounded by $m/(J+1)$, and the first moment is lower semicontinuous. Bounded $f$ makes $F$ Lipschitz on probability measures. The noise lemma plus the summably small interpolation errors gives the finite-time tracking assertion by the ordinary integral Gronwall argument. Uniform attraction, rather than a claim that all equilibria are stable, then implies convergence of the actual iterates.

For unbounded weights, the authors correctly abandon this Lipschitz argument. On $\mathcal K$,

$$
\sup_{y\in\mathcal K}\sum_{k\ge J}f(k)y_k
\le m\sup_{k\ge J}f(k)/k\longrightarrow0.
$$

Thus $s,Q,F$ are uniformly continuous there, $\|F\|_1\le2+2m$, and the drift tails vanish uniformly. The recursion error is $O((b_n+1)/n)=o(1)$, where $b_n=\max_{k\le mn} f(k)=o(n)$. A merely vanishing error is sufficient on bounded intervals of the harmonic clock; its infinite sum need not converge.

The interpolated paths are uniformly Lipschitz: directly from a single graph update, $\|(n+1)(y_{n+1}-y_n)\|_1\le2m+2$. Compactness and equicontinuity produce uniform limits of shifted segments. Noise control and uniform continuity of $F$ show that each such limit solves the integral equation. Lemma 22 and uniform attraction apply to these solutions, yielding the contradiction in lines 137–144. This is a valid stochastic-approximation argument with a continuous, potentially non-Lipschitz drift. No monotone coupling or monotonicity of $f$ is hidden in it.

Finally, unbounded $s$ is continuous on $\mathcal K$, although it is not continuous on all of $\ell^1$. The proof uses precisely this restricted continuity.

## Result 11 — Noise lemma (`lem:noise`): SOUND

Location: `sec_normal.tex:74–92`; extension at `sec_sublinear.tex:89–91`.

Each coordinate's weighted martingale series has summable increment variances. Intersecting the corresponding probability-one events over the countably many coordinates is legitimate. Its tails control every finite set of coordinates uniformly over all later partial sums.

For the remaining coordinates, summing the recursion expresses the noise as endpoint measures minus drift and error sums. Both endpoint tails are uniformly small on $\mathcal K$. On a clock interval of length $T$, drift tails contribute $O_T(J^{-1})$ in the bounded case, and a quantity tending to zero uniformly in the unbounded case. The recursion error contributes $o(1)$. Letting $N\to\infty$, then $J\to\infty$, proves the asserted $\ell^1$ control. There is no appeal to an invalid general $\ell^1$-martingale convergence theorem.

## Result 12 — Flow representation (`lem:flowrep`): SOUND

Location: `sec_normal.tex:103–116`.

The mass derivative is $s(w)/m$. Dividing $w'=Aw$ by its mass gives

$$
z'=Qz+\frac{s(z)}m(e_0-z)=\frac{s(z)}mF(z).
$$

The clock has positive bounded speed, so the time change is global. Positivity and mass normalization keep the solution in probability vectors. On the weighted $\ell^1$ space the bounded-rate generator is bounded, permitting the first-moment calculation $\mu'=m-\mu$. Hence $\mathcal K$ is invariant. The definition of $A$ and the factor $1/m$ are correct.

## Result 13 — Uniform attraction (`prop:attract`): SOUND

Location: `sec_normal.tex:118–159`; extension at `sec_sublinear.tex:122–135`.

Variation of constants produces a scalar renewal equation for $\sigma=s(w)$. The density $\kappa=e^{-\gamma t}h(t)/m$ is positive, continuous, nonarithmetic, and has integral one, finite positive mean, and an exponentially integrable envelope. These are the conditions needed here for the key renewal theorem. Applying it to $\kappa$ itself gives the asserted limit of the renewal density $v$. The locally uniformly convergent convolution series first gives local boundedness; convergence at infinity then gives global boundedness.

Uniformity in the initial measure deserves checking. An explicit bound is

$$
\left|\tilde\sigma_y(t)-C_y\right|
\le |\tilde g_y(t)|
+\int_0^t |v(t-u)-\bar\mu^{-1}|G(u)\,du
+\bar\mu^{-1}\int_t^\infty G(u)\,du,
$$

where $G(u)=\beta e^{-\gamma u}$ in the bounded case and $G(u)=\varepsilon(m+a_\varepsilon)e^{-(\gamma-\varepsilon)u}$ in the unbounded case, with $\varepsilon<\gamma$. All three terms tend to zero independently of $y\in\mathcal K$. Also $C_y\ge\alpha/(\gamma\bar\mu)>0$, so normalizing the vector renewal limit is safe uniformly in $y$.

The vector convolution is handled with the integrable envelope $e^{-\gamma u}\|P_ue_0\|_1=e^{-\gamma u}$. It gives $z\to\gamma\mathcal R$ uniformly. The mean of this limit is $m$ by Tonelli and the defining Laplace-transform equation. It is exactly $p(m\gamma)$.

One minor directional imprecision: `sec_normal.tex:152` mentions the clock's *lower* speed bound when inferring convergence as $\tau\to\infty$. The relevant bound for this direction is its upper speed bound, $t(\tau)\ge m\tau/\beta$, which was already established. This is a reference to the wrong half of an available two-sided bound, not a missing estimate. The unbounded version explicitly uses the correct direction.

## Result 14 — Two-level example (`ex:two`): SOUND

Location: `sec_normal.tex:175–183`.

Substitution of $z=c/(c+ma)$ and $c=b+(a-b)z$ gives

$$
(a-b)z^2+(2b+ma-a)z-b=0.
$$

The constant term is negative and the value at 1 is $ma>0$; the derivative on $[0,1]$ is positive, since its minimum is at least $\min(2b+(m-1)a,(m+1)a)>0$. Thus there is exactly one root in $(0,1)$. The recurrence gives the stated geometric tail. At $m=2,a=1,b=2$, both radicals in the example are correct. Constant $f$ gives $c=f(0)$ and geometric ratio $m/(m+1)$.

## Result 15 — Local convergence theorem (`thm:localbdd`): SOUND

Location: `sec_local.tex:31–39,164–213`; extension at `sec_sublinear.tex:146–168`.

**Counting.** An actual ball contributes exactly $A(H)$ rooted isomorphisms. On the degree event, an edge received by an interior vertex cannot be repeated. If instead its sender is interior, all $m$ outgoing slots are already assigned to distinct prescribed targets. Every edge of the tree has an interior endpoint, so at most one slot assignment contributes. All incident edges of interior vertices are then fixed. The only possible discrepancy with an induced ball is an extra edge between boundary vertices. Its union bound is $O_\varepsilon(n^{-1})$ after division by the root factor, as claimed.

**Integration.** The convergence is uniform on sets of ages bounded away from zero and from coincidences. The remaining near-coincidence labelings form an $O(\delta+n^{-1})$ fraction, and the embedding bound controls them. Strictly, when invoking compactness within $(0,1)^V$, one can also discard the strip where an age exceeds $1-\delta$; that strip has $O(\delta+n^{-1})$ fraction and the same bound. Alternatively extend the tagged calculation continuously to terminal age 1. This is an ordinary endpoint detail of the stated Riemann-sum argument.

**Cutoff.** The probability of visiting an old label bounds the omitted contribution uniformly in $n$. The truncated integrals increase to the full nonnegative integral and are bounded by one, so integrability is proved rather than assumed. Tightness gives total mass one over the countable collection of shapes. An initial-vertex exception vanishes by the old-vertex estimate.

**Two roots.** Intersecting radius-$r$ balls imply distance at most $2r$, hence have probability at most $\mathbb E|B_{2r}|/n=O(n^{-1})$. For disjoint embeddings the forced-process proof applies to a forest and gives independent tagged limits, so its density factors. Edges between the two boundaries alter neither induced ball. Edges involving an interior vertex are excluded by its incoming-degree condition or its filled outgoing slots. These observations justify the product limit and therefore vanishing variance of each empirical shape frequency.

The last passage to all bounded functions of a fixed-radius ball uses the uniform expected tail of the ball size. It does not claim that convergence of a single mean proves convergence in probability. The unbounded joint edge and moment bounds supply exactly the same cutoff, counting, and two-root estimates with constants depending on the fixed shape/radius.

## Result 16 — Explicit factors (`prop:factors`): SOUND

Location: `sec_local.tex:43–68`.

For an interior target, final degree $k_i$ equals its number of forced incoming jumps. It must therefore have no unforced jump. Multiplying the waiting probabilities on the intervals between the forced times gives the displayed powers, and the likelihood factors at those jumps are $f(0),\ldots,f(k_i-1)$. A boundary leaf has at most one forced incoming jump. It gives factor 1 when there is no such jump, and gives $h_\lambda(\log(t_1/x_i))$ when there is one; subsequent behavior is unrestricted and integrates out.

Independence is independence of the limiting forced birth processes, not independence of edges of the finite graph. Under (E1)–(E3), $h_\lambda$ is finite on finite time intervals by the affine majorant, so these factors remain valid. The no-child radius-one star reduces to $p_0(c)$, with its $m!$ slot factor canceled by its automorphisms.

## Result 17 — Forced normalisation (`lem:forcedS`): SOUND

Location: `sec_local.tex:89–106`; extension at `sec_sublinear.tex:148–152`.

The likelihood identity `eq:com` is exact: at a forced slot one removes the original transition probability and restores it as a factor in the likelihood product. It holds for arbitrary nonnegative history functions and any positive kernel, with the eligible total weight evaluated immediately before that slot. I also checked it by exact enumeration; see below.

For bounded $f$, normalized endpoint distributions differ in total variation by at most $C\bar K/t$. At a disagreement at most two labels are added to the accumulated set. A finite number $e$ of forced slots and a discrete Gronwall product over $t\in[\varepsilon n/2,n]$ give a bounded expected discrepancy, uniformly in the labels and assignments. Taking the accumulated discrepancy through the entire interval controls the supremum in the statement. The weight discrepancy divided by $\varepsilon n$ then vanishes in $L^1$.

For unbounded weights it would be wrong to bound weight differences by the number of differing vertices. The authors replace this by a running upper bound on the degree-vector $\ell^1$ difference. Assumption (E2) gives the global estimate $\sum_i|f(D_i)-f(D_i')|\le L\sum_i|D_i-D_i'|$. The same finite-horizon coupling argument consequently works. Constants may diverge as $\varepsilon\downarrow0$; only fixed positive cutoffs are used in this lemma.

## Result 18 — Tagged degrees (`lem:tagged`): SOUND

Location: `sec_local.tex:108–144`; extension at `sec_sublinear.tex:154–158`.

At an unforced slot the true tagged increment is categorical. The discrepancy from independent Bernoulli increments consists of the normalization error and the $O(t^{-2})$ probability of simultaneous tagged successes. These errors sum to $o(1)$ over a fixed logarithmic age interval using the forced normalization lemma. Assigned slots are removed from all ordinary chains and produce their deterministic increments instead. Removing finitely many ordinary opportunities has vanishing effect.

The independent chains have one-batch rate $mf(k)/(ct)$, which becomes the birth rate $\lambda f(k)/u$ in age $u$. Multiple jumps within a batch have probability $O(t^{-2})$ in the bounded case. Birth-time and forced-time displacements cause only an $O(\delta/\varepsilon)$ error. At any fixed receiver there is at most one assigned incoming slot in a batch because the shape is simple and the labels are injective. Thus an earlier forced slot in that batch cannot spoil the final $O(n^{-1})$ pre-slot comparison.

For unbounded weights the comparison is stopped at degree $M$, so all constants are finite before stopping. Degree moments bound the stopping probability in the graph uniformly for labels above the cutoff. The limiting processes also have uniform finite moments on these age intervals by the same affine majorant, even with finitely many forced jumps. Let $n\to\infty$, then $M\to\infty$. This proves total variation convergence of the finite integer-valued observation vector. The statement does not claim total variation convergence of unobserved continuous jump times.

## Result 19 — Embedding probability (`prop:embed`): SOUND

Location: `sec_local.tex:146–162`; extension at `sec_sublinear.tex:160–164`.

The exact change of measure, the pre-slot normalization limit, and total variation convergence of the finite degree vector give the stated limit after multiplication by $n^e$. For bounded weights all likelihood factors are uniformly bounded when labels exceed $\varepsilon n$. The numerical constant $(4C/\varepsilon)^e$ is a valid loose bound.

For unbounded weights, applying Hölder to the squared product requires moments of order $2e$, not just $e$. The extension uses precisely $2e$. Together with the deterministic bound on $n/S^-$, this proves uniform integrability, permitting convergence of the likelihood expectation despite correlations between numerators and denominators. It also bounds the scaled embedding probabilities uniformly above the cutoff. Convergence along every convergent labeling sequence, continuity of the explicit limiting factors, and the finite set of slot assignments give uniformity on compact compatible age sets.

## Result 20 — Moments with forced slots (`lem:moments`): SOUND

Location: `sec_sublinear.tex:19–35`.

Sublinearity gives $f(k)\le\varepsilon(k+a)$ globally after increasing the intercept, without requiring a monotone kernel. For $Z=D_i+a$, the increment estimate

$$
(Z+1)^p-Z^p\le p(1+1/a)^{p-1}Z^{p-1}
$$

and the lower denominator $\alpha t$ give the factor $1+2p\varepsilon/(\alpha t)$ at an unassigned slot. Multiplication over $m$ slots and $\varepsilon=\alpha\theta/(2m)$ gives exponent $p\theta/t$. Each of the at most $q$ assigned slots contributes at most $(1+1/a)^p$, even if the assignment hits this vertex. The harmonic bound gives exactly the displayed $K(j/i)^{p\theta}$.

The constants depend on $p,q,\theta,f,m$, which is allowed. They are uniform over the locations of the forced slots and the observation moment. Applying the lemma to $i<n$, and treating the newest degree $D_n(n)=0$ separately, covers all vertices in the later summed bounds. Bounded increments are not used here.

## Result 21 — Sublinear joint edge bound (`lem:edges2`): SOUND

Location: `sec_sublinear.tex:37–71`, including its unnumbered Schur and degree consequences.

At a prescribed slot sent by label $j$, the denominator is at least $\alpha(j-1)\ge\alpha j/2$. The likelihood identity places all numerator moments under the same process with at most $e$ forced slots. Hölder with exponent $e$, followed by Result 20 with $p=q=e$, gives the factor $j^{\theta-1}i^{-\theta}$ for each prescribed edge. This works for repeated targets and repeated edges as well as for disjoint pairs. The case $e=0$ is trivial and need not use a zeroth Hölder exponent.

For the kernel $H_\theta$, both Schur sums are bounded by $i^{-1/2}/(1/2-\theta)$. This proves an operator norm bound uniform in $n$. For paths of length $l$, the edge constant is $K_l$; it need not be a fixed constant raised to $l$. Summing the finitely many lengths $l\le r$ still gives a finite $K_r$, sufficient for tightness and the old-vertex estimate.

For labels above $\varepsilon n$, a kernel factor is at most $1/(\varepsilon n)$: write it as $j^{-1}(j/i)^\theta\le1/i$. This recovers the unicyclic witness bound. Taking $\theta=1/4,p=2,q=0$ in the moment lemma gives

$$
\frac1n\sum_{i<n}\mathbb E D_i(n)^2
\le\frac{K}{\sqrt n}\sum_{i<n}i^{-1/2}\le2K.
$$

The same maximum-degree and uniform-integrability conclusions therefore hold. No uniform bound on individual attachment probabilities has been silently retained.

## Result 22 — Unbounded flow uniqueness (`lem:flow2`): SOUND

Location: `sec_sublinear.tex:93–144`, including its semigroup and attraction consequences.

The pure birth chain is nonexplosive: stop at a finite degree and apply the affine-majorant expectation bound, then send the stopping level to infinity. Its positive mass-preserving semigroup is strongly continuous on $\ell^1$ and on first-moment weighted $\ell^1$. A fixed finite time has a finite operator bound in the latter norm; uniform boundedness over all times is neither claimed nor required.

For finitely supported measures the generator identity holds. Since $Q$ is bounded from the first-moment space into $\ell^1$, density and the contraction bound extend the integral identity to every finite-mean initial measure. Such a measure belongs to the generator domain. The functions $g_y,h$ are continuous by weighted strong continuity and satisfy the subexponential bounds displayed in `eq:gh`.

For a solution taking values in $\mathcal K$, $Qy$ and $s(y)$ are continuous in time in the required norms, by the compact-set continuity estimate. Thus the product differentiation with $P_{t-u}$ is legitimate despite the unbounded generator. Applying the positive functional $s$ to variation of constants is justified by Tonelli for its positive integral; finite-mean bounds make the resulting quantities finite. The scalar Volterra equation has a unique locally bounded solution by iteration or the local Gronwall estimate, hence determines $w,z$, and the clock.

The tilted renewal equation then proves uniform attraction for all such solution segments. Its clock estimate is $t\ge m\tau/B_f$, where one fixes any finite bound $B_f=\varepsilon(m+a_\varepsilon)$ on $s(\mathcal K)$. The construction gives $\pi=p(m\gamma)$, mean $m$, and $s(\pi)=m\gamma$. Strict decrease of $M$ establishes uniqueness of $c_f$. The subsequent compactness proof only needs uniqueness and attraction of solutions arising as limits of shifted segments; there is no circular assumption that the empirical measures already converge.

## Independent checks: programs, methods, and outputs

### Programs and resource limits

All programs I ran are saved in this folder. No author program was executed or imported.

| Program | Purpose | Output |
|---|---|---|
| `referee_numerics.py` | 80-digit scalar solutions, 100-digit recomputation, product laws, tail bounds, ball integrals | `referee_theory.json`, `referee_numerics.out` |
| `referee_sim.c` | Independent vertex-weight Fenwick sampler; induced radius-one and radius-two ball counts | Executable `referee_sim`; per-run JSON files |
| `referee_run.py` | Sequentially run 14 graph simulations, two seeds for each main function and $m$ | `referee_simulations.json`, `referee_simulations.out`, `referee_sim_*_m*_s*.json` |
| `referee_checks.py` | Exact rational finite-history enumeration; full histogram comparisons; audit of supplied data | `referee_checks.out` |
| `referee_report_audit.py` | Report formatting and final cross-check of copied numerical values | `referee_report_audit.out` |

Reproduction commands, in this directory:

```sh
python3 referee_numerics.py > referee_numerics.out
cc -O2 -Wall -Wextra -o referee_sim referee_sim.c -lm
python3 referee_run.py > referee_simulations.out
python3 referee_checks.py > referee_checks.out
python3 referee_report_audit.py --check > referee_report_audit.out
```

The numerical script took 11.623 seconds. The 14 simulations took 13.277 seconds in total; each took 0.614–1.531 seconds. Reported maximum child RSS was 41,517,056 bytes, about 40 MiB. The rational/statistical script took 0.194 seconds. Programs have 240-second alarms; the runner allows only one simulation child at a time. Multiprecision work used a 30,000-element weight table and remained far below 1 GB. No visible windows, agents, pushes, or writes outside this directory were used.

### Scalar equation: 20-digit checks and means

The three main kernels were

$$
f_{\rm sqrt}(k)=\sqrt{k+1},\qquad
f_{\rm log}(k)=\log(k+2),\qquad
f_{\rm osc}(k)=\sqrt{k+1}+0.4(-1)^k.
$$

The last is genuinely non-monotone: its first values are $1.4,1.01421356\ldots,2.13205081\ldots,1.6,\ldots$. It is positive, has bounded increments, and is sublinear. The first two have the same required properties. I also calculated the paper's two-level rule and constant weights as controls.

| Kernel | $m$ | $c_f$ |
|---|---:|---:|
| sqrt | 2 | 1.56615793588614703496585887462 |
| sqrt | 3 | 1.76362867132520643954607871030 |
| log | 2 | 1.17452918181764039954324561477 |
| log | 3 | 1.31960613675772645520675382383 |
| oscillating | 2 | 1.62436015847691144178658636885 |
| oscillating | 3 | 1.80008505907094963631654903163 |
| two-level $1,2,2,\ldots$ | 2 | 1.56155281280883027491070492799 |
| two-level $1,2,2,\ldots$ | 3 | 1.64575131106459059050161575364 |
| constant 1 | 2 or 3 | 1 exactly |

Here is the beginning of each main law; the JSON gives $p_0,\ldots,p_{10}$ to 30 significant digits.

| Kernel | $m$ | $p_0$ | $p_1$ | $p_2$ | $p_3$ |
|---|---:|---:|---:|---:|---:|
| sqrt | 2 | .439172342909 | .199869765564 | .112383279750 | .069941799241 |
| sqrt | 3 | .370227990679 | .184920772905 | .112726590739 | .075447264722 |
| log | 2 | .458652914629 | .188574847002 | .104973121800 | .066246406420 |
| log | 3 | .388228192599 | .174912317379 | .105226539795 | .071182592688 |
| oscillating | 2 | .367140128808 | .281426834074 | .096944473075 | .085686198924 |
| oscillating | 3 | .300009923418 | .260192656862 | .096589778666 | .093605300734 |

The accuracy check controls the infinite tail, rather than stopping at a small term alone. All these functions satisfy the common global bound $f(k)\le(k+120)/20$. For sqrt and the oscillating rule this follows from $\sqrt{k+1}\le(k+1)/20+5$; for log, use its tangent line at $k+2=20$. Write $b=d/(m/20)>1$. If $R_K$ is the last included tail product, then

$$
\sum_{k>K}R_k(d)
\le R_K(d)\sum_{\ell\ge1}\frac{(K+120)_\ell}{(K+120+b)_\ell}
=R_K(d)\frac{K+120}{b-1}.
$$

The summation identity follows by the beta integral, or by telescoping rising-factorial ratios. For the six main calculations the script used 1,740–18,309 terms; the upper bounds on omitted $M$-tails were at most $1.71\times10^{-65}$. The omitted mass of the finite pmf is $R_K<10^{-68}$, and its omitted first moment is bounded by $KR_K+R_K(K+120)/(b-1)<2.1\times10^{-64}$. Summed masses and means equal 1 and $m$, respectively, to the 30 displayed significant digits. The recurrence residuals are about $10^{-81}$. The independently summed $\sum f(k)p_k$ equals $c_f$ to the displayed precision.

For each root, the script records the endpoints $c\pm10^{-24}$ and the scalar residual signs there. They are strictly positive at the lower endpoint and strictly negative at the upper endpoint, with magnitudes around $10^{-24}$, overwhelmingly larger than the tail bound. Repeating the finite series at 100 digits changes it by about $10^{-79}$. These are high-precision numerical brackets with analytic truncation bounds; the arithmetic itself is not a formal interval-arithmetic certificate. Twenty-digit accuracy is amply supported.

Uniqueness is analytic, not inferred from the solver: $R_1(d)$ and every other term strictly decrease, and the series is finite for all $d>0$. For instance, $M'(c_f)$ for the six main cases is approximately $-1.7582,-2.4704,-2.3535,-3.2329,-1.5905,-2.3132$, respectively; the full derivative values are in the JSON. Their negative signs are consistent with the strict-decrease proof.

### Independent graph simulation and degree comparisons

The C program samples directly from a tree of **vertex** weights, whereas the author's code samples degree classes and then vertices. After every sampled endpoint, it increments that endpoint's in-degree and changes its weight before the next draw. It inserts the new vertex only after its $m$ edges. Thus the implementation independently follows the defined model.

For the first 1,000 vertices in every run, every Fenwick choice was checked against a direct cumulative sum of all current eligible vertex weights using the same uniform random variate; all checks passed. Final total in-degree was exactly $m(n-1)$. The final $S_n$ was independently recomputed from the degree array. The largest discrepancy between the running weight total and a recomputed total at checkpoints was $4.52\times10^{-5}$ in an unnormalized sum of order $10^6$.

Every row below has $n=10^6$. Parentheses show signed error from the calculated limit. The $\ell^1$ error uses the complete empirical histogram and a 10,000-entry independently recomputed limiting law, including its tail beyond the largest observed degree.

| Kernel | $m$ | Seed | $S_n/n$ (error) | empirical $p_0$ | $\ell^1$ error | maximum degree |
|---|---:|---:|---:|---:|---:|---:|
| sqrt | 2 | 89 | 1.566173706 $+.0000158$ | .439394 | .0028698 | 101 |
| sqrt | 2 | 97 | 1.566007323 $−.0001506$ | .439382 | .0022513 | 117 |
| sqrt | 3 | 89 | 1.763613042 $−.0000156$ | .369943 | .0028631 | 166 |
| sqrt | 3 | 97 | 1.763503760 $−.0001249$ | .370409 | .0028435 | 184 |
| log | 2 | 89 | 1.174687355 $+.0001582$ | .458418 | .0020759 | 80 |
| log | 2 | 97 | 1.174321316 $−.0002079$ | .459202 | .0023845 | 89 |
| log | 3 | 89 | 1.319753197 $+.0001471$ | .388122 | .0030720 | 114 |
| log | 3 | 97 | 1.319443832 $−.0001623$ | .388142 | .0029940 | 128 |
| oscillating | 2 | 89 | 1.623874943 $−.0004852$ | .366881 | .0023431 | 97 |
| oscillating | 2 | 97 | 1.624435307 $+.0000751$ | .367405 | .0018710 | 111 |
| oscillating | 3 | 89 | 1.799681541 $−.0004035$ | .299507 | .0035204 | 155 |
| oscillating | 3 | 97 | 1.800247140 $+.0001621$ | .300231 | .0029289 | 179 |

The largest absolute discrepancy among $p_0,\ldots,p_3$ in these 12 runs was $0.00058368$, for the log rule at $m=3$, seed 97, degree 1. The largest $|S_n/n-c_f|$ was $0.00048522$, for the oscillating rule at $m=2$, seed 89. There is no systematic discrepancy apparent in two seeds; this is a finite-size check, not an empirical convergence-rate theorem.

The root in-degree distribution for a uniform root is exactly the empirical in-degree histogram conditional on the graph. I additionally sampled 100,000 uniform roots with replacement per run. For seed 89 their degree probabilities at 0 through 3 were:

| Kernel | $m$ | sampled root $p_0,p_1,p_2,p_3$ | sampled mean |
|---|---:|---|---:|
| sqrt | 2 | .43881, .19974, .11222, .06985 | 1.99533 |
| sqrt | 3 | .36951, .18585, .11169, .07631 | 3.00415 |
| log | 2 | .45808, .18812, .10629, .06726 | 1.98865 |
| log | 3 | .38904, .17358, .10476, .07104 | 2.99884 |
| oscillating | 2 | .36728, .28206, .09692, .08427 | 1.99773 |
| oscillating | 3 | .29852, .26189, .09596, .09366 | 2.99783 |

The graph-wide mean in-degrees are exactly 1.999998 and 2.999997. The extra root sample has its own sampling noise, as expected. All root samples and full histograms are saved.

### Three small induced balls

The program checks three shapes while preserving orientations and excluding extra edges between boundary vertices:

1. The radius-one star with root in-degree zero and $m$ distinct older parents. Its limit is $p_0$.
2. $H_0$: the radius-two ball with root in-degree zero, each parent having in-degree one, and all $m^2$ grandparents distinct. There are no additional induced edges.
3. $H_1$: the analogous radius-two tree with exactly one parent of in-degree two, its additional child a boundary leaf, and every other parent of in-degree one. Again all vertices are distinct and no additional induced edges occur.

The two radius-two probabilities can be independently integrated using just $a=f(0),b=f(1),d=f(2)$. Let

$$
A=\lambda a,\quad B=\lambda b,\quad D=\lambda d,\quad
u=\frac{a}{c(1+A)},\quad L_0=1+A+mB,\quad L_1=1+A+(m-1)B+D.
$$

Then

$$
P(H_0)=\frac{u^m}{L_0},\qquad
P(H_1)=m u^{m-1}\frac{\lambda ab}{c(1+A)}
\left[\frac1{(1+B)L_1}+\frac1{L_0L_1}\right].
$$

For a parent with no extra child, integration over its age gives $u x^B$, conditional on root age $x$. For a parent with one extra child, split that child's time before and after the root time. The two integrals give

$$
\frac{\lambda ab}{c(1+A)}
\left[\frac{x^D}{1+B}+\frac{x^B-x^D}{D-B}\right].
$$

Multiplying by the other parent factors and $x^A$, and integrating over $x$, yields the second formula. It remains continuous at $D=B$. This derivation is independent of the author's program and also checks the likelihood factor when a parent's earlier child precedes the forced root jump. The unconstrained boundary vertices integrate out with their normalized parent-age densities.

| Kernel | $m$ | $P(H_0)$ | seed 89 | seed 97 | $P(H_1)$ | seed 89 | seed 97 |
|---|---:|---:|---:|---:|---:|---:|---:|
| sqrt | 2 | .0133524705 | .013373 | .013207 | .0237410631 | .023509 | .023862 |
| sqrt | 3 | .0009327497 | .000968 | .000945 | .0025180554 | .002533 | .002486 |
| log | 2 | .0123720385 | .012305 | .012358 | .0221122758 | .022165 | .022297 |
| log | 3 | .0008422411 | .000863 | .000913 | .0022827970 | .002236 | .002415 |
| oscillating | 2 | .0191769445 | .019202 | .019375 | .0241145831 | .024257 | .024324 |
| oscillating | 3 | .0015115523 | .001564 | .001542 | .0030786590 | .003023 | .003137 |

The largest absolute radius-two discrepancy in these runs is $0.00023206$, for sqrt $H_1$, $m=2$, seed 89. Radius-one star frequencies differ from their empirical $p_0$ by only 1–35 vertices per million because of finite-graph parallel edges or edges between parents. Those excluded configurations are correctly not counted as the simple star.

The two-level control gave $S_n/n=1.561552000$, $p_0=.438448$, $H_0=.010668$, $H_1=.022782$. Its respective limits are $1.5615528128\ldots,.4384471872\ldots,.0106478453\ldots,.0226841245\ldots$. The constant-1 control gave $S_n/n=1$, $H_0=.015795$ versus $1/63=.0158730159\ldots$, and $H_1=.030219$ versus $40/1323=.0302343159\ldots$. The rational constant-kernel values also follow directly from Poisson incoming processes.

### Exact finite-history check of the forcing identity

`referee_checks.py` enumerates every ordered slot history for $n=6,m=2$, with the rational non-monotone kernel $f(k)=1+\tfrac12(-1)^k$. It compares the original process to the process forcing slot 1 of vertex 3 to vertex 1 and slot 2 of vertex 5 to vertex 3, using updated degrees in all probabilities. It checks both the constant history function and the indicator $D_1(6)=3$.

```text
original histories=14400, forced histories=1800
total probabilities original=1 forced=1
Psi=1: original=1307/11200; forced-weighted=1307/11200; difference=0
Psi=D_1(6)=3: original=1047/28028; forced-weighted=1047/28028; difference=0
finite E[D_U^2]=7102649/1287000 = 5.51876379176 (bound 78)
```

This finite check is not a substitute for the likelihood proof, but independently checks the model convention, the conditioning direction, and the pre-slot factors.

### Comparison with the paper's numbers: agreement, with one ERROR

The theoretical values in Table 1 agree at their printed precision. For sqrt at $m=2$, the author's stored scalar value is about $4.44\times10^{-15}$ below my value, consistent with the author's much earlier tail truncation. This has no effect on the five printed decimal places. The two-level scalar and degree probabilities agree to double precision. Its parent/child age-ratio mean is independently $0.445194101601104\ldots$, as printed. Its $H_0$ limit is $0.0106478452860825\ldots$, also as printed. The four supplied files agree with the displayed runs after rounding.

However, `PAPER.tex:210–212` contains a false maximum-discrepancy statement. In `data/sim_1e6_s22.json`, the observed sqrt $p_2$ is .112943 and the limit is .1123832797497645. The absolute difference is .0005597202502355. The stated iid standard-deviation scale is

$$
\sqrt{.1123832797497645(1-.1123832797497645)/10^6}
\approx .00031584,
$$

giving a ratio **1.772178369**, exceeding 1.3. Even using only the rounded table entry .11294 gives about 1.76. The two-level $H_0$ discrepancy in run 1 gives 1.307177, which appears to be the origin of 1.3, but it is not the largest discrepancy across the table.

The iid expression is described as a hypothetical independence scale. It is not a proved standard error for preferential-attachment empirical counts, which are dependent. Thus the appropriate correction is a descriptive statement about this scale, without presenting it as a calibrated test of the limit theorem.

### Lean scope and verification status

File inspected: `lean/P0089_Finite.lean`, all 221 lines. `PAPER.tex` contains no explicit claim that Lean proves the main theorem. The file's own header describes three finite algebraic pieces, and its theorem statements have that limited scope.

| Lean statements | What is established in the source | Scope limitation |
|---|---|---|
| `sum_L`, `sum_L_sq`, `sum_min_eq`, `sum_L_sq_eq`, `sum_L_sq_le` | Shifted harmonic-sum identities and their bound, for all finite $N$ | They do not formalize conditional edge bounds or random degree moments |
| `l1_normalise` | The finite normalized-weight $\ell^1$ inequality used in the coupling | It does not construct or estimate the stochastic coupling |
| `two_levels` | The radical quadratic root, its interval, the scalar relation, geometric ratio bounds, and rational expressions for mass and mean | There is no probability law or infinite `tsum` of the pmf in the statement; interpreting the two rational expressions as mass and mean uses the usual geometric-series formulas |

The index shift is correct: `L N i` sums $1/(s+1)$ for integers $i\le s<N$, with $N=n-1$ and $i=0,\ldots,N$. I independently derived $\sum L=N$ and $\sum L^2=2N-H_N$. The normalized-weight inequality follows from adding and subtracting $w'/W$ and $|W-W'|\le\sum|w-w'|$. The radical identities in `two_levels` reduce to $c^2+c=4$, $z(c+2)=c$, and $z=2-c$, exactly as the file indicates.

I found no `sorry`, `admit`, or declared auxiliary axiom. The final `#print axioms` commands request diagnostics; their output is not supplied. Source inspection is not a kernel-compilation result, and I do not certify that this file elaborates against an unspecified Mathlib version. No installed `lean` was found on PATH or in the usual user elan location, and the supplied folder contains no pinned Lean/Mathlib project or build log. Even a successful compilation would establish only these finite identities, not (i)–(iii), renewal theory, stochastic approximation, or local convergence.

### Citation and model-scope checks

These are checks against the manuscript's descriptions and the mathematics used in its proofs. I could not inspect the external papers or survey, so exact theorem hypotheses, historical priority, bibliography metadata, the number “24,” and the claimed survey attribution are not independently certified here.

| Reference | Use in the manuscript | Assessment from the supplied text |
|---|---|---|
| Aletti et al.; Deijfen and van der Hofstad | Open problem for non-affine fixed-out-degree local limits | The result addresses precisely the described model and advertises the restriction to (E1)–(E3). Verify the actual problem wording and numbering against the survey before relying on the priority claim. Deijfen and van der Hofstad are credited as contributors of the problem, rather than cited as proving the requested theorem. |
| CSV | Related degree-count LLN, a fluid limit, and a similar time change for a different edge-addition model | The manuscript explicitly distinguishes its fixed-$m$ model. It proves its own normalization, drift control, and attraction rather than importing CSV's conclusion for an unmatched model. The claim about CSV's remark on bounded numbers of edges requires the external text to verify. |
| KRL and KR | Product degree law for sublinear attachment in the $m=1$ setting | The degree-index convention needs clarification at `PAPER.tex:61–63`: the standard positive-degree power kernel translates to $f(k)=(k+1)^a$ when $k$ denotes in-degree here. Literally $f(k)=k^a$ at in-degree zero violates this paper's model and assumptions. The product formula with the proper shift is consistent. |
| RTV | Continuous-time branching embedding and degree/local limits for $m=1$ | The $m=1$ comparison is appropriate for kernels satisfying the required branching-process hypotheses. The phrase “for every $f$” should be restricted or explained: arbitrary positive kernels can produce explosive continuous-time branching processes, so unrestricted existence and limit claims would be false. No RTV theorem is used to shortcut the proof for $m\ge2$. |
| Feller, Chapter XI | Key renewal theorem in Result 13 and its extension | This is the one named external theorem carrying a proof step. The density is nonarithmetic; the input is directly Riemann integrable; its mean is finite and positive. Those hypotheses are checked, and applying the theorem to $\kappa$ gives the desired renewal-density limit. Exact edition/page verification is unavailable. |
| Benaïm; Pemantle | Stochastic-approximation context | The proof gives its own noise control, tracking/compactness argument, and attraction proof. It does not depend on an unspecified finite-dimensional stochastic-approximation theorem applying automatically in $\ell^1$. |
| BA; BRST; BBCS; GHHR; Lo; van der Hofstad vol. 2 | Affine models, degree sequence, and local-limit background | The statement “a version” and the references to extensions signal convention differences. These results are not used to prove the non-affine assertions. An exact equivalence with a particular affine model is not established or needed. |
| Dereich–Mörters | Concave kernels in a different model with random outgoing degree | The manuscript explicitly distinguishes independent per-target connections from its sequential fixed-$m$ model; no transfer of their theorem is attempted. The detailed historical scope cannot be checked without those papers. |
| Banerjee–Deka–Olvera-Cravioto | Collapsed branching-process local limits | The collapse model is correctly separated in the text. In general a sum of nonlinear constituent weights is not a function solely of the collapsed degree; an affine kernel has that property for a fixed number of constituents. This observation prevents treating their result as automatically solving this paper's model. Exact scope of their external theorem remains unverified. |
| Aldous–Steele; Benjamini–Schramm; Garavaglia–van der Hofstad–Litvak | Definitions and context for local convergence | The manuscript states the convergence notion it actually proves and keeps orientations in balls. There is no load-bearing theorem imported from these sources with unchecked hypotheses. |

The citations to the Brain software/project concern provenance, not proof. Funding and provenance statements were outside the mathematical audit.

## Corrections and precise locations

1. **Required numerical correction — `PAPER.tex:210–212`.** Replace the false “largest is 1.3” statement by approximately 1.8 of the stated hypothetical iid scale, or omit the maximum claim. The exact maximum in the supplied degree/ball data is 1.772178369 for sqrt $p_2$, run 4 (`data/sim_1e6_s22.json`). Keep the qualification that independence is hypothetical; a valid PA sampling standard error has not been proved here.

2. **Degree-convention clarification — `PAPER.tex:61–63`.** Specify that the power $k^a$ in the older $m=1$ literature is indexed by positive total degree, or write the translated in-degree kernel $(k+1)^a$. With this paper's index, $k^a$ would give $f(0)=0$ and fail to define the stated initial attachment step.

3. **Branching-process qualifier — `PAPER.tex:63–65`.** Qualify “for every $f$” by the nonexplosion and Malthusian/integrability hypotheses needed for a continuing branching process and the cited limit results. For example, a single individual with rates $f(k)=(k+1)^2$ has a finite sum of expected holding times and infinitely many children in finite time. A stopped finite-prefix embedding is a different assertion from an unrestricted nonexplosive embedding and limit theorem. Under this paper's (E1)–(E3), the required nonexplosion estimate is already provided later.

4. **Clock-reference correction — `sec_normal.tex:152–153`.** In the inference from $t\to\infty$ to $\tau\to\infty$, cite $d\tau/dt\le\beta/m$, equivalently $t(\tau)\ge m\tau/\beta$. The cited lower bound is the wrong direction for that inference, although both bounds are available in Lemma 12.

5. **Optional proof precision — `sec_local.tex:187–190`.** To make the Riemann-sum compactness statement literally use compact subsets of the declared open age domain, also remove the terminal strip $x_i>1-\delta$, then let $\delta\downarrow0$. Its contribution is $O_\varepsilon(\delta+n^{-1})$ by Proposition 19. Extending the convergence statement to age 1 is an equivalent fix. This endpoint bookkeeping does not affect the theorem.

6. **Formal-verification wording if added — `lean/P0089_Finite.lean:13–15,165–174`.** Describe `two_levels` as checking the closed-form geometric mass/mean expressions. A claim that it formalizes the probability law, its infinite sums, or the main theorem would exceed its statement. A reproducible formal-verification claim would also need a pinned Lean/Mathlib environment and successful kernel-check output. The present manuscript makes no such main-theorem claim.

Task: “You are refereeing a mathematical paper that has been posted” — run started 12 November 2026, 18:50 Asia/Tbilisi, as recorded in the local launch log.
