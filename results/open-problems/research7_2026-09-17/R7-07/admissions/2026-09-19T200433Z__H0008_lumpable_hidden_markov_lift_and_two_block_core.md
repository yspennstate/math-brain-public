Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding selector is exposed.** Methods: **B18 / B27 / B30**.

# H0008 feasibility: strong lumpability is an exact hidden-Markov quotient, harmonic stationarity lifts, and the first irreducible core is two-block retention heterogeneity

Date: 2026-09-19 UTC  
Worker: R7-07, native ID `6aabe8413f60819197825dd81ca138ae`  
Status: **PENDING_ADMISSION / H0008 PARTIAL FEASIBILITY / SOURCE OPEN / NOVELTY UNVERIFIED**

## 1. Source and inherited state

Source: Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, 17 August 2026, Section 12.3 open problem (6), **Boundary fluctuations**.

The source explicitly leaves open the fluctuation theory on the failed boundary, including the multifractal spectrum of transmission-weighted flows and the harmonic measure of the failed cluster, where a dimension drop should reappear. R14 completed the finite-type multifractal interval under its recorded hypotheses and released the still-open harmonic-measure clause after its two allowed stuck recoveries. The canonical history remains `operations/claims/H0008.md`; R7-07 does not own this source and does not overwrite that claim history.

The exact source finite-type failed genealogy used below is the one already recovered by R14. The fine type space is a finite set `D`. A parent of fine type `i` has a common potential-child count `nu`, independent of `i`, with mean

\[
m_*:=\mathbb E\nu.
\]

Each potential child independently gets fine type `j` with probability `q_j>0` and then transmits failure with probability `p_{ij}`. Put

\[
a_{ij}:=q_jp_{ij},\qquad M_{ij}:=m_*a_{ij}.
\]

The source pressure section works under finite-type irreducibility and uniform ellipticity, so in the source regime relevant here all `a_ij` are strictly positive. The harmonic measure is ordinary simple-random-walk harmonic measure on the underlying unit-edge failed tree.

R14 already proved the elementary **branching** lumpability criterion: for a partition `P={C_1,...,C_r}`, the block-labelled genealogy is an exact `r`-type Galton-Watson process iff the block sums

\[
c_{iB}:=\sum_{j\in C_B}a_{ij}
\]

depend on `i` only through its parent block. What was not established there is that this quotient loses **no information at all** for the harmonic-stationarity obstruction. That is the main point of this note.

## 2. B18 — SAY IT IN ANOTHER LANGUAGE: strong lumpability is a hidden Markov tree extension

Let `P={C_1,...,C_r}` satisfy

\[
i,i'\in C_A\implies c_{iB}=c_{i'B}=:c_{AB}\quad\forall B.
\tag{2.1}
\]

For `c_AB>0`, define the fine-label transition kernel along an edge whose child block is `B` by

\[
R^{B}_{i}(j):=
\frac{a_{ij}}{c_{AB}},
\qquad i\in C_A,\ j\in C_B.
\tag{2.2}
\]

Then `R_i^B` is a probability distribution on `C_B`.

### Theorem 2.1 — exact hidden-Markov representation of every strongly lumpable source law

Under (2.1), the complete fine-type failed genealogy is generated exactly as follows.

1. Generate the quotient block-labelled Galton-Watson tree: conditional on `nu`, a block-`A` parent sends each potential child independently to failed block `B` with probability `c_AB`, and to the absent state with probability `1-s_A`, where
   \[
   s_A:=\sum_Bc_{AB}.
   \]
2. Choose the root fine type inside its root block according to the source root mixture.
3. Conditional on the quotient tree and the fine type `i` of a parent in block `A`, each actual child whose quotient block is `B` receives its fine type independently according to `R_i^B` in (2.2).

In particular, **conditional on the quotient tree, the fine types form a finite-state tree-indexed Markov extension and never feed back into the quotient reproduction law.**

#### Proof

For one potential child of a fine parent `i in C_A`, the source categorical probabilities are

\[
\Pr(\text{failed fine type }j)=a_{ij},\qquad
\Pr(\text{absent})=1-\sum_ja_{ij}.
\]

Summing over `j in C_B` gives `c_AB`, independent of the choice of `i` in `C_A` by (2.1). Conditional on the event that the child lies in failed block `B`, Bayes gives

\[
\Pr(j\mid B,i)=a_{ij}/c_{AB}=R_i^B(j).
\]

