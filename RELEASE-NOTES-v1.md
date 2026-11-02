# Welsh (cy) AOSP dictionary v1.0 — release notes

Title: Welsh main dictionary for FUTO / HeliBoard (AOSP) v1.0
Asset: main_cy.dict (284,439 bytes)
SHA-256: 6a241693d69935fc3d9b5695817b74957f610af2a819694495191264c71e8acf
Also include in the release: cy_wordlist.combined (source, 41,239 entries)

Body:

The missing piece for Welsh on privacy keyboards.

FUTO Keyboard has had a Welsh *layout* since 2025 and a Welsh *emoji*
lookup — but no Welsh dictionary, so no real word prediction. The community
hub its docs point to (Helium314/aosp-dictionaries) listed Welsh as
emoji-only. This is a full main dictionary: 41,239 Welsh words, frequencies
counted from a Welsh Wikipedia corpus sample on a log scale, with a
517-entry hand-tuned spoken layer on top — the contractions people actually
type (dwi'n at maximum frequency) and the full mutation system
(cath → gath / nghath / chath; Cymru → Nghymru; mawr → fawr).

Built from the spoken layer first shipped in ask-welsh-pack v1.0 for
AnySoftKeyboard, retuned for AOSP's 0–255 frequency ladder.

Install: FUTO Settings → Languages & Models → Welsh → Dictionary → import
main_cy.dict.

Field-tested in FUTO Keyboard 2026-11-01: **4/4 pass** — "Dwi'n byw yng
Nghymru", "Fy nghath i a dy gath di" (the sentence that broke the ASK
pack), "Bore da, diolch yn fawr", "Mae'r dŵr yn y tŷ".

Known limits, honestly: no next-word (bigram) data in v1.0; corpus register
still leans formal outside the spoken layer.
