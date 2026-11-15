import sys
sys.argv = ["x", "12"]
exec(open("check_grammar8.py").read().split("# coverage against")[0].replace("print(r,", "0 and print(r,"))
print("distinct reduced profiles 2..12:", sum(len({p for p, n in S[r] if not n}) for r in range(2, 13)))
print("distinct reduced volumes 2..12:", sum(len(vols[r]) for r in range(2, 13)))
