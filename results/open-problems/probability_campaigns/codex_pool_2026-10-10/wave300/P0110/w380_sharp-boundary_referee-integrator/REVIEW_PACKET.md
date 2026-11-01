# P0110 sharp-boundary referee packet (w380, 2026-10-10)

Target source: Auffinger-Damron-Hanson, *50 years of first passage percolation*, Question 22. The Northwestern PDF prints the relation as (4.13); the arXiv v2 cited by w378 prints it as (4.19). Both ask for a distribution for which $\chi=2\xi-1$ is established. Chatterjee's 2013 theorem assumes existence of strong exponents; it does not itself furnish such a law. Current openness remains UNKNOWN after a bounded search. This packet makes no claim to solve P0110.

## Verdicts

| Claim | Verdict | Reproduction and scope |
| --- | --- | --- |
| w378 L1, forced axial path | **KEEP** | Every nonaxial path to $ne_1$ has at least $n+2$ edges, hence costs at least $(n+2)a>nb$. The axial path costs at most $nb$. Under iid weights it is an $n$-term independent sum, with variance $n\sigma^2$ and deviation zero. This is a finite-scale statement. |
| w378 L1, sharp support threshold | **KEEP** | At $n(b-a)=2a$, setting all $n$ axial edges to $b$ and all $n+2$ edges of the disjoint upper detour to $a$ ties the two paths; above threshold the detour wins. No other path can have fewer than $n+2$ edges. The sharpness is uniform over assignments, not a universal assertion for every iid sample. |
| w378 L2, law-uniform contraction | **KEEP** | For fixed $M,n$, choose $\epsilon<2/(Mn)$ and iid Uniform$[1,1+\epsilon]$. Both passage times are straight-path sums, so $\operatorname{Var}T_{Mn}/(M\operatorname{Var}T_n)=1$. The law depends on $n$, so the conclusion excludes only a **law-independent** onset $N$. |
| w378 L3, fixed Uniform-law cutoff | **KEEP** | For a fixed $\epsilon>0$, $n\epsilon<2$ gives strict support comparison; at equality the axial sum is strictly below its endpoint maximum almost surely, while every detour costs at least $n+2$. Above the cutoff, require axis edges within $\delta=(n\epsilon-2)/(4n+4)$ of the upper endpoint and detour edges within $\delta$ of the lower endpoint. The detour saves at least $(n\epsilon-2)/2$ on an event of probability $(\delta/\epsilon)^{2n+2}>0$. Thus almost-sure unique axial optimality holds iff $n\epsilon\le2$. |
| w379 C1, monotone transfer | **KEEP** | For any nonconstant finite nonnegative law choose $0<l<h$ with both tail probabilities positive, then $n(h-l)>2l$. The disjoint $n$-edge axial path and $(n+2)$-edge upper detour have the heavy/light event with probability $p_h^n p_l^{n+2}>0$. On it, unrestricted cost is strictly below the unique coordinatewise nondecreasing path cost. |
| w379 C2, linear axial gap | **KEEP** | Set block spacing $L=n+2$. The heavy/light events depend on disjoint edge sets and are iid Bernoulli($q$). Replacing successful blocks in the axial path saves at least $\delta=n(h-l)-2l$ each. Since $D_N$ is exactly the axial sum, $D_N-T_N\ge\delta\sum_{k<\lfloor N/L\rfloor}1_{E_k}$. The strong law yields $\liminf(D_N-T_N)/N\ge\delta q/L>0$ a.s. The final bound against $E\tau$ additionally needs $E\tau<\infty$. |

Independent exact check: `python -X utf8 reproduce.py` is bounded by `COMPUTE_GATE.json` and returns 256 configurations, one heavy/light configuration, $q=1/256$, $\delta q/L=1/1280$ for weights $1,2$ and $n=3$; the Uniform$[1,5/4]$ variance ratio at $n=2,M=2$ is exactly 1. For the same Uniform law, the cutoff is $n=8$; at $n=9$ the explicit detour event has probability $40^{-20}$ and saves at least $1/8$. Full output is in `REPRODUCTION.json`. The combinatorial proof, not this finite check, supports the infinite-lattice claims.

## Load-bearing gap

All kept statements concern a finite crossover or a raw monotone axial comparison. None establishes either exponent for one fixed iid law. The next proof step is to select one admissible fixed law and one precise pair of exponent definitions, then prove existence and compatible estimates in those definitions. A law-dependent crossover scale and a centered or interior-direction transfer remain open under these counterexamples.

Independent reviewer: w380. These are mathematical checks of the cited peer packets; separate-account and served-model verification belong to the coordinator before ingestion. No new theorem is authored in this packet.

Reviewed source hashes (SHA-256): w378 `BOUNDARY_LEMMA.md` A4B07B8A29C7F8F38158D082D9393332420F1746D46F9CC30EFB3EA4CFD44C5B; w379 `INDEPENDENT.md` 3A80BEC73DC774BE7EC4BC8668E0E284699C108E3AD51937A5A1E5AE7F83930A. A changed source needs a fresh check; the hashes are provenance receipts, not mathematical proof.
