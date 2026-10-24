# account01/B14 r11 — rough-law closure for the grouped compiler and threshold status

Pinned baseline: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 recorded by the source package as `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This note does not overwrite the baseline. It closes the measure-theoretic interface needed by the complete nine-eigenvalue replacement currently in the improvement tree and records the exact multiplicity boundary reached in this run.

## 1. Complex pushforward domination for arbitrary rough laws

### Lemma 1 — dominated complex pushforward

Let `Y` be an `R^d`-valued random variable whose law is `p(y)dy`, and let `H` be any complex measurable random variable with `|H|<=1`. Define the finite complex measure

`nu(B)=E[H 1_{Y in B}]`.

Then `nu` has a measurable density `a` satisfying

`|a(y)|<=p(y)` almost everywhere.

Consequently, if `p<=M` and `int p=1`, then

`||a||_2^2 <= int p^2 <= M`.

#### Proof

For every Borel set `B`, total variation satisfies

`|nu|(B) <= E[|H|1_{Y in B}] <= P(Y in B)=int_B p(y)dy`.

Hence `|nu|` is dominated by `p(y)dy`. Radon--Nikodym gives a measurable density `a=dnu/dy`, and domination of total variation gives `|a|<=p` almost everywhere. The `L^2` estimate follows from `p^2<=Mp`. No regular conditional probability, pointwise density selection, moment or support assumption is required. QED.

This is the precise justification for pushing `e^{itF}`-weighted laws to a projection or linear image in the grouped product-Fourier proof. It applies equally when `F` contains arbitrary same-bank quadratic and affine phases.

## 2. Removing mollifiers without smoothness or support bounds

### Lemma 2 — uniform `L^2` mollifier bounds identify the original pushforward

Let `nu` be a finite complex Borel measure on `R^d`, let `rho_eps` be a standard approximate identity, and suppose

`sup_eps ||nu*rho_eps||_2 <= C`.

Then `nu=a(x)dx` for some `a in L^2` with `||a||_2<=C`. Moreover, along every sequence `eps_j downarrow0`, every weakly convergent `L^2` subsequence of `nu*rho_eps_j` has the same limit `a`.

#### Proof

The closed `L^2` ball of radius `C` is weakly compact. Choose a weakly convergent subsequence `a_j=nu*rho_eps_j -> a` in `L^2`. For every `psi in C_c^infinity`,

`int psi(x)a_j(x)dx = int (psi*tilde rho_eps_j)(y) dnu(y)`.

The convolutions converge uniformly to `psi`; since `nu` has finite total variation, the right side tends to `int psi dnu`. Weak `L^2` convergence gives the left side tending to `int psi a`. Thus `nu=a dx` as distributions and hence as finite measures. Weak lower semicontinuity gives `||a||_2<=C`. Uniqueness of the Radon--Nikodym density makes every subsequential limit equal to `a`. QED.

This closes the only potentially delicate limiting sentence in the grouped compiler. The argument is insensitive to unbounded support and does not require uniform tail control.

## 3. Conditioning-generated translations are norm-free

If an outside original-coordinate environment `Z=z` changes a linear image by a translation `u(z)`, then

`a_{t,z}(x)=a_t(x-u(z))`

has exactly the same `L^p` norms. More generally, Lemma 1 applied fiberwise gives measure domination, and a uniform fiber inequality can be integrated against the positive outside law by Tonelli. Therefore arbitrarily large or nonintegrable translations never enter the constants. This is the correct interpretation of all conditioning in the scalar/pair pivot branches and in the new grouped Fourier receiver.

No assertion of a conditional cap derived from an unconditional marginal is being made: the cap is obtained either from an original product density or from a full-rank linear image of an independent original-coordinate bank.

## 4. Zero row marginals in weighted subset Hölder

In the grouped compiler let `alpha_i=P(i in T)`. If `alpha_i=0`, then row `i` belongs to no subset of positive sampling weight and must simply be omitted before writing the exponent `1/alpha_i`. For the remaining rows, `0<alpha_i<=1/2`, so the scalar Fourier-power input at `p=1/alpha_i>=2` is valid. This is a notation cleanup only and does not alter the entropy inequality or any constant.

## 5. Application to the complete nine-eigenvalue replacement

The current replacement proof uses two marginal-free consequences of the grouped compiler:

1. for a literal original-coordinate crossing block `M`,

`E_3(M)>0  =>  ||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,

