Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** The requested GPT-6 / maximum setting is not authenticated by the exposed runtime.

# P03 FEI — exact transverse section recombination and sharp block payment

## Status and mechanism delta

Parent problem: Friedgut--Kalai Fourier entropy--influence (FEI), to prove one finite universal constant `C` with

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Source status before -> after: OPEN -> OPEN. Universal finite constant: UNKNOWN -> UNKNOWN. P03 native finite atlas: 6 -> 6.** No restricted section theorem or finite check below is counted as full FEI.

This run proves a fresh-variable-free, all-dimensional **projected recombination telescope**. If the physical variables split as `A sqcup Y`, then physically revealing all of `Y` in any adaptive order gives the exact identity

\[
\boxed{H(S_A)=\mathbb E_y H(\widehat{f_y}^{\,2})+S^A_{\mathcal T_Y}},
\]

where `S` is the parent spectral random set, `f_y` is the physical `Y`-section on `A`, and `S^A_T` is the weighted sum of Jensen--Shannon divergences of the two child squared spectra **after marginalizing them to `A`**. Data processing and P03's inherited sharp recombination theorem then give

\[
\boxed{
H(S_A)\le \mathbb E_y H(\widehat{f_y}^{\,2})
 +\frac2{\ln2}J^{\rm fold}_{\mathcal T_Y}
\le \mathbb E_y H(\widehat{f_y}^{\,2})
 +\frac2{\ln2}I_Y(f).
}
\tag{0.1}
\]

The coefficient `2/ln2` is best possible, already for one transverse physical bit.

Combining (0.1) with NM13-02's complete-block allocation compression gives a new hereditary cross-gluing theorem: if every `Y`-section on `A` has direct FEI constant `C_A` and every `A`-section on `Y` has hereditary constant `K_Y`, then a full physical tree exists with

\[
\boxed{R_{\mathcal T}(f)\le C_A I_A(f)+(K_Y+2/\ln2)I_Y(f).}
\tag{0.2}
\]

There is no orthogonality, controller, symmetry, degree, branch-independence, or fresh-variable assumption. The recombination surcharge is paid once for the whole block.

## Dependencies and scope

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Current P03 entrypoint: `proofnet24/P03-fei/README.md`, blob `d226f1c4a460a0f90ba25f40a8a6b6a8d03ab2e9`. Its retired false routes remain retired: pointwise erasure converse, fixed-coefficient affine drift, resolvent/interpolation, all-coordinate absolute-overlap selector, derivative-degree scalar schedule, blind curvature payment, fixed-`s<2` Renyi payment, and related superseded scalar surrogates.

The restricted fresh-control theorem referenced in `operations/PROB10_2026-09-20.md` was read from creation commit `ef1087448014f0f6e5c9b4671c200a4020d8e3ea`. It proves `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` for arbitrary Boolean seeds under appended controls with `c>=3` and `2^{-c}M_0(f)<=1`. It explicitly does **not** prove fixed-domain FEI because `Gamma_c` appends variables and is not a closed derivative-chain transition. No fresh controls are used here.

Immediately preceding own substantive report: `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T15-29-48+0300__fei-spectral-orthogonal-controller-splicing.md`, blob `7a4cf6bd978750ce2fe13c95ac5f5db36c6032e9`, creation commit `984ea410fefed379e96f21450934a75e5c94fd2b`. It proves the two-controller spectral-orthogonal factorization and retains the universal theorem `J_i^rec<=B_i`, hence `S_T<=R_T`.

Sharp recombination dependency: `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-15-00Z__fei-sharp-recombination-clarkson-endpoint.md`, blob `37d0738076bd5f686a874e150f23d7ed54e7636d`, which proves

\[
J_i^{\rm rec}(f)\le\frac2{\ln2}j_i(f),\qquad j_i=\min\{\operatorname{Inf}_i,1-\operatorname{Inf}_i\},
\tag{1.1}
\]

and proves the coefficient sharp by a bent quadratic child and a one-point flip.

