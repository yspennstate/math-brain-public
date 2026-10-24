# B16 FEI signed transport — full-Borel payment of relation-resolved physical-translation oscillation

**Run:** `20260921T230508Z-b16-fei-c11`  
**Scope:** account01 / B16, joint FEI interface C, signed transport / noise interpolation  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Scientific master refreshed before write:** `08301dc36102395dc741ff1d9c779ede7c0b9ac7`  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** one new universal full-Borel dimension-free payment theorem for the relation-resolved translation-oscillatory source, one exact physical-plaquette mean identity, and one explicit obstruction showing the translation-invariant mean cannot be discarded. No novelty or publication-priority claim.

## 0. Why this run changes representation

The immediately preceding account01/B16 report,

`account01/B16/20260921T225305Z-quarterturn-selfphase/REPORT.md`,

reorganized the retained R32/terminal source into a quarter-turn characteristic-function packet and proved that the one self-phase extension `RM(1,n)+<b_f>` annihilates the terminal law pointwise. It also proved a microscopic `s^4 J` envelope, but the oscillatory logarithmic corridor remained open. The current joint state makes clear that another positive scalar-current estimate is the wrong next move: the genuine half-band Boolean family of the account02 interactive package has positive live current divided by `J` tending to infinity while still satisfying `H<4I`.

This run therefore keeps **individual dual relation labels** through the physical-translation step instead of compressing them to one scalar shell packet.

The named compatible other-account result consumed substantively is:

`proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260921T223248Z-relation-orientation-lift/REPORT.md`

(blob `ba900d4cc7cb6c7e2757b8983b3c1960577dea0e`).

That report proves for every even relation `A` the physical-translation inequality

\[
\operatorname{Inf}_i(h_A)\le |A|\,j_i,\qquad
h_A(y)=\prod_{x\in A} f(x+y),
\]

and consequently, for the authentic relation-resolved R32 packet

\[
V_s(y)=\bigl(r_A(s)\nu_A(y)\bigr)_A,
\quad
\nu_A(y)=\frac{1-h_A(y)}2,
\]

the pointwise-in-time Hilbert bound

\[
\mathbb E_y\|V_s-\mathbb EV_s\|_2^2
\le
J(f)\,N x\,\Pr[\mathrm{Bin}(N-1,x)\ge3],
\qquad x=\sin^2(s/N).
\tag{0.1}
\]

The report deliberately left the Borel integration and the translation-invariant mean open. The present run closes the first of those two pieces.

I also use the account04/B16 finite-resolvent no-reuse split

\[
w_{<2}(s)+w_{>2}(s)=\frac4{s^3}
\]

and its live/outside-live partition, and the account02/B16 Hodge--Shapley/ordered-flag result

`account02/B16/20260921T224955Z-hodge-shapley-flag-ladder/REPORT.md`

(blob `56c1829a0188eb2966db00bc9ece806c99676b7b`),

which identifies the still-missing mean-side target: compiler-authorized nonreusing physical `3/1` Hodge/q-flip incidences.

**Mechanism change:** from scalar characteristic-function / positive-current control to a relation-resolved physical-translation centering before the Borel square.

---

## 1. Relation-resolved source and the inherited pointwise physical bound

Let the truth-table cube have size

\[
N=2^n\ge4.
\]

Let `D` be any relation code contained in

\[
C_0=RM(1,n)^\perp.
\]

Thus every nonzero `A in D` has even cardinality at least four. Let `mathcal A` be any subfamily of such relations; it may include gate-separation and retained-terminal predicates, because deleting relation coordinates can only decrease the Hilbert norms below.

For a Boolean phase `f:F_2^n->{-1,1}`, put

\[
h_A(y)=\prod_{x\in A} f(x+y),
\qquad
\nu_A(y)=\frac{1-h_A(y)}2.
\tag{1.1}
\]

For Borel time `s`, let

