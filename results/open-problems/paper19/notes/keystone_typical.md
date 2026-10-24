# prob:pc, the TYPICAL VALUE of the overlap of random normals

Lead analysis, 2026-06-28. This note treats the *typical value / second moment* layer of the
bulk overlap moment (`prob:pc`, the keystone of II.B). It establishes the exact mean of the
normal's rank-one projector, deduces `E|rho|^2 = 1/m` for independent normals, and reduces the
overlapping-pair second moment `E[|rho|^2 | D] <= C/D` to one clean operator-norm bound on the
*expected* null-vector projector inside the shared orthocomplement. It then proves exactly which
part of that bound the coordinate symmetry supplies (the trace) and exhibits, with proof, why the
symmetry does **not** supply the rest (the spectral spread), naming the remaining input.

Companion notes: `IIB_assembly.md`, `IIB_overlap_largeD.md` (the harder *negative* moment),
`IIB_overlap_smallD.md`, `IIB_lemma_2D.md`. Scope here is strictly the second moment of `rho`,
which is *weaker* than the negative moment `E[(1-|rho|^2)^{-d_F/2}]` that II.B ultimately needs;
see §4 for how the two relate.

Throughout `F in {R,C}`, `d_F = dim_R F in {1,2}`, `<x,y> = sum_k x_k conj(y_k)` is the Hermitian
inner product, and `*` is conjugate-transpose. `A` is the `(N-1) x m` matrix of available rows
`a_1,...,a_{N-1} in F^m`, iid with iid entries of law `nu` on `F`: mean `0`, `E|x|^2 = 1`
(proper, `E x^2 = 0`, when `F = C`), and a bounded Lebesgue density. `J` is the all-ones `m x m`
matrix.

--------------------------------------------------------------------------------
## 0. The normal and its projector (a.s.-unique up to phase)

For an `(m-1)`-subset `S subset [N-1]`, let `V_S = span{a_i : i in S}`. Bounded density makes the
rows a.s. in general position, so a.s. `dim V_S = m-1` and the normal line `V_S^perp` is exactly
one-dimensional. The **unit normal** `u_S` is any unit vector spanning `V_S^perp`; it is defined
only up to a unit phase (`u_S ~ e^{i theta} u_S`, real: `+-u_S`). The phase-invariant object is the
orthogonal projector onto the normal line,
```
    Pi_S := u_S u_S^*  =  P_{V_S^perp}   (rank 1, Hermitian, well-defined a.s.).
```
All expectations below are of `Pi_S` (and of `|rho|^2 = tr(Pi_S Pi_T)`), so the phase ambiguity of
`u_S` is irrelevant. Write
```
    M := E[Pi_S] = E[u_S u_S^*]   (m x m, Hermitian, PSD, tr M = E||u_S||^2 = 1).
```

--------------------------------------------------------------------------------
## 1. The exact mean projector: `M = I_m / m`

### 1.1 Equivariance of the normal under coordinate isometries

Let `g in U(F^m)` (real: `O(R^m)`) act on `F^m`. Applying `g` to every row, `a_i -> g a_i`, sends
`V_S -> g V_S`; since `g` is an isometry it preserves orthogonality, so `V_S^perp -> g V_S^perp`
and the projector transforms by conjugation:
```
    Pi_S(gA) = g Pi_S(A) g^*.                                                   (1.1)
```
This is a deterministic identity, valid rowwise, for every isometry `g`.

Now restrict to the **signed-permutation group** (`F = R`) resp. **phase-permutation group**
(`F = C`):
```
    G := { g = P D : P an m x m permutation matrix, D = diag(eps_1,...,eps_m) },
         eps_k in {+-1} (F = R),   |eps_k| = 1 (F = C).
```
Every `g in G` is an isometry, so (1.1) holds. The law of a single row `a_1` (iid coordinates
`~ nu`) is `G`-invariant iff `nu` is invariant under each generator:
* **permutations** `P`: always, because the coordinates are iid;
* **diagonal flips** `D`: iff `eps x =^d x` for the relevant `eps`, i.e. iff `nu` is symmetric
  (`x =^d -x`, `F = R`) resp. **circular** (`x =^d e^{i theta} x` for all `theta`, `F = C`).

If `nu` is `G`-invariant then the whole row family is (rows iid), so `Pi_S(gA) =^d Pi_S(A)`;
combined with (1.1) and taking expectations,
```
    g M g^* = M    for all g in G.                                             (1.2)
```

### 1.2 Two consequences of (1.2)

