# Addendum — excess slab mass forces diagonal-tail mass on the slab itself

Run: `20260924T063211Z-account01-B13-auto11`  
Parent report: `REPORT.md` in this same immutable run folder.  
Status: supporting strengthening only; full QFORM remains OPEN.

Keep the notation of Theorem 2 in the report. In particular,

`Q(x)=x^T A x`, `Q_kappa(x)=x^T A_kappa x`,
`R_kappa(x)=Q(x)-Q_kappa(x)`,

and the completed account02/B13 finite-direction theorem gives

`||p_(Q_kappa(X))||_infty <= H_kappa`

under the unit-product-set law on `E=prod_i E_i`.

Let

`p=|{x in E:Q(x) in J}|`,
`a=(p-H_kappa |J|)_+`.

Then for every `s>0`,

`|{x in E:Q(x) in J, |R_kappa(x)|>s}|`
` >= p-H_kappa(|J|+2s)`.                                            (A.1)

Indeed, on `{Q in J, |R_kappa|<=s}` one has `Q_kappa in J+[-s,s]`, and the latter event has volume at most `H_kappa(|J|+2s)`.

If `a>0`, choose

`s=a/(4H_kappa)`.                                                    (A.2)

Then (A.1) gives the distributional strengthening

`boxed:
 |{x in E:Q(x) in J,
          |R_kappa(x)|>a/(4H_kappa)}|
 >=a/2.}`                                                           (A.3)

Thus **at least half of the slab mass in excess of the finite-direction baseline `H_kappa|J|` lies on points where the omitted coefficient-small diagonal tail has definite magnitude**.

Integrating `|R_kappa|` over the set in (A.3) immediately recovers

`L_kappa(E)>=a^2/(8H_kappa)`,                                       (A.4)

which is exactly the moment obstruction in the parent report, but (A.3) is strictly more informative geometrically.

In slab-ratio notation `rho_E=p/|J|`, (A.3) becomes

`boxed:
 |{x in E:Q(x) in J,
          |R_kappa(x)|>
          |J|(rho_E-H_kappa)/(4H_kappa)}|
 >= |J|(rho_E-H_kappa)/2}`                                         (A.5)

whenever `rho_E>H_kappa`.

For the account02/B13 exact two-line endpoint, `kappa=1/2`, `|C|<=10`, `m<=2`, and `r=#{i notin C:|d_i|>1/2}` give

`H_r=500 e (r+12)(8+log(r+12))`.

Therefore every high-ratio bounded finite-union product witness has a quantitatively large **on-slab** subset where the distributed small-diagonal bank itself has size at least the threshold in (A.5). This does not discard the tail and does not impose any uniform support diameter; remote or fragmented support is charged rather than normalized away.
