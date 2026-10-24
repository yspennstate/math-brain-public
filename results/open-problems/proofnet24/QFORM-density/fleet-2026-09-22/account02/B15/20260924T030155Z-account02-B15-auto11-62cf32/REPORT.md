SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T03:01:55Z.
attacking: logarithmic Schur-remainder payment after an indefinite physical pair, especially the both-nonzero-diagonal chamber, then the ruled rough-input bridge.

# account02/B15 — logarithmic Schur payment and a nested half-Riesz compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.  
Status: `NEW_SUPPORTING_THEOREMS / ROUGH-RULED-BRIDGE-CHECKED / FULL_QFORM_OPEN`.

## 1. First unpaid implication

The unrestricted owner theorem is still OPEN. The local B15 issue is no longer qualitative regularity: the newest account03/B15 result proves an explicit finite height certificate for every fixed rank-at-least-three matrix, and the completed same-constant compiler then gives a `C_0` representative only after height is paid. The global missing step is uniformity under `s_3(A)>=1`.

This run improves the indefinite-physical-pair route in two ways.

1. A nonzero physical Schur diagonal costs only **logarithmically** when it is small, rather than the quarter-power loss from the all-purpose square-root small-ball compiler.
2. If the Schur remainder contains an invertible physical `2x2` block of either sign, the completed orientation-free rank-two half-Riesz theorem can be inserted before the outer logarithmic envelope. This yields only logarithmic dependence on the inner determinant and removes the inner `sigma_min` loss present in the contemporaneous nested log-envelope argument.

What remains unpaid is structural: turn the spectral condition into a dimension-free aggregate receiver before reciprocating local minors or entries. The estimates below reduce one raw physical-entry route to at worst logarithmic dimension loss when a quantitatively good outer pair is already available, but they do not remove that logarithm.

Dependencies used at exact scope:

- owner-pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, in particular the ruled one-sheet theorem and the Schur-complement eigenvalue persistence lemma;
- account03/B15 physical-pair logarithmic envelope at `2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`;
- orientation-free rank-two affine half-Riesz theorem at `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`;
- newest compatible account03/B15 fixed-matrix closure at `bea3c88b8ba5df9f7fbed3bf0676709971a1e9da`;
- account04/B15 rough-trace and same-constant `C_0` compiler at `7b2b0f54db9acbd23a5f69f715178ab666e22d8e`;
- the immediately preceding account02/B15 one-null-diagonal theorem at `1205ce188002747c102b80c97d0493985fa6fe34`.

A concurrent account01/B15 report, `5ba58fd0d529b51cf11d770bb231022074db9f68`, independently closes a nested indefinite Schur pair by log-envelope self-convolution with a power dependence on the inner parameters. Section 4 below gives a different insertion which is logarithmic in the inner determinant and does not use its smallest singular value.

## 2. Scalar quadratic logarithmic potential

For `q>0` define

`Psi(q)=4 sqrt(2q)` for `0<q<=1/8`,

`Psi(q)=2+log(8q)` for `q>=1/8`.

### Theorem 2.1 — `QFORM-SCALAR-QUADRATIC-LOG-POTENTIAL-v1`

Let `V` have a probability density bounded by one. Let `b!=0` and allow arbitrary affine coefficients. For

`Y=bV^2+ell V+c`

and every `L>0`,

`boxed( sup_t E log_+(L/|Y-t|) <= Psi(L/|b|). )`                 (2.1)

No support, moment, smoothness, or continuity assumption is used.

### Proof

Complete the square. A deterministic translation of the ORIGINAL variable preserves its density cap, so it is enough to treat `Y=bW^2+c`. Put `q=L/|b|`.

For every `a in R` and `rho>0`,

`Leb{x: |x^2-a|<rho} <=2 sqrt(2rho)`.                              (2.2)

Indeed, if `a<=-rho` the set is empty; if `-rho<a<rho` it lies in `|x|<sqrt(a+rho)`; and if `a>=rho` its length is

`2[sqrt(a+rho)-sqrt(a-rho)]`,

which is maximal at `a=rho`. Hence

`P(|W^2-a|<rho) <= min(1,2sqrt(2rho)).`                            (2.3)

Layer cake gives

