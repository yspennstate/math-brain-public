VERDICT: PROVED exact three-bit optimizer and its unique stationary first-order Markov exception

For the three-bit binary deletion channel, let M_3(d)=max_P I(X^3;Y), in bits per block. PROOF.md gives its unique maximizing distribution for every 0<d<1 through one strictly monotone scalar equation. It also proves that this distribution is a stationary first-order Markov marginal at exactly one deletion probability d_*. An exact characterization and rigorous bracket are

    B(d_*/(1-d_*))=0,    1/2<d_*<2/3,

where B is given in PROOF.md (4) and is strictly concave in its positive argument. Numerically,

    d_* approximately 0.5411822311387567,
    Markov flip probability approximately 0.1631254884527100.

The decimal values are estimates. The existence, uniqueness and rational bracket are proved without numerical root finding.

At d=1/2 the optimizer has constant-word orbit mass a equal to the unique root in (0,1) of

    85a^3-239a^2+244a-81=0.

Its other orbit masses are 8(1-a)/9 and (1-a)/9. The resulting exact finite-block value is

    M_3(1/2)=3/8+(3/8)log2(6/(1+2a))+(1/8)log2(2/a).

Numerically a is approximately 0.6508389034459541 and M_3(1/2)/3 is approximately 0.3652690590790527 bits per input bit. The candidate Markov optimum at d=1/2 is excluded by the exact positive derivative log2(6561/5776).

This does not solve C(d), improve the best known asymptotic bounds, or establish that a Markov process is suboptimal for the infinite channel. It is a finite special case. The standard symmetry and run-count reduction for length three is already known; no literature-priority claim is made for this specialization or the exceptional parameter.

Reproduction, from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_three_bit.py
```

The script writes results.json, results.csv and computation_output.txt, and appends its command and full output to LOG.md. It uses only the Python standard library. All checks passed:

- Two independent channel constructions agreed exactly for 32 rational-probability rows, each normalized exactly.
- The unreduced entropy formula agreed on 100 random orbit laws, with maximum discrepancy 6.66e-16 bits.
- Direct row-divergence checks at ten deletion probabilities had maximum spread 5.27e-15 bits.
- Seven eight-input Blahut–Arimoto runs, starting asymmetrically and making no symmetry assumption, matched the formula to 4.45e-16 bits.
- A raw-channel-divergence criterion independently reproduced the exceptional root found with 90-digit Decimal arithmetic.
- Integer polynomial multiplication, exact rational endpoint signs, finite-difference derivatives, an independent cubic root, and a separate divergence expression audited the load-bearing algebra and numbers.

Floating-point dual checks are numerical audits, not directed interval certificates. The proof is the basis for the theorem. The final verification used about 16.2 MiB peak RSS and 0.08 seconds. Its inherited nice level was 20. The sandbox emitted a warning when nice attempted to change this to 15; the observed level was already more yielding than requested.

The initial guess that no deletion probability permits an optimal Markov marginal failed. Its unique exception is part of the final theorem. No other failure or unresolved proof gap was found. A first-order Markov restriction must not be substituted for the full input simplex, and finite-block mutual information must not be described as an achievable infinite-channel rate without paying for hidden boundaries.

The bounded literature search used the web tool and finished within ten minutes. It found no solution or substantial advance after the supplied status. Primary pages actually opened:

- Dimitris Papailiopoulos, *Binary Deletion Channel Capacity to Within One Hundredth of a Bit*, [arXiv:2609.19412](https://arxiv.org/abs/2609.19412).
- Özgür Soysal, *A New Upper Bound on the Binary Deletion Channel Capacity*, [arXiv:2609.13351](https://arxiv.org/abs/2609.13351).
- Hassan Khodaiemehr, Chen Feng, Tolga M. Duman, *Improved Lower Bounds on the Capacity of the Binary Deletion Channel via a Learning Approach to Run-Length Inputs*, [arXiv:2609.24908](https://arxiv.org/abs/2609.24908).
- Hassan Khodaiemehr, Chen Feng, *Orbit Reduction and Learned Run Distributions for Finite-Blocklength Binary Deletion Channels*, [arXiv:2609.24889v2](https://arxiv.org/html/2609.24889v2), particularly Proposition 1 and Proposition 2(c), which already establish the symmetry reduction used here.

The next worker should examine blocklength four at d_*. The length-three obstruction disappears there, so comparing its unique optimum with the first-order Markov family tests whether this exceptional coincidence survives even one further blocklength. Any claim about the full C(d) still needs an argument uniform in blocklength. Checking older literature for the explicit scalar equation and exceptional parameter would also clarify novelty.

Task: “push this problem forward by one checkable piece,” 14 Nov 2026, approximately 22:00 Asia/Tbilisi (exact prompt timestamp unavailable).
