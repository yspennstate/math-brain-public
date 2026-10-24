SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T11:04:01Z.
attacking: decouple before rough localization — prove that arbitrary fragments of one duplicated coordinate copy become mass-homogeneous cap-one difference laws, then apply the fixed-source volume receiver without fragment tax.

# account02/B14 — one-copy difference localization before Brascamp–Lieb payment

Status: **NEW SUPPORTING LOCALIZATION THEOREM + SOURCE-VALID PROOF-INTERFACE OBSTRUCTION; FULL QFORM OPEN; CONTINUITY SEPARATE.**

The target remains: independent real coordinates with probability densities at most one and an arbitrary real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, support, connectedness, log-concavity, bounded-fragment, post-rotation-independence, or diagonal-basis hypothesis is introduced below.

## First unpaid implication

`QFORM-DIFFERENCE-SIDE-LOCALIZE-OR-KEEP-OSCILLATORY-SIDE-WHOLE-v1`:

> Once a decoupled D/D′/D5/projected-crossing receiver has been exposed, route arbitrary rough spatial localization to only one duplicated **difference-side** copy and extract the true submass before any Brascamp–Lieb/Hausdorff–Young norm. If a structural branch genuinely requires localizing the oscillatory-side source before its characteristic-function norm, or normalizing both copies simultaneously, this compiler does not pay that step; another whole-law receiver or a different product-preserving partition is still needed.

The point proved here is that support fragmentation itself is free on the difference side. The whole undecomposed copy automatically repairs every localized fragment back to density cap one.

## 1. One-copy difference localization theorem

### Theorem — `QFORM-ONE-COPY-DIFFERENCE-LOCALIZATION-v1`

Let `f` be a probability density on `R` with `0<=f<=1`. Let `rho` be any nonnegative integrable function of mass

`m = int rho`, `0<m<=1`.

Define the finite difference density

`G_rho(w) = int_R f(w+y) rho(y) dy = (f * tilde(rho))(w)`.

Then

`int_R G_rho(w) dw = m`,

and, pointwise,

`0 <= G_rho(w) <= int rho = m`.

Consequently

`gamma_rho(w) := G_rho(w)/m`

is a probability density satisfying

`boxed{ ||gamma_rho||_infinity <= 1. }`                                      (1.1)

No property of `rho` other than positivity and its mass was used. In particular (1.1) is uniform over arbitrary translations, remote fragments, unbounded supports, countably many components, infinite BV, and laws with no moments.

Now let

`f = sum_a rho_a`

be any finite or countable positive decomposition, with masses `m_a=int rho_a`. Tonelli gives the exact identity

`boxed{ f * tilde(f) = sum_a m_a gamma_a, }`                                (1.2)

where every `gamma_a` is a cap-one probability density and `sum_a m_a=1`.

The same statement holds for a soft/randomized localization: if measurable `theta_a>=0` satisfy `sum_a theta_a=1`, put `rho_a=f theta_a` and repeat the argument.

### Product version

For independent coordinates `f_j<=1`, decompose only one copy in each coordinate,

`f_j = sum_a rho_{j,a}`, `m_{j,a}=int rho_{j,a}`.

Then

`tensor_j (f_j * tilde(f_j))
 = sum_alpha m_alpha tensor_j gamma_{j,alpha_j}`,                         (1.3)

where

`m_alpha = prod_j m_{j,alpha_j}`, `sum_alpha m_alpha=1`,

and every factor `gamma_{j,alpha_j}` is a probability density bounded by one. Thus an arbitrary finite or countable product localization of one duplicated copy becomes an **exact convex mixture of admissible cap-one product difference laws**.

This is the desired mass homogeneity. Normalizing a tiny source fragment would ordinarily raise its density cap by `1/m`; after differencing against the whole copy, its unnormalized difference density is itself at most `m`, so the normalization loss cancels exactly.

### Slope corollary

Conditioned on any localization label `alpha`, the difference coordinates remain independent and cap one. Hence for every coefficient vector `a`, the standard Ball–Rogozin bound yields

`boxed{ ||p_{a^T W | alpha}||_infinity <= sqrt(2)/||a||_2. }`              (1.4)

So after one-copy differencing the undecomposed copy acts as a distributed whole-bank anchor. There is no fragment-count, fragment-mass, translation, diameter, or tail factor in the conditional slope cap.

## 2. Exact interface with the fixed-source decoupling theorem

The required fixed source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

proves Theorem D. For disjoint original-coordinate sets `I,J`, with `M=A_IJ`,

`Z=e_3(M^T M)`,

and volume-sampling row marginals at most `1/2`, it gives

`boxed{ ||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6). }`                         (2.1)

The proof first decouples on the `J` variables. Its right side is linear in the product law of

`W=X_J-X'_J`,

