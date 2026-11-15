"""an agent, 13 Nov 2026: settle the 47 BORDERLINE rows of DESERVE.tsv (41 NICHE + 6 READ_STATEMENT).
Rule: a row stays when it is a well-posed, named problem with a literature, even if its reach is narrow (score 3 means
narrow, not wrong). A row is replaced when it has no mathematical statement anyone could prove or refute (an empirical
puzzle, a discussion question, a slogan), or when its question is explained or settled. Replacements come from
DL_CANDIDATES_1113.tsv after an arXiv abstract check, as N02-N06 did on 11 Nov.
Writes SETTLE_BORDERLINE_1113.tsv and DL_CANDIDATES_1113.tsv."""
import csv

KEEP = {
    "T059": "Robbins' problem is well posed (value of the full-information expected-rank problem) with a steady literature",
    "T062": "Sylvester's problem for d>=3 is a precise extremal question in geometric probability",
    "T073": "noisy majority vote on Z^2: a precise phase-transition question for an interacting particle system",
    "T096": "SK Glauber mixing: the open core (rapid mixing up to beta=1, not only beta<1/4 or via other chains) is precise",
    "T101": "Lorentz mirror model: a precise percolation-type question on Grimmett's list",
    "T104": "Oliveira's conjecture: precise, partly proved; we are proving cases of Alon's Conj 1.5 under it (STRAT14-20)",
    "T165": "SRBM positive recurrence in dimension >=4: a precise characterisation problem",
    "T169": "Neuhauser-Pacala coexistence: a precise question in the regime the known proofs leave",
    "T173": "slotted ALOHA stability for 4+ users: a precise classical problem",
    "T177": "Derrida-Retaux critical regime: precise; a residual statement remains after Chen-Dagard-Derrida-Hu-Lifshits-Shi",
    "T185": "alpha-fair bandwidth sharing stability with general file sizes: a precise stability question",
    "T186": "circumference of G(n,c/n) for every c>1: a precise scaling-limit question",
    "T194": "Drossel-Schwabl fire lanes: a precise question of van den Berg and Brouwer",
    "T200": "3-d Brownian intersection exponents: well posed (exact values), even if no closed form is expected; keep as stated",
    "T215": "copolymer critical slope at a selective interface: a precise universality question",
    "T217": "monotonicity of once-excited walk speed in low dimension: precise",
    "T218": "VRRW finite-range localization a.s.: precise",
    "T220": "marginal disordered pinning free energy: a precise asymptotic question",
    "T222": "Steele's TSP variance limit: precise (see E0030 memory, open 13 Nov)",
    "T258": "basins of symmetric spurious minima (Arjevani-Field): a precise landscape question",
    "T337": "sample complexity of attention for sparse token retrieval: precise for a stated model",
    "T340": "batch normalization orthogonalizes representations: a precise rate question (Daneshmand et al.)",
    "T359": "scaling laws for associative memories: precise in the linear associative-memory model",
    "T381": "robust undetectable watermarks: a precise cryptographic question about language-model outputs",
    "T400": "neural contextual bandits beyond the lazy regime: a precise regret question",
    "T402": "kernel Stein discrepancy controlling convergence: a precise question with a narrow open remainder",
    "NT18": "Erdos-Straus: precise and famous",
    "DG14": "Chern's isoparametric conjecture: precise remaining cases",
    "AN05": "Polya-Szego for polygons with n>=5 sides: precise",
    "AN10": "Krzyz conjecture: precise; coefficients 6 and 7 recently, general case open",
    "AN12": "separable quotient problem for Banach spaces: precise and long-standing",
    "GE08": "Erdos-Ulam: precise; follows from Bombieri-Lang (NT21) but is open unconditionally",
}
REPLACE = {
    "T313": "Do GANs learn the distribution: a discussion question; no statement to prove",
    "T318": "cold posterior effect: an empirical puzzle with no agreed mathematical statement",
    "T320": "depth of normalizing flows: a narrow question with no literature found by two queries; weakest DL row",
    "T321": "Langevin mixing for nonconvex learning objectives: too broad as titled; no single target",
    "T339": "approximation rates of distributions by generative networks: broad as titled; no sharp target",
    "T358": "intrinsic robustness of natural data: no mathematical statement",
    "T399": "next-token prediction on planning tasks: no agreed mathematical statement",
    "T401": "deep ensembles versus Bayesian model averaging: a discussion question",
    "T403": "information bottleneck: a disputed empirical claim; mutual information is infinite for deterministic nets",
    "T404": "simplicity bias of the parameter-function map: no agreed precise conjecture",
    "T414": "IWAE tighter-bound paradox: explained by Rainforth et al. (2018)",
    "T415": "reward-model overoptimization scaling laws: an empirical law",
    "T419": "why LoRA works: not a stated conjecture",
    "T420": "deep learning as renormalization group flow: not a well-posed target",
    "T422": "critical batch size and gradient noise scale: an empirical rule",
}

