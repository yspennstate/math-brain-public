# -*- coding: utf-8 -*-
"""mutate_md.py - one-line faults for literature proofs outside probability. Every operator changes exactly ONE
step at exactly ONE place and records what it did; the bank builder picks operators per proof.

Started from the probability campaign's mutate.py (2026-09-06; that file is never edited
from here) and extended for analysis/PDE, algebra, number theory, combinatorics, geometry, topology, logic and
learning theory: domain vocabularies for the word operators, a wrong-local-reference operator, a limit-order
operator, an unjustified-interchange operator, the restates-the-claim guard, and a difficulty estimate.

THE TAXONOMY (the nine classes of the design plus two named extras), one per operator:
    sign_flip                     sign_flip
    inequality_direction          ineq_flip, ineq_to_eq, word_flip (direction words)
    quantifier_swap               quantifier_swap (math), quant_word (for all / for some)
    dropped_hypothesis            hypothesis_drop, hypothesis_swap (weakened or altered)
    wrong_constant_or_exponent    const_change, limit_target
    off_by_one_index              index_shift, sum_bound_shift
    wrong_lemma_cited             theorem_swap (named results), ref_shift (a local equation or result number)
    limit_order                   limit_order (two limit-type operators swapped)
    unjustified_interchange       interchange (limit/expectation/supremum moved across an integral or sum)
    extremum_swap                 limop_swap (sup/inf, max/min, limsup/liminf)
    set_operator_swap             setop_swap

Tier A = a reader who checks the line against its neighbours can see the symbol is wrong; tier B = the line reads
naturally and the fault is semantic. Tiers are priors on validity; the hand-read sample measures the rate.

    python mutate_md.py --demo proofs.jsonl --n 8 --seed 1
"""
import argparse
import hashlib
import io
import json
import random
import re

# ----------------------------------------------------------------------------- math-mode helpers
MATH_SPAN = re.compile(
    r"\\begin\{(?:equation|align|gather|multline|eqnarray|alignat|flalign)\*?\}.*?\\end\{(?:equation|align|gather|multline|eqnarray|alignat|flalign)\*?\}"
    r"|\\\[.*?\\\]|\$\$.*?\$\$|\\\(.*?\\\)|\$(?:[^$\\]|\\.)+\$", re.S)
PROTECTED = re.compile(r"\[citation\]|\(ref [^)]*\)|\(eq \d+\)")


def math_spans(step):
    return [(m.start(), m.end()) for m in MATH_SPAN.finditer(step)]


def in_math(step, pos):
    return any(a <= pos < b for a, b in math_spans(step))


def in_protected(step, pos):
    return any(m.start() <= pos < m.end() for m in PROTECTED.finditer(step))


def _occurrences(step, pattern, need_math=None):
    out = []
    for m in re.finditer(pattern, step):
        if in_protected(step, m.start()):
            continue
        if need_math is None or in_math(step, m.start()) == need_math:
            out.append((m.start(), m.end(), m.group(0)))
    return out


def _swap_table(pairs):
    table = {}
    for a, b in pairs:
        table[a] = b
        table[b] = a
    return table


def _regex_for_keys(keys, word=True):
    ks = sorted(keys, key=len, reverse=True)
    body = "|".join(re.escape(k) for k in ks)
    if word:
        return r"(?<![A-Za-z\\-])(?:" + body + r")(?![A-Za-z-])"
    return r"(?:" + body + r")(?![A-Za-z])"


# ----------------------------------------------------------------------------- vocabularies
INEQ = _swap_table([(r"\leq", r"\geq"), (r"\le", r"\ge"), (r"\leqslant", r"\geqslant"), (r"\lesssim", r"\gtrsim"),
                    (r"\ll", r"\gg"), (r"\preceq", r"\succeq"), (r"\prec", r"\succ")])
LIMOPS = _swap_table([(r"\limsup", r"\liminf"), (r"\sup", r"\inf"), (r"\max", r"\min"), (r"\varlimsup", r"\varliminf")])
SETOPS = _swap_table([(r"\cup", r"\cap"), (r"\bigcup", r"\bigcap"), (r"\subseteq", r"\supseteq"),
                      (r"\subset", r"\supset"), (r"\subsetneq", r"\supsetneq"), (r"\vee", r"\wedge"),
                      (r"\bigvee", r"\bigwedge"), (r"\oplus", r"\otimes")])
QUANT = _swap_table([(r"\forall", r"\exists")])
LIMIT_TARGET = _swap_table([(r"\to 0", r"\to \infty"), (r"\to0", r"\to\infty"), (r"\rightarrow 0", r"\rightarrow \infty"),
                            (r"\to +\infty", r"\to 0"), (r"\to -\infty", r"\to +\infty"), (r"\to 1", r"\to 0")])
# direction words: swapping reverses an order, a bound or an orientation (taxonomy inequality_direction)
WORDS_DIR = _swap_table([("at most", "at least"), ("increasing", "decreasing"), ("non-increasing", "non-decreasing"),
                         ("nonincreasing", "nondecreasing"), ("sufficiently large", "sufficiently small"),
                         ("large enough", "small enough"), ("upper", "lower"), ("bounded above", "bounded below"),
                         ("maximum", "minimum"), ("maximal", "minimal"), ("supremum", "infimum"), ("larger", "smaller"),
                         ("greater", "smaller"), ("dominates", "is dominated by"),
                         ("tends to zero", "tends to infinity"), ("upper semicontinuous", "lower semicontinuous"),
                         ("subsolution", "supersolution"), ("subharmonic", "superharmonic"), ("subadditive", "superadditive"),
                         ("submultiplicative", "supermultiplicative"), ("lower bound", "upper bound"),
                         ("injective", "surjective"), ("monomorphism", "epimorphism"), ("kernel", "cokernel"),
                         ("covariant", "contravariant"), ("orientation-preserving", "orientation-reversing"),
                         ("even", "odd"), ("necessary", "sufficient"), ("ascending", "descending"),
                         ("expanding", "contracting"), ("overestimates", "underestimates"), ("faster", "slower"),
                         ("positive definite", "negative definite"), ("positive semidefinite", "negative semidefinite"),
                         ("convex", "concave"), ("open", "closed"), ("dense", "nowhere dense"),
                         ("nonempty", "empty"), ("finite", "infinite"), ("countable", "uncountable"),
                         ("positive", "negative"), ("nonnegative", "nonpositive"), ("non-negative", "non-positive"),
                         ("recurrent", "transient"), ("stable", "unstable"), ("prime", "composite"),
                         ("connected", "disconnected"), ("rational", "irrational"), ("algebraic", "transcendental"),
                         ("abelian", "non-abelian"), ("torsion", "torsion-free"), ("reducible", "irreducible"),
                         ("consistent", "inconsistent"), ("decidable", "undecidable"), ("computable", "uncomputable"),
                         ("satisfiable", "unsatisfiable"), ("realizable", "unrealizable"), ("underfitting", "overfitting"),
                         ("strongly convex", "strongly concave"), ("submodular", "supermodular")])
QUANT_WORDS = _swap_table([("for all", "for some"), ("for every", "for some"), ("for each", "for some"),
                           ("for any", "for some"), ("every", "some")])
