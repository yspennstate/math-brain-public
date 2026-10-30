# B12 — the source-valid n=18 FEI margin counterexample is composition-prime

**Outcome:** `CANDIDATE_REFUTED` at the current read-once-\(\Gamma\)/AND-extremality scope.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target and change

The live owner target is the all-gate inequality
\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i I_i^t(G;p)\,
\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p),
\tag{G}
\]
and, for the current read-once value-iteration potential with
\[
C_0=\Gamma(1/2)=6.4548,
\]
the normalized required quadratic margin
\[
c_G^\Gamma(p)
=
-\frac{D_G^\Gamma(p)}
{Q_G(p)},
\qquad
Q_G(p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out}).
\tag{0.1}
\]

The old missing implication was that the largest required margin is attained by a
decomposable/AND-type gate, so the read-once \(\Gamma\) would extend to every
Boolean gate.

Two exact peer results are consumed, not merely cited:

1. `fleet03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`,
   blob `e49efe403698395b700278d067c245c12a7b15eb`, proves that the
   source-valid balanced \(n=18\) Numaro gate at unbiased inputs satisfies
   \[
   c_G
   =
   4\left(\frac{H(G)}{I(G)-1}-C_0\right)
   \ge
   0.2681828436921863026325758917943138734666491688421,
   \tag{0.2}
   \]
   using \(I(G)=261/128\) and the certified entropy interval
   \[
   6.776605309005978082519790221891882314787235038
   \le H(G)\le
   6.776605309005978082519790221891882314787235039.
   \tag{0.3}
   \]
   The current two-input AND margin is only about \(0.0043974201\).

2. `fleet04/B15/20260922T004054Z-gate-margin-composition/REPORT.md`
   proves for every disjoint block composition \(F=A(B_1,\ldots,B_m)\)
   the exact identities
   \[
   D_F=D_A+\sum_i\lambda_iD_{B_i},
   \qquad
   Q_F=Q_A+\sum_i\lambda_iQ_{B_i},
   \tag{0.4}
   \]
   hence \(c_F\) is the \(Q\)-weighted convex barycenter of the factor
   margins. Therefore every minimal margin-threshold counterexample may be
   chosen composition-prime.

This report proves that the **same explicit \(n=18\) source gate in (0.2) is
itself composition-prime**. Thus the failure is not an artefact of recursively
composing smaller bad gates.

## 1. Composition-prime criterion by monotone cofactors

Let \(g:\{0,1\}^n\to\{0,1\}\) be monotone. For a nonempty proper coordinate
block \(B\subset[n]\), write \(C=[n]\setminus B\). For each assignment
\(z\in\{0,1\}^B\), let
\[
g_z(y)=g(z,y),\qquad y\in\{0,1\}^C,
\]
and let
\[
N_B(z)=|\{y:g_z(y)=1\}|.
\]

### Lemma 1 — an intermediate cofactor count forbids one-bit block compression

If there exists \(z\in\{0,1\}^B\) with
\[
N_B(0_B)<N_B(z)<N_B(1_B),
\tag{1.1}
\]
then there do not exist Boolean maps \(b:\{0,1\}^B\to\{0,1\}\) and
\(A:\{0,1\}^{1+|C|}\to\{0,1\}\) such that
\[
g(x_B,x_C)=A(b(x_B),x_C)
\quad\text{for every }x.
\tag{1.2}
\]

**Proof.**
Monotonicity gives the pointwise order
\[
g_{0_B}\le g_z\le g_{1_B}.
\]
The strict inequalities in (1.1) therefore imply that \(g_z\) is distinct from
both endpoint cofactors. Hence the family
\(\{g_w:w\in\{0,1\}^B\}\) contains at least three different Boolean functions.
Under (1.2) it could contain at most the two rows
\(A(0,\cdot)\) and \(A(1,\cdot)\). Contradiction. \(\square\)

