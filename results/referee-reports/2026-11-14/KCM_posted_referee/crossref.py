import json, urllib.request
dois = ["10.1088/0305-4470/21/19/017", "10.1007/s00440-007-0072-3", "10.1103/PhysRevLett.53.1244",
        "10.1007/978-3-031-93115-4", "10.1007/BF01877751", "10.1007/BF01613147", "10.1007/s00440-002-0239-x",
        "10.2140/pmp.2025.6.479", "10.1137/25M180425X", "10.1007/BF01613146", "10.1007/s10959-018-0812-6",
        "10.1007/BF01019705"]
for d in dois:
    try:
        req = urllib.request.Request("https://api.crossref.org/works/" + d, headers={"User-Agent": "referee-check/1.0"})
        m = json.load(urllib.request.urlopen(req, timeout=30))["message"]
        au = ", ".join(a.get("family", "?") for a in m.get("author", []))
        print(d, "|", au, "|", (m.get("title") or [""])[0][:90], "|", (m.get("container-title") or [""])[0],
              m.get("volume"), m.get("issue"), m.get("page"),
              (m.get("published-print") or m.get("issued", {})).get("date-parts"))
    except Exception as e:
        print(d, "ERROR", e)
