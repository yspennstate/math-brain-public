Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0130 — uniform Abel correctors, a nonmixing extension, and the canonical tail defect

Date: 2026-09-18  
Slot: R7-05 Sharp Inequality Research  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12, printed p. 13.  
Status: **PARTIAL relative to the full source.**

The admission-fixed metric remains

`M_closed` = largest finite cookie depth `M` for which an evidenced exact closed escape-probability formula holds for every i.i.d. bounded stack law neutral after visit `M` in the transient regime.

It was already saturated at all finite depths, so this artifact does not redefine it:

\[
M_{\rm closed}=\infty\quad\text{before and after.}
\]

The mathematical advances here concern the remaining stationary-dependent infinite-stack branch.

---

## 1. Cumulative input and notation

The preceding R7-05 report established infinite-stack truncation continuity under the bounded projective condition

\[
\sum_{j\ge0}\left\|E[Y_j\mid\mathcal F_0]\right\|_\infty<\infty,
\tag{1.1}
\]

where `Y_j` is the centered site drift of a deliberately weakened finite-cookie prefix and `F_n` is the past environment sigma-field.  The proof used a bounded Gordin corrector to build a negative-power Lamperti supermartingale, then glued that high-population estimate to the exact `2K-2` finite-cookie visibility lemma.

This note asks whether summability in (1.1) is stronger than necessary.

Fix `0<beta<bar(delta)-1`.  Choose a finite prefix and a radial weakening `q` so that its stationary mean drift satisfies

\[
\bar\delta_q>1+\beta.
\tag{1.2}
\]

Put

\[
Y_n=\delta_n^q-\bar\delta_q,
\qquad E Y_n=0.
\]

The variables `Y_n` are bounded because the weakened prefix has finite depth.

---

# 2. B29 — add the Abel boundary instead of summing the projective series

For `0<r<1`, define the Abel-predictive corrector

\[
G_{r,n}:=\sum_{j\ge0}r^j E[Y_{n+j}\mid\mathcal F_n].
\tag{2.1}
\]

For each fixed `r<1`, this converges in `L^infinity` with

\[
\|G_{r,n}\|_\infty\le \frac{\|Y_0\|_\infty}{1-r}.
\]

A direct index shift gives the exact resolvent identity

\[
\boxed{
E[G_{r,n+1}\mid\mathcal F_n]
=\frac{G_{r,n}-Y_n}{r}.
}
\tag{2.2}
\]

Indeed,

\[
\begin{aligned}
rE[G_{r,n+1}\mid\mathcal F_n]
&=\sum_{j\ge0}r^{j+1}E[Y_{n+1+j}\mid\mathcal F_n]\\
&=\sum_{k\ge1}r^kE[Y_{n+k}\mid\mathcal F_n]\\
&=G_{r,n}-Y_n.
\end{aligned}
\]

Define

\[
c_{r,n}:=-\beta r G_{r,n}.
\tag{2.3}
\]

Then (2.2) yields

\[
\boxed{
E[c_{r,n+1}\mid\mathcal F_n]-c_{r,n}
=\beta Y_n-\beta(1-r)G_{r,n}.
}
\tag{2.4}
\]

The first term is exactly the cancellation needed in the preceding projective-corrector proof.  The second is the Abel boundary error.

This motivates the following strictly weaker sufficient condition.

### Uniform Abel condition (UAC)

For the selected weakened prefix,

\[
\boxed{
\varepsilon(r):=
\left\|(1-r)G_{r,0}\right\|_\infty
\longrightarrow0
\qquad(r\uparrow1).
}
\tag{2.5}
\]

Stationarity makes the same bound valid at every `n`.

## Theorem 2.1 — UAC implies polynomial high-population safety

Assume (1.2) and (2.5).  For every `beta<bar(delta)_q-1`, there are deterministic constants `L,C_beta<infinity` such that for every finite stopping time `sigma` of the joint environment/cookie filtration,

\[
\boxed{
P_q(\text{eventual extinction}\mid\mathcal H_\sigma,
V_\sigma=k)
\le C_\beta(1+k)^{-\beta},
\qquad k\ge L.
}
\tag{2.6}
\]

### Proof

Choose `r<1` so close to one that