Newest complementary NM13-02 report: `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T16-08-00+0300__multiway-orthogonal-label-splicing.md`, creation commit `8a11e68b663e81f3ec270f72786ff94b7c4d6486`. It pays a many-way orthogonal-label surcharge by `2I_Y` and obtains a `9/5` hereditary certificate for a connected cubic-cycle family. Its coefficient is better under its structural orthogonality hypothesis; the theorem below is the arbitrary-section fallback and does not edit the peer claim.

Also used: NM13-02 block compression, `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T15-08-00+0300__block-compression-balanced-controller.md`, blob `c155fb1d672bfe9858463391f2db0d15c5b5559d`, which proves for every complete adaptive physical `A`-prefix

\[
R_{\mathcal T_A}(f)\le B_A(f):=H(S_A\mid S_{A^c}),
\qquad Q_{\mathcal T_A}=I_A(f).
\tag{1.2}
\]

The owner continuation `proofnet24/P03-fei/continuations/2026-09-20-logarithmic-packets/REPORT.md`, blob `dd853989dfca39e69a3d0334d984f1d3183d08fc`, was inspected for overlap; it leaves arbitrary overlapping packets unpaid and is not used below.

External source check on 20 September 2026: González--MacManus--Pereyra, arXiv:2606.00246 (submitted 29 May 2026), still states universal FEI as a conjecture; its key restriction inequality would imply FEI if universal, while the paper proves restricted stopping-tree classes. Current literature continues to attribute FEI to Friedgut--Kalai (1996). A bounded search did not establish an exact prior match for the theorem below; publication priority is **UNVERIFIED**. `POSTED.md` was checked; the posted Kalai entropy/singularity manuscript is a different exact claim.

## Different approaches this run

1. **Recursive Hellinger/KL selector surcharge.** Valid in the preceding spectral-orthogonal splice, but without new structure it can reuse descendant influence. NM13-02 now pays it once under orthogonal labels; forcing that representation universally would be artificial, so this was not pursued.
2. **Coefficient-packet payment.** The new packet continuation gives useful controlled-incidence estimates, but arbitrary overlap remains the live obstruction there. Combining it with a section tree reintroduces an uncontrolled incidence parameter.
3. **Projected child-law data processing.** Successful. Keep the full dependent child spectra, marginalize only after forming the exact physical child laws, and charge the projected mixture entropy to full Jensen--Shannon recombination. This is a genuinely different method from the preceding controller/Hellinger run.

## 1. One-step projected recombination identity

Let `g` be Boolean on `A sqcup R`, let `i in R`, and let `g^+,g^-` be the two physical children. Let `P,Q` be their squared Fourier laws on `A sqcup (R\{i})`; write `P_A,Q_A` for their marginals on `A`. Define `M_A(g)=H(S_A)`.

### Lemma 1

\[
\boxed{
M_A(g)-\frac{M_A(g^+)+M_A(g^-)}2
=\operatorname{JS}(P_A,Q_A)
\le\operatorname{JS}(P,Q)=J_i^{\rm rec}(g).
}
\tag{2.1}
\]

### Proof

For each residual Fourier label `T`, write

\[
u_T=\widehat g(T),\qquad v_T=\widehat g(T\cup\{i\}).
\]

Up to the harmless convention for the physical signs,

\[
\widehat{g^+}(T)=u_T+v_T,\qquad
\widehat{g^-}(T)=u_T-v_T.
\]

Therefore

\[
\frac12\widehat{g^+}(T)^2+\frac12\widehat{g^-}(T)^2=u_T^2+v_T^2.
\tag{2.2}
\]

The right side is exactly the parent squared spectral law with the spectral bit `S_i` forgotten. Marginalizing (2.2) further to `A` shows that the parent `A`-marginal is `(P_A+Q_A)/2`. Hence

\[
M_A(g)-\frac{M_A(g^+)+M_A(g^-)}2
=H\!\left(\frac{P_A+Q_A}{2}\right)-\frac{H(P_A)+H(Q_A)}2
=\operatorname{JS}(P_A,Q_A).
\]

