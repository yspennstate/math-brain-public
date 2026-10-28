SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T11:13:24Z.
attacking: the genuinely rotated physical 3x3 indefinite block; combine an interlacing dichotomy with moving-critical-value logarithmic averaging so the third direction removes the rank-two log without rotating the product source.

# account03/B11 r56 — a product-valid localized theorem for every indefinite physical 3x3 block

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures / quantitative inequalities and rigorous computations  
Status: `NEW AMBIENT SUPPORTING THEOREM / LOCALIZED INDEFINITE 3x3 BRANCH CLOSED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`


The first essential implication attacked is:

`QFORM-INDEFINITE-PHYSICAL-3X3-LOCALIZED-v1`.

It is proved below with an explicit constant.

## 1. Main theorem

### Theorem 1 — every genuinely rotated indefinite physical triple is paid

Let `A` be any real symmetric `n x n` matrix and let three literal ORIGINAL coordinates `I={i,j,k}` have principal block

`C=A[I,I]`.

Assume `C` is invertible and indefinite and put

`s=sigma_min(C)=min{|lambda|: lambda eigenvalue of C}>0`.

For independent original inputs with one-dimensional probability densities bounded by one, the full ambient quadratic form

`Q=X^T A X`

has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= C_ind/s`,

where one may take

`C_ind = 4*22^(3/4)*3^(1/4) = 53.47580311161168... .`       (1.1)

The theorem covers both inertia signatures `(2,1)` and `(1,2)`, arbitrary affine terms created by every outside coordinate, arbitrary dense outside couplings, and arbitrary additional spectrum.

No continuity conclusion is claimed for this full branch.

The proof is entirely in literal source coordinates. Its two branches are:

1. a majority-sign physical scalar pivot of magnitude at least `s/3`; or
2. a physical indefinite pair with `sigma_min >= s/3`, in which the remaining original scalar moves the logarithmic critical value with a quadratic coefficient tied exactly to `det C`.

The second branch is new and is the quantitative mechanism that removes the opposite-sign rank-two logarithm without taking a worst fiber.

## 2. Structural interlacing dichotomy

First suppose `C` has inertia `(2,1)`. Order its eigenvalues

`lambda_1 < 0 < lambda_2 <= lambda_3`.

Because `sigma_min(C)>=s`,

`lambda_1 <= -s`, `lambda_2>=s`, `lambda_3>=s`.              (2.1)

### Lemma 2.1

Either some physical diagonal satisfies

`C_kk >= s/3`,                                                   (2.2)

or every `2x2` physical principal block `B` is indefinite and

`sigma_min(B)>s/3`.                                               (2.3)

**Proof.** Assume (2.2) fails, so all three physical diagonals are `<s/3`. Delete any one coordinate and let `B` be the remaining principal pair, with eigenvalues `mu_1<=mu_2`. Cauchy interlacing gives

`lambda_1 <= mu_1 <= lambda_2 <= mu_2 <= lambda_3`.             (2.4)

Hence `mu_2>=lambda_2>=s`. On the other hand

`mu_1+mu_2=tr(B)<2s/3`,

so

`mu_1<2s/3-mu_2<=-s/3`.                                         (2.5)

Thus `B` is indefinite and both eigenvalue magnitudes exceed `s/3`. QED.

For inertia `(1,2)`, apply the same statement to `-C`. Equivalently, either some diagonal is `<=-s/3`, or every physical pair is indefinite with least singular value `>s/3`.

This dichotomy is local to an already selected physical triple; it does NOT assert that the global three-large-eigenvalue hypothesis forces such a triple.

## 3. Branch A: majority-sign pivot

Again treat inertia `(2,1)`. Suppose a diagonal pivot `d=C_kk>=s/3` exists. Reorder the triple as

`C=[[B,r],[r^T,d]]`.                                             (3.1)

Because `d>0`, Sylvester inertia additivity shows that the Schur complement

`S=B-r r^T/d`                                                    (3.2)

is indefinite. Condition on all original coordinates outside the triple. They contribute only affine terms to the selected three variables.

The preceding account03/B11 theorem `QFORM-INDEFINITE-PAIR-L3-v1`, source

`yspennstate/math-open-problems@65874e307e960615e2da0e659b588fb94490f40e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T101550Z-account03-B11-QFORM-r55/REPORT.md`

gives for the complete affine Schur-pair remainder

`||p_R||_3 <=22 |det S|^(-1/3)`.                                (3.3)

That same report applies the completed dependent-square smoothing lemma (canonical proof: account01/B11, commit `2279571f59ade7a9ec478af1e4818f6c117ac224`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`) to the completed original scalar square. It yields

`||p_Q||_infinity
 <=4*22^(3/4)|d|^(-1/4)|det C|^(-1/4)`.                         (3.4)

