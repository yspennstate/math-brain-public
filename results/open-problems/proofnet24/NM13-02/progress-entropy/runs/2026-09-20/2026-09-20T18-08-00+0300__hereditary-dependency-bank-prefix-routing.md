Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** No authenticated GPT-6 / maximum-effort runtime metadata is exposed here.

# NM13-02 T01 — hereditary dependency-bank prefix routing

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI): prove a finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Unrestricted universal finite constant before -> after:** **UNKNOWN -> UNKNOWN**.

No finite-dimensional verification, influence-profile estimate, structured routing theorem, or restricted fresh-control theorem below is promoted to full FEI.

**Newest P03 obstruction actually addressed.** The newest P03 main report,

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T17-31-48+0300__fei-balanced-block-log-hereditary.md`,

proves a universal balanced-section hereditary compiler with coefficient `Theta(log n)` and records

`remaining_obstruction: remove logarithmic balanced-section depth via constant-depth certified routing or a new summable cross-scale rebate`.

The scheduled P03 dependency-bank continuation

`proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T14-08-00Z__report.md`

had already proved a direct weighted-depth dependency-bank inequality and explicitly identified the still-missing **orientation / conditional-allocation** payment for hereditary trees. Those are peer results; the local inequalities used below are rederived, so no P03 theorem is silently treated as independently certified.

**New mechanism.** For an arbitrary binary coordinate partition tree `Pi`, this run proves that the *same accumulated spectral mutual-information bank* that P03 used on the direct entropy side survives on the hereditary side. With singleton leaves and leaf depths `d_i`, there is an actual full physical restriction tree `T` such that

\[
\boxed{
R_T(f)+\mathcal M_{\Pi}(f)
\le \rho\sum_i\bigl(d_i-1+2^{-d_i}\bigr)\operatorname{Inf}_i(f),
\qquad \rho:=\frac2{\ln2}.
}
\tag{0.1}
\]

Thus the orientation cost does **not** require a second cross-scale bank. It is absorbed into a slightly *smaller* weighted-depth budget, while the accumulated dependency bank remains as a nonnegative rebate.

Choosing an influence-adapted prefix code gives the universal instance-sensitive corollary

\[
\boxed{
R_T(f)+\mathcal M_{\Pi}(f)
\le \rho I(f)\left(H_2(q)+\sum_iq_i^2\right),
\qquad q_i=\frac{\operatorname{Inf}_i(f)}{I(f)}.
}
\tag{0.2}
\]

This replaces the ambient `log n` by the Shannon entropy of the **influence profile**. It is still not full FEI because `H_2(q)` can be `log n`.

The theorem also has a certified-leaf form. If a leaf block has direct coefficient `C` and hereditary coefficient `K`, then after routing depth `d` its hereditary coefficient is

\[
\boxed{
\kappa_{C,K}(d)
=C+(d-1)\rho+(K-C+\rho)2^{-d}.
}
\tag{0.3}
\]

Taking two-coordinate leaves, for which every Boolean section is quadratic and hence `(C,K)=(2,1)`, recovers P03's newest balanced coefficient exactly when all depths are equal, **but now with `+\mathcal M_\Pi(f)` on the left**. This is the promised summable cross-scale rebate.

---

## 1. Current dependencies and compact NM13-02 handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

The exact T01 contract in `operations/PROB10_2026-09-20.md` remains in force: the reported fresh-control inequality appends variables and is restricted; it is not a fixed-domain proof of FEI. Archived false resolvent/erasure/affine-variance/coefficient-specific drift routes are not revived.

Newest own substantive report preserved:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T17-08-00+0300__bidirectional-biquadratic-block-selector.md`, creation commit `e6cd41f8533ab4c08dec059de2c241491177ed22`, blob `4a25ee785dace8dd06d578f8fb140c1c5c9c5865`.

It proves, independently of P03 peer certification, the projected transverse payment and the two-sided hereditary block selector. It gives a uniform hereditary coefficient `3/2+1/ln2` on block-bidegree `(2,2)` phases and a direct coefficient `2+2/ln2`; full FEI remains open.