For the inequality, put `M=(P+Q)/2`. Then

\[
\operatorname{JS}(P,Q)=\frac12D_2(P\Vert M)+\frac12D_2(Q\Vert M).
\]

Marginalization is a deterministic channel, and the log-sum inequality gives `D_2(P_A||M_A)<=D_2(P||M)` and the same for `Q`. Averaging proves `JS(P_A,Q_A)<=JS(P,Q)`. QED.

The point is that only recombination information still visible on `A` can increase the `A`-marginal entropy; recombination living solely in the yet-unqueried part of `Y` is automatically discarded.

## 2. Exact adaptive projected telescope

Let `T_Y` be any complete adaptive physical `Y`-prefix: every branch queries each coordinate of `Y` exactly once, no coordinate of `A`, and then stops. At a node `v`, let `P_v,Q_v` be the child squared spectra and define

\[
S^A_{\mathcal T_Y}:=\sum_v w_v\operatorname{JS}((P_v)_A,(Q_v)_A),
\]

\[
S_{\mathcal T_Y}:=\sum_vw_vJ_{i(v)}^{\rm rec}(f_v),\qquad
J^{\rm fold}_{\mathcal T_Y}:=\sum_vw_vj_{i(v)}(f_v).
\]

### Theorem 2

\[
\boxed{H(S_A)=\mathbb E_yH(\widehat{f_y}^{\,2})+S^A_{\mathcal T_Y}.}
\tag{3.1}
\]

Moreover

\[
\boxed{
S^A_{\mathcal T_Y}\le S_{\mathcal T_Y}
\le\frac2{\ln2}J^{\rm fold}_{\mathcal T_Y}
\le\frac2{\ln2}I_Y(f).
}
\tag{3.2}
\]

Thus (0.1) holds.

### Proof

Apply the equality in Lemma 1 at every internal node and multiply by its physical cylinder weight. All intermediate `A`-marginal entropy terms telescope through the adaptive tree. At a terminal leaf all of `Y` is fixed, so the remaining spectrum lives only on `A`; its `A`-marginal entropy is exactly `H(f_y)`. Every final physical assignment `y` has weight `2^{-|Y|}` even when the query order is adaptive. This proves (3.1).

The first inequality of (3.2) is Lemma 1 summed over the tree. The second is inherited (1.1). For the last, `j_i<=Inf_i` pointwise and a complete physical `Y`-prefix partitions the original `i`-edges for every `i in Y`, so

\[
\sum_vw_v\operatorname{Inf}_{i(v)}(f_v)=I_Y(f).
\]

Hence `J^fold_T<=I_Y(f)`. QED.

The preceding P03 theorem `J_i^rec<=B_i` and NM13-02 block compression add the structure-sensitive refinement

\[
\boxed{
H(S_A)\le\mathbb E_yH(f_y)
+\min\left\{R_{\mathcal T_Y},\frac2{\ln2}J^{\rm fold}_{\mathcal T_Y}\right\}
\le\mathbb E_yH(f_y)
+\min\left\{B_Y(f),\frac2{\ln2}I_Y(f)\right\}.
}
\tag{3.3}
\]

Thus exact-isospectral or otherwise low-recombination prefixes automatically pay less than the universal worst case.

## 3. Sharpness

### Theorem 3

The coefficient `2/ln2` in

\[
H(S_A)\le\mathbb E_yH(f_y)+cI_Y(f)
\tag{4.1}
\]

cannot be replaced by any smaller universal `c`.

### Proof

Let `d=2m`, `N=2^d`, and

\[
g(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{d-1}x_d}.
\]

This is bent, so every Fourier coefficient has magnitude `rho=N^{-1/2}`. Let `h` be obtained by flipping only `g(0)`, and add one physical selector bit `t` whose two restrictions are `g,h`. Take `A` to be the `d` background coordinates and `Y={t}`. The children disagree on exactly one of `N` inputs, hence `I_Y=Inf_t=delta=N^{-1}=rho^2`.

