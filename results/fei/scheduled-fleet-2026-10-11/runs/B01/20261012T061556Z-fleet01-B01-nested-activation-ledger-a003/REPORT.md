# B01 / A003 — depth-free singleton-log ledger for nested fresh activations

**Run:** `20261012T061556Z-fleet01-B01-nested-activation-ledger-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-UPPER-SET-ASYMMETRY`  
**Attempt:** `A003-GUP-NESTED-ACTIVATION-LEDGER-3`  
**Status:** an all-depth restricted-class theorem is author-proved and pending A086/A094 review. Full FEI remains **OPEN**.

## 1. Frozen obstruction and prior status

For `p(S)=hat f(S)^2`, `pi(S)=sum_{T superset S} p(T)`, write

`U(f)=sum_S p(S) log_2(pi(S)/p(S))`

and

`G(f)=sum_i [U(f)-E U(f|x_i)]`.

The universal target remains `G(f)<=aI(f)+bU(f)` with absolute `a<infinity` and `b<1`. The previous A003 run proved that a one-layer fresh activation cannot pay its excess using only fresh-selector influence and newly created `U`: balanced majority leaves a `(1/pi)log_2 n+O(1)` mismatch. It identified the unpaid term

`p L_1(g)`, where `L_1(g)=sum_j hat g({j})^2 log_2(1/hat g({j})^2)`.

The bounded objective here was to retain that exact logarithmic credit and determine whether repeated fresh activations necessarily charge it once per depth, or whether its physical Fourier scaling supplies a single-use ledger.

## 2. Repaired one-layer inequality

For a Boolean core `g`, let a fresh block of `d>=1` controls activate `g` on one word and output `1` otherwise. Put `p=2^(-d)`, `r=Pr[g=-1]`, and call the resulting function `F`. Define

`W_1(g)=sum_j hat g({j})^2`.

Using the exact prior activation identity and the scalar rewrite

`R_p(r)=M(pr)-pM(r)+2p phi(r)-2phi(pr)`,  
`phi(x)=x^2 log_2(1/x^2)`, `M(t)=phi(1-2t)`,

this run proves the central-difference modulus

`|phi(x)-[phi(x+h)+phi(x-h)]/2| <= 64h^2(1+log_2(1/h))`.

Since `|r_{j,+}-r_{j,-}|=|hat g({j})|`, the complete signed data-coordinate charge is bounded by the retained singleton credit, yielding

`G(F) <= pG(g)+320p[W_1(g)+L_1(g)]+C_* I_ctl`,

where

`C_*=1+2(1+1/e)/ln 2 < 4.947`, `I_ctl=2rpd`.

This repairs the exact failure found in the majority family: the logarithmic term is retained rather than replaced by a pointwise `O(I_ctl)` budget.

## 3. All-depth nonreuse theorem

Let `f_0=g`. At stage `t`, activate `f_{t-1}` on one word of a fresh block of `d_t>=1` controls, outputting `1` elsewhere. Put

`D_t=d_1+...+d_t`, `q_t=2^(-D_t)`.

Then `f_t` equals `g` exactly when all accumulated controls are active. Direct Fourier expansion gives

`W_1(f_t)=q_t^2 W_1(g)+4D_t q_t^2 r^2`,

`L_1(f_t)=q_t^2 L_1(g)+2D_t q_t^2 W_1(g)+4D_t q_t^2 r^2 log_2(1/(4q_t^2r^2))`.

The local singleton charges generated across every layer therefore enter the root estimate as

`C_m=sum_t (q_m/q_{t-1})[W_1(f_{t-1})+L_1(f_{t-1})]`.

Because the cumulative depths are distinct integers,

`sum 2^(-D_s)<=2`, `sum D_s2^(-D_s)<=2`, `sum D_s^2 2^(-D_s)<=6`.

Consequently

`C_m <= 2q_mL_1(g)+6q_mW_1(g)+(28+8/(e ln2))I_ctl(f_m)`.

The weighted local control influences telescope exactly to the physical root control influence. The resulting theorem is

`G(f_m) <= q_mG(g)+640q_mL_1(g)+1920q_mW_1(g)+C_chain I_ctl(f_m)`,

