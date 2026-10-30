SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T00:15:12Z.
attacking: N3 decoupled-time gluing — compare the full mixed-hub collision integral with every single physical-pair collision certificate.

# B03 report: local-vs-global collision separation inside the no-pivot class

Run: `20260923T001512Z-fleet02-B03-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **ESSENTIAL_STEP_APPLIED + REFUTED INTERMEDIATE LOCALIZATION MECHANISM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and correction-safe scope

Fresh brain control was read on main and refreshed before publication. The active owner control remains revision `2026-09-22.15`, sole target QFORM, with no applicable pause. The current no-pivot reduction N3 is source-pinned in the newest Claude synthesis. The exact Fourier inputs used below are:

1. `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`: Theorem H (mixed hub/Fresnel/BL) and Theorem D/D'/D5.
2. Later compatible geometric source `yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`, same directory, `GEOMETRIC_ROUTE_REPORT.md`: the no-pivot class and the one-hub plus one-rank-one family are legitimate surviving structures; the gluing lemma is still open.
3. Designated partner fleet03/B03, `yspennstate/math-open-problems@438f565ec17517e0b742b333154a4c9881209958`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T222730Z-fleet03-B03-QFORM-r20b/REPORT.md`: translation-uniform indefinite-pair half-Riesz and its exact independent-copy identity.

No use is made of law-uniform pointwise quadratic-phase decay, post-rotation independence, conditional sum/difference density caps, arbitrary-joint rank-three coarea, or a universally good physical minor.

## 2. Exact N3 family

Fix `m>=2` and nonzero real `a,b`. Order the original coordinates as one hub `h`, a bank `V={v_1,...,v_m}`, and a disjoint bank `E={e_1,...,e_m}`. Put

```
A_m(a,b) =
[ 0                 (a/sqrt(m)) 1^T      0          ]
[ (a/sqrt(m)) 1     0_{m x m}            0          ]
[ 0                 0                    (b/m) J_m  ].
```

The star block has eigenvalues `+|a|,-|a|` and zero otherwise; `(b/m)J_m` has sole nonzero eigenvalue `b`. Hence the nonzero spectrum of `A_m(a,b)` is `{+|a|,-|a|,b}` up to the sign convention for `a`. In particular, if `|a|,|b|>=1`, this is an exact target matrix with three eigenvalues of modulus at least one.

Its physical no-pivot scales are explicit:

`max_i |A_ii| = |b|/m`,

and for every distinct pair `i,j`,

`|det A[{i,j},{i,j}]| <= a^2/m`,

with equality only for a hub--V pair. Thus for every fixed `tau>0`, taking

`m > max(|b|,a^2)/tau`

puts the matrix strictly in N3(tau).

## 3. All decoupled k-volume certificates with k>=3 vanish

For arbitrary disjoint coordinate sets `I,J`, the cross block `A_m[I,J]` is the sum of two blocks with disjoint coordinate support:

- the star contributes rank at most one, because the unique hub can lie in at most one of `I,J`;
- the E-bank contributes rank at most one, since it is a restriction of `(b/m)J_m`.

Therefore

`rank A_m[I,J] <= 2`                                             (3.1)

for every disjoint `I,J`. Consequently every 3x3 (and higher) cross minor vanishes and

`e_k(A_m[I,J]^T A_m[I,J]) = 0` for every `k>=3`.                (3.2)

So Theorem D, its relaxed-marginal D' extension, and the unconditional D5 extension are identically silent on this N3 family. This is stronger than merely saying a selected cross minor is small: there is no positive cross-volume certificate of order at least three anywhere.

This does not challenge those theorems. It refutes only an attempted N3 closure that relies exclusively on forcing a positive D/D'/D5 cross-volume certificate.

## 4. The full form is nevertheless uniformly bounded: exact application of Theorem H

For independent original-coordinate inputs with densities at most one,

`Q_m = 2a X_h (m^{-1/2} sum_j X_{v_j}) + b (m^{-1/2} sum_k X_{e_k})^2`.       (4.1)

Apply source Theorem H with hub set `H={h}`, active set `I=V union E`, no conditioned remainder, and rank-one Fresnel direction

`r = m^{-1/2} 1_E`, `lambda=b`.

The augmented Theorem-H row vectors are

`rho_i=(0,a/sqrt(m))` for `i in V`,
`rho_i=(1/sqrt(m),0)` for `i in E`.

Hence

`G = sum_i rho_i rho_i^T = diag(1,a^2)`,

and every normalized leverage is exactly `1/m <= 1/2`. The theorem therefore gives, for every `t!=0`,

`|phi_m(t)| <= 4 pi^(3/2) |a|^(-1) |b|^(-1/2) |t|^(-3/2)`.   (4.2)

Using `|phi_m|<=1` and integrating the envelope,

`int_R |phi_m(t)| dt <= 6 [4 pi^(3/2)|a|^(-1)|b|^(-1/2)]^(2/3)`,

so Fourier inversion yields

`||p_{Q_m}||_infinity <= 3 * 4^(2/3) |a|^(-2/3)|b|^(-1/3)`.   (4.3)

For `|a|,|b|>=1`, the right side is at most

`C_H = 3*4^(2/3) = 7.559526299369239...`.                     (4.4)

Thus this exact N3 family is uniformly controlled only after the hub and both banks are aggregated together.

## 5. New decoupled-time consequence: the global collision potential is dimension free

Let `Q_m'` be an independent copy and let `h_m` be the density of `Q_m-Q_m'`. From (4.3),

`||h_m||_infinity <= ||p_{Q_m}||_infinity =: C_m`,            (5.1)

because `h_m=p_{Q_m}*p_{-Q_m}` and the second factor has L1 norm one.