\[
\varepsilon(r)<\frac12(\bar\delta_q-1-\beta).
\tag{2.7}
\]

For this fixed `r`, `c_{r,n}` is uniformly bounded.  Choose `a` so large that

\[
1+\frac{c_{r,n}}{k+a}\in[1/2,3/2]
\]

for all `n,k>=0`, and define

\[
F_n(k)=(k+a)^{-\beta}
\left(1+\frac{c_{r,n}}{k+a}\right).
\tag{2.8}
\]

For the weakened finite-depth forward branching chain, once `k` exceeds the prefix depth, the exact one-step decomposition used in the preceding R7-05 proof gives, conditionally on the current environmental past,

\[
E[\Delta_n]=\delta_n^q,
\qquad
E[\Delta_n^2]=2k+O(1),
\qquad
E|\Delta_n|^3=O(k^{3/2}),
\tag{2.9}
\]

with an exponentially small complement to `|Delta_n|<=k/2`; all error constants are uniform because the weakened prefix is bounded.

Taylor expansion of (2.8), using (2.4), gives

\[
\begin{aligned}
&E[F_{n+1}(V_{n+1})\mid\mathcal H_n]-F_n(V_n)\\
&\qquad=
\beta\Bigl(\beta+1-\bar\delta_q-(1-r)G_{r,n}\Bigr)
(k+a)^{-\beta-1}
+o(k^{-\beta-1}),
\end{aligned}
\tag{2.10}
\]

uniformly in the environmental past.  The local fluctuation `Y_n` cancels: this is exactly why the sign in (2.3) was chosen.

By (2.7), the coefficient in (2.10) is bounded above by

\[
-\frac\beta2(\bar\delta_q-1-\beta)<0.
\]

Hence for deterministic sufficiently large `L`, `F_{n\wedge\tau_L}(V_{n\wedge\tau_L})` is a nonnegative supermartingale while the population stays above `L`, where `tau_L` is the first visit to `[0,L]`.

Optional stopping, exactly as in the preceding projective-corrector argument, gives

\[
P_q(\tau_L<\infty\mid\mathcal H_\sigma,V_\sigma=k)
\le C_\beta(1+k)^{-\beta}.
\]

Extinction implies a visit to `[0,L]`, so (2.6) follows.  The argument starts at an arbitrary finite stopping time because the drift estimate is conditional on the actual environmental history rather than on a deterministic phase.  QED.

## Corollary 2.2 — infinite-stack gluing under UAC

Let the full positive stack dominate the selected weakened prefix `q`.  Let the depth-`M` approximation agree with the full stack for the first `M` cookies and be neutral afterwards.  The cumulative exact visibility lemma says that, below population `K`, their censored one-step kernels agree whenever

\[
M\ge2K-2.
\]

At their common first exit through population at least `K`, both continuation processes dominate `q`, so (2.6) applies conditional on the exit history.  Therefore

\[
0\le h-h_M\le C_\beta K^{-\beta}.
\]

Taking `K=floor(M/2)+1` yields

\[
\boxed{
0\le p_{\rm esc}^{(\infty)}-p_{\rm esc}^{(M)}
\le C_\beta M^{-\beta},
\qquad
p_{\rm esc}^{(M)}\uparrow p_{\rm esc}^{(\infty)}.
}
\tag{2.11}
\]

Thus the previous summable-projective hypothesis can be replaced by UAC.

The implication from the old hypothesis to UAC is immediate: if the norms in (1.1) are summable then dominated convergence gives `(1-r)G_{r,0}->0` in `L^infinity`.  The converse is false, as the next example shows.

---

# 3. A genuinely nonmixing stationary-ergodic class covered by UAC

Let `T x=x+alpha mod 1` be an irrational rotation of the circle with Haar-distributed initial phase `x`.  This is stationary and ergodic but not mixing.

Choose, for example,

\[
p_1(x)=\frac12+0.35+0.05\cos(2\pi x),
\qquad
p_2(x)=\frac12+0.35+0.05\sin(2\pi x),
\tag{3.1}
\]

and make later cookies neutral for the weakened baseline.  Both displayed biases lie strictly between `1/2` and `1`; the mean total drift of these first two cookies is `1.4>1`.  The two coordinates together recover the phase up to a null ambiguity, so the present stack reveals the rotation phase.