# one-directional: the replacement does NOT deliver what the step uses (hypothesis weakened or altered)
WORDS_B = {
    "uniformly": "pointwise", "uniformly continuous": "continuous", "uniformly bounded": "bounded",
    "uniformly elliptic": "elliptic", "uniformly convex": "convex", "strongly convex": "convex",
    "compact": "closed", "compactly supported": "bounded", "continuous": "measurable", "Lipschitz": "continuous",
    "smooth": "continuous", "analytic": "smooth", "holomorphic": "continuous", "differentiable": "continuous",
    "absolutely continuous": "continuous", "absolutely convergent": "convergent", "bounded": "finite",
    "complete": "separable", "separable": "infinite-dimensional", "reflexive": "Banach", "Hilbert": "Banach",
    "finite-dimensional": "separable", "finite dimensional": "separable", "self-adjoint": "symmetric",
    "symmetric": "self-adjoint", "positive definite": "positive semidefinite", "invertible": "injective",
    "bijective": "surjective", "isomorphism": "homomorphism", "homeomorphic": "homotopy equivalent",
    "diffeomorphic": "homeomorphic", "isometric": "conformal", "simply connected": "connected",
    "closed manifold": "compact manifold", "orientable": "connected", "Hausdorff": "first countable",
    "metrizable": "Hausdorff", "locally compact": "locally closed", "paracompact": "Hausdorff",
    "finitely generated": "countably generated", "Noetherian": "commutative", "Artinian": "Noetherian",
    "principal ideal domain": "integral domain", "unique factorization domain": "integral domain",
    "integral domain": "commutative ring", "field": "integral domain", "algebraically closed": "perfect",
    "perfect": "infinite", "separable extension": "algebraic extension", "Galois": "normal", "normal": "separable",
    "free": "projective", "projective": "flat", "injective module": "divisible module", "flat": "torsion-free",
    "torsion-free": "reduced", "irreducible": "connected", "smooth variety": "normal variety",
    "proper": "separated", "projective variety": "quasi-projective variety", "ample": "nef", "very ample": "ample",
    "nef": "pseudo-effective", "coprime": "distinct", "relatively prime": "distinct", "squarefree": "odd",
    "prime": "odd", "prime power": "integer", "primitive": "nonzero", "cyclic": "abelian", "abelian": "solvable",
    "solvable": "finite", "nilpotent": "solvable", "simple": "perfect", "regular graph": "connected graph",
    "bipartite": "triangle-free", "planar": "sparse", "connected graph": "graph", "Hamiltonian": "connected",
    "independent set": "set", "matching": "subgraph", "linearly independent": "nonzero", "orthonormal": "orthogonal",
    "orthogonal": "linearly independent", "unitary": "invertible", "Hermitian": "normal", "convex function": "function",
    "concave": "quasi-concave", "coercive": "bounded below", "monotone": "continuous", "elliptic": "degenerate elliptic",
    "parabolic": "elliptic", "hyperbolic": "parabolic", "weak solution": "distributional solution",
    "strong solution": "weak solution", "classical solution": "weak solution", "viscosity solution": "weak solution",
    "in $L^2$": "in $L^1$", "in $L^p$": "in $L^1$", "in $H^1$": "in $L^2$", "in $W^{1,p}$": "in $L^p$",
    "in $C^1$": "in $C^0$", "in $C^\\infty$": "in $C^1$", "in $C^2$": "in $C^1$", "strongly": "weakly",
    "in norm": "weakly", "in measure": "in distribution", "almost everywhere": "in measure",
    "i.i.d.": "identically distributed", "independent": "uncorrelated", "sub-Gaussian": "square-integrable",
    "subgaussian": "square-integrable", "bounded variance": "finite mean", "Lipschitz continuous": "continuous",
    "$L$-smooth": "differentiable", "strongly monotone": "monotone", "PAC-learnable": "learnable",
    "realizable": "agnostic", "consistent": "complete", "complete theory": "consistent theory",
    "decidable": "recursively enumerable", "computable": "definable", "countable model": "model",
    "well-ordered": "totally ordered", "totally ordered": "partially ordered", "transitive": "reflexive",
    "first-order": "second-order", "recursive": "recursively enumerable", "definable": "arbitrary",
    "with probability one": "with positive probability", "with positive probability": "with probability one",
    "positive measure": "measure zero", "finite measure": "sigma-finite measure", "sigma-finite": "infinite",
    "finite variance": "infinite variance", "finite mean": "infinite mean", "finite expectation": "infinite expectation",
    "square-integrable": "integrable", "uniformly integrable": "integrable", "martingale": "submartingale",
    "stationary": "ergodic", "ergodic": "stationary", "exchangeable": "identically distributed",
}
MODE_RE = re.compile(r"(?<![A-Za-z])((?:converge[sd]?|convergence|holds?|hold|tends?)\s+)(almost surely|a\.s\.\\?|almost everywhere|in probability|in distribution|in law|uniformly|strongly|weakly|in norm|pointwise)(?![A-Za-z])")
MODE_SWAP = {"almost surely": "in probability", "a.s.": "in probability", "a.s.\\": "in probability",
             "almost everywhere": "in measure", "in probability": "in distribution", "in distribution": "in probability",
             "in law": "in probability", "uniformly": "pointwise", "strongly": "weakly", "weakly": "strongly",
             "in norm": "weakly", "pointwise": "uniformly"}
DROP = ("independent", "bounded", "uniformly", "integrable", "finite", "continuous", "nonnegative", "non-negative",
        "increasing", "uniformly integrable", "square-integrable", "measurable", "compact", "positive", "Lipschitz",
        "monotone", "decreasing", "symmetric", "centered", "closed", "open", "connected", "irreducible", "smooth",
        "analytic", "holomorphic", "convex", "concave", "coercive", "elliptic", "separable", "complete", "reflexive",
        "self-adjoint", "invertible", "injective", "surjective", "bijective", "orthogonal", "orthonormal", "unitary",
        "Hermitian", "finite-dimensional", "finitely generated", "Noetherian", "Artinian", "commutative", "abelian",
        "cyclic", "simple", "prime", "coprime", "squarefree", "primitive", "torsion-free", "free", "projective",
        "flat", "proper", "ample", "nef", "reduced", "normal", "regular", "simply connected", "orientable",
        "Hausdorff", "metrizable", "paracompact", "locally compact", "locally finite", "countable", "nonempty",
        "distinct", "linearly independent", "dense", "nowhere dense", "planar", "bipartite", "regular", "acyclic",
        "connected", "Lipschitz continuous", "differentiable", "sub-Gaussian", "subgaussian", "well-ordered",
        "consistent", "decidable", "computable", "definable", "recursive", "transitive", "strictly", "uniformly elliptic",
        "positive definite", "strongly convex", "compactly supported", "absolutely continuous", "stationary", "ergodic")
NOUNS = (r"random|variable|variables|function|functions|sequence|sequences|process|processes|set|sets|measure|"
         r"measures|martingale|family|families|increments|increment|domain|domains|operator|operators|kernel|"
         r"kernels|subset|subsets|sample|samples|Markov|chain|walk|graph|graphs|matrix|matrices|map|maps|mapping|"
         r"mappings|space|spaces|group|groups|ring|rings|module|modules|field|fields|ideal|ideals|extension|"
         r"extensions|variety|varieties|scheme|schemes|sheaf|sheaves|bundle|bundles|manifold|manifolds|surface|"
         r"surfaces|curve|curves|metric|metrics|form|forms|solution|solutions|subsolution|supersolution|"
         r"functional|functionals|norm|norms|topology|topologies|cover|covers|partition|partitions|polynomial|"
         r"polynomials|integer|integers|number|numbers|element|elements|vector|vectors|subspace|subspaces|"
         r"lattice|lattices|order|orders|relation|relations|model|models|theory|theories|formula|formulas|"
         r"structure|structures|algebra|algebras|category|categories|functor|functors|morphism|morphisms|"
         r"homomorphism|homomorphisms|embedding|embeddings|immersion|submersion|region|regions|boundary|"
         r"hypothesis|hypotheses|class|classes|learner|learners|estimator|estimators|loss|losses|kernel|"
         r"and|,|in|on|with|of|for|if|then|such|that|whenever")
