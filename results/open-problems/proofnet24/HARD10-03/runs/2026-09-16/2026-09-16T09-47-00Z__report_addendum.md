# HARD10-03 — 2026-09-16T09-20-22Z checkpoint addendum

This file is append-only. It records the exact delivery receipt for the main report, a dimension-`d>=3` generalization of the Green-resolvent estimate, and the final self-review for this iteration. It does not overwrite any earlier task file.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T09-20-22Z__report.md`

Create commit:

`6215580567142e87f23fe9525a232546e6719984`

Exact-create-commit readback blob:

`b778dc4cc1c1df6e5d4510206198a0f792bc0c94`

The file was fetched using the exact create commit ref and the opening status text matched. Therefore the main report delivery is **VERIFIED**.

No transient retry was needed. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

## 2. NEW-L75B — dimension-general Green-resolvent envelope

The proof of NEW-L74 is not special to dimension three except for transience and the form of the Green kernel. It extends to every `d>=3` for the rate-one-per-edge nearest-neighbor walk.

Let

\[
g_d(z)=\int_0^\infty p_t^{(d)}(0,z)\,dt.
\]

The standard Gaussian heat-kernel bound gives

\[
g_d(z)\le C_d(1+|z|)^{2-d}.
\tag{2.1}
\]

For an arbitrary `n`-point set `A subset Z^d` and a fixed `x`, order lattice points by radius or split at `R asymp n^{1/d}`. The near-field row sum is

\[
\sum_{r\le R} O(r^{d-1})\,O(r^{2-d})
=O(R^2),
\]

and the far contribution is at most

\[
O(nR^{2-d}).
\]

With `R asymp n^{1/d}`, both terms are `O(n^{2/d})`. Hence

\[
\sup_x\sum_{y\in A}g_d(y-x)
\le C_d n^{2/d},
\]

and therefore the normalized uniform Green energy satisfies

\[
\boxed{
\mathcal E_{g_d}(A)
\le C_d n^{-1+2/d}.
}
\tag{2.2}
\]

The spectral Jensen argument of NEW-L74 gives in every transient dimension

\[
\mu_\beta(A)
\ge
\frac{n}{1+n\mathcal E_{g_d}(A)/\beta}.
\]

Using (2.2):

### Corollary NEW-L75B — PROVED

For every `d>=3`, finite nonempty `A subset Z^d`, and `beta>0`,

\[
\boxed{
\mu_\beta(A)
\ge
\frac{n}{1+C_d n^{2/d}/\beta}
\ge
c_d\min\{n,\beta n^{1-2/d}\}.
}
\tag{2.3}
\]

Consequently the strong-Rayleigh invariant-set theorem yields

\[
\boxed{
\mathbb P(C_{\pi_\beta}(u)=A)
\le
\exp\{-c_d\min(n,\beta n^{1-2/d})\}.
}
\tag{2.4}
\]

The crossover `n asymp beta^{d/2}` is exactly the one-particle diffusive volume. For `d=3`, (2.3)--(2.4) reduce to NEW-L75 with the middle exponent `beta n^{1/3}`.

This generalization is not used to claim a new infinite-cycle theorem in dimensions already covered by the literature; it is recorded because it confirms that the resolvent leakage mechanism has the expected diffusive-volume scaling and is not an artifact of the `d=3` exponents.

---

## 3. Final self-review of NEW-L76

The independent-slab instability statement in the main report was rechecked after exact readback.

* The first-slab cycle `C=C_P(0)` is `P`-invariant by definition, so composing `Q=R o P` gives exactly as many arrows from `C` to `C^c` as `R` does.
* Each outgoing `Q` arrow certifies that its tail lies in a `Q`-cycle not contained in `C`, so `|E_C(Q)|>=N_out(R,C)` is deterministic.
* The root-averaging identity is an annealed point-shift statement for the joint law. The shift is determined by the first slab; conditional on that first slab, translating the independent second slab preserves its distribution. Thus no anticipative conditioning of the second slab is introduced.
* Conditioning on the first slab makes `C` deterministic for the independent second slab, so applying NEW-L74 to `C` is legitimate. This is fundamentally different from applying a deterministic-set bound retroactively to the cycle selected by the same clocks.
* The conclusion is only support noncontainment at time `2 beta`. It does not imply `L_{2 beta}(0)>L_beta(0)`, and no monotonicity claim is made.

No defect was found in these steps.

---

## 4. Current exact bottleneck

The full `d=3` conjecture remains **OPEN / PARTIAL**. The strongest new fixed-support envelope now has a large middle regime

\[
\exp(-c\beta n^{1/3}),
\qquad
\beta^{3/2}\lesssim n\lesssim\beta^3,
\]

but a fixed-support estimate alone still cannot be summed over all spatially arbitrary supports. The missing theorem must recover connected primitive-return information or a nonanticipative low-entropy skeleton. The most concrete next target is a mediator-skeleton counting lemma with entropy `o(beta n^{1/3})` in that middle regime, or an independent-slab Lyapunov theorem showing that repeated support instability forces escape to an infinite cycle rather than mere reshuffling among large finite cycles.

No Gmail/email, Google Drive, repository settings/workflows/permissions changes, force-push, public posting, third-party contact, or paid compute were used.