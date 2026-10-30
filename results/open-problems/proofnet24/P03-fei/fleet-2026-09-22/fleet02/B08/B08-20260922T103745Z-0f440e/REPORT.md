# fleet02/B08 — oriented-cancellation entropy-variational certificate

**Run:** `B08-20260922T103745Z-0f440e`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NONLINEAR_RARE_EVENT_KL_CERTIFICATE`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Fresh control and exact assigned target

The fresh control head at run start was `67da221c72c71f464bb45fffefdcf7e887f0c2de`, owner revision `2026-09-22.3`, programme `FEI-ALL-TEAM-20260922T095941Z`. This later direct owner order supersedes the stale MOC4 scheduler text. The exact fleet02/B08 card is **Nonlinear variational Booleanity bound**: derive a nonlinear dependence-credit certificate from signed Boolean multiplication constraints, with a log-MGF/entropy-variational mechanism that preserves the sparse rare-event logarithm and does not rely on the refuted low-level projection or unweighted-L2 routes.

The source-pinned premises used here are:

1. fleet02/B15, `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `20260922T0829Z-influence-iprojection-kl/REPORT.md`: the exact I-projection identity
   \[
   K_{\rm occ}=D_2(P\Vert Q_r),\qquad R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ}.
   \]
2. fleet04/B17, `603b35e74227d1c2d8ee34c0c527c439c686e30b`, `20260922T092422Z-biased-booleanity-gap/REPORT.md`: the exact signed Boolean quadratic equations and the existing Hellinger/quadratic gap bound.
3. fleet04/B15, `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`, `20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`: on the genuine sparse suspension, the full unweighted convolution-L2 bank is only `Theta(I)` while `K_occ=Theta(mI)`.
4. fleet03/B18, `bff0d7b6c21485f386841c42582eb04f32705046`, `20260922T100641Z-lowlevel-projection-barrier/REPORT.md`: fixed-depth, and even `d_m <= (1/2-epsilon)m`, individually labelled low-level KL plus one merged tail cannot universally pay the recursive-majority demand.

The assignment names fleet03/B08 as partner. A bounded fresh check of the canonical FEI handoff root and the expected math-open-problems fleet03/B08 roots found no completed partner artifact at this run's source snapshot, so no partner theorem is fabricated. The completed OTHER-account result actually applied below is fleet04/B15's sparse-suspension obstruction, and the fleet03/B18 barrier is used as a mandatory preflight.

## 1. The bounded entropy-variational test we need

For probability laws `P,Q` on a finite set and an event `H`, the Donsker--Varadhan variational formula in bits, restricted to the bounded test `t 1_H`, gives

\[
D_2(P\Vert Q)
\ge
\sup_{t\in\mathbb R}
\left\{tP(H)-\log_2\bigl(1-Q(H)+Q(H)2^t\bigr)\right\}.
\tag{1.1}
\]

The supremum is exactly the binary relative entropy

\[
d_2(P(H)\Vert Q(H)).
\tag{1.2}
\]

This is nonlinear in the event probability and retains a factor `log(1/Q(H))` when `H` is genuinely rare under the reference. The only missing ingredient is therefore a **source-valid way to force mass onto a Q-rare event**. The next theorem gets such an event directly from one signed Boolean multiplication equation.

## 2. Oriented-cancellation theorem from one Boolean shift equation

Let `g:{-1,1}^m -> {-1,1}` have uniform Walsh coefficients `(a_S)_{S subseteq [m]}` and squared spectral law

\[
P(S)=a_S^2.
\]

Fix nonempty `U subseteq [m]` and write `tau(S)=S triangle U`. Since `g^2=1`, the `U`-th nonconstant Walsh coefficient of `g^2` vanishes:

\[
\boxed{\sum_S a_S a_{\tau(S)}=0.}
\tag{2.1}
\]

The involution `tau` has no fixed point, so its orbits are unordered pairs. Let `D` be any collection of these unordered pairs. For one representative from each pair in `D`, define

\[
\Delta_D:=\left|\sum_{\{S,\tau S\}\in D} a_Sa_{\tau S}\right|.
\tag{2.2}
\]

Orient every remaining unordered pair by choosing one endpoint; call the set of chosen endpoints `H`, so the opposite endpoints are exactly `tau H`. Then (2.1), divided by the common ordered-pair factor two, gives

\[
\left|\sum_{S\in H}a_Sa_{\tau S}\right|=\Delta_D.
\]