# citation mismatches: the replacement result does NOT deliver what the step uses
THEOREMS = {
    "Fatou's lemma": "the dominated convergence theorem", "Fatou": "dominated convergence",
    "monotone convergence": "dominated convergence", "dominated convergence": "Fatou's lemma",
    "Fubini": "Tonelli", "Tonelli": "Fubini", "Cauchy-Schwarz": "Jensen", "Cauchy--Schwarz": "Jensen",
    "Cauchy\u2013Schwarz": "Jensen", "H\\\"older": "Jensen", "H\\\"{o}lder": "Jensen", "Hölder": "Jensen",
    "Holder's inequality": "Jensen's inequality", "Jensen's inequality": "Markov's inequality", "Young's inequality": "Jensen's inequality",
    "Minkowski": "Jensen", "Markov's inequality": "Chebyshev's inequality", "Chebyshev's inequality": "Markov's inequality",
    "Gronwall": "Young", "Gr\\\"onwall": "Young", "Grönwall": "Young", "Poincar\\'e": "Sobolev", "Poincaré inequality": "Sobolev inequality",
    "Sobolev embedding": "Morrey", "Rellich": "Banach-Alaoglu", "Rellich--Kondrachov": "Banach--Alaoglu",
    "Arzel\\`a-Ascoli": "Banach-Alaoglu", "Arzela-Ascoli": "Banach-Alaoglu", "Arzelà-Ascoli": "Banach-Alaoglu",
    "Banach-Alaoglu": "Arzela-Ascoli", "Banach--Alaoglu": "Arzela--Ascoli", "Hahn-Banach": "Banach-Steinhaus",
    "Hahn--Banach": "Banach--Steinhaus", "Banach-Steinhaus": "Hahn-Banach", "open mapping theorem": "closed graph theorem",
    "closed graph theorem": "open mapping theorem", "Riesz representation": "Hahn-Banach", "Lax-Milgram": "Riesz representation",
    "Lax--Milgram": "Riesz representation", "spectral theorem": "open mapping theorem", "Stone-Weierstrass": "Arzela-Ascoli",
    "Weierstrass": "Runge", "Baire category": "Zorn's lemma", "Zorn's lemma": "Baire category theorem",
    "Radon-Nikodym": "Lebesgue differentiation", "Lebesgue differentiation": "Radon-Nikodym", "Lusin": "Egorov", "Egorov": "Lusin",
    "Vitali": "Egorov", "Plancherel": "Hausdorff-Young", "Parseval": "Hausdorff-Young", "Hausdorff-Young": "Parseval",
    "Riemann-Lebesgue": "Plancherel", "Paley-Wiener": "Plancherel", "maximum principle": "Harnack inequality",
    "Harnack": "Schauder", "Schauder": "Harnack", "Calder\\'on-Zygmund": "Schauder", "Calderon-Zygmund": "Schauder",
    "De Giorgi": "Schauder", "Nash-Moser": "Schauder", "Krylov-Safonov": "Schauder", "Aubin-Lions": "Banach-Alaoglu",
    "Lions-Magenes": "Aubin-Lions", "Duhamel": "Gronwall", "Picard-Lindel\\\"of": "Peano", "Picard": "Peano", "Peano": "Picard",
    "implicit function theorem": "inverse function theorem", "inverse function theorem": "implicit function theorem",
    "Taylor's theorem": "the mean value theorem", "mean value theorem": "intermediate value theorem",
    "intermediate value theorem": "mean value theorem", "Rolle": "Cauchy", "Cauchy's theorem": "Morera's theorem",
    "Cauchy's integral formula": "Liouville's theorem", "Liouville": "Rouch\\'e", "Rouch\\'e": "Liouville", "Rouché": "Liouville",
    "Morera": "Cauchy", "Schwarz lemma": "maximum modulus principle", "Montel": "Hurwitz", "Hurwitz": "Montel",
    "Riemann mapping": "Montel", "Nakayama": "Artin-Rees", "Artin-Rees": "Nakayama", "Krull": "Nakayama",
    "Nullstellensatz": "Hilbert's basis theorem", "Hilbert's basis theorem": "Nullstellensatz", "Hilbert basis theorem": "Nullstellensatz",
    "Bezout": "Gauss's lemma", "B\\'ezout": "Gauss's lemma", "Bézout": "Gauss's lemma", "Gauss's lemma": "Eisenstein",
    "Eisenstein": "Gauss's lemma", "Chinese remainder theorem": "Hensel's lemma", "Hensel": "Chevalley-Warning",
    "Chevalley-Warning": "Hensel's lemma", "Dirichlet's theorem": "the prime number theorem", "prime number theorem": "Dirichlet's theorem",
    "quadratic reciprocity": "Hensel's lemma", "Fermat's little theorem": "Wilson's theorem", "Wilson's theorem": "Fermat's little theorem",
    "Euler's theorem": "Fermat's little theorem", "Lagrange's theorem": "Cauchy's theorem", "Sylow": "Lagrange",
    "Cayley-Hamilton": "Jordan", "Cayley--Hamilton": "Jordan", "Jordan normal form": "Schur decomposition", "Schur": "Jordan",
    "Burnside": "Sylow", "Maschke": "Schur", "Wedderburn": "Maschke", "Artin-Wedderburn": "Maschke", "Galois correspondence": "Sylow theorems",
    "Riemann-Roch": "Serre duality", "Serre duality": "Riemann-Roch", "Bertini": "Riemann-Roch", "Zariski's main theorem": "Bertini",
    "Hodge": "Lefschetz", "Lefschetz": "Hodge", "Kodaira vanishing": "Serre vanishing", "Serre vanishing": "Kodaira vanishing",
    "Grothendieck-Riemann-Roch": "Hirzebruch-Riemann-Roch", "Hirzebruch": "Grothendieck", "Chow's lemma": "Zariski's main theorem",
    "Hall's theorem": "K\\\"onig's theorem", "Hall": "Dilworth", "Dilworth": "Hall", "K\\\"onig": "Hall", "Menger": "Hall",
    "Tutte": "Hall", "Ramsey": "Tur\\'an", "Tur\\'an": "Ramsey", "Turán": "Ramsey", "Turan": "Ramsey", "Szemer\\'edi": "Ramsey",
    "Szemerédi": "Ramsey", "regularity lemma": "removal lemma", "removal lemma": "regularity lemma", "Erd\\H{o}s-Ko-Rado": "Sperner",
    "Sperner": "Erd\\H{o}s-Ko-Rado", "LYM": "Sperner", "Kruskal-Katona": "Sperner", "Lov\\'asz local lemma": "the union bound",
    "local lemma": "the union bound", "union bound": "Cauchy-Schwarz", "Cauchy-Davenport": "Vosper", "Vosper": "Cauchy-Davenport",
    "Freiman": "Pl\\\"unnecke", "Pl\\\"unnecke": "Freiman", "pigeonhole": "Ramsey", "inclusion-exclusion": "the union bound",
    "Cayley's formula": "Kirchhoff's theorem", "Kirchhoff": "Cayley", "matrix-tree": "Cayley's formula",
    "Brouwer": "Borsuk-Ulam", "Borsuk-Ulam": "Brouwer", "Borsuk--Ulam": "Brouwer", "Lefschetz fixed point": "Brouwer",
    "Poincar\\'e duality": "Alexander duality", "Poincaré duality": "Alexander duality", "Alexander duality": "Poincar\\'e duality",
    "Mayer-Vietoris": "K\\\"unneth", "Mayer--Vietoris": "K\\\"unneth", "K\\\"unneth": "Mayer-Vietoris", "Künneth": "Mayer-Vietoris",
    "Hurewicz": "Whitehead", "Whitehead": "Hurewicz", "van Kampen": "Hurewicz", "Seifert-van Kampen": "Hurewicz",
    "universal coefficient": "K\\\"unneth", "excision": "Mayer-Vietoris", "Freudenthal": "Hurewicz", "Serre spectral sequence": "Mayer-Vietoris",
    "Gauss-Bonnet": "Stokes", "Gauss--Bonnet": "Stokes", "Stokes": "Gauss-Bonnet", "divergence theorem": "Stokes' theorem",
    "Sard": "Whitney", "Whitney": "Sard", "Hopf-Rinow": "Myers", "Myers": "Bonnet-Myers", "Bonnet-Myers": "Hopf-Rinow",
    "Cartan-Hadamard": "Hopf-Rinow", "Bishop-Gromov": "Cheeger-Gromoll", "Cheeger-Gromoll": "Bishop-Gromov",
    "Rauch": "Toponogov", "Toponogov": "Rauch", "Frobenius": "Darboux", "Darboux": "Frobenius", "Nash embedding": "Whitney embedding",
    "Whitney embedding": "Nash embedding", "de Rham": "Hodge", "Bochner": "Weitzenb\\\"ock", "Weitzenb\\\"ock": "Bochner",
    "compactness theorem": "completeness theorem", "completeness theorem": "compactness theorem", "L\\\"owenheim-Skolem": "compactness",
    "Lowenheim-Skolem": "compactness", "Löwenheim-Skolem": "compactness", "downward L\\\"owenheim-Skolem": "upward L\\\"owenheim-Skolem",
    "G\\\"odel's completeness": "G\\\"odel's incompleteness", "incompleteness theorem": "completeness theorem",
    "Tarski": "G\\\"odel", "Rice's theorem": "the halting problem", "halting problem": "Rice's theorem", "recursion theorem": "Rice's theorem",
    "Zermelo": "Zorn", "axiom of choice": "countable choice", "Ramsey's theorem": "K\\\"onig's lemma", "K\\\"onig's lemma": "Ramsey's theorem",
    "Hoeffding": "Markov", "Azuma": "Hoeffding", "McDiarmid": "Hoeffding", "Bernstein": "Chebyshev", "Talagrand": "Chebyshev",
    "Chernoff": "Chebyshev", "Sauer-Shelah": "the union bound", "Sauer": "the union bound", "VC": "Rademacher", "Rademacher": "VC",
    "Dudley": "Sauer-Shelah", "symmetrization": "the union bound", "Massart": "Dudley", "Pinsker": "Jensen", "Fano": "Le Cam",
    "Le Cam": "Fano", "Assouad": "Fano", "Talagrand's inequality": "Chebyshev's inequality", "contraction lemma": "the union bound",
    "Ledoux-Talagrand": "the union bound", "Danskin": "the envelope theorem", "envelope theorem": "Danskin's theorem",
    "Slutsky": "Prokhorov", "Prokhorov": "Slutsky", "Portmanteau": "Skorokhod", "Donsker": "Skorokhod",
    "Borel-Cantelli": "Fubini", "Borel--Cantelli": "Fubini", "Borel\u2013Cantelli": "Fubini", "law of large numbers": "central limit theorem",
    "central limit theorem": "law of large numbers", "Doob's maximal inequality": "Doob's optional stopping theorem",
    "optional stopping": "martingale convergence", "It\\^o's formula": "Girsanov's theorem", "Itô's formula": "Girsanov's theorem",
    "Girsanov": "It\\^o", "Perron-Frobenius": "Gershgorin", "Perron--Frobenius": "Gershgorin", "Gershgorin": "Perron-Frobenius",
    "Courant-Fischer": "Weyl", "Courant--Fischer": "Weyl", "Weyl's inequality": "Courant-Fischer", "Cauchy interlacing": "Weyl's inequality",
    "Eckart-Young": "Courant-Fischer", "Eckart--Young": "Courant-Fischer", "Davis-Kahan": "Weyl", "Davis--Kahan": "Weyl",
    "Wedin": "Davis-Kahan", "Marchenko-Pastur": "Wigner", "Wigner": "Marchenko-Pastur", "Bai-Yin": "Marchenko-Pastur",
    "Gordon": "Slepian", "Slepian": "Sudakov-Fernique", "Sudakov-Fernique": "Slepian", "Kantorovich": "Jensen",
    "Brenier": "Kantorovich", "Rockafellar": "Fenchel", "Fenchel": "Rockafellar", "Moreau": "Fenchel", "Fenchel-Young": "Jensen",
    "Karush-Kuhn-Tucker": "Lagrange", "KKT": "Lagrange", "Farkas": "Hahn-Banach", "Krein-Milman": "Hahn-Banach",
    "Caratheodory": "Helly", "Carath\\'eodory": "Helly", "Helly": "Radon", "Radon's theorem": "Helly's theorem",
    "Kakutani": "Brouwer", "Nash": "Kakutani", "von Neumann": "Nash", "minimax theorem": "Nash's theorem",
    "Lyapunov": "LaSalle", "LaSalle": "Lyapunov", "Banach fixed point": "Brouwer fixed point", "Banach fixed-point": "Brouwer fixed-point",
    "contraction mapping": "Brouwer fixed point", "Schauder fixed point": "Banach fixed point", "Leray-Schauder": "Banach",
    "Cantor": "Baire", "Heine-Borel": "Bolzano-Weierstrass", "Heine--Borel": "Bolzano--Weierstrass", "Bolzano-Weierstrass": "Heine-Borel",
    "Tychonoff": "Heine-Borel", "Urysohn": "Tietze", "Tietze": "Urysohn", "Dini": "Egorov", "Abel": "Dirichlet",
    "Dirichlet's test": "Abel's test", "Abel's test": "Dirichlet's test", "Stirling": "Wallis", "Euler-Maclaurin": "Stirling",
    "Cauchy-Riemann": "Laplace", "Laplace transform": "Fourier transform", "Fourier inversion": "Plancherel",
    "Poisson summation": "Fourier inversion", "Shannon": "Nyquist", "Kraft": "Shannon", "Pinsker's inequality": "Jensen's inequality",
    "data processing inequality": "Pinsker's inequality", "Gibbs": "Jensen", "log-sum inequality": "Jensen's inequality",
}
CITE_CONTEXT = re.compile(r"^(?:'s)?\s+(?:inequality|inequalities|lemma|theorem|bound|formula|criterion|estimate|"
                          r"argument|principle|identity|representation|decomposition|duality|embedding|correspondence|"
                          r"test|rule|trick|property|condition|conditions|fixed point|fixed-point|formula)\b")
