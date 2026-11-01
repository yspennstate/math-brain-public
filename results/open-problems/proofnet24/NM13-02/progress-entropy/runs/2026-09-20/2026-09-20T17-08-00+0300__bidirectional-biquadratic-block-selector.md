Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** No authenticated GPT-6 / maximum-effort metadata is exposed in this runtime.

# NM13-02 T01 — bidirectional transverse block selection and biquadratic-section hereditary FEI

## 0. Parent scope/bound versus demonstrated mechanism gain

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Unrestricted universal finite constant before -> after:** **UNKNOWN -> UNKNOWN**.

No finite-dimensional check, fresh-control theorem, or restricted section theorem below is promoted to full FEI.

**New mechanism.** P03's newest report leaves the full-scope obstruction as **universal section certification / proper block selection for hereditary allocation**, with a structure-sensitive block selector or a summable projected-recombination rebate on signed-translation-rigid connected cores as the next attack. This run proves a two-sided paid block selector. If a physical partition `A sqcup Y` has direct FEI control on all transverse sections and hereditary control on the opposite sections in **both orientations**, then one may choose which block to query first and average the two possible coefficient profiles. In the symmetric case, if every transverse section has direct constant `C` and hereditary constant `K`, then

\[
\boxed{
R_{\mathcal T}(f)
\le \frac{C+K+2/\ln2}{2}\,I(f).
}
\tag{0.1}
\]

The proof is fresh-variable-free and does not require orthogonality or branch independence. The particular projected-recombination estimate needed from P03 is rederived below from Jensen–Shannon/Hellinger contraction, so the new theorem does not assume the peer report is already certified.

Applying (0.1) with the preserved exact quadratic section constants `C=2`, `K=1` gives a new all-dimensional hereditary class. If the ANF phase polynomial admits a bipartition for which every monomial has at most two variables in each side (block bidegree at most `(2,2)`), then

\[
\boxed{
R_{\mathcal T}(f)
\le \left(\frac32+\frac1{\ln2}\right)I(f)
=2.942695040888963\ldots\,I(f).
}
\tag{0.2}
\]

The same class satisfies the independent direct estimate

\[
\boxed{
H(\widehat f^{\,2})
\le \left(2+\frac2{\ln2}\right)I(f)
=4.885390081777927\ldots\,I(f).
}
\tag{0.3}
\]

This class includes connected degree-four cores and is stable under an **arbitrary global quadratic twist**.

For the explicit quartic cycle

\[
P_d(a,y)=\sum_{j\in\mathbb Z/d\mathbb Z}a_ja_{j+1}y_jy_{j+1},
\qquad d\ge3,
\tag{0.4}
\]

and every quadratic polynomial `q(a,y)`, the phase `(-1)^{P_d+q}` is signed-translation-rigid, its degree-4 interaction hypergraph is one connected component with minimum vertex cover `ceil(d/2)`, yet (0.2)-(0.3) hold uniformly in `d` and in the quadratic twist. Thus a genuinely large, signed-rigid connected core admits the proper block selector requested by P03, without a separator-depth penalty.

---

## 1. Current dependencies and compact handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

Newest P03 substantive report consumed for the **statement of the live obstruction only**:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T16-28-06+0300__fei-transverse-section-recombination.md`, creation commit `e95768c9f04ed33f3ebb4f58e6160b823bbb83d3`, blob `c56efdc0fbb65e6c481cd0a9928812c043930235`.

It proves a projected recombination telescope and records

`remaining_obstruction: universal section certification / proper block selection for hereditary allocation`

with the next attack `structure-sensitive block selector or summable projected-recombination rebate on signed-translation-rigid connected cores`. Those are P03 peer claims pending later independent review. The local projected-recombination inequality needed here is reproved in Sections 3-4.

Immediately preceding NM13-02 substantive report:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T16-08-00+0300__multiway-orthogonal-label-splicing.md`, creation commit `8a11e68b663e81f3ec270f72786ff94b7c4d6486`, blob `ce62f121f6b8324009ff47ffa0afdd28ee18f50a`.

It pays an arbitrary finite orthogonal-label partition once by a physical label boundary and proves a `9/5` hereditary bound for a connected cubic cycle. The present run removes the spectral-orthogonality hypothesis on a different structural class by using two-sided section certification rather than label factorization.

