# QFORM account02/B15 r21 — no uniform positive Besov/Sobolev regularity even in the smooth tight fixed-A class

**Status:** SOURCE-VALID REGULARITY SEPARATION / FULL QFORM OPEN  
**Assignment:** Absolute continuity and regularity; complementary constructions/source-valid counterexamples.  
**Execution:** WITHOUT_VERIFIED_BRAIN.  
**Owner target:** independent one-dimensional densities `f_i<=1`; real symmetric `A` with at least three eigenvalues of modulus at least one; prove a universal essential density bound for `X^TAX` or give a valid counterexample. Continuity is logically separate.

## 1. First unpaid implication

The completed assigned-partner result account03/B15 r20 (`yspennstate/math-open-problems@626e33966e69eda517dd09776028cbd80bd5d372`) gives the exact positive tent representation. For a probability law `mu`,

`T_epsilon(mu;y)=epsilon^{-2} E (epsilon-|Z-y|)_+`

satisfies

`||p_mu||_infinity = sup_{epsilon>0,y} T_epsilon(mu;y)`

(with `+infinity` if no bounded density exists). Hence the full QFORM theorem is exactly the uniform estimate

`E (epsilon-|X^T A X-y|)_+ <= C epsilon^2`

for every admissible target instance, center, and scale. This is the first unpaid implication. No continuity statement is used to infer it.

The purpose of the present report is to eliminate a broad family of possible intermediate regularity payments.

## 2. Source family already proved in B15 r11

Source pin: account02/B15 r11, canonical proof

`yspennstate/math-open-problems@4fc6472947c7e5551592974a34e7bc4bfe78def0`.

That report proves the following. There is a sequence `tau -> infinity` and strictly positive real-analytic Schwartz probability densities `f_tau` satisfying `0<f_tau<=1`, uniformly tight, such that for three iid coordinates with density `f_tau`,

`Q_tau=X_1^2+X_2^2+X_3^2`,  `A=I_3`,

one has the high-frequency certificate

`|hat p_tau(tau)|=|phi_{Q_tau}(tau)| >= c0`,  `c0=(3/8)^3=27/512`.

Moreover every member of this same family satisfies the common height bound

`||p_tau||_infinity <= 2*pi`,

and the outputs are uniformly tight. Thus the matrix is fixed, perfectly conditioned, and normalized (`s_3(A)=1`); all source densities are already inside the analytic-Schwartz cap-one normal form.

## 3. Exact finite-difference Fourier lemma

For `p in L1(R)`, define `Delta_h p(t)=p(t+h)-p(t)`. For every integer `m>=1`, frequency `xi`, and shift `h`,

`||Delta_h^m p||_1 >= |exp(i xi h)-1|^m |hat p(xi)|`.                     (3.1)

Proof: `widehat{Delta_h^m p}(xi)` equals `(exp(-i xi h)-1)^m hat p(xi)` up to the harmless sign convention. The elementary Fourier bound `|hat g(xi)|<=||g||_1` gives (3.1). No smoothness of `p` is required.

Apply (3.1) to `p=p_tau`, `xi=tau`. If

`pi/(2 tau) <= h <= 3*pi/(2 tau)`,

then `tau h in [pi/2,3pi/2]`, so

`|exp(i tau h)-1| = 2 |sin(tau h/2)| >= sqrt(2)`.

Therefore

`||Delta_h^m p_tau||_1 >= c0 * 2^(m/2)`                         (3.2)

throughout that entire interval. At the central shift `h_tau=pi/tau`,

`||Delta_{h_tau}^m p_tau||_1 >= c0 * 2^m`.                    (3.3)

For `m=1`, in particular,

`||p_tau(.+pi/tau)-p_tau||_1 >= 2c0 = 27/256`,                (3.4)

although `pi/tau -> 0`.

Thus there is **no target-uniform L1 translation modulus**, even inside this fixed-`I_3`, analytic-Schwartz-source, uniformly tight, uniformly height-bounded class. By the Kolmogorov-Riesz compactness criterion, the output densities are not relatively compact in `L1`, despite their uniform tightness and common `L-infinity` bound.

## 4. No uniform positive Besov regularity of any order

Fix any `s>0`, choose an integer `m>s`, and use the standard finite-difference homogeneous Besov seminorm