Since `|d|>=s/3` and `|det C|>=s^3`,

`boxed: ||p_Q||_infinity
 <=4*22^(3/4)*3^(1/4)/s
 =53.47580311161168.../s.`                                       (3.5)

For inertia `(1,2)`, reflect the output and matrix; `-Q` has the same density supremum and `-C` has inertia `(2,1)`.

## 4. A uniform logarithmic averaging lemma for a moving square center

The second branch uses the completed original-coordinate pair-log theorem, source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its raw envelope is: if `U,V` are independent cap-one variables and `B` is an invertible indefinite physical pair, with

`D=|det B|`, `kappa=sigma_min(B)`,

then after arbitrary affine shifts, for every gradient cutoff `R>0`,

`p_F(t)
 <=2sqrt(2)/R
   +D^(-1/2) log_+(2R^2/(kappa |t-t_0|))`                         (4.1)

for almost every `t`. The singularity at the critical value is logarithmic and is retained rather than falsely bounded.

The following elementary lemma is the new compiler.

### Lemma 4.1 — `QFORM-MOVING-SQUARE-LOG-AVERAGE-v1`

Let `W` have a probability density bounded by one. For every `delta!=0`, every `w_0,z_0,z in R`, and every `a>0`,

`boxed:
 E log_+( a / |z-z_0-delta(W-w_0)^2| )
 <=4 sqrt(2a/|delta|).`                                           (4.2)

**Proof.** For every `rho>0` and every center `xi`,

`|{w: |w^2-xi|<rho}| <=2sqrt(2rho).`                              (4.3)

Indeed, if `xi<=-rho` the set is empty. If `-rho<xi<=rho`, its length is at most `2sqrt(xi+rho)<=2sqrt(2rho)`. If `xi>=rho`, its length is

`2(sqrt(xi+rho)-sqrt(xi-rho))
 =4rho/(sqrt(xi+rho)+sqrt(xi-rho))
 <=2sqrt(2rho)`.                                                   (4.4)

Translation and scaling therefore give

`P(|z-z_0-delta(W-w_0)^2|<rho)
 <=2 sqrt(2rho/|delta|)`.                                         (4.5)

Layer cake now yields

`E log_+(a/|...|)
 =int_0^infinity P(|...|<a e^(-u)) du
 <=2sqrt(2a/|delta|) int_0^infinity e^(-u/2)du
 =4sqrt(2a/|delta|).`                                             (4.6)

No conditional density bound after a rotation is used. QED.

## 5. Branch B: no majority-sign pivot

Assume inertia `(2,1)` and no diagonal reaches `s/3`. By Lemma 2.1 choose any two original coordinates as an indefinite physical pair. Write the selected triple, in those literal coordinates, as

`C=[[B,r],[r^T,d]]`,                                              (5.1)

with

`kappa=sigma_min(B)>s/3`, `D=|det B|`.                            (5.2)

After conditioning every outside original coordinate, the conditional polynomial in the triple is

`x^T B x +2w r^T x + d w^2 +2 ell^T x+2 eta w+c`,                (5.3)

where `x=(U,V)`. For fixed `w`, complete the physical pair. Its critical output value is

`tau(w)
 =d w^2+2eta w+c-(ell+r w)^T B^(-1)(ell+r w)
 =delta w^2+beta w+gamma`,                                       (5.4)

where the leading coefficient is the exact Schur determinant ratio

`boxed: delta=d-r^T B^(-1)r=det C/det B.`                         (5.5)

Thus

`D |delta|=|det C|`.                                              (5.6)

Complete the scalar square in (5.4), so `tau(w)=delta(w-w_0)^2+tau_0`. Apply (4.1) conditional on `W=w`, then average over the authentic cap-one original scalar `W`. Lemma 4.1 with

`a=2R^2/kappa`

gives

`E log_+(2R^2/(kappa|z-tau(W)|))
 <=8R/sqrt(kappa|delta|)`.                                       (5.7)

Therefore

`p_Q(z)
 <=2sqrt(2)/R
   +8R/sqrt(D kappa |delta|)
 =2sqrt(2)/R+8R/sqrt(kappa |det C|).`                             (5.8)

Optimize in `R>0`. The minimum is

`boxed:
 ||p_Q||_infinity
 <=8*2^(1/4) (kappa |det C|)^(-1/4).`                            (5.9)

Using `kappa>s/3` and `|det C|>=s^3`,

`boxed:
 ||p_Q||_infinity
 <8*6^(1/4)/s
 =12.52067664058630.../s.`                                       (5.10)

This is uniform through genuinely rotated `(2,1)` geometry with no large physical diagonal. Reflection gives `(1,2)`.

### What the third direction did

For the rank-two control `2XY`, with independent centered unit uniforms,

`p_{2XY}(t)=log(1/(2|t|))`, `0<|t|<1/2`,                         (5.11)

