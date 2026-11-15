import json, csv
rows = [json.loads(l) for l in open("../top200_probability_2026_10_14/list.jsonl", encoding="utf-8") if l.strip()]
five = "T323 T325 T341 T347 T354 T367 T370 T378 T382".split()
replace = {"T352": "reported answered (arXiv 2401.10371 v7 Thm 3.3, a paper titled Langevin Unlearning): read the theorem, then replace",
 "T363": "duplicate of T269 (which margin gradient descent finds in homogeneous networks)"}
check = {"T327": "induction heads on Markov chains: Nichani-Damian-Lee (2024) prove a version; check the open core",
 "T329": "memorization with bounded bit complexity: Vardi-Yehudai-Shamir give optimal bounds up to logs; check the open core",
 "T331": "zero-one laws for GNNs: Adam-Day et al. (2023) prove one; check what remains",
 "T335": "curse of parametric complexity: Lanthaler-Stuart prove the curse; check the row asks something still open",
 "T342": "random features vs networks for one neuron: Yehudai-Shamir prove the separation; check the open core",
 "T344": "adversarial examples in random networks: Bubeck et al., Bartlett et al., Montanari-Wu cover wide classes of widths; check the open core",
 "T365": "possible overlap with T277 (depth separation for gradient-trained networks on hierarchical targets): read both",
 "T367": "possible overlap with T241 (global convergence of feature-learning infinite-width deep limits): read both",
 "T373": "possible overlap with T268 (depth-independent sample complexity under spectral-norm constraints): read both",
 "T379": "Kalai-Vempala prove calibrated models must hallucinate; check the row asks a quantitative question still open",
 "T382": "Weisz-Amortila-Szepesvari (2021) give an exponential lower bound for linearly realizable Q*; check which setting the row leaves open",
 "T391": "intrinsic-dimension adaptation of diffusion models: several 2024 proofs (Potaptchik et al., Huang-Wei-Chen); check the open core",
 "T407": "CNN vs fully connected sample complexity: Li-Zhang-Arora (2021) prove a separation; check the open core",
 "T408": "gain from invariance: Tahmasebi-Jegelka (2023) give the exact gain for kernels; check the open core",
 "T409": "Testing the manifold hypothesis: Fefferman-Mitter-Narayanan (2016) is a theorem with this title; check the row asks the computational question",
 "T411": "posterior sampling with diffusion priors: Gupta-Jalal-Parulekar-Price-Xun (2024) prove hardness; check the open core",
 "T418": "GP bandit regret: Vakili's COLT open problem; partly answered since (Whitehouse-Ramdas-Wu, Lattimore, Salgia et al.); check the stated kernel class"}
border = {"T337": "sample complexity of attention for sparse token retrieval: narrow",
 "T339": "approximation rates of distributions by generative networks: broad as titled, small literature on a sharp form",
 "T340": "batch normalization orthogonalizes representations: narrow",
 "T358": "intrinsic robustness of natural data distributions: no agreed mathematical statement",
 "T359": "scaling laws for associative memories: narrow",
 "T381": "robust undetectable watermarks: a cryptography problem more than deep-learning theory",
 "T399": "next-token prediction on planning tasks: no agreed mathematical statement in the title",
 "T400": "neural contextual bandits beyond the lazy regime: narrow",
 "T401": "deep ensembles vs Bayesian model averaging: a discussion question; check for a precise target",
 "T402": "kernel Stein discrepancy and convergence: Gorham-Mackey and follow-ups settle much; narrow remainder",
 "T403": "information bottleneck: a disputed empirical claim (Saxe et al.); check for a precise target",
 "T404": "simplicity bias of the parameter-function map: no agreed precise conjecture",
 "T414": "importance-weighted autoencoder tighter-bound paradox: explained by Rainforth et al.; narrow",
 "T415": "scaling laws for reward-model overoptimization: an empirical law, no mathematical statement",
 "T419": "why LoRA works: not a stated conjecture; check for a precise target",
 "T420": "deep learning as a renormalization group flow: not a well-posed target as titled",
 "T422": "critical batch size and gradient noise scale: an empirical rule; check for a precise target"}
theirs = {r["id"]: (r["verdict"], r["reason"]) for r in csv.DictReader(open("../top200_review_2026_11_10/VERDICTS.tsv", encoding="utf-8"), delimiter="\t")}
out = open("DESERVE.tsv", "a", encoding="utf-8", newline="\n"); n = {}
for r in rows[322:422]:
    i = r["problem_id"]; tv, tr = theirs.get(i, ("?", ""))
    if i in replace: sc, v, why = 0, "REPLACE", replace[i]
    elif tv == "RESTATE": sc, v, why = (5 if i in five else 4), "DESERVES_RESTATE", "agent: " + tr
    elif i in check: sc, v, why = (5 if i in five else 4), "CHECK_STATEMENT", check[i]
    elif i in border: sc, v, why = 3, "BORDERLINE_NICHE", border[i]
    else: sc, v, why = (5 if i in five else 4), "DESERVES", "recognised problem of deep-learning theory"
    n[v] = n.get(v, 0) + 1
    out.write("\t".join([i, r["list"], r["title"], str(sc), v, why, "2026-11-11 title read, an agent; agent verdict: " + tv]) + "\n")
out.close(); print(n)
