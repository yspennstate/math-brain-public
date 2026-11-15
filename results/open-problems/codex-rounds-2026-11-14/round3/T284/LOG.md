# T284 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 03:44 +04 (Asia/Tbilisi).

## Orientation and scope

Read the previous REPORT.md, LOG.md, PROOF.md, AUDIT.md, and verify.py in ~/codex_op_1114/briefs/T284. Those files remain read-only. Read startup memory, the brain index, and the compute governor. Governor status warn, mode owner_away_open, CPU saturated: only tiny single-thread checks are planned. The current instruction forbidding writes outside this folder overrides global mesh/checklist/brain write routines; none are run. No git, subagents, or external communications.

All Python runs use `env OMP_NUM_THREADS=1 nice -n 15 python3`, bounded tiny inputs, and no GPU or numerical libraries.

## Bounded literature check (03:44–03:47, under five minutes)

Web queries: `"independent set" "overlap" "2026" algorithm hardness sparse`; `"independent set" "log d" "2025" "2026" algorithms`; `"2411.01836"`.

Actually opened primary sources:

- David Gamarnik, *The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures*, arXiv:2109.14409, https://arxiv.org/abs/2109.14409 .
- Shuangping Li and Tselil Schramm, *Some easy optimization problems have the overlap-gap property*, arXiv:2411.01836v3, https://arxiv.org/abs/2411.01836 . The arXiv page gives last revision 24 June 2025. Its shortest-path example does not settle sparse independent-set search.
- Abhishek Dhawan, Eren C. Kızıldağ, Neeladri Maitra, Cheng Mao, Timothy L. H. Wee, *Half-Optimal Induced Matchings in Random Graphs: Online and Low-Degree Algorithms*, arXiv:2610.40369, https://arxiv.org/abs/2610.40369 . The abstract concerns induced matchings and restricted algorithm classes.
- Shachar Lovett, *Approximating Independent Sets Using Additive Combinatorics*, arXiv:2610.25047, https://arxiv.org/abs/2610.25047 . Its abstract gives a quasipolynomial algorithm with approximation factor N/exp((log N)^(1/3)), not a polynomial algorithm producing a linear independent set in G(n,d/n).

No settlement found in this limited check. No claim of exhaustive literature coverage and no SOLVED_ELSEWHERE.md.

For the inherited analytic input, opened Elchanan Mossel, Krzysztof Oleszkiewicz, Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, https://arxiv.org/pdf/1108.1210 . Corollary 1.11 on PDF page 5 includes negative output exponents and biased product measures; this is exactly the inequality used by the earlier proof.

## Independent re-derivation of the earlier claim

For one refreshed edge, stationarity and E[Y|X]=(1-delta)X+delta p imply E[XY]=p^2+(1-delta)p(1-p), so P(X=1|Y=0)=delta p. Conditional on a fixed trial's full H and solver bits, internal original edges of its chosen k-set are independent Bernoulli(delta d/n). Selection of the first successful trial would invalidate this conditioning; the earlier proof correctly uses a union bound over predetermined trials.

With r=delta/2, the reverse hypercontractive time condition is (1-delta)(1+r)<=1-r. Since f in [0,1], E f^r>=E f>=v. Thus E[(T f)^(-r)]<=v^(-1) and P(T f<u)<=u^r/v. For v=c n^(-s), u=n^(-h), this gives c^(-1)n^(s-hr). Taking h>=2(s+L)/delta yields n^(-L). Independent Poisson-Chernoff optimization at threshold eta n/2 and mean at most eta n/4 gives rate (eta n/4)(2 log 2-1), matching the previous proof. Together with conditional trial independence and the predetermined-trial repair union bound this re-derives the main theorem. It holds.

A fresh exact enumeration, different from the previous bitmask graph enumeration, will check the posterior using a multinomial expansion of the two-coordinate joint law; the previous script will also be rerun from this working directory so its JSON output lands here.

## Choice recorded before extension work

Prove a vanishing-density-loss version of the same amplification lemma for a solver with constant success, with polynomial runtime. Use n-dependent refresh delta_n tending to zero while delta_n log n tends to infinity. Then the negative-moment bad-input bound tends to zero even with a fixed polynomial number of trials. Repair costs O(delta_n n)=o(n). An explicit dyadic-log choice gives loss O(n log log n/log n), failure O((log n)^(-K)) for any fixed K, and n^2 trials. This directly addresses the previous report's question about removing fixed density slack, for the narrower constant-success hypothesis. It does not promise zero loss, polynomially small failure, or an all-algorithm obstruction.

Potential wider form within the same lemma: if success >=1/w_n with known, efficiently computable w_n>=1 and log w_n=o(log n), choose delta_n to dominate log w_n/log n by a diverging margin. The output still loses o(n) with fixed polynomially many trials. Establish only after checking uniformity and finite-bit sampling.