For any probability density `h<=C` and any `r>0`,

`int |u|^(-1/2) h(u) du`
` <= 4 C sqrt(r) + r^(-1/2)`.

Optimizing at `r=1/(4C)` gives the elementary endpoint bound

`int |u|^(-1/2)h(u)du <= 4 sqrt(C)`.                           (5.2)

The partner's exact Riesz/independent-copy identity therefore gives

`int_R |t|^(-1/2)|phi_m(t)|^2 dt`
` = sqrt(2 pi) E |Q_m-Q_m'|^(-1/2)`
` <= 4 sqrt(2 pi C_m)`
` <= 4 sqrt(2 pi C_H)`                                         (5.3)

when `|a|,|b|>=1`. Numerically the last universal constant is

`4 sqrt(2 pi C_H) = 27.56748942459127...`.                    (5.4)

This is a genuine dimension-free decoupled-time estimate. The independent copy is used only through the law of `Q_m-Q_m'`; no sum/difference coordinate pair is declared independent.

## 6. Every single nonzero physical-pair collision certificate diverges

Now take one hub--V physical pair. Its quadratic piece is

`F_{m,j}=2a X_h X_{v_j}/sqrt(m)`.                              (6.1)

For the admissible law `X_h,X_{v_j} iid Uniform[1,2]`, write `Y=X_h X_{v_j}` and `c_m=2a/sqrt(m)`. Then

`eta_{m,j}(t)=E exp(it F_{m,j}) = eta_Y(c_m t)`.

Consequently the weighted collision integral scales **exactly** as

`I_loc(m):=int_R |t|^(-1/2)|eta_{m,j}(t)|^2 dt`
` = |c_m|^(-1/2) I_Y`
` = m^(1/4)(2|a|)^(-1/2) I_Y`.                                (6.2)

The partner theorem ensures `I_Y<infinity`. It is also strictly positive; more explicitly, since `Y,Y' in [1,4]`, `|Y-Y'|<=3`, and the partner Riesz identity gives

`I_Y = sqrt(2 pi) E|Y-Y'|^(-1/2) >= sqrt(2 pi/3)`.             (6.3)

Hence

`I_loc(m) >= sqrt(pi/(3|a|)) m^(1/4)`.                        (6.4)

Thus the local pair collision endpoint necessarily blows up as `m^(1/4)` even though the full mixed-hub collision endpoint (5.3) stays bounded independently of `m`.

This is not a weakness of the partner estimate: its scale is forced by the physical coefficient. For the pair matrix

`B_m=[[0,a/sqrt(m)],[a/sqrt(m),0]]`,

`D=|det B_m|=a^2/m`, `kappa=sigma_min(B_m)=|a|/sqrt(m)`,

so the partner theorem gives precisely

`H_{1/2}(F_{m,j}) <= C_ind |a|^(-1/2)m^(1/4)`,                (6.5)

matching the unavoidable power in (6.4).

## 7. Applying the partner ambient pivot theorem shows the same localization loss

The only nonzero physical scalar diagonals lie in the E-bank and have

`d=b/m`.

Pivot one E coordinate. Since `(b/m)J_m` has rank one, its Schur complement on the remaining E coordinates is zero; the hub--V star is unchanged. Taking any hub--V pair in that residual, the partner fleet03/B03 ambient theorem gives

`||p_Q||_infinity`
` <= C_ind |d|^(-1/2)(D kappa)^(-1/6)`
` = C_ind |ab|^(-1/2) m^(3/4)`.                              (7.1)

So a proof that first localizes to one physical square pivot and one physical indefinite pair pays a polynomial `m^(3/4)` loss on this exact N3 target family, while the source-valid mixed-hub aggregation pays no `m` at all by (4.3).

Equation (7.1) is an application of the designated partner theorem, not a criticism of it: its hypotheses and homogeneity are correct. The construction shows only that a structural theorem cannot promise a dimension-free *single local certificate* of that type throughout N3.

## 8. Corrected proof obligation

The following intermediate mechanism is therefore refuted:

> N3 can be closed by forcing either a positive order-3/order-5 decoupled cross volume, or a single physical square-pivot plus indefinite-pair half-Riesz certificate with universal scale.

On `A_m(a,b)`, every cross volume of order at least three is exactly zero and every available single local pair collision scale worsens with `m`, but the complete form has a uniform density and a uniform global independent-copy endpoint after hub/bank aggregation.

A corrected structural gluing statement must therefore allow an **augmented mixed-hub frame** (or an equivalent bank/ridge aggregate) *before* taking the fractional collision endpoint. At minimum, the live N3 proof map needs three branches:

1. D/D'/D5 cross-volume smoothing when a genuine cross-volume certificate exists;
2. mixed-hub/Fresnel smoothing when a low-rank hub plus spread square supplies the missing exponent;
3. a remaining genuinely hybrid no-pivot class in which neither certificate is available.

The source's geometric report already identifies (2) qualitatively; the new point here is the exact collision-scale separation (5.3) versus (6.4), showing quantitatively why the independent-copy endpoint must be formed **after** aggregation rather than on one physical pair.

The full QFORM conjecture and N3 remain OPEN.

## 9. Verification notes

The spectrum and no-pivot scales are analytic from the displayed block matrix. The cross-rank bound is analytic from the star-plus-rank-one support decomposition. A finite regression checker was also run for `m=2,3,4,5,10,100`; it confirmed the nonzero spectrum `[-1,1,1]` at `a=b=1`, `max|A_ii|=max pair determinant=1/m`, and exhaustive maximum cross rank two for `m=2,3`. The checker is corroborating evidence only; none of the all-m claims depends on finite enumeration.
