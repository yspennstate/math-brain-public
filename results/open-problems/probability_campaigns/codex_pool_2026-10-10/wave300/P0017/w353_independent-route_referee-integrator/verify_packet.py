"""Small CPU-only reproductions; writes only under this worker folder.

The numerical integration is independent of the closed gamma-function formula.
The experiment is evidence about finite cases, not the asymptotic proof.
"""
from __future__ import annotations

import ctypes
import json
import math
import os
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class MemoryStatus(ctypes.Structure):
    _fields_ = [("length",ctypes.c_ulong),("load",ctypes.c_ulong),
                ("total_physical",ctypes.c_ulonglong),("available_physical",ctypes.c_ulonglong),
                ("total_pagefile",ctypes.c_ulonglong),("available_pagefile",ctypes.c_ulonglong),
                ("total_virtual",ctypes.c_ulonglong),("available_virtual",ctypes.c_ulonglong),
                ("available_extended_virtual",ctypes.c_ulonglong)]


def fresh_resources():
    memory = MemoryStatus()
    memory.length = ctypes.sizeof(memory)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
        raise OSError("GlobalMemoryStatusEx failed")
    def cpu_times():
        values = [ctypes.c_ulonglong() for _ in range(3)]
        if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in values)):
            raise OSError("GetSystemTimes failed")
        return tuple(v.value for v in values)
    before = cpu_times()
    time.sleep(0.25)
    after = cpu_times()
    idle,kernel,user = [b-a for a,b in zip(before,after)]
    total = kernel+user
    busy = (total-idle)/total if total else 1.0
    return {"checked_at_utc":datetime.now(timezone.utc).isoformat(),
            "available_physical_bytes":memory.available_physical,"cpu_busy_fraction":busy,
            "minimum_available_physical_bytes":2*1024**3,"maximum_cpu_busy_fraction":0.80,
            "admit":memory.available_physical >= 2*1024**3 and busy <= 0.80}


def write(name, payload):
    (ROOT / name).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def simpson(fun, upper, panels):
    step = upper / panels
    value = fun(0.0) + fun(upper)
    for j in range(1, panels):
        value += (4 if j % 2 else 2) * fun(j * step)
    return value * step / 3


def audit_w352():
    rows = []
    for p in (2, 4, 8, 16, 32, 64, 128):
        # At the cutoff exp(-y**p) <= exp(-45); test two independent meshes.
        upper = 45.0 ** (1.0 / p)
        energies = []
        moments = []
        for panels in (4096, 8192):
            z = simpson(lambda y: math.exp(-y**p), upper, panels)
            y2 = simpson(lambda y: y*y*math.exp(-y**p), upper, panels) / z
            r_mean = simpson(lambda y: y**p*math.exp(-y**p), upper, panels) / z
            r2 = simpson(lambda y: y**(2*p)*math.exp(-y**p), upper, panels) / z
            power = simpson(lambda y: y**(2*p-2)*math.exp(-y**p), upper, panels) / z
            variance_x = 1.0 + r2 - r_mean*r_mean
            energies.append(p*p*y2*power/variance_x)
            moments.append({"EY2": y2, "EX": 1.0+r_mean, "VarX": variance_x})
        a = 1.0 / p
        exact = p*p/(1+a) * math.exp(math.lgamma(3*a)+math.lgamma(2-a)-2*math.lgamma(a))
        error = abs(energies[-1]-exact)/exact
        mesh_error = abs(energies[-1]-energies[-2])/exact
        assert error < 2e-8, (p, error)
        assert mesh_error < 2e-7, (p, mesh_error)
        assert abs(moments[-1]["VarX"]-(1+a)) < 2e-8
        rows.append({"p":p,"closed_form_Dp":exact,"quadrature_Dp":energies[-1],"relative_error":error,"mesh_relative_difference":mesh_error,"Dp_over_p":exact/p,"conditional_mean_variance":1/(p+1),"input_dirichlet_energy":1,"moments_by_quadrature":moments[-1]})
    return rows


def posterior_obstruction():
    rows = []
    for t in (0.25, 1.0, 4.0):
        for alpha in (0.0, -1.0, -2.0, -4.0, -8.0):
            # alpha=(-1-y+t)/sqrt(t), for X=Exp(1)-1.
            y = t-1-alpha*math.sqrt(t)
            phi = math.exp(-alpha*alpha/2)/math.sqrt(2*math.pi)
            survival = 0.5*math.erfc(alpha/math.sqrt(2))
            mills = phi/survival
            ratio = 1+alpha*mills-mills*mills
            assert 0 < ratio <= 1
            if alpha <= -4:
                assert ratio > 0.9
            rows.append({"t":t,"y":y,"alpha":alpha,"posterior_variance_over_t":ratio,"violates_candidate_pointwise_margin_0_9":ratio>0.9})
    gaussian = []
    for t in (0.25, 1.0, 4.0):
        conditional_variance = t/(1+t)
        variance_of_conditional_mean = 1/(1+t)
        assert abs(conditional_variance+variance_of_conditional_mean-1) < 1e-15
        gaussian.append({"t":t,"input_variance":1,"mean_posterior_variance":conditional_variance,"variance_of_conditional_mean":variance_of_conditional_mean,"gradient_energy_contraction_for_linear_f":1/(1+t)**2})
    return rows, gaussian


