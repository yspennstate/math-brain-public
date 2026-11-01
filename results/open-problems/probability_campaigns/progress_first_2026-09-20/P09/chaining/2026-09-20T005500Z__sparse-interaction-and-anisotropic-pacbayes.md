Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — sparse block interactions, anisotropic PAC-Bayes, and a sharp obstruction to Gaussian smoothing

**Status: PROVED PARTIAL.** This run makes two mathematical advances and one negative advance toward Randomstrasse101 Conjecture 16. First, it extends the previous disjoint-block theorem to tensor families whose coordinate-block interaction hypergraphs have bounded degree, using a dimension-free matching-layer projection lemma. Second, it proves an anisotropic covariance/PAC-Bayes inequality which strictly contains the isotropic Aden-Ali bound as the special case `D_t=I`. Third, it proves that *even fully anisotropic product-Gaussian smoothing cannot by itself solve the conjecture at `p=2`*: a single diagonal tensor forces a `d^(1/(2r))` loss in that entire proof template although its true Gaussian-series norm is dimension-free. This identifies a concrete reason the next method must use a mixture/sparse posterior or a chaining construction that preserves direct-sum geometry rather than only changing covariance.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Source target: for symmetric deterministic order-`r` tensors `T_i` and iid standard Gaussians `g_i`,

```text
E ||sum_i g_i T_i||_{sym(I_p)}
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_{sym(I_p)}^2)^(1/2),
```

  with the source symmetric norm `||T||_{sym(I_p)}=sup_{||x||_p<=1}|T[x,...,x]|`.
- Regime attacked: `2 <= p < 2r`.
- Current primary baselines recovered and not relabeled as new: BGJLR, arXiv:2411.10633, Theorem 1.2 gives the general type-2 upper exponent `gamma=1/2-1/(2r)` (up to a logarithm) in this regime; Aden-Ali, arXiv:2503.10580, Theorem 1.2 / Corollary 1.3 gives the sharper contraction-parameter/PAC-Bayes inequality and removes the BGJLR logarithm from the leading variance term. Randomstrasse101 explicitly says the full conjecture is settled for `p>=2r` and remains blocked by a volumetric barrier for `p<2r`. A bounded fresh primary-source search in this run found no later full arbitrary-tensor resolution in `2<=p<2r`; this is not an exhaustive worldwide prior-art claim.
- Historical continuity: the old C0035 and successor-gate files remain untouched. The immediately previous P09 theorem, `2026-09-19T235900Z__block-direct-sum-covariance-theorem.md`, is inherited as a proved repository checkpoint, not silently rederived or overwritten.

## 1. Old theorem, fixed full-source metric, and the exact new obligation

Write

```text
alpha := 1/2 - 1/p,
gamma := 1/2 - 1/(2r).
```

For arbitrary deterministic tensors, the recovered general polynomial exponent remains

```text
old full-source exponent: gamma,
new full-source exponent: gamma,
target exponent:          alpha.
```

So this run does **not** claim the full conjecture.

The previous P09 report proved the target scaling for block-direct-sum tensors. If `[d]=B_1 disjoint_union ... disjoint_union B_m`, `|B_j|<=b`, and every `T_i` is a sum of tensors supported on the individual `B_j^r`, then the previous theorem gives

```text
E ||sum_i g_i T_i||_{sym(I_p)}
 <= C(r,p)[b^gamma log(2b)+sqrt(log(2m))] S,   2<=p<=r,
```

and

```text
E ||sum_i g_i T_i||_{sym(I_p)}
 <= C(r,p)[b^gamma log(2b)+1] S,               r<p<2r,
```

where `S=(sum_i ||T_i||_{sym(I_p)}^2)^(1/2)`.

The unresolved structural obligation left by that proof was: **what survives when the tensors have cross-block interactions?** A naive decomposition into matching layers risked two losses: (i) extracting a matching layer might have much larger injective norm than the original tensor because of cancellation, and (ii) summing layer estimates by triangle could cost the number of layers. This run resolves (i) dimension-freely and quantifies (ii) exactly.

## 2. Full versus symmetric injective norm

For a symmetric order-`r` tensor `A`, also write

```text
||A||_{I_p}
 := sup_{||x_1||_p,...,||x_r||_p<=1} |A[x_1,...,x_r]|.
```

The real polarization identity gives constants depending only on `r` such that

