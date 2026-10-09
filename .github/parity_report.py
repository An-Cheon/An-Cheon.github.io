# Compare Jekyll build outputs for render-parity.yml; prints Markdown for the job summary.
import filecmp
import os
import sys

NL = "\n"
FENCE = "`" * 3


def walk(root):
    out = set()
    for d, _, fs in os.walk(root):
        for f in fs:
            out.add(os.path.relpath(os.path.join(d, f), root))
    return out


def snippet(x, i):
    return x[max(0, i - 300):i + 300]


pairs = [p.split(":") for p in sys.argv[1:]]
for a, b in pairs:
    fa, fb = walk(a), walk(b)
    diff = sorted(f for f in fa & fb if not filecmp.cmp(f"{a}/{f}", f"{b}/{f}", shallow=False))
    print(f"### {a} vs {b}: files {len(fa)} / {len(fb)}, only-left {len(fa - fb)}, "
          f"only-right {len(fb - fa)}, differing {len(diff)}")
    for f in sorted(fa - fb)[:10]:
        print(f"- only in {a}: `{f}`")
    for f in sorted(fb - fa)[:10]:
        print(f"- only in {b}: `{f}`")
    for f in diff[:40]:
        print(f"- differs: `{f}`")
    for f in diff[:6]:
        x = open(f"{a}/{f}", "rb").read().decode("utf-8", "replace")
        y = open(f"{b}/{f}", "rb").read().decode("utf-8", "replace")
        n = min(len(x), len(y))
        i = next((k for k in range(n) if x[k] != y[k]), n)
        print(NL + f"`{f}` first diff at {i} (len {len(x)} vs {len(y)})")
        print(FENCE + NL + "A: " + snippet(x, i) + NL + "---" + NL + "B: " + snippet(y, i) + NL + FENCE)


# Also emit GitHub annotations (visible on the run page without signing in).
def annotate(level, title, msg):
    msg = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    title = title.replace("%", "%25").replace(":", "%3A").replace(",", "%2C")
    print(f"::{level} title={title}::{msg[:3500]}", flush=True)


for a, b in pairs:
    fa, fb = walk(a), walk(b)
    diff = sorted(f for f in fa & fb if not filecmp.cmp(f"{a}/{f}", f"{b}/{f}", shallow=False))
    head = (f"{a} vs {b}: files {len(fa)}/{len(fb)}, only-left {sorted(fa - fb)[:10]}, "
            f"only-right {sorted(fb - fa)[:10]}, differing {len(diff)}: {diff[:60]}")
    annotate("notice", f"{a} vs {b}", head)
    if (a, b) != ("_serial", "_parallel"):
        continue
    for f in diff[:8]:
        x = open(f"{a}/{f}", "rb").read().decode("utf-8", "replace")
        y = open(f"{b}/{f}", "rb").read().decode("utf-8", "replace")
        n = min(len(x), len(y))
        i = next((k for k in range(n) if x[k] != y[k]), n)
        annotate("warning", f"{f} @{i} len {len(x)} vs {len(y)}",
                 "SERIAL: " + x[max(0, i - 200):i + 400] + "\n=====\nPARALLEL: " + y[max(0, i - 200):i + 400])


# Gate: serial vs parallel may only differ in files that also differ between
# two serial builds (e.g. swconf.js embeds the wall-clock build time).
def differing(a, b):
    fa, fb = walk(a), walk(b)
    return (fa ^ fb) | {f for f in fa & fb if not filecmp.cmp(f"{a}/{f}", f"{b}/{f}", shallow=False)}


noise = differing("_serial", "_serial2")
bad = sorted(differing("_serial", "_parallel") - noise)
if bad:
    annotate("error", "PARITY FAILED", f"{len(bad)} files differ beyond serial noise {sorted(noise)}: {bad[:60]}")
    sys.exit(1)
annotate("notice", "PARITY OK", f"serial and parallel identical except serial-vs-serial noise {sorted(noise)}")
