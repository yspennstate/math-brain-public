Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed. **`C_E0070: 1 -> 1` (NO MOVEMENT); methods B27 / B21 / B4.**

# E0070 / Björklund Problem 2 — exact quotient equivalence, null-recurrent Schreier star, and minimal fixed-weight proof

Date: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Start snapshot: `5462594ecd474c1b3927c7a26cd502a1df437ba6`  
Fresh pre-write master observed: `023f470c04782ed26a7525c05b441e937108b9d9`

## 1. Source target and cumulative state

The outside source is Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2 (2014), Appendix II §7.1, Problem 2, printed PDF p.24:

> Construct a countable measured group `(G,mu)` and an infinite-index subgroup `H<G` such that `G/H` does not admit any nonconstant left `(quasi-)mu`-harmonic functions whatsoever.

Primary source: <https://arxiv.org/abs/1406.0763>.

The source defines a measured group by semigroup generation of `supp(mu)`, and §4.1 defines left quasiharmonicity by the existence of an arbitrary constant defect `ell(phi)`:

\[
\int_G \phi(sg)\,d\check\mu(s)=\phi(g)+\ell(\phi),\qquad g\in G.
\]

The admitted R7-03 construction is

\[
G=\operatorname{Sym}_{\rm fin}(\mathbb N_0),\qquad
H=\operatorname{Stab}_G(0),\qquad
\tau_n=(0\ n),\qquad
\mu(\tau_n)=p_n>0,
\]

with \(\sum_{n\ge1}p_n=1\); the paper fixes the explicit choice \(p_n=2^{-n}\).  The preceding run corrected a source-interface exposition error but left the arbitrary-defect proof intact.  This artifact executes the prescribed nonrepeating methods B27, B21, and B4.

The frozen metric is already `C_E0070=1`, so none of the strengthenings below is counted as source-metric movement.

---

## 2. B27 — exact quotient/pullback equivalence, in both directions

A possible audit concern in the existing paper is that it says the group equation “descends” to the quotient, but does not isolate an if-and-only-if statement.  For the symmetric measure actually used here, the correspondence is exact.

### Proposition 2.1 (right-H-invariant pullback equivalence for a symmetric measured group)

Let \(G\) be countable, let \(H<G\), and let \(\mu\) be a **symmetric** probability measure on \(G\), so \(\check\mu=\mu\).  Put \(X=G/H\) and let \(\pi(g)=gH\).  For a function \(u:X\to\mathbb C\), define its pullback

\[
\Phi_u(g)=u(gH).
\]

Then:

1. \(u\mapsto\Phi_u\) is a bijection between functions on \(X\) and right-\(H\)-invariant functions on \(G\).
2. Whenever the relevant sums are defined,
   \[
   \sum_{s\in G}\mu(s)\Phi_u(sg)
   =
   \sum_{s\in G}\mu(s)u(sgH).
   \tag{2.1}
   \]
   Hence the group convolution is right-\(H\)-invariant and induces the quotient operator
   \[
   (P_Xu)(gH):=\sum_{s\in G}\mu(s)u(sgH).
   \tag{2.2}
   \]
3. Fix \(c\in\mathbb C\).  If all sums in (2.2) are defined, then
   \[
   \Phi_u\text{ satisfies }\int_G\Phi_u(sg)d\check\mu(s)=\Phi_u(g)+c\ \forall g
   \]
   if and only if
   \[
   P_Xu=u+c\quad\text{on }X.
   \tag{2.3}
   \]
4. In the R7-03 star construction, source \(\mu\)-integrability of \(\Phi_u\) is exactly
   \[
   \sum_{n\ge1}p_n|u(n)|<\infty,
   \tag{2.4}
   \]
   and (2.4) automatically makes every quotient convolution sum absolutely convergent.

#### Proof

