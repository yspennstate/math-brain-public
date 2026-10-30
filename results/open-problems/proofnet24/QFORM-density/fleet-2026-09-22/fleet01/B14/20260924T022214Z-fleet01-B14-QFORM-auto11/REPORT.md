SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-24T02:22:14Z.
attacking: two-sided mass-homogeneous overlap localization — preserve full unnormalised mass simultaneously through arbitrary translated slice fragments and arbitrary translated slope fragments, then apply fleet02/B14's completed theorem to a strict target family.

# fleet01/B14 — two-sided overlap localization

Run: `20260924T022214Z-fleet01-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Status: **NEW SUPPORTING LOCALIZATION THEOREM + STRICT FULL-TARGET APPLICATION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN. Nothing below assumes moments, bounded support, connected support, finite fragment count, centering, log-concavity, post-rotation independence, or uniform pointwise quadratic Fourier decay.

## 1. Completed designated-partner result used

The completed fleet02/B14 source used in this report is

- source snapshot: `yspennstate/math-open-problems@0adab5e8aa852db2831d712bc820c9ea347b79ae`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260924T020607Z-fleet02-B14-QFORM-auto11/REPORT.md`;
- theorem: `QFORM-OVERLAP-SLOPE-SUBPROBABILITY-HOMOGENEITY-v1`.

Its input is a probability variable `X` with density at most one, an independent probability slice law `(L,Y)` with disintegration

`P((L,Y) in dl dy)=nu_l(dy) dl`,

and frozen transforms

`F_t(l)=int exp(i t y) nu_l(dy)`,
`ess sup_l |F_t(l)| <= A |t|^(-1/2)`.

For an independent slope-bank positive measure `tau` of mass `m`, if `S_#tau` has density cap `M` and `R` is arbitrary, the output finite measure of

`Q=H(X)+2XL+Y+2XS(Z)+R(Z)`

has continuous density satisfying

`||p_Q^(tau)||_infinity <= 5 pi^(-1/5) A^(2/5) m^(3/5) M^(2/5)`.       (1.1)

The proof keeps the whole slope bank through a second Plancherel step. I use that exact mechanism and constant below.

## 2. New theorem: two-sided subprobability homogeneity

### Theorem `QFORM-OVERLAP-TWO-SIDED-SUBPROBABILITY-HOMOGENEITY-v1`

Let `X` have a probability density `f_X<=1`. Let `mu` be a finite positive measure on `(L,Y)` of total mass

`n=mu(R^2)`, `0<n<=1`,

independent of `X`, and suppose

`mu(dl,dy)=nu_l(dy) dl`,
`int nu_l(R) dl=n`.

For `t!=0`, set

`F_t(l)=int exp(i t y) nu_l(dy)`

and assume

`ess sup_l |F_t(l)| <= A |t|^(-1/2)`.                               (2.1)

Let `tau` be a finite positive measure on a second independent bank `Z`, of total mass `m`, `0<m<=1`. Let `S=S(Z)` and `R=R(Z)` be arbitrary measurable functions. Suppose the positive pushforward `S_#tau` has a Lebesgue density bounded by `M`.

Let `eta` be the unnormalised output measure of

`Q=H(X)+2XL+Y+2XS(Z)+R(Z)`.                                         (2.2)

Then `eta` has a continuous `C_0` density and

`boxed:
 ||p_eta||_infinity
 <= 5 pi^(-1/5) A^(2/5) M^(2/5) (nm)^(3/5).`                       (2.3)

The estimate is uniform in translations, in `H`, and in the arbitrary phase `R`.

### Proof

Define

`G_t(x)=int exp(2itxl) F_t(l) dl`.

Because `|F_t(l)|<=nu_l(R)`, (2.1) gives

`int |F_t(l)|^2 dl
 <= [ess sup_l |F_t(l)|] int |F_t(l)| dl
 <= A |t|^(-1/2) int nu_l(R) dl
 = A n |t|^(-1/2).`                                                  (2.4)

With the Fourier convention used by the partner, Plancherel after `xi=2tx` yields

`||G_t||_2^2
 = (pi/|t|) int |F_t(l)|^2 dl
 <= pi A n |t|^(-3/2),`                                             (2.5)

hence

`||G_t||_2 <= sqrt(pi A n)|t|^(-3/4).`                              (2.6)

Next push the complex measure `exp(itR(z)) tau(dz)` forward by `S`. Call its density `g_t`. Its total variation is dominated by the positive measure `S_#tau`, so

`||g_t||_1 <= m`, `||g_t||_infinity <= M`,

and therefore

`||g_t||_2^2 <= m M`.                                                (2.7)

Define

`K_t(x)=int exp(2itxs) g_t(s) ds`.

A second Plancherel identity gives

`||K_t||_2^2 <= pi m M |t|^(-1)`,
`||K_t||_2 <= sqrt(pi m M)|t|^(-1/2).`                              (2.8)

