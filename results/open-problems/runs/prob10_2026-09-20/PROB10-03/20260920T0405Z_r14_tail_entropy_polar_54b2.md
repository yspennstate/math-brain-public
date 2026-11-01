Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE METRIC NO MOVEMENT: rigorous `kappa=-1` bracket width `6.48139658710 -> 6.48139658710`. This is the fifth consecutive unchanged R14 PROB10 source-metric run; the method changes again inside PROB10-03. Three materially different attacks: (A) exact full-line first-Jacobian tail envelopes, (B) entropy/variance decomposition of the delicate `H_B` sign, (C) exact Gaussian-polytope radial duality and a Farkas obstruction.**

# PROB10-03 — R14 bounded iteration: derivative tails, entropy balance, and radial duality

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO RIGOROUS ENDPOINT MOVED / NEW ANALYTICAL TAIL AND SIGN REDUCTIONS**.

## 1. Contract, continuity, and consumed state

I obeyed `operations/PROB10_2026-09-20.md`, remained on the exact negative-margin spherical Gaussian perceptron, and made no scheduler change.

Consumed before doing the new mathematics:

- `operations/PROB10_2026-09-20.md` on current `master`;
- root `POSTED.md` on current `master`;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, preserving rather than overwriting its canonical state;
- immutable Campbell refocus handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, blob `edaa787e384c28a4b5a658dbba80f664cde75882`, which preserves owner navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2` and Campbell metric `S=5`;
- newest prior R14 PROB10 report `runs/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_face_transverse_9c61.md`;
- R14 proof artifact `artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_face_reduction.md`;
- complementary NM13-03 report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md`;
- complementary NM13-07 reports `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-full2-two-scalar-reduction.md` and `...__t03-moment-jacobian-broad-contraction.md`;
- the exact NM13-07 Jacobian compiler source `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_moment_jacobian_compiler.py`.

The old negative-margin failure constraints remain active: the globally optimized one-parameter partial lift is exhausted at `12.78437096216`; MZZ-style weighted second moment has positive-overlap/local-curvature obstructions; `N^{-1/2}` sphere nets pay `Theta(N log N)` entropy; plain facet first moment is too weak; smaller-radius algorithms do not solve the exact sphere; and direct whole-product interval arithmetic destroys cancellations in the complete-second-lift reconstruction.

## 2. Frozen source model and rigorous metric

Freeze

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`, with fixed `alpha` and `N->infinity`.

A lower endpoint means SAT probability tends to one. An upper endpoint means SAT probability tends to zero.

Entering and leaving this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = 6.48139658710`.

The `alpha=12.75` complete-second-lift point remains a **candidate only**.

## 3. Fresh source/scope check

The current primary-source distinction remains unchanged.

- El Alaoui--Sellke, arXiv:2010.15811, is the exact Gaussian sphere model but explicitly treats the negative-margin FRSB/Parisi structure conjecturally and returns a feasible vector at radius `sqrt(qbar N)` with `qbar<1`, not a full-radius threshold theorem.
- Stojnic, arXiv:1306.3980, remains the rigorous negative-margin upper-bound baseline.
- Stojnic, arXiv:2312.16531, fits the NSP into stationarized fully lifted RDT and describes concrete capacity values after substantial numerical work; a displayed finite-lift numerical value is not silently treated here as an outward-certified endpoint.
- A bounded fresh search through 20 September 2026 found 2025 replica/algorithmic work on negative perceptrons but no later primary theorem plainly replacing the rigorous full-radius bracket above. This is dated bounded negative evidence, not a worldwide novelty certificate.

`POSTED.md` still explicitly distinguishes the owner's posted zero-margin/Ising work from this continuous negative-margin spherical target.

## 4. Attack A — exact full-line derivative tails

