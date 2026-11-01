import json
ADJ = {0: [1, 7, 8, 10, 11, 12, 14], 1: [2, 5, 7, 10, 11, 12, 16], 2: [3, 5, 6, 7, 9, 14, 15], 3: [4, 5, 9, 10, 11, 12, 14], 4: [0, 5, 6, 11, 14, 15, 16], 5: [0, 6, 10, 12, 14, 15, 16], 6: [0, 1, 3, 7, 12, 13, 16], 7: [3, 4, 8, 10, 11, 14, 15], 8: [1, 2, 3, 4, 9, 12, 15], 9: [0, 1, 4, 5, 11, 14, 16], 10: [2, 4, 6, 8, 9, 11, 13], 11: [2, 5, 6, 8, 12, 13, 14], 12: [2, 4, 7, 9, 10, 15, 16], 13: [2, 3, 7, 8, 12, 15, 16], 14: [6, 8, 10, 12, 13, 15, 16], 15: [0, 1, 3, 6, 9, 10, 11], 16: [0, 2, 3, 7, 8, 10, 11]}
H=set(range(5)); U=set(range(5,10)); p,x,a=10,11,12; q,r=13,14
W={x,r,p}; S0={p,q,a}
def wit(C): return sorted(v for v in ADJ if v not in C and C <= set(ADJ[v]))
p={"partner_checker_blob":"b3f2b2650c959b221f2bd955281788bf0bcc5dc6","W_three_hit_witnesses":wit(W),"S0_three_hit_witnesses":wit(S0),"H_vertices_entering_x":sorted(h for h in H if x in ADJ[h]),"U_vertices_entering_x":sorted(u for u in U if x in ADJ[u])}
assert p["W_three_hit_witnesses"]==[0,3,7]
assert p["S0_three_hit_witnesses"]==[14]
assert p["H_vertices_entering_x"]==[0,1,3,4]
assert p["U_vertices_entering_x"]==[7,9]
p["result"]="PASS"
print(json.dumps(p,sort_keys=True,indent=2))