Earlier NM13-02 results retained and not overwritten include: exact quadratic-rank allocation; one- and two-affine-flat classes; decision-tree and nested-spine certificates; variance-paid separators; quadratic-normalized Wiener control; guarded derivative selectors; oblique-derivative payments; character-child cross-fibre rescue; complete physical-block compression; multiway orthogonal-label splicing. Their hypotheses remain unchanged.

The current P03 README still marks full FEI open and preserves the correction chain. In particular this run does not reintroduce the false pointwise-erasure converse, fixed affine drift, all-coordinate absolute-overlap selector, derivative-degree scalar schedule, blind curvature payment, fixed-`s<2` Renyi payment, frozen-parent endpoint payment, marginal-entropy substitution, arbitrary orthogonal-involution relaxation, or fresh-variable shortcut.

### Primary-source status checked in this run

González–MacManus–Pereyra, arXiv:2606.00246, submitted 29 May 2026 and revised in June 2026, still states universal FEI as a conjecture and explains that its restriction inequality would imply full FEI only if universal. Li–Han, arXiv:2512.03117, submitted 2 December 2025, gives a general entropy-influence inequality with an additional coordinate-profile term; it is not a universal `C I(f)` theorem. A bounded fresh search did not recover a source-matching universal resolution. Publication priority for the theorem below is **UNVERIFIED**.

---

## 2. Definitions and the two local inequalities

Let `U` be a physical coordinate block and `g:{-1,1}^U->{-1,1}`. Let `S_U` be its spectral random set,

\[
\Pr[S_U=T]=\widehat g(T)^2.
\]

For a physical split `U=A\sqcup B`, write `g_b` for the `A`-section after fixing `B=b`, and `g_a` for the `B`-section after fixing `A=a`. Write

\[
I_A(g)=\sum_{i\in A}\operatorname{Inf}_i(g),\qquad I_B(g)=\sum_{i\in B}\operatorname{Inf}_i(g).
\]

### Lemma 2.1 — projected transverse entropy payment

For every split `U=A\sqcup B`,

\[
\boxed{
H(S_A)\le \mathbb E_b H(\widehat{g_b}^{\,2})+\rho I_B(g),
\qquad \rho=2/\ln2.
}
\tag{2.1}
\]

The symmetric statement holds with `A,B` exchanged.

#### Proof

Reveal `B` physically, one coordinate at a time. At a query `i`, the two child Fourier coefficients on each residual fibre are `u_T+v_T` and `u_T-v_T`, so after forgetting the queried spectral bit the parent law is the equal mixture of the two child squared Fourier laws. Hence the one-step loss of the retained `A`-marginal entropy is a Jensen–Shannon divergence.

For child spectral laws `P,Q`,

\[
\operatorname{JS}_2(P,Q)
\le \frac1{\ln2}\left(1-\sum_T\sqrt{P_TQ_T}\right).
\tag{2.2}
\]

This follows by summing the scalar inequality

\[
\frac12\left[a\ln\frac{2a}{a+b}+b\ln\frac{2b}{a+b}\right]
\le \frac12(\sqrt a-\sqrt b)^2.
\]

For Boolean children `h_+,h_-`,

\[
\sum_T|\widehat h_+(T)\widehat h_-(T)|
\ge |\langle h_+,h_-\rangle|
=|1-2\operatorname{Inf}_i(g)|.
\]

Therefore the one-step projected loss is at most

\[
\rho\min\{\operatorname{Inf}_i(g),1-\operatorname{Inf}_i(g)\}
\le \rho\operatorname{Inf}_i(g).
\]

The physically queried influences telescope exactly over a complete `B`-prefix to `I_B(g)`. Summing gives (2.1). QED.

### Lemma 2.2 — complete-block hereditary compression

For a complete physical query of all coordinates in `A`, in any adaptive order,

\[
\boxed{
R_{T_A}(g)\le H(S_A\mid S_B).
}
\tag{2.3}
\]

