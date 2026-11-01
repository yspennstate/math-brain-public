"""Wikipedia REST-summary harvester -> concept-node draft bundles (.part gated).

Fetches lead-paragraph extracts for a curated list of named mathematical
results and notions via the Wikipedia REST API (designed for programmatic
access; real User-Agent; ~1 req/s). Every harvested entry enters as kind
CONCEPT: a lead paragraph describes a result faithfully but rarely states it
with complete hypotheses, and the population doctrine is that the
under-hypothesized false statement is worse than the honest description.
Authored lanes supply precise theorem/definition versions; dedupe is by
logical_name, and harvested concepts deliberately use a wiki- prefix so they
never collide with authored precise nodes. Output is .part until sampled.
"""

from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
import urllib.request

import wiki_formulas  # the lead with its formulas kept (tools/wiki_formulas.py)

API = "https://en.wikipedia.org/api/rest_v1/page/summary/"
UA = "math-brain-population/1.0 (local research corpus; polite rate with backoff)"
RATE_S = 2.2
MAX_RETRIES = 3
# the inbox beside this repository (or MATH_BRAIN_INBOX)
_INBOX = os.environ.get("MATH_BRAIN_INBOX") or os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "math-brain-inbox")
OUT_DIR = os.path.join(_INBOX, "wikipedia-harvester")
MAX_STATEMENT = 1200
MIN_STATEMENT = 80

