# B12 FEI — exact arity-5 unate center exclusion and a C-parametric dictator-tube bound

**Status:** `ESSENTIAL_STEP_APPLIED / ARITY5_UNATE_CENTER_CLOSED / FULL_FEI_OPEN`.

Full uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and mathematical sources were read directly; the native `math_brain`/`brain` runtime and authenticated receiver-context retrieval were unavailable in this invocation.

## 1. Live target and peer results actually consumed

The current owner message supersedes the older B12 row-coding mechanism for substantive work and asks all FEI workers to converge on the all-gate formulation

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le \sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

and either prove the extremal-gate implication or falsify it. The source-exact equivalence of (G) with FEI is in

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, observed blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

Two completed other-account results are used rather than duplicated.

1. **account02/B12, gate-margin falsification**:
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T025438Z-gate-margin-falsification/REPORT.md`, observed blob `bf37b4fd5ceae2c40e2b59266e2701fed8ff2780`.
   Its exact implication used here is that the old read-once/AND extremality hope is already false: the exact balanced ten-input gate `G10` has
   \[
   \frac{H(G10)}{I(G10)-1}>6.459372281637855731,
   \]
   hence requires quadratic gate margin `c_G10>0.018289126551422924>0.01`; the shared-graft `F5` gives the stronger `c_F5>0.2682037981828`. Therefore this run does not repeat an AND-extremality proof attempt. It narrows the untouched arity-five falsifier frontier.

2. **account02/B13, character-tube theorem**:
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T035349Z-character-tube-prime-defect/REPORT.md`.
   For a balanced Boolean `g`, an original-coordinate signed dictator `sigma chi_i`, defect
   \[
   \alpha=\Pr[g\ne\sigma\chi_i],\qquad L=\log_2(1/\alpha),
   \]
   its exact singleton specialization gives
   \[
   I(g)-1\ge 2\alpha(L-2),
   \tag{1.1}
   \]
   while the same source gives, with `m=4alpha(1-alpha)`,
   \[
   H(g)\le h_2(m)+m\log_2(2^n-1).
   \tag{1.2}
   \]
   These two inequalities are used below to sharpen the tube quantitatively at the current candidate constant.

For comparison with the live fixed candidate, account01/B18 fixes
\[
C^\dagger=6.521851214
\]
and `Gamma^dagger` in
`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`.

## 2. New exact theorem: the entire balanced unate five-input center is harmless

### Theorem 2.1

Let `G:{0,1}^5->{-1,+1}` be balanced under the uniform product measure, depend essentially on all five inputs, and be **unate**. Then

\[
\boxed{
\frac{H(G)}{I(G)-1}
\le
R_*:=\frac{44}{5}-\frac95\log_2 3
=5.9470674987019185\ldots<6.
}
\tag{2.1}
\]

Equality is attained, up to input permutation, input complementation and output complementation, by one labeled monotone orbit. A representative monotone truth mask is

`0xeee0eac0`.

For this extremizer the exact spectral data are

\[
\boxed{I=\frac{13}{8}},
\qquad
\boxed{H=\frac{11}{2}-\frac98\log_2 3}.
\tag{2.2}
\]

There are exactly 30 labeled monotone maximizers, and they form one `S_5` permutation orbit of the representative above.

### Proof / finite certificate

A monotone Boolean function on `n+1` variables is exactly a pair `(f_0,f_1)` of monotone functions on `n` variables with `f_0<=f_1` pointwise. Recursing this order relation from `n=0` enumerates **all 7,581 monotone Boolean functions on five variables**, with no heuristic search or NPN sampling.

The checker `check_arity5_unate_tube.py` then:

* keeps the 621 balanced monotone functions;
* keeps the 526 among them for which all five coordinates are essential;
* computes the Walsh transform exactly over integers;
* computes total influence as an exact rational number from squared Walsh coefficients;
* encloses every required `log_2(m)` by rational lower/upper bounds using the positive atanh series
  \[
  \ln x=2\sum_{r\ge0}\frac{y^{2r+1}}{2r+1},\qquad y=\frac{x-1}{x+1},
  \]
  with an explicit geometric tail bound;
* proves for every nonmaximizer the strict inequality
  \[
  R_*[I(G)-1]-H(G)>0;
  \]
* identifies exactly 30 equality spectra, verifies that their truth masks are precisely the permutation orbit of `0xeee0eac0`, and verifies (2.2).

The closest nonmaximizer still has certified slack greater than `0.10845859334434965` in the unnormalised quantity `R_*(I-1)-H`, so the classification is not a floating-point tie.

Finally, a unate gate becomes monotone after complementing some input coordinates and possibly the output. Under the **uniform** product measure these operations only permute cube points and change Fourier signs/labels; they preserve balance, essentiality, squared Fourier masses, `H`, and `I`. Therefore the monotone certificate proves (2.1) for every essential balanced unate five-input gate. QED.

### Consequence for the owner's arity-five falsifier frontier

At uniform bias, a balanced gate can violate the final read-once potential only if `H/(I-1)>6.4573`, and it can challenge the current `C^dagger` center only if `H/(I-1)>6.521851214`. Theorem 2.1 is stronger than both thresholds:

\[
R_*<6<6.4573<C^\dagger.
\]

Hence:

\[
\boxed{\text{any five-input balanced-center falsifier must be non-unate.}}
\tag{2.3}
\]

This is a strict reduction of the untouched arity-five search requested by the owner. It does **not** certify all 616,126 five-input NPN classes, and it does **not** control off-center product biases.

## 3. New analytic sharpening: a C-parametric physical-dictator tube

The account02/B13 source stated a clean coefficient-6 tube. Its same exact inequalities yield a sharper statement at any fixed target `C>2`.

For `0<alpha<=1/2`, write `L=log_2(1/alpha)>2`. Since `m=4alpha(1-alpha)<=4alpha`,

\[
h_2(m)\le m\log_2(e/m)
\]

and `log_2(2^n-1)<n`. From (1.2),

\[
H(g)
\le4\alpha\,[n+L-2+\log_2 e].
\tag{3.1}
\]

Combining this with (1.1) gives

\[
\boxed{
\frac{H(g)}{I(g)-1}
\le
2+2\frac{n+\log_2 e}{L-2}.
}
\tag{3.2}
\]

Therefore, for every `C>2`,

\[
L\ge 2+\frac{2(n+\log_2 e)}{C-2}
\quad\Longrightarrow\quad
H(g)\le C[I(g)-1].
\tag{3.3}
\]

Equivalently, any balanced witness with `H(g)>C[I(g)-1]` must, for **every** original-coordinate signed dictator, satisfy

\[
\boxed{
\Pr[g\ne\sigma\chi_i]
>
2^{-2-2(n+\log_2 e)/(C-2)}.
}
\tag{3.4}
\]

This is still an original-physical-coordinate statement; it does not turn a free affine or character gauge into an invariant operation.

At the current candidate `C=C^dagger=6.521851214`, (3.4) becomes

\[
\boxed{
\Pr[g\ne\sigma\chi_i]
>
2^{-0.4422967287839648\,n-2.638099297218037}.
}
\tag{3.5}
\]

For example:

* `n=10`: the right side is `0.00748871247686863`, i.e. more than `7.6684/1024` cube points. Since a balanced function and a balanced dictator differ in an even number of points, any counterexample must differ on at least **8** points.
* `n=20`: the right side is `0.000349109231512852`, i.e. more than `366.0675` points, hence at least **368** points after the same parity constraint.

This is quantitatively stronger than the earlier convenient `C=6` tube `alpha<=2^{-n/2-3}` when one is testing the actual `C^dagger` candidate.

## 4. Verification artifact and exact output

The committed checker is

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T041709Z-arity5-unate-tube/check_arity5_unate_tube.py`.

A source-equivalent local execution returned:

```
PASS
monotone_total 7581
balanced_monotone 621
essential_balanced_monotone 526
maximizer_count 30
maximizer_permutation_orbit_size 30
representative_mask 0xeee0eac0
Rstar_interval 5.9470674987019185 5.9470674987019185
Rstar_exact 44/5 - (9/5) log2(3)
Hstar_exact 11/2 - (9/8) log2(3)
Istar_exact 13/8
strict_nonmax_gap_lower 0.10845859334434965 mask 0xfeecf000
```

The local executed checker SHA-256 is

`a877b440ecf919eb9015617f552657dd9a87dff43988117dbbac3a60c3d37116`.

The repository also stores `check_arity5_unate_tube.out` with the same certification summary. This finite theorem is a certificate for the stated five-input balanced-unate center only; it is not promoted to a universal FEI proof.

## 5. Relation to the superseded interface-B row route

The older account04/B12 assignment asked for an influence-relative code for robust near-subcube derivative rows. Its key global constraint is retained: account04/B18's mixed-curvature identity is genuine integrability of rows from one Boolean function, and `sum_k d_k` is a second factorial spectral moment that is **not automatically O(J)**. Nothing in this report assumes, weakens, or silently replaces that fact.

The later owner message, however, explicitly instructs every FEI worker to stop opening new routes and converge on the all-gate target. The present arity-five theorem and the C-parametric tube therefore replace another row-local attempt for this invocation rather than being combined with an unpaid `sum d_k` charge.

## 6. What changed and what remains open

**New proved step 1.** The entire essential balanced unate five-input center is excluded as a falsifier by the sharp finite theorem (2.1). The five-input center search can be restricted to non-unate gates.

**New proved step 2.** The current `C^dagger` candidate forces the explicit Hamming separation (3.5) from every original-coordinate signed dictator. This sharpens the account02/B13 coefficient-6 tube at the actual target constant.

**Peer step consumed.** The older AND/decomposable extremality conjecture is already rigorously falsified by account02/B12 using `G10` and the shared-graft family; this run does not claim that as a new result.

**Still missing.** Full FEI is open. The current scalar candidate still requires the all-gate inequality for every genuinely composition-prime gate at every interior bias, or a genuine source-valid counterexample. Within the owner-requested arity-five falsification programme, the remaining center frontier is the non-unate sector; the off-center biased frontier remains broader.

No benchmark gold, email/Drive, paid or remote compute, workflow dispatch, unrelated private data, scheduler mutation, permission change, or notification enabling was used.
