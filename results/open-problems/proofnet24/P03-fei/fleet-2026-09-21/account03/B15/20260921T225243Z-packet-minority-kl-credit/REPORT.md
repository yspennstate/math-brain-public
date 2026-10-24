# B15 — exact packet-minority KL cancellation under genuine coordinate restrictions

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive-brain retrieval or receiver-context use entered this mathematics.

**Role / interface:** account03/B15, joint interface D: conditional packet decompositions under real restrictions and the actual unpaid arithmetic/Shannon remainder.

**Scientific base refreshed before delivery:** `a003049664a4233768660d9b33d6f3fca86b4a69` on `master`.

## 0. Mechanism change and peer result consumed

The last several B15 reductions had left the same universal implication in different forms: control the real-restriction minority softmax current

\[
\mathcal W(f)=\sum_i W_i(f)
\]

by folded influence. Rather than try another credit-free positive upper bound, this run changes method and puts the **negative information credit back inside the actual restriction-local remainder**.

The named completed other-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260921T222602Z-zero-valuation-height-tilt-obstruction/REPORT.md`

(blob `f85d23ec06d69416084fe742c8fc710f74910a15`). It proves on the genuine one-point Boolean family that after the valuation escort, both directions of the **global** physical-height KL tilt are exponentially too large relative to influence, even though every packet valuation is zero. Its exact conclusion is that a correct interface-D proof must preserve `positive normalizer - forward information credit` to exponentially small relative scale. The same report also observes that the account03 real-restriction current `W` stays tiny on that family.

I apply that warning here to the same normalized real-restriction expression and obtain an exact local `normalizer - KL` identity. The resulting KL is not the bad global height-tilt divergence: it is a relative entropy between two probability laws on **actual unordered magnitude-pair packets seen by one genuine coordinate restriction**.

I also retain the account02/B15 all-cost valuation theorem

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260921T170301Z-valuation-tail-majorization/REPORT.md`

(blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`). The new packet KL admits an exact chain-rule split into a valuation-pair credit and a conditional physical-mesh credit, so this is now the correct point at which valuation information can enter without discarding the remaining negative credit.

No automatic physical projection integrality is assumed anywhere below.

---

## 1. Genuine restriction edge laws

Let

\[
f:\{0,1\}^n\to\{-1,+1\},\qquad p_S=\widehat f(S)^2.
\]

Fix a physical coordinate `i`. Index the Fourier-cube `i`-edges by `T` not containing `i`, and write

\[
x_T=p_T,\qquad y_T=p_{T\cup\{i\}},\qquad m_T=x_T+y_T,
\]

\[
s_T=\min(x_T,y_T),\qquad q_T=\frac{s_T}{m_T}\in[0,1/2]
\]

when `m_T>0`. Since every Fourier atom occurs in exactly one such edge,

\[
\sum_T m_T=1.
\tag{1.1}
\]

Let `F_i(T)` be the exact **unordered magnitude-pair packet label**

\[
F_i(T)=\{\,|\widehat f(T)|,|\widehat f(T\cup\{i\})|\,\}.
\]

For a packet-pair type `t`, define

\[
\pi_i(t)=\sum_{T:F_i(T)=t}m_T,
\qquad
b_i(t)=\sum_{T:F_i(T)=t}s_T.
\tag{1.2}
\]

Then `pi_i` is a probability law. Because the exact two magnitudes are fixed on one fibre `t`, the minority fraction `q_t` is fixed there and

\[
b_i(t)=q_t\pi_i(t).
\tag{1.3}
\]

Put

\[
M_i=\sum_Ts_T=\sum_t b_i(t).
\tag{1.4}
\]

When `M_i>0`, define the normalized **minority packet law**

\[
\mu_i(t)=\frac{b_i(t)}{M_i}.
\tag{1.5}
\]

The inherited real-restriction softmax current is

\[
W_i=rac12\sum_Ts_T\log_2\frac{m_T}{2s_T}.
\tag{1.6}
\]

Zero-minority edges contribute zero.

---

## 2. PROVED: the real-restriction softmax is exactly normalizer minus packet KL

### Theorem B15-PACKET-MINORITY-KL-01

For every coordinate with `M_i>0`,

\[
\boxed{
2W_i
=M_i\left[
\log_2\frac1{2M_i}
-D_{\rm KL,2}(\mu_i\|\pi_i)
\right].
}
\tag{2.1}
\]

For `M_i=0`, both sides are defined to be zero.

### Proof

On packet type `t`, (1.3) gives

\[
q_t=\frac{b_i(t)}{\pi_i(t)}
=M_i\frac{\mu_i(t)}{\pi_i(t)}.
\]

Therefore

\[
\begin{aligned}
2W_i
&=\sum_t b_i(t)\log_2\frac1{2q_t}\\
&=M_i\sum_t\mu_i(t)
\left[
\log_2\frac1{2M_i}
-\log_2\frac{\mu_i(t)}{\pi_i(t)}
\right]\\
&=M_i\left[
\log_2\frac1{2M_i}-D_{\rm KL,2}(\mu_i\|\pi_i)
\right].
\end{aligned}
\]

QED.

### Exact sufficiency of the packet-pair label

The same identity can be written first on the full edge set. Let

\[
\bar\pi_i(T)=m_T,\qquad \bar\mu_i(T)=s_T/M_i.
\]

Then

\[
D(\bar\mu_i\|\bar\pi_i)=D(\mu_i\|\pi_i).
\tag{2.2}
\]

Indeed, within one exact pair packet `t`, `s_T/m_T=q_t` is constant, so

\[
\bar\mu_i(\,\cdot\mid F_i=t)=\bar\pi_i(\,\cdot\mid F_i=t).
\]

The conditional KL in the chain rule is therefore exactly zero. Thus (2.1) loses **no information at all** by passing from individual Fourier edges to exact unordered magnitude-pair packets.

This is the source-exact conditional packet decomposition requested by interface D.

---

## 3. PROVED: two distinct negative information credits in the Shannon remainder

Let `S` be the root spectral sample, let

\[
C=1_{\{i\in S\}},\qquad T=S\setminus\{i\},
\]

and retain the unordered magnitude-pair label `F_i=F_i(T)`.

The preceding account03/B15 restriction theorem proved that on a packet type with minority fraction `q`, if `rho` is the fraction of the two orientations, then

\[
I(C;T\mid F_i=t)
=h_2(q+\rho(1-2q))-h_2(q).
\]

Consequently the spectral erasure entropy is exactly

\[
B_i:=H(C\mid T)
=H(C\mid F_i)-I(C;T\mid F_i)
=\sum_t\pi_i(t)h_2(q_t).
\tag{3.1}
\]

This is the first negative credit: it removes spurious orientation entropy created by forgetting which exact Fourier edge occurred.

Now put

\[
\eta(q)=q+(1-q)\log_2\frac1{1-q}.
\]

The exact scalar identity

\[
h_2(q)=q\log_2\frac1{2q}+\eta(q)
\tag{3.2}
\]

combined with (2.1) yields a second exact representation:

### Theorem B15-TWO-CREDIT-SHANNON-02

\[
\boxed{
B_i
=M_i\left[
\log_2\frac1{2M_i}-D_{\rm KL,2}(\mu_i\|\pi_i)
\right]
+\sum_t\pi_i(t)\eta(q_t).
}
\tag{3.3}
\]

Thus a coarse packet proof has two different information cancellations available:

1. `-I(C;T|F_i)`, which refunds **orientation mixing within a fixed unordered magnitude pair**;
2. `-M_i D(mu_i||pi_i)`, which refunds the **global minority-normalizer cost across different magnitude-pair packets**.

They are not the same credit and should not be dropped or merged into an unsigned packet count.

The exact restriction entropy drop is

\[
\Delta_iH
=B_i+\sum_t\pi_i(t)j(q_t),
\tag{3.4}
\]

where

\[
j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right).
\]

Therefore the actual unpaid restriction remainder has the exact packet form

\[
\boxed{
\Delta_iH
=M_i\left[
\log_2\frac1{2M_i}-D_{\rm KL,2}(\mu_i\|\pi_i)
\right]
+\sum_t\pi_i(t)[\eta(q_t)+j(q_t)].
}
\tag{3.5}
\]

No packet integrality assumption enters (3.5).

---

## 4. Applying the peer sharp restriction kernel: a narrow paid residual

The completed account01/B15 genuine-restriction theorem

`account01/B15/20260921T140113Z-restriction-gap-carry-vulnerability/REPORT.md`

proves for each restriction edge, with large squared magnitude `A^2` and small squared magnitude `B^2`, the sharp sandwich

\[
B^2\log_2\frac{A^2}{B^2}+4B^2
\le\delta(A,B)
\le
B^2\log_2\frac{A^2}{B^2}+\frac3{\ln2}B^2.
\tag{4.1}
\]

For one edge with minority fraction `q`, its logarithmic-gradient term differs from the present `2W` term by

\[
B^2\log_2\frac{A^2}{B^2}
-
B^2\log_2\frac{A^2+B^2}{2B^2}
=B^2\log_2(2(1-q)),
\]

which lies in `[0,B^2]`. Summing and using (2.1) gives the new packet-KL sandwich

### Corollary B15-PACKET-REMAINDER-SANDWICH-03

\[
\boxed{
M_i\left[
\log_2\frac1{2M_i}-D(\mu_i\|\pi_i)+4
\right]
\le \Delta_iH
}
\tag{4.2}
\]

and

\[
\boxed{
\Delta_iH
\le
M_i\left[
\log_2\frac1{2M_i}-D(\mu_i\|\pi_i)
+1+\frac3{\ln2}
\right].
}
\tag{4.3}
\]

This is a real restriction, exact-packet version of the interface-D arithmetic/Shannon remainder. The only nonconstant term is now an explicit `positive minority normalizer - negative packet KL` difference; the remaining scalar residue costs only a universal multiple of `M_i`, and `M_i<=min(Inf_i,1-Inf_i)`.

---

## 5. PROVED: valuation/mesh separation can be done inside the KL by chain rule

Every exact magnitude packet `a` already carries its signed packet valuation `r_a`. For a magnitude-pair type

\[
t=\{a,b\},
\]

let `V_i(t)` record the corresponding valuation pair, ordered by the smaller/larger Fourier magnitude if needed to make the map deterministic.

Because `V_i` is a deterministic coarsening of `F_i`, the KL in (2.1) splits exactly:

\[
\boxed{
D(\mu_i\|\pi_i)
=D(\mu_i^V\|\pi_i^V)
+\sum_v\mu_i^V(v)
D(\mu_i(\cdot\mid v)\|\pi_i(\cdot\mid v)).
}
\tag{5.1}
\]

Both terms are nonnegative.

This is the safe way to separate the already-controlled valuation/carry structure from the still-unpaid physical mesh structure. It does **not** split a signed height gap into two independently positive edge charges. Instead it keeps the negative information credit intact and resolves it into

- a valuation-pair information credit; and
- a conditional within-valuation physical-mesh information credit.

The account02 valuation-tail theorem is an input for the first factor, but it does not by itself lower-bound that KL. The zero-valuation family below shows why the second term is indispensable: all valuation labels there are identical, so the first KL is zero while the entire cancellation occurs in the conditional mesh KL.

---

## 6. Application to the consumed account01 zero-valuation obstruction

Take the peer family

\[
f_n(0)=1,\qquad f_n(x)=-1\quad(x\ne0),\qquad N=2^n.
\]

The peer report proves that all packet valuations are zero and that the global second-stage physical-height forward/reverse KL divergences are order `n`, while `I=2n/N` and `H/I->4`.

For a fixed coordinate, however, the actual restriction has

\[
M_i=\frac2N.
\tag{6.1}
\]

There are only two unordered magnitude-pair classes. Writing `U` for the unique large-small edge class and `E` for the equal-small class,

\[
\pi_i(U)=\frac{N^2-4N+8}{N^2},
\qquad
\pi_i(E)=\frac{4N-8}{N^2},
\tag{6.2}
\]

while the minority packet law is

\[
\mu_i(U)=\frac2N,
\qquad
\mu_i(E)=1-\frac2N.
\tag{6.3}
\]

A direct simplification gives

\[
\boxed{
D(\mu_i\|\pi_i)
=n-2-rac2N\log_2\frac{N^2-4N+8}{8}.
}
\tag{6.4}
\]

But

\[
\log_2\frac1{2M_i}=n-2.
\tag{6.5}
\]

Thus the packet KL cancels the entire order-`n` minority normalizer, leaving only

\[
\boxed{
2W_i
=\frac4{N^2}\log_2\frac{N^2-4N+8}{8}.
}
\tag{6.6}
\]

This is exactly the tiny real-restriction current observed by the consumed peer report. The cancellation is not heuristic: (6.4)-(6.6) show where the negative information goes.

At `n=20`, the positive normalizer term is

\[
M_i\log_2(1/(2M_i))=3.4332275390625\times10^{-5},
\]

whereas `2W_i=1.3460519584097774e-10`; their ratio is about `255059.064965`. The packet KL is `17.999929428111084` bits in the normalized bracket. A positive-only estimate would therefore lose more than five orders of magnitude even at this moderate dimension.

This calculation **does not prove FEI**. It proves that the new packet KL is exactly the restriction-local negative credit needed to survive the strongest current zero-valuation obstruction.

---

## 7. A second stress test: width-two tribes needs an unbounded packet-KL refund

For width-two tribes with `m` blocks, the previous account03/B15 exact spectrum gives, for `m>=4`,

\[
M_i=q_i=\frac12\left(\frac34\right)^{m-1}.
\tag{7.1}
\]

Hence

\[
\log_2\frac1{2M_i}=(m-1)\log_2\frac43.
\tag{7.2}
\]

The exact prior formula also gives

\[
\frac{W_i}{q_i}\longrightarrow\frac14\log_2 5.
\tag{7.3}
\]

By (2.1), therefore,

\[
\boxed{
D(\mu_i\|\pi_i)
=(m-1)\log_2\frac43
-2\frac{W_i}{M_i}
}
\tag{7.4}
\]

and so

\[
D(\mu_i\|\pi_i)
=(m-1)\log_2\frac43-rac12\log_2 5+o(1).
\tag{7.5}
\]

The packet KL grows linearly and cancels an unbounded raw normalizer, leaving a bounded softmax payment.

At the previously extremal tested `m=8` point,

\[
M_i=0.066741943359375,
\]

\[
\log_2(1/(2M_i))=2.9052624949519066,
\]

\[
D(\mu_i\|\pi_i)=1.4870791169116828,
\]

and

\[
2W_i/M_i=1.4181833780402238.
\]

So even the family that refutes `mathcal W<=0.7J` relies on a large negative packet information credit. This makes a credit-free `M_i log(1/M_i)` summation the wrong target.

---

## 8. Current-run computation / counterexample test

A new standard-library checker independently constructed exact integer Walsh spectra, exact unordered magnitude-pair classes, the edge law `pi_i`, the minority law `mu_i`, `W_i`, and the restriction kernel.

It exhaustively checked every Boolean truth table through `n=4` (65,812 functions total). Results:

- maximum numerical discrepancy in (2.1): `2.7755575615628914e-17`;
- violations of the upper restriction inequality derived from (3.5): `0` at floating-point tolerance;
- reproduced maximal `mathcal W/J`: `0` (`n=1,2`), `0.2902410118609203` (`n=3`), `0.2956885087668035` (`n=4`).

The same checker evaluated the one-point family at `n=3,4,8,12,20`; the normalizer-to-surviving-current ratio grows from `1.7227` at `n=3` to `255059.064965` at `n=20`, consistent with (6.4)-(6.6).

These finite computations are stress tests only; the theorems above are analytic.

---

## 9. Exact remaining universal implication

The previous concrete target

\[
\mathcal W\le\frac34J
\]

is exactly equivalent, via (2.1), to the negative-credit inequality

\[
\boxed{
\sum_i M_iD(\mu_i\|\pi_i)
\ge
\sum_iM_i\log_2\frac1{2M_i}
-\frac32J.
}
\tag{9.1}
\]

This remains **OPEN / CONDITIONAL**. Equation (9.1) is not advertised as easier merely because it is equivalent; its value is structural: it identifies the missing theorem as a lower bound on the information generated by **actual Boolean packet-pair incidence**, rather than an upper bound on a raw arithmetic normalizer.

The chain rule (5.1) now supplies a non-lossy interface to the spectral-lattice/centroid-carry machinery. The next attempt should keep both KL pieces negative and ask whether the account02 all-cost valuation tails can force part of the valuation-pair divergence, while the zero-valuation and tribes tests force the conditional mesh divergence to carry the rest. If a valuation-only lower bound is proposed, the one-point family refutes it immediately because its valuation-pair KL is zero.

A proof of (9.1) would give the existing conditional FEI constant `5/2+3/ln 2 = 6.82808512266689...`. A Boolean counterexample to (9.1) would kill the present `3/4` route but not FEI.

---

## 10. Status and joint handoff

### PROVED in this run

1. Exact packet-minority KL identity (2.1), with exact sufficiency of the unordered magnitude-pair packet label (2.2).
2. Exact two-credit Shannon remainder (3.3)-(3.5): orientation mutual information and packet-minority KL are distinct negative credits.
3. Packet-KL restriction sandwich (4.2)-(4.3), consuming the peer sharp restriction kernel.
4. Exact KL chain decomposition into valuation-pair and conditional physical-mesh credits (5.1).
5. Exact local cancellation formula on the consumed zero-valuation one-point family (6.4)-(6.6).
6. Width-two-tribes asymptotic packet-KL cancellation (7.4)-(7.5), using the already-proved exact tribes spectrum.

### REFUTED / DEAD DIRECTION

A proof that separately upper-bounds the raw minority normalizer `M_i log(1/M_i)` by influence while dropping the packet KL. Width-two tribes requires an unbounded KL refund, and the one-point family requires cancellation to extremely small relative scale.

### OPEN

Full uniform-cube FEI remains **OPEN / NOT PROVED**. The concrete current route still needs (9.1), or another dimension-free inequality that retains the same actual negative credits.

**consumed_peer_artifact:** account01/B15 `20260921T222602Z-zero-valuation-height-tilt-obstruction/REPORT.md` (blob `f85d23ec06d69416084fe742c8fc710f74910a15`), plus the compatible account01 sharp restriction kernel and account02 valuation-tail majorization as stated above.

**applied_to_claim:** the exact real-coordinate restriction Shannon/softmax remainder after unordered magnitude-pair conditioning; the peer global-height obstruction is converted into a local packet-law cancellation test rather than a positive KL payment.

**remaining_implication:** prove or refute (9.1), equivalently `mathcal W<=3J/4`, using Boolean packet-pair incidence while retaining both valuation-pair and conditional mesh KL credits.

**next_recipient:** account02/B15 for the minority-weighted valuation-pair KL component; account01/B15 for the conditional physical-height/mesh credit after its valuation escort.

**full_problem_change:** `OPEN -> OPEN`.

**mechanism_change:** `positive aggregate softmax bound -> exact real-restriction packet normalizer minus negative KL, followed by a KL chain rule across valuation and mesh labels`.