```text
||A||_{sym(I_p)} <= ||A||_{I_p} <= c_r ||A||_{sym(I_p)}.    (2.1)
```

For example one may take a nonoptimal `c_r <= r^r/r!`. This is the same dimension-free equivalence used in BGJLR. We use the full norm only to prove projection stability, then return to the source symmetric norm.

## 3. Block-interaction hypergraphs

Fix a coordinate partition

```text
[d] = B_1 disjoint_union ... disjoint_union B_m,
|B_v| <= b.
```

For a coefficient multi-index `I=(i_1,...,i_r)`, define its block support

```text
bsupp(I) := {v in [m] : some i_t lies in B_v}.
```

For `1<=q<=r`, let `H_q` be the `q`-uniform hypergraph on `[m]` whose edges are precisely the `q`-sets `e` for which at least one tensor `T_i` has a nonzero coefficient with `bsupp(I)=e`. Let

```text
Delta_q := maximum vertex degree of H_q,
Delta_* := max_{2<=q<=r} Delta_q
```

(with `Delta_*=0` when there are no `q>=2` interactions).

This definition is family-level: the same hypergraph contains the support patterns of all deterministic summands. No independence of entries, no rank-one assumption, and no covariance independence between different block interactions is imposed.

For a matching `M` in `H_q`, define `Q_{q,M}A` by keeping exactly those coefficients of `A` whose block support is an edge of `M`, and zeroing the rest.

## 4. New projection lemma: extracting an arbitrary matching layer costs only `C(r)`

### Lemma 4.1 (matching-layer projection stability)

For every symmetric order-`r` tensor `A`, every coordinate partition above, every `q`, and every matching `M` in `H_q`,

```text
||Q_{q,M} A||_{sym(I_p)} <= C_r ||A||_{sym(I_p)},          (4.1)
```

where `C_r` depends only on `r`, not on `d,m,b,q,M,p`.

This is the key point that prevents the matching decomposition from destroying cancellations by an uncontrolled dimension factor.

### Proof

It suffices, by (2.1), to show

```text
||Q_{q,M} A||_{I_p} <= q^r ||A||_{I_p}.                    (4.2)
```

For every edge `e in M`, choose an arbitrary ordering

```text
e=(v_{e,1},...,v_{e,q}).
```

For a surjection `a:[r]->[q]`, let `R_{M,a}` retain precisely those coefficients for which there is one common edge `e in M` and slot `t` lies in coordinate block `B_{v_{e,a(t)}}` for every `t`.

Every coefficient whose block support is exactly an edge of `M` determines at least one such surjection, and in fact exactly one after the edge ordering and slot labels are fixed. Therefore

```text
Q_{q,M} = sum_{a:[r]->>[q]} R_{M,a}.                       (4.3)
```

The number of surjections is at most `q^r<=r^r`, so it remains to prove that every `R_{M,a}` is contractive for the full injective norm.

Fix `a`. In slot `t`, first coordinate-project onto

```text
C_t := union_{e in M} B_{v_{e,a(t)}}.
```

This is an `l_p` contraction. Because `M` is a matching, for a fixed slot the blocks in this union are pairwise disjoint and each coordinate in `C_t` belongs to exactly one edge label `e`.

Now choose independent Rademacher signs

```text
epsilon_e^(1),...,epsilon_e^(r-1),   e in M.
```

For `t<r`, define an `l_p` isometry `U_t` which multiplies coordinates in `B_{v_{e,a(t)}}` by `epsilon_e^(t)`. In the last slot define `U_r` to multiply coordinates in `B_{v_{e,a(r)}}` by

```text
prod_{s=1}^{r-1} epsilon_e^(s).
```

After the coordinate restrictions, a coefficient with edge labels `e_1,...,e_r` across its slots gets random multiplier

```text
prod_{s=1}^{r-1} epsilon_{e_s}^(s) epsilon_{e_r}^(s).
```

Its expectation is `1` exactly when `e_1=...=e_r`, and `0` otherwise. Hence `R_{M,a}` is the expectation of tensor products of `l_p` isometries, composed with slotwise coordinate contractions. Consequently

```text
||R_{M,a}A||_{I_p} <= ||A||_{I_p}.
```

Summing over the at most `q^r` surjections in (4.3) proves (4.2), and (2.1) proves (4.1). QED.

### Why this is useful

