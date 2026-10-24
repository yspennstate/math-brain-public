SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-22T23:42:00Z.
attacking: the two-sided-curvature/rank-two logarithmic obstruction after an outer scalar pivot; test whether the genuinely third independent square pays the log singularity without any fiber supremum.

# account02/B06 — a third product-bank square absorbs an exact hyperbolic logarithmic singularity

**Run:** `b06-20260922T234200Z-e4c1068b3e5d`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

Fresh start control was `yspennstate/math-research-brain@a8293374154bdde63ae77be6877476933763f51d`; prepublication refresh reached `8dd9195eeb54c9ac675a472a027c27783dd328f4`. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no B06 pause. Live corrections retained: no post-rotation independence, no unrestricted fiber supremum, no arbitrary-joint rank-three coarea bound, no positive moment of a worst conditional projection cap, no law-uniform pointwise Fresnel decay, and no small-tail characteristic-function truncation.

## 1. Source-valid inputs

1. **Product projection cap.** account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, proves that a unit scalar projection of an arbitrary cap-one product vector has density at most `sqrt(e)`. This is a weighted physical-space fiber integral, not a spectral fiber supremum.

2. **Previous exact obstruction.** account02/B06 run `b06-20260922T210504Z-abc2116c80c5`, canonical `yspennstate/math-open-problems@dc9752d372165b011f4c8b1101174a6698ae2c64`, constructed

`R_eps = 2 eps^(-2) U1 U2 + 2(U1 V2+U2 V1) + 2 eps^2 V1 V2
       = 2(U1/eps+eps V1)(U2/eps+eps V2)`,

whose cross block has `s_2=1` and whose opposite self-block norm is `eps^2`, yet for independent centered unit uniforms its density diverges logarithmically at zero. Its coefficient matrix has only two nonzero eigenvalues `+/-(eps^(-2)+eps^2)`, so it refutes only the perturbative rank-two intermediate statement, not QFORM.

