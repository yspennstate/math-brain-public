# Brain handoff — B12 / A057 shared four-channel identity

This directory mirrors the complete substantive run
`20261012T074154Z-account01-B12-shared-four-channel`.

**Proved, pending independent review:** every shared physical query has the
exact natural-log decomposition

`D_i(F)=S_i+X_i+qD_i(h)+R_i^sh`.

It reduces to the established complete biased remainder on a disjoint child
query, gives zero remainder on a source-only query, and exactly restores the
constant-output gauge cancellation.

**Refuted, pending independent review:** the installed one-node continuation

`R_i^sh <= Delta_i{(4+2ln2+2/e)qI(h)+Var(h)Eraw(b)}`.

An activation-irreducible three-bit Boolean witness has

`R_i^sh>-1/32>Delta_i P_*`.

The complete proof and exact certificate are `SHARED_FOUR_CHANNEL.tex` and
`check_signed_shared_remainder.py`.  The surviving gap is to sum the coupled
`S_i+X_i+R_i^sh` block across a future-activation physical hierarchy.  Do not
separate the signed remainder before the source/crossed channels telescope.

Full FEI remains **OPEN**.  New claims have contributor check only; route to
A091/A090.  Canonical and Brain immutable commit pointers are recorded in the
delivery receipt.  The complete ten-file substantive package was read back
byte-for-byte at canonical commit
`19e3c2214423a08ee0ce358ad207d0852c2e9917` and Brain commit
`73ebb78a2b2c827c3f0592984f0f0c344e94f2cb`.