\[
\theta=\frac{s}{N},
\qquad
r_A(s)=2\sigma_A
\sin^{|A|}\theta\,
\cos^{N-|A|}\theta,
\tag{1.2}
\]

where `sigma_A in {+1,-1}` is arbitrary. In the authentic source it contains the R32 factor `(-1)^{|A|/2}` and any fixed gate orientation. Define

\[
V_s(y)=\bigl(r_A(s)\nu_A(y)\bigr)_{A\in\mathcal A}.
\tag{1.3}
\]

The account03/B17 even-relation translation theorem gives

\[
\boxed{
\mathbb E_y\|V_s-\mathbb EV_s\|_2^2
\le
\frac{J(f)}4\sum_{A\in\mathcal A}|A|r_A(s)^2.
}
\tag{1.4}
\]

Writing

\[
x=\sin^2(s/N),
\]

and enlarging `mathcal A` to all subsets of cardinality at least four,

\[
\frac14\sum_A |A|r_A(s)^2
\le
S_N(x):=
\sum_{k=4}^N
k\binom Nk x^k(1-x)^{N-k}.
\tag{1.5}
\]

The exact binomial identity is

\[
\boxed{
S_N(x)
=
Nx\,\Pr[\mathrm{Bin}(N-1,x)\ge3].
}
\tag{1.6}
\]

Two elementary consequences are

\[
\boxed{
S_N(x)\le Nx,
}
\tag{1.7}
\]

and, by the third falling-factorial moment,

\[
\boxed{
S_N(x)
\le
\frac{N(N-1)(N-2)(N-3)}6\,x^4
\le
\frac{N^4}{6}x^4.
}
\tag{1.8}
\]

These inequalities preserve the signed R32 phase inside each relation coordinate until the final Hilbert square; no scalar shell total variation is introduced.

---

## 2. NEW THEOREM — the entire full-Borel translation-oscillatory bank is paid by `J`

### Theorem 2.1 — `P03-B16-RELATION-BOREL-OSCILLATION`

For every Boolean `f`, every relation family `mathcal A subset C_0`, and every choice of signs `sigma_A` in (1.2),

\[
\boxed{
4\int_0^\infty
\frac{
\mathbb E_y\|V_s(y)-\mathbb EV_s\|_2^2
}{s^3}\,ds
\le
C_N J(f),
}
\tag{2.1}
\]

where

\[
\boxed{
C_N=
\frac{
2\log N+\frac83-\frac23\log6
}{N}.
}
\tag{2.2}
\]

In particular, because `N=2^n>=4`,

\[
\boxed{
C_N\le C_4
=
1.0611872690219362\ldots <1.062,
}
\tag{2.3}
\]

and

\[
C_N=O\!\left(\frac{\log N}{N}\right).
\tag{2.4}
\]

Thus the full low+high Borel energy of the **physical-translation fluctuation** of the relation-resolved R32 packet is dimension-free and in fact vanishes with truth-table size.

### Proof

By (1.4)--(1.8),

\[
\mathbb E\|V_s-\mathbb EV_s\|_2^2
\le J(f)S_N(\sin^2(s/N)).
\tag{2.5}
\]

Set

\[
s_0=6^{1/6}\sqrt N,
\qquad
s_1=N.
\]

For `N>=2`, `s_0<=s_1`.

#### Small Borel scale: `0<s<=s_0`

Using (1.8) and `|sin u|<=u`,

\[
S_N(\sin^2(s/N))
\le
\frac{N^4}{6}\left(\frac{s}{N}\right)^8
=
\frac{s^8}{6N^4}.
\]

Hence

\[
4\int_0^{s_0}\frac{S_N}{s^3}\,ds
\le
\frac{4}{6N^4}\int_0^{s_0}s^5\,ds
=
\frac{s_0^6}{9N^4}
=
\frac{2}{3N}.
\tag{2.6}
\]

#### Intermediate scale: `s_0<=s<=N`

Using (1.7) and again `|sin(s/N)|<=s/N`,