where

`C_chain=C_*+320(28+8/(e ln2)) < 10324`.

This constant is independent of depth, every activation probability, terminal bias, and dimension. The proof is in `NESTED_ACTIVATION_LEDGER.tex`.

## 4. New restriction-closed class

Suppose a restriction-closed terminal class `B` obeys both

`G(g)<=A I(g)` and `H(g)<=C I(g)`.

Since `W_1<=I` and `L_1<=H`, every finite nested fresh-activation chain over `B` obeys

`G(f)<=K I(f)`, `K=max{A+640C+1920,C_chain}`.

The enlarged class is restriction closed: a control restriction kills or shortens an activation block, and a data restriction acts on the terminal core. Restriction induction gives

`U(f)<=K I(f)` and `H(f)<=(2+2K)I(f)`.

For signed-parity terminals, this yields the explicit all-depth FEI constant

`H(f)<20650 I(f)`.

This is a strict extension of the earlier one-layer parity-activation endpoint. It covers arbitrary depth and arbitrary fresh block sizes without a growing constant.

## 5. Verification and mandatory controls

`CHECK.py` recomputes Walsh spectra, upper-set masses, every restriction value in `G`, and the singleton ledger directly. The command

`python CHECK.py`

passes:

- 1,434 one-layer tests and 2,664 hierarchy tests;
- exhaustive Boolean cores through three variables;
- majority, sparse one-point defect, whole-set addressing, near tensor, shared-variable overlap, an exact-one three-bit prime control, parity, and 12 seeded random five-bit cores;
- exact `W_1` formulas and 70-digit `L_1` agreement;
- the local retained-credit inequality, the all-depth theorem, and the geometric ledger bound.

The finite checks are falsifiers and normalization checks only. The all-parameter conclusion is analytic.

## 6. Movement and remaining universal gap

**PROVED (author, pending review):** The first-level logarithmic mismatch exposed by the previous majority obstruction can be retained and charged only once along every hierarchy of nested fresh one-word activations with a fixed terminal core.

**PROVED (author, pending review):** Nested fresh activations over any terminal restriction-closed class with fixed FEI and `G/I` constants inherit dimension-, depth-, bias-, and rarity-independent constants. In particular, arbitrary-depth nested activations of signed parities satisfy FEI with constant below 20,650.

**NOT PROVED:** General restriction trees can change coherent cores from node to node. Their singleton-log credits do not all descend from one terminal spectrum, so this ledger does not prove universal GU' or full FEI.

**Exact remaining obstruction:** prove a nonreused global credit for changing coherent cores across arbitrary Boolean hierarchies, or construct a genuine Boolean family refuting such a credit. The mandatory majority, rare-defect, addressing, near-tensor, overlap, parity, and prime-gate controls do not falsify the fixed-core theorem.

Full FEI remains **OPEN**.

## 7. Source and execution record

- Source head at research: `862bef2a2f671ed8ed3b8e71054614f074865763`.
- Owner order blob: `81b6d6f988aee4489512c6e62543253900620453`.
- Case-target overlay blob: `97e41262ebb4f09eec53630a918acae09efc9a48`.
- Current-status blob: `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- B01 compact-contract blob: `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- Previous majority no-go: canonical commit `8e917b7f2190d0d624de3469053f5cda4625978f`, report blob `d47fd0740c103128fe1c2a7a80bab5b49b56303d`, proof blob `0d53cfb8dbb41786ea281065b4f72271059a9da9`.
- Previous exact activation transfer: canonical commit `8344aa4aa688790494e3ebd46bb94b13f659ce18`, proof blob `fd291e847f0f7a21591398af6b415fa00787cd17`.
- Literature/priority claim: none. This is a source-bound internal strengthening, not a novelty claim.
- Configuration: natural execution; no worker launched; no protected source read; no paid compute; no scheduler or shared-index mutation.
- Exposed model: Codex on GPT-5 as identified by the runtime instructions; reasoning-effort setting not exposed.
- Independent review: not performed here; route to A086 and A094.
- Native Brain ingestion: not claimed.