LIMTYPE = r"\\(?:limsup|liminf|varlimsup|varliminf|lim|sup|inf|max|min)(?![A-Za-z])"   # (?!..) 2026-09-06: never the prefix of \limits
LIMTYPE_IC = r"\\(?:limsup|liminf|varlimsup|varliminf|lim|sup|inf)(?![A-Za-z])"   # interchange: \min/\max carry their argument in braces
LIMCLASS = {"sup": "S", "max": "S", "inf": "I", "min": "I", "lim": "L", "limsup": "LS", "varlimsup": "LS", "liminf": "LI", "varliminf": "LI"}
SUBSUP = r"(?:\\nolimits|\\limits)?(?:_\{(?:[^{}]|\{[^{}]*\})*\}|_[A-Za-z0-9])?(?:\^\{(?:[^{}]|\{[^{}]*\})*\}|\^[A-Za-z0-9])?"
OP_LIM = re.compile(r"(" + LIMTYPE + SUBSUP + r")\s*(" + LIMTYPE + SUBSUP + r")")
INTLIKE = r"(?:\\int|\\iint|\\oint|\\sum|\\prod|\\mathbb\{E\}|\\E\b|\\mathbf\{E\}|\\operatorname\{E\})"
OP_INT = re.compile(r"(" + LIMTYPE_IC + SUBSUP + r")\s*(" + INTLIKE + SUBSUP + r")")
OP_INT2 = re.compile(r"(" + INTLIKE + SUBSUP + r")\s*(" + LIMTYPE_IC + SUBSUP + r")")


# ----------------------------------------------------------------------------- operator table
OPS = []


def op(name, mechanism, taxonomy, tier, need_math):
    def deco(fn):
        OPS.append((name, mechanism, taxonomy, tier, need_math, fn))
        return fn
    return deco


