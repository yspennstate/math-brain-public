"""Print title, authors, comment and the whole abstract of given arXiv ids.  usage: lit_ids.py <out file> <id> [<id> ...]"""
import re, sys, time, urllib.parse, urllib.request

out = open(sys.argv[1], "w", encoding="utf-8", newline="")
ids = sys.argv[2:]
for k in range(0, len(ids), 10):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(ids[k:k + 10]), "max_results": 10})
    s = ""
    for attempt in range(3):
        try:
            s = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-client/1.0"}), timeout=45).read().decode("utf-8")
            if "<entry>" in s:
                break
        except Exception as e:
            print("attempt", attempt, "failed:", str(e)[:80], file=out)
        time.sleep(8)
    for e in s.split("<entry>")[1:]:
        i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
        t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
        au = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:200]
        ab = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
        c = re.search(r"<arxiv:comment[^>]*>(.*?)</arxiv:comment>", e, re.S)
        cat = re.search(r'<arxiv:primary_category[^>]*term="([^"]*)"', e)
        print("==", i, "|", t, "|", au, "|", cat.group(1) if cat else "?", "|", " ".join(c.group(1).split())[:200] if c else "", file=out)
        print("  ", ab, file=out)
    time.sleep(4)
out.close()
print("ids", len(ids))
