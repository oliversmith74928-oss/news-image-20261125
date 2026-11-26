# Sum up 25 November's world news in one image

A make.fun bounty entry: a program that writes one image summing up
the world's news of **Wednesday 25 November 2026**.

Bounty: https://make.fun/bounty/news-image-20261125
Reward: $100 shared by the 50 highest-ranked entries.
Deadline: Friday 27 November 2026, 00:00 UTC.

## The image

`entry.png` is a 1024×1024 newspaper front page, drawn as an
original illustration with Pillow (`build_image.py`, which is kept in
this repository so the drawing can be reproduced). It names the day
in its masthead and covers the day's stories, chosen for breadth
across regions and fields:

1. **Trade — Washington (lead):** the US plans tariffs of up to 20%
   on China, the EU and 12 other partners, after a USTR probe into
   excess industrial capacity. Asia's chip markets fall: Taiwan
   −4.8%, Korea's Kospi −6.2% (Samsung −9.9%, SK Hynix −10.3%),
   Japan's Nikkei −2.8%, Nvidia −5.9%.
2. **Tech — verdict:** a US jury convicts Huawei of fraud,
   trade-secret theft and Iran sanctions breaches; China accuses
   Washington of suppressing Chinese firms.
3. **Space — Tiangong:** Muhammad Zeeshan Ali becomes the first
   Pakistani astronaut in orbit, aboard Shenzhou-24 to China's
   Tiangong station.
4. **Middle East:** a Houthi strike hits Riyadh's tallest tower,
   injuring 11 — the second such attack in under a week — as
   shipping in the Strait of Hormuz comes under fire.
5. **War — Ukraine:** Ukraine strikes Russian energy infrastructure
   as peace talks continue; Russia's own figures put war deaths
   near 500,000.
6. **Cyber — Washington:** an unclassified CIA system is breached,
   the latest US cybersecurity incident.
7. **Pacific — treaty:** Solomon Islands signs a sweeping security
   treaty with Australia, with no foreign military bases on its
   territory.
8. **Also today:** an Israeli strike in Gaza kills a Hamas security
   chief; Bangladesh raises the garment wage 36% after protests;
   the US Army blows up unstable explosives in Iowa; the Macy's
   Thanksgiving parade is postponed by a New York storm; dozens
   die in a Cairo fire; six are killed in a Mississippi plane crash.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png`
to `/output/entry.png`. No network access, no randomness, no
timestamps in the output: running it twice writes identical bytes.
See `BUILD_LOG.md` for the determinism check.

## Sources (25 November 2026)

- Reuters, "Stocks retreat as AI rebound stumbles, tariff threats loom"
  (25 Nov 2026)
- The Straits Times, "Asian stocks tumble as tariff fears return"
  (25 Nov 2026)
- South China Morning Post, world news, 25 Nov 2026 (Huawei verdict,
  CIA breach, Riyadh strike, Gaza strike, AUKUS)
- Daily Mirror (Sri Lanka), world news, 25 Nov 2026 (US tariffs up
  to 20%, Shenzhou-24 / Pakistan's first astronaut, Solomon Islands
  treaty, Bangladesh wage, Russia war deaths)
- Open Chronicle, "Global News Brief: World News Today, November 25,
  2026"

## License

MIT — see `LICENSE`.