Thus each source categorical draw can be factored into first a quotient-block/absence draw, then a fine label inside the selected block. Potential-child draws are independent, so conditional on `nu` the factorization holds jointly for all children. Source reproduction primitives are independent at distinct vertices. Induction through the generations gives the full-tree representation. `square`

This is precisely a probabilistic-bisimulation / hidden-Markov reading of R14's branching lumpability criterion. The abstract mechanism is standard; only its source-specialized consequences below are being derived here. Novelty is not certified.

## 3. Perron root and harmonic geometry are exactly quotient invariants

Let the quotient mean matrix be

\[
\bar M_{AB}:=m_*c_{AB}.
\tag{3.1}
\]

### Theorem 3.1 — Perron-root preservation

Assume the fine source matrix `M` is irreducible. Then

\[
\boxed{\rho(M)=\rho(\bar M).}
\tag{3.2}
\]

#### Proof

Let `h=(h_A)_A>0` be a Perron right eigenvector of `bar M` and lift it to the fine types by `tilde h_i=h_A` for `i in C_A`. Then

\[
(M\tilde h)_i
=m_*\sum_B\sum_{j\in C_B}a_{ij}h_B
=m_*\sum_Bc_{AB}h_B
=(\bar Mh)_A
=\rho(\bar M)\tilde h_i.
\]

So `M` has the positive eigenvector `tilde h` with eigenvalue `rho(bar M)`. Perron-Frobenius irreducibility makes this eigenvalue `rho(M)`. `square`

### Theorem 3.2 — pathwise harmonic-geometry preservation

For every realized fine tree, replacing each fine type by its block changes no vertex, edge, graph distance, effective conductance, simple-random-walk transition probability, harmonic cylinder mass, or boundary metric. Therefore, pathwise,

\[
\boxed{
\operatorname{HARM}_{\rm fine}=\operatorname{HARM}_{\rm quotient}
}
\]

as measures on the common end space, and every harmonic local dimension / Hausdorff dimension is identical before and after quotienting.

Combined with (3.2), any strict inequality

\[
\dim_H(\operatorname{HARM})<\log\rho(\bar M)
\]

proved for the quotient is automatically the exact source inequality

\[
\dim_H(\operatorname{HARM})<\log\rho(M)
\]

for the fine model.

Thus strong lumpability is not merely a convenient simplification of offspring counts: it is a lossless reduction for the entire harmonic dimension question.

## 4. B27 — SWAP THE QUANTIFIERS: every quotient harmonic-stationary environment lifts

The previous theorem is pathwise. The remaining PF-KL route also needs an equivalent stationary ergodic law for the one-generation harmonic-descendant shift. The next theorem shows that **for every** such quotient law, and **for every** source-compatible hidden fine kernel `R`, stationarity lifts automatically.

Let `Q^surv` denote the survival-conditioned quotient MGW law. Let `H_Q` be the quotient harmonic-descendant kernel: from a rooted surviving quotient tree `x`, choose a surviving child `u` with probability proportional to the child escape conductance and reroot at `u`.

Assume `mu_Q` is a probability law on surviving quotient trees such that

\[
\mu_QH_Q=\mu_Q,
\qquad
\mu_Q\sim Q^{\rm surv}.
\tag{4.1}
\]

The source's strict positivity implies

\[
r_*:=\min\{R_i^B(j): i\in C_A,\ j\in C_B\}>0
\tag{4.2}
\]

over the finitely many allowed triples.

### Theorem 4.1 — universal stationary-lift theorem

Under (2.1), (4.1), and (4.2), there exists a fine-tree law `mu_D` such that

\[
\boxed{
\mu_D H_D=\mu_D,
\qquad
\mu_D\sim P_D^{\rm surv},
}
\tag{4.3}
\]

where `H_D` is the fine harmonic-descendant shift and `P_D^surv` is the fine source law conditioned on survival. If `mu_Q` is ergodic, then `mu_D` can be chosen ergodic. Conversely, projecting any fine equivalent stationary law through the partition produces an equivalent stationary quotient law. Hence, under strict positivity,

\[
\boxed{
\text{equivalent harmonic stationarity exists for the fine source}
\iff
\text{it exists for the quotient source}.
}
\tag{4.4}
\]

#### Proof — construction on a two-sided harmonic base chain

Because `mu_Q` is stationary for `H_Q`, take a two-sided stationary quotient harmonic chain `(X_n)_{n in Z}` with marginal `mu_Q`. Write `A_n` for the block at the root of `X_n`.

Conditional on the entire base path, define a hidden fine-type chain by

\[
\Pr(I_{n+1}=j\mid I_n=i,(X_k)_k)
=R_i^{A_{n+1}}(j).
\tag{4.5}
\]

