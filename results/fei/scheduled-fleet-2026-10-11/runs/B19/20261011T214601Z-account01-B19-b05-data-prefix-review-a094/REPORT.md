# B19 / A094 second-chain challenge: B05 bent data-prefix telescope

Run ID: `20261011T214601Z-account01-B19-b05-data-prefix-review-a094`  
Primary packet: `A094` (Proof-chain challenger)  
Reviewed target: `B05-A023-BENT-DATA-PREFIX-TELESCOPE-v1`  
Stable gap: `B05_RARE_REFUNDS`  
Full FEI status: **OPEN**

## Verdict

The B05 calculation has a correct and useful core, but its claims must be separated.

1. **ACCEPTED at narrow exact scope:** the support/sign counts, affine formula for the conditional-entropy packet `L_m`, constant nonnegative `L`-credit, geometric telescope, activation factor, and terminal `L` and `Q` bounds are correct for every even `k=2h>=4` in the declared genuine Boolean bent one-point-defect family.
2. **Scope gap located:** `Gamma_m^L=L_m-L_(m+1)/2` is an `L`-ledger interaction component. By itself it is not the complete physical entropy order-swap term at the data node. The latter also contains the phase/JS component `Gamma_m^Q`. B05 bounded only the terminal `Q_h`; it did not prove a prefix law or a sign for `Gamma_m^Q`. Thus the sentence that the displayed `Gamma_m^L` are, without qualification, the full credits absorbed by physical data-query nodes is not established by the written proof.
3. **Repair proved here, pending a fresh reviewer:** the phase packet obeys the same affine law. Its raw prefix credit is constant and nonnegative. Consequently the complete physical order-swap credit is `Gamma_m^L+Gamma_m^Q>=0`, and the exact full selector-decrement telescope holds. Because B19 supplied this missing argument, this strengthened version is not independently accepted by B19; it requires a fresh reviewer.

The result is still a specified-family amortization. It gives no universal stopping rule, no addressing theorem, and no proof of FEI.

## 1. Immutable source objects

The reviewed B05 bundle is at open-problems commit `8ffa3a930c849135d366d10d8d4f2e8afd0da67c`, path `reports/fei-2026-10-11/runs/B05/20261011T212522Z-account01-B05-data-prefix-a023/`.

The same report is visible in later commit `10bd8f25e7f93509b1ccb4daf9d8999fcb776f98` with:

* `REPORT.md` blob `c0353372b1e896045504067fb77724f588397527`;
* `CLAIMS.json` blob `d4c3c3746a10759421e8975547a9fd32117f98c0`;
* `PROGRESS.json` blob `256fbf8438568ea41e2cc6fe79adf6af3aab2f51`.

Dependencies actually used were the accepted family/activation notation from B05 commit `80cc2e5027efa56d79c4ecdf7d4949759ef2068b`, its B19 review at commit `7955d427222392911dc6af2e4ee3aa8aab67ac8c`, and the preceding control-first report at commit `440ecfff652a0b02f072c98bc4524d59a2a8bf2a` (report blob `4b02b427aaf3f2d683a4ec195c9b747976035272`).

No literature novelty is claimed. This is an internal reconstruction and strengthening of a campaign-specific calculation.

## 2. Independent reconstruction of the accepted `L` theorem

Let `k=2h`, `delta=2^(-k)`, `rho=2^(-h)=sqrt(delta)`, and

\[
b(u,v)=(-1)^{\sum_{j=1}^h u_jv_j}.
\]

Let `b'` flip only the origin and let `s` select `b` or `b'` with a fresh physical selector `y`. After `m` surviving restrictions `u_1=...=u_m=0`, put

\[
c_m=2^m\rho,\qquad e_m=2^m\delta=c_m\rho.
\]

### 2.1 Exact support and signs

The restricted background is a tensor of `m` constant coordinates and `h-m` quadratic pairs. Its normalized Walsh transform has support size `c_m^(-2)`, and every nonzero coefficient has magnitude `c_m`. Since the inverse transform at the origin is one, the signed coefficient sum is one. Therefore

\[
N_+(m)+N_-(m)=c_m^{-2},\qquad
c_m[N_+(m)-N_-(m)]=1,
\]

so

\[
N_\pm(m)=\frac{c_m^{-2}\pm c_m^{-1}}2.
\]

Flipping the origin subtracts `2e_m` from every normalized coefficient. At an old support frequency, the selector midpoint and half-difference are

\[
a=c_m(\pm1-\rho),\qquad v=c_m\rho;
\]

off support they are `a=-e_m`, `v=e_m`. This independently reproduces B05's complete support/sign ledger.

### 2.2 Affine packet and telescope

For `q=a^2+v^2` and `theta=v^2/q`, the conditional component of the selector decrement is

