# B01 / A001 quantifier audit and critical-prime reduction

## Status

**Artifact target:** complete pending independent review.  
**Mathematical target:** full FEI remains **OPEN**.  
**New claim scope:** two exact reductions, author-proved and pending A086/A094 review. Neither is a full FEI proof.

## 1. Bounded objective and prior status

The selected primary packet is A001 (Quantifier audit). The objective was to finish the source-pinned all-dimensions inventory after A002--A005 supplied the missing transformation, endpoint, and constant ledgers; then locate the first unsupported universal statement without importing FEI circularly.

Before this run:

- A003 had proved `C_FEI<=C_step<=C_FEI+2/ln2`, `C_L<=C_FEI<=C_L+3/ln2`, and a one-way posterior-forest sufficient condition.
- A002/A005 had shown that full support, rare output, low total influence, diffuse coordinate influences, and several selector/cyclic endpoints can still contain an arbitrary Boolean seed, while STEP criticality is not preserved by the activation controls.
- A004 had proved the fixed-coordinate `1/ln2`, `2/ln2`, and `3/ln2` bridge losses sharp on genuine bent one-point-defect selectors. The existential coordinate question remained open.
- The current status had isolated positive local deficit surplus for every coordinate of a minimum-dimensional counterexample, but no all-function reduction to the simultaneous critical and tensor-prime class had been written in the A001 deliverable.

## 2. Exact target, units and sources

For every finite `n` and Boolean sign `f:{-1,1}^n->{-1,1}` under the uniform law,

`H(f)=sum_S fhat(S)^2 log_2(1/fhat(S)^2)` and `I(f)=sum_S |S|fhat(S)^2`.

Full FEI asks for one finite `C`, independent of `n,f`, with `H(f)<=CI(f)`. Constants satisfy `H=I=0`; ratios are formed only for nonconstant functions.

Sources actually read and used:

1. Owner-approved public paper: `yspennstate/fourier-entropy-threshold-functions`, commit `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, `paper/main.tex`, blob `1a9af8c62a32566a6ad1b7323a84d103a8375e93`. In particular, its variational joint-witness bound, addressing calculation, scope paragraph, and product-biased threshold theorem.
2. Recovered reductions source: `reports/fei-2026-10-11/source_material/reductions/paper/forests.tex`, blob `3fd08d81a2bcd96acaaa268757c7f343e71e8249`.
3. A003 complete endpoint packet: commit `87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`, report blob `85308728bbfffe5cd3afd554cae783110fc57035`.
4. A002 hardness transformations: commit `e42cfede006893c5237743b6261ceba2784c9655`, report blob `4515ec2e17411aca8644bc1789796633d9dcc20f`.
5. A005 endpoint admission: commit `69fdc6d41576bc4921ba44a8acce696103bf6a81`, report blob `a32f008d392e999167eef98e4656dea03ad643fc`.
6. A004 constant/unit audit: commit `34a52995051072ea8e4768734a6a61b7e760ad83`, report blob `c8418de4065be156d6196ae92881804434d2029a`.
7. B07 fixed-cyclic source: `runs/B07/20261011T213754Z-account01-B07-a034-fiber-phase/PHASE_SCOPE.md`, blob `b9fe5f9cb171420581997c20819b718378c125a5`.
8. Current state: `CURRENT_STATUS.md` blob `b367bbecba7527025320bded136fdb22eee5f362`.

No literature novelty is claimed. The public paper is the primary scientific source; this run is a campaign quantifier synthesis and new exact normal-form proof from already established identities.

## 3. Theorem inventory and first unpaid lines

`TARGET_QUANTIFIERS.md` gives the full table. The essential classification is:

- Regular functions, bounded combinations of regular functions, bounded read-`k`/`M` compositions, product-biased symmetric thresholds, read-once threshold formulas, fresh-selector/orthogonality closures, and fixed `(d,K,nu)` phase/fiber functions are **proved class theorems**. The first missing edge is a universal representation whose labels, overlaps, ranks, and activation costs are paid by `O(I)`.
- The complete posterior-forest residual bound is **sufficient, one way**: `J_f<=K I(f)` for an admissible package would imply FEI with the stated additive constant. Universal construction/payment is the first missing line; no converse is used.
- The relevant-coordinate endpoint and signed downward endpoint are **equivalent to FEI in finiteness** by explicit additive sandwiches. Their optimal constants are not identified.
- A uniform fixed-cyclic conditional completion is **FEI-strength** because it admits arbitrary tensor cores; bounded fiber support is a genuine restriction and is not such a completion.

## 4. New result I: critical-prime normal form

**Claim B01-A001-CRITICAL-PRIME-NORMAL-FORM-v1 (PROVED, pending review).** Every nonconstant genuine Boolean `f` has a restriction-critical tensor-prime descendant `h` satisfying `H(h)/I(h)>=H(f)/I(f)`. Consequently the supremum defining `C_FEI` is unchanged when restricted to that class.

For a relevant coordinate `i`, let `f_+,f_-` be the restrictions and

`bar H_i=(H(f_+)+H(f_-))/2`, `bar I_i=(I(f_+)+I(f_-))/2`, `Delta_iH=H(f)-bar H_i`.

Since restriction averages all non-`i` directional influences,

`bar I_i=I(f)-I_i(f)`.

With `R=H(f)/I(f)`, exact algebra gives

`bar H_i-R bar I_i=R I_i(f)-Delta_iH`.  (4.1)

If `Delta_iH<R I_i`, the right side is positive. The average of `H(f_b)-R I(f_b)` is therefore positive, so one child is nonconstant and has ratio greater than `R`. Restrict to it.

If the current function is restriction-critical but has a nontrivial disjoint product factorization `uv`, exact tensor identities give `H(uv)=H(u)+H(v)` and `I(uv)=I(u)+I(v)`. Hence `R(uv)` is the influence-weighted average of the two factor ratios; retain a factor with ratio at least `R(uv)`.

The retained factor is itself a restriction descendant: fix the discarded nonconstant Boolean factor at an input where it equals `+1`; fixing it at `-1` would only negate the retained factor and would also preserve squared spectrum, entropy, and influence.

Each operation strictly lowers the number of relevant variables. Alternating them terminates at a function that admits neither improvement: it is restriction-critical and tensor-prime, and its ratio never decreased.

If `C_critstep` is the supremum of `min_i Delta_iH/I_i` over the critical-prime class, then criticality and the A003 entropy bridge give

`C_FEI<=C_critstep<=C_FEI+2/ln2`.

Thus the exact surviving gap is:

> Is there one finite `K` such that every nonconstant restriction-critical tensor-prime Boolean `h` has a relevant coordinate `i` with `Delta_iH<=K I_i(h)`?

This is equivalent to FEI in finiteness. It does not evade addressing, rare restrictions, prime gates, or the bent one-point-defect obstruction; it only removes strictly improvable restrictions and disjoint tensor redundancy.

## 5. New result II: fixed-cyclic conditional completion is FEI-strength

**Claim B01-A001-FIXED-CYCLIC-STRENGTH-v1 (PROVED, pending review).** Fix a Boolean seed `f_0(X,Y)`. For arbitrary Boolean `g` on fresh variables and `t>=1`, put `F_t=f_0 g^{tensor t}`. The B07 product identity gives

`H_{F_t}(S_{Y union Z^t}|S_X)=H_{f_0}(S_Y|S_X)+tH(g)`.

If finite `A,K`, independent of `g,t`, satisfy

`H_{F_t}(S_{Y union Z^t}|S_X)<=A+KtI(g)`

for every Boolean `g` and every `t`, then division by `t` and `t->infinity` gives `H(g)<=KI(g)` for every `g`. Thus this completion is FEI-strength. The additive overhead disappears, but no equality of optimal constants is asserted. The fixed-fiber-support theorem remains noncircular because tensoring a positive-entropy core multiplies support exponentially and leaves that class.

## 6. Circularity audit

The following edges are rejected:

1. Using `C_step<=C_FEI+2/ln2` as an independent finite bound on `C_step`.
2. Treating the forest reference measure as an `O(I)` expected code without paying its posterior, rank, root and normalization terms.
3. Applying FEI to the arbitrary tensor core to prove the fixed-cyclic conditional estimate.
4. Suppressing unbounded `m,k,M`, overlaps, labels or reused-selector collision terms in the public class theorems.
5. Promoting weighted/non-Boolean prefix examples or one finite constant violation to a genuine Boolean unbounded-ratio counterfamily.

## 7. Validation

Command:

`python3 verify_quantifier_reduction.py`

Observed output is archived in `VERIFY.out`. It exhaustively checked all 270 nonconstant truth tables through dimension three, 746 relevant-coordinate instances of (4.1), the monotone critical-prime descent for every table, and 256 nonconstant tensor pairs with factor dimensions at most two. Result: **PASS**. Maximum floating residual in (4.1) was `2.220e-16`; influence identities used exact rational arithmetic. This is a finite implementation audit only; Sections 4--5 are the all-dimensional proofs.

## 8. Movement, limitations and next action

The packet's two required artifacts are complete pending independent review. Mathematical movement is the exact critical-prime normal form and the explicit tensor-order quantifier in the fixed-cyclic hardness test. These eliminate noncritical restrictions and disjoint tensors from the active good-coordinate search and prevent the conditional phase route from being mislabeled as easier.

Full FEI remains open. The universal critical-prime coordinate estimate, universal posterior residual payment, and universal joint-witness cost remain unproved.

**Next action:** A086 or A094 should reconstruct (4.1), the termination argument, the tensor-prime alternation, and the fixed-cyclic `t->infinity` quantifiers. After review, the mathematical attack should target the existential coordinate estimate only on restriction-critical tensor-prime functions, testing the bent one-point-defect selector and actual prime Boolean gates.

## 9. Configuration and delivery separation

- Model: Codex as exposed by this run; reasoning effort not exposed.
- Subagents: none.
- Scheduler/graph mutation: none.
- Independent review: not yet performed.
- Native Brain ingestion: not claimed.
- Persistence receipts are recorded in `PROGRESS.json`; they are not evidence of mathematical acceptance or downstream use.