Preserved earlier NM13-02 mathematics used here:

1. **Complete physical block compression** (`2026-09-20T15-08-00+0300__block-compression-balanced-controller.md`, blob `c155fb1d672bfe9858463391f2db0d15c5b5559d`): every complete adaptive physical `A`-prefix satisfies
   \[
   R_{\mathcal T_A}(f)\le B_A(f):=H(S_A\mid S_{A^c}),
   \qquad Q_{\mathcal T_A}=I_A(f).
   \tag{1.1}
   \]
2. **Exact quadratic-rank hereditary telescope** (`2026-09-20T03-10-31+0300__quadratic-rank-hereditary-allocation.md`): for every quadratic phase with polar rank `r`, every full physical restriction tree has allocation `r/2`, hence
   \[
   R_{\mathcal T}(f)=r/2\le I(f).
   \tag{1.2}
   \]
   The same report proves the squared Fourier law is uniform on an affine coset of size `2^r`, so `H(f)=r`.
3. Exact influence budgets and max-splicing, one-point quadratic defects, descendant-influence and variance-paid separators, quadratic-normalized Wiener control, affine-flat classes, guarded selectors, oblique-derivative payments, character-child cross-fibre rescue, and the complete-block theorem remain preserved.

Restricted fresh-control results remain restricted: they append variables and do not settle fixed-domain FEI. Retired false routes remain retired: the false pointwise erasure converse, fixed-coefficient affine drift, all-coordinate absolute-overlap selector, derivative-degree scalar schedule, blind root-curvature payment, fixed-`s<2` Renyi payment, frozen-parent endpoint payment, marginal-entropy substitution, and arbitrary orthogonal-involution relaxation.

### Primary-source status checked 20 September 2026

González–MacManus–Pereyra, arXiv:2606.00246v2, submitted 29 May 2026 and last revised 9 June 2026, still states universal FEI as a conjecture. Its restriction inequality would imply full FEI if it held universally; the paper proves restricted stopping-tree classes. Li–Han, arXiv:2512.03117, submitted 2 December 2025, strengthens Han's general inequality but retains the coordinate-profile correction `sum_i I_i log(1/I_i)` rather than a universal `C I(f)` bound. A bounded fresh search did not recover a source-matching universal resolution. Publication priority for the theorem below is **UNVERIFIED**.

---

## 2. Definitions

Let `f:{-1,1}^{A sqcup Y}->{-1,1}`. Let `S=(S_A,S_Y)` be the spectral random set with

\[
\Pr[S=T]=\widehat f(T)^2.
\]

Write

\[
I_A(f)=\sum_{i\in A}\operatorname{Inf}_i(f),
\qquad
I_Y(f)=\sum_{j\in Y}\operatorname{Inf}_j(f).
\tag{2.1}
\]

For a physical section `y` of `Y`, let `f_y` denote the Boolean function remaining on `A`; similarly `f_a` is the section on `Y` after fixing `A`.

The hereditary allocation at a one-coordinate physical query `i` is

\[
B_i(f)=H(S_i\mid S_{[n]\setminus\{i\}}),
\]

and the allocation of a full restriction tree is the physical-cylinder weighted sum of these node costs.

Put

\[
\rho:=\frac2{\ln2}=2.8853900817779268\ldots .
\tag{2.2}
\]

---

## 3. A self-contained sharp projected recombination payment

The newest P03 report contains the same projected telescope. Since that report is a peer dependency rather than an independently certified theorem, this section rederives exactly the estimate used below.

### Lemma 3.1 — Jensen–Shannon is paid by Hellinger square

For probability laws `P,Q` on a finite set, with base-2 Jensen–Shannon divergence,

\[
\boxed{
\operatorname{JS}_2(P,Q)
\le \frac1{\ln2}\left(1-\sum_x\sqrt{P_xQ_x}\right).
}
\tag{3.1}
\]

### Proof

It suffices to prove the scalar natural-log inequality

\[
\frac12\left[a\ln\frac{2a}{a+b}+b\ln\frac{2b}{a+b}\right]
\le \frac12(\sqrt a-\sqrt b)^2
\tag{3.2}
\]