@op("ineq_flip", "inequality_direction", "inequality_direction", "A", True)
def c_ineq(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(INEQ, word=False), True):
        out.append((s, e, INEQ[t]))
    for m in re.finditer(r"(?<=[A-Za-z0-9)}\]\s])([<>])(?=[\s0-9A-Za-z(\\{])", step):
        if in_math(step, m.start()) and step[m.start() - 1:m.start()] not in "<>" and step[m.end():m.end() + 1] not in "<>=":
            out.append((m.start(), m.end(), ">" if m.group(1) == "<" else "<"))
    return out


@op("ineq_to_eq", "inequality_strengthened", "inequality_direction", "B", True)
def c_ineq_eq(step):
    return [(s, e, "=") for s, e, t in _occurrences(step, r"\\(?:leq|le|geq|ge|leqslant|geqslant)(?![A-Za-z])", True)]


GATED_DIR = {"open", "closed", "even", "odd"}
GATE_NOUN = re.compile(r"\s+(?:set|sets|ball|balls|subset|subsets|cover|covers|interval|intervals|neighbou?rhood|neighbou?rhoods|"
                       r"map|maps|manifold|manifolds|form|forms|condition|conditions|cone|disc|disk|domain|orbit|"
                       r"number|numbers|integer|integers|function|functions|permutation|permutations|cycle|cycles|"
                       r"degree|index|dimension|part|prime|primes|subgroup|subgroups|embedding|immersion|surface|surfaces|"
                       r"curve|curves|region|regions|half-space|halfspace|cell|cells|simplex|simplices|face|faces)")


@op("word_flip", "direction_word", "inequality_direction", "A", False)
def c_words_dir(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(WORDS_DIR), False):
        if t in GATED_DIR and not GATE_NOUN.match(step[e:e + 24]):
            continue
        if step[e:e + 1] == "-" or step[max(0, s - 1):s] == "-":
            continue
        out.append((s, e, WORDS_DIR[t]))
    fixed = []
    for s0, e0, rep in out:
        art = re.search(r"(?:^|\s)(an?)\s$", step[max(0, s0 - 4):s0])
        if art and rep[:1].isalpha():
            want = "an" if rep[0] in VOWEL else "a"
            if art.group(1) != want:
                fixed.append((s0 - len(art.group(1)) - 1, e0, want + " " + rep))
                continue
        fixed.append((s0, e0, rep))
    return fixed


@op("quantifier_swap", "quantifier", "quantifier_swap", "A", True)
def c_quant(step):
    return [(s, e, QUANT[t]) for s, e, t in _occurrences(step, _regex_for_keys(QUANT, word=False), True)]


@op("quant_word", "quantifier_word", "quantifier_swap", "A", False)
def c_quant_word(step):
    return [(s, e, QUANT_WORDS[t]) for s, e, t in _occurrences(step, _regex_for_keys(QUANT_WORDS), False)]


def _in_script(step, pos):
    """True when pos sits inside an unclosed _{...} or ^{...} group of its math span (an index, not a sign)."""
    start = 0
    for a, b in math_spans(step):
        if a <= pos < b:
            start = a
            break
    depth = 0
    k = pos - 1
    while k >= start:
        ch = step[k]
        if ch == "}":
            depth += 1
        elif ch == "{":
            if depth == 0:
                return k >= 1 and step[k - 1] in "_^"
            depth -= 1
        k -= 1
    return False


@op("sign_flip", "sign", "sign_flip", "B", True)
def c_sign(step):
    out = []
    for m in re.finditer(r"(?<=[A-Za-z0-9)}\]])\s*([+-])\s*(?=[A-Za-z0-9(\\{])", step):
        if not in_math(step, m.start()):
            continue
        if "\\to" in step[max(0, m.start() - 4):m.start()]:
            continue
        if _in_script(step, m.start(1)):
            continue
        if re.match(r"[A-Za-z]\s*$", step[max(0, m.start(1) - 2):m.start(1)]) and re.match(r"\s*1(?![0-9.])", step[m.end(1):m.end(1) + 3]):
            continue
        out.append((m.start(1), m.end(1), "-" if m.group(1) == "+" else "+"))
    return out


VOWEL = "aeiouAEIOU"


@op("hypothesis_drop", "hypothesis_dropped", "dropped_hypothesis", "B", False)
def c_drop(step):
    """Drop a hypothesis word so that the residue still reads as prose (2026-09-06 11:4x, after the dry sample showed
    2/2 hypothesis_drop items with a grammar tell: 'continuous and in (0,inf)', 'the map is for locally uniform').
    Admitted shapes:
      X noun                 -> noun                         (article repaired)
      X and Y ... / X, Y ... -> Y ...    (first conjunct)    only when Y is a plain word, never a clause '$u$ is'
      A and X ...            -> A ...    (later conjunct)    whatever follows X (noun, preposition, punctuation)
      P, Q and X ...         -> P and Q ...                  (a comma list keeps its conjunction)
      A, X ...               -> A ...
      bounded uniformly in   -> bounded in
    A lone predicate adjective before a preposition ('is continuous for ...') has no grammatical residue and is not a site."""
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(DROP), False):
        after = step[e:e + 40]
        if BOUND_TAIL.match(after):
            continue
        if not _word_admitted(t):
            continue
        if re.search(r"(?:strictly|monotonically|not|non-|non|weakly|locally|globally|almost|uniformly|absolutely)\s*$", step[max(0, s - 16):s]):
            continue
        m = re.match(r"\s+(" + NOUNS + r")\b", after)
        mid = None
        if not m:
            # one intervening adjective: 'centered Gaussian vector', 'compact Hausdorff space' (2026-09-06)
            m2 = re.match(r"\s+([A-Z][a-z]+|[a-z]+(?:-[a-z]+)?)\s+(" + NOUNS + r")\b", after)
            if m2 and (m2.group(1)[0].isupper() or m2.group(1).lower() in DROP_SET) and m2.group(2) not in ("and", ","):
                m, mid = m2, m2.group(1)
        nxt = (mid or m.group(1)) if m else ""
        if nxt in ("measure", "measures") and t in ("positive", "finite", "nonnegative", "non-negative"):
            continue
        before = step[max(0, s - 60):s]
        off = max(0, s - 60)
        conj = re.search(r"(\s*)(,|\band)\s+$", before)
        e_sp = e + 1 if step[e:e + 1] == " " else e
        if conj and t == "uniformly":
            continue   # ', uniformly in x' has no prose residue without the adverb
        if conj and conj.group(2) == "," and nxt in ("and", ","):
            conj = None   # 'P, X and Y': the comma may be appositive - drop 'X and ' instead (first-conjunct path)
        if conj and not in_math(step, off + conj.start(2)):
            # a later conjunct: drop it with its conjunction; a comma list gets its 'and' back
            s2, e2, rep = off + conj.start(), e, ""
            if conj.group(2) == "and":
                head = before[:conj.start()]
                lst = re.search(r",(\s+)([^,]{1,40}?)\s*$", head)
                if lst and not in_math(step, off + lst.start()) and "$" not in lst.group(2):
                    s2 = off + lst.start()
                    rep = " and " + lst.group(2)
            if not (m or t == "uniformly" or re.match(r"\s*(?:[.,;:)]|$)", after)):
                # 'A and X <something else>' - only prose continuations we understand
                continue
            out.append((s2, e2, rep))
            continue
        if nxt in ("and", ","):
            # first conjunct: 'X and Y' -> 'Y' only when Y is a plain word (not '$u$ is ...', not a clause)
            rest = after[m.end():m.end() + 30]
            if not re.match(r"\s*[A-Za-z][A-Za-z-]*(?:\s+[A-Za-z][A-Za-z-]*)?\s*(?:\$|\\|[A-Za-z]|[.,;:])", rest):
                continue
            if re.match(r"\s*[A-Za-z][A-Za-z-]*\s+(?:is|are|be|being|has|have|was|were|holds?|satisf)", rest):
                continue
            if re.match(r"\s*(?:is|are|be|being|has|have|was|were|holds?|satisf\w*|the|we|it|this|that|then|so|hence|thus|let|"
                        r"there|its|their|each|every|for|by|since|if|in|on|of|with|converge\w*|define\w*|denote\w*|"
                        r"suppose|assume|apply\w*|obtain\w*|conclude\w*|use\w*|write\w*|note|see|recall)\b", rest):
                continue
            w = re.match(r"\s*([A-Za-z][A-Za-z-]*)", rest).group(1)
            if w.lower() not in DROP_SET and not re.search(r"(?:ed|ous|ive|able|ible|al|ic|ian|ent|ant|ary|less|ful|free)$", w.lower()):
                continue   # 'connected and contains' - a verb, not a second hypothesis
            e2 = e + m.end()
            e2 = e2 + 1 if step[e2:e2 + 1] == " " else e2
            out.append((s, e2, ""))
            continue
        if t == "uniformly":
            out.append((s, e_sp, ""))
            continue
        if not m or nxt in ("in", "on", "with", "of", "for", "if", "then", "such", "that", "whenever"):
            continue
        # adjective before a noun: drop it, repair the article
        s2, rep = s, ""
        art = re.search(r"(?:^|\s)(an?)\s$", step[max(0, s - 4):s])
        if art:
            want = "an" if nxt[0] in VOWEL else "a"
            if art.group(1) != want:
                s2 = s - len(art.group(1)) - 1
                rep = want + " "
        out.append((s2, e_sp, rep))
    return out


