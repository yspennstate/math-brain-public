Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 first progress-first run — block direct sums breach the ambient volumetric loss

**Status: PROVED PARTIAL.** This report proves a source-normalized Gaussian type-2 bound for a new structured class of arbitrary within-block symmetric tensors. It does **not** prove Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Operational authority: `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.
- Historical continuity: the old C0035 reports and successor-gate history are preserved in place. C0035 remains mathematically `PARTIAL / UNDECIDED` and operationally retired. This new P09 line does not inherit C0035's metric or stagnation history.

## 1. Exact source normalization and current baseline

Let `r>=2`, `p>=2`, let `T_1,...,T_n in (R^d)^{\otimes r}` be deterministic symmetric order-`r` tensors, and let `g_1,...,g_n` be independent standard Gaussians. The source uses the **symmetric injective** norm

```text
||T||_{I_p} := sup_{||x||_p <= 1} | <T,x^{\otimes r}> |.
```

Conjecture 16 asks for

```text
E || sum_i g_i T_i ||_{I_p}
   <= polylog(d,n) C(r,p) d^(1/2-1/p)
      (sum_i ||T_i||_{I_p}^2)^(1/2).
```

Write

```text
alpha := 1/2 - 1/p.
```

The unresolved regime targeted here is `2 <= p < 2r`.

The strongest general polynomial dimension exponent recovered from the primary baseline Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, Theorem 1.2, is

```text
gamma := 1/2 - 1/(2r)
```

(up to an `O_{r,p}(log d)` factor) throughout `p<2r`. Thus the generic polynomial exponent gap is

```text
gamma - alpha = 1/p - 1/(2r) = (2r-p)/(2pr) > 0.
```

Their theorem is stated in their injective-norm/type-2 language; for symmetric tensors, polarization changes only constants depending on `r` (and the source itself cites this work as settling its symmetric conjecture for `p>=2r`). Standard conditioning on Gaussian magnitudes transfers their Rademacher type-2 estimate to the Gaussian series needed here with no new dimension loss.

Aden-Ali, arXiv:2503.10580, improves the parameter inequality (in particular removing a logarithmic loss in the leading variance term), but the higher contraction/Frobenius parameters remain the obstruction in the universal low-`p` regime. A bounded current primary-source search for this run found no later paper proving the full arbitrary-tensor Conjecture 16 in `2<=p<2r`. This is a bounded search statement, not a claim of exhaustive worldwide literature coverage.

### Full-source metric

For arbitrary deterministic symmetric tensors, the best recovered general exponent remains

```text
before: gamma = 1/2 - 1/(2r)
after:  gamma = 1/2 - 1/(2r)
target: alpha = 1/2 - 1/p.
```

So the **full conjecture is not yet improved** in this run. The mathematical progress is a new structural theorem below that replaces ambient dimension `d` by the largest interacting block size `b` for a genuinely broader correlated tensor family.

## 2. Counterexample first: a tempting Frobenius-collapse lemma is false

A natural way to try to erase the `p<2r` barrier is to hope that every relevant contraction tensor `A` satisfies a dimension-free or polylogarithmic comparison

```text
||A||_F <= polylog(d) ||A||_{I_p}.
```

That route is false even for diagonal symmetric tensors.

For any order `q>=1`, define

```text
A_q := sum_{k=1}^d e_k^{\otimes q}.
```

Then exactly

```text
||A_q||_F = sqrt(d),
```

while

```text
||A_q||_{I_p}
 = sup_{||x||_p<=1} |sum_k x_k^q|
 = 1                       if p <= q,
 = d^(1-q/p)               if p > q.
```

The second line follows from the monotonicity of finite-dimensional `l_s` norms when `p<=q`, and from Holder with equality at the flat nonnegative vector when `p>q`. Hence

```text
||A_q||_F / ||A_q||_{I_p}
 = d^(1/2)                 if p <= q,
 = d^(q/p-1/2)             if q < p < 2q.