\[
S_N\le N\sin^2(s/N)\le\frac{s^2}{N}.
\]

Therefore

\[
\begin{aligned}
4\int_{s_0}^{N}\frac{S_N}{s^3}\,ds
&\le
\frac4N\int_{s_0}^{N}\frac{ds}{s}\\
&=
\frac{
2\log N-\frac23\log6
}{N}.
\end{aligned}
\tag{2.7}
\]

#### Large scale: `s>=N`

The trivial bound `S_N<=N` gives

\[
4\int_N^\infty\frac{S_N}{s^3}\,ds
\le
4N\int_N^\infty s^{-3}\,ds
=
\frac2N.
\tag{2.8}
\]

Adding (2.6)--(2.8) proves (2.1)--(2.2).

For real `N>=4`, the derivative of `(2 log N+c)/N`, with `c=8/3-(2/3)log 6`, is negative, so (2.3) follows by evaluating `N=4`. QED.

### Interpretation

The account02/account04 half-band obstruction does **not** contradict this theorem. Their divergent object is the already-compressed positive current. Theorem 2.1 pays a different, finer object: the physical-translation-centered, relation-labelled packet before the relation identities are collapsed into a scalar source and before a positive current is formed.

This distinction is exactly why the relation labels cannot be discarded too early.

---

## 3. Live/high/outside-window no-reuse corollary

Let `w(s)` be any nonnegative Borel multiplier satisfying

\[
0\le w(s)\le\frac4{s^3}.
\]

Then Theorem 2.1 immediately gives

\[
\boxed{
\int_0^\infty
w(s)\,
\mathbb E\|V_s-\mathbb EV_s\|_2^2\,ds
\le C_NJ(f).
}
\tag{3.1}
\]

More importantly, if

\[
w_L+w_H+w_O=\frac4{s^3}
\tag{3.2}
\]

is the **actual account04 no-reuse partition**

\[
w_L=1_Ww_{<2},
\qquad
w_H=w_{>2},
\qquad
w_O=1_{W^c}w_{<2},
\]

then

\[
\boxed{
\sum_{\rho\in\{L,H,O\}}
\int
w_\rho(s)
\mathbb E\|V_s-\mathbb EV_s\|_2^2\,ds
\le C_NJ(f).
}
\tag{3.3}
\]

Thus the live low, R16/high and outside-live pieces may all be carried separately without paying the centered relation bank three times. Their **sum** is paid once by (2.1).

No terminal term or negative R32 credit is used to prove (3.3); they remain available for the mean component and the authentic compiler compatibility problem.

---

## 4. Operator corollary — what the compiler still has to prove

The result survives any relation-space contraction.

Let `T_s` be a linear operator on the relation-coordinate Hilbert space which commutes with physical translation and satisfies

\[
\|T_s\|_{2\to2}\le M
\]

for every `s`. Then

\[
\boxed{
4\int_0^\infty
\frac{
\mathbb E\|
T_s(V_s-\mathbb EV_s)
\|_2^2
}{s^3}\,ds
\le
M^2C_NJ(f).
}
\tag{4.1}
\]

This is immediate from Theorem 2.1.

Consequently the account03/B17 remaining implication has become quantitatively explicit on the centered subspace:

> it is enough to prove that the authentic refunded relation-to-active-syndrome / Hodge-parent operator has a dimension-free `l_2` norm on the physical-translation-centered relation subspace.

If that operator is contractive (`M<=1`), the complete low/high/live/outside centered source costs less than `1.062 J`, and its cost actually decays like `(log N)/N`.

The remaining difficulty is therefore **not** Borel integration on this subspace.

---

## 5. NEW exact mean identity for physical q-flip plaquettes

The translation-invariant mean is not mysterious once a relation has actually been identified with a physical q-flip plaquette.

Fix a physical coordinate `i` and a displacement `w` with `w_i=0`. Let

\[
Q_{i,w}(x)
=
\{x,x+e_i,x+w,x+w+e_i\}.
\]

