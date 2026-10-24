# account02 / B18 complete fixed-multiplicity audit — r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Pins and scope

The mathematical source audited end to end is the immutable 790-line `manuscript.tex` with baseline commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, and SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`. During this run master advanced because other workers added audit/support artifacts; at the last pre-write package refresh it was `1b6a5a125347f5d07c79332ac9ab535d106de5fa`, and `manuscript.tex` still had the same git blob. The support package read in full comprised README, SOURCE_MANIFEST (once it appeared on master), AUDIT, proof_map, verify.py and checks.json. The line-by-line ledger in this run covers every source line 1--790 without gaps.

This review is one worker's independent mathematical audit. It is not formal verification, not a release certificate, and not a claim that the unrestricted three-large-eigenvalue QFORM conjecture is solved.

## Verdict

**Mathematical baseline: PASS.** I found no fatal mathematical gap and no FALSE manuscript statement in the pinned 17-eigenvalue proof. I independently checked the theorem quantifiers and scaling, every displayed analytic identity used downstream, every lemma invocation and hypothesis, the nonsymmetric interpolation, both rank bounds, the spectral-to-volume conversion, the Fourier constants, the pivot kernels, Schur counts including the singular case, and the distinction between full and truncated half potentials.

**Package reproducibility: GAP, nonfatal to the proof.** `AUDIT.md` records a historical self-audit suite with counts such as 504 interpolation seeds, 800 Schur cases, 1040 nonsymmetric perturbation cases and 160 graph cases. The current `verify.py` explicitly says it is a new delivery-reproducibility suite that does not reproduce the unavailable original suite, and current `checks.json` records 534 interpolation seeds, 18 volume cases, 240 Schur threshold cases and 30 graph cases. The later SOURCE_MANIFEST correctly acknowledges this distinction. Repair: retain the historical counts only as an authoring-agent report and label the current `verify.py/checks.json` as a distinct executed suite wherever the package is summarized. Impact: provenance/reproducibility only; none of those finite tests is used as a proof premise.

**UNCHECKED in this run:** the compiled-PDF binary/hash and claimed visual inspection, because the binary is not stored in the GitHub package; exhaustive novelty/priority across the literature; and reproduction of the historical finite-test suite. These are not dependencies of the written mathematical proof. Search misses are not treated as novelty evidence.

## End-to-end proof audit

The theorem statement at lines 47--57 is correctly normalized: independent real coordinates have arbitrary densities bounded by `K`, `A` is arbitrary real symmetric, `b,c` are arbitrary, and `s_17(A)>=s>0`; the claimed bound scales as `K^2/s`. The final scaling at lines 726--749 is exact: for `Y=KX`, the manuscript's `tilde Q` equals `(K^2/s)Q`, so the normalized density bound rescales to `10000 K^2/s`. The 33-eigenvalue corollary is immediate from monotonicity of singular values.

The Fourier preliminaries pass with the stated convention. Plancherel carries factor `2 pi`, inversion carries `1/(2 pi)`, the Gaussian inversion formula is normalized correctly, and the negative-half-moment identity gives the coefficient `1/sqrt(2 pi)`. The power envelope integrates to `2ap/(p-1)`. For the `3/4` envelope the weighted integral is exactly `12 sqrt(u)`. These constants propagate consistently.

The geometric rank-one Brascamp--Lieb proof is self-contained. The heat-flow derivative is
`F[sum c_i v_i^2 - |sum c_i u_i v_i|^2] >= 0` by the frame identity; compact-support Gaussian tails justify the integrations by parts, the large-time limit has the correct Gaussian normalization because `sum c_i=d`, and Fatou plus monotone truncation handles general nonnegative integrable inputs. The product-projection lemma then uses a deterministic orthogonal change of variables only; it never asserts independence after rotation. Its entropy estimate gives `exp(d/2)`. The scalar Fourier-power lemma follows from Plancherel, an integrable even power, Fourier inversion at zero, and that internally proved projection bound.

The decoupling and regularized determinant theorem pass. Copies are introduced only on the original product bank. The difference coordinates remain independent and have density cap one. For `H=alpha I+a^2M^TM`, `alpha=(2 pi e)^2`, the frame weights satisfy the trace identity; all one-dimensional scaling factors in the Brascamp--Lieb application are correct. The `d_i` powers cancel against the scalar Fourier bound and the `c_j` entropy factor contributes exactly the extra `e^(theta/2)` needed to make `(2 pi e/sqrt(alpha))^theta=1`. Taking fourth roots gives
`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2 e^2))^(-1/8)`.
Cauchy--Binet then yields the crossing-volume envelopes. At order five the exponent is `5/4>1` and direct inversion gives `5e Z_5^(-1/10)`; at order three the exponent is only `3/4`, and the proof correctly uses the extra `|t|^-1/2` Riesz weight rather than claiming direct density inversion.

The coordinate-pivot section also passes. The scalar-square profile is a measure-domination statement after conditioning, not an independence assertion. The definite-pair proof needs only a joint density cap. In the hyperbolic pair proof, orthogonal eigenvectors are used to parameterize a deterministic level set while the product density is still evaluated in the original coordinates. The tail estimate chooses an original coordinate with a large component and uses only its cap and total mass. The exact near-region and logarithmic constants are valid. The quarter-power lemma's random-sign cut is an original-coordinate cut; the determinant bound supplies the `1/4` Fourier decay and Gaussian smoothing gives coefficient approximately `3.995259362<16`, so the stated `16` is safe.

The algebraic skeleton is the most sensitive part and passes. In volume-sampled interpolation, the bordered determinant identity is exact and sorted-row/column signs disappear after squaring. Singular seeds can have nonsingular extensions, so the manuscript correctly states an inequality, not an equality. For the chosen seed,
`P=A[:,T] A[S,T]^{-1} A[S,:]` has rank at most `r`, exactly interpolates rows `S` and columns `T`, and need not be symmetric. In the completion `A=D+R+E`, `D` vanishes on `S union T`, `E` is zero-diagonal, `R_LL=P_LL` has rank at most `r`, while globally `R-P` is supported in rows `T` or columns `S`, giving the separate global bound `rank R<=3r`. Those two ranks are both genuinely used and are not interchangeable.

The no-pivot spectral-to-volume proposition then closes correctly. A small volume ratio gives `||E||_F<=1/16`; singular-value perturbation plus `rank R<=3r` forces at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon`, and because `D` vanishes on the seed those entries lie in `L`. On an `(r+1)`-set in `L`, the diagonal lower bound `371/400` exceeds the worst row sum `4(1/7+1/16)=23/28`. Strict diagonal dominance makes `R_HH` rank `r+1`, contradicting `rank R_LL<=r`. The random-cut expectation is exactly `4^-k`. Therefore `s_9` in the no-pivot case gives full half-potential `12 sqrt(80e)=176.959336...<200`, and `s_17` gives density `800e=2174.625463...<2400`.

