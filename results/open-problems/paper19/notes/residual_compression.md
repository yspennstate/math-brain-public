# Off-support compressed-resolvent bound: which theorem, and is the compression routine?

Agent note, 2026-06-28. This is the final technical step of the Appendix B closure
(`parts/appendix_keystone.tex`, Proposition `appB:resolvent`). Companion, read-only:
`notes/residual_locallaw.md` (the resolvent-monotonicity reduction). That note reduces the
keystone residual to a single off-support estimate; here I discharge it and am explicit about
(i) the exact published theorem invoked, (ii) the one genuine structural subtlety — the
compressed resolvent is *not* the resolvent of the compression — and (iii) whether the
application is verbatim or a benign extension. Bottom line up front: verbatim for Gaussian
entries (Wishart, [BEKYY14]); a mild, off-support-only extension of the separable anisotropic
law [KY17] for general sub-Gaussian entries, with the one nonroutine point isolated in Section 5.

## 0. Setup and normalization

Condition on the shared span `E` (dimension `m-D`); inside `E^perp ~= F^D` work with the `D-1`
disjoint projected rows. Realization (`residual_locallaw.md` lines 16-22):
```
   a_i  iid mean-0 var-1 sub-Gaussian (bounded-density) rows in F^m,  i = 1..D-1,
   A = [a_1 ... a_{D-1}]            iid-entry,  m x (D-1),
   B : F^D -> F^m  fixed isometry onto E^perp,  B^*B = I_D,  P := BB^* = P_{E^perp},
   g_i = B^* a_i in F^D,  G = B^* A = [g_1 ... g_{D-1}]   (D x (D-1)),
   Q := (1/D) G G^* = (1/D) B^*(A A^*) B   on  E^perp ~= F^D.
```
The columns `g_i` are iid and isotropic, `E[g_i g_i^* | E] = B^*B = I_D`, but the `D` entries of a
single `g_i` are NOT independent (they are a rectangular linear image `B^* a_i` of the `m`
independent entries of `a_i`). `u` is the a.s.-unique unit null vector of `Q` (rank `Q <= D-1`).

**Normalization.** The task writes `Q = GG^*`; for the Marchenko-Pastur (MP) statements to read
cleanly I use the sample-covariance scaling `Q = (1/D) GG^*` (equivalently `g_i -> g_i/sqrt D`),
so the empirical spectrum of `Q` is MP at aspect ratio `(D-1)/D -> 1` on `[0,4]`, with hard-edge
density `rho(x) = (2 pi)^{-1} sqrt((4-x)/x)` and Stieltjes transform `m`. The null vector `u` and
hence `M_E := E[u u^* | E]` are scale-invariant, so the eventual bound on `lambda_max(M_E)` does
not depend on this choice. For real `z = -eta`, `eta in (0,1)`,
```
   m(-eta) = int_0^4 rho(x)/(x + eta) dx = (1 + o(1)) eta^{-1/2}   (eta -> 0),
```
since near `x=0`, `rho(x) ~ (pi sqrt x)^{-1}` and `int_0^infty (pi sqrt x)^{-1}(x+eta)^{-1} dx =
eta^{-1/2}`. The whole hard edge enters ONLY through this one scalar.

**Target.** `|| E[(Q + eta)^{-1} | E] || <= (1 + o(1)) m(-eta) = (1+o(1)) eta^{-1/2}` for
`eta -> 0` with `eta >> 1/D`. Fed into `residual_locallaw.md` (3.2),
`lambda_max(M_E) <= eta || E[(Q+eta)^{-1}|E] || <= (1+o(1)) sqrt(eta) = o(1)`.

## 1. The trap: the compressed resolvent is not the resolvent of the compression

This is the point the task flags, and it is real. Let `C : F^{m-D} -> F^m` be an isometry onto
`E`, so `[B,C]` is `m x m` unitary and `H := A A^*` block-decomposes over `E^perp (+) E` as
```
   H = [ B^*HB   B^*HC ]   with   B^*HB = D * Q,   (the D from the normalization)
       [ C^*HB   C^*HC ] .
```
The Schur/Krein complement of the `E^perp`-block of the resolvent of `H` is
```
   B^*(A A^* - z)^{-1} B = ( B^*HB - z - W(z) )^{-1},
   W(z) := B^*HC ( C^*HC - z )^{-1} C^*HB         ("self-energy").                  (1.1)
```
So the COMPRESSED resolvent `B^*(AA^*-z)^{-1}B` equals `(Q' - z - W)^{-1}` with `Q' = B^*HB`, and
this is NOT `(Q' - z)^{-1}`, the resolvent of the COMPRESSION, unless `W(z) = 0`. Here `W(z) != 0`:
the disjoint rows couple `E^perp` to `E` through `AA^*`. Two consequences, both fatal to a naive
shortcut:

