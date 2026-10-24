# account04/B13 — arbitrary-bias joint credit and a rare-pivot quarter-influence exclusion

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Live target:** source-current all-gate FEI inequality for the fixed `Gamma^dagger` candidate.  

## 0. What changed in this run

The later owner control has superseded the older interface-B-only execution wording and asks the FEI fleet to converge on the source-exact all-gate inequality. I therefore keep the previous account04/B18 mixed-curvature conservation and exact zero-defect classification intact, but do not reopen the already-retired ordinary-depth or cube-measure-times-dimension routes.

The first source-current missing implication is the restriction **LOCAL-GLUING** problem. For a physical pivot `j`, account04/B17 proved the exact identity

\[
D_\Gamma(G)=qD_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal R_{\Gamma,j}+\mathcal C_j,
\]

where `t=p_j`, `q=1-t`, and

\[
\mathcal C_j=H(B\mid S)+I(S;J)\ge 0
\]

is the exact source-side information credit. A minimum-essential-arity counterexample can survive a pivot only if its local term `R+C` is negative.

The newest compatible other-account result consumed here is

`account02/B13/20260922T045511Z-joint-credit-critical-core/REPORT.md`

(commit `547cb4e42877590ce8195a5a4859b0facb13877e`). It proves at an **unbiased** pivot the sharp source-valid lower bound

\[
\mathcal C_j\ge
h_2\!\left(\frac{1-2\sqrt{\delta(1-\delta)}}2\right),
\qquad
\delta=\Pr(G_0\ne G_1),
\]

and from it excludes balanced-child negative gluing whenever `delta>=1/4` at the center. The argument below changes that theorem in one precise direction: it extracts from the same actual Boolean coefficient coupling a weaker but **arbitrary-pivot-bias** lower bound. Combined with the certified small-bias tail of the live potential, it excludes every balanced-child negative gluing node with normalized influence at least one quarter throughout an explicit rare-bias collar.

Full uniform-cube FEI remains open.

## 1. Exact source geometry at arbitrary pivot bias

Let

\[
f_b=(-1)^{G_b},\qquad b\in\{0,1\},
\]

be the two actual Boolean restrictions on the common product space of the remaining coordinates. Expand in its real biased orthonormal Fourier basis,

\[
f_0=\sum_S a_S\chi_S,\qquad
f_1=\sum_S b_S\chi_S.
\]

Parseval gives `sum a_S^2=sum b_S^2=1`. Put

\[
T_S=q a_S^2+t b_S^2.
\]

The latent branch posterior at spectral atom `S` is

\[
x_S=\Pr(B=1\mid S)=\frac{t b_S^2}{T_S}
\]

when `T_S>0`. Hence

\[
H(B\mid S)=\sum_S T_S h_2(x_S).
\tag{1.1}
\]

Define

\[
u_S=2\sqrt{x_S(1-x_S)}
=\frac{2\sqrt{tq}\,|a_Sb_S|}{T_S}.
\tag{1.2}
\]

The actual child disagreement probability is

\[
\delta=\Pr(f_0\ne f_1),
\]

so Booleanity and Parseval give the signed overlap identity

\[
\sum_S a_Sb_S=\mathbb E[f_0f_1]=1-2\delta.
\tag{1.3}
\]

Therefore

\[
\mathbb E_T u_S
=2\sqrt{tq}\sum_S|a_Sb_S|
\ge 2\sqrt{tq}\,|1-2\delta|.
\tag{1.4}
\]

This keeps the actual signed Boolean coupling. No arbitrary probability-law relaxation has been introduced.

## 2. New arbitrary-bias joint-credit theorem

Use the elementary binary-entropy inequality

\[
h_2(x)\ge 4x(1-x),\qquad 0\le x\le1.
\tag{2.1}
\]

Since `u_S^2=4x_S(1-x_S)`, equations (1.1), (2.1), Jensen, and (1.4) yield

\[
\begin{aligned}
H(B\mid S)
&\ge \mathbb E_T u_S^2\\
&\ge (\mathbb E_Tu_S)^2\\
&\ge 4tq(1-2\delta)^2.
\end{aligned}
\]

The second part of the exact B17 credit is nonnegative. Hence:

