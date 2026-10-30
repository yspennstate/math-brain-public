# MOC4 fleet04/B09 — standard-channel ceiling from the same unistochastic matrix

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker/run:** fleet04/B09, `20260922T041453Z-b09-moc4-r34`  
**Assignment:** integrate the valid algebraic/geometric pieces and prove the exact remaining unitary-orbit step, including limit cases  
**Candidate:** `MOC4-STANDARD-CHANNEL-CEILING-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; the parent MOC4 target remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact live proof state consumed

Fix a support direction and write

\[
h(U)=\Re\!\left(\eta\det(D_a+UD_bU^*)\right),\qquad
H_\sigma=\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right),
\]

\[
M=\max_{\sigma\in S_4}H_\sigma,
\qquad
m=\frac1{24}\sum_{\sigma\in S_4}H_\sigma.
\]

I read the newest complete campaign-lead report available at this run, fleet03/B07 `fleet03-B07-20260922T033411Z-d2a63b2a`, scientific commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. Its `MOC4-V4-FIBER-ROOF-v1` and `MOC4-V4-PAIR-GAP-CEILING-v1` give the following exact decomposition and obstruction.

Let `V_4` be the normal Klein four subgroup of `S_4`; its six cosets are indexed by `rho in S_3`. Put

\[
B_\rho=\frac14\sum_{\sigma:\rho_\sigma=\rho}H_\sigma,
\qquad Q=\max_\rho B_\rho,
\qquad \Delta=M-Q,
\qquad d=M-m.
\]

For every true unitary, the centered support decomposes as

\[
h(U)-m=k(U)+y(U),
\]

where the `V_4` twirl kills the standard/oriented term `k` and leaves the pair-quotient term `y`. The lead proves that a genuine support violation

\[
h(U)=M+\gamma,\qquad \gamma>0,
\]

must satisfy

\[
\boxed{k(U)\ge\gamma+\Delta}. \tag{1}
\]

With the six pair-specific endpoint gaps `g_tau` and `G=sum_tau g_tau`, it also proves

\[
\boxed{\gamma\le\frac{3d-\Delta-G/2}{4}}. \tag{2}
\]

The lead's exact stress spectra leave `(2)` sharp at `gamma<=1/2` in the abstract low-frequency/twirl relaxation, so the first missing implication is explicitly to use genuine same-unitary compatibility.

I also directly consume the assigned OTHER-account partner fleet01/B07. Its exact Spin(6) stationarity report `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`, scientific commit `ebf5fd79e719931fbacc23a12ce7c06a456c0019`, supplies the genuine two-channel exterior-square objective and the complete first-order balances. Its later `MOC4-CARTAN-HESSIAN-PACKING-v1` (`proofnet24/collective-MOC4/fleet01/B07/20260922T030302Z-b07-moc4-r11/REPORT.md`) gives, on the branch where all sixteen Cartan zero-entry endpoints are target-safe, the exact one-entry curvature payments used in Section 4 below. No arbitrary bistochastic middle compound is introduced.

Finally I use fleet03/B09 `MOC4 complementary-minor/unitary compatibility`, report blob `06b56b516f3d36c9fa1e11601e775771fcf7e285`, which proves for `P=(|u_ij|^2)` and the tetrahedral sign matrix `E`

\[
\boxed{D=\frac14E^TPE}. \tag{3}
\]

This run applies `(3)` directly to the lead's standard channel rather than using it only as a background compatibility identity.

## 2. New theorem: the standard channel is already in the endpoint standard hull

For a permutation endpoint `sigma`, let `rho_sigma` be its `V_4` coset and define its standard-channel value

\[
\kappa_\sigma:=H_\sigma-B_{\rho_\sigma}. \tag{4}
\]

Put

\[
\boxed{K_{\rm std}:=\max_{\sigma\in S_4}\kappa_\sigma}. \tag{5}
\]

### Theorem — `MOC4-STANDARD-CHANNEL-CEILING-v1`

For every complex spectra `a,b`, every support direction `eta`, and every true unitary `U`,

\[
\boxed{k(U)\le K_{\rm std}.} \tag{6}
\]

Consequently every genuine support violation satisfies

\[
\boxed{0<\gamma\le K_{\rm std}-\Delta}. \tag{7}
\]

In particular, because always `K_std>=Delta`, the exact equality

\[
\boxed{K_{\rm std}=\Delta} \tag{8}
\]

is a complete certificate that this entire spectra/support-direction instance is MOC4-safe for **all** true unitaries.

### Proof

Let

\[
P=(|u_{ij}|^2).
\]

It is doubly stochastic, so choose any Birkhoff decomposition

\[
P=\sum_{\sigma\in S_4}\lambda_\sigma P_\sigma,
\qquad \lambda_\sigma\ge0,
\qquad \sum_\sigma\lambda_\sigma=1. \tag{9}
\]

The exact same-unitary identity `(3)` is linear in `P`. If `S_\sigma` denotes the three-dimensional standard-representation matrix associated to the permutation endpoint, then

\[
D=\sum_\sigma\lambda_\sigma S_\sigma. \tag{10}
\]

The lead's `k` is precisely the support coefficient paired with this standard/oriented channel. At a permutation endpoint, averaging over its `V_4` coset kills the standard representation and leaves `B_{rho_sigma}`. Hence its standard contribution is exactly

\[
k(P_\sigma)=H_\sigma-B_{\rho_\sigma}=\kappa_\sigma. \tag{11}
\]

By linearity of the standard channel in `D`, equations `(9)`-`(11)` give

\[
\boxed{k(U)=\sum_\sigma\lambda_\sigma\kappa_\sigma}. \tag{12}
\]

Therefore `k(U)` is already a convex combination of the 24 endpoint standard-channel values, proving `(6)`. If `h(U)=M+gamma`, combine `(6)` with the lead's exact lower bound `(1)`:

\[
\gamma+\Delta\le k(U)\le K_{\rm std},
\]

which is `(7)`.

For completeness, `K_std>=Delta`: choose an endpoint `sigma_*` with `H_{sigma_*}=M`. Since `B_{rho_{sigma_*}}<=Q`,

\[
\kappa_{\sigma_*}=M-B_{\rho_{\sigma_*}}\ge M-Q=\Delta.
\]

Thus `(8)` is the sharp zero-reserve case of `(7)`. QED.

### Why this is genuinely a same-unitary step

The lead's abstract sharp relaxation preserves the low-frequency `S_4` identities and all pair/fiber roofs but does not require its standard channel to arise from the same `P=|U|^2` that carries the first exterior power. Equation `(12)` is exactly that missing compatibility. It does **not** assume a common positive lift for the full `(P,R)` data; those stronger lifts are already refuted elsewhere in the campaign.

## 3. Direct closure of the lead's exact `1/2` stress direction

The campaign-lead report gives the exact simple real spectra

\[
a=(-1,2,1,0),\qquad b=(-1,1,-2,2),\qquad \eta=1. \tag{13}
\]

Its endpoint arithmetic is

\[
M=36,\qquad m=\frac{29}{6},\qquad Q=15,
\]

\[
d=\frac{187}{6},\qquad \Delta=21,
\]

and the six pair gaps are

\[
36,9,36,32,4,24,
\qquad G=141. \tag{14}
\]

Thus the lead's V4-plus-pair ceiling leaves exactly

\[
\gamma\le\frac{3d-\Delta-G/2}{4}=\frac12. \tag{15}
\]

Now compute the six Klein-fiber means and the 24 numbers `(4)` exactly. The new standard-channel maximum is

\[
\boxed{K_{\rm std}=21=\Delta}. \tag{16}
\]

Therefore `(7)` gives

\[
\boxed{\gamma\le0}. \tag{17}
\]

So this spectra/support-direction instance is fully safe for every true unitary. The lead's exact half-integer low-frequency witness is thereby proved non-unitary in the precise missing sense: it requires a standard-channel value outside the convex hull forced by the same unistochastic matrix `P`.

This is a target-level closure of one nontrivial support direction that had remained maximally sharp under the previous endpoint/fiber/pair relaxation. It is not a proof of MOC4 for arbitrary spectra.

The committed standard-library verifier reproduces `(14)`-`(17)` using only `Fraction` and exact `S_4` enumeration. Its captured output is

```text
PASS MOC4-STANDARD-CHANNEL-CEILING-v1
M = 36
m = 29/6
Q = 15
d = 187/6
Delta = 21
pair_gaps = 36,9,36,32,4,24
G = 141
lead_V4_pair_ceiling = 1/2
Kstd = 21
standard_channel_ceiling = 0
```

## 4. Named-partner strengthening on the all-zero-endpoints-safe branch

The assigned partner fleet01/B07 `MOC4-CARTAN-HESSIAN-PACKING-v1` proves that if a gap-positive global maximizer has all sixteen Cartan zero-entry endpoints target-safe, then for each selected entry `(i,j)` its exact Cartan quadratic has curvature `Gamma_ij>=0` and

\[
\Gamma_{ij}|u_{ij}|^2\ge\gamma. \tag{18}
\]

In the same genuine two-channel Spin(6) objective, let

\[
W:=\max_{\alpha,\beta}\max\{|X_{\alpha\beta}/2+K_{\alpha\beta}|,
|X_{\alpha\beta}/2-K_{\alpha\beta}|\}. \tag{19}
\]

The rank-two Cartan linear and antilinear pieces each have squared Frobenius norm `2`, so directly from the partner's two-channel energy formula

\[
0\le\Gamma_{ij}\le4W. \tag{20}
\]

Hence every entry of the same maximizing unitary obeys

\[
P_{ij}=|u_{ij}|^2\ge\varepsilon:=\frac{\gamma}{4W}. \tag{21}
\]

If `W=0`, the support is unitary-independent and no positive gap exists. Otherwise `4 epsilon<=1`. Write

\[
P=\varepsilon J+(1-4\varepsilon)P', \tag{22}
\]

where `J` is the all-ones matrix and `P'` is doubly stochastic. Since `E^TJE=0`, the standard channel has no uniform component. Applying `(12)` to `P'` therefore gives

\[
k(U)\le(1-4\varepsilon)K_{\rm std}
=\left(1-\frac\gamma W\right)K_{\rm std}. \tag{23}
\]

Combining `(23)` with `(1)` yields the strictly sharper zero-face-safe ceiling

\[
\boxed{
\gamma\le
\frac{W\,(K_{\rm std}-\Delta)}{W+K_{\rm std}}.
} \tag{24}
\]

This is a direct application of the named partner's Cartan geometry to the lead's residual standard channel. It is not an auxiliary constant substitution: it converts a target gap into a uniform positive floor on the same `P` whose standard component is responsible for `(1)`, shrinking the entire standard Birkhoff polytope toward its uniform center.

## 5. Updated compact conditional chain

For any fixed spectra/support direction:

1. The lead's V4 roof forces every genuine violation to pay `k>=gamma+Delta`.
2. This run forces the same standard channel to satisfy `k<=K_std`, hence `gamma<=K_std-Delta`.
3. Independently, the lead's six pair roofs give `(2)`. Thus every genuine violation obeys the combined exact ceiling
   \[
   \boxed{
   \gamma\le\min\left\{K_{\rm std}-\Delta,
   \frac{3d-\Delta-G/2}{4}\right\}.}
   \tag{25}
   \]
4. If all Cartan zero endpoints are safe, the named partner sharpens the first term to `(24)`.
5. If `K_std=Delta`, the support direction is solved outright for all unitaries, including zero-entry, singular-determinant, and repeated-spectrum cases, because the proof used no inverses, spectral divisions, genericity, or limiting argument.
6. In the residual case `K_std>Delta`, the unpaid target remains to use the symmetric quotient `R`, the exact stationarity equations, odd-Weyl/Plücker constraints, and/or a zero-face support identity to eliminate the now smaller positive reserve. No full-proof claim is made.

This is a materially different mechanism from the preceding B09 zero-anchor positive-lift no-go: it does not seek another lift. It uses the already-proved exact standard-channel projection of the **same** unistochastic matrix to close a previously sharp relaxation instance and reduce the general reserve.

## 6. Verification, limits, and non-claims

The verifier `verify_standard_channel_ceiling.py` uses only Python standard-library exact rational arithmetic. It enumerates all 24 permutations, the six `V_4` fibers, and the six transposition roofs for `(13)`. No numerical tolerance is used.

The theorem `(6)`-`(7)` itself is exact for arbitrary complex spectra/support directions and uses only Birkhoff's theorem plus the already-proved identity `(3)`. It remains valid at repeated spectra, zero spectral entries, singular `A+B`, reducible unitaries, and boundary unitaries. The partner refinement `(24)` is only asserted on the partner's all-zero-endpoints-safe positive-gap global-maximizer branch.

No claim of full MOC4, worldwide novelty, a common full `(P,R)` lift, or a counterexample is made. No benchmark material, held-out answer, credential, scheduler identifier, machine-local path, unrelated private data, email/Drive material, public posting, paid model/API/Codex call, remote workflow, permission change, or notification enabling was used.
