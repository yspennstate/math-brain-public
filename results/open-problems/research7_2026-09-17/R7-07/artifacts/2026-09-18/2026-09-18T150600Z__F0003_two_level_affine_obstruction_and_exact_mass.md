Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — two-level affine obstruction to pointwise growing-modulus mixing, and its exact aggregate mass

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside source: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Section 5 immediately after Theorem 5.2.  
Frozen source-matching cubic metric:

\[
a_3:=\sup\{a:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative value entering this artifact: `a_3>=1/4`. Nothing below changes that value. The point of this run is instead to test, and if necessary destroy, the proposed growing-modulus route before spending another run trying to prove a false uniform statement.

Methods: **B20 FIND WHY THE ALGORITHM FAILS / B28 REPLACE FOR ALL WITH TYPICAL / B3 PROVE SOMETHING STRONGER.**

---

## 1. Idea before code

The preceding run reduced real singularity to cyclic cokernel-surjection moments and proposed controlling

\[
\rho_Q(n)
:=
\sup_{\substack{y\in(\mathbb Z/Q\mathbb Z)^n\\
\sum_i y_i=0,\ \operatorname{MinCos}(y)=\mathbb Z/Q\mathbb Z}}
Q^{n-1}\Pr(A_{n,3}y=0).
\tag{1.1}
\]

If `rho_Q(n)=n^{o(1)}` held for `Q=n^{1/3-o(1)}`, then the preceding surjection inequality would give `a_3>=1/3-o(1)`.

The first task this run was therefore not to prove (1.1), but to try to break it. It breaks dramatically.

There are full-affine-span, zero-sum vectors taking only **two residue values** for which `A y=0` is equivalent to a fixed equitable `1:2` cut in a cubic graph. For a fixed vector, that event has probability only `Theta(sqrt(n)(4/9)^n)`, exponentially small but enormously larger than `Q^{-n}` when `Q` grows polynomially. Thus no pointwise `Q^{-(n-1)} n^{o(1)}` estimate can hold on all full-affine-span rows.

The useful fact is that this does **not** kill the averaged cokernel route. The total number of such two-level rows is only `phi(Q) * binom(n,n/3)`, and their complete contribution to the surjection moment is exponentially small:

\[
\mathbb E S_Q^{(2)}(A)
=
\Theta\!\left(\varphi(Q)\left(\frac{2^{4/3}}3\right)^n\right).
\tag{1.2}
\]

Since `2^(4/3)/3 < 1`, polynomially growing `Q` costs nothing here. The correct next object is therefore an **average stratified by residue-profile entropy**, not the supremum (1.1).

---

# 2. B3 — a complete two-level classification, first for general fixed degree

The cubic statement becomes clearer as a special case of a deterministic `d`-regular lemma.

### Theorem 2.1 — two-level modular null rows are equitable cuts

Let `G` be a finite `d`-regular multigraph with adjacency matrix `A`, let `Q>d` and `gcd(d,Q)=1`, and let

\[
y_i=\alpha+u\,1_{\{i\in S\}}
\qquad (i=1,\dots,n),
\tag{2.1}
\]

where `u` is a unit modulo `Q` and both `S` and its complement are nonempty. Then `Ay=0 mod Q` if and only if there is one integer `k in {1,...,d-1}` such that

\[
d\alpha+k u=0\pmod Q
\tag{2.2}
\]

and every vertex has exactly `k` incident neighbour-stubs landing in `S`. Necessarily

\[
|S|=\frac{k}{d}n.
\tag{2.3}
\]

Conversely, whenever (2.3) is integral and every vertex has exactly `k` neighbour-stubs in `S`, taking

\[
\alpha=-k d^{-1}u\pmod Q
\tag{2.4}
\]

gives `Ay=0` and `sum_i y_i=0`.

#### Proof

For a vertex `v`, let `j(v)` be the number of its `d` incident neighbour-stubs whose opposite endpoint lies in `S`. Then

\[
(Ay)_v=d\alpha+j(v)u.
\tag{2.5}
\]

Because `u` is a unit and `Q>d`, the `d+1` residues

\[
d\alpha,\ d\alpha+u,\dots,d\alpha+du
\]

are pairwise distinct modulo `Q`. Hence if `(Ay)_v=0` for every `v`, there is a unique integer `k in {0,...,d}` such that `j(v)=k` for every vertex. Since both residue classes in (2.1) are nonempty, `k=0` would force no edge-stub to hit `S` and `k=d` would force every edge-stub to hit `S`; either contradicts `d`-regularity and nonemptiness of both sides. Thus `1<=k<=d-1` and (2.2) holds.

Now count directed incidences whose endpoint lies in `S` in two ways. Every one of the `n` vertices sends exactly `k` such incidences, so their number is `kn`. Every vertex of `S` receives exactly `d` incidences, so the same number is `d|S|`. This proves (2.3).

Conversely, if every vertex has exactly `k` neighbours in `S`, then (2.5) and (2.4) give `Ay=0`. Moreover

\[
d\sum_i y_i
=d(n\alpha+|S|u)
=n(d\alpha)+d|S|u
=-nku+nku=0.
\]

Since `d` is invertible modulo `Q`, `sum_i y_i=0`. QED.

### Corollary 2.2 — exact cubic normal form

Assume now `d=3`, `Q>3`, and `3` is invertible modulo `Q`. Every two-valued, full-affine-span, zero-sum row `y` that can satisfy `A y=0` is, after naming its smaller residue class `S`, uniquely of the form

\[
|S|=\frac n3,
\qquad
 y_i=
\begin{cases}
 2u/3,&i\in S,\\
 -u/3,&i\notin S,
\end{cases}
\qquad u\in(\mathbb Z/Q\mathbb Z)^\times,
\tag{2.6}
\]

and `Ay=0` is equivalent to

\[
\boxed{\text{every vertex has exactly one neighbour in }S.}
\tag{2.7}
\]

The alternative `k=2` is the same row after replacing `S` by its complement and `u` by `-u`. Thus the canonical choice is always the `n/3` class.

The difference of the two values in (2.6) is the unit `u`, so the coordinates generate all of `Z/QZ`; these rows are genuinely surjective cokernel test maps, not subgroup-coset aliases.

---

# 3. B20 — exact failure of the pointwise mixing algorithm

Work in the cubic configuration model on `n` labelled vertices, with `3n` half-edges paired uniformly. A cubic graph requires `n` even. The event (2.7) also forces `n/3` even, hence `n` is a multiple of `6`; write `n=6m`.

Fix `S` with `|S|=n/3`, and let `E_S` be the event that every vertex has exactly one neighbour in `S` (counting incident stubs in the configuration model). We count all pairings realizing `E_S`.

* At each vertex of `S`, choose its unique stub whose partner also lies in `S`: `3^(n/3)` choices.
* Pair those `n/3` chosen `S`-stubs: `(n/3-1)!!` choices.
* At each vertex outside `S`, choose its unique stub whose partner lies in `S`: `3^(2n/3)` choices.
* Pair the remaining `2n/3` stubs of `S` bijectively with those selected outside stubs: `(2n/3)!` choices.
* Pair the remaining `4n/3` outside stubs among themselves: `(4n/3-1)!!` choices.

Since the total number of pairings is `(3n-1)!!`,

\[
\boxed{
\Pr_{\rm conf}(E_S)
=
\frac{3^n (n/3-1)!!\,(2n/3)!\,(4n/3-1)!!}{(3n-1)!!}.
}
\tag{3.1}
\]

For `n=6m`, use `(2r-1)!!=(2r)!/(2^r r!)` to rewrite (3.1) exactly as

\[
\Pr_{\rm conf}(E_S)
=
3^{6m}2^{4m}
\frac{(2m)!(8m)!(9m)!}{m!(18m)!}.
\tag{3.2}
\]

Stirling's formula now gives

\[
\boxed{
\Pr_{\rm conf}(E_S)
\sim
4\sqrt{\frac{\pi n}{6}}
\left(\frac49\right)^n.
}
\tag{3.3}
\]

The exponential base is exact: after cancelling the `n log n` and linear terms, the remaining exponential factor is

\[
3^n\times(1/3)^{n/6}\times(2/3)^{2n/3}\times(4/3)^{2n/3}\times 3^{-3n/2}
=(4/9)^n.
\]

### Passing to the uniform simple cubic graph

Conditioned on `E_S`, the `S-S` part is a perfect matching with one participating stub per `S` vertex and is automatically simple. The cross part is also automatically simple because every outside vertex has cross-degree one. The only possible loops or parallel edges are in the outside-outside pairing, where every outside vertex has exactly two remaining stubs. Hence

\[
\Pr_{\rm conf}(\text{Simple}\mid E_S)
\to e^{-3/4},
\tag{3.4}
\]

the standard fixed-degree configuration-model simplicity constant for degree `2`. Unconditionally, for cubic configurations,

\[
\Pr_{\rm conf}(\text{Simple})\to e^{-2}.
\tag{3.5}
\]

Therefore for the uniformly random **simple** cubic graph,

\[
\boxed{
\Pr_{\rm simple}(E_S)
\sim
4e^{5/4}\sqrt{\frac{\pi n}{6}}
\left(\frac49\right)^n.
}
\tag{3.6}
\]

Only the `Theta(sqrt(n)(4/9)^n)` form is needed below; the constants in (3.4)-(3.6) are included because the factorization makes them explicit.

### Corollary 3.1 — the proposed pointwise `rho_Q` theorem is false

Take the canonical row (2.6) for this fixed `S`. It is zero-sum and full affine span, and by Corollary 2.2 its null event is exactly `E_S`. Hence

\[
\rho_Q(n)
\ge
Q^{n-1}\Pr_{\rm simple}(E_S)
=
Q^{n-1}\Theta\!\left(\sqrt n\,(4/9)^n\right).
\tag{3.7}
\]

If `Q=n^{theta+o(1)}` for **any fixed `theta>0`**, then

\[
\log\rho_Q(n)
=\theta n\log n+n\log(4/9)+o(n\log n),
\tag{3.8}
\]

so `rho_Q(n)` is vastly larger than `n^{o(1)}`. In particular the preceding run's proposed pointwise milestone at `theta=1/3-o(1)` is impossible.

This is not a flaw in the exact surjection inequality. It pinpoints the flaw in the proposed *way of estimating its expectation*: full affine span does not imply a flat residue profile. A row can use two residues differing by a unit and still span the entire cyclic group.

---

# 4. B28 — the bad pointwise family is exponentially negligible after averaging

Let

\[
S_Q^{(2)}(A)
=
\#\{y:(\mathbb Z^n/A\mathbb Z^n)\twoheadrightarrow\mathbb Z/Q\mathbb Z:\ y\text{ uses exactly two residue values}\}.
\tag{4.1}
\]

Corollary 2.2 gives an exact parametrization of every row in (4.1) that can contribute. Choose

1. its canonical `n/3` class `S`, in `binom(n,n/3)` ways;
2. the unit difference `u`, in `phi(Q)` ways.

Then (2.6) determines the row uniquely. Consequently

\[
\boxed{
\mathbb E S_Q^{(2)}(A)
=
\varphi(Q)\binom n{n/3}\Pr_{\rm simple}(E_S).
}
\tag{4.2}
\]

Using

\[
\binom n{n/3}
\sim
\frac{3}{2\sqrt{\pi n}}
\exp\{nH(1/3)\},
\qquad
H(1/3)=\log3-\frac23\log2,
\tag{4.3}
\]

and (3.6), we obtain the explicit asymptotic

\[
\boxed{
\mathbb E S_Q^{(2)}(A)
\sim
 e^{5/4}\sqrt6\,\varphi(Q)
\left(\frac{2^{4/3}}3\right)^n.
}
\tag{4.4}
\]

Indeed

\[
H(1/3)+\log(4/9)
=
\log\left(\frac{2^{4/3}}3\right),
\tag{4.5}
\]

and

\[
\frac{2^{4/3}}3=0.839947\ldots<1.
\]

Thus for every polynomially growing modulus, and in fact for every `phi(Q)=exp(o(n))`,

\[
\boxed{
\mathbb E S_Q^{(2)}(A)=e^{-c n+o(n)}
}
\tag{4.6}
\]

with

\[
c=\log3-\frac43\log2=0.174416\ldots>0.
\]

This is the exact distinction the pointwise supremum erased: an individual two-level row is much more likely than `Q^{-n}`, but there are exponentially too few such rows for the family to matter in the cokernel-surjection average.

---

# 5. What this says about the correct growing-modulus problem

The previous exact implication remains valid:

\[
\mathbf1_{\{\det A=0\}}
\le
\frac{|\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/Q\mathbb Z)|}{\varphi(Q)}.
\tag{5.1}
\]

But the moment must now be decomposed by residue-profile complexity:

\[
\mathbb E|\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/Q\mathbb Z)|
=
\mathbb E S_Q^{(2)}(A)
+
\mathbb E S_Q^{(\ge3)}(A).
\tag{5.2}
\]

