Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0029: promotion to the rank-2 law, an exact path theorem, and the frontier free-energy representation

## 1. Source target and purpose of this artifact

The active source is Krzysztof Burdzy, *My favorite open problems*, Problem 9, “Do peaks of random labelings repell each other?”  For a uniformly random labeling of the `n x n` discrete square, conditioned on exactly two peaks, let `rho_n` be the graph distance between those peaks.  The source asks whether

\[
\rho_n/n\Longrightarrow 0.
\]

The frozen source metric is

\[
D_*:=\limsup_{n\to\infty}\mathbb E[\rho_n/n\mid\text{exactly two peaks}].
\]

This artifact does **not** determine `D_*`; it gives a new exact reduction.  The central point is that the true two-peak pair law is only a polynomial tilt of the much simpler law obtained by forcing the two peaks to carry the two largest labels.  That reduction is valid on every finite connected graph.  On a path, the rank-2 law is exactly solvable and already yields macroscopic separation after the polynomial tilt.  On the square, it isolates the remaining problem as a two-seed completion/free-energy estimate.

The three Section-B routes used here are:

- **B6 (deform to a solved geometry):** solve the rank-2 completion law exactly on the path;
- **B21 (import an analogous-field representation):** rewrite the completion count as a frontier-growth Feynman–Kac partition function;
- **B30 (localize the gluing failure):** promote the second birth to rank 2 and prove that putting it back changes pair weight by at most a factor `N-1`.

The earlier run's B2/B18/B25 triple is not repeated.

## 2. Descending reveal language

Let `G=(V,E)` be a finite connected simple graph with `|V|=N`.  A labeling is equivalent to a descending-label order

\[
\omega=(x_1,x_2,\ldots,x_N).
\]

A revealed vertex `x_k` is a **birth** when it has no neighbor among the already revealed vertices:

\[
N(x_k)\cap\{x_1,\ldots,x_{k-1}\}=\varnothing.
\]

As proved in the preceding R7-04 report, births are exactly peaks of the completed labeling.

For a nonempty seed set `T\subseteq V`, define `F(T)` to be the number of orders of `V\setminus T` that can be appended after the vertices of `T` have already been revealed, with no further birth.  Equivalently, writing `S` for the current revealed set, every next vertex must lie in

\[
\partial S:=\{x\notin S:N(x)\cap S\neq\varnothing\}.
\]

Thus

\[
F(V)=1,\qquad
F(T)=\sum_{x\in\partial T}F(T\cup\{x\}).
\tag{2.1}
\]

For two nonadjacent vertices `r,v`, let `W(r,v)` be the number of descending orders with exactly two births, first `r` and second `v`.  Here `r` is the global maximum; the label/rank of `v` is not prescribed.

If `r\sim v`, then they cannot both be peaks.  Hence only nonadjacent pairs matter below.

## 3. B30: promotion of the second birth to rank 2

### Theorem 3.1 (rank-2 promotion bound)

For every finite connected graph `G` and every ordered nonadjacent pair `(r,v)`,

\[
\boxed{F(\{r,v\})\le W(r,v)\le (N-1)F(\{r,v\}).}
\tag{3.1}
\]

Consequently, for the unordered pair weight

\[
H(\{r,v\}):=W(r,v)+W(v,r),
\]

we have

\[
\boxed{2F(\{r,v\})\le H(\{r,v\})\le 2(N-1)F(\{r,v\}).}
\tag{3.2}
\]

#### Proof

Take an order counted by `W(r,v)`.  Suppose the second birth `v` occurs at position `k`:

\[
\omega=(r,x_2,\ldots,x_{k-1},v,x_{k+1},\ldots,x_N).
\]

Because `v` is a birth, it has no neighbor among `r,x_2,\ldots,x_{k-1}`.  Define the **promotion map**

\[
\Phi(\omega)
=(r,v,x_2,\ldots,x_{k-1},x_{k+1},\ldots,x_N).
\]

We check that `\Phi(\omega)` has no birth after its first two vertices.

- For each `x_j` with `2\le j<k`, the original order already required `x_j` to have a neighbor among `r,x_2,\ldots,x_{j-1}`.  Promotion inserts `v` before `x_j` but removes none of those witnesses.
- For each vertex originally after `v`, its set of earlier vertices is unchanged as a set: only the position of `v` inside that earlier set changes.
- Since `r\not\sim v`, `v` at position 2 is indeed the second birth.

