# FOREST / fleet01 B20 — fixed-graph Cocks closes STAR-2 in the simple category; density/cyclomatic squeeze

**Run:** `20260922T094714Z-B20-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** **OPEN**  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh control, lead, partner, and exact scope

The active owner programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, owner-control revision `2026-09-22.2`. The target is the original unit, unrooted, all-sizes forest law on every finite simple graph `G`: for every distinct physical edges `e,f`,

`P(e,f in F) <= P(e in F) P(f in F)`.

Equivalently, with `Z` the number of all forests and `Z_e,Z_f,Z_ef` the usual marked counts,

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

Newest campaign-lead version consumed: fleet01/B01

`20260922T080733Z-b01-forest-auto11/report.md`

blob `7eccff21a034648951b1a5886db0330b60c3a5da`, candidate `FOREST-CERTIFIED-CONTRACTION-STAR2-v2`. Its first unpaid universal step is the residual triangle-edge contraction case. Contracting a triangle edge `g` in a simple graph creates only size-two parallel classes on the contracted star. After simplification this becomes a simple graph `H_g` with activity `2` on those star edges and activity `1` elsewhere. The lead proved the exact physical-edge sign-transfer lemma but treated general STAR-2 as unpaid.

Named OTHER-account result actually consumed and applied: fleet04/B03

`20260922T070756Z-B03-forest-r12-34330b0f/report.md`

blob `a09681b45ae7e7e2d470fb5a2cdcd23c5c51fa38`. It independently removes the same conditioning debt by passing to an edge-minimal labelled loopless-multigraph counterexample, giving for every third physical label `g`

`C_eg C_fg >= C_ef Var(X_g)`

and hence, for `a=rho_ef>0`,

`rho_eg rho_fg >= a`, with `rho_eg,rho_fg<0`.

I also use two previously proved own-team inputs without altering them:

* B20 `20260922T084701Z-B20-forest-r11`, blob `06b8ee47c9219a00ac5e06f8c21890ac3422b9ef`, for the source-valid **ground-set-degree** CLC two-row inequality (not the refuted rank-degree variant);
* B20 `20260922T012259Z-B20-e3d71907`, blob `1a94f31efde4c0422d81cd81c1fb16b82bc57860`, for the exact path-cut flux identities and multi-step quotient-path completion in the 3-connected obstruction.

## 2. Source correction: the final Semple-Welsh paper already records Cocks's fixed-graph theorem

The lead correctly quotes an earlier sentence in the main body of Semple-Welsh saying that the authors were unable to pass from the unit graph conjecture to arbitrary series/parallel extensions. However, the **post-submission Note in the final published paper supersedes that state**.

Semple-Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), printed p. 13, states:

> Cocks has shown that if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

In their definitions, `M(G)` being independence correlated means exactly that the independent-set Rayleigh inequality holds for **every positive real edge weighting**, not only at unit weights. The same final Note also records the Cocks/Wagner 2-sum result.

Bibliographic source: C. C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17(4) (2008), 511-518, DOI `10.1017/S0963548308009152`. Its public abstract confirms the equivalence programme and the 2-sum theorem. I did not obtain the full Cocks proof body in this run; the fixed-graph theorem statement itself is nevertheless explicitly printed in the final Semple-Welsh paper. This report therefore treats it as an imported published theorem while preserving that proof-body audit boundary.

This matters because `H_g` below is a **simple graph**, so no convention about multigraphs is needed in applying the theorem.

## 3. New integrated theorem: every third edge is certified inside an edge-minimal simple counterexample

Assume the source conjecture is false and choose a counterexample `G` with the minimum number `m` of edges among finite simple graphs. Fix a violating pair `e,f` and put

`C_ij=Cov(X_i,X_j)`, `v_i=Var(X_i)`, `rho_ij=C_ij/sqrt(v_i v_j)`, `a=rho_ef>0`.

Fix any third physical edge `g`.

### Deletion stratum

Conditioning on `X_g=0` gives the uniform forest law of the smaller simple graph `G\g`. By edge minimality,

`Cov(X_e,X_f | X_g=0) <= 0`.

### Contraction stratum

Conditioning on `X_g=1` and deleting the compulsory edge is the uniform forest law of `G/g`, a loopless multigraph after discarding loops. Because `G` is simple, every new parallel class has size exactly two and lies on the one contracted star.

Let `H_g` be the **simple** graph obtained by collapsing each such parallel pair to one effective edge. The pushforward conditional law is the forest law on `H_g` with activity `2` on the collapsed star edges and activity `1` on every other edge. The graph `H_g` has strictly fewer than `m` edges.

By simple edge minimality, `H_g` satisfies Conjecture 1.1 at unit weights for every pair of its edges. By the fixed-graph Cocks theorem recorded above, `M(H_g)` is independence correlated, so the Rayleigh inequality holds at **all positive weights**, in particular at the exact `{1,2}` STAR-2 weighting.

Now apply the lead's exact physical-edge sign transfer:

* if `e,f` become the two copies of one parallel class, they are mutually exclusive and their conditional covariance is automatically nonpositive;
* otherwise, if `bar e,bar f` are their effective images, then

  `Cov(X_e,X_f | X_g=1)=alpha_e alpha_f Cov(Y_bar_e,Y_bar_f)`

  with `alpha_i` equal to `1/2` for a marked edge in a doubled class and `1` otherwise.

Hence in every case

`Cov(X_e,X_f | X_g=1) <= 0`.

Therefore **every third edge is certified in the original simple minimal counterexample**. The generic STAR-2 branch is not an unpaid theorem once the final published Cocks result is admitted.

### Simpson consequence

The binary law of total covariance gives

`C_ef
 <= Cov(E[X_e|X_g],E[X_f|X_g])
 = C_eg C_fg/v_g`,

so for every `g notin {e,f}`,

**(S-simple)** `C_eg C_fg >= C_ef v_g`,

or equivalently

**(S-rho)** `rho_eg rho_fg >= a > 0`.

The two correlations with `g` have the same nonzero sign. They cannot both be positive: otherwise `e,f,g` form a positive triangle, and cyclic application of (S-rho) gives, for `a,b,c in (0,1)`,

`a<=bc, b<=ac, c<=ab`,

whose product says `abc <= (abc)^2`, impossible. Hence

**(M-simple)** `rho_eg<0` and `rho_fg<0` for every third edge `g`.

This reproduces fleet04/B03's all-conditioner conclusion **without leaving the simple category**, so the earlier simple-graph separator/path-cut machinery remains directly available and no parallel-excess bookkeeping is needed for the next stage.

## 4. New quantitative theorem: cyclomatic-density squeeze on any simple minimal counterexample

Let

`K=|F|`, `mu=E K`, `delta=m-mu`, `s=p_e+p_f`,

and

`t_i=Cov(X_i,K)/sqrt(delta p_i(1-p_i))`.

The source-valid ground-set-degree CLC two-row inequality proved in B20 `20260922T084701Z` is

**(CLC2)**

`(2-s)a^2 + 2a(2delta-3+s) + (t_e+t_f)^2 <= s`.

Its derivation uses the degree-`m` homogenized independent-set polynomial, `0<=N<=I` for the normalized covariance operator, the `{e,f}` block of `N-N^2`, and precisely the all-edge sign/product system (S-rho)/(M-simple). No rank-degree homogenization is used.

Drop the nonnegative square. Define

`F(s)=(2-s)a^2+2a(2delta-3+s)-s`.

Then

`dF/ds = -(1-a)^2 <= 0`.

Every unit forest edge has `p_i<=1/2` by the deletion injection, so `s<=1`. Since `F(s)<=0` and `F` is decreasing,

`F(1)<=0`, i.e.

**(D1)** `a^2+4a(delta-1) <= 1`.

If the relevant counterexample is connected on `n` vertices, every forest has at most `n-1` edges, hence `mu<=n-1` and

`delta-1=m-mu-1 >= m-n`.

Therefore

**(D2)** `a^2+4(m-n)a <= 1`,

so

**(D3)**

`a <= sqrt(4(m-n)^2+1)-2(m-n)
     = 1/(sqrt(4(m-n)^2+1)+2(m-n)).`

This is a graph-density obstruction, not merely a ground-set-size bound.

### 3-connected specialization

The inherited exact separator reductions localize a minimal simple counterexample to the 3-connected obstruction used by the path-cut work. Then minimum degree is at least three, so `2m>=3n`, hence `m-n>=m/3`. Thus

**(D4)**

`a <= sqrt(4m^2/9+1)-2m/3 ~ 3/(4m)`.

### Block-cyclomatic specialization

The exact R02/P0001 theorem `runs/R02/20260918T0024Z_8c7d1e52.md`, blob `968967909df972f84700eae10ea676cccc648dc6`, proves p-NC whenever every nontrivial 2-connected block has cyclomatic number at most `6`. A 3-connected minimal counterexample is one nontrivial block, so it must satisfy

`m-n+1 >= 7`, hence `m-n>=6`.

Putting `m-n=6` in (D3) gives the universal numerical cap

**(D5)**

`a <= sqrt(145)-12 = 0.0415945787922954801...`.

Thus any source counterexample surviving the current reductions would have to exhibit a **strictly positive but at most about 4.16% Pearson correlation** for its violating pair. This is stronger than the earlier coarse constant caps and is obtained without a finite census beyond the already source-certified R02 threshold.

## 5. Exact algebra checker

`density_checker.py` symbolically verifies the only algebraic reductions used in Section 4. Its archived output is:

```text
dF_ds= -(a - 1)**2
F_at_s1= a**2 + 4*a*delta - 4*a - 1
density_sub= a**2 + 4*a*d - 1
general_root_residual= 0
d6_root= -12 + sqrt(145)
d6_root_residual= 0
d6_decimal= 0.0415945787922954801
mindegree_root_residual= 0
STATUS=PASS
```

The checker is regression only; (D1)-(D5) are proved symbolically above.

## 6. Compact conditional end-to-end state after this run

The source-safe chain is now:

1. choose an edge-minimal **simple** counterexample and a violating pair `e,f`;
2. deletion conditioning on any third edge is good by simple minimality;
3. contraction conditioning pushes to the lead's exact simple STAR-2 law on a strictly smaller simple graph `H_g`;
4. the final published Semple-Welsh Note records Cocks's theorem that unit Conjecture 1.1 on `H_g` upgrades `M(H_g)` to independence correlated at all positive weights;
5. therefore every contraction stratum is good and (S-simple)/(S-rho)/(M-simple) hold for **all** third edges in the original simple graph;
6. fleet04/B03 independently reaches the same all-conditioner sign/product system via loopless-multigraph minimality, so the two routes are compatible rather than competing;
7. retaining the simple category keeps the exact path-cut flux laws and multi-step quotient-path completion available without parallel-class bookkeeping;
8. the ground-set CLC two-row inequality plus graph rank/density gives (D2)-(D5).

The parent FOREST conjecture is still **OPEN**. Current 2026 literature is consistent with that status: Fang-Ma, arXiv:2604.27755, still formulate the graphic unrooted spanning-forest Rayleigh statement as Conjecture 14.15 rather than a theorem.

## 7. First remaining universal implication

The lead's current STAR-2 debt is paid. The first unpaid step is now genuinely graph-global:

> In a 3-connected simple minimal counterexample, combine the exact reconnection identity and B20 path-cut/multi-step quotient-flow conservation with the simultaneous all-edge constraints (S-rho)/(M-simple) to rule out **arbitrarily small** positive `a` satisfying (D2).

Equivalently, the transport side now needs to force either `Delta_G(e,f)>=0` directly or a **positive lower bound on `a` in terms of the same cyclomatic/density parameter** that contradicts

`a <= 1/(sqrt(4(m-n)^2+1)+2(m-n)).`

This is sharper than trying another local three-edge cone or another STAR-2 gadget: the contraction layer is already certified, and the remaining obstruction must use common-graph path/cut compatibility.

## 8. Failures and boundaries preserved

* No claim of full FOREST proof, novelty, priority, or publication readiness is made.
* The original Cocks proof body was not directly available in this run; only the fixed-graph theorem statement printed in the final Semple-Welsh paper and the published Cocks bibliographic/abstract record were inspected. A publication-grade final proof should audit the original Cocks argument or independently rederive that theorem.
* No disputed rank-degree CLC statement is used.
* No unrestricted weighted graphic-Rayleigh theorem is assumed independently of Cocks's fixed-graph implication.
* No finite search is promoted to a universal theorem.
* No new brain installation or benchmark work was performed.
* No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private transcripts, email, Drive, public posting, paid model/API/Codex call, remote workflow, permission bypass, B21/B22, or cross-account native action appears here.

**Final classification: `ESSENTIAL_STEP_APPLIED`.** The newest lead's residual STAR-2 conditioning step is closed in the simple minimal category by an exact published fixed-graph theorem plus the lead's own sign-transfer lemma, and the resulting all-edge certification yields the new density/cyclomatic correlation squeeze (D2)-(D5). The source conjecture remains OPEN.

## 9. Model / effort / context

Model self-report: `GPT-5.6 Sol`.  
Requested effort: maximum actually supported.  
Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning-token/time usage: `UNKNOWN_NOT_EXPOSED` (unknown is not zero).  
Brain context: `WITHOUT_VERIFIED_BRAIN`.
