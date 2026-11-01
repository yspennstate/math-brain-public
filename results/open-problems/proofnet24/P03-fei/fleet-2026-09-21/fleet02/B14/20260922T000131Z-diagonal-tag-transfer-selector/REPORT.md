# B14 — diagonal tag-transfer selector and proxy-injective critical cores

**Status:** **ESSENTIAL_STEP_APPLIED / PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain cognitive/retrieval module was used.  
**Role:** Campaign A, FEI erasure/selector/restriction.  
**Model self-report:** GPT-5.6 Sol. Requested reasoning: maximum actually supported. Configured/known reasoning selector: UNKNOWN / not exposed. Provider reasoning-token usage and thinking-time usage: not exposed.  
**Novelty/priority:** unverified; no publication-priority claim.

## 0. Exact before/after and completed peer result consumed

Fresh scientific `master`, the applicable repository rules, `proofnet24/P03-fei/README.md`, the current joint FEI state, and the execution reset were read before this write.

The preceding three substantive fleet02/B14 reports were:

1. `20260921T210915Z-crossing-information-selector`: a physical posterior-crossing/KL selector paid the rare survivor Shannon scale, but still required a block with a bounded corrected-erasure cost;
2. `20260921T220126Z-stationary-trigger-selector`: a stationary selector paid closed `q/(16r)` trigger systems and localized failure to a stalled exceptional sector;
3. `20260921T230653Z-asymmetric-shortcircuit-ledger`: the paid full-block region was enlarged asymmetrically, and on fixed-relative error a random-order first-mismatch tree was proved to spend at least `15rq/16` folded influence while leaving small pivotality uncertainty. Its **upper corrected Shannon cost remains open**.

Thus the same global interface-A obligation is not yet discharged. This run deliberately does **not** scan another threshold or try to upper-bound the same first-mismatch numerator. It executes a different physical mechanism: if two rare pivotality rows are carried by the same near-subcube proxy, query one **pivot itself**. A diagonal Fourier tag then survives in the other pivot and makes the restriction cheap.

The named completed other-account result used decisively is

`fleet04/B17/20260921T231353Z-true-stall-exception-ladder/REPORT.md`.

That report strengthens the stalled-core reduction to TRUE_STALL and gives an exact Boolean obstruction to charging certified-row influence to exceptional-endpoint influence: its family `G_{r,m}` has `m` certified pivots of influence `q` all using the **same exact atom proxy**, only `r` exceptional controls of influence `3q`, and certified/exceptional influence ratio `m/(3r) -> infinity`. The present theorem shows that this fan-in geometry cannot survive ratio-critical reduction: duplicate proxy rows admit a much cheaper singleton physical restriction, with zero entropy cost in the exact family.

I also use the completed fleet04/B13 result

`fleet04/B13/20260921T2325Z-asymmetric-exception-compiler/REPORT.md`.

Its paid low-defect branch produces a proxy atom `Q` of density `q=2^{-r}` with total pivotality-support error

\[
e\le {q\over 8(r+1)}
\tag{0.1}
\]

and the existing asymmetric B14 block theorem pays the row whenever the average-control condition holds. The same tolerance (0.1) is exactly the duplicate-proxy regime treated below.

**FULL-PROBLEM CHANGE:** NONE. Full FEI remains open.  
**MECHANISM CHANGE:** YES. The operation is now a pivot singleton selected by a *pairwise Fourier-tag collision*, not the defining control block or its short-circuit tree.

## 1. Normalization and the current sufficient end-to-end interface

Let

\[
f:\{0,1\}^n\to\{-1,+1\},\qquad
\Pr(X=S)=\widehat f(S)^2
\]

be the Fourier spectral sample. Spectral entropy is in bits. Put

\[
p_i=\Pr(i\in X)=\operatorname{Inf}_i(f),\qquad
j_i=\min(p_i,1-p_i),\qquad
J(f)=\sum_i j_i.
\]

Character multiplication may be used to median-center a state; it preserves spectral entropy and folded influence.

For a physical singleton restriction `i`, write

\[
\Delta_iH=H(f)-\frac12\bigl(H(f_{i=0})+H(f_{i=1})\bigr),
\]
\[
D_i=J(f)-\frac12\bigl(J(f_{i=0})+J(f_{i=1})\bigr).
\]

