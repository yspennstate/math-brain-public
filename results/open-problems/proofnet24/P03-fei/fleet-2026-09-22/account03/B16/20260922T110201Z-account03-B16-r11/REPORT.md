# account03/B16 — log-weighted Walsh-lattice cancellation flow

**Run:** `20260922T110201Z-account03-B16-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Classification:** `PROVED_ASSIGNED_TRANSPORT_THEOREM / AUXILIARY_BRIDGE / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Brain status:** authenticated private repository control/state/source retrieval was genuinely used in this invocation; `full_brain_connected=false` and no native learned-memory ingestion is claimed.

## 0. Current scope and sources

Fresh owner control was revision `2026-09-22.3`. The older seven-FEI and interface-C duties are superseded. The live B16 assignment is Path B: construct an entropy-weighted signed cancellation flow on spectral atoms, preserving full Boolean-convolution signs, lateral partners, rare-event logarithms, and one-use credit accounting.

The consolidated current state keeps two corrections binding here:

1. complete **unweighted** convolution `L2` is refuted as a universal KL payment on sparse suspensions; a successful Path-B statistic must retain the logarithm;
2. fixed/low-depth labelled KL followed by one merged tail is refuted by recursive ternary majority; a successful statistic must keep genuinely multiscale/high-cardinality information.

I use two exact source results.

**IPROJ (account02/B15).** Retrieved from `yspennstate/math-open-problems@3b546dc77811cf4c9a5f3fbac36e834b0f236bd6`, path `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`. For the actual nonempty spectral law `P=w^+` with coordinate-occurrence vector `r`, the conditional-product I-projection `Q_r` obeys

\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
\]

and for every conditional-product Gibbs law `nu`,

\[
D_{\rm KL,2}(P\Vert\nu)=K_{\rm occ}+D_{\rm KL,2}(Q_r\Vert\nu).
\tag{0.1}
\]

The live residual is `R_Gamma=B_inf^Gamma+K_occ`.

**Partner account04/B16.** Retrieved from the same repository snapshot, path `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T094238Z-all-constraint-boolean-projection/REPORT.md`. Its theorem `B16-ALL-CONSTRAINT-BOOLEAN-PROJECTION` keeps the actual Fourier signs and, for any target nonempty law `nu^+`, proves

\[
vD_{\rm KL,2}(w^+\Vert\nu^+)
\ge -2\log_2\mathbb E_p|B_{\nu,p}|,
\tag{0.2}
\]

where `B_{nu,p}` is the physical field with target magnitudes and the **common source signs**. I apply (0.2) below with `nu^+=Q_r`.

No current candidate potential is assumed universal in this report.

---

## 1. PROVED — canonical logarithmic cancellation flow

The construction is a finite-state identity and therefore applies directly to spectral atoms.

### Theorem 1 — `P03-B16-LOG-WALSH-FLOW-v1`

Let `Omega` be finite and let `P,Q` be probability laws with `P << Q`. First assume they have the same positive support. Put

\[
L(s):=\log_2\frac{P(s)}{Q(s)},
\qquad
Z(t):=\sum_{s\in\Omega}P(s)^{1-t}Q(s)^t,
\]

and define the normalized exponential bridge

\[
\rho_t(s):=\frac{P(s)^{1-t}Q(s)^t}{Z(t)},
\qquad 0\le t\le1.
\tag{1.1}
\]

On every **ordered** pair of distinct atoms define

\[
\boxed{
J_t(s,u):=(\ln2)\,\rho_t(s)\rho_t(u)\,[L(s)-L(u)].
}
\tag{1.2}
\]

Then:

1. `J_t(s,u)=-J_t(u,s)`; no positive/negative receiver partition is used.
2. **Atomwise conservation** holds exactly:
   \[
   \boxed{
   \partial_t\rho_t(s)+\sum_uJ_t(s,u)=0
   }
   \qquad(s\in\Omega).
   \tag{1.3}
   \]
3. The one-sided KL in bits is exactly the weighted flow action
   \[
   \boxed{
   D_{\rm KL,2}(P\Vert Q)
   =\int_0^1(1-t)\,\frac12\sum_{s,u}
   J_t(s,u)[L(s)-L(u)]\,dt.
   }
   \tag{1.4}
   \]
