"""Vet agent's general-mathematics candidates (top200_general_2026_11_10/candidates_general.tsv) by title and
append them to DESERVE.tsv under the list name TOP200_GENERAL. Read-only on agent's folder.
Scores: 5 = a central problem of its field, 4 = well known and worth a place, 3 = known but light for a top 200.
Status notes marked (memory) were written from memory on 2026-11-11 and are checked separately (GENERAL_LITCHECK.tsv)."""
import csv

SRC = "../top200_general_2026_11_10/candidates_general.tsv"
STAMP = "2026-11-11 title read, an agent"

FOUR = set("NT08 NT14 NT16 NT17 NT19 NT20 NT23 NT26 AG08 AG13 AG14 AL03 AL05 AL06 AL08 AL09 AL10 TO06 TO09 TO10 TO14 "
           "DG01 DG02 DG03 DG04 DG05 DG07 DG11 AN06 AN08 AN11 AN13 AN14 PD10 PD11 PD15 PD16 PD17 DY05 DY07 DY08 "
           "CO02 CO05 CO08 CO10 GE02 GE05 GE06 LO03 LO04 LO06 IT01 IT02 OA02 OA04".split())
THREE = {
 "NT18": "a single Diophantine family with no known link to a wider theory",
 "GE08": "a recreational statement; follows from Bombieri-Lang, which is already NT21",
 "AN10": "a coefficient problem of narrow reach",
 "AN05": "polygons with five or more sides only; light for a top 200",
 "AN12": "a Banach-space existence question of narrow reach",
 "DG14": "the remaining cases of a classification; light for a top 200",
}
SPECIAL = {
 "CO12": ("CHECK_STATUS", 5, "a 2026 construction with n^(1+c) unit distances, against the conjectured n^(1+o(1)), was reported (memory); "
                             "if it stands the row becomes the true exponent between 1+c and 4/3"),
 "AG10": ("REPORTED_SOLVED_VERIFY", 5, "Katzarkov-Kontsevich-Pantev-Yu posted a proof of irrationality in 2025 (memory); unrefereed"),
 "PD08": ("REPORTED_SOLVED_VERIFY", 5, "Hou-Wang-Yang posted a computer-assisted proof of non-uniqueness without forcing in 2025 (memory); unrefereed"),
 "GE07": ("REPORTED_SOLVED_VERIFY", 3, "Baek posted a proof that Gerver's sofa is optimal in 2024 (memory); under review"),
 "PD14": ("RESTATE", 5, "global regularity is false in part of the range: Merle-Raphael-Rodnianski-Szeftel built smooth blow-up for "
                        "defocusing supercritical Schroedinger in some dimensions (memory); state the remaining cases"),
 "TO13": ("RESTATE", 5, "the rationality form is false (Austin, Grabowski); the open statement is integrality for torsion-free groups"),
 "AN07": ("DESERVES", 4, "proved for all sufficiently large degrees (Tao 2020); intermediate degrees open"),
 "DG06": ("DESERVES", 4, "proofs for smooth surfaces have been announced and are not generally accepted; say so in the row"),
 "DG09": ("DESERVES", 5, "R^4, R^5, R^6 are done (Chodosh-Li; Chodosh-Li-Minter-Stryker; Mazet), so R^7 is the last case (memory)"),
 "AN01": ("DESERVES", 5, "Hilbert-space case; a 2023 preprint of Enflo claims a proof and is unverified"),
 "NT05": ("DESERVES", 5, "Mochizuki's claimed proof is not accepted by the community; treat as open"),
 "CO03": ("DESERVES", 4, "Suk (2016) gives 2^(n+o(n)); the exact value 2^(n-2)+1 is open"),
 "CO08": ("DESERVES", 4, "a proof for large k was announced by Ajtai-Komlos-Simonovits-Szemeredi and is unpublished"),
 "AL04": ("DESERVES", 5, "the unit conjecture fell (Gardam 2021); zero divisors and idempotents are open"),
}

with open(SRC, encoding="utf-8", newline="") as f:
    cand = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
with open("DESERVE.tsv", encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
keep = [l for l in lines if l and l.split("\t")[1] != "TOP200_GENERAL"]
new = []
for c in cand:
    k, title = c["key"], c["title"]
    if k in SPECIAL:
        verdict, score, reason = SPECIAL[k]
    elif k in THREE:
        verdict, score, reason = "BORDERLINE_NICHE", 3, THREE[k]
    elif k in FOUR:
        verdict, score, reason = "DESERVES", 4, "well-known open problem of " + c["domain"]
    else:
        verdict, score, reason = "DESERVES", 5, "central open problem of " + c["domain"]
    new.append("\t".join([k, "TOP200_GENERAL", title, str(score), verdict, reason, STAMP]))
with open("DESERVE.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(keep + new) + "\n")
from collections import Counter
print(len(keep) - 1, "rows kept,", len(new), "general rows written;", dict(Counter(l.split("\t")[4] for l in new)),
      "scores", dict(Counter(l.split("\t")[3] for l in new)))