DROP_SET = {w.lower() for w in DROP} | {w.split()[-1].lower() for w in DROP}
BOUND_TAIL = re.compile(r"\s+(?:by|above by|below by|from above|from below|in terms of)\b")
# words whose meaning changes with the field: a swap is admitted only in the paper's home domain group
AMBIGUOUS_HOME = {
    "complete": {"analysis"}, "separable": {"analysis"}, "normal": {"algebra_nt_co", "geom_top_log"},
    "regular": {"algebra_nt_co"}, "simple": {"algebra_nt_co"}, "free": {"algebra_nt_co"}, "proper": {"geom_top_log"},
    "primitive": {"algebra_nt_co"}, "perfect": {"algebra_nt_co"}, "flat": {"algebra_nt_co"}, "field": {"algebra_nt_co"},
    "projective": {"algebra_nt_co"}, "reduced": {"algebra_nt_co"}, "prime": {"algebra_nt_co"}, "closed": {"analysis", "geom_top_log"},
    "open": {"analysis", "geom_top_log"}, "symmetric": {"analysis", "ml_theory"}, "orthogonal": {"analysis", "ml_theory"},
    "stationary": {"ml_theory"}, "ergodic": {"ml_theory"}, "consistent": {"geom_top_log", "ml_theory"},
    "independent": {"ml_theory"}, "transitive": {"geom_top_log", "algebra_nt_co"}, "cyclic": {"algebra_nt_co"},
    "monotone": {"analysis", "ml_theory"}, "convex": {"analysis", "ml_theory"}, "concave": {"analysis", "ml_theory"},
}
_DOMAIN = {"group": ""}


def set_domain(group):
    """The builder names the paper's domain group before asking for candidates (ambiguous words are gated on it)."""
    _DOMAIN["group"] = group or ""


def _word_admitted(word):
    home = AMBIGUOUS_HOME.get(word.lower())
    if home is None:
        return True
    return _DOMAIN["group"] in home


@op("hypothesis_swap", "hypothesis_weakened", "dropped_hypothesis", "B", False)
def c_words_b(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(WORDS_B), False):
        if BOUND_TAIL.match(step[e:e + 16]):
            continue
        if not _word_admitted(t):
            continue
        out.append((s, e, WORDS_B[t]))
    for m in MODE_RE.finditer(step):
        if not in_math(step, m.start()):
            mode = m.group(2)
            out.append((m.start(2), m.end(2), MODE_SWAP.get(mode, "in probability")))
    return out


@op("const_change", "constant_or_exponent", "wrong_constant_or_exponent", "B", True)
def c_const(step):
    out = []
    for m in re.finditer(r"\^\{?(2|3|4|1/2|1/4|-1|-2|1/3|2/3|3/2)\}?(?![0-9/])", step):
        if in_math(step, m.start()):
            cur = m.group(1)
            new = {"2": "3", "3": "2", "4": "2", "1/2": "1/4", "1/4": "1/2", "-1": "-2", "-2": "-1", "1/3": "2/3",
                   "2/3": "1/3", "3/2": "1/2"}[cur]
            out.append((m.start(1), m.end(1), new))
    for m in re.finditer(r"(?<![0-9.\^_{])\b(2|4|8|16)\b(?![0-9.}])", step):
        if in_math(step, m.start()) and step[m.start() - 1:m.start()] not in "^_":
            cur = m.group(1)
            new = {"2": "4", "4": "2", "8": "4", "16": "8"}[cur]
            out.append((m.start(1), m.end(1), new))
    for m in re.finditer(r"\\frac\{1\}\{(2|4)\}", step):
        if in_math(step, m.start()):
            out.append((m.start(1), m.end(1), "4" if m.group(1) == "2" else "2"))
    return out


@op("limit_target", "limit_value", "wrong_constant_or_exponent", "A", True)
def c_limit(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(LIMIT_TARGET, word=False), True):
        # 2026-09-06: '0 \\rightarrow V \\rightarrow ... \\rightarrow 0' is an exact sequence, not a limit
        if not re.search(r"[A-Za-z0-9)}]\s*$", step[max(0, s - 6):s]):
            continue
        if re.search(r"(?:^|[^A-Za-z])0\s*\\(?:to|rightarrow|longrightarrow)\b", step[max(0, s - 400):s]) or "\\xrightarrow" in step[max(0, s - 200):e + 40]:
            continue
        out.append((s, e, LIMIT_TARGET[t]))
    return out


@op("index_shift", "off_by_one", "off_by_one_index", "A", True)
def c_index(step):
    out = []
    for m in re.finditer(r"([A-Za-z])\s*([+-])\s*1(?![0-9.])", step):
        if in_math(step, m.start()):
            other = "-" if m.group(2) == "+" else "+"
            out.append((m.start(2), m.end(), other + "1"))
    return out


@op("sum_bound_shift", "off_by_one_bound", "off_by_one_index", "A", True)
def c_sum_bound(step):
    out = []
    for m in re.finditer(r"\\(?:sum|prod|bigcup|bigcap|max|min)_\{([a-zA-Z])=(0|1)\}", step):
        if in_math(step, m.start()):
            cur = m.group(2)
            out.append((m.start(2), m.end(2), "1" if cur == "0" else "0"))
    for m in re.finditer(r"\^\{?([a-zA-Z])\s*([+-])\s*1\}?", step):
        pass
    return out


@op("theorem_swap", "citation_mismatch", "wrong_lemma_cited", "B", False)
def c_theorem(step):
    out = []
    for s, e, t in _occurrences(step, _regex_for_keys(THEOREMS), False):
        if not re.search(r"'s|inequality|lemma|theorem|formula|convergence|stopping|numbers|duality|embedding|principle|test|problem", t):
            if not CITE_CONTEXT.match(step[e:e + 28]):
                continue
        if step[e:e + 2] == "'s" and not t.endswith("'s"):
            continue
        out.append((s, e, THEOREMS[t]))
    return out


REF_LOCAL = re.compile(r"\(eq (\d+)\)")
REF_NUMBERED = re.compile(r"\b(Lemma|Theorem|Proposition|Corollary|Claim|Equation|Step|Case|Remark)s?\s+(\d+(?:\.\d+){0,2})\b")


