# FOREST / fleet01 B20 — STAR-2 debt removed and a parallel-class mediation obstruction

**Run:** `20260922T084701Z-B20-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** **OPEN**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source-exact scope and current team state

The target is the unit uniform law on **all** acyclic edge subsets of every finite simple graph, including the empty forest, disconnected forests and every forest size. For distinct physical edges `e,f`,

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`

is equivalent to

`P(e,f in F) <= P(e in F)P(f in F)`.

Fresh owner controls were read coherently from `yspennstate/math-research-brain` main at `cb211d35ef70b804af6a329a2c689172098f6fe4`, owner-control revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. New brain installation and benchmark work remain stopped.

The newest complete campaign-lead report consumed is fleet01/B01 run `20260922T080733Z-b01-forest-auto11`, commit `ff5c762464c33fb496946541d46a81ef0e2a71d5`, candidate `FOREST-CERTIFIED-CONTRACTION-STAR2-v2`. Its first unpaid step is the triangle-edge contraction case: after contracting a triangle edge in a simple graph, parallel pairs push forward to a simple graph with activities `2` on one star and `1` elsewhere. The lead calls a third edge certified when the conditional covariance after contraction is already known nonpositive.

The assigned named OTHER-account result actually consumed and applied is fleet04/B03 run

`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B03/20260922T040956Z-B03-forest-r12/report.md`,

Git blob `8812d4c9be5debaec40c02c2b13779bba8b62fae`.

Its exact simple path-bundle theorem says that replacing an unmarked base edge by `k` internally vertex-disjoint paths of length `a>=2` realizes effective activity

`q=k/(2^a-1)`

up to a common positive factor in all four marked partition functions, and therefore multiplies the marked Rayleigh difference by a positive square. In particular every positive integer activity `r` is realized exactly by `a=2`, `k=3r` in a finite simple unit graph.

A compatible earlier B20 theorem, `FOREST-MULTIGRAPH-MINIMAL-SIMPSON-v1` (commit `1bb11ef5510d2b548aebd5fd37fa4ba141749c06`), used exactly that partner lemma to prove that the simple unit target is equivalent to the unit target for finite labelled loopless multigraphs. I re-derived the load-bearing argument below against the new lead; no cached permission or disputed fixed-graph weighted theorem is used.

For the quantitative extension in Sections 5--6 I also use the compatible fleet03/B03 result `FOREST-CLC-TWOROW-AMPLIFICATION-v1`, commit `33b2e68bc71b6750249f865f6970424a6ae888d6`. Its only imported analytic input is the source-checked completely-log-concave homogeneous covariance operator for a matroid independent-set polynomial; the two-row inequality needed below is re-derived explicitly.

## 2. Re-derived source-equivalent category change

A labelled loopless multigraph forest contains at most one member of each parallel class. Collapse every parallel class of a loopless multigraph `M` to one edge of a simple graph `H`, and let `r_h` be the positive integer multiplicity of class `h`.

The labelled unit forest partition function of `M` is exactly the weighted forest polynomial of `H` at activities `r_h`: every macro forest using `h` has exactly `r_h` choices of its labelled copy.

If the two marked copies lie in one class, they are mutually exclusive and their covariance is nonpositive. Otherwise they lie in distinct classes `E,F`. For a fixed marked copy in class `E`, fixing that copy removes the class multiplicity, so the four labelled counts are the corresponding derivatives of the weighted simple polynomial. The Rayleigh difference

`Delta_EF=Z_E Z_F-Z Z_EF`

of a multiaffine polynomial is independent of the two marked variables `y_E,y_F` themselves. Hence the marked class weights may be reset to one, while every unmarked integer class weight `r_h` is realized by the fleet04/B03 simple path-bundle with `a=2,k=3r_h`. The resulting graph is finite, simple and unit-weight, and its marked gap is a strictly positive square factor times `Delta_M(e,f)`.

Therefore:

> **Simple-unit FOREST is true for all finite simple graphs iff unit FOREST is true for all finite labelled loopless multigraphs.**

So, if the source conjecture is false, choose a counterexample `M` with the minimum number `m` of labelled edges among **all loopless multigraph counterexamples**. This is a source-equivalent minimal category, not an unrelated weighted strengthening.

## 3. The new lead integration: every third edge is certified

Fix a violating labelled pair `e,f` in the edge-minimal loopless multigraph `M`, and write

`C_ij=Cov(X_i,X_j)`, `sigma_i^2=Var(X_i)`, `rho_ij=C_ij/(sigma_i sigma_j)`, `a=rho_ef>0`.

For any third labelled edge `g`:

* `X_g=0` gives the unit forest law of `M\g`, which has fewer labelled edges, hence `Cov(e,f|g=0)<=0` by minimality.
* `X_g=1`, followed by deleting the compulsory `g`, gives the unit forest law of `M/g`; any loops created from copies parallel to `g` are impossible in a forest and are deleted. The resulting loopless multigraph has fewer labelled edges, so `Cov(e,f|g=1)<=0`. If a marked edge becomes a loop, its conditional covariance is simply zero.

The binary law of total covariance therefore gives, for **every** third labelled edge,

`C_ef <= C_eg C_fg / Var(X_g)`.

Equivalently,

`boxed: rho_eg rho_fg >= a > 0.`                                      (3.1)

As usual, applying (3.1) to any positive pair shows positive correlation is transitive; a positive triangle is impossible because cyclic application would give `xyz <= (xyz)^2` with `0<xyz<1`. Thus positive pairs form a matching. Since `e,f` themselves form one positive pair, every third edge satisfies

`boxed: rho_eg<0 and rho_fg<0.`                                      (3.2)

This directly pays the newest lead's STAR-2 conditioning debt: in the source-equivalent loopless-multigraph minimal category, **all** third-edge contraction strata are certified. The special `{1,2}` star representation remains correct bookkeeping, but it is no longer an unpaid theorem. In the lead's quantitative budget one may replace `s_cert` by all `m-2` third labelled edges.

This is also consistent with the fresh fleet03/B01 scope correction: unrestricted STAR-2 is parent-equivalent and therefore should not be attacked as a stand-alone theorem. The useful move is precisely the source-equivalent category change above.

## 4. New theorem: an exact parallel-class mediation cap

The all-edge Simpson geometry has an additional consequence that was not used in the earlier multigraph reduction.

Let `C={g_1,...,g_r}` be any parallel class disjoint from the marked pair, of size `r>=1`. Let

`Y=1{some copy in C is selected}`, `p=P(Y=1)`.

A forest contains at most one copy from `C`, and conditional on `Y=1` the selected label is uniform among the `r` symmetric copies. Hence, for every `j`,

`P(X_gj=1)=p/r`,

`Cov(X_e,X_gj)=Cov(X_e,Y)/r`,

`Cov(X_f,X_gj)=Cov(X_f,Y)/r`,

and

`Var(X_gj)=p(r-p)/r^2`.

Apply the all-edge Simpson inequality (3.1) to the physical copy `g_j`:

`C_ef <= Cov(e,g_j)Cov(f,g_j)/Var(g_j)`

`      = Cov(e,Y)Cov(f,Y)/(p(r-p)).`                                (4.1)

By Cauchy--Schwarz,

`|Cov(e,Y)| <= sigma_e sqrt(p(1-p))`,

`|Cov(f,Y)| <= sigma_f sqrt(p(1-p))`.

The product in (4.1) is positive, so

`a=C_ef/(sigma_e sigma_f) <= (1-p)/(r-p).`                          (4.2)

Thus every third parallel class in a hypothetical minimal counterexample obeys the exact cap

`boxed: a <= (1-p)/(r-p) <= 1/r.`                                   (4.3)

For `r>1` and `p>0` the second inequality is strict. Equivalently,

`boxed: p <= (1-a r)/(1-a),  and therefore  a r <= 1.`              (4.4)

This is a genuine structural restriction on parallel multiplicity. A large class can mediate the same positive marked covariance through each of its labelled copies only if the violation `a` is correspondingly tiny.

No finite computation is used in this theorem.

## 5. Two-row CLC inequality in the loopless unit category

For completeness, here is the exact quantitative inequality needed to aggregate (4.4).

Let `K=|F|`, `mu=E K`, `delta=m-mu`, `q_i=1-p_i`, and

`t_i=Cov(X_i,K)/sqrt(delta p_i q_i)`.

For the degree-`m` homogenized exponent vector `U=(m-K,X_1,...,X_m)`, complete log concavity gives `D-Sigma >=0`, where `D=diag(EU)` and `Sigma=Cov(U)`. Therefore

`N=D^(-1/2) Sigma D^(-1/2)` satisfies `0<=N<=I`, so `M=N-N^2>=0`.

Take the `{e,f}` principal block of `M`, scale by `diag(q_e^(-1/2),q_f^(-1/2))`, and test on `(1,1)`. Direct multiplication gives

`0 <= s-(t_e+t_f)^2-(2-s)a^2+2a(s-1)`
`     - sum_{g notin {e,f}} q_g (rho_eg+rho_fg)^2`,                 (5.1)

where `s=p_e+p_f`.

By (3.1)--(3.2), for every third label

`(rho_eg+rho_fg)^2 >= 4 rho_eg rho_fg >= 4a`.

Also