Section 4 proves the first term is exponentially negligible. Therefore the next genuine question is not a pointwise estimate but

\[
\boxed{
\mathbb E S_Q^{(\ge3)}(A)=n^{o(1)}
\quad\text{for some }Q=n^{1/3-o(1)},
}
\tag{5.3}
\]

or a still finer entropy-stratified version of it.

The two-level calculation suggests the right statistic. If a residue profile has empirical entropy `H(q)`, then the number of rows with that profile is approximately `exp(nH(q))`. The null-pairing probability must be estimated on the **same exponential scale**, rather than by a uniform worst-case bound. For the exact two-level saddle `q=(2/3,1/3)`, the fixed-row pairing exponent is

\[
\log(4/9)=\log\binom31-3H(1/3),
\]

so after multiplying by the number of rows the residual exponent is

\[
\log3-2H(1/3)
=
\log(2^{4/3}/3)<0.
\tag{5.4}
\]

The uniform `Q`-residue profile is the opposite endpoint: candidate entropy is about `log Q` per coordinate, and a successful global moment theorem must show the null-pairing entropy cancels it to within `o(log n)` total loss. The hard regime is therefore the interpolation between very low-alphabet profiles such as Section 4 and nearly flat profiles already treated by fixed-group mixing/local-CLT machinery.