### Theorem 2.1 — arbitrary-bias Boolean joint-credit lower bound

For every actual Boolean pair of restrictions and every interior pivot bias,

\[
\boxed{
\mathcal C_j=H(B\mid S)+I(S;J)
\ge V_t(1-2\delta)^2,
\qquad V_t=4t(1-t).
}
\tag{2.2}
\]

Equivalently, since `It_j=V_t delta`, the bound is entirely influence-relative: it depends on the pivot only through `V_t` and the normalized influence `It_j/V_t`. It has no ambient-dimension factor and no number-of-rows factor.

At `t=1/2`, (2.2) is exactly the quadratic lower bound used as the coarse step inside account02/B13's sharper center theorem. The new point is that (2.2) survives unchanged for arbitrary `t` after the natural `V_t` scaling.

## 3. Exact insertion into LOCAL-GLUING

The account04/B17 exact cocycle has

\[
\begin{aligned}
\mathcal R_{\Gamma,j}={}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)\\
&+\delta\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(V_t\delta),
\end{aligned}
\tag{3.1}
\]

where `r_b=Pr(G_b=1)` and `r=qr_0+tr_1`. Combining (2.2) and (3.1) gives the source-exact arbitrary-bias lower envelope

\[
\boxed{
\begin{aligned}
\mathcal R_{\Gamma,j}+\mathcal C_j\ge{}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)\\
&+\delta\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(V_t\delta)\\
&+V_t(1-2\delta)^2.
\end{aligned}}
\tag{3.2}
\]

This is the useful general statement from the run. The only non-scalar object left on the right is the potential Jensen term in the two child output biases.

For balanced children, `r_0=r_1=1/2`, that term vanishes identically. By symmetry put

\[
u=\min(t,1-t),\qquad V=4u(1-u),
\]

and define

\[
F_u(\delta)
=\delta\bigl(\Gamma(u)+h_2(V)\bigr)
-h_2(u)-h_2(V\delta)+V(1-2\delta)^2.
\tag{3.3}
\]

Then balanced-child negative gluing requires `F_u(delta)<0`.

## 4. The live Gamma-dagger tail

The source-current fixed candidate is

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\qquad
a^\dagger=0.268204856.
\tag{4.1}
\]

Account01/B18's completed source theorem (`20260922T0325Z-addressing-star-cdagger`) records that for `0<u<=1/2`, with `L=log_2(1/u)`,

\[
\Gamma_0(u)>u(4.9096L+2.22).
\]

Therefore

\[
\boxed{
\Gamma^\dagger(u)>
 u(4.9096L+2.22)+0.268204856\,u(1-u).
}
\tag{4.2}
\]

Only this already source-certified tail lower bound is used below.

## 5. New rare-pivot quarter-influence exclusion

### Theorem 5.1

For the live `Gamma^dagger`, suppose a physical pivot has balanced Boolean children and

\[
0<u:=\min(t,1-t)\le2^{-15}.
\]

If

\[
\delta=\Pr(G_0\ne G_1)\ge\frac14,
\]

then

\[
\boxed{\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j>0.}
\tag{5.1}
\]

Equivalently, every negative balanced-child gluing node in this rare-bias collar must satisfy the influence-relative exceptional condition

\[
\boxed{
\frac{\operatorname{It}_j}{V_t}<\frac14.
}
\tag{5.2}
\]

#### Proof

By (3.2), it suffices to prove `F_u(delta)>0` for (3.3).

First, `F_u` is increasing on `[1/4,1]` in the stated collar. Its derivative is

\[
F_u'(\delta)=
\Gamma^\dagger(u)+h_2(V)
-Vh_2'(V\delta)-4V(1-2\delta).
\tag{5.3}
\]

For `delta>=1/4`,

\[
h_2'(V\delta)\le\log_2\frac1{V\delta}
\le\log_2\frac4V,
\]

and `-4V(1-2delta)>=-2V`. Since `u<=1/2`,

\[
\frac4V=\frac1{u(1-u)}\le\frac2u,
\qquad V\le4u.
\]

Dropping the nonnegative `h_2(V)` and the positive quadratic part of (4.2), with `L>=15`, gives