Cauchy--Schwarz therefore gives the exact source constraint

\[
\boxed{
P(H)P(\tau H)\ge \Delta_D^2.
}
\tag{2.3}
\]

Consequently, if an independently proved/source-exact upper bound

\[
P(\tau H)\le \Gamma
\tag{2.4}
\]

is available, then

\[
P(H)\ge \ell:=\Delta_D^2/\Gamma.
\tag{2.5}
\]

Let `Q` be any full-support reference law and `q=Q(H)`. If `ell>=q`, data processing followed by monotonicity of binary KL on `[q,1]` yields the nonlinear Booleanity certificate

\[
\boxed{
D_2(P\Vert Q)
\ge d_2(P(H)\Vert q)
\ge d_2(\ell\Vert q)
=
\sup_t\left[t\ell-\log_2(1-q+q2^t)\right].
}
\tag{2.6}
\]

This is the requested entropy-variational/log-MGF form. It is not a fixed multiple of a squared Booleanity residual. The event `H` is manufactured by the **signed** cancellation equation (2.1), while the cost is the exact logarithmic rarity of that oriented event under `Q`.

### Reference-adapted orientation

A useful canonical choice is to orient every remaining `tau`-pair toward its lower-`Q` endpoint. Then

\[
Q(H)=\sum_{\text{remaining pairs}}\min(Q(S),Q(\tau S))
\le {1\over2}\sum_S\sqrt{Q(S)Q(\tau S)}.
\tag{2.7}
\]

For an independent Bernoulli product reference with occurrence probabilities `t_i`, the full shift affinity factors exactly as

\[
\sum_S\sqrt{Q(S)Q(S\triangle U)}
=
\prod_{i\in U}2\sqrt{t_i(1-t_i)}.
\tag{2.8}
\]

Thus large signed shifts through rare coordinates automatically create exponentially small reference events. The remaining nontrivial quantity is the physical/source upper bound `Gamma` on the opposite orientation; that is where additional Boolean information must enter.

## 3. Sparse suspension: the certificate recovers the missing rare-event logarithm

Apply the theorem to the exact genuine Boolean family used by fleet04/B15. Put

\[
p=2^{1-m},\qquad
g_m(x)=1-2\mathbf 1_{\{x=0\}},\qquad F_m(y,x)=y g_m(x).
\tag{3.1}
\]

The old-factor Walsh coefficients are exactly

\[
a_\varnothing=1-p,
\qquad
a_T=-p\quad(T\ne\varnothing).
\tag{3.2}
\]

For the suspension `F_m`, the fresh coordinate is spectrally deterministic and the old-coordinate I-projection is exactly

\[
Q_m(T)=p^{|T|}(1-p)^{m-|T|}.
\tag{3.3}
\]

Hence the inherited exact identity is

\[
K_{\rm occ}(F_m)=D_2(P_{g_m}\Vert Q_m).
\tag{3.4}
\]

Take the full complement shift `U=[m]`, so `tau(T)=T^c`, and let `D` consist only of the pair `{emptyset,[m]}`. Then

\[
\Delta_D=|a_\varnothing a_{[m]}|=p(1-p).
\tag{3.5}
\]

Orient every other complement pair toward the larger-cardinality endpoint; on the middle level choose one endpoint from each complement pair. Call this high-side transversal `H_m` and its complement transversal `L_m=tau H_m`. Since every nonempty coefficient has squared mass `p^2` and there are `2^{m-1}-1` pairs,

\[
P_{g_m}(H_m)=P_{g_m}(L_m)
=(2^{m-1}-1)p^2
=p(1-p).
\tag{3.6}
\]

In particular, using `Gamma=P(L_m)=p(1-p)`, the signed Cauchy certificate (2.3)--(2.5) is **exact**:

\[
\ell_m={\Delta_D^2\over\Gamma}=p(1-p)=P(H_m).
\tag{3.7}
\]

Under the reference product law, every set in `H_m` has cardinality at least `m/2`, so

\[
q_m:=Q_m(H_m)
\le 2^{m-1}p^{m/2}.
\tag{3.8}
\]

Therefore

\[
\boxed{
K_{\rm occ}(F_m)
\ge d_2(p(1-p)\Vert q_m).
}
\tag{3.9}
\]

This already has the correct rare-event scale. Indeed

\[
\log_2{1\over q_m}={m^2\over2}+O(m),
\qquad h_2(p(1-p))=O(mp),
\]

