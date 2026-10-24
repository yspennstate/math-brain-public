# FEI progress: arbitrary quadratic twists of symmetric cores

20 September 2026. Owner-requested research continuation by ChatGPT (GPT-6 Astra Pro).

**Full Friedgut–Kalai Fourier entropy–influence conjecture: NOT PROVED in this continuation.** The positive results below are all-dimensional theorems for explicitly stated classes. Their proofs use the published O'Donnell–Wright–Zhou symmetric-function theorem. The new arguments are supplied in full; no independent review, formal verification, or publication-priority clearance is claimed.

## 1. Main results

Use the uniform cube `F_2^n`, and take entropy in bits. A sign function is Boolean when its values are in `{−1,+1}`. Define

\[
\widehat f(S)=2^{-n}\sum_x f(x)(-1)^{\sum_{i\in S}x_i},\quad
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},
\]
\[
\alpha_i(f)=\Pr[f(x)\ne f(x+e_i)],\quad
j_i(f)=\min\{\alpha_i(f),1-\alpha_i(f)\},\quad
I(f)=\sum_i\alpha_i(f),\quad J(f)=\sum_i j_i(f).
\]

Terms of mass zero contribute zero. A function is **d-part-symmetric** with respect to a partition `V_1,...,V_d` when it depends only on the `d` block Hamming weights. Parts are nonempty unless they arise from restriction, in which case empty parts are discarded.

**Theorem A (constant-preserving quadratic twisting).** Let `h` be any d-part-symmetric Boolean function. Let `Q` be any polynomial of degree at most two over `F_2`, using any of the same coordinates. Then

\[
\boxed{H((-1)^Qh)\le(12.04+\log_2 d)J((-1)^Qh)
\le(12.04+\log_2 d)I((-1)^Qh).}
\tag{1.1}
\]

There are no restrictions on the rank, graph, density, or cross-part interactions of `Q`; its linear and constant terms are also arbitrary. In particular, **an arbitrary quadratic twist of a fully symmetric Boolean function satisfies FEI with constant 12.04**, even when the resulting function is not symmetric.

The proof yields more than (1.1). Call coordinate `i` mixed if the neighbor set of `i` in the quadratic interaction graph contains some, but not all, of the other coordinates of at least one symmetry part. If `E` is the set of mixed coordinates and `C_d=12.04+log_2 d`, then

\[
\boxed{H((-1)^Qh)\le C_dJ((-1)^Qh)-(C_d/4-2)|E|.}
\tag{1.2}
\]

**Theorem B (arbitrarily many independent cores, arbitrarily coupled quadratically).** Partition the physical coordinates into disjoint groups `U_1,...,U_m`. For each `t`, let `h_t(x_{U_t})` be any `d_t`-part-symmetric Boolean function on that group. For arbitrary quadratic `Q` on all coordinates, put

\[
F(x)=(-1)^{Q(x)}\prod_{t=1}^m h_t(x_{U_t}),\qquad d_*:=\max_t d_t.
\]

Then

\[
\boxed{H(F)\le(12.04+\log_2 d_*)J(F)
\le(12.04+\log_2 d_*)I(F).}
\tag{1.3}
\]

Thus the constant does not grow with the number of independent cores. In particular, products of arbitrarily many symmetric Boolean functions, with completely unrestricted quadratic interactions within and between their blocks, have the single constant **12.04**.

The independence here means that the cores use disjoint physical coordinate groups. The final function `F` need not factor over those groups. Arbitrary dependence of the cores through overlapping input groups is **not** admitted. Nor do these proofs establish the bound with minimum influence over arbitrary invertible linear changes of input coordinates.

### A concrete high-degree example

For any `k<=n`, the function

\[
h(x)=(-1)^{\sum_{A\subseteq[n],\,|A|=k}\prod_{i\in A}x_i}
=(-1)^{\binom{|x|}{k}\bmod2}
\]

is symmetric. Its high-degree terms can overlap extensively. Theorem A permits multiplication by any quadratic phase, with the same constant 12.04, without expressing those high-degree terms as independent clauses. This is an example of the hypotheses, not a claim that all alternative representations under earlier theorems have been excluded.

## 2. Published input and elementary preliminaries

The input from O'Donnell, Wright and Zhou [OWZ11, Theorems 1–2] is

