#!/usr/bin/env python3
"""Entry for make.fun bounty news-summary-01.

Writes a summary of the world's news of Wednesday 11 November 2026 to
/output/entry.txt. The summary is a fixed text held in this repository
(the program runs with no network), so both runs write the same bytes.
"""
import os
import sys

SUMMARY = """Wednesday, 11 November 2026

Iran kept the Strait of Hormuz shut: the Washington Institute counted 37 ships attacked in October and 10 more in November; two tankers caught fire after hitting naval mines, and Rubio said US economic pressure was 'so devastating' no major combat was needed, while the Justice Department charged three Iran-backed operatives over nearly 20 attacks and plots in the US and Europe. In Abu Dhabi, Russia, Ukraine and the US agreed the largest prisoner exchange of the war, numbers due Thursday; Zelenskyy called the talks 'constructive and quite substantive', with no ceasefire breakthrough. NATO jets scrambled twice as suspected Russian drones crossed into the Baltic states, closing Vilnius and Kaunas airports. Israeli fire killed at least seven Palestinians in Gaza, including a father and his 13-year-old son, medics said, as the new Knesset was sworn in with no government. The WHO said at least 1,771 people have been killed in Yemen since August as government forces launched a counteroffensive. At COP31 in Antalya, Guterres said the climate crisis was 'outrunning us' and fossil fuels 'must go the way of the dinosaurs'. DR Congo reported 11,042 Ebola cases and 5,387 deaths, the second-deadliest outbreak. The House voted 211-204 to shelve impeachment articles against Defence Secretary Hegseth, and Republicans chose Jim Jordan as minority leader, 106-73. British police arrested a 41-year-old US Army officer near Gloucester for suspected spying for Russia. In Mississippi, Democrat Scott Colom led Republican Cindy Hyde-Smith by about 3,500 votes, too close to call. Salvadoran troops and Haitian police destroyed a gang leader's house near Port-au-Prince; up to 20 killed, unconfirmed. A US judge ruled Donald Trump's $10bn defamation suit against the BBC can proceed. US consumer prices rose 0.4% in October, and traders expect a Fed rate rise in December. Anthropic set a $70-$78 price range for its Nasdaq listing, worth up to $1.4 trillion.
"""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SUMMARY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
