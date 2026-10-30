# A084: continuum certificate for the biased AND restriction

## exact target, quantifiers, hypotheses and units

For independent X~Bernoulli(p), Y~Bernoulli(q), g(X,Y)=(-1)^(XY), and physical restriction A={X}, determine the sign of F(p,q)=J_A-M_A for every (p,q) in (0,1)^2. The orthonormal characters are (X-p)/sqrt(p(1-p)) and (Y-q)/sqrt(q(1-q)). All entropies are in bits. J_A is mutual information between the physical X child and its remaining spectral label; M_A is conditional entropy of the spectral X label given the spectral Y label. Boundary values below mean continuous limits of this experiment.

**Resolved scope:** F>0 throughout the real rectangle [1/10,3/20] x [1/5,3/10]; a separate certified cover gives 94 negative boxes in [1/16,15/16]^2. Boundary identities and pointwise boundary sign reductions are proved below. **The requested full-square sign map is OPEN.** Its compact cover retains 902 unresolved boxes. No assertion that a grid covers all real biases is made.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full. The canonical README, CURRENT_STATUS, claim/obstruction/packet registries, next actions, and campaign plan were read/scanned; the A084 acceptance contract is in the plan's B17 subsection. The board snapshot is 2026-10-11 22:47 UTC; B17 STREAM_NOTES v1, 22:40 UTC assigns this AND sign map. The supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and sources were scanned; no supplemental theorem is used as a proof premise. The four context paper text versions were scanned, with current threshold Proposition 7.1 and Corollary 7.2, and percolation Theorems 3.1-3.2 inspected as scope references. The latter's pivotal entropy bound is not substituted for spectral conditional entropy. Earlier B05/B09/B19 reports were scanned, and B09 REPORT sections 2 and 4 locate the restriction experiment and prior isolated AND witness. All text source paths and SHA256 pins are in out/SOURCE_MANIFEST.json; extracted locators are in out/SOURCE_EXCERPTS.txt. These reads do not constitute independent acceptance of the papers or earlier runs.

## complete derivation or exact first unsupported line

Put r=4q(1-q), t=pr. Expanding 1-2XY by centered Bernoulli characters gives the signed coefficients

    1-2pq, -2q sqrt(p(1-p)), -2p sqrt(q(1-q)),
    -2 sqrt(p(1-p)q(1-q)).

Thus the squared masses in the order empty,X,Y,XY are

    a=(1-2pq)^2, b=4p(1-p)q^2, c=p^2 r, d=p(1-p)r.

Their sum is 1 and c+d=t. The physical X=0 child is constant; the X=1 child is 1-2Y, with nonempty spectral mass r. Consequently

    J_A=h(t)-p h(r),
    M_A=H(a,b,c,d)-h(t),
    F=2h(t)-p h(r)-H(a,b,c,d).                 (1)

Here h is binary entropy and 0 log 0=0. The useful alternative, avoiding the four-atom entropy, is

    M_A=(1-t)h(b/(1-t))+t h(p),
    F=h(t)-p h(r)-(1-t)h(b/(1-t))-t h(p).     (2)

At the isolated point t=1 use the continuous interpretation. This occurs only at p=1,q=1/2 on the closed square.

### Exact boundaries and the internal zero line

Direct substitution in (1) yields

    F(0,q)=F(1,q)=F(p,0)=0,
    F(p,1)=-h(4p(1-p)),
    F(p,1/2)=0.                              (3)

The entire q=1/2 line is therefore zero, not merely the rational sample points. On that line the four masses are ((1-p)^2,p(1-p),p^2,p(1-p)), so their entropy is 2h(p), whereas t=p and r=1.

For a fixed p in (0,1), differentiation at q=1/2 is legitimate: the potentially singular term h(r) has increment O(u^2 log(1/|u|)) where u=q-1/2, and all four parent masses there are positive. Since t_q=r_q=0 at q=1/2 and a_q=-4p(1-p), b_q=4p(1-p), c_q=d_q=0,

    F(p,1/2+u)=-4p(1-p) log2((1-p)/p) u
                +O_p(u^2 log(1/|u|)).        (4)