and after decoupling uses only that each coordinate density of `W` is a probability density at most one. Diagonal/self blocks and arbitrary affine terms disappear or remain harmless exactly as stated in the source.

Apply (1.3) to **only the copied variables** `X'_J`. If `R_alpha(t)` denotes the decoupled majorant for localization label `alpha`, Theorem D's Brascamp–Lieb calculation applies to every normalized conditional `W` law with exactly the same `M,Z` and volume marginals. Hence

`R_alpha(t) <= C_D(t)`

uniformly in `alpha`, and linearity before the square root gives

`|phi_Q(t)|^2 <= sum_alpha m_alpha R_alpha(t) <= C_D(t) sum_alpha m_alpha = C_D(t)`.   (2.2)

Therefore **any arbitrary one-copy localization of the difference-side coordinates is zero-tax for Theorem D**. The same argument applies verbatim to D′ and D5, because their source proofs have the same linear difference-law input before the Brascamp–Lieb/Holder payment.

This is stronger than normalizing each spatial fragment of the original variables: the localization label is carried through the exact decoupling identity until convolution with the whole copy has restored the cap-one class.

## 3. A target-valid matrix where the gain is explicit

Let `I` contain six coordinates and `J` three. Put

`M = (1/sqrt(2)) * [[1,0,0],
                    [1,0,0],
                    [0,1,0],
                    [0,1,0],
                    [0,0,1],
                    [0,0,1]]`

and

`A = [[0,M],[M^T,0]]`.

Then

`M^T M=I_3`,

so the nonzero spectrum of `A` is

`{1,1,1,-1,-1,-1}`.

Thus this family is strictly inside the owner target. Moreover

`Z=e_3(M^T M)=1`.

There are exactly eight nonzero `3 x 3` row minors of `M`, obtained by choosing one of the two copies of each standard basis row. Each has squared determinant `1/8`; every one of the six rows occurs in four of the eight minors. Hence every volume-sampling row marginal is exactly

`4/8=1/2`.

The fixed-source theorem therefore gives the concrete universal inequality

`boxed{ ||p_{2 X_I^T M X_J}||_infinity <= 6 sqrt(e)
       = 9.89232762420077... . }`                                           (3.1)

This holds for completely arbitrary independent cap-one source laws, including arbitrary translated, fragmented, and unbounded supports.

## 4. Finite remote-comb obstruction to fragment-first normalization

For each of the three `J` coordinates take the cap-one density

`f_N = 1_{E_N}`,

where `E_N` is the union of `N` pairwise disjoint intervals of length `1/N`. Their locations may be arbitrarily far apart.

### Bad order: localize the original variables first

Condition each original `J` coordinate on its tooth. The normalized conditional density has height `N`. After translating the tooth to the origin and rescaling to a cap-one variable,

`X_{J,j}=c_{k_j}+N^(-1) Z_j`,

all tooth centers contribute only affine terms, but the cross block becomes

`M_N=M/N`.

Thus

`e_3(M_N^T M_N)=N^(-6)`.

The volume marginals are unchanged, so Theorem D gives only

`boxed{ ||p_{Q | tooth labels}||_infinity <= 6 sqrt(e) N. }`               (4.1)

Averaging the conditional density bounds over all labels leaves the same factor `N`. The unchanged whole law has (3.1), so this divergence is entirely proof-interface loss.

### Safe order: decouple first, localize only the copy

Instead, perform the source decoupling and localize only `X'_J`. For one tooth `I_k`, let

`rho_k=1_{I_k}`, `m_k=1/N`.

The corresponding unnormalized difference density is

`G_k(w)=int_{I_k} f_N(w+y) dy <= 1/N`,

and therefore

`gamma_k=N G_k <=1`.

For any triple of tooth labels, the normalized `W` law is again an independent cap-one product law and the matrix is still the **original** `M`. Hence each normalized contribution to the decoupled majorant has the same source bound as (3.1), and the label masses sum to one. The final result is exactly

`boxed{ ||p_Q||_infinity <= 6 sqrt(e), }`                                  (4.2)

with no dependence on `N` or on the tooth locations.

So arbitrary translations and finite remote fragmentation are genuinely free on the difference side once the proof order is correct.

## 5. Countably fragmented unbounded-support endpoint

The distinction becomes infinite rather than merely growing. Choose positive numbers

`m_k = c/[k (log(k+1))^2]`, `k>=1`,

where `c` normalizes `sum_k m_k=1`. Put the `k`th interval at an arbitrarily remote location, for example

`I_k=[4^k,4^k+m_k]`,

and set

`f_infinity = 1_{union_k I_k}`.

This is an admissible cap-one probability density with countably fragmented unbounded support and no imposed moment condition.

Conditioning the three original `J` variables on teeth `(k_1,k_2,k_3)` and rescaling them to cap-one variables replaces the cross block by

`M_{k_1,k_2,k_3}=M diag(m_{k_1},m_{k_2},m_{k_3})`.

