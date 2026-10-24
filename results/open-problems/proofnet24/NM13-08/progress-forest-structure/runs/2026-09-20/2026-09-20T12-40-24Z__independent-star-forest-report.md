Model actually run: **GPT-5.6 Sol**. Reasoning-effort setting: **UNVERIFIED**.

# NM13-08 / T07 — star-tail nilpotent decomposition and arbitrary star-forest theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and substantive move

The preceding NM13-08 run proved a 52-state cycle-tail annihilator and an arbitrary-multiplicity theorem for three independent terminals joined to disjoint unions of `P1,...,P11,C3,...,C8`. The next recorded route was to derive marked cycle-tail recurrences. Rather than spend this run on another `C8 -> C9` finite cutoff, I switched to a materially different right-component geometry: **unbounded-degree stars**.

The new mechanism is stronger in a direction the path/cycle library did not address. A right star `S_m=K_{1,m}` has an arbitrary number of leaves. Keeping the three terminals and the star center gives only `B_4=15` frontier partitions; repeated leaf insertion has an exact nilpotent form `(L-5I)^4=0`. That makes every unmarked and one-/two-marked star transfer a bounded-degree polynomial in the star size `m` after removal of a positive `5^m` factor. This permits a symbolic all-`m,n` sign proof rather than a finite size census.

`POSTED.md` and the current LIVE20 mapping were read and respected. No historical or peer artifact is overwritten. No email, Drive, public posting, paid compute, workflow, access/permission change, or schedule change is performed.

## 1. Parent theorem before/after, separate from mechanism gain

For a finite graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e
\]

and for distinct edges `e,f`