New proof artifact:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_polar_reduction.md`

creation commit `7b8c8787a84f8ebb1014da7b60f2528c4236f38e`.

The preceding centered-Hessian report had compact `|z|<=9` interval-Simpson center enclosures but correctly did not claim rigorous derivative tails. This run closes that analytical tail gap.

On the R14 candidate box

`|p-p_c|<=1/2000`, `|B-B_c|<=1/50`,

coarsen to `3/5<p<2/3`, `0<B<5`. For `|z|>=9`, let

`Y=sqrt(p)z+sqrt(1-p)H-1`,

`f=E exp[-B(Y_+)^2]`, `m_r=E[Y_+^r exp(-B Y_+^2)]/f`.

I proved uniformly

`m_1<=4|z|`, `m_2<=3z^2`, `m_3<=11|z|^3`, `m_4<=4z^4`.

The proof splits according to the sign of the conditional mean. If the mean is negative, `f>=1/2`; if it is nonnegative, completing the square identifies `J_r/J_0` with moments of a shifted Gaussian conditioned positive, whose conditioning probability is also at least `1/2`. Both cases reduce to elementary Gaussian moment bounds with `|mu|<=(10/9)|z|`.

Combining these estimates with the exact tilted-moment compiler and log-concavity gives

`|u|<=7z^2`, `|u_mu|<=40|z|`, `|u_B|<=3z^2`,

`0<=u_BB<=4z^4`, `|u_muB|<=240|z|^3`, `-3<=u_mumu<=0`.

The last bound uses the exact score-variance identity

`u_mumu=Var_tilt(Y)/s^4-1/s^2`

and Gaussian-convolution log-concavity.

For the outer standard Gaussian, the exact finite exponential-series bound

`e>163/60`

implies

`phi(9)<U=(1/2)(60/163)^40`.

Mills plus the exact tail-moment recurrence then gives explicit two-sided `z^2,z^4` tail bounds. Substitution yields

`Tail(I) < 3.0e-16`,

`Tail(I_B) < 1.2e-16`,

`Tail(I_BB) < 1.4e-14`,

`Tail(K) < 6.4e-14`,

`Tail(K_B) < 6.4e-11`,

`Tail(K_p) < 4.8e-13`.

Using the exact full-line OU identities reconstructs the omitted-tail uncertainty

`delta_tail(I_p)<5.4e-14`,

`delta_tail(I_Bp)<5.4e-11`.

This is genuine mechanism movement: the first-Jacobian full-line tail layer is now proved analytically rather than assumed from numerics. It still does not certify the compact `[-9,9]` parameter-box enclosure required for `alpha=12.75`.

## 5. Attack B — test the entropy-monotonicity shortcut and isolate its exact failure

I tried to replace interval certification of `H_B>0` by a structural sign proof.

For the conditional exponential tilt of `X=Y_+^2`, put

`M=-I_B>0`, `V=I_BB>=0`,

`L=E KL(nu_B||nu)=-(I-BI_B)`.

I proved exactly

`L_B=BV`,

`L(B)=int_0^B tV(t)dt`,

and

`H=-L+4B^2 M A_0`.

At a stationary root `H=0`, this gives the exact derivative identity

`H_B = 2L/B - BV - LV/M + L(A_{0,D}/A_0)D_B`.            (5.1)

The first pair has the variance-history representation

`2L/B-BV=(2/B)int_0^B t[V(t)-V(B)]dt`.                   (5.2)

This is useful, but it also falsifies the hoped-for shortcut: the generic signs `L>=0`, `M>0`, `V>=0` do **not** determine `H_B`. One must control variance evolution over the entire tilt interval and the reconstructed radial correction `(A_{0,D}/A_0)D_B`. Hence “convexity of `I` in `B`” alone cannot certify the Miranda monotonicity sign.

At the existing numerical-only center, the large positive and negative pieces cancel to a final `H_B` of only about `4.38e-4`. This diagnostic is consistent with the previously observed interval wrapping and is not used as a theorem.

This is the required written obstruction after repeated unchanged source metrics: a sign proof that forgets the correlated radial reconstruction is mathematically insufficient.

## 6. Attack C — dualize the feasibility obstruction exactly

For a fixed disorder realization define

`P={x:Gx>=-1}`,

`K=conv(0,-g_1,...,-g_M)`.

I proved the elementary polar identity

`P^circ=K`

and, writing `r(K)=min_{||u||=1}h_K(u)`, the exact source equivalence

`SAT <=> r(K)<=1`,

`UNSAT <=> r(K)>1`.

Indeed

`h_K(u)=max(0,max_a<-g_a,u>)`,

so `r(K)<=1` is literally the existence of a unit `u` satisfying every source inequality.

This also gives a precise obstruction to ordinary Farkas duality: the linear system `Gx>=-1` is always strictly feasible at `x=0`, so no one-vector LP infeasibility certificate can establish source UNSAT. Any successful direct dual proof must control the **radial/inradius obstruction uniformly over directions**. The polar identity is standard convex geometry and is not claimed as novel; its purpose is to prevent another run from pursuing a structurally impossible single-Farkas-vector route.

## 7. Executed exact self-check

Checker source:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_checker.py`

