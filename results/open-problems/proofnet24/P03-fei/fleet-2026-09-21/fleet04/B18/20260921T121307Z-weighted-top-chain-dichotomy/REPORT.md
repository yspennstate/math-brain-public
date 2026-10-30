# B18 FEI proof integration — weighted top-chain defect dichotomy

**Date:** 21 September 2026  
**Role:** fleet04/B18, FEI proof integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED universal finite-degree bridge. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Priority:** UNVERIFIED. No novelty claim is made.

## 0. Fresh source-exact frontier

This run used fresh `math-open-problems` master after the 21 September owner continuation. The compatible proof inputs are:

1. fleet03/B18, `20260921T120954Z-top-degree-parity-endpoint/REPORT.md`, blob `466cb3e97c438bce515f9d87958656767236f30e`: for a Boolean function of Fourier degree `d`, every nonzero degree-`d` coefficient is an integer multiple of `2^(1-d)`, hence has magnitude at least `2^(1-d)`; this eliminates the exact uniform-activity scalar endpoint but leaves a weighted-stability gap;
2. fleet04/B14, `2026-09-21T111505Z-js-strong-concavity-selector/REPORT.md`, blob `6e88e3464112a642fb6707f2f22f1eec3779543b`: the singleton recombination profile has the strong-concavity rebate
   `JS_i <= j(M_i) - (c_*/3) V_i`, with `c_*=2/ln 2`, and the critical-core route needs a mass-weighted existential rebate rather than exact endpoint nonattainment;
3. fleet01/B18, `20260921T111435Z-erasure-exit-dual/REPORT.md`, blob `eb51df70d0e43e8255ebee6dc904da4f2e5d8389`: a maximal-ratio restriction core must remain inside the all-scale erasure/Bayes tube, so any useful scalar defect must carry actual spectral mass;
4. fleet02/B18, `20260921T103159Z-product-phase-kl-stability/REPORT.md`, blob `ca55417b041fac6d21619a4217c6ee866a1eff34`: Hellinger-scale endpoint rigidity alone is insufficient; a universal proof ultimately needs a KL/mass-scale payment or another resource such as signed orientation/transport.

The next missing implication identified by the newest endpoint work was: **turn the top-degree parity obstruction into a weighted defect that cannot have literally zero mass.** The result below does this quantitatively, but the resulting floor is exponential in the degree, so it does not close FEI.

## 1. Fibre notation

Let

`f:{-1,1}^n -> {-1,1}`

be nonconstant Boolean, with Fourier degree `d>=1`. Write

`p_S = hat f(S)^2`.

For an oriented cube edge `T -> T union {i}`, `i notin T`, put

`w_i(T) = p_T + p_{T union {i}}`,

and whenever `w_i(T)>0`,

`q_i(T) = p_{T union {i}} / w_i(T)`.

Thus the oriented Fourier-amplitude ratio across the edge is

`sqrt(p_{T union {i}}/p_T) = sqrt(q_i(T)/(1-q_i(T)))`

when both masses are positive.

Define the degree-dependent threshold

`rho_d = 2^(-1+1/d)`,

`q_d = rho_d^2/(1+rho_d^2) = 1/(1+2^(2-2/d))`.

For every finite `d>=2`,

`q_d > 1/5`,

and `q_d` decreases to `1/5` as `d -> infinity`. More precisely,

`q_d = 1/5 + (8 ln 2)/(25 d) + O(d^-2)`.

The threshold `1/5` is therefore not an arbitrary numerical choice: it is the limiting posterior corresponding to an amplitude ratio `1/2`, exactly the parity barrier exposed by the top-degree theorem.

## 2. PROVED: one top chain carries a quantitative bad edge

### Theorem 2.1 — weighted top-chain defect

For every nonconstant Boolean function of Fourier degree `d`, there exists an oriented edge `T -> T union {i}` such that

`q_i(T) >= q_d`

and simultaneously

`p_{T union {i}} >= 4^(1-d)`.

Consequently

`sum_{i,T: q_i(T)>=q_d} p_{T union {i}} >= 4^(1-d)`.

### Proof

Choose a top-degree label `S` with `|S|=d` and `hat f(S) != 0`. By the inherited top-degree parity theorem,

`|hat f(S)| >= 2^(1-d)`,

hence

`p_S >= 4^(1-d)`.                                                     (2.1)

Fix any ordering `S={i_1,...,i_d}` and the resulting maximal chain

`S_0=empty subset S_1 subset ... subset S_d=S`,

where `S_k={i_1,...,i_k}`. Put `a_k=|hat f(S_k)|`.

Suppose first that every defined edge on this chain had `q<q_d`. Whenever the lower mass is positive this gives

`a_k/a_(k-1) < sqrt(q_d/(1-q_d)) = rho_d`.

