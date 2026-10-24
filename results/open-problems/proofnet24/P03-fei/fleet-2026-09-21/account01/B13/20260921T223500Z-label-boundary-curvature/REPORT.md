# B13 FEI route 2/13 — from block-profile obstruction to a label-entropy / mixed-curvature bridge

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical/cognitive brain retrieval or receiver-context was available or used.

**Route:** APPROACHES 2/13. This run deliberately changes mechanism after the preceding B13 two-block quadratic interaction theorem: first it constructs a decisive non-Boolean relaxation showing that *all* of those complementary-cut inequalities are too weak to imply FEI, then it replaces them by a higher-order Booleanity constraint and an exact entropy-to-physical-boundary lemma.

**Priority:** no novelty or publication-priority claim. The bounded-degree junta mechanism below is essentially the standard degree/support argument; it is rederived because its exact form identifies why the relaxed profile is non-Boolean.

## 1. Compatible other-account result substantively consumed

The primary completed input is **account04/B13**, `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`. Its one-shot source-frontier construction leaves source representatives `S` after revealing one physical block and defines, for each surviving source row `r`, a coordinate-subcube proxy

\[
Q_r=\{z_{F_r}=a_r\},\qquad q_r(z)=1_{Q_r}(z),
\]

with physical error `e_r=mu(E_r triangle Q_r)`. The branch-dependent character label is

\[
T(z)=\{r\in S:q_r(z)=1\}.
\]

That report proves that after gauging by `chi_{T(z)}` the expected residual ordinary influence is exactly `sum_{r in S} e_r` and is at most the global depth-defect bank. It identifies the still-unpaid quantity sharply as the Shannon/information cost of the character label `T(z)` together with the reveal cost.

I also use the already completed **account03/B13** robust integrability-DAG theorem (`20260921T203308Z-integrability-dag/REPORT.md`) only for the reciprocal-component refinement in Section 5. The main entropy-boundary theorem in Section 4 does not need the DAG.

## 2. Decisive obstruction: the previous all-cut quadratic constraint is not enough

The preceding B13 theorem proved that for every Boolean squared spectrum and every complementary cut `A|B`, if

- `a` is the nonempty spectral mass entirely on `A`,
- `b` is the nonempty spectral mass entirely on `B`, and
- `q` is the spectral mass meeting both sides,

then

\[
q\ge \gamma ab,
\qquad
\gamma=\frac{13-3\sqrt{17}}8=0.078835390393377\ldots .
\tag{2.1}
\]

It was tempting to combine (2.1) over a hierarchy of cuts to pay Shannon label entropy. That route is now **decisively killed in its present form**.

For every `m>=2`, define an abstract random subset `S_m subseteq [m]` by

\[
\Pr(S_m=\varnothing)=\frac{47}{64},
\]
\[
\Pr(S_m=\{i\})=\frac1{4m}\quad(1\le i\le m),
\]
\[
\Pr(S_m=\{i,j\})=
\frac1{64\binom m2}\quad(i<j),
\]

and no other mass. Thus the total singleton mass is `1/4`, the total pair mass is `1/64`, and

\[
\mathbb E|S_m|=\frac14+\frac2{64}=\frac9{32}.
\tag{2.2}
\]

For a cut `U|U^c` with `|U|=u`, let `a_U,b_U,q_U` be the exact analogues of the three masses above. Then

\[
a_U=rac{u}{4m}+rac{\binom u2}{64\binom m2},
\qquad
b_U=rac{m-u}{4m}+rac{\binom{m-u}2}{64\binom m2},
\]
\[
q_U=rac{u(m-u)}{64\binom m2}.
\tag{2.3}
\]

Writing `x=u/m`,

\[
a_U\le\frac{17}{64}x,
\qquad
b_U\le\frac{17}{64}(1-x),
\]
while

\[
q_U
=\frac1{32}\frac{m}{m-1}x(1-x)
\ge\frac1{32}x(1-x).
\]
Therefore every nontrivial cut obeys the stronger inequality

\[
\boxed{
q_U\ge \frac{128}{289}a_Ub_U,
\qquad
\frac{128}{289}=0.44290657\ldots>\gamma.
}
\tag{2.4}
\]

So this law satisfies **all** of the previously proved quadratic complementary-cut constraints, with a factor more than five stronger than required.

But its entropy is

\[
H(S_m)
=-\frac{47}{64}\log_2\frac{47}{64}
+\frac14\log_2(4m)
+\frac1{64}\log_2\!\left(64\binom m2\right),
\tag{2.5}
\]
so

\[
\boxed{
\frac{H(S_m)}{\mathbb E|S_m|}=\log_2 m+O(1)\to\infty.
}
\tag{2.6}
\]

The local checker in this folder evaluated every cut for `m=5,8,16,64,256,1024,4096`; there were zero violations. At `m=4096`, the minimum observed `q_U/(a_Ub_U)` was `0.470277878850`, while `H/E|S|=15.218553983760`.

Thus **the all-cut quadratic profile inequalities by themselves cannot imply FEI**, even for a relaxed law supported only on sets of cardinality at most two.

