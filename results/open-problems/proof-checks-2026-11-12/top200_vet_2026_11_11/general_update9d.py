"""Record the second arXiv queries of 11 Nov (dl_lit14.out, q14.txt): the 22 deep-learning rows whose first query
matched only unrelated records, probability row T195, and the source for the note of T310; extend the memory."""
import io
import shutil

CH = "2026-11-11 abstracts read on arXiv (dl_lit14.out, second query), an agent"
NONE = "two queries returned nothing on the question; nothing found that settles it"
APPL = "the second query returned applied papers only; nothing found that settles it"
NOTE = {
    "T244": "no change (the perturbative hierarchy of arXiv 2204.01058 is the row's starting point)",
    "T279": "no change (arXiv 2606.20469, 2502.08448)",
    "T293": "no change (no recent hit)",
    "T309": NONE,
    "T313": NONE,
    "T320": NONE,
    "T324": "no change (survey arXiv 2512.01868)",
    "T332": "no change (arXiv 2607.16676, 2611.08246)",
    "T346": APPL,
    "T357": "no change (arXiv 2502.13283)",
    "T358": "no change (no hit after 2021)",
    "T361": "no change (arXiv 2410.01243, 2404.07009)",
    "T379": APPL,
    "T384": NONE,
    "T387": "no change (arXiv 2306.16921 and 2301.13833 are the row's starting point)",
    "T391": "no change, the statement check stands: sample complexity eps^-(k v 2) in the intrinsic dimension k on "
            "unions of subspaces (arXiv 2605.30153)",
    "T392": "no change (arXiv 2609.06947)",
    "T395": APPL,
    "T396": "no change (arXiv 2609.13920, 2607.28185 treat recurrent networks with noise)",
    "T399": NONE,
    "T409": NONE,
    "T411": APPL,
}
FAM = {"T195": "no change (hardness of counting fixed-size slices, arXiv 2608.02503; #BIS itself is open)"}
assert len(NOTE) == 22
OLD310 = ("(Balasubramanian, Banerjee, Ghosal, 2024; cited from memory, not among this batch's hits, to be confirmed "
          "by the follow-up query)")
NEW310 = "(arXiv 2409.08469, in continuous and discrete time, and in Wasserstein-2 distance)"

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
n310 = 0
for k, r in enumerate(rows):
    c = r.split("\t")
    if len(c) < 7:
        continue
    if c[0] == "T310" and c[1] == "TOP200_DL":
        assert OLD310 in c[5]
        c[5] = c[5].replace(OLD310, NEW310)
        rows[k] = "\t".join(c)
        n310 += 1
        continue
    if c[1] == "TOP200_DL" and c[0] in NOTE:
        note = NOTE[c[0]]
    elif c[1] == "TOP200_FAMOUS" and c[0] in FAM:
        note = FAM[c[0]]
    else:
        continue
    assert "title read" in c[6], c[0]
    seen[c[0]] = c[2]
    tail = c[6].split(";", 1)[1] if ";" in c[6] else ""
    c[5] = (c[5] + "; " if c[5] else "") + note
    c[6] = CH + (";" + tail if tail else "")
    rows[k] = "\t".join(c)
missing = sorted((set(NOTE) | set(FAM)) - set(seen))
assert not missing, missing
assert n310 == 1
out = nl.join(rows)
assert len(out) > len(s) and out.count(nl) == s.count(nl)
left = [r.split("\t")[0] for r in rows if r.count("\t") >= 6 and "title read" in r.split("\t")[6]
        and r.split("\t")[1] in ("TOP200_DL", "TOP200_FAMOUS", "TOP200_GENERAL")]
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(out)

with io.open("DL_LITCHECK.tsv", "a", encoding="utf-8", newline="") as f:
    f.write("\t".join(["-", "rows queried a second time, no change", ", ".join(sorted(NOTE)) + ": nothing found that "
                       "settles the row (notes per row in DESERVE.tsv); T310: source of the N^(-1/2) rate confirmed, "
                       "arXiv 2409.08469", CH]) + "\n")
with io.open("FAMOUS_LITCHECK.tsv", "a", encoding="utf-8", newline="") as f:
    f.write("\t".join(["T195", seen["T195"], FAM["T195"], CH]) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Eleventh batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Eleventh batch, same day (second queries, dl_lit14.out): the 22 deep-learning rows and probability row T195 whose
first query missed are checked, none changes. With this every row of the three lists has been checked against arXiv
abstracts except T127 (a peer's claim): 557 rows, 39 changed. The check reads abstracts of the newest hits only; a
row marked unchanged is not proved open.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("recorded", len(seen), "rows; rows of the three lists still only title-read:", " ".join(left))