\[
\begin{aligned}
F_u'(\delta)
&>u(4.9096L+2.22)-4u(L+1)-8u\\
&=u(0.9096L-9.78)\\
&\ge3.864u>0.
\end{aligned}
\tag{5.4}
\]

So it is enough to check `delta=1/4`.

At that point

\[
F_u(1/4)=
\frac14\Gamma^\dagger(u)+\frac14h_2(V)
-h_2(u)-h_2(V/4)+\frac V4.
\tag{5.5}
\]

Use the standard entropy bounds

\[
h_2(x)\ge x\log_2(1/x),
\qquad
h_2(x)\le x\log_2(e/x),
\tag{5.6}
\]

and the elementary `log_2 e<3/2`. Because `V/4=u(1-u)`, (4.2), (5.5), and (5.6) give

\[
\begin{aligned}
\frac{F_u(1/4)}u
>{}&
\left(\frac{4.9096}{4}-1\right)L
+\frac{2.22}{4}-\frac32\\
&+(1-u)\left(\frac{0.268204856}{4}-\frac52\right).
\end{aligned}
\tag{5.7}
\]

The last parenthesis is negative, so replacing `1-u` by `1` only lowers the right side. With `L>=15`,

\[
\frac{F_u(1/4)}u
>
0.2274(15)+0.555-1.5-2.432948786
=0.033051214>0.
\tag{5.8}
\]

Thus `F_u(1/4)>0`; monotonicity (5.4) gives `F_u(delta)>0` for every `delta>=1/4`. QED.

The cutoff `2^-15` is deliberately conservative. It comes from transparent analytic inequalities, not from a sampled bias grid.

## 6. How the peer result changes the critical-core picture

Before account02/B13's new theorem, the exact restriction cocycle retained the correct information credits but did not yield a dimension-free exclusion region for arbitrary Boolean child pairs. Their convex signed-overlap theorem closes the **unbiased** balanced-child region `delta>=1/4`.

The present extension shows that the same actual signed overlap also controls branch entropy at arbitrary bias after multiplying by `V_t`. The live potential's linear-log tail then closes the opposite extreme: every sufficiently rare pivot with `delta>=1/4`.

Hence, on the balanced-child slice, a negative local gluing node for the live candidate cannot simultaneously have normalized influence at least one quarter and lie either

1. exactly at the unbiased center (account02/B13), or
2. in the explicit rare-bias collar `min(t,1-t)<=2^-15` (this report).

The remaining LOCAL-GLUING geometry is therefore more localized: small normalized influence `delta<1/4`, intermediate pivot biases, and/or unequal child output measures where the potential Jensen term in (3.2) must be paid. This is a genuine reduction of the source-current missing implication, not a proof of full FEI.

## 7. Relation to the preserved account04/B18 interface-B results

Nothing in this argument modifies or weakens the account04/B18 exact mixed-curvature identities

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]

or its exact zero-defect classification by a character-twisted signed one-point defect. In particular, this report does **not** replace `sum d_k` by `O(J)`, does not charge a small cube-measure error by ambient dimension, and does not use unsigned support overlap in place of the opposite-sign term.

The new restriction-cocycle theorem is orthogonal to that rigidity bank: it supplies a dimension-free, influence-relative local information payment directly from two actual Boolean children. If the all-gate route ultimately needs to return to derivative stability, (2.2) is a compatible nonreusing local credit rather than a second-factorial-moment charge.

## 8. Status and next exact implication

**Proved this run:** arbitrary-bias credit bound (2.2), all-child local lower envelope (3.2), and the live-candidate rare-pivot quarter-influence exclusion (5.1)-(5.2).

**Not proved:** LOCAL-GLUING for intermediate biases, unequal child output measures, or normalized influence below one quarter; the universal all-gate inequality; full FEI.

The next source-exact target is to control the Jensen term

\[
q\Gamma^\dagger(r_0)+t\Gamma^\dagger(r_1)-\Gamma^\dagger(qr_0+tr_1)
\]

against the credit in (3.2), or to derive a stronger biased analogue of account02/B13's convex `Psi` theorem that uses both `H(B|S)` and `I(S;J)` rather than only the first term. Either improvement would attack the remaining intermediate-bias/unequal-child local-gluing region without reverting to an ambient-dimensional continuity loss.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
