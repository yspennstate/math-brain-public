Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT in the frozen metric: external/source-verified `p_comb <= 2 -> <= 2`, while the track's written candidate `p_comb <= 1 -> <= 1` remains pending independent validation. Methods B9/B14/B25.**

# HARD7-02 — randomize the scalar shift into an independent matching

Status: **PARTIAL / SOURCE CONJECTURE OPEN.** This run does not claim Conjecture 3.9, does not promote the pending `p_comb<=1` argument, and does not claim publication priority. It develops a genuinely different route to the sub-logarithmic regime.

## 1. Continuity, ownership, source and runtime checks

I resumed the exclusive claim

`operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`

and did not return to the released Han target. Before doing mathematics I re-read the HARD7 control file, the two new-methods owner/control files, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the current claim, the newest HARD7-02 report, and the neighboring C0031/C0032 non-Hermitian/heavy-tail records. I also repeated targeted searches over the `probability_1000_intake_*/problems.jsonl` corpus and exact target aliases. The connector truncates those large JSONL files, so this is targeted intake recovery, not a fictitious claim that every one of roughly 780 entries was semantically re-read in full. No ownership collision, release, posted-paper collision, or equivalent Bernoulli-singularity claim was found.

The source remains Dongbin Li, Alexander E. Litvak and Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2, revised 11 August 2026. Conjecture 3.9 asks, in the independent-row fixed-row-sum model, whether `d(n)->infinity` alone implies the circular law. Corollary 1.4 proves the current published/source regime `d >= (log n)^(2+eps)`, `d=o(n)`. The same paper explicitly notes that the `C log n` least-singular-value threshold is forced at `z=0` by zero columns. Fresh searches on 20 September 2026 located no later theorem settling Conjecture 3.9 or lowering the circular-law condition for this exact model.

The nearest solved problem I re-read is Litvak--Lytova--Tikhomirov--Tomczak-Jaegermann--Youssef, *Circular law for sparse random regular digraphs*, arXiv:1801.05576. In the doubly regular model they obtain the circular law for `d->infinity`; their key sparse input is a random-normal/product-structure argument for intermediate singular values. That paper is especially relevant here because the new representation below manufactures an exact product-like matching variable while retaining the easier independent-row law.

A search also recovered Ben Arous--Dang, *Smallest Singular Value for Perturbations of Random Permutation Matrices*, arXiv:1404.3954. Its stated perturbation theorem concerns a random permutation plus a diagonal perturbation; I found no theorem in this search that can simply be quoted for an arbitrary matrix `M-lambda P`. Thus the representation below is not being mislabeled as a solved invertibility theorem.

Runtime/capability status is unchanged. The native scheduling interface exposed to this workflow has title/prompt/schedule/timing/enabled controls, but no model selector, reasoning selector, authenticated reasoning telemetry, or guaranteed run duration. Therefore GPT-6/maximum remains prompt-requested only. The earlier P26 `You cannot modify this task` incident cannot be repaired by a repository edit; the legitimate workaround is an authorized owner/workspace scheduling context or platform support, not permission bypass or a duplicate task. I made no scheduler modifications this run.

## 2. Frozen metric

The fixed quantity is

`p_comb = inf { p>=0 : for every eps>0, the circular law is rigorously established in the frozen row-combinatorial model whenever d >= (log n)^(p+eps) and d=o(n) }`.

The two evidence levels remain separated:

- external/source-verified: `p_comb <= 2` before and after;
- current HARD7-02 written candidate, still awaiting independent validation: `p_comb <= 1` before and after.

Hence this run is **no movement** in the metric. It is the second unchanged run after the `<=1` candidate movement, so Section I is not yet triggered.

## 3. New idea before any checker

The previous run showed that Hilbert--Schmidt/ridge transport reaches every `d->infinity` but cannot by itself remove the ridge because nonnormal pseudospectra are unstable. The regular-digraph literature suggests that the missing ingredient should be product structure in the normals-to-rowspaces argument.

The fixed-row-sum ensemble has a symmetry that seems not to have been used in the preceding HARD7-02 route: because its law is invariant under **independent row and column permutations**, the deterministic scalar shift can be converted, in distribution and without approximation, into an **independent uniform perfect matching**. This provides fresh randomness exactly where `z=0` loses invertibility because of zero columns.

The three moves are:

- **B14 (find the group acting):** exploit the `S_n x S_n` action on the row-slice ensemble;
- **B9 (randomize):** turn `lambda I` into `lambda P` with `P` uniform and independent of the matrix;
- **B25 (count the same thing twice):** count compatible residual matchings to recover exponential block anti-concentration from coordinate-level spread.

No code was written. The claims below are analytic/all-dimensional and are proved on the page; manufacturing a small finite checker would not test the actual obstruction.

## 4. Exact independent-matching representation

