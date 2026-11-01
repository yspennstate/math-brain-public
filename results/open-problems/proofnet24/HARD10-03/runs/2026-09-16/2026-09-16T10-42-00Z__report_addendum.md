# HARD10-03 — 2026-09-16T10-24-00Z checkpoint addendum

This file is append-only. It records the exact delivery receipt for the main report, a dimension-general form of NEW-L77/78, and the final post-write self-review. It does not overwrite any prior task file.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T10-24-00Z__report.md`

Create commit:

`31f53017938240446f0112a0b8b0a1259e4d7c5c`

Exact-create-commit readback blob:

`f74833fbdd9ef582535a9a31430768613c458e47`

The file was fetched using the exact create commit ref and the opening target/status plus previous-checkpoint section matched. Therefore the main report delivery is **VERIFIED**.

No transient retry was needed. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

## 2. NEW-L77B — dimension-general nonlocal leakage

The continuum-embedding proof of NEW-L77 is dimension-independent. For the rate-one-per-edge continuous-time nearest-neighbor walk on `Z^d`, the standard two-sided Gaussian estimate gives, for every fixed `d>=1`, constants `a_d,c_d,beta_d>0` such that

\[
|z|\le a_d\sqrt\beta
\quad\Longrightarrow\quad
p_\beta^{(d)}(0,z)\ge c_d\beta^{-d/2}
\qquad(\beta\ge\beta_d).
\]

Embed a finite `A subset Z^d` as a union of unit cubes `Omega_A subset R^d`, and put `r asymp sqrt(beta)`. Exactly as in the main report,

\[
\mu_\beta(A)
\ge
c_d\beta^{-d/2}
\int_{\Omega_A}\int_{\Omega_A^c}
1_{\{|u-v|\le r\}}\,dv\,du.
\]

Riesz rearrangement minimizes this radial nonlocal perimeter at a Euclidean ball `B_R` with `R^d asymp n=|A|`. The same boundary-layer calculation gives

\[
I_r(B_R)
\ge
c_d\min\{R^d r^d,R^{d-1}r^{d+1}\}.
\]

Since `r asymp sqrt(beta)`, this yields:

### Corollary NEW-L77B — PROVED

For every fixed `d>=1`, every sufficiently large `beta`, and every finite nonempty `A subset Z^d`,

\[
\boxed{
\mu_\beta(A)
\ge
c_d\min\{|A|,\sqrt\beta\,|A|^{1-1/d}\}.
}
\]

The crossover is `|A| asymp beta^{d/2}`, the diffusive one-particle volume.

Whenever the strong-Rayleigh invariant-set theorem is available (in particular for the interchange/exclusion setting used here),

\[
\boxed{
\mathbb P(C_{\pi_\beta}(u)=A)
\le
\exp\{-c_d\min(n,\sqrt\beta\,n^{1-1/d})\}.
}
\]

For `d=3` this is NEW-L78. This dimension check is not used to claim a new infinite-cycle result in dimensions covered by existing literature; it records the natural nonlocal-perimeter scaling of the leakage mechanism.

---

## 3. Post-write self-review of NEW-L77/78/79

The main derivation was rechecked after exact readback.

1. **Tagged-particle rate convention.** With rate-one clocks on each unoriented incident edge, a tagged particle has generator `Gf(x)=sum_{y~x}(f(y)-f(x))`; the quoted near-diagonal heat-kernel lower bound therefore uses exactly the same `beta` convention as the interchange process.
2. **Lattice-to-continuum comparison direction.** The argument only integrates cube pairs whose Euclidean representatives are within `r`; for those pairs the lattice centers are within the diffusive near-diagonal range. Hence the inequality is a lower bound on `mu_beta`, in the required direction.
3. **Riesz direction.** `I_r(Omega)=|Omega||B_r|-self_r(Omega)`. Riesz maximizes the self-interaction for the symmetric ball, therefore the cross interaction `I_r` is minimized by the ball. The direction used in NEW-L77 is correct.
4. **Large-ball geometry.** For `R>=r`, the outer shell volume is `Theta(R^{d-1}r)` and each shell point has `Theta(r^d)` exterior interaction volume, giving `Theta(R^{d-1}r^{d+1})`. In `d=3`, after multiplying by `beta^{-3/2}` this is `Theta(sqrt(beta) n^{2/3})`.
5. **Small-ball geometry.** For `R<=r`, the ball case has nonlocal perimeter `Theta(R^d r^d)` up to constants; after the heat-kernel factor this is `Theta(n)`. Thus the two regimes meet at `n asymp beta^{d/2}` with no gap.
6. **Strong-Rayleigh dependency.** NEW-L78 does not claim independence of final occupancies; it uses the already archived negative-association theorem to upper-bound the all-occupied event by the product of its marginals, then AM-GM/exponential leakage.
7. **Independent-slab scope.** NEW-L79 applies NEW-L77 only to the second slab after conditioning on the first. The selected first-slab cycle is therefore deterministic relative to the fresh clocks, so there is no anticipative use of a deterministic-set estimate.
8. **No hidden monotonicity.** NEW-L79 is only a support-noncontainment statement under an independent extra slab. It is not a claim that cycle length, diameter, capacity, or any cycle event is monotone in time.

No defect was found in these steps.

---

## 4. Exact remaining gap

The full `d=3` conjecture remains **OPEN / PARTIAL**. The new fixed-support bound is now

\[
\exp\{-c\sqrt\beta\,n^{2/3}\}
\qquad(n\gg\beta^{3/2}),
\]

which has the correct heat-boundary-layer scaling for large geometric regions. What is still missing is a summable encoding of spatially arbitrary final cycle supports that preserves primitive-return/mediator information. A raw union bound over subsets remains invalid.

The next attack should therefore target either (i) a deterministic annular/mediator skeleton with entropy below the new exponent, or (ii) a fresh-slab Lyapunov quantity that converts the support-instability lower bound into irreversible progress. No Gmail/email, Google Drive, workflow/settings/permission changes, force-push, public posting, third-party contact, or paid compute were used.