\[
H(u)\le C_d I(u),\qquad C_d=12.04+\log_2 d,
\tag{2.1}
\]

for d-part-symmetric Boolean `u`. Their constants and symmetry classes are not new results of this continuation.

### 2.1 The same published bound with folded influence

Multiplication by a character `chi_A(x)=(-1)^{sum_{i in A}x_i}` translates the Fourier spectrum by symmetric difference with `A`. It preserves `H` and `J`, and replaces `alpha_i` by `1-alpha_i` precisely when `i in A`.

For a d-part-symmetric function, all influences within a part are equal. Let `A` be the union of precisely those whole parts whose common influence exceeds `1/2`. The character `chi_A` itself is part-symmetric, so `u chi_A` remains in the class of (2.1). Its total influence is `J(u)`. Consequently

\[
H(u)=H(u\chi_A)\le C_dI(u\chi_A)=C_dJ(u).
\tag{2.2}
\]

An arbitrary character times a part-symmetric function satisfies the same folded bound, by character invariance. A restriction of a part-symmetric function is part-symmetric on the remaining coordinates: the fixed Hamming weight in each part merely shifts the argument of its weight table. The number of nonempty parts cannot increase.

### 2.2 Tensorization

For sign functions on disjoint coordinate sets, Fourier coefficients multiply and their squared Fourier laws are independent. Shannon entropy adds. Each physical influence, and hence its folded value, is exactly the influence in the corresponding factor. Therefore

\[
H\left(\prod_t u_t\right)=\sum_tH(u_t),\qquad
J\left(\prod_t u_t\right)=\sum_tJ(u_t).
\tag{2.3}
\]

A product of part-symmetric factors with at most `d_*` parts per factor, or any character times that product, thus has the folded FEI bound with `C_{d_*}`. This assertion is about the factorized leaf functions below, not about pretending that their quadratically coupled parent is independent.

## 3. Restricting physical coordinates costs at most two entropy bits each

**Lemma 3.1.** Let `f` be any Boolean function, `E` a fixed set of `k` physical coordinates, and `R` its complement. For a uniform physical assignment `z` on `E`, write `f_z` for the restriction. Then

\[
\boxed{H(f)\le\mathbb E_zH(f_z)+2k,}
\tag{3.1}
\]
\[
\boxed{\mathbb E_zJ(f_z)\le\sum_{i\in R}j_i(f).}
\tag{3.2}
\]

**Proof.** Let `S` have the squared Fourier distribution of `f`. If `T subset R`, the Fourier coefficient of a restriction is

\[
\widehat{f_z}(T)=\sum_{A\subseteq E}\widehat f(T\cup A)\chi_A(z).
\]

Orthogonality of the characters of `z` gives

\[
\mathbb E_z\widehat{f_z}(T)^2
=\sum_{A\subseteq E}\widehat f(T\cup A)^2
=\Pr(S_R=T).
\tag{3.3}
\]

Construct a joint distribution by first sampling uniform `Z` on the physical assignments and then sampling `Y`, conditionally on `Z=z`, from the squared Fourier law of `f_z`. Every leaf is Boolean, so every conditional law is normalized. Equation (3.3) identifies the marginal law of `Y` with that of `S_R`. Therefore

\[
\begin{aligned}
H(f)&=H(S_R)+H(S_E\mid S_R)\\
&\le H(Y)+k\\
&\le H(Y,Z)+k\\
&=\mathbb E_zH(f_z)+H(Z)+k\\
&=\mathbb E_zH(f_z)+2k.
\end{aligned}
\]

No spectral-coordinate independence was assumed.

For `i in R`, averaging the physical edge-disagreement indicator over the fixed coordinates gives `alpha_i(f)=E_z alpha_i(f_z)`. The function `t -> min(t,1-t)` is concave on `[0,1]`. Hence

\[
\mathbb E_zj_i(f_z)\le j_i(f).
\]

Sum over `R` to obtain (3.2). QED.

The coefficient two in the universal deletion bound is sharp. The two-variable quadratic phase `f(x_1,x_2)=(-1)^{x_1x_2}` has four Fourier masses `1/4`, hence entropy two. Fixing `x_1` leaves a constant or a character, each of entropy zero.

**Corollary 3.2 (paid deletion).** If every `f_z` satisfies `H(f_z)<=C J(f_z)`, then