```

Thus whenever `p<2q` the ratio is polynomial in `d`. At `q=r` this reproduces exactly the threshold `p<2r` that appears in the BGJLR volumetric obstruction. Therefore a universal proof strategy that simply replaces all contraction Frobenius norms by `polylog(d) * ||.||_{I_p}` cannot prove Conjecture 16.

This counterexample suggests that the proof must preserve how mass is distributed across coordinates rather than collapse all geometry into one ambient Frobenius norm.

## 3. New covariance-structure theorem: disjoint coordinate blocks

Partition the coordinates into disjoint blocks

```text
[d] = B_1 disjoint_union ... disjoint_union B_m,
|B_j| <= b.
```

Assume each source tensor has the form

```text
T_i = sum_{j=1}^m T_{ij},
```

where `T_{ij}` is an arbitrary symmetric order-`r` tensor supported on `B_j^r`.

There is **no rank-one assumption inside a block**, no independence of tensor entries, and no independence between the Gaussian block processes: the same coefficients `g_i` drive every block. Thus this class permits arbitrary deterministic covariance across blocks through the common Gaussian vector.

For a block-supported tensor `A_j`, write

```text
a_j := ||A_j||_{I_p}.
```

### Lemma 3.1 — exact block norm when `2<=p<=r`

For `A=sum_j A_j` with disjoint coordinate-block supports,

```text
||A||_{I_p} = max_j a_j.
```

**Proof.** For any `x` with `||x||_p<=1`, let `t_j=||x_{B_j}||_p`. Homogeneity gives

```text
|<A,x^r>| <= sum_j a_j t_j^r.
```

Since `sum_j t_j^p<=1` and `r>=p`, one has `sum_j t_j^r<=sum_j t_j^p<=1`; therefore the right side is at most `max_j a_j`. The reverse inequality follows by taking `x` supported entirely on a maximizing block and using a block extremizer. QED.

### Lemma 3.2 — constant-equivalent `l_s` block norm when `p>r`

Let

```text
s := p/(p-r).
```

Then

```text
2^(-1/s) (sum_j a_j^s)^(1/s)
 <= ||A||_{I_p}
 <= (sum_j a_j^s)^(1/s).
```

For odd `r`, the constant `2^(-1/s)` can be replaced by `1`.

**Proof of the upper bound.** Again put `t_j=||x_{B_j}||_p`. Then

```text
|<A,x^r>| <= sum_j a_j t_j^r.
```

The constraint is `sum_j t_j^p<=1`. Setting `u_j=t_j^r`, this is `||u||_{p/r}<=1`, whose dual exponent is

```text
(p/r)' = p/(p-r)=s.
```

Holder therefore gives `sum_j a_j t_j^r <= ||a||_s`.

**Proof of the lower bound.** For every block choose a norm-one block vector `y_j` attaining `|<A_j,y_j^r>|=a_j`. Split the blocks according to the sign of this extremal value. At least one sign class `J` carries at least half of `sum_j a_j^s`, hence

```text
(sum_{j in J} a_j^s)^(1/s) >= 2^(-1/s)||a||_s.
```

Within that class all chosen polynomial values have the same sign. Choose nonnegative scalars `t_j` attaining Holder duality under `sum_{j in J} t_j^p=1`, and set `x_{B_j}=t_j y_j` on `J`, zero elsewhere. Then

```text
|<A,x^r>| = sum_{j in J} a_j t_j^r
           = (sum_{j in J} a_j^s)^(1/s).
```

This proves the stated lower bound. If `r` is odd, replacing `y_j` by `-y_j` flips the sign blockwise, so all blocks can be aligned and equality holds. QED.

## 4. Gaussian aggregation without paying for the number of blocks polynomially

Define

```text
Y_j(g) := sum_i g_i T_{ij},
Z_j(g) := ||Y_j(g)||_{I_p},
a_{ij} := ||T_{ij}||_{I_p},
L_j := (sum_i a_{ij}^2)^(1/2),
S := (sum_i ||T_i||_{I_p}^2)^(1/2).
```

Suppose that on every block (dimension at most `b`) we have the local Gaussian type-2 estimate

```text
E Z_j <= K_b L_j.                                      (4.1)
```

The next result is the new covariance-structure step.

### Theorem 4.1 — direct-sum Gaussian type-2 inequality

Under the block support assumption above:

**(i) `2<=p<=r`:**

```text
E ||sum_i g_i T_i||_{I_p}
 <= [K_b + C sqrt(log(2m))] S.                         (4.2)
```

**(ii) `r<p<2r`:** with `s=p/(p-r)>2`,

```text
E ||sum_i g_i T_i||_{I_p}
 <= 2^(1/s)[K_b + C sqrt(s)] S.                        (4.3)
