# FOREST fleet02/B01 — unit-minor contraction plus exact 3-terminal response residual

Run: `B01-20260922T032950Z-forest-r13`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Secondary finding: **CANDIDATE_REFUTED** for triangle-only compression of a general 3-terminal separator side.  
Parent target: **not promoted by this run**  
Context: **WITHOUT_VERIFIED_BRAIN**

## 1. Source-bound state actually consumed

The active target is the uniform law on all unrooted acyclic edge subsets of a finite simple graph, with unit edge weights. The required inequality is pairwise negative edge correlation.

This run consumed the latest lead handoff `FOREST-KN-COCKS-RECONCILED-v3`, path

The named OTHER-account result actually applied is the partner fleet03/B02 handoff
`fleet03-B02-20260922T0322Z-theta3-multigraph-reduction.md`, blob `3ca8177c939ff28e9b192276e478940e7fda4f9b`. Its exact contribution is the unit-law equivalence between finite simple graphs and finite loopless multigraphs obtained by the theta-3 replacement, together with the unit-minor sign-cluster consequence.

I also retained the exact prior B01 two-separator reduction, report blob `59fb19252eaa411eb1d321035e40721a15c6477f`, and fleet01/B03's aggregate overlap budget, handoff blob `224b6c313cff2cedc570c6133861a2d3a4a55549`, as constraints. No benchmark material or brain-installed memory was used.

## 2. Conditional end-to-end route for this alternative mechanism

A fully internal separator/deletion-contraction route would now read:

1. use partner theta-3 simulation to pass from the simple target to the equivalent loopless-multigraph unit target;
2. choose an edge-minimal loopless-multigraph counterexample `(M,e,f)`;
3. use deletion and contraction of every third edge as *unit* smaller minors, giving exact all-third-edge Simpson sign forcing without any weighted contraction theorem;
4. use separator transfer while retaining the complete boundary partition law, not merely a normalized scalar or guessed edge activities;
5. rule out all possible separator responses and finally the 3-connected/sign-cluster core.

Step 3 is now source-valid from the partner theorem. This run adds two new facts needed for steps 3--4: the marked edges of an edge-minimal multigraph counterexample must be singleton parallel classes, and a general 3-terminal separator response has exactly one scalar degree of freedom beyond a weighted boundary triangle. The latter scalar is genuinely nonzero even for the 3-spoke star, so a triangle-only reduction is false.

## 3. Pure unit deletion-contraction: no Cocks or weighted quotient is needed for the contraction endpoint

Assume the target is false. By the partner theta-3 theorem, it is false on loopless multigraphs as well. Choose a loopless multigraph `M` with the fewest nonloop edges admitting a bad pair `e,f`, and let `X_e,X_f` be the corresponding edge indicators under the unit uniform forest law.

Fix a third nonloop edge `g`, write `T=X_g`, `p=P(T=1)`, and

`c = Cov(X_e,X_f) > 0`.

Conditioning on `T=0` gives the unit forest law of `M\g`. Conditioning on `T=1`, followed by contraction of `g` and deletion of loops, gives the unit forest law of the smaller loopless multigraph `M/g`. Both have fewer nonloop edges, so edge-minimality gives conditional covariances

`c_0 = Cov(X_e,X_f | T=0) <= 0`,
`c_1 = Cov(X_e,X_f | T=1) <= 0`.

The exact total-covariance identity is

`c = (1-p)c_0 + p c_1 + p(1-p)(mu_e^1-mu_e^0)(mu_f^1-mu_f^0)`.

Also

`Cov(X_e,T)=p(1-p)(mu_e^1-mu_e^0)`,
`Cov(X_f,T)=p(1-p)(mu_f^1-mu_f^0)`,
`Var(T)=p(1-p)`.

Therefore, for **every** third edge `g`,

`Cov(X_e,T) Cov(X_f,T) / Var(T)
 = c - (1-p)c_0 - p c_1
 >= c > 0`.                                            (3.1)

Thus the two covariance rows have the same strict sign at every third edge. This reproduces the partner's qualitative sign-cluster statement, but the point for this B01 route is methodological: the contraction endpoint is now paid entirely by smaller *unit* minors. The previous B01 use of fixed-graph Cocks to absorb parallel-class weights is no longer needed for this endpoint.

## 4. New structural lemma: the bad marked edges are singleton parallel classes

The partner reduction moves the minimal problem to loopless multigraphs, so parallel classes must be handled exactly rather than silently simplified.

**Lemma.** In an edge-minimal loopless-multigraph counterexample `(M,e,f)`, neither marked edge has a parallel mate.

Proof. Suppose the parallel class `C` containing `e` has size `m>=2`. Since parallel edges cannot co-occur in a forest, `f` is not in `C` for a bad pair. Collapse only the labelled class `C` to one class-variable `x`; keep `f` as variable `y`, and leave all other physical edges at unit activity. Multiaffinity gives

`Z(x,y)=A+xB+yC+xyD`.

Putting `x=m` reproduces the labelled multigraph after summing over the `m` choices of a used member of `C`. For the **specific** copy `e`, the four relevant labelled counts are

`Z = A+mB+C+mD`,
`Z_e = B+D`,
`Z_f = C+mD`,
`Z_ef = D`

when `y=1` (equivalently retain `y` symbolically and differentiate). Hence its raw Rayleigh gap with `f` is

`Delta_{e,f}=Z_e Z_f-Z Z_ef = BC-AD`,

independent of the multiplicity `m` of `C`.

Delete a different parallel copy `e'` from `C`. The new multiplicity is `m-1`, but the same calculation gives the same `BC-AD<0`. Thus `M-e'` is a smaller counterexample with the same marked pair, contradicting edge-minimality. The argument for `f` is identical. QED.