`E log_+(q/|W^2-a|)
 =int_0^infinity P(|W^2-a|<q e^{-v}) dv`

`<=int_0^infinity min(1,2sqrt(2q)e^{-v/2}) dv.`                   (2.4)

If `q<=1/8`, the cap never reaches one and (2.4) is `4sqrt(2q)`. If `q>=1/8`, the switching time is `log(8q)` and (2.4) is `2+log(8q)`. This proves (2.1). QED.

The point is the `min(1,...)` in (2.3). Dropping it recovers only a square-root bound; retaining it converts weak curvature into a logarithmic cost.

## 3. Indefinite outer pair plus any nonzero physical Schur diagonal

Split ORIGINAL coordinates as `X=(P,Z)`, with `P=(X_1,X_2)`, and write

`A=[[D,B],[B^T,C]]`,

where `D` is an invertible indefinite physical `2x2` principal block. Put

`Delta=|det D|`, `kappa=sigma_min(D)`,
`S=C-B^T D^(-1)B`.

Assume one remaining original coordinate `V` has Schur diagonal coefficient

`b=S_VV !=0`.

All other Schur entries, all cross couplings, and all affine terms are arbitrary.

The completed physical-pair envelope says, for every `r>0`, after completing the outer pair in the original coordinates,

`p_Q(t) <=2sqrt(2)/r
 +Delta^(-1/2) E log_+( 2r^2/[kappa |t-R(Z)|] ),`                 (3.1)

where `R(Z)=Z^T S Z+ell^T Z+c`.

Condition on every Schur coordinate except `V`. On each fibre,

`R=bV^2+alpha V+beta`

with arbitrary fibre-dependent `alpha,beta`. Apply Theorem 2.1 with `L=2r^2/kappa`. Writing

`q=2r^2/(kappa|b|)`,

we obtain

`boxed(
 ||p_Q||_infinity
 <=4(kappa|b|)^(-1/2) q^(-1/2)
   +Delta^(-1/2) Psi(q),  q>0.
)`                                                               (3.2)

The optimization is explicit. If `kappa|b|<=32 Delta`, the large-`q` critical point is

`q_*=4Delta/(kappa|b|)>=1/8`,

and

`boxed(
 ||p_Q||_infinity
 <=[4+log(32Delta/(kappa|b|))]/sqrt(Delta).
)`                                                               (3.3)

If `kappa|b|>=32Delta`, the small-`q` branch optimizes to

`boxed(
 ||p_Q||_infinity
 <=2^(13/4)(Delta kappa |b|)^(-1/4).
)`                                                               (3.4)

Both equal `4/sqrt(Delta)` at the transition. A convenient globally valid single line is therefore

`boxed(
 ||p_Q||_infinity
 <=Delta^(-1/2)
   [4+log_+(32Delta/(kappa|b|))].
)`                                                               (3.5)

This is the first new payment. Compared with account03/B15 auto27, the weak-diagonal dependence improves from `|b|^(-1/4)` to `log(1/|b|)`. Height is proved before any continuity statement.

## 4. A general half-Riesz-to-log compiler and nested physical pair theorem

### Lemma 4.1 — `QFORM-HALF-RIESZ-TO-LOG-v1`

Let `W` be any real random variable satisfying

`sup_t E|W-t|^(-1/2) <=H`.                                       (4.1)

Then, for every `L>0`, with `z=H^2 L`,

`boxed(
 sup_t E log_+(L/|W-t|)
 <=Xi(z),
)`                                                               (4.2)

where

`Xi(z)=2sqrt(z)` for `0<z<=1`,

`Xi(z)=2+log z` for `z>=1`.

Proof: `P(|W-t|<rho)<=min(1,Hsqrt(rho))`, then integrate the layer cake exactly. QED.

Now suppose the Schur complement `S` contains an invertible physical `2x2` principal block `E` on two remaining ORIGINAL coordinates `U,V`; no sign assumption is needed. Put

`delta=|det E|>0`.

Condition on all other Schur coordinates. The conditional polynomial in `(U,V)` has quadratic matrix exactly `E` and arbitrary affine coefficients. The completed rank-two affine half-Riesz theorem gives uniformly in those affine coefficients

`sup_t E[ |R-t|^(-1/2) | outside ] <=128 delta^(-1/4).`            (4.3)