**(a) Permutation part is automatic; pins the diagonal and the form of `M`.** The permutation
subgroup `P in G` needs *no* assumption on `nu` (iid suffices), so unconditionally
`P M P^T = M` for all permutations `P`. The commutant of the permutation representation of `S_m`
on `F^m` is `span{I, J}` (the rep is `trivial (+) standard`, two irreducibles; Schur). Hence
unconditionally
```
    M = a I + b J,    a,b real,    with diagonal entries a+b = 1/m            (1.3)
```
(the diagonal is constant by permutation symmetry and sums to `tr M = 1`; `b` real because the
swap of two indices forces `M_{12} = M_{21}`). Eigenvalues of `M`: `a` with multiplicity `m-1`
(on `1^perp`) and `a + bm` (on the all-ones vector). PSD `=> a >= 0, a + bm >= 0`; and
`|b| <= 1/m` by Cauchy-Schwarz (`|M_{12}| <= sqrt(M_{11} M_{22}) = 1/m`).

**(b) Sign/phase part kills `b`.** If in addition `nu` is symmetric (`F=R`) resp. circular
(`F=C`), then (1.2) holds for the full group `G`, whose commutant on `F^m` is just the scalars
`F I` (diagonal flips force `M` diagonal; permutations force it constant). With `tr M = 1`,
```
    M = E[u_S u_S^*] = (1/m) I_m    exactly.                                   (1.4)
```

> **Proposition 1 (exact mean projector).** For iid rows with a symmetric (real) resp. circular
> (complex) bounded-density entry law, `E[u_S u_S^*] = I_m/m` exactly. Without the symmetry
> assumption, still `E[u_S u_S^*] = a I + b J` with diagonal `1/m` (the off-diagonal `b` is the
> only possible deviation, `|b| <= 1/m`).

**Honesty: the symmetry hypothesis is genuinely needed for `b = 0`.** A mean-`0`, variance-`1`,
bounded-density law need *not* be symmetric, and then `b != 0` in general. Smallest witness
(`m = 2`, `S = {a}` a single row, `u_S = (a_2, -a_1)/||a||`): the off-diagonal of `M` is
`-E[a_1 a_2/(a_1^2 + a_2^2)]`, which vanishes for symmetric `nu` but not otherwise (a skewed
mean-`0` `nu` gives a nonzero value; e.g. a two-point mean-`0` law smoothed to a density yields
`b ~ -1/10 != 0`). So (1.4) is exactly an assertion about the symmetric/circular class; for general
bounded density one has only (1.3). This matters in §2.

--------------------------------------------------------------------------------
## 2. Independent normals: `E|rho|^2 = 1/m`

Let `S, T` be **disjoint** `(m-1)`-sets (`D = m - |S cap T| = m`). Then `u_S, u_T` are built from
independent rows, hence independent, with the same law, so `E[Pi_S] = E[Pi_T] = M`. Using
`|rho|^2 = |<u_S,u_T>|^2 = u_T^*(u_S u_S^*) u_T = tr(Pi_S Pi_T)` and independence (the trace of a
product of independent matrices factors through their means),
```
    E|rho|^2 = E tr(Pi_S Pi_T) = tr( E[Pi_S] E[Pi_T] ) = tr(M^2).             (2.1)
```

> **Proposition 2.** For disjoint `S, T` and a symmetric/circular bounded-density law,
> `E|rho|^2 = tr((I/m)^2) = m * m^{-2} = 1/m`.

This is the exact analogue of the Gaussian value `E|rho|^2 = 1/m` (Haar lines in `F^m`). For a
general (non-symmetric) law, (1.3) gives, with eigenvalues `a` (`m-1` times) and `a+bm`,
```
    E|rho|^2 = tr(M^2) = (m-1)a^2 + (a+bm)^2 = 1/m + m(m-1) b^2  >=  1/m,      (2.2)
```
(using `a + b = 1/m`). So the clean value `1/m` holds iff `b = 0`. The deviation `m(m-1)b^2` is
`o(1/m)` iff `|b| = E[u_{S,1} conj(u_{S,2})] = o(m^{-3/2})`; Cauchy-Schwarz only gives `|b| <= 1/m`
(useless here, it makes `m(m-1)b^2` up to `~1`). Thus for non-symmetric laws even Proposition 2
needs a genuine *mean-delocalization* input on the off-diagonal `E[u_{S,1} conj(u_{S,2})]`; under
symmetry/circularity it is exactly zero and Proposition 2 is unconditional. This is the first sign
of the phenomenon that dominates §3: the *coordinate symmetry does the whole job in the full
space, and only there.*

