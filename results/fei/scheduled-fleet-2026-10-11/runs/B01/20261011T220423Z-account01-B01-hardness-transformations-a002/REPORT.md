# B01 / A002 — hardness-preserving Boolean transformations

Run: `20261011T220423Z-account01-B01-hardness-transformations-a002`  
Primary packet: `A002` (Hardness-preserving transformations)  
Stable gap: `G-R-SELECT`  
Status: **PROVED transformation ledger pending independent review; full FEI remains OPEN**

## 1. Exact objective and mathematical movement

The preceding A003 run froze three full-FEI-strength endpoints. Its restriction-step target quantifies over all genuine Boolean seeds, but the arbitrary-seed admission statement had only the disjoint tensor identity. A002 requires the exact tensor, balancing, activation, and coding transformations, including what each transformation destroys.

This run proves the complete ledger and a joint embedding theorem:

> For every nonconstant Boolean seed `g` and every `epsilon>0`, there is a genuine Boolean `F` with full Walsh support such that
> \[
> I(F)\le\epsilon,\qquad
> \max_i I_i(F)/I(F)\le\epsilon,\qquad
> \Pr(F=-1)\le\epsilon,
> \]
> and
> \[
> \left|\frac{H(F)}{I(F)}-\frac{H(g)}{I(g)}\right|\le\epsilon.
> \]

Consequently, the optimal FEI constant on this simultaneous full-support/low-influence/rare-output class is exactly the unrestricted optimal constant. This is an admission theorem, not a bound on that constant.

In contrast, the embedding introduces cheap physical control coordinates. It does **not** preserve high restriction-step criticality. Tensoring is the only transformation below that preserves every local ratio exactly. The distinction closes a possible circular use of the A003 `STEP(K)` endpoint.

The component identities are in `TRANSFORMATION_LEDGER.tex`; property survival is frozen in `HYPOTHESIS_SURVIVAL.json`.

## 2. Conventions

For a sign-valued Boolean function on the uniform cube, write

\[
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},
\quad
I(f)=\sum_S|S|\widehat f(S)^2,
\quad
\mu(f)=\mathbb Ef.
\]

Let `phi(t)=t log_2(1/t)`, with `phi(0)=0`. All new physical inputs are fresh, disjoint, and uniformly independent. Statements about spectral independence are made only where coefficient factorization proves them.

## 3. Tensor ledger

For `f` and `g` on disjoint variable blocks, let `T=f g`. Fourier coefficients factor:

\[
\widehat T(A\cup B)=\widehat f(A)\widehat g(B).
\]

Thus the spectral set is the union of two independent spectral sets and

\[
\boxed{
H(T)=H(f)+H(g),\quad I(T)=I(f)+I(g),\quad \mu(T)=\mu(f)\mu(g).
}\tag{3.1}
\]

Every physical coordinate retains its directional influence. More strongly, for a coordinate `i` in the `f` block,

\[
I_i(T)=I_i(f),\qquad \Delta_iH(T)=\Delta_iH(f),\tag{3.2}
\]

because both children retain the independent `g` spectral factor. Hence tensor powers satisfy

\[
H(f^{\otimes m})=mH(f),\quad I(f^{\otimes m})=mI(f),
\quad \mu(f^{\otimes m})=\mu(f)^m,\tag{3.3}
\]

and preserve every local `Delta_iH/I_i` ratio exactly. Full Walsh support is preserved iff every factor has full support. Balance is preserved if at least one factor is balanced.

## 4. Balancing and two-cell selector ledger

### 4.1 Dictator balance

With one fresh sign `y`, put

\[
B_g(x,y)=y g(x).
\]

Its spectrum is a label shift `S -> S union {y}`. Therefore

\[
\boxed{
\mu(B_g)=0,quad H(B_g)=H(g),quad I(B_g)=I(g)+1.
}\tag{4.1}
\]

This destroys full Walsh support in the enlarged cube and destroys restriction criticality: `Delta_yH(B_g)=0` while `I_y(B_g)=1`.

### 4.2 Two-cell selector

For balanced `h` and two fresh signs `y_1,y_2`, define

\[
M_h=\frac{1+h}{2}y_1+\frac{1-h}{2}y_2.
\]

