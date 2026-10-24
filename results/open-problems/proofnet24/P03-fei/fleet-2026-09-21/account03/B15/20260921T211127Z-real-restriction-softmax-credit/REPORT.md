# B15 — real-restriction softmax minority weighting and exact negative orientation credit

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role / interface:** account03/B15, joint interface D (conditional packet decompositions under real restrictions and the unpaid arithmetic/Shannon remainder).

## 0. Mandatory mechanism change and peer result actually consumed

The last three substantive account03/B15 reports were the punctured-subcube KL obstruction, the adjacent-mesh boundary attempt, and the global one-sided magnitude-flow reduction. None closed a new universal FEI implication. This run therefore does **not** continue the same aggregate one-sided-flow proof. It switches to an actual coordinate restriction and keeps the conditional packet information credit exactly.

The named cross-account result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260921T2003Z-kl-softmax-collision-credit/REPORT.md`, blob `4c1049ef0c4495991a48b556eedadde912d87503`.

That report proves that for a two-origin collision, with origin weights `(1-rho,rho)` and mesh-depth gap `g`, the **post-KL** residual is

\[
\Psi(\rho,g)=-\frac12\log_2\bigl(\rho+(1-\rho)4^{-g}\bigr).
\]

It also shows that this residual can remain linearly large in a generic remote collision, so the KL credit cannot simply be dropped.

A second input retained without re-proving is account02/B15's valuation-tail majorization, blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`: valuation depth and every valuation tail are already paid by folded influence. Thus a successful restriction argument should not split the total Fourier height into a separately paid valuation ledger and an independently upper-bounded mesh ledger before the information credits are spent.

The new result below applies the account01 softmax to a **genuine Fourier restriction pair**. The key difference is structural: in a real restriction the same post-KL softmax appears multiplied by the minority spectral mass. A potentially order-one packet-orientation entropy is then canceled exactly by a negative conditional mutual-information credit.

---

## 1. Real restriction pair and exact entropy drop

Let `f:{0,1}^n->{-1,+1}` and fix coordinate `i`. For every `T` not containing `i`, write

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad
m_T=u_T^2+v_T^2.
\]

When `m_T>0`, define the **minority mass fraction**

\[
q_T=\frac{\min\{u_T^2,v_T^2\}}{m_T}\in[0,1/2].
\]

Let `h_2` be binary entropy in bits and put

\[
j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right).
\]

### Theorem B15-REAL-RESTRICTION-01

The contribution of this pair to the restriction entropy drop

\[
\Delta_iH=H(f)-\frac{H(f_{i=0})+H(f_{i=1})}{2}
\]

is exactly

\[
\boxed{m_T\,[h_2(q_T)+j(q_T)]}.
\tag{1.1}
\]

Hence

\[
\boxed{
\Delta_iH=\sum_{T:i\notin T}m_T\,[h_2(q_T)+j(q_T)].
}
\tag{1.2}
\]

### Proof

The parent pair contributes

\[
\phi(u_T^2)+\phi(v_T^2)
=\phi(m_T)+m_T h_2(q_T),
\qquad \phi(x)=x\log_2(1/x).
\]

The two restrictions have Fourier coefficients `u_T+v_T` and `u_T-v_T`. Put

\[
r_\pm=\frac{(u_T\pm v_T)^2}{2m_T}
=\frac12\pm\operatorname{sgn}(u_Tv_T)\sqrt{q_T(1-q_T)}.
\]

Then `r_++r_-=1`, and the average child contribution is

\[
\frac12\phi((u_T+v_T)^2)+\frac12\phi((u_T-v_T)^2)
=\phi(m_T)-m_T+m_T h_2(r_+).
\]

Subtracting gives (1.1); `h_2(r_+)` is sign-independent. Summing over `T` gives (1.2). No integrality or lattice projection is used. QED.

---

## 2. Exact packet-orientation credit under an unordered magnitude-pair coarsening