4. No cancellation credit is reused inside (1.4): every unordered pair occurs exactly once because of the factor `1/2`, and
   \[
   \frac12\sum_{s,u}J_t(s,u)[L(s)-L(u)]
   =(\ln2)\operatorname{Var}_{\rho_t}(L)\ge0.
   \tag{1.5}
   \]

### Proof

Differentiate (1.1). Since

\[
\partial_t\log\bigl(P(s)^{1-t}Q(s)^t\bigr)
=-\ln2\,L(s),
\]

we have

\[
\partial_t\rho_t(s)
=-(\ln2)\rho_t(s)\bigl[L(s)-\mathbb E_{\rho_t}L\bigr].
\tag{1.6}
\]

On the other hand, summing (1.2) in `u` gives

\[
\sum_uJ_t(s,u)
=(\ln2)\rho_t(s)\bigl[L(s)-\mathbb E_{\rho_t}L\bigr],
\]

which is (1.3). This is conservation at **each atom**, not merely after total summation.

For the entropy identity define

\[
F(t):=\log_2 Z(t).
\]

Because `P,Q` are probability laws, `F(0)=F(1)=0`. Direct differentiation gives

\[
F'(t)=-\mathbb E_{\rho_t}L,
\qquad
F''(t)=(\ln2)\operatorname{Var}_{\rho_t}(L).
\tag{1.7}
\]

In particular

\[
F'(0)=-D_{\rm KL,2}(P\Vert Q).
\]

The integral Taylor formula at `t=1` yields

\[
0=F(1)=F(0)+F'(0)+\int_0^1(1-t)F''(t)\,dt,
\]

hence

\[
D_{\rm KL,2}(P\Vert Q)
=(\ln2)\int_0^1(1-t)\operatorname{Var}_{\rho_t}(L)\,dt.
\tag{1.8}
\]

Finally

\[
\frac12\sum_{s,u}\rho_t(s)\rho_t(u)[L(s)-L(u)]^2
=\operatorname{Var}_{\rho_t}(L),
\]

and substitution of (1.2) proves (1.4)-(1.5). `QED`.

### Zero spectral coefficients

The actual Boolean spectrum can have zeros. This causes no loss. Work on `supp(Q)` and, for `0<epsilon<1`, set

\[
P_\epsilon=(1-\epsilon)P+\epsilon Q.
\tag{1.9}
\]

Then `P_epsilon,Q` have common positive support and Theorem 1 supplies a feasible atomwise-conservative flow. Since the simplex is finite and `P<<Q`,

\[
D_{\rm KL,2}(P_\epsilon\Vert Q)\to D_{\rm KL,2}(P\Vert Q).
\tag{1.10}
\]

Thus the right side of (1.4), evaluated for `P_epsilon`, converges **exactly** to the desired KL. This is the support-complete definition of the flow action below; no missing-support entropy is discarded.

---

## 2. PROVED — full Walsh-lattice decomposition and common-source signs

Now let the state space be the Walsh lattice `Omega=2^[k]`. Each unordered pair `{S,T}` has the unique nonzero lateral translation

\[
U=S\triangle T.
\]

Write

\[
J_t^U(S):=J_t(S,S\triangle U),
\]

with the convention that it is zero when an endpoint is outside the active support. Then

\[
J_t^U(S\triangle U)=-J_t^U(S)
\]

and the atomwise continuity equation is the exact full-lattice identity

\[
\boxed{
\partial_t\rho_t(S)+\sum_{U\ne\varnothing}J_t^U(S)=0.
}
\tag{2.1}
\]

Moreover

\[
\boxed{
D_{\rm KL,2}(P\Vert Q)
=\lim_{\epsilon\downarrow0}\sum_{U\ne\varnothing}\mathcal A_U(P_\epsilon,Q),
}
\tag{2.2}
\]

where

\[
\mathcal A_U
:=\int_0^1(1-t)\,\frac12\sum_S
J_t^U(S)[L(S)-L(S\triangle U)]\,dt\ge0.
\tag{2.3}
\]

This is a genuine **multiscale/high-cardinality** reserve: no degree cutoff, no merged high-level tail, and no selected receiver set appears. Every lateral Walsh partner participates.

### Common-source sign gauge

Let `a_S` be the actual signed Fourier amplitudes and choose

\[
\varepsilon_S=\operatorname{sgn}(a_S)\in\{\pm1\},
\]

arbitrarily on a zero coefficient. Along the bridge define amplitudes

\[
c_t(S)=\varepsilon_S\sqrt{\rho_t(S)}.
\tag{2.4}
\]

