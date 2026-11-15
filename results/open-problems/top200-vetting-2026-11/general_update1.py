"""Write GENERAL_LITCHECK.tsv and update the flagged TOP200_GENERAL rows of DESERVE.tsv and rows T382, T243 of
STATEMENT_PASS.tsv, after reading the arXiv abstracts in general_lit.out (11 Nov 2026)."""
CHK = "2026-11-11 abstracts read on arXiv, an agent"

G = {
 "CO12": ("REPLACE_DISPROVED", "5",
          "DISPROVED in May 2026: an OpenAI model produced a counterexample to the conjectured n^(1+o(1)) bound and five "
          "mathematicians published a human-verified version the same day (so reported in arXiv 2608.28997 and 2607.20525; "
          "follow-up Lee-Pohoata-Zhu 2607.05374). The primary paper was not read. Replace the row, or restate it as the "
          "true exponent of the largest number of unit distances."),
 "AG10": ("REPORTED_SOLVED", "5",
          "irrationality of the very general cubic fourfold: proof posted by Katzarkov-Kontsevich-Pantev-Yu in 2025 (memory; "
          "their atoms are used in Guere 2610.40811), and OpenAI work on very general members of Hassett divisors is cited "
          "there. Primary papers not read; unrefereed as far as checked. Replace unless the row is kept as REPORTED."),
 "PD08": ("REPORTED_SOLVED", "5",
          "Hou-Wang-Yang (arXiv 2509.25116v2) give a computer-assisted proof of non-uniqueness of Leray-Hopf solutions of "
          "the unforced 3D equations. Unrefereed as far as checked; replace unless kept as REPORTED."),
 "GE07": ("REPORTED_SOLVED", "3",
          "Baek (arXiv 2411.19826v1, Nov 2024) proves that Gerver's sofa is optimal. Refereeing status not checked."),
 "PD14": ("REPLACE_OR_RESTATE", "5",
          "global regularity is false in the cases treated: blow-up from smooth data for defocusing supercritical "
          "Schroedinger with (d,p) = (3,27), (4,9), (5,7) (Buck-Carballeira-Gomez-Serrano-Shi 2609.23685, computer-assisted) "
          "and for the real-valued defocusing wave equation with p = 3, d >= 9; p = 5, d >= 7; p = 7, d >= 6 "
          "(Cadiot-Ionescu-Palasek 2610.06678v3). What is open is the low powers in low dimension; state those."),
}
EXTRA = [
 ("-", "Erdos-Szemeredi sum-product conjecture over R", "reported disproved in 2026 (arXiv 2607.20525 abstract); not on our lists, no action"),
 ("PD01", "Navier-Stokes regularity", "arXiv 2609.18808v2 (one author, 'a very short proof') claims global regularity; not credible "
          "without a check, no change to the row"),
 ("-", "candidates not on any list", "Chowla's conjecture, Leopoldt's conjecture, the lonely runner conjecture, infinitely many real "
       "quadratic fields of class number one: none appears in DESERVE.tsv; possible replacements for the rows above"),
]

with open("DESERVE.tsv", encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
out = ["id\ttitle\tfinding\tchecked"]
n = 0
for i, l in enumerate(lines):
    p = l.split("\t")
    if len(p) == 7 and p[1] == "TOP200_GENERAL" and p[0] in G:
        v, s, r = G[p[0]]
        lines[i] = "\t".join([p[0], p[1], p[2], s, v, r, CHK]); n += 1
        out.append("\t".join([p[0], p[2], v + ": " + r, CHK]))
for k, t, r in EXTRA:
    out.append("\t".join([k, t, r, CHK]))
with open("DESERVE.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
with open("GENERAL_LITCHECK.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(out) + "\n")

U = {
 "T382": ("RESTATE", "planning with a generative model is mapped except at a constant number of actions: under q*-realizability the "
          "query complexity is exponential when the action set is exponentially large (Weisz-Amortila-Szepesvari), and "
          "Weisz-Szepesvari-Gyorgy (arXiv 2110.02195v2) extend the exponential lower bound to few actions [A of order "
          "min(d^(1/4), H^(1/2)), from memory of the part of the abstract not printed], while TensorPlan is polynomial for a "
          "fixed number of actions under v*-realizability. Restate as: with a constant number of actions and stochastic "
          "transitions, is polynomial query complexity possible under q*-realizability alone?", CHK),
 "T243": ("RESTATE", "finite-dimensional rates of order width^(-1/2) in Wasserstein distance are now routine (Agazzi-Mosig Garcia-"
          "Trevisan 2607.06290 for tensor programs; Celli 2601.21539 and Giovagnini-Kotitsas-Romito 2605.02771 for general "
          "weights), and the order 1/n for smooth test functions is in Favaro-Hanin-Marinucci-Nourdin-Peccati. Open: the sharp "
          "rate in a functional metric on C(K) with its dependence on depth; state that.", CHK),
}
with open("STATEMENT_PASS.tsv", encoding="utf-8", newline="") as f:
    sl = f.read().split("\n")
m = 0
for i, l in enumerate(sl):
    p = l.split("\t")
    if p and p[0] in U:
        sl[i] = "\t".join((p[0],) + U[p[0]]); m += 1
with open("STATEMENT_PASS.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(sl))
print("general rows updated:", n, "| litcheck rows:", len(out) - 1, "| statement rows updated:", m)