- **Wrong object.** The monotonicity lemma of `residual_locallaw.md` needs `(Q + eta)^{-1}`, the
  resolvent of the compression. The isotropic law [BEKYY14] applied to `AA^*` with test vectors in
  `E^perp` controls `B^*(AA^*-z)^{-1}B = (Q'-z-W)^{-1}`, a different matrix.
- **Wrong aspect ratio.** `AA^*` is `m x m` of rank `D-1 << m`, hence MP at aspect ratio
  `m/(D-1) -> infinity`; its deterministic equivalent is `m_{AA^*}(z) I` with `m_{AA^*}` the MP
  transform at that LARGE ratio, not the ratio-1 transform `m`. The compression `Q` is `D x D` with
  `D-1` samples, ratio `(D-1)/D -> 1`. The two transforms are genuinely different functions.

The correct move is to build the compression INTO the matrix before taking the resolvent, i.e. use
the separable model `H_sep := P A A^* P = sqrt(Sigma) A A^* sqrt(Sigma)` with `Sigma = P`
(`sqrt P = P`). Then `H_sep` is exactly block-diagonal over `E^perp (+) E`:
```
   H_sep = B (D*Q) B^*  (+)  0_E ,   so   B^*(H_sep - z)^{-1} B = (D*Q - z)^{-1},          (1.2)
```
i.e. its Schur self-energy is `W_sep(z) ≡ 0` by construction. Feeding `H_sep` (not `AA^*`) into the
ANISOTROPIC local law returns the resolvent of the compression at the correct ratio. This is the
substantive reason [KY17] (separable), not [BEKYY14] (plain isotropic), is the right input in the
non-Gaussian case.

## 2. The theorem we cite

**Gaussian sub-case (verbatim).** If the entries of `a_i` are real/complex Gaussian, then
`g_i = B^* a_i ~ N(0, B^*B) = N(0, I_D)` has iid standard-Gaussian entries, so `Q = (1/D) GG^*` is a
genuine (real/complex) Wishart matrix at ratio `(D-1)/D`. The isotropic local law of

  [BEKYY14] Bloemendal, Erdős, Knowles, Yau, Yin, "Isotropic local laws for sample covariance
  and generalized Wigner matrices," Electron. J. Probab. 19 (2014), no. 33 (arXiv:1308.5729),

applies VERBATIM: for deterministic unit `v,w in F^D` and `z` on the spectral domain
`{ eta := |Im z| >= D^{-1+eps} }` (extended off-support, Section 3),
```
   <v,(Q - z)^{-1} w> = m(z) <v,w> + O_<(Psi(z)),   Psi(z) = sqrt(Im m(z)/(D eta)) + 1/(D eta),
```
with `m` the ratio-1 MP transform, `O_<` = stochastic domination uniform in deterministic `v,w`.
No extension is needed in this sub-case.

**General sub-Gaussian entries.** Here `g_i = B^* a_i` is isotropic but not iid-entry, so we use the
separable model of Section 1 and the anisotropic local law of

  [KY17] Knowles, Yin, "Anisotropic local laws for random matrices," Probab. Theory Related
  Fields 169 (2017), 257-352 (arXiv:1410.3516),

for `Q_Sigma = sqrt(Sigma) X X^* sqrt(Sigma)` (`X` iid `m x N`, `Sigma` deterministic PSD). Its
content: a deterministic "anisotropic equivalent" `Pi(z)` (solution of the matrix MP/Dyson equation
in `Sigma`) with, for deterministic unit `v,w` on the same domain,
`<v,(Q_Sigma - z)^{-1} w> = <v, Pi(z) w> + O_<(Psi(z))`. We apply it with `X = A`, `Sigma = P`. By
(1.2) the `E^perp`-block is the resolvent of the compression; the deterministic equivalent
restricted to `E^perp` is SCALAR,
```
   Pi(z)|_{E^perp} = m(z) I_D,                                                        (2.1)
```
the ratio-1 MP transform, because on `range(Sigma) = E^perp` the population acts as the identity
(`Sigma|_{E^perp} = I_D`) and the effective ratio is `(D-1)/D -> 1`. (Equivalently: `Q = (1/D)GG^*`
has iid isotropic columns, so by the universal MP theorem its limiting spectrum is MP(1); (2.1) is
the anisotropic refinement of that fact.) Thus for deterministic unit `w in F^D`,
```
   <w,(Q - z)^{-1} w> = m(z) + O_<(Psi(z))   uniformly in w.                          (2.2)
```

