SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T19:03:53Z.
attacking: rough-input regularity at the newest Fisher-information/mixture frontier; isolate the first unpaid implication and test whether any source-valid cap-one approximation can preserve the needed quantitative output height without continuity.

# fleet02/B15 auto11 — universal Fisher-approximation cost, mixture cost, and a rough ruled witness

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T190353Z-fleet02-B15-qform-auto11`  
Status: **PROVED REGULARITY-CLOSURE OBSTRUCTION / RULED ROUGH BRIDGE CHECKED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The full owner target is still

`sup ||p_(X^T A X)||_infinity < infinity`

over all dimensions, all independent cap-one marginals, and all symmetric `A` with at least three eigenvalues of modulus at least one.

The new projected-Fisher theorem at

`math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`,
`proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`

proves, under `sqrt(f_i) in H^1`,

`||p_Q||_infinity <= (r-1) J_E / [2 s (r-2)^2]`,

where `J_E=sum_i ell_i I(f_i)`, and under the cap improves this to

`||p_Q||_infinity <= [r d_E + sqrt(J_E d_E)]/(4s)`,
`d_E=min(D_r,J_E/(r-2)^2)`.

The first unpaid regularity implication is therefore not continuity of the rough output. It is whether arbitrary cap-one laws can be reached from this regular class with a **uniform projected-information budget**, or whether one can replace the absolute Fisher estimate of the signed score term by a cap/product cancellation estimate. The first possibility is ruled out below in a way that is uniform over *all* H1 approximants, not only Gaussian mollification.

## 2. Quantitative theorem: every H1 approximation of a unit interval pays diverging Fisher information

Let

`u=1_[0,1]`.

Let `f` be any probability density with `sqrt(f) in H^1(R)`, set

`eta=||f-u||_1`,
`I(f)=4 ||(sqrt f)'||_2^2`.

### Theorem 2.1 — `QFORM-FISHER-ROUGH-CLOSURE-COST-v1`

If `0<eta<=1/8`, then

`boxed( I(f) >= 1/(4 eta) )`.                                 (2.1)

No density-cap assumption is needed.

### Proof

Put `g=sqrt(f)` and `v=1_[0,1]`. The elementary inequality

`(sqrt(a)-sqrt(b))^2 <= |a-b|`

implies

`||g-v||_2 <= sqrt(eta)`.                                     (2.2)

For every `0<h<=1`, the shifted unit interval has

`||v(.+h)-v||_2^2=2h`,

hence

`||g(.+h)-g||_2`
` >= ||v(.+h)-v||_2-||g(.+h)-v(.+h)||_2-||g-v||_2`
` >= sqrt(2h)-2 sqrt(eta)`.                                  (2.3)

On the other hand the standard H1 translation estimate gives

`||g(.+h)-g||_2 <= h ||g'||_2 = h sqrt(I(f))/2`.               (2.4)

Set `h=8 eta`, which is at most one. Then the right side of (2.3) is

`sqrt(16 eta)-2 sqrt(eta)=2 sqrt(eta)`.

Together with (2.4),

`4 eta sqrt(I(f)) >= 2 sqrt(eta)`,

which is exactly (2.1). Among substitutions `h=k eta` in this argument, `k=8` optimizes the resulting constant. QED.

This strictly strengthens the smoothing warning in the Fisher source: it is not merely that one particular cap-preserving Gaussian mollifier has `I(f_delta)->infinity`; **every** H1 approximation in L1 to the interval density has information at least of order `eta^-1`.

## 3. Cap-one weak separation for every fixed Fisher budget

Now assume also `0<=f<=1`. Let

`m=1-int_0^1 f(x) dx = P_f(R\[0,1])`.

Because `f<=1`, the deficit inside `[0,1]` equals the mass outside, so

`||f-u||_1=2m`.                                                (3.1)

If `m<=1/16`, Theorem 2.1 gives

`I(f)>=1/(8m)`.

If `m>1/16`, there is already fixed separation. Therefore every cap-one Fisher-regular probability density satisfies

`boxed( m >= min(1/16, 1/(8 I(f))) )`.                        (3.2)

Consequently, if `I(f)<=J<infinity`,