so the two-direction saddle really is unbounded. In (5.3), the third original coordinate does not need to be source-disjoint after an algebraic square completion. Instead it *moves the pair's critical value quadratically*. The determinant identity (5.5) forces the speed of that motion: a small Schur coefficient is exactly compensated by the pair determinant. The one-dimensional tube estimate (4.3) averages the log into a finite quantity, and `D|delta|=|det C|` eliminates the potentially bad pair determinant. This is the third-direction smoothing mechanism in this branch.

## 6. Ambient conclusion and all-sign localized corollary

The estimates above were conditional on arbitrary outside original coordinates and are uniform in those conditioning values. Averaging the conditional interval bounds proves Theorem 1 for the full ambient form. Product structure is never asserted after a non-coordinate rotation.

There is an immediate same-source corollary. If a literal physical `3x3` block `C` is positive or negative definite with `sigma_min(C)>=s`, every `2x2` principal pair is definite with both eigenvalue magnitudes at least `s` by interlacing. The standard two-coordinate ellipse/Beta argument then gives conditional density at most `pi/s`; averaging the third coordinate and the outside variables preserves that cap.

Hence:

### Corollary 6.1 — `QFORM-PHYSICAL-3X3-LOCALIZED-REPAIR-v1`

If **any literal original-coordinate `3x3` principal block** has all three eigenvalue magnitudes at least `s>0`, with arbitrary signature, then the full ambient form has an essentially bounded density with

`boxed: ||p_Q||_infinity <=53.476/s.`                             (6.1)

This gives a product-valid proof of the localized physical-triple regime without the refuted arbitrary-joint 3D coarea lemma.

It does **not** solve the global owner target: the live correction family

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`

has nonzero spectrum `{1,1,-1}` but no uniformly conditioned physical `3x3` principal block. The remaining bridge is an aggregate/diffuse extraction theorem before inversion, not another local 3x3 estimate.

## 7. Designated partner account04/B11 applied at an actual inequality

The freshest completed designated-partner artifact visible before publication is

`QFORM-RULED-PHYSICAL-TRIPLE-DET6-v1`,

source

`yspennstate/math-open-problems@da4db4dae881f0b5239c93291ee3d7e76216c945`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T101034Z-account04-B11-ruled-triple-l3-r3/REPORT.md`.

For the literal ruled subfamily

`C=[[a,t,0],[t,0,0],[0,0,lambda]]`, `t lambda !=0`,               (7.1)

it proves the continuous bound

`||p_Q||_infinity <=6(|t|^2|lambda|)^(-1/3)=6|det C|^(-1/3)`.    (7.2)

Applying it at the actual normalized inequality `|t|=|lambda|=1` gives

`boxed: ||p_Q||_infinity <=6`                                    (7.3)

for every cap-one product input and every arbitrary ambient extension of

`[[a,1,0],[1,0,0],[0,0,+/-1]]`,                                  (7.4)

uniformly in `a` and all outside couplings. This is a sharper continuous special case inside Theorem 1.

## 8. Deterministic verification

`VERIFY.py` is an algebraic/finite checker, not a proof substitute. With fixed seed `20260924` it samples 60,000 orthogonal conjugates of both indefinite signatures and verifies:

- the interlacing dichotomy has zero violations;
- in the no-majority-pivot branch every tested physical pair has `kappa/s>=1/3`;
- `det C=det B*(d-r^T B^(-1)r)` to numerical precision;
- the exact square-tube bound has numerical ratio below `2sqrt(2)`;
- the two branch constants are `53.475803111611683` and `12.520676640586299`.

Its output ends

`QFORM_B11_R56_LOCALIZED_INDEFINITE_CHECK_PASS`.

## 9. Scope and next implication

**Proved this run:** a universal `C/s` essential density bound for every ambient form containing a uniformly conditioned literal indefinite physical `3x3` block, both `(2,1)` and `(1,2)`; plus the all-sign localized corollary. The proof explicitly retains the rank-two logarithmic control and identifies quadratic critical-value motion as the third-direction smoother in the no-pivot chamber.

**Not proved:** continuity in the full new indefinite branch; extraction of such a uniformly conditioned physical triple from merely three large global eigenvalues; the diffuse aggregate regime; the unrestricted QFORM conjecture; or a counterexample.

The next B11 implication is:

`QFORM-DIFFUSE-AGGREGATE-TO-LOCAL-L3-GLUE-v1`:
use the new local theorem only after aggregating original-coordinate banks, so that the known family with every physical triple ill-conditioned is paid without a reciprocal-minor loss. Any such compiler must preserve product provenance and cannot invoke the refuted arbitrary-joint, conditional-cap, fiber-supremum, or pointwise-decay interfaces.

Full QFORM remains OPEN / not proved / not disproved.
