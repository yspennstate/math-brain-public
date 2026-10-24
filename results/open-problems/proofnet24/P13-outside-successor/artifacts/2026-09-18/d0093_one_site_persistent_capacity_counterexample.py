#!/usr/bin/env python3
"""Exact finite self-check for the D0093 one-site persistent-capacity obstruction.

One open ARW site has a stack over {S,J}.  S is an attempted sleep and is
effective iff exactly one active particle is present.  J is a jump; either
jump direction exits this one-site interval, so direction is irrelevant here.
"""


def stabilize_one_site(stack: str, q: int):
    active = q
    exits = 0
    for used, instr in enumerate(stack, 1):
        if instr == "S":
            if active == 1:
                return {"sleepers": 1, "exits": exits, "used": used, "stabilized": True}
            # With >=2 active particles the sleep instruction is ineffective.
        elif instr == "J":
            active -= 1
            exits += 1
            if active == 0:
                return {"sleepers": 0, "exits": exits, "used": used, "stabilized": True}
        else:
            raise ValueError(f"bad instruction {instr!r}")
    return {"sleepers": None, "exits": exits, "used": len(stack), "stabilized": False}


stack = "SJJ"
one = stabilize_one_site(stack, 1)
two = stabilize_one_site(stack, 2)

print(f"stack={stack}")
print("q=1", one)
print("q=2", two)

assert one == {"sleepers": 1, "exits": 0, "used": 1, "stabilized": True}
assert two == {"sleepers": 0, "exits": 2, "used": 3, "stabilized": True}

print("PASS: the same fresh stack traps one particle, while adding one particle destroys that trap and both particles exit.")
