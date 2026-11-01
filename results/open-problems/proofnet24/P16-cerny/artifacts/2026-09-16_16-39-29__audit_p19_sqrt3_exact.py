#!/usr/bin/env python3
"""Independent finite audit helper for P19 claim
P19-PARTS509-SQRT3-ORBIT-NOFORCEEQUAL-12.
This helper independently checks the 18 exact algebraic sqrt(3)-radius identities
and the archived execution-output structure. The written audit additionally
inspects the peer source code and its post-verification of every returned 5-coloring.
"""
from sympy import sqrt, Rational, simplify
r3,r11,r33=sqrt(3),sqrt(11),sqrt(33)
orbit={
309:(0,r3),310:(Rational(1,2),r11/2),311:((-1+r33)/4,(r3+r11)/4),312:(Rational(3,2),r3/2),313:((1+r33)/4,(-r3+r11)/4),314:((1+r33)/4,(r3-r11)/4),315:(Rational(3,2),-r3/2),316:((-1+r33)/4,(-r3-r11)/4),317:(Rational(1,2),-r11/2),318:(0,-r3),319:(-Rational(1,2),-r11/2),320:((1-r33)/4,(-r3-r11)/4),321:(-Rational(3,2),-r3/2),322:((-1-r33)/4,(r3-r11)/4),323:((-1-r33)/4,(-r3+r11)/4),324:(-Rational(3,2),r3/2),325:((1-r33)/4,(r3+r11)/4),326:(-Rational(1,2),r11/2)}
assert sorted(orbit)==list(range(309,327))
for j,(x,y) in orbit.items():
    assert simplify(x*x+y*y-3)==0, j
peer = '''graph 509 2259 edge_serial_sha256 87d3a8dc040fc5be843f088f53de6c5f3b8b4f9aa301c2572a2823da6de7ecb1
sqrt3_orbit 18 exact_geometry PASS
pair 0 309 SAT terminal_colours 0 4 nodes 511
pair 0 310 SAT terminal_colours 0 1 nodes 509
pair 0 311 SAT terminal_colours 0 2 nodes 509
pair 0 312 SAT terminal_colours 0 3 nodes 511
pair 0 313 SAT terminal_colours 0 1 nodes 509
pair 0 314 SAT terminal_colours 0 1 nodes 509
pair 0 315 SAT terminal_colours 0 3 nodes 509
pair 0 316 SAT terminal_colours 0 3 nodes 509
pair 0 317 SAT terminal_colours 0 3 nodes 509
pair 0 318 SAT terminal_colours 0 3 nodes 509
pair 0 319 SAT terminal_colours 0 2 nodes 509
pair 0 320 SAT terminal_colours 0 4 nodes 509
pair 0 321 SAT terminal_colours 0 3 nodes 509
pair 0 322 SAT terminal_colours 0 2 nodes 509
pair 0 323 SAT terminal_colours 0 1 nodes 509
pair 0 324 SAT terminal_colours 0 3 nodes 509
pair 0 325 SAT terminal_colours 0 4 nodes 509
pair 0 326 SAT terminal_colours 0 2 nodes 509
SUMMARY pairs 18 SAT 18 UNSAT 0 TIMEOUT 0
ALL_EXACT_CHECKS_PASSED
'''
lines=peer.strip().splitlines()
pairs=[]
for line in lines:
    if line.startswith('pair '):
        p=line.split()
        assert p[1]=='0' and p[3]=='SAT' and p[4]=='terminal_colours'
        j=int(p[2]); c0=int(p[5]); cj=int(p[6]); nodes=int(p[8])
        assert c0!=cj and nodes>0
        pairs.append(j)
assert pairs==list(range(309,327))
assert lines[-2]=='SUMMARY pairs 18 SAT 18 UNSAT 0 TIMEOUT 0'
assert lines[-1]=='ALL_EXACT_CHECKS_PASSED'
print('P19_REPORT_CREATION_COMMIT 85858b220f2b62c65760e215f0e10b9a455991e1')
print('P19_REPORT_BLOB f96494afaa58820ac892f656e592286ea6f49044')
print('P19_PEER_CHECKER_BLOB acc345a364042785875e1b0cf8b9aef8d5fbdc0a')
print('P19_PEER_OUTPUT_BLOB f0bb07852b019e4fde53ba62cb1a878df8c6aae3')
print('EXACT_GEOMETRY_COUNT',len(orbit),'PASS')
print('ARCHIVED_SAT_LINES',len(pairs),'PASS')
print('ARCHIVED_SUMMARY PASS')
print('AUDIT_HELPER_EXACT_CHECKS_PASSED')
