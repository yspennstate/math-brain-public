# B05 / A023 — retained-U payment for fully overlapping bent surgery

**Run:** `20261012T053720Z-fleet01-B05-bent-overlap-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gaps:** `B05_RARE_REFUNDS` / `OVERLAP_PRODUCT` / `G-UPPER-SET-ASYMMETRY`  
**Status:** a new all-parameter shared-variable class theorem is author-proved, pending A087/A094 review. Full FEI remains **OPEN**.

## 1. Frozen objective and accepted baseline

The immediately preceding B05 theorem was independently accepted by A094 at its declared scope: every finite fresh selector tree with disjoint complete sibling variable sets satisfies

`U(F_root)-sum_leaf w_leaf U(g_leaf) <= C_sep I_sel(F_root)`, `C_sep<16.964`.

The review identified the first unpaid line exactly: shared-variable upper-mass overlap. This run does not redo the accepted separated proof. It freezes one fully overlapping, unbounded test class required by the B05 contract:

- `g` is any bent Boolean function on even `k>=8` data bits;
- `h` is obtained by flipping `g` at one input point;
- a fresh `d`-bit selector chooses `h` at one word and `g` elsewhere;
- `k` and `d` are arbitrary.

The two children use the same physical variables and have coincident full Fourier support. The objective is to retain both child `U` packets exactly once and pay the complete selector charge by physical selector influence with a constant independent of `k` and `d`.

## 2. Exact shared-variable identity

For arbitrary Boolean children `g,h` on the same variables, write

`a_T=hat g(T)`, `b_T=hat h(T)`, `d_T=b_T-a_T`,

and upper masses

`A_T=sum_{R superset T}a_R^2`, `B_T=sum_{R superset T}b_R^2`, `D_T=sum_{R superset T}d_R^2`.

For activation probability `p=2^-d` and `c_T=(1-p)a_T+p b_T`, direct Walsh summation proves

`U(F) = sum_T c_T^2 log_2(((1-p)A_T+pB_T)/c_T^2)`

`       +p(1-p) sum_T d_T^2 log_2(D_T/d_T^2)`

`       +(pd/2-p^2d) sum_T d_T^2`.

This formula is exact and uses no disjointness or orthogonality. It follows because the control-empty coefficient is `c_T`, every nonempty control coefficient has magnitude `p|d_T|`, and the corresponding upper masses are `(1-p)A_T+pB_T` and `p 2^(-|Q|)D_T`.

This exact identity is reusable beyond the theorem below; it isolates the shared-spectrum overlap in the ratios `B_T/A_T` rather than treating coherent coefficients as a disjoint mixture.

## 3. PROVED: bent one-point overlap payment

Let `g` be any bent sign on even `k>=8` bits and let `h` be its one-point flip. For every selector depth `d>=1`, with `p=2^-d`,

`J := U(F)-(1-p)U(g)-pU(h) <= 71 I_ctl(F)`.

Here the disagreement probability is `delta=2^-k` and

`I_ctl(F)=2pd delta`.

The constant 71 is independent of dimension, rarity, the bent phase pattern, and the flipped point.

### Why the rare logarithm cancels

Bentness gives flat coefficients `a_T=alpha s_T`, where `alpha=2^(-k/2)` and `s_T` is a sign. A one-point flip changes every coefficient by the same magnitude `2 delta`, with `delta=alpha^2`.

After factoring the flat upper masses, define relative perturbations `u_T,v_T,w_T` for the child cap, flipped atom, and coherent empty-control atom. For `k>=8`,

`|u_T|,|v_T| <= (17/4)alpha`, `|w_T| <= (33/8)p alpha`.

All terms containing the long cap logarithm `k-|T|` cancel atom by atom between the coherent packet, difference packet, and retained children. The remainder is a scalar function

`Phi_p(u,v,w)=(1+w)ln((1+pu)/(1+w))-p(1+v)ln((1+u)/(1+v))`.

Its linear term is exactly `pv-w=4p(1-p)delta`, and a uniform Hessian bound gives `Phi_p<97p delta`. Summing all `2^k=1/delta` atoms and restoring bits yields

`J <= 140p delta + I_ctl <= 71 I_ctl`.

The complete derivation is in `BENT_OVERLAP_PAYMENT.tex`.

## 4. Verification and mandatory controls

Command:

`python CHECK.py`

The deterministic checker performed:

- 24 direct truth-table Walsh comparisons against the exact shared-node formula, with maximum error `1.0e-74`;
- 48 theorem cases across `k=8,10,12`, affine bent variants, distinct flip points, and `d=1,2,4,8`;
- exact rational checks of every perturbation range used in the proof;
- 1,312 exhaustive small Boolean one-point-surgery controls;
- majority, point-defect, addressing, and near-tensor controls.

It passed 345,464 assertions with zero failures and no randomness. The largest theorem-case ratio observed was `J/I_ctl=4.861279949438929`, far below the deliberately coarse analytic constant 71. The computation corroborates normalization and endpoints; the theorem is analytic for every even `k>=8` and every `d>=1`.

## 5. Movement and exact limitations

**PROVED, pending independent review:** the separated-child hypothesis can be removed for an unbounded family with maximal physical and spectral overlap. The complete rare logarithm cancels after retaining child packets; it is not charged pointwise.

**Class extension:** unlike the accepted separated hierarchy, both children here share all data variables and every Fourier atom. Unlike the already known neighboring-orthogonality endpoint, this class has coincident supports. The theorem therefore covers a genuinely new overlap regime.

**Not proved:** one node is not an arbitrary shared-variable hierarchy. Repeated point surgeries can change the cap ratios coherently, and this proof does not show that their quadratic remainders have single-use ownership across descendants. It also does not bound arbitrary shared Boolean children.

**Not a full-FEI result:** the theorem supplies neither universal `U<=KI` nor unbounded `H/I`. Full FEI remains OPEN.

## 6. Physical credit ledger and next action

The stopping rule reveals the fresh selector controls, stopping at the first inactive bit or reaching the active word. It is physical, adaptive, finite, and spends each selector coordinate once. The terminal packets `(1-p)U(g)` and `pU(h)` are retained exactly once.

The next exact action is a two-surgery chain: start from a bent seed, flip two input points with controllable Hamming relation, derive the interaction term in the cap ratios, and determine whether the Hessian payment decomposes into two owned selector credits or develops a cross-surgery debt. Adjacent-point and near-tensor surgeries are mandatory falsifiers. Success would be the first step toward a shared-variable hierarchy; failure should produce a parameterized Boolean obstruction, not a finite seed.

## 7. Sources and execution record

- Owner order blob: `81b6d6f988aee4489512c6e62543253900620453`.
- Case-target overlay blob: `97e41262ebb4f09eec53630a918acae09efc9a48`.
- Current-status blob: `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- B05 compact contract blob: `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Stream index blob: `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Obstruction registry blob: `e111933338dff1d7798c5e59b43700bbf30f7b96`.
- Accepted separated theorem: B05 final commit `72824efa4229ee109fc344f1a021840982509ee5`, report blob `6f7ae1410866fe2a9c31d00e0e72479f6098f139`, proof blob `c5d1d75e98b98ede3de3e16498c5353e45f9afd2`.
- Independent A094 acceptance: report blob `cdccc705dde0594893643257f3514132a274fabf`; reviewer made no repair.
- Configuration: natural execution, no worker launched, no protected source read, no paid compute, no scheduler or graph mutation.
- Exposed model: GPT-5 Codex as identified by runtime instructions; reasoning-effort setting was not exposed.
- Literature novelty claim: none. This is a campaign-internal source-bound theorem.
- Independent review of this theorem: not yet performed; route to A087/A094.
- Native Brain ingestion: not claimed; repository mirror only.