For fixed p<1/2, F is positive just below that line and negative just above it. For fixed p>1/2 the signs reverse. These neighborhoods depend on p. No assertion of a uniform strip through p=1/2 or p=1 is justified by (4).

The four outer edges also have analytic reductions. The elementary natural-log expansion is

    h(z)=z log2(1/z)+z/ln(2)+E(z),
    |E(z)| <= z^2/[2 ln(2)(1-z)]  (0<=z<1). (5)

Indeed, -(1-z)ln(1-z)-z=-sum_{k>=2} z^k/[k(k-1)], with absolute sum at most z^2/[2(1-z)]. Using (5) on vanishing atoms and ordinary Taylor estimates on positive atoms in (1) proves the following pointwise limits:

    lim_{p->0} F(p,q)/(p log2(1/p))=4q(1-2q)
        for every fixed 0<q<1;
    lim_{p->1} F(p,q)/((1-p)log2(1/(1-p)))=-4q
        for every fixed 0<q<1, q!=1/2;
    lim_{q->0} F(p,q)/q=4p(1-p)log2((1-p)/p)
        for every fixed 0<p<1.               (6)

For clarity, in the first limit the atom entropy coefficient is b+d=4pq+O(p^2); twice h(t) contributes 2pr, and p h(r) has no p log p term. In the second limit the newly vanishing atoms b,d have total mass 4q(1-p)+O((1-p)^2); J has no (1-p)log(1-p) term when r<1. In the third limit, b=O(q^2), c+d=4pq+O(q^2), and H=h(4pq)+4pq h(p)+O_p(q^2 log(1/q)); this gives the stated coefficient.

At p=1/2, the third coefficient vanishes, but the exact identity H=2h(q) gives

    F(1/2,q)=2h(2q(1-q))-(1/2)h(4q(1-q))-2h(q)
            =-2q^2 log2(1/q)+O(q^2)          (q->0). (7)

This is negative sufficiently close to q=0. It is symmetric under q->1-q, proving the same near q=1. For every other fixed interior p, F(p,1)<0 by (3) and continuity. Thus all four edges have pointwise analytic sign reductions, including their exceptional fixed-bias cases. Joint corner scaling and transition curves are not settled by these pointwise reductions.

The extra zeros can already be proved to exist, without assigning them shapes. For every fixed p>1/2, (4) gives F>0 just above q=1/2 while (3) gives F<0 near q=1. The intermediate value theorem supplies at least one extra zero in (1/2,1). Moreover code/topology.py certifies F(49/100,1/4)<-11/100. At p=49/100, (6) gives a positive neighborhood of q=0 and (4) a positive neighborhood just below q=1/2. There are therefore at least two extra zeros in (0,1/2), one on each side of q=1/4. The fixed point and exact log enclosure are saved in out/ZERO_TOPOLOGY.json. This refutes a proposed sign map containing only q=1/2, and shows why a universal monotonicity claim in q cannot be used.

### Interval certificate: all points of each box are covered

The checker uses only fractions for signs. For x>0, multiply x by a power of 2 to place it in [1,2], and set z=(x-1)/(x+1). For N=20,

    ln x = 2 sum_{j=0}^{N-1} z^(2j+1)/(2j+1) + R_N,
    |R_N| <= 2|z|^(2N+1)/[(2N+1)(1-z^2)].

The same series encloses ln 2. The quotient is enclosed by the minimum and maximum of all four endpoint quotients; this handles negative logarithms correctly. Bounds are rounded outward to multiples of 2^-48 using integer floor/ceiling. No binary64 values participate in a sign decision.

Interval addition, multiplication and squaring enclose the exact masses. Intersecting a mass interval with [0,1] is valid since these are genuine probability atoms. The interval for r uses concavity of 4q(1-q). For phi(x)=-x log2 x with a positive lower endpoint, monotonicity of log and interval multiplication suffice. If a mass interval starts at zero and has upper endpoint <=1/4, phi is increasing there (ln 4>1), so [0,phi(upper)] encloses it. Otherwise [0,1] is a valid crude bound. Binary entropy intervals use its concavity, with maximum 1 if the interval crosses 1/2. Combining these operations in (1) encloses F on the entire box.