#### Proof

Induct on `|A|`. For a root query `i\in A`, the root allocation is

\[
B_i(g)=H(S_i\mid S_{A\setminus\{i\}},S_B).
\]

By the same child-mixture identity, the equal mixture of the two child laws on `(S_{A\setminus\{i\}},S_B)` is the parent marginal. Conditional entropy is concave in the joint law, so the average descendant allocation is at most

\[
H(S_{A\setminus\{i\}}\mid S_B).
\]

Add the root term and use the conditional entropy chain rule. QED.

---

## 3. Dependency bank on a coordinate partition tree

Let `Pi` be a rooted full binary tree of physical coordinate blocks. Each internal node `V` is partitioned into children `V_0,V_1`; the leaves form a partition of the active coordinates.

For every internal node `V` and every physical outside assignment `z` on `U\setminus V`, let `g_z` be the resulting section on `V`. Define the accumulated dependency bank

\[
\boxed{
\mathcal M_{\Pi}(g)
=
\sum_{V\in\operatorname{Int}(\Pi)}
\mathbb E_z\, I_{\widehat{g_z}^{\,2}}(S_{V_0};S_{V_1}).
}
\tag{3.1}
\]

It is nonnegative. At a root split `U=A\sqcup B`, it decomposes exactly as

\[
\mathcal M_\Pi(g)
=I(S_A;S_B)
+\mathbb E_b\mathcal M_{\Pi_A}(g_b)
+\mathbb E_a\mathcal M_{\Pi_B}(g_a).
\tag{3.2}
\]

---

## 4. New theorem — anisotropic banked hereditary routing

The theorem is stated coordinatewise because that is what permits influence-adapted routing.

### Theorem 4.1

Assume that each leaf block `L` of `Pi` comes with nonnegative coordinate coefficients `c_i,k_i` such that **every** Boolean physical section `h` on that leaf satisfies

\[
H(\widehat h^{\,2})\le\sum_{i\in L}c_i\operatorname{Inf}_i(h)
\tag{4.1}
\]

and has a full physical restriction tree with

\[
R(h)\le\sum_{i\in L}k_i\operatorname{Inf}_i(h).
\tag{4.2}
\]

Let `d_i` be the depth of the leaf containing coordinate `i`. Then:

1. the direct dependency-bank estimate is
   \[
   \boxed{
   H(\widehat g^{\,2})+\mathcal M_\Pi(g)
   \le\sum_i(c_i+\rho d_i)\operatorname{Inf}_i(g);
   }
   \tag{4.3}
   \]
2. there exists a full physical restriction tree `T` such that
   \[
   \boxed{
   R_T(g)+\mathcal M_\Pi(g)
   \le\sum_i\kappa_i(d_i)\operatorname{Inf}_i(g),
   }
   \tag{4.4}
   \]
   where
   \[
   \boxed{
   \kappa_i(d)
   =c_i+(d-1)\rho+(k_i-c_i+\rho)2^{-d}.
   }
   \tag{4.5}
   \]

### Proof

Induct on the partition tree. The leaf case is exactly (4.1)-(4.2), and (4.5) at `d=0` equals `k_i`.

Let the root split be `A\sqcup B`, with child partition trees `Pi_A,Pi_B`. Denote the inductive direct right sides on the two children by `D_A,D_B` and the inductive hereditary right sides by `K_A,K_B`.

For the direct estimate, use

\[
H(g)+I(S_A;S_B)=H(S_A)+H(S_B).
\]

Adding the two child dependency banks and applying Lemma 2.1 in both orientations gives

\[
\begin{aligned}
H(g)+\mathcal M_\Pi(g)
&=H(S_A)+H(S_B)
 +\mathbb E_b\mathcal M_{\Pi_A}(g_b)
 +\mathbb E_a\mathcal M_{\Pi_B}(g_a)\\
&\le \mathbb E_b\bigl[H(g_b)+\mathcal M_{\Pi_A}(g_b)\bigr]
 +\mathbb E_a\bigl[H(g_a)+\mathcal M_{\Pi_B}(g_a)\bigr]
 +\rho I(g)\\
&\le D_A+D_B+\rho I(g).
\end{aligned}
\tag{4.6}
\]