`|p|_{B^s_{1,q};m} = ( int_0^infinity [ h^{-s} ||Delta_h^m p||_1 ]^q dh/h )^(1/q)`

for `1<=q<infinity`, and the corresponding supremum for `q=infinity`.

For finite `q`, integrate only over `[pi/(2tau),3pi/(2tau)]`. By (3.2), and because `h^{-s} >= (2tau/(3pi))^s` there,

`|p_tau|_{B^s_{1,q};m}`
` >= c0 * 2^(m/2) * (2/(3pi))^s * (log 3)^(1/q) * tau^s`.     (4.1)

For `q=infinity`, (3.3) gives

`|p_tau|_{B^s_{1,infinity};m}`
` >= c0 * 2^m * pi^{-s} * tau^s`.                            (4.2)

Hence for **every positive order `s` and every `q in [1,infinity]`**, no uniform positive-order Besov bound can hold on the target-normal-form class. This is stronger than the previous absence of a common pointwise modulus of continuity: even averaged/translation-based positive regularity blows quantitatively like `tau^s`.

## 5. Fractional W^{s,1} and BV consequences

For `0<s<1`, write the Gagliardo seminorm in translation form,

`[p]_{W^{s,1}} = int_R ||Delta_h p||_1 |h|^{-1-s} dh`.

Using only positive `h` in the interval above and (3.2) with `m=1`,

`[p_tau]_{W^{s,1}}`
` >= c0*sqrt(2) * (2/pi)^s * (1-3^{-s})/s * tau^s`.           (5.1)

Thus no uniform fractional `W^{s,1}` bound exists for any `0<s<1`.

If `p_tau` has finite total variation, the standard translation inequality

`||Delta_h p_tau||_1 <= |h| Var(p_tau)`

combined with (3.4) gives

`Var(p_tau) >= (2c0/pi) tau = (27/(256*pi)) tau`.             (5.2)

If a member is not BV, the claimed absence of a uniform BV bound is of course even more immediate. Therefore neither BV nor `W^{1,1}` can supply a target-uniform output regularity payment.

## 6. Logical implication ledger

The known qualitative statements remain separate:

1. Every nonzero quadratic pushforward of an absolutely continuous joint law is absolutely continuous.
2. Absolute continuity alone does not imply essential boundedness (e.g. a squared uniform variable).
3. Essential boundedness alone does not imply a continuous representative in general (rank-two positive-definite examples give a jump at the hard edge).
4. Under the product hypothesis and rank at least three, every **fixed** matrix has an individually bounded `C_0` output density; the bound may depend on the matrix.
5. The owner theorem asks for one `L-infinity` constant uniform over all target matrices and product laws.

The present construction shows that item 4 cannot be quantitatively upgraded, from the target hypotheses alone, to any common positive Besov/Sobolev/BV regularity even after restricting to the fixed matrix `I_3` and exceptionally smooth, uniformly tight inputs. Indeed this special family already has the common height bound `2*pi`, while its positive regularity seminorms diverge.

Therefore any proof of item 5 that attempts to obtain the universal height through output compactness, a common translation modulus, a positive Besov norm, a fractional `W^{s,1}` norm, or a BV bound is unavailable at target scope. This is not a counterexample to QFORM: it is a source-valid counterexample to those intermediate implications.

## 7. Partner application and surviving mechanism

The completed account03/B15 r20 tent theorem is compatible and was applied above. It also proves that moving a conditional `L-infinity` cap outside the tent mixture simply recovers the expectation of that cap, so tent regularization does not rescue an unintegrable conditional-height estimate.

The surviving route is therefore the direct positive scale estimate

`E (epsilon-|X^T A X-y|)_+ <= C epsilon^2`,

or an equivalent averaged small-ball estimate, **before** taking a conditional `L-infinity` norm, a reciprocal local-minor cost, or an output regularity seminorm. Original-coordinate product geometry and translation/packing information must remain present at that stage.

## 8. Acceptance / status

Acceptance satisfied by an explicit rigorous target-valid counterexample to a broad regularity bridge, with quantitative divergence constants and the remaining connection to the full theorem stated exactly. The universal bounded-density conjecture itself remains OPEN.