Let `C=1_{i\in S}` for the root spectral sample `S`, and let `T=S\setminus\{i\}`. Then

\[
\Pr[T=t,C=0]=u_t^2,\qquad \Pr[T=t,C=1]=v_t^2.
\]

Coarsen `T` by the **unordered magnitude pair**

\[
F(T)=\{\,|u_T|,|v_T|\,\}.
\]

Fix one fibre with magnitudes `A>=B>=0`, and define

\[
q=\frac{B^2}{A^2+B^2}.
\]

Let `rho` be the conditional fraction of `T`'s in this fibre for which the coordinate-containing coefficient has magnitude `A` rather than `B`. Because every member of this fibre has the same marginal `T`-mass `A^2+B^2`, this is also the mass fraction of the two orientations.

### Theorem B15-ORIENTATION-CREDIT-02

On this fibre,

\[
\Pr[C=1\mid F]=q+\rho(1-2q),
\tag{2.1}
\]

and the exact negative information credit is

\[
\boxed{
I(C;T\mid F)
=h_2\!\bigl(q+\rho(1-2q)\bigr)-h_2(q).
}
\tag{2.2}
\]

Consequently

\[
\boxed{
H(C\mid F)-I(C;T\mid F)=h_2(q),
}
\tag{2.3}
\]

independently of the orientation imbalance `rho`.

### Proof

Conditional on the exact `T`, the membership probability of `C` is either `q` or `1-q`; both have entropy `h_2(q)`. Averaging the two orientations gives (2.1). Therefore

\[
H(C\mid T,F)=h_2(q),
\]

while `H(C|F)` is the first entropy in (2.2). The conditional mutual-information identity

\[
I(C;T\mid F)=H(C\mid F)-H(C\mid T,F)
\]

gives (2.2)-(2.3). QED.

### Why this matters

If the two orientations are nearly balanced and `q` is tiny, the coarse entropy `H(C|F)` is close to one full bit. Equation (2.2) says that this apparent cost is almost entirely a **negative information credit**: after the exact credit is retained, the surviving cost is only `h_2(q)`. Thus a packet proof that replaces `H(C|T)` by `H(C|F)` and drops `I(C;T|F)` loses precisely the cancellation demanded by the joint interface-D order.

---

## 3. Applying account01's post-KL softmax to the genuine restriction packet

For the same unordered pair `A>=B>0`, let

\[
g=\log_2(A/B).
\]

Because `q=B^2/(A^2+B^2)`,

\[
4^{-g}=\frac{B^2}{A^2}=\frac{q}{1-q}.
\]

Apply the account01 two-origin post-KL softmax with origin weights `(1-q,q)`. Its residual collapses exactly to

\[
\boxed{
\Psi(q)=\frac12\log_2\frac1{2q}.
}
\tag{3.1}
\]

The binary entropy has the exact identity

\[
\boxed{
h_2(q)=2q\Psi(q)+\eta(q),
\qquad
\eta(q)=q+(1-q)\log_2\frac1{1-q}.
}
\tag{3.2}
\]

This is the concrete application of the peer softmax to the **same normalized two-origin remainder** inside a real restriction. The generic collision residual is proportional to `Psi`; after the actual restriction orientation credit is kept, the surviving Shannon term carries the extra minority factor `q`.

There is no contradiction with the account01 remote-gap obstruction: that theorem concerns a generic recombination in which all source depth is infected by the finest origin. A Boolean coordinate restriction is a different operation, with the exact `u+v,u-v` interference in Section 1.

---

## 4. The new symmetric softmax current

Define

\[
\boxed{
W_i(f)=\sum_T m_Tq_T\Psi(q_T)
=\frac12\sum_T \min(u_T^2,v_T^2)
\log_2\frac{u_T^2+v_T^2}{2\min(u_T^2,v_T^2)}.
}
\tag{4.1}
\]

Also put