The exact folded-drift identity gives

\[
D_i=j_i+C_i\ge j_i,
\tag{1.1}
\]

where `C_i>=0` is the sum of folded posterior crossings of surviving coordinates.

For the already established bounded correction

\[
\mathcal C(f)=\sum_i\mathfrak j(j_i),
\qquad
\mathcal F(f)=H(f)-\mathcal C(f),
\qquad
0\le\mathcal C(f)\le {2\over\ln2}J(f),
\tag{1.2}
\]

the exact singleton corrected decrement has the form

\[
E_i:=\Delta_i\mathcal F=B_i-Q_i\le B_i,
\qquad Q_i\ge0,
\tag{1.3}
\]

where `B_i=H(X_i|X_{-i})` is the spectral erasure entropy.

A sufficient Campaign-A step is therefore either a direct `Delta H <= C D` inequality or the weaker corrected inequality `E<=CD`, with a globally bounded potential. The theorem below supplies both on a new pairwise geometry.

## 2. PROVED: diagonal tag-transfer restriction lemma

For distinct physical coordinates `i,j`, define the **diagonal mismatch mass**

\[
\varepsilon_{ij}
:=\Pr\bigl(f(x)\ne f(x\oplus e_i\oplus e_j)\bigr).
\tag{2.1}
\]

By the Walsh correlation identity,

\[
\boxed{
\varepsilon_{ij}
=\Pr(X_i\oplus X_j=1).
}
\tag{2.2}
\]

Set `bar epsilon_ij=min(epsilon_ij,1-epsilon_ij)`.

### Theorem 2.1 — a surviving Fourier tag pays the restriction

For every Boolean `f` and every distinct `i,j`,

\[
\boxed{
B_i\le h_2(\varepsilon_{ij}),
\qquad
E_i\le h_2(\varepsilon_{ij}),
}
\tag{2.3}
\]

and, more strongly,

\[
\boxed{
\Delta_iH
\le
h_2(\varepsilon_{ij})
+{2\over\ln2}\,\bar\varepsilon_{ij}.
}
\tag{2.4}
\]

In particular, if `epsilon_ij=0` or `1`, restricting `i` preserves spectral entropy exactly.

### Proof

For every Fourier fibre indexed by `T subseteq [n]\{i}`, put

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),
\qquad w_T=u_T^2+v_T^2,
\]

and, when `w_T>0`,

\[
t_T={\min(u_T^2,v_T^2)\over w_T}\in[0,1/2].
\]

The exact one-coordinate restriction decomposition is

\[
B_i=\sum_T w_T h_2(t_T),
\qquad
JS_i=\sum_Tw_T\mathfrak j(t_T),
\qquad
\Delta_iH=B_i+JS_i,
\tag{2.5}
\]

with the already proved scalar bound

\[
\mathfrak j(t)\le{2\over\ln2}t.
\tag{2.6}
\]

Let

\[
M_i:=\sum_T\min(u_T^2,v_T^2)=\sum_Tw_Tt_T.
\]

Partition the fibres according to whether `j in T`. If `j notin T`, the `v_T` coefficient has odd `{i,j}` parity and `u_T` has even parity. If `j in T`, the roles reverse. Thus in every fibre the smaller squared coefficient is bounded by the odd-parity coefficient and also by the even-parity coefficient. Summing gives

\[
M_i\le\varepsilon_{ij},
\qquad
M_i\le1-\varepsilon_{ij},
\qquad
M_i\le\bar\varepsilon_{ij}.
\tag{2.7}
\]

Concavity of binary entropy and `sum_T w_T=1` yield

\[
B_i\le h_2(M_i)
\le h_2(\bar\varepsilon_{ij})
=h_2(\varepsilon_{ij}).
\tag{2.8}
\]

Equation (1.3) gives the corrected inequality. Equations (2.5)--(2.7) and (2.6) give

\[
JS_i\le {2\over\ln2}M_i
\le {2\over\ln2}\bar\varepsilon_{ij},
\]

which proves (2.4). QED.

### Interpretation

If the spectral bits `X_i` and `X_j` are almost the same (or almost complementary), then `j` is an almost-perfect tag for the Fourier fibre bit erased by restricting `i`. This is not a prescribed-coordinate theorem: the step is selected only when a second physical coordinate supplies this tag.