Averaging physical section influences is exact, so every coordinate coefficient increases by `rho` at one partition ancestor. This proves (4.3).

For the hereditary estimate, first build an `A`-first physical tree: completely query `A`, then on every resulting `B`-section graft the inductive hereditary tree for `Pi_B`. By Lemma 2.2,

\[
R_{A\text{-first},\mathrm{prefix}}(g)
\le H(S_A\mid S_B).
\]

Now **keep the dependency bank rather than dropping it**. Using (3.2),

\[
\begin{aligned}
R_{A\text{-first}}(g)+\mathcal M_\Pi(g)
&\le H(S_A\mid S_B)+I(S_A;S_B)
 +\mathbb E_b\mathcal M_{\Pi_A}(g_b)\\
&\qquad +\mathbb E_a\bigl[R_B(g_a)+\mathcal M_{\Pi_B}(g_a)\bigr]\\
&=H(S_A)+\mathbb E_b\mathcal M_{\Pi_A}(g_b)
 +\mathbb E_a\bigl[R_B(g_a)+\mathcal M_{\Pi_B}(g_a)\bigr]\\
&\le D_A+\rho I_B(g)+K_B.
\end{aligned}
\tag{4.7}
\]

The last line uses Lemma 2.1 and the two inductive hypotheses. Symmetrically, an actual `B`-first physical tree satisfies

\[
R_{B\text{-first}}(g)+\mathcal M_\Pi(g)
\le K_A+\rho I_A(g)+D_B.
\tag{4.8}
\]

Choose the cheaper of these two actual trees. Since `min{x,y}<=(x+y)/2`,

\[
R_T(g)+\mathcal M_\Pi(g)
\le\frac12(D_A+K_A+D_B+K_B+\rho I(g)).
\tag{4.9}
\]

Thus, for a coordinate whose child-level direct and hereditary coefficients are `C_t,K_t`, one ancestor updates them by

\[
C_{t+1}=C_t+\rho,
\qquad
K_{t+1}=\frac{C_t+K_t+\rho}{2}.
\tag{4.10}
\]

Starting at `C_0=c_i,K_0=k_i`, solve (4.10):

\[
C_d=c_i+d\rho,
\]

and direct substitution verifies

\[
K_d=c_i+(d-1)\rho+(k_i-c_i+\rho)2^{-d}.
\]

This is (4.5), completing the induction. QED.

### Mechanism interpretation

The root mutual information in (4.7) cancels the difference between marginal and conditional block entropy **exactly**. The child dependency banks are then propagated through the direct side and the hereditary side simultaneously. Hence cross-scale spectral dependence is not repeatedly charged: it remains an accumulated rebate all the way to the root.

---

## 5. Two universal specializations

### 5.1 Singleton leaves

A one-variable Boolean sign is constant or an affine character. Hence its spectral entropy and hereditary allocation are both zero: `c_i=k_i=0`.

Theorem 4.1 becomes

\[
\boxed{
R_T(f)+\mathcal M_\Pi(f)
\le \rho\sum_i\bigl(d_i-1+2^{-d_i}\bigr)\operatorname{Inf}_i(f).
}
\tag{5.1}
\]

This is (0.1).

### 5.2 Two-coordinate quadratic leaves and recovery of P03's balanced constant

Every Boolean sign on two variables has quadratic ANF phase. The preserved exact quadratic theorem gives

\[
H(h)\le2I(h),\qquad R(h)\le I(h).
\]

Thus a two-coordinate leaf may take `(C,K)=(2,1)`, and at routing depth `d`

\[
\boxed{
\kappa_{2,1}(d)
=2+(d-1)\rho+(\rho-1)2^{-d}.
}
\tag{5.2}
\]

If `n=2^L` and the coordinates are paired at the bottom of a completely balanced partition hierarchy, every pair leaf has depth `d=L-1`. Then (5.2) is