with `C_3=3 sqrt(2)e(9/2)^(1/6)<14.819`, arbitrary same-bank quadratic/affine phases retained;

2. for a literal crossing block,

`E_2(M)>0  =>  sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,

with `C_2=8 sqrt(e)2^(-1/8)<12.096`.

Lemmas 1–2 above verify that these statements remain valid for arbitrary cap-one input densities, without smoothing, compact support, moments or bounded translations.

Normalize `K=s=1`, with `eta=1/100`, `kappa=1/80^2`.

### No pivot

Under `s_9(A)>=1`, the audited baseline spectral-to-volume proposition at order three gives

`V_3(A)>=kappa^3`.

A fair original-coordinate cut therefore produces a literal cross block with

`E_3(M)>=4^(-3)kappa^3`,

so

`E_3(M)^(-1/6)<=160`.

The first receiver yields a bounded density `<2400`.

### Scalar pivot

A scalar pivot removes one original coordinate, leaving at least eight Schur directions. If the Schur complement has a pivot, the audited baseline pivot theorem gives truncated half-potential at most `600`, hence full half-potential at most `601`. If it has no pivot, it still has at least five unit directions; the baseline order-two volume proposition and random cut give

`E_2>=4^(-2)kappa^2`,

and the second receiver gives full half-potential `<153`. Thus in either case the scalar square profile gives

`||p_Q||_infinity <= 10*601 = 6010`.

### Pair pivots

A definite pair has density cap `pi/sqrt(eta)<32`. An indefinite pair leaves a Schur complement with a surviving unit-scale spectral direction; the baseline hyperbolic/logarithmic-potential estimate gives `<251`. These are measure-domination statements and remain valid for arbitrary rough laws by the fiberwise/Tonelli formulation above.

Therefore

`boxed: s_9(A)>=s>0 => ||p_(X^TAX+b^TX+c)||_infinity <=6010 K^2/s`.

The standard scaling is `Y=KX`, `Q=(s/K^2) Qtilde`.

This is the same complete nine-direction theorem independently reconstructed elsewhere in the tree; this B14 note specifically verifies that its limiting, measurable-version and conditional-kernel steps introduce no extra regularity assumptions.

## 6. Review state

The repository now contains two genuinely separate complete PASS reconstructions of the nine-direction theorem:

- account01/B16, commit `54ec2a651d854563f8db0d92c4c3426f76551786`;
- account03/B08, commit `c02a08f19d010e508578695a5906744fdbcfcd70`.

The author-side addendum at commit `fe715611a677e15c0498e2284284b540651218f5` records that these are distinct end-to-end reconstructions and that the two-review evidence requested by the owner protocol is present. A further independent complete replacement was subsequently recorded by account02/B01 at commit `3e27a438cd8beb580ca1951cb5fd264ad0241486`.

This note does not unilaterally rewrite the pinned release manuscript; release-baseline promotion remains an owner/B20 synthesis action.

## 7. Why this run stops at nine

Multiplicity eight is not closed by the current analytic machinery. A new structural theorem proves that in the remaining no-pivot `s_8>=1` branch, either the order-three disjoint volume is already large (and the density receiver pays it), or there is a quantitatively nonzero overlap-one/two-sided collar with currencies `Omega_1` and `Xi_2`.

That structural reduction is rigorous, but it does not itself give a density bound. The missing theorem is a product-preserving analytic receiver for the `Omega_1/Xi_2` collar when the common physical diagonal may be zero. Existing scalar-pivot overlap receivers divide by or otherwise spend that diagonal and therefore do not close the zero-diagonal chamber.

Hence the lowest **complete bounded-density theorem** justified in this run is multiplicity **9**. Multiplicity **8** remains an explicitly isolated open proof obligation; multiplicity **3** remains open.
