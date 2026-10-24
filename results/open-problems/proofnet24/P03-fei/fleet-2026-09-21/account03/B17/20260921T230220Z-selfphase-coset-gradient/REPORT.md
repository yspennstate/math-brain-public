# B17 FEI interface-C adversary — self-phase terminal-zero obstruction and coset-gradient replacement

**Run:** `20260921T230220Z-B17-fei11-8b736ec2`  
**Scope:** account03 / B17, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Route:** **NEW C-SELF-PHASE-COSET-GRADIENT**. This changes method from the preceding B17 relation-orientation and finite-moment obstructions. It does not repeat an exhaustive Boolean sweep.

## 0. Exact target and completed peer result consumed

The current interface-C problem is not to bound a raw positive current: that all-Boolean route is already refuted. The live question is whether the signed finite-window source can be transported to physical influence before the final square while retaining terminal, R16, R32 and outside-window companions.

**consumed_peer_artifact:** account01/B16,
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T225305Z-quarterturn-selfphase/REPORT.md`, source commit `5bee3ad064bbb4afab3743cf1d64148cc0c5e017`, with the subsequent handoff at `8aa870c86e6b2f0d5761beaea4333011c2f72fa7`.

The peer proves, for every linear mask code `M` containing `RM(1,n)`, the exact quarter-turn characteristic packet
\[
\Xi_{M,b}(s)=\mathbb E_M\cos(s\beta_0)-\mathbb E_M\cos(s\beta_b),
\]
its entropy transform, and the self-phase fact
\[
b\in M\quad\Longrightarrow\quad \Xi_{M,b}\equiv0,\qquad \Theta_M(b)=0.
\]
In particular the one-generator extension `RM(1,n)+<b_f>` kills the terminal characteristic packet exactly, while after minimizing-character gauge the physical boundary of the truth mask is `J(f)`.

**applied_to_claim:** I test whether this exact terminal annihilation is enough to make the remaining positive live packet universally `O(J)`. It is not. I then keep the self-phase extension **before positivity** and derive a signed code-coset gradient with a dimension-free `J/N` local window payment.

I also use the already-completed account03/B16 finite-window amplitude theorem only as a local analytic input: its derivative bound and exact dual-code second moment. No peer PASS label is promoted to full FEI.

---

## 1. PROVED — exact self-phase code-coset gradient identity

Let `M <= F_2^N` be a linear mask code containing `RM(1,n)`, let a Boolean phase be
\[
f(x)=(-1)^{b_x},
\]
and define the index-at-most-two self-phase extension
\[
M^+=M+\langle b\rangle.
\]
Let `Phi_f(m)` be **any** scalar or Hilbert-valued gate functional whose phase dependence is only through the signed truth-table entries
\[
f(x)(-1)^{m_x}.
\]
Let `Phi_1` denote the same functional for the comparator phase `1`.

### Theorem 1.1 — `P03-B17-SELF-PHASE-COSET-GRADIENT`

For every such functional,
\[
\boxed{
\mathbb E_M\Phi_f-\mathbb E_{M^+}\Phi_f
=\frac12\,\mathbb E_M(\Phi_f-\Phi_1).
}
\tag{1.1}
\]
Equivalently, if `D_b Phi_f(m)=Phi_f(m)-Phi_f(m+b)`, then
\[
\boxed{
\mathbb E_M\Phi_f-\mathbb E_{M^+}\Phi_f
=\frac12\mathbb E_M D_b\Phi_f.
}
\tag{1.2}
\]
If `b in M`, both sides vanish.

### Proof

For every `m`,
\[
f(x)(-1)^{m_x+b_x}=(-1)^{m_x},
\]
so exactly
\[
\Phi_f(m+b)=\Phi_1(m).
\tag{1.3}
\]
If `b notin M`, the extension is the disjoint union `M^+=M union (M+b)`, hence
\[
\mathbb E_{M^+}\Phi_f
=\frac12\mathbb E_M\Phi_f+
 \frac12\mathbb E_M\Phi_f(m+b)
=\frac12(\mathbb E_M\Phi_f+\mathbb E_M\Phi_1).
\]
Rearrangement proves (1.1). If `b in M`, translation by `b` permutes `M`; then `E_M Phi_f=E_M Phi_1`, so the same formula gives zero. QED.

This is a signed **pre-square** identity. It does not positive-part any Borel time, relation, parent or syndrome.

---

## 2. PROVED — finite-window self-phase gradient has a local `J/N` payment

Fix any truth-table gate partition `Q`, and for a mask `m` write the two signed cell amplitudes `(u_f(m),v_f(m))` and comparator amplitudes `(u_0(m),v_0(m))`. For a finite resolvent interval `0<=A<B`, use the authentic scalar kernel
\[
K_{[A,B]}(u,v)
=F_{[A,B]}((u+v)^2)-F_{[A,B]}((u-v)^2),
\]
with
\[
F_{[A,B]}(x)=\int_A^B\frac{x}{x+t}\,dt.
\]
Set
\[
\Gamma_{[A,B]}
:=\mathbb E_M K_{[A,B]}(u_f,v_f)
 -\mathbb E_{M^+}K_{[A,B]}(u_f,v_f).
\tag{2.1}
\]

The completed finite-window amplitude theorem gives pointwise
\[
|K_f-K_0|^2
\le16(\sqrt B-\sqrt A)^2(\delta u^2+\delta v^2),
\tag{2.2}
\]
and, because `M` contains `RM(1,n)`, exact orthogonality gives
\[
\mathbb E_M(\delta u^2+\delta v^2)=\frac{4|E|}{N^2},
\tag{2.3}
\]
where `E={x:f(x)=-1}` after choosing a global sign.

### Theorem 2.1 — `P03-B17-SELF-PHASE-WINDOW-J-SINK`

In the minimizing-character gauge,
\[
\boxed{
|\Gamma_{[A,B]}|^2
\le \frac{8(\sqrt B-\sqrt A)^2}{N}\,J(f).
}
\tag{2.4}
\]
Equivalently,
\[
\boxed{
N|\Gamma_{[A,B]}|^2
\le8(\sqrt B-\sqrt A)^2J(f).
}
\tag{2.5}
\]
For the low window `[0,T]`,
\[
N|\Gamma_{[0,T]}|^2\le8T J(f),
\tag{2.6}
\]
and at the live split `T=2`,
\[
\boxed{N|\Gamma_{[0,2]}|^2\le16J(f).}
\tag{2.7}
\]

### Proof

By Theorem 1.1,
\[
\Gamma_{[A,B]}=\frac12\mathbb E_M(K_f-K_0).
\]
Jensen and (2.2) yield
\[
|\Gamma|^2
\le4(\sqrt B-\sqrt A)^2
 \mathbb E_M(\delta u^2+\delta v^2)
=\frac{16(\sqrt B-\sqrt A)^2|E|}{N^2}.
\tag{2.8}
\]
Multiplying `f` by a character only translates the affine mask average, so both sides of the code-coset identity are invariant under the legitimate minimizing-character gauge. Choose that gauge and the global sign so `|E|<=N/2`. Then `I(f_gauged)=J(f)`, while edge isoperimetry gives
\[
\frac{2|E|}{N}\le I(f_{gauged})=J(f).
\tag{2.9}
\]
Substitution into (2.8) proves (2.4). QED.

The significance is structural: the `N` normalization that was dangerous after scalar parent compression is already canceled for **one exact self-phase code step** before positivity. The surviving issue is nonreusing aggregation across the authentic doubled-parent/Hodge ladder, not the local finite-window logarithm.

---

## 3. Exact admissible Boolean stress tests

The accompanying standard-library checker performs no exhaustive search. It uses exact `RM(1,4)` masks and four exact Boolean functions: the previous sign-changing B17 witness, a one-point defect, a character, and the constant function.

For the sign-changing witness
\[
Q=\{0,3,4,7,9,10,12,15\},\qquad
E=\{0,1,3,5,10,12,14,15\},
\]
it obtains exactly
\[
J=3/2,\qquad
\mathbb E_M(\delta u^2+\delta v^2)=1/8=4|E|/16^2.
\]
The finite-window self-phase gradient stays **negative**, so the replacement theorem does not smuggle in positivity. At `T=1/8,1/4,1/2,2`, respectively,
\[
\Gamma=-0.01267078462838,
-0.01394647195714,
-0.01267078462838,
-0.00627095923319.
\]
The exact coset averaging identity is satisfied to floating roundoff; the squared values are far below the analytic bound (2.6).

For the one-point defect, `J=1/2` and the exact amplitude second moment is `1/64`. For a character, `J=0`, `b in RM(1,4)`, so `M^+=M` and `Gamma=0` exactly; the constant boundary is also zero. These boundary cases are important: the set-size-to-`J` step must be made **after** character gauge, while the code-coset identity itself already collapses characters to zero.

Checker SHA-256: `c73ce159d53a5b8d88a4f669d3785f30e6da7244d1ce551d0846b7525b95000b`.  
Recorded-output SHA-256: `502fe9b3e2ebc9d6d4dbe65107e59a5934f7c62cb9bfd676718312a8755978f6`.

---

## 4. REFUTED — exact terminal annihilation does not make the remaining positive live packet `O(J)`

The peer self-phase theorem makes a tempting bridge plausible:

> **False bridge.** Once the terminal code is extended by the Boolean truth phase so that `Theta_M(b)=0`, the remaining retained positive live triple packet is bounded by `C J(f)` with a universal constant.

This is false even for exact admissible Boolean functions.

Take the genuine half-band Boolean family from the completed account02 collision theorem. With `D>=128`, put
\[
n=D-1,\quad N=2^D,\quad d=\lceil D/2\rceil,
\]
and let `f_D=1-2 1_Q` where `Q` is the stated affine two-plane. It has
\[
J(f_D)=I(f_D)=\frac{8n}{N},\qquad H(f_D)<4I(f_D).
\tag{4.1}
\]
Let
\[
P_0=RM(1,D),\qquad P_1=RM(d,D),\qquad
P_2=P_1+\langle b_{f_D}\rangle.
\tag{4.2}
\]
By the consumed account01 theorem,
\[
\boxed{\Theta_{P_2}(b_{f_D})=0.}
\tag{4.3}
\]

For one of the exact charged active triples `R`, write `b_R^{P,h}` for the active coefficient with code `P` and Boolean phase `h`. The same coset identity gives
\[
\boxed{
b_R^{P_2,f_D}
=\frac12\left(b_R^{P_1,f_D}+b_R^{P_1,1}\right).}
\tag{4.4}
\]
The account02 bounded-independence collision lemma applies with an arbitrary bounded dependent multiplier and is unchanged by multiplication by a fixed sign pattern. Therefore **both** terms on the right of (4.4) obey, on the live interval, the same norm bound
\[
E_1\le \frac{4\pi T^3}{\sqrt m},
\qquad T=(2n)^{-1/2},\quad m=2^{d-1}-1.
\tag{4.5}
\]
Hence by Minkowski
\[
\|b_R^{P_2,f_D}\|_{L^2(ds/s^3)}\le\sqrt{E_1}.
\tag{4.6}
\]
For the affine base code, the same completed theorem proves on `[NT/2,NT]`
\[
E_0:=\|b_R^{P_0,f_D}\|^2_{L^2(ds/s^3)}
\ge\frac{21T^6}{131072},
\tag{4.7}
\]
and for every `D>=128`, `E_1<=E_0/4`. Therefore the retained coefficient after the terminal-zero self-phase extension satisfies
\[
\begin{aligned}
\|b_R^{P_0,f_D}-b_R^{P_2,f_D}\|^2
&\ge(\sqrt{E_0}-\sqrt{E_1})^2\\
&\ge E_0/4.
\end{aligned}
\tag{4.8}
\]
Using the same normalized charged-triple factor `4/9`, this one exact triple already gives the positive packet lower bound
\[
\boxed{
\frac49\int_{NT/2}^{NT}
\frac{|b_R^{P_0,f_D}(s)-b_R^{P_2,f_D}(s)|^2}{s^3}\,ds
\ge\frac{7}{3145728\,n^3}.}
\tag{4.9}
\]
Its ratio to `J=8n/2^D` diverges exponentially.

### Classification of this obstruction

**REFUTED:** terminal annihilation by itself implies an all-Boolean `O(J)` bound on the retained positive triple/live packet.

**NOT REFUTED:** FEI; the source family itself has `H/I<4`.

**NOT CLAIMED:** that inserting `P_2` into every existing compiler stage leaves every other compiler multiplier unchanged. Equation (4.9) is an exact source-packet obstruction to the proposed *terminal-zero sufficiency lemma*, not a relabeling of the already-refuted complete positive-current theorem.

This distinction matters: the terminal-zero extension is useful only if its signed coset difference is exploited **before** the final positive packet is formed.

---

## 5. Replacement mechanism and exact remaining implication

The failed bridge suggests the replacement directly:

1. introduce the self-phase extension while the gate is still signed;
2. replace the terminal remainder by the exact coset gradient (1.1), rather than by a positive retained-current norm;
3. use the local normalized bound (2.5) at each legitimate gate/window;
4. only after the authentic doubled-parent/Hodge allocation has been shown nonreusing, send the residual square to the ordered physical flag bank.

This is genuinely different from the preceding B17 relation-shell, moment-credit and orientation-counting attacks: it uses the **quotient `M^+/M` itself as a signed one-bit martingale direction**.

**remaining_implication:** prove that the authentic doubled-parent/Hodge-Shapley compiler admits a nonreusing aggregation of these self-phase coset gradients, with the existing live low/high split, outside-window term, negative R32 shells, R16 credits and terminal bookkeeping co-located, so that summing the local `N^{-1}` bound does not recreate an `N`, codimension or parent-multiplicity loss.

A particularly sharp target is to show that the Hodge ladder from account02/B16 can be realized as a martingale sequence of compatible code-coset gradients whose quadratic variations sum at most a universal constant times `J(f)`. The present report proves the one-step inequality and proves that **post-square terminal killing is insufficient**; it does not prove the multi-step nonreuse theorem.

**next_recipient:** `account02/B16` for the Hodge-Shapley/nonreuse compatibility, with `account03/B16` and `account03/B18` for live-window signed aggregation and proof integration. `account01/B16` is the source-side self-phase compatibility reference.

**Full FEI remains OPEN / NOT PROVED.**