Put

\[
h_{i,w,x}(y)
=
f(y+x)f(y+x+e_i)f(y+x+w)f(y+x+w+e_i),
\]

and

\[
\nu_{i,w,x}(y)=\frac{1-h_{i,w,x}(y)}2.
\]

Let

\[
\eta_i(z)
=
\frac{1-f(z)f(z+e_i)}2
\]

be the physical sensitivity-support bit. Then pointwise,

\[
\nu_{i,w,x}(y)
=
{\bf1}\{\eta_i(y+x)\ne\eta_i(y+x+w)\}.
\tag{5.1}
\]

Therefore

\[
\boxed{
\mathbb E_y\nu_{i,w,x}(y)
=
p_i(w),
}
\tag{5.2}
\]

where

\[
p_i(w)
=
\Pr_y[\eta_i(y)\ne\eta_i(y+w)]
\]

is exactly the support-disagreement channel in account03/B18's oriented physical curvature

\[
\kappa_i(w)=p_i(w)+4o_i(w).
\tag{5.3}
\]

In particular,

\[
\boxed{
\mathbb E\nu_{i,w,x}\le\kappa_i(w).
}
\tag{5.4}
\]

### Proof

Write

\[
e_i(z)=f(z)f(z+e_i)=1-2\eta_i(z).
\]

Then

\[
h_{i,w,x}(y)
=e_i(y+x)e_i(y+x+w).
\]

For two `+/-1` bits, their product is `-1` exactly when the corresponding `0/1` bits differ. This is (5.1), and averaging proves (5.2). QED.

This is the exact mean-side companion to Theorem 2.1: if the account02 Hodge--Shapley Gap A can map every charged source relation nonreusingly to its authentic ordered physical q-flip, the translation-invariant mean is already in the `p_i(w)` part of the same physical `kappa` bank.

---

## 6. RIGOROUS OBSTRUCTION — centering alone can erase the entire source

The mean in Section 5 cannot be declared negligible or reconstructed from the centered variance.

Take, in any dimension `n>=2`,

\[
f(x)=(-1)^{x_1x_2},
\]

with all other coordinates dummy, and take the physical plaquette

\[
Q=\{0,e_1,e_2,e_1+e_2\}.
\]

The second derivative of the quadratic phase is constant, so for every translation `y`,

\[
\boxed{
\prod_{x\in Q}f(x+y)=-1.
}
\tag{6.1}
\]

Thus

\[
\nu_Q(y)\equiv1,
\qquad
\nu_Q-\mathbb E\nu_Q\equiv0.
\tag{6.2}
\]

The entire relation packet lies in the translation-invariant mean and contributes **zero** to Theorem 2.1's centered bank.

At the same time,

\[
\operatorname{Inf}_1(f)=\operatorname{Inf}_2(f)=\frac12,
\]

all dummy-coordinate influences vanish, and hence

\[
\boxed{J(f)=1.}
\tag{6.3}
\]

By (5.2),

\[
p_1(e_2)=1.
\]

So the missing mean is a genuine physical q-flip flag, not a pathology and not an FEI counterexample.

This refutes the stronger shortcut

> “after keeping relation labels, discard their physical-translation means and pay only the centered relation variance.”

That shortcut can delete the whole source even on a two-variable quadratic phase. A complete interface-C proof must route the mean separately into the physical q-flip/orientation bank or into an exactly nonreused signed terminal/R16 companion.

---

## 7. What the new theorem changes in the joint interface-C chain

The current smallest honest chain is now:

1. **signed retained source / R32 relation expansion:** already proved by account01/account04;
2. **keep relation labels through physical translation:** forced by account03/B17's exact scalar-shell non-identifiability example;
3. **translation-centered relation packet -> full low/high/live/outside Borel payment:** **PROVED HERE**, with cost
   \[
   C_NJ(f),\qquad C_N<1.062;
   \]