The positive rectangle splits into 64 final boxes, each with rational F lower endpoint >0. Each split bisects one coordinate and retains both children, so the union of the leaves is the complete initial rectangle, including its boundary. The compact cover uses the same rule; its sign-negative leaves are rigorous, while unresolved leaves are retained.

### Finite-to-continuum completeness lemma, with its limitation

For a compact K contained in (0,1)^2 with a known positive separation min_K |F|>0, adaptive rational boxes and successively increased N and output bits produce a finite sign certificate on K. Proof: phi and h are continuous including their zero endpoints; their interval enclosures shrink with the argument intervals and arithmetic errors. Every point with nonzero F has a sufficiently small rational neighborhood with the same certified strict sign. Compactness gives a finite subcover. This is a rigorous continuum bridge, but the separation assumption cannot be silently applied to this whole square: it contains the exact zero line and additional sign transitions. Fixed N=20,48 bits alone cannot certify arbitrarily tiny strict margins.

**Exact first unsupported line:** that the unknown additional zero curves have a specified count/shape, or that all 902 unresolved compact boxes can be assigned a sign by the fixed-bias boundary reductions. Neither has been proved. In particular an exact description of the complete failure region {F>0} beyond the certified open/closed rectangles remains open.

## executed validation with domain, arithmetic, commands and outputs

The frozen spec precedes the searches. The binary64 pilot is evidence only (88 evaluations, explicit two-bit family). The certificate command is `python -X utf8 code/certify.py` from the run directory, equivalently `python -X utf8 runs/20261011T224831Z-fleet05-A084-continuum-parameters/code/certify.py` from the agent directory. Observed certificate runtime: 57.235 seconds. It visited 1991 boxes on [1/16,15/16]^2 and returned 94 negative and 902 unresolved leaves; the separate positive rectangle returned 64 positive leaves and no unresolved leaf. Files: out/POSITIVE_RECTANGLE.json, out/COMPACT_COVER.json, out/RESULT.json. Runtime was under the frozen 60-second pilot cap; memory estimate <100 MB, no >300 MB job was launched. No dimension escalation or GPU was used. Code and leaf receipts are saved for a reviewer to reconstruct the bounds.

## proof dependencies and changed downstream conclusions

The sign certificates depend on direct Bernoulli Fourier expansion, elementary Shannon chain rule, and the proved series remainder above. They do not depend on the unreviewed B09 universal uncertainty theorem or on a Maassen-Uffink premise. The previous isolated B09 falsifier expands to a real positive-area rectangle. It is therefore a robust continuum obstruction to tax-free transfer at induced biases, not a numerical artifact at one rational point. This does not bound conditional entropy by influence, pay a stopping tree, or settle uniform FEI.

## one next mathematical action and independent reviewer

Next: obtain an interval enclosure for the normalized divided difference F(p,q)/(q-1/2), using analytic treatment of the vanishing h(r) term, then prove or refute monotonicity in p on each side of q=1/2. This attacks the unclassified zero curves directly; simply enlarging the grid spends effort near known exact zeros. Independent reviewers: A090 (primary), A094 (alternate); consumers B09/A041/A046 and B13/A064.

## actual persistence receipts or precise save blocker

All source, output, proof, protocol-shaped ledger and rolling files are under the A084 directory. out/RECEIPTS.json records SHA256 and sizes and the schema/leaf validation. Each file is below 20 MB. Shared trees and other agents' folders were read only. No git, brain writes, external messaging, upload, or shared-index mutation was performed; supervisor copy and independent review are pending.

**Universal bridge:** This stage moves the B17-lead target of continuum-certified biased restriction payment, feeding C019 stopping-tree payment and G-BIASED-TAX: a single AND witness now has a proved positive-area continuum region, with exact zero-line and four-edge reductions. It does not improve the universal C019 payment constant; conditional label cost, joint corner regimes, extra zero curves, and nonreusing physical influence payment remain. The NEXT divided-difference/monotonicity step targets exactly the continuous bias obstruction encountered by composition and restriction arguments, making it a shorter route to a valid universal bridge than another isolated sample or a larger uniform-cube census.