---

# 6. Exact failures and retained successes of the three methods

### B20 — FIND WHY THE ALGORITHM FAILS

**Succeeded decisively.** The attempted sequential `Q^{-1}`-per-row smoothing cannot be uniform because two-level full-affine rows have one deterministic admissible neighbour composition. Formula (3.7) is an explicit counterexample to the pointwise milestone.

### B28 — REPLACE FOR ALL WITH TYPICAL

**Succeeded for the first exceptional stratum.** Although the pointwise probability is exponentially larger than `Q^{-n}`, the exact total two-level surjection contribution is exponentially small by (4.4). Thus low-alphabet exceptions can in principle be removed by an aggregate entropy argument rather than controlled pointwise.

### B3 — PROVE SOMETHING STRONGER

**Succeeded as a structural theorem.** Theorem 2.1 classifies every two-level modular null row of every fixed-degree regular graph as an equitable cut, and the cubic specialization yields the exact simple-graph asymptotic (3.6) and exact aggregate moment (4.4). This is stronger than merely exhibiting one counterexample row.

None of these results by itself changes the real-singularity exponent `a_3`; they correct the next route and identify the next honest averaged quantity.

---

# 7. Dated literature / source check — 2026-09-18

* **Primary source:** Van Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797. The source's sharp rare-event target is distinct from the now-solved qualitative nonsingularity conjecture.  
  https://arxiv.org/abs/2005.02797