The proof did not assume the matching components were already separated in the deterministic norm. It shows that a matching layer can be *extracted* from an arbitrary tensor with only an order-dependent loss. Thus the earlier concern that cancellations could make every matching projection enormous is false for a single matching projection.

## 5. Edge coloring turns bounded interaction degree into finitely many direct-sum layers

A `q`-uniform hypergraph of maximum degree `Delta_q` has a greedy edge coloring with at most

```text
L_q <= q(Delta_q-1)+1 <= q Delta_q                  (q>=2)  (5.1)
```

colors, because an edge meets at most `q(Delta_q-1)` other edges. For `q=1`, all singleton edges already form one matching, so put `L_1<=1`.

Write

```text
H_q = M_{q,1} disjoint_union ... disjoint_union M_{q,L_q}
```

with each `M_{q,l}` a matching, and set

```text
T_i^(q,l) := Q_{q,M_{q,l}} T_i.
```

Every coefficient has one unique block-support cardinality and one unique color, hence

```text
T_i = sum_{q=1}^r sum_{l=1}^{L_q} T_i^(q,l).              (5.2)
```

By Lemma 4.1,

```text
S_(q,l)
 := (sum_i ||T_i^(q,l)||_{sym(I_p)}^2)^(1/2)
 <= C_r S.                                                  (5.3)
```

For one matching layer, define the superblock belonging to edge `e` by

```text
U_e := union_{v in e} B_v.
```

The superblocks `U_e`, `e in M_{q,l}`, are pairwise disjoint and satisfy `|U_e|<=qb<=rb`. Moreover `T_i^(q,l)` has no coefficient crossing two distinct superblocks `U_e`. Thus each matching layer is exactly of the block-direct-sum form handled in the previous P09 theorem, with local dimension at most `rb`.

## 6. New theorem: sparse block-interaction tensors satisfy a stronger type-2 bound

Let

```text
Lambda := L_1 + ... + L_r.
```

By (5.1),

```text
Lambda <= 1 + sum_{q=2}^r q Delta_q <= C_r(1+Delta_*).     (6.1)
```

### Theorem 6.1 (bounded block-interaction degree)

Let `2<=p<2r` and let `T_1,...,T_n` be symmetric order-`r` tensors. Suppose the family admits a coordinate partition into blocks of size at most `b`, with block-interaction hypergraphs `H_q` as above. Put

```text
gamma = 1/2 - 1/(2r),
S = (sum_i ||T_i||_{sym(I_p)}^2)^(1/2).
```

Then, for `2<=p<=r`,

```text
E ||sum_i g_i T_i||_{sym(I_p)}
 <= C(r,p) Lambda
    [(rb)^gamma log(2rb) + sqrt(log(2m))] S,                (6.2)
```

and, for `r<p<2r`,

```text
E ||sum_i g_i T_i||_{sym(I_p)}
 <= C(r,p) Lambda
    [(rb)^gamma log(2rb) + 1] S.                            (6.3)
```

In particular, using (6.1), the factor `Lambda` may be replaced by `C_r(1+Delta_*)`.

### Proof

Use decomposition (5.2), triangle inequality, and then expectation:

```text
E ||sum_i g_i T_i||
 <= sum_{q,l} E ||sum_i g_i T_i^(q,l)||.
```

For each fixed `(q,l)`, the tensors are a direct sum over the pairwise disjoint superblocks `U_e`, each of size at most `rb`. Apply the previous P09 direct-sum theorem in local dimension `rb`. For `2<=p<=r`,

```text
E ||sum_i g_i T_i^(q,l)||
 <= C(r,p)[(rb)^gamma log(2rb)+sqrt(log(2m))] S_(q,l),
```

and for `r<p<2r`,

```text
E ||sum_i g_i T_i^(q,l)||
 <= C(r,p)[(rb)^gamma log(2rb)+1] S_(q,l).
```

Use (5.3) and sum over the `Lambda` matching layers. QED.

### What is genuinely broader than the previous theorem

The previous theorem corresponds essentially to no cross-block interaction. Theorem 6.1 allows arbitrary symmetric tensors *inside every interacting collection of blocks*, permits the same Gaussian coefficients to couple all interactions, and allows every coordinate block to participate in many different hyperedges. The only new structural parameter is the maximum interaction degree.

No independence of layers is used. No entrywise sparsity inside a participating superblock is assumed. The price of overlap is explicit and deterministic.

## 7. Dimension exponent and nontrivial regimes already at the conjectured scale

Suppose, up to polylogarithmic factors,