## 3. The missing ingredient is genuinely Boolean: a degree/support rigidity lemma

The relaxation above is not a Boolean squared Fourier spectrum for `m>=5`. The reason is a useful exact Booleanity constraint.

### Lemma 3.1 — support uncertainty for a low-degree cube polynomial

If a nonzero real function `h:{-1,1}^N -> R` has Fourier degree at most `r`, then

\[
\boxed{\Pr(h\ne0)\ge2^{-r}.}
\tag{3.1}
\]

**Proof.** Induct on `r` and the number of relevant variables. If `h` is constant the claim is immediate. Otherwise choose a relevant variable and write

\[
h(x',x_N)=a(x')+x_N b(x'),
\]

with `b` nonzero and of degree at most `r-1`. Whenever `b(x')!=0`, at least one of `a(x')+b(x')` and `a(x')-b(x')` is nonzero. Hence

\[
\Pr(h\ne0)\ge\frac12\Pr(b\ne0)
\ge\frac12 2^{-(r-1)}=2^{-r}.
\]
`QED`

### Corollary 3.2 — exact bounded-degree junta bound

If a Boolean `f` has Fourier degree at most `d`, every relevant coordinate satisfies

\[
\operatorname{Inf}_i(f)\ge2^{-(d-1)}.
\tag{3.2}
\]

Indeed `D_i f` is a nonzero `{0,plus/minus 1}`-valued function of degree at most `d-1`, and its support density is exactly `Inf_i(f)`. Since

\[
I(f)=\sum_S |S|\widehat f(S)^2\le d,
\]

the number `M` of relevant coordinates obeys

\[
\boxed{M\le d\,2^{d-1}.}
\tag{3.3}
\]

For `d=2`, at most four coordinates can be relevant. The relaxation in Section 2 has positive singleton mass on every one of its `m` coordinates, so if it were a Boolean squared spectrum it would have `m` relevant variables while having Fourier degree at most two. Hence it is impossible for every `m>=5`.

This is the precise lesson from the failed quadratic route: the missing constraint is not another complementary-cut Gini inequality. Booleanity couples *spectral depth* to the number of coordinates on which small masses can genuinely live.

## 4. Universal replacement lemma: entropy of a cube-valued label is paid by its physical edge boundary

The account04/B13 proxy-gauge theorem leaves exactly a finite-valued character label. For such labels there is a clean dimension-free inequality.

### Theorem 4.1 — partition entropy / edge-boundary inequality

Let `Z` be uniform on `{0,1}^B` and let `Y=Y(Z)` take values in any finite set. Define

\[
I(Y):=\sum_{k\in B}
\Pr\bigl(Y(Z)\ne Y(Z\oplus e_k)\bigr).
\]

Then

\[
\boxed{H(Y)\le I(Y).}
\tag{4.1}
\]

**Proof.** For every output value `y`, let `A_y={z:Y(z)=y}` and `mu_y=Pr(Y=y)`. The cube edge-isoperimetric inequality gives

\[
I(1_{A_y})\ge2\mu_y\log_2\frac1{\mu_y}.
\]

Summing over `y` yields

\[
\sum_y I(1_{A_y})\ge2H(Y).
\]

For a fixed coordinate edge, if `Y` is unchanged then no fiber indicator changes; if `Y` changes, exactly two fiber indicators change. Therefore

\[
\sum_y I(1_{A_y})=2I(Y),
\]

which proves (4.1). `QED`

This lemma is all-dimensional and has no alphabet-size term.

## 5. Application to the source-frontier character label: Shannon cost becomes actual mixed curvature

Return to the account04/B13 source-frontier situation. For each surviving robust source row `r`, write

\[
Q_r=\{z_{F_r}=a_r\},
\qquad s_r=\mu(Q_r)=2^{-|F_r|},
\]
\[
E_r=\{D_r f\ne0\},
\qquad j_r=\mu(E_r),
\qquad e_r=\mu(E_r\triangle Q_r).
\]

Assume the established robust regime

\[
e_r\le\delta j_r,
\qquad 0\le\delta<\frac12.
\tag{5.1}
\]

Let

\[
T(z)=\{r:q_r(z)=1\},
\qquad q_r=1_{Q_r}.
\]

For `k in F_r`, the proxy indicator flips on exactly a `2s_r` fraction of `k`-edges. Let

\[
p_{rk}:=\operatorname{Inf}_k(1_{E_r}).
\]

The elementary boundary-perturbation inequality gives

\[
p_{rk}\ge2(s_r-e_r).
\tag{5.2}
\]

Also `s_r>=j_r-e_r>=(1-delta)j_r`, so

\[
\frac{e_r}{s_r}\le\frac{\delta}{1-\delta}.
\]
Hence

\[
\boxed{
2s_r\le
\frac{1-\delta}{1-2\delta}\,p_{rk}.
}
\tag{5.3}
\]

Now combine Theorem 4.1 with a union bound only at the *physical edge* level:

\[
\begin{aligned}
H(T)
&\le I(T)\\
&\le\sum_r\sum_{k\in F_r} I_k(q_r)\\
&=\sum_r\sum_{k\in F_r}2s_r\\
&\le
\frac{1-\delta}{1-2\delta}
\sum_r\sum_{k\in F_r}p_{rk}.
\end{aligned}
\tag{5.4}
\]

Using the exact mixed-derivative quantity from the joint proof state,

\[
\kappa_{rk}=p_{rk}+4o_{rk}\ge p_{rk},
\]
we obtain the new bridge

\[
\boxed{
H(T)
\le
\frac{1-\delta}{1-2\delta}
\sum_r\sum_{k\in F_r}\kappa_{rk}.
}
\tag{5.5}
\]

At the current `delta=1/16` integrability scale,

\[
\boxed{
H(T)\le\frac{15}{14}
\sum_r\sum_{k\in F_r}p_{rk}
\le\frac{15}{14}
\sum_r\sum_{k\in F_r}\kappa_{rk}.
}
\tag{5.6}
\]

This is exactly the quantity that the newest account04/B13 report left abstract: **the character-label Shannon entropy is now converted, with a universal constant, into genuine source-to-control mixed Boolean boundary/curvature.** No Fannes term, number of labels, number of variables, or ambient dimension occurs.

### Reciprocal-component refinement

Use the account03/B13 integrability DAG and take one surviving source representative `r` from each reciprocal component `C_r`. Split the proxy controls into the internal reciprocal controls `C_r\{r}` and all remaining external controls.

All members of a reciprocal component have the same proxy density `s_r`. From `|s_r-j_i|<=delta j_i`,

\[
j_i\ge\frac{s_r}{1+\delta}.
\]
Therefore the internal part of the edge-boundary union bound is

\[
2(|C_r|-1)s_r
\le2(1+\delta)\sum_{i\in C_r}j_i.
\tag{5.7}
\]

Summing over disjoint source components and applying (5.3) only to external controls gives

\[
\boxed{
H(T)
\le
2(1+\delta)J(f)
+\frac{1-\delta}{1-2\delta}
\mathcal P_{\rm ext},
}
\tag{5.8}
\]
where

\[
\mathcal P_{\rm ext}
:=
\sum_{r\in S}
\sum_{k\in F_r\setminus C_r}p_{rk}.
\]

At `delta=1/16`,

\[
\boxed{
H(T)\le\frac{17}{8}J(f)+\frac{15}{14}\mathcal P_{\rm ext}.
}
\tag{5.9}
\]

The same statement holds with `p_{rk}` replaced by `kappa_{rk}`. Thus the reciprocal-clique part of the formerly unpaid character entropy is already `O(J)`; the only remaining label bank is the **external/source-to-control mixed boundary**. For robust external targets this is the one-way DAG bank; exceptional targets are retained explicitly rather than silently treated as robust.

## 6. What this changes and what remains open

### Proved this run

1. The complete family of the preceding B13 two-block quadratic cut inequalities is insufficient for FEI: the explicit laws `P_m` satisfy them all with constant at least `128/289` while `H/E|S| -> infinity`.
2. The obstruction is genuinely non-Boolean; the elementary degree/support lemma forces every degree-`d` Boolean function to depend on at most `d 2^{d-1}` coordinates.
3. For **every** finite-valued deterministic label on a uniform cube, `H(label) <= physical total influence(label)`.
4. Applying this to the newest account04/B13 proxy-gauge label converts its unpaid Shannon cost into the exact mixed-boundary bank (5.5), with constant `15/14` at the current robustness scale.
5. After reciprocal-component contraction, the internal character-label entropy is at most `17J/8`; only the external mixed-boundary bank in (5.9) remains.

### Still open

The new theorem does **not** prove that

\[
\mathcal P_{\rm ext}=O(J)
\]

and bounding it crudely by `sum_k d_k` would merely reintroduce the uncontrolled second-factorial spectral moment. The next universal implication must show that this *selected external incidence bank* is absorbed by the existing depth-defect / folded-activation / curvature-refund credits, with nonreuse, or else that a large external bank forces the complementary paid branch.

This is considerably narrower than the prior statement “pay the character-label entropy”: the label entropy itself is no longer mysterious. It is a physical edge-boundary quantity, and in the robust proxy branch it is source-exactly dominated by the same mixed derivative geometry already present in the joint proof network.

**Full FEI remains OPEN / NOT PROVED.**

## 7. Handoff

`consumed_peer_artifact`:
- `account04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md` (primary, used to identify and instantiate `T(z)`);
- `account03/B13/20260921T203308Z-integrability-dag/REPORT.md` (used only for the reciprocal-component refinement).

`applied_to_claim`: equations (5.5)--(5.9), converting proxy character-label Shannon entropy into mixed physical boundary/curvature and isolating the sole external incidence bank.

`remaining_implication`: pay `P_ext` dimension-freely by existing defect/activation/refund resources without replacing it by the raw second moment.

`next_recipients`: account04/B13 and account04/B18 for mixed-curvature/phase integration; account01/B18 for the crossing/refund compiler.