\[
M_i(f)=\sum_Tm_Tq_T=\sum_T\min(u_T^2,v_T^2).
\tag{4.2}
\]

Then

\[
M_i\le \min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}=:q_i.
\tag{4.3}
\]

Let

\[
B_i=H(1_{i\in S}\mid S\setminus\{i\})
=\sum_Tm_Th_2(q_T)
\]

be the spectral erasure entropy in coordinate `i`.

### Theorem B15-SOFTMAX-ERASURE-03

Exactly,

\[
\boxed{
B_i=2W_i+\sum_Tm_T\eta(q_T).
}
\tag{4.4}
\]

Moreover

\[
\boxed{
2W_i+M_i\le B_i
\le2W_i+\left(1+\frac1{\ln2}\right)M_i
\le2W_i+\left(1+\frac1{\ln2}\right)q_i.
}
\tag{4.5}
\]

Thus the unpaid part of the erasure/Shannon term is equivalent, up to an already influence-paid additive term, to the symmetric minority-weighted softmax current `W_i`.

### Proof

Equation (4.4) is (3.2) summed with weights `m_T`. Since

\[
q\le\eta(q)
\]

and

\[
(1-q)\log_2\frac1{1-q}
\le\frac{q}{\ln2},
\]

we have

\[
q\le\eta(q)\le\left(1+\frac1{\ln2}\right)q.
\]

Summation and (4.3) give (4.5). QED.

This is not merely a rename of `B_i`: it identifies its hard component as the post-KL softmax from the peer collision theorem, but with the exact real-restriction minority weighting and the orientation credit already spent.

---

## 5. PROVED scalar JS payment and a new full-FEI reduction

The other scalar term in (1.2) also has an influence-scale bound.

### Lemma B15-JS-SCALAR-04

For `0<=q<=1/2`,

\[
\boxed{
j(q)\le\frac{2}{\ln2}\,q.}
\tag{5.1}
\]

The constant is sharp as `q->0`.

### Proof

Put `x=2sqrt(q(1-q))`. In natural logs,

\[
j(q)\ln2
=\frac12[(1+x)\ln(1+x)+(1-x)\ln(1-x)].
\]

Also `2q=1-sqrt(1-x^2)`. Both sides vanish at `x=0`. The derivative of the first side is `artanh(x)`, while the derivative of the second is `x/sqrt(1-x^2)`. The latter dominates because their derivatives are respectively `1/(1-x^2)` and `1/(1-x^2)^{3/2}`, equal at zero and ordered thereafter. Hence (5.1). QED.

Combining (1.2), (3.2), (4.3), and (5.1) gives the universal restriction inequality

\[
\boxed{
\Delta_iH
\le 2W_i+\left(1+\frac3{\ln2}\right)q_i.
}
\tag{5.2}
\]

The scalar constant

\[
c_0=1+\frac3{\ln2}=5.32808512266689\ldots
\]

is sharp for this scalar decomposition as `q->0`.

Now define

\[
\mathcal W(f)=\sum_iW_i(f),\qquad
J(f)=\sum_i q_i.
\]

### CONDITIONAL Theorem B15-SYMMETRIC-SOFTMAX-REDUCTION-05

If there is a universal finite `kappa` such that

\[
\boxed{\mathcal W(f)\le\kappa J(f)}
\tag{5.3}
\]

for every Boolean `f`, then full FEI follows with

\[
\boxed{
H(f)\le\left(1+\frac3{\ln2}+2\kappa\right)I(f).
}
\tag{5.4}
\]

### Proof

Multiply `f` by the character that folds every spectral marginal to `q_i`. This preserves spectral entropy, `J`, and each unordered magnitude-pair statistic `W_i`, while the gauged function has total influence `J`.

Under (5.3), some relevant coordinate satisfies `W_i<=kappa q_i`. Equation (5.2) gives

\[
\Delta_iH\le(c_0+2\kappa)q_i.
\]