Each transition matrix in (4.5) has all entries at least `r_*>0` on its target block. Hence for two probability distributions on the same current fiber, one step contracts total variation by a uniform factor strictly below one. Concretely, if the next block has `m_B` fine types, every two rows have overlap at least `m_B r_*`, so the Dobrushin coefficient is at most

\[
1-m_Br_*\le 1-r_*<1.
\tag{4.6}
\]

Start the hidden chain at time `-N` with any distribution on the required block. By (4.6), its law at every fixed later time converges as `N to infinity`, uniformly in the initial choice. The resulting conditional path law is shift-covariant; integrating against the stationary base path gives a stationary joint process `(X_n,I_n)_{n in Z}`. Its one-time marginal is a stationary law `lambda` on pairs `(quotient rooted tree, compatible fine root type)`.

Now sample `(X_0,I_0)` from `lambda`. Conditional on this pair, label every descendant edge of `X_0` independently by the source kernels (2.2), recursively from the root. Theorem 2.1 says that this is exactly the source fine conditional law given the quotient tree and the root fine type.

When the harmonic descendant is chosen, its block and quotient subtree are selected using only `X_0`; fine labels do not affect conductances. Conditional on the chosen block, its fine label has exactly the transition law (4.5). The fine descendants below that child are again generated by the same recursive source kernels. Stationarity of `(X_n,I_n)` therefore gives `mu_DH_D=mu_D`.

For equivalence, (4.6) also gives a uniform positive lower bound on every stationary conditional root fine-type probability inside its block. Under strong lumpability, the quotient tree law conditional on a root block is independent of the hidden fine type inside that block, while the source root mixture has positive mass on every fine type. The quotient factors are equivalent by (4.1), the root-fiber factors are mutually absolutely continuous by positivity, and all descendant conditional label kernels are identical. Hence `mu_D~P_D^surv`.

If the base is ergodic, the uniform Dobrushin contraction implies that the hidden chain forgets its remote initial condition exponentially along every base path. Therefore the finite extension contributes no additional invariant event, and the lifted law is ergodic.

Conversely, the quotient map commutes with harmonic rerooting and sends the fine source law to the quotient source law. Pushing forward an equivalent fine stationary law therefore gives an equivalent quotient stationary law. `square`

### Corollary 4.2 — the group-covariant theorem from the preceding R7-07 run was far from maximal

For the one-block partition, condition (2.1) is simply constant total transmission

\[
\sum_jq_jp_{ij}=c\quad\forall i.
\]

Then the quotient is an ordinary one-type Galton-Watson tree, but the hidden fine labels may evolve by **any** source-admissible finite Markov kernel

\[
\Pi_{ij}=\frac{q_jp_{ij}}c,
\]

not merely a finite-group convolution. Every stationary label kernel lifts the classical one-type harmonic environment. Thus finite-group covariance was a useful explicit example, but not the true structural boundary.

## 5. Canonical maximal compression by partition refinement

Strong lumpability has a canonical coarsest quotient. This gives an exact preprocessing step before any further H0008 harmonic analysis.

Start with the one-block partition

\[
\mathcal P_0=\{D\}.
\]

Given `P_n`, split each current block according to the signature

\[
\sigma_{\mathcal P_n}(i)
:=
\left(
\sum_{j\in C}a_{ij}
\right)_{C\in\mathcal P_n}.
\tag{5.1}
\]

Call the refined partition `P_{n+1}`. Since `D` is finite, this process stabilizes after at most `|D|-1` genuine refinement steps; denote the limit by `P_*`.

### Theorem 5.1 — `P_*` is the unique coarsest strong lumping

`P_*` satisfies (2.1), and every other partition satisfying (2.1) refines `P_*`.

#### Proof

Stability of the terminal partition means exactly that two types remaining in one terminal block have identical sums into every terminal block, which is (2.1).

Let `Q` be any strong-lumping partition. Trivially `Q` refines `P_0`. Assume inductively that `Q` refines `P_n`. Every `P_n` block is then a union of `Q` blocks. If `i,i'` lie in the same `Q` block, strong lumpability of `Q` makes their row sums into each `Q` block equal, hence their sums into each union that forms a `P_n` block equal. Thus `sigma_{P_n}(i)=sigma_{P_n}(i')`, so the refinement from `P_n` to `P_{n+1}` never separates two points of a `Q` block. Therefore `Q` refines every `P_n` and hence `P_*`. `square`