3. **Named partner account03/B06 r21.** canonical `yspennstate/math-open-problems@da1ec290db2acb0c6d155899d242d0a66f624592`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T222149Z-account03-B06-qform-r21/REPORT.md`. In the strict-higher-rank bicolooop state, either a wedge-diffuse side survives or an actual physical `2x2` cross minor is forced, and the latter branch is paid by

`||p_Q||_infinity < 9.25 / sqrt(|a| gamma)`.

The remaining wedge-diffuse branch may not discard the nonzero higher-rank tail.

## 2. Elementary half-Riesz fact for a bounded density

### Lemma 2.1
If a real random variable `Y` has density at most `L`, then for every `t`,

`E |Y-t|^(-1/2) <= 2 sqrt(2L)`.                                    (2.1)

**Proof.** Layer cake gives

`E|Y-t|^(-1/2)=int_0^infinity P(|Y-t|<s^(-2)) ds`.

The probability is at most `min(1,2L s^(-2))`. Splitting at `s=sqrt(2L)` gives exactly `2sqrt(2L)`. Equality is attained by the density `L 1_[t-1/(2L),t+1/(2L)]`. QED.

This is the one-dimensional probability-weighted substitute for taking a singular fiber supremum.

## 3. New product-preserving curved-fiber theorem

### Theorem 3.1 — `QFORM-THIRD-SQUARE-HYPERBOLIC-ABSORPTION-v1`
Let `X_I`, `X_J`, and a physical coordinate `Z` be mutually independent original-coordinate product banks, all one-dimensional coordinate densities bounded by one. Let

`U=u^T X_I`, `V=v^T X_J`, `||u||_2=||v||_2=1`.

After conditioning any disjoint outside original-coordinate bank, suppose the remaining value can be written

`T = F(X_I) + 2 d (U-theta) V + a (Z-zeta)^2 + c`,                (3.1)

where `a d !=0`, `F` is arbitrary measurable, and the displayed shifts/constants may depend on the conditioned outside coordinates but not on `V` in the coefficient `theta`. Then the conditional and hence unconditional law has an essentially bounded density satisfying

`boxed( ||p_T||_infinity <= 4 sqrt(2e) / sqrt(|a d|) ).`            (3.2)

More generally, if the three scalar inputs `U,V,Z` have density caps `L_U,L_V,L_Z`, the right side is

`4 sqrt(2) L_Z sqrt(L_U L_V) / sqrt(|a d|)`.                        (3.3)

No moments, support restrictions, log-concavity, centered laws, or post-rotation independence are used.

### Proof
Fix the outside conditioning and `X_I=x`. The square variable `a(Z-zeta)^2` has density bounded pointwise by

`L_Z / (sqrt(|a|) sqrt(|y|))`                                      (3.4)

on its sign half-line, regardless of its shift. Therefore, writing `m=2d(U(x)-theta)`,

`p_T(t | X_I=x)
 <= (L_Z/sqrt(|a|)) E_V |mV-s_x|^(-1/2)`                           (3.5)

for a suitable scalar `s_x`.

The variable `mV` has density cap `L_V/|m|`. Lemma 2.1 gives

`E_V |mV-s_x|^(-1/2)
 <= 2 sqrt(2 L_V/|m|)
 = 2 sqrt(L_V/(|d| |U(x)-theta|))`.                                (3.6)

Average (3.6) over the genuine product bank `X_I`. Since `U` has density cap `L_U`, another application of Lemma 2.1 gives

`E |U-theta|^(-1/2) <= 2 sqrt(2L_U)`.                              (3.7)

Combining (3.5)-(3.7) proves (3.3). The source-valid scalar projection theorem gives `L_U,L_V<=sqrt(e)`; the physical original coordinate has `L_Z<=1`, yielding (3.2). QED.

### Scope
The theorem tolerates **arbitrary same-side curvature on the entire `I` bank** through `F`. It does not tolerate an arbitrary quadratic self-term on the `J` bank; the previous run proves that such a term cannot be discarded merely because its operator norm is small. The new currency is instead a genuinely third independent product-bank square.

## 4. The previous exact adversary becomes a target-valid bounded family after the third square

For `eps>0` and arbitrary independent cap-one inputs `U1,U2,V1,V2,Z`, set

`Q_eps = R_eps + Z^2`.                                               (4.1)

Put

`S1=U1/eps+eps V1`, `S2=U2/eps+eps V2`,
`s^2=eps^(-2)+eps^2`, `W_i=S_i/s`.

The variables `W1,W2,Z` are mutually independent: `W1` uses only `(U1,V1)`, `W2` only `(U2,V2)`, and `Z` a fifth original coordinate. The coefficient vectors defining `W1,W2` have Euclidean norm one, so the weighted product-projection theorem gives `||p_Wi||_infinity<=sqrt(e)`. Moreover

`Q_eps = 2 s^2 W1 W2 + Z^2`.                                       (4.2)

Theorem 3.1 with `d=s^2`, `a=1` therefore gives

`boxed( ||p_(Q_eps)||_infinity <= 4 sqrt(2e)/s ).`                   (4.3)

Since `s^2=eps^(-2)+eps^2>=2`,

`boxed( ||p_(Q_eps)||_infinity <= 4 sqrt(e) < 6.595 )`               (4.4)

for **every** `eps>0` and every admissible input law.

This family is now an exact instance of the full target: the coefficient matrix has nonzero spectrum

`{ +s^2, -s^2, 1 }`,                                                (4.5)

so it has three eigenvalues of modulus at least one. Thus the exact rank-two logarithmic obstruction from the previous run is not a target obstruction once the genuinely third independent square direction is retained. The third direction pays the logarithm before any fiber maximum is taken.

For the checker value `eps=1/8`, `s^2=4097/64`; the exact spectrum is `{4097/64,-4097/64,1,0,0}` and (4.3) is `1.165679704597...`.

## 5. Application to the named partner's current branch split

The account03/B06 r21 physical-minor branch is already closed by the actual inequality

`||p_Q||_infinity < 9.25/sqrt(|a|gamma)`.                           (5.1)

Theorem 3.1 supplies a complementary payment for the branch where the residual is reduced **exactly, without spectral truncation**, to one grouped hyperbolic direction plus the genuine outer product-coordinate square. In the r21 normalization `h_1 h_2>(4/5)gamma^2` implies `h_1>(2/sqrt(5))gamma`; hence an exact rank-one grouped certificate with `|d|>=h_1` would give

`||p_Q||_infinity
 < 4 sqrt(2e) sqrt(sqrt(5)/2) / sqrt(|a|gamma)
 < 9.87 / sqrt(|a|gamma).`                                         (5.2)

Equation (5.2) is a real conditional inequality, not a claim that the certificate has already been forced. The live correction against dropping a nonzero spectral tail remains binding.

The first unpaid implication is therefore sharper:

`QFORM-WEDGE-DIFFUSE-THIRD-DIRECTION-PAYMENT-v1` — in the r21 wedge-diffuse survivor, either (i) manufacture an exact product-preserving one-hyperbolic-plus-one-square representation to which Theorem 3.1 applies, or (ii) retain the small higher-rank tail in a grouped spectral-window estimate with residual exponent strictly above the square-kernel threshold. A merely small opposite self-block or a truncation to the top singular direction is not valid.

## 6. Exact check and integrity

The deterministic checker `CHECK.py` uses exact rational arithmetic for `eps=1/8` to verify the factorization matrix, orthogonality/equal norm of the two factor vectors, and therefore the nonzero spectrum `+/-4097/64` together with the independent `+1` square direction. `CHECK_OUTPUT.txt` terminates with `QFORM_B06_THIRD_SQUARE_CHECK_PASS` and records the numerical bounds. The analytic proof above does not depend on the finite check.

No FEI, installation, benchmark, email, notification, task, permission, public-release, paid-model/API, Drive, or remote-workflow action was taken.
