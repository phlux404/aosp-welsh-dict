# Draft PR for Helium314/aosp-dictionaries — Add Welsh (cy) main dictionary

Repo checked 2026-11-02 ~00:31 UTC: Welsh appears exactly once in the
index table — emoji only (9,171 words, 2026-09-22). No main dictionary.

## PR title
Add Welsh (cy) main dictionary

## PR body (draft)

This adds the first main Welsh dictionary to the hub.

- `main_cy.dict` — compiled with dicttool_aosp from the wordlist below
- `cy_wordlist.combined` — 41,239 entries, header
  `dictionary=main:cy,locale=cy,description=Welsh,version=55`
  (version > 18 per the repo's wordlist notes)

Frequencies were counted from a Welsh Wikipedia (cywiki) corpus sample
and log-scaled onto the 0–255 ladder — a linear scale was tried first in
the sister AnySoftKeyboard project and squashed everyday words, so the
log ladder is deliberate. A 517-entry hand-tuned spoken layer is merged
over the top by max-frequency: common contractions (dwi'n, f=255) and
full mutation paradigms for everyday nouns (cath/gath/nghath/chath;
mawr/fawr; Cymru/Nghymru), which corpus-only Welsh dictionaries miss.

No next-word / bigram data. Field-tested in FUTO Keyboard with:
"Dwi'n byw yng Nghymru", "Fy nghath i a dy gath di",
"Bore da, diolch yn fawr", "Mae'r dŵr yn y tŷ".

Source project: https://github.com/phlux404/ask-welsh-pack (spoken layer)

## Notes for whoever opens the PR
- Follow the repo's existing folder pattern for dictionaries/wordlists
  (`<type>_<locale>` naming) — confirm exact folder names in the live
  repo at PR time; do not guess them from this draft.
- The index-table row to add: Welsh | main | (kind blank) | no next-word |
  41239 words | date | source link.
- Phillip creates any Codeberg account / fork himself; no credentials
  pass through chat.