Averaging preserves (4.3), so Lemma 4.1 applies with

`H=128 delta^(-1/4)`.

Insert (4.2) into the outer pair envelope (3.1). With

`q=2H^2r^2/kappa`,

`||p_Q||_infinity
 <=4H kappa^(-1/2) q^(-1/2)+Delta^(-1/2)Xi(q).`                   (4.4)

If the large-`q` critical point lies above one, it is

`q_*=4H^2Delta/kappa`.

If it lies below one, simply choosing `q=1` gives at most `4/sqrt(Delta)`. Hence in all cases

`boxed(
 ||p_Q||_infinity
 <=Delta^(-1/2)
   [4+log_+(4H^2Delta/kappa)].
)`                                                               (4.5)

Using (4.3),

`boxed(
 ||p_Q||_infinity
 <=Delta^(-1/2)
   [4+log_+(65536 Delta/(kappa sqrt(delta)))].
)`                                                               (4.6)

This is the second new payment. It applies in particular to the genuinely indefinite two-coordinate Schur remainder with both physical diagonal coefficients nonzero which was the first local gap in the previous account02/B15 run.

The dependence in (4.6) is only logarithmic in the inner determinant and has **no inner `sigma_min(E)` factor**. Thus it improves, in the near-singular inner-pair regime, the concurrent account01/B15 self-convolution theorem whose displayed constant behaves like `(delta sigma_min(E))^(-1/10)`.

The rank-two source also records a smaller range-affine constant; because the present inner block is a full two-dimensional physical block, every conditional affine term lies in that two-dimensional range. Keeping only the universally quoted `128` in (4.6) avoids making the improvement depend on that secondary constant.

## 5. Logarithmic dimension loss once an outer pair is quantitatively paid

Assume now the full owner hypothesis `s_3(A)>=1` and let the selected outer physical pair `D` be invertible indefinite. The owner-pinned Schur-complement persistence lemma implies that `S` has at least one eigenvalue of modulus at least one. Hence

`||S||_op>=1.`                                                    (5.1)

Let `m=n-2` and

`eta=max_{i,j}|S_ij|`.

Since `||S||_op<=m eta`,

`eta>=1/m.`                                                       (5.2)

There are two cases.

**Large physical diagonal.** If `d=max_i|S_ii|>=eta/2`, then `d>=1/(2m)`, and (3.5) gives

`||p_Q||_infinity
 <=Delta^(-1/2)[4+log_+(64m Delta/kappa)].`                       (5.3)

**Off-diagonal dominates.** Otherwise choose `i!=j` with `|S_ij|=eta`. For the physical block

`E=[[S_ii,S_ij],[S_ij,S_jj]]`,

both diagonals have magnitude `<eta/2`, so

`|det E|>=eta^2-|S_iiS_jj|>3eta^2/4.`                            (5.4)

Thus `sqrt(delta)>=sqrt(3)/(2m)`. Formula (4.6) gives

`||p_Q||_infinity
 <=Delta^(-1/2)
   [4+log_+((131072/sqrt(3)) m Delta/kappa)].`                    (5.5)

Combining the cases,

`boxed(
 ||p_Q||_infinity
 <=Delta^(-1/2)
 [4+log_+(C_log m Delta/kappa)],
 \quad C_log=131072/sqrt(3)<7.57*10^4.
)`                                                               (5.6)

So a quantitatively paid outer indefinite physical pair reduces the entire arbitrary Schur remainder to at most a **logarithmic dimension loss**. A definite outer pair already has the dimension-free bound `pi/sqrt(Delta)`.

Equation (5.6) is not the full conjecture: the logarithm is still dimension-dependent, and the target does not force one uniformly conditioned physical pair. Its value is to isolate the remaining issue as aggregation before reciprocal payment rather than regularity.

## 6. New exact-target chamber with both Schur diagonals nonzero

Let `X,Y,U,V` be arbitrary independent cap-one variables and set

`boxed( Q=4XY+U^2+2UV+(1/4)V^2. )`                               (6.1)

The matrix is block diagonal with outer block

`D=[[0,2],[2,0]]`

and inner Schur block

`E=[[1,1],[1,1/4]].`

Its eigenvalues are

