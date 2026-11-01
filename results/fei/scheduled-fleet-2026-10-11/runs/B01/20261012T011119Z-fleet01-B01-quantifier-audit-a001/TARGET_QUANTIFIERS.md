# A001 exact quantifier audit

## 1. Full target and conventions

For every integer `n>=0` and genuine Boolean sign `f:{-1,1}^n->{-1,1}`, under the uniform product law, put

`P_f(S)=fhat(S)^2`,

`H(f)=sum_S P_f(S) log_2(1/P_f(S))`, and

`I(f)=sum_S |S| P_f(S)`.

The convention is `0 log_2(1/0)=0`. The full Fourier Entropy--Influence conjecture is

> **FEI(C).** There exists one finite real `C`, independent of `n` and `f`, such that `H(f)<=C I(f)` for all genuine Boolean signs.

Constants have `H=I=0`, so FEI holds for them without forming `H/I`. Ratios below are used only for nonconstant functions, for which `I>0`.

Define

`C_FEI=sup{H(f)/I(f): f is a nonconstant genuine Boolean sign in any finite dimension}`.

Thus full FEI is exactly the assertion `C_FEI<infinity`.

## 2. Source-pinned theorem inventory

Labels are deliberately scope-sensitive: **CLASS** is a proved restricted theorem, **SUFFICIENT** is a one-way universal implication to FEI, **EQUIVALENT-FINITE** means only finiteness equivalence with controlled additive constants, and **FEI-STRENGTH** means the proposed uniform completion would imply full FEI by an arbitrary-core embedding.

| Route/result | Exact quantifiers retained | Status for full FEI | First unpaid implication |
|---|---|---|---|
| Regular Boolean functions | Every regular Boolean sign; `H<=C_reg D`, `C_reg<8.937`, with the paper's regularity and character-distance definitions | **CLASS** | No theorem makes every Boolean function regular at dimension-independent influence cost. |
| Combination of regular gates | Every `F(h_1,...,h_m)` in the theorem; constant grows as `11.238+(17/5)log_2 m` | **CLASS** | Need a representation of arbitrary Boolean functions with the label/overlap cost paid by `O(I)`, not by unbounded `log m`. |
| Read-`k`, at most `M` regular pieces per gate | Every function satisfying the paper's read/combination hypotheses; constant `41+7log_2 k+(29/5)log_2 M` | **CLASS** | Arbitrary Boolean functions do not have bounded `k,M`; no universal decomposition paying the logarithms is proved. |
| Product-biased symmetric thresholds and read-once threshold formulas | Every stated threshold gate under every product bias has corrected `FEI+` constant `<744`; the paper's formula closure then gives uniform-cube class results | **CLASS** | A general Boolean gate is not a biased symmetric threshold, and no bounded-cost universal threshold decomposition is proved. |
| Fresh-selector / neighboring-orthogonality multiplexer extension | Every selector construction satisfying the paper's fresh physical selector and orthogonality (or stated positive selector-energy) hypotheses | **CLASS / PROVED CLOSURE** | Reused selector variables, collision credits and arbitrary shared-variable interference are outside the theorem. |
| Queue/variational witness theorem | Every admissible representation has the displayed exact witness reference bound; the addressing family has expected cost `<10 I` | **CLASS plus exact interface** | A uniform expected joint-witness cost bound for every Boolean function, including rank, sparse-root and normalization terms, is unproved. |
| Posterior forest residual `J_f` | If there is finite `K` such that every Boolean `f` admits a complete admissible representation with `J_f<=K I(f)`, then FEI holds with `C=2+K_ref+K`, `K_ref=3+2log_2 3+log_2(6e)` | **SUFFICIENT** | Universal existence and the bound `J_f<=K I(f)` are unproved. No converse is used. |
| Relevant-coordinate restriction step | `C_step=sup_f min_{i:I_i(f)>0} Delta_iH/I_i(f)` obeys `C_FEI<=C_step<=C_FEI+2/ln 2` | **EQUIVALENT-FINITE** | Prove one finite dimension-independent upper bound on the minimum over relevant physical coordinates. The right inequality does not itself give a bound without FEI. |
| Signed downward law | With the recovered Boolean autocorrelation constraints, `C_L<=C_FEI<=C_L+3/ln 2` | **EQUIVALENT-FINITE** | Prove `L(f)<=K I(f)` universally (or the corresponding existential refinement). Non-Boolean prefix laws do not settle realizability. |
| Fixed `(d,K,nu)` phase/fiber theorem | Every Boolean `f(X,Y)` of `X`-degree `d>=1`, conditional fiber support at most `K`, and variance at least `nu>0` satisfies the displayed dimension-independent bound | **CLASS** | Arbitrary functions need not have fixed `d,K,nu`; fixed `K` excludes arbitrary tensor cores exactly. |
| Uniform fixed-cyclic conditional completion | Fix a Boolean seed `f_0(X,Y)`. If constants `A,K<infinity` work for every Boolean core `g` and every tensor order `t` in the conditional inequality in Section 4 below, then `H(g)<=K I(g)` for every `g` | **FEI-STRENGTH** | The uniform conditional estimate is unproved. Bounded fiber support is not such an estimate. |