The exact hub-level factorisation is

`eta_hat(t)=int f_X(x) exp(itH(x)) G_t(x)K_t(x) dx`.

Since `0<=f_X<=1`, Cauchy--Schwarz and (2.6),(2.8) give

`|eta_hat(t)|
 <= pi sqrt(A M n m)|t|^(-5/4).`                                   (2.9)

The total mass of `eta` is `nm`, so also

`|eta_hat(t)|<=nm`.                                                  (2.10)

For every `B,C>0`, direct integration at the threshold `(C/B)^(4/5)` gives

`int_R min(B,C|t|^(-5/4)) dt = 10 C^(4/5) B^(1/5).`                (2.11)

Substituting `B=nm` and `C=pi sqrt(A M n m)` into (2.11), followed by Fourier inversion, gives exactly

`(1/(2pi))*10*[pi sqrt(A M n m)]^(4/5)*(nm)^(1/5)
 =5 pi^(-1/5)A^(2/5)M^(2/5)(nm)^(3/5)`.

This proves (2.3), and the integrable Fourier transform gives a continuous density vanishing at infinity. QED.

## 3. Exact double-fragment localization compiler

Suppose the slice law and slope law are decomposed into arbitrary countable positive pieces

`mu=sum_j mu_j`, `mu_j(R^2)=n_j`, `sum_j n_j=1`,
`tau=sum_k tau_k`, `tau_k(Omega)=m_k`, `sum_k m_k=1`.

Let `A_j` be the frozen-slice constant for `mu_j`, and `M_k` the positive slope-density cap for `S_#tau_k`. The theorem applied to each `(j,k)` cell gives

`||p_jk||_infinity
 <=5 pi^(-1/5) A_j^(2/5) M_k^(2/5)(n_jm_k)^(3/5).`                 (3.1)

Therefore the exact zero-tax hypotheses are

`A_j <= A_0 n_j`,
`M_k <= M_0 m_k`.                                                    (3.2)

Indeed, (3.1) becomes

`||p_jk||_infinity
 <=5 pi^(-1/5)(A_0M_0)^(2/5)n_jm_k`,                               (3.3)

and summing all positive cell densities yields

`boxed:
 ||p_Q||_infinity
 <=5 pi^(-1/5)(A_0M_0)^(2/5),`                                     (3.4)

which is exactly the unsplit whole-law constant. There is no dependence on the number of pieces, their locations, their separation, support diameter, or moments.

More generally, if

`A_j<=A_0 n_j^alpha`, `M_k<=M_0 m_k^beta`,

then the positive cell compiler carries mass powers

`n_j^((3+2alpha)/5) m_k^((3+2beta)/5)`.                            (3.5)

Thus linear unnormalised mass homogeneity `alpha>=1`, `beta>=1` is the exact threshold for arbitrary positive refinement without a partition-count tax. For `N` equal pieces on one side the certificate costs `N^[2(1-alpha)/5]`; if both sides are split into `N` equal pieces with `alpha=beta=0`, the purely positive certificate costs `N^(4/5)`. This is a proof-interface barrier, not a counterexample to QFORM.

## 4. Arbitrary translated-fragment corollary

The hypotheses (3.2) hold automatically for arbitrary translation mixtures when the smoothing source is retained before normalisation.

### 4.1 Slice side

Let `(L_0,Y_0)` be a probability slice source with

`ess sup_l |F_t^0(l)| <= A_0 |t|^(-1/2)`.

Let `T` be any independent random element, with no support or moment assumption, and let `a(T),b(T)` be arbitrary measurable real functions. Define

`L=L_0+a(T)`, `Y=Y_0+b(T)`.

For an arbitrary positive fragment `rho_j` of the law of `T`, of mass `n_j`, the unnormalised frozen transform is

`F_{t,j}(l)
 =int exp(it b(u)) F_t^0(l-a(u)) rho_j(du)`.

Hence

`ess sup_l |F_{t,j}(l)| <= n_j A_0 |t|^(-1/2)`,                    (4.1)

independently of how far the translations move or how fragmented/unbounded their support is.

### 4.2 Slope side

Let `S_0` be an independent real source with density cap `M_0`. Let `U` be arbitrary and independent, and set

`S=S_0+c(U)`.

For an arbitrary positive fragment `sigma_k` of the law of `U`, of mass `m_k`,

`S_#sigma_k = p_{S_0} * (c_#sigma_k)`,

so

`||p_{S_#sigma_k}||_infinity <= M_0 m_k`.                           (4.2)

Any additional phase `R(S_0,U)` is free in the overlap theorem because the phase-weighted slope pushforward is dominated in total variation by this positive pushforward.

Combining (4.1),(4.2) with (3.4) proves simultaneous zero-tax localization of arbitrary countable translation fragments on both sides. No bounded diameter, bounded fragment count, moment, or centering assumption enters.