`sum_g q_g=(m-2)-(mu-s)=delta-2+s`.

Hence

`boxed: (2-s)a^2 + 2a(2delta-3+s) + (t_e+t_f)^2 <= s.`             (5.2)

Dropping only the square recovers the source-secure two-row obstruction

`boxed: (2-s)a^2 + 2a(2delta-3+s) <= s.`                           (5.3)

The point of retaining the loopless labelled category is that (3.1) is now available for every third physical label, including copies in parallel classes.

## 6. New theorem: a global cap on total parallel excess

Partition the `N=m-2` third labelled edges into `k` parallel classes of sizes `r_1,...,r_k`. Put

`E=N-k=sum_j (r_j-1)`

for the total **parallel excess**, and let `p_j` be the occupancy probability of class `j`.

Because a forest uses at most one copy from a class,

`mu-s=sum_j p_j`.

Applying (4.4) to every class and summing gives

`mu-s <= (k-aN)/(1-a)`.

Therefore

`delta=m-mu >= m-s-(k-aN)/(1-a).`                                  (6.1)

Insert (6.1) into (5.3). Since its left side is increasing in `delta`, straightforward algebra yields the exact necessary inequality

`boxed: 4 a E <= (1-a^2) ((1+a)s-2a).`                             (6.2)

Since every labelled edge in a unit down-set has `p_i<=1/2`, one has `s<=1`, and consequently

`boxed: E <= ((1-a)^2(1+a))/(4a).`                                 (6.3)

Equivalently the number `k` of distinct third parallel classes must satisfy

`boxed: k >= (m-2) - ((1-a)^2(1+a))/(4a).`                         (6.4)

This is a new graph-structural localization of any minimal counterexample: parallel multiplicity cannot absorb the all-edge Simpson constraints freely. If there is even one duplicate third label (`E>=1`), then necessarily

`4a <= (1-a)^2(1+a)`,

whose unique root in `(0,1)` is approximately `0.193936566`; larger violations force the minimal counterexample to be simple. More generally (6.2), not this numerical corollary, is the useful exact form.

The derivation is symbolic and exact; no numerical experiment is used for the theorem.

## 7. Compact end-to-end state and the new first unpaid implication

After integrating the newest lead with the assigned partner, the source-safe chain is now:

1. fleet04/B03's simple path-bundle theorem makes the simple-unit target equivalent to the labelled loopless-multigraph unit target;
2. choose a minimum-labelled-edge loopless multigraph counterexample;
3. every deletion and contraction stratum is a smaller source-equivalent instance, so (3.1) holds for **every** third labelled edge;
4. positive pairs form a matching and the violating pair is strictly negatively correlated with every third label;
5. the lead's STAR-2 debt is therefore fully paid in this category: `s_cert=m-2`;
6. the two-row CLC operator gives (5.2)--(5.3);
7. the new class-symmetry argument gives the per-class cap (4.2)--(4.4) and the aggregate parallel-excess cap (6.2)--(6.4);
8. the earlier exact path--cut flux identities and quotient-path completion remain valid verbatim with labelled multiplicity.

The parent conjecture is **not** solved. The first genuinely unpaid universal implication is no longer STAR-2. It is:

> combine the exact edge-labelled path--cut / multi-step quotient-path transport with the simultaneous all-edge sign/product system, now additionally constrained by (6.2), to show that any residual Hall/flow overload forces a forbidden positive correlation between a third labelled edge and `e` or `f` (or directly forces the target Rayleigh gap nonnegative).

A useful way to organize the next attack is by the support/parallel decomposition. If a hypothetical overload is paid mostly by repeated labels in a few quotient cuts, (6.2) limits the available parallel excess in terms of the violation `a`; if it is paid by many distinct support classes, the transport must exploit genuinely different graph edges and can be attacked on the simplified quotient. A successful next theorem should make that dichotomy quantitative without paying a factor proportional to quotient-path length.

## 8. Failure / scope record

* No unrestricted weighted graphic-Rayleigh theorem is assumed.
* No disputed fixed-graph Cocks shortcut is used.
* No claim that antitone STAR-2 likelihood ratios imply negative association is made.
* No union/intersection-preserving Hall map is assumed; existing K4 obstructions remain binding.
* No full-proof, novelty, priority or publication claim is made.
* No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive data, paid model/API/Codex call, remote workflow, public posting, permission change or cross-account native action appears here.

**Final classification: `ESSENTIAL_STEP_APPLIED`.** The latest lead's first unpaid STAR-2 step is discharged by the source-equivalent multigraph minimality mechanism, and the new parallel-class mediation / excess inequalities (4.2) and (6.2) further constrain the remaining transport obstruction. The FOREST conjecture remains OPEN.
