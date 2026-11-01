# QFORM B20 r24 — physical third-resource wedge/anchor quantization

Status: `ESSENTIAL_STEP_APPLIED / O3-STAR-THIRD-RESOURCE-QUANTIZED / FULL_TARGET_OPEN`.

Target: for independent real coordinates with densities at most one and real symmetric A with at least three eigenvalues of modulus at least one, prove a universal essential density bound for X^T A X or give a valid counterexample. No moment, support, log-concavity, diagonal-basis or post-rotation-independence assumption is used below. Continuity is not claimed.

## Sources actually consumed

Fresh designated-partner source is fleet03/B20 r22, canonical math `5de4e98c424cd036c97126ffa3d6abef6191b0e1`. In its exact-rank-three robust 2+1 O3 chamber, the whitened-diffuse case is paid by `<162`, the physical-pivot case by `<1215`, and every surviving state contains an ORIGINAL coordinate i in the selected original-coordinate block L with

`|A_ii| < 1/48`, `||A[i,L\{i}]||_2 > 1/48`.

Moreover the selected physical block C=A[L,L] has a factorisation `C=V N V^T`, `V^T V=I`, with `s_min(N)>=delta>1/6`; hence `s_3(C)>1/6`.

The pinned interactive source `e5f71d79eff325201dd0274053d20268ce65b837` is used at equation level in two places. First, its Theorem H pays any exact `one physical hub + one rank-one leaf square + diagonal leaf twist` state satisfying the normalized mixed-frame leverage bound: with H={i}, r=1,

`|phi(t)| <= 4 pi^(3/2) |lambda|^(-1/2) det(Gtilde)^(-1/2) |t|^(-3/2)`,

so `||p_Q||_inf <= 3*4^(2/3) (|lambda| det(Gtilde))^(-1/3)`.

Second, its unrestricted fifth-volume theorem from the accompanying Fourier route remains a paid exit on any ORIGINAL physical cross block M:

`||p_Q||_inf <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`;

in particular `e_5>=1/1024` gives `<10 sqrt(2e)<23.317`.

The newest compatible two-gradient receiver is fleet03/B19 r24: for two ORIGINAL coordinates and a disjoint ORIGINAL product bank, if the 2-row physical cross matrix M has `Delta2=sqrt(det(MM^T))>0`, then

`sup_z P(|R-z|<=eps) <= 12(2 Delta2)^(-1/3) eps^(2/3)`

and `sup_z E|R-z|^(-1/2) <21.687 Delta2^(-1/4)`.

## New theorem: QFORM-STAR-THIRD-RESOURCE-WEDGE-ANCHOR-v1

Let a real symmetric physical-coordinate block be

`C = [[a,m^T],[m,B]]`,

where `m in R^d`, `r=||m||_2>0`, and B is real symmetric. Put `gamma=s_3(C)` and assume `gamma>0`.

For each physical leaf j define

`W_j = sum_{k<l; k,l != j} (m_k B_{jl} - m_l B_{jk})^2`,

`E_j = sum_{k != j} (m_j B_{jk} - B_{jj} m_k)^2`.

Let `W=sum_j W_j`, `E=sum_j E_j`. Then

`boxed: W+E >= r^2 gamma^2 / 2`.

### Proof

Let `b_j` be row j of B. The full squared wedge area between m and b_j is

`F_j := r^2 ||b_j||_2^2 - <m,b_j>^2 = sum_{k<l}(m_k B_{jl}-m_l B_{jk})^2`.

The terms with neither index equal to j are exactly W_j; the terms with one index equal to j are exactly E_j. Hence

`F:=sum_j F_j = W+E`.

Put `e=m/r`, `P=I-ee^T`. Row summation gives the exact identity

`F = r^2 ||B P||_F^2`.

Decompose B orthogonally as

`B = alpha ee^T + e z^T + z e^T + B_0`,

with `z perp e`, `B_0=P B P`. Then

`||B P||_F^2 = ||z||_2^2 + ||B_0||_F^2`,

whereas the Frobenius distance to the one-dimensional family `span{mm^T}=span{ee^T}` is

`dist_F(B,span{mm^T})^2 = 2||z||_2^2 + ||B_0||_F^2 <= 2||BP||_F^2 = 2F/r^2`.