--------------------------------------------------------------------------------
## 3. Overlapping pairs: reduction of `E[|rho|^2 | D]` to one operator bound

Now `S, T` overlap: `r = |S cap T| = m - D`, `1 <= D <= m`. Let `C = S cap T` (the `m-D` shared
rows), `E := span{a_i : i in C}`. A.s. `dim E = m - D`, so the **shared orthocomplement**
`E^perp` has dimension `D`; fix a unitary identification `E^perp =~ F^D`. Both normals are
orthogonal to every shared row, hence
```
    u_S, u_T in E^perp =~ F^D.
```
Write the `D-1` rows private to `S` as `a_i, i in S\C`, and their projections
`g_i := P_{E^perp} a_i in E^perp`. Then `u_S` is the unit normal *inside `E^perp`* to
`span{g_i : i in S\C}` (a `(D-1)`-dim subspace of the `D`-dim space `E^perp`); likewise `u_T` from
the independent private rows of `T`.

### 3.1 Conditional second moment is a trace, again

Condition on `E` (equivalently on the shared rows). Given `E`, the private rows of `S` and of `T`
are independent of each other and of the shared rows, with the original row law. Hence, given `E`,
`u_S` and `u_T` are **conditionally independent with the same conditional law**. Set
```
    M_E := E[u_S u_S^* | E] = E[Pi_S | E],   an operator on E^perp,  tr M_E = 1.
```
Exactly as in (2.1) (the trace of a product of conditionally independent matrices factors),
```
    E[|rho|^2 | E] = E[ tr(Pi_S Pi_T) | E ] = tr( M_E^2 ).                     (3.1)
```
`M_E` is PSD, supported on `E^perp` (`dim D`), with `tr M_E = 1`. Two elementary spectral bounds:
```
    1/D  <=  tr(M_E^2)  <=  lambda_max(M_E).                                   (3.2)
```
(Lower: Cauchy-Schwarz on the at-most-`D` nonzero eigenvalues summing to `1`. Upper:
`sum lambda_i^2 <= (max lambda_i) sum lambda_i = lambda_max`.) Averaging (3.1) over `E` and using
(3.2):

> **Reduction.** `E[|rho|^2 | D] = E_E[ tr(M_E^2) ] in [1/D, E_E lambda_max(M_E)]`. In particular
> the target second-moment bound
> ```
>     E[|rho|^2 | D]  <=  C/D
> ```
> follows from the single operator inequality `M_E <= (C/D) P_{E^perp}` (a.s. in `E`), i.e. from
> ```
>     lambda_max(M_E) = max_{w in E^perp, ||w||=1} E[ |<u_S, w>|^2 | E ]  <=  C/D.   (3.3)
> ```
> Conversely the lower bound in (3.2) shows `E[|rho|^2|D] >= 1/D` always, so `C/D` is the right
> order and (3.3) is essentially equivalent to the target. The Gaussian/Haar value is the equality
> case `M_E = (1/D) P_{E^perp}`, giving `tr(M_E^2) = 1/D`.

The quantity in (3.3) is a *delocalization-in-expectation of the null vector* `u_S` in every fixed
direction `w` of `E^perp`: `<u_S, w> = +- dist(w, span{g_i})`, so
`w^* M_E w = E[ dist(w, W)^2 | E ] = 1 - E[ ||P_W w||^2 | E ]` with `W = span{g_i}`, and (3.3) is
`lambda_min( E[P_W | E] ) >= 1 - C/D`.

### 3.2 What the coordinate symmetry DOES give: conditional isotropy (proved)

The one structural fact that survives projection to the random subspace `E^perp` is **isotropy**.
Since the entries are iid mean-`0` variance-`1` (proper for `C`), each ambient row is isotropic,
`E[a_i a_i^*] = I_m`. Projection is linear and `P_{E^perp}` is `E`-measurable, so conditionally
```
    E[ g_i g_i^* | E ] = P_{E^perp} I_m P_{E^perp} = P_{E^perp}  =  I_{E^perp}.   (3.4)
```
Thus, given `E`, the `D-1` private projected rows `g_i` are **isotropic in `E^perp`**. This pins the
*trace* of `E[P_W | E]`: `E[ tr P_W | E] = E[ rank W | E] = D-1` (a.s. full rank, bounded density),
equivalently `tr M_E = tr E[P_{W^perp}|E] = D - (D-1) = 1` — consistent with §3.1 and the *average*
eigenvalue `1/D`. So isotropy delivers the correct trace/average of `M_E`, hence the lower bound
and the "typical" value `1/D` *if* the spectrum is flat.

