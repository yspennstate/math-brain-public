# fleet02/B14 r38 early checkpoint

Status: substantive partial theorem proved; full QFORM remains open.

## First unpaid implication

The newest fleet03/B14 r38 chirp-slice compiler is localization-safe only if the *unnormalized* slice Fourier coefficient scales with the mass of every localized bank piece. The next full-target step is therefore: before refining a curvature-active bank, either prove this mass-homogeneous slice bound or pay a whole-active D'/D5/ridge/hub/Fresnel certificate. Active Fresnel fragmentation is expected to lose a positive power of fragment count.

## Subprobability chirp-slice Lp calculation

Let X have a probability density f<=1 and be independent of a finite positive bank measure on (L,Y) of total mass m<=1, disintegrated as nu_l(dy) dl. Suppose

    ess sup_l |hat(nu_l)(t)| <= A |t|^{-1/2},  t!=0.

For arbitrary measurable real H put T=H(X)+2XL+Y, interpreted as the pushforward submeasure. The fleet03/B14 r38 proof extends verbatim to

    |hat(mu_T)(t)| <= min{m, sqrt(pi*m*A)|t|^{-3/4}}.

Hence for 4/3<q<=2 and p=q/(q-1),

    int |hat(mu_T)(t)|^q dt
      <= [6q/(3q-4)] (pi A)^{2/3} m^{q-2/3},

and Hausdorff-Young gives

    ||p_T||_p <= (2pi)^(-1/q)[6q/(3q-4)]^(1/q)
                 (pi A)^(2/(3q)) m^(1-2/(3q)).

In particular, if a localization into bank pieces of masses m_j satisfies A_j<=A0 m_j, then every displayed Lp bound is exactly linear in m_j, so summing arbitrary countably many pieces costs no fragment/support/translation/moment factor.

For q=3/2 (p=3),

    ||p_T||_3 <= (9/pi)^(2/3)(pi A)^(4/9)m^(5/9).

An independent square S=a(Z-b)^2 with cap-one Z satisfies

    ||p_S||_(3/2) <= 5^(2/3)|a|^(-1/3).

Therefore

    ||p_(T+S)||_infty
      <= 45^(2/3) pi^(-2/9) A^(4/9) m^(5/9)|a|^(-1/3).

Under A<=A0 m this is linear in m; arbitrary positive localization of the bank then transfers the same global constant exactly.

Next: make the active-Fresnel fragmentation obstruction quantitative on Q=2XL+W^2+Z^2 and compare with Claude Theorem A.