For the gauged function `q_i=Inf_i`, and the average total influence of the two restrictions is `I-Inf_i`. Induction on dimension yields (5.4), and `J(f)<=I(f)` returns the ordinary FEI form. QED.

A concrete currently-live target is

\[
\boxed{\mathcal W(f)\stackrel{?}{\le}\frac34J(f).}
\tag{5.5}
\]

It would imply full FEI with

\[
C=\frac52+\frac3{\ln2}=6.82808512266689\ldots.
\]

**Equation (5.5) is OPEN / CONJECTURAL, not proved here.**

---

## 6. Genuine Boolean counterexample test: constants <=0.7 are already false

The new statistic was stressed on width-two tribes, because this family is already difficult for restriction selectors but has an exact product spectrum.

Let `f_m` be OR of `m` disjoint two-variable AND blocks. Every coordinate has

\[
q_i=\alpha_m=\frac12\left(\frac34\right)^{m-1}.
\]

Put

\[
v_m^2=\frac14\left(\frac9{16}\right)^{m-1},\qquad
u_m^2=\left(1-2(3/4)^m\right)^2.
\]

For every coordinate the exact softmax current is

\[
\begin{aligned}
W_i
&=v_m^2\left[\left(\frac43\right)^{m-1}-1\right]\frac12\log_2 5\\
&\quad+\min(\nu_m^2,v_m^2)\frac12\log_2
\frac{\nu_m^2+v_m^2}{2\min(\nu_m^2,v_m^2)}.
\end{aligned}
\tag{6.1}
\]

The first term is all nonempty activity outside the selected block; there the two Fourier magnitudes have ratio exactly `3`. The second is the exceptional empty-frequency pair.

Since the family is transitive,

\[
\mathcal W/J=W_i/q_i.
\]

At `m=8` (`n=16`) equation (6.1) gives

\[
\boxed{\mathcal W/J=0.7090916890201119\ldots>0.7.}
\tag{6.2}
\]

Therefore any universal claim `mathcal W<=0.7 J` is **REFUTED**. This is a genuine Boolean obstruction, not a relaxed packet law.

The same exact formula gives

`0.193494, 0.301012, 0.442204, 0.601564, 0.675823, 0.704334, 0.709092, 0.701973, 0.689478, 0.675167, 0.660948`

for `m=2,...,12`, and

\[
\lim_{m\to\infty}\mathcal W/J=\frac14\log_2 5=0.5804820237218405\ldots.
\]

Thus the width-two tribes stress family does **not** refute the `3/4` target, but it shows the target has only modest room and rules out a tempting `1/2` or `0.7` theorem.

---

## 7. Independent current-run stress calculations

The companion checker computes only this new statistic and the new identities; it does not rerun the settled FEI/read-once certificate.

- Exhaustive Boolean truth tables through `n=4` give maximal `mathcal W/J` values `0` at `n=2`, `0.2902410118609203` at `n=3`, and `0.2956885087668035` at `n=4`.
- The hash-verified 18-variable Numaro seed (`f8a7bb2c...c7839`) has
  \[
  I=J=2.0390625,\qquad
  \mathcal W=0.9971418005023995,
  \qquad \mathcal W/J=0.48901973357972084.
  \]
  Its two coordinate classes have very unequal local behavior: the auxiliary class reaches about `W_i/q_i=1.8962273`, so a pointwise `W_i<=c q_i` with a small universal `c` is not the right statement even though the aggregate is moderate.
- Direct pairwise evaluation of (1.1) has maximum numerical discrepancy below `1.4e-16` through exhaustive `n<=4`, and below `2.1e-17` on the Numaro seed.

The checker file SHA-256 before repository write was

`98075dc0d969b875f784989a24ff2cfa5c0d07046fd22d49d3a941b8af2c1acb`.

These are implementation/stress checks, not finite proofs of the universal `3/4` target.

---

## 8. Relation back to valuation depth and the unpaid arithmetic remainder

