# B05 / A023: rare logarithmic debt is transported, not paid, by control-first revelation

Run ID: `20261011T202804Z-fleet01-B05-rare-restrictions-a023`  
Primary packet: `A023` (Amortized rarity budget)  
Stable gap / obstruction: `B05_RARE_REFUNDS` / `O-B05`  
Attempt: `A023-ORDER-1`  
Full FEI status: **OPEN**

## Outcome

**PROVED, pending independent review.** For the accepted sparse activated bent one-point-surgery family, revealing every activation control before revealing the selector does not amortize away the selector's rare logarithm. It moves the same leading selector packet to the all-zero control branch. If `d=2^{-3k}` is the selector influence, then both orders incur

\[
  d\bigl(k+\log_2 e+o(1)\bigr)
\]

of selector packet entropy. The two orders differ only through the empty-data Fourier packet, by at most

\[
  d\,2^{-k}(3k+7)
\]

for every even `k >= 4`.

This is a precise no-go theorem for the proposed control-first first-revelation rule. It does **not** refute an optimized adaptive tree that interleaves data queries, a nonlocal child-deficit transport, or FEI.

## Exact target and prior status

The accepted claim `B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO-v1` proves that no fixed constants `K,A,B` pay every selector node by

\[
 L\le Kd+A V_{\rm post}+B M_{\rm inf}.
\]

Its exact family and scope were independently accepted in B19. Its next action was to compare the two genuine physical restriction orders and retain terminal entropy. The unresolved question was whether revealing the rare activation event first supplies a one-use global credit that removes the logarithmic selector bill.

The bounded objective here was therefore:

> For the same actual Boolean family, compare (i) selector first and (ii) all activation controls first, using an exact entropy telescope; identify the order-swap correction and determine whether the `d k` debt survives.

## Boolean family and conventions

Let `k >= 4` be even, put

\[
 \delta=2^{-k},\qquad r=2k,\qquad p=2^{-r}=\delta^2,
 \qquad d=p\delta=\delta^3.
\]

Work on `F_2` coordinates, with the standard normalized Walsh transform and entropy in bits. Define the quadratic bent sign function

\[
 b(x)=(-1)^{x_1x_2+\cdots+x_{k-1}x_k}.
\]

Then `b(0)=1`, `E b=sqrt(delta)`, and every Walsh coefficient of `b` has magnitude `sqrt(delta)`. Flip exactly the origin:

\[
 b'(x)=b(x)-2\mathbf 1_{\{x=0\}}.
\]

Thus `b'` is still sign-valued and

