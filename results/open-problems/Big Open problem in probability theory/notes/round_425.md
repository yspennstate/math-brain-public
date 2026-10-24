# Round 425 coefficient-scale audit for the bridge-record cycle

Round 425 audits the last bridge-record cycle instead of applying another
formal split.  The purpose is to isolate the quantitative invariant that must
turn the repeated reductions into an actual vanishing estimate.

The cycle from Rounds 420--424 has the schematic form
\[
  \text{persistent}
  \to
  \text{bounded-gap pair}
  \to
  \text{fixed-gap pair}
  \to
  \text{confined bridge}
  \to
  \text{inward-free bridge}+\text{bridge-return spread}
  \to
  \text{prefix record}+\text{long run}.
\]
It creates one additional bridge-record marker and retains new spread and
long-run terms.

Let \(K_m,D_m,A_m,B_m\) denote, respectively, the source scale, source
prefix-record coefficient, long-run coefficient, and bounded-successor budget
at one bridge-record depth \(m\).  The bounded-gap and fixed-gap steps use
\[
  B_m
  =
  \left\lceil \frac{64\beta_i}{\Theta_i}K_m\right\rceil+1
\]
and the fixed-gap scale update
\[
  K_{m+1}=8K_mB_m.
\]
The inward-free absorption step updates the coefficient by
\[
  D_{m+1}=D_mB_m
\]
and the long-run coefficient by
\[
  A_{m+1}=A_m+D_{m+1}.
\]

Therefore the important ratio satisfies the exact gain
\[
  \frac{D_{m+1}}{K_{m+1}}
  =
  \frac{D_m}{8K_m}.
\]
Thus the bridge-record cycle loses large finite factors \(B_m\), but the
new geometric scale grows by an additional factor \(8\) beyond the same
\(B_m\).  After \(r\) completed cycles,
\[
  \frac{D_{m+r}}{K_{m+r}}
  =
  8^{-r}\frac{D_m}{K_m}.
\]
This is the first non-formal descent quantity visible in the current ladder.

The long-run coefficient obeys
\[
  \frac{A_{m+1}}{K_{m+1}}
  =
  \frac{A_m}{8K_mB_m}
  +
  \frac{D_m}{8K_m}.
\]
Consequently, if \(A_m/K_m\) is already controlled and the \(D_m/K_m\) ratio
is summable along the cycle, then the normalized long-run coefficient is also
controlled.  This does not prove the theorem, but it identifies the correct
scale-normalized bookkeeping.

The remaining proof obligation is now quantitative:

1. show that each newly retained bridge-return or adjacent return-spread
   family at scale comparable to \(K_m\) is bounded, after summing over \(j\)
   and the finite \(h\)-range, by \(O(K_m^{-1})\) or a stronger decaying
   profile;
2. show that the long-run profile is controlled strongly enough that
   \(A_m W_{\beta_i,p}T^{\rm long}_{i,j}\) vanishes after the radial-tail and
   subdivision limits;
3. check that older retained spread families remain summable under the same
   normalized \(D_m/K_m\) gain and are not merely being pushed forward.

If these estimates hold uniformly in the outer finite index \(i\), the
bridge-record cycle becomes a genuine descent mechanism rather than only a
renaming ladder.  The next mathematical target is therefore not another
profile conversion, but a scale-decay lemma for the retained spread and
long-run profiles strong enough to exploit
\[
  D_{m+r}/K_{m+r}=8^{-r}D_m/K_m.
\]