\[
2+(L-2)\rho+(\rho-1)2^{1-L},
\]

which is exactly the coefficient in P03's newest balanced-block theorem. The new statement is strictly stronger at the mechanism level because it proves

\[
R_T(f)+\mathcal M_\Pi(f)
\le K_LI(f),
\]

rather than only `R_T(f)<=K_L I(f)`.

---

## 6. Influence-profile prefix coding

Let the positive-influence coordinates have

\[
p_i=\operatorname{Inf}_i(f),\qquad
I=\sum_i p_i>0,
\qquad
q_i=p_i/I.
\]

If there is only one positive-influence coordinate, `f` depends on at most one bit and `R=0`.

Otherwise take Shannon code lengths

\[
\ell_i=\left\lceil\log_2\frac1{q_i}\right\rceil.
\]

Kraft's inequality gives

\[
\sum_i2^{-\ell_i}\le\sum_iq_i=1,
\]

so there is a binary prefix tree with these code lengths. Suppressing unary vertices can only decrease the actual leaf depths. Since

\[
d\mapsto d-1+2^{-d}
\]

is increasing on nonnegative integers, Theorem 4.1 and (5.1) give

\[
R_T(f)+\mathcal M_\Pi(f)
\le\rho I\sum_iq_i\left(\ell_i-1+2^{-\ell_i}\right).
\tag{6.1}
\]

Now

\[
\ell_i-1\le\log_2\frac1{q_i},
\qquad
2^{-\ell_i}\le q_i.
\]

Therefore

\[
\boxed{
R_T(f)+\mathcal M_\Pi(f)
\le\rho I(f)
\left[
H_2(q)+\sum_iq_i^2
\right].
}
\tag{6.2}
\]

This is (0.2). In particular, with effective influence support

\[
N_{\mathrm{eff}}:=2^{H_2(q)},
\]

the hereditary allocation is `O(I log N_eff)`, not `O(I log n)`.

The theorem is universal but not a universal FEI constant: a flat influence profile has `H_2(q)=log_2 n`.

---

## 7. Application: a signed-translation-rigid anchored multiplexer

The gain is not only formal. Let `k>=2`, let

\[
a\in\mathbb F_2^k,
\qquad
y=(y_z)_{z\in\mathbb F_2^k}\in\mathbb F_2^{2^k},
\]

and define the Boolean phase

\[
P_k(a,y)=y_a+y_0y_1\pmod2,
\qquad
F_k=(-1)^{P_k}.
\tag{7.1}
\]

Here `0,1` denote two fixed distinct data addresses. The ambient dimension is

\[
n_k=k+2^k.
\]

### 7.1 Exact influences

For every address coordinate `a_j`, toggling it replaces the selected independent fair data bit by a different fair data bit, while the anchor cancels. Thus

\[
\operatorname{Inf}_{a_j}(F_k)=\frac12.
\tag{7.2}
\]

For the two anchored data bits,

\[
D_{y_0}P_k=1_{\{a=0\}}+y_1,
\qquad
D_{y_1}P_k=1_{\{a=1\}}+y_0,
\]

so both have influence `1/2`. Every other data coordinate has derivative `1_{\{a=z\}}`, hence influence `2^{-k}`. Therefore

\[
\boxed{
I(F_k)=\frac{k+4-2^{2-k}}2.
}
\tag{7.3}
\]

Put

\[
D_k:=k+4-2^{2-k}.
\]

The normalized influence profile has `k+2` heavy atoms of mass `1/D_k` and `2^k-2` light atoms of mass `2^{1-k}/D_k`. Hence

\[
\boxed{
H_2(q)
=\log_2D_k
+\frac{(2-2^{2-k})(k-1)}{D_k},
}
\tag{7.4}
\]

and

\[
\boxed{
\sum_iq_i^2
=\frac{k+2+2^{2-k}-2^{3-2k}}{D_k^2}.
}
\tag{7.5}
\]

Combining with (6.2),