Thus **the source sign never changes**. The signed edge current

\[
\widetilde J_t(S,T):=\varepsilon_S\varepsilon_TJ_t(S,T)
\tag{2.5}
\]

is still antisymmetric. If

\[
(\operatorname{div}_\varepsilon\widetilde J)(S)
:=\varepsilon_S\sum_T\varepsilon_T\widetilde J(S,T),
\]

then `epsilon_S^2=1` gives

\[
\boxed{
\partial_t\rho_t(S)+(\operatorname{div}_\varepsilon\widetilde J_t)(S)=0.
}
\tag{2.6}
\]

So common signs are retained without breaking conservation; they are a gauge on the exact mass flow, not an absolute-value relaxation.

For the **uniform** Walsh basis, define the full signed convolution

\[
\mathcal C_t(U)=\sum_S c_t(S)c_t(S\triangle U)
=\sum_S\varepsilon_S\varepsilon_{S\triangle U}
\sqrt{\rho_t(S)\rho_t(S\triangle U)}.
\tag{2.7}
\]

At the actual Boolean endpoint, `c_0(S)=a_S`, hence

\[
\boxed{
\mathcal C_0(U)=\sum_Sa_Sa_{S\triangle U}
=\widehat{G^2}(U)=\mathbf1_{\{U=\varnothing\}}.
}
\tag{2.8}
\]

Every transport edge in (2.3) lies in exactly the same translation fiber as one common-source signed term in (2.7). This is the requested full-Boolean-convolution geometry. Importantly, **I do not square and sum (2.7) as an entropy payment**; that is precisely the retired unweighted-`L2` mechanism. The payment is the logarithmic action (2.3).

For an arbitrary biased product basis, the entropy-flow theorem remains exact; one should use the partner's physical field rather than falsely replacing the biased multiplication table by XOR convolution.

---

## 3. Exact insertion into the FEI I-projection ledger

For a Boolean gate under product bias, let

\[
m=\widehat G_p(\varnothing),\qquad v=1-m^2,
\]

let `P^+=w^+` be its actual normalized nonempty spectral law, and let `Q_r` be the exact influence-marginal I-projection from IPROJ. Form full spectral laws

\[
\mathsf P(\varnothing)=m^2,
\quad \mathsf P(S)=vP^+(S),
\]

\[
\mathsf Q(\varnothing)=m^2,
\quad \mathsf Q(S)=vQ_r(S)\qquad(S\ne\varnothing).
\tag{3.1}
\]

Then the constant atom contributes zero likelihood ratio and therefore

\[
\boxed{
D_{\rm KL,2}(\mathsf P\Vert\mathsf Q)
=vK_{\rm occ}.
}
\tag{3.2}
\]

Applying Theorem 1 gives an exact, atom-conservative, full-support logarithmic flow with total action

\[
\boxed{
\mathcal A_{\log}(G,p):=vK_{\rm occ}(G,p).
}
\tag{3.3}
\]

Using IPROJ (0.1), for any Gibbs/product target `nu_Gamma^+`,

\[
vD(P^+\Vert\nu_\Gamma^+)
=\underbrace{\mathcal A_{\log}}_{vK_{\rm occ}}
+\underbrace{vD(Q_r\Vert\nu_\Gamma^+)}_{\text{influence-marginal price credit}}.
\tag{3.4}
\]

This is the **no-reuse ledger**. The flow owns exactly the first term and does not spend the second. In the all-gate residual

\[
D_\Gamma=vR_\Gamma=vB_{\inf}^\Gamma+\mathcal A_{\log}.
\tag{3.5}
\]

Therefore the still-open universal implication is now the source-exact signed-flow statement

\[
\boxed{
\mathcal A_{\log}(G,p)+vB_{\inf}^\Gamma(G,p)\ge0
}
\tag{3.6}
\]

for every required prime source/bias of a genuinely live candidate. Equation (3.6) is **not proved here**; by (3.5) it is exactly the original remaining gate inequality, not a claimed shortcut.

---

## 4. Named partner result applied to this exact flow

Take the account04/B16 physical comparison field with target `nu^+=Q_r` and the same common signs. Its endpoint amplitudes are exactly the `t=1` amplitudes of the full law in (3.1). Hence the partner theorem (0.2) becomes

\[
\boxed{
\mathcal A_{\log}=vK_{\rm occ}
\ge \Phi_{\rm bool}:=-2\log_2\mathbb E_p|B_{Q_r,p}|.
}
\tag{4.1}
\]