## Earlier verifier rerun

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114/briefs/T284/verify.py` (cwd is this folder).

Output:
```
nice: setpriority: Operation not permitted
status: PASS
exact_bayes_identities: 4096
exact_conditional_binomial_cases: 225
conditional_cases_by_set_size: {'2': 192, '3': 32, '4': 1}
boolean_negative_moment_checks: 3060
randomized_negative_moment_checks: 80
ceiling_and_mean_checks: 12933
kappa_decimal: 0.09657359027997265470861606072908828403775006718012762706034
nice: 20
omp_num_threads: 1
elapsed_seconds: 0.2675
max_rss_bytes_macos: 15417344
```
The inherited priority 20 is lower than requested 15; sandbox refuses raising it. The earlier script wrote verification.json in this folder only. Independent derivation plus rerun support the earlier result.

## Extension refined before proof draft

A logarithmic dyadic schedule removes the need to know the success probability. Use m=ceil(log_2 n), refresh rates delta_j=2^(-j), j=1,...,m, and n^2 trials at each rate. Return the largest valid repaired set. For any one scale, the failure bound is

`v_n^(-1) n^(-delta_j/2) + exp(-n) + n^2 exp[-(log 2-1/2) delta_j d k_n(k_n-1)/n]`.

The exact repair mean is delta_j d k_n(k_n-1)/(2n); deleting at most ceil(twice this mean) vertices permits the displayed rate. For any fixed K>0 choose in the analysis a scale between beta_n and 2 beta_n, where beta_n=2(log(1/v_n)+K log log n)/log n. If log(1/v_n)=o(log n), this scale exists eventually. The bad-input term is at most (log n)^(-K), and loss at most

`ceil[4 d k_n(k_n-1)(log(1/v_n)+K log log n)/(n log n)] = o(n)`.

The scale is used only to prove a guarantee; the algorithm does not compute v_n or K. This establishes the wider subpolynomial-success form within the chosen vanishing-loss amplification piece. No improved guarantee is asserted for arbitrary inverse-polynomial starting success.

## Proof saved

Saved PROOF.md with the full dyadic-schedule theorem. It applies to every polynomial-time computable target k_n with k_n/n->a>0 and starting success v_n=n^(-o(1)). The exact loss is D_{n,K}=ceil[4 d k_n(k_n-1)(log(1/v_n)+K log log n)/(n log n)]. The same algorithm works for every K>0, using n^2 ceil(log_2 n) calls. Each guarantee uses one scale in the analysis, avoiding a union-bound loss across scales. A 10 ceil(log_2 n)-bit Bernoulli implementation contributes at most n^(-5) total variation error over the whole run.

Next: independent refresh-mask enumeration, exhaustive small biased-product moment checks, exact small binomial tails, dyadic-scale and rounding checks including enormous integer n, and an adversarial read of the corollary's constant-representation assumption.

## Extension verifier first run

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify_extension.py`.

The run stopped at the finite scale test `assert beta > 2^(-m)`. The test included n=3 and a small K, whereas the proof assumes n sufficiently large. This is a test-domain error: beta can be below the schedule's smallest rate at these finite sizes. Add an explicit check counting and excluding cases outside this eventual hypothesis, rather than assuming all n in the grid satisfy it. No proof claim uses those excluded finite sizes.

Adversarial read also caught a representation issue in the draft corollary: a computable constant need not be polynomial-time computable. Restrict the overlap-scale corollary to integer d and rational epsilon (so log d is polynomial-time approximable), and explicitly require polynomial-time computability for any wider real-constant formulation. This changes neither the main theorem nor the stated vanishing-loss argument.

## Extension verification passed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify_extension.py`.

Output:
```
nice: setpriority: Operation not permitted
status: PASS
latent_refresh_posterior_checks: 90
count_based_posterior_checks: 396
dyadic_negative_moment_checks: 6120
worst_moment_ratio: 1.0
exact_binomial_tail_checks: 111
scale_and_loss_checks: 369
all_scale_sampler_budget_checks: 8
excluded_small_scale_cases: 4
rounding_checks: 19482
largest_test_n: 2^8192 (symbolic integers only; no n-sized allocation)
gamma_decimal: 0.1931471805599453094172321214581765680755001343602552541206800094933936219696947156058633269964186875
nice: 20
omp_num_threads: 1
elapsed_seconds: 1.5033
max_rss_bytes_macos: 16482304
```

Full data: extension_verification.json. The 90 posterior checks enumerate the elementary variables (original edge, refresh bit, replacement bit) directly; the 396 count checks independently enumerate how many zero original edges were refreshed. These differ from the prior bitmask graph-kernel enumeration. Binomial tails are exact rational sums compared with a high-precision exponential bound. Moment tests numerically check the imported inequality at eight dyadic scales and three biases, not a proof of that inequality. The huge-n checks allocate only small collections of integers with up to 8193 bits, never a graph of that size. Peak measured RSS was about 16.5 MB.

The repair exponent gamma was independently optimized as t log(t/mu)-t+mu at t=lambda, mu=lambda/2, giving lambda(log 2-1/2). A separate rational atanh series checks log 2. Four small-n cases are explicitly outside the scale-existence hypothesis; the theorem's eventual statements do not cover them.

## Adversarial audit saved

Saved AUDIT.md. Rechecked dependence (I uses H only; fixed-trial conditioning; union over predetermined trials), the negative exponent, ceil monotonicity, the exact factor two between repair mean and lambda, the beta-to-dyadic scale selection, all-scale finite-bit sampling, and the fact that B does not need the unknown success bound. Checked the limiting repair exponent a second way by substituting x=log n. The overlap corollary now includes an explicit rational series and tail bound for polynomial-time approximation of log d.

Attempts to strengthen the theorem fail at specific bounds: delta=O(1/log n) only gives a constant bad-input estimate at fixed polynomial runtime; starting success n^(-s), s>0 fixed, keeps beta bounded away from zero; and replacing polylogarithmic failure by n^(-L) likewise keeps beta bounded away from zero. These observations restrict this proof, not all possible amplification methods.

## Final readback

REPORT.md has the required first-line verdict and states the advance, both commands, failed checks and corrections, remaining uncertainty, and a concrete next question. Read back the saved JSON and confirmed all seven deliverables: REPORT.md, PROOF.md, LOG.md, AUDIT.md, verify_extension.py, verification.json, extension_verification.json. The report distinguishes exact rational tail calculations from their numerical exponential comparisons. No further code or theorem changes followed the passing verifier. All writes stayed in this folder; the earlier folder was read only. T284 itself remains unresolved.