For one selector bit, the parent spectral marginal on `A` is exactly `(P+Q)/2`, where `P,Q` are the child squared spectra. Therefore

\[
H(S_A)-\frac{H(g)+H(h)}2=\operatorname{JS}(P,Q).
\tag{4.2}
\]

The inherited sharp-recombination proof computes the two likelihood ratios

\[
r_+=(1-2\rho)^2,\qquad r_-=(1+2\rho)^2
\]

with proportions `(1+rho)/2,(1-rho)/2`. For

\[
\psi(r)=\frac12\log_2\frac2{1+r}+\frac r2\log_2\frac{2r}{1+r}
\]

it obtains

\[
\operatorname{JS}(P,Q)=\frac{1+\rho}{2}\psi(r_+)+\frac{1-\rho}{2}\psi(r_-)
=\frac2{\ln2}\rho^2+O(\rho^3).
\]

Divide (4.2) by `I_Y=delta=rho^2` and let `d` tend through even integers. The ratio tends `2/ln2`. Together with Theorem 2 this proves sharpness. QED.

The extremizing recombination survives **exactly after projection to `A`**, so the block coefficient itself, not merely an intermediate one-step bound, is sharp.

## 4. Hereditary transverse gluing

Assume every physical `Y`-section `f_y` on `A` satisfies

\[
H(f_y)\le C_A I(f_y).
\tag{5.1}
\]

Physical sectioning preserves the `A`-edge budget exactly, so `E_y I(f_y)=I_A(f)`. Theorem 2 gives

\[
\boxed{H(S_A)\le C_A I_A(f)+\frac2{\ln2}I_Y(f).}
\tag{5.2}
\]

Since `B_A(f)=H(S_A|S_Y)<=H(S_A)`, NM13-02 block compression implies that every complete adaptive physical `A`-prefix obeys

\[
\boxed{R_{\mathcal T_A}(f)\le C_A I_A(f)+\frac2{\ln2}I_Y(f).}
\tag{5.3}
\]

Now additionally suppose every `A`-section `f_a` on `Y` has a full hereditary certificate

\[
R_{\mathcal U_a}(f_a)\le K_Y I(f_a).
\tag{5.4}
\]

Query all of `A` first and graft those leaf trees. The exact restriction influence identity gives `E_a I(f_a)=I_Y(f)`, so

\[
\boxed{
R_{\mathcal T}(f)\le C_A I_A(f)+(K_Y+2/\ln2)I_Y(f)
\le\max\left\{C_A,K_Y+\frac2{\ln2}\right\}I(f).
}
\tag{5.5}
\]

This proves (0.2). In particular, whenever `C_A>=K_Y+2/ln2`, an arbitrary compatible transverse gluing inherits the constant `C_A` with no dimension or number-of-sections penalty.

A direct two-sided variant is also immediate. If every `Y`-section on `A` has direct constant `C_A` and every `A`-section on `Y` has direct constant `C_Y`, then `H(S)<=H(S_A)+H(S_Y)` and Theorem 2 in both orientations gives

\[
\boxed{
H(f)\le(C_A+2/\ln2)I_A(f)+(C_Y+2/\ln2)I_Y(f).
}
\tag{5.6}
\]

These are restricted closure statements, not universal FEI.

## 5. What remains

The theorem removes the dependent-branch mixing bill for an **entire physical block**: all mixing visible in the untouched spectral block is paid once by physical influence, and the universal coefficient is already optimal. What is still missing is a universal proper-block selector / section-certification theorem. For Corollary (5.5) one must still find a split for which one transverse section family has a dimension-free direct certificate and the opposite leaves have a dimension-free hereditary certificate. Recursing (5.5) on arbitrary functions without such structure simply adds the sharp surcharge at successive scales and yields no dimension-free constant.

Thus the live obstruction narrows from “hereditary allocation plus dependent recombination” to **universal section certification / proper block selection for hereditary allocation** on the signed-translation-rigid connected high-degree core.

