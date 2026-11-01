# FOREST / fleet03 B03 — exact K_{3,n} stress family and the missing minimal-core constraint

**Run:** `20260922T073110Z-fleet03-B03-forest-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-K3N-MINIMALITY-STRESS-v1`  
**Parent target:** **OPEN**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source scope and named peer result consumed

The target is the Grimmett--Winkler law on **all unrooted forests** of every finite simple graph: the empty forest, disconnected forests, and every forest size are retained. For distinct edges `e,f`, write

`Delta(e,f)=Z_e Z_f-Z Z_ef`.

The target is `Delta(e,f)>=0` for every finite simple graph. No rooted, fixed-size, spanning-tree, or arbitrary-weight statement is substituted for this source statement.

I consumed the latest complete assigned-partner result available at the run snapshot: **fleet04/B01**, run `fleet04-b01-20260922T061100Z-forest-r12`, candidate `FOREST-MULTIGRAPH-SIMPSON-CLOSURE-v1`, scientific blob `7273e128225a5cbbfa2fd3a70ad7d66f3581f85a`.

Its exact structural input is this. If the source conjecture fails and `G` is chosen edge-minimal among finite labelled loopless multigraph counterexamples, with a positively correlated violating pair `e,f`, set `a=rho_ef>0`. Deletion and contraction by every third edge `g` are smaller exact loopless-multigraph instances, so the total-covariance identity gives

`rho_eg rho_fg >= rho_ef = a > 0`                                            (1)

for every `g` outside `{e,f}`. In particular `rho_eg,rho_fg<0`, positive-covariance pairs form a matching, and the inherited complete-log-concavity row budget yields

`T_e+T_f+a^2+(m-2)a <= 1`.                                                    (2)

The partner's first unpaid step is that (2) alone is not contradictory and the minimal-multigraph structure has not yet been transferred sharply to the separate rational-weight 3-connected-core reduction.

This run attacks exactly that gap by computing a non-series-parallel 3-connected asymptotic family and asking which parts of (1) can possibly follow from core geometry alone.

## 2. Exact transfer matrix for K_{3,n}

Let the left class of `K_{3,n}` be `{A,B,C}` and the right class be `{r_1,...,r_n}`. For `n>=3` the graph is 3-connected: deleting at most two vertices leaves at least one vertex on each side and hence a connected complete bipartite remainder.

Process the right vertices one at a time. A partial forest induces one of five connectivity partitions on `{A,B,C}`:

`0=A|B|C`, `1=AB|C`, `2=AC|B`, `3=A|BC`, `4=ABC`.

When a fresh right vertex is introduced, a chosen subset of its three incident edges is admissible exactly when it meets each existing connectivity block in at most one left vertex. In the state order above, the exact transfer matrix is

```
T = [[4,1,1,1,1],
     [0,4,0,0,2],
     [0,0,4,0,2],
     [0,0,0,4,2],
     [0,0,0,0,4]].
```

Put `T=4I+N`. Then `N^3=0` and the only nonzero entry of `N^2` is `(0,4)=6`, so `T^n` is explicit. Starting from `(1,0,0,0,0)` and summing final states gives

`Z_n = 4^(n-2) (3n^2+13n+16)`.                                               (3)

For a marked edge `A-r`, the corresponding inclusion transition is

```
E_A = [[1,1,1,0,1],
       [0,1,0,0,1],
       [0,0,1,0,1],
       [0,0,0,1,2],
       [0,0,0,0,1]].
```

Thus `Z_e = v E_A T^(n-1) 1`. Two marked right vertices are evaluated by inserting two marked transition matrices; two marked edges on the same right vertex use the transition that requires both selected edges. Straight expansion gives the formulas below.

## 3. Exact all-n forest-pair counts

All edges have the same one-edge count

`Z_e = 4^(n-3) (3n^2+23n+38)`.                                               (4)

There are three pair orbits.

**Same left endpoint, different right endpoints** (`SL`, e.g. `A-r_1,A-r_2`):

`Z_ef^SL = 3*4^(n-4)(n^2+11n+22)`,

`Delta_SL = 2*16^(n-3)(41n^2+181n+194) > 0`.                                 (5)

**Vertex-disjoint endpoints** (`D`, e.g. `A-r_1,B-r_2`):

`Z_ef^D = 4^(n-4)(3n^2+33n+82)`,

`Delta_D = 2*16^(n-3)(17n^2+77n+66) > 0`.                                    (6)

**Same right endpoint** (`SR`, e.g. `A-r_1,B-r_1`):

`Z_ef^SR = 8*4^(n-3)(n+3)`,

`Delta_SR = 16^(n-3)(n-1)(9n^3+51n^2+104n+92)`.                              (7)

Hence the complete family `K_{3,n}` satisfies the source negative-correlation inequality for every pair; equality occurs only in the trivial `n=1` same-right case, and all three orbit gaps are strictly positive once they exist nontrivially.

This is an exact structured theorem, not a finite census.

## 4. Exact correlations and the asymptotic stress

Let

`A_n=3n^2+23n+38`, `B_n=9n^2+29n+26`.

Because `rho_ef = -Delta(e,f)/(Z_e (Z-Z_e))`, equations (3)--(7) give

`rho_SL = -2(41n^2+181n+194)/(A_n B_n)`,

`rho_D  = -2(17n^2+77n+66)/(A_n B_n)`,