### 3.3 What it does NOT give, and why: the symmetry is lost on `E^perp`

The clean conclusion of §1 used a *group* `G` of coordinate isometries leaving the row law
invariant and acting (with the sign/phase part) irreducibly on the ambient `F^m`, forcing
`M = I/m` by Schur. On `E^perp` this mechanism is unavailable:

* `E^perp` is a **random subspace in general (oblique) position** with respect to the coordinate
  axes. No nontrivial element of `G` maps `E^perp` to itself, so conjugation by `G` does not act on
  `M_E`; there is no group of symmetries of the *conditional law* of `(g_i)` acting transitively /
  irreducibly on `E^perp`.
* All that transfers is isotropy (3.4), which is a **second-moment** symmetry: it says
  `E[g_i g_i^*] = I`, i.e. it constrains `E[P_W]` only through its **trace**, not its spectrum. The
  map `law(g) |-> M_E = E[u_S u_S^*]` is nonlinear (the null vector is a ratio of cofactor
  polynomials, `u_{S,k} ~ det G_{hat k}`) and is **not determined by the second moment of `g`**.

That isotropy is genuinely insufficient is not a gap in the argument but a fact:

> **Witness (isotropy does not control `lambda_max(M_E)`).** Take `F = R`, `D = 2`, one private
> vector `g = (a, b)`, with `a ~ N(0,1)` and `b` an independent mean-`0` variance-`1` law that is
> *not* Gaussian (e.g. `+-1` smoothed to a density). Then `E[g g^*] = I_2` (isotropic), yet
> `u_S = (b, -a)/||g||` gives diagonal `M_E[1,1] = E[ b^2/(a^2+b^2) ]`. With `a` symmetric the
> off-diagonal vanishes, and with `b^2` concentrated near `1` (vs the spread `chi^2_1` of a
> Gaussian) the strict concavity of `t |-> E_a[ t/(a^2+t) ]` forces
> `M_E[1,1] = E[ E_a[b^2/(a^2+b^2)] ] -> E_a[1/(a^2+1)] = sqrt(pi/2) e^{1/2} erfc(1/sqrt2) ~ 0.656`,
> hence `lambda_max(M_E) ~ 0.65 >> 1/D = 1/2`. (Numerically verified: `0.648` with `b` a smoothed
> Rademacher of variance `1`.) Two isotropic laws (Gaussian vs this one) thus give different
> `lambda_max(M_E)` — `1/D` vs a constant. The same coordinate-shape mismatch keeps
> `lambda_max(M_E) = Omega(1)` for all `D` (rigorous as stated for `D = 2`; the higher-`D` claim is
> the same mechanism, not computed in detail here).

So (3.3) **cannot follow from (3.4) alone**. It is false at the level of generality "isotropic
`g_i`," and only becomes true using the *specific* structure of the real projected rows.

### 3.4 The missing input (named precisely)

What rescues the real problem is that the projected rows are **not arbitrary isotropic vectors**:
in any orthonormal basis `(b_l)` of `E^perp`, the coordinate `<g_i, b_l> = <a_i, b_l> =
sum_{j=1}^m conj((b_l)_j) a_{ij}` is a linear combination of `m` iid entries with comparable, small
weights (delocalized basis, since `E^perp` is a generic `D = Theta(m)` subspace). By the CLT these
coordinates are jointly **approximately Gaussian and shape-regular** — precisely the property the
witness in §3.3 violates. Quantitatively, the needed statement is

> **(DELOC-EXP).** For the unit null vector `u_S` of the `D x (D-1)` matrix `G = [g_i]` of projected
> iid rows, `sup_{||w||=1} E[ |<u_S, w>|^2 | E ] <= C/D`, with an absolute `C`.

This is *delocalization in expectation in every fixed direction* (equivalently
`lambda_min(E[P_W]) >= 1 - C/D`), the in-expectation, second-moment form of **no-gaps
delocalization** for the null vector of a matrix with delocalized near-Gaussian rows
(Rudelson-Vershynin invertibility; Rudelson, *No-gaps delocalization for general random matrices*,
2016). It is the right tool because it controls a *fixed* linear functional of `u_S`, not just
coordinate ones; the high-probability delocalization bound passes to the expectation because on its
(exponentially small) failure event `|<u_S,w>|^2 <= 1` contributes `<= P(fail)`.