Thus `\Phi(\omega)` is a valid no-further-birth completion starting from the ordered seeds `(r,v)`.  The number of such promoted orders is exactly `F(\{r,v\})`.

Conversely, every promoted order itself is a preimage with `v` at position 2, so `\Phi` is surjective.  Given a promoted order, a preimage is completely determined by the position `k\in\{2,\ldots,N\}` to which `v` is demoted.  Therefore every fiber has size between `1` and `N-1`.  Summing fiber sizes proves (3.1).  Since `F(\{r,v\})=F(\{v,r\})`, adding the two ordered inequalities gives (3.2).  ∎

### Exact fiber statistic

The polynomial loss in (3.1) can itself be written exactly.  Let

\[
\sigma=(r,v,u_3,\ldots,u_N)
\]

be a promoted order counted by `F(\{r,v\})`.  Define

\[
J_v(\sigma):=\min\Big\{t\ge3:
\big(u_t\sim v\big)
\ \text{or}\ 
N(u_t)\cap\{r,u_3,\ldots,u_{t-1}\}=\varnothing
\Big\}.
\tag{3.3}
\]

The minimum exists: `v` has a neighbor somewhere among `u_3,\ldots,u_N` because `G` is connected and `r\not\sim v`.

If `v` is demoted to position `k`, the moved vertices `u_3,\ldots,u_k` must simultaneously satisfy two conditions:

1. none is adjacent to `v`, otherwise `v` ceases to be a birth;
2. each already has an earlier neighbor without using `v`, otherwise moving it before `v` creates an extra birth.

Hence the allowable positions are exactly

\[
k=2,3,\ldots,J_v(\sigma)-1,
\]

and the fiber size is

\[
h_v(\sigma)=J_v(\sigma)-2.
\tag{3.4}
\]

Therefore the exact ordered-pair weight is

\[
\boxed{
W(r,v)=\sum_{\sigma\in\mathcal G_{r,v}}h_v(\sigma)
=F(\{r,v\})\,\mathbb E_{\mathcal G_{r,v}}h_v,
}
\tag{3.5}
\]

where `\mathcal G_{r,v}` is the uniform set of rank-2 no-further-birth completions.  This identifies precisely what is lost by forcing the second peak to carry the second-highest label.

## 4. Polynomial equivalence of the true pair law and the rank-2 pair law

Let `\mathcal P` be the set of unordered nonadjacent vertex pairs.  Define the **rank-2 pair law**

\[
Q_G(A)
:=
\frac{\sum_{\{r,v\}\in A}F(\{r,v\})}
{\sum_{\{r,v\}\in\mathcal P}F(\{r,v\})},
\qquad A\subseteq\mathcal P,
\tag{4.1}
\]

and let `P_G` be the actual unordered peak-pair law conditioned on exactly two peaks.  Since the actual weight of `\{r,v\}` is `H(\{r,v\})`, (3.2) implies, for every event `A`,

\[
\boxed{
\frac{1}{N-1}Q_G(A)
\le P_G(A)
\le (N-1)Q_G(A).
}
\tag{4.2}
\]

This is a useful contiguity statement: the two measures can differ only by a polynomial factor, never by an exponential factor in `N`.

For the `n\times n` square, `N=n^2`, so if for some fixed `\varepsilon>0`

\[
Q_{G_{n,n}}\{d(r,v)\le\varepsilon n\}=o(n^{-2}),
\tag{4.3}
\]

then (4.2) gives

\[
P_{G_{n,n}}\{\rho_n\le\varepsilon n\}=o(1).
\]

In particular

\[
\liminf_{n\to\infty}
\mathbb E[\rho_n/n\mid\text{two peaks}]\ge\varepsilon,
\]

which refutes the source convergence.  Similarly, a rank-2 large-deviation bound against macroscopic separation stronger than `o(n^{-2})` would transfer to a YES proof.

Thus the source problem has been reduced to the spatial free energy of `F(\{r,v\})`, up to the harmless polynomial loss `n^2`.

## 5. B6: exact solution of the rank-2 completion law on a path

The path is not the source graph; it is a solved deformation whose mechanism can be read exactly.  Let `P_N` have vertices `1,\ldots,N`, and let `1\le i<j\le N` with `j-i\ge2`.  Put

\[
L=i-1,\qquad g=j-i-1,\qquad R=N-j,
\]

so

\[
L+g+R=N-2=:m,
\qquad g\ge1.
\]

### Theorem 5.1 (exact path completion count)