Thus the partner's all-constraint Boolean projection is a legitimate **sink of this same logarithmic current**. It is not an additional KL credit. If one spends `Phi_bool`, the remainder

\[
\mathcal A_{\log}-\Phi_{\rm bool}\ge0
\tag{4.2}
\]

is the only unspent part; one may not subsequently count the full `K_occ` again.

This supplies the requested partner application while keeping every common sign until the final physical `|B|` step already justified in the partner theorem.

---

## 5. Mandatory barriers: why this mechanism is genuinely different

### Recursive ternary majority / low-level barrier

The low-level projection obstruction removes only mechanisms that retain bounded/low labelled levels and merge the rest. The present quantity is exactly

\[
\sum_{U\ne0}\mathcal A_U=K_{\rm occ}
\]

(with the factor `v` for the full gate law), over **all** spectral atoms and all XOR distances. Therefore it retains the complete high-cardinality dependence for every depth of recursive majority. This is an analytic consequence of Theorem 1, not an extrapolation from a finite check.

As a code-path test, `CHECK.py` constructs depth-two recursive ternary majority on nine variables. It obtains

\[
K_{\rm occ}=2.170812831054787\ \text{bits}.
\]

At regularization `epsilon=10^{-5}`, the exact KL is `2.170683396091381` bits and numerical integration of the flow action gives `2.170683396091594` bits, discrepancy `2.14e-13`. The regularized value converges to the full `K_occ` as `epsilon` tends to zero.

### Rare-event logarithm / unweighted-L2 barrier

For the two-atom diagnostic

\[
P=(1-\delta,\delta),\qquad
Q=(1-\delta2^{-m},\delta2^{-m}),
\]

the rare atom contributes the exact logarithmic term `delta*m` to KL (with the compensating first-atom term), while the squared unweighted displacement is only `2 delta^2(1-2^{-m})^2`. For `delta=2^{-12}`, `m=40`, the checker finds

- KL/action: `0.009413447530195428` bits;
- unweighted `L2`: `1.1920928955056441e-07`;
- ratio: `78965.72125952125`.

This diagnostic is not itself a Boolean counterfamily; it verifies the mechanism responsible for surviving the genuine sparse-suspension obstruction. On any actual Boolean source the theorem returns that source's **exact** KL, so no rare-event logarithm can disappear through this transport representation.

---

## 6. Verification

`CHECK.py` is standard-library only and was executed before publication. It returned `PASS` and checked:

- 20 positive finite-law instances;
- maximum atomwise continuity error `2.220446049250313e-16`;
- maximum pair-Dirichlet identity error `4.440892098500626e-16`;
- maximum numerical KL/action integration error `9.103828801926284e-14`;
- all 256 Boolean functions on three variables for the exact full Walsh convolution identity, maximum error `0`;
- exact translation-fiber partition of the complete-graph action, error `0`;
- the depth-two recursive-majority preflight described above;
- the rare-event logarithmic diagnostic described above.

The theorem is analytic; these checks are implementation/factor/sign falsification tests only.

---

## 7. Status, failed shortcuts, and next recipient

**PROVED:** the logarithmic complete-graph/Walsh-lattice flow (1.2), atomwise conservation (1.3)/(2.1), common-sign gauge conservation (2.6), exact one-sided entropy action (1.4), XOR/lateral decomposition (2.2)-(2.3), full Boolean-convolution sign linkage (2.7)-(2.8), and exact FEI I-projection ledger (3.2)-(3.5).

**REFUTED/retired and not revived:** unweighted convolution `L2` as a replacement for KL; bounded/low-level labelled KL plus one merged tail; receiver-only pairing; positive-parting signed convolution equations.

**OPEN:** the universal comparison (3.6), equivalently a proof that the exact log-weighted action is always large enough to pay the negative `B_inf` on the remaining prime gate/bias region. Partner account04/B16 supplies the physical lower sink (4.1), but no theorem yet proves `Phi_bool >= -v B_inf` universally.

**Next recipient:** `account01/B15`. The most useful next attack is to apply its restriction/I-projection chain rule directly to the translation-resolved credits `A_U`, preserving the hierarchy term and the factor `(1-t)`, rather than coarse-graining by Fourier degree. This exact action is designed to survive the recursive-majority and sparse-event barriers simultaneously.

No full FEI claim is made.