Let `M` be the `n x n` row-combinatorial matrix: its rows are independent and each is uniform on the binary vectors with exactly `d` ones. Let `lambda in C` be arbitrary.

### Theorem 4.1 (bi-permutation decoupling)

There exists a pair `(M',P)` such that

1. `M'` has exactly the same law as `M`;
2. `P` is a uniform `n x n` permutation matrix;
3. `M'` and `P` are independent; and
4. the complete singular-value vector satisfies

`sv(M-lambda I) =_d sv(M'-lambda P)`.

The same equality in distribution holds for every measurable function of the singular values, including ridge log determinants and least singular values.

#### Proof

Let `R,C` be independent uniform permutation matrices, independent of `M`. Since the row laws are iid and each row law is invariant under coordinate permutations,

`R M C =_d M`.

Permutation matrices are unitary, hence

`sv(M-lambda I)=sv(R(M-lambda I)C)=sv(RMC-lambda RC)`.

Put `P=RC` and `M'=RMC`. It remains only to verify the independence, because marginal invariance alone is not enough. For any event `A` in matrix space and any fixed permutation matrix `p`,

`P(M' in A, P=p)`
` = sum_{r c=p} P(R=r,C=c) P(r M c in A)`
` = n! * (n!)^{-2} * P(M in A)`
` = P(M in A)/n!`.

Here every term has the same matrix probability by left/right invariance, and there are exactly `n!` factorizations `p=rc`. This factors as `P(M in A) P(P=p)`, proving independence. ∎

For the normalized circular-law shift, one takes

`lambda = z sqrt(d(1-d/n))`.

For every fixed `z != 0`, `|lambda|` is of order `sqrt(d)`. The zero-column obstruction at `z=0` is therefore not transported into an exact zero column: the independent matching contributes one nonzero `-lambda` entry to every row and every column.

## 5. Exact residual product structure under row exposure

The representation remains useful after conditioning.

### Lemma 5.1 (residual matching law)

Let `I` be any set of exposed rows and write

`T = [n] \ P(I)`.

Conditional on the values `P(i)` for `i in I`, the restriction of `P` to `I^c` is a uniform bijection

`I^c -> T`.

Moreover, this residual bijection is independent of all unexposed matrix rows `{M_i : i in I^c}`, which remain independent uniform `d`-slice rows.

#### Proof

This is exact counting for a uniform permutation: after fixing `|I|` images, each of the `(n-|I|)!` bijections between the two residual sets is equally likely. Independence from the matrix rows follows from Theorem 4.1 and row independence. ∎

Thus, if `E` is the span of the already exposed shifted rows and `v` is any unit vector in `E^perp` measurable from the exposed sigma-field, then the next unexposed shifted row has the form

`R - lambda e_J`,

where `R` is a fresh uniform `d`-slice row and `J` is a fresh uniform element of the residual column set, independent of `R` at that exposure step.

## 6. A second anti-concentration mechanism that costs no `sqrt(d)` conditioning factor

For a complex random variable `X`, set

`L(X,t)=sup_a P(|X-a|<=t)`.

For a finite coordinate set `T` and vector `v`, define the level concentration profile

`q_T(v,r)=sup_a |{j in T : |v_j-a|<=r}|/|T|`.

### Lemma 6.1 (two-source one-row bound)

In the setting of Lemma 5.1, for every `t>0`,

`P(dist(R-lambda e_J,E)<=t | exposed data)`
` <= min( L(v^* R,t), q_T(v,t/|lambda|) )`                         (6.1)

for every exposed-data-measurable unit normal `v in E^perp`, provided `lambda != 0`.

#### Proof

The distance event implies

`|v^*(R-lambda e_J)|<=t`.

Conditional on the exposed data, `v^*R` and `-lambda conj(v_J)` are independent. For independent complex random variables `X,Y`, conditioning first on `Y` and then on `X` gives the elementary convolution inequality

`L(X+Y,t)<=min(L(X,t),L(Y,t))`.

For `J` uniform on `T`, the concentration function of `lambda conj(v_J)` is exactly bounded by `q_T(v,t/|lambda|)`. ∎

This matters because the source's fixed-slice comparison to iid Bernoulli produces a `sqrt(d)` conditioning prefactor. The matching term in (6.1) has **no such prefactor**. Whenever a normal has many coordinate levels on the residual set, the shift itself supplies anti-concentration.

There is also a complementary flat-mode identity. If `v=c 1+w`, then for every slice row `R` and every matching coordinate `J`,

`v^*(R-lambda e_J)=conj(c)(d-lambda)+w^*R-lambda conj(w_J)`,

hence deterministically

`|v^*(R-lambda e_J)|`
` >= |c| |d-lambda| - (sqrt(d)+|lambda|) ||w||_2`.                  (6.2)

