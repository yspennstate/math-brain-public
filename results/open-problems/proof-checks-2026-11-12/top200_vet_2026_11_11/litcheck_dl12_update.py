"""Replace the verdict of the 12 DL rows of LITCHECK.tsv that read 'not yet read against the paper', after reading
the arXiv abstracts in full (dl12_abs_full.out, 11 Nov 2026).  The theorem statements were not read."""
A = "abstract read in full 2026-11-11, an agent"
V = {
 "T253": "CONFIRMED_ABSTRACT: 2205.10217 lower-bounds the smallest NTK eigenvalue with about N parameters and sqrt(N) neurons; 2007.12826 gives lambda_min bounded away from 0 once Nd >> n. The restatement to the sharp constant stands",
 "T261": "CONFIRMED_ABSTRACT: sharp test-error asymptotics for p/d^k1, n/d^k2 constant, all k1, k2 > 0, covariates on the sphere, double descent at n = p. Sphere only; other input laws are what is left",
 "T283": "CONFIRMED_ABSTRACT: Hopkins' conjecture disproved (vanishing degree n^(1-O(eps)) advantage, yet a noise-tolerant distinguisher in time n^(O(log^(1/(k-1)) n))); second construction with a non-product null",
 "T284": "CONFIRMED_ABSTRACT: shortest s-t path has the overlap gap property in sparse G(n,p) and with exponential weights, and is solved by O(log n)-degree polynomials; uniform approximate sampling in polynomial time",
 "T292": "CONFIRMED_ABSTRACT: first polynomial-time learner for constant k with no assumption on signs or conditioning",
 "T305": "CONFIRMED_ABSTRACT: gradient complexity d^(1/4) polylog(1/eps) up to logs from a warm start, for smooth log-densities with Frobenius-Lipschitz Hessian and isoperimetry",
 "T310": "CONFIRMED_ABSTRACT: KSD rate 1/sqrt(N) in continuous and discrete time, polynomial in d under assumptions on kernel and potential; Wasserstein-2 only with a bilinear kernel component and with a curse of dimensionality",
 "T314": "CONFIRMED_ABSTRACT: polynomial-time sampling with o(1) total-variation error at every beta < 1; v1, unrefereed. Removal stands as REPORTED",
 "T350": "CONFIRMED_ABSTRACT: online SGD, even activation of information exponent k* > 2, orthonormal directions, power-law second layer: sharp transition times and scaling-law exponents",
 "T361": "CONFIRMED_ABSTRACT: same paper as T350 (sharp per-direction transitions adding up to a smooth power law)",
 "T352": "PARTLY_CONFIRMED: the abstract gives privacy guarantees for noisy GRADIENT DESCENT on non-convex problems; the row is about hidden-state noisy SGD. Theorem 3.3 not read here. Whether minibatch SGD is covered (a follow-up of the same authors treats stochastic gradients, from memory) should be checked before the row is removed",
 "T377": "CONFIRMED_ABSTRACT: 2503.02877 proves weak-to-strong generalization for random-feature teacher and student with its quantitative limit; 2610.09044 gives the quadratic improvement under a Gaussian universality assumption (ReLU, one spherical harmonic)",
}
with open("LITCHECK.tsv", encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
n = 0
for i, l in enumerate(lines):
    p = l.split("\t")
    if p and p[0] in V and len(p) >= 5:
        p[4] = V[p[0]] + " (" + A + ")"
        lines[i] = "\t".join(p); n += 1
with open("LITCHECK.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
print("rows updated:", n)