`rho_SR = -(n-1)(9n^3+51n^2+104n+92)/(A_n B_n)`.                              (8)

Therefore

`rho_SL ~ -82/(27n^2)`, `rho_D ~ -34/(27n^2)`, while `rho_SR -> -1/3`.         (9)

So a genuinely 3-connected graph with many overlapping cycles can simultaneously contain order-one local correlations and order-`n^-2` correlations.

Now choose the weak pair `e=A-r_1`, `f=A-r_2`, and a third edge `g=B-r_3` (`n>=3`). Both `rho_eg` and `rho_fg` are of the disjoint orbit. The ratio of the product magnitude to the marked-pair magnitude is

`R_n = rho_D^2/|rho_SL|`

`    = 2(17n^2+77n+66)^2 / [(41n^2+181n+194) A_n B_n]`.                        (10)

The denominator of (10) minus its numerator is exactly

`1107 n^6 + 16941 n^5 + 102441 n^4 + 318247 n^3`
`+ 542740 n^2 + 488300 n + 182960`,                                           (11)

which is positive for every `n>0`. Hence

`R_n < 1` for every `n>=3`, and `R_n ~ 578/(1107 n^2)`.                        (12)

For example `R_3≈0.0140862`, already a factor about 71 below one, and the ratio tends to zero quadratically.

## 5. What this rules out, and the sharpened missing implication

Equation (1) is therefore **not** a generic consequence of 3-connectivity, dense overlapping cycles, or a lower bound on nonzero correlation magnitudes. `K_{3,n}` supplies exact source-model witnesses in which a natural third-edge product is smaller than the marked correlation magnitude by a factor `Theta(n^-2)`. In terms of `m=3n`, honest correlations of order `m^-2` occur in the hard 3-connected regime.

This does not refute the partner theorem: (1) is asserted for a **positive pair in an edge-minimal counterexample**, whereas every pair in `K_{3,n}` is negatively correlated. Instead it identifies the indispensable structure that a closing argument must preserve.

**Sharpened missing implication (`FOREST-MINIMAL-CORE-BRIDGE-v1`).** Any route combining the partner's minimal-loopless-multigraph theorem with the rational-weight 3-connected-core theorem must preserve enough of edge-minimality/positive-pair structure that the all-edge product domination (1), or a quantitatively equivalent contradiction, survives the passage to the core. It cannot replace that step by “3-connected graphs have correlations bounded away from zero” or by a sign-agnostic magnitude estimate.

Equivalently, a direct contradiction inside the minimal multigraph universe must use the simultaneous concentration demanded by (1): **all** `m-2` third edges are negative to both endpoints of one positive pair and every product is at least `a`. The exact `K_{3,n}` family shows that ordinary 3-connected correlation geometry does not come close to this pattern.

This is the useful structural constraint from the failed adversary: the remaining proof must be *minimality-sensitive*, not merely *core-connectivity-sensitive*.

## 6. Independent exact regression

A standard-library checker enumerated every edge subset of `K_{3,n}` for `1<=n<=5`, retained exactly the acyclic subsets, and independently verified (3)--(7) for every applicable orbit. Selected exact values are:

- `n=3`: `Z=328`, `Z_e=134`, `Delta_SL=2212`, `Delta_D=900`, `Delta_SR=2212`;
- `n=4`: `Z=1856`, `Z_e=712`, `Delta_SL=50368`, `Delta_D=20672`, `Delta_SR=91200`;
- `n=5`: `Z=9984`, `Z_e=3648`, `Delta_SL=1087488`, `Delta_D=448512`, `Delta_SR=3084288`.

It also checks the exact positive-coefficient polynomial (11) and rational values of `R_n` for `3<=n<=9`. Checker SHA-256: `c99b928a5c272fbd6f0b84cd8b35bec7000fa72182cb084720ba98eabd156bdf`. Output SHA-256: `14c262bbf4d8a08ba6c1636af86dff4d9140cb67893db5310f0f8dd22ac65b1b`.

## 7. Status and next recipient

The parent FOREST conjecture remains **OPEN**. No source-valid counterexample was found. The new exact family validates the conjectured sign on a hard structured class while decisively eliminating a tempting generic magnitude/core-connectivity closure of the current Simpson-budget route.

Next mathematical action for the team: prove `FOREST-MINIMAL-CORE-BRIDGE-v1`, or remain entirely in the edge-minimal loopless-multigraph universe and derive a contradiction from the simultaneous product constraints plus a genuinely minimality-sensitive identity. Recipient: assigned partner `fleet04/B01` and FOREST lead `fleet01/B01`.

## 8. Provenance

- Current target/control package: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, owner control revision `2026-09-22.2`.
- Assigned partner consumed: fleet04/B01, `fleet04-b01-20260922T061100Z-forest-r12`, `FOREST-MULTIGRAPH-SIMPSON-CLOSURE-v1`, report blob `7273e128225a5cbbfa2fd3a70ad7d66f3581f85a`.
- Exact checker/output are in this immutable run directory.
- No installed brain retrieval or receiver-context use occurred; this run is `WITHOUT_VERIFIED_BRAIN`.

Scoped privacy/provenance review: only mathematical formulas, logical account/slot identifiers, source-bound peer identifiers, and control revision are included. No credentials, scheduler identifiers, machine paths, email/Drive material, benchmark gold, unrelated private transcripts, public posting, paid API/model/Codex use, or remote workflow dispatch occurred.