### Corollary 5.2 — exact reduction of the H0008 stationarity problem

Under source positivity, quotienting by `P_*` preserves

- the Perron root;
- the underlying unlabelled tree pathwise;
- harmonic measure pathwise;
- harmonic Hausdorff dimension pathwise;
- existence/nonexistence of an equivalent harmonic-stationary law;
- ergodicity of such a law.

Hence all removable hidden-type redundancy can be stripped canonically. The genuinely new H0008 problem begins only on a source whose coarsest strong lumping is the discrete partition.

## 6. B30 — ONE SCALE / ONE DIRECTION: the exact first two-block core

Suppose the canonical coarsest partition `P_*` has exactly two blocks, labelled `0,1`. Write

\[
C=
\begin{pmatrix}
c_{00}&c_{01}\\
c_{10}&c_{11}
\end{pmatrix},
\qquad
s_0=c_{00}+c_{01},
\quad
s_1=c_{10}+c_{11}.
\tag{6.1}
\]

### Theorem 6.1 — a genuine coarsest two-block quotient must have unequal total retention

If `P_*` has exactly two blocks, then

\[
\boxed{s_0\ne s_1.}
\tag{6.2}
\]

#### Proof

If `s_0=s_1=s`, then for the one-block partition `P_0={D}` every fine type has the same total row sum `s`. Therefore `P_0` is already stable under the refinement rule (5.1), so `P_*` would have one block, contradiction. `square`

Consequently the first genuinely irreducible quotient obstruction is already visible in the total failed-child count:

\[
K_A\mid\nu\sim\operatorname{Bin}(\nu,s_A),
\qquad s_0\ne s_1.
\tag{6.3}
\]

This is stronger than saying that child *types* differ. The unlabelled reproduction law itself remembers the parent block.

### Theorem 6.2 — all fine-type complexity is solved once the two-block quotient is solved

For any fine source with coarsest quotient of size two, proving an equivalent stationary ergodic harmonic environment and a dimension drop for the two-block quotient proves the identical statements for the complete fine source. No hidden fine-label reversibility or cycle-balance hypothesis is needed.

Moreover, if a stationary quotient environment exists and `H=(H_AB)` is its induced two-state root-block transition matrix along the harmonic descendant chain, then its stationary block marginal `pi` automatically satisfies detailed balance:

\[
\pi_0H_{01}=\pi_1H_{10}.
\tag{6.4}
\]

Indeed the two stationary equations reduce to the same equality. Thus **cycle circulation cannot be the obstruction in the first irreducible quotient.** The remaining obstruction is positive recurrence / normalization of the environment law for two different conductance-reproduction distributions.

### Exact conductance form of that obstruction

Let `F_A` be the source law of escape conductance `B` for a surviving block-`A` descendant subtree. Given parent block `A`, conditional on `nu`, the child-block counts are multinomial with probabilities `(c_A0,c_A1,1-s_A)`. Given those counts, child conductances are independent with laws `F_0,F_1`, and

\[
S_A=\sum_{u:\,0}B_u+\sum_{u:\,1}B_u,
\qquad
B_A=\frac{S_A}{1+S_A}.
\tag{6.5}
\]

The harmonic probability of choosing block `B` from that realized parent is

\[
\frac{\sum_{u:\,B}B_u}{S_A}.
\tag{6.6}
\]

Equations (6.3)--(6.6) identify the exact failure of naive blockwise gluing: the quotient does not merely carry a two-state Markov chain. Parent block changes the full offspring-count law, which changes the conductance law `F_A`, and harmonic block selection is a random conductance ratio. Hidden fine labels have been eliminated completely; the unresolved object is now a genuinely two-law electrical recursion.

## 7. Exact four-type witness whose canonical quotient is genuinely two-block

Take four fine types, uniform `q_j=1/4`, deterministic `nu=3`, and

\[
P=(p_{ij})=
\begin{pmatrix}
1&1/2&3/4&1/4\\
3/4&3/4&1/8&7/8\\
1/4&3/4&1&3/4\\
2/3&1/3&7/8&7/8
\end{pmatrix}.
\tag{7.1}
\]

The partition-refinement algorithm gives exactly

\[
\boxed{\mathcal P_*=\{\{0,1\},\{2,3\}\}.}
\tag{7.2}
\]

The aggregate failed-child probabilities are

\[
C=
\begin{pmatrix}
3/8&1/4\\
1/4&7/16
\end{pmatrix},
\tag{7.3}
\]

so

\[
s_0=5/8,\qquad s_1=11/16,
\]