## 3. PROVED: physical proxy agreement forces a small diagonal mismatch

For a physical coordinate `i`, let

\[
\eta_i(x)=1_{\{f(x)\ne f(x\oplus e_i)\}}
\]

be its pivotality event, viewed as an `i`-invariant function on the cube.

### Lemma 3.1 — two rows close to one proxy have a cheap diagonal

Let `Q` be any physical event independent of both `i` and `j`. If

\[
\Pr(\eta_i\triangle Q)\le e_i,
\qquad
\Pr(\eta_j\triangle Q)\le e_j,
\tag{3.1}
\]

then

\[
\boxed{\varepsilon_{ij}\le e_i+e_j.}
\tag{3.2}
\]

### Proof

Along the two-edge path `x -> x+e_i -> x+e_i+e_j`, endpoint disagreement is the XOR of the two edge-status bits:

\[
1_{\{f(x)\ne f(x+e_i+e_j)\}}
=
\eta_i(x)\oplus\eta_j(x+e_i).
\]

Because `Q` is independent of `i`, `Q(x)=Q(x+e_i)`. Hence if the two pivotality bits differ, at least one differs from `Q`. Union bound and translation invariance of uniform measure give (3.2). QED.

More generally, for two proxy events `Q_i,Q_j` independent of `i,j`,

\[
\varepsilon_{ij}
\le e_i+e_j+\Pr(Q_i\triangle Q_j).
\tag{3.3}
\]

This metric form will be useful for the remaining distinct-proxy sector.

## 4. PROVED: duplicate near-subcube proxies have a `23/20` physical singleton payment

Call `(i,Z,Q)` **A12-certified** if

- `Z` is a nonempty physical block disjoint from `i`, `r=|Z|`;
- `Q` is one atom of the `Z` cube, so `q=2^{-r}`;
- after the current median-character normalization, the pivotality support obeys
  \[
  \Pr(\eta_i\triangle Q)\le {q\over8(r+1)}.
  \tag{4.1}
  \]

This is the total-error scale produced by the completed fleet04/B13 asymmetric low-defect compiler. It is also sufficient for the earlier asymmetric full-block theorem whenever the average-control condition holds, since (4.1) implies separately `E^-<=q/16` and `E^+<=q/[8(r+1)]`.

### Theorem 4.1 — duplicate-proxy singleton selector

Suppose two distinct active pivots `i,j` admit A12 certificates with the **same** physical atom `(Z,Q)`. Then restricting either pivot is a genuine physical paid step:

\[
\boxed{
E_i\le {3\over4}D_i,
\qquad
\Delta_iH<{23\over20}D_i.
}
\tag{4.2}

The same holds with `i,j` interchanged.

### Proof

By Lemma 3.1,

\[
\varepsilon_{ij}\le {q\over4(r+1)}=:x.
\tag{4.3}
\]

Density mismatch is at most symmetric-difference error, so the folded pivot mass satisfies

\[
j_i\ge q-{q\over8(r+1)}
=q\left(1-{1\over8(r+1)}\right)=:d_0.
\tag{4.4}
\]

(The `r=1` half-density case is also valid after folding.) Hence `D_i>=d_0` by (1.1).

We now bound the erasure term uniformly in `r`. The elementary inequality

\[
h_2(s)\le s\log_2{e\over s}
\tag{4.5}
\]

gives, using `q=2^{-r}`, `log_2(r+1)<=r`, and `log_2 e<3/2`,

\[
\begin{aligned}
h_2(x)
&\le {q\over4(r+1)}
\left(r+2+\log_2(r+1)+\log_2e\right)\\
&< {q\over4(r+1)}\left(2r+{7\over2}\right)\\
&\le {3\over4}
q\left(1-{1\over8(r+1)}\right)
={3\over4}d_0.
\end{aligned}
\tag{4.6}
\]

The last inequality is equivalent to `r>=7/8`.

Since `epsilon_ij<=x<=1/2`, Theorem 2.1 gives

\[
E_i\le B_i\le h_2(\varepsilon_{ij})\le h_2(x)\le {3\over4}D_i.
\]

For the coherent term, `2/ln2<3`, so

\[
JS_i
\le {2\over\ln2}\varepsilon_{ij}
< {3q\over4(r+1)}.
\]

Furthermore

\[
{3q\over4(r+1)}
\le {2\over5}d_0,
\tag{4.7}
\]

because after multiplying by `20(r+1)/q`, (4.7) is exactly `15<=8r+7`, true for `r>=1`. Therefore

\[
\Delta_iH=B_i+JS_i
<\left({3\over4}+{2\over5}\right)D_i
={23\over20}D_i.
\]
QED.

### Exact shared-support limit

If both pivotality events equal the same proxy exactly, `e_i=e_j=0`, then `epsilon_ij=0` and Theorem 2.1 gives

\[
\boxed{\Delta_iH=0.}
\tag{4.8}
\]

The other pivot is an exact Fourier tag which prevents any spectral collision when `i` is restricted.

## 5. PROVED: a globally nonreused physical deduplication compiler

The previous theorem is local, but its budget is the exact folded drift, so it compiles globally without any new potential.

At a centered state, use the following physical policy.

1. **Duplicate step.** If two A12-certified active pivots share the same proxy atom `(Z,Q)`, restrict one of those pivots.
2. **Direct block step.** Otherwise, if an A12-certified witness `(i,Z,Q)` satisfies the average-control condition
   \[
   \sum_{k\in Z}j_k\le rj_i,
   \tag{5.1}
   \]
   apply the already proved asymmetric full-block restriction `Z`; it obeys `Delta_Z H<=12 D_Z`.
3. Otherwise stop and label the state **INJECTIVE_TRUE_STALL** for this phase.

Re-center each child and repeat. Every successful operation removes at least one physical coordinate, so the tree is finite.

By Theorem 4.1 every duplicate step has coefficient `<23/20<12`, and every direct block step has coefficient `12`. If `w_v` is the reach probability of node `v`, exact physical telescoping gives

\[
\sum_{v\text{ successful}}w_v\Delta_vH
\le12\sum_vw_vD_v
\le12J(f_{\rm root}).
\tag{5.2}
\]

Consequently

\[
\boxed{
H(f)-12J(f)
\le
\mathbb E_{\ell}
\bigl[H(f_\ell)-12J(f_\ell)\bigr].
}
\tag{5.3}
\]

Thus any Boolean function with `H/J>12` has a physical descendant with positive `H-12J` that is INJECTIVE_TRUE_STALL. Among such descendants one may choose minimum relevant dimension.

### Structure of an INJECTIVE_TRUE_STALL state

Such a state satisfies simultaneously:

1. no A12 witness is directly payable by (5.1);
2. no two A12-certified pivots admit the same proxy atom;
3. every A12-certified pivot has a strict-influence path to a non-A12 coordinate.

For item 3, start from any A12 witness `(i,Z,Q)`. Failure of (5.1) gives some `k in Z` with `j_k>j_i`. If `k` is A12-certified, repeat from any of its witnesses. Folded influence strictly increases, so no coordinate repeats; finiteness forces termination at a non-A12 coordinate.

This is the same monotone exception-ladder idea as fleet04/B17, but with two genuine strengthenings: the wider asymmetric A12 error scale and **proxy injectivity** forced by an actual singleton restriction.

## 6. The fleet04/B17 fan-in obstruction is real but cannot be the critical obstruction

In fleet04/B17's exact family `G_{r,m}`, all `m` certified pivots `y_1,...,y_m` have the same exact pivotality support `Q={x=0^r}`. Their total certified influence can overwhelm the exceptional controls by the factor `m/(3r)`, correctly refuting any attempt to charge raw certified influence to raw endpoint influence.

But for every pair `y_a,y_b`, (4.8) gives

\[
\Delta_{y_a}H=0,
\qquad
D_{y_a}\ge j_{y_a}=q>0.
\tag{6.1}
\]

Hence restricting `y_a` strictly increases the `H/J` ratio whenever `H>0`. The family therefore cannot occur as an `H/J`-maximizing restriction-critical obstruction while `m>=2`. The endpoint-fan-in counterexample remains valid at its stated scope, but its repeated-proxy geometry is removed before the minimal dangerous core.

This is why the new theorem is not merely another auxiliary constant: it changes the exact critical-core exception sector produced by the realizable induction.

## 7. Quantitative separation of the remaining proxies

The tag-transfer theorem also gives a metric obstruction for any two approximate proxies.

Let `(i,Q_i)` and `(j,Q_j)` have errors `e_i,e_j`, with the proxy events independent of both pivots, and put

\[
s=e_i+e_j+\Pr(Q_i\triangle Q_j).
\]

If `s<=1/2`, then by (3.3) and Theorem 2.1,

\[
\boxed{
E_i\le h_2(s),
\qquad
\Delta_iH\le h_2(s)+{2\over\ln2}s.
}
\tag{7.1}
\]

Therefore on an `H/J` restriction-critical core of ratio `R`,

\[
\boxed{
Rj_i
\le h_2(s)+{2\over\ln2}s.
}
\tag{7.2}
\]

On an `F/J` corrected-critical core of ratio `rho`,

\[
\boxed{
rho j_i\le h_2(s).
}
\tag{7.3}
\]

Thus surviving low-error proxies cannot cluster arbitrarily in physical symmetric-difference distance. The exact next sector is not generic fan-in; it is an **injective, quantitatively separated family of proxy atoms feeding noncertified higher-influence endpoints**.

Equations (7.2)--(7.3) are lower separation constraints, not a proof that the remaining proxy packing has bounded total cost.

## 8. Diagnostic check

A checker accompanying this report exhaustively scans all Boolean functions through four variables modulo global sign, all unordered coordinate pairs, and every relevant Fourier fibre. It verifies:

- the exact physical/spectral identity (2.2);
- `M_i<=min(epsilon,1-epsilon)`;
- `B_i<=h_2(epsilon)`;
- `JS_i<=(2/ln2)M_i`;
- the resulting full bound (2.4).

There are **197,000** function/pair cases in the scan. Maximum observed positive violation of every displayed inequality is `0` at floating precision, and the physical/spectral diagonal mismatch residual is exactly `0` in the computed dyadic arithmetic path. This is regression evidence only; Sections 2--5 are analytic proofs.

The scalar `23/20` certificate was also checked through `r=10000`; the actual ratio bound is largest at `r=1` and is about `1.104271`, below the proved coarse `1.15` constant. The decimal is not used in the proof.

## 9. Primary-literature status

A fresh bounded primary-source check found González--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (arXiv:2606.00246, May 29 2026), whose stopping-tree framework shows how suitable physical restriction decrement inequalities compile to FEI but does not prove the universal decrement. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions* (arXiv:2609.21563, September 18 2026), proves FEI for plateaued and partially bent classes, not universally.

No claim is made that the diagonal tag-transfer inequality, duplicate-proxy compiler, or proxy-injective critical-core reduction is new in the literature. Failure of a bounded search to locate the exact formulation would not establish novelty.

## 10. Exact remaining universal obligation and handoff

**Old unpaid implication:** upper-bound the corrected Shannon cost of the fixed-relative first-mismatch tree, or otherwise pay the TRUE_STALL sector.

**New proved inference:** before that hard numerator must be faced, every repeated near-subcube proxy can be removed by a cheap **physical pivot restriction**. At the current fleet04/B13 asymmetric error scale the uncorrected coefficient is `<23/20`, and exact repeated supports cost zero. Combining this with the existing direct block step gives the realizable compiler (5.3).

**Remaining universal obligation:** rule out or pay an **INJECTIVE_TRUE_STALL** minimum-dimensional core: no directly payable A12 row, no common proxy atom shared by two A12 pivots, and every remaining A12 row runs by strict increasing folded influence to a genuinely non-A12 endpoint. Equivalently, exploit the now-forced proxy separation (7.2)--(7.3) to pay distinct-proxy fan-in, or return to the fixed-relative short-circuit numerator only on this proxy-injective residual.

This does not assert an every-coordinate payment, does not use a tensor-stable every-critical-core shell statement, and does not reopen global phase/rank/l1 or sign-free parity-profile sufficiency.

**Outcome label:** `ESSENTIAL_STEP_APPLIED`.  
**FULL-PROBLEM CHANGE:** NONE — full FEI is still OPEN / NOT PROVED.  
**MECHANISM CHANGE:** YES — a pairwise diagonal Fourier tag now supplies a direct pivot restriction and globally nonreused deduplication phase.