## 5. Actual strict-target application of the completed fleet02/B14 theorem

Take mutually independent real variables/vectors

`X, L_0, Z_0, Y, T=(T_1,...,T_r), U=(U_1,...,U_s)`

with every original coordinate having a probability density at most one, and take specifically

`Y ~ Uniform[-1/2,1/2]`.

The laws of `T` and `U` may be arbitrarily translated, disconnected and unbounded, with no moments. Let `a,c,d` be arbitrary deterministic vectors and `B,D` arbitrary real symmetric matrices. Consider

`Q = 2X(L_0+a^T T+Z_0+c^T U)
     +Y^2+T^TBT+U^TDU+2Z_0 d^T U.`                                 (5.1)

This is an actual quadratic form in the original independent coordinates.

### Slice certificate

Use

`L=L_0+a^T T`,
`Y_phase=Y^2+T^TBT`.

Let

`I(t)=int_{-1/2}^{1/2} exp(it y^2) dy`.

The completed fleet02/B14 stress calculation proves

`|I(t)|<=4|t|^(-1/2)`.                                              (5.2)

Since the density of `L_0` is at most one,

`F_t(l)
 = I(t) E[ f_{L_0}(l-a^TT) exp(it T^TBT) ]`

satisfies

`ess sup_l |F_t(l)|<=4|t|^(-1/2)`.                                 (5.3)

Thus the fleet02/B14 theorem is being applied with the actual slice constant

`A=4`.

For every arbitrary positive fragment of the `T` law of mass `n_j`, the same equation gives the stronger unnormalised relation `A_j<=4n_j`.

### Slope certificate

Use the independent slope bank `(Z_0,U)` with

`S=Z_0+c^TU`,
`R=U^TDU+2Z_0d^TU`.

Because `Z_0` itself has density cap one,

`p_S(s)=E f_{Z_0}(s-c^TU) <=1`,                                    (5.4)

so the partner theorem has the actual slope cap

`M=1`,

regardless of `c,D,d`, the dimension of `U`, or its support/tails. For every positive fragment of the `U` law of mass `m_k`, the unnormalised cap is `M_k<=m_k`.

### Density inequality

Substituting `A=4`, `M=1` into the completed fleet02/B14 overlap-slope theorem gives directly

`boxed:
 ||p_Q||_infinity
 <= 5 pi^(-1/5) 4^(2/5)
 = 6.924111078456212... .`                                         (5.5)

Moreover the density is continuous and vanishes at infinity. Applying the two-sided compiler to arbitrary simultaneous `T`- and `U`-fragment decompositions gives **the identical constant (5.5)**, not a fragment-count or separation-dependent bound.

### Exact target check

In the original coordinates `(X,L_0,Z_0,Y)`, the retained principal block of the homogeneous matrix of (5.1) is

`A_* = [[0,1,1,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,1]].`                                                (5.6)

Its spectrum is

`spec(A_*)={sqrt(2),1,0,-sqrt(2)}.`                                 (5.7)

Therefore this principal block alone has three eigenvalues of modulus at least one. By Cauchy interlacing, every ambient matrix in (5.1), for arbitrary `a,c,d,B,D`, lies inside the owner's exact three-large-eigenvalue target. Thus (5.5) is a genuine full-target-family inequality, not merely a diagonal/projection control.

The family is indefinite and off-diagonal, and both translated banks may be arbitrarily high-dimensional and diffuse. The result does not use moments or bounded supports.

## 6. What this resolves and what remains open

This run resolves a specific localization interface: when an overlap receiver already has one source-valid half-order slice certificate and one source-valid slope-density certificate, arbitrary translation mixtures and arbitrary countable remote fragments on **both** sides can be retained with exactly zero tax if the unnormalised certificate parameters carry their natural linear mass. Normalising active fragments before the Plancherel payment is unnecessary and can create an artificial positive power of the fragment count.

This does **not** solve the unrestricted QFORM theorem. From the bare hypothesis `s_3(A)>=1`, one still has to force a product-preserving overlap decomposition with universally controlled whole-law slice and slope certificates, or enter another completed fleet chamber. General quadratic cross-couplings between the two translated banks are not covered by the factorisation used here. The rough-law structural extraction problem therefore remains explicit.

## 7. Integrity / scope guards

- Full unrestricted QFORM: **OPEN**.
- Uniform pointwise quadratic Fourier decay: not used; known false.
- No post-rotation independence is asserted.
- No arbitrary-joint coarea cap is used.
- No fixed fragment-count or bounded-diameter localization is asserted.
- No interval-only estimate is promoted to an arbitrary Borel profile.
- No moment or support hypothesis is hidden in the translation compiler.
- The fleet02/B14 result is applied at equations (5.3)--(5.5), with its exact hypotheses checked.