The current public source is `yspennstate/fourier-entropy-threshold-functions`, commit `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, `paper/main.tex` blob `1a9af8c62a32566a6ad1b7323a84d103a8375e93`. The recovered posterior-forest source is `reports/fei-2026-10-11/source_material/reductions/paper/forests.tex`, blob `3fd08d81a2bcd96acaaa268757c7f343e71e8249`. Exact endpoint derivations are in A003 commit `87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`; the fixed-cyclic source is B07 `PHASE_SCOPE.md`, blob `b9fe5f9cb171420581997c20819b718378c125a5`.

## 3. PROVED: restriction-critical tensor-prime normal form

This is a source-bound synthesis of the A003 restriction identity, exact tensor additivity, and the current critical-step frontier. It is not a proof of FEI.

For nonconstant `f`, write `R(f)=H(f)/I(f)`. For a relevant coordinate `i`, let `f_+` and `f_-` be the two restrictions and set

`bar H_i=(H(f_+)+H(f_-))/2`, `bar I_i=(I(f_+)+I(f_-))/2`,

`Delta_iH=H(f)-bar H_i`.

Exact influence splitting gives `bar I_i=I(f)-I_i(f)`. Hence

`bar H_i-R(f)bar I_i = R(f)I_i(f)-Delta_iH`.  (1)

Call `f` **restriction-critical** when

`Delta_iH >= R(f) I_i(f)` for every relevant physical coordinate `i`.

Call it **tensor-prime** when, after deleting dummy variables and constant factors, it is not a nontrivial product `u(x_A)v(x_B)` on disjoint nonempty coordinate blocks with both factors nonconstant.

**Lemma.** Every nonconstant Boolean `f` has a restriction-critical tensor-prime Boolean descendant `h` with `R(h)>=R(f)`.

**Proof.** If `f` is not restriction-critical, choose relevant `i` with `Delta_iH<R(f)I_i`. Equation (1) says the average of `H(f_b)-R(f)I(f_b)` over the two children is positive. Therefore at least one child is nonconstant and has ratio strictly larger than `R(f)`. Replace `f` by that child.

If the current function is restriction-critical but factors as `u v` on disjoint variables, spectral independence gives

`H(uv)=H(u)+H(v)`, `I(uv)=I(u)+I(v)`.

Thus `R(uv)` is the influence-weighted average of `R(u),R(v)`, and one nonconstant factor has ratio at least `R(uv)`. Replace the current function by that factor. After either replacement the number of relevant variables strictly decreases. Repeating terminates, and the terminal function is both restriction-critical and tensor-prime, with ratio no smaller than the starting ratio. QED.

This factor replacement is genuinely a restriction descendant: the discarded nonconstant Boolean factor takes both signs, so fix its block at an input where its value is `+1` (or use `-1`, which only negates the retained factor and leaves its spectrum squared unchanged).

Consequently

`C_FEI = sup{R(h): h is nonconstant, restriction-critical and tensor-prime}`.  (2)

This removes no hard instances by assumption: it is an exact hardness-preserving descent.

If

`C_critstep=sup_h min_{i:I_i(h)>0} Delta_iH/I_i(h)`

over the same critical-prime class, then criticality, (2), and the A003 fixed-coordinate entropy bound yield

`C_FEI <= C_critstep <= C_FEI+2/ln 2`.  (3)

Thus bounded good-coordinate cost remains equivalent to FEI in finiteness even after reduction to critical tensor-prime functions. Equation (3) does **not** identify optimal constants.

## 4. PROVED: exact fixed-cyclic FEI-strength test

Fix one Boolean seed `f_0(X,Y)` on disjoint uniform blocks. For arbitrary Boolean `g(Z)` on fresh variables and `t>=1`, let

`F_t=f_0 product_{s=1}^t g(Z_s)`.

The spectral law is a product conditional on the unchanged `X` frequency, so the B07 identity gives

`H_{F_t}(S_{Y union Z^t}|S_X)=H_{f_0}(S_Y|S_X)+t H(g)`,

and `I(g^{tensor t})=t I(g)`.

Suppose there exist finite constants `A,K`, depending on the fixed seed but not on `g` or `t`, such that for every genuine Boolean `g` and every `t>=1`,

`H_{F_t}(S_{Y union Z^t}|S_X) <= A+K t I(g)`.  (4)

Substitution gives

`t H(g) <= Kt I(g)+A-H_{f_0}(S_Y|S_X)`.

Divide by `t` and let `t` tend to infinity. Then `H(g)<=K I(g)` for every Boolean `g`; constants are harmless. Therefore (4) is FEI-strength. This rejects any attempt to call a uniform fixed-cyclic conditional completion an easier endpoint. It does not assert equality of its optimal constant with `C_FEI`, and it does not apply to the fixed-support theorem: for `H(g)>0`, the conditional fiber support grows exponentially with `t`.

## 5. Circular edges explicitly rejected

- `C_step<=C_FEI+2/ln2` cannot be used to prove `C_step<infinity` unless FEI is already known; the useful direction for a new proof is a direct universal bound on `C_step` or on its critical-prime restriction.
- The forest Gibbs/reference inequality does not pay the expected witness cost. Replacing that missing estimate by `H<=CI` is circular.
- The fixed-cyclic identity does not bound its conditional entropy. Invoking FEI on the arbitrary tensor core to do so assumes the desired conclusion.
- The class theorems in the threshold paper do not supply a universal bounded-cost representation. Treating an arbitrary number of gates, read overlap, or labels as a constant is a quantifier error.
- A finite witness against a proposed constant, a weighted/non-Boolean law, or a fixed-prefix obstruction is not an unbounded genuine-Boolean FEI counterfamily.

## 6. Exact surviving universal obstruction

After all proved implications are composed, the first unsupported dimension-independent assertion can be stated without representation language:

> **OPEN critical-prime coordinate estimate.** Does there exist a finite `K` such that every nonconstant restriction-critical tensor-prime Boolean `h` has some relevant coordinate `i` satisfying `Delta_iH<=K I_i(h)`?

By (2)--(3), this is equivalent to full FEI in finiteness. The fixed-coordinate additive losses are already sharp on the bent one-point-defect family; any improvement must exploit the existential coordinate and/or nonlocal structure. Addressing/multiplexers, rare restrictions, near tensors and prime Boolean gates remain mandatory tests.