\[
\boxed{
\frac{R_T(F_k)+\mathcal M_\Pi(F_k)}{I(F_k)}
\le
\rho\left[
\log_2D_k
+\frac{(2-2^{2-k})(k-1)}{D_k}
+\frac{k+2+2^{2-k}-2^{3-2k}}{D_k^2}
\right].
}
\tag{7.6}
\]

As `k->infinity`, the right side is

\[
\rho\log_2 k+2\rho+o(1).
\tag{7.7}
\]

By contrast, P03's newest universal balanced compiler sees `L=ceil(log_2 n_k)=k+1` and gives

\[
K_{\mathrm{bal}}(k)
=2+(k-1)\rho+(\rho-1)2^{-k}
=\Theta(k).
\tag{7.8}
\]

Thus the new routing improves the hereditary coefficient on this family from `Theta(log n_k)=Theta(k)` to

\[
\boxed{\Theta(\log k)=\Theta(\log\log n_k).}
\]

The checker shows the crossover numerically: at `k=6`, the balanced/profile coefficients are approximately `16.4564` versus `12.6073`; at `k=20`, `56.8224` versus `17.9081`; at `k=80`, `227.0604` versus `23.9051`.

The preserved degree theorem gives only a `Theta(k)` generic coefficient here because `deg P_k=k+1`, so this is also a strict asymptotic improvement over the all-degree hereditary certificate.

### 7.2 Signed-translation rigidity

The anchor removes the standard multiplexer sign symmetry. Suppose a translation `t=(alpha,beta)` makes the multiplicative derivative of `F_k` constant. Equivalently, the additive phase derivative

\[
P_k(a,y)+P_k(a+\alpha,y+\beta)
\]

is constant.

If `alpha!=0`, then for every data coordinate `y_z` the multiplexer contribution to its coefficient is

\[
1_{\{a=z\}}+1_{\{a+\alpha=z\}},
\]

the indicator of two distinct address points. For `k>=2` choose `z` outside the two anchored labels; the quadratic anchor contributes no `y_z` term, so this nonconstant coefficient cannot be canceled. Hence `alpha=0`.

With `alpha=0`, the derivative is

\[
\beta_a+\beta_0y_1+\beta_1y_0+\beta_0\beta_1.
\tag{7.9}
\]

Constancy forces `beta_0=beta_1=0`; then `beta_a` must be constant in `a`, and because it vanishes at the two anchored addresses it must vanish identically. Thus `beta=0`.

So `F_k` has **no nontrivial signed translation symmetry**. Its top-degree ANF monomials `y_z a_1\cdots a_k` occur for every data address `z`, so the degree-`k+1` interaction hypergraph is one connected component. The example therefore remains inside the signed-rigid connected-core regime that motivated the earlier proper-block obstruction, while exhibiting a large gain from influence-adapted cross-scale routing.

---

## 8. Executed sanity checks

New checker:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T18-08-00+0300__check_hereditary_dependency_routing.py`

creation commit `ae7c98871671895580ec4b54ab28ff06712c97fa`, blob `73f033d649385db5d84a6ec005c9c5fe229c37d5`.

Executed output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T18-08-00+0300__hereditary_dependency_routing_output.json`

creation commit `0ca3553ae49f7c4c950417babaa7d64419035823`, blob `ff23b5ac6b257b53c400a0816f716dd411df2671`, status `PASS`.

The checker:

- exhaustively tested all Boolean functions modulo global sign in dimensions 2 and 3 against every labeled binary coordinate partition tree: 8 and 384 tree/function cases respectively, with maximum `R+M-RHS = 0.0`;
- tested 220 deterministic dimension-4 Boolean functions against all 15 labeled binary partition trees, 3,300 cases total, with maximum `R+M-RHS = -1.5579426615...`;
- brute-forced the anchored multiplexer influence formulas and absence of nontrivial signed translations at `k=2,3`;
- compared the profile and newest balanced coefficients through `k=80`.

These computations are sanity checks only. The all-dimensional theorem is proved analytically above.

