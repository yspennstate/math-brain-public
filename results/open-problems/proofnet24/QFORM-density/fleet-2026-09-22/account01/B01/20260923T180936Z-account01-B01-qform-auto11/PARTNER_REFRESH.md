# Late designated-partner refresh — account02/B01 r47

After the canonical report was published, account02/B01 completed a newer theorem:

- source commit: `339c1fdf3bc65a79f5be126e730dd3b251320e66`
- source path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T180438Z-auto11/REPORT.md`
- theorem: `QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1`.

It states that after an original-coordinate scalar completion

    Q=a(X0+h)^2+R,

if the residual has one original hub Y with nonzero slope `m=m_J` into an untouched original bank J, and if

    C=A_R[I,J](I-P_m),   F_C=||C||_F>0,

then, with no row-marginal hypothesis and no rank hypothesis on C,

    H_{1/2}(R) <= 8 (||m|| F_C)^(-1/4),
    ||p_Q||_infinity <= 8 |a|^(-1/2)(||m|| F_C)^(-1/4).

## Actual equation-level application

Use five ORIGINAL independent cap-one coordinates `X,Y,U,V1,V2`. Let

    e=(1,1)/sqrt(2),   q=(1,-1)/sqrt(2)

and define

    Q_*=X^2+2Y<e,V>+2U<q,V>.

Complete X. Then `a=1`, the residual hub is Y, `m=e`, `I={U}`, `J={V1,V2}`, and because `q perpendicular e`,

    C=q^T,   ||m||=1,   F_C=1.

The projected crossing has a single I-row, so its normalized one-volume row weight is exactly 1; this is the maximally concentrated case that the older row-marginal-gated version could not use. The new partner theorem gives

    boxed: ||p_{Q_*}||_infinity <= 8.

The residual bipartite cross matrix with hubs (Y,U) and bank V is `[e^T;q^T]`, whose singular values are exactly 1,1. Therefore its symmetric spectrum is `{+1,+1,-1,-1}`; the independent X-square adds another `+1`. Hence

    spec(Q_*)={1,1,1,-1,-1},

so this is a full-target-valid application.

This newest partner result and the theorem of the present B01 run are complementary. The partner pays any nonzero projected transverse crossing after a scalar square peel; the present theorem pays an exact two-hub zero-self-block packet directly by integrating the `|L|^{-1}` conditional-density singularity against its two-dimensional slope law. The combined structural survivor is therefore more sharply an aligned state in which every useful projected crossing collapses to zero/tiny and internal two-hub curvature must carry the third spectral resource.

Full QFORM remains OPEN. No continuity conclusion is inherited from the partner theorem.
