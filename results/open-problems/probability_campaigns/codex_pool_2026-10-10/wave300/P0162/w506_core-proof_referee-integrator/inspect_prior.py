"""Print only the P0162 neighborhood in one dated dedup index."""
from pathlib import Path

p = Path("~/<private-repo>/06_math_research/probability_1000_intake_F_20260908/raw/dedup_index.json")
s = p.read_text(encoding="utf-8")
start = 0
while (i := s.find("P0162", start)) >= 0:
    print("offset", i, "context", s[max(0, i-260):i+650].replace("\n", " "))
    start = i+5
