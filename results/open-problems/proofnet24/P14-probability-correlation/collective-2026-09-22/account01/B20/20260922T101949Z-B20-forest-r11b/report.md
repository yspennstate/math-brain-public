# FOREST / account01 B20 — source-safe weighted nullity-three exclusion and a support-nullity squeeze

**Run:** `20260922T101949Z-B20-forest-r11b`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** **OPEN**  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh source state and correction boundary

The target is the original Grimmett--Winkler unit law: for every finite simple graph `G`, with `F` uniform over every acyclic edge subset (all sizes, disconnected forests included), prove for every distinct pair of physical edges `e,f`

`P(e,f in F) <= P(e in F) P(f in F)`.

Fresh controls were read from `yspennstate/math-research-brain` at commit `5ead403d17d1b7917780a7531af081d06eb4e6df`, owner-control revision `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. No new brain-installation or benchmark work is used here.

Latest complete campaign-lead version consumed: account01/B01

`20260922T080733Z-b01-forest-auto11/report.md`, blob `7eccff21a034648951b1a5886db0330b60c3a5da`, candidate `FOREST-CERTIFIED-CONTRACTION-STAR2-v2`.

Its exact residual was the source-generated `{1,2}` STAR-2 contraction law and, beyond that, a graph-global compatibility step.

Named assigned OTHER-account result actually consumed and applied: account04/B03

`20260922T070756Z-B03-forest-r12-34330b0f/report.md`, blob `a09681b45ae7e7e2d470fb5a2cdcd23c5c51fa38`.

Its source-safe core is the edge-minimal **loopless labelled multigraph** contradiction frame. If `e,f` are a violating pair and

`C_ij=Cov(X_i,X_j)`, `v_i=Var(X_i)`, `rho_ij=C_ij/sqrt(v_i v_j)`, `a=rho_ef>0`,

then for every third physical label `g`

`C_eg C_fg >= C_ef v_g`,

hence

`rho_eg rho_fg >= a`,

and positive-covariance pairs form a matching. Therefore every third label has

`rho_eg<0`, `rho_fg<0`.

I also retain the source-safe ground-set completely-log-concave two-row inequality from B20 `20260922T084701Z-B20-forest-r11`, blob `06b8ee47c9219a00ac5e06f8c21890ac3422b9ef`.

### Correction to the immediately preceding B20 route

The preceding B20 report `20260922T094714Z-B20-forest-r11`, blob `7a63fff1877f546700ebfc4cdca77fd908475129`, returned to an edge-minimal **simple** counterexample by importing a purported fixed-graph Cocks upgrade. A later source audit already present in the repository, account02/B02 `B02-20260922T013646Z-forest-r12/cocks_scope_correction.md`, blob `733d840093ca109d38f4e336d228ae1ddedf77c0`, records that the accessible Cocks mechanism is class-level and does not source-secure the implication

`unit pNC on one fixed G => all-positive-weight pNC on the same G`.

Accordingly this run does **not** use that fixed-graph step. Historical artifacts are left unchanged. The simple-category density consequences in the preceding B20 report are not treated as accepted source-safe progress here. The ground-set CLC algebra itself survives and is re-used below entirely inside account04/B03's loopless-minimal frame.

## 2. Marked edges are singleton parallel classes

Let `M` be a minimum-labelled-edge loopless multigraph counterexample and `e,f` a violating pair, so `C_ef>0`.

The two marked labels cannot lie in the same parallel class: then they are mutually exclusive and their covariance is negative.

More strongly, neither marked label has any other parallel mate. Suppose `g != e` is parallel to `e`. Label symmetry of the uniform forest law gives

`Cov(X_f,X_g)=Cov(X_f,X_e)=C_ef>0`.

But account04/B03's all-conditioner Simpson theorem implies that the graph on physical labels whose edges are positive-covariance pairs is a matching. The positive pairs `(f,e)` and `(f,g)` would share `f`, contradiction. Thus `e` and `f` each form singleton parallel classes.

This small fact is load-bearing below because it lets us collapse all other parallel classes without changing the marked observables themselves.

## 3. Collapse to a weighted simple support graph

Collapse each parallel class of `M` to one edge of a simple support graph `H`, and give that support edge activity equal to the positive integer size of the class. Every support forest `A` has exactly the product of those class sizes over `A` labelled lifts. Hence the push-forward of the unit labelled-multigraph forest law is exactly the positive-integer-weight forest law on `H`.

Because the marked classes are singleton, the effective indicators of their support edges are exactly `X_e,X_f`. Therefore their positive covariance survives the collapse unchanged.

The weighted forest polynomial factors over the 2-connected blocks (bridges being one-edge factors), because a set of graph edges is acyclic if and only if its restriction to every block is acyclic. Consequently two edges in different blocks are independent under every product edge weighting. Hence the two marked support edges lie in one common nontrivial block `B`, and that weighted block itself has a positive marked covariance.

The next theorem gives a new restriction on `B`.

## 4. New theorem: every simple graph of block cyclomatic number at most three is weighted I-Rayleigh

For a connected graph put

`nu(G)=|E(G)|-|V(G)|+1`.

### Theorem `FOREST-WEIGHTED-NULLITY3-20260922`

If every nontrivial 2-connected block of a finite simple graph `G` has cyclomatic number at most `3`, then for every positive real edge weighting and every distinct pair `i,j`,

`Delta_G(i,j) >= 0`.

The proof is self-contained apart from the standard graph-theoretic characterization of 2-connected `K4`-minor-free graphs as series-parallel graphs.

### 4.1 Exact weighted series and parallel closure

Write the forest polynomial of a graph with a distinguished edge `g` as

`Q(z)=Z0+z Z1`,

where `Z0` is the deletion polynomial and `Z1=dQ/dz`.

#### Parallel extension

Replace `g` by parallel edges of weights `x,y`. Then

`P=Z0+(x+y)Z1`.

For two unaltered marked edges, the Rayleigh difference is the base difference evaluated at `z=x+y`. For the new pair,

`Delta_P(x,y)=Z1^2 >=0`.

For a new edge `x` and an outside marked edge `h`,

`Delta_P(x,h)=Z1 Z0_h-Z0 Z1_h=Delta_Q(g,h)`.

So all-positive-weight forest Rayleigh is preserved by parallel extension.

#### Series extension

Replace `g` by a two-edge path of weights `x,y`. A forest which does not use the base connection has local factor `1+x+y`, while a forest which uses the base connection must use both path edges. Thus

`P=(1+x+y)Z0+xy Z1`.

Put `A=1+x+y` and `q=xy/A`. For two outside marked edges,

`Delta_P(h,k)=A^2 Delta_Q(h,k; z=q)`.

For the two new series edges,

`Delta_P(x,y)=Z0(Z0-Z1)>=0`.

Here `Z0-Z1` has nonnegative coefficients: `Z1` counts exactly the deletion-forests to which the deleted edge can be added, a subfamily of all deletion-forests counted by `Z0`.

Finally, for a new edge `x` and an outside edge `h`,

`Delta_P(x,h)=y(1+y) Delta_Q(g,h)>=0`,

and symmetrically for `y`.

Hence weighted forest Rayleigh is preserved by series extension as well.

It follows immediately that every series-parallel graph is weighted I-Rayleigh.

### 4.2 Exact weighted `K4` base case

There are only two edge-pair orbits in `K4`: adjacent and disjoint.

Label

`a=01, b=02, c=03, d=12, e=13, f=23`.

Because the forest polynomial is multiaffine, the Rayleigh difference for a marked pair is independent of the two marked activities themselves.

For the adjacent pair `(a,b)`, direct exact expansion gives

`Delta_ab = d^2(1+c+e+f)^2`
`         + d(1+c+e+f)(1+c+e+f+2ef)`
`         + ef(1+e)(1+f) >=0`.

For the disjoint pair `(a,f)`,

`Delta_af = (be-cd)^2 + be(1+b+e) + cd(1+c+d) >=0`.

Thus `K4` is weighted I-Rayleigh for every positive weighting.

### 4.3 The cyclomatic-three structure

Let `B` be a 2-connected simple block with `nu(B)<=3`.

If `B` has no `K4` minor, it is series-parallel, hence weighted I-Rayleigh by Section 4.1.

Suppose it has a `K4` minor. Since `K4` has maximum degree three, a `K4` minor model contains a subdivision `S` of `K4`. Subdivision preserves cyclomatic number, so `nu(S)=3`. Hence `nu(B)=3` as well.

There can be no proper 2-connected enlargement of `S` inside `B` without increasing cyclomatic number: an extra edge between existing vertices, or an ear whose internal vertices are new and whose endpoints lie in the existing 2-connected subgraph, increases `|E|-|V|+1` by one. A component attached at only one existing vertex would violate 2-connectivity. Therefore `B` itself is a subdivision of `K4`.

Repeatedly applying the exact series-extension formula to the weighted `K4` base case proves that `B` is weighted I-Rayleigh.

Finally the block product factorization proves the theorem for all of `G`.

## 5. Consequence for a minimal loopless multigraph counterexample

Return to the support graph `H` of the edge-minimal loopless multigraph counterexample `M`. Its marked block `B` carries a positive weighted covariance, so Section 4 rules out

`nu(B)<=3`.

Therefore every source counterexample surviving account04/B03's loopless-minimal reduction must satisfy

`boxed: nu(B) >= 4.`

This is a graph-global support restriction, not a local three-edge inequality and not a weighted strengthening assumed from the original conjecture: the weighted theorem has been proved explicitly for this low-cyclomatic class.

## 6. Source-safe nullity / parallel-excess squeeze

Now combine the preceding support theorem with the source-safe CLC two-row inequality already proved in B20 `20260922T084701Z` inside the same loopless-minimal category.

Let

`m=|E(M)|`, `K=|F|`, `mu=E K`, `delta=m-mu`, `s=p_e+p_f`,

and retain `a=rho_ef>0`. That theorem gives

`(2-s)a^2 + 2a(2delta-3+s) + (t_e+t_f)^2 <= s`.

Drop the nonnegative square and move the right side left. As a function of `s` the remaining expression has derivative

`-(1-a)^2 <=0`.

Every physical edge in the unit down-set has marginal at most `1/2` by deletion injection, so `s<=1`. Therefore evaluation at `s=1` gives the source-safe universal consequence

`boxed: a^2 + 4a(delta-1) <=1.`

Let `r(M)` be the graphic-matroid rank. Every forest has size at most `r(M)`, so `mu<=r(M)` and

`delta>=m-r(M)=:nu(M)`.

Thus

`boxed: a^2+4a(nu(M)-1)<=1.`                                      (6.1)

Let `E` be the total parallel excess of `M`, i.e. the number of physical labels beyond one representative in each support class. Collapsing parallel classes preserves rank, so

`nu(M)=nu(H)+E`.

The marked support block already has `nu(B)>=4`, hence `nu(H)>=4`. Inserting this into (6.1) gives the new exact ladder

`boxed: a^2+4a(E+3)<=1,`                                          (6.2)

or equivalently

`boxed: a <= sqrt(4(E+3)^2+1)-2(E+3).`                            (6.3)

In particular:

- if `E=0`, then `a<=sqrt(37)-6 = 0.0827625302982196890...`;
- if `E>=1`, then `a<=sqrt(65)-8 = 0.0622577482985496524...`;
- if `E>=2`, then `a<=sqrt(101)-10 = 0.0498756211208902702...`;
- if `E>=3`, then `a<=sqrt(145)-12 = 0.0415945787922954801...`.

Equivalently,

`E <= (1-a^2)/(4a)-3`.

This is strictly source-safer than the preceding B20 simple-density squeeze because it never leaves the loopless-minimal contradiction frame and never invokes the disputed fixed-graph Cocks upgrade.

## 7. Exact checker

`weighted_nullity3_checker.py` independently enumerates the `K4` forest polynomial, verifies both orbit formulas symbolically, verifies the exact series/parallel extension identities, and verifies the root ladder. Its archived output is:

```text
K4_WEIGHTED_RAYLEIGH_CHECK=PASS
ADJACENT_FORMULA=d^2(1+c+e+f)^2+d(1+c+e+f)(1+c+e+f+2ef)+ef(1+e)(1+f)
DISJOINT_FORMULA=(be-cd)^2+be(1+b+e)+cd(1+c+d)
SERIES_PAIR_FORMULA=Z0*(Z0-Z1)
SERIES_MIXED_FORMULA=y*(1+y)*(Z1*Z0h-Z0*Z1h)
PARALLEL_PAIR_FORMULA=Z1^2
PARALLEL_MIXED_FORMULA=Z1*Z0h-Z0*Z1h
E=0 a_max=0.0827625302982196890
E=1 a_max=0.0622577482985496524
E=2 a_max=0.0498756211208902702
E=3 a_max=0.0415945787922954801
STATUS=PASS
```

The computation is regression only; Sections 4 and 6 are symbolic proofs.

## 8. Compact end-to-end state and first unpaid universal implication

The source-safe chain after this run is:

1. assume the original simple-unit target fails and choose a minimum-labelled-edge counterexample in the larger loopless-multigraph class;
2. account04/B03 gives good deletion/contraction strata for every third physical label, hence all-edge Simpson and the positive-pair matching geometry;
3. the violating marked labels are necessarily singleton parallel classes;
4. collapse the remaining parallel classes to integer activities on a simple support graph `H`; the positive marked covariance survives exactly;
5. the new weighted-nullity-three theorem forces the marked support block to have cyclomatic number at least four;
6. the source-safe CLC two-row inequality then forces the quantitative nullity/parallel ladder (6.2)--(6.3);
7. the earlier exact path-cut flux identities and multi-step quotient-path completion remain the graph-global mechanism available beyond this spectral/localization stage.

The parent FOREST conjecture remains **OPEN**. The first unpaid universal implication is now more specific:

> rule out an edge-minimal loopless graphic counterexample whose marked support block has cyclomatic number at least four, whose positive-correlation graph is a matching, whose violating pair is negative-correlated with every other physical label and satisfies the all-edge Simpson products, and whose violation obeys the nullity/parallel cap (6.3).

A useful exact target for the transport programme is to derive from the path-cut / quotient-flow identities either the Rayleigh inequality directly or a lower bound on `a` exceeding

`sqrt(4(E+3)^2+1)-2(E+3)`.

The new theorem eliminates every weighted support block of cyclomatic number at most three before that flow problem even begins. It also makes repeated parallel labels quantitatively more expensive rather than treating them as unstructured multiplicity.

## 9. Honest classification and preserved failures

**Classification: `ESSENTIAL_STEP_APPLIED`.** The support of any source-equivalent minimal counterexample is now forced beyond weighted cyclomatic number three, and the violation satisfies the new source-safe nullity/parallel ladder.

Preserved boundaries:

- no full FOREST proof is claimed;
- no fixed-graph Cocks upgrade is used;
- the preceding B20 report's Cocks-dependent simple-category deductions are not promoted;
- no rank-degree homogenization is used;
- no finite census is promoted to a universal theorem;
- no claim of novelty or priority is made;
- no new brain installation or benchmark work was performed;
- no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private transcripts, email, Drive, public posting, paid/remote model call, workflow dispatch, permission bypass, B21/B22, or cross-account native action is included.

## 10. Model / effort / provenance

Model self-report: `GPT-5.6 Sol`.  
Requested effort: maximum actually supported.  
Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning-token/time usage: `UNKNOWN_NOT_EXPOSED` (unknown is not zero).  
Brain context: `WITHOUT_VERIFIED_BRAIN`.