@op("ref_shift", "wrong_local_reference", "wrong_lemma_cited", "B", False)
def c_ref(step):
    """A local equation or result number changed to ANOTHER number that occurs in the same step or proof context:
    the step now cites the wrong line. Candidates carry the alternative in the replacement; the builder checks the
    alternative exists in the pair (it passes the whole proof through `context`)."""
    out = []
    nums = [m.group(1) for m in REF_LOCAL.finditer(step)]
    for m in REF_LOCAL.finditer(step):
        k = int(m.group(1))
        alt = k + 1 if k >= 1 else 2
        out.append((m.start(1), m.end(1), str(alt)))
        if k >= 2:
            out.append((m.start(1), m.end(1), str(k - 1)))
    for m in REF_NUMBERED.finditer(step):
        if in_math(step, m.start()):
            continue
        num = m.group(2)
        parts = num.split(".")
        last = int(parts[-1])
        parts2 = parts[:-1] + [str(last + 1)]
        out.append((m.start(2), m.end(2), ".".join(parts2)))
        if last >= 2:
            parts3 = parts[:-1] + [str(last - 1)]
            out.append((m.start(2), m.end(2), ".".join(parts3)))
    return out


@op("limit_order", "limit_order", "limit_order", "A", True)
def c_limit_order(step):
    out = []
    for m in OP_LIM.finditer(step):
        if not in_math(step, m.start()):
            continue
        a, b = m.group(1), m.group(2)
        if a == b:
            continue
        ca = LIMCLASS.get(re.match(r"\\([a-z]+)", a).group(1)); cb = LIMCLASS.get(re.match(r"\\([a-z]+)", b).group(1))
        if ca == cb and ca in ("S", "I"):
            continue   # 2026-09-06 hand-read: max_i sup_t -> sup_t max_i is the same number
        out.append((m.start(), m.end(), b + " " + a))
    return out


@op("interchange", "unjustified_interchange", "unjustified_interchange", "B", True)
def c_interchange(step):
    out = []
    for rx in (OP_INT, OP_INT2):
        for m in rx.finditer(step):
            if not in_math(step, m.start()):
                continue
            a, b = m.group(1), m.group(2)
            out.append((m.start(), m.end(), b + " " + a))
    return out


@op("limop_swap", "extremum_or_limit_operator", "extremum_swap", "A", True)
def c_limop(step):
    return [(s, e, LIMOPS[t]) for s, e, t in _occurrences(step, _regex_for_keys(LIMOPS, word=False), True)]


@op("setop_swap", "set_operation_direction", "set_operator_swap", "A", True)
def c_setop(step):
    return [(s, e, SETOPS[t]) for s, e, t in _occurrences(step, _regex_for_keys(SETOPS, word=False), True)]


OP_INDEX = {o[0]: o for o in OPS}
TAXONOMY = sorted({o[2] for o in OPS})

# ----------------------------------------------------------------------------- guards and difficulty
_WORD = re.compile(r"[A-Za-z]{3,}")
_STOP = {"the", "and", "for", "that", "with", "this", "then", "there", "which", "from", "are", "let", "have", "has",
         "such", "where", "when", "into", "also", "since", "thus", "hence", "therefore", "each", "any", "all", "some",
         "every", "given", "follows", "obtain", "get", "see", "using", "use", "now", "first", "second", "proof", "holds",
         "hold", "implies", "because", "these", "those", "than", "its", "one", "two", "can", "will", "not", "but"}


def _toks(t):
    return {w.lower() for w in _WORD.findall(t or "")} - _STOP


def restates_claim(step, claim):
    """The scar of 2026-08-17: a step whose conclusion IS the theorem cannot host a derivation fault. Token overlap
    with the claim above 0.55 (Jaccard) marks the step as a restatement and the builder skips it as a site."""
    a, b = _toks(step), _toks(claim)
    if not a or not b:
        return False
    return len(a & b) / len(a | b) > 0.55


def find_context_ok(cand, steps):
    """ref_shift: the alternative number must exist somewhere in the proof (as a local eq or a numbered result)."""
    name, i, s, e, rep = cand
    if name != "ref_shift":
        return True
    joined = " ".join(steps)
    st = steps[i]
    if st[max(0, s - 4):s] == "(eq ":
        return ("(eq %s)" % rep) in joined
    return re.search(r"\b(?:Lemma|Theorem|Proposition|Corollary|Claim|Equation|Step|Case|Remark)s?\s+" + re.escape(rep) + r"\b", joined) is not None


BASE_DIFF = {"ineq_flip": 1.0, "limop_swap": 1.0, "setop_swap": 1.0, "limit_target": 1.5, "word_flip": 1.5, "quant_word": 2.0,
             "quantifier_swap": 2.0, "sum_bound_shift": 2.0, "index_shift": 2.0, "sign_flip": 2.0, "const_change": 2.5,
             "ineq_to_eq": 2.5, "limit_order": 3.0, "interchange": 3.0, "ref_shift": 3.0, "theorem_swap": 3.0,
             "hypothesis_swap": 3.5, "hypothesis_drop": 4.0}


def difficulty(op_name, step_index, n_steps, removed, steps):
    """A heuristic estimate, not a measurement: operator class, proof length, whether the removed token recurs
    elsewhere in the proof (a local contradiction the reader can spot), and the site's position."""
    d = BASE_DIFF.get(op_name, 2.5)
    if n_steps >= 8:
        d += 0.5
    if n_steps >= 15:
        d += 0.5
    others = " ".join(st for k, st in enumerate(steps) if k != step_index)
    if removed and len(removed) >= 2 and removed in others:
        d -= 0.75
    if step_index == n_steps - 1:
        d += 0.5
    label = "easy" if d <= 1.75 else ("medium" if d <= 3.0 else "hard")
    return round(d, 2), label


# ----------------------------------------------------------------------------- candidates / apply
DEFINITIONAL_START = re.compile(r"^\s*(?:Let|Define|Set|Put|Denote|Write|Consider|Fix|Choose|Take|Recall|We (?:define|set|put|denote|write|choose|fix|take))")
DEF_MARK = re.compile(r":=|\\coloneqq|\\triangleq|\\stackrel\{[^{}]*def[^{}]*\}|\\overset\{[^{}]*def[^{}]*\}|=:|\\equiv")
DEF_GUARDED_OPS = {"sign_flip", "const_change", "index_shift", "sum_bound_shift", "setop_swap", "limop_swap"}
CLAIM_GUARDED_OPS = {"hypothesis_drop", "hypothesis_swap"}


def _defines_here(step, s):
    """True when the site sits inside a defining math span (':=' etc.) - changing a definition is a choice, not an error."""
    for a, b in math_spans(step):
        if a <= s < b:
            return DEF_MARK.search(step[a:b]) is not None
    return False


def _claim_grants(removed, claim):
    """The hypothesis-drop trap (2026-08-17): a hypothesis the claim states is in force whatever a step says, so dropping
    or weakening its re-citation leaves a derivation that still holds. Skip when the removed word (or its head, for
    'uniformly X' / 'X continuous' phrases) occurs in the claim."""
    r = (removed or "").strip().lower()
    if not r:
        return False
    c = " " + re.sub(r"\s+", " ", (claim or "").lower()) + " "
    heads = {r}
    parts = r.replace("-", " ").split()
    if parts:
        heads.add(parts[0])
        heads.add(parts[-1])
    for h in heads:
        if len(h) >= 4 and re.search(r"(?<![a-z])" + re.escape(h) + r"(?![a-z])", c):
            return True
    return False


POS_NOTATION = re.compile(r"\\ge(?:q|qslant)?\s*0|>\s*0|_\{?\+\}?|\\mathbb\{R\}_|\\R_|\\mathbb\{R\}\^\{?\+|\[0,\s*\\infty|\(0,\s*\\infty")


BACKREF = re.compile(r"(?:\b(?:this|that|these|those|such an?|the same|the above|the latter|the former|said)\s+)$", re.I)
LOGIC_WORDS = {"recursive", "computable", "decidable", "definable", "consistent", "recursively", "primitive"}
LOGIC_NOUN = re.compile(r"\s+(?:set|sets|function|functions|predicate|predicates|subset|subsets|language|languages|theory|theories|"
                        r"ordinal|ordinals|real|reals|structure|structures|model|models|relation|relations|sequence|sequences|"
                        r"enumeration|tree|trees|degree|degrees|formula|formulas)\b")


