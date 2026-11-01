Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** No authenticated GPT-6 / maximum-effort runtime metadata is exposed here.

# NM13-02 T01 — spectral-TV hereditary recombination, toggle-compatible branches, and a finite-field unequal-spectrum splice

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI): prove a universal finite constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Unrestricted universal finite constant before -> after:** **UNKNOWN -> UNKNOWN**.

No finite-dimensional check, restricted fresh-control theorem, lattice theorem, flat-tail theorem, or branch-compatibility theorem below is promoted to full FEI.

**Newest P03 obstruction actually addressed.** The newest P03 handoff read in this run is

`proofnet24/P03-fei/continuations/2026-09-20-flat-tail-and-arithmetic-drift/HANDOFF.md`

from commit `33571041414a0b61c90e988dabccf5df5946d448`. It reports a direct FEI theorem for a spectrum with one arbitrary exceptional coefficient and a common flat tail, a `6+log2(R+1)` theorem for finitely many exceptional frequencies, and several exact failures of proposed arithmetic-remainder selectors. In particular, prescribed-coordinate arithmetic payment fails exponentially, the proposed global coefficient two for the arithmetic remainder fails on the known NAND27 example, the earlier small-cube existential selector coefficient fails on NAND27, and symmetric thresholds give much larger all-coordinate arithmetic charges. These are **not** FEI counterexamples. P03 leaves arbitrary unequal Fourier weights as the live universal obligation.

This run attacks the missing **dependent-branch recombination** step between such direct leaf certificates. The main new result is a universal one-step inequality

\[
\boxed{B_i(f)\le \operatorname{TV}(P_i^+,P_i^-),}
\]

where `P_i^+,P_i^-` are the squared Fourier laws of the two physical children. On a broad `toggle-compatible` two-hard-child geometry this becomes the exact linear Hellinger payment

\[
\boxed{B_i(f)=2M_i(f)\le 2j_i(f),}
\]

and if compatibility fails on at most one Fourier fibre it still gives

\[
\boxed{B_i(f)\le4M_i(f)\le4j_i(f).}
\]

This yields a constant-preserving hereditary splice with no depth penalty. The mechanism is then applied unconditionally to a new all-dimensional finite-field selector family whose **children have one exceptional coefficient plus a flat tail but whose parent has two distinct nontrivial tail magnitudes**. The resulting physical tree has hereditary coefficient `8/3`, while the newest P03 generic few-exception sufficient coefficient applied at the parent grows like `3m+6`. This compares sufficient certificates; it does not claim P03 has no other sharper representation of the parent.

---

## 1. Current dependencies and compact NM13-02 handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