```text
b <= d^beta,
Delta_* <= d^delta.
```

The polynomial part of (6.2)-(6.3) is

```text
d^(delta + beta gamma).
```

Therefore Theorem 6.1 reaches the conjectured `d^alpha` scaling for this class whenever

```text
delta + beta gamma <= alpha,
alpha=1/2-1/p,
gamma=1/2-1/(2r).                                          (7.1)
```

This strictly enlarges the earlier direct-sum region `beta gamma<=alpha` by allowing polynomially many overlapping block interactions when `alpha>0`.

Examples:

1. `r=p=3`: `alpha=1/6`, `gamma=1/3`. With constant-size or polylog-size blocks (`beta=0`), the theorem allows interaction degree as large as `d^(1/6)` up to logarithms while retaining the conjectured ambient exponent. With `b=d^(1/4)`, it still allows `Delta_*=d^(1/12)`.

2. `r=3,p=4`: `alpha=1/4`, `gamma=1/3`. Blocks of size `d^(1/2)` may still have interaction degree `d^(1/12)` while remaining at the conjectured exponent.

3. `p=2`: `alpha=0`. The theorem reaches the desired polylogarithmic scale whenever both block size and interaction degree are polylogarithmic. This already includes interacting families far beyond a disjoint union of tensor blocks.

This is a restricted theorem and is labeled `PROVED PARTIAL`, not a proof of Conjecture 16.

## 8. Where the volumetric obstruction moved

For a genuinely dense `q`-uniform interaction hypergraph on `m` blocks,

```text
Delta_q can be of order m^(q-1).
```

Thus the edge-color/triangle factor in Theorem 6.1 can be polynomially catastrophic. The theorem isolates the new bottleneck cleanly:

> The remaining problem is not extracting a matching layer; Lemma 4.1 does that dimension-freely. The remaining problem is aggregating very many interacting layers without taking their norms one at a time.

One tempting next lemma would be a deterministic Littlewood-Paley estimate

```text
(sum_l ||Q_l A||_{sym(I_p)}^2)^(1/2)
 <= polylog(d) C_r ||A||_{sym(I_p)}.                         (8.1)
```

If true for matching layers, it could potentially replace a linear layer count by square-function aggregation. Before building on it, this run tried to refute it.

## 9. Counterexample: the naive matching-layer square function is false for every `r>=3`

### Proposition 9.1

For every fixed `r>=3`, there are symmetric order-`r` tensors `A` on `m` coordinates and matching decompositions of their complete `r`-uniform block support such that

```text
(sum_l ||Q_l A||_{sym(I_2)}^2)^(1/2)
 >= c_r m^((r-1)/2),                                       (9.1)
```

while

```text
||A||_{sym(I_2)} <= C_r sqrt(m).                            (9.2)
```

Thus (8.1) fails by a polynomial factor `m^((r-2)/2)`.

### Proof

Take singleton coordinate blocks and the complete `r`-uniform hypergraph on `[m]`. For every `r`-set `e`, choose an independent random sign `epsilon_e` and form the symmetric squarefree polynomial

```text
P_epsilon(x) := sum_{|e|=r} epsilon_e prod_{j in e} x_j.
```

For a fixed `x` with `||x||_2<=1`, this is a centered subgaussian random variable with variance

```text
sum_{|e|=r} prod_{j in e} x_j^2
 <= (sum_j x_j^2)^r / r!
 <= 1/r!.
```

Take a fixed sufficiently fine Euclidean net of the unit sphere of cardinality `exp(O_r(m))`. A union bound gives, with positive probability,

```text
sup_{x in net} |P_epsilon(x)| <= C_r sqrt(m).
```

The standard homogeneous-polynomial net argument then enlarges this only by an `r`-dependent constant, proving the existence of a sign choice satisfying (9.2).

Now properly edge-color the complete `r`-uniform hypergraph into matchings. Every nonempty matching layer consists of disjoint squarefree monomials. For `p=2<=r`, the exact direct-sum geometry from the previous P09 theorem says that the symmetric injective norm of such a layer is the maximum norm of one edge monomial. For one edge,

```text
sup_{sum_j x_j^2<=1} prod_{j in e}|x_j| = r^(-r/2),
```

by AM-GM, with equality when the `r` active coordinates all have magnitude `1/sqrt(r)`. Hence every nonempty color layer has norm exactly `r^(-r/2)`.