def _site_is_backref(step, s, removed):
    """(a) 'this centered polynomial' re-cites an established object; (b) a logic word outside a logic noun phrase
    ('the recursive step' = induction) is not a computability hypothesis; (c) 'bounded on H' is operator boundedness;
    (d) 'centered A_t' with 'A_t - E[A_t]' in the formula that follows is redundant. (2026-09-06 second hand-read)"""
    r = (removed or "").strip().lower()
    head = r.split()[0] if r else ""
    if BACKREF.search(step[max(0, s - 14):s]):
        return True
    if head.rstrip("-").replace("non", "") in LOGIC_WORDS or head in LOGIC_WORDS:
        if not LOGIC_NOUN.match(step[s + len(removed.rstrip()):]):
            return True
    if head == "bounded" and re.match(r"\s*(?:on|from|by|in\s+norm|as an? operator)\b", step[s + len(removed.rstrip()):]):
        return True
    if head == "centered" and re.search(r"-\s*\\(?:E|mathbb\{E\}|mathbf\{E\}|operatorname\{E\})", step[s:s + 160]):
        return True
    return False


BOUNDED_NOUNS = re.compile(r"^\s*(?:coordinate\s+|closed\s+|open\s+|unit\s+|small\s+)?(?:box|boxes|ball|balls|interval|intervals|cube|cubes|"
                           r"rectangle|rectangles|disc|discs|disk|disks|annulus|annuli|polytope|polytopes|simplex|simplices|"
                           r"sphere|spheres|circle|circles|torus|tori|segment|segments|cell|cells)\b")
COMPOUND_FIELD = re.compile(r"(?:residue|number|function|finite|splitting|vector|scalar|local|global|class|ground|base|"
                            r"quotient|fraction|prime|closed|algebraically closed|perfect|totally real|cyclotomic)\s+$", re.I)


def _site_is_phrase(step, s, e, removed, inserted):
    """(a) antonym coordination, (b) compact->closed on a bounded-by-name set, (c) a compound noun ending in 'field'
    (2026-09-06 third hand-read, real multi-domain items)."""
    r = (removed or "").strip().lower()
    head = r.split()[0] if r else ""
    after = step[e:e + 40]
    before = step[max(0, s - 40):s]
    m = re.match(r"\s*(?:and|or|,)\s+([a-z-]+)", after) or (
        re.match(r"\s*([a-z-]+)", after) if r.endswith(("and", ",")) else None)
    if m and WORDS_DIR.get(head) == m.group(1):
        return True
    m = re.search(r"([a-z-]+)\s+(?:and|or)\s+$", before)
    if m and WORDS_DIR.get(head) == m.group(1):
        return True
    if head == "compact" and (inserted or "").strip().lower() in ("closed", "bounded") and BOUNDED_NOUNS.match(step[s + len(removed.rstrip()):]):
        return True
    if head == "field" and COMPOUND_FIELD.search(before):
        return True
    return False


def _notation_grants(removed, after):
    """The hypothesis the notation right after the site already states (2026-09-06 hand-read)."""
    r = (removed or "").strip().lower()
    head = r.split()[0] if r else ""
    if head in ("positive", "nonnegative", "non-negative") and POS_NOTATION.search(after):
        return True
    if head == "finite" and re.search(r"(?<![a-z])finite(?![a-z])", after.lower()):
        return True
    return False


def candidates(steps, claim="", ops=None, domain_group=None):
    """[(op, step_index, start, end, replacement)] over all steps, minus restating steps, definitional sites, hypotheses the
    claim already grants, and invalid references. domain_group gates the field-ambiguous hypothesis words."""
    if domain_group is not None:
        set_domain(domain_group)
    out = []
    skip = {i for i, st in enumerate(steps) if claim and restates_claim(st, claim)}
    for name, mech, tax, tier, need_math, fn in OPS:
        if ops and name not in ops:
            continue
        for i, st in enumerate(steps):
            if i in skip:
                continue
            if name in DEF_GUARDED_OPS and DEFINITIONAL_START.match(st):
                continue
            try:
                for s, e, rep in fn(st):
                    if st[s:e] == rep:
                        continue
                    if name in DEF_GUARDED_OPS and _defines_here(st, s):
                        continue
                    if name in CLAIM_GUARDED_OPS and _claim_grants(st[s:e], (claim or "") + " " + " ".join(steps[:i])):
                        continue   # 2026-09-06 hand-read: 'this finite vector' (finite by construction two steps up) is a re-citation
                    if name in CLAIM_GUARDED_OPS and _notation_grants(st[s:e], st[e:e + 90]):
                        continue   # 'measurable non-negative f: R^2 -> R_{>=0}' - the codomain says it
                    if name in CLAIM_GUARDED_OPS and _site_is_backref(st, s, st[s:e]):
                        continue
                    if name in CLAIM_GUARDED_OPS and _site_is_phrase(st, s, e, st[s:e], rep):
                        continue
                    if need_math and _defines_here(st, s) and name in ("ineq_flip", "ineq_to_eq"):
                        continue
                    c = (name, i, s, e, rep)
                    if not find_context_ok(c, steps):
                        continue
                    out.append(c)
            except Exception:
                continue
    return out


def apply(steps, cand):
    name, i, s, e, rep = cand
    st = steps[i]
    new = st[:s] + rep + st[e:]
    new = re.sub(r"  +", " ", new)
    new = re.sub(r" ([,;.])(?=\s|$)", r"\1", new)   # a removed trailing word leaves no space before its comma
    out = list(steps)
    out[i] = new
    removed, inserted = st[s:e], rep
    mut_hash = hashlib.sha256(("%s|%d|%d|%d|%s|%s" % (name, i + 1, s, e, removed, inserted)).encode("utf-8")).hexdigest()
    score, label = difficulty(name, i, len(steps), removed, steps)
    return out, {"op": name, "mechanism": OP_INDEX[name][1], "taxonomy": OP_INDEX[name][2], "tier": OP_INDEX[name][3],
                 "step": i + 1, "start": s, "end": e,
                 "before": st[max(0, s - 40):e + 40], "after": new[max(0, s - 40):s + len(rep) + 40],
                 "removed": removed, "inserted": inserted, "mutation_sha256": mut_hash,
                 "difficulty_score": score, "difficulty": label}


def choose(steps, rng, claim="", n=2, exclude_ops=(), tier_first=True, avoid_steps=()):
    cands = [c for c in candidates(steps, claim) if c[0] not in exclude_ops and (c[1] + 1) not in avoid_steps]
    if not cands:
        return []
    rng.shuffle(cands)
    if tier_first:
        cands.sort(key=lambda c: 0 if OP_INDEX[c[0]][3] == "A" else 1)
    picked, used_steps, used_ops = [], set(), set()
    for c in cands:
        if c[1] in used_steps or c[0] in used_ops:
            continue
        picked.append(c)
        used_steps.add(c[1])
        used_ops.add(c[0])
        if len(picked) >= n:
            break
    return picked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", required=True)
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--op", default="")
    a = ap.parse_args()
    rows = [json.loads(l) for l in io.open(a.demo, encoding="utf-8") if l.strip()]
    rows = [r for r in rows if r.get("accept")]
    rng = random.Random(a.seed)
    rng.shuffle(rows)
    shown = 0
    for r in rows:
        cands = candidates(r["steps"], r.get("statement", ""), ops=[a.op] if a.op else None)
        if not cands:
            continue
        c = rng.choice(cands)
        new, info = apply(r["steps"], c)
        print("=====", r["paper"], r.get("domain_group"), r["kind"], "step", info["step"], "of", r["n_steps"], "|", info["op"],
              info["taxonomy"], info["tier"], info["difficulty"])
        print("  BEFORE:", info["before"].replace("\n", " "))
        print("  AFTER :", info["after"].replace("\n", " "))
        shown += 1
        if shown >= a.n:
            break


if __name__ == "__main__":
    main()
