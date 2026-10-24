# account02/B14 r34 corollary — one-sided remote-fragment localization with arbitrary hub self-curvature

This file records one concrete localization consequence of `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1` from this run.

Use the completed account03/B14 r32 shear result at
`yspennstate/math-open-problems@7d56182ff8bd5766d26974c9b02d543ee155654e`,
which proves the following unnormalized fact. If

`W=aX3+bX4-beta`, `|b|>=|a|`,

`X4` remains a full cap-one probability coordinate, and `X3` is replaced by any positive subdensity fragment of mass `m`, then the pushforward submeasure of `W` has mass `m` and density cap at most

`m/|b|`.                                                         (1)

Now let an outer original-coordinate invertible indefinite pair have

`D=|det C|`, `kappa=sigma_min(C)`,

and suppose exact completion leaves

`Y = h X0^2 + X0[s0+2d(aX3+bX4-beta)] + R(X3,X4,Z)`,             (2)

where **`h` is arbitrary**, `R` is arbitrary and may use the same bank coordinates, and every displayed coordinate is an original coordinate with the required product independence before conditioning.

For a fragment of `X3` of mass `m`, (1) and scaling by `2d` give the unnormalized slope cap

`L <= m/(2|db|)`.                                                (3)

The arbitrary-self mass compiler from the r34 report then gives the fragment output bound

`||p_(Q,frag)^sub||_inf`
` <= 8 sqrt( mL/kappa ) + C_* m/sqrt(D)`
` <= m [4sqrt(2)/sqrt(|db|kappa) + C_*/sqrt(D)],`                (4)

where

`C_* = 2+log2+sqrt(2 pi e) erfc(1/sqrt(2))`
`    = 4.004506265397... .`                                      (5)

Therefore, for **any finite or countable positive decomposition** of the cap-one density of `X3` into fragments of masses `m_j`, summing (4) yields exactly

`boxed: ||p_Q||_inf`
` <= 4sqrt(2)/sqrt(|db|kappa) + C_*/sqrt(D).`                    (6)

There is no dependence on the number, locations, separation, diameters, or moments of the fragments. They may be arbitrarily remote or unbounded. Conditioning-generated `s0,beta` and all affine terms are harmless because they only translate the slope or the pair critical value.

The novelty relative to account03/B14 r32 and account02/B14 r33 is the arbitrary self coefficient `h`: r33 required the hub self coefficient to vanish exactly, while (6) is unchanged for every `h in R`. This is proved by copy-differencing the hub, not by asserting coefficient-to-output-law continuity.

Full QFORM remains open; this corollary is a support-free localization interface for any branch that exposes (2).
