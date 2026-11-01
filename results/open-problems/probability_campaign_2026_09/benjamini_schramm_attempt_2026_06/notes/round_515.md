# Round 515 span-scale audit: the scalar closure needs a two-scale norm

Rounds 507--514 contain useful scalar diagnostics, but they hide a span-scale
assumption.  In the same-scale packet norm
\[
  E_z(\Pi)\le C^{|\Pi|}w^{E_r(\Pi)}\alpha^{L(\Pi)},
\]
a child atom from height \(h\) to height \(h'\) contributes, through the
recursive bound, a factor
\[
  C\,qz^2w^2\,\alpha^{|h-h'|}.
\]
After dividing by the parent output span factor, monotone child subdivisions
do not carry the extra \(z^{|h-h'|}\) used in Rounds 507--514.  For example,
a monotone chain of child atoms whose lengths sum to \(S\) contributes
\[
  \alpha^S
  \sum_{m\ge1} (Cqz^2w^2)^m \binom{S-1}{m-1}
  =
  \alpha^S\, Cqz^2w^2(1+Cqz^2w^2)^{S-1}.
\]
Dividing by the output \(\alpha^S\) leaves exponential growth in \(S\).
Thus a same-scale \(C^k\alpha^L\) norm cannot justify the scalar closure as
currently written.

The calculations in Rounds 507--514 should instead be read as a
length-resolved or two-scale Ansatz.  If child packets are controlled with a
stronger span parameter \(\theta\) and the parent output is measured with a
weaker parameter \(\alpha>\theta\), then a child atom has effective span
weight
\[
  \left(\frac{\theta}{\alpha}\right)^{|h-h'|}.
\]
The previous scalar formulas correspond to taking this effective ratio to be
approximately \(z/\alpha\), i.e. \(\theta\approx z\).

The corrected target is therefore a Banach-scale estimate:
\[
  \mathcal T:\mathcal B_\theta\longrightarrow \mathcal B_\alpha,
  \qquad 0<\theta<\alpha<1,
\]
where \(\mathcal T\) is the packet root transform.  In such an estimate the
span-resolved skeleton uses
\[
  t=\theta/\alpha
\]
for child atoms and
\[
  t_V=z/\alpha
\]
for root-column vertical atoms.  The scalar checks from Rounds 507--514 show
that there is room when \(t\) is of order \(z/\alpha\), but they do not yet
prove a fixed point in one norm.

This changes the immediate objective.  The next rigorous step is not the
record-envelope lemma alone, but a two-scale packet inequality:

1. prove the record-envelope decomposition in the scalar model with separate
   child and vertical span ratios \(t=\theta/\alpha\) and \(t_V=z/\alpha\);
2. prove \(\mathcal T:\mathcal B_\theta\to\mathcal B_\alpha\) with constants
   uniform for a usable interval of \(\theta<\alpha\);
3. find a bootstrap or analytic-norm argument that turns these two-scale
   estimates into finiteness at every \(z<M_q^{-1}\).

This audit does not discard the scalar work, but it downgrades Rounds
507--514 from a closure proof to a calibrated model for the two-scale
estimate that is still needed.