After centering, the site drift is a finite linear combination of the Fourier modes `e^{+/-2 pi i x}`.  Consequently

\[
E[Y_j\mid\mathcal F_0]=Y(T^j x).
\]

Its `L^infinity` norm is independent of `j`, so the projective series (1.1) diverges whenever the centered drift is nonzero.

For a single Fourier mode,

\[
(1-r)\sum_{j\ge0}r^j e^{2\pi i(x+j\alpha)}
=
\frac{(1-r)e^{2\pi i x}}{1-r e^{2\pi i\alpha}}.
\tag{3.2}
\]

Because `alpha` is irrational, `e^{2 pi i alpha} !=1`, and the supremum norm of (3.2) tends to zero as `r` tends to one.  The same holds for any finite Fourier combination.  Hence UAC holds although the old projective-summability condition fails.

This is a strict mathematical extension of the preceding dependent-environment theorem: infinite-stack gluing now covers a concrete stationary-ergodic nonmixing class.

---

# 4. B2 — a long-block obstruction to every uniform corrector proof of this type

The next question is whether UAC itself follows from stationary ergodicity.  It does not.

Consider a stationary alternating-renewal process of `+` and `-` blocks with an unbounded finite-mean block-length law.  Encode the block sign in the finite-prefix drift `Y_n=+a` or `-a`, with mean zero.  Encode the residual block information in the cookie stack without changing this centered drift—for example by redistributing a fixed total finite-prefix drift between two positive cookies.  Thus the present environment can reveal that a very long constant-sign future block remains.

For every `r` near one and every very large `L`, the stationary process has positive probability of a present state with residual `+` block length at least `L`.  On such a state,

\[
(1-r)G_{r,0}
\ge
 a(1-r)\sum_{j=0}^{L-1}r^j
-\|Y_0\|_\infty r^L.
\tag{4.1}
\]

Choose `L` much larger than `(1-r)^{-1}`.  The first term is then close to `a` while the second is negligible.  Hence

\[
\limsup_{r\uparrow1}
\|(1-r)G_{r,0}\|_\infty>0.
\tag{4.2}
\]

So UAC can fail under stationary ergodicity, just as the stronger projective condition can.

This is **not** a counterexample to truncation continuity.  If the constructed cookie environment has only finite cookie depth, the full and truncated models agree identically for every sufficiently large `M`.  Therefore (4.2) proves something more precise: bounded/projective/Abel correctors are sufficient mechanisms, not necessary mechanisms.  A true counterexample to source-level truncation continuity would have to exploit essentially infinite cookie depth along the surviving trajectory, not merely long spatial memory.

---

# 5. B27 — swap the quantifiers and isolate the exact tail event

The full positive stack and all neutral-tail truncations admit a grand monotone coupling using one uniform random variable for every site/visit.  Let

\[
E_M=\{\text{the depth-}M\text{ forward chain survives}\},
\qquad
E_\infty=\{\text{the full forward chain survives}\}.
\]

Positivity gives the pathwise nesting

\[
E_M\subseteq E_{M+1}\subseteq E_\infty.
\tag{5.1}
\]

Define quenched survival functions

\[
h_M(\omega,k)=P_{\omega,k}(E_M),
\qquad
h(\omega,k)=P_{\omega,k}(E_\infty),
\]

and

\[
h_*(\omega,k):=\lim_{M\to\infty}h_M(\omega,k).
\tag{5.2}
\]

By monotone convergence of events,

\[
\boxed{
h_*(\omega,k)
=P_{\omega,k}\left(\bigcup_{M\ge1}E_M\right).
}
\tag{5.3}
\]

Therefore the exact truncation-continuity defect is

\[
\boxed{
d(\omega,k):=h(\omega,k)-h_*(\omega,k)
=P_{\omega,k}\left(
E_\infty\cap\bigcap_{M\ge1}E_M^c
\right).
}
\tag{5.4}
\]

Equation (5.4) has a useful pathwise meaning:

> truncation continuity fails exactly when the full forward process can survive on an event on which **every fixed finite cookie-depth truncation dies**.

In other words, any genuine failure must require arbitrarily deep cookies along survival.

## Proposition 5.1 — the defect is harmonic under upper ellipticity

