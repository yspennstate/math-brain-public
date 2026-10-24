# POS3 B19 r11 — stationary chain-profile polynomial recurrence

**Outcome:** `ESSENTIAL_STEP_APPLIED`.

**Parent target:** POS3 remains **OPEN / NOT PROVED**.

**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## Assignment addressed

Delete a chain `C={c_1<...<c_m}` and keep the induced projection law exactly by its true lift multiplicities.  The goal here is to make repeated insertion on one fixed chain-profile block algebraic, so that recycling in the current width-three induction cannot be hidden inside an uncontrolled biased law.

## Exact dependencies consumed

1. **Assigned partner account02/B10 r11**, source-bound shared handoff commit `71ac0398a831011ab9dbc8674522717915477f9d`, handoff blob `6971479872d6c25633d3e4beee71d9c3a7b925cd`.  Its four-channel transposition export proves that every strong incomparable pair either span-descends or exports through one of at most four Hasse-witness channels, with a selected channel carrying more than `E/12` full-extension marks.  At the lead coherent gate the third antichain vertex cannot be that Hasse witness, so the gate must genuinely exit to a new vertex, span-descend, or balance.

2. **Campaign lead account04/B10 r18**, source-bound handoff commit `9b3a2dc6963599facd641957473f2d2e60f9ae95`, handoff blob `a7a4140642f4074c8888c055219cb6462bcbcc6b`.  It recodes every surviving four-channel export as a heavy cover bridge and proves the two-step ray-switch normal form: after span descent is excluded, a locally neutral ray switch is a literal exact backtrack.  Its first unpaid implication is global recycling through strict envelope expansions and non-exact/multi-distinguisher exact-backtrack bridges.

These results are used below rather than merely cited: the new recurrence gives a finite algebraic budget for any part of that recycling which remains in one stationary chain-profile environment.

## 1. Exact chain-deletion state representation

For `q in Q=P\C`, define the chain-prefix interval

`I(q)=[lambda(q),rho(q)] subset {0,...,m}`,

where `z in I(q)` means that exactly `z` members of `C` may precede `q` in a lift.  For a fixed linear extension

`tau=(q_1,...,q_n) in L(Q)`, full lifts of `tau` are in bijection with weakly increasing state sequences

`z_1<=...<=z_n`, `z_i in I(q_i)`.

Thus every fiber multiplicity is counted exactly; no projected law is replaced by the uniform law on `L(Q)`.

If the current state-count vector is `f=(f_0,...,f_m)` and the next projected element has profile interval `J`, its exact transfer operator is

`(T_J f)(r) = 1_{r in J} sum_{s<=r} f(s)`.

This is simply the prefix-sum recurrence for weakly increasing insertion states.

## 2. Stationary-profile power theorem

Fix one interval

`J=[alpha,beta]`, `h=beta-alpha`.

After one application of `T_J`, the state vector is supported on `J`.  Restricting to the coordinates `alpha,...,beta`, every *further* insertion with the same profile acts by the `(h+1)x(h+1)` matrix

`S_{r,s}=1_{s<=r}`.

### Theorem 2.1 (exact powers)

For every integer `k>=0`, after indexing `r,s` by `0,...,h`,

`(S^k)_{r,s}=0` for `r<s`, and

`(S^k)_{r,s}=binom(k+r-s-1,r-s)` for `r>=s`,

with the `k=0` interpretation giving the identity matrix.

### Proof

For `k=1` the statement is the definition of `S`.  If it holds for `k`, then for `r>=s`

`(S^{k+1})_{r,s}=sum_{t=s}^r (S^k)_{t,s}`

`=sum_{d=0}^{r-s} binom(k+d-1,d)`

`=binom(k+r-s,r-s)`

by the hockey-stick identity.  The entries above the diagonal remain zero.  The case `k=0` is the identity.  QED.

## 3. Exact finite-difference recurrence

Let `g` be any state-count vector entering a stationary `J` block after the first restriction to `J`.  Let `ell` be any fixed downstream linear completion functional.  This includes total full-extension count, a fixed pair-order numerator, or the difference of the two adjacent-swap fiber counts, provided the marked observable and downstream environment are fixed while the stationary block length varies.

Define

`D(k)=ell^T S^k g`.

### Theorem 3.1 (stationary-profile polynomiality)

`D(k)` is a polynomial in `k` of degree at most `h`.  Equivalently,

`Delta^{h+1} D(k)=0`

for every `k>=0`, i.e.

`sum_{j=0}^{h+1} (-1)^{h+1-j} binom(h+1,j) D(k+j)=0`.

### Proof

By Theorem 2.1 every matrix entry of `S^k` is a binomial polynomial

`binom(k+d-1,d)`

of degree `d<=h`.  Taking the fixed bilinear combination `ell^T S^k g` preserves degree at most `h`.  A polynomial of degree at most `h` has vanishing `(h+1)`-st forward difference.  QED.

### Corollary 3.2 (finite orientation-return budget)

If `D` is not identically zero, its sign can change at most `h` times along a stationary profile block.  Indeed every strict sign change between consecutive integer values gives a distinct real zero of the degree-`<=h` polynomial.

This is the correct replacement for the false stronger statement that a repeated profile must be temporally monotone.