\[
\ell(a,v)=q h_2(\theta).
\]

Define

\[
P_\pm=((\pm1-\rho)^2+\rho^2)
h_2\!\left(\frac{\rho^2}{(\pm1-\rho)^2+\rho^2}\right),
\]

and `A_L=(P_++P_-)/2`, `B_L=(P_+-P_-)/2`. Summing the two support signs gives `A_L+c_m B_L`. The off-support count is `e_m^(-1)-c_m^(-2)`, and each off-support frequency contributes `2e_m^2`, hence total `2c_m rho-2delta`. Thus

\[
\boxed{L_m=A_L-2\delta+c_m(B_L+2\rho).}\tag{2.1}
\]

When `u_(m+1)=1`, the origin is excluded and the selector packet vanishes. When it is zero, the packet is `L_(m+1)`. Consequently

\[
\Gamma_m^L=L_m-\frac12L_{m+1}
=\frac{A_L-2\delta}{2}.\tag{2.2}
\]

For `rho<=1/2`, each support parameter lies in `[0,1/2]`; concavity gives `h_2(t)>=2t`. Hence `P_\pm>=2rho^2=2delta`, so `Gamma_m^L>=0`. Since the surviving prefix has probability `2^(-m)`, iteration gives

\[
\boxed{L_0=\sum_{m=0}^{h-1}2^{-m}\Gamma_m^L+2^{-h}L_h.}\tag{2.3}
\]

The activation event has probability `p=delta^2`, and it is applied once, after the core identity. The B05 terminal estimates also check:

\[
2^{-h}L_h\le2\delta+\delta\rho(k+\log_2 e),\qquad
2^{-h}Q_h\le\frac{2\delta}{\ln2}.\tag{2.4}
\]

This proves the narrow B05 theorem exactly as an `L`-ledger telescope plus a separately bounded terminal phase packet.

## 3. First unsupported physical-transfer line

Let `Delta_y(s_m)` denote the actual spectral-entropy decrement caused by restricting the physical selector. The standard midpoint/half-difference split is

\[
\Delta_y(s_m)=L_m+Q_m,
\]

where `Q_m` is the phase/JS packet. If `x=u_(m+1)`, the full two-coordinate order-swap interaction is

\[
\Delta_y(s_m)-\frac12\Delta_y((s_m)_{x=0})
-\frac12\Delta_y((s_m)_{x=1}).\tag{3.1}
\]

The `x=1` term vanishes and the `x=0` term is `Delta_y(s_(m+1))`, so (3.1) equals

\[
\Gamma_m^L+\Gamma_m^Q,
\qquad
\Gamma_m^Q:=Q_m-\frac12Q_{m+1}.\tag{3.2}
\]

The B05 report proved neither an expression nor a sign for `Gamma_m^Q`. A terminal bound on `Q_h` cannot determine the sign of the intermediate differences. Therefore (2.2) alone is not the complete physical data-node credit. This is a scope/chain gap, not a refutation of the `L` telescope.

## 4. Repair: the phase prefix is affine and nonnegative

For `0<=t<=1/2`, define

\[
j(t)=1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right).
\]

The phase contribution of a frequency is `q j(theta)`. Define

\[
R_\pm=((\pm1-\rho)^2+\rho^2)
j\!\left(\frac{\rho^2}{(\pm1-\rho)^2+\rho^2}\right),
\]

and `A_Q=(R_++R_-)/2`, `B_Q=(R_+-R_-)/2`. The support-count calculation is identical to section 2. Off support, `theta=1/2` and `j(1/2)=1`. Hence

\[
\boxed{Q_m=A_Q-2\delta+c_m(B_Q+2\rho).}\tag{4.1}
\]

It follows immediately that

\[
\boxed{\Gamma_m^Q=Q_m-\frac12Q_{m+1}
=\frac{A_Q-2\delta}{2},}\tag{4.2}
\]

independent of `m`.

To prove its sign, use the elementary binary-entropy inequality

\[
h_2(r)\le2\sqrt{r(1-r)},\qquad 0\le r\le1.
\tag{4.3}
\]

For completeness, write `r=(1+x)/2`, `0<=x<=1`, and

\[
F(x)=\sqrt{1-x^2}-h_2((1+x)/2).
\]

Then `F(0)=F(1)=0` and

\[
F'(x)=\frac{\operatorname{atanh}x}{\ln2}
-\frac{x}{\sqrt{1-x^2}}.
\]

The derivative of the right-hand side is

\[
\frac{\sqrt{1-x^2}/\ln2-1}{(1-x^2)^{3/2}},
\]

so `F'` first increases from zero and then decreases to minus infinity, crossing zero exactly once. Hence `F` first increases and then decreases between equal zero endpoints, proving (4.3). Taking

\[
r=\frac12+\sqrt{t(1-t)}
\]

