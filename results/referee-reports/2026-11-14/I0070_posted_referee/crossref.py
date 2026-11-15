import json, urllib.request
dois = ["10.1007/s00030-025-01090-2", "10.1088/1361-6544/abd613", "10.1007/s00028-022-00786-7",
        "10.1007/s00440-023-01249-x", "10.5802/crmath.833", "10.1007/BF01084893",
        "10.1016/j.jfa.2010.05.012", "10.1007/s40072-019-00134-w"]
for d in dois:
    try:
        req = urllib.request.Request("https://api.crossref.org/works/" + d, headers={"User-Agent": "referee-check/1.0"})
        m = json.load(urllib.request.urlopen(req, timeout=30))["message"]
        au = ", ".join(a.get("family", "?") for a in m.get("author", []))
        print(d, "|", au, "|", (m.get("title") or [""])[0][:90], "|", (m.get("container-title") or [""])[0],
              m.get("volume"), m.get("issue"), m.get("page"), m.get("article-number"),
              (m.get("published-print") or m.get("issued", {})).get("date-parts"))
    except Exception as e:
        print(d, "ERROR", e)
