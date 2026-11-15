import sys
sys.argv = ["x", "7"]
exec(open("check_grammar8.py").read().split("# coverage against")[0].replace("print(r,", "0 and print(r,"))
exec(open("check_mid8.py").read().split("# ---------- 1.")[0])
for w in ("abacbdeced", "abacbdcede", "abcadbecde", "ababcdefefcd", "abacbdefcfed"):
    v = vol(pm_of(w)) if len(w) <= 10 else None
    print(w, v, "in class" if v in vols[len(w)//2] else "outside class")
print("313/1260 in class r=6?", F(313,1260) in vols[6])
d = json.load(open(f"{R}/data/volumes_T12.json"))
V12 = {tuple(json.loads(k)): F(v["volume"]) for k, v in d["orbits"].items()}
for w in ("ababcdefefcd", "abacbdefcfed"):
    v = V12[tuple(canonical(pm_of(w)))]
    print(w, v, "in class" if v in vols[6] else "outside class")
print("313/1260 among r=6 reduced volumes?", F(313,1260) in {F(x) for x in V12.values()})