def targeted_store_read():
    db = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
    con = sqlite3.connect(db, uri=True, timeout=2)
    con.execute("PRAGMA query_only=ON")
    queries = [
        ("title-target", "SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? OR title LIKE ? OR title LIKE ? LIMIT 14", ("%P0017%", "%Dimension-free log-concave%", "%KLS%")),
    ]
    rows = []
    for name, query, args in queries:
        for row in con.execute(query, args):
            entry = dict(zip(("id","kind","title","body","metadata_json"), row))
            entry["query"] = name
            rows.append(entry)
    con.close()
    write("STORE_P0017_REPORT.json", rows)
    return [{"id":r["id"],"kind":r["kind"],"title":r["title"]} for r in rows]


def main():
    gate = {"captured_utc":datetime.now(timezone.utc).isoformat(),"decision":"ALLOW small serial stdlib CPU-only deterministic quadrature","allowed_scope":"7 peer cases at 2 meshes of <=8192 panels, 15 closed-form posterior cases, 3 Gaussian checks; one bounded read-only title query","wall_budget_seconds":50,"threads_requested":1,"gpu":False,"training":False,"network":False,"store_writes":False,"delete":False,"cpu_count":os.cpu_count(),"resource_gates_changed":False,"method":"Fresh local scope gate; no heavy computation or process/service changes"}
    gate["fresh_resource_probe"] = fresh_resources()
    gate["decision"] = "ALLOW" if gate["fresh_resource_probe"]["admit"] else "DEFER numerical experiment"
    write("COMPUTE_GATE.json", gate)
    if not gate["fresh_resource_probe"]["admit"]:
        if (ROOT/"MEASUREMENTS.json").exists():
            previous = json.loads((ROOT/"MEASUREMENTS.json").read_text(encoding="utf-8"))
            if "fresh_host_gate_passed" not in previous:
                write("PRELIMINARY_MEASUREMENTS.json", {"accepted":False,"reason":"The preliminary run had only a scope gate, no fresh host-resource probe.","measurements":previous})
        write("MEASUREMENTS.json", {"experiment_status":"DEFERRED","accepted":False,"fresh_host_gate_passed":False,"command":"python -X utf8 ~/brain_workers/w353/verify_packet.py","reason":"Fresh host-resource gate did not admit the numerical experiment.","gate":gate,"mathematical_proofs":"Analytic derivations in ATTEMPT.md and REVIEW_PACKET.md remain available; no accepted numerical improvement claim."})
        print(json.dumps(gate,indent=2))
        return
    started = time.perf_counter()
    peer_rows = audit_w352()
    posterior, gaussian = posterior_obstruction()
    measurement = {"command":"python -X utf8 ~/brain_workers/w353/verify_packet.py","measured_utc":datetime.now(timezone.utc).isoformat(),"accepted":True,"fresh_host_gate_passed":True,"experiment_status":"PASS","gate":gate,"w352_independent_reproduction":peer_rows,"posterior_obstruction":posterior,"gaussian_identity_checks":gaussian,"claims":{"peer_asymptotic":"proved analytically in REVIEW_PACKET.md; finite quadrature is not an asymptotic proof","own_tail_limit":"proved analytically in ATTEMPT.md; not inferred from rounded numbers","full_KLS_proof_checked":False},"max_peer_relative_error":max(r["relative_error"] for r in peer_rows),"candidate_pointwise_margin_0_9_violations":sum(r["violates_candidate_pointwise_margin_0_9"] for r in posterior),"numerical_elapsed_seconds":time.perf_counter()-started}
    assert measurement["numerical_elapsed_seconds"] < gate["wall_budget_seconds"]
    write("MEASUREMENTS.json", measurement)
    print(json.dumps({"peer_cases":len(peer_rows),"max_peer_relative_error":measurement["max_peer_relative_error"],"Dp_p2":peer_rows[0]["closed_form_Dp"],"Dp_p128":peer_rows[-1]["closed_form_Dp"],"Dp_over_p128":peer_rows[-1]["Dp_over_p"],"posterior_cases":len(posterior),"pointwise_margin_0_9_violations":measurement["candidate_pointwise_margin_0_9_violations"],"posterior_max_ratio":max(r["posterior_variance_over_t"] for r in posterior),"gaussian_checks":len(gaussian),"numerical_elapsed_seconds":measurement["numerical_elapsed_seconds"]},indent=2))
    print(json.dumps({"store_title_matches":targeted_store_read()},ensure_ascii=False))


if __name__ == "__main__":
    main()