\[
 \widehat {b'}(T)=\widehat b(T)-2\delta
 \quad\text{for every }T.
\]

Let `y` be a fresh physical selector and set

\[
 s(y,x)=\frac{b(x)+b'(x)}2+y\frac{b(x)-b'(x)}2.
\]

Let `z in F_2^r`, `A(z)=1_{z=0}`, and activate on one control point:

\[
 F(y,x,z)=1+A(z)(s(y,x)-1).
\]

The two selector children are the genuine Boolean functions

\[
 G(x,z)=1+A(z)(b(x)-1),\qquad
 H(x,z)=1+A(z)(b'(x)-1).
\]

Activation and selection commute exactly. This is the structural reason the two orders can be compared without a surrogate distribution.

For a selector with Fourier midpoint `a_W` and selector half-difference `v_W`, put

\[
 q_W=a_W^2+v_W^2,\qquad \theta_W=v_W^2/q_W,
 \qquad \Psi(a,e)=(a^2+e)h_2\!\left(\frac e{a^2+e}\right),
\]

with zero packets contributing zero. Its packet entropy is `L=sum_W q_W h_2(theta_W)`.

## 1. Exact order comparison for the selector packet

For the unactivated core selector `s`, every data frequency `T` has

\[
 a_T=\widehat b(T)-\delta,\qquad v_T=\delta,
 \qquad q_T=(\widehat b(T)-\delta)^2+\delta^2.
\]

Write

\[
 L_{\rm core}=\sum_T\Psi(\widehat b(T)-\delta,\delta^2).
\]

If the controls are revealed first, the selector is encountered only on the event `z=0`, of probability `p`. Hence the complete expected selector packet in the control-first tree is exactly

\[
 L_{\rm CF}=pL_{\rm core}. \tag{1}
\]

For the selector-first tree, the activation transform gives the following Fourier midpoint and selector half-difference.

* If `T` is nonempty, then for every control frequency `U`,
  \[
  a_{T,U}=p(\widehat b(T)-\delta),\qquad v_{T,U}=p\delta.
  \]
  Therefore `theta_{T,U}=theta_T`; summing the `p^{-1}` control copies gives exactly `p` times the core contribution.
* For `T=emptyset` and `U` nonempty,
  \[
  a_{\varnothing,U}=p(\sqrt\delta-\delta-1),\qquad v_{\varnothing,U}=p\delta.
  \]
* At `(T,U)=(emptyset,emptyset)`,
  \[
  a_{\varnothing,\varnothing}=1+p(\sqrt\delta-\delta-1),\qquad
  v_{\varnothing,\varnothing}=p\delta.
  \]

Consequently the selector-first packet `L_SF=L(F;y)` satisfies the exact identity

\[
\begin{aligned}
L_{\rm SF}-pL_{\rm core}
={}&(p^{-1}-1)\Psi\!\left(p(\sqrt\delta-\delta-1),p^2\delta^2\right)\\
&+\Psi\!\left(1+p(\sqrt\delta-\delta-1),p^2\delta^2\right)\\
&-p\Psi(\sqrt\delta-\delta,\delta^2). \tag{2}
\end{aligned}
\]

Thus the order discrepancy is supported entirely on the empty-data frequency. All nonempty data frequencies transport their rarity logarithm with coefficient exactly one.

## 2. Uniform bound on the order correction

For `0<e<=a^2+e`, binary entropy obeys

\[
 \Psi(a,e)\le e\log_2\!\left(\frac{e_{\rm Euler}(a^2+e)}e\right). \tag{3}
\]

For even `k>=4`, the three absolute contributions in (2) obey:

\[
\begin{array}{rcl}
p\Psi(\sqrt\delta-\delta,\delta^2)
 &\le& p\delta^2(k+3),\\
(p^{-1}-1)\Psi(p(\sqrt\delta-\delta-1),p^2\delta^2)
 &\le& p\delta^2(2k+3),\\
\Psi(1+p(\sqrt\delta-\delta-1),p^2\delta^2)
 &\le& p^2\delta^2(6k+3)\le p\delta^2.
\end{array}
\]

The last inequality uses `delta^2(6k+3)<=1`, valid from `k=4` onward and decreasing thereafter. The triangle inequality now gives

\[
 \boxed{\ |L_{\rm SF}-L_{\rm CF}|\le p\delta^2(3k+7)
       =d\delta(3k+7).\ } \tag{4}
\]

No pointwise `O(d)` payment has appeared; the correction is smaller than the leading debt by a factor tending to zero.

## 3. The unpaid logarithm

Uniformly in `T`,

\[
 q_T=\delta(1+O(\sqrt\delta)),\qquad
 \theta_T=\delta(1+O(\sqrt\delta)).
\]

Also `q_T theta_T=delta^2` exactly. From

\[
 h_2(t)=t\log_2(1/t)+t\log_2 e+O(t^2)
\]

and the `delta^{-1}` data frequencies,

\[
 L_{\rm core}=\delta\bigl(k+\log_2 e+O(\sqrt\delta)\bigr). \tag{5}
\]

Combining (1), (4), and (5),

\[
 \boxed{
 \frac{L_{\rm CF}}d=k+\log_2 e+O(\sqrt\delta),\qquad
 \frac{L_{\rm SF}}d=k+\log_2 e+O(\sqrt\delta+\delta k).
 } \tag{6}
\]

The activation event is indeed revealed only once in the control-first tree, but after that revelation the one-point defect still has conditional rarity `delta`. Its expected entropy charge is `p * delta log_2(1/delta)=d k`. A bounded scalar first-revelation credit cannot pay this family.

## 4. Exact full entropy swap ledger

The comparison above concerns the rare packet `L`, not a truncated tree. Terminal entropy is retained by the following exact identity.

For any Boolean `u` with mean `a`, let

\[
 \mathcal A_pu=1+A(z)(u-1),\qquad
 C_p(a)=H(\mathcal A_pu)-pH(u).
\]

Directly from the activation Fourier coefficients, `C_p` depends only on `a` and equals, with `R=log_2(1/p)` and `phi(t)=t log_2(1/t)`,

\[
\begin{aligned}
C_p(a)={}&\phi((1-p(1-a))^2)
 +p(1-p)(1-a)^2\left[2R+\log_2\frac1{(1-a)^2}\right]\\
&+2pR(1-a^2)-p\phi(a^2). \tag{7}
\end{aligned}
\]

Let `Delta_y(g)=H(g)-[H(g|y=1)+H(g|y=-1)]/2`. Since the means of `b,s,b'` are respectively `sqrt(delta)`, `sqrt(delta)-delta`, `sqrt(delta)-2delta`,

\[
\begin{aligned}
\Delta_y(F)-p\Delta_y(s)
={}&C_p(\sqrt\delta-\delta)\\
&-\frac12 C_p(\sqrt\delta)
-\frac12 C_p(\sqrt\delta-2\delta). \tag{8}
\end{aligned}
\]

Equation (8) is the exact global debt/refund created by swapping the control prefix past the selector. It is a scalar empty-frequency Jensen correction. Equation (2) isolates its `L` component; the remainder is the phase/KL component. Therefore neither ordering discards terminal entropy or silently reuses an activation credit.

## 5. First-revelation ledger and stopping rule

The tested stopping rule is physical, adaptive, finite, and uses no nonphysical bias:

1. Query `z_1,...,z_r` in order.
2. At the first `z_i=1`, stop: the residual function is the constant `1`.
3. If all controls are zero (probability `p`), query the genuine selector `y`; then continue on the selected Boolean core.

The activation credit is owned only when the all-zero control event is resolved and is never reused below that point. Nevertheless the expected selector debt below it is (1), with the growing ratio (6). The complete machine-readable audit is in `RARITY_CREDIT_LEDGER.json`.

This closes the specific mechanism "reveal the activation controls first and pay rarity once." It leaves open a mechanism that queries data before resolving the selector, or that transports a child deficit with an additional nonlocal invariant.

## 6. Validation

`rare_order_checker.py` performed two checks.

* Direct normalized Walsh transforms of the actual sign truth tables for `k=2,4`, including all `r=2k` controls, verified:
  * `Delta=L+Q` for the core and activated selector;
  * equation (8) against the scalar formula (7);
  * the aggregated formula (2) against the full transform.
* Aggregated exact-formula evaluation for `k=4,6,8,10,12,16,20` checked the asymptotic transport and the analytic bound (4).

Command:

```text
python3 rare_order_checker.py
```

Observed runtime was 4.6 seconds. Arithmetic was IEEE-754 binary64 for numerical corroboration. The all-`k` claim and bound are analytic and do not depend on floating-point signs. There was no random seed and no search.

At `k=20`,

\[
 L_{\rm core}/\delta=21.4426916012,\quad
 L_{\rm SF}/d=21.4427106747,
\]

and the relative order error was `8.8951e-7`. The full output is archived in `checker_output.txt`.

## 7. Mandatory falsifiers and exact scope

* **Sparse one-point defect / rare restriction:** this is the test family itself, with an actual Boolean origin flip and an actual `2^{-2k}` control event.
* **Near tensor:** `b` is a tensor of genuine two-bit quadratic gates, while the origin flip destroys the exact tensor factorization; no tensor-only cancellation is assumed.
* **Actual prime Boolean gate:** `y` is a fresh physical selector coordinate. No synthetic mixture or changed prior replaces it.
* **Shared-variable interference:** both selector children share every control and data variable; the exact Fourier formulas retain this interference.
* **Terminal entropy and parity-zero erasure:** (7)–(8) retain the terminal core entropy and all empty-frequency coefficients. Zero packets use the declared zero convention.
* **Addressing / whole-set controls:** no conclusion is drawn about addressing functions or existential coordinate choice. The theorem refutes only this declared control-first stopping rule on this declared family.

There is no claim of literature novelty. This is a source-bound campaign derivation from the already accepted B05 family.

## 8. Status, dependency delta, and next action

Claim `B05-A023-CONTROL-FIRST-ORDER-TRANSPORT-NOGO-v1` is **ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW**.

Packet `A023` remains **OPEN / PARTIAL_PROGRESS**: the run proves a rigorous growing expected debt for the proposed rule, satisfying the pilot renewal milestone, but it does not construct the positive complete amortization demanded by the packet's target statement.

Downstream consequence: A027, A028, and A064 must not treat a control-first activation stopping rule with bounded `O(d)` first-revelation credit as sufficient. A positive potential must either carry an explicit `d log(1/delta)` credit, obtain a matching KL/terminal cancellation, or change the stopping geometry.

Independent review requested from A087 or A094. The review should reconstruct (2) from the physical Fourier transform, verify the bound in (4) without floating point, and check that the full entropy swap (8) preserves terminal terms.

Next mathematical action: query one data coordinate before the selector on the all-zero control branch and determine whether the `d k` bill decreases by a telescoping conditional KL credit or simply redistributes across the two data children. This is materially different from another control/selector reorder.

## Sources actually read and relied on

* Current campaign files at open-problems branch head `ba64c22ce44969cb56166874de8224207800dec9`:
  * `CURRENT_STATUS.md`, blob `8c9c63579ecdd4afa385bb94caf79ee6296addcf`;
  * `STREAM_PACKET_INDEX.json`, blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`;
  * `assignments/B05.json`, blob `05447e6d999437bb82a266b427bd76a4b37266b6`;
  * `EXECUTION_PROTOCOL.json`, blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
  * `PACKET_STATUS.json`, blob `3a5ca0894678a9fd9908aae9596923d3038a03f8`;
  * `CLAIM_REGISTRY.json`, blob `6a3e1aa94f81ec01841a083c97449739b9e72baa`;
  * `OBSTRUCTION_REGISTRY.json`, blob `dd482025647aed25166b46cc217a7ed77dcaa767`.
* Original B05 proof: open-problems commit `80cc2e5027efa56d79c4ecdf7d4949759ef2068b`, `reports/fei-2026-10-11/runs/B05/20261011T193057Z-fleet01-B05-rare-restrictions/REPORT.md`.
* Independent B19 review: open-problems commit `7955d427222392911dc6af2e4ee3aa8aab67ac8c`, corresponding B19 run report.
* Current Brain campaign mirror at branch head `653d3533acb3fce8196bdb50eaa046bcff2b5a58`; `CURRENT_STATUS.md` has the same blob `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.
* Reconciled supplement seed files at the owner-provided baseline commits `bfb1d10b25cb5cb2e09112357cd24b21b5b1fe5e` (open-problems) and `4c068736601dade589d094a37bdb880ad0cd1416` (Brain), including `REPORT.md`, `CAMPAIGN.md`, `NATIVE_MAPPING.md`, `COUNTEREXAMPLES.md`, and `SEED_LEMMAS.md`.

No protected evaluation material, held request payload, held PR229/source, email, scheduler state, or public-release operation was accessed.

## Execution metadata

Exposed assistant identity: Codex, based on GPT-5. A reasoning-effort selector and continuous-hour guarantee were not exposed. The only timed compute was the 4.6-second checker above. Natural mathematical derivation, validation, artifact writing, persistence, and readback are recorded separately; no claim is made about unobserved capacity or downstream ingestion.