for `a,b>=0`, and then sum and divide by `ln 2`.

For `s=a+b>0`, put `t=|a-b|/s in [0,1]`. After dividing by `s/4`, (3.2) is equivalent to

\[
(1+t)\ln(1+t)+(1-t)\ln(1-t)
\le2\left(1-\sqrt{1-t^2}\right).
\tag{3.3}
\]

Let the right side minus left side be `F(t)`. Then `F(0)=0` and

\[
F'(t)=2\left(\frac{t}{\sqrt{1-t^2}}-\operatorname{artanh}t\right).
\]

For

\[
g(t)=\frac{t}{\sqrt{1-t^2}}-\operatorname{artanh}t,
\]

we have `g(0)=0` and

\[
g'(t)=\frac{1-\sqrt{1-t^2}}{(1-t^2)^{3/2}}\ge0.
\]

Thus `F'(t)>=0`, and (3.3) follows; the endpoint `t=1` follows by continuity. Summing (3.2) gives (3.1). QED.

### Lemma 3.2 — one physical split

Let a physical coordinate `i` split a Boolean parent into children `g,h`, and let `P,Q` be their squared Fourier laws. Put

\[
j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\]

Then

\[
\boxed{
\operatorname{JS}_2(P,Q)\le \rho\,j_i(f).
}
\tag{3.4}
\]

### Proof

The Hellinger affinity is

\[
A(P,Q)=\sum_T\sqrt{P_TQ_T}
=\sum_T|\widehat g(T)\widehat h(T)|.
\]

By the triangle inequality and Parseval,

\[
A(P,Q)\ge\left|\sum_T\widehat g(T)\widehat h(T)\right|
=|\langle g,h\rangle|.
\tag{3.5}
\]

For Boolean children,

\[
\langle g,h\rangle=1-2\operatorname{Inf}_i(f).
\]

Hence

\[
1-A(P,Q)
\le1-|1-2\operatorname{Inf}_i(f)|
=2j_i(f).
\]

Apply Lemma 3.1. QED.

The coefficient `rho=2/ln2` is the same sharp coefficient reported by P03, but sharpness is not needed below.

---

## 4. Projected transverse section inequality

### Proposition 4.1
For every partition `A sqcup Y`,

\[
\boxed{
H(S_A)
\le \mathbb E_y H(\widehat{f_y}^{\,2})+\rho I_Y(f).
}
\tag{4.1}
\]

The symmetric statement with `A,Y` interchanged also holds.

### Proof

Physically reveal all coordinates of `Y` in any complete adaptive order. At a node querying `i in Y`, let the child squared spectra be `P,Q` and let `P_A,Q_A` be their marginals on the still-unqueried spectral block `A`.

For each residual Fourier label `T`, write the two parent fibre coefficients as

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}).
\]

The child coefficients are `u_T+v_T` and `u_T-v_T`, so

\[
\frac12(u_T+v_T)^2+\frac12(u_T-v_T)^2=u_T^2+v_T^2.
\tag{4.2}
\]

Thus the parent spectral law after forgetting `S_i` is the equal mixture of the two child spectral laws. After marginalizing to `A`, the one-step decrement of the `A`-marginal entropy is exactly

\[
\operatorname{JS}_2(P_A,Q_A).
\tag{4.3}
\]

Jensen–Shannon divergence contracts under marginalization, so

\[
\operatorname{JS}_2(P_A,Q_A)\le\operatorname{JS}_2(P,Q)\le\rho j_i(f_v)
\tag{4.4}
\]

by Lemma 3.2 at the current node `v`.

Summing (4.3) over the complete `Y`-prefix telescopes exactly:

\[
H(S_A)=\mathbb E_yH(\widehat{f_y}^{\,2})
 +\sum_vw_v\operatorname{JS}_2((P_v)_A,(Q_v)_A).
\tag{4.5}
\]

Since `j_i<=Inf_i` and the nodes querying each physical coordinate partition the original edges of that coordinate,

\[
\sum_vw_vj_{i(v)}(f_v)
\le\sum_vw_v\operatorname{Inf}_{i(v)}(f_v)
=I_Y(f).
\tag{4.6}
\]

Combining (4.4)-(4.6) gives (4.1). QED.

This is the exact P03 mechanism needed here, independently checked rather than assumed.

