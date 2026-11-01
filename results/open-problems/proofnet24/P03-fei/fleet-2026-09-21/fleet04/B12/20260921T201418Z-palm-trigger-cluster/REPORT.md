# B12 FEI — scale-separated Palm trigger clusters

**Run:** `B12-20260921T201418Z-r39`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** analytic partial theorem for the low-defect/near-subcube sector, plus exact finite diagnostic checks. No novelty or publication-priority claim.

## 0. Live assignment and consumed cross-account result

The live common control `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z` assigns fleet04/B12 to interface B:

> convert robust near-subcube derivative rows to an influence-relative code.

This run substantively consumes the completed other-account result

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/20260921T194351Z-curvature-palm-nonreuse/REPORT.md`

(report Git blob `ddf8baf96385418c56a91c48f62c04168633faaa`).

That report identifies, for the spectral sample `S`,
\[
 q_{ik}:=\Pr(i,k\in S)=\kappa_{ik}/4
\]
and hence the exact Palm predecessor observables
\[
 \alpha_{ik}=\frac{q_{ik}}{2j_i},\qquad
 \beta_k=\frac{d_k}{2I}.
\]
It proves a useful low-congestion KL payment but also proves by odd majority that the raw depth bank cannot satisfy a universal payment `D_seq >= c sum_i d_i`. Thus the high-depth branch must be **clustered before it is paid**.

The current fleet04/B18 interface supplies the complementary mixed-curvature conservation and robust near-subcube geometry. The purpose of this run is to make the word "cluster" exact.

## 1. Setup

Let
\[
 \mu(A)=\widehat f(A)^2,\qquad S\sim\mu,\qquad
 j_i=\Pr(i\in S)>0.
\]
For each active coordinate `i`, define the derivative Palm remainder law
\[
 \nu_i(B)
 =\Pr(S\setminus\{i\}=B\mid i\in S),
 \qquad B\subseteq[n]\setminus\{i\}.
\]
For a set `F` not containing `i`, let `U_F` denote the uniform law on all subsets of `F`.

Call row `i` **epsilon-Palm-robust with trigger set `F_i`** if
\[
 \operatorname{TV}(\nu_i,U_{F_i})\le\epsilon.
\tag{1.1}
\]
The physical-erasure/stability route of fleet02/B12 produces precisely this type of conclusion in its sufficiently small defect regime: the normalized derivative Palm law is close to the uniform power-set law of the nearby coordinate subcube.

Throughout the main numerical corollary take
\[
 \epsilon\le\frac1{16}.
\tag{1.2}
\]

The exact pair mass is
\[
 q_{ik}:=\Pr(i,k\in S)=q_{ki}.
\tag{1.3}
\]

## 2. PROVED: trigger membership gives two-sided pair-mass control

### Lemma B12-PALM-TRIGGER-PAIR-01

If row `i` is epsilon-Palm-robust, then for every `k != i`,
\[
 k\in F_i
 \quad\Longrightarrow\quad
 j_i\left(\frac12-\epsilon\right)
 \le q_{ik}\le
 j_i\left(\frac12+\epsilon\right),
\tag{2.1}
\]
while
\[
 k\notin F_i
 \quad\Longrightarrow\quad
 q_{ik}\le \epsilon j_i.
\tag{2.2}
\]

### Proof

Under `U_{F_i}`, the event `k in B` has probability `1/2` if `k in F_i` and `0` otherwise. Total variation changes the probability of any event by at most `epsilon`. Since
\[
 \nu_i(k\in B)=\frac{q_{ik}}{j_i},
\]
(2.1)-(2.2) follow immediately. QED.

This turns fleet03's exact pair curvature `q_ik=kappa_ik/4` into a robust **trigger test**.

## 3. PROVED: nonreciprocal triggers are strict influence-scale escapes

### Theorem B12-SCALE-ESCAPE-02

Suppose rows `i` and `k` are both epsilon-Palm-robust and `k in F_i`.

If `i notin F_k`, then
\[
 \boxed{
 j_k\ge
 G_\epsilon j_i,\qquad
 G_\epsilon:=\frac{1/2-\epsilon}{\epsilon}.
 }
\tag{3.1}
\]
At `epsilon=1/16`,
\[
 \boxed{j_k\ge7j_i.}
\tag{3.2}
\]

If instead `i in F_k`, then
\[
 \boxed{
 R_\epsilon^{-1}
 \le\frac{j_k}{j_i}\le
 R_\epsilon,\qquad
 R_\epsilon:=\frac{1/2+\epsilon}{1/2-\epsilon}.
 }
\tag{3.3}
\]
At `epsilon=1/16`, `R_epsilon=9/7`.

### Proof

If `k in F_i`, (2.1) gives
\[
 q_{ik}\ge j_i(1/2-\epsilon).
\]
If `i notin F_k`, (2.2) applied to row `k` gives
\[
 q_{ik}=q_{ki}\le\epsilon j_k,
\]
which proves (3.1).

If the trigger is reciprocal, apply (2.1) in both directions to the same symmetric mass `q_ik`; division yields (3.3). QED.

Thus a robust trigger edge has only two possibilities:

1. **comparable scale and reciprocal**, or
2. **nonreciprocal and geometrically increasing influence**.

This is the first influence-relative nonreuse structure of the current robust-row branch.

## 4. PROVED: reciprocal robust rows have exactly the same trigger signature

The pair statement alone does not yet justify contracting a cluster: two reciprocal rows might conceivably share only each other but disagree on all other triggers. The three-coordinate Palm events rule this out.

### Theorem B12-TRIGGER-LOCKING-03

Assume `epsilon<=1/16`. If robust rows `i,k` satisfy
\[
 k\in F_i,\qquad i\in F_k,
\]
then
\[
 \boxed{
 F_i\setminus\{k\}=F_k\setminus\{i\}.
 }
\tag{4.1}
\]
Equivalently, with
\[
 T_i:=\{i\}\cup F_i,
\]
one has
\[
 \boxed{T_i=T_k.}
\tag{4.2}
\]

### Proof

Suppose, for contradiction, that there is
\[
 \ell\in F_i\setminus\{k\},
 \qquad
 \ell\notin F_k.
\]
Let
\[
 t_{ik\ell}:=\Pr(i,k,\ell\in S).
\]
Under `U_{F_i}`, the event `{k,l} subseteq B` has probability `1/4`. Hence
\[
 t_{ik\ell}
 \ge j_i\left(\frac14-\epsilon\right).
\tag{4.3}
\]
Under `U_{F_k}`, the event `{i,l} subseteq B` has probability zero because `l notin F_k`. Hence
\[
 t_{ik\ell}\le\epsilon j_k.
\tag{4.4}
\]
Reciprocity and (3.3) give
\[
 j_k\le R_\epsilon j_i.
\]
Therefore (4.3)-(4.4) would require
\[
 \frac14-\epsilon\le R_\epsilon\epsilon.
\tag{4.5}
\]
At `epsilon<=1/16`, the left side is at least `3/16`, while at the endpoint the right side is
\[
 \frac97\cdot\frac1{16}=\frac9{112}<\frac3{16},
\]
a contradiction. Thus
`F_i\setminus{k} subseteq F_k\setminus{i}`; symmetry gives the reverse inclusion. QED.

### Corollary B12-EXACT-TRIGGER-COMPONENTS-04

Make an undirected graph on robust rows, joining `i,k` exactly when the trigger relation is reciprocal. Every connected component `C` has one exact common trigger signature `T_C` such that
\[
 \boxed{F_i=T_C\setminus\{i\}\quad(i\in C).}
\tag{4.6}
\]

This is much stronger than a vague similarity cluster: all reciprocal robust rows expose exactly the same Boolean trigger block.

## 5. PROVED: the robust quotient graph is scale-acyclic

Contract the reciprocal components of Corollary 04. If a robust row in component `C` points by a trigger to a robust row in a different component `D`, reciprocity is impossible, hence Theorem 02 gives
\[
 j_D\ge7j_C
\tag{5.1}
\]
at `epsilon=1/16` (interpreting the statement rowwise for the actual endpoints).

Therefore every cross-component robust trigger edge strictly increases influence scale. In particular:

- there is no directed cycle after reciprocal contraction;
- along any chain of nonreciprocal robust trigger edges,
  \[
  j_{i_t}\ge7^t j_{i_0};
  \]
- because every influence is at most `I=sum_i j_i`, such a chain has length at most
  \[
  \left\lfloor\log_7\frac I{j_{i_0}}\right\rfloor.
  \tag{5.2}
  \]

The high-depth robust sector is therefore not an arbitrary congested graph. It is an exact-block DAG with geometrically separated scales.

## 6. PROVED: in the physical near-subcube sector, each scale escape drops codimension by at least three

Now add the physical information already present in the fleet04 near-subcube branch. Suppose the same trigger set `F_i` comes from a coordinate subcube of measure
\[
 s_i=2^{-|F_i|}
\]
whose support approximation satisfies
\[
 |s_i-j_i|\le\rho j_i,\qquad \rho\le1/16.
\tag{6.1}
\]
For a nonreciprocal robust trigger edge `i -> k`, (3.2) gives `j_k>=7j_i`. Thus
\[
 \frac{s_k}{s_i}
 \ge
 \frac{(1-\rho)j_k}{(1+\rho)j_i}
 \ge
 7\frac{15}{17}
 =\frac{105}{17}>4.
\tag{6.2}
\]
But `s_k/s_i` is an integral power of two. Hence it is at least `8`, so
\[
 \boxed{|F_k|\le|F_i|-3.}
\tag{6.3}
\]

So, inside the doubly robust physical/Palm sector, every nonreciprocal transition removes at least three trigger coordinates at once. The hierarchy has a literal integer depth drop, not only an asymptotic scale separation.

## 7. What this does and does not pay

This theorem directly implements the cluster side of the fleet03/B12 dichotomy:

- fleet03 proved that raw pairwise KL terms cannot be summed because a latent cluster bit is redundantly visible many times;
- the present theorem proves that sufficiently robust comparable-scale rows are not merely correlated -- they have **one identical trigger signature and may be contracted as one block**;
- any robust trigger that escapes that block must jump upward by at least a factor `7` in influence, and in the physical near-subcube sector drops codimension by at least `3`.

This is a genuine reduction of the remaining high-depth cluster branch.

It is **not yet a proof of FEI**. In particular, the current argument does not bound the total branching/address entropy of many small components feeding a larger component, and it does not control targets that are outside the robust sector. Mixed-curvature conservation still has to be combined with this exact-block hierarchy so that each cross-component resource is charged only once. The majority obstruction to paying the entire raw depth bank remains binding.

## 8. Exact finite diagnostic check

`check_palm_trigger_clusters.py` was executed with exact rational arithmetic. It enumerates all Boolean truth tables up to dimension four after quotienting by global sign, computes exact Walsh-square spectra and Palm laws, chooses the closest uniform power-set trigger law, and checks:

- trigger/nontrigger pair-mass bounds;
- the factor-7 nonreciprocal scale escape;
- the `9/7` reciprocal influence ratio;
- exact reciprocal trigger-signature locking;
- common signature on every reciprocal connected component.

Results:

| n | Boolean functions checked | functions with robust rows | robust rows | reciprocal directed edges |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 0 |
| 2 | 8 | 6 | 10 | 8 |
| 3 | 128 | 95 | 159 | 120 |
| 4 | 32768 | 7996 | 11188 | 7728 |

There were **zero violations**. The checker SHA-256 is
`f7bc64a2786674574f87fae31c6092350078685e32fa503fce070880bd67fed7`.

This finite enumeration is diagnostic evidence only. The proof is the event/TV argument above.

## 9. Next implication

The next precise target is a **component-level charging lemma**.

Let the reciprocal components be contracted and keep only robust-to-robust cross-component trigger edges. Because all rows in a component have one common trigger signature, repeated rowwise payment should be replaced by one block activation. Because every outgoing component transition increases influence by at least `7`, the remaining charge is a geometrically ordered DAG rather than the raw factorial-depth bank.

The missing implication is to prove that the exact prefix/factorial rebate from the fleet03 Palm insertion code pays:

1. one activation for each reciprocal trigger block, plus
2. its nonreciprocal scale escapes,

with total `O(I)` cost, while preserving fleet04/B18's mixed-curvature/nonreuse constraints. A proof of that charging lemma would remove the present robust high-depth-cluster obstruction; nonrobust rows would remain as the separate stability sector.

**Full FEI remains OPEN.**