`2,-2,(5+sqrt(73))/8,(5-sqrt(73))/8.`                            (6.2)

Since `(5+sqrt(73))/8>1`, this is a literal owner-target matrix with exactly three eigenvalues of modulus at least one. Both Schur diagonal coefficients are nonzero, so the previous one-null theorem does not apply.

Here `Delta=4`, `kappa=2`, and taking the Schur diagonal coefficient `b=1` in (3.3) gives

`boxed(
 ||p_Q||_infinity
 <=(4+log64)/2
 =2+3log2
 =4.0794415416... .
)`                                                               (6.3)

Only after (6.3) is paid may the same-constant rank-at-least-three compiler be invoked; it yields a canonical

`boxed( p_Q in C_0(R),  ||p_Q||_infinity<=2+3log2. )`             (6.4)

Thus continuity is downstream of the essential-height estimate, not its source.

## 7. Required owner-pinned ruled theorem applied to the same target

Condition in (6.1) on the ORIGINAL coordinate `V=v`:

`Q=4XY+U^2+2vU+(1/4)v^2
  =4XY+(U+v)^2-(3/4)v^2.`                                        (7.1)

The active physical block on `(X,Y,U)` is invertible, has signature `(+,+,-)`, and curvature magnitudes `(2,1,2)`. Therefore the later affine-range correction to the ruled theorem is automatic: the affine term is in the range of the invertible block, and `U->U+v` is an original-coordinate translation.

The source coefficient is

`C_+
 =(1/2) int_0^(2pi)
 [sin^2(theta)/2+cos^2(theta)+1/2]^(-1/2) dtheta`

`=int_0^(2pi) [4+2cos^2(theta)]^(-1/2) dtheta
 <=pi.`                                                          (7.2)

Hence for every interval `I`,

`boxed(
 P{Q in I, Q>=-(3/4)V^2} <=pi |I|.
)`                                                               (7.3)

Equivalently, for every `epsilon>0` and `y`,

`boxed(
 E[(epsilon-|Q-y|)_+ 1_{Q>=-(3/4)V^2}]
 <=pi epsilon^2.
)`                                                               (7.4)

This is a genuine completed-source payment to a positive majority submeasure in a new both-nonzero-Schur-diagonal target chamber.

## 8. Why the new logarithmic physical certificate is still not universal

Consider the diffuse rank-one Schur bank

`S_m=(1/m) J_m`

and outer pair `D=[[0,2],[2,0]]`. The full matrix has nonzero spectrum `{2,-2,1}`, hence is in the owner target for every `m`.

Every physical Schur entry equals `1/m`, so the raw diagonal theorem gives only

`||p_Q||_infinity <=2+(1/2)log(64m).`                             (8.1)

This grows, albeit only logarithmically.

But the growth is an artifact of physical-entry payment. Put

`T_m=m^(-1/2) sum_j Z_j`.

The Rogozin-Ball projection theorem gives `||p_Tm||_infinity<=sqrt(2)`. Therefore `W_m=sqrt(2)T_m` has density cap one and is independent of the outer pair, while

`Q=4XY+(1/2)W_m^2.`                                               (8.2)

The owner-pinned three-variable Theorem A applied with smallest curvature `sigma=1/2` gives the dimension-free actual bound

`boxed( ||p_Q||_infinity <=12sqrt(pi). )`                         (8.3)

Thus even logarithmic max-entry payment is not the final interface. Aggregation of the Schur bank before inversion is essential. This is a source-valid obstruction to declaring (5.6) a universal route; it is not a counterexample to QFORM.

## 9. Latest account03/B15 result applied

The newest compatible partner report is account03/B15 auto31 at `bea3c88b8ba5df9f7fbed3bf0676709971a1e9da`. It proves the previously missing algebraic boundary where every physical `2x2` principal determinant vanishes: a nonsingular physical triple with all pair minors zero has an explicit finite density bound. Combined with its preceding pair theorem, it gives an elementary finite `L^infinity` certificate for **every fixed symmetric matrix of rank at least three** under arbitrary cap-one product laws.

Apply that fixed-instance conclusion to the concrete target (6.1): qualitative fixed-matrix boundedness and `C_0` regularity are independently available. Our contribution (6.3) is the sharper law-uniform chamber constant and is obtained before continuity. More generally, the partner theorem confirms that B15's remaining owner-level issue is not existence of a density or individual continuity; it is uniform control of the height over matrices, dimensions, and laws.