\[
H(f)\le C\left(J(f)-\sum_{i\in E}j_i(f)\right)+2|E|.
\tag{3.4}
\]

In particular, a lower bound `j_i(f)>=eta` for all removed coordinates closes the same constant whenever `C eta>=2`. This is a standard entropy/restriction payment; the substantive issue is to find coordinates that both have a proved payment and leave a certified class. Sections 4–6 do that for arbitrary quadratic interactions.

## 4. Symmetry-breaking quadratic rows have a fixed influence cost

Write

\[
Q(x)=q_0+\sum_i\ell_ix_i+\sum_{i<j}A_{ij}x_ix_j,
\]

with symmetric zero-diagonal adjacency matrix `A` over `F_2`, and let
`N_i={j!=i:A_ij=1}`. The quadratic multiplicative derivative is a character:

\[
(-1)^{Q(x)+Q(x+e_i)}=(-1)^{\ell_i}\chi_{N_i}(x).
\tag{4.1}
\]

For any Boolean `h`, the multiplicative derivative

\[
g_i(x_{-i})=h(x_i=0,x_{-i})h(x_i=1,x_{-i})
\]

is also Boolean. Consequently, for `F=(-1)^Qh`,

\[
1-2\alpha_i(F)=(-1)^{\ell_i}\mathbb E[g_i\chi_{N_i}].
\tag{4.2}
\]

### 4.1 A two-character lemma

If a Boolean function `g` is invariant under a transposition of coordinates `j,k`, and exactly one of `j,k` belongs to a Fourier label `N`, then

\[
\boxed{|\widehat g(N)|\le\tfrac12.}
\tag{4.3}
\]

Indeed, let `N'` be the transposed label. Symmetry gives `ghat(N)=ghat(N')`. Thus