In particular, the exactly constant normal is not a small-ball obstruction for a fixed circular-law shift `z != 0`: its scalar projection is the nonzero deterministic number `conj(c)(d-lambda)`, and `|d-lambda|~d` as `d->infinity`.

The prospective dichotomy is therefore structurally clean:

- non-flat residual normal -> matching-level anti-concentration (6.1);
- sufficiently flat normal -> row-sum/shift separation (6.2).

The unresolved middle/sparse-normal regime is recorded below rather than hidden.

## 7. B25: exact block counting for the residual matching

The main advantage over a fresh independent coordinate is that the matching entropy survives for an entire unexposed block.

Let `U,T` have the same cardinality `r`, and let `pi:U->T` be a uniform bijection. Suppose that after conditioning on every variable except this residual matching, each row `i in U` has a compatibility set `A_i subset T` with

`|A_i| <= s < r`.

### Lemma 7.1 (compatible-matching bound)

One has the exact elementary bound

`P(pi(i) in A_i for every i in U)`
` <= s^(r-s) s! / r!`.                                           (7.1)

Consequently, if `s/r -> q` with a fixed `0<q<1`, then

`log P(all compatible) <= r [log q + 1-q] + O_q(log r)`,            (7.2)

and `log q+1-q<0`.

#### Proof

Fix any ordering of the rows. During the first `r-s` exposures, before choosing the image of row number `k+1`, there are `r-k` available columns while at most `s` of them can lie in that row's compatibility set. Therefore

`P(first r-s constraints all hold)`
` <= product_{k=0}^{r-s-1} s/(r-k)`
` = s^(r-s) s!/r!`.

The remaining `s` constraints have conditional probability at most one, proving (7.1). Stirling's formula gives (7.2). ∎

Applied to shifted rows, after fixing the fresh slice rows and a normal `v`, take

`A_i={j in T: |v^*R_i-lambda conj(v_j)|<=t}`.

If `q_T(v,t/|lambda|)<=q<1`, every compatibility set has size at most `qr`, and (7.1) gives exponential block suppression without demanding independent shift coordinates. This is the precise product structure that the regular-digraph proof had to manufacture by a substantially more elaborate switching/random-normal construction.

## 8. A large sub-logarithmic base block where the random shift provably dominates

The matching representation also gives a rigorous base case below the source's `C log n` least-singular-value range.

Fix `z != 0` and write

`lambda=z sqrt(d(1-d/n))`.

Let

`K=floor(|lambda|/4)`

and, for large enough `n` so that `K>=1`, define

`mu_*=(K/e) n^(-4/K)`,
`m_*=floor(n mu_*/d)`.

For `d->infinity`, `d=o(n)`, one has `m_*->infinity` and

`m_*/n = d^(-1/2) n^(-O_z(1/sqrt(d)))`                              (8.1)

up to `z`-dependent constants.

Take any deterministic row set `I` of size `m_*` and let `J=P(I)`. Then the `m_* x m_*` matching-aligned minor is

`H_{I,J}=M_{I,J}-lambda P_{I,J}`,

where `P_{I,J}` is itself a permutation matrix.

### Proposition 8.1 (shift-dominated matching-aligned base minor)

With probability at least `1-2n^{-3}` for all large `n`,

`s_min(H_{I,J}) >= 3|lambda|/4`.                                  (8.2)

#### Proof

Conditional on `P`, `J` is fixed and independent of `M`. Each row degree of the binary block `M_{I,J}` is hypergeometric with mean

`d m_*/n <= mu_*`,

and each column degree is binomial `Bin(m_*,d/n)` with the same mean bound, because the matrix rows are independent. The standard hypergeometric/binomial Chernoff bound gives, for either kind of degree `D`,

`P(D>=K) <= (e mu_*/K)^K = n^{-4}`.

A union bound over at most `2m_*<=2n` row/column degrees shows that, with probability at least `1-2n^{-3}`, every row and column degree of `M_{I,J}` is `<K`. Hence

`||M_{I,J}||_2 <= sqrt(||M_{I,J}||_1 ||M_{I,J}||_infty) < K <= |lambda|/4`.

Since `P_{I,J}` is unitary,

`s_min(M_{I,J}-lambda P_{I,J}) >= |lambda|-||M_{I,J}||_2 >= 3|lambda|/4`.

Finally `K` is a positive constant multiple of `sqrt(d)` and tends to infinity; taking logarithms in the definition of `m_*` gives (8.1), hence `m_*->infinity`. ∎

This is not a circular-law theorem and does not move `p_comb`. It is, however, a genuinely sub-logarithmic invertibility statement at every fixed `z!=0`, valid for a large `n^{1-o(1)}` matching-aligned minor even when `d` grows arbitrarily slowly.