\[
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of the two edge indicators under the uniform measure on **all** forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No complete-order metric moves in this run.

**Demonstrated mechanism before:** finite path/cycle atom response-strip closure (`P1..P11,C3..C8`) plus a 52-state all-cycle-length unmarked recurrence.

**Demonstrated mechanism after:** a 15-state nilpotent **star-leaf tail algebra** giving closed transfer formulas for every `S_m`, and an infinite-atom local-to-global sign theorem admitting **arbitrary finite star forests with arbitrary component sizes**. This removes any component-size cutoff in a new unbounded-degree right-component direction.

## 2. Recovered P14 and exact literature scope

Only essential dependencies were reread.

1. **Grimmett–Winkler, arXiv:math/0302185 / RSA 24 (2004).** Their conjecture is the unit-weight uniform measure on **all forests**, not the spanning-tree measure and not a fixed-component ensemble. They verified every graph with at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly note that edge negative association for a uniform spanning tree was already known separately.
2. **P14/HARD10 repository complement.** The exact dense-nine computation covers the complementary 19–36-edge sector. Repository continuity therefore covers all `274,668` unlabeled simple nine-vertex graphs; the dense sector contains `120,314` graphs and `25,304,635` present-edge-pair checks. P14's block factorization and two-separator transfer, together with the recovered Cocks fixed-graph unit-to-positive-weight implication, reduce a vertex-minimal source counterexample to a **3-connected** graph. This is a reduction, not closure of the conjecture.
3. **Erickson, arXiv:1008.3660.** Erickson proves the stronger all-positive-weight independent-set-Rayleigh property for **series-parallel** graphs by a sum-of-squares representation. The class below contains `K_{3,3}` as soon as the right side has at least three vertices, so it is not covered by that theorem.
4. **Later work.** Huang's arboreal-gas papers still describe the general negative-correlation problem as open while proving restricted cases. Bado proves strict unit pairwise negative correlation for every wheel, another restricted 3-connected non-series-parallel family. Tang–Zhang, arXiv:2603.10738 (11 March 2026), treat specified ensembles on the complete graph, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; that is not the arbitrary-graph uniform law mixing all component counts.

A bounded public search on 20 September 2026 did not locate the exact independent-terminal arbitrary-star-forest class below. That is negative evidence only; novelty/priority remains **UNVERIFIED**.

## 3. Retained five-state terminal algebra

Fix three independent terminals `0,1,2`. Their connectivity has five partitions

\[
0|1|2,\quad 0|12,\quad 01|2,\quad 02|1,\quad 012.
\]

For one isolated right vertex adjacent to all three terminals,

\[
S=4I+N,\qquad N^3=0.
\]

Every terminal-symmetric unmarked right atom used here has transfer

\[
T=A I+B N+C N^2.
\]

After factoring `A>0`, write

\[
\widehat T=I+aN+cN^2,
\qquad
\rho(T)=\frac{a^2/2-c}{a}.
\]

For any product of normalized atoms,

\[
\prod_j(I+a_jN+c_jN^2)=I+uN+vN^2,
\]

with

\[
\frac{u^2}{2}-v=\sum_j\rho_j a_j.
\]

Thus, for `u>0`,

\[
v=\frac{u^2}{2}-hu,
\qquad
h=\frac{\sum_j\rho_j a_j}{\sum_j a_j},
\]

so `h` is a positive weighted average of the component responses.

## 4. New decomposition lemma: 15-state star-leaf nilpotence

Let `S_m=K_{1,m}` have center `c` and leaves `x_1,...,x_m`; every star vertex is adjacent to all three terminals. During leaf insertion retain the frontier `(0,1,2,c)`. Its connectivity has `B_4=15` partitions.

One unmarked leaf step introduces a fresh leaf `x`, considers the four edges

\[
cx,\ x0,\ x1,\ x2,
\]

rejects cyclic choices, and then forgets `x`. Let `L` be the resulting exact `15 x 15` transfer.

### Lemma `T07-STAR-TAIL-NILPOTENT-23`

Set `J=L-5I`. Then

\[
\boxed{J^4=0},
\]

with exact ranks

\[
\operatorname{rank}J=8,\qquad
\operatorname{rank}J^2=2,\qquad
\operatorname{rank}J^3=1,\qquad
\operatorname{rank}J^4=0.
\]

Hence for every integer `r>=0`,

\[
\boxed{
5^{-r}L^r
=I+\frac r5J+\frac{\binom r2}{25}J^2+\frac{\binom r3}{125}J^3.
}
\tag{4.1}
\]

The checker constructs all 15 partitions and all leaf transitions by exact acyclicity enumeration and verifies the displayed ranks and nilpotence. Equation (4.1) is then the finite binomial expansion because `J^4=0`.

The same formula handles marked stars. A marked edge pair distinguishes at most two leaves. By permuting leaves, put those leaves first; their one- or two-edge-required transition matrices replace the first one or two `L` factors, and all remaining leaves contribute (4.1). Therefore, after dividing by the positive scalar `5^m`, every unmarked, one-marked, or two-marked star transfer is a matrix whose entries are polynomials of degree at most three in `m`. This is the finite-dimensional closure needed for an all-size sign proof.

## 5. Closed unmarked star transfer and a universal response strip

Let `T_m` be the unmarked three-terminal transfer of `S_m`. Exact symbolic multiplication using (4.1) gives

\[
\boxed{
5^{-m}T_m
= A_m I+B_mN+C_mN^2
}
\]

with

\[
A_m=\frac{3m+20}{5},
\qquad
B_m=\frac{4m^2+31m+25}{25},
\qquad
C_m=\frac{m(16m^2+127m+107)}{750}.
\tag{5.1}
\]

Consequently

\[
\rho_m
=
\frac{43m^3+622m^2+2510m+1875}
{30(3m+20)(4m^2+31m+25)}.
\tag{5.2}
\]

Two exact factorizations give the whole range at once:

\[
\rho_m-\frac{43}{360}
=
\frac{5m^2+47m+200}
{72(3m+20)(4m^2+31m+25)}>0,
\tag{5.3}
\]

and

\[
\frac18-\rho_m
=
\frac{m(8m^2+107m+385)}
{120(3m+20)(4m^2+31m+25)}\ge0.
\tag{5.4}
\]

Thus every finite star size `m>=0` lies in the **same size-independent strip**

\[
\boxed{\frac{43}{360}<\rho_m\le\frac18},
\]

with the upper equality only at `m=0`. Therefore an arbitrary product of unmarked star components, of arbitrary and unequal sizes, has

\[
\boxed{
u\ge0,
\qquad
v=\frac{u^2}{2}-hu,
\qquad
\frac{43}{360}\le h\le\frac18.
}
\tag{5.5}
\]

This is the key gain over the previous finite atom libraries: the admissible atom family itself is infinite.

## 6. Infinite-atom symbolic strip-admission lemma

### Lemma `T07-SYMBOLIC-STAR-STRIP-ADMISSION-23`

Consider an atom family `A_m`, `m>=0`, with a common normalized response strip `[alpha,beta]`. Suppose the automorphism group of an atom and of a pair of atoms reduces all one-/two-edge marked configurations to finitely many **symbolic schemes** whose response polynomials

\[
Q_\tau(u,v;m)
\quad\text{or}\quad
Q_\tau(u,v;m,n)
\]

are nonnegative on `u>=0`, `v=u^2/2-hu`, `h in [alpha,beta]`, over their physical integer parameter ranges. Then three independent terminals joined to an arbitrary finite disjoint union of atoms `A_{m_i}` are p-NC under the uniform-all-forests law.

### Proof

Fix present edges `e,f`. They meet at most two right components. Expose those components, including whichever required-edge transfer applies. Every remaining component is unmarked; after factoring its positive identity coefficient, the product of all remaining components is `U(u,v)=I+uN+vN^2` with `(u,v)` in the common response strip. Each of `I,I_e,I_f,I_ef` is affine in `(u,v)`, hence their Rayleigh numerator is exactly the corresponding symbolic quadratic `Q_tau`. The finite symbolic scheme hypothesis supplies its sign for the actual component sizes. Restoring all factored positive scalars multiplies `Delta` by a positive square. QED.

Unlike the preceding finite-atom lemma, this admits infinitely many atom sizes because the marked schemes are symbolic in `m,n`.

## 7. Exact symbolic sign certificate for every star size

For a star component, edge types are:

- `c`: a center-to-terminal spoke;
- `s`: a leaf-to-terminal spoke;
- `i`: a center-to-leaf internal edge.

Leaf permutations and terminal `S_3` reduce same-component pairs to exactly **10 symbolic schemes**:

`cc_diff`, `cs_same`, `cs_diff`, `ci`, `ss_sameleaf_diff`, `ss_diffleaf_same`, `ss_diffleaf_diff`, `si_sameleaf`, `si_diffleaf`, `ii_diffleaf`.

Across two star components there are exactly **13 oriented symbolic schemes**:

`cc_same`, `cc_diff`, `cs_same`, `cs_diff`, `sc_same`, `sc_diff`, `ci`, `ic`, `ss_same`, `ss_diff`, `si`, `is`, `ii`.

The checker constructs every marked transfer from the exact 15-state matrices and, independently, compares all required symbolic marked patterns against direct star DP for physical sizes through `m=5`.

For each scheme, substitute

\[
v=\frac{u^2}{2}-hu,
\qquad
\frac{43}{360}\le h\le\frac18,
\]

and write

\[
R_\tau(u,h)=\sum_{k=0}^4 c_{\tau,k}(h)u^k.
\]

Each `c_{tau,k}` is quadratic in `h`. The checker expands it in the degree-two Bernstein basis on `[43/360,1/8]`. For **22 of the 23 schemes**, after shifting the size variables to their physical minima (`m=m_0+x`, `n=n_0+y`), every nonzero Bernstein coefficient is a polynomial in `x,y` with nonnegative monomial coefficients. Hence those 22 schemes are nonnegative for every allowed integer size and every point of the response strip.

Exactly one scheme leaves that cone: two leaf spokes on **distinct leaves to different terminals** in the same star (`m>=2`). Its normalized response quadratic has coefficients

\[
\begin{aligned}
q_{00}&=\frac{2(464m^4+9573m^3+70162m^2+206968m+202658)}{390625},\\
q_{10}&=\frac{2(648m^3+10357m^2+51908m+66572)}{78125},\\
q_{01}&=-\frac{12(255m^2+3454m+11572)}{15625},\\
q_{20}&=\frac{4(493m^2+6611m+23131)}{15625},\\
q_{11}&=\frac{12(7m-44)}{3125},
\qquad
q_{02}=\frac{144}{625}.
\end{aligned}
\tag{7.1}
\]

Using the retained strip-discriminant identity,

\[
4c_4c_2-c_3^2
=q_{02}\left(q_{20}+\frac{q_{01}}2\right)-\frac{q_{11}^2}{4},
\]

we get the exact positive polynomial

\[
\boxed{
K(m)=\frac{108(573m^2+7832m+30144)}{9765625}>0.
}
\tag{7.2}
\]

Here `c_4=q_02/4>0`, while `c_0>0` and `c_1>=0` on the whole strip. Therefore the quadratic core `c_4u^2+c_3u+c_2` has negative discriminant and is positive for every real `u`; hence

\[
R(u,h)=u^2(c_4u^2+c_3u+c_2)+c_1u+c_0>0.
\]

This closes the only non-Bernstein scheme.

The archived execution reports

`certificate_counts {'REGULAR': 22, 'DISCRIMINANT': 1}`

and ends `ALL_EXACT_CHECKS_PASS`.

## 8. New arbitrary-star-forest theorem

Let

\[
H=\bigsqcup_{j=1}^q K_{1,m_j},
\qquad q\ge0,\quad m_j\ge0,
\]

where `K_{1,0}` means a single isolated right vertex. Introduce three new **independent** terminals and join every terminal to every vertex of `H`:

\[
G=\overline{K_3}\vee H.
\]

### Theorem `T07-INDEPENDENT-STAR-FOREST-PNC-23`

For every finite star forest `H` and every pair of distinct present edges `e,f` of `G`,

\[
\boxed{\Delta_G(e,f)\ge0}.
\]

Thus the uniform measure on **all** forests of `G` has pairwise negative edge correlation.

If there is at least one present edge pair, equality occurs only for the degenerate single-component case `H=K_{1,0}`, namely `G=K_{3,1}`. In that case `G` is a tree, so every edge subset is acyclic and the edge indicators are independent. In all other physical cases the symbolic certificates above are strict.

### Proof

Equations (5.3)–(5.5) put every unmarked star size in the common strip `[43/360,1/8]`. Section 7 verifies all 23 symbolic marked schemes on that strip for every physical integer size. Apply `T07-SYMBOLIC-STAR-STRIP-ADMISSION-23`. For strictness, the checker finds the only zero constant response at the physical boundary in `cc_diff` at `m=0`; any nonempty background gives a positive higher response term, and every other same-/cross-component scheme has positive constant response at its minimum physical size. QED.

This is an all-parameter theorem in two senses: the number of components `q` is arbitrary and every component size `m_j` is arbitrary. It is not a finite graph enumeration and has no star-size cutoff.

For

\[
H=\bigsqcup_j K_{1,m_j},
\]

we have

\[
|V(G)|=3+\sum_j(m_j+1),
\qquad
|E(G)|=\sum_j(4m_j+3).
\]

A clean one-parameter subfamily is

\[
G_m=\overline{K_3}\vee K_{1,m},\qquad m\ge0,
\]

with

\[
|V(G_m)|=m+4,
\qquad
|E(G_m)|=4m+3.
\]

The first member beyond the repository's complete nine-vertex baseline is `m=6`:

\[
|V|=10,\qquad |E|=27,
\]

with exact forest count

\[
I_G(\mathbf 1)=2{,}090{,}000
\]

and minimum Rayleigh numerator

\[
\boxed{4{,}923{,}437{,}500}.
\]

The checker also gives `m=3`: 7 vertices, 15 edges, 5,701 forests and minimum gap 80,404.

## 9. Why this is genuinely complementary to NM13-04 and earlier NM13-08 work

This class is not another presentation of the companion triangle-seeded family. The three terminals here are independent. If `H` has an edge, `bar(K3) join H` has clique number exactly 3; if `H` is independent it has clique number 2. By contrast, every nonempty triangle-seeded join `K3 join L` contains a `K4`. Deleting the three seed-triangle edges from a unit-weight p-NC theorem is not an available inheritance principle.

It is also genuinely outside the preceding NM13-08 path/cycle atom library. For `m>=3`, the right induced component `K_{1,m}` has maximum degree at least three, whereas every retained path/cycle atom has right maximum degree at most two. The present theorem removes the star-size cutoff entirely rather than adding another finite atom.

Once the right side has at least three vertices, `G` contains `K_{3,3}` between the independent terminal triple and any three right vertices, so it is nonplanar and not series-parallel. Hence Erickson's series-parallel theorem does not subsume the class. The result is a restricted infinite 3-connected/non-series-parallel direction, not the general conjecture.

## 10. Exact checker and residual obstruction

Executed checker:

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T12-40-24Z__independent-star-forest-checker.py`

Archived output:

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T12-40-24Z__independent-star-forest-checker.out`

The checker uses exact integer/rational/SymPy polynomial arithmetic for every sign decision. No floating-point sign test is used. It reconstructs the 15-state leaf operator, verifies the nilpotence/ranks, derives (5.1)–(5.4), validates all marked symbolic transfers against direct DP at several physical sizes, certifies all 23 symbolic pair schemes, and performs physical checks on `G_3` and `G_6`.

**Residual obstruction.** The parent conjecture still has arbitrary 3-connected structure with no distinguished independent terminal triple and no star-forest decomposition. Even inside the present three-terminal framework, admitting arbitrary right **trees** would require controlling a branching recursion with more than one live branch shape; the star proof succeeds because every branch is a single leaf and all unmarked leaf steps use one nilpotent operator. The next distinct attack is therefore to replace a leaf by a bounded-depth branch and test whether the star-tail nilpotent cone survives under one level of recursive branching. A first target is right components that are depth-two subdivided stars, seeking a two-operator nilpotent/triangular algebra rather than another finite component-size cutoff.

## 11. Progress accounting

- Parent theorem: **OPEN -> OPEN**.
- Complete all-graph order: **9 -> 9**.
- Counterexample-order lower bound: **>=10 -> >=10**.
- Mechanism gain: finite path/cycle atom library -> **infinite star-size atom family** with exact 15-state nilpotent tail and symbolic marked-response positivity.
- New application: all graphs `bar(K3) join H` for arbitrary finite star forests `H`, with no bound on the number of star components or their sizes.
- Restricted theorem status: **CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW**.
- Novelty/priority: **UNVERIFIED**.