---

## 5. New bidirectional hereditary block selector

### Theorem 5.1
Let `f` live on `A sqcup Y`. Suppose the following four uniform section certificates hold:

1. every `Y`-section `f_y` on `A` satisfies
   \[
   H(f_y)\le C_A I(f_y);
   \tag{5.1}
   \]
2. every `A`-section `f_a` on `Y` has a full hereditary tree with
   \[
   R(f_a)\le K_Y I(f_a);
   \tag{5.2}
   \]
3. every `A`-section `f_a` on `Y` satisfies
   \[
   H(f_a)\le C_Y I(f_a);
   \tag{5.3}
   \]
4. every `Y`-section `f_y` on `A` has a full hereditary tree with
   \[
   R(f_y)\le K_A I(f_y).
   \tag{5.4}
   \]

Then there is a full physical restriction tree satisfying

\[
\boxed{
R_{\mathcal T}(f)
\le\min\left\{
C_A I_A(f)+(K_Y+\rho)I_Y(f),
(K_A+\rho)I_A(f)+C_Y I_Y(f)
\right\}.
}
\tag{5.5}
\]

In the symmetric case `C_A=C_Y=C` and `K_A=K_Y=K`,

\[
\boxed{
R_{\mathcal T}(f)
\le\frac{C+K+\rho}{2}I(f).
}
\tag{5.6}
\]

### Proof

**Query `A` first.** By the preserved complete-block compression theorem,

\[
R_{\mathcal T_A}(f)
\le H(S_A\mid S_Y)\le H(S_A).
\tag{5.7}
\]

Proposition 4.1 and (5.1) give

\[
H(S_A)
\le \mathbb E_yH(f_y)+\rho I_Y(f)
\le C_A\mathbb E_y I(f_y)+\rho I_Y(f).
\]

Averaging physical `Y`-sections preserves the `A`-edge budget, so

\[
\mathbb E_y I(f_y)=I_A(f).
\]

Hence the entire `A`-prefix costs at most

\[
C_AI_A(f)+\rho I_Y(f).
\tag{5.8}
\]

After `A` is fixed, graft the hereditary trees (5.2). Averaging over `a` preserves the `Y`-edge budget:

\[
\mathbb E_a I(f_a)=I_Y(f).
\]

Thus this orientation gives

\[
R\le C_AI_A+(K_Y+\rho)I_Y.
\tag{5.9}
\]

Interchanging `A,Y` gives the second expression in (5.5). Choose the cheaper orientation.

For the symmetric case, the two candidate bounds sum to

\[
(C+K+\rho)(I_A+I_Y)=(C+K+\rho)I(f).
\]

The smaller of two numbers is at most their average, proving (5.6). QED.

### Direct entropy companion

Under only the symmetric direct section hypothesis `H(section)<=C I(section)` in both orientations, Proposition 4.1 gives

\[
H(S_A)\le CI_A+\rho I_Y,
\qquad
H(S_Y)\le CI_Y+\rho I_A.
\]

Subadditivity of Shannon entropy yields

\[
\boxed{
H(S_A,S_Y)\le(C+\rho)I(f).
}
\tag{5.10}
\]

This direct theorem is separate from the hereditary certificate (5.6).

**Mechanism interpretation.** The selector does not require guessing in advance which side carries the influence. If one orientation would place the expensive recombination-plus-leaf coefficient on most of the influence, the opposite orientation swaps the coefficient profile. The min of the two physical trees is therefore paid by the arithmetic mean of the two section constants. This is a genuine proper-block selection rule, not a whole-cube restatement.

---

## 6. Quadratic sections: exact constants needed by the selector

For completeness, the two quadratic constants used below are recalled with their proof content.

Let `g=(-1)^q` be a quadratic phase, let `M_q` be its alternating polar matrix over `F_2`, and let `r=rank(M_q)`.

The preserved quadratic-rank theorem proves that the squared Fourier law is uniform on an affine coset of `im M_q`, hence

\[
H(g)=r.
\tag{6.1}
\]

If `d` is the number of nonzero rows of `M_q` and `h` is the number of zero polar rows with nonzero linear derivative, then

\[
I(g)=d/2+h.
\tag{6.2}
\]

Since `r<=d`,