This is a genuine Boolean selector. The pure `y_1,y_2` coefficients and the two signed copies of each nonempty coefficient of `h` are disjoint, giving

\[
\boxed{
\mu(M_h)=0,quad H(M_h)=2+\frac12H(h),quad
I(M_h)=1+\frac12I(h).
}\tag{4.2}
\]

For an arbitrary nonconstant seed `g`, take

\[
h_m=y_0 g^{\otimes m}.
\]

It is balanced and has `H(h_m)=mH(g)`, `I(h_m)=mI(g)+1`. Thus the two-cell selector has dimension `mn+3` and

\[
\frac{H(M_{h_m})}{I(M_{h_m})}
=\frac{2+mH(g)/2}{3/2+mI(g)/2}
\longrightarrow\frac{H(g)}{I(g)}.\tag{4.3}
\]

Hence unrestricted two-cell selectors retain arbitrary FEI hardness. The limit uses a growing tensor count; a fixed single selector does not preserve the ratio exactly.

## 5. Sparse activation with arbitrary mean

Let `A_r(z)=prod_{j=1}^r(1+z_j)/2`, `p=2^{-r}`, and

\[
F(x,z)=1+A_r(z)(g(x)-1).
\]

The circuit equals `g` only on the all-active control cell and equals `+1` otherwise. Direct truth-table probabilities give

\[
\boxed{
\mu(F)=1-p+p\mu,qquad
\Pr(F=-1)=\frac p2(1-\mu).
}\tag{5.1}
\]

A data coordinate is pivotal only on the active cell. A control coordinate is pivotal exactly when all other controls are active and `g=-1`. Hence

