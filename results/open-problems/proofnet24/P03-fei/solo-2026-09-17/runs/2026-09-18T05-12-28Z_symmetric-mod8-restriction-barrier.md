# Solo FEI continuation: transitive mod-8 restriction barrier

## Outcome

Full Friedgut--Kalai Fourier entropy--influence remains **OPEN**. This
continuation closes the most plausible repair left by the preceding Shannon
barrier: neither choosing a favorable coordinate nor averaging over all
coordinates can extend the unequal-NAND potential to a dimension-free
restriction induction.

For every `n` divisible by 8, define

    A_n(x)=1{|x| mod 8 in {0,1,2}}.

For the complement-invariant indicator potential `W_c=U+cQ`, with any fixed
real `c`, let

    D_i=W_c(A_n)-[W_c((A_n)_{i=0})+W_c((A_n)_{i=1})]/2.

Then every coordinate is equivalent and

    D_i/Inf_i(1-2A_n)=gamma n+o(n),

where

    gamma=(3sqrt(2)/8)sin^2(pi/8)log_2(cot^2(pi/8))
         =0.19751... >0.

Therefore no universal constant controls even the best coordinate, and the
aggregate ratio is identical. This includes the unequal-NAND potential
`c=2/ln2`. It is a proof-method obstruction, not a counterexample to FEI or to
`W_c<=CI`.

All work in this continuation was done by the primary assistant. Subagents,
delegated tasks, other-model calls, commissioned audits and outside contacts:
zero. Actual model and reasoning-level metadata are not exposed and are
therefore **UNVERIFIED**.

The freshly read master head at the start was
`5f07753df0c6c94cdf8892d4b3df29df36031b24`; the newest prior solo commit was
`b60d428145fb94991c9b6807f1de7d6321a97313`. The current exclusion material,
latest P03 handoff, solo continuation notes and newest barrier proof were read
first. The original P03 finite-dimensional metric 6 remains a prior reported
fact only; its exhausted enumeration was not resumed.

## 1. Why this was the live question

The previous continuation proved an unbounded restriction defect at one
marked selector coordinate. It explicitly left open two possibilities:

    some coordinate i has D_i<=C Inf_i,

or

    sum_i D_i<=C sum_i Inf_i.

Either would support a recursive extension of the disjoint-product potential.
The new symmetric family refutes both because all coordinates have the same
linearly growing normalized defect.

An intermediate calculation on the bent-marker family is retained in
`FAVORABLE_COORDINATE_SEPARATION_2026-09-18.md`. It proves that, for every fixed
`c`, all marker-coordinate defects are eventually positive, but its data
coordinate defect/influence ratio tends to zero. Thus the marker sharply
separates worst-coordinate from best-coordinate behavior but does not itself
refute a constant favorable-coordinate theorem. This motivated the transitive
search rather than another unrestricted truth-table enumeration.

## 2. Exact spectral decomposition

Let `omega=exp(pi i/4)` and

    alpha_r=(1+omega^(-r)+omega^(-2r))/8.

The coefficient on every Fourier set of size `k` is exactly

    c_{n,k}=sum_{r=0}^7 alpha_r
       ((1+omega^r)/2)^(n-k)
       ((1-omega^r)/2)^k.

This follows by inserting the eighth-root filter for the periodic value
sequence and factoring the sum over bits.

Put

    a=cos(pi/8), b=sin(pi/8), q=b^2,
    R=a^2/b^2, L=log_2 R.

There are three asymptotically disjoint spectral bands:

- `r=1,7`, centered at level `qn`;
- `r=2,6`, centered at `n/2`;
- `r=3,5`, centered at `(1-q)n`.

For `8|n`, the middle band alternates zero and constant-magnitude levels, so
its positive edge cost is zero. The outer bands have fixed adjacent squared
ratio `R`. Since

    |alpha_1|^2+|alpha_3|^2=3/32,

binomial summation gives

    W_c(A_n)/n -> kappa=(3/16)qL.

The two restrictions have dimension `n-1`. In each outer band, one parity of
levels has equal adjacent masses and the other has ratio `R^2`; the middle
band has constant squared mass. Both children therefore satisfy

    W_c(child)/(n-1) -> kappa_child=(3/8)q^2L.