---

## 9. Failure / residual obstruction / next attack

The new theorem does **not** remove the influence-profile entropy term in the worst case. For nearly uniform `q`, (6.2) is still `Theta(I log n)`. The dependency bank can also vanish: bent quadratics have independent spectral coordinate blocks across natural cuts, although those particular functions are harmless because the quadratic leaf certificate stops the routing immediately.

So the full obstruction is now narrower than P03's balanced-depth statement:

> **Flat-profile hard cores:** prove that every function with diffuse coordinate influences either admits large certified leaf blocks, or has a coordinate partition tree whose accumulated dependency bank cancels a constant fraction of the profile-depth currency.

Equivalently, seek a dichotomy of the form

\[
\mathcal M_\Pi(f)
+\text{certified-leaf rebate}
\gtrsim
\rho I(f)H_2(q)-O(I(f)).
\]

Nothing here proves such a dichotomy. The immediate stress family should therefore have (i) nearly flat influences, (ii) no low-degree or symmetry leaf certificate, and (iii) small dependency bank across many cuts. If one can construct such a family, this routing route is quantitatively blocked; otherwise a bank-versus-certification lemma is the next nonredundant target.

This is a materially different attack from the retired pointwise-erasure, fixed-drift, absolute-overlap, derivative-degree scalar, blind-curvature, fixed-Renyi, marginal-substitution and arbitrary-orthogonal routes.

---

## ledger_delta

```yaml
ledger_delta:
  worker: NM13-02
  parent: T01_FEI
  date: 2026-09-20
  source_status_before: OPEN
  source_status_after: OPEN
  unrestricted_constant_before: UNKNOWN
  unrestricted_constant_after: UNKNOWN
  latest_P03_obstruction:
    report: proofnet24/P03-fei/runs/2026-09-20/2026-09-20T17-31-48+0300__fei-balanced-block-log-hereditary.md
    obstruction: remove logarithmic balanced-section depth via constant-depth certified routing or a new summable cross-scale rebate
    peer_claim_assumed_established: false
  new_theorem:
    name: hereditary dependency-bank prefix routing
    singleton_form: "R_T + M_Pi <= (2/ln2) sum_i (d_i-1+2^-d_i) Inf_i"
    profile_form: "R_T + M_Pi <= (2/ln2) I [H_2(q)+sum_i q_i^2]"
    certified_leaf_coefficient: "C+(d-1)(2/ln2)+(K-C+2/ln2)2^-d"
  mechanism_gain:
    - preserves the accumulated mutual-information dependency bank on the hereditary side
    - generalizes balanced routing to arbitrary influence-adapted coordinate partition trees
    - recovers the newest P03 balanced coefficient on quadratic pair leaves, with an extra nonnegative bank on the left
    - improves anchored multiplexer routing from Theta(log n) to Theta(log log n)
  application:
    family: "F_k(a,y)=(-1)^(y_a+y_0 y_1), k>=2"
    properties:
      - signed-translation-rigid
      - connected degree-(k+1) interaction core
      - exact influence profile proved
      - profile hereditary coefficient Theta(log k)
  checker:
    path: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T18-08-00+0300__check_hereditary_dependency_routing.py
    commit: ae7c98871671895580ec4b54ab28ff06712c97fa
    blob: 73f033d649385db5d84a6ec005c9c5fe229c37d5
    status: PASS
  output:
    path: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T18-08-00+0300__hereditary_dependency_routing_output.json
    commit: 0ca3553ae49f7c4c950417babaa7d64419035823
    blob: ff23b5ac6b257b53c400a0816f716dd411df2671
    status: PASS
  finite_checks_are_proof: false
  fresh_control_promoted_to_full_FEI: false
  failed_routes_preserved: true
  remaining_obstruction: "flat-influence hard cores: dependency-bank-or-certified-leaf dichotomy strong enough to erase H_2(q)"
  next_attack: "construct or rule out a flat-influence signed-rigid high-degree family with simultaneously small partition dependency bank and no large certified leaf block"
```