`boxed( P_f([0,1]) <= 1-min(1/16,1/(8J)) )`.                  (3.3)

Thus a cap-one class with a common finite Fisher budget is not weakly dense at `Uniform[0,1]`. This is a genuine weak-topology obstruction: `[0,1]` is a continuity set of the limiting uniform law, while (3.3) leaves a fixed mass gap for every fixed `J`.

There is also a cap-free qualitative version. If `f_n=>u` weakly and `sup I(f_n)<infinity`, then `g_n=sqrt(f_n)` is bounded in `H^1`. Weak convergence makes the probabilities tight, hence the `L2` masses of `g_n` tight. Rellich compactness on bounded intervals plus tightness gives a subsequence converging strongly in `L2(R)` to some `g in H^1`. Then `f_n=g_n^2 -> g^2` in `L1`, so the weak limit forces `g^2=u`, i.e. `g=1_[0,1]` a.e., impossible because that indicator is not in `H^1`. Hence even without the cap, a uniform Fisher budget cannot converge weakly to the interval law.

## 4. Product/projected-information separation on an exact normalized QFORM target

Take

`A = [[0,1,0],[1,0,0],[0,0,1]]`,                             (4.1)

so

`Q=2X_1X_2+X_3^2`,

and the spectrum is exactly `{1,-1,1}`. This is an exact normalized three-large-eigenvalue target. Since the chosen three-dimensional spectral space is all of `R^3`, its leverage diagonal is `(1,1,1)` and

`J_E=I(f_1)+I(f_2)+I(f_3)`.                                  (4.2)

Let `F=prod_i f_i` be any Fisher-regular product density and let `U_3=u^tensor3`. If

`eta=||F-U_3||_1<=1/8`,

then marginalization contracts L1, so `||f_i-u||_1<=eta`. Theorem 2.1 therefore yields

`boxed( J_E >= 3/(4 eta) )`.                                  (4.3)

Hence **no L1 approximation of the cube source can retain a bounded projected-information certificate**, even though the matrix and its three large eigenvalues are fixed perfectly.

For cap-one products there is also a direct weak separation at fixed projected-information budget. If `J_E<=J`, some coordinate has `I(f_i)<=J/3`; by (3.2),

`P(f_i in [0,1]) <= 1-c_J`,

where

`c_J=min(1/16,3/(8J))`.                                      (4.4)

Therefore

`boxed( P_F([0,1]^3) <= 1-c_J )`.                             (4.5)

So the class of cap-one product inputs with `J_E<=J` is not weakly dense at the cube source for this exact target matrix.

In particular, the Fisher theorem's compact-kernel subclass `g*nu`, for which `I<=pi^2`, is a substantial moment-free regular class but is not a closure class for all cap-one marginals. Equation (3.3) already leaves a fixed unit-interval mass deficit at that budget.

## 5. Completed fleet03/B15 partner result: general inverse-scale approximation cost