## 9. Attack the new route: the exact obstruction is now recursive, not zero columns

The group trick does **not** by itself prove invertibility. An arbitrary residual normal can be supported almost entirely outside the remaining matching set `T`; then `q_T(v,r)` can equal one and (6.1) supplies no gain. This is a real obstruction, not a missing union bound.

For the actual shifted rowspace there is a useful exact interpretation. Let `I` be the exposed rows and `T=[n]\P(I)`. Reorder the used columns `P(I)` and write the exposed block as

`H_I = [ B  C ]`,

where

`B=M_{I,P(I)}-lambda P_{I,P(I)}`

is square. A normal `v=(v_{P(I)},v_T)` satisfies

`B v_{P(I)} + C v_T = 0`.                                         (9.1)

Therefore:

- a nonzero normal with `v_T=0` exists **iff** the smaller shifted block `B` is singular;
- if `B` is invertible, then
  `||v_{P(I)}|| <= ||B^{-1}C|| ||v_T||`.

So the worst failure of matching anti-concentration is equivalent to a **smaller shifted-invertibility problem**. Proposition 8.1 gives a genuine terminal scale at which this recursion is easy because the `lambda P` term dominates the sparse block.

This suggests a multiscale proof architecture absent from the previous ridge route:

1. randomize the shift by Theorem 4.1;
2. expose rows in blocks while retaining a residual uniform matching;
3. use random normals plus Lemma 7.1 whenever the normal has coordinate spread on the residual set;
4. if the normal localizes away from that set, use (9.1) to descend to the smaller matching-aligned shifted block;
5. terminate the descent at the scale `m_*` of Proposition 8.1.

The missing theorem is now sharply isolated: one needs a quantitative statement that this descent either acquires residual coordinate spread often enough to control the logarithmic singular-value tail, or reaches the shift-dominated base scale without paying a non-summable loss.

## 10. Relation to the closest solved proof

The 2018 sparse random-regular-digraph paper explains that its decisive new ingredient is to inject randomness, choose random Gaussian normals to rowspaces, prove those normals are typically unstructured, and then recover anti-concentration for intermediate singular values. In the present row-combinatorial model, Theorem 4.1 gives an **exact independent perfect matching** for free. Lemma 7.1 then converts coordinate spread of a normal directly into exponential block suppression.

What is still absent is the analogue of their structural theorem on random normals, now adapted to the residual set `T` and to the recursion (9.1). This is materially narrower than the previous vague obligation "prove a better least-singular-value theorem below log n".

## 11. What the three moves accomplished

- **B14 — FIND THE GROUP ACTING:** succeeded. The `S_n x S_n` symmetry gives the exact independent-shift representation `M-lambda I =_sv M'-lambda P`.
- **B9 — RANDOMIZE:** succeeded at the structural level. Residual row exposure retains a uniform matching independent of fresh slice rows, adding a second anti-concentration mechanism with no `sqrt(d)` conditioning prefactor.
- **B25 — COUNT THE SAME THING TWICE:** succeeded. Direct residual-matching counting yields (7.1), an exponential block bound whenever a normal has nontrivial coordinate-level spread.

The route did **not** move `p_comb` because the random-normal spread/recursive-gluing theorem is not yet proved. The base-scale Proposition 8.1 and the recursion identity (9.1) are the main new pieces to carry forward.

## 12. Next checkpoint if this target continues

Do not return to ridge-transport bookkeeping next run. Attack the recursive gluing statement directly with three different unused moves. The most promising next triple is:

- **B3:** prove a stronger invariant combining residual coordinate spread with the condition number of the square block `B`;
- **B13:** seek a monovariant along the block descent, such as normalized residual leverage `tr(Q_{TT})/|T|`;
- **B29:** compactify the recursion by treating the terminal `m_*` block as the boundary point at infinity/zero residual fraction.

A concrete target is to prove that for a Gaussian random normal `v` to the exposed shifted rowspace, either

`q_T(v,c/(√|T|)) <= 1-kappa`

with fixed `c,kappa>0`, or the square block `B` in (9.1) has a quantitatively small singular value. The latter branch can then be iterated until Proposition 8.1 rules it out. If this dichotomy closes with summable losses, it would give a route to the a.e.-`z` logarithmic uniform-integrability estimate below `C log n`, which is exactly the regime the current `p_comb<=1` candidate cannot reach.

## 13. Ledger delta for coordinator consumption

`HARD7-02 | Li--Litvak--Yu Conjecture 3.9, row-combinatorial circular law | external p_comb: <=2 -> <=2; written candidate <=1 -> <=1 (pending independent validation) | PARTIAL / SOURCE OPEN | new independent-permutation-shift + residual-matching block route; shift-dominated base minor proved`

No shared root ledger, peer track, claim owner, scheduler, email, Drive, workflow, or public repository was modified.