Any matching contains at most `floor(m/r)` edges, whereas the complete hypergraph has `binom(m,r)` edges. Therefore every matching decomposition has at least

```text
L >= binom(m,r)/floor(m/r) >= c_r m^(r-1)
```

nonempty layers. Consequently

```text
(sum_l ||Q_l A||^2)^(1/2)
 = r^(-r/2) sqrt(L)
 >= c_r m^((r-1)/2).
```

This proves (9.1), and comparison with (9.2) refutes (8.1). QED.

### Consequence

A successful dense-interaction proof cannot first decompose a deterministic tensor into all of its matching layers and then hope for a universal `l_2` inequality between the layer norms and the original injective norm. Such a decomposition destroys cancellations already present inside a *single deterministic summand*. The random-sign complete hypergraph is the clean witness.

This is an important correction to the most obvious continuation of the previous report.

## 10. Second new tool: anisotropic PAC-Bayes covariance inequality

The failure above says the next proof should preserve each whole deterministic `T_i` while changing the geometry of the Gaussian-process argument. Aden-Ali's 2025 theorem uses an isotropic product-Gaussian prior/posterior. The following extension allows an arbitrary positive-definite covariance in each tensor slot.

This theorem is proved here because it gives an exact mathematical object to optimize in the next run. I did not find this anisotropic formulation stated in the two primary tensor papers checked here; that is **not** a publication-level novelty claim.

### Weighted contractions

Work first with a possibly asymmetric tensor family

```text
T_k in R^(d_1) tensor ... tensor R^(d_r).
```

Choose positive-definite matrices `D_t in R^(d_t x d_t)`, `t=1,...,r`. For `J subseteq [r]` and an order-`|J|` tensor `A` living in the slots in `J`, define

```text
||A||_(F,D_J)^2
 := <A, (tensor_{t in J} D_t) A>.
```

For `0<=ell<=r`, define

```text
sigma_ell(D)^2
 := sup_{x_t in B_p^(d_t)}
    sum_{J subseteq [r], |J|=ell}
    sum_k
    || T_k contracted by (x_t)_(t notin J) ||_(F,D_J)^2.    (10.1)
```

For `ell=0`, this is the ordinary weak variance

```text
sup_x sum_k T_k(x_1,...,x_r)^2.
```

For `ell=r`, it is the weighted Frobenius sum

```text
sum_k <T_k,(D_1 tensor ... tensor D_r)T_k>.
```

Also define the geometric cost

```text
H_p(D_1,...,D_r)
 := sum_{t=1}^r h_p(D_t),

h_p(D) := sup_{||x||_p<=1} x^T D^(-1)x.                  (10.2)
```

For diagonal `D=diag(w_1,...,w_d)`, this is explicit:

```text
h_2(D) = max_j w_j^(-1),
```

and for `p>2`,

```text
h_p(D)
 = (sum_j w_j^(-p/(p-2)))^((p-2)/p).                     (10.3)
```

### Theorem 10.1 (anisotropic product-Gaussian PAC-Bayes)

Let `g_k` be iid standard Gaussians. Then for every choice of positive-definite `D_1,...,D_r`,

```text
E ||sum_k g_k T_k||_(I_p)
 <= inf_{beta>0}
    { H_p(D_1,...,D_r)
      sum_{ell=0}^r beta^(1-ell) sigma_ell(D)^2 }^(1/2).  (10.4)
```

One may further infimize the right side over the matrices `D_t`.

Setting every `D_t=I` recovers Aden-Ali Theorem 1.2 (up to only notation), because then `H_p=sum_t d_t^(1-2/p)` and the weighted contractions become his variance parameters.

### Proof

Use the same PAC-Bayesian lemma as Aden-Ali, but take prior

```text
pi = product_{t=1}^r N(0, beta^(-1) D_t)
```

and, for a point `x=(x_1,...,x_r)` in the product of `l_p` unit balls, posterior

```text
rho_x = product_{t=1}^r N(x_t, beta^(-1) D_t).
```

Because every `T_k` is multilinear and the perturbations in different slots are independent and centered,

```text
E_{theta~rho_x} T_k(theta_1,...,theta_r)
 = T_k(x_1,...,x_r).                                      (10.5)
```

For the standard Gaussian coefficient `g_k`, its log-MGF is exactly quadratic. Expanding the posterior second moment slot by slot, every subset `J` of perturbed slots contributes one covariance factor `beta^(-1)D_t` in each `t in J`; cross terms with a centered perturbation appearing only once vanish. Therefore

