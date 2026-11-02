#!/usr/bin/env python3
"""Generate an AOSP .combined wordlist for Welsh (cy).

Sources:
 - the cywiki corpus sample used by the ASK Welsh pack (recounted here,
   log-scaled onto the AOSP 0-255 ladder)
 - the hand-tuned spoken layer from the ASK pack (frequencies kept
   verbatim, merged by MAX so the spoken layer always wins ties)
Output: cy_wordlist.combined (header + ' word=<w>,f=<n>' lines)
"""
import math
import re
import time
import xml.etree.ElementTree as ET
from collections import Counter

BASE = "/home/phlux/workspace/projects/AnySoftKeyboard/addons/languages/welsh"
CORPUS = BASE + "/pack/dictionary/inputs/cywiki_sample.txt"
SPOKEN = BASE + "/pack/dictionary/prebuilt/welsh_spoken.xml"
OUT = "/home/phlux/workspace/projects/aosp-welsh-dict/cy_wordlist.combined"

MIN_COUNT = 3
FLOOR, CEIL = 20, 215
LADDER = 18.0  # f points per decade of corpus frequency

# Welsh-aware tokenizer: letters (incl. accented Latin + Latin Ext-A for
# w/y circumflex), internal apostrophes kept.
TOKEN = re.compile(r"[A-Za-z\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u017f']+")

counts = Counter()
with open(CORPUS, encoding="utf-8") as fh:
    for line in fh:
        for tok in TOKEN.findall(line):
            w = tok.strip("'")
            if w and any(c.isalpha() for c in w):
                counts[w] += 1

max_count = max(counts.values())
freq = {}
for w, c in counts.items():
    if c < MIN_COUNT:
        continue
    f = round(CEIL - LADDER * (math.log10(max_count) - math.log10(c)))
    freq[w] = max(FLOOR, min(CEIL, f))

# Spoken layer overlay (max-merge).
spoken = {}
root = ET.parse(SPOKEN).getroot()
for el in root.iter("w"):
    w = (el.text or "").strip()
    if w:
        spoken[w] = max(spoken.get(w, 0), int(el.get("f", "0")))
for w, f in spoken.items():
    freq[w] = max(freq.get(w, 0), f)

date = int(time.time())
with open(OUT, "w", encoding="utf-8") as out:
    out.write("dictionary=main:cy,locale=cy,description=Welsh,date=%d,version=55\n" % date)
    for w in sorted(freq, key=lambda x: (-freq[x], x)):
        out.write(" word=%s,f=%d\n" % (w, freq[w]))

print("corpus tokens=%d types=%d max_count=%d" % (sum(counts.values()), len(counts), max_count))
print("kept=%d spoken=%d" % (len(freq), len(spoken)))
for probe in ["dwi'n", "nghath", "gath", "cath", "fawr", "mawr", "Nghymru",
              "nghymru", "Cymru", "cymru", "Ngheri", "bore", "da", "diolch", "yn"]:
    print(probe, freq.get(probe))