Since `M^TM=I`,

`Z_{k_1,k_2,k_3}
 = e_3(M_k^T M_k)
 = (m_{k_1}m_{k_2}m_{k_3})^2`.

The conditional Theorem-D certificate is therefore

`6 sqrt(e) (m_{k_1}m_{k_2}m_{k_3})^(-1/3)`.

Multiplying by the cell mass `m_{k_1}m_{k_2}m_{k_3}` and summing the conditional suprema gives the fragment-first certificate

`6 sqrt(e) [sum_k m_k^(2/3)]^3`.                                          (5.1)

But

`m_k^(2/3) asymp k^(-2/3) (log k)^(-4/3)`,

and this series diverges. Hence (5.1) is `+infinity`.

For the **identical unchanged law**, the whole-source theorem (3.1) is finite, and the one-copy difference localization theorem again makes every normalized copied-tooth difference density cap one, yielding the same `6 sqrt(e)` decoupled certificate. Thus bounded diameter, finite fragment count, or tail truncation are not legitimate substitutes for the correct mass-homogeneous proof order.

This is `QFORM-FRAGMENT-FIRST-DIVERGES-BUT-DIFFERENCE-SIDE-ZERO-TAX-v1`.

It is a proof-interface obstruction, not a QFORM counterexample.

## 6. Application of the newest completed designated partner result

The newest completed compatible account03/B14 report is

`yspennstate/math-open-problems@80105e9cf5c3522438505be597f46b0605f41adf`.

It proves that a Gaussian location-scale mixture with inverse-half-variance moment `M_G` has

`Var_BV(g) <= sqrt(2/pi) M_G`.

Hence the normalized Gaussian-mixture chamber `M_G<=sqrt(2pi)` has total variation at most two, and that bound survives weak limits. For an `N`-tooth cap-one comb, any weak Gaussian-mixture approximation must satisfy

`liminf M_G >= N sqrt(2pi)`.

Thus the partner rules out uniform **pre-decoupling Gaussian regularization** of the rough owner class.

The present theorem gives a complementary positive mechanism. It does not approximate the rough marginal at all. It first invokes the exact independent-copy identity already present in the fixed-source proof and then localizes one copy. For a tooth of mass `m`, convolution with the undecomposed cap-one copy produces an unnormalized difference density bounded by exactly `m`; after division by its true mass the auxiliary difference law is cap one. Therefore the Gaussian/BV fragment penalty identified by the partner is absent from the legal post-decoupling difference law.

In particular, for the same remote `N`-tooth source, the partner's necessary Gaussian peak moment grows linearly in `N`, whereas the conditional copied-tooth difference laws entering Theorem D retain cap one for every `N`. The two statements are compatible because the latter is an exact transformed law in a decoupling proof, not a Gaussian approximation to the original marginal.

This identifies a useful architectural boundary:

`rough source -> decouple exactly -> localize one difference-side copy -> normalize true mass -> BL/HY`

is safe, whereas

`rough source -> localize original active variable -> normalize fragment -> pay inverse curvature`

or

`rough source -> uniformly regularize each marginal -> pay regularization scale`

can be arbitrarily expensive.

## 7. What this does and does not close

The new compiler removes arbitrary translations, fragment count, unbounded support, and tiny fragment masses **inside any already-exposed decoupled receiver whose only difference-law hypothesis is independent density cap one**. It is immediately compatible with fixed-source D, D′, and D5 and with analogous projected-crossing proofs having the same decoupled product-law interface.

It does **not** prove that bare `s_3(A)>=1` always admits one of those receivers with universal matrix parameters. Nor does it make it safe to localize the oscillatory-side original variables before their characteristic-function norms, or to normalize both duplicated copies. The remaining full-target debt is therefore more sharply structural: obtain a product-preserving orientation/partition that leaves the rough localization on the difference side, or exit through a different whole-law receiver before any active-fragment normalization.

Full unrestricted QFORM remains OPEN. No counterexample was found. Continuity of the unrestricted output law remains a separate question; Theorem D itself gives a continuous density in its stated chamber because its characteristic function is integrable.

## Source discipline

Fresh fixed source consumed at exact commit `e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed Theorem D was applied quantitatively in (3.1), (4.1), and (5.1), rather than merely cited.

Newest completed compatible designated partner consumed: account03/B14 `20260924T093427Z-account03-B14-QFORM-auto11`, canonical math commit `80105e9cf5c3522438505be597f46b0605f41adf`; its BV/weak-closure obstruction is used in Section 6.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Authenticated repository retrieval and readback occurred, but genuine native receiver retrieval of the exact prior QFORM checkpoint was not established. Model self-report: `GPT-5.6 Sol`. Configured reasoning effort and provider reasoning telemetry are `UNKNOWN / not exposed`; provider reasoning-token and pure-thinking-time fields are null.