PAGES = [
    # the owner's research areas, as the B12 research bank tests them (added 2026-09-02 after the
    # bank's brain arm was found serving notes with zero store coverage for nine of its families)
    "Marchenko–Pastur distribution", "Wigner semicircle distribution", "Wigner surmise",
    "Poincaré separation theorem", "Cauchy interlacing theorem", "Weyl's inequality",
    "Matrix Chernoff bound", "Operator norm", "Singular value", "Random matrix",
    "Littlewood–Offord problem", "Sperner's theorem", "Khintchine inequality",
    "Hoeffding's inequality", "Azuma's inequality", "McDiarmid's inequality",
    "Paley–Zygmund inequality", "Efron-Stein inequality", "Concentration inequality",
    "Harris inequality", "FKG inequality", "Russo–Margulis formula", "Percolation theory",
    "First passage percolation", "Self-avoiding walk", "Connective constant",
    "Subadditivity", "Fekete's lemma", "Peierls argument", "Griffiths inequality",
    "Cover's theorem", "Hopfield network", "Perceptron", "Gardner problem",
    "VC dimension", "Radon's theorem", "Rademacher complexity", "Sauer–Shelah lemma",
    "Graeco-Latin square", "Mutually orthogonal Latin squares", "Latin square",
    "Hall's marriage theorem", "Ramsey's theorem", "Probabilistic method",
    "Erdős–Rényi model", "Random graph", "Expander graph", "Expander mixing lemma",
    "Cheeger constant (graph theory)", "Alon–Boppana bound", "Spectral gap",
    "Mixing time of Markov chains", "Markov chain mixing time", "PageRank", "Power iteration",
    "Kirchhoff's theorem", "Laplacian matrix", "Barabási–Albert model",
    "Preferential attachment", "Scale-free network", "Edge of chaos",
    # analysis
    "Intermediate value theorem", "Mean value theorem", "Taylor's theorem",
    "Fundamental theorem of calculus", "Bolzano\u2013Weierstrass theorem",
    "Heine\u2013Borel theorem", "Banach fixed-point theorem", "Baire category theorem",
    "Arzel\u00e0\u2013Ascoli theorem", "Stone\u2013Weierstrass theorem",
    "Hahn\u2013Banach theorem", "Open mapping theorem (functional analysis)",
    "Closed graph theorem", "Uniform boundedness principle", "Banach\u2013Alaoglu theorem",
    "Riesz representation theorem", "Spectral theorem", "Parseval's theorem",
    "Fourier inversion theorem", "Plancherel theorem", "Weierstrass approximation theorem",
    "Dominated convergence theorem", "Monotone convergence theorem", "Fatou's lemma",
    "Fubini's theorem", "Radon\u2013Nikodym theorem", "Egorov's theorem", "Lusin's theorem",
    "Vitali covering lemma", "Lebesgue differentiation theorem", "Riesz\u2013Fischer theorem",
    "H\u00f6lder's inequality", "Minkowski inequality", "Young's convolution inequality",
    "Gr\u00f6nwall's inequality", "Picard\u2013Lindel\u00f6f theorem", "Peano existence theorem",
    "Implicit function theorem", "Inverse function theorem", "Sard's theorem",
    "Green's theorem", "Stokes' theorem", "Divergence theorem",
    "Cauchy's integral theorem", "Cauchy's integral formula", "Residue theorem",
    "Liouville's theorem (complex analysis)", "Maximum modulus principle",
    "Riemann mapping theorem", "Rouch\u00e9's theorem", "Schwarz lemma",
    "Morera's theorem", "Casorati\u2013Weierstrass theorem", "Picard theorem",
    # algebra
    "Lagrange's theorem (group theory)", "Sylow theorems", "Cayley's theorem",
    "Isomorphism theorems", "Jordan\u2013H\u00f6lder theorem", "Classification of finite simple groups",
    "Fundamental theorem of finitely generated abelian groups", "Burnside's lemma",
    "Orbit-stabilizer theorem", "Cauchy's theorem (group theory)",
    "Chinese remainder theorem", "Fundamental theorem of algebra",
    "Fundamental theorem of Galois theory", "Abel\u2013Ruffini theorem",
    "Hilbert's Nullstellensatz", "Hilbert's basis theorem", "Nakayama's lemma",
    "Cayley\u2013Hamilton theorem", "Jordan normal form", "Rank\u2013nullity theorem",
    "Smith normal form", "Perron\u2013Frobenius theorem", "Courant\u2013Fischer theorem",
    "Eckart\u2013Young theorem", "Gershgorin circle theorem",
    # number theory
    "Fermat's little theorem", "Euler's theorem", "Wilson's theorem",
    "Quadratic reciprocity", "Prime number theorem", "Dirichlet's theorem on arithmetic progressions",
    "Bertrand's postulate", "Chebyshev's theorem", "Fermat's Last Theorem",
    "Lagrange's four-square theorem", "Sum of two squares theorem",
    "Mordell\u2013Weil theorem", "Hasse\u2013Minkowski theorem", "Chevalley\u2013Warning theorem",
    "Hensel's lemma", "Riemann hypothesis", "Goldbach's conjecture", "Twin prime conjecture",
    "Green\u2013Tao theorem", "Szemer\u00e9di's theorem",
    # combinatorics + graph theory
    "Pigeonhole principle", "Inclusion\u2013exclusion principle", "Ramsey's theorem",
    "Hall's marriage theorem", "K\u00f6nig's theorem (graph theory)", "Menger's theorem",
    "Max-flow min-cut theorem", "Tur\u00e1n's theorem", "Erd\u0151s\u2013Ko\u2013Rado theorem",
    "Sperner's theorem", "Dilworth's theorem", "Four color theorem",
    "Kuratowski's theorem", "Euler's formula", "Handshaking lemma",
    "Cayley's formula", "Matrix tree theorem", "Lov\u00e1sz local lemma",
    "Szemer\u00e9di regularity lemma", "Five color theorem",
    # probability + statistics
    "Law of large numbers", "Central limit theorem", "Berry\u2013Esseen theorem",
    "Borel\u2013Cantelli lemma", "Kolmogorov zero\u2013one law", "Doob's martingale convergence theorems",
    "Optional stopping theorem", "Donsker's theorem", "Glivenko\u2013Cantelli theorem",
    "Cram\u00e9r's theorem (large deviations)", "Sanov's theorem", "Chernoff bound",
    "Azuma's inequality", "Talagrand concentration inequality", "Slutsky's theorem",
    "Bayes' theorem", "De Finetti's theorem", "Birkhoff's ergodic theorem",
    "Perron\u2013Frobenius theorem", "Johnson\u2013Lindenstrauss lemma",
    # topology + geometry
    "Tychonoff theorem", "Urysohn's lemma", "Tietze extension theorem",
    "Brouwer fixed-point theorem", "Borsuk\u2013Ulam theorem", "Jordan curve theorem",
    "Invariance of domain", "Seifert\u2013Van Kampen theorem", "Poincar\u00e9 conjecture",
    "Gauss\u2013Bonnet theorem", "Nash embedding theorems", "Whitney embedding theorem",
    "Hairy ball theorem", "Ham sandwich theorem", "Classification of surfaces",
    "Euler characteristic", "Banach\u2013Tarski paradox", "Isoperimetric inequality",
    # logic + set theory + computation
    "Cantor's theorem", "Cantor's diagonal argument", "Schr\u00f6der\u2013Bernstein theorem",
    "Zorn's lemma", "Well-ordering theorem", "Axiom of choice",
    "Continuum hypothesis", "G\u00f6del's incompleteness theorems", "G\u00f6del's completeness theorem",
    "Compactness theorem", "L\u00f6wenheim\u2013Skolem theorem", "Halting problem",
    "Rice's theorem", "Cook\u2013Levin theorem", "P versus NP problem",
    "Church\u2013Turing thesis", "Curry\u2013Howard correspondence", "Four color theorem",
    # mathematical physics + dynamics + misc named results
    "Noether's theorem", "KAM theorem", "Poincar\u00e9 recurrence theorem",
    "Liouville's theorem (Hamiltonian)", "Sharkovskii's theorem", "Banach\u2013Steinhaus theorem",
    "Krein\u2013Milman theorem", "Choquet theory", "Farkas' lemma",
    "Minimax theorem", "Nash equilibrium", "Arrow's impossibility theorem",
    "Brouwer degree", "Sperner's lemma", "Knaster\u2013Tarski theorem",
    "Kakutani fixed-point theorem", "Birkhoff\u2013von Neumann theorem", "Hall's theorem",
    "Wigner semicircle distribution", "Marchenko\u2013Pastur distribution", "Tracy\u2013Widom distribution",
    "Universal approximation theorem", "Vapnik\u2013Chervonenkis dimension", "No free lunch theorem",
    # extension batch 3: more analysis
    "Lebesgue integral", "Riemann integral", "Measure (mathematics)", "Sigma-algebra",
    "Borel set", "Cantor set", "Cantor function", "Dirichlet function",
    "Uniform continuity", "Absolute continuity", "Bounded variation", "Lipschitz continuity",
    "Convex function", "Jensen's inequality", "H\u00f6lder's inequality", "Cauchy\u2013Schwarz inequality",
    "AM\u2013GM inequality", "Rearrangement inequality", "Chebyshev's inequality",
    "Markov's inequality", "Fatou\u2013Lebesgue theorem", "Beppo Levi theorem",
    "Riemann series theorem", "Abel's theorem", "Dirichlet's test", "Alternating series test",
    "Ratio test", "Root test", "Weierstrass M-test", "Dini's theorem",
    "Ascoli\u2013Arzel\u00e0 theorem", "Sobolev space", "Poincar\u00e9 inequality", "Rellich\u2013Kondrachov theorem",
    "Lax\u2013Milgram theorem", "Spectral radius", "Gelfand's formula", "Fredholm alternative",
    "Compact operator", "Trace class", "Polar decomposition", "Riesz projection",
    # extension: more algebra and linear algebra
    "Group action", "Class equation", "Semidirect product", "Free group",
    "Presentation of a group", "Nilpotent group", "Solvable group", "Simple group",
    "Module (mathematics)", "Tensor product", "Exact sequence", "Snake lemma",
    "Five lemma", "Schur's lemma", "Wedderburn\u2013Artin theorem", "Artin\u2013Wedderburn theorem",
    "Noetherian ring", "Krull dimension", "Localization (commutative algebra)", "Integral extension",
    "Going up and going down", "Dedekind domain", "Discrete valuation ring",
    "Eigendecomposition of a matrix", "Singular value decomposition", "QR decomposition",
    "LU decomposition", "Cholesky decomposition", "Gram\u2013Schmidt process",
    "Moore\u2013Penrose inverse", "Matrix exponential", "Sylvester's law of inertia",
    "Courant minimax principle", "Weyl's inequality", "Hoffman\u2013Wielandt inequality",
    # extension: more probability and statistics
    "Martingale (probability theory)", "Stopping time", "Brownian motion", "Wiener process",
    "Ito's lemma", "Stochastic differential equation", "Fokker\u2013Planck equation",
    "Kolmogorov extension theorem", "Kolmogorov continuity theorem", "L\u00e9vy process",
    "Poisson process", "Markov chain", "Ergodic theory", "Mixing (mathematics)",
    "Coupling (probability)", "Total variation distance", "Wasserstein metric",
    "Kullback\u2013Leibler divergence", "Entropy (information theory)", "Mutual information",
    "Fisher information", "Cram\u00e9r\u2013Rao bound", "Maximum likelihood estimation",
    "Bayesian inference", "Hoeffding's inequality", "Bernstein inequalities (probability theory)",
    "Efron\u2013Stein inequality", "Log-Sobolev inequality", "Concentration of measure",
    "Gaussian process", "Random walk", "Galton\u2013Watson process", "Percolation theory",
    # extension: geometry, topology, dynamics
    "Metric space", "Complete metric space", "Compact space", "Connected space",
    "Quotient space (topology)", "Product topology", "Covering space", "Homotopy",
    "Homology (mathematics)", "Cohomology", "De Rham cohomology", "Betti number",
    "Morse theory", "Riemannian manifold", "Geodesic", "Sectional curvature",
    "Ricci curvature", "Laplace\u2013Beltrami operator", "Hodge theory", "Chern class",
    "Symplectic geometry", "Hamiltonian mechanics", "Lyapunov exponent", "Chaos theory",
    "Attractor", "Bifurcation theory", "Feigenbaum constants", "Mandelbrot set",
    "Julia set", "Rotation number", "Anosov diffeomorphism", "Arnold diffusion",
    # extension: logic, computation, discrete
    "Peano axioms", "First-order logic", "Model theory", "Proof theory",
    "Lambda calculus", "Type theory", "Set theory", "Forcing (mathematics)",
    "Large cardinal", "Constructible universe", "Recursion theorem", "Kleene's recursion theorem",
    "Busy beaver", "Kolmogorov complexity", "NP-completeness", "Polynomial hierarchy",
    "PSPACE", "BPP (complexity)", "Interactive proof system", "PCP theorem",
    "Expander graph", "Spectral graph theory", "Cheeger constant", "Random graph",
    "Erd\u0151s\u2013R\u00e9nyi model", "Small-world network", "Graph coloring", "Chromatic polynomial",
    "Matroid", "Latin square", "Block design", "Steiner system",
    "Error correcting code", "Hamming code", "Reed\u2013Solomon error correction", "Shannon's source coding theorem",
    "Noisy-channel coding theorem", "Fast Fourier transform", "Convolution theorem", "Nyquist\u2013Shannon sampling theorem",
    # batch 5: special functions and classical analysis
    "Gamma function", "Beta function", "Riemann zeta function", "Dirichlet series",
    "Bessel function", "Legendre polynomials", "Hermite polynomials", "Chebyshev polynomials",
    "Orthogonal polynomials", "Hypergeometric function", "Elliptic integral", "Elliptic function",
    "Weierstrass elliptic function", "Theta function", "Modular form", "Eisenstein series",
    "Stirling's approximation", "Euler\u2013Maclaurin formula", "Laplace's method", "Stationary phase approximation",
    "Watson's lemma", "Mellin transform", "Laplace transform", "Z-transform",
    "Poisson summation formula", "Abel summation", "Ces\u00e0ro summation", "Tauberian theorem",
    # batch 5: algebraic geometry and number theory upper floors
    "Algebraic variety", "Affine variety", "Projective variety", "Scheme (mathematics)",
    "Sheaf (mathematics)", "Divisor (algebraic geometry)", "Riemann\u2013Roch theorem", "Bezout's theorem",
    "Elliptic curve", "Weierstrass equation", "Group law on elliptic curves", "Torsion subgroup",
    "Modularity theorem", "Birch and Swinnerton-Dyer conjecture", "Weil conjectures", "Zeta function of a variety",
    "Class field theory", "Ideal class group", "Dirichlet unit theorem", "Minkowski's theorem",
    "Geometry of numbers", "p-adic number", "Ostrowski's theorem", "Local field",
    "Galois cohomology", "Kummer theory", "Cyclotomic field", "Fermat's theorem on sums of two squares",
    # batch 5: Millennium and Hilbert class problems
    "Millennium Prize Problems", "P versus NP problem", "Hodge conjecture", "Navier\u2013Stokes existence and smoothness",
    "Yang\u2013Mills existence and mass gap", "Hilbert's problems", "Hilbert's tenth problem", "Matiyasevich's theorem",
    "Continuum hypothesis", "Collatz conjecture", "ABC conjecture", "Erd\u0151s\u2013Straus conjecture",
    "Invariant subspace problem", "Kakeya set", "Falconer's conjecture", "Union-closed sets conjecture",
    # batch 5: statistics and stochastic upper floors
    "Gauss\u2013Markov theorem", "Central limit theorem for martingales", "Law of the iterated logarithm",
    "Large deviations theory", "Varadhan's lemma", "Girsanov theorem", "Feynman\u2013Kac formula",
    "Kalman filter", "Metropolis\u2013Hastings algorithm", "Gibbs sampling", "Markov chain Monte Carlo",
    "Bootstrapping (statistics)", "Delta method", "Fisher\u2013Neyman factorization theorem", "Rao\u2013Blackwell theorem",
    "Lehmann\u2013Scheff\u00e9 theorem", "Neyman\u2013Pearson lemma", "Wilks' theorem", "Stein's paradox",
    "James\u2013Stein estimator", "Empirical Bayes method", "De Moivre\u2013Laplace theorem", "Lindeberg condition",
    # batch 5: more geometry/topology/dynamics
    "Poincar\u00e9\u2013Bendixson theorem", "Hartman\u2013Grobman theorem", "Stable manifold theorem", "Center manifold",
    "Smale horseshoe", "Ergodic hypothesis", "Birkhoff ergodic theorem", "Oseledets theorem",
    "Gromov's theorem on groups of polynomial growth", "Banach\u2013Mazur theorem", "Borsuk's conjecture",
    "Systolic geometry", "Myers's theorem", "Hopf\u2013Rinow theorem", "Cartan\u2013Hadamard theorem",
    "Bishop\u2013Gromov inequality", "Cheeger's inequality", "Weyl law", "Can one hear the shape of a drum?",
    # batch 5: computation and logic upper floors
    "Time hierarchy theorem", "Space hierarchy theorem", "Savitch's theorem", "Immerman\u2013Szelepcs\u00e9nyi theorem",
    "Ladner's theorem", "Blum's speedup theorem", "Kleene's recursion theorem", "Post's theorem",
    "Turing degree", "Arithmetical hierarchy", "Analytical hierarchy", "Reverse mathematics",
    "Goodstein's theorem", "Paris\u2013Harrington theorem", "Kruskal's tree theorem", "Robertson\u2013Seymour theorem",
    "Graph minor theorem", "Courcelle's theorem", "Zero-knowledge proof", "Probabilistically checkable proof",
]


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return ("wiki-" + slug)[:80]