\[
\boxed{
F_{P_N}(\{i,j\})
=\frac{(N-2)!\,2^{g-1}}{L!\,g!\,R!}.
}
\tag{5.1}
\]

#### Proof

After the two seeds `i,j` are revealed, the unrevealed vertices split into three regions.

- The left tail `1,\ldots,i-1` can only be revealed in the forced order
  `i-1,i-2,\ldots,1`.
- The right tail `j+1,\ldots,N` can only be revealed in the forced order
  `j+1,j+2,\ldots,N`.
- In the middle gap `i+1,\ldots,j-1`, at each step the next vertex must be the leftmost unrevealed vertex adjacent to the `i`-side cluster or the rightmost unrevealed vertex adjacent to the `j`-side cluster.  For the first `g-1` middle-gap additions either side may be chosen, and the final vertex is then forced.  Hence there are exactly `2^{g-1}` internal middle-gap orders.

For any fixed middle-gap order, the three regional sequences have lengths `L,g,R`; arbitrary interleaving preserving each internal order gives

\[
\frac{m!}{L!g!R!}
\]

full suffix orders.  Multiplying by `2^{g-1}` proves (5.1).  ∎

### Corollary 5.2 (exact rank-2 gap law)

Summing (5.1) over all unordered nonadjacent path pairs gives

\[
\sum_{i<j-1}F_{P_N}(\{i,j\})
=\frac{4^m-2^m}{2}.
\tag{5.2}
\]

Under the rank-2 law `Q_{P_N}`, the number `g=j-i-1` of vertices strictly between the two seeds has distribution

\[
\boxed{
Q_{P_N}(g=q)=\frac{\binom mq}{2^m-1},
\qquad q=1,\ldots,m.
}
\tag{5.3}
\]

Equivalently, `g` is `Binomial(m,1/2)` conditioned on `g>0`.

#### Proof

For (5.2), sum the multinomial expression:

\[
\sum_{L+g+R=m,\ g\ge1}
\frac{m!2^{g-1}}{L!g!R!}
=\frac12\left((1+2+1)^m-(1+1)^m\right).
\]

For fixed `g=q`, summing over `L+R=m-q` gives

\[
\frac{m!2^{q-1}}{q!}
\sum_{L+R=m-q}\frac1{L!R!}
=2^{m-1}\binom mq.
\]

Divide by (5.2).  ∎

### Corollary 5.3 (the true two-peak path law is macroscopically separated)

Let `\rho_N` be the distance between the two peaks of a uniformly random labeling of `P_N`, conditioned on exactly two peaks.  Then

\[
\boxed{\rho_N/N\ \xrightarrow{\mathbb P}\ 1/2.}
\tag{5.4}
\]

More quantitatively, for every fixed `\varepsilon>0` and `N` large enough,

\[
\mathbb P_2\left(\left|\rho_N/N-\tfrac12\right|>\varepsilon\right)
\le
(N-1)\,
\frac{2\exp\!\left(-2\varepsilon^2N^2/(N-2)\right)}{1-2^{-(N-2)}}.
\tag{5.5}
\]

#### Proof

Under `Q_{P_N}`, `\rho_N=g+1` and `m=N-2`, so exactly

\[
\frac{\rho_N}{N}-\frac12
=\frac{g-m/2}{N}.
\]

Hoeffding's inequality for `Binomial(m,1/2)`, followed by conditioning on `g>0`, yields

\[
Q_{P_N}\left(\left|\rho_N/N-\tfrac12\right|>\varepsilon\right)
\le
\frac{2\exp(-2\varepsilon^2N^2/m)}{1-2^{-m}}.
\]

Apply the upper half of (4.2).  The polynomial factor `N-1` is dominated by the exponential tail, proving (5.4) and (5.5).  ∎

The qualitative one-dimensional macroscopic-separation phenomenon is already part of the prior literature around random-labeling peaks; this corollary is used here as a **solved-case rederivation and mechanism check**, not as a novelty claim.

## 6. B21: frontier-growth Feynman–Kac representation

There is an exact change-of-measure representation for `F(T)` that makes its spatial content explicit.

Starting from `S_0=T`, define an auxiliary frontier process by choosing

\[
X_{k+1}\ \text{uniformly from }\partial S_k,
\qquad
S_{k+1}=S_k\cup\{X_{k+1}\}.
\tag{6.1}
\]

This is **not** the law of a uniformly random labeling conditioned on one or two peaks.  It is only an auxiliary proposal chain.