This is stronger than merely observing that a parallel marked pair is good: it excludes *any* extra clone of either marked edge in the minimal multigraph obstruction.

## 5. Exact 3-terminal separator response: weighted triangle plus one unavoidable residual

The prior B01 run completely retained the two-terminal response `lambda=C_B/D_B`. The next separator level has three boundary vertices, say `1,2,3`. Let a side `B` meet the rest only at these vertices, and count `B`-forests by the induced boundary partition:

- `d`: all three boundary vertices pairwise disconnected;
- `a`: partition `12|3`;
- `b`: partition `13|2`;
- `c`: partition `23|1`;
- `t`: all three boundary vertices connected.

Here `d>0` because at least the empty forest belongs to the first class (and there may be additional internal-edge forests there).

For a forest on the opposite side `A`, acyclicity of the union depends only on its own boundary partition and the partition above. Direct rank/unique-path checking gives the five compatibility weights contributed by `B`:

`w_0   = d+a+b+c+t`,
`w_12  = d+b+c`,
`w_13  = d+a+c`,
`w_23  = d+a+b`,
`w_123 = d`.                                             (5.1)

Now add three *virtual labelled* boundary edges to `A`, with activities

`x_12=a/d`, `x_13=b/d`, `x_23=c/d`.

For an `A`-forest whose boundary partition is respectively `0,12,13,23,123`, summing over all compatible acyclic subsets of that weighted triangle contributes

`1+x12+x13+x23+x12*x13+x12*x23+x13*x23`,
`1+x13+x23`,
`1+x12+x23`,
`1+x12+x13`,
`1`.

Multiplying by `d` matches the last four weights in (5.1) **exactly**. For the all-disconnected class it misses only one scalar. Define

`tau_B = d*t - (a*b+a*c+b*c)`.

If `Z_tri(A)` denotes the forest partition function after adding the weighted virtual triangle, and `Z_sep(A)` denotes the partition function restricted to `A`-forests that keep `1,2,3` pairwise disconnected, then the exact gluing identity is

**`Z_{A union B} = d Z_tri(A) + (tau_B/d) Z_sep(A)`.**       (5.2)

No boundary information has been discarded: `(d,a,b,c,t)` is represented by the three induced edge activities plus the single residual `tau_B/d`.

The same identity holds coefficientwise in any marked edge activities lying in `A`, because the compatibility calculation is performed forest-by-forest before summation.

## 6. Genuine counterexample to triangle-only separator compression

A tempting next step would be to replace every 3-terminal side by only the weighted boundary triangle from Section 5, i.e. to assume `tau_B=0`. This is false even for a tree.

Let `B` be the three-spoke star with center `o` and boundary leaves `1,2,3`. Every subset of its three edges is a forest. Exactly:

- `d=4` (empty set plus the three one-spoke subsets),
- `a=b=c=1` (the three two-spoke subsets),
- `t=1` (all three spokes).

Hence

`tau_B = 4*1-(1+1+1)=1`,

so the residual in (5.2) is `tau_B/d=1/4`.

Indeed the pair-state weights force `x12=x13=x23=1/4`. The weighted triangle then gives the all-disconnected compatibility weight

`4*(1+3/4+3/16)=31/4`,

whereas the true side contributes `w_0=8`. The missing `1/4` is exactly `tau_B/d`.

Therefore a 3-separator proof that records only three induced boundary edge weights is not source-valid. The full five-cell boundary law compresses to **three edge activities plus one residual scalar**, not to edge activities alone.

## 7. First remaining implication exposed exactly

For marked edges `e,f` lying in `A`, write

`P = d Z_tri(A)`, `R=Z_sep(A)`, `s=tau_B/d`.

Then `Z=P+sR`, coefficientwise in the marked activities. The Rayleigh gap expands exactly as

`Delta_{e,f}(Z)
 = Delta_{e,f}(P)
 + s [P_e R_f + R_e P_f - P R_ef - R P_ef]
 + s^2 [R_e R_f - R R_ef]`.                              (7.1)

The first term is the weighted-triangle baseline. The two later terms are the **entire** three-terminal separator debt. In particular, it is invalid to replace them by an unsupported claim that the terminal-disconnected sector `R` is itself Rayleigh: conditioning on a connectivity sector is precisely the kind of step the campaign has prohibited without proof.

Thus the next source-valid separator question is sharply localized:

> control the linear and quadratic residual terms in (7.1), using the fact that `(d,a,b,c,t)` comes from an actual forest side `B` and the all-third-edge sign constraints (3.1), or construct an actual graph for which such control fails.

The star witness shows this is a real obligation, not a normalization artifact.

## 8. Status and nonclaims

**ESSENTIAL_STEP_APPLIED:** yes. The named partner's theta-3 equivalence is applied to replace the weighted contraction endpoint by exact unit-minor deletion/contraction, and the new singleton-marked-class lemma removes a parallel-edge ambiguity in the minimal multigraph obstruction.

**CANDIDATE_REFUTED (submechanism):** yes. General 3-terminal separator compression to only a weighted boundary triangle is false; the 3-spoke star has residual `1/4`.

**FULL_PROOF_CANDIDATE:** no for this route. Equation (7.1) is a precise remaining debt, not a proof of its sign. The separate lead complete-graph/Cocks candidate and its existing reviews are left unchanged.

No external novelty or priority claim is made. No scheduler mutation, brain installation, benchmark work, public posting, or human activation occurred in this mathematical work.

## 9. Source/provenance note

All mathematical source dependencies used for the argument above were repository handoffs named in Section 1. The only fresh counterexample is the explicit 3-spoke star, whose eight subsets are enumerated in Section 6, so no hidden computation is required for it. Exploratory scratch computation was not used as proof evidence and is not part of this report.