\[
\boxed{H(g)\le2I(g).}
\tag{6.3}
\]

The same prior theorem proves that on every full physical restriction tree the hereditary allocation is exactly `r/2`; therefore

\[
\boxed{R(g)=r/2\le I(g).}
\tag{6.4}
\]

So quadratic sections have the symmetric constants

\[
C=2,\qquad K=1.
\tag{6.5}
\]

---

## 7. Bidegree-(2,2) ANF theorem

Represent a Boolean sign function as

\[
f(x)=(-1)^{P(x)},
\]

where `P` is its unique algebraic normal form over `F_2`. Let `[n]=A sqcup Y`.

### Definition 7.1
`P` has **block bidegree at most `(2,2)`** if every ANF monomial `m` satisfies

\[
|m\cap A|\le2,
\qquad
|m\cap Y|\le2.
\tag{7.1}
\]

Equivalently, after fixing either block, the phase polynomial on the other block is quadratic.

### Theorem 7.2 — hereditary biquadratic-section selector
If `P` has block bidegree at most `(2,2)` for some nontrivial physical partition `A sqcup Y`, then `f=(-1)^P` has a full physical restriction tree with

\[
\boxed{
R_{\mathcal T}(f)
\le\left(\frac32+\frac1{\ln2}\right)I(f).
}
\tag{7.2}
\]

Moreover

\[
\boxed{
H(\widehat f^{\,2})
\le\left(2+\frac2{\ln2}\right)I(f).
}
\tag{7.3}
\]

Both constants are independent of the dimension, the sizes of the blocks, the number of quartic monomials, and all lower-degree quadratic couplings.

### Proof
Every `Y`-section on `A` is a quadratic phase, and every `A`-section on `Y` is a quadratic phase. Thus Section 6 supplies `C=2`, `K=1` in both orientations. Theorem 5.1 gives

\[
R\le\frac{2+1+2/\ln2}{2}I
=\left(\frac32+\frac1{\ln2}\right)I,
\]

proving (7.2). The direct companion (5.10) gives (7.3). QED.

### Structural scope

The class is restriction-closed. It contains arbitrary degree-3 monomials that meet both colors, arbitrary degree-4 monomials split `2+2`, and arbitrary lower-degree terms. In particular, multiplying by any arbitrary quadratic phase preserves the hypothesis.

This is a proper-block theorem: neither block need be bounded in size, and the proof never queries the whole cube merely to restate `H<=H`.

---

## 8. Application to P03's signed-rigid connected-core obstruction

For `d>=3`, take two `d`-coordinate blocks

\[
A=\{a_0,\dots,a_{d-1}\},
\qquad
Y=\{y_0,\dots,y_{d-1}\},
\]

with indices modulo `d`, and define

\[
P_d(a,y)=\sum_{j=0}^{d-1}a_ja_{j+1}y_jy_{j+1}.
\tag{8.1}
\]

Let `q(a,y)` be an **arbitrary quadratic polynomial**, with arbitrary cross-block quadratic couplings, and set

\[
f_{d,q}=(-1)^{P_d+q}.
\tag{8.2}
\]

### Proposition 8.1 — one connected quartic core with unbounded separator size
The degree-4 ANF hyperedges are

\[
E_j=\{a_j,a_{j+1},y_j,y_{j+1}\}.
\]

Adjacent edges share the pair `{a_{j+1},y_{j+1}}`, so the degree-`>=3` interaction hypergraph is one connected component.

Every physical variable occurs in at most two of these quartic edges. Hence every vertex cover has size at least `ceil(d/2)`. Taking alternating `a_j` variables gives a cover of exactly that size. Therefore

\[
\boxed{\tau(P_d)=\lceil d/2\rceil.}
\tag{8.3}
\]

So the family is not a bounded-hitting-set or one-hub artifact.

### Proposition 8.2 — signed-translation rigidity survives every quadratic twist
For every quadratic `q`, the only translation `t` satisfying

\[
f_{d,q}(x+t)=\pm f_{d,q}(x)
\]

for all `x` is `t=0`.

### Proof
Write the translation as `t=(alpha,beta)` on the two blocks. A signed translation symmetry is equivalent to the Boolean derivative