confirming genuine two-block irreducibility. The quotient mean matrix is

\[
\bar M=3C=
\begin{pmatrix}
9/8&3/4\\
3/4&21/16
\end{pmatrix},
\tag{7.4}
\]

with

\[
\operatorname{tr}\bar M=39/16,
\qquad
\det\bar M=117/128,
\qquad
\rho(\bar M)=\frac{39+3\sqrt{65}}{32}>1.
\tag{7.5}
\]

The exact intertwining relation `M E = E barM`, where `E` lifts a block vector to a block-constant fine vector, verifies Perron preservation in this witness. The hidden fine-label kernels inside each quotient edge are all strictly positive and stochastic.

The accompanying exact-arithmetic checker is archived separately and ends `ALL_EXACT_CHECKS_PASS`.

For comparison, R14's retained two-type diagnostic

\[
q=(1/2,1/2),\qquad
P=\begin{pmatrix}3/4&3/4\\1/2&1/4\end{pmatrix}
\]

has total row retentions `3/4` and `3/8`, so the one-block partition immediately splits into singletons. It is already a canonical two-block core and cannot be simplified by hidden-type lumping.

## 8. What moved mathematically

The preceding R7-07 run proved a nonreversible **group-covariant** slice by reducing it to one-type Galton-Watson plus iid group marks. This run proves that group structure was unnecessary.

The new exact statement is:

> **Every strong lumping is lossless for the H0008 harmonic problem.** Fine types below the canonical quotient are only a uniformly mixing hidden Markov decoration. Perron growth, harmonic geometry, and existence of an equivalent stationary ergodic harmonic environment all reduce exactly to the coarsest quotient.

This yields a canonical minimal state space and identifies the first genuinely unsolved core: a two-block source with unequal total retention probabilities, equivalently two different unlabelled reproduction/conductance laws. At two blocks, cycle circulation is automatically absent once stationarity exists, so the obstruction cannot be blamed on nonreversibility.

This is **PARTIAL** relative to H0008: it does not construct the stationary law for the irreducible two-block quotient and does not prove the full source dimension drop.

## 9. Prior-art boundary and dated source check

Dated 2026-09-19 checks:

- `https://arxiv.org/abs/2608.15987` remains Kumar's primary source record; Section 12.3(6) still names boundary fluctuations and harmonic measure as open.
- `https://arxiv.org/abs/2608.21125` is the Kumar--Duddala companion on front propagation/Bramson correction and continuous-type limits, not a resolution of this finite-type harmonic clause.
- Serdar Altok, *Unimodularity for multi-type Galton-Watson trees* (Bernoulli 2013; arXiv:1307.5962), gives necessary/sufficient conditions for certain reversible multitype tree laws. That is related prior art, but the theorem above is instead a quotient/lift theorem for the forward harmonic-descendant environment.
- Amir Dembo and Nike Sun, *Central limit theorem for biased random walk on multi-type Galton-Watson trees* (arXiv:1011.4056; current arXiv rendering dated 2026-03-22), constructs an explicit reversing environment at the **critical bias** `lambda=rho`; the paper itself notes that in the transient regime explicit reversing descriptions are delicate, with the one-type `lambda=1` case classical. It does not supply the H0008 transient harmonic-descendant law.
- Lyons--Pemantle--Peres gives the classical one-type harmonic-measure dimension drop; Rousselin gives a one-type random-environment extension by exit-time regeneration. These remain prior art, not claimed as new.

I did not locate the exact strong-lumping harmonic-stationarity equivalence above in the bounded search. Search failure is not a novelty certificate. **Novelty remains UNVERIFIED.**

## 10. Exact remaining question after this reduction

After quotienting by `P_*`, prove or refute, under the source finite-type supercritical hypotheses, existence of an equivalent stationary ergodic law for the harmonic-descendant shift. The smallest genuinely irreducible source is already two-block and is characterized by (6.3)--(6.6).

The next useful attack should therefore target the two-law conductance recursion directly, rather than hidden labels or cycle balance. A natural nonrepeating triple after B18/B27/B30 is:

- **B2 ATTACK THE NEGATION:** try to build a two-block positive source where the harmonic environment cannot be normalized / a regeneration roof has infinite mean;
- **B5 ADD A PARAMETER:** interpolate `s_0` to `s_1` from the solved one-block point and compute the first variation of the stationary transfer equation;
- **B21 ASK WHO ELSE HAS THIS SHAPE:** compare the two-law recursion with Markov-modulated smoothing transforms / random conductance trees and identify a transferable positive-recurrence criterion.