The final pivot chain passes. The two elementary kernels have near-region constant `2 asinh(sqrt 2)+pi+2 arcosh(sqrt 2)=7.196771497...<8` and log-kernel bound 8. A scalar pivot under two surviving eigenvalues gives truncated half-potential below 600; definite and indefinite two-coordinate pivots are smaller. Proposition `prop:nine` correctly upgrades the no-pivot full half-potential or pivot truncated half-potential to a global `<=601` half-potential by bounding the outside kernel by one. In the main theorem the scalar pivot removes one coordinate and leaves at least 16 large eigenvalues, hence enough for `prop:nine`; a two-coordinate pivot leaves at least 15. The largest final branch is the scalar one, `6010<10000`.

## Counterexample/adversarial checks

A useful counterexample to an invalid simplification confirms why the interpolation must remain nonsymmetric. Let

```
A = [[0,1,2,0],
     [1,0,0,3],
     [2,0,0,0],
     [0,3,0,0]],
S={1}, T={2}   (1-based).
```

Then `B=A[S,T]=1` and

```
P=A[:,T] B^{-1} A[S,:]
 = [[0,1,2,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,3,6,0]].
```

`rank(P)=1`, and P exactly matches row S and column T as required. But `(P+P^T)/2` has rank 2, its row S is `[0,1/2,1,0]`, and its column T is `[1/2,0,0,3/2]^T`; symmetrization destroys both exact interpolation identities and the rank budget. Thus any audit or proposed repair that silently symmetrizes P is false.

