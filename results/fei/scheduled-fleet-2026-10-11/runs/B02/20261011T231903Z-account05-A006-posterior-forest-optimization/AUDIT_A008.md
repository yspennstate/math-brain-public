# Independent reconstruction of B02-A008-DICTIONARY-QUOTIENT-CODE v1

Verdict: **HOLDS at the original stated scope; no repair supplied.** This accepts a different normalized dictionary/output experiment, not the original conditioned partition-forest residual or unrestricted FEI. Original statement SHA256: ea1737df5842d834546a101d59cc86c0824308079accf5039f2261b893586367.

I reconstructed the proof from the structural sampling choices and implemented a separate product-of-four-states enumeration; no author checker was imported or executed. Read sources: A008's REPORT.md, WHOLE_SET_CODEC.tex and CLAIMS.json, run 20261011T221357Z-account05-A008-gate-label-compression. Source hashes are in out/SOURCES.json.

## Normalization, decoder and ambiguity

For a fixed finite table, first select k under kappa, then a gate set F under product eta/E_k, then independent nonempty local subsets. Successive finite summation gives exactly mass 1. Each named gate has one subset and occurs once. Union is a deterministic finite output map, whether or not local subsets overlap. The canonical ownership/source-SCC/breadth-first reconstruction is possible because each finite condensation DAG has a source ancestor for every vertex; parent attachments lie in the owning subset and child support. This reconstruction is a function of the decoded record, not an unpaid random field in the old queue.

For a finite rational mass p, the integer ceil(-log2 p) is found by comparisons with dyadic rationals. The lengths have Kraft sum <=1, so sorted canonical binary codewords exist and yield finite prefix decoding. Only one global rounding overhead is used. The finite pushforward Q(A)=sum_{D(r)=A}a(r) is normalized. A second prefix code based on Q identifies A; it may construct a canonical record, but it does not identify the sampled latent record. The KL identity gives a legitimate output-reference entropy credit, not a subtraction from the bits of a transmitted random record. The full reference includes mass 1-v at empty and vQ at nonempty, and its expected prefix length is less than h2(v)+sum P(A)(-log Q(A))+1. The chosen structural table is fixed across output sets; mixtures charge their selector.

## Independent sunflower output counting

For each of m slots use states absent, common-only, private-only, or both. A nonzero state marks an included gate, and the dictionary has canonical increasing gate order. With k included slots its mass is kappa_k/[binom(m,k)3^k], where kappa_k=(m+1)/(mk(k+1)). These weights telescope to 1. There is no child-occurrence ordering in this generator and hence no factorial multiplicity.

An output private T, |T|=t>=1, forces included gates exactly T and every local subset private-only. Thus Q(T)=kappa_t/[binom(m,t)3^t]. To produce common+T, choose u extra common-only gates outside T. For u=0 the t gates have 2^t-1 local choices (exclude all-private); for u>0 they have 2^t choices. Summing these disjoint events recovers A008's complete formula. Common-only has Q({0})=sum_k kappa_k 3^(-k)>=1/6. The checker enumerated all 5,454 records for m=1,...,6 and verified every output mass and total normalization with Fractions.

The Boolean expansion gives exactly the same spectral law as the first A006 stage, independently: common singleton mass (1-2^-m)^2; each of T and common+T has mass 4^-m; empty has mass 4^-m; I=1+(m-1)2^-m>=1.

For both rare outputs the individual cost is at most log[t(t+1)]+log binom(m,t)+t log3<=3m+2t: use t(t+1)<=(m+1)^2, m+1<=2^m, binom(m,t)<=2^m, and log3<2. The total rare cost is bounded by r_m=8m2^-m-6m4^-m. Its values at m=1,2 are 5/2,13/4. For m>=2,

    4^(m+1)(r_m-r_(m+1))=16(m-1)2^m-18m+6
                               >=46m-58>0.

Thus the complete nonempty expectation is <3+13/4=25/4<=25I/4. The binary sector and single prefix rounding each contribute at most I, proving <33I/4 for the full-output code.

Any common-only latent record has probability kappa_k/[binom(m,k)3^k]<=1/m. For k<m, binom(m,k)>=m; for k=m, 3^m>=m; and kappa_k<=1. Therefore every latent record, and every randomized selection of such a record, pays at least log m on this output. Its spectral expectation is at least (1-2^-m)^2 log m. The output quotient can erase the latent identity; a decoder required to recover that identity cannot.

## Scope and review receipt

The addressing special table has 2^a uniformly selected names and 2^a uniform control subsets, with one mandatory data coordinate; every pair yields a unique spectral output and its code has length 2a. Direct coefficient expansion gives H=2a and I=1+a/2. This is an existing calibration. A half-weight mixture adds one paid selector bit.

The finite proof above establishes A008's full combined statement at its original scope. It proves neither a bound on B_lambda nor universal selection of a cheap table. The independent trace checker passed 5,863 assertions through this review section and saved out/A008_REVIEW_CHECK.json after 4.179 seconds. Its all-m inequalities are analytic, not inferred from the finite enumeration. Shared registries and A008's files were not changed; the independent acceptance is recorded only in this run's CLAIMS.json for supervisor adoption.