\[
\boxed{
I(F)=p\{I(g)+r(1-\mu)\},quad
I_i(F)=pI_i(g),quad I_{z_j}(F)=p(1-\mu).
}\tag{5.2}

The Fourier coefficients split into three disjoint types:

* constant coefficient `1-p+p mu`;
* each nonempty pure-control coefficient has magnitude `p(1-mu)`;
* for every nonempty data set `S` and every control set `U`, the coefficient has magnitude `p |ghat(S)|`.

Summing their raw entropies proves the arbitrary-mean identity

\[
\boxed{
\begin{aligned}
H(F)={}&p\{H(g)-\phi(\mu^2)\}+2rp(1-\mu^2)\\
&+(2^r-1)\phi\bigl(p^2(1-\mu)^2\bigr)
+\phi\bigl((1-p+p\mu)^2\bigr).
\end{aligned}}
\tag{5.3}
\]

For balanced `g`, this reduces to the recovered formula

\[
H(F)=pH(g)+2rp(2-p)+(1-p)^2\log_2\frac1{(1-p)^2},
\quad I(F)=p(I(g)+r).\tag{5.4}
\]

If `g` has full Walsh support and is nonconstant, then `F` has full support for every `r>=1`: all three coefficient types above are nonzero. Physical input independence remains exact, but the spectral control and data labels are correlated through the three-type mixture.

Activation does not preserve `STEP` criticality. The controls may have small entropy decrement relative to their influence; in odd-module constructions this ratio can tend to zero. Therefore low influence or rare output alone cannot be used as a critical-core terminal.

## 6. Auxiliary coding ledgers

### 6.1 Parity lift

For one fresh physical sign `z`, set

\[
P_g(x,z)=g(x_1z,\ldots,x_nz).
\]

In the Fourier expansion, each seed set `S` is relabelled as

\[
S\quad\mapsto\quad
S\cup\{z:|S|\text{ is odd}\}.
\]

Thus

\[
\boxed{
H(P_g)=H(g),\quad \mu(P_g)=\mu(g),quad
I(P_g)=I(g)+\Pr_{S\sim P_g}(|S|\text{ odd})\le2I(g).
}\tag{6.1}
\]

Every lifted spectral set has even cardinality, so each spectral membership bit is determined by the others. Consequently

\[
\boxed{B(P_g)=\sum_iH(S_i\mid S_{-i})=0.}\tag{6.2}
\]

The physical restriction `z=+1` is exactly `g`. This lift uses independent physical inputs but creates maximal deterministic spectral parity correlation. It destroys full Walsh support and shows why zero erasure is not an easy FEI terminal.

### 6.2 One-point full-support surgery

Let `u` be a Boolean truth table on `N>=2` inputs with an odd number of negative outputs. Every unnormalized Walsh sum is `2 mod 4`, up to sign, and therefore nonzero. Any truth table can be made odd-negative by flipping at most one value.

Apply this to `g^{otimes m}`, `N=mn`. If `u_m` is the resulting full-support function, the normalized Fourier vectors differ in `l_2` by at most

\[
2^{1-N/2}.
\]

The total variation `tau_m` of their squared spectral laws is at most the same quantity. Entropy continuity on `2^N` atoms and the `N` affected incident edges give

\[
\boxed{
H(u_m)=mH(g)+o(1),\quad I(u_m)=mI(g)+o(1),
\quad \mu(u_m)=\mu(g)^m+O(2^{1-N}).
}\tag{6.3}

More explicitly,

\[
|H(u_m)-mH(g)|\le h_2(\tau_m)+\tau_m\log_2(2^N-1),
\quad |I(u_m)-mI(g)|\le2N2^{-N}.\tag{6.4}
\]

This preserves the global ratio asymptotically, not local coordinate structure.

## 7. PROVED: simultaneous full-support/low-influence/rare-output embedding

Fix a nonconstant seed `g` in dimension `n`. Let `u_m` be the full-support surgery of `g^{otimes m}`. Since `|mu(g)|<1`, equation (6.3) gives `mu(u_m)=o(1)`. Set

\[
r_m=\lceil\sqrt m\rceil,qquad p_m=2^{-r_m},qquad
F_m=1+A_{r_m}(u_m-1).
\]

Its dimension is

\[
N_m=mn+r_m.
\]

By section 5, every `F_m` is genuine Boolean and has full Walsh support. Moreover,

\[
I(F_m)=p_m\{mI(g)+o(m)+r_m(1-o(1))\}
\sim p_m mI(g)\longrightarrow0,\tag{7.1}
\]

\[
\max_i I_i(F_m)\le2p_m,qquad
\frac{\max_i I_i(F_m)}{I(F_m)}\longrightarrow0,\tag{7.2}
\]

and

\[
\Pr(F_m=-1)=\frac{p_m}{2}(1-o(1))\longrightarrow0.\tag{7.3}
\]

Divide (5.3) by `p_m m`. Equations (6.3), `r_m/m ->0`, and the elementary endpoint bounds for `phi` give

\[
\frac{H(F_m)}{p_m m}\longrightarrow H(g),qquad
\frac{I(F_m)}{p_m m}\longrightarrow I(g).
\]

Therefore

\[
\boxed{
\frac{H(F_m)}{I(F_m)}\longrightarrow\frac{H(g)}{I(g)}.
}\tag{7.4}

This proves the epsilon-form theorem in section 1. More precisely, for every `eta>0` define

\[
R(\eta)=\sup\left\{\frac{H(F)}{I(F)}:\ F\text{ nonconstant and full support},\
 I(F)\le\eta,\ \frac{\max_iI_i(F)}{I(F)}\le\eta,\
 \Pr(F=-1)\le\eta\right\}.
\]

Subclass inclusion gives `R(eta)<=C_FEI`. Given any seed and any accuracy `delta>0`, apply the construction with the smaller tolerance `min(eta,delta)`; the resulting function lies in the class defining `R(eta)` and its ratio is within `delta` of the seed ratio. Taking first the supremum over seeds and then `delta` to zero gives

\[
\boxed{R(\eta)=C_{FEI}\quad\text{for every }\eta>0}\tag{7.5}

in the extended-real sense.

This architecture is consistent with Shalev's earlier low-influence reduction. No novelty claim is made for tensor-plus-activation. The contribution here is the source-pinned exact arbitrary-mean ledger and the simultaneous hypothesis-survival statement required by A002.

## 8. Mandatory falsifiers and scope controls

* **Addressing/multiplexers:** choose the whole-set addressing function as `g`; (4.3) and (7.4) preserve its ratio. Neither two-cell selectors nor the joint-smallness class excludes it.
* **Sparse defects and rare restrictions:** choose the accepted one-point-defect seed. The global `H/I` ratio survives, including rare logarithms. Activation introduces cheap controls, so the every-coordinate B05 obstruction is not claimed to survive.
* **Near tensors:** the construction starts from arbitrary `g` and its exact tensor powers; one truth-table flip is exponentially negligible globally but may destroy local factorization. No near-tensor local theorem is inferred.
* **Actual prime gate:** the two-bit AND sign can be used as `g`; all transformations remain genuine Boolean circuits. The checker includes every nonconstant two-bit gate.
* **Parity-zero erasure:** (6.2) deliberately realizes it while retaining `H(g)`, so erasure-zero terminal arguments remain invalid.
* **Shared-variable interference:** none of the tensor or activation formulas is extended to overlapping physical factors. The two-cell selector proof uses exact coefficient disjointness created by fresh leaves.

## 9. Deterministic verification

`verify_transformations.py` independently constructs truth tables and exact integer Walsh transforms. It checks every nonconstant Boolean function through dimension three, tensor squares, dictator balancing, two-cell selectors, arbitrary-mean activation for `r=1,2`, every physical influence, and parity lifts. It also verifies the odd-negative full-support lemma on all truth tables through dimension four.

Command and output:

```text
python verify_transformations.py
status=PASS
nonconstant_functions_checked=270
identity_checks=7254
odd_negative_full_support_tables_checked=32904
max_abs_error=8.882e-16
random_seed=None
```

Integer Walsh calculations are exact; entropy comparisons use binary64 only as finite corroboration. The all-dimensional results are the analytic proofs above.

## 10. Literature and source pins

* Campaign claim ledger `C012`--`C015`: `research_pushes/2026-10-11-full-fei-100-agents/CLAIMS.md`, blob `d7279735b4dcfaf7552cf271b7413fc5c0f427b6`.
* Recovered research-status summary: `research_pushes/2026-10-11-full-fei-100-agents/baseline/RESEARCH_STATUS.md`, blob `fb2178e17184af14f42b23b342d8f466243c763f`.
* Full-support collision admission proof: `research_pushes/2026-09-30-fei-log-allocation/COLLISION_ADMISSION.md`, blob `9d259f117479d325b9bddc431a85afd5639db9a9`.
* Joint-smallness and cheap-coordinate boundary: `proofnet24/P03-fei/continuations/2026-09-30-critical-odd-modules/REPORT.md`, blob `79510a3f9b5781ad86ecaa156579fbea79899b74`.
* Primary literature: Guy Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, arXiv:1806.03646, Theorems 3 and 19 and Section 3.2. It proves that an appropriate `I(f)<=2^{-s(n)}`, `s(n)=o(n)`, class result implies full FEI and credits the activation mechanism to Wan--Wright--Wu.

No publication-priority claim is made.

## 11. Claim delta, remaining obstruction, and handoff

**PROVED pending independent review:**

1. `B01-A002-ARBITRARY-MEAN-ACTIVATION-LEDGER-v1`, equations (5.1)--(5.3).
2. `B01-A002-JOINT-HARDNESS-EMBEDDING-v1`, equations (7.1)--(7.5).
3. Complete survival ledger for tensoring, balancing, parity coding, full-support surgery, and activation.

**OPEN:** all three A003 universal constants. The new embedding does not bound `C_step`, `C_L`, or the posterior-forest residual. In particular, its cheap controls prevent it from supplying high-criticality counterexamples.

A086 or A094 should review the arbitrary-mean Fourier partition in (5.3), the full-support proof, and every limit after division by `p_m m`. A005 should use `HYPOTHESIS_SURVIVAL.json` to reject any supposedly easier endpoint that admits the joint class but has no mechanism beyond the conditions listed there.

Next B01 action: A005 noncircularly test the frozen A003 endpoints against these embeddings, beginning with any proposed `STEP` proof that uses only full support, rare output, or small influences.

## 12. Execution metadata

The runtime exposed Codex. It exposed no model selector, reasoning-effort selector, continuous-hour guarantee, billing identity, or remaining allowance meter. Natural research, computation, persistence, independent review, and native Brain ingestion are recorded separately. No protected evaluation material, held request, scheduler change, email, public release, merge, deployment, paid-credit use, or live-store mutation was used.
