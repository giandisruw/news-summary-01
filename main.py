#!/usr/bin/env python3
"""Entry for make.fun bounty news-summary-01.

Writes a summary of the world's news of Wednesday 11 November 2026 to
/output/entry.txt. The summary is a fixed text held in this repository
(the program runs with no network), so both runs write the same bytes.
"""
import os
import sys

SUMMARY = """Wednesday, 11 November 2026

Iran dominated the day. Tehran said it is still awaiting a US reply to its seven conditions for peace talks and that the Strait of Hormuz will stay closed until they are met; three oil tankers caught fire after hitting naval mines, and November has already seen at least 37 attacks on shipping there, the most since the war began in its ninth month. US Secretary of State Marco Rubio said in Paris that America's economic pressure was working so well that major combat operations were no longer needed, while Treasury Secretary Scott Bessent moved onto a military base after Iranian threats, and the Justice Department charged three Iran-backed operatives over nearly 20 alleged plots in the US and Europe.

In Abu Dhabi, the first Ukraine-Russia-US talks were called "constructive" by President Zelenskyy, and the sides agreed a large prisoner exchange; NATO scrambled jets after drones strayed into Baltic airspace. In Gaza, Israeli forces killed at least seven people, including a father and his 13-year-old son, and Israel's new parliament was sworn in with no government after a deadlocked election. Yemen's government said its strikes killed or wounded about 190 Houthi fighters, while the WHO counted at least 1,771 dead in the fighting since August.

At COP31 in Antalya, UN chief Antonio Guterres warned leaders that slow climate action had put the world "on a path to destruction." The Democratic Republic of Congo confirmed 11,042 Ebola cases and 5,387 deaths, the second-deadliest outbreak on record. In Washington, the House voted 211-204 to kill the impeachment of Defense Secretary Pete Hegseth, and Republicans chose Jim Jordan as minority leader. British police arrested a US Army officer on suspicion of spying for Russia. Anthropic filed for a listing that could value it at $1.4 trillion.

Sources: Reuters, New York Times, Al Jazeera.
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
