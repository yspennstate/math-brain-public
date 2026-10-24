# B18 / A087 — independent review of the modulation-block hierarchy

**Run:** 20261012T015740Z-account01-B18-a087-modulation-review  
**Primary packet:** A087 (Restriction referee)  
**Reviewed target:** B06-A027-MODULATION-BLOCK-HIERARCHY@1  
**Attempt:** A087-MODULATION-REVIEW-2  
**Verdict:** reviewed theorem **ACCEPTED at its exact restricted scope**;
point-defect constant sharpened from \(9/2\) to \(4\), pending fresh review.
Full FEI remains **OPEN**.

## Main review result

The original B06 proof was reconstructed from the actual theorem artifact.
For
\[
F(x,z)=g(x_1h_1(z),\ldots,x_nh_n(z)),\qquad
h_S=\prod_{i\in S}h_i,
\]
the exact coefficient identity
\[
\widehat F(S,T)=\widehat g(S)\widehat{h_S}(T)
\]
is correct. It gives
\[
H(F)=H(g)+\sum_S\widehat g(S)^2H(h_S),
\]
\[
I_X(F)=I(g),\qquad
I_Z(F)=\sum_S\widehat g(S)^2I(h_S).
\]

Every physical \(Z\)-child is obtained from \(g\) by input sign flips, so its
squared spectrum is exactly that of \(g\). Thus the conditional mixing term is
exactly \(M_Z=0\); no mismatch or KL credit is being silently discarded.
Sequentially revealing the fresh block counts every \(Z\)-edge exactly once,
with its true fair-tree reach probability. Disjoint fresh blocks therefore
iterate without influence reuse, and the final sign-flipped base entropy is
retained.

The theorem is noncircular because it assumes an FEI constant only for the
explicitly occupied auxiliary products \(h_S\), not for arbitrary Boolean
functions. It does not assert that every Boolean function admits such a
representation.

## New sharpening

For the point defect \(q_m\), \(N=2^m\), and
\(\delta=4(N-1)/N^2\),
\[
I(q_m)=\frac{2m}{N},\qquad
H(q_m)=h_2(\delta)+\delta\log_2(N-1).
\]
The elementary inequality \(h_2(u)\le u\log_2(e/u)\) gives
\[
\frac{H(q_m)}{I(q_m)}
<
\frac{2}{m}\bigl(2m+\log_2e-2\bigr)<4
\qquad(m\ge2).
\]
For \(m=1\) the ratio is zero, and the exact formula tends to \(4\).
Therefore the nonlinear arbitrary-depth subclass has the sharper bound
\[
H(f_L)\le\max(C_0,4)I(f_L),
\]
and \(4\) is asymptotically sharp for these auxiliary products. This
strengthening is a new contributor claim and must be independently reviewed
by A094 or A085.

## Independent computation

The separate checker passed 939,550 assertions:

- 20,480 exhaustive one-step Boolean modulation instances;
- 256 two-level hierarchies;
- exact point-defect Fourier laws and influences for \(1\le m\le16\).

All Fourier, branch, influence, and sequential ledger assertions used exact
rational arithmetic. The largest displayed finite ratio was
3.9302714045408793 at \(m=16\). This numerical value is diagnostic; the
all-\(m\) bound is the proof in **POINT_DEFECT_SHARPENING.tex**.

## Controls

The review explicitly checked constant products, the empty spectral set,
character plateaux, actual physical children, path weights, the retained
terminal, and coordinate nonreuse. Addressing and near tensors enter only as
bases with known constants. Bent splices remain outside the theorem because
their branch squared spectra differ. Universalizing the auxiliary-product
hypothesis would be FEI-hard and is not done.

## Exact remaining obstacle

The first universal gap is unchanged but sharper: control the first proper
physical block whose branches do not share one squared spectrum. Such a proof
must pay the nonzero conditional mixing term and terminal entropy with actual
path probabilities and without charging any physical influence twice.

This is not a full-FEI proof, a counterexample, an infinite-depth theorem, or
acceptance of any unequal-branch stopping policy.

## Source pins

- B18 contract blob e6e014bc066a2f8b0454a1944ef6e03b969a5690.
- Protocol blob 457358ff62cbf1141a72096bcabdf95bf18c1be2.
- Stream index blob 58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704.
- Packet status blob 1beba565780ac4c3c1f28a00b20ca4d5e4e59ebb.
- Claim registry blob bceaed2294e4dab574d363750858c6d3866137f8.
- Obstruction registry blob e111933338dff1d7798c5e59b43700bbf30f7b96.
- B06 original report blob b60891374b632476414b559358d6581fef43804a.
- B06 proof blob 9927e481b42d747006b834a68f070ed208180019.
- B06 checker blob 2cbb1ea3a91e06c951889ccc76a3c034b9750dbd.
- Source head before this review: 655241557ba83c4deb77ba8ac51d766b6c25f186.

## Routing

The accepted restricted theorem can be consumed by A028, A029, A065, A096,
and A097. Route the sharper constant to A094 or A085 for fresh review, because
B18 contributed it. Route the unequal-branch first gap to A089.

No scheduler change, additional worker, publication, native Brain ingestion,
or full-FEI result is claimed. The runtime exposed no separate model or
reasoning-effort selector.