**The exact statement used downstream** is (2.2) at `z = -eta`: a direction-uniform off-support
resolvent law with deterministic limit `m(-eta) ~ eta^{-1/2}`.

## 3. Off-support: the error term is o(1), with room to spare

We evaluate at the real point `z = -eta < 0`, OUTSIDE the spectrum `[0,4]` of `Q (>= 0)`, at
distance `eta` from the hard edge. Two simplifications make this the easiest regime for any local
law:

- **The fluctuation term collapses.** At real `z = -eta`, `m(-eta) in R` and `Im m(-eta) = 0`, so
  the leading piece of `Psi` vanishes and `Psi(-eta) = 1/((D-1) eta)`. The relative error is
  ```
     Psi(-eta)/m(-eta) = [1/(D eta)] / eta^{-1/2} = 1/(D sqrt(eta)),
  ```
  which is `o(1)` as soon as `eta >> 1/D^2` — far weaker than the `eta >> 1/D` we will use, and far
  above the hard-edge eigenvalue spacing `~ 1/D^2`. We never resolve that spacing.
- **Off-support is robust.** `(Q+eta)^{-1}` is PSD with deterministic norm bound `1/eta` (distance
  to spectrum), so all large-deviation steps in the local-law proof are controlled by `eta`, not by
  the population spectrum; the off-support real axis is reached from `eta + i0^+` by analytic
  continuation / `Im z -> 0`.

The safe operating point is `eta = 1/log D` (comfortably mesoscopic, far above `D^{-1+eps}`): there
`Psi/m = sqrt(log D)/D -> 0` with enormous margin, and the local-law domain hypothesis `eta >=
D^{-1+eps}` holds trivially. So (2.2) gives `<w,(Q+eta)^{-1}w> = m(-eta)(1 + o(1))` uniformly in
deterministic unit `w`, the `o(1)` uniform over `w` and over the isometry `B`.

## 4. Hypotheses: iid entries of A, not of g_i

The hypothesis both cited laws require is iid (mean-0, unit-variance, suitable-moment / sub-Gaussian)
ENTRIES of the data matrix `X`. We feed in `X = A`, whose entries ARE iid by assumption. The
non-iid structure of `g_i = B^* a_i` is NOT a violation: the mixing by `B` is absorbed into the
deterministic population covariance `Sigma = P` of the separable model, which is exactly the device
the anisotropic law exists to handle (its whole point is to allow `sqrt(Sigma) X` = linear images of
iid columns). `B` is deterministic given `E`, of minimal complexity (orthonormal columns), and the
class `{ B : B^*B = I_D }` maps to a single `Sigma`-class (rank-`D` projection); the local-law
constants are uniform over it, so no shared span `E` is excluded. Finally, the bounded-density
assumption is NOT needed for the local law (iid sub-Gaussian entries with the standard moment bounds
suffice); bounded density is used elsewhere in Appendix B (the polar-cap Lemma `appB:tail`), not here.

## 5. Rank-deficient population: the one place care is needed

Here is the honest gap between "verbatim citation" and what we use, in the non-Gaussian case. [KY17]
is stated for `Sigma` bounded above AND below, `tau <= Sigma <= tau^{-1}`. Our `Sigma = P` is a
rank-`D` projection: eigenvalues `{0,1}`, so it fails the lower bound. Two facts make this a benign,
off-support-only extension rather than a new result:

(a) **The kernel decouples exactly.** `H_sep = P AA^* P` is genuinely block-diagonal over
`E^perp (+) E` (it annihilates `ker P = E` and maps into `range P = E^perp`); by (1.2) the
`E`-block contributes only the trivial `-1/z` and the `E^perp`-block is exactly `(D*Q - z)`. So the
degeneracy of `Sigma` lives entirely in the decoupled `E`-block; the law is needed only on the
non-degenerate `E^perp`-block, where the EFFECTIVE population is `I_D`.

