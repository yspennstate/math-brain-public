# B05 / A023 — fixed-shared-block orbit transport

**Run:** `20261014T032726Z-fleet01-B05-fixed-shared-block-a023`  
**Claim:** `B05-FIXED-SHARED-BLOCK-TRANSPORT-v1`  
**Status:** **AUTHOR_PROVED_PENDING_REVIEW**  
**Full FEI:** **OPEN**

## 1. Bounded objective and delta

The previous accepted state contained:

1. the reviewed B05 rare-refund obstruction, which rules out a universal
   all-node fixed-price payment at unchanged hypotheses;
2. the B05/B19 shared-coordinate degree-shift counterfamily, which rules out
   every fixed scalar multiplier of shared-coordinate pivotal mass; and
3. the B01 coefficient-one block potential for one reused physical
   coordinate.

This run tests the first genuinely nested case: two reused physical
coordinates, with arbitrary Boolean terminal cores and arbitrary activation
probabilities.  The resulting theorem is stronger than that bounded target:
it works for every fixed shared block of size `k`, and its potential contracts
under every order of physical revelation.

The exact price is also exposed.  Private singleton blocks retain coefficient
one, but the shared mean orbit has coefficient `k`.  Thus the theorem is
uniform in core dimension, bias, and reveal depth for a fixed shared block,
but not uniform in the number of reused coordinates.  It is not full FEI and
does not complete A023.

## 2. Definitions

Let

\[
q(t)=t\log _2(1/t)+\frac{2t}{\ln 2},\qquad q(0)=0.
\]

On `[0,1]`, `q` is increasing and concave.  Let `X` be a distinguished set
of `k` physical coordinates.  For a Boolean function `f` and a base set
`S` disjoint from `X`, define its `X`-orbit energy

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2.
\]

Define

\[
\Phi(f)=\sum_i q(\widehat f(\{i\})^2)
\]

and the fixed-shared-block potential

\[
\Lambda_X(f)=kq(E_X^f(\varnothing))
 +\sum_{i\notin X}q(E_X^f(\{i\})). \tag{2.1}
\]

The factor `k` in the empty orbit is deliberate: after multiplication there
are `k` shared singleton coefficients, all lying in that one orbit.

## 3. Main theorem

### Theorem 3.1 — product transport through a fixed shared block

Let `f:{-1,1}^{X\sqcup U}->{-1,1}` and
`g:{-1,1}^{X\sqcup V}->{-1,1}`, where `U` and `V` are disjoint and
`|X|=k`.  Put `h(x,u,v)=f(x,u)g(x,v)`.  Then

\[
\begin{split}
\Phi(h)\le {}&
 \sum_{i\in U}q(E_X^f(\{i\}))
 +\sum_{j\in V}q(E_X^g(\{j\}))\\
&+kq\!\left(\min\{E_X^f(\varnothing),
                         E_X^g(\varnothing)\}\right). \tag{3.1}
\end{split}
\]

In particular,

\[
\Phi(fg)\le \Lambda_X(f)+\Lambda_X(g). \tag{3.2}
\]

This is coefficient one on every private orbit.  It permits arbitrary Boolean
cores, arbitrary bias, and nonflat orbit spectra.

### Theorem 3.2 — complete physical revelation

For the same `f`, if `f_\xi` denotes restriction to `X=\xi`, then

\[
\mathbb E_{\xi\in\{-1,1\}^X}\Phi(f_\xi)
 \le \sum_{i\notin X}q(E_X^f(\{i\}))
 \le \Lambda_X(f). \tag{3.3}
\]

### Theorem 3.3 — first-revelation contraction

For any `x in X`, put `X'=X\setminus\{x\}`.  Then