\[
|\widehat g(N)|
=\left|\mathbb E\,g\,\frac{\chi_N+\chi_{N'}}2\right|
\le\mathbb E\left|\frac{\chi_N+\chi_{N'}}2\right|=\tfrac12.
\]

The last equality follows because `chi_N/chi_N'=(-1)^{x_j+x_k}`: the half-sum is zero on `x_j!=x_k` and has magnitude one on `x_j=x_k`, each event having probability one half.

This argument needs Boolean boundedness and actual amplitude symmetry; it is not an estimate for arbitrary spectral probability distributions.

### 4.2 The quarter-influence conclusion

Suppose `h` is part-symmetric and `i` is mixed. In the part witnessing mixing, choose `j in N_i` and `k notin N_i`, both different from `i`. The derivative `g_i` is invariant under their transposition. Equations (4.2)–(4.3) give

\[
|1-2\alpha_i(F)|\le\tfrac12,
\qquad
\boxed{\tfrac14\le\alpha_i(F)\le\tfrac34,\quad j_i(F)\ge\tfrac14.}
\tag{4.4}
\]

The bound is uniform in the dimension, block sizes, choice of symmetric core, and every other quadratic interaction. It includes small blocks without an asymptotic argument.

The constant `1/4` is attained. Take the symmetric three-variable core `h=(-1)^{x_1x_2x_3}` and `Q=x_1x_2`. Coordinates 1 and 2 are mixed, and the product is a one-point defect, negative exactly at `(1,1,0)`. Every coordinate has influence `1/4`.

## 5. The remaining quadratic graph preserves block symmetry

Remove all mixed coordinates and put `W_r=V_r\E`. For every retained coordinate `i`, its row is constant on each original part after excluding `i` itself, and therefore on each residual part.

Between two nonempty residual parts, the adjacency matrix has constant rows and constant columns. Undirected symmetry implies that its entries are all equal. Within a residual part, every vertex is adjacent to all or to none of its other vertices. If there are at least two vertices, symmetry of the edges makes that choice consistent across vertices. With zero or one vertex there is no quadratic term to discuss.

It follows that the quadratic part on retained coordinates has the form

\[
\sum_r a_r\binom{w_r}{2}+\sum_{r<s}a_{rs}w_rw_s\pmod2,
\qquad w_r=|x_{W_r}|.
\tag{5.1}
\]

In particular it is invariant under permutations inside every residual part. Fixing the deleted coordinates converts edges meeting them into linear terms on the retained coordinates, and edges wholly inside them into a constant. Hence each physical restriction satisfies

\[
F_z=\pm\chi_{L_z}u_z,
\tag{5.2}
\]

where `u_z` is a Boolean function of at most `d` residual block weights. The product `u_z` combines the restricted core with the symmetric quadratic part (5.1); neither its degree nor its weight table is restricted.

Equation (2.2) therefore gives `H(F_z)<=C_d J(F_z)` for every physical assignment `z`, even though the leaves may be strongly dependent on that assignment.

Apply (3.4) and then (4.4):

\[
\begin{aligned}
H(F)
&\le C_d\left(J(F)-\sum_{i\in E}j_i(F)\right)+2|E|\\
&\le C_dJ(F)-(C_d/4-2)|E|\\
&\le C_dJ(F),
\end{aligned}
\]

since `C_d>=12.04>8`. This proves Theorem A, including its stronger version (1.2).

More generally this proof transfers any hereditary, character-normalizable part-symmetric FEI constant `C>=8` without an additional constant loss. The value 12.04 comes solely from the published symmetric input, not from fitting numerical experiments.

## 6. Independent cores with arbitrary cross-core quadratic coupling

Now let `h=prod_t h_t(x_{U_t})` as in Theorem B. Partition the coordinates into three categories.

* `E_cross`: coordinates with at least one quadratic neighbor outside their own core group `U_t`.
* `E_mixed`: coordinates not in `E_cross` whose neighbor set mixes one of the symmetry parts of their own group.
* `R`: every other coordinate.

These sets are disjoint. For `i in U_t`, the multiplicative derivative `h(x)h(x+e_i)` depends only on `U_t\{i}`: every other core squares to one. If `i in E_cross`, the character in (4.2) contains a nonempty label outside that group. Averaging those independent physical coordinates makes the correlation zero. Therefore

\[
\boxed{j_i(F)=\tfrac12\quad(i\in E_{\rm cross}).}
\tag{6.1}
\]

For `i in E_mixed`, the transposition argument within its own group still gives

\[
\boxed{j_i(F)\ge\tfrac14\quad(i\in E_{\rm mixed}).}
\tag{6.2}
\]

Delete `E=E_cross union E_mixed`. No quadratic edge remains between different core groups. Inside each residual core, the graph argument of Section 5 gives a quadratic function of that core's residual block weights. Thus, after removing a character and a global sign, every leaf is a product of independent part-symmetric Boolean factors with at most `d_*` parts each. Equations (2.2)–(2.3) give the leaf bound with `C=12.04+log_2 d_*`.

The deletion lemma now yields the explicit stronger result

\[
\boxed{
H(F)\le C J(F)-(C/2-2)|E_{\rm cross}|
                 -(C/4-2)|E_{\rm mixed}|.}
\tag{6.3}
\]

Both deducted terms are nonnegative, so (1.3) follows. This proves Theorem B.

The proof does not replace the parent by a product spectral law: only actual physical restrictions have the factorization, and their recombination cost was retained in (3.1).

## 7. What changed, and what has not been solved

The positive change is an explicit physical-coordinate payment for arbitrary quadratic interactions around fully general symmetric or part-symmetric cores. It retains their full high-degree weight tables and allows arbitrarily many independently supported cores without a factor-count penalty. No fresh controls are introduced, no low-density hypothesis is used, and no quadratic rank restriction is imposed.

The preceding repository theorem on arbitrary quadratic coupling of jointly independent one-point clauses has a stronger constant four and an affine-minimum conclusion on its stated class. Those results remain intact. This continuation instead allows arbitrary symmetric high-degree cores, with the published symmetric constant, and proves a physical-coordinate folded-influence bound. It does **not** claim constant four, arbitrary input-affine invariance, or a set-theoretic separation from every alternative representation in prior work.

Theorem A is not unrestricted FEI. Every Boolean function is trivially n-part-symmetric, but substituting `d=n` gives a coefficient growing with `log n`. Theorem B also requires disjoint core groups. Taking one arbitrary core and assigning singleton symmetry parts does not remove the logarithm.

Nor may `Q` be replaced by an unrestricted phase while retaining the proof. For example, for `m>=4` on `m+1` coordinates,

\[
F_m(x)=(-1)^{x_1x_2\cdots x_m}
\]

is a nonsymmetric perturbation of the symmetric constant core: the last coordinate is irrelevant, while the first `m` coordinates each have folded influence `2^{1-m}`. These relevant influences tend to zero. This refutes a uniform influence payment based simply on counting coordinates that an arbitrary higher-degree phase makes nonsymmetric. The derivative of a quadratic is a character, and this property was essential to (4.2)–(4.3). This example is not a counterexample to FEI, and it can itself be handled by more appropriate block structure.

### Remaining full-scope task

The repository's universal weighted-erasure target remains unproved:

\[
\sum_i H(S_i\mid S_{-i})\le K I(f)
\quad\text{for every Boolean }f,
\]

with one constant `K` independent of the function and dimension. The already-established restriction argument would then give full FEI with `K+2/ln2`. This report does not count rederiving that implication as progress and does not assert the false pointwise converse.

The present positive theorem supplies additional certified stopping classes for that program. Extending its payment to genuinely dependent high-degree cores, or proving a universal weighted allocation estimate, is still a substantive missing mathematical step. A proposed extension must pay rare, nonsymmetric high-degree defects by probability or entropy rather than charge a fixed amount for every affected coordinate.

## 8. Executed exact checks

Run from this directory:

```sh
python3 verify_quadratic_symmetry.py --output verification.json
```

The accompanying `verification.json` is actual output of the included program, with status `PASS`:

| Check family | Executed count and scope |
| --- | --- |
| Quadratic graph / partition structure | 108,506 checks through dimension 5, including both joint block symmetry and independent symmetric factors |
| All symmetric core tables and all homogeneous quadratic graphs | 67,732 parameter cases through dimension 5 |
| All block-symmetric core tables, partitions, quadratic graphs, and linear terms | 29,896 parameter cases through dimension 3 |
| Reproducibly sampled products of part-symmetric cores | 840 cases in dimensions 4–10, including arbitrary linear terms |
| Physical restriction leaves | 171,150 leaf truth tables checked |
| Exact symbolic cancellation at an entropy-deletion equality | 1 certificate |

Parameter-case families overlap; these counts must not be described as that many distinct Boolean functions or as exhaustive coverage of all functions in dimension five. The random samples were selected with seed `20260920`, then checked using exact arithmetic.

The checker verifies Parseval, equality between physical and Fourier influence, the quarter- and half-influence payments, the homogeneous residual graph, restricted part symmetry and factorization after removal of the actual linear phase, the partial Fourier mixture identity, folded-influence concavity, entropy deletion, and the stronger numerical inequality (6.3).

Walsh coefficients and influence counts are integers. Entropy and `log_2 d` comparisons use rational intervals. For `1<=x<=2`, with `z=(x-1)/(x+1)`, the logarithm enclosure follows from

\[
\ln x=2\sum_{j=0}^{M-1}\frac{z^{2j+1}}{2j+1}+R_M,
\qquad
0\le R_M\le\frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
\]

The program uses `M=40`, rational range reduction, and outward rounding to denominator `2^80`. Exact powers of two are treated exactly. An equality initially produced overlapping entropy intervals; the checker was strengthened to factor coefficient magnitudes and cancel common logarithms of primes before comparison. This was an interval-dependency issue, not a counterexample to the deletion lemma. No floating-point tolerance was substituted for proof.

Additional exact certificates in the output preserve the failed monotone-compression shortcut and the higher-degree counting obstruction described in `WORKLOG.md`. Finite checks do not prove the all-dimensional theorems; the proofs are Sections 2–6, with the cited published input.

## 9. Sources consumed, provenance, and scope control

### Primary mathematical input

[OWZ11] Ryan O'Donnell, John Wright, Yuan Zhou, *The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions*, ICALP 2011, LNCS 6755, pp. 330–341, DOI `10.1007/978-3-642-22006-7_28`. Author manuscript: <https://www.cs.cmu.edu/~odonnell/papers/fei.pdf>. Theorem 1 gives 12.04 for symmetric functions; Theorem 2 gives `12.04+log_2 d` for d-part-symmetric functions. These statements and the definition of part symmetry were read in the manuscript; the theorem pages were also inspected as page images.

[GMP26] Maria Jose Gonzalez, Paul MacManus, Maria Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, 2026: <https://arxiv.org/html/2606.00246v2>. Consulted for current conjecture status and the restriction/stopping-tree approach, not used as an additional unproved lemma in Sections 2–6.

A bounded search for quadratic twists, symmetric cores, and FEI did not establish publication priority for Theorems A–B. Absence of a search result is not evidence of novelty. Entropy chain rules, character invariance, tensorization, and the restriction mixture identity are standard ingredients, not claimed new here.

### Repository dependencies actually consulted

- `proofnet24/P03-fei/README.md`, blob `b880799e93758ca6576dfc9aa9711c1d4c32d08a`: complete current entrypoint at the start of this continuation. It identifies the retired shortcuts and live weighted target.
- `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`: complete erasure/JS reduction, its quantifiers, and its unresolved logarithmic term.
- `proofnet24/P03-fei/README_before_2026-09-20-shifted-thresholds.md`: historical index consulted for scope, not a claim that every linked report was reread.
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`: the visible tree/refinement portions were consulted. The present proof does not depend on its further portions or assert an exhaustive reread.
- `proofnet24/P03-fei/continuations/2026-09-19-quadratic-coupling/REPORT.md`, blob `b0950878596c587facfa4e5a76f480a4821d557c`: theorem statement and opening proof material read; lines 1–85 separately retrieved to confirm its exact independence and affine-minimum scope. Its later improvements are not used as premises here.

**Superseded targets checked:** no use of the refuted all-coordinate absolute-overlap selector, the false pointwise `H<=B+(2/ln2)I`, a retired full-resolvent payment, a universal fixed-coefficient affine entropy-drift bound, or a zero-boundary-debt decomposition. No unreviewed material in the recovered large Library patch is needed.

**Reused results:** the published symmetric FEI bound with its symmetry hypothesis; elementary Fourier/entropy identities; the existing universal-erasure implication only to state the remaining gap.

**New mathematical delta:** the paid symmetry-breaking coordinate lemma, residual block-graph argument, and Theorems A–B with unchanged published constants and explicit defect margins.

**Actual checks:** exactly the families and counts in Section 8 and the accompanying output. No additional agents or independent auditor were used. No claim of a maximal configurable reasoning setting is made.

**Remaining full-scope gap:** unrestricted dependent high-degree Boolean functions still lack a dimension-independent entropy payment. Native P03 atlas metrics, schedules, ownership, and other workers' results are not changed by this report. Repository delivery does not establish subsequent worker uptake.

## 10. Universal quadratic pair budget and a separate transfer criterion

The following statement does not require symmetry and may be useful beyond the certified classes above. It does not itself bound unrestricted spectral entropy.

**Lemma 10.1.** For any Boolean `h`, any quadratic `Q`, and any coordinate `i` whose quadratic row `N_i` is nonempty,

\[
\boxed{j_i(h)+j_i((-1)^Qh)\ge\tfrac12.}
\tag{10.1}
\]

**Proof.** For the Boolean multiplicative derivative `g_i`, put `a=E g_i` and `b=E g_i chi_{N_i}`. Since `N_i` is nonempty, its character takes each sign with probability one half. Choose signs of `a` and `b` separately. Then

\[
|a|+|b|\le\mathbb E|\pm1\pm\chi_{N_i}|=1.
\]

The two folded influences are `(1-|a|)/2` and `(1-|b|)/2` by (4.2), so their sum is at least one half. QED.

**Corollary 10.2 (low-folded-influence transfer).** Let `E={i:N_i!=empty}`. Suppose, for some `C>=4`, every physical restriction `h_z` obtained by fixing `E` satisfies `H(h_z)<=C J(h_z)`. If

\[
j_i(h)\le\tfrac12-\tfrac2C\qquad(i\in E),
\tag{10.2}
\]

then `H((-1)^Qh)<=C J((-1)^Qh)`.

Indeed, after all coordinates in `E` are fixed, `Q` is affine in the remainder; character invariance supplies the assumed leaf bound for the twisted leaves. Lemma 10.1 gives `j_i((-1)^Qh)>=2/C` on `E`, and (3.4) pays the deletion at the unchanged constant. The assumption is only a leaf certificate; it has not been proved for arbitrary `h` with a universal `C`. In particular, this is not an unrestricted quadratic-twist closure theorem obtained from a single inequality for `h` itself.

The companion checker tested (10.1) for every Boolean base and homogeneous quadratic graph through dimension three: 2,084 function/graph parameter cases and 4,640 relevant coordinate comparisons, all exact. Linear phase terms preserve folded influences and do not affect the statement. This elementary pair budget is recorded as a useful implication, not asserted to have no antecedent in the literature.
