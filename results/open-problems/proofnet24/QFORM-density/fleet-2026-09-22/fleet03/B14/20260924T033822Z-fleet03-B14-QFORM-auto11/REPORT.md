SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T03:38:22Z.
attacking: overlap-through-the-square localization: keep a transverse original/product-bank hub inside the square vertex while averaging a source-disjoint random slope, uniformly over translations, fragments and unbounded supports.

# fleet03/B14 — transverse-vertex random-slope localization

Run: `20260924T033822Z-fleet03-B14-QFORM-auto11`.

Status: **NEW SCOPED SUPPORTING THEOREM / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Scope and correction ledger

The owner target remains the unrestricted statement: independent real input coordinates with density cap one, arbitrary real symmetric `A`, at least three eigenvalues of modulus at least one, and one universal output-density cap. No moment, support, connected-support, log-concavity, Gaussian, iid, or spectral-coordinate independence hypothesis is used below.

This run retains the live corrections forbidding law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, conditional-cap-as-independence, fixed support diameter/fragment count, interval-only rough-hub transfer, and bare reciprocal-pivot payment. In particular, the argument below never rotates the product law and never normalizes a remote fragment.

A nearby completed source is the interactive mixed-square receiver

`yspennstate/math-open-problems@c1d2f72c5206c55f41c229457b6407d9e23c0b`
`proofnet24/QFORM-density/interactive/20260923T211300Z-hub-square-receivers/REPORT.md`, Section 2.

That theorem treats

`a H_1^2 + b(Y) H_1 + d(Y) H_2 + R(Y)`

with the square-hub coefficient independent of the transverse hub `H_2`. The present theorem keeps the same scale-quality endpoint while allowing the square vertex to depend arbitrarily on that transverse hub. This is the overlap created when a physical square is completed before the transverse affine resource is paid.

The designated partner theorem actually used is fleet04/B14 r10,

`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

It states that an invertible physical three-coordinate principal block `B`, with `sigma=min |lambda(B)|`, gives the translation/tail/fragment-uniform bound `6 sqrt(pi)/sigma`.

## 2. Main theorem

### Theorem `QFORM-TRANSVERSE-VERTEX-RANDOM-SLOPE-LOCALIZATION-v1`

Let `W,U,Z` be mutually independent. Assume `W,U` have Lebesgue densities satisfying

`||p_W||_infinity <= K_W`,   `||p_U||_infinity <= K_U`.

Let `D=D(Z)` be a real random variable whose marginal law has a Lebesgue density with

`||p_D||_infinity <= M < infinity`.

No independence is assumed between `D(Z)` and any other function of `Z`. Let `Phi(U,Z)` be an arbitrary finite measurable real function and let `R(Z)` be an arbitrary finite measurable real function. For `a!=0`, define

`Q = a (W + Phi(U,Z))^2 + D(Z) U + R(Z)`.            (2.1)

Then `Q` is absolutely continuous and

`boxed: ||p_Q||_infinity,ess <= 4 sqrt(2) K_W sqrt(K_U M/|a|).`     (2.2)

Equivalently, if `D=2S` and `||p_S||_infinity<=M_S`, then

`boxed: ||p_Q||_infinity,ess <= 4 K_W sqrt(K_U M_S/|a|).`          (2.3)

The constants are independent of the locations of the laws, the number and separation of support fragments, support diameter, tails, and every moment.

### Proof

Fix `(u,z)` and write `h=Phi(u,z)`. Translation of `W` preserves its density cap. For either sign of `a`, the random variable

`V=a(W+h)^2`

is absolutely continuous away from the single critical value, with the standard two-branch formula. Pointwise almost everywhere,

`p_{V|u,z}(v)
 <= K_W |a|^(-1/2) |v|^(-1/2) 1_{a v>0}`.             (2.4)

Indeed, when `a>0`, the two inverse branches contribute

`[p_W(-h+sqrt(v/a))+p_W(-h-sqrt(v/a))]/(2 sqrt(a v))`

for `v>0`, and the cap `K_W` gives (2.4); reflection handles `a<0`.

Now fix `z` with `d=D(z)!=0`. Such `z` have full probability because `D` has a density. The scaled variable `dU` has a probability density `g_d` with

`||g_d||_infinity <= m_d := K_U/|d|`.                 (2.5)

For an output value `s`, condition first on `U` and apply (2.4). Then

`p_{Q|Z=z}(s)
 <= K_W |a|^(-1/2)
    integral_{a(s-R(z)-v)>0}
    |s-R(z)-v|^(-1/2) g_d(v) dv`.                    (2.6)

The location `Phi(U,z)` has disappeared from the upper bound: it only translated the square before its one-sided critical kernel was formed. This is the key overlap-preserving step.

For every probability density `g<=m` and every `t`, the one-sided bathtub inequality is

`integral_{v<t} (t-v)^(-1/2) g(v) dv <= 2 sqrt(m)`,    (2.7)

and identically on the other half-line. To verify (2.7), the decreasing kernel is maximized by saturating the cap `m` on the interval of length `1/m` adjacent to the singularity; the resulting integral is

`m integral_0^(1/m) r^(-1/2) dr = 2 sqrt(m)`.

Equations (2.5)-(2.7) therefore give, uniformly in the output target and in every other feature of `z`,

`||p_{Q|Z=z}||_infinity
 <= 2 K_W sqrt(K_U/(|a| |D(z)|)).`                   (2.8)

It remains to average only the reciprocal square root of the random slope. If a real random variable `T` has probability density bounded by `M`, the symmetric bathtub estimate gives

`E |T|^(-1/2)
 <= M integral_{-1/(2M)}^(1/(2M)) |t|^(-1/2) dt
 = 2 sqrt(2M).`                                       (2.9)

This estimate is translation-uniform and requires no moment. Averaging (2.8) over `Z`, while allowing `D` and `R` to be arbitrarily correlated, gives

`||p_Q||_infinity,ess
 <= 2 K_W sqrt(K_U/|a|) E|D|^(-1/2)
 <= 4 sqrt(2) K_W sqrt(K_U M/|a|)`,                  (2.10)

which is (2.2). If `D=2S`, scaling gives `||p_D||_infinity<=M_S/2`, and (2.3) follows. The conditional square laws are absolutely continuous and the finite mixture bound constructs an absolutely continuous output law. QED.

## 3. Why the residual hypothesis is the right boundary

The theorem permits the square vertex `Phi(U,Z)` to depend arbitrarily on the transverse hub `U`, but it requires the additive residual outside that square to be `R(Z)`, not a completely arbitrary `R(U,Z)`.

This is not cosmetic. The proof pays the affine map `U -> D(z)U` by the one-sided Riesz integral. If an arbitrary `U`-dependent residual were admitted, it could cancel that affine map before the singularity is averaged. For example `R(U,z)=-D(z)U` would reduce (2.1) to the translated square alone, whose density need not be bounded. Thus (2.2) is a genuine overlap theorem with an explicit structural boundary, not an arbitrary-joint coarea assertion.

## 4. Product-bank compiler and zero translation tax

Suppose the variables arise from three pairwise disjoint original-coordinate product banks:

`W = w dot X_I`,   `U = u dot X_J`,   `S = s dot X_K`,

with `I,J,K` disjoint. The one-dimensional product-projection cap previously used and proved in this B14 line is

`C(v)=min{ ||v||_infinity^(-1), sqrt(2) ||v||_2^(-1) }`,           (4.1)

with the obvious convention when a component vanishes; see the pinned B14 aggregate-row report

`yspennstate/math-open-problems@34b68b60ef29a9fbac49e9d16663592fc1f7917b`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T203535Z-fleet03-B14-QFORM-auto11/REPORT.md`.