(b) **Off-support, the limit `tau -> 0` is controlled `tau`-freely.** Regularize
`Sigma_e := (1-e) P + e I_m`, which lies in [KY17]'s class with `tau = e`. For the operator-norm
resolvent at `z = -eta`,
```
   || (H_e - z)^{-1} - (H_sep - z)^{-1} || <= eta^{-2} || H_e - H_sep ||
       = eta^{-2} * O(e || AA^* ||) = O(e D / eta^2)   (since ||AA^*|| = O(D) w.h.p.),
```
because off-support the resolvent is `eta`-Lipschitz in the matrix, with NO dependence on `tau` —
this is precisely where off-support-ness (Section 3) is used. Likewise the anisotropic equivalent
`Pi_e(z)|_{E^perp} -> m(z) I_D` as `e -> 0`. Taking `e = D^{-10}` makes the regularization error
`O(D^{-9}/eta^2)` negligible at `eta = 1/log D`, while [KY17] applies at `Sigma_e`.

The only thing this argument must borrow from [KY17] beyond its black-box statement is that its
error `Psi_e` and `Pi_e` are controlled as `tau = e -> 0` at the off-support point; since the
off-support resolvent norm is `tau`-free, the `tau`-dependence of [KY17]'s constants enters only
through `Pi_e` and is continuous in `Sigma`. This is routine but it is a (short) argument, not a line
of the published theorem. I therefore record the non-Gaussian closure as "modulo a benign,
off-support extension of [KY17] to a rank-deficient population," and the Gaussian closure as
verbatim [BEKYY14]. An author preferring zero extension can either (i) restrict the universality
claim to Gaussian-comparable entries via the standard four-moment / Lindeberg swap (only the off-
support `m(-eta)` need match), or (ii) cite a degenerate-population MP local law directly.

## 6. From the quadratic form to the operator norm and the expectation

`R := E[(Q + eta)^{-1} | E]` is a fixed deterministic PSD `D x D` matrix, so
`||R|| = sup_{||w||=1} <w, R w> = <w_*, R w_*>` at its (deterministic) top eigenvector `w_*`. For
each deterministic unit `w`, take `E[· | E]` of the high-probability law (2.2). On the good event
`Omega` (`P(Omega^c | E) <= D^{-100}`), `<w,(Q+eta)^{-1}w> <= m(-eta) + Psi * D^{o(1)}`; off `Omega`
use the deterministic `<w,(Q+eta)^{-1}w> <= ||(Q+eta)^{-1}|| <= 1/eta`. Hence
```
   <w, R w> = E[<w,(Q+eta)^{-1}w> | E] <= m(-eta)(1 + o(1)) + (1/eta) D^{-100}
            = m(-eta)(1 + o(1)),
```
uniformly in deterministic `w` (so in particular at `w = w_*`), since `(1/eta) D^{-100} = D^{-100}
log D = o(m(-eta))`. Therefore `||R|| <= m(-eta)(1 + o(1))`. No net is required: the anisotropic law
is already uniform over all deterministic unit vectors, including the deterministic `w_*`. The bound
holds uniformly over `B = B(E)`, hence over the shared span `E`.

(Sanity check on the mechanism: the random resolvent has `||(Q+eta)^{-1}|| = 1/eta` at the spiky null
direction `u`, but `E[(Q+eta)^{-1}]` smears that spike over the sphere via the delocalization
`E[u u^*] ~ I/D`, contributing only `~ 1/(D eta)` to any fixed direction — negligible against
`m(-eta) = eta^{-1/2}` once `eta >> 1/D^2`. This is why the expected operator norm is `eta^{-1/2}`,
not the worst-case `eta^{-1}`.)

## 7. Assembly and the manuscript paragraph

Chaining `residual_locallaw.md` (3.2) with Section 6 and `m(-eta) = (1+o(1)) eta^{-1/2}`,
```
   lambda_max(M_E) <= eta || E[(Q+eta)^{-1} | E] || <= eta * m(-eta)(1+o(1)) = (1+o(1)) sqrt(eta);
```
at `eta = 1/log D`, `lambda_max(E[u u^* | E]) <= (1+o(1)) (log D)^{-1/2} = o(1)`, which is exactly the
delocalization-in-expectation `(appB:residual)`. Unconditionally `lambda_max(E[uu^*]) <=
E_E lambda_max(M_E) = o(1)`.

Manuscript-ready paragraph (slots into the proof / remark of Proposition `appB:resolvent`):

