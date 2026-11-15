"""Record the arXiv checks of 11 Nov, third batch (general_lit6a.out, general_lit6b.out); note the full Lean check of T104;
extend two memories.  usage: general_update4.py HH:MM"""
import io
import shutil
import sys

stamp = sys.argv[1]
CH = "2026-11-11 abstracts read on arXiv (general_lit6a.out, general_lit6b.out), an agent"
UPD = {
    "NT02": ("REPORTED_SOLVED",
             "reported proved in Oct 2026: a manuscript credited to OpenAI; account with explicit constants arXiv 2610.15483 "
             "(Banks: (1 - beta) log q >= 0.003 for every conductor), simpler proof 2610.21099 (Kerr), elementary proof with "
             "constant 1/100 in 2610.30476 (Guo). Primary source not read. Replace, or keep as REPORTED_SOLVED"),
    "AG05": ("RESTATE",
             "a counterexample in dimension three is reported (Alpoge; arXiv 2609.17795 van den Essen, 2610.24889 de Bondt, "
             "2611.03572 speaks of the conjecture as solved for N >= 3). The two-dimensional case is the open statement "
             "(2610.33919); restate the row to it"),
    "DG02": ("CHECK_STATEMENT",
             "arXiv 2609.11980 (Guo, Fang, Lu, Sep 2026) claims a metric of positive sectional curvature on S^3 x S^3, which "
             "would refute the positive-curvature case; one preprint, found by an automated agent, not confirmed. Read it "
             "before changing the row"),
}
KEEP = {
    "NT09": "no change", "NT10": "no change", "NT12": "no change", "NT13": "no change", "NT19": "no change",
    "NT20": "no change", "NT22": "no change", "NT23": "no change", "NT24": "no change", "NT25": "no change",
    "NT21": "no change",
    "AG04": "no change",
    "AG06": "no change: nonvanishing is shown to imply abundance (arXiv 2610.35913); threefolds in characteristic above 42 "
            "(2610.10439)",
    "AG07": "no change", "AG08": "no change", "AG09": "no change", "AG13": "no change", "AG14": "no change",
    "AL01": "no change: M_23 is now a Galois group over Q, the last sporadic group (arXiv 2608.08538)",
    "AL07": "no change", "AL08": "no change", "AL09": "no change", "AL10": "no change",
    "TO01": "no change", "TO06": "no change", "TO07": "no change", "TO08": "no change", "TO09": "no change",
    "TO11": "no change", "TO12": "no change", "TO14": "no change", "TO04": "no change",
    "DG01": "no change (a positive-curvature metric on S^3 x S^3 is claimed in arXiv 2609.11980; S^2 x S^2 untouched)",
    "DG03": "no change", "DG07": "no change", "DG12": "no change", "DG11": "no change",
}

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
for k, r in enumerate(rows):
    c = r.split("\t")
    if len(c) < 7 or c[1] != "TOP200_GENERAL":
        continue
    if c[0] in UPD:
        seen[c[0]] = c[2]
        c[4], c[5], c[6] = UPD[c[0]][0], UPD[c[0]][1], CH
        rows[k] = "\t".join(c)
    elif c[0] in KEEP:
        seen[c[0]] = c[2]
        c[5] = (c[5] + "; " if c[5] else "") + KEEP[c[0]]
        c[6] = CH
        rows[k] = "\t".join(c)
missing = sorted((set(UPD) | set(KEEP)) - set(seen))
assert not missing, missing
out = nl.join(rows)
assert len(out) > len(s) and out.count(nl) == s.count(nl)
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(out)

p2 = "GENERAL_LITCHECK.tsv"
with io.open(p2, encoding="utf-8", newline="") as f:
    t = f.read()
nl2 = "\r\n" if "\r\n" in t else "\n"
add = ["\t".join([k, seen[k], UPD[k][0] + ": " + UPD[k][1], CH]) for k in UPD]
add.append("\t".join(["-", "rows with no change", ", ".join(sorted(KEEP)) + ": nothing in the newest abstracts settles the row "
                      "(notes per row in DESERVE.tsv)", CH]))
t = t.rstrip("\r\n") + nl2 + nl2.join(add) + nl2
with io.open(p2, "w", encoding="utf-8", newline="") as f:
    f.write(t)

# T104 note and state: the reader's Lean check now covers the whole theorem
D = "~/brain-repo/06_math_research/t104_alon_agent_2026_11_11/"
with io.open(D + "GAP_STATE_FORM.md", encoding="utf-8", newline="") as f:
    g = f.read()
old = "the normalisation paragraph is not formalised)"
assert g.count(old) == 1
gnl = "\r\n" if "\r\n" in g else "\n"
g = g.replace(old, "the whole statement, normalisation included, is" + gnl +
              "`06_math_research/lean_checks_agent/t104_all_n_full`, commit 952215e, theorem T104Full.psi_nonneg)")
with io.open(D + "GAP_STATE_FORM.md", "w", encoding="utf-8", newline="") as f:
    f.write(g)
with io.open(D + "STATE.md", encoding="utf-8", newline="") as f:
    st = f.read()
snl = "\r\n" if "\r\n" in st else "\n"
st = st.rstrip("\r\n") + snl + snl + (
    "11 Nov " + stamp + ". an agent formalised the whole theorem for n >= 14 in Lean, normalisation included "
    "(T104Full.psi_nonneg, lean_checks_agent/t104_all_n_full, commit 952215e, standard axioms).") + snl
with io.open(D + "STATE.md", "w", encoding="utf-8", newline="") as f:
    f.write(st)

# memories
MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m1 = "t104_two_eigenvalue_family_psi_nonneg_all_n_elementary_2026_11_11.md"
with io.open(MD + m1, encoding="utf-8", newline="") as f:
    a = f.read()
anl = "\r\n" if "\r\n" in a else "\n"
assert "t104_all_n_full" not in a
a = a.rstrip("\r\n") + anl + anl + (
    "Later the same day (" + stamp + "): an agent formalised the whole theorem for n >= 14 in Lean, normalisation "
    "included (T104Full.psi_nonneg, 06_math_research/lean_checks_agent/t104_all_n_full, commit 952215e, standard axioms).") + anl
with io.open(MD + m1, "w", encoding="utf-8", newline="") as f:
    f.write(a)
shutil.copyfile(MD + m1, MR + m1)

m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Third batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Third batch, same day (40 rows: number theory, algebraic geometry, algebra, topology, geometry; general_lit6a.out, general_lit6b.out; abstracts only):
- NT02 Landau-Siegel zeros: reported proved absent in Oct 2026 (manuscript credited to OpenAI; arXiv 2610.15483 Banks with explicit constants, 2610.21099 Kerr, 2610.30476 Guo).
- AG05 Jacobian conjecture: counterexample in dimension three reported (Alpoge; arXiv 2609.17795, 2610.24889); dimension two open.
- DG02 Hopf sign conjecture: arXiv 2609.11980 claims positive sectional curvature on S^3 x S^3; one preprint, unconfirmed.
Thirty-seven other rows unchanged. Running count: 87 rows checked by name, 14 changed.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged; T104 note, state and two memories extended")
