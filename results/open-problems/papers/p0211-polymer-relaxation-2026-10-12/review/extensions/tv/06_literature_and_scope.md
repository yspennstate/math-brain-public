# Cutoff literature and the precise scope of the proved extension

## Result now proved in the accompanying TeX note

For the count chain with upward rate `b(n-k)/n` and downward rate `k(k-1)/n`, at fixed `b>0`:

- Worst-case count total-variation cutoff is at `sqrt(n) log(n)/(8 sqrt(b))`, with an `O_b(sqrt(n))` window.
- Each count endpoint separately has this cutoff and window.
- Worst-case count separation cutoff is at `sqrt(n) log(n)/(4 sqrt(b))`, with an `O_b(sqrt(n))` window.
- For a reversible polymer chain that strongly lumps to this count chain, singleton endpoint fibers give exact equality of endpoint densities after conditioning on the count. Consequently, endpoint total variation and endpoint separation equal their count-chain counterparts at every time.
- This proves polymer endpoint cutoff and worst-case polymer lower bounds. It does **not** prove arbitrary-start polymer mixing upper bounds or cutoff.

The proof is an application of established birth–death cutoff theory. The model-specific work is the precise hitting-time asymptotic and variance control. It should not be presented as a new general method for cutoff.

## Primary theorem actually used

Guan-Yu Chen and Laurent Saloff-Coste, **Computing cutoff times of birth and death chains**, *Electronic Journal of Probability* **20** (2015), no. 76, 1–47. DOI: [10.1214/EJP.v20-4077](https://doi.org/10.1214/EJP.v20-4077).

Primary full text checked: [arXiv:1502.00361 PDF](https://arxiv.org/pdf/1502.00361), printed page 5, Theorem 1.4(1), and printed page 4, Theorem 1.3(1). [Journal record](https://projecteuclid.org/journals/electronic-journal-of-probability/volume-20/issue-none/Computing-cutoff-times-of-birth-and-death-chains/10.1214/EJP.v20-4077.full).

Theorem 1.4 uses the maximum of the two endpoint-to-central-state hitting means as the TV cutoff location and the maximum standard deviation as a valid window. The central state must have stationary mass bounded below on both sides. Theorem 1.3 uses the sum of endpoint means and variances for endpoint separation. Remark 1.2 identifies boundary starting states as maximizers of continuous-time birth–death separation. These statements apply to our unbounded-rate generators through uniformization and exact time rescaling.

## Related density-dependent-process theory

A. D. Barbour, Graham Brightwell, and Malwina Luczak, **Convergence to equilibrium for density dependent Markov jump processes**, *Electronic Journal of Probability* **31** (2026), paper 104. DOI: [10.1214/26-EJP1548](https://doi.org/10.1214/26-EJP1548).

Primary full text checked: [arXiv:2505.12926v4](https://arxiv.org/pdf/2505.12926), Assumptions 1–3 (printed pages 4–5), Theorem 1.2 (printed page 6). [Journal record](https://projecteuclid.org/journals/electronic-journal-of-probability/volume-31/issue-none/Convergence-to-equilibrium-for-density-dependent-Markov-jump-processes/10.1214/26-EJP1548.full).

Their theorem gives constant-window cutoff near the time when a stable deterministic flow enters the fluctuation scale. Its stated hypotheses use rates `N r_J(X/N)` with functions `r_J` independent of `N`, and starting scaled states in a fixed compact subset of the attraction basin away from the fixed point.

**Our applicability calculation (inference, not a statement of their theorem).** Put `N=sqrt(bn)`, `x=k/N`, and speed physical time up by `N/b`. Our rescaled jump rates become

```
birth: N [1 - b x/N],
death: N [x^2 - x/N].
```

Their limiting deterministic flow is `x'=1-x^2`, with fixed point `1` and linear decay rate `2`. Its fluctuation-scale arrival time is `(1/4) log N + O_b(1)`. Returning to physical time gives `sqrt(n) log(n)/(8 sqrt(b)) + O_b(sqrt(n))`, in agreement with the rigorous passage proof.

The new theorem is **not a literal direct application**: our rate functions retain `N`-dependent corrections; moreover the all-monomer start has scaled density `n/N=N/b`, which escapes every fixed compact set. A uniform perturbation argument and a separate entrance estimate would be required. The direct birth–death proof supplied here resolves both endpoints without relying on these unverified extensions of the general theorem.

A. D. Barbour, Graham Brightwell, and Malwina Luczak, **Long-term concentration of measure and cut-off**, *Stochastic Processes and their Applications* **152** (2022), 378–423. DOI: [10.1016/j.spa.2022.05.004](https://doi.org/10.1016/j.spa.2022.05.004). Primary full text: [arXiv:1902.00822v2](https://arxiv.org/pdf/1902.00822), with [published open-access text](https://eprints.lse.ac.uk/115196/1/Brightwell_long_term_concentration_published.pdf).

This work supplies broader concentration-and-coupling methods for cutoff, including continuous-time processes and initial-state-dependent formulations. It is relevant context, but no unverified specialization of its concentration hypotheses is needed in the accompanying proof.

## What remains genuinely open in this extension

1. A matching arbitrary-start **polymer** TV upper bound. Count projection and endpoint identities alone do not give it.
2. A limiting TV profile or proof that the order `sqrt(n)` is the smallest possible TV window. The present theorem supplies an upper bound on window order.
3. Uniform cutoff asymptotics when `b=b_n` varies. All constants in the present proof may depend on fixed `b`; varying-parameter regimes need further estimates.

No unresolved estimate is left in the fixed-`b` count cutoff or the two polymer endpoint cutoff arguments.