The newest own substantive report preserved is

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T18-08-00+0300__hereditary-dependency-bank-prefix-routing.md`,

creation commit `e23471d1b49930f4f23d0458e39f68933d3338b6`. It proves a banked hereditary partition-tree inequality and influence-profile prefix routing. Earlier NM13-02 mathematics remains preserved with its hypotheses: exact quadratic-rank allocation; one- and two-affine-flat classes; decision-tree/nested-spine certificates; variance-paid separators; quadratic-normalized Wiener control; guarded derivative selectors; oblique derivative payment; character-child cross-fibre payment; complete physical-block compression; multiway orthogonal-label splicing; bidirectional biquadratic block selectors.

The one prior fact used essentially below is the already proved **complete-block compression**: if `h` is any Boolean function, querying all its physical coordinates gives a full restriction tree with

\[
R(h)\le H(\widehat h^{\,2}).
\tag{1.1}
\]

Thus a direct FEI certificate on a leaf can be converted into a hereditary leaf certificate without assuming restriction closure.

The restricted fresh-control theorem remains restricted to appended controls and is not a fixed-domain proof of FEI. The false pointwise-erasure converse, fixed-coefficient affine-drift route, all-coordinate absolute-overlap selector, derivative-degree scalar schedule, blind curvature payment, fixed-`s<2` Renyi payment, frozen-parent endpoint payment, marginal-entropy substitution, arbitrary orthogonal-involution relaxation, and the newest false arithmetic-selector constants are not revived.

### Primary-source status checked in this run

A fresh primary-source lookup on 20 September 2026 found González--MacManus--Pereyra, arXiv:2606.00246, still stating universal FEI as a conjecture and explaining that their restriction inequality would imply full FEI if it held for all Boolean functions. Li--Han, arXiv:2512.03117, still proves the strengthened general estimate with the additional coordinate-profile term `sum_i I_i log(1/I_i)` and sharp constants one; it is not a universal `C I(f)` theorem. Publication priority for the new lemmas below is **UNVERIFIED**.

P03's new flat-tail theorem is treated as a **peer report pending later independent review**. The unconditional finite-field application below rederives the child spectrum and the needed direct `8/3` entropy bound, so it does not rely on P03's reported proof.

---

## 2. One physical split and the allocation fibre formula

Let

\[
f:\{-1,1\}^{\{i\}\cup U}\to\{-1,1\}
\]

and let `g,h` be the two restrictions obtained by fixing the physical coordinate `i`. For every residual Fourier label `T subset U`, write

\[
u_T=\widehat g(T),\qquad v_T=\widehat h(T),\qquad
x_T=|u_T|,\qquad y_T=|v_T|.
\]

The parent coefficients in the corresponding Fourier fibre are

\[
\widehat f(T)=\frac{u_T+v_T}{2},\qquad
\widehat f(T\cup\{i\})=\frac{u_T-v_T}{2}.
\tag{2.1}
\]

Let `S` denote the random Fourier subset of the parent, distributed by squared Fourier mass. The hereditary allocation at this split is

\[
B_i(f)=H(S_i\mid S_U).
\]

For a fixed residual label with `x_T^2+y_T^2>0`, binary-entropy symmetry removes the relative sign of `u_T,v_T`, giving

\[
B_i(f)=\sum_T\Phi(x_T,y_T),
\tag{2.2}
\]

where

\[
\Phi(x,y)
=\frac{x^2+y^2}{2}\,
 h_2\!\left(\frac{(x-y)^2}{2(x^2+y^2)}\right),
\qquad \Phi(0,0)=0.
\tag{2.3}
\]

The two child squared Fourier laws are

\[
P_T=x_T^2,\qquad Q_T=y_T^2,
\tag{2.4}
\]

and both have total mass one.

---

## 3. Scalar lemma and the universal spectral-TV allocation bound

### Lemma 3.1

For `0<=p<=1/2`,

\[
\boxed{h_2(p)\le2\sqrt{p(1-p)}.}
\tag{3.1}
\]

#### Proof

Put

\[
t=\sqrt{\frac p{1-p}}\in[0,1],\qquad p=\frac{t^2}{1+t^2}.
\]

After multiplying (3.1) by `(1+t^2) ln 2`, it is equivalent to `F(t)>=0`, where

\[
F(t)=2t\ln2-(1+t^2)\ln(1+t^2)+2t^2\ln t
\tag{3.2}
\]

with the continuous convention `t^2 ln t=0` at zero. We have `F(0)=F(1)=0`. Moreover

\[
F'(t)=2g(t),\qquad
g(t)=\ln2+t\ln\frac{t^2}{1+t^2},
\]

\[
g'(t)=\ln\frac{t^2}{1+t^2}+\frac2{1+t^2},
\qquad
g''(t)=\frac{2(1-t^2)}{t(1+t^2)^2}\ge0.
\tag{3.3}
\]

Thus `g'` is increasing, from `-infinity` as `t downarrow 0` to `1-ln2>0` at `t=1`. Hence `g` first decreases and then increases. Also `g(0+)=ln2>0`, `g(1)=0`, and because `g'(1)>0`, `g(t)<0` just to the left of one. Therefore `g` has exactly one interior zero, changing from positive to negative, and then increases back to zero at the endpoint. Consequently `F` first increases and then decreases between its two zero endpoints, so `F>=0`. QED.

### Lemma 3.2 — fibre TV bound

For all `x,y>=0`,

\[
\boxed{\Phi(x,y)\le\frac12|x^2-y^2|.}
\tag{3.4}
\]

#### Proof

Assume `x^2+y^2>0` and set

\[
p=\frac{(x-y)^2}{2(x^2+y^2)}\in[0,1/2].
\]

Then

\[
2\sqrt{p(1-p)}
=\frac{|x^2-y^2|}{x^2+y^2}.
\]

Insert Lemma 3.1 into (2.3). QED.

### Theorem 3.3 — universal spectral-TV allocation

For every Boolean function and every physical coordinate split,

\[
\boxed{
B_i(f)\le \operatorname{TV}(P,Q)
:=\frac12\sum_T|P_T-Q_T|.
}
\tag{3.5}
\]

#### Proof

Sum (3.4) over all Fourier fibres and use (2.4). QED.

This theorem is universal, but by itself it is **not** a universal FEI selector: total variation need not be linearly controlled by the physical influence. The point of the next section is that the exact spectral geometry in P03's newest obstruction can force such a linear payment.

---

## 4. Hellinger payment and toggle-compatible branches

Define the child spectral Hellinger defect

\[
M_i(f):=\frac12\left(1-\sum_T\sqrt{P_TQ_T}\right)
       =\frac14\sum_T(x_T-y_T)^2.
\tag{4.1}
\]

Also write

\[
j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\]

By triangle inequality and Parseval,

\[
\sum_Tx_Ty_T
\ge\left|\sum_Tu_Tv_T\right|
=|\langle g,h\rangle|
=|1-2\operatorname{Inf}_i(f)|.
\]

Therefore

\[
\boxed{M_i(f)\le j_i(f).}
\tag{4.2}
\]

### Definition 4.1

The child pair `(g,h)` is **toggle-compatible** if for every residual Fourier label `T`,

\[
x_T=y_T\quad\text{or}\quad x_Ty_T=0.
\tag{4.3}
\]

Thus any fibre on which both children are spectrally present has exactly the same magnitude in the two children; supports may otherwise differ arbitrarily, signs are arbitrary, and the common magnitude may depend on `T`.

### Theorem 4.2 — exact toggle payment

If the two children are toggle-compatible, then

\[
\boxed{
B_i(f)=\operatorname{TV}(P,Q)=2M_i(f)\le2j_i(f).
}
\tag{4.4}
\]

#### Proof

If `x_T=y_T`, then the fibre allocation, TV contribution and squared magnitude difference all vanish. If exactly one magnitude is nonzero, say `(x_T,y_T)=(a,0)`, then

\[
\Phi(a,0)=a^2/2,
\]

while the TV contribution is `a^2/2` and the contribution to `2M_i` is also `a^2/2`. Sum over fibres and use (4.2). QED.

This is a genuinely two-hard-child statement. Neither child need be a character, quadratic, affine-flat sign, or isospectral copy of the other.

### Theorem 4.3 — one exceptional amplitude-drift fibre

Suppose (4.3) holds at every Fourier label except possibly one label `e`. Then

\[
\boxed{
B_i(f)\le\operatorname{TV}(P,Q)\le4M_i(f)\le4j_i(f).
}
\tag{4.5}
\]

#### Proof

Let

\[
W=\sum_{T\ne e}|x_T^2-y_T^2|.
\]

Compatibility off `e` implies

\[
W=\sum_{T\ne e}(x_T-y_T)^2.
\tag{4.6}
\]

Because both child spectral laws have total mass one,

\[
|x_e^2-y_e^2|
=\left|\sum_{T\ne e}(y_T^2-x_T^2)\right|
\le W.
\tag{4.7}
\]

Hence

\[
\operatorname{TV}(P,Q)
=\frac12\left(W+|x_e^2-y_e^2|\right)
\le W.
\tag{4.8}
\]

On the other hand,

\[
M_i(f)=\frac14\left(W+(x_e-y_e)^2\right)\ge W/4.
\tag{4.9}
\]

Combine Theorem 3.3, (4.8), (4.9), and (4.2). QED.

### Corollary 4.4 — the common flat-tail case in P03's newest geometry

If both children have one common exceptional label `e`, and away from `e` every nonzero coefficient in either child has the same common magnitude `a`, then (4.5) applies. Their tail supports and signs may differ arbitrarily. If the exceptional magnitudes also agree, the stronger exact identity (4.4) applies.

This is the direct complementary recombination statement needed for the corresponding part of P03's newest one-exception/flat-tail theorem. If the two child tail magnitudes themselves differ, then every common tail-support frequency becomes an amplitude-drift fibre and Theorem 4.3 no longer applies; that extension remains **UNPROVED**.

---

## 5. Constant-preserving dependent-branch closure

The exact physical influence decomposition at a split is

\[
I(f)=\operatorname{Inf}_i(f)+\frac{I(g)+I(h)}2.
\tag{5.1}
\]

### Theorem 5.1 — toggle tree closure

Let a finite physical stopping tree have the property that every internal sibling pair is toggle-compatible. Suppose every stopping leaf `u` has a direct FEI certificate

\[
H(f_u)\le K I(f_u)
\]

for one constant `K>=2`. Then there is a full physical restriction tree extending the stopping tree such that

\[
\boxed{R_T(f)\le K I(f).}
\tag{5.2}
\]

#### Proof

By complete-block compression (1.1), every stopping leaf admits a full tree with allocation at most its entropy, hence at most `K I(f_u)`. Work backward. At an internal node, Theorem 4.2 gives

\[
B_i\le2j_i\le2\operatorname{Inf}_i\le K\operatorname{Inf}_i.
\]

Average the two descendant bounds and use (5.1). QED.

### Theorem 5.2 — one-exception-compatible tree closure

If instead every internal sibling pair is compatible away from at most one Fourier fibre, the same conclusion holds for every `K>=4`.

The proof is identical using (4.5).

### Project-conditional splice with P03

P03's newest report states that a Boolean function with one arbitrary exceptional Fourier coefficient and a flat tail has a direct coefficient strictly below four. Conditional on that peer theorem surviving later independent review, Theorem 5.2 immediately upgrades any dependent stopping tree of such leaves to a **hereditary coefficient four** whenever each sibling pair shares a common exceptional label and is magnitude-compatible off that label. This is a genuine hereditary use of P03's newest direct theorem, not a claim that the peer theorem was re-audited here.

The next section gives a completely independent application, so the mathematical gain of this run does not rest on that conditional splice.

---

## 6. Unconditional finite-field application: flat-tail children, unequal-tail parent

Let `q=2^m`, identify each `m`-bit block with the finite field `F_q`, and use any fixed `F_2`-linear basis. On three blocks `(x,z,y) in F_q^3` define

\[
G_y(x,z,y)=1-2\mathbf 1_{\{y=xz\}},
\qquad
G_x(x,z,y)=1-2\mathbf 1_{\{x=yz\}}.
\tag{6.1}
\]

The first function is the concrete multiplication-graph family appearing in P03's newest handoff; here all formulas needed for the splice are rederived.

### 6.1 Exact child spectra

For a Fourier character indexed by linear functionals `(alpha,beta,gamma)`,

\[
\widehat{\mathbf1_{\{y=xz\}}}(\alpha,\beta,\gamma)
=q^{-3}\sum_{x,z}
(-1)^{\alpha(x)+\beta(z)+\gamma(xz)}.
\tag{6.2}
\]

If `gamma=0`, this vanishes unless `alpha=beta=0`, where it equals `1/q`. If `gamma!=0`, then the map

\[
x\mapsto (z\mapsto\gamma(xz))
\]

is an isomorphism from `F_q` to its dual: injectivity follows because nonzero `x` makes `xz` run over the whole field. Thus for each `beta` there is exactly one `x` for which the inner `z`-character is trivial, and the sum in (6.2) has magnitude `q`. Therefore

\[
\widehat G_y(0)=1-\frac2q=:c,
\]

and every other nonzero coefficient has magnitude

\[
a=\frac2{q^2},
\]

with support exactly `gamma!=0`, of cardinality `q^2(q-1)`. By coordinate permutation, `G_x` has the same head and tail magnitude, with tail support exactly `alpha!=0`.

Hence the two children are toggle-compatible at **every** residual Fourier label.

### 6.2 Exact child influence and entropy

For `G_y`, flipping a `y`-bit changes membership in the graph with probability `2/q`. Flipping a nonzero `x`-direction changes the product only when `z!=0`, and then exactly two `y` values out of `q` lie on one of the two graph endpoints, so each `x`-bit has influence

\[
\frac{2(q-1)}{q^2}.
\]

The same holds for every `z`-bit. Thus

\[
\boxed{
I(G_y)=I(G_x)=\frac{6m}{q}-\frac{4m}{q^2}.
}
\tag{6.3}
\]

The tail squared mass is

\[
s=q^2(q-1)a^2=\frac{4(q-1)}{q^2},
\]

and the head squared mass is `p_0=c^2=1-s`. Therefore

\[
\boxed{
H(G_y)=H(G_x)
=-p_0\log_2p_0+s(4m-2).
}
\tag{6.4}
\]

We now prove, independently of P03's flat-tail theorem,

\[
\boxed{H(G_y)=H(G_x)<\frac83 I(G_y).}
\tag{6.5}
\]

Use `-p ln p <=1-p` to get

\[
-p_0\log_2p_0\le\frac{s}{\ln2}.
\]

Let `c_0=1/ln2`. Since `2/3<ln2<1`, we have `1<c_0<3/2`. Inequality (6.5) follows from

\[
(q-1)(4m-2+c_0)
\le \frac43m(3q-2),
\tag{6.6}
\]

because the right side minus the left side is exactly

\[
q(2-c_0)+\frac{4m}{3}+c_0-2>0
\]

for `q>=2,m>=1`. (The elementary lower bound `ln2>2/3` follows, for example, from `ln x>2(x-1)/(x+1)` at `x=2`.)

### 6.3 The selector splice

Add one selector bit `b` and define

\[
F_m(b,x,z,y)=
\begin{cases}
G_y(x,z,y),&b=0,\\
G_x(x,z,y),&b=1.
\end{cases}
\tag{6.7}
\]

Because the child spectra are toggle-compatible, Theorem 4.2 gives

\[
B_b(F_m)=2M_b(F_m)\le2\operatorname{Inf}_b(F_m).
\tag{6.8}
\]

In fact all quantities can be computed exactly. The child tail supports have intersection

\[
q(q-1)^2
\]

and symmetric difference

\[
r=2q(q-1).
\]

Every toggled tail fibre contributes `a^2/2`, so

\[
\boxed{B_b(F_m)=\frac{r a^2}{2}=\frac{4(q-1)}{q^3}.}
\tag{6.9}
\]

The two negative graph sets each have size `q^2`. Their intersection solves

\[
y=xz,\qquad x=yz,
\]

hence `x(1-z^2)=0`. In characteristic two, `z^2=1` forces `z=1`, so the intersection has `q+q-1=2q-1` points. Thus

\[
\boxed{
\operatorname{Inf}_b(F_m)
=\frac{2(q-1)^2}{q^3}.
}
\tag{6.10}
\]

In particular `B_b/Inf_b=2/(q-1)<=2`.

By (1.1) and (6.5), each child can be completed physically with hereditary allocation at most `(8/3)I(child)`. Grafting those two trees below the selector query and using (6.8) and (5.1) gives the all-dimensional theorem

\[
\boxed{
R_T(F_m)\le\frac83 I(F_m)
\qquad\text{for every }m\ge1.
}
\tag{6.11}
\]

This is an analytic hereditary theorem, not finite-dimensional verification.

### 6.4 Why this genuinely crosses P03's newest unequal-weight obstruction

The parent `F_m` is no longer one-exception plus one flat tail. At a residual tail label where both children are present, one of the two selector Fourier coefficients has magnitude `a=2/q^2` and the other is zero. At a label where exactly one child is present, both selector Fourier coefficients have magnitude `a/2=1/q^2`. Hence, besides the head, the parent has **two distinct nonzero tail magnitudes**:

\[
\frac2{q^2}\quad\text{on }q(q-1)^2\text{ frequencies},
\]

and

\[
\frac1{q^2}\quad\text{on }4q(q-1)\text{ frequencies}.
\tag{6.12}
\]

For `q>=4`, applying P03's newest generic few-exception theorem with smallest unit `1/q^2` counts

\[
R_m=1+q(q-1)^2
\]

frequencies larger than the unit, so that sufficient coefficient is

\[
6+\log_2(R_m+1)=3m+O(1).
\tag{6.13}
\]

By contrast, the new hereditary splice keeps coefficient `8/3` independent of `m`. Again, (6.13) is only a comparison with that generic sufficient certificate; it is not a lower bound on every possible P03 or FEI proof for `F_m`.

The child direct ratio in (6.4)/(6.3) tends to `8/3`, so the `8/3` coefficient is asymptotically tight for the **leaf-entropy graft used here**, not asserted optimal for hereditary allocation itself.

---

## 7. Why the new TV theorem does not close FEI

The universal estimate `B_i<=TV(P,Q)` cannot by pure probability geometry be turned into `B_i<=C j_i` for arbitrary child spectral laws. If two probability vectors move a small amount of mass between two coordinates, TV is first order in the displacement while squared Hellinger defect is second order. For example

\[
P=(1/2+\varepsilon,1/2-\varepsilon),\qquad
Q=(1/2-\varepsilon,1/2+\varepsilon)
\]

has `TV=2 epsilon` but Hellinger defect of order `epsilon^2`. These probability vectors are a **relaxation obstruction only**; they are not asserted to be Boolean Fourier spectra and are not FEI counterexamples.

The toggle theorem succeeds precisely because no common-support amplitude drift is allowed. More generally, from

\[
\frac12|x^2-y^2|
=\frac12(x-y)^2+\min(x,y)|x-y|
\]

we obtain the exact decomposition

\[
\operatorname{TV}(P,Q)
=2M_i+\Gamma_i,
\qquad
\Gamma_i:=\sum_T\min(x_T,y_T)|x_T-y_T|.
\tag{7.1}
\]

Thus `Gamma_i` is the **precise remaining common-support amplitude-drift surcharge** for this route. Toggle compatibility makes it zero. One exceptional drift fibre is paid by norm conservation, giving Theorem 4.3. With many drift fibres, cancellations of squared-mass changes prevent the same argument.

This also explains why the direct extension to two children with **different flat-tail amplitudes** was not proved: every overlap frequency contributes to `Gamma_i`. The newest P03 arithmetic structure may constrain those amplitudes, but no dimension-free linear payment for the resulting `Gamma_i` was obtained in this run. That extension is **UNPROVED**.

The next nonredundant target is therefore a Boolean/arithmetic payment for `Gamma_i` when many common-support amplitudes differ, ideally using P03's divisibility remainder `D` or a multiscale grouping that is hereditary under restriction. A proof must exploit Boolean spectral arithmetic; abstract Hellinger/TV geometry alone cannot supply it.

---

## 8. Executed sanity checks

The new checker is

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T19-08-00+0300__check_spectral_tv_splicing.py`,