### Theorem 6.1 (exact frontier partition function)

For every nonempty seed set `T` in a connected graph,

\[
\boxed{
F(T)=
\mathbb E_T^{\mathrm{fr}}
\left[
\prod_{k=0}^{N-|T|-1}|\partial S_k|
\right].
}
\tag{6.2}
\]

#### Proof

Every valid no-further-birth completion is exactly one path of the process (6.1).  A particular valid path

\[
S_0,S_1,\ldots,S_{N-|T|}=V
\]

has auxiliary probability

\[
\prod_{k=0}^{N-|T|-1}|\partial S_k|^{-1}.
\]

Multiplying by the product in (6.2) gives one.  Summing over all valid paths therefore gives exactly their number, `F(T)`.  ∎

So `F(T)` is a discrete Feynman–Kac partition function whose potential is

\[
V(S)=\log|\partial S|.
\tag{6.3}
\]

The square-grid source is now a comparison of two-root partition functions at different seed separations.

This representation also explains why a naive local one-step comparison can fail: moving one seed changes the early geometry only locally, but through (6.2) it may alter the entire future sequence of boundary potentials.  The path formula (5.1) is an explicit example where seed separation changes the completion partition function by exponentially large factors even though the seed move itself is local.

## 7. The new square-grid target

Let

\[
Q_n:=Q_{G_{n,n}}
\]

be the rank-2 pair law on the `n\times n` square.  The full Burdzy source has now been reduced to the following quantitative spatial question:

> **Two-root free-energy target.** Determine whether, for some fixed `\varepsilon>0`,
> \[
> Q_n\{d(r,v)\le\varepsilon n\}=o(n^{-2}),
> \tag{7.1}
> \]
> or instead whether the complementary macroscopic-separation probabilities are `o(n^{-2})` for every fixed `\varepsilon>0`.

By (4.2), the first alternative yields a source-valid **NO**; sufficiently strong versions of the second yield **YES**.  Any exponential-rate large-deviation theorem for `Q_n` automatically transfers to the true conditioned pair law because the promotion tilt costs only `n^2`.

This is sharper than the preceding run's raw pair-weight problem: the uncontrolled location of the second birth has been removed at only polynomial cost.  The hard object is now only the rank-2 two-seed completion partition function `F(\{r,v\})`.

## 8. What failed and what remains open

1. **No grid asymptotic has yet been proved.**  The frozen metric `D_*` remains `UNKNOWN/UNMEASURED`.
2. The exact path theorem is a deformation/analogue, not a proof for the square.
3. A bounded-degree argument alone does not give a useful local ratio bound for `F(\{r,v\})`: the Feynman–Kac product records boundary changes over `Theta(N)` future steps.
4. The polynomial promotion theorem does not say that `Q_n` itself is spatially uniform.  It says only that solving the spatial question under `Q_n` is sufficient up to an `n^2` loss.
5. Existing exact `n\le4` square data remain finite certificates only and do not move `D_*`.
6. A fresh 2026-09-18 source/literature check still finds Burdzy's official Problem 9 posed as open and Burdzy–Pal's *Twin peaks* as the closest primary treatment; failure to find a later solution is negative evidence, not a novelty certificate.

## 9. Next mathematical attacks

Do not repeat B6/B21/B30 immediately.  The next useful triple is:

- **B3 — prove something stronger:** seek an exponential large-deviation/free-energy separation theorem for `Q_n`, which would survive the polynomial promotion tilt automatically;
- **B7 — take the limit:** define finite-box two-root free energies and test a subadditive/thermodynamic limit as the scaled seed displacement varies;
- **B24 — find the extremal object:** identify which seed separation/location maximizes `F(\{r,v\})`, beginning with interior versus boundary seeds and near versus macroscopic separation.

A particularly concrete next lemma is a block-gluing inequality for `\log F(\{r,v\})` with an error `o(n)` or, better, `O(\log n)` under macroscopic seed displacement.  The promotion theorem means that any resulting exponential gap is already strong enough for the original two-peak law.

## 10. Source-level status

- exact source: Burdzy Problem 9 on the square grid;
- mathematical status: **OPEN / PARTIAL**;
- frozen metric before: `UNKNOWN/UNMEASURED`;
- frozen metric after: `UNKNOWN/UNMEASURED`;
- movement: **NO MOVEMENT**;
- substantive gain: arbitrary-graph polynomial reduction to the rank-2 pair law, an exact solved path model, and an exact frontier partition-function representation.