Consequently, to prove composition-primality it suffices to rule out every
proper block \(B\) with \(2\le |B|\le n-1\). Any nontrivial disjoint Boolean
block decomposition contains such a block, and that block would have at most
two cofactors. Singleton blocks are the trivial leaf factors.

## 2. Exact source representation of the \(n=18\) gate

I reused the exact source reconstruction from
`fleet01/B15/20260921T130641Z-carry-congruence-n18-profile/`.
The reconstructed truth table is accepted only after matching the published
SHA-256
```
f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839
```
and has nine **core** coordinates \(0,\ldots,8\) and nine **host**
coordinates \(9,\ldots,17\).

The host variables control the following pairwise-disjoint pairs of core cells:
\[
\begin{array}{c|c}
j&\text{core cells switched on by host }j\\ \hline
0&(78,79)\\
1&(113,121)\\
2&(228,484)\\
3&(170,186)\\
4&(149,151)\\
5&(338,466)\\
6&(284,316)\\
7&(291,295)\\
8&(393,457).
\end{array}
\tag{2.1}
\]
Every cell in (2.1) is false in the base core function, and the eighteen cells
are distinct.

The checker independently verifies monotonicity: there are zero decreasing
edges. It also obtains the exact edge-disagreement counts
\[
29184\quad\text{for each core coordinate},\qquad
512\quad\text{for each host coordinate}.
\tag{2.2}
\]
Since the denominator is \(2^{17}\), the influences are
\[
\frac{29184}{2^{17}}=\frac{57}{256}
\quad\text{and}\quad
\frac{512}{2^{17}}=\frac1{256},
\]
so every coordinate is relevant and
\[
I(G)=9\left(\frac{57}{256}+\frac1{256}\right)
=\frac{261}{128},
\tag{2.3}
\]
matching the independent source record.

## 3. Exact elimination of all proper blocks

Let \(T\subseteq\{0,1\}^{18}\) be the true set of \(g\). Define the exact
subset and superset zeta counts
\[
S(M)=|\{x\in T:x\subseteq M\}|,\qquad
U(M)=|\{x\in T:M\subseteq x\}|.
\tag{3.1}
\]
For a candidate block \(B\) and \(C=[18]\setminus B\),
\[
N_B(0_B)=S(C),\qquad N_B(1_B)=U(B).
\tag{3.2}
\]
For \(i,j\in B\), exact inclusion-exclusion gives
\[
N_B(\{i\})=S(C\cup\{i\})-S(C),
\tag{3.3}
\]
and
\[
N_B(\{i,j\})
=
S(C\cup\{i,j\})-S(C\cup\{i\})-S(C\cup\{j\})+S(C).
\tag{3.4}
\]

The deterministic exhaustive certificate checks all
\[
\sum_{k=2}^{17}\binom{18}{k}
=262124
\tag{3.5}
\]
proper nontrivial blocks.

* A singleton-pattern witness (3.3) satisfying the strict inequalities of
  Lemma 1 eliminates all but **20,767** blocks.
* A pair-pattern witness (3.4) eliminates all but **511** of those.
* The 511 survivors are **exactly**
  \[
  B=[9]\cup H,
  \qquad
  H\subsetneq\{\text{nine host coordinates}\}.
  \tag{3.6}
  \]
  There are \(2^9-1=511\) such blocks.

The remaining 511 have a direct analytic witness. Let \(j\) be any host
coordinate outside \(B\), let \(r\ge1\) be the number of outside hosts, and
fix the core coordinates to either special cell controlled by \(j\). Set every
host coordinate lying in \(B\) to zero. Because that core cell is false in the
base function and all host special pairs are disjoint, the residual function
of the \(r\) outside hosts is **exactly the literal \(h_j\)**. Its true-count is
\[
2^{r-1}.
\tag{3.7}
\]
At the all-zero assignment on \(B\), the core is the all-zero core cell and the
conditional true-count is \(0\); at the all-one assignment on \(B\), the
all-one core cell is true and the conditional true-count is \(2^r\). Hence
\[
0<2^{r-1}<2^r,
\tag{3.8}
\]
so Lemma 1 eliminates every block in (3.6).

