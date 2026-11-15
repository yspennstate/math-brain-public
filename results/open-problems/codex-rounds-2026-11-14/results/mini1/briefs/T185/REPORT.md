VERDICT: PARTIAL sharp linear-workload certificate and finite-mean stability when sum_i rho_i/b_i < 1

For route `i`, let `b_i` be its rate when it is the only route present, equal to the smallest capacity on its path. Wrote a complete proof in `PROOF.md` of the following statements for independent Poisson arrivals and arbitrary strictly positive finite-mean file sizes:

- A positive linear residual-workload function has uniform strictly negative generator drift outside a workload threshold if and only if `beta=sum_i rho_i/b_i<1`.
- The optimal normalized certificate is `Y=sum_i W_i/b_i`, with negative-drift margin `1-beta`.
- In this region the full residual-state process is positive Harris recurrent, with `E_x tau_empty <= Y(x)/(1-beta)`. Its mean empty-to-empty regenerative cycle is at most `1/[nu(1-beta)]`, where `nu` is the total arrival rate. The invariant empty probability is at least `1-beta`.

The argument uses only feasibility and Pareto efficiency, and therefore applies to every weighted alpha-fair policy with positive weights and `alpha>0`. No smoothness or second moment is needed. This elementary sufficient region is not asserted to be new.

The obstruction is exact. In a two-link unit-capacity network with a through route and one local route per link, route loads `(1/5,1/2,1/2)` give link loads `(7/10,7/10)` but `beta=6/5`. Every positive linear residual-workload function has positive generator drift at some arbitrarily large states. This excludes that proof method; it does not show instability.

The literature check finished in about three minutes. No later unrestricted solution was found. The supplied status omits conditional stochastic recurrence through Nam H. Lee's 2008 dissertation, explicitly noted on p. 1863 of Yingjia Fu and Ruth J. Williams's [2022 paper](https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf). This is not a new removal of the distributional restrictions. Maria Vlasiou, Jiheng Zhang and Bert Zwart's [2026 paper](https://link.springer.com/article/10.1007/s11134-026-09978-1), [arXiv:1411.4841](https://arxiv.org/abs/1411.4841), treats phase-type files and heavy traffic. Full references and search limitations are recorded in `LOG.md`. The search does not certify that no other paper exists.

Reproduce the finite checks with:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_certificate.py
```

Output: all exact checks passed; both link loads `7/10`, scalar load `6/5`, 512 weight vectors checked, and the minimum service formula verified by rational vertex enumeration over 7 and 15 active supports. Full output/data: `certificate_checks.json`; command and output: `LOG.md`. The run finished in under one second. The sandbox rejected setting nice priority (`setpriority: Operation not permitted`), although the command ran; no heavy computation was attempted.

`AUDIT.md` independently re-derives the emptying-time bound by a scalar busy-period branching argument and checks the service bound through link utilizations. It also records the bounded-support, small-residual, heavy-tail, boundary-load, and regeneration cases.

What failed: a fixed positive linear residual-workload drift cannot use the full subcritical region, even in the small two-link example. What remains unproved: T185 outside `beta<1`, renewal-arrival extensions, and any claim of novelty for the certificate. No counterexample to stochastic stability was found or claimed.

Next worker: use the explicit two-link example to test a nonlinear residual-profile Lyapunov function or drift over a state-dependent interval. Such an argument must overcome the positive instantaneous linear drift at states containing files on a single route. For a fluid-to-stochastic approach, first compare Lee's precise hypotheses with the intended file-size class; do not assume the general bridge theorem already applies.

Task: “push this problem forward by one checkable piece,” received 14 November 2026, approximately 22:06 Asia/Tbilisi; exact receipt time unavailable.