For every scalar c, the matrix

`C_c = [[a,m^T],[m,c mm^T]]`

has rank at most two: every leaf column is a scalar multiple of `[1; c m]`, together with the hub column `[a;m]`. Therefore Eckart--Young gives

`gamma=s_3(C) <= ||C-C_c||_op <= ||B-cmm^T||_F`.

Taking the infimum over c and combining with the previous display yields

`gamma^2 <= 2F/r^2`, i.e. `F=W+E >= r^2 gamma^2/2`. QED.

This proof is entirely in original physical coordinates. There is no source rotation, no conditional projected-density substitution, no worst-fiber supremum, and no pointwise oscillatory-decay assertion.

## Exact application to the newest designated-partner survivor

In fleet03/B20 r22, the selected physical block C has

`gamma=s_3(C)>1/6`, `r=||A[i,L\{i}]||_2>1/48`.

Therefore the new theorem gives the fixed dimension-free third-resource packet

`boxed: W+E > 1/165888`.

Consequently

`boxed: W>1/331776  or  E>1/331776`.

This is strictly stronger than the previous statement that a single strong star survives: the third spectral direction is now forced into one of two explicit ORIGINAL-coordinate aggregate currencies.

The W packet is precisely aggregate currency for the two-physical-gradient receiver. For a particular j, the physical cross matrix from the original pair {i,j} to the other leaves has rows `(m_k)_{k!=j}` and `(B_jk)_{k!=j}`, so

`det(M_j M_j^T)=W_j`, `Delta2_j=sqrt(W_j)`.

Hence any subbranch with one `W_j >= 1/331776` is immediately upgraded to

`sup_z P(|Q-z|<=eps) <79.247 eps^(2/3)`,

and its half-Riesz currency is `<106.245`. These exponents cross the square-root singularity threshold needed by the already-completed scalar/pair transducers. The genuinely new residual issue is therefore not existence of a second-gradient resource, but how to spend it when W is diffusely distributed over many weak physical rows.

The E packet consists of anchored physical 2x2 minors

`m_j B_jk-B_jj m_k = det [[m_j,m_k],[B_jj,B_jk]]`.

It must be paid in aggregate: the live correction forbids promoting aggregate minor mass to a single uniformly good reciprocal minor. In the exact rank-one-plus-diagonal leaf geometry, the pinned Theorem H is already the natural payment mechanism; robustness to a small dense twist is exactly the source's stated missing estimate.

## Strongest conditional end-to-end position

The current source-pinned graph pays: diffuse selected-frame O3 (`<162`), physical pivot (`<1215`), compatible robust indefinite physical pair (`<194` from B20 r23), fixed collective-tail certificates (`<107` from B20 r23), high fifth-volume physical cross blocks (`<23.317`), and now every surviving O3 star is forced to carry `W+E>1/165888`. A robust single W_j is paid to 2/3-small-ball scale by the newest two-gradient theorem and can be linearly completed whenever a paid disjoint singularity transducer is present.

The full target is not yet closed. Separate upstream N3/O0 low-volume packets and arbitrary-extra-spectrum descent also remain.

## First unpaid implication

`QFORM-O3-STAR-AGGREGATE-WEDGE-OR-ANCHOR-PAYMENT-v1`.

Full hypotheses: original independent cap-one product source; the exact-rank-three robust 2+1 O3 selected physical block of fleet03/B20 r22; diffuse and pivot exits failed; `|A_ii|<1/48`; `||A[i,L\{i}]||>1/48`; arbitrary same-side and conditioned outside couplings retained; and therefore `W+E>1/165888` as proved above.

Required conclusion: obtain a universal linear small-ball/density bound by either

1. spending diffuse aggregate W with a multi-gradient/source-product receiver without selecting a vanishing W_j, or
2. spending aggregate anchored-minor E through Theorem-H/ridge/grouped-square/pair geometry without reciprocal-minor extraction,

or source-preservingly reduce either branch to a previously paid packet.

The next mechanism should be aggregate-before-inversion. A second Cauchy--Schwarz that merely reproduces a square-root collar is insufficient, and conditioning on a rotated projection and treating it as independent is forbidden.

Full QFORM: OPEN / NOT PROVED / NOT DISPROVED. Global continuity: OPEN.