```

The constant `C` is universal. In particular, (4.3) has **no polynomial or logarithmic dependence on the number `m` of disjoint blocks**.

### Proof

For each `j`, the map `g -> Z_j(g)` is Lipschitz in Euclidean Gaussian coefficient space with constant at most `L_j`. Indeed,

```text
|Z_j(g)-Z_j(h)|
 <= ||sum_i (g_i-h_i)T_{ij}||_{I_p}
 = sup_{||x||_p<=1} |sum_i (g_i-h_i)<T_{ij},x^r>|
 <= ||g-h||_2 sup_{||x||_p<=1}(sum_i <T_{ij},x^r>^2)^(1/2)
 <= L_j ||g-h||_2.
```

Hence Gaussian concentration gives, for every fixed `s>=2`,

```text
(E Z_j^s)^(1/s) <= E Z_j + C sqrt(s)L_j
                 <= (K_b+C sqrt(s))L_j.               (4.4)
```

#### Case `2<=p<=r`

Lemma 3.1 says the global norm is exactly `max_j Z_j`. Standard Gaussian maximal concentration then gives

```text
E max_j Z_j <= max_j E Z_j + C sqrt(log(2m)) max_j L_j.
```

Also Lemma 3.1 applied to each deterministic `T_i` gives

```text
L_j^2 = sum_i a_{ij}^2
      <= sum_i (max_k a_{ik})^2
       = S^2.
```

Using (4.1) proves (4.2).

#### Case `r<p<2r`

Lemma 3.2 and Jensen/Minkowski give

```text
E ||sum_i g_i T_i||_{I_p}
 <= E (sum_j Z_j^s)^(1/s)
 <= (sum_j E Z_j^s)^(1/s)
 <= (K_b+C sqrt(s))(sum_j L_j^s)^(1/s).               (4.5)
```

Since `s>2`, the mixed-norm Minkowski inequality gives

```text
(sum_j L_j^s)^(1/s)
 = [sum_j (sum_i a_{ij}^2)^(s/2)]^(1/s)
 <= [sum_i (sum_j a_{ij}^s)^(2/s)]^(1/2).             (4.6)
```

Lemma 3.2, now applied to each deterministic tensor `T_i`, says

```text
(sum_j a_{ij}^s)^(1/s) <= 2^(1/s)||T_i||_{I_p}.
```

Substituting this into (4.6), then into (4.5), yields (4.3). QED.

### Why this is a covariance result rather than an independence trick

No `Y_j` are assumed independent. They can be maximally correlated because every block uses the same Gaussian coefficient vector `(g_i)`. The proof works because the deterministic source norm itself has an exact `l_infinity` / constant-equivalent `l_s` direct-sum geometry, and because Gaussian concentration controls each block using its coefficient-space Lipschitz radius.

## 5. Insert the best general block theorem

BGJLR Theorem 1.2 yields, in dimension `b` and `p<2r`, a type-2 estimate of the form

```text
K_b <= C(r,p) b^gamma log(2b),
gamma = 1/2 - 1/(2r),                                 (5.1)
```

with only `r,p`-dependent changes when passing to the source's symmetric normalization. To see that the Rademacher formulation also controls the present Gaussian series, write `g_i=epsilon_i |g_i|`, condition on the magnitudes, apply the Rademacher type-2 inequality, and then use Cauchy/Jensen:

```text
E_g ||sum_i g_i A_i||
 <= C_type E [sum_i |g_i|^2 ||A_i||^2]^(1/2)
 <= C_type [sum_i E g_i^2 ||A_i||^2]^(1/2)
 = C_type [sum_i ||A_i||^2]^(1/2).
```

Combining (5.1) with Theorem 4.1 proves the following source-normalized structured theorem.

### Corollary 5.1 — polynomially growing arbitrary blocks

For every block-direct-sum family above and `2<=p<2r`,

```text
E ||sum_i g_i T_i||_{I_p}
 <= C(r,p) [b^gamma log(2b) + sqrt(log(2m))] S,
                                                       2<=p<=r,
```

and

```text
E ||sum_i g_i T_i||_{I_p}
 <= C(r,p) [b^gamma log(2b) + 1] S,
                                                       r<p<2r.
```

This is stronger than inserting ambient dimension `d` into the generic type-2 theorem whenever `b<<d`.

## 6. Dimension-exponent gain

Put `b=d^beta`. The new polynomial loss is `d^(beta gamma)` rather than `d^gamma`. Therefore the conjectured full-source exponent `d^alpha` is already sufficient for this block class whenever

```text
beta gamma <= alpha.
```

Equivalently,

```text
beta <= beta_* := alpha/gamma
                 = r(p-2) / [p(r-1)].                 (6.1)
