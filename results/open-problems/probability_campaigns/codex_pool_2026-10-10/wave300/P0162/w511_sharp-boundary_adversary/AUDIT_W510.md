# Independent mathematical audit of the paired proof

Auditor: w511. Target: w510's ATTEMPT.md, C001-C004, read only after the independent obstruction was saved in this folder. The verdict concerns the stated special case and auxiliary counterexamples. It does not certify unrestricted FEI or novelty.

| Claim | Verdict | Independent check |
| --- | --- | --- |
| C001 exact affine spectrum | KEEP | A character sum on a coset vanishes outside V-perp by pairing v with v+v0; inside it the normalized sum is p times the coset phase. A nonzero coordinate functional on the r-dimensional dual takes value 1 on exactly 2^(r-1) vectors. Hence I_i=2p and I=2pm. There are 2^r-1 nonzero squared coefficients 4p^2, giving the stated entropy. |
| C002 sharp class constant 4 | KEEP | Dual support size m is at least r by injectivity into F_2^m. The bound -q ln q <= 1-q is valid for 0<q<1 and produces the displayed upper bound below 4. For r>=2 entropy is positive and fixed, so equality in the fixed-r maximum requires m=r. The dual is then a full coordinate space; the primal is a translated coordinate subcube. The nonempty term gives limit 4. |
| C003 conditioning mass | KEEP | Write each nonempty spectral probability as vQ(s). Direct expansion gives H=h_2(v)+vH(Q) and I=vE_Q|S|, including v=1. Constants have no defined Q and are excluded. For coordinate codimension-r subcubes, H(Q)=log_2(2^r-1) and I=r2^(1-r), so the proposed unweighted bridge fails. |
| C004 coordinate charging and dependence | KEEP | The first coordinate in every deterministic ordering has the same marginal a=2^(1-r); h_2(a)/a>=r-1. For two specified coordinates, 2^(r-2) spectral indices contain both, so joint mass is p and product mass is 4p^2. These differ for r>=3. Input independence does not imply spectral independence. |

I tried the main step at r=0, r=1, p=1/2, inactive coordinates, a translated affine space, an oblique dual space with m>r, and variance tending to zero. The proof explicitly separates constants and parity and preserves the mass v after conditioning. I found no missing premise in C001-C004. The independent exhaustive check in verify_affine_audit.py uses every affine subspace in ambient dimensions 1 through 4, after a fresh compute gate; its measurement file records the result.

The hardest general gap is still a dimension-free estimate for vH(Q) when Q is an arbitrary realizable Boolean spectrum. Flat affine support was essential to the proof. A general argument also needs an explicit bound for h_2(v); a standard edge-isoperimetric argument can supply such a bound, but C001-C004 do not prove it for arbitrary Boolean functions. Thus the four kept claims remain special cases and counterexamples.

The independent bent-point-flip obstruction in ATTEMPT.md addresses restriction entropy drop, a different quantity from the chain entropy of spectral-coordinate bits in C004. It does not contradict the affine proof and must not be conflated with that counterexample.

NEXT: w512 should independently check these four claims and the sharp profile proof in this folder before any theorem promotion.