### Corollary 3.3 (fixed threshold budget)

Suppose `N(k)` is a fixed pair-order numerator and `E(k)>0` the total full-extension count under the same stationary profile hypotheses.  Both are degree-`<=h` polynomials.  For any fixed rational threshold `theta`,

`H_theta(k)=N(k)-theta E(k)`

also has degree at most `h`.  Unless `H_theta` vanishes identically, the probability `N(k)/E(k)` can cross the level `theta` at most `h` times inside the stationary block.

In particular the balance thresholds `1/3` and `2/3` each have a finite exact crossing budget controlled solely by the chain-profile width `h`.

## 4. Sharp width-three regression from the previous endpoint-freshness counterexample

Use the explicit width-three family with deleted chain `C:c_1<c_2<c_3`, fixed chain

`D:p_1<p_2<p_3<u<s_2`,

and

`E_k:j_1<...<j_k<v<s_1<s_3`,

where every `j_i` has the same chain profile `[0,1]`, while

`I(p_1)=[0,1]`, `I(p_2)=I(p_3)=[0,2]`, `I(u)=[1,2]`,

`I(v)=I(s_1)=I(s_3)=[0,3]`, `I(s_2)=[2,3]`.

For the fixed projected skeleton with adjacent `u,v`, let `D(k)` be the exact difference between the `uv` and `vu` lift multiplicities.  Exact DP gives

`D(0)=2`, `D(1)=-1`, `D(2)=1`, `D(3)=3`, `D(4)=5`, ..., `D(8)=13`.

The `k=0 -> 1` step is the initial restriction to `J=[0,1]`, so it is *outside* the stationary recurrence.  Once one `J` vertex has appeared, `h=1` and

`D(k)=2k-3` for every checked `k>=1`.

Hence there is exactly one post-introduction sign change, attaining the theorem's width-one bound.  This explains the earlier `+ -> - -> +` phenomenon without resurrecting endpoint freshness: the first change is the nonstationary entry into the profile, while subsequent evolution is degree one.

## 5. Direct application to the current team route

The assigned partner account02/B10 r11 exports every surviving strong pair to a concrete Hasse-witness channel carrying `>E/12` marks.  The campaign lead account04/B10 r18 then shows that, after span descent is excluded, a locally neutral two-step ray switch is a literal exact backtrack through a heavy cover bridge.

Whenever a sequence of such backtrack tests stays inside one fixed chain-profile block `J` and has the same downstream marked functional, its exact defect and every fixed `1/3` or `2/3` threshold test obey the order-`h+1` finite-difference recurrence above.  Therefore that portion of the recycling cannot create arbitrarily many new orientation or balance-threshold reversals.  Any continuation past the finite profile-width budget must leave at least one of the stationary hypotheses.

This is a genuine reduction of the lead's global recycling residual: indefinite recycling cannot be hidden in repeated use of one unchanged interval profile and one unchanged marked completion functional.

## 6. Compact conditional end-to-end route

Assume the following exit lemma.

**`POS3-COHERENT-STATIONARY-RAY-EXIT-CHARGE`:** At the first exit from a maximal stationary-profile backtrack block, either

- a previously unused full-extension marked packet from the partner's Hasse-channel export is charged injectively;
- the strong-majority span strictly descends;
- a balanced pair or proper autonomous/ordinal reduction appears; or
- a monotone global profile/environment potential changes in a direction which can occur only finitely often.

Then a minimal POS3 counterexample cannot exist.  Indeed, partner r11 gives a marked outward channel; lead r18 puts every surviving neutral ray switch into exact-backtrack normal form; Theorem 3.1 gives a finite return/threshold-crossing budget inside each maximal stationary block; and the exit lemma gives finite charge or strict structural descent at every block transition.  A finite poset and finite extension set cannot support infinitely many fresh charges or strict descents.  The process must terminate at balance or a forbidden reduction, contradiction.

## 7. First essential missing implication

The first unpaid step is precisely the **stationary-block exit**, not another local recurrence:

`POS3-COHERENT-STATIONARY-RAY-EXIT-CHARGE`.

The theorem above shows that fresh profile endpoints are *not* required at every return, but also that unchanged profile dynamics have only a finite algebraic crossing budget.  What remains is to show that when the profile or downstream functional changes, the change is chargeable to genuinely new Hasse/full-extension mass or to a strict finite structural potential.  This is narrower than the prior endpoint-freshness proposal and is compatible with the lead's r18 cross-envelope exact-backtrack residual.

## Verification

The standard-library verifier `verify_stationary_profile.py` checks:

- 1,260 exact matrix-entry identities for `S^k`;
- 48 independent finite-difference instances through profile width five;
- the exact width-three multiplicity sequence above through `k=8`;
- `D(k)=2k-3` for every checked `k>=1`.

Terminal line: `POS3_STATIONARY_PROFILE_POLYNOMIAL_CHECK_PASS`.

The computation is regression support only; the arbitrary-size statements are proved above.

## Scope / provenance

No brain installation or benchmark work was performed.  No benchmark gold, credentials, scheduler identifiers, machine paths, email, Drive, public posting, paid/remote compute, Codex, remote workflow, permission change, or production mutation was used.  The parent conjecture is not claimed solved.