\[
\Delta_t(P_d+q)(x)=(P_d+q)(x+t)+(P_d+q)(x)
\]

being constant.

Because `q` is quadratic, `Delta_t q` has degree at most one. The homogeneous cubic part of `Delta_t P_d` is

\[
\sum_j\Big[
\alpha_j a_{j+1}y_jy_{j+1}
+\alpha_{j+1}a_jy_jy_{j+1}
+\beta_j a_ja_{j+1}y_{j+1}
+\beta_{j+1}a_ja_{j+1}y_j
\Big].
\tag{8.4}
\]

Each displayed cubic monomial is unique to its indicated translation coefficient: terms involving one `a` and two adjacent `y`'s cannot cancel terms involving two `a`'s and one `y`, and within each type the cyclic supports are distinct for `d>=3`. If the derivative were constant, its cubic part would vanish, forcing every `alpha_j=beta_j=0`. Hence `t=0`. QED.

### Theorem 8.3 — uniform hereditary and direct FEI bounds on the rigid quartic cycle
For every `d>=3` and every quadratic twist `q`,

\[
\boxed{
R_{\mathcal T}(f_{d,q})
\le\left(\frac32+\frac1{\ln2}\right)I(f_{d,q}),
}
\tag{8.5}
\]

and

\[
\boxed{
H(\widehat{f_{d,q}}^{\,2})
\le\left(2+\frac2{\ln2}\right)I(f_{d,q}).
}
\tag{8.6}
\]

### Proof
Every quartic monomial in `P_d` contains exactly two variables from `A` and two from `Y`, while every monomial of the arbitrary quadratic twist automatically satisfies the `(2,2)` bidegree condition. Apply Theorem 7.2. QED.

This is the promised application to P03's current obstruction: a **proper physical block** certifies a signed-translation-rigid, single-connected, unbounded-separator core, and the direction is chosen by the actual block influence split rather than by a fresh variable, a root scalar, or a recursively accumulated selector surcharge.

### Untwisted influence scale
For `q=0`, every coordinate has influence `3/16`. For example,

\[
\partial_{a_k}P_d
=y_k\big(a_{k-1}y_{k-1}+a_{k+1}y_{k+1}\big).
\]

The two products inside the parentheses are independent Bernoulli variables of density `1/4`, so their XOR has density `3/8`; multiplying by the independent bit `y_k` gives `3/16`. The same computation holds for every `y_k`. Therefore

\[
\boxed{I((-1)^{P_d})=\frac{3d}{8}.}
\tag{8.7}
\]

The hereditary certificate is consequently linear in the true influence although the core degree is four, the component size is `2d`, and its minimum separator size grows like `d/2`.

---

## 9. What failed and what remains

The theorem does **not** produce a universal proper block. Its combinatorial hypothesis can fail already for very small quartic hypergraphs.

For example, take five variables and include all five quartic monomials supported on the four-subsets of the five variables, i.e. the complete `4`-uniform hypergraph `K_5^{(4)}`. There is no bipartition for which every quartic edge has a `2+2` split: if a coloring has `k` red vertices, omitting a red vertex would require `k-1=2`, while omitting a blue vertex would require `k=2`; with both colors present these conditions are incompatible. Thus the immediate attempt to turn Theorem 7.2 into a universal degree-four result fails for a concrete structural reason.

Likewise, (5.5) still requires section certificates in both orientations. An arbitrary signed-rigid connected core may have hard sections on every proper cut, and nothing here proves a universal way to avoid that.

This is therefore a genuine restricted hereditary theorem, not full FEI. The parent scope and universal constant are unchanged.

**Next nonredundant attack.** Replace a single exact `(2,2)` partition by a **fractional/multi-block selector**: seek a bounded family or distribution of physical cuts so that every high-degree interaction is balanced on enough cuts, while each physical coordinate's influence is charged only boundedly many times. The target is an averaged version of (5.5) whose projected-recombination surcharges telescope against a fractional cut potential. The `K_5^{(4)}` obstruction above is the first test: a successful multi-cut theorem should cover it without assuming one balanced bipartition. If that fails, construct the smallest core for which every useful transverse section family remains hard and quantify the missing rebate.

---

## 10. Executed sanity checker