## 10. Independent ruled rough-input audit

Let an invertible active physical `3x3` block be `B`, and condition on all outside ORIGINAL coordinates `W=w`. Then

`Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)`

`=(x+B^(-1)d(w))^T B(x+B^(-1)d(w))+c(w).`                        (10.1)

Thus the source's affine-range hypothesis is automatic. Completion is a coordinatewise translation of the original independent variables; no independence after spectral rotation is asserted.

For arbitrary rough active marginals, mollify only the three original-coordinate densities:

`f_i^(eta)=f_i*rho_eta`.

Then `0<=f_i^(eta)<=1`, each has mass one, and

`||prod_i f_i^(eta)-prod_i f_i||_1
 <=sum_i ||f_i^(eta)-f_i||_1 ->0.`                               (10.2)

For fixed `w`, define the majority restricted pushforward by the same measurable quadratic map and the same conditional sheet. Restriction and deterministic pushforward contract total variation, so the smooth ruled interval estimate passes to the rough conditional submeasure with exactly the same coefficient. Averaging `w` then gives the ambient estimate. No representative of a rough output density is evaluated on a surface. The equality sheet has zero mass because it is the zero set of a nonzero polynomial under an absolutely continuous product law.

The geometric factors also recheck exactly. For

`q_0(z)=z_1^2+z_2^2-z_3^2`,

`F(theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3)`,

one has

`F_theta x F_t=(1/2) grad q_0(F)`,

so `d sigma/|grad q_0|=(1/2)dtheta dt`. Undoing spectral scaling gives

`v_theta=(-sin(theta)/sqrt(lambda_1),
          cos(theta)/sqrt(lambda_2),
          1/sqrt(mu)).`

The ruling parameter is not arclength, so the line estimate contributes `1/|v_theta|`; the two-dimensional product-projection cap `2` cancels the coarea factor `1/2`. This reproduces exactly the owner-pinned one-sheet coefficient. The bridge is therefore an interval/measure argument and does not use continuity to smuggle in height.

## 11. Regularity ledger

**Absolute continuity.** Let the joint input merely have an `L^1` density `F`, and let `q(x)=x^T A x+b^T x+c` be nonconstant. For a null set `N`, coarea gives

`int_{q^{-1}(N)} F(x)|grad q(x)| dx=0.`                           (11.1)

The affine critical set `{grad q=0}` is empty or a proper affine subspace and hence Lebesgue-null. On its complement use the exhaustion `{|grad q|>=1/k}` to deduce `int_{q^{-1}(N)}F=0`. Thus `q_#(Fdx)<<dx`. This is qualitative and has no universal-height content.

**Essential boundedness.** Equations (3.3)-(3.5), (4.6), (6.3), and the ruled submeasure estimate (7.3) are paid directly by interval/logarithmic-potential arguments.

**Continuity.** The completed fixed-rank-at-least-three theorem supplies a `C_0` representative for each fixed cap-one product instance. The same-constant compiler may therefore be applied only after an interval inequality is established. It does not say that an arbitrary bounded density is continuous and it supplies no class-uniform continuity modulus.

## 12. State and next implication

Full QFORM: `OPEN -> OPEN`.

New paid facts:

- weak nonzero Schur diagonal after an indefinite pair: logarithmic rather than quarter-power cost;
- arbitrary invertible physical Schur pair: logarithmic determinant cost via the completed rank-two half-Riesz theorem, no inner `sigma_min`;
- once an outer pair is quantitatively paid, arbitrary target Schur remainder: at worst logarithmic dimension loss;
- new exact target `4XY+U^2+2UV+V^2/4`: full density at most `2+3log2`, and owner-pinned ruled majority submeasure at most `pi`;
- ruled smooth-to-rough passage independently checked at interval/measure level.

The first unpaid implication is now explicitly **aggregate-before-inversion**: remove the remaining logarithmic physical-coordinate loss by a collective Schur/grouped-volume/hub receiver, and simultaneously cover target matrices with no quantitatively good physical pair. Diffuse rank-one banks show that even the logarithmic max-entry certificate is not itself the final uniform mechanism.
