# Independent A087 review of B06-A027 modulation blocks

## Verdict

**B06-A027-MODULATION-BLOCK-HIERARCHY@1** is **ACCEPTED at its stated
restricted scope**. The coefficient factorization, entropy and influence
identities, physical-child law, sequential queried-influence ledger, finite
iteration, and terminal accounting all reconstruct without an unproved
universal step.

The source's point-defect constant \(9/2\) is valid. A separate contributor
calculation sharpens it to the asymptotically optimal constant \(4\);
that sharpening requires a fresh independent reviewer.

## Reconstruction

For
\[
F(x,z)=g(x_1h_1(z),\ldots,x_nh_n(z)),
\qquad h_S=\prod_{i\in S}h_i,
\]
expand \(g=\sum_S\widehat g(S)\chi_S\). Then
\[
F(x,z)=\sum_S\widehat g(S)\chi_S(x)h_S(z),
\]
so, because \(X\) and the fresh block \(Z\) are disjoint,
\[
\widehat F(S,T)=\widehat g(S)\widehat{h_S}(T).
\]
With \(\mu(S)=\widehat g(S)^2\) and
\(\nu_S(T)=\widehat{h_S}(T)^2\), Parseval makes
\(\mu\) and every \(\nu_S\) probability laws. The spectral law of \(F\) is
exactly the joint law
\[
\Pr\{S,T\}=\mu(S)\nu_S(T).
\]
The entropy chain rule and degree expectation therefore give
\[
H(F)=H(g)+\sum_S\mu(S)H(h_S),
\]
\[
I_X(F)=I(g),\qquad
I_Z(F)=\sum_S\mu(S)I(h_S).
\]

Fixing \(z\) changes the coefficient at \(S\) to
\(\widehat g(S)h_S(z)\). Since \(h_S(z)^2=1\), every physical child has
exactly the squared spectrum \(\mu\). Hence the block-mixing term is genuinely
zero, not merely omitted:
\[
M_Z=0,\qquad H(F)-\mathbb E_z H(F_z)
=\sum_S\mu(S)H(h_S).
\]
There is no hidden mismatch/KL rebate in this special class because the
branch squared spectra coincide exactly.

When the coordinates of \(Z\) are revealed sequentially, at step \(j\) the
uniform average over all prior prefixes and all unrevealed suffixes counts
each original edge in direction \(z_j\) exactly once. Thus
\[
\sum_j\mathbb E_{\text{prefix}}I_{z_j}(F_{\text{prefix}})
=I_Z(F).
\]
Path weights are the actual fair probabilities \(2^{-d}\); no coordinate is
reused.

If every occupied \(h_S\) satisfies
\(H(h_S)\le C_Z I(h_S)\), the one-block decrement is at most
\(C_ZI_Z(F)\). The terminal child is a sign-flipped input copy of \(g\), so
its entropy is exactly \(H(g)\). Iterating over disjoint fresh blocks gives
\[
H(f_L)\le C_0I(f_0)+
\sum_{\ell=1}^LC_\ell\bigl(I(f_\ell)-I(f_{\ell-1})\bigr)
\le\max_\ell C_\ell\,I(f_L).
\]
This is a finite-depth theorem in every dimension, not a limit inferred from
finite computation.

## Endpoints and controls

- Empty spectral set: \(h_\varnothing=1\), so both auxiliary entropy and
  influence are zero.
- Constant modulator/product: zero entropy and zero influence; the premise is
  well-defined.
- Character-coded plateau: block decrement and added influence both vanish;
  all base entropy remains at the terminal.
- Rare point defect: its logarithmic entropy is included in the exact
  auxiliary ratio. The new bound is \(H(q_m)<4I(q_m)\) for \(m\ge2\).
- Addressing or near tensors: admissible only as bases with an already proved
  constant; no new constant is inferred.
- Bent splice: unequal branch squared laws violate the theorem's hypothesis
  and remain a live obstruction.
- Shared signed dictator: allowing arbitrary auxiliary products would contain
  FEI itself; the source does not make that circular generalization.
- Properness: at least one older physical variable remains, so the newest
  block is not the full current variable set.

## Independent finite reconstruction

The file **independent_modulation_review.py** is a separate exact
implementation. It checked 20,480 one-step Boolean modulation instances,
256 two-level hierarchies, and the point-defect laws through 16 variables.
It made 939,550 exact assertions for Fourier laws, physical children,
influences, and sequential restriction ledgers. Floating point was used only
for a displayed finite ratio diagnostic.

Command: python3 independent_modulation_review.py > CHECK.out.
Randomness: none.

## Scope after review

The reviewed theorem closes A027 only on the modulation hierarchy. The first
unpaid universal line is still:

> Given an arbitrary Boolean function whose physical block branches have
> unequal squared spectra, find a proper block or compensated stopping rule
> that pays the complete conditional branch-spectrum entropy without reusing
> influence and without dropping the terminal.

No full-FEI conclusion follows.