Therefore any form

`Q = a (W + Phi(U,X_K))^2 + 2 U S + R(X_K)`             (4.2)

satisfies

`boxed: ||p_Q||_infinity,ess
 <= 4 C(w) sqrt( C(u) C(s) / |a| ).`                    (4.3)

This is uniform even when all three vectors are completely diffuse. No individual coefficient has to be bounded away from zero.

Translations cost exactly zero in the literal sense relevant to this assignment. A translation of `W` is absorbed into `Phi`; a translation `U -> U+t` changes `R(Z)` by the allowed term `-tD(Z)`; and translating a linear slope projection `S` changes it by a constant while preserving its density cap. No support truncation, moment comparison, or bounded-diameter surrogate is introduced.

Remote fragments and unbounded support likewise cost zero because (2.4)-(2.10) depend only on density caps and total mass. The bathtub bounds already optimize over arbitrary measurable support geometry.

## 5. Exact-target diffuse three-bank family

Take three disjoint size-`m` product banks and unit coefficient vectors

`w=u=s=m^(-1/2) (1,...,1)`

on their respective banks. Put

`W=w dot X_I`, `U=u dot X_J`, `S=s dot X_K`,

and consider

`Q_m = W^2 + 2 U S`.                                   (5.1)

On the deterministic orthonormal span of the three bank directions, the matrix is

`diag(1) direct_sum [[0,1],[1,0]]`,

so its nonzero spectrum is exactly

`{1,1,-1}`.                                             (5.2)

Thus (5.1) is inside the exact owner target for every `m`. The projection caps in (4.1) are at most `sqrt(2)`, so (4.3) gives

`boxed: ||p_{Q_m}||_infinity,ess <= 8`                  (5.3)

for every `m` and every admissible cap-one product law.

This is genuinely a bank-first localization. A physical triple containing one coordinate from each bank has principal matrix