```text
sum_k E_{theta~rho_x} T_k(theta)^2
 <= sum_{ell=0}^r beta^(-ell) sigma_ell(D)^2.             (10.6)
```

The KL divergence is exact:

```text
KL(rho_x || pi)
 = (beta/2) sum_t x_t^T D_t^(-1)x_t
 <= (beta/2) H_p(D_1,...,D_r).                             (10.7)
```

Applying the PAC-Bayes lemma with scale parameter `lambda>0` gives

```text
E ||sum_k g_k T_k||_(I_p)
 <= (lambda/2) sum_ell beta^(-ell) sigma_ell(D)^2
    + beta H_p(D)/(2 lambda).                              (10.8)
```

Optimizing `lambda` yields exactly (10.4). QED.

### Source-symmetric consequence

For symmetric tensors the source norm is at most the full injective norm, and the full/symmetric deterministic norms are equivalent up to `C_r`; hence (10.4) is immediately usable as a source-normalized covariance inequality after only order-dependent constants.

## 11. A no-go theorem for this entire anisotropic Gaussian-smoothing template

A natural hope was that choosing `D_t` cleverly might remove the low-`p` volumetric obstruction. Before treating that as the next main route, this run tested the simplest possible hard witness.

### Proposition 11.1 (anisotropic product-Gaussian smoothing still loses `d^(1/(2r))` at `p=2`)

Let there be one deterministic order-`r` diagonal tensor

```text
A := sum_{j=1}^d e_j^(tensor r),
```

and take `p=2`. Its full and symmetric injective norms equal `1`, so for one Gaussian coefficient

```text
E ||g A||_(I_2) = E|g| = O(1).                            (11.1)
```

Nevertheless the right side of Theorem 10.1 is at least

```text
c_r d^(1/(2r))                                             (11.2)
```

for **every** choice of positive-definite anisotropic covariances `D_1,...,D_r` and every `beta>0`.

### Proof

Put

```text
h_t := lambda_max(D_t^(-1)).
```

For `p=2`,

```text
H_2(D)=sum_t h_t.                                          (11.3)
```

Since `D_t >= h_t^(-1) I` in Loewner order,

```text
D_1 tensor ... tensor D_r
 >= (prod_t h_t^(-1)) I.
```

The unweighted Frobenius norm of `A` is `sqrt(d)`, so the top weighted contraction obeys

```text
sigma_r(D)^2
 = <A,(D_1 tensor ... tensor D_r)A>
 >= d / prod_t h_t.                                        (11.4)
```

The weak variance for this one tensor is

```text
sigma_0(D)^2 = ||A||_(I_2)^2 = 1.                         (11.5)
```

Discard all the nonnegative intermediate terms from (10.4). The squared PAC-Bayes bound is at least

```text
(sum_t h_t)
[ beta + beta^(1-r) d/(prod_t h_t) ].                     (11.6)
```

For `a>0`,

```text
inf_{beta>0} [beta + a beta^(1-r)] = c_r a^(1/r).
```

Thus (11.6) is at least

```text
c_r d^(1/r)
(sum_t h_t)/(prod_t h_t)^(1/r).
```

AM-GM gives

```text
sum_t h_t >= r (prod_t h_t)^(1/r),
```

so the squared bound is at least `c_r d^(1/r)`. Taking a square root proves (11.2). QED.

### Interpretation

This is a proof-method obstruction, not a counterexample to Conjecture 16. The actual random norm in (11.1) is dimension-free, while every product-Gaussian posterior with arbitrary covariance loses `d^(1/(2r))` in the PAC-Bayes objective.

The witness is exactly the kind of direct-sum geometry handled well by the previous P09 theorem. Product-Gaussian smoothing forces all `d` diagonal directions into one weighted Frobenius contraction and therefore cannot see the `l_infinity` geometry of the direct sum.

So merely replacing the isotropic covariance by a Lewis-weight or leverage-score covariance cannot be the whole solution.

## 12. What was learned about the volumetric barrier

This run separates three issues that had been conflated:

1. **Layer extraction is not the fundamental problem.** Matching-layer projections are dimension-free up to `C_r` (Lemma 4.1).

2. **Norm-by-norm layer aggregation is genuinely too crude in dense interactions.** Proposition 9.1 shows even an `l_2` deterministic layer square function can be polynomially larger than the original tensor norm because projection destroys cancellations inside one tensor.

