# Correction and strengthened synthesis for account03/B20 QFORM r17

This file is an additive correction to `REPORT.md`; the original report is retained immutably.

## 1. Scope correction

The sentence in `REPORT.md` that informally takes `tau=1/4` when invoking account04/B20 r3 is not the correct reason that its cross-dominated theorem applies. In the account01/B20 r13 high-window setup, `tau=(1+||b||/|a|)^(-2)>=1/4` is inherited, not a freely reset parameter.

The correct interface is stronger and exact: the selected high-window physical row `j` satisfies

`max{|d|,||c||}>tau/9`.

Therefore, if that row is cross-dominated, `||c||>|d|`, then automatically `||c||>tau/9`, so account04/B20 r3 applies. No replacement of `tau` is needed.

## 2. Correct synthesis theorem — `QFORM-BALANCED-HUB-HIGHWINDOW-SEPARATION-v1`

Use the fresh account01/B20 r12 balanced-hub packet after the retained physical pivot `|a|>=3501/8000`: there is a residual physical hub `p` and disjoint banks `U,V` with

`alpha=||S[U,p]||>1/(8sqrt2)`,
`beta =||S[V,p]||>1/(8sqrt2)`.

Hence the full cross row of `p` satisfies

`||S[p,-p]|| >= sqrt(alpha^2+beta^2)>1/8`.                    (2.1)

Suppose this same hub `p` is also the selected rank-two high-window coordinate `j` from account01/B20 r13. Then the entire state is already paid:

* if `||c||>|d|`, the high-window property gives `||c||>tau/9`, and account04/B20 r3 gives `||p_Q||inf<5262`;
* if `|d|>=||c||`, then (2.1) gives `|d|>1/8`. The diagonal-dominated branch for this selected high-window coordinate was already completely paid by account01/B20 r13 (same-sign and opposite-sign second-pivot cases).

Consequently:

`boxed( an unpaid fresh balanced-hub state cannot have p=j. )`       (2.2)

This is the correct new compatibility exclusion supplied by r17.

There is also a quantitative sharpening in the diagonal-dominated same-sign subcase. If `ad>0`, the original physical pair `{i,p}` has

`det B=ad`,

and by `|a|>=3501/8000`, `|d|>1/8`,

`|det B|>3501/64000`.

The source-valid definite physical-pair theorem therefore yields

`||p_Q||inf < pi sqrt(64000/3501)=13.432096533...<13.433`.     (2.3)

This improves the numerical bound on that already-paid overlap; it is not a claim that the overlap was previously open.

## 3. Direct-alignment re-pivot identity remains valid

The algebraic identity from `REPORT.md` is unchanged. If

`||M-lambda u v^T||F<1/32`

and `d!=0`, then after exact second physical Schur pivoting at `p`,

`T[U,V]=M-(alpha beta/d)u v^T`,

so with `mu=lambda-alpha beta/d`,

`||T[U,V]-mu u v^T||F<1/32`.                                  (3.1)

This is an exact matrix statement and does not promote `u,v` to independent random coordinates.

## 4. Correct next obligation

The useful consequence is now a **separation constraint** rather than a newly closed unpaid sign branch. In the still-unpaid low-leverage balanced-hub packet, the physical hub `p` must be distinct from the selected rank-two high-window coordinate `j` whenever the older localized high-window reduction applies. Since the residual high window still has a physical coordinate with leverage `P_jj>1/32`, the next unpaid synthesis step is:

`QFORM-HUB-VERSUS-HIGHWINDOW-TWO-ANCHOR-PAYMENT-v1`:

exploit the coexistence of the strong hub `p` and a distinct high-window coordinate `j` to force either a quantitative physical pair/triple, an aggregate determinant bank, or a paid ridge/grouped-square packet, retaining original-coordinate product provenance.

The full QFORM conjecture and full-target continuity remain OPEN.