CANDS = [
    ("C01", "Self-stabilization at the edge of stability",
     "Prove that gradient descent with step size eta on a two-layer network (beyond the quadratic-model setting) drives the top Hessian eigenvalue to 2/eta and keeps it there while the loss decreases non-monotonically.",
     "Cohen et al. 2021; Damian, Nichani, Lee 2023 (self-stabilization under assumptions)"),
    ("C02", "Clustering of tokens in self-attention dynamics",
     "For the continuous-time self-attention dynamics on the sphere with V = identity (Geshkovski, Letrouit, Polyanskiy, Rigollet), prove that for every inverse temperature beta and dimension d >= 3 and almost every initial configuration the tokens converge to a single cluster.",
     "Geshkovski-Letrouit-Polyanskiy-Rigollet, A mathematical perspective on transformers, open problems"),
    ("C03", "The leap complexity conjecture",
     "Prove that online SGD on a two-layer network learns a sparse function on the hypercube with Theta(d^{max(Leap-1,1)}) samples, Leap being the leap complexity of its Fourier support, for jointly trained layers.",
     "Abbe, Boix-Adsera, Misiakiewicz 2023 (proved for layerwise training)"),
    ("C04", "Depth separation between depth three and depth four",
     "Is there a function on [0,1]^d computable by polynomial-size depth-4 ReLU networks that polynomial-size depth-3 networks cannot approximate in L2 under a natural distribution?",
     "Eldan-Shamir 2016 (2 vs 3); Vardi-Shamir 2020 (natural-proof barrier)"),
    ("C05", "Provable grokking on modular addition",
     "Prove that gradient descent with weight decay on a two-layer network trained on a fraction of modular addition first interpolates and only after a time growing with 1/lambda generalizes, with the learned Fourier features.",
     "Nanda et al. 2023; Mohamadi et al. 2024; Morwani et al. 2024"),
    ("C06", "Global convergence of gradient descent for deep ReLU networks at moderate width",
     "Prove that gradient descent from random initialization reaches zero training loss for depth >= 3 ReLU networks whose width is polynomial in n but below the neural-tangent-kernel regime.",
     "Allen-Zhu-Li-Song; Du et al.; Nguyen-Mondelli; Bombari-Amani-Mondelli (minimum width)"),
    ("C07", "Benign overfitting of gradient-trained two-layer ReLU networks",
     "Characterise the data distributions for which GD-trained two-layer ReLU networks interpolate noisy labels and still have test error tending to the Bayes error, beyond near-orthogonal high-dimensional data.",
     "Frei, Chatterji, Bartlett 2022; Kou et al. 2023; Kornowski-Yehudai-Shamir 2023 (tempered)"),
    ("C08", "Convergence of Adam with problem-independent hyperparameters",
     "Does Adam with fixed beta1 < sqrt(beta2) < 1 independent of the problem converge to stationary points on smooth nonconvex objectives, or is there a counterexample?",
     "Reddi et al. 2018; Zhang et al. 2022 (problem-dependent beta2); Wang et al. 2023"),
    ("C09", "The catapult phase for wide networks",
     "Prove the catapult dynamics of Lewkowycz et al. (loss spike then convergence to a flatter region for step sizes between 2/lambda0 and 4/lambda0) for two-layer networks of finite width with non-linear activations.",
     "Lewkowycz et al. 2020; Zhu et al. 2023 (quadratic models)"),
    ("C10", "Optimal step count for score-based diffusion",
     "What is the optimal dimension dependence of the number of discretisation steps for diffusion models to reach KL error eps with L2-accurate scores and finite second moment: linear in d (Benton et al.), or sqrt(d), or smaller?",
     "Benton, De Bortoli, Doucet, Deligiannidis 2024; Chen et al. 2023; Li et al. 2024"),
    ("C11", "Neural collapse in deep networks trained on data",
     "Prove that gradient descent on cross-entropy for a deep network (not the unconstrained-features model) on separable data reaches neural collapse of the last-layer features.",
     "Papyan-Han-Donoho 2020; Mixon et al.; Sukenik-Mondelli-Lampert 2023 (deep UFM)"),
    ("C12", "Minimal width for uniform universal approximation by ReLU networks",
     "Determine the exact minimal width of deep ReLU networks that are dense in C(K, R^{d_y}) for compact K in R^{d_x}.",
     "Park-Yun-Lee-Shin 2021 (L^p case); Cai 2023; Kim-Min-Park 2024"),
    ("C13", "In-context learning of nonlinear functions by trained transformers",
     "For a one-layer softmax transformer trained by gradient flow on in-context regression with a nonlinear function class (e.g. single-index), characterise the in-context predictor it converges to.",
     "Zhang-Frei-Bartlett 2023 (linear); Oko et al. 2024; Kim-Suzuki 2024"),
    ("C14", "Implicit bias of gradient descent in deep matrix factorization",
     "Give an explicit characterisation of the limit of gradient flow from small initialization on depth-L matrix factorization for matrix completion, now that it is not nuclear-norm minimisation.",
     "Gunasekar et al. 2017; Razin-Cohen 2020; Li-Luo-Lyu 2021 (greedy low-rank learning)"),
    ("C15", "Sample complexity of learning parities with transformers by gradient descent",
     "Prove a lower bound on the samples or steps gradient descent needs for a constant-depth transformer to learn k-sparse parities without intermediate tokens, matching the known upper bounds.",
     "Edelman et al. 2022; Kim-Suzuki 2025; related to N03 (CoT S_5)"),
    ("C16", "Mean-field limit of deep residual networks",
     "Prove a mean-field limit (law of large numbers in width and depth) for the training dynamics of deep residual networks and the global convergence of the limit.",
     "Lu-Ma-Lu-Lu-Ying 2020; Ding-Chen-Li-Wright 2022; Barboni-Peyre-Vialard 2024"),
    ("C17", "Sharpness of SGD minima under label noise",
     "Prove that SGD with label noise on an overparametrised network converges to a minimiser of the Hessian trace on the zero-loss manifold, with a rate, beyond the small-learning-rate limit.",
     "Blanc et al. 2020; Damian-Ma-Lee 2021; Li-Wang-Arora 2022"),
    ("C18", "Width-depth trade-off for exact ReLU representation",
     "Restating N01: determine the minimal width of a depth-k ReLU network that exactly represents every continuous piecewise-linear function on R^d with a given number of pieces.",
     "Hertrich-Basu-Di Summa-Skutella 2021; Haase-Hertrich-Loho 2023 (depth lower bounds)"),
]

with open("DESERVE.tsv", encoding="utf-8") as fh:
    rows = list(csv.reader(fh, delimiter="\t"))
title = {r[0]: r[2] for r in rows[1:]}
border = [r[0] for r in rows[1:] if r[4].startswith("BORDERLINE")]
missing = [i for i in border if i not in KEEP and i not in REPLACE]
extra = [i for i in list(KEEP) + list(REPLACE) if i not in border]
assert not missing and not extra, (missing, extra)
with open("SETTLE_BORDERLINE_1113.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["id", "title", "decision", "reason"])
    for i in border:
        w.writerow([i, title[i], "KEEP" if i in KEEP else "REPLACE", KEEP.get(i) or REPLACE[i]])
with open("DL_CANDIDATES_1113.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["key", "title", "statement", "anchors_from_memory", "litcheck"])
    for c in CANDS:
        w.writerow(list(c) + ["PENDING: arXiv abstracts not yet read; anchors are from memory"])
print("border", len(border), "keep", len(KEEP), "replace", len(REPLACE), "candidates", len(CANDS))