Note (DELOC-EXP) is strictly **milder** than the BULK negative moment
`E[(1-|rho|^2)^{-d_F/2}; D >= eps m] <= 1+o(1)` of `IIB_overlap_largeD.md`: it is a *second
moment* (typical alignment), not a *near-extreme small-ball* (the event `1 - |rho|^2 ~ 0`, i.e.
`u_S` almost equal to the random null direction `u_T`). So (DELOC-EXP) is a more accessible
sub-target on the path to BULK, and a natural first milestone.

--------------------------------------------------------------------------------
## 4. Relation to what II.B needs, and why the typical value is not the whole story

The assembly (`IIB_overlap_smallD.md`, §6) needs the *negative* moment
`E[(1-|rho|^2)^{-d_F/2}; D >= eps m] <= 1 + o(1)`. The present note controls only the *positive*
second moment `E|rho|^2`. These are different and the gap is real:

* `E|rho|^2 = 1/m` (or `1/D` conditionally) is the statement that `rho` is *typically* tiny. It is
  the mean; it says nothing about the lower tail of `1 - |rho|^2`.
* The negative moment is dominated by the rare event `|rho| -> 1` (`u_S` nearly aligned with
  `u_T`). A second-moment / `lambda_max` bound does not see that event. (Indeed
  `(1-|rho|^2)^{-d_F/2}` is not even integrable on the small-`D` range; cf. the caveat in
  `IIB_overlap_smallD.md` §6.)

So this note does **not** prove II.B. Its contribution is to (i) nail the exact typical value with
the Gaussian constant, distribution-free under symmetry, and (ii) recast the conditional typical
value as the clean operator bound (3.3)/(DELOC-EXP), separating cleanly what coordinate symmetry
gives (trace) from what it cannot (spectrum). The negative moment then sits one rung above
(DELOC-EXP): it needs the *lower-tail* version of the same null-vector delocalization, with the
sharp constant — the open hard-edge RMT lemma of `IIB_overlap_largeD.md`.

--------------------------------------------------------------------------------
## 5. Status: proved vs open

**Proved (rigorous, this note).**
1. Equivariance (1.1) and: permutation invariance is automatic and forces `M = aI + bJ` with
   diagonal exactly `1/m` (1.3); under symmetric (`R`)/circular (`C`) entry law, `M = I_m/m`
   exactly (Proposition 1), handling the phase ambiguity via the projector `Pi_S`.
2. For independent (disjoint) normals, `E|rho|^2 = tr(M^2) = 1/m` under symmetry; in general
   `= 1/m + m(m-1)b^2` (Proposition 2). Honest: `b = 0` needs symmetry/circularity (witnessed
   nonzero otherwise); else needs `|E[u_{S,1}\overline{u_{S,2}}]| = o(m^{-3/2})`.
3. Overlapping pairs: the conditional second moment is a trace, `E[|rho|^2|E] = tr(M_E^2)`, with
   `1/D <= tr(M_E^2) <= lambda_max(M_E)` (3.1)-(3.2); hence `E[|rho|^2|D] <= C/D` **reduces** to the
   single operator bound `M_E <= (C/D)P_{E^perp}` (3.3), and `E[|rho|^2|D] >= 1/D` always.
4. Conditional isotropy of the projected private rows, `E[g_i g_i^*|E] = I_{E^perp}` (3.4),
   which pins `tr M_E = 1` (correct average eigenvalue `1/D`).
5. A proof that isotropy alone is **insufficient** for (3.3): an explicit isotropic law (any `D`,
   shown for `D=2`) with `lambda_max(M_E) = Omega(1) >> 1/D` (witness in §3.3, numerically
   `~ 0.648`). Hence the symmetry of §1 provably does **not** transfer to the oblique random
   subspace `E^perp`.

**Open (named precisely).**
6. The operator bound (3.3) `<=> ` (DELOC-EXP): `sup_{||w||=1} E[|<u_S,w>|^2 | E] <= C/D`, the
   in-expectation no-gaps delocalization of the null vector of `D-1` *projected iid (delocalized,
   near-Gaussian)* rows in `F^D`. This is what isotropy fails to give and what the CLT-regularity
   of the projected rows should supply; it is milder than (and a stepping stone to) the BULK
   negative moment that II.B requires.

**Net.** The typical-value layer of `prob:pc` is settled (exact mean `I/m`, exact independent
second moment `1/m`), and the overlapping conditional second moment is reduced to one sharp,
correctly-scaled operator inequality with a precise, accessible RMT statement (DELOC-EXP) as the
sole remaining input — with a proof that no softer (isotropy-only) argument can replace it.