Assume, for this proposition only, a uniform upper ellipticity

\[
p_{x,i}\le1-\kappa
\qquad\text{a.s. for some }\kappa>0.
\tag{5.5}
\]

Let `S_k` be the full-stack number of successes before the `k`-th failure at the next site.  Under (5.5), `S_k<infinity` almost surely.  In the grand coupling the truncated value `S_k^(M)` increases to `S_k` and, because `S_k` uses only finitely many tosses, is eventually exactly equal to `S_k`.

The harmonic equation for each truncation is

\[
h_M(\omega,k)
=E_\omega\left[h_M(\theta\omega,S_k^{(M)})\right].
\]

Letting `M` tend to infinity and using bounded convergence gives

\[
\boxed{
h_*(\omega,k)
=E_\omega\left[h_*(\theta\omega,S_k)\right].
}
\tag{5.6}
\]

The full survival function satisfies the same equation, hence

\[
\boxed{
d(\omega,k)
=E_\omega\left[d(\theta\omega,S_k)\right].
}
\tag{5.7}
\]

Thus `d` is a bounded nonnegative harmonic function for the full environment-population skew product.

For

\[
\tau_K=\inf\{n:V_n=0\text{ or }V_n\ge K\},
\]

while `1<=V_n<K` there is conditional probability at least `kappa^(K-1)` that the next `V` value is zero, so `tau_K<infinity` almost surely.  Optional stopping of the bounded martingale

\[
d(\theta^n\omega,V_n)
\]

gives the exact boundary identity

\[
\boxed{
d(\omega,k)
=E_{\omega,k}\left[
 d(\theta^{\tau_K}\omega,V_{\tau_K});
 V_{\tau_K}\ge K
\right].
}
\tag{5.8}
\]

This is the canonical form of the remaining obstruction.  The source-level stationary-ergodic infinite-stack problem is reduced, under (5.5), to proving that this nonnegative tail harmonic function is identically zero—or constructing an environment for which it is not.

The UAC theorem above implies `d=0`; the long-block finite-depth example shows that `d=0` can hold even when UAC fails.  So the right unrestricted object is `d`, not any particular corrector norm.

---

# 6. What this does and does not settle

### New proved content

1. The projective/Gordin hypothesis can be weakened to the uniform Abel condition (2.5).
2. Under UAC, the exact same polynomial truncation bound `O(M^{-beta})` holds for every `beta<bar(delta)-1` obtainable from a weakened finite prefix.
3. Irrational-rotation cookie environments give an explicit stationary-ergodic nonmixing class satisfying UAC but not projective summability.
4. Stationary ergodicity alone does not imply UAC: long stationary renewal blocks violate it.
5. Under upper ellipticity, the full residual source obstruction is the nonnegative harmonic tail defect (5.4)-(5.8).

### Not proved

- No source-level formula for arbitrary `(SE)+(POS_1)` is obtained.
- No stationary-ergodic counterexample to truncation continuity is obtained.
- The defect `d` is not proved identically zero under bare stationary ergodicity.
- No independent P26 or distinct OTHER-track full-source audit exists.

Accordingly C0130 remains **PARTIAL / SOURCE OPEN**.

---

# 7. Method outcomes

1. **B2 — ATTACK THE NEGATION FIRST: PARTIAL SUCCESS / NO SOURCE COUNTEREXAMPLE.** A stationary-ergodic long-block construction destroys both projective summability and UAC, proving these hypotheses are not automatic.  Finite-depth instances still have zero truncation defect, so this does not refute source continuity.
2. **B27 — SWAP THE QUANTIFIERS: SUCCESS.** Instead of demanding a uniform corrector, the exact leftover event is `E_infinity intersect all_M E_M^c`; under upper ellipticity its probability is a bounded nonnegative harmonic function of the environment-population skew product.
3. **B29 — ADD THE POINTS AT INFINITY: SUCCESS.** Abel regularization yields a strictly broader corrector theorem and covers explicit nonmixing irrational-rotation environments.

The frozen metric nevertheless remains `infinity -> infinity`, so under the owner protocol this is the sixth ordinary unchanged CLOSABLE iteration and requires an immutable operational handoff/retirement of C0130 rather than another same-target ordinary run.