gives `2sqrt(r(1-r))=1-2t` for `t<=1/2`, and therefore

\[
j(t)\ge2t.\tag{4.4}
\]

Each `R_\pm` is at least `2rho^2=2delta`, so `A_Q>=2delta` and

\[
\boxed{\Gamma_m^Q\ge0.}\tag{4.5}
\]

Combining (2.3) with its `Q` analogue proves the exact complete telescope

\[
\boxed{
\Delta_y(s_0)=
\sum_{m=0}^{h-1}2^{-m}(\Gamma_m^L+\Gamma_m^Q)
+2^{-h}\Delta_y(s_h).
}\tag{4.6}
\]

Finally, the general two-coordinate entropy identity

\[
\Delta_y H(f)-\mathbb E_x\Delta_y H(f_x)
=\Delta_x H(f)-\mathbb E_y\Delta_x H(f_y)
\tag{4.7}
\]

shows that every summand `Gamma_m^L+Gamma_m^Q` is exactly the physical selector/data order-swap interaction at the corresponding data node. Thus the intended physical interpretation is valid after adding (4.1)--(4.7).

## 5. Difficult-limit and falsifier audit

* **Smallest endpoint:** `k=2` (outside the stated `k>=4` theorem but algebraically meaningful) and every stated `k>=4` case pass the identities. No division by a vanishing support count occurs.
* **Large `k`:** the proof is analytic. The author's binary64 output at `k=60` cannot resolve all lower-order terms reliably, but no theorem step depends on that output. The independent checker uses 100-decimal-digit arithmetic through `k=200`.
* **Rare activation:** multiplication by `p=delta^2` occurs once after the core telescope. The prefix probability `2^(-m)` is separate and is not folded into `p` twice.
* **Sparse one-point defect:** all off-support frequencies are retained; their total is exactly `2c_m rho-2delta` for both packet functions.
* **Near tensors / prime gates:** the proof uses equal quadratic-pair magnitudes. It does not survive unequal factors automatically.
* **Addressing/multiplexers:** no addressing claim follows. The support-count affine law is special to this bent construction.
* **Shared variables:** the two selector children share all data. The direct physical restrictions and the full order-swap identity retain that interference.
* **Boolean realizability:** every function used is a genuine Boolean sign; no relaxed prefix law is substituted.

## 6. Independent computation

`B05_FULL_PREFIX_CHECK.py` is independent of B05's binary64 script. It constructs genuine restricted truth tables, uses exact integer FWHTs, and evaluates only logarithms/square roots with 100-decimal-digit `Decimal` arithmetic. It checks:

* direct truth-table `L_m` and `Q_m` against (2.1) and (4.1) for `k=2,4,6,8,10` and all `m`;
* `Delta_y=L+Q` directly from three spectral entropies;
* constancy and nonnegativity of both raw credits;
* equality of `Gamma_m^L+Gamma_m^Q` with the physical two-coordinate order-swap expression;
* closed-form nonnegativity for every even `k` from 2 through 200.

Command and result:

```text
python B05_FULL_PREFIX_CHECK.py
status=PASS
truth_table_rows_checked=15
closed_form_k_even_checked=2..200
decimal_digits=100
max_truth_table_formula_error=6.184000E-98
```

There is no random seed or search. The finite computation corroborates but does not replace the all-`k` proof.

## 7. Claim/dependency delta and next action

* `B05-A023-BENT-DATA-PREFIX-TELESCOPE-v1`: **accepted only in the narrowed reading** “exact nonnegative `L`-ledger telescope plus terminal full-packet bound.” The stronger physical-node sentence needs the phase repair.
* `B19-A094-BENT-FULL-PREFIX-TELESCOPE-v1`: **analytically proved pending fresh independent review.** It adds the exact `Q_m` affine formula, `Gamma_m^Q>=0`, the full `L+Q` telescope, and the physical order-swap identification.
* Packet A023 remains partial. Full FEI remains open.

The next mathematically discriminating test is the one requested by B05: replace identical bent pairs by unequal genuine prime Boolean factors and freeze the resulting factor-dependent ratios. Determine whether the scalar inequality behind (4.4) plus the new support/sign weights still makes every complete `L+Q` raw credit nonnegative. The first negative instance would delimit the mechanism; a proof would supply a nontrivial near-tensor extension.

Fresh review should be routed to A087 (or another reviewer not contributing this repair), with B05 and B20 as consumers.

## 8. Execution metadata

The runtime exposed Codex; no model selector, reasoning-effort selector, continuous-hour guarantee, billing identity, or remaining allowance meter was exposed. Natural derivation, exact computation, persistence, independent review, and native Brain ingestion are recorded separately. No protected evaluation material, held request, scheduler state, email, public release, merge, or live-store mutation was accessed.