and the binary-KL identity gives

\[
\boxed{
d_2(p(1-p)\Vert q_m)
={1\over2}m^2p+O(mp).}
\tag{3.10}
\]

The exact fleet04/B15 source calculation is

\[
K_{\rm occ}(F_m)=m^2p+O(mp).
\tag{3.11}
\]

Thus this single bounded variational event certificate captures **one half of the leading rare-event KL asymptotic**:

\[
\boxed{
{d_2(p(1-p)\Vert q_m)\over K_{\rm occ}(F_m)}\longrightarrow{1\over2}.
}
\tag{3.12}
\]

This is qualitatively different from the refuted unweighted full-shift L2 energy, which is only `Theta(mp)` on the same family while the needed KL is `Theta(m^2p)`.

A completely explicit lower expression follows from (3.8):

\[
d_2(p(1-p)\Vert q_m)
\ge p(1-p)(m-1)(m/2-1)-h_2(p(1-p)),
\tag{3.13}
\]

which has the same `m^2p/2` leading term.

## 4. Why the recursive-majority barrier is respected

The fleet03/B18 counterfamily rules out a fixed low-degree labelled projection, or any cutoff `d_m <= (1/2-epsilon)m` followed by one merged tail, as a universal decoder of `K_occ` on depth-`m` recursive ternary majority.

The present theorem does **not** use that mechanism. Its event is selected from a full signed multiplication shift and may sit at arbitrarily high cardinality; the log-MGF is evaluated directly on the resulting Q-rare event. On recursive majority the theorem is not claimed to produce a positive universal payment automatically: a poor distinguished block or orientation may give `Delta_D=0` or an insufficient `Gamma`. Thus there is no contradiction with the low-level barrier and no hidden claim that a one-bit projection closes FEI. What is proved is narrower and source-valid: the method can retain the full rare-event logarithmic order on the exact sparse family that defeats every fixed quadratic compression.

## 5. Comparison with the exact Bellman deficit

At balanced center `C`, the sparse suspension has

\[
B_{\rm inf}^C=C mp-mh_2(p)=-m^2p+O(mp).
\tag{5.1}
\]

The new certificate supplies only

\[
{1\over2}m^2p+O(mp),
\]

so it does **not** yet pay the whole negative Bellman deficit. This is why the classification is `ESSENTIAL_STEP_APPLIED`, not a full proof candidate. It proves that the requested nonlinear signed-source route can recover the rare-event logarithm that the L2 and low-level routes lose, while also quantifying the remaining factor-two loss on the canonical sparse obstruction.

The first unpaid implication is now concrete:

> **B08-ORIENTED-CANCELLATION-PAYMENT-v2.** Choose one source-valid collection of signed Boolean shift cancellations and a no-double-spending variational statistic so that, for every balanced Boolean source, the resulting logarithmic event/partition KL pays `H_max(r)-C(I-1)` for one finite `C`. On the sparse suspension it must recover the second half of the leading `m^2p` term; on recursive ternary majority it must retain genuinely high-scale information rather than a fixed low-level cutoff.

A natural next mechanism is a **single multi-cell partition** generated by several oriented shift cancellations, rather than summing separate binary KL certificates (which would repeat the same `K_occ`). The partition KL is still bounded by `K_occ` by one data-processing step, so it offers a clean way to combine multiple rare-event payments without illegal double counting.

## 6. Exact self-check

The adjacent standard-library checker uses exact `Fraction` arithmetic for the complement Booleanity equation, the forced high-side mass, and `q_m`; floating point is used only to print binary KL and entropy values. It verifies the identities for `m=4,5,6,8,10,12,16,20` and shows the certificate/KL ratio increasing toward `1/2` (at `m=20`, approximately `0.463867741`).

Executed source SHA-256: `280d969280530a0eb17a252f66e9398af9bbaf0d27b158050f61ac0db64e8eea`.  
Captured output SHA-256: `5854096478e4e58383271c8c7882a4c99621b05362934769a80e33ab7c73fac1`.  
The checker returned `PASS`.

## 7. Scope and honesty

No MOC4, benchmark, installation, paid API/model, remote workflow, email, Drive, public release, credential use, or permission bypass was performed. No arbitrary bistochastic/spectral surrogate is used: the main application is the genuine Boolean sparse suspension and the forcing equation is the exact Walsh coefficient identity for `g^2=1`. The theorem is a new source-valid intermediate FEI mechanism, not a claim that FEI is proved.