\[
\mathbb E_{\sigma\in\{-1,1\}}
 \Lambda_{X'}(f\mid x=\sigma)\le \Lambda_X(f), \tag{3.4}
\]

where the empty-orbit coefficient in `\Lambda_{X'}` is `k-1`.  Iterating
(3.4) proves contraction under every reveal order.  For `k=2`, this is the
requested four-element-orbit calculation and handles either `x`-first or
`y`-first revelation with the same parent budget.

## 4. Proof

Full details appear in `PROOF.md`; the key calculation is short.

For `i in U`, let

\[
F_i(\xi)=\mathbb E_u[f(\xi,u)\chi_i(u)],\qquad
G_0(\xi)=\mathbb E_v[g(\xi,v)].
\]

The `X`-Fourier vector of `F_i` is exactly
`(fhat({i} union A))_{A subset X}`.  The corresponding conditional singleton
function for `h` is `F_i G_0`.  Since `|G_0|<=1`, Parseval gives

\[
\sum_{A\subseteq X}\widehat h(\{i\}\cup A)^2
 =\mathbb E_\xi F_i(\xi)^2G_0(\xi)^2
 \le E_X^f(\{i\}).
\]

The actual singleton `hhat({i})` is one member of the output orbit.  Monotonicity
of `q` therefore pays it with `q(E_X^f({i}))`.  The `V` coordinates are
symmetric.

For the empty orbit, write `F_0=E_u f` and `G_0=E_v g`.  Then

\[
E_X^h(\varnothing)=\mathbb E_\xi F_0(\xi)^2G_0(\xi)^2
 \le \min\{E_X^f(\varnothing),E_X^g(\varnothing)\}.
\]

Every shared singleton `hhat({x})`, `x in X`, is a component of this orbit.
Summing its `k` charges proves (3.1).

For revelation, the restricted coefficient is the Walsh evaluation

\[
\widehat {f_\xi}(\{i\})
 =\sum_{A\subseteq X}\widehat f(\{i\}\cup A)\chi_A(\xi).
\]

Parseval and concavity of `q` give (3.3).  Finally, after revealing one
coordinate, every child `X'`-orbit has the form

\[
\sum_{B\subseteq X'}(a_B+\sigma b_B)^2.
\]

Its average over `sigma` is `sum_B(a_B^2+b_B^2)`, the parent `X`-orbit
energy.  Jensen pays each private orbit once.  The child empty orbit has
weight `k-1`, no larger than the parent's weight `k`, proving (3.4).

## 5. Why this matters for the rare-refund gap

For two nested rare activations using physical coordinates `x,y`, take
`X={x,y}` and absorb all disjoint control variables into the private side of
the activating factor.  The theorem is indifferent to the activation
probabilities and to the terminal Boolean core.  Four Fourier coefficients
per private singleton are transported together, so the degree-shift term
which defeated scalar pivotal credit is not discarded.  Revealing `x` first
or `y` first spends the same parent orbit budget in expectation.

This is a real class extension:

| Quantity | Previous verified scope | New proved scope |
|---|---|---|
| Reused physical coordinates | exactly one | arbitrary fixed `k` |
| Terminal core | arbitrary Boolean | arbitrary Boolean |
| Activation bias | arbitrary | arbitrary |
| Private-orbit coefficient | 1 | 1 |
| Shared empty-orbit coefficient | 1 | `k` |
| Reveal order | one coordinate | every order inside fixed `X` |
| Changing overlap sets | open | still open |

The accepted shared-coordinate rare family survives: its shifted private
singleton lies inside the relevant orbit and is paid once.  The theorem does
not reinterpret the entire shared edge as a rare pivotal event.

## 6. Verification

`CHECK.py` exhausts all `65,536` pairs of Boolean factors on `(x,y,u)` and
`(x,y,v)`.  For every pair it checks (3.2); for every factor it checks full
revelation and `x`-first sequential contraction.  It also performs `6,000`
seeded tests for `k=1,2,3`, private dimensions one or two.  `CHECK.out`
records a pass.  This is finite numerical support only; the theorem rests on
the analytic proof above.

## 7. Exact remaining gap

The fixed-block theorem does **not** supply the requested universal retained
credit:

1. the empty-orbit coefficient grows as `k`, so no address-count-independent
   constant has been obtained;
2. an arbitrary hierarchy can change its shared set from node to node, so a
   coefficient may enter several incomparable orbit blocks;
3. the theorem controls the singleton potential `Phi`, not yet the complete
   signed upper-set charge `Delta_i U = B_i-Gamma_i+KL_i` with terminal `U`
   and entropy retained; and
4. no all-tree injection from these orbit charges to disjoint physical
   pivotal events is proved.

Thus A023 remains **OPEN / PARTIAL AUTHOR-PROVED BRIDGE**, and full FEI remains
**OPEN**.

## 8. Next mathematical move

Replace the factor `k q(E_X(empty))` by an entropy-sensitive partition of the
empty orbit.  The next frozen test should ask whether

\[
\sum_{x\in X}q(\widehat h(\{x\})^2)
\]

can be paid by one `q(E_X^h(empty))` plus a signed KL/upper-set refund that
telescopes under (3.4).  It must be tested first on the accepted nested rare
majority/bent-core family and on changing two-block overlaps such as
`{x,y}` followed by `{y,z}`.

## 9. Source and review status

The direct input is the B01 one-shared-coordinate theorem delivered at
canonical commit `9e6482990f0c41d77844709348d4fffc99985c5f` (full bundle
`caedfbe205c111e1f8f64f88f8cf2114c4dea069`).  The shared-coordinate
counterfamily and its independent scope review are pinned in `SOURCE_PINS.md`.
No literature novelty claim is made.

This package requires independent review by A087 or A094 before reuse as an
accepted campaign result.