```

Consequences:

- At `p=2`, `alpha=0`; polynomially growing blocks are not covered at the conjectured dimension exponent by (5.1), but `b=polylog(d,n)` is compatible with Conjecture 16 up to its allowed polylogarithms.
- For every `p>2`, (6.1) allows **polynomially growing arbitrary dense blocks**, not just rank-one or independent-entry tensors.
- Example: `r=3,p=3` gives `beta_*=1/2`; arbitrary symmetric tensors inside blocks of dimension up to about `d^(1/2)` satisfy the conjectured ambient dimension exponent (up to logs).
- As `p -> 2r` from below, `beta_* -> 1`, coherently matching the already known `p>=2r` regime.

This is the run's measurable structural gain: the source target is now proved for a correlated block-direct-sum class with block growth exponent up to `beta_*`, while the arbitrary-tensor exponent gap remains open.

## 7. What remains: cross-block interactions are the real obstruction

An arbitrary symmetric tensor is not block diagonal. Relative to a coordinate partition, its coefficients split across `r`-tuples of blocks. Think of those nonzero block patterns as hyperedges of an `r`-uniform interaction hypergraph.

A **matching** of this interaction hypergraph consists of hyperedges with disjoint coordinate-block unions. After grouping the at most `r` coordinate blocks in each hyperedge into one superblock, a matching layer falls under the direct-sum theorem above with local dimension at most `rb`.

This gives a concrete route from the theorem to arbitrary tensors, but it also exposes the next obstruction sharply: a dense `r`-uniform interaction hypergraph can require on the order of `m^(r-1)` matching layers. Summing those layers by the triangle inequality would reintroduce a disastrous polynomial factor. This is a combinatorial form of the same volumetric barrier seen in Section 2.

So the next missing statement is **not** another per-block estimate. It is a way to combine many cross-block interaction layers by square-function/chaining geometry rather than by `l_1` summation.

## 8. Next attack

The next run should target one of the following equivalent-looking bridges and try to refute it before relying on it:

1. **Randomized matching-layer square function.** For a decomposition into interaction-matchings `T_i=sum_ell T_i^(ell)`, seek a source-normalized inequality whose loss depends on a square function

   ```text
   (sum_ell S_ell^2)^(1/2),
   S_ell^2=sum_i ||T_i^(ell)||_{I_p}^2,
   ```

   rather than `sum_ell S_ell`.

2. **Scale-dependent hyperedge sparsification.** In a Dudley/generic-chaining decomposition, sparsify the interaction hypergraph separately at each metric scale so only near-disjoint hyperedges survive, then apply Corollary 5.1 locally. The required statement must preserve the canonical Gaussian metric, not merely coefficient Frobenius mass.

3. **Decoupled cross-block process.** Polarize the symmetric process to `r` independent block variables, use a random coloring to turn a positive fraction of cross-block monomials into disjoint-part interactions, and ask whether repeated decoupling can recover them with an `l_2` rather than `l_1` layer cost.

A successful bridge must avoid a factor polynomial in the number of matching layers. The diagonal tensor `A_q` from Section 2 should remain the first stress test for any proposed square-function lemma.

## 9. Obligation ledger

```text
O1  Exact source normalization recovered.                         DONE
O2  Strongest generic low-p polynomial exponent recovered.       DONE
O3  Universal Frobenius-collapse shortcut tested/refuted.        DONE
O4  Correlated arbitrary-within-block direct-sum theorem.        DONE (PROVED PARTIAL)
O5  Target exponent for b=d^beta, beta<=beta_*.                  DONE (for block-direct-sum class)
O6  Cross-block matching-layer square-function inequality.       OPEN
O7  Arbitrary deterministic symmetric tensors, 2<=p<2r.          OPEN
O8  Full Conjecture 16.                                           OPEN
```

No closure is claimed. No independent review is requested as a prerequisite to continuing the mathematics.

## 10. Continuity notes

The registered P09 role already exists in `operations/progress_first_2026-09-20/REGISTRY.md`; this report therefore does not create or steal a canonical source owner. I also inspected the contemporaneous RS-2026-CL-A Gaussian/Hermite handoff. Its low-degree-to-Ornstein--Uhlenbeck bridge is complementary but does not supply the cross-block tensor square-function inequality needed here, so it was not duplicated.

Old C0035 history remains untouched. This is the first immutable report under the new P09 chaining root and starts a fresh P09 mathematical obligation ledger rather than reviving the retired C0035 route.
