"""Download archived copies of the old 3oheme.com blog from the Wayback Machine.

Writes everything under _archive_3oheme/ (ignored by Jekyll because of the leading underscore):
  cdx.txt          full capture index for the domain
  selected.tsv     the one capture chosen per URL
  html/, files/    raw original responses (id_ mode, no Wayback toolbar)
"""
import os, re, subprocess, sys, time, urllib.parse, urllib.request

OUT = "_archive_3oheme"
CDX = ("https://web.archive.org/cdx/search/cdx?url=3oheme.com&matchType=domain"
       "&fl=timestamp,original,statuscode,mimetype,length&filter=statuscode:200")
UA = {"User-Agent": "palomoduarte.com archive recovery (owner of 3oheme.com)"}


def get(url, tries=6):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                return r.read()
        except Exception as e:  # 429s and resets: back off and retry
            wait = 10 * (i + 1)
            print(f"  retry {i+1} in {wait}s: {e}", flush=True)
            time.sleep(wait)
    return None


def checkpoint(msg):
    """Commit and push what we have so a timeout never loses work."""
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return
    subprocess.run(["git", "add", OUT], check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode == 0:
        return
    subprocess.run(["git", "commit", "-qm", msg], check=True)
    for _ in range(3):
        subprocess.run(["git", "pull", "-q", "--rebase"], check=False)
        if subprocess.run(["git", "push", "-q"]).returncode == 0:
            return
        time.sleep(5)


def key(url):
    p = urllib.parse.urlsplit(url)
    host = p.hostname or ""
    host = host[4:] if host.startswith("www.") else host
    path = p.path.rstrip("/") or "/"
    return host + path + ("?" + p.query if p.query else "")


def main():
    os.makedirs(f"{OUT}/html", exist_ok=True)
    os.makedirs(f"{OUT}/files", exist_ok=True)
    raw = get(CDX)
    if raw is None:
        sys.exit("could not fetch CDX index")
    text = raw.decode("utf-8", "replace")
    open(f"{OUT}/cdx.txt", "w").write(text)

    best = {}
    for line in text.splitlines():
        parts = line.split(" ")
        if len(parts) < 4:
            continue
        ts, orig, status, mime = parts[:4]
        k = key(orig)
        is_html = mime.startswith("text/html")
        is_file = mime.startswith("image/") or mime == "application/pdf"
        if not (is_html or is_file):
            continue
        if ts >= "2016":  # the domain expired; later captures are someone else's spam site
            continue
        # keep the latest capture taken before 2016 (the blog era); else the earliest one
        prev = best.get(k)
        if prev is None or (ts < "2016" and (prev[0] >= "2016" or ts > prev[0])):
            best[k] = (ts, orig, mime)

    rows = sorted(best.items())
    print(f"{len(rows)} unique URLs selected", flush=True)
    with open(f"{OUT}/selected.tsv", "w") as f:
        for k, (ts, orig, mime) in rows:
            f.write(f"{ts}\t{orig}\t{mime}\n")
    checkpoint("Add Wayback capture index for 3oheme.com")

    for n, (k, (ts, orig, mime)) in enumerate(rows, 1):
        sub = "html" if mime.startswith("text/html") else "files"
        name = re.sub(r"[^A-Za-z0-9._-]+", "_", k)[:180]
        if sub == "html":
            name += ".html"
        dest = f"{OUT}/{sub}/{name}"
        if os.path.exists(dest):
            continue
        print(f"[{n}/{len(rows)}] {ts} {orig}", flush=True)
        body = get(f"https://web.archive.org/web/{ts}id_/{orig}")
        if body is not None:
            open(dest, "wb").write(body)
        time.sleep(1)
        if n % 40 == 0:
            checkpoint(f"Add 3oheme.com archive pages ({n}/{len(rows)})")
    checkpoint("Add 3oheme.com archive pages (done)")


if __name__ == "__main__":
    main()