If some lower mass were zero and the next upper mass positive, that edge would instead have `q=1`, already contradicting `q<q_d`; an interval of two consecutive zero masses cannot lead to the nonzero terminal mass without such a zero-to-positive edge. Therefore the all-low assumption forces

`a_d < a_0 rho_d^d <= rho_d^d = 2^(1-d)`,

contradicting top-degree granularity. Hence at least one chain edge has `q>=q_d`.

Take the **last** such edge and let its upper label be `S_k`. Every later chain edge has `q<q_d`, hence squared amplitude ratio

`p_{S_j}/p_{S_(j-1)} < rho_d^2 < 1`

for `j>k` (there can be no later zero-to-positive jump, because that would have `q=1>=q_d`). Thus mass decreases after the selected edge and

`p_{S_k} >= p_{S_d}=p_S >= 4^(1-d)`

by (2.1). This selected edge proves both assertions. QED.

### What this improves

The preceding endpoint report proved only that some endpoint-like top chain must contain a posterior at least `1/5`, while warning that its mass might be exponentially small. Theorem 2.1 supplies the missing explicit weight: **the defect can indeed be exponentially small, but not smaller than `4^(1-d)` on at least one offending upper atom.**

This is not dimension-independent. It is, however, an actual weighted statement rather than exact nonattainment.

## 3. PROVED: scalar-rebate versus upward-orientation dichotomy

The strong-concavity route uses the unoriented fibre parameter

`s_i(T)=min(q_i(T),1-q_i(T)) in [0,1/2]`.

A large oriented posterior can evade a scalar deviation only by reversing orientation, `q>1/2`. This yields a clean two-resource dichotomy.

Fix any target endpoint parameter `tau<q_d`. Define

`U(f) = sum_{i,T: q_i(T)>1/2} p_{T union {i}}`

(the total upper mass on upward-oriented edges), and

`E_tau(f) = sum_{i,T: q_d<=q_i(T)<=1/2} w_i(T) (q_i(T)-tau)^2`.

### Theorem 3.1 — weighted scalar-or-orientation dichotomy

At least one of the following holds:

1. **upward-orientation resource**

   `U(f) >= 4^(1-d)`;                                                     (3.1)

2. **scalar endpoint-deviation resource**

   `E_tau(f) >= 2 * 4^(1-d) * (q_d-tau)^2`.                              (3.2)

### Proof

Take the edge furnished by Theorem 2.1. Its upper mass is at least `4^(1-d)` and its posterior is at least `q_d`.

If its posterior exceeds `1/2`, its own upper mass contributes to `U`, giving (3.1).

Otherwise `q_d<=q<=1/2`, so on this edge `s=q`, and

`w = p_upper/q >= 2 p_upper`.

Its single contribution to `E_tau` is therefore at least

`2 p_upper (q_d-tau)^2 >= 2 * 4^(1-d) (q_d-tau)^2`,

which is (3.2). QED.

This is the useful integration point. A top-degree parity defect cannot disappear into an unweighted statement. It must appear either as:

- genuine mass on an edge whose Fourier weight grows upward, which is a natural input for the signed-overlap / transport / collision routes; or
- a definite weighted displacement from the scalar endpoint on a down-oriented fibre, which is exactly the type of resource the B14 strong-concavity calculation can rebate.

## 4. PROVED corollary in the B14 `(M_i,V_i)` variables

For coordinate `i`, B14 defines

`M_i = sum_T w_i(T) s_i(T)`,

`V_i = sum_T w_i(T) (s_i(T)-M_i)^2`.

Suppose the scalar branch (3.2) occurs. For its selected coordinate `i`, define the full endpoint-deviation energy

`D_i(tau) = sum_T w_i(T) (s_i(T)-tau)^2`.

Since the selected down-oriented edge has `s=q`,

`D_i(tau) >= 2 * 4^(1-d) (q_d-tau)^2`.                                  (4.1)

But exactly

`D_i(tau) = V_i + (M_i-tau)^2`.                                          (4.2)

Hence at least one of

`V_i >= 4^(1-d) (q_d-tau)^2`,                                           (4.3)

or

`|M_i-tau| >= 2^(1-d) (q_d-tau)`                                        (4.4)

must hold.

In the variance subcase, the already-proved B14 strong-concavity theorem immediately yields the explicit finite-degree recombination rebate

`JS_i <= j(M_i) - (c_*/3) 4^(1-d) (q_d-tau)^2`,                         (4.5)

where `c_*=2/ln2`.

The mean-displacement subcase (4.4) must instead be fed into the scalar supporting-line gap around the critical endpoint. No claim is made here that (4.4) alone gives a dimension-independent payment; its scale is again exponential in `d`.

Thus, after top-degree parity, a hypothetical endpoint-like critical core has only three possibilities at finite degree:

- upward-oriented mass at least `4^(1-d)`;
- a variance rebate of order `4^(1-d)`;
- a scalar mean displacement of order `2^(1-d)`.