creation commit `ffa796a044acada680f3e37c41c918973dcc8b3d`, blob `385834352a6e8b15c292f701c1b927118974da2e`.

Its actually executed output is

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T19-08-00+0300__spectral_tv_splicing_check.json`,

creation commit `74a1cbf04923209330118847d5b0bf229772529d`, blob `4241fc78de00bb9cb2335f7a16297858cbae3e2f`.

The run returned `PASS`. It checked:

1. the scalar inequality on 200,001 grid points;
2. every ordered pair of Boolean functions modulo global sign through residual dimension three: 16,452 pairs total, with maximum `B-TV=0` to floating precision;
3. 4,196 toggle-compatible pairs, with exact numerical `B=TV=2M` and maximum `B/j=2`;
4. 34,920 one-exception compatibility certificates, with maximum `TV-4M=0`;
5. 2,500 deterministic dimension-four random pairs, including 46 toggle pairs and 175 one-exception pairs;
6. the actual finite-field graph/splice families for `m=1,2,3,4`, verifying child spectra, support geometry, influence and entropy formulas, parent two-tail magnitude counts, exact root allocation/Hellinger/TV identities, and the `8/3` graft inequality.

The finite checks are sanity checks only. The theorems in Sections 3--6 are proved analytically above.

---

## 9. Source status, limitations, and no-overclaim statement

- Full FEI remains open; no universal finite constant is supplied.
- P03's newest one-exception/few-exception statements are preserved as peer reports, not silently promoted to independently certified theorems.
- The unconditional finite-field application does not depend on those peer statements.
- The restricted fresh-control theorem remains restricted.
- No historical false lemma is revived.
- The abstract two-coordinate probability drift example in Section 7 is not a Boolean FEI counterexample.
- Publication priority and independent review of the new spectral-TV/toggle lemmas are **UNVERIFIED**.
- No POSTED result is relabeled as new; the new statement is the hereditary spectral-TV/toggle recombination mechanism and its selector splice, not the already reported direct flat-tail child theorem.

---

## 10. `ledger_delta`

```yaml
ledger_delta:
  task: NM13-02
  parent: T01_Fourier_entropy_influence
  parent_status_before: OPEN
  parent_status_after: OPEN
  unrestricted_universal_constant_before: UNKNOWN
  unrestricted_universal_constant_after: UNKNOWN
  newest_peer_obstruction:
    source: proofnet24/P03-fei/continuations/2026-09-20-flat-tail-and-arithmetic-drift/HANDOFF.md
    commit: 33571041414a0b61c90e988dabccf5df5946d448
    issue: hereditary_recombination_for_arbitrary_unequal_spectral_weights_after_flat_tail_direct_certificates
  mechanism_gain:
    - universal_B_i_le_spectral_TV_of_children
    - toggle_compatible_exact_B_equals_TV_equals_2M_le_2j
    - one_exception_amplitude_drift_B_le_4M_le_4j
    - constant_preserving_dependent_branch_tree_closure
  demonstrated_application:
    family: F_m_selector_between_two_finite_field_multiplication_graph_signs
    dimensions: all_m_ge_1
    child_spectrum: one_head_plus_flat_tail
    parent_spectrum: one_head_plus_two_distinct_tail_magnitudes
    hereditary_bound: R_T_le_(8/3)_I
    generic_P03_few_exception_parameter: R_m=1+q(q-1)^2_for_q_ge_4
    generic_P03_sufficient_coefficient_behavior: 3m+O(1)
  project_conditional_corollary:
    statement: P03_one_exception_flat_tail_leaves_with_common_exceptional_label_and_compatible_off_head_inherit_constant_4
    dependency_status: peer_report_pending_independent_review
  failed_extension:
    - different_flat_tail_amplitudes_create_many_common_support_drift_fibres
    - abstract_TV_Hellinger_geometry_cannot_pay_multiple_drift_fibres_linearly
  residual_obstruction: dimension_free_Boolean_arithmetic_payment_for_Gamma_i=sum_min_amplitude_times_amplitude_drift
  checker:
    status: PASS
    code_commit: ffa796a044acada680f3e37c41c918973dcc8b3d
    output_commit: 74a1cbf04923209330118847d5b0bf229772529d
    exhaustive_ordered_pairs_through_dimension_3: 16452
    toggle_pairs: 4196
    one_exception_certificates: 34920
    deterministic_dimension_4_pairs: 2500
    finite_field_instances: 4
  fresh_control_status: RESTRICTED_PRESERVED
  false_lemma_corrections: PRESERVED
  independent_review: PENDING
  publication_priority: UNVERIFIED
  public_posting: none
  peer_or_history_overwrite: none
  email_drive_paid_compute_access_schedule_changes: none
```