Executed code:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T17-08-00+0300__bidirectional_biquadratic_selector_check.py`

Creation commit `18d20f4c9c15abe7dd381a09d2e87ecb3c7cb5df`; readback blob `2023fe0a19f5ea5209333523384cc07d8ecf00af`.

Archived actual output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T17-08-00+0300__bidirectional_biquadratic_selector_check.out`

Creation commit `5a82137f57b4ac67493c8e98339b8ddc7030b71b`; readback blob `2b9b72bfd8963da6ecad74976803d8c3b24ee782`.

The executed checker returned `PASS`. It performed:

1. all `65,812` ordered Boolean child pairs through residual dimension three, with maximum violation of `JS <= (2/ln2) j` equal to `0.0`;
2. all `32,767` nonconstant four-variable Boolean functions modulo global sign, using the two `2+2` block orders, with zero violations of the new hereditary constant and maximum observed `min(R_A,R_Y)/I = 1.826623093714895`;
3. `200` deterministic random `3+3` bidegree-`(2,2)` phases, with zero violations and maximum observed ratio `1.0590291000571317`;
4. the untwisted quartic cycle at `d=3,4`, verifying `I=3d/8` and no nontrivial signed translation;
5. `100` deterministic quadratic twists at `d=3` and `40` at `d=4`, with zero hereditary-bound failures and zero signed-rigidity failures;
6. a `20,001`-point scalar check of the Jensen–Shannon/Hellinger inequality, with maximum numerical residual `1.27e-16`.

These computations are sanity checks only. The theorem arguments above are all-dimensional and analytic.

---

## ledger_delta

```yaml
ledger_delta:
  worker: NM13-02
  parent: T01_Friedgut_Kalai_FEI
  date: 2026-09-20
  model: GPT-5.6_Sol
  reasoning_level: UNVERIFIED
  parent_scope_before: OPEN
  parent_scope_after: OPEN
  universal_finite_constant_before: UNKNOWN
  universal_finite_constant_after: UNKNOWN
  mechanism_gain:
    - bidirectional_transverse_hereditary_selector:
        statement: "R <= min{C_A I_A+(K_Y+2/ln2)I_Y, (K_A+2/ln2)I_A+C_Y I_Y}"
        proof_status: PROVED
        fresh_controls: false
    - symmetric_selector:
        statement: "R <= (C+K+2/ln2)/2 * I"
        proof_status: PROVED
    - bidegree_2_2_phase_class:
        hereditary_constant: "3/2 + 1/ln2 = 2.942695040888963..."
        direct_FEI_constant: "2 + 2/ln2 = 4.885390081777927..."
        proof_status: PROVED_RESTRICTED
    - quartic_cycle_quadratic_twists:
        scope: "all d>=3, arbitrary quadratic q"
        connected_high_degree_core: true
        signed_translation_rigid: true
        min_vertex_cover: "ceil(d/2)"
        proof_status: PROVED_RESTRICTED
  p03_precise_obstruction_consumed:
    report: "proofnet24/P03-fei/runs/2026-09-20/2026-09-20T16-28-06+0300__fei-transverse-section-recombination.md"
    obstruction: "universal section certification / proper block selection for hereditary allocation"
    peer_claim_assumed_established: false
    note: "required projected recombination estimate independently rederived"
  preserved_history:
    quadratic_rank_telescope: true
    complete_block_compression: true
    fresh_control_results_remain_restricted: true
    false_lemma_corrections_preserved: true
  failed_strengthening:
    - "one exact (2,2) bipartition is not universal; K5^(4) has no such balanced cut"
    - "arbitrary signed-rigid connected cores may have hard sections on every proper cut"
  remaining_obstruction: "universal or fractional proper-block selector with summable projected-recombination rebate"
  next_attack: "fractional/multi-block balanced-cut potential, first stress-tested on K5^(4)"
  checker:
    code_commit: 18d20f4c9c15abe7dd381a09d2e87ecb3c7cb5df
    code_blob: 2023fe0a19f5ea5209333523384cc07d8ecf00af
    output_commit: 5a82137f57b4ac67493c8e98339b8ddc7030b71b
    output_blob: 2b9b72bfd8963da6ecad74976803d8c3b24ee782
    status: PASS
  independent_review: PENDING
  full_FEI_claim: false
```