3. **Ellipsoidal smoothing alone is also too crude.** Proposition 11.1 shows arbitrary anisotropic product-Gaussian smoothing still pays a polynomial loss on the simplest diagonal tensor.

These two negative statements point in the same direction: the next proof needs a stochastic/chaining device that preserves direct-sum or sparse-mixture geometry *before* taking a Frobenius contraction or separate layer norms.

## 13. Remaining gap and next concrete attack

The full arbitrary-tensor exponent is still

```text
gamma = 1/2 - 1/(2r)
```

rather than

```text
alpha = 1/2 - 1/p.
```

The next attack will therefore **not** pursue a universal deterministic matching-layer square function and will **not** merely tune an anisotropic Gaussian covariance.

The concrete next target is a **mixture/sparse-posterior PAC-Bayes lemma** adapted to a coordinate-block partition. The intended posterior is a mixture over sparse block supports (or a hierarchical block tree) rather than one full-dimensional Gaussian. The proof target is an inequality of the schematic form

```text
E ||sum_i g_i T_i||_(I_p)
 <= inf_{mixture posterior}
    sqrt{ [mixture KL cost] x [mixture-weighted contraction energy] },
```

with these two required features:

- on a direct sum of `m` blocks, the KL/entropy term should be `O(log m)` rather than a Euclidean/Frobenius cost over all blocks, recovering the exact geometry that Proposition 11.1 says a single Gaussian misses;
- on a dense interaction tensor, the posterior should keep the whole `T_i` intact and randomize the *test vector / block support*, avoiding the cancellation-destroying deterministic layer decomposition refuted by Proposition 9.1.

A first finite-dimensional candidate is: choose a random subset of coordinate blocks at a geometrically distributed scale, condition a Gaussian perturbation to that subset, and mix over the subset law. The immediate calculation to do next is the exact KL of this mixture against a matching sparse prior and the second-moment expansion of `T_k(x+Z)`; the goal is to see whether the top weighted Frobenius term becomes a multiscale sum of local contractions rather than one ambient contraction.

If that mixture still collapses to the same `d^(1/(2r))` diagonal witness, it will be rejected immediately and the method will pivot to a direct generic-chaining construction with sparse increments instead.

## 14. Obligation ledger

```text
O1  Go beyond disjoint coordinate blocks.
    BEFORE: open.
    AFTER:  proved for bounded-degree block-interaction hypergraphs, Theorem 6.1.

O2  Prevent projection of a matching layer from destroying the source norm.
    BEFORE: unresolved.
    AFTER:  solved dimension-freely by Lemma 4.1.

O3  Replace the linear number-of-layers loss in dense interactions.
    BEFORE: proposed square-function route.
    AFTER:  naive deterministic l2 layer square function refuted by Proposition 9.1.

O4  Test covariance preconditioning as a way around the volumetric barrier.
    BEFORE: untested.
    AFTER:  anisotropic PAC-Bayes theorem proved, but product-Gaussian template shown insufficient by Proposition 11.1.

O5  Full arbitrary deterministic-tensor Conjecture 16 for 2<=p<2r.
    BEFORE: open.
    AFTER:  open; generic exponent unchanged at gamma.

O6  Next route.
    Mixture/sparse posterior or sparse-increment chaining that preserves deterministic cancellation and direct-sum geometry before Frobenius aggregation.
```

## 15. Accuracy labels

- **PROVED PARTIAL:** Lemma 4.1, Theorem 6.1, Theorem 10.1, Proposition 9.1, Proposition 11.1 as written above.
- **KNOWN / RECOVERED PRIMARY RESULT:** BGJLR Theorem 1.2 and Aden-Ali Theorem 1.2 / Corollary 1.3; no novelty claimed for those.
- **OPEN:** full Randomstrasse101 Conjecture 16 for arbitrary deterministic symmetric tensors in `2<=p<2r`.
- **NOT CLAIMED:** publication novelty of the anisotropic PAC-Bayes formulation; only a bounded primary-source comparison was performed.
- **NO CLOSURE CLAIM:** no paper folder, external audit, or public posting is requested or justified by this report.

## 16. Delivery scope

This report is the only new P09 research file intended for this run. No historical or peer report is overwritten; no email, Drive, public post, permission bypass, force-push, or scheduler replacement is part of this iteration.