4. **physical q-flip relation mean -> support-disagreement channel:** **PROVED HERE** by (5.2);
5. **compiler-authorized nonreusing Hodge/q-flip cover:** still OPEN; this is account02/B16 Gap A;
6. **terminal Hodge defect and the `0/4`,`2/2` sectors, with high/outside ledger retained exactly:** still OPEN.

This materially narrows the source-side problem. Once Gap A is proved, the two parts of a relation coordinate have natural sinks:

\[
\nu_A
=
(\nu_A-\mathbb E\nu_A)+\mathbb E\nu_A.
\]

The first is paid by Theorem 2.1; for an authenticated physical plaquette, the second is exactly `p_i(w)` and is paid by the signed physical-flag bank.

The remaining risk is **operator amplification / compatibility**, not the Borel corridor itself. In particular, one must not infer from (2.1) that the already-compressed scalar positive current is `O(J)`; the genuine half-band counterexample remains decisive against that false statement.

---

## 8. Exact computation

The companion standard-library checker

`check_relation_borel_oscillation.py`

was executed before repository delivery. It verifies:

- `708` exact rational binomial identities/envelope inequalities for (1.6)--(1.8);
- `2,336` exhaustive Boolean physical-plaquette checks through dimension three, confirming (5.2);
- the constant-plaquette quadratic obstruction for dimensions `2` through `6`, always with `J=1`;
- numerical universal-shell Borel integrals for `N=4,8,16,32,64`, all strictly below the analytic bound.

The analytic constants are

\[
\begin{array}{c|cccccccc}
N&4&8&16&32&64&128&256&1024\\
\hline
C_N&
1.06119&
0.70388&
0.43858&
0.26261&
0.15297&
0.08731&
0.04907&
0.01498.
\end{array}
\]

Executed source SHA-256:

`7067190827be0fefd6d3091f8b00b1be7f2113dae1097edec89fd68514df3cf2`

Executed stdout SHA-256:

`2d9ecea62c1035bc199bf0173123864e3bf27ab7541ff12a4b4a34c2ebccba0a`

The numerical integrals are diagnostics only. Theorem 2.1 and the plaquette identity are analytic.

---

## 9. Classification and next handoff

### PROVED

1. The full `4/s^3` Borel integral of the relation-resolved physical-translation-centered R32 packet is at most
   \[
   \frac{2\log N+\frac83-\frac23\log6}{N}J(f)<1.062J(f).
   \]
2. The same payment is no-reuse compatible with the actual live-low / high-R16 / outside-live Borel partition.
3. Any uniformly `l_2`-bounded relation-space compiler operator inherits the same centered payment.
4. For an authentic physical q-flip plaquette, the translation-invariant frustration mean equals exactly the physical support-disagreement probability `p_i(w)`.
5. Centering alone is insufficient: the quadratic phase `(-1)^{x_1x_2}` has a plaquette with constant frustration one and zero centered fluctuation.

### NOT PROVED

- a compiler-authorized nonreusing Hodge/q-flip cover for every charged doubled parent;
- a dimension-free operator norm for the full refunded relation-to-active-syndrome map;
- payment of every terminal Hodge defect and the non-`1/3` square sectors;
- full FEI.

### Next B16 target

Use the account02 Hodge--Shapley ladder **before** same-syndrome scalar compression and test its exact action on

\[
V_s-\mathbb EV_s
\quad\text{and}\quad
\mathbb EV_s
\]

separately.

The first target is now concrete: prove the ladder/clone transition is an `l_2` contraction (or has a fixed norm) on the centered relation space, which would close that entire source component by (4.1).

For the mean component, prove that the same nonreusing Hodge assignment actually produces the ordered physical q-flip `Q_{i,w}` required by (5.2). If it does, its source mean goes directly to `p_i(w)<=kappa_i(w)`. If it does not, produce the smallest genuine doubled-parent syndrome for which the mean cannot be represented by the parent flag; that would identify the missing signed correction rather than returning to the refuted positive-current target.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