The retired pointwise-erasure, resolvent/interpolation, fixed-drift, absolute-overlap, derivative-degree, blind-curvature, minor-child-plus-curvature, and fixed-Renyi routes remain retired.

## 6. Executed sanity checks

Checker:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T16-28-06+0300__check_transverse_section_recombination.py`
(local SHA-256 `5f1bed13e8d264ab34e27d29e0325425a7320fa5bbc05a78d3703702b4f73755`).

Output:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T16-28-06+0300__transverse_section_recombination_output.json`
(local SHA-256 `c9a1a0e28b3fdd398f4803a2304c0f2e3901988fe6cdd118f16f9f31d6292a82`).

Executed results:

- all `65,812` Boolean functions through dimension four, every nonempty proper physical block: `919,072` `(f,A)` cases; maximum numerical violation of (0.1) was `0.0`;
- `20,000` deterministic-seed local stress cases in dimensions 2--8; maximum `projected_gap-JS` was `4.440892098500626e-16`, maximum violation of `JS<=(2/ln2)j_i` was `0.0`;
- sharp bent sequence for `d=2,4,6,8,10,12,14`; ratios were `2.19518, 2.80566, 2.86921, 2.88156, 2.88445, 2.88515, 2.88533`, approaching `2/ln2=2.8853900817779268...`; the marginal gap matched full JS to floating precision.

Checker status: **PASS**. These are self-checks supporting the analytical proof, not independent review.

## Next nonredundant attack

Search for a structure-sensitive block selector on the signed-translation-rigid connected core: a physical split `A sqcup Y` where either (i) all `Y`-sections land in an existing dimension-free direct class while the `A`-leaves retain a hereditary certificate, or (ii) the projected ledger `S^A_TY` has a summable structural rebate strictly below its sharp worst-case influence envelope. A family forcing repeated near-`2/ln2` projected recombination for every useful proper split would decisively delimit this route.

## ledger_delta

```yaml
ledger_delta:
  owner: P03
  parent_problem: Friedgut-Kalai Fourier entropy-influence
  parent_status_before: OPEN
  parent_status_after: OPEN
  universal_finite_constant_before: UNKNOWN
  universal_finite_constant_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  fresh_variables_used: false
  new_theorems:
    - statement: H(S_A) = E_y H(f_y) + S^A_TY
      scope: every Boolean function, every physical block split, every complete adaptive Y-prefix
    - statement: H(S_A) <= E_y H(f_y) + (2/ln2) I_Y(f)
      coefficient: 2/ln2
      sharp: true
    - statement: R_T <= C_A I_A + (K_Y+2/ln2) I_Y
      scope: direct-certified Y-sections and hereditary-certified A-leaves
  mechanism_gain:
    - arbitrary dependent physical section mixing is paid once by projected Jensen-Shannon recombination
    - no controller orthogonality, symmetry, degree, branch independence, or fresh-control hypothesis
    - sharp coefficient already attained asymptotically by a one-bit transverse block
  source_level_gain: none; unrestricted FEI remains open
  complementary_peer_result:
    worker: NM13-02
    commit: 8a11e68b663e81f3ec270f72786ff94b7c4d6486
    relation: orthogonal-label theorem has sharper coefficient 2 under structure; this is the arbitrary-section fallback
  checker:
    exhaustive_block_cases: 919072
    random_local_cases: 20000
    max_block_violation: 0.0
    max_local_gap_minus_JS: 4.440892098500626e-16
    sharp_sequence_last_ratio_d14: 2.885331351251807
    target_constant: 2.8853900817779268
    status: PASS
  retired_routes_preserved:
    - pointwise erasure
    - resolvent/interpolation
    - fixed affine drift
    - absolute-overlap selector
    - derivative-degree scalar schedule
    - blind curvature
    - fixed-Renyi exponent
  remaining_obstruction: universal section certification / proper block selection for hereditary allocation
  next_attack: structure-sensitive block selector or summable projected-recombination rebate on signed-translation-rigid connected cores
  independent_review: PENDING
  publication_priority: UNVERIFIED
```

**End of complete run report.**