The latest compatible partner result read in this run is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T182510Z-fleet03-B15-qform-auto25/REPORT.md`

at the current math source. It proves for a Gaussian location-scale mixture

`Y=M+sigma G`, `G~N(0,1)`,

that the branch assumption `E sigma^-1<=sqrt(2pi)` forces

`P(Y in [0,1]) <= alpha_*`
with

`alpha_*=2 Phi(sqrt(pi/2))-1=0.7899085945...`,

so this Gaussian-component class is not weakly dense at the interval law.

The same completed proof gives a useful quantitative extension for arbitrary inverse-scale budget. Put

`K=E sigma^-1`.

For any interval `I` of length `L`, conditioning on `(M,sigma)` and centering the Gaussian optimally gives

`P(Y in I | M,sigma) <= 2 Phi(L/(2sigma))-1`.

The function

`a_L(x)=2 Phi(Lx/2)-1`

is increasing and concave for `x>=0`. Jensen therefore gives

`boxed( sup_|I|=L P(Y in I) <= 2 Phi(LK/2)-1 )`.              (5.1)

The partner theorem is (5.1) with `L=1` and `K=sqrt(2pi)`. If a mixture density `g` satisfies

`||g-u||_1<=eta`,

then `P_g([0,1])>=1-eta/2`, so (5.1) forces

`boxed( K >= 2 Phi^-1(1-eta/4) )`.                            (5.2)

Thus every Gaussian-mixture approximation of the unit interval must send its inverse-scale budget to infinity; the partner's fixed positive separation is the special bounded-budget case. The Fisher and Gaussian-mixture branches therefore fail as closure mechanisms for different quantitative reasons: Fisher cost is at least algebraic `eta^-1`, while the Gaussian inverse-scale cost in (5.2) diverges with the Gaussian quantile.

## 6. The pinned e5f ruled theorem pays the same rough target directly

The required completed source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

proves the one-sheet theorem for exact rank-three signature `(+, +, -)`. For eigenvalue magnitudes `lambda_1,lambda_2,mu`, the majority-side density is bounded by

`C_+ = (lambda_1 lambda_2 mu)^(-1/2)`
`      * int_0^(2pi) [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta`.   (6.1)

For `(1,1,-1)`,

`C_+=pi sqrt(2)`.                                              (6.2)

Now take the actual rough source

`X_1,X_2,X_3 iid Uniform[0,1]`.

For matrix (4.1),

`Q=2X_1X_2+X_3^2>=0` almost surely.                            (6.3)

Thus the majority one-sheet submeasure is the **entire** output law. Applying (6.1)-(6.2) gives the genuine owner-target inequality

`boxed( P(Q in I) <= pi sqrt(2) |I| )`                        (6.4)

for every interval `I`, hence

`boxed( ||p_Q||_infinity <= pi sqrt(2) )`.                    (6.5)

The triangular approximate identity is paid at once:

`boxed( E (eps-|Q-y|)_+ <= pi sqrt(2) eps^2 )`                (6.6)

for every `eps>0` and every center `y`.

This is the promised real application of a completed pinned result. It also improves the `<=6` physical `L^p` witness used in the latest fleet03/B15 report for this same rough example.

Crucially, (6.4) is an **essential-boundedness** conclusion obtained from an interval estimate. It does not use continuity.

## 7. Independent audit of the ruled rough-input bridge

The smooth geometric constant checks exactly. After spectral rescaling, for

`q_0(z)=z_1^2+z_2^2-z_3^2`

and `s>=0`, the ruling

`F(theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3)`

satisfies

`F_theta x F_t = (1/2) grad q_0(F)`

with consistent orientation, hence

`d sigma/|grad q_0| = (1/2) dtheta dt`.                        (7.1)

Undoing the spectral scaling makes the ruling direction

`v_theta=(-sin(theta)/sqrt(lambda_1), cos(theta)/sqrt(lambda_2), 1/sqrt(mu))`,

so the non-arclength parameter contributes exactly `1/|v_theta|`. A line integral of the projected three-dimensional source density is a value of a two-dimensional product projection density; the completed Ball/Livshyts-Paouris-Pivovarov projection cap is `2`. The factor `2` cancels the coarea `1/2` and yields (6.1). No independence is asserted after spectral rotation.

For rough original marginals, mollify each **original coordinate**: `f_i^delta=f_i*rho_delta`. This preserves independence and the cap. Product L1 convergence follows from telescoping,

`||prod f_i^delta-prod f_i||_1 <= sum_i ||f_i^delta-f_i||_1 ->0`.   (7.2)

Deterministic projection/quadratic pushforward contracts total variation. Therefore every already-proved smooth interval domination

`mu_delta(I)<=C_+ |I|`

passes to the rough law with the **same** `C_+`. This is the safe limiting step: no pointwise evaluation of an arbitrary L-infinity representative on a ruling is needed in the rough law, and output continuity is never invoked.

For an ambient form with an invertible physical `3x3` block `B` of signature `(2,1)`, condition on all outside original coordinates `W=w`:

`Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)`
`      =(x+B^-1 d(w))^T B(x+B^-1 d(w))+c(w)`.                  (7.3)

The affine term is automatically in `range(B)` because `B` is invertible, exactly satisfying the corrected scope of the ruled theorem. The completion is a translation in the original independent coordinates, so cap-one independence is preserved. The same active-coordinate mollification then yields

`P(Q in I, Q>=c(W)) <= C_B |I|`,                              (7.4)

with the exact ruled coefficient `C_B`. This verifies the newest continuation's rough/affine bridge at its legitimate scope; it does not claim a two-sheet estimate.

## 8. What the Fisher score identity says after the cap has paid the divergence term

The new Fisher proof writes, with a selected `r`-dimensional spectral space and centered primitive `Phi` of a nonnegative test `psi` of mass `m`,

`E psi(Q) = - E[Phi(Q) div V] - E[Phi(Q) V dot S]`             (8.1)

in the regular case after `delta->0`, where `S` is the product score. Under the original cap, the projection small-ball estimate already gives

`D=E R^-2 <= D_r`.

Hence

`|E Phi(Q) div V| <= m r D_r/(4s)`.                           (8.2)

For `r=3`, `s=1`,

`D_3=6(4pi/3)^(2/3)=15.5911083588...`,

so the completely cap-paid divergence contribution is

`3D_3/4=11.6933312691...`.                                    (8.3)

The only genuinely rough regularity term left in this route is therefore the **signed score pairing** in (8.1). Cauchy-Schwarz replaces it by `sqrt(J_E D_3)` and thereby loses precisely the cancellation that Theorem 2.1 shows cannot be recovered by a bounded information approximation.

The ruled witness makes that cancellation quantitative. For any smooth cap-one nonnegative-support approximation of the cube source in (4.1), the support condition still gives `Q>=0`, so (6.5) remains valid while `J_E->infinity` by Theorem 2.1. Combining (8.1)-(8.3) with (6.5) gives the signed estimate

`boxed( |E[Phi(Q) V dot S]| <= (pi sqrt(2)+3D_3/4) m <16.137 m )`.   (8.4)

Thus the **actual signed term stays uniformly bounded while its Fisher/Cauchy majorant diverges**. This is not a new proof of (6.5)—it is an exact diagnosis of what any successful rough-score continuation must exploit.

## 9. Implication ledger: absolute continuity, essential boundedness, continuity

These implications must remain distinct.

1. Under the owner target, absolute continuity is qualitative. For `q(x)=x^T A x`, a null set `N` satisfies by local coarea

`int_(q^-1(N)) F(x)|grad q(x)| dx=0`.

Since `grad q=2Ax` vanishes only on the proper null subspace `ker A` for nonzero `A`, the pushforward has no mass on `N`. This gives absolute continuity but no universal density height.

2. Essential boundedness is exactly an interval domination statement such as (6.4). The rough ruled bridge proves it without continuity.

3. Continuity is stronger and logically separate. The current owner continuation reports a fixed-instance `C_0` theorem in the consolidated manuscript under the rank-three target, but that individual-output regularity does not supply the missing class-wide height. Nothing in this report uses continuity to derive (6.4), (6.5), or any other height estimate.

## 10. Exact remaining implication

The regularity/closure routes are now more sharply delimited:

- bounded Gaussian inverse-scale budget cannot weakly approach the interval law (partner theorem, strengthened by (5.1)-(5.2));
- bounded projected Fisher budget cannot weakly approach it either, and every L1 H1 approximation pays at least (2.1);
- nevertheless product-sensitive ruled geometry pays an exact rough target source directly by (6.4).

Therefore a full proof cannot be obtained by proving the theorem on either of these regular subclasses and invoking qualitative weak/continuity closure with the regularity budget held fixed. The first unpaid implication in the Fisher route is a **uniform signed-score cancellation estimate** using final cap/product provenance rather than `|S|^2`; in the physical ruled branch the first unpaid local term remains the minority/two-sheet contribution, for which the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids a generic X-ray-only substitute. Globally, a structural exit into the completed volume/hub/grouped-coordinate branches is still required when no uniformly conditioned physical triple exists.

The latest source head resolved before this report was `math-open-problems@810eb1d6e50d68ab2ee70591edb690051823c163`; its new `rho*-M*`/single-hub additions do not supersede the ruled theorem or remove the rough signed-score/two-sheet obligations above. Full unrestricted QFORM remains OPEN.