For an unequal pair with magnitudes `A>=B`, the softmax parameter obeys

\[
\Psi(q)=\frac12\log_2\frac{A^2+B^2}{2B^2}
\le\log_2(A/B).
\tag{8.1}
\]

If the two magnitudes belong to spectral packets with total height

\[
h=r+d=\log_2(1/|\widehat f|),
\]

then the right side of (8.1) is the **coupled** height drop

\[
(r_B-r_A)+(d_B-d_A).
\]

The account02 valuation theorem already controls the complete valuation-depth law under spectral mass. The present restriction decomposition says the next arithmetic task is not to upper-bound the two signed pieces separately. First multiply the total height gap by the actual minority spectral mass and keep the packet-orientation mutual-information credit. Only after those operations is a valuation/mesh separation potentially safe.

This is the exact sense in which the peer valuation result has been applied to the same normalized remainder: valuation is treated as an already-paid component of the coupled height, while the remaining candidate `mathcal W` preserves the real-restriction minority weight and does not discard the negative information credit.

---

## 9. What is proved, refuted, and still open

### PROVED

1. Exact real-restriction pair decomposition (1.1)-(1.2).
2. Exact unordered-packet orientation credit (2.2)-(2.3).
3. Exact application of account01's post-KL softmax to a genuine restriction pair, including the minority factor (3.1)-(3.2).
4. Two-sided softmax representation of the spectral erasure term (4.4)-(4.5).
5. Sharp scalar JS payment `j(q)<=2q/ln2` and restriction inequality (5.2).
6. Conditional implication `mathcal W<=kappa J => FEI` with constant `1+3/ln2+2kappa`.
7. Exact width-two-tribes formula (6.1).

### REFUTED

A universal `mathcal W<=0.7J` bound: width-two tribes with `m=8` gives `0.709091689...`.

### OPEN / CONDITIONAL

The concrete aggregate target

\[
\mathcal W\le\frac34J
\]

remains open. Full FEI remains **OPEN / NOT PROVED**.

---

## 10. Next attack / joint handoff

The next attack should stay on interface D but work with `mathcal W`, not return to the refuted raw normalizer or credit-free arithmetic interpolation.

1. Partition `W_i` by spectral packet pairs and keep the exact orientation credit from Section 2.
2. Apply account02's all-cost valuation majorization only after the minority edge mass has been formed, seeking a bound on the valuation portion of `mathcal W` that does not multiply packet depth by ambient edge degree.
3. The remaining mesh term should then be attacked with the fibre KL/softmax credit, not by a raw maximum gap.
4. Stress every proposed constant against width-two tribes (`0.709091689...`) and the Numaro auxiliary coordinates (`1.896...` locally).

A full proof of `mathcal W<=3J/4` would already give a finite universal FEI constant `6.828085...`; a Boolean counterexample above `3/4` would decisively redirect the route.

**consumed_peer_artifact:** `account01/B15/20260921T2003Z-kl-softmax-collision-credit/REPORT.md` (`4c1049ef0c4495991a48b556eedadde912d87503`), with account02/B15 valuation-tail majorization (`7633ed3dca15ea17d4c17af94e621f4ab3745691`) retained as the valuation input.

**applied_to_claim:** exact coordinate-restriction Shannon/erasure remainder after unordered magnitude-pair conditioning, with `-I(C;T|F)` retained.

**remaining_implication:** prove or refute a dimension-free aggregate bound `mathcal W<=kappa J`; concrete next target `kappa=3/4`.

**next_recipient:** `account01/B15` (feed back the real-restriction minority weighting of its post-KL softmax); account02/B15 can then attempt the valuation-tail payment after minority weighting.

**full_problem_change:** `OPEN -> OPEN`.

**mechanism_change:** `global one-sided magnitude flow -> real-restriction conditional packetization with exact negative orientation credit and minority-weighted post-KL softmax`.