Therefore:

### Theorem 2 — the published \(n=18\) gate is composition-prime

For the source-valid balanced monotone \(n=18\) gate above, there is no proper
coordinate block \(B\) with \(2\le|B|\le17\) and no Boolean maps \(A,b\) for
which
\[
G(x_B,x_C)=A(b(x_B),x_C).
\tag{3.9}
\]
Thus \(G\) admits no nontrivial disjoint Boolean block decomposition.

This is an exact finite theorem about the specified truth table, not a random
search and not a statement about arbitrary non-Boolean spectral laws.

## 4. Apply the theorem to the live gate-margin candidate

The exact fleet03/B15 balanced-gate identity and entropy certificate give
\[
c_G(1/2,\ldots,1/2)
\ge
0.2681828436921863026325758917943138734666491688421.
\tag{4.1}
\]
Against the current AND margin \(c_{\rm AND}\approx0.0043974201\),
\[
\frac{c_G}{c_{\rm AND}}>60.9864.
\tag{4.2}
\]

By Theorem 2, this larger-margin gate is composition-prime. By the exact
fleet04/B15 barycenter theorem, no explanation by hidden disjoint
decomposition is possible: decomposable gates inherit only convex averages of
factor margins.

Hence the old implication

> the current read-once \(\Gamma\) is universally valid because the extremal
> required margin is attained by a decomposable/AND-type gate

is false in the strongest relevant finite sense supplied here: a source-valid,
balanced, **composition-prime** gate already asks for a much larger margin.

## 5. Exact status and replacement obligation

**Classification:** `CANDIDATE_REFUTED`.

What is refuted:
- universal validity of the current read-once fixed-point \(\Gamma\) with
  \(\Gamma(1/2)=6.4548\);
- decomposable/AND extremality for its required margin.

What is not refuted:
- the gate reformulation (G);
- the existence of some other finite-cap symmetric nonnegative \(\Gamma\);
- the Fourier entropy-influence conjecture itself.

The replacement obligation is therefore the genuinely universal one:
construct/prove a different symmetric nonnegative \(\Gamma\) satisfying (G)
for every gate and every bias. Any such cap must in particular satisfy
\[
\Gamma(1/2)\ge
6.5218457109230465756581439729485784683666622922105\ldots
\tag{5.1}
\]
because the composition-prime \(n=18\) gate can be recursively self-composed
and fleet03/B15 proves that its limiting entropy/influence ratio is exactly
\(H(G)/(I(G)-1)\).

No full-FEI conclusion is claimed.

## 6. Reproducibility

`check_n18_composition_prime.py` reconstructs the exact source table, checks its
published SHA-256, balance, monotonicity and exact influences, computes subset
and superset zeta transforms, tests every proper nontrivial block using the
singleton/pair count witnesses, and explicitly verifies the host-literal
witness on every one of the remaining 511 blocks.

Checker SHA-256:
`884359aee4d4a92b4ea6ca812aa2104bf1d8d4f681fae539486290f6eebc972b`

Captured stdout SHA-256:
`3a1378bd9a03de3856f2b403e66121278924942c89d635d0b85afca7d9fc3a06`

The checker exits normally with:
```
PASS
truth_sha256 = f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839
blocks_checked = 262124
singleton_survivors = 20767
pair_survivors = 511
pair_survivors_exactly_core_supersets = True
analytic_residual_witnesses = 511
core_influence_edge_count_each = 29184
host_influence_edge_count_each = 512
composition_prime = True
```

The finite program is a reproducibility certificate for the explicit source
gate. The mathematical consequence uses the proved monotone-cofactor lemma plus
the analytic elimination of the final structured survivor family.
