VERDICT: PARTIAL explicit degree-three critical tree with nonconvergent radius-conditioned laws

An explicit nontransitive tree T of maximum degree three has been constructed with p_c(T)=1/2 and no infinite open cluster at criticality. Nevertheless, conditioning on connection from its root to graph-distance spheres fails to converge on one fixed edge event. At radii N_k+1, where N_k=2^(k^2+10), that edge's conditional opening probability tends to 1/2 along odd k and to 1 along even k. The complete proof is in PROOF.md.

This is a counterexample to an extinction-only general argument, not a counterexample on Z^3 or a proof of T160. The tree lacks transitivity and fails uniqueness of the infinite cluster above criticality. The result supplies an explicit obstruction that a proposed general construction must exclude. No claim of literature novelty is made.

The mechanism is alternating survival probabilities in two branches. At selected depths their suppressed-level counts differ by k. Independently derived bounds give weaker-branch/stronger-branch survival ratio at most 16*2^(−k). The actual critical parameter and critical extinction at every vertex are proved, rather than assumed.

Verification command, run from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
```

The run exited 0. It passed 378 exact forward-distribution/backward-recursion comparisons at p=1/3,1/2,2/3; 378 second-moment checks; 126 reciprocal-identity checks; and 16 fixed-edge formulas by exhaustive enumeration of 33,856 configurations. It also checked 32 stage certificates. The data are in stage_certificates.csv. These are bounds derived from the proof, not simulated probabilities. Exact output is in audit_output.txt and copied into LOG.md. Runtime was 0.270 seconds, peak RSS 15,663,104 bytes, one thread. The inherited nice priority was 20; the redundant `nice -n 15` emitted a priority warning and the process retained priority 20.

The proof was checked a second way: its lower survival bound follows both from a second moment and a reciprocal recursion; its upper bound follows both from a plateau union bound and the reciprocal recursion. The root-edge formula was checked against full configuration enumeration, including the case where the unsuccessful branch edge remains open. The graph-distance radius offset and the first stage were checked explicitly.

The literature check ended within four minutes of session start. No verified new solution of the three-dimensional Bernoulli IIC limit was located. Opened sources include:

- Deepan Basu and Artem Sapozhnikov, *Kesten’s incipient infinite cluster and quasi-multiplicativity of crossing probabilities*, [arXiv:1603.06884](https://arxiv.org/abs/1603.06884). Their theorem requires uniqueness and quasi-multiplicativity; the latter is not established here for Z^3.
- Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe, *Robust construction of the incipient infinite cluster in high dimensional critical percolation*, [arXiv:2502.10882](https://arxiv.org/abs/2502.10882). Its input is high-dimensional two-point asymptotics; it does not establish the Z^3 statement.
- Malo Hillairet, *Short, Quantitative Construction of the IIC in Planar Percolation*, [arXiv:2509.18852](https://arxiv.org/abs/2509.18852), version 3 dated 28 May 2026. This is a planar construction.
- Raphaël Cerf, *θ(p_c, Z^d)=0?*, [arXiv:2608.23661](https://arxiv.org/abs/2608.23661). Its abstract concerns Bernoulli site percolation and a finite-cluster-tail alternative, not the bond IIC limit.

Search results also included secondary claims about T001. Those were not verified or used, and the present result does not depend on the truth of critical extinction on Z^3. No SOLVED_ELSEWHERE.md was created because no verified solution or substantial new advance of T160 itself was found. This was a short search, not an exhaustive literature review.

What failed or remains uncertain: there is no lattice ratio limit, improved Z^3 bound, or proof of the IIC limit here. The tree obstruction does not apply to the full Basu–Sapozhnikov assumptions. Its novelty was not established.

Next worker: use this example as a test for any proposed compactness/uniqueness proof. Identify a quantitative consequence of transitivity and lattice geometry that prevents alternating dominance of long connections. Establishing such a control on Z^3, rather than only critical extinction or existence of subsequential limits, is the unresolved step. Do not spend time simulating the exponentially large tree; its obstruction is already proved analytically.

Task: “push this problem forward by one checkable piece” — received 14 Nov 2026, approximately 22:02 Asia/Tbilisi.