> The factor `\|\EE[(Q+\eta)^{-1}\mid E]\|` is the resolvent of the *compression*
> `Q=B^*(AA^*)B` of the sample covariance, evaluated at the off-support point `z=-\eta<0`. It must
> not be confused with the *compressed resolvent* `B^*(AA^*-z)^{-1}B`, which by the Schur complement
> equals `(Q-z-W(z))^{-1}` with a nonzero self-energy `W(z)` and corresponds to the wrong aspect
> ratio `m/(D-1)\to\infty`. We instead realize `Q` through the separable sample-covariance matrix
> `P(AA^*)P` with the rank-`D` projection `\Sigma=P_{E^\perp}`, which is block-diagonal across
> `E^\perp\oplus E` and whose `E^\perp` block is precisely `Q`. The anisotropic local law for
> separable sample covariance \cite{KnowlesYin2017} (in the Gaussian case the isotropic law
> \cite{BEKYY2014} applies directly, as `g_i\sim\mathcal N(0,I_D)` is then iid-entry) gives, for
> every deterministic unit `w\in\F^D`, `\langle w,(Q+\eta)^{-1}w\rangle=m(-\eta)+O_\prec(\Psi)` with
> `\Psi=1/((D-1)\eta)` (the `\sqrt{\Im m}` term vanishes on the real axis); taking expectations and
> the supremum over the deterministic top eigenvector yields
> `\|\EE[(Q+\eta)^{-1}\mid E]\|=(1+o(1))m(-\eta)`. The data matrix `A` has i.i.d. entries, as both
> laws require; the non-product structure of `g_i=B^*a_i` is carried entirely by the deterministic
> population `\Sigma=P`. Since `\Sigma` is a projection (rank-deficient, outside the range of
> `\tau\le\Sigma\le\tau^{-1}` assumed in \cite{KnowlesYin2017}), this is an application of that law
> to a degenerate population; the kernel `E` decouples exactly and, off the spectrum, the resolvent
> is controlled independently of `\tau`, so the estimate is a routine off-support extension rather
> than a new local law. With `m(-\eta)=(1+o(1))\eta^{-1/2}` and `\eta=1/\log D` this is
> `(appB:residual)`.

## 8. Verdict

- **Fully rigorous modulo citation? Gaussian entries: YES, verbatim** (Wishart + [BEKYY14] isotropic
  local law). **General sub-Gaussian entries: YES modulo one short, standard off-support extension**
  of [KY17] to a rank-deficient population (Section 5) — not a new local law.
- **Exact theorems cited.** [KY17] Knowles-Yin, PTRF 169 (2017) 257-352 (arXiv:1410.3516),
  anisotropic local law for the separable sample-covariance model `sqrt(Sigma) X X^* sqrt(Sigma)`,
  applied with `Sigma = P_{E^perp}`; [BEKYY14] Bloemendal-Erdős-Knowles-Yau-Yin, EJP 19 (2014)
  no. 33 (arXiv:1308.5729), isotropic local law, for the Gaussian/Wishart sub-case. (Theorem numbers
  to be confirmed against the published versions; the statements used are the sample-covariance
  anisotropic/isotropic local laws as quoted in Section 2.)
- **Is the compression routine, or does it need care?** Mostly routine, with two named points of
  care, both discharged above and neither requiring a hard-edge eigenvector statement:
  1. The compressed resolvent `B^*(AA^*-z)^{-1}B` is NOT the resolvent of the compression
     `(Q-z)^{-1}` (Schur self-energy `W(z) != 0`, and wrong aspect ratio). Resolved by realizing `Q`
     as the separable `P(AA^*)P` (self-energy `= 0` by block-diagonality), Section 1.
  2. The population `Sigma = P` is rank-deficient, outside [KY17]'s stated hypotheses. Resolved by
     exact kernel decoupling plus a `tau`-free off-support regularization, Section 5 — the one place
     a (short) argument beyond a black-box citation is needed.
- **Genuine residual subtlety.** Only the rank-deficient-population extension (point 2). It is
  strictly easier than the in-bulk/hard-edge regime because we sit off the spectrum at distance
  `eta = 1/log D`; the feared object — sharp `polylog(D)/D` isotropic delocalization of the bottom
  null vector — is never invoked. Removable entirely for Gaussian-comparable entries via a moment
  swap if one wants a zero-extension statement.

Bib: [KY17] Knowles-Yin, PTRF 169 (2017) 257-352, arXiv:1410.3516; [BEKYY14]
Bloemendal-Erdős-Knowles-Yau-Yin, EJP 19 (2014) no. 33, arXiv:1308.5729.