creation commit `7fe9cb6a52fa6f74dc6e518744694da47bcacd7d`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_checker.out`

creation commit `28470d0f272e26dd65b072756ccd959799d095d9`.

The executable uses exact rational arithmetic for the Gaussian-tail constants and source bracket, and exact SymPy algebra for the stationary entropy-balance identity. It ends

`ALL_EXACT_CHECKS_PASS`.

The output was read back from exact commit `28470d0f272e26dd65b072756ccd959799d095d9` before this report was written. Self-checks are not independent audits.

## 8. Source metric versus mechanism movement

### Source metric

Before:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

After:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

**Movement: none.**

### Auxiliary movement

1. first-Jacobian derivative-tail status on the `12.75` box: **uncertified -> explicit analytical bounds**;
2. `H_B` sign burden: opaque cancellation -> exact entropy/variance/radial identity (5.1)-(5.2);
3. direct dual route: generic Farkas idea -> exact Gaussian-polytope inradius formulation, with ordinary LP-Farkas infeasibility ruled out structurally.

## 9. Remaining full-scope gap and next bounded route

The source-moving obligation is now strictly compact:

1. outward-certify the closed one-dimensional moment formulas and second derivatives on `z in [-9,9]` over the small R14 box;
2. append the exact outer-tail theorem from this run;
3. certify either the centered-Hessian contraction hypotheses or, preferably if easier, `H_B>0`, `alpha_p>0` plus the four monotone-face corner signs;
4. certify `Psi>0` on the resulting root box;
5. only then invoke the already source-matched complete-second-lift implication and move `alpha_U` to `12.75`.

A genuinely different analytic alternative is to use (5.2) plus quantitative control of the radial term to prove `H_B>0` without a whole-box derivative enclosure. No such inequality is claimed yet.

Status remains **OPEN / PARTIAL**. No full capacity determination, publication novelty, or independent validation is claimed.

```yaml
ledger_delta:
  worker: "R14 / PROB10-03"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  status: "PARTIAL / OPEN"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
    requested_gpt6_maximum_native_setting: "not available on exposed scheduler surface"
  source_metric: "rigorous whp threshold bracket width alpha_U-alpha_L"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  source_movement: "none"
  unchanged_run_count_for_current_PROB10_refocus: 5
  obstruction_after_repeated_unchanged_runs: "generic entropy/log-concavity signs do not determine H_B because variance-history and D_B radial correction remain; direct product intervals lose these cancellations"
  auxiliary_movement:
    first_jacobian_outer_tails: "uncertified -> proved explicit bounds"
    H_B_structure: "opaque four-term cancellation -> entropy/variance/radial identity"
    dual_structure: "ordinary Farkas route ruled out; exact Gaussian-polytope inradius formulation"
  new_theorems:
    - "R14-T03-FIRST-JAC-TAIL"
    - "R14-T03-ENTROPY-BALANCE"
    - "R14-T03-POLAR-RADIAL (standard convex-duality mechanism; no novelty claim)"
  candidate_not_certified:
    alpha_U: "12.75"
    reason: "compact parameter-box interval/Taylor enclosure and Psi positivity remain"
  artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_polar_reduction.md @ 7b8c8787a84f8ebb1014da7b60f2528c4236f38e"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_checker.py @ 7fe9cb6a52fa6f74dc6e518744694da47bcacd7d"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_checker.out @ 28470d0f272e26dd65b072756ccd959799d095d9"
  campbell_handoff: "preserved; no duplicate handoff and no claim overwrite"
  independent_audits: 0
```

No scheduler state, cadence, email, Drive object, public posting, permission, shared claim, peer file, workflow, or force-push action was changed.