Exact endpoint equality is no longer one of the possibilities.

## 5. Decisive numerical calibration

The attached `calibrate_weighted_top_chain.py` evaluates the analytic floor for representative degrees. It is a calibration, not a proof.

Using the inherited illustrative endpoint value

`tau = 0.1740316570325050`

(the value quoted by fleet03 for its current hard-ratio calibration, not needed for the theorem), the down-branch energy floor is

`2 * 4^(1-d) * (q_d-tau)^2`.

Selected values are:

- `d=2`: `q_d=1/3`, mass floor `1/4`, energy floor `1.2688512e-2`;
- `d=5`: `q_d=0.2480507469`, mass floor `3.90625e-3`, energy floor `4.28033e-5`;
- `d=15`: `q_d=0.2151976935`, mass floor `3.72529e-9`, energy floor `1.26261e-11`;
- `d=20`: `q_d=0.2113212411`, mass floor `3.63798e-12`, energy floor `1.01173e-14`.

The calculation makes the obstruction precise: the parity bridge is quantitatively real but loses exponentially with Fourier degree. A universal FEI proof cannot stop here.

As an additional non-proof sanity check during this run, the chain theorem was tested against all `65,812` Boolean truth tables through `n=4`; no violation occurred. The analytic proof above does not depend on that enumeration.

## 6. Integration with the current universal proof attempt

This run does **not** prove the weighted target proposed in the fleet03 endpoint report,

`sum_{i,T:q_i(T)>=1/5} p_{T union {i}} >= c I(f)`

with a dimension-independent `c>0`. It proves only the absolute degree-dependent floor `4^(1-d)`.

That distinction is decisive. The new result advances the proof state in two ways:

1. it closes the logical gap between “exact endpoint impossible” and “some positive amount of endpoint defect is carried by actual spectral mass” at each finite degree;
2. it isolates the precise remaining amplification problem: convert the exponential seed furnished by top-degree parity into a payment proportional to influence, either by propagating the defect down many chains or by charging upward-oriented mass through signed transport / collisions.

The fleet01 erasure-tube theorem says a maximal-ratio counterexample must satisfy a simultaneous all-scale Bayes constraint. The fleet02 product-phase theorem says a bounded Hellinger separation cannot by itself pay a KL-scale rare-coordinate defect. Theorem 3.1 is compatible with both warnings: it supplies a **seed mass**, not yet a universal-scale bank.

A promising next implication is therefore one of the following two genuinely new statements:

- **propagation:** in a restriction-critical hard core, one bad top-chain edge forces `Omega(I)` total bad-edge mass by repeated two-face / block compatibility; or
- **orientation payment:** if upward-oriented mass is not negligible, the signed all-shift convolution identities force a transport/collision rebate of comparable size, after which the remaining down-oriented system can use B14 strong concavity.

Either would upgrade the exponential seed to a dimension-free selector. Neither is proved here.

## 7. Claim ledger

### PROVED

- Degree-dependent posterior threshold `q_d=1/(1+2^(2-2/d))>1/5`.
- Every nonconstant degree-`d` Boolean function has an edge with `q>=q_d` and upper spectral mass at least `4^(1-d)`.
- Therefore total high-posterior upper mass is at least `4^(1-d)`.
- For every `tau<q_d`, either upward-oriented upper mass is at least `4^(1-d)`, or down-oriented endpoint-deviation energy is at least `2*4^(1-d)(q_d-tau)^2`.
- In the down branch, for some coordinate either `V_i>=4^(1-d)(q_d-tau)^2` or `|M_i-tau|>=2^(1-d)(q_d-tau)`; the variance alternative gives the explicit B14 strong-concavity rebate (4.5).

### CONDITIONAL / inherited dependencies

- The top coefficient lower bound `|hat f(S)|>=2^(1-d)` is inherited from fleet03/B18's proved top-degree parity theorem.
- The conversion from a variance lower bound to (4.5) uses fleet04/B14's proved strong-concavity theorem.
- Applying `tau=tau(r)` to a maximal-ratio critical core uses the current scalar-frontier reduction and its endpoint parameter; this run does not re-audit that dependency because the owner requested creative FEI work rather than audits.

### OPEN

- Amplify the `4^(1-d)` seed to a dimension-independent fraction of influence, or replace it by a block-level payment that is dimension-independent.
- Charge the upward-orientation branch universally through signed transport/collision structure.
- Close the all-scale erasure-tube / KL-scale Booleanity gap.
- Full uniform-cube Fourier entropy-influence.

### REFUTED / NOT CLAIMED

- Exact endpoint nonattainment is **not** by itself a dimension-independent rebate.
- The new exponential seed is **not** a proof of `Omega(I)` weighted stability.
- Finite truth-table checks are **not** universal evidence.
- No publication priority or full FEI proof is claimed.

**Brain status:** `WITHOUT_VERIFIED_BRAIN`.