`(1/m) [[1,0,0],[0,0,1],[0,1,0]]`,

whose minimum absolute eigenvalue is `1/m`. Other triples missing one of the active banks are singular. Hence a physical-triple receiver can deteriorate with `m`, while (5.3) remains constant because the original-coordinate banks are aggregated before reciprocal scale is paid.

## 6. An overlapping-vertex exact-target family with constant 2

The scope extension is visible already in three original coordinates. Let `W,U,S` be arbitrary independent cap-one variables and let

`Q_* = 2(W+U)^2 + 4 U S
      + ell_W W + ell_U U + ell_S S + c`,                (6.1)

with arbitrary deterministic affine coefficients. Completing only the `W` square gives

`Q_*
 = 2(W+U+ell_W/4)^2
   + [4S + ell_U-ell_W] U
   + ell_S S + c - ell_W^2/8`.                           (6.2)

Thus (2.2) applies with

`a=2`, `K_W=K_U=1`, `D=4S+ell_U-ell_W`, `M=1/4`.

Consequently

`boxed: ||p_{Q_*}||_infinity,ess <= 2`                   (6.3)

uniformly in every affine translation and in all admissible laws.

The homogeneous matrix of (6.1), in order `(W,U,S)`, is

`A_*=[[2,2,0],[2,2,2],[0,2,0]]`.                         (6.4)

Its characteristic polynomial is

`lambda^3-4 lambda^2-4 lambda+8`.                        (6.5)

The polynomial changes sign on `(-2,-1)`, `(1,2)`, and `(4,5)`; since `A_*` is real symmetric these are its three real eigenvalues. Hence every eigenvalue has modulus strictly larger than one, so (6.1) is a literal full-target chamber, not a two-eigenvalue control.

The coefficient of the `W` square in (6.1) depends on the transverse hub after completion (`Phi=U+ell_W/4`), which is exactly the overlap absent from the older Section-2 mixed-square formulation.

## 7. Designated fleet04/B14 result applied at an actual inequality

Apply fleet04/B14 r10 to the same physical matrix `A_*`. Let

`sigma_* = min |lambda(A_*)|`.

By the sign brackets in Section 6, `sigma_*>1`. The partner theorem gives, for the same arbitrary cap-one inputs and the same affine terms,

`||p_{Q_*}||_infinity,ess <= 6 sqrt(pi)/sigma_* < 6 sqrt(pi).`     (7.1)

The new localization theorem gives (6.3), so on this actual target matrix the two proved receivers yield the concrete combined inequality

`boxed: ||p_{Q_*}||_infinity,ess
 <= min{ 2, 6 sqrt(pi)/sigma_* } = 2.`               (7.2)

This is a literal use of the completed designated partner result at the displayed form, not a generic citation.

For a scale-comparison control, on `aW^2+cUS` the partner block has eigenvalues `{a,|c|/2,-|c|/2}` and therefore r10 gives

`6 sqrt(pi) / min{|a|,|c|/2}`,

while Theorem 2 gives

`4 sqrt(2)/sqrt(|ac|)`.

Both are valid; the second is better in the balanced large-scale chamber because it pays the square and random slope multiplicatively rather than through the smallest physical eigenvalue.

## 8. Continuity ledger

Theorem 2 proves absolute continuity and an essential `L^infinity` bound. It does **not** claim continuity for arbitrary `Phi(U,Z)`.

If `Phi` is independent of `U`, i.e. `Phi=Phi(Z)`, then conditional on `Z=z` the output is a convolution of the translated-square density with the density of `D(z)U`. For `D(z)!=0` this convolution belongs to `C_0`. The envelope in (2.8) is integrable in `z` by (2.9), so dominated convergence shows that the unconditional density is in `C_0` with the same height bound. Thus continuity is proved on that non-overlapping subbranch only.

For the genuinely overlapping family (6.1), this report records only the essential-height conclusion. Full-target continuity remains a separate open issue.

## 9. What this does and does not close

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new theorem closes a specific localization interface: a transverse independent hub may participate arbitrarily in the *vertex of a paid physical/product-bank square* while the same transverse hub is used linearly against a source-disjoint random slope. Arbitrary shifts, fragments and unbounded supports incur no constant loss.

It does not show that `s_3(A)>=1` always forces such a decomposition. In a generic Schur elimination, the residual can contain an additional genuinely `U`-dependent quadratic term outside the completed square; that term lies beyond Theorem 2 unless another receiver pays it. The next B14 implication is therefore structural/analytic: combine the generic strict-margin closure from the previous run with a product-bank choice for which either the transverse Schur self-curvature vanishes/is paid by an existing definite receiver, or the random-slope Riesz mechanism can be upgraded without allowing arbitrary cancellation of the affine `U` resource.

No Gaussian, log-concavity, moment, compact-support, connected-support or diagonal-basis assumption was introduced.