def fetch_summary(title: str):
    url = API + urllib.parse.quote(title.replace(" ", "_"), safe="")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < MAX_RETRIES:
                try:
                    wait = float(exc.headers.get("Retry-After", "30"))
                except (TypeError, ValueError):
                    wait = 30.0
                time.sleep(min(wait, 120.0) + 2.0)
                continue
            return {"_error": f"HTTPError: {exc.code}"}
        except Exception as exc:  # noqa: BLE001
            return {"_error": f"{type(exc).__name__}: {exc}"}
    return {"_error": "retries-exhausted"}


def already_harvested() -> set[str]:
    import glob

    done: set[str] = set()
    for path in glob.glob(OUT_DIR + r"\*.json") + glob.glob(OUT_DIR + r"\*.part"):
        try:
            data = json.load(open(path, encoding="utf-8"))
            done.update(e["logical_name"] for e in data.get("entries", []))
        except Exception:  # noqa: BLE001
            continue
    return done


def main() -> int:
    import os

    os.makedirs(OUT_DIR, exist_ok=True)
    entries = []
    skipped = []
    seen = set()
    done = already_harvested()
    existing_batches = len(
        [p for p in os.listdir(OUT_DIR) if p.endswith((".json", ".part"))]
    )
    for title in PAGES:
        if slugify(title) in done:
            continue
        if title in seen:
            continue
        seen.add(title)
        time.sleep(RATE_S)
        data = fetch_summary(title)
        if "_error" in data:
            skipped.append((title, data["_error"][:80]))
            continue
        if data.get("type") == "disambiguation":
            skipped.append((title, "disambiguation"))
            continue
        extract = re.sub(r"\s+", " ", (data.get("extract") or "")).strip()
        if len(extract) < MIN_STATEMENT:
            skipped.append((title, "extract-too-short"))
            continue
        page_title = data.get("title") or title
        # The summary's extract drops every formula and closes the gap ("states that if is a continuous function"):
        # 76 of 443 harvested cards had lost the theorem itself (repaired 2026-09-23). Keep the formulas when the
        # parse-API lead matches the extract and every guard in wiki_formulas.formula_lead passes; otherwise keep
        # the extract as before. Either way the revision read is recorded.
        time.sleep(RATE_S)
        # the summary and the parse lead are read from the same revision, so a lower overlap is additions (the summary
        # strips parentheticals: "(commonly referred to as PIE)"), not drift; the dropped-word and leading-formula guards
        # inside formula_lead still refuse anything that loses or prepends text
        kept, revid, why = wiki_formulas.formula_lead(page_title, extract, min_overlap=0.7)
        revision = "rest-summary-%s" % time.strftime("%Y-%m-%d")
        if kept:
            extract, revision = kept, "parse-lead-rev-%s" % revid
        if len(extract) > MAX_STATEMENT:
            trimmed, end = None, MAX_STATEMENT
            while trimmed is None:
                cut = extract.rfind(". ", 0, end)
                candidate = extract[: cut + 1] if cut > MIN_STATEMENT else extract[:MAX_STATEMENT]
                if not kept or wiki_formulas.tex_ok(candidate) or cut <= MIN_STATEMENT:
                    trimmed = candidate
                end = cut
            if kept and not wiki_formulas.tex_ok(trimmed):
                skipped.append((title, "trim-cuts-a-formula"))
                continue
            extract = trimmed
        page_url = (data.get("content_urls", {}).get("desktop", {}) or {}).get(
            "page", "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))
        )
        entries.append(
            {
                "key": slugify(title)[:60],
                "namespace": "harvest.wikipedia",
                "logical_name": slugify(title),
                "kind": "concept",
                "title": page_title,
                "statement": extract,
                "proof_text": None,
                "assumptions": [],
                "domain": "harvested overview (Wikipedia lead)",
                "source": {
                    "source_id": f"wikipedia:{page_title}",
                    "url": page_url,
                    "revision": revision,
                    "license": "CC-BY-SA-4.0",
                    "excerpt": None,
                },
            }
        )
        print(f"OK   {title} ({len(extract)} chars; {why})")
    for start in range(0, len(entries), 180):
        chunk = entries[start : start + 180]
        n = existing_batches + start // 180 + 1
        draft = {
            "spec": "mathbrain-draft-v1",
            "author_agent": "wikipedia-harvester",
            "bundle_slug": f"wikipedia-harvest-{n:03d}",
            "entries": chunk,
            "relations": [],
        }
        out_path = f"{OUT_DIR}\\bundle_{n:03d}.part"
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(draft, fh, indent=1)
        print(f"wrote {out_path}: {len(chunk)} entries")
    print(f"total {len(entries)} harvested, {len(skipped)} skipped")
    for title, why in skipped[:20]:
        print(f"SKIP {title}: {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
