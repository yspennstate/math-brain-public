# account02/B20 release-gate audit and threshold synthesis

Run: `20260924T135824Z-account02-B20-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Role: release gate / independent synthesis / threshold accounting, account02 counterexample emphasis.

## Source pins and scope

Initial invocation control pin: `yspennstate/math-research-brain@f4759cdc5e22625ce5f12cc02295be60cf13e1a4`.  
Invocation-resolved math master: `yspennstate/math-open-problems@fb1c176f3e981f3e59465f58ce0d0c817e54244d`; final prepublication master refresh advanced to `80d86eedac01aafbf61b34446b6eed696ca75dce` through concurrent immutable worker additions.  
Pinned baseline manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
The 790-line manuscript is unchanged byte-for-byte on the refreshed master.

I read the full manuscript, `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md`. I also independently reconstructed the post-baseline nine-direction replacement and inspected the latest compatible multiplicity-eight collar / exact-zero two-anchor work. Peer labels are not used as premises below.

## Release-gate verdict

**Pinned 17-eigenvalue baseline: PASS.** I found no mathematical defect in the theorem as stated. The proof is valid for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine terms, and `s_17(A)>=s>0`; it proves the essential density bound `10000 K^2/s`. It does not prove the unrestricted three-eigenvalue conjecture.

**Threshold reduction: PASS at multiplicity 9, with a complete replacement argument.** Independent reconstruction below gives the stronger theorem

` s_9(A)>=s>0  =>  ||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s.`

**Multiplicity 8: GAP / UNPROVED.** The no-pivot branch is reduced to a quantitative overlap-one / two-sided collar, and an exact-zero two-anchor subcase is paid, but no dependence-safe aggregate collar receiver currently closes the general branch. I do not claim eight, and do not claim unrestricted three.

## Complete line-range audit of `manuscript.tex`

The ranges below cover every source line 1--790 with no logical section omitted. `PASS` means I rederived the displayed identity/inequality and checked the quantifiers used downstream. `UNCHECKED` is reserved below only for historical finite-test counts outside the symbolic proof, not for manuscript mathematics.

| Lines | Status | Audit reasoning / downstream impact |
|---|---|---|
| 1--46 | PASS | Preamble, notation, abstract and scope agree with the proved normalized/scaled theorem. No hidden regularity, moment, support, sign, or post-rotation independence assumption appears. |
| 47--61 | PASS | Main theorem and 33-corollary quantifiers are correct. `s_17(A)>=s` scales exactly under `A/s`; `s_17>=s_33` is the stated stronger-hypothesis implication. |
| 62--90 | PASS | Parameters `eta=1/100`, `kappa=80^-2`, pivot definition and 9/17 architecture are consistent with later counts. Continuity is explicitly separated from essential boundedness. |
| 91--121 | PASS | Fourier convention `hat f(t)=int e^{itx}f(x) dx`, Plancherel factor `2pi`, inversion factor `1/(2pi)`, Gaussian `g_epsilon` and rough-law regularization are consistent. Weak convergence plus uniform Fourier convergence gives the asserted density without assuming a priori continuity of the law. |
| 122--131 | PASS | Power-envelope integral is `2ap/(p-1)`, hence density cap `ap/[pi(p-1)]`. |
| 132--160 | PASS | Riesz/Gamma representation and Gaussian inversion give coefficient `1/sqrt(2pi)`. The `3/4` envelope weighted integral is exactly `12 sqrt(u)`. Extended values/atoms are handled by Tonelli. |
| 161--181 | PASS | Singular-value perturbation and rank-shift statements are used on possibly nonsymmetric auxiliary matrices, correctly in singular values rather than eigenvalues. |
| 183--207 | PASS | Schur count is correct. In the invertible case, positive/negative compression of `A^{-1}` gives the strict-complement count; in the singular ambient case, `s_j(S_epsilon)` continuity plus threshold `t-|epsilon|` is sufficient. A shorter rank-only proof is also valid: `A=UBU^T+diag(0,S)` with rank first term `<=k`, hence `s_{j+k}(A)<=s_j(S)`. No fixed-threshold loss occurs. |
| 208--220 | PASS | Strict row diagonal dominance and section transition are standard and used with strict numerical slack later. |
| 221--255 | PASS | Geometric rank-one Brascamp--Lieb heat-flow proof has the correct sign: `partial_t F-Delta F>=0`, so the integral is nondecreasing toward the product-mass Gaussian limit. Compact-support heat tails justify integration by parts; monotone truncation handles rough inputs. |
| 256--282 | PASS | Product-projection density proof uses only an orthogonal deterministic coordinate completion and BL integration. It does not assert independence after rotation. `-b log b<=1-b` yields `e^{d/2}` exactly. |
| 283--301 | PASS | Scalar Fourier-power estimate correctly uses `m=floor(p/2)>=p/4`, Fourier inversion at zero for the continuous convolution density, and the product-projection cap. Difference density remains `<=1`. |
| 302--324 | PASS | Cross-form setup and two/four-power decoupling duplicate literal independent coordinates only. Pure same-bank phases cancel under modulus; no conditional recapping shortcut is used. |
| 325--373 | PASS | Regularized determinant/graph proof: `alpha=(2pi e)^2`; frame weights lie in `[0,1]`; trace identity matches; BL/scalar-Fourier constants cancel to exponent `-1/8`. The determinant is on the physical cross matrix and no marginal volume gate is introduced. |
| 374--403 | PASS | `Z_k=e_k(M^TM)` is the ordered physical crossing volume. Retaining the order-`k` determinant term yields `u_k=pi e Z_k^{-1/(2k)}`. Order 5 gives integrable exponent `5/4`; order 3 is used only with the Riesz weight, not by direct inversion. |
| 404--422 | PASS | Scalar square inverse-branch domination has the correct `|a|^-1/2 |z-v|^-1/2` profile and is valid for rough cap-one inputs as a measure domination statement. |
| 423--436 | PASS | Definite 2D quadratic coarea/area estimate gives `pi/sqrt(D)` uniformly in affine shifts. No support or smoothness hypothesis is added. |
| 437--482 | PASS | Indefinite hyperbolic envelope: determinant normalization, branch parameterization, Jacobian, compact-middle length and two tail integrals give the stated `D^-1/2(6+log_+(16 sqrt(D)/|z-v|))` envelope. Constants have positive slack. |
| 483--525 | PASS | Quarter-power concentration: diagonal branch gives square-root small ball and hence the weaker quarter power; off-diagonal branch uses sign symmetrization only on coefficients, not an independence claim. The determinant Fourier bound gives `|t|^-1/4`; Gaussian optimization yields the stated universal 16. Log-potential layer cake is valid when `||S||>=1`. |
| 526--544 | PASS | Pivot/no-pivot and `V_r` definitions are coherent. Absence of a principal determinant pivot gives the physical entry bound `|a_ij|<sqrt(eta^2+eta)<1/7`. |
| 545--564 | PASS | Determinant-squared seed sampling uses only nonsingular disjoint seeds. The nonsymmetric interpolant `P=A[:,T] B^-1 A[S,:]` has rank `<=r`, agrees on seed rows/columns, and the bordered-minor identity yields the expected Frobenius error bound with multiplicity at most `(r+1)^2`. Singular extensions only make the global inequality one-sided, which is sufficient. |
| 565--580 | PASS | Completion support was checked entrywise. `D` vanishes on `S union T`; `E` has zero diagonal; `R-P` is supported in rows `T` or columns `S`, giving global `rank R<=3r`; on `LxL`, exactly `R=P`, so restricted rank `<=r`. The distinction global `3r` versus restricted `r` is essential and correctly retained. |
| 581--619 | PASS | Spectral-to-volume proposition is correct for `k<=5`. If `V_{r+1}/V_r<kappa`, then `epsilon<=(r+1)/80<=1/16`. With `m=4k-3>=4r+1`, rank shift forces `r+1` large entries of diagonal `D` outside the seed. There `|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`; for `r<=4`, row sum `<23/28<371/400`, contradicting restricted rank. The `r=0` operator-norm contradiction is also valid. |
| 620--630 | PASS | Fair physical coordinate cut has expectation `4^-k V_k`; ordered disjoint pairs are counted with exactly probability `2^-2k`. |
| 631--645 | PASS | No-pivot consequences use order 3 for full half-potential and order 5 for density with the correct scaling `Z_k^-1/(2k)<=160`. |
| 646--674 | PASS | Truncated half-potential definition is explicit. The two kernel estimates are valid; in the log kernel, centered intervals maximize overlap and Tonelli gives the uniform 8. |
| 675--714 | PASS | Pivot truncated-half-potential proposition is valid in scalar, definite-pair and indefinite-pair cases. Full versus truncated quantities are not conflated. The scalar branch actually gives the sharper bound `H<=200+120 log 16<533`, although the proposition records `<=600`. |
| 715--724 | PASS | `s_9>=1` half-potential proposition correctly splits pivot/no-pivot and turns truncated `H<=600` into full half potential `<=601` by bounding the outside kernel by one. |
| 725--749 | PASS | Main normalized proof: no-pivot uses 17/order5; scalar pivot loses one Schur direction and invokes the 9-direction half-potential; definite pair is direct; indefinite pair loses two directions and needs only nonzero Schur norm. All conditional bounds are integrated by Tonelli, avoiding exceptional-slice assumptions. |
| 750--790 | PASS | Scaling `Y=KX` is exact: `Q=(s/K^2) Qtilde`, giving `K^2/s`. Threshold-accounting and limitations accurately state that 17 is not optimal and three is not proved. Bibliographic citations are attribution only; specialized inputs used in the proof are reproved. |

## Requested sensitive-point audit

### Nonsymmetric interpolation support — PASS

The interpolation is deliberately nonsymmetric. The random quadratic form is never replaced by `R` or `E`; they are deterministic algebraic auxiliaries. Since singular values, Frobenius norm and rank are valid for nonsymmetric matrices, no symmetry is required in the perturbation/rank step. Entry support gives

`R-P = (rows supported on T) + (remaining columns supported on S)`,

so the two support pieces have ranks at most `r` each.

### Global `rank<=3r` versus restricted `rank<=r` — PASS and sharp mechanism

The global count is `rank P + r + r <=3r`; the complement block is exactly `P[L,L]`, rank `<=r`. The spectral-to-volume contradiction uses the global count only to force large diagonal entries and the restricted count only after those entries are known to lie in `L`. Replacing both by one rank estimate would lose the 17 threshold. The abstract data are saturated at multiplicity eight (`r=2`), so the present rank mechanism alone cannot prove order-three volume from `s_8`.

### `D` vanishing on the seed — PASS

`D_ii=0` on `S union T` by definition. This is what forces all large diagonal coordinates selected in the volume proof into `L`, where the sharper rank bound applies.

### Spectral-to-volume conversion — PASS

The only delicate endpoint is strictness: a failed target volume yields one ratio `<kappa`; therefore the selected completion has the strict enough error bound. All subsequent dominance inequalities have positive slack. No equality case is silently discarded.

### Fourier normalization — PASS

Every Fourier constant is consistent with `hat f(t)=int e^{itx} f(x)dx`: Plancherel `2pi`, inversion `1/(2pi)`, Gaussian multiplier `e^{-epsilon t^2}`, Riesz coefficient `1/sqrt(2pi)`, and the determinant regularizer `alpha=(2pi e)^2`.

### Heat-flow / rough-law limits — PASS

The BL proof is first established for bounded compact support, where Gaussian tails control all derivatives. Large-time scaling has an integrable Gaussian dominator; small-time passage uses Lebesgue points plus Fatou. General nonnegative integrable inputs are monotone truncations. Later density statements for rough laws are obtained either by Fourier regularization or domination of measures; smoothness is not imported.

### Schur counts — PASS

The original moving-threshold singular-ambient proof is valid. For release robustness I recommend the dependency-closed rank-only replacement

`A = U B U^T + diag(0,S),  rank(UBU^T)<=k`,

which immediately gives `s_{j+k}(A)<=s_j(S)` and hence `N_S(t)>=N_A(t)-k` without inverse or limiting language.

### Full versus truncated half-potentials — PASS

`H(Q)` is truncated at distance one. The pivot proposition proves only this truncated bound. Proposition 9 explicitly adds at most one from the complement and obtains the full half-potential. The no-pivot order-three route already bounds the full half-potential. The main scalar-pivot profile uses only the full quantity after this conversion.

## `verify.py`, `checks.json`, and self-audit metadata

`verify.py` is correctly pinned to the baseline SHA-256 and checks exact diagonal-dominance arithmetic, exact nonsymmetric interpolation/bordered identities and aggregate sampling on finite matrices, plus numerical Schur and graph-weight diagnostics. The committed `checks.json` reports PASS with 534 exact interpolation seeds, 18 volume cases, 240 Schur threshold cases, 30 graph-weight cases, and exact dominance slack `297/2800`. These finite checks are consistent with the symbolic proof but are not treated as a proof certificate.

`AUDIT.md` records older historical finite-test counts (504, 10, 192, 800, 1040, 160). Those historical runs are **UNCHECKED** in this invocation because the delivery checker explicitly says it is a new scoped suite and does not reproduce them. This is a reproducibility/presentation distinction only; no theorem step depends on those historical counts.

## Complete multiplicity-nine replacement — PASS

I independently reconstructed the grouped physical-product Fourier compiler rather than accepting a peer verdict.

Let literal original-coordinate banks `H,I,J` be disjoint. Promote a `k`-dimensional orthogonal projection `W` of `X_H` with density cap `M_H`; let the `J` restriction of the promoted coefficient matrix have full row rank with singular-value product `S`. Orthogonally project the remaining physical `I-J` crossing rows away from that promoted row space, obtaining `C`. For determinant weights on `ell`-row Gram minors, with inclusion marginals `alpha_i<=1/2`, the exact weighted Holder decomposition is

`prod_i |psi_i| = prod_T (prod_{i in T}|psi_i|^(1/alpha_i))^(w_T)`.

The joint linear image of the literal difference bank has Gram determinant

`S^2 det(C_T C_T^T)`.

The product-projection theorem, the scalar Fourier-power estimate at `p=1/alpha_i`, and the entropy inequality

`H(w)+sum_i alpha_i log alpha_i <= ell log ell - log(ell!)`

therefore give

`|phi_Q(t)| <= min(1, K_{k,ell}|t|^{-(k+ell)/2})`,

where

`K_{k,ell}=M_H^(1/2) pi^((k+ell)/2) 2^(ell/4) e^((k+2ell)/4)
 (ell^ell/ell!)^(1/4) S^-1/2 Z_ell^-1/4`.

The key dependence check is sound: one first conditions on the literal `I` bank, duplicates only literal `J`, and then averages the original independent `I` coordinates. Same-bank phases cancel in modulus; no conditional projected-density cap is inferred from an unconditional marginal.

Promotion of any physical row carrying more than half of the current exterior-volume mass terminates after at most three rows. Gram--Schmidt gives exact incident-mass identities, so one obtains the marginal-free receivers

`||p_Q||_infinity <= C3 E3(M)^-1/6`,

`C3 = 3 sqrt(2) e (9/2)^(1/6) = 14.818337662843...`,

and

`sup_a E|Q-a|^-1/2 <= C2 E2(M)^-1/8`,

`C2 = 8 sqrt(e) 2^-1/8 = 12.095072570796...`.

Now normalize `K=s=1` and assume `s_9(A)>=1`.

* no pivot: baseline order-three spectral-to-volume gives `V3>=kappa^3`; a fair physical cut has `E3>=4^-3 kappa^3`, hence `E3^-1/6<=160` and `||p||_infinity<=160 C3=2370.934026...`;
* scalar pivot: the Schur complement retains 8 directions. If it has a pivot, the *proved sharper value inside* baseline Proposition pivot-H is `H<=200+120 log16`; adding the tail gives full half-potential `<=201+120 log16`. If it has no pivot, `s_5>=1`, order-two spectral-to-volume plus a fair cut and the new `E2` receiver give `<153`. The outer square profile therefore gives

`||p||_infinity <= 10(201+120 log16) = 2010+1200 log16 = 5337.106466687737... <5338`;
* definite pair pivot: `10pi<32`;
* indefinite pair pivot: seven Schur directions remain, so the existing quarter/log argument gives `<251`.

Scaling back yields the complete theorem

**`s_9(A)>=s>0 => ||p_Q||_infinity < 5338 K^2/s`.**

Dependency map closes as

`BL -> product projection + scalar Fourier powers -> grouped compiler -> E3 density / E2 half-potential`

and

`sampling + completion + rank + dominance -> spectral-to-volume -> random cut`,

with the pivot lemmas and Schur count closing the other branches. No lower-threshold lemma is assumed.

## Multiplicity-eight frontier — structural PASS, analytic GAP

I independently checked the current no-pivot `s_8` reduction. If `V3>=kappa^3`, the nine-proof E3 receiver already closes the law. Otherwise the sharp interpolation argument forces

`V2>=kappa^2`,

`Omega1 >= c_*^2 kappa^2`,

`Xi2 >= (delta_*^2/2) kappa^2`,

where

`epsilon_* = sqrt(18 kappa)=3 sqrt(2)/80`,
`c_*=1-epsilon_*`,
`delta_*=0.854335140191...>0`.

The proof is correct: Markov retains half the determinant-squared seed mass with `||E||_F^2<=18kappa`; rank six plus `s_8>=1` forces two large diagonal residual coordinates; their bordered minors give `Omega1`, while `P_HH=A[H,T]B^-1A[S,H]` and strict diagonal dominance give the two-sided product currency `Xi2`.

The obvious disjoint third minors are *small*, not large:

`det A[S union {h1}, T union {h2}] = det(B) E_{h1 h2}`,

and similarly with `h1,h2` reversed. Hence the collar is genuinely overlapping and cannot be repackaged as hidden disjoint E3 by the same seed.

The latest exact-zero two-anchor receiver is also correct. If a literal pair `H` has `A[H,H]=0` and outside cross map `C` of row rank two, then conditioning on the complement makes `X_H` purely affine. With `G=CC^T`, product projection gives the slope vector density cap `e/sqrt(det G)`, and the exact two-dimensional inverse-radius split gives

`||p_Q||_infinity <= e sqrt(2pi) det(G)^-1/4`.

This pays an important exact-zero local subcase but not the aggregate collar.

### New account02 counterexample/obstruction: bounded induced anchor curvature does not control the bilateral shear

A tempting next shortcut is: once the bilateral shear creates a uniformly nonsingular two-dimensional anchor quadratic, the translations of the two outer product banks should be uniformly controlled. This is false even in a clean no-pivot local packet.

For `0<epsilon<10^-2`, take three two-coordinate banks `S,H,T` and set

`B=A[S,T]=epsilon I_2`,
`C=A[S,H]=sqrt(epsilon) I_2`,
`D=A[H,T]=sqrt(epsilon) I_2`,
`A[H,H]=0`,

with the other local diagonal blocks zero. Then every physical diagonal is zero and every local principal two-coordinate determinant has modulus at most `epsilon<eta`, so this packet is in the no-pivot scale. Yet

`P = D B^-1 C = I_2`,

so the bilateral-shear induced anchor matrix is exactly

`K=A[H,H]-(P+P^T)=-2 I_2`,

with `|det K|=4`, uniformly separated from zero. At the same time

`||B^-1 C|| = ||B^-T D^T|| = epsilon^-1/2 -> infinity`.

Thus neither the collar relation nor a fixed nonsingular induced `K` controls the shear translations. Any multiplicity-eight receiver whose proof needs a dimension-free bound on those translation matrices is invalid. This does **not** refute the eight-eigenvalue density theorem; it rules out that proof shortcut and reinforces that the shifted product masks must be retained exactly or averaged before reciprocal local payment.

## First unpaid implication

The current first universal debt is therefore:

**`QFORM-EIGHT-AGGREGATE-MASKED-COLLAR-RECEIVER`** — under the full independent cap-one product hypotheses, no `eta` pivot, `s_8(A)>=1`, failed disjoint E3 exit, and the quantitative aggregate `Omega1/Xi2` collar above, prove a dimension-free essential density bound while retaining arbitrary same-bank curvature, arbitrarily ill-conditioned determinant-sampled seeds, and the literal shifted product masks; or give a valid counterexample.

A local exact-zero pair is paid. A proof may not select one tiny collar and pay its reciprocal, may not bound the bilateral shear by its induced anchor determinant, may not rotate the source and declare independence, and may not turn the order-two Fourier endpoint into an L-infinity bound by generic interpolation.

## Release accounting

- Baseline 17 theorem: `PASS` in this complete independent review.
- Nine-direction replacement: `PASS` in this complete independent reconstruction, constant `<5338 K^2/s`.
- Eight-direction structural collar: `PASS`.
- Exact-zero two-anchor subreceiver: `PASS`.
- General eight-direction aggregate/masked collar receiver: `GAP`.
- Unrestricted three-eigenvalue QFORM: `OPEN`, not claimed solved.
- Global continuity: separate; no-pivot E3 branches are `C_0`, mixed pivot/collar branches are only essential-density statements unless separately proved.

No manuscript source was overwritten. This audit/improvement is immutable supporting material for owner synthesis; independent-validation status still requires the owner-defined two genuinely separate complete reviews of the exact candidate being promoted.