For (1), \(\Phi_u(gh)=u(ghH)=u(gH)=\Phi_u(g)\), so every pullback is right-\(H\)-invariant.  Conversely, if \(\Phi\) is right-\(H\)-invariant, define \(u(gH)=\Phi(g)\).  This is well-defined: if \(gH=g'H\), then \(g'=gh\) for some \(h\in H\), hence \(\Phi(g')=\Phi(gh)=\Phi(g)\).  The two operations are inverse.

Equation (2.1) is simply the definition of the pullback.  If \(g'=gh\), then for every \(s\),

\[
\Phi_u(sg')=\Phi_u(sgh)=u(sghH)=u(sgH)=\Phi_u(sg),
\]

so the convolution depends only on \(gH\), proving (2).

Because \(\mu\) is symmetric, \(d\check\mu=d\mu\).  Substituting (2.1) into the source left-quasiharmonic equation gives

\[
(P_Xu)(gH)=u(gH)+c
\]

for every \(g\), which is exactly (2.3).  This implication is reversible term by term, proving (3).

For the star construction, `supp(mu)={tau_n:n>=1}` and \(\tau_nH\) corresponds to the quotient point \(n\).  Thus source integrability at the identity is

\[
\sum_{s\in G}\mu(s)|\Phi_u(s)|
=
\sum_{n\ge1}p_n|u(n)|.
\]

At the center \(0\), this is exactly the absolute convergence condition for \((P_Xu)(0)\).  At a leaf \(k\), every generator except \(\tau_k\) fixes \(k\), while \(\tau_k\) sends \(k\) to \(0\); hence

\[
\sum_{n\ge1}p_n|u(\tau_n k)|
=p_k|u(0)|+(1-p_k)|u(k)|<\infty.
\]

Therefore source integrability at the identity automatically guarantees every convolution in the quotient equation is absolutely defined.  ∎

### Corollary 2.2 (no quotient/group convention gap for E0070)

For the R7-03 construction, the source statement “no nonconstant left quasiharmonic functions on \(G/H\)” is exactly equivalent to

\[
\{\Phi:G\to\mathbb C:\ \Phi\text{ right-}H\text{-invariant and source-valid left quasiharmonic}\}
=
\mathbb C\mathbf 1.
\]

There is no missing converse, coset-orientation ambiguity, or loss of an integrability hypothesis in passing between the group and the quotient.

### Why symmetry is stated explicitly

For a general nonsymmetric measure the source calls \(\phi\) `mu`-integrable while the left convolution uses \(\check\mu\).  One should therefore formulate the general quotient-domain statement with the exact pullback integrability convention rather than silently identifying the two measures.  The present construction is symmetric and every \(\tau_n\) is an involution, so this issue disappears completely.  The proof above intentionally makes no broader nonsymmetric claim.

---

## 3. B21 — the weighted Schreier graph is a null-recurrent infinite star

The quotient can be viewed as the weighted Schreier graph of the transitive action \(G\curvearrowright G/H\).  Under the identification \(G/H\cong\mathbb N_0\), its Markov kernel is

\[
P(0,k)=p_k,
\qquad
P(k,0)=p_k,
\qquad
P(k,k)=1-p_k
\quad(k\ge1),
\tag{3.1}
\]

with all other off-diagonal entries zero.

This viewpoint gives three useful structural facts.

### Proposition 3.1 (reversibility and null recurrence)

The chain (3.1) is irreducible, reversible with respect to counting measure, recurrent, and null recurrent.

#### Proof

Irreducibility follows because \(p_k>0\): the center communicates directly with every leaf.  Equation (3.1) is symmetric in the two endpoints of every non-loop edge, so

\[
P(x,y)=P(y,x),
\]

and counting measure is reversible.

Starting from a leaf \(k\), at each step the chain jumps to \(0\) with probability \(p_k\) and otherwise remains at \(k\).  Hence the hitting time of \(0\) is geometric with parameter \(p_k\), and is finite almost surely.  From \(0\), one step chooses a leaf \(K\) with law \(\Pr(K=k)=p_k\), after which the chain returns to \(0\) almost surely.  Thus \(0\), and hence every state, is recurrent.

Let \(T_0^+\) be the first return time to \(0\) after time zero.  Conditional on the first chosen leaf \(K=k\), the additional waiting time to return has mean \(1/p_k\).  Therefore

\[
\mathbb E_0T_0^+
=1+\sum_{k\ge1}p_k\frac1{p_k}
=1+\sum_{k\ge1}1
=\infty.
\]

The irreducible recurrent chain is therefore null recurrent. ∎

### Proposition 3.2 (all harmonic functions are constant, without boundedness or integrability)

If \(Pu=u\) pointwise for the kernel (3.1), then \(u\) is constant.  No boundedness or integrability assumption is needed.

#### Proof

At leaf \(k\),

\[
p_ku(0)+(1-p_k)u(k)=u(k),
\]

so \(p_k(u(0)-u(k))=0\).  Since \(p_k>0\), \(u(k)=u(0)\) for every \(k\). ∎

This is stronger than the harmonic part of the source request.  Integrability is needed only to rule out a nonzero quasiharmonic defect.

### Proposition 3.3 (even conditional center convergence rules out nonzero defect)

Suppose \(u:\mathbb N_0\to\mathbb C\) satisfies the leaf equations for

\[
Pu=u+c.
\tag{3.2}
\]

If the center series \(\sum_{k\ge1}p_ku(k)\) converges in its displayed order — even without absolute convergence — then \(c=0\) and \(u\) is constant.

#### Proof

The leaf equations give

\[
u(k)=u(0)-\frac{c}{p_k},
\tag{3.3}
\]

and hence

\[
p_ku(k)=p_ku(0)-c.
\tag{3.4}
\]

Because \(\sum p_k=1\) with all \(p_k>0\), we have \(p_k\to0\).  If \(c\ne0\), the summands in the purported center series satisfy

\[
p_ku(k)\longrightarrow-c\ne0,
\]

so the series cannot converge.  Thus \(c=0\), and (3.3) makes \(u\) constant. ∎

This removes a possible definitional fragility: Björklund’s actual source hypothesis is the stronger absolute \(\mu\)-integrability, but the contradiction already follows from the weakest necessary condition for the center convolution to exist as an ordinary series.

### Conceptual interpretation

The infinite-star quotient is a null-recurrent weighted Schreier chain.  The constant Poisson forcing \((I-P)u=-c\mathbf 1\) has the unique formal leaf profile \(u(k)=u(0)-c/p_k\).  Null recurrence manifests here as an infinite total expected excursion length, and the same reciprocal \(1/p_k\) growth makes any nonzero forcing incompatible with the center convolution.  This is the mechanism behind the source construction, expressed entirely in standard Markov-chain language.

---

## 4. B4 — minimal literal-source proof for the single fixed law `p_n=2^{-n}`

The general positive-weight theorem is not needed to answer Problem 2.  The following proof uses only the single explicit example and the literal source definitions.

### Theorem 4.1 (fixed explicit source solution)

Let

\[
G=\operatorname{Sym}_{\rm fin}(\mathbb N_0),\qquad
H=\operatorname{Stab}_G(0),\qquad
\mu((0\ n))=2^{-n}\quad(n\ge1).
\]

Then \((G,\mu)\) is a countable measured group, \([G:H]=\infty\), and \(G/H\) admits no nonconstant source-valid left \(\mu\)-quasiharmonic function.

#### Proof

**Measured-group hypotheses.**  The finitary symmetric group is countable because

\[
G=\bigcup_{m\ge0}\operatorname{Sym}(\{0,1,\dots,m\}),
\]

a countable union of finite sets.  Also \(\sum_{n\ge1}2^{-n}=1\), so \(\mu\) is a probability measure.  Every support element \(\tau_n=(0\ n)\) is an involution, hence \(\mu=\check\mu\).  For distinct positive \(i,j\),

\[
\tau_i\tau_j\tau_i=(i\ j),
\]

so the star transpositions generate every finitary transposition and hence all of \(G\).  Since the generators are involutions, group generation is semigroup generation.  Finally,

\[
G/H\longrightarrow\mathbb N_0,\qquad gH\mapsto g(0),
\]

is a bijection, so \([G:H]=\infty\).

**Quotient equation.**  Let \(u:G/H\to\mathbb C\) be source-valid left quasiharmonic, with defect \(\ell\).  By Proposition 2.1, under \(G/H\cong\mathbb N_0\) it obeys

\[
Pu=u+\ell,
\]

and source integrability is

\[
\sum_{k\ge1}2^{-k}|u(k)|<\infty.
\tag{4.1}
\]

At leaf \(k\),

\[
2^{-k}u(0)+(1-2^{-k})u(k)=u(k)+\ell,
\]

so

\[
u(k)=u(0)-2^k\ell.
\tag{4.2}
\]

If \(\ell\ne0\), then the \(k\)-th summand in (4.1) equals

\[
2^{-k}|u(k)|=|2^{-k}u(0)-\ell|\longrightarrow|\ell|>0,
\]

contradicting convergence of (4.1).  Hence \(\ell=0\).  Equation (4.2) now gives \(u(k)=u(0)\) for every \(k\), so \(u\) is constant. ∎

### Minimality of assumptions used by the proof

For this fixed example the proof uses only:

1. countability of \(G\);
2. semigroup generation by `supp(mu)`;
3. infinite index of \(H\);
4. symmetry \(\mu=\check\mu\);
5. the literal left quasiharmonic equation with one constant defect;
6. source integrability at the identity.

No boundedness, finite moment, finite generation, Poisson-boundary theorem, Fredholm theorem, numerical estimate, asymptotic approximation, or external lemma is used.

---

## 5. Failure search and what could still be wrong

The three attacks above were chosen to expose rather than decorate the proof.

- **Potential missing converse between quotient and group formulations:** eliminated by Proposition 2.1.
- **Potential left/right or inverse-generator convention mismatch:** eliminated for the actual example because every generator is an involution and \(\mu=\check\mu\); the quotient operator is the standard left-action Schreier operator.
- **Potential dependence on a strong interpretation of integrability:** eliminated by Proposition 3.3; nonzero defect already prevents ordinary convergence of the center series.
- **Potential hidden use of the general positive-weight theorem:** eliminated by the fixed `2^{-n}` proof in Theorem 4.1.
- **Potential bounded-harmonic-only argument:** absent; the harmonic statement is pointwise and the quasiharmonic contradiction allows arbitrary unbounded \(u\).

No mathematical counterexample or missing source hypothesis was found in this run.

The remaining closure deficits are not mathematical lemmas: the repository protocol still lacks an actual independent P26 full-proof audit and a distinct OTHER-track full-proof audit, and publication novelty remains unverified.

---

## 6. Dated literature check, 2026-09-18

The current arXiv record remains `1406.0763v2`, last revised 2014-07-07, and the HTML source still contains the same Appendix-II Problem 2 and the §4.1 arbitrary-defect quasiharmonic definition.

A bounded fresh search on 2026-09-18 used combinations of:

- `Björklund Problem 2 quasiharmonic quotient`;
- `Five remarks random walks groups quasiharmonic homogeneous space`;
- `star transposition quasiharmonic finitary symmetric group`;
- later star-transposition random-walk literature.

The search surfaced recent finite-symmetric-group star-transposition work, including Vanshika Jain and Evita Nestoridi, *Hitting-time mixing for the star transposition shuffle* (arXiv:2608.13727, 2026), and other representation/mixing papers.  Those concern finite \(S_n\) shuffle mixing and do not state Björklund Problem 2 or the infinite-star homogeneous-space construction above.  No retrieved source stated a later resolution of the exact problem.  This is **negative evidence only** and is not a novelty or worldwide-openness certificate.

Repository exact-ID/audit searches also still expose no independent P26 or distinct OTHER-track full-proof audit for E0070.

---

## 7. Metric and disposition

```text
C_E0070 before: 1
C_E0070 after:  1
movement: NO MOVEMENT
ordinary unchanged count: 4 -> 5
status: PROVED CANDIDATE / protocol closure open
```

This is the fifth ordinary unchanged run after the metric first moved to one.  Under the CLOSABLE protocol, the target is **not yet retired**; retirement/handoff is triggered after six unchanged ordinary runs.

For the next ordinary run, if E0070 remains active and unaudited, use a nonrepeating adversarial triple rather than adding another equivalent star-kernel proof.  Suggested methods: **B2 / B14 / B12** — attack the exact source theorem’s negation directly on the group without quotient notation; use the stabilizer/group action to rederive the quotient identification independently; and test whether a convolution-power invariant yields a genuinely independent contradiction or precisely identify why source integrability is insufficient to iterate the operator.  If the frozen metric remains unchanged, record count six and perform the prescribed immutable handoff/rotation procedure rather than continuing theorem ornamentation.