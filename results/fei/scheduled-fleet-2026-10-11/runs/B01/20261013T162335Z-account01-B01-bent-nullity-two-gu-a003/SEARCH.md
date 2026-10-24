# Bounded search record

Search programs: `search_gu_nullity_two.py` and `search_bent_shields.py` in
the run workspace. The archived certificate does not depend on either.

Commands used:

```
python search_gu_nullity_two.py --m 5 --matrices 12 --restarts 6 --steps 120
python search_gu_nullity_two.py --m 6 --matrices 5 --restarts 3 --steps 80
python search_gu_nullity_two.py --m 6 --matrices 16 --restarts 4 --steps 120 --seed 20261014
python search_bent_shields.py --m 6 --matrices 6 --restarts 4
```

The final command was interrupted after obtaining the archived witness:

```
ratio = 2.9743752964517123
rows  = [31, 52, 7, 34]
mask  = 13594860716390676976
G     = 14.871876482258562
I     = 5.0
```

Search values were floating-point candidate locators only. All claims use
`CHECK_BENT_GU.py`.