* **Current status check:** MathDB's record refreshed in September 2026 states that qualitative nonsingularity is settled while the sharp singularity-probability exponent remains unknown. This is a secondary status source, not a novelty certificate.  
  https://mathdb.com/p/346391/the-nonsingularity-conjecture-for-random-regular-graph-adjac
* **Fixed-group mixing:** András Mészáros, *The distribution of sandpile groups of random regular graphs*, arXiv:1806.03736 / Trans. AMS 2020. Its group-distribution machinery is for fixed finite groups; it does not supply the growing-modulus aggregate theorem (5.3).  
  https://arxiv.org/abs/1806.03736
* **Adjacency cokernels:** Hoi H. Nguyen and Melanie Matchett Wood, *Cokernels of adjacency matrices of random r-regular graphs*, arXiv:1806.10068. This imports the fixed-group mixing into cokernel moments and qualitative nonsingularity, again not the polynomially growing cyclic target.  
  https://arxiv.org/abs/1806.10068
* **Recent neighboring work:** Yukun He and Jiaoyang Huang, *The oriented Kesten--McKay law for random regular digraphs*, arXiv:2609.05297 (submitted 2026-09-04), proves directed hard-edge/small-ball estimates. It is a directed model and does not resolve Vu's undirected sharp exponent.  
  https://arxiv.org/abs/2609.05297

A bounded fresh search found no later source-matching proof of `P(A_{n,d} singular)=n^{-d+2+o(1)}` for fixed undirected `d`. This remains negative evidence only.

---

# 8. Metric, status, and next mathematical object

Frozen metric before: `a_3>=1/4`.  
Frozen metric after: `a_3>=1/4`.  
Movement: **NO MOVEMENT**.

New exact auxiliary result: the proposed pointwise `rho_Q=n^{o(1)}` theorem is **REFUTED AS AN AUXILIARY ROUTE**, while the entire two-level exceptional family contributes only

\[
\Theta\!\left(\varphi(Q)(2^{4/3}/3)^n\right)
\]

to the cyclic surjection moment.

The source problem itself remains **PARTIAL / OPEN**. This artifact does not label F0003 refuted or proved.

The next correct obstruction is the averaged profile-stratified quantity (5.3), especially rows using at least three residues but still far from the equidistributed sector. Because this run is the third consecutive ordinary no-movement run for the frozen metric, the owner protocol requires the **next R7-07 run to be the thinking-only STUCK1 diagnosis**, not another ordinary lemma run.