Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-08 / T07 — one-edge terminal-response algebra and arbitrary mixed-spider forests

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and substantive move

The preceding NM13-08 run introduced the mixed spider `D_{p,q}`: one center, `p` direct one-edge legs, and `q` subdivided two-edge legs. It proved a commuting two-tail algebra and pairwise negative edge correlation for

\[
\overline{K_3}\vee(D_{p,q}\sqcup rK_1),\qquad p,q,r\ge0.
\]

Its explicit residual obstruction was **cross-component pairs when two marked edges lie in two distinct mixed-spider components**. A direct four-parameter orbit calculation had become too expensive. The recorded next attack was to replace that census by an abstract theorem for one-edge response vectors.

This run executes exactly that attack. The new point is that every unmarked or one-edge-required mixed-spider transfer lies in a five-dimensional commutative matrix algebra `C(x,z)`. Multiplication in this algebra makes the Rayleigh numerator for edges in two distinct components collapse to a scalar quadratic in the residual response variable `u`. Exact symbolic positivity of four quantities then closes all 38 physical cross-component schemes. Combining this with the preceding same-component theorem proves p-NC for **an arbitrary finite multiset of mixed spiders**, with both the number of components and both leg counts unbounded.

No historical or peer file is overwritten. No email, Drive, public posting, paid compute, workflow execution, permission/access change, or schedule change is performed.

## 1. Parent theorem before/after — separate from mechanism progress

For a finite graph `G=(V,E)` let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e.
\]

At unit weights write `I`, `I_e`, `I_f`, `I_{ef}` for the total forest count and the corresponding required-edge counts, and

\[
\Delta_G(e,f)=I_eI_f-I I_{ef}.
\]

Then `Delta_G(e,f)>=0` is exactly pairwise negative correlation of the indicators of distinct edges `e,f` under the uniform law on **all** forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No complete-order metric moves in this run.

**Mechanism before:** a two-tail mixed-spider algebra and a theorem for one mixed spider plus isolated right vertices; two marked edges in different mixed-spider components were not controlled.

**Mechanism after:** a commutative **one-edge terminal-response algebra** and a cross-component Rayleigh determinant identity reducing every distinct-component pair to four scalar positivity conditions, with an exact all-parameter certificate. This promotes one mixed spider to an arbitrary finite mixed-spider forest.

## 2. Exact source and P14 scope recovered

Only essential dependencies were reread.

1. **Grimmett–Winkler, arXiv:math/0302185 / Random Structures & Algorithms 24 (2004).** Their conjecture is the unit-weight uniform law on **all forests**. They verify every graph with at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly separate the already-known negative-association theorem for the uniform spanning tree.
2. **P14/HARD10 dense-nine complement.** Repository claim `HARD10-N9-DENSE-UNIT-PAIR-20260916-01` covers all `120,314` unlabeled nine-vertex graphs with 19--36 edges and all `25,304,635` present-edge pairs. Together with Grimmett–Winkler this covers all `274,668` unlabeled simple graphs on nine vertices.
3. **P14 structural reduction.** Block/direct-sum factorization reduces a vertex-minimal counterexample to 2-connected. The preserved two-separator transfer, together with the fixed-graph unit-to-positive-weight implication recorded from the Cocks/Semple--Welsh line, reduces it further to a **3-connected** graph. This is a reduction only, not a proof of the conjecture.
4. **Erickson, arXiv:1008.3660.** Erickson proves a stronger positive-weight Rayleigh/SOS theorem for spanning-forest polynomials of **series-parallel** graphs. The nontrivial family below contains `K_{3,3}`, hence is outside that scope.
5. **Later work.** Stark proves the complete-graph case for sufficiently large order by enumeration. Huang `arXiv:2311.00965` still treats general arboreal-gas negative correlation as open while proving special cases. Bado proves the uniform-all-forests statement for wheels. Tang--Zhang `arXiv:2603.10738` treats specified ensembles on `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph law mixing all forest component counts.

A bounded 20 September 2026 search did not locate the exact independent-terminal arbitrary mixed-spider-forest theorem below. This is negative evidence only; novelty/priority remains **UNVERIFIED**.

## 3. Mixed spiders and the retained response strip

Let `D_{p,q}` be the tree with center `c`, direct leaves `d_1,...,d_p` joined by `cd_i`, and subdivided legs

\[
c-b_j-x_j,\qquad 1\le j\le q.
\]

The previous run proved, by a 15-state exact frontier transfer, that the normalized unmarked transfer of `D_{p,q}` has form

\[
T_{p,q}=A_{p,q}I+B_{p,q}N+C_{p,q}N^2,\qquad N^3=0,
\]

and that its response parameter

\[
\rho_{p,q}=\frac{(B/A)^2/2-C/A}{B/A}
\]

satisfies

\[
\boxed{\frac{43}{360}<\rho_{p,q}\le\frac18},
\]

with equality at the upper endpoint only for `p=q=0`, i.e. a single isolated right vertex.

For any product of normalized unmarked components one therefore has

\[
U(u,v)=I+uN+vN^2,
\qquad
v=\frac{u^2}{2}-hu,
\qquad
\boxed{\frac{43}{360}\le h\le\frac18}.
\tag{3.1}
\]

This follows from the exact weighted-average response identity retained from the earlier runs.

## 4. New decomposition lemma: the one-edge terminal-response algebra

Use the five terminal-connectivity states

\[
0|1|2,\quad0|12,\quad01|2,\quad02|1,\quad012.
\]

For `x=(x_1,x_2,x_3)` put `t=x_1+x_2+x_3` and define

\[
C(x,z)=
\begin{pmatrix}
1&x_1&x_2&x_3&z\\
0&1&0&0&t-x_1\\
0&0&1&0&t-x_2\\
0&0&0&1&t-x_3\\
0&0&0&0&1
\end{pmatrix}.
\tag{4.1}
\]

Also define the symmetric bilinear form

\[
\kappa(x,y)=(x_1+x_2+x_3)(y_1+y_2+y_3)-x\cdot y
=\sum_{i\ne j}x_i y_j.
\tag{4.2}
\]

### Lemma `T07-ONE-EDGE-TERMINAL-ALGEBRA-26`

The matrices (4.1) obey

\[
\boxed{C(x,z)C(y,w)=C(x+y,z+w+\kappa(x,y)).}
\tag{4.3}
\]

In particular this algebra is commutative.

Moreover, after extraction of a positive diagonal scalar, every unmarked mixed-spider transfer and every transfer requiring one specified present edge of a mixed spider belongs to this algebra.

### Proof

Multiplying (4.1) directly gives the three new first-row coordinates `x_i+y_i`; the `(i,5)` entries become `(sum(x+y))-(x_i+y_i)`; and the `(1,5)` entry is `z+w+kappa(x,y)`. This proves (4.3) and commutativity because `kappa` is symmetric.

For the mixed-spider assertion, the exact two-tail frontier DP from the previous run was reused with one required local edge. The seven local edge types are

- `c`: center-to-terminal spoke;
- `ds`: direct-leaf-to-terminal spoke;
- `di`: direct internal edge `c-d`;
- `b`: subdivider-to-terminal spoke;
- `x`: endpoint-to-terminal spoke;
- `i1`: internal edge `c-b`;
- `i2`: internal edge `b-x`.

For each type the symbolic `5 x 5` transfer has a constant positive diagonal `d`, zeros outside the positions displayed in (4.1), and, after division by `d`, satisfies

\[
M_{i,5}/d=\sum_j M_{1,j}/d-M_{1,i}/d
\]

for the three middle states. Thus it is exactly `C(x,z)`. The dependence on `p,q` is rational with positive physical denominators and follows from the previously proved commuting two-tail formulas; this is symbolic in `p,q`, not interpolation at finitely many sizes. QED.

## 5. New cross-component Rayleigh identity

Consider two distinct right components. Normalize their unmarked transfers to

\[
A=C(x,z),\qquad B=C(y,w).
\]

Let requiring edge `e` in the first component change its response to

\[
E=C(x+\delta,z+\alpha),
\]

and requiring edge `f` in the second change it to

\[
F=C(y+\varepsilon,w+\beta).
\]

Write

\[
d=\sum_i\delta_i,\qquad e_0=\sum_i\varepsilon_i,
\qquad k=\kappa(\delta,\varepsilon),
\tag{5.1}
\]

\[
a=d+\alpha+\kappa(\delta,y),
\qquad
b=e_0+\beta+\kappa(x,\varepsilon),
\tag{5.2}
\]

and

\[
H_0=1+\sum x_i+\sum y_i+z+w+\kappa(x,y),
\qquad
s_0=4+2\left(\sum x_i+\sum y_i\right).
\tag{5.3}
\]

Appending arbitrary unmarked components contributes `U(u,v)` from (3.1). Exact multiplication in (4.3) shows that the four normalized forest counts have the common affine form

\[
L(X,Y)=H(X,Y)+S(X,Y)u+6v.
\]

The increments are

\[
H(E,B)-H(A,B)=a,
\qquad H(A,F)-H(A,B)=b,
\]

\[
H(E,F)-H(A,B)=a+b+k,
\]

and the corresponding `S` increments are `2d`, `2e_0`, and `2d+2e_0`.

Expanding the determinant

\[
L(E,B)L(A,F)-L(A,B)L(E,F)
\]

gives the exact identity

\[
\Delta^*=4de_0u^2+igl(2ae_0+2bd-ks_0\bigr)u-6kv+ab-H_0k.
\tag{5.4}
\]

After the strip substitution `v=u^2/2-hu`,

\[
\boxed{
\Delta^*=(4de_0-3k)u^2+
\bigl(2ae_0+2bd-k(s_0-6h)\bigr)u+
(ab-H_0k).
}
\tag{5.5}
\]

All omitted factors are positive diagonal normalizations of the two marked component transfers and of the unmarked remainder.

This is the new cross-component sign lemma. If

\[
k\ge0,
\quad L_2:=4de_0-3k\ge0,
\tag{5.6}
\]

\[
L_{1,\min}:=2ae_0+2bd-k\left(s_0-6\frac{43}{360}\right)\ge0,
\quad C_0:=ab-H_0k\ge0,
\tag{5.7}
\]

then `Delta^*>=0` for every `u>=0` and every strip coordinate `h in [43/360,1/8]`. Indeed the linear coefficient in (5.5) is increasing in `h` when `k>=0`, so the lower strip endpoint is worst. Strict inequalities imply a strict Rayleigh gap.

The archived checker independently proves (4.3) and (5.5) as polynomial identities over symbolic variables.

## 6. Exact all-parameter cross-component certificate

Terminal permutations reduce a spoke edge to one distinguished terminal. There are seven local edge types, and a pair of types uses two terminal-relation cases exactly when both are spokes (`c,ds,b,x`). Thus unordered type pairs give

\[
\binom{7+1}{2}=28
\]

base schemes, plus ten extra different-terminal spoke/spoke schemes, for exactly

\[
\boxed{38\text{ symbolic cross-component schemes}.}
\]

For the first component use parameters `(p,q)` and for the second `(r,s)`. Shift by the physical minimum required by the marked edge type:

- `c`: `(0,0)`;
- `ds,di`: `(1,0)`;
- `b,x,i1,i2`: `(0,1)`.

Thus write `p=p_0+X_1`, `q=q_0+X_2`, `r=r_0+X_3`, `s=s_0+X_4` with all `X_i>=0`.

The staged exact SymPy calculation forms `k,L_2,L_{1,min},C_0` for every scheme. After cancellation, **both numerator and denominator of every one of these 152 rational functions have strictly positive coefficients** in `X_1,...,X_4`. Hence all four quantities are strictly positive at every physical parameter value.

The exact certificate contains 38 schemes. Its SHA-256 is

`8d698ab33fa8c259dc545089080b8253f78fe5221bbd1bf5f0ddd56d63d79f0b`.

The smallest positive numerator coefficient seen in each family is

\[
\begin{array}{c|r|c}
\text{quantity}&\text{minimum coefficient}&\text{scheme attaining the minimum}\\ \hline
k&264600&(c,c,\text{same terminal})\\
L_2&691488&(c,c,\text{different terminals})\\
L_{1,\min}&154893312&(c,c,\text{different terminals})\\
C_0&963780608&(c,c,\text{different terminals}).
\end{array}
\]

The largest numerator term counts are respectively `36,36,84,160`. There are **zero failures**. A separately generated compressed replay certificate, SHA-256 `fdd36c53bea6943a0d2699cddf66380411e9bf399ef51e6c8a753ccae4117952`, also executed successfully and reproduced the same four minima.

Two earlier monolithic regeneration attempts exceeded the local execution cap. They are not represented as successful executions. The theorem uses the successfully executed staged exact coefficient generation plus the exact verifier archived with this report.

## 7. New all-parameter theorem

### Theorem `T07-INDEPENDENT-MIXED-SPIDER-FOREST-PNC-26`

Let

\[
H=\bigsqcup_{j=1}^m D_{p_j,q_j},
\qquad m<\infty,\quad p_j,q_j\ge0,
\]

and let

\[
\boxed{G=\overline{K_3}\vee H},
\]

where the three vertices in `bar(K3)` are independent and each is adjacent to every right vertex. Then for every distinct present edges `e,f`,

\[
\boxed{\Delta_G(e,f)\ge0.}
\]

The inequality is strict for every physical pair except in the degenerate graph `m=1,p_1=q_1=0`, namely `K_{3,1}`. In that tree every edge subset is acyclic, so the edge indicators are independent.

### Proof

Fix `e,f`.

**Case 1: both edges lie in the same mixed-spider component.** Expose that component. The previous exact same-component theorem reduces its possible marked pairs to 48 symbolic schemes and proves their Rayleigh response polynomial nonnegative for every residual response satisfying (3.1): 41 schemes by strip-Bernstein coefficients and seven by the strip-discriminant identity. Every other mixed-spider component has response in the same strip, and products preserve the strip by the weighted-average response identity. Hence the previous same-component proof applies unchanged with an arbitrary number of other mixed-spider components, not merely isolated vertices. The only zero-constant local case is the two distinct center spokes of `D_{0,0}`; it is an actual equality only when no other right component remains, i.e. `G=K_{3,1}`.

**Case 2: the edges lie in two distinct mixed-spider components.** Apply Lemma 4 and (5.5). The 38-scheme exact certificate proves strict positivity of `k,L_2,L_{1,min},C_0` for every physical pair of component parameters. Therefore every coefficient in the quadratic (5.5) is nonnegative and its constant term is strictly positive. Thus `Delta_G(e,f)>0`.

The two cases exhaust all edge pairs. QED.

The status of this restricted theorem is **CANDIDATE_FULL pending independent review**. It is not promoted to a solution of the parent conjecture.

## 8. A genuinely uncovered complementary family

A clean subfamily is

\[
\boxed{G_{m,q}=\overline{K_3}\vee\left(\bigsqcup_{j=1}^m D_{0,q}\right)},
\qquad m\ge2,\ q\ge3.
\]

Each right component is a once-subdivided `q`-arm star: it has diameter four and a degree-`q` branch vertex, so it is neither a path, cycle, nor star. Both `m` and `q` are unbounded. Its exact size is

\[
|V|=3+m(1+2q),
\qquad
|E|=m(3+8q).
\]

This is strictly beyond the preceding NM13-08 theorem, which allowed only one mixed spider plus isolated vertices.

It is also complementary to the current NM13-04 **triangle-seeded arbitrary-star-forest** line. Here the left terminal triple is independent and the right side contains multiple depth-two branching components. Nontrivial graphs in the present class have clique number at most three, whereas every nonempty triangle-seeded join `K_3\vee L` contains a `K_4`. Unit-weight p-NC has no inheritance rule under deleting the three seed-triangle edges, so the present theorem is not a corollary of NM13-04.

Whenever the right side has at least three vertices, `G` is 3-connected and contains `K_{3,3}`. Hence the family is nonplanar and non-series-parallel, placing it directly in the structural regime left after the P14 minimal-counterexample reduction and outside Erickson's series-parallel theorem.

As an independent finite sanity check, exact forest DP on

\[
\overline{K_3}\vee(D_{0,2}\sqcup D_{0,2})
\]

gives 13 vertices, 38 edges,

\[
I=533404640,
\]

and minimum Rayleigh numerator

\[
\boxed{11018693065536},
\]

attained by an `i1` internal edge in one subdivided arm of each of the two components. This finite check is not the proof; the 38-scheme symbolic transfer above is.

## 9. Literature boundary and what is not claimed

The distinction from neighboring results remains essential.

- The uniform-spanning-tree theorem is not the uniform-all-forests conjecture.
- Erickson's weighted SOS theorem is for series-parallel graphs; the present graphs contain `K_{3,3}`.
- Stark's complete-graph theorem is a special complete-graph result.
- Tang--Zhang's 2026 result includes complete-graph forests with a **fixed number of components**; it does not establish the arbitrary-graph uniform law mixing all component counts.
- Bado's wheel theorem is another genuine all-forests infinite class, not a general solution.
- This run proves only the displayed independent-terminal mixed-spider-forest class. It does not prove p-NC for arbitrary finite graphs or arbitrary right trees.

## 10. Residual obstruction, failures, and next attack

The previous residual obstruction — two marked edges in distinct mixed-spider components — is removed.

The new obstruction is structural rather than multiplicity-based: arbitrary right trees need not be depth-two mixed spiders, and arbitrary 3-connected graphs need not decompose around one independent terminal triple. The natural next attack is therefore **not** another component-count enlargement. It is to characterize which rooted branch gadgets preserve the `C(x,z)` one-edge cone. Two concrete routes are now available:

1. derive a center-gluing/depth-three operator criterion whose unmarked and one-edge increments preserve (5.6)--(5.7); or
2. eliminate the 38 atom-specific checks by proving an abstract cone theorem for admissible one-edge increments `(delta,alpha)` in the `C(x,z)` algebra.

A successful version would extend arbitrary-multiset closure to a substantially larger class of right trees and would be a genuine mechanism advance toward the parent problem.

Execution honesty: two monolithic regeneration attempts timed out; the successful evidence is the staged exact symbolic generation, exact coefficient verifier, compressed replay checker, and the independent finite DP sanity check. No floating-point sign decision enters the theorem.

## 11. Durable artifacts

This run creates, without overwriting older work:

- this substantive report;
- `2026-09-20T14-37-32Z__ledger_delta.yaml`;
- `2026-09-20T14-37-32Z__mixed-spider-forest-cross-response-checker.py`;
- `2026-09-20T14-37-32Z__mixed-spider-forest-cross-response-checker.out`.

The checker/output preserve the generic algebra identity, the cross-component determinant formula, the exact 38-scheme certificate digest and positivity summary, and the independent DP sanity value. The full claim remains pending later independent review.