A second obstruction concerns lowering the multiplicity by merely changing `k=5` to `k=4`. The same structural argument would make 13 directions (`4*4-3`) force fourth crossing volume, but the determinant envelope would have exponent exactly `k/4=1`: `min(1,u/|t|)`, whose L1 tail diverges. This is a proof-route obstruction, not a counterexample to a 13-eigenvalue theorem. It means the present direct Fourier-inversion dependency map cannot lower 17 without an additional analytic input.

## Primary-source verification

The manuscript cites only Bennett--Carbery--Christ--Tao (BCCT) and Rudelson--Vershynin (RV), and explicitly says they are classical antecedents while the constants needed here are proved internally. That description is source-matched.

* RV, arXiv:1402.4492, Theorem 1.1 assumes independent real-valued coordinates with densities bounded by `K` almost everywhere and gives an `O(1)^d K^d` bound for every d-dimensional orthogonal projection. Its Theorem 1.2 gives the sharp `sqrt(2) K` bound for a normalized scalar linear combination. Thus the manuscript's broad product-projection attribution is correct. RV does **not** supply the manuscript's exact `e^(d/2)` constant; that exact constant is proved inside lines 258--282, so no source hypothesis/constant is being smuggled in.
* BCCT, arXiv:math/0505065, is indeed a Brascamp--Lieb paper and explicitly describes techniques partly based on monotonicity formulas for positive solutions to heat equations. This matches the stated antecedent for the manuscript's heat-flow proof. Again, the specialized rank-one inequality and constant one are proved directly at lines 221--255, so BCCT is not an unproved dependency.

I found no external theorem whose hypotheses or constant are silently imported into the 17-eigenvalue proof.

## Package-file audit

`README.md`: **PASS** as a description of the candidate, source pins, scope and limitations. `SOURCE_MANIFEST.json`: **PASS** for the immutable manuscript hash/blob and for its explicit warning that the current reproducibility suite differs from the historical self-audit; the PDF-binary assertions are **UNCHECKED** here. `AUDIT.md`: **GAP** only in reproducibility presentation because its historical finite-test counts are not reproduced by the current suite; its mathematical summary is consistent with the source. `proof_map.csv`: **PASS**; its labeled statement/proof ranges agree with the manuscript and were used only as a navigation aid, not as a substitute for reading. `verify.py`: **PASS** on static inspection; it pins the correct source hash, tests the sensitive nonsymmetric interpolation/rank identities and labels itself non-certifying. `checks.json`: **PASS** for consistency with the current `verify.py` schema and pinned source; this B18 run did not re-execute the exact repository script, so independent dynamic execution of that file is **UNCHECKED**, while the proof constants and principal exact identities above were independently recomputed.

## Threshold decision and next obligation

I do **not** reduce 17 in this run. The owner requires a complete replacement proof, constants and dependency map before lowering the theorem, and I do not have such a closed argument. The cleanest exact next obligation exposed by this audit is the order-four endpoint: either prove an additional source-valid estimate that upgrades the borderline `|t|^-1` fourth-volume envelope to an integrable bound for the full arbitrary-affine rough-law class, or improve the structural argument so fewer spectral directions still force an order-five analytic currency. Until one of those is proved end to end, the audited threshold remains 17.
