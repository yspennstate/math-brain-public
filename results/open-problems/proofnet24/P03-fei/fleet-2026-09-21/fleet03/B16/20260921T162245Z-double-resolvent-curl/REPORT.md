# B16 FEI signed transport — double-resolvent three-curvature transport

**Date:** 21 September 2026  
**Scope:** `fleet03 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact game-theoretic transport identities and a sharp energy theorem; no novelty or publication-priority claim.

## 0. Route change and entering state

This run read the owner-required `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` before substantive work. It also consumed the newest compatible signed-transport state rather than rechecking the read-once certificate.

The relevant entering facts are:

1. fleet04 proved that the difference between ordinary fine-player Shapley and the exact dummy-invariant block-coupled selector is **purely third-and-higher signed curvature**. For a Harsanyi dividend touching `s` clone pairs, with `r` of those pairs doubled, its refinement coefficient has squared norm at most `1/(8s)`;
2. fleet03 rewrote the internal first-hit bank as an exact inverse-number noisy-plaquette resolvent, with prefix/suffix antisymmetry and the terminal mixed difference kept inside the signed plaquette field;
3. fleet04 rewrote the low radial Hardy bank as a central two-sided Ward transform of the same signed plaquette-plus-terminal field;
4. fleet01 proved exact original-coordinate q-flip Radon/energy-distance payments for the central odd channel. The remaining missing map is from the **fully refunded compiler curvature** to those physical-cut frequencies.

The previous selector work still left an all-orders object: its Harsanyi formula contains every mixed dividend of order at least three. The new route below eliminates that all-orders appearance **exactly**. The entire ordinary-Shapley/block-selector discrepancy is the divergence of an antisymmetric current whose current on each pair of clone blocks is a **double inverse-number resolvent of genuine third finite differences**. For the retained compiler, those third differences are a signed curl of the plaquette-plus-terminal field.

This is not full FEI: the resulting third-curvature current still needs a dimension-free payment by the authentic original-coordinate q-flip/Radon/noisy-square banks.

No R32 coefficient is absolute-valued. Negative entropy credits remain signed. The original q-flip coordinates, dual-code multiplicities, R16 moment refunds and terminal-band accounting are not altered or spent twice.

---

## 1. Paired game and the known refinement defect

Let a finite cooperative game `V` have `m` labeled clone pairs

\[
P_a=\{a0,a1\},\qquad a=1,\ldots,m.
\]

Write its Harsanyi expansion as

\[
V(S)=\sum_{T\subseteq S} d(T).
\tag{1.1}
\]

For a fine coalition `T`, define

\[
S(T)=\{a:T\cap P_a\ne\varnothing\},\qquad
s(T)=|S(T)|,
\]

and the doubled and single touched blocks

\[
D(T)=\{a:P_a\subseteq T\},\qquad
U(T)=S(T)\setminus D(T),
\]

with

\[
r(T)=|D(T)|,
\qquad |T|=s(T)+r(T).
\tag{1.2}
\]

Let `Psi_a` be the aggregate of the two ordinary fine-player Shapley values in `P_a`, and let `Phi_a` be the Shapley value of block `P_a` in the coarse game obtained by restricting `V` to unions of whole pairs.

The fleet04 refinement theorem gives, dividend by dividend,

\[
\Psi_a-\Phi_a
=\sum_{T:a\in S(T)}d(T)w_a(T),
\tag{1.3}
\]

where, writing `s=s(T)`, `r=r(T)`,

\[
w_a(T)=
\begin{cases}
\displaystyle \frac{s-r}{s(s+r)},&a\in D(T),\\[5pt]
\displaystyle -\frac{r}{s(s+r)},&a\in U(T).
\end{cases}
\tag{1.4}
\]

and `sum_a w_a(T)=0`. The new question is whether this zero-sum coefficient vector has an exact transport structure that retains the inverse support factors instead of paying it by a generic norm estimate.

---

## 2. `P03-B16-SHAPLEY-MINIMUM-CURRENT` — **PROVED**

For distinct clone blocks `a,b`, define an antisymmetric current

\[
\boxed{
J_{ab}:=
\sum_T\frac{d(T)}{s(T)|T|}
\left[
1_{\{a\in D(T),\ b\in U(T)\}}
-
1_{\{b\in D(T),\ a\in U(T)\}}
\right].
}
\tag{2.1}
\]

Then `J_ab=-J_ba`.

### Theorem 2.1 — exact divergence

For every paired game,

\[
\boxed{
\Psi_a-\Phi_a
=\sum_{b\ne a}J_{ab}
\qquad(a=1,\ldots,m).
}
\tag{2.2}
\]

#### Proof

It is enough to check one Harsanyi dividend `d=d(T)`. Put `s=s(T)`, `r=r(T)`, so `|T|=s+r`.

If `a in D(T)`, the current sends

\[
\frac{d}{s(s+r)}
\]

to each of the `s-r` single touched blocks. Its divergence at `a` is therefore

\[
(s-r)\frac{d}{s(s+r)}
=d\,w_a(T).
\]

If `a in U(T)`, it receives that amount from each of the `r` doubled blocks, giving

\[
-r\frac{d}{s(s+r)}
=d\,w_a(T).
\]

Untouched blocks receive zero. Summing dividends proves (2.2). `square`

Thus the refinement defect is not merely zero-sum: every mixed dividend transports its signed mass **only from doubled touched blocks to single touched blocks**, with exact edge amount

\[
\boxed{d(T)/(s(T)|T|).}
\tag{2.3}
\]

No positive part, absolute dividend, path length or synthetic distance is introduced.

### Theorem 2.2 — minimum-energy current for one dividend

For one dividend, let

\[
\delta_a(T):=d(T)w_a(T).
\]

On the complete graph of the `s` touched blocks, the current in (2.3) is exactly

\[
\boxed{
J_{ab}(T)=\frac{\delta_a(T)-\delta_b(T)}s.
}
\tag{2.4}
\]

Consequently it is the unique minimum-energy antisymmetric current with divergence `delta(T)`, and

\[
\boxed{
\sum_{a<b}J_{ab}(T)^2
=\frac1s\sum_a\delta_a(T)^2
=\frac{d(T)^2r(s-r)}{s^2(s+r)^2}
\le\frac{d(T)^2}{8s^2}.
}
\tag{2.5}
\]

The constant `1/8` is sharp whenever `r=s/3` is integral.

#### Proof

For a doubled block and a single block,

\[
w_D-w_U
=\frac{s-r+r}{s(s+r)}
=\frac1{s+r},
\]

while blocks of the same type have equal `w`. This proves (2.4).

For any antisymmetric current `F` with `div F=delta`, write

\[
J_{ab}=\varphi_a-\varphi_b,
\qquad \varphi_a=\delta_a/s.
\]

If `H=F-J`, then `div H=0`, and discrete integration by parts gives

\[
\sum_{a<b}J_{ab}H_{ab}
=\sum_a\varphi_a\,\operatorname{div}H(a)=0.
\]

Hence `||F||_2^2=||J||_2^2+||H||_2^2`, proving minimality. The complete-graph identity

\[
\sum_{a<b}(\delta_a-\delta_b)^2
=s\sum_a\delta_a^2
\]

uses `sum_a delta_a=0` and gives the first equality in (2.5). Inserting (1.4) gives

\[
\sum_a w_a^2
=\frac{r(s-r)}{s(s+r)^2}.
\]

Finally, with `x=r/s`,

\[
s^2\frac{r(s-r)}{s^2(s+r)^2}
=\frac{x(1-x)}{(1+x)^2}
\le\frac18,
\]

with equality at `x=1/3`. `square`

This strengthens the previous `1/sqrt{s}` coefficient observation: after passing to the **correct transport current**, the squared current scale is `1/s^2`, not merely `1/s`.

---

## 3. A genuine two-parameter thinning law

The two inverse counts in (2.3) can both be generated by honest probability interpolation.

For `0<=x,y<=1`, put the following law on one clone pair `(X_0,X_1)`:

\[
\boxed{
\begin{aligned}
\nu_{x,y}(11)&=xy^2,\\
\nu_{x,y}(10)&=\nu_{x,y}(01)=xy(1-y),\\
\nu_{x,y}(00)&=1-2xy+xy^2.
\end{aligned}
}
\tag{3.1}
\]

All four probabilities are nonnegative and sum to one. Moreover

\[
\Pr(X_0=1)=\Pr(X_1=1)=xy,
\qquad
\Pr(X_0=X_1=1)=xy^2.
\tag{3.2}
\]

Therefore, if a fine set `T` uses exactly one clone from a given pair, the probability that this local requirement is present is `xy`; if it uses both clones, the probability is `xy^2`. Across independent pairs,

\[
\boxed{
\Pr(T\subseteq R_{x,y})=x^{s(T)}y^{|T|}.
}
\tag{3.3}
\]

This is precisely the joint generating law for **touched-pair support** and **fine-player degree**.

---

## 4. `P03-B16-DOUBLE-RESOLVENT-THREE-CURVATURE` — **PROVED**

Fix distinct clone blocks `a,b`. Let `R_{x,y}^{a,b}` sample every pair other than `a,b` independently according to (3.1), while every clone in `P_a union P_b` is held absent.

For `epsilon in {0,1}`, use the forward finite difference convention

\[
\Delta_qV(S)=V(S\cup\{q\})-V(S).
\]

Define the oriented third-curvature source

\[
\boxed{
Q_{a\to b}(x,y)
:=xy^2\sum_{\epsilon=0}^1
\mathbb E\,
\Delta_{a0}\Delta_{a1}\Delta_{b\epsilon}
V(R_{x,y}^{a,b}).
}
\tag{4.1}
\]

### Theorem 4.1 — exact oriented resolvent

For every paired game,

\[
\boxed{
Q_{a\to b}(x,y)
=
\sum_{\substack{T:\ a\in D(T)\\ b\in U(T)}}
 d(T)x^{s(T)-1}y^{|T|-1}.
}
\tag{4.2}
\]

Consequently

\[
\boxed{
J_{ab}
=\int_0^1\!\int_0^1
\left[Q_{a\to b}(x,y)-Q_{b\to a}(x,y)\right]
\,dx\,dy.
}
\tag{4.3}
\]

Thus every third-and-higher Harsanyi term in the selector mismatch has been resummed into **third finite differences only**, with two exact inverse-number resolvents.

#### Proof

Apply the third difference in (4.1) to one Harsanyi monomial `1_{T subseteq S}`.

It vanishes unless both clones of `a` lie in `T` and exactly the chosen clone `b epsilon` lies in `T`; if the other clone of `b` also lies in `T`, it remains absent in every term of the difference and the monomial is identically zero. Hence summing `epsilon` selects exactly the dividends with `a in D(T)` and `b in U(T)`, each once.

For such a `T`, the remaining requirement `T minus {a0,a1,b epsilon}` lies in the random pairs outside `a,b`. By (3.3), its inclusion probability is

\[
x^{s(T)-2}y^{|T|-3}.
\]

Multiplication by the prefactor `xy^2` gives

\[
x^{s(T)-1}y^{|T|-1},
\]

proving (4.2). Integrating uses

\[
\int_0^1x^{s-1}dx\int_0^1y^{|T|-1}dy
=\frac1{s|T|},
\]

which is exactly the current coefficient (2.1). `square`

### Meaning of the two resolvents

The `y` integral inserts `1/|T|`, the familiar fine-player inverse number operator. The new `x` integral inserts the **independent pair-support inverse** `1/s(T)`. Both are necessary: one counts selected fine generators and the other counts physically redundant clone blocks.

This is the main advance of the run. The all-order selector correction is no longer an uncontrolled endpoint sum of complete-pair Fourier frequencies; it is an integrated third-curvature current with both combinatorial multiplicities already inverted.

---

## 5. `P03-B16-PLAQUETTE-CURL-FACTORISATION` — **PROVED**

Apply the preceding theorem to the retained compiler game

\[
G=E-R_d,
\]

for which the inherited exact plaquette-plus-terminal field is

\[
\mathcal P_{uv}(S)
:=\kappa_{g_S}(g_u,g_v)+\Delta_{uv}R_d(g_S),
\qquad
\Delta_{uv}G=-\mathcal P_{uv}.
\tag{5.1}
\]

No terminal split is made.

For two clone blocks `a,b`, define

\[
\boxed{
\begin{aligned}
\Xi_{ab}(x,y):=
\sum_{\epsilon=0}^1\mathbb E\big[
&-\Delta_{b\epsilon}\mathcal P_{a0,a1}(R_{x,y}^{a,b})\\
&+\Delta_{a\epsilon}\mathcal P_{b0,b1}(R_{x,y}^{a,b})
\big].
\end{aligned}
}
\tag{5.2}
\]

Then (4.1) gives

\[
Q_{a\to b}-Q_{b\to a}=xy^2\Xi_{ab}(x,y).
\]

Hence the fine/block selector discrepancy of the full retained compiler is exactly

\[
\boxed{
J_{ab}^{G}
=\int_0^1\!\int_0^1xy^2\Xi_{ab}(x,y)\,dx\,dy,
\qquad
\Psi_a(G)-\Phi_a(G)=\sum_{b\ne a}J_{ab}^{G}.
}
\tag{5.3}
\]

Equation (5.3) is a signed **curl-divergence factorisation**:

- the q-flip plaquette-plus-terminal field is differentiated once more, producing a three-curvature curl;
- the double resolvent integrates that curl into an antisymmetric current;
- the selector refinement defect is the divergence of that current.

Every sign remains inside `Xi_ab` until the final square or payment. In particular, R32 `0 mod 4` debits and `2 mod 4` negative credits are not separated; the terminal mixed difference remains inside `mathcal P`; and no q-flip is replaced by an abstract Hamming path.

A direct current-energy consequence, with no triangle inequality inside the curl, is

\[
\boxed{
\sum_{a<b}(J_{ab}^{G})^2
\le\frac16
\sum_{a<b}\int_0^1\!\int_0^1
xy^2\,\Xi_{ab}(x,y)^2\,dx\,dy,
}
\tag{5.4}
\]

because `integral_0^1 integral_0^1 x y^2 dx dy=1/6` and weighted Cauchy--Schwarz applies to each **signed net curl** `Xi_ab`.

Equation (5.4) does **not** by itself bound the divergence vector: a generic conversion from current energy to divergence energy on an `m`-vertex complete graph costs a factor `m`. The point of (5.3) is to expose the exact current before that lossy step, so that it can be routed directly into the original-coordinate cut/Radon bank.

---

## 6. Attempted refutation: one resolvent is not enough

A natural shortcut is to keep only the fine-player inverse degree `1/|T|` and omit the pair-support inverse `1/s(T)`. This is **REFUTED** as a dimension-free transport mechanism.

Take a single signed dividend with

\[
s=30,\qquad r=10,\qquad |T|=s+r=40.
\]

For every doubled-to-single touched-block edge, the exact current is

\[
\frac1{s|T|}=\frac1{1200}.
\]

The one-resolvent shortcut would put

\[
\frac1{|T|}=\frac1{40}
\]

on each such edge, an amplitude overpayment by `s=30`.

There are `r(s-r)=200` transport edges. Therefore

\[
\boxed{
\mathcal E_{\rm exact}=\frac1{7200},
\qquad
\mathcal E_{\rm one\ resolvent}=\frac18,
}
\tag{6.1}
\]

an **energy overpayment factor `900=s^2`**.

This family also saturates the sharp bound in (2.5):

\[
\mathcal E_{\rm exact}=\frac1{8s^2}.
\]

So the extra pair-support resolvent is not a cosmetic improvement. It removes a genuine quadratic support loss at the exact extremal ratio `r/s=1/3`.

The older generic endpoint-`L2` shortcut remains dead as well: the pair-correlation handoff already exhibited exponentially growing endpoint evaluation norm on arbitrary games. Formula (4.3) avoids that endpoint by integrating the third curvature with the exact two inverse-number factors instead.

---

## 7. Exact finite falsification checks

`check_double_resolvent_transport.py` was compiled/executed locally with exact rational arithmetic. It does not rerun any FEI certificate.

It checked:

- direct fine-player Shapley versus direct coarse-block Shapley on deterministic rational games with 2, 3 and 4 clone pairs, and verified equality with the divergence in (2.2);
- 60 exact rational `(x,y)` evaluations of the genuine pair-thinning law (3.1), comparing direct expected third differences to the generating polynomial (4.2);
- all 1,225 single-dividend types `2<=s<=50`, `1<=r<s`, verifying the exact energy identity (2.5) and the sharp `1/(8s^2)` current bound;
- the `s=30,r=10` one-resolvent obstruction, obtaining exact current energy `1/7200` versus `1/8`, ratio `900`.

The sharp scaled current energy `1/8` occurs at every tested `r=s/3`, beginning `(s,r)=(3,1)` and ending `(48,16)` in the tested range.

These checks are falsification evidence. Theorems 2.1--5.1 are algebraic proofs and do not rely on finite enumeration.

---

## 8. Relation to the newest three-face physical bridge

A concurrent fleet03/B12 continuation found, on every Boolean function of a physical 3-cube, exact pair-inclusion agreement between the spectral sample and the physical sensitivity set, and an exhaustively sharp local cubic defect bound `|d_3|<=I_face/6` on that 3-cube.

The present theorem makes a three-face interface structurally relevant: **all** higher selector-refinement orders have now been reduced to integrated third finite differences. However, the B12 local statement is about triples of genuine physical cube coordinates, whereas the three differences in (5.2) are differences in actual q-flip generator coordinates. A q-flip generator is generally not one physical coordinate. Therefore the B12 constant cannot simply be inserted into (5.4); doing so would silently discard the original-coordinate geometry.

The next bridge must explicitly pass the signed q-flip three-curvature curl through the established q-flip Radon transform to physical derivative/sensitivity frequencies. This is exactly where dual-code multiplicity and the fleet01 central odd multiplier theorem should enter.

---

## 9. Status ledger

### **PROVED**

- `P03-B16-SHAPLEY-MINIMUM-CURRENT`: the ordinary-fine versus block-coupled Shapley defect is exactly the divergence of the signed current (2.1).
- For each Harsanyi dividend, that current is the unique minimum-energy complete-graph flow and has sharp energy at most `d(T)^2/(8s(T)^2)`.
- `P03-B16-DOUBLE-RESOLVENT-THREE-CURVATURE`: all third-and-higher refinement orders are exactly resummed into third finite differences under the genuine two-parameter pair-thinning law (3.1).
- `P03-B16-PLAQUETTE-CURL-FACTORISATION`: for the retained compiler, the current is the double-resolvent integral of the signed curl of the plaquette-plus-terminal field.
- the signed current-energy bound (5.4), which squares only after prefix/suffix/terminal cancellation has been retained inside `Xi_ab`.

### **REFUTED / DEAD AT ITS EXACT SCOPE**

- paying this selector transport with only the fine-degree inverse resolvent `1/|T|`; it can overpay current energy by `s^2`, with exact factor `900` already at `s=30,r=10`;
- the previously killed generic coupled-endpoint `L2` estimate remains dead;
- this run does not revive diagonal-only plaquette, absolute-correlation transport, pointwise q-flip load, or raw Poincare shortcuts.

### **PRESERVED / UNSPENT**

- signed R32 cancellation and negative entropy credits;
- original-coordinate physical disagreement geometry;
- dual-code relation multiplicity;
- R16 moment/high-resolvent refunds;
- the separate terminal-band payment. `Delta^2 R_d` stays inside `mathcal P` in (5.2)--(5.4).

### **OPEN**

Full FEI remains **OPEN / NOT PROVED**. No universal influence bound for the current in (5.3) has yet been proved.

---

## 10. Next attack

The precise next target is no longer an all-order Shapley/Harsanyi estimate. It is the **three-curvature q-flip-to-physical bridge**:

> express the signed curl `Xi_ab(x,y)` of (5.2), after the legitimate translated/pivoted q-flip basis averaging, as an original-coordinate cut/Radon multiplier and prove a dimension-independent square payment by the existing fractional noisy-square / central energy-distance bank, while retaining the terminal term in the same transform.

There are two concrete tests.

1. **Positive route.** Derive the physical Walsh multiplier of the basis-averaged third-curvature current. If it has a uniform odd-frequency envelope after the two inverse-number factors, fleet01's central Radon-energy theorem can pay it without counting q-flip channels.
2. **Kill route.** Search for an authentic Boolean family where that *fully refunded double-resolvent* multiplier still grows with dimension. The old raw `Theta(n)` multiplier and the generic endpoint game are not valid counterexamples because the Ward refunds and both resolvents remove exactly those mechanisms.

The most useful new structural fact for that next calculation is that only a signed **third** curvature has to be mapped. Higher selector orders have already been integrated away exactly.