Singleton entropy and every fixed `cQ` correction are exponentially small.
Hence

    D_i/n -> (3/16)q(1-2q)L.

## 3. Exact influence and normalized constant

A coordinate changes the function exactly when the other `n-1` bits have
weight congruent to 2 or 7 modulo 8. The binomial residue distribution tends
to uniform, again by the eighth-root filter, so

    Inf_i -> 1/4.

Multiplying the defect limit by four yields the stated `gamma`. Symmetry makes

    min_i D_i/Inf_i
      =[sum_i D_i]/[sum_i Inf_i]
      =gamma n+o(n).

This proves both restriction barriers at once.

## 4. Exact checks

Executed from the solo folder:

    python check_favorable_coordinate_separation.py
    python check_symmetric_mod8_restriction.py
    python -m py_compile check_favorable_coordinate_separation.py
    python -m py_compile check_symmetric_mod8_restriction.py

Both scripts returned `PASS`.

The first compares the exact bent-marker data-branch formulas with full Walsh
transforms for `m=2,4,6,8,10,12`; all coordinate defects are rigorously
positive for the actual NAND potential at `m=6,8,10,12`.

The second computes symmetric Walsh coefficients as exact Krawtchouk sums and
uses 160-bit outward rational logarithm intervals. It agrees with full truth
table transforms at `n=4,8,12`, checks the symmetric formulas through `n=64`,
and proves

    D_i/Inf_i > n/6

at `n=32,40,48,56,64`. The all-dimensional asymptotic is proved analytically;
finite computation is only a self-check and not an independent audit.

## 5. Search path and failed weaker route

The bent-marker calculation first showed

    D_data=[(m+2)/(8ln2)]2^(-m/2)+O(m^2 2^(-m)),

while its selector defect is order `m2^(-m)`. This proves eventual positivity
at every marker coordinate, but the best normalized ratio tends to zero and
the aggregate ratio tends to zero. It could not rule out constant-charge
coordinate choice.

A structured search was then restricted to symmetric Hamming-weight
functions, whose spectra have only `n+1` distinct coefficients. It identified
the period-eight pattern `11100000`. The computation suggested linear growth;
the root-of-unity calculation above supplies the proof. This was not a repeat
of the exhausted finite Boolean-cell enumeration, and no finite maximum is
claimed.

## 6. Literature and novelty limits

Fresh primary-source searches included:

- `site:arxiv.org Fourier entropy influence conjecture symmetric Boolean functions modulo Hamming weight restriction induction`
- `site:arxiv.org "Fourier Entropy-Influence" symmetric functions restriction`
- `site:arxiv.org Fourier entropy influence mod 8 Boolean function`

They did not identify a directly matching restriction-potential obstruction.
Search failure is not a novelty proof. The construction and asymptotic are
therefore labeled **novelty UNVERIFIED**. Known coordinate-restriction and
composition frameworks already acknowledged in earlier reports remain prior
art.

## 7. Exact remaining obligation

The full target remains

    K(f)=sum_edges min(p_S,p_T)|log_2(p_S/p_T)|
       <=C sum_S |S|p_S

under the signed Boolean convolution identities. The new theorem removes the
entire route

    unequal-NAND potential
      -> choose or average one-coordinate restrictions
      -> induction on arbitrary Boolean functions.

What remains genuinely live is a signed non-reusing multiscale transport, or a
nonlocal block theorem whose accounting is not the sum of coordinate defects.
No such inequality is proved.

## 8. Measured execution

The supplied run start was 2026-09-18T04:57:00Z and the first sampled shell
clock was 04:57:21Z. This report checkpoint is 05:12:28Z: 15 minutes 28 seconds
from supplied start and 15 minutes 7 seconds between sampled shell clocks.
This includes retrieval, derivation, structured search, exact checking,
literature search and writing; it is not a claim of continuous model compute.
GitHub delivery time is not included.

Intervals between continuations are not counted as research time. Neither the
schedule nor this report establishes an hour of work or ten continuous hours.
