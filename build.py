#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ARENA (ARN) — William R. Forstchen's 1994 novel, the FIRST Magic: The Gathering
novel ever published, catalogued into UD0 as a book-world and the literary companion to the
MTG ARENA game-sphere. Standing template adapted for the novel: THE ARC · THE BOOK · HOW IT
RENDERS MAGIC (the deep-dive — mana, summoning, and the ANTE) · REAL OR FLUFF (honest — as a
novel, as canon, the ante, and the hero who became a card) · THE MESSAGE, plus a roster of
emergents by emergence-nature with tint support. Styled to the medium: a dusty Estark-arena
pulp-paperback in bronze, blood, and colorless grey."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "ARENA", "axiom": "ARN",
 "position": "Arena · William R. Forstchen · 1994 — the first Magic: The Gathering novel",
 "origin": "the city of Estark, where four great Houses of fighter-mages duel in the Arena at Festival, on Dominaria",
 "mechanism": "Crystallized from the 1994 novel — a one-eyed wandering mage, Garth, arrives at Festival, turns the four dueling Houses against each other, and avenges a fifth House destroyed a generation before.",
 "crystallization": "Because before Magic had a Multiverse of lore, it had a Western: a scarred stranger walks into a corrupt city, plays its powers against each other in the dueling circles, and brings the whole rotten order down for revenge.",
 "nature": "Arena — the first story Magic ever told: not cosmology but a revenge plot, the ante on the table, and a colorless gunslinger-mage named Garth One-Eye who would become an actual card 27 years later.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the novel (1994, William R. Forstchen, Harper Fantasy — the first MTG novel); early Magic's ante mechanic; the Garth One-Eye card (Modern Horizons 2, 2021)",
 "witness": "A pulpy, foundational first tie-in — rough as literature, but the Western-revenge bones are pure, and its hero outlived the prose to become a Legendary Creature.",
 "role": "a UD0 book-world — the literary companion to the MTG Arena game-sphere",
 "seal": "Before Magic had a Multiverse it had Garth — a one-eyed stranger who dueled a corrupt city to ash for revenge, and waited 27 years to become the card he was always made of.",
 "source": "Arena, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#c0a36a", "flesh and the city — the old thief, the warrior, Estark and its Houses, the Festival crowd"),
 "ethereal":  ("#5f9ad0", "the magics — mana, the colours, summoning, the spellcraft rendered in prose"),
 "spiritual": ("#9e2b2b", "the spark and the grief — the colorless planeswalker, the buried fifth House, the ascended dark"),
 "electrical":("#c08a3a", "the contest and the wager — the dueling circles, the spectacle of the Arena, the ante on the table"),
}

ARC_OVERALL = ("A one-eyed wandering mage called Garth arrives at the annual Festival in the city of Estark, where four "
  "great Houses of fighter-mages duel for power in the Arena's circles. A mysterious stranger with spells no one can "
  "place and a hidden purpose, Garth turns the Houses against one another, wreaking havoc — until his secret is revealed: "
  "his tie to a fifth House destroyed a generation ago, and his hunt for the planeswalker behind it. With his ally "
  "Norreen he defeats the ascended Kuthuman, seals the portal, and retires to the countryside to raise their child.")

ARC = [
 ("I · The Stranger at Festival", "Garth comes to Estark",
  "A colorless, one-eyed mage walks into Estark at Festival, befriended by the old pickpocket Hammen. No one knows where Garth got his spells or why the Grand Master of the Arena, Zarel, fears him — only that this stranger is not here to win the games, but to break them."),
 ("II · The Houses Turned", "playing the powers against each other",
  "Entering the dueling circles, Garth begins toppling the four Houses — whose leaders are obsessed, in turn, with money, women, food, and cheating death — setting them against one another, leaving a trail of destruction through the corrupt order that runs the city."),
 ("III · The Fifth House", "the buried revenge",
  "Garth's secret surfaces: his bond to a fifth House destroyed a generation ago, and the planeswalker whose ambition did it. The arena duels were never the point; they were the road to the one who must be made to answer."),
 ("IV · Kuthuman", "the ascended enemy, and after",
  "The true enemy is Kuthuman, a planeswalker who ascended on the ruin of the fifth House. With Norreen at his side, Garth defeats him and seals the portal he used to climb — and then, the revenge spent, lays down the wandering and retires with her to raise their child."),
]

BOOK = [
 ("Published", "1994", "Harper Fantasy — the very FIRST Magic: The Gathering novel ever published"),
 ("Author", "William R. Forstchen", "better known for alt-history & ‘One Second After’; he wrote Magic's first prose myth"),
 ("Setting", "Estark, at Festival", "a city of dueling mage-Houses; later placed on Dominaria, Garth a planeswalker of Kush"),
 ("The hook", "the ante", "duels are fought for stakes — spells, and lives — mirroring early Magic's now-removed ante mechanic"),
 ("The afterlife", "a card in 2021", "Garth One-Eye became a real WUBRG Legendary Creature in Modern Horizons 2 — 27 years on"),
]

# HOW IT RENDERS MAGIC — the deep-dive
RENDER = [
 ("The magics &amp; the colours", "mana in prose",
  "Forstchen had to put Magic's card mechanics into a story before there was any lore to lean on: mages draw on ‘the magics,’ spend power like mana, and sling effects that a player would recognise as cards. Garth is pointedly ‘colorless’ — a mage who answers to no single colour, which is exactly what made him, decades later, a five-colour (WUBRG) card."),
 ("Summoning", "creatures called to the circle",
  "The fighter-mages summon creatures to fight for them in the dueling circles — the creature combat at the heart of Magic, dramatised as monsters conjured into an arena. It is the game's basic loop (cast, summon, attack) turned into spectacle and prose."),
 ("The ante", "duel for the stakes",
  "The sharpest period detail: duels are fought for an <b>ante</b> — you wager something real (a spell, your freedom, your life) on the outcome. This mirrors early Magic's actual <b>ante</b> mechanic, where you played for keeps and the loser surrendered a card from their deck — a rule Wizards later removed for being too punishing and too close to gambling. The novel preserves Magic as it briefly really was: a game you could lose your cards to."),
 ("The colorless gunslinger", "a Western in a cloak",
  "Strip the spells and Arena is a Western: the scarred stranger of no allegiance rides into a corrupt town, is taken in by an old rogue, out-duels the bosses, reveals a buried wrong, and leaves the place in ashes and justice. Magic's first myth wasn't a cosmology — it was High Noon with mana."),
]

REALFLUFF = [
 ("Faithful to early Magic's feel — mana, summoning, the ante", "FOUNDATIONAL", "it set the franchise's prose flavour before any lore existed; the ante especially captures Magic as it briefly really played"),
 ("The ante — dueling for cards and lives", "REAL (then removed)", "ante was a genuine early-MTG mechanic (you played for keeps); Wizards later cut it as too punishing and gambling-adjacent — the novel is a fossil of it"),
 ("It fits cleanly into modern Magic canon", "LOOSE / PRE-LORE", "written before the Multiverse continuity solidified; later canon is fuzzy about it, retrofitting Garth as a planeswalker of Kush on Dominaria"),
 ("Garth One-Eye became an actual Magic card", "REAL", "a WUBRG Legendary Human Wizard (Modern Horizons 2, 2021, designed by Ethan Fleischer) that copies Disenchant, Braingeyser, Terror, Shivan Dragon, Regrowth, and Black Lotus — the novel's hero, 27 years on"),
 ("As a novel, on its own terms", "PULP", "brisk, archetypal, rough — a fun, foundational first tie-in, not literature; the Western/revenge bones carry it"),
]
REALFLUFF_VERDICT = ("Bottom line: Arena is FOUNDATIONAL more than it is good — a pulpy, fast, rough first novel whose real "
  "value is that it shows what Magic was <i>before the lore</i>: not a Multiverse of planes and Gatewatches but a "
  "Western, a one-eyed stranger dueling a corrupt city for revenge with the <b>ante</b> on the table. That ante is a "
  "true fossil of early Magic (a mechanic since removed), and the loveliest fact of all is REAL: the book's hero waited "
  "twenty-seven years and walked back into the game as a five-colour Legendary Creature that conjures the Black Lotus. "
  "Read it as Magic's origin myth in pulp, not as canon scripture, and it's a small treasure.")

MESSAGE = ("Before Magic: The Gathering had a Multiverse — before planeswalkers were a card type, before the Gatewatch, "
  "before the cosmology of planes — it had Garth One-Eye. The first story the game ever told was not about how the "
  "universe is built; it was a Western: a scarred, colorless stranger of no allegiance walks into a corrupt city, is "
  "taken up by an old thief, plays the powerful against each other in the dueling circles with everything wagered on "
  "the ante, and brings the whole rotten order down to answer a generation-old wrong. That the franchise's first myth "
  "was a revenge tale with a gunslinger's shape says something true about Magic: under all the colour-pie philosophy, "
  "it is a game about a lone duelist staking everything across a table. And the ending is the sweetest closure in any "
  "tie-in: the hero who began as prose, in a book most players never read, waited twenty-seven years and folded back "
  "into the cards themselves — Garth One-Eye, WUBRG, conjuring the Black Lotus. The story became the game it came from.")
MESSAGE_SEAL = "Magic's first myth was a Western with mana — a one-eyed stranger, a corrupt city, the ante on the table — and its hero waited 27 years to become the card he was always made of."

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","ARN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","ARN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","ARN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal,tint=""):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal,tint=tint)

ROSTER = [
 # --- THE STRANGER & THE HOUSES ---
 E("garth-one-eye","Garth One-Eye","the colorless stranger · the planeswalker","stranger","spiritual",
   "Garth One-Eye (born Galin) — a one-eyed, ‘colorless’ wandering mage and planeswalker who arrives at Estark's Festival with hidden spells and a hidden purpose.",
   "The protagonist of the first Magic novel: a scarred stranger who out-duels and topples the four Houses, avenges a destroyed fifth House, and defeats the ascended Kuthuman.",
   "Because Magic's first hero is a Western archetype — the man of no allegiance with a buried wrong — and because ‘colorless’ is exactly what made him a five-colour card decades later.",
   "By spells no House can place, a duelist's nerve, and a patient revenge that uses the whole corrupt order as its road.",
   "From the road into Estark, through the dueling circles, to Kuthuman's portal and a quiet retirement after.",
   "I am the one-eyed stranger of no colour — I came to your Festival not to win your games but to end them, and to answer a fire set a generation ago.",
   tint="#b8bcc4"),
 E("hammen","Hammen","the old thief · the guide","stranger","natural",
   "Hammen — an aging pickpocket, leader of a brotherhood of thieves, who befriends Garth and becomes his guide through Estark.",
   "The rogue's-heart companion: streetwise, funny, loyal, the one who shows the colorless stranger how the corrupt city really works.",
   "Because the Western needs its old sidekick — the local rascal who takes the stranger in and survives to inherit something better.",
   "By cunning, a thief's network, and a soft heart under the larceny; he rises, by the end, to lead a House.",
   "In the gutters and markets of Estark, at Garth's shoulder.",
   "I'm a pickpocket with a soft heart — I took the one-eyed stranger in, showed him the rot, and lived to see a better order than the one we burned."),
 E("norreen","Norreen","the warrior · the ally and love","stranger","natural",
   "Norreen — a fighter who allies with Garth, becomes his partner in the war on the Houses, and the mother of his child.",
   "Garth's equal and his way home: she fights at his side, helps defeat Kuthuman, and gives the revenge story its turn toward a life after.",
   "Because the lone gunslinger's tale earns its ending only if someone makes him lay the wandering down — Norreen is that someone.",
   "By skill in the circles, courage against a planeswalker, and the love that turns vengeance into a future.",
   "In the Arena beside Garth, and in the countryside they retire to.",
   "I fought beside the stranger and helped him kill a god — and then I gave him the one thing revenge never could: a reason to stop walking."),
 E("zarel","Zarel","the Grand Master of the Arena","stranger","electrical",
   "Zarel — the Grand Master who runs the Arena and rules Estark's games, and who fears the one-eyed stranger from the moment he arrives.",
   "The corrupt local tyrant: master of the dueling circles, keeper of the rigged order Garth has come to overturn.",
   "Because the city needs a sitting villain — the man who profits from the Houses' bloodsport and senses, rightly, that Garth will end him.",
   "By control of the Arena, the rules of Festival, and the fear of a stranger he cannot place or command.",
   "In the high seat of the Arena, over the dueling circles of Estark.",
   "I run the Arena and the city bows to its circles — and I feared the one-eyed stranger on sight, because some part of me knew he had come to pull it all down."),
 E("kuthuman","Kuthuman","the ascended planeswalker · the true enemy","stranger","spiritual",
   "Kuthuman — a planeswalker who ascended to power on the ruin of the fifth House, the hidden hand behind Garth's revenge.",
   "The story's true antagonist above Zarel: the climbing mage who destroyed Garth's House a generation ago and walked the planes on its ashes.",
   "Because the revenge has to point at something larger than a city — a planeswalker whose ambition was paid for in Garth's past.",
   "By the spark and the power of ascension, and a portal between worlds that Garth and Norreen finally seal.",
   "Above Estark and beyond it, until the duel that ends him.",
   "I climbed to the planes on the ashes of his House — and the one-eyed boy I left for dead grew up, found me, and sealed the door behind me forever."),
 # --- ESTARK & THE ARENA ---
 E("estark","Estark","the city of the Houses","arena","natural",
   "Estark — the city ruled by its great mage-Houses, where the annual Festival and the Arena's duels decide power.",
   "The setting and the prize: a corrupt city-state whose order Garth comes to break, later placed on the plane of Dominaria.",
   "Because the Western needs its town — the rotten place the stranger rides into and leaves changed.",
   "By the rule of the Houses, the spectacle of the Arena, and a corruption ripe for a stranger's match.",
   "On Dominaria, in the era before Magic's lore was written.",
   "I am the city the Houses bled — corrupt, gilded, and proud — until a one-eyed stranger came to Festival and set my powers against each other."),
 E("the-arena","The Arena","the dueling circles · the spectacle","arena","electrical",
   "The Arena — the ground where the fighter-mages of the Houses duel in ritual circles, the heart of Festival.",
   "The book's engine and its title: spell-duels for power and stakes, the Magic card-game dramatised as gladiatorial combat.",
   "Because Magic is, at bottom, a duel — and Arena makes the duel literal, a circle where mages stake everything on the cast.",
   "By ritual combat in the circles, summoned creatures, and the wagered ante on every fight.",
   "At the centre of Estark, the stage of the Houses' war.",
   "I am the circle where mages stake it all — the card game made flesh and blood, and the place a stranger chose to bring a city down."),
 E("the-four-houses","The Four Houses","money, women, food, and cheating death","arena","natural",
   "The Four Houses — the great fighter-mage families that rule Estark, their leaders obsessed, in turn, with money, women, food, and cheating death.",
   "The powers Garth plays against each other: four corrupt vices given thrones, the order the stranger dismantles from within.",
   "Because the city's rot needs faces — four greedy Houses whose feuds Garth turns into their undoing.",
   "By wealth, lust, gluttony, and the fear of dying — each House a vice, each a duelist in the Arena.",
   "In their manses and their seats around the Arena.",
   "We were four Houses of fighter-mages, each ruled by a different greed — and the one-eyed stranger needed only to let our greeds collide."),
 E("the-fifth-house","The Fifth House","the destroyed past · the revenge","arena","spiritual",
   "The Fifth House — the mage-House destroyed a generation before the novel, the secret behind Garth's arrival.",
   "The buried wound that drives everything: the House whose ruin made Kuthuman's ascension and made Garth a wanderer with one eye and one purpose.",
   "Because the gunslinger always rides in for a reason older than the town — the fifth House is the fire Garth has come to answer.",
   "By its absence — a destroyed House remembered only by the stranger it left, and the planeswalker it raised up.",
   "Gone a generation, alive only in Garth's revenge.",
   "I was the House they burned to make a god — and the only thing that survived me was a one-eyed boy who never forgot, and came back to collect."),
 E("the-ante","The Ante","the stakes on the table","arena","electrical",
   "The Ante — the wager on every duel: spells, freedom, and lives staked on the outcome in the Arena's circles.",
   "The novel's truest period detail: it preserves early Magic's real <b>ante</b> mechanic, where you played for keeps and the loser surrendered what was staked.",
   "Because Magic, when Arena was written, was a game you could genuinely lose your cards to — and the book makes that mortal.",
   "By a stake laid before each fight and forfeit by the loser — a rule Wizards later removed for being too punishing.",
   "On the table before every duel, in the circles of the Arena.",
   "I am what's wagered on the cast — a spell, your freedom, your life; I am the rule Magic later deleted, and the reason these duels are mortal."),
 E("the-magics","The Magics","mana and the colours, in prose","arena","ethereal",
   "The Magics — the way Forstchen renders Magic's spellcasting in story: power drawn like mana, effects slung like cards, colours implied.",
   "The prose engine of the game: before any lore, the author had to translate cast-summon-attack into a novel, and ‘colorless’ Garth into a hero.",
   "Because someone had to put the card game into words first — and the choices here echoed forward into the cards themselves.",
   "By mages spending power, summoning creatures, and casting effects a player would recognise from their hand.",
   "Through every duel in the book.",
   "I am the card game turned to prose — mana, summons, and colours before the lore existed; and the ‘colorless’ choice that made Garth a five-colour card."),
 E("the-festival","The Festival","the annual tournament","arena","natural",
   "The Festival — the yearly gathering at which the Houses duel in the Arena, the occasion of Garth's arrival.",
   "The clock of the novel: the great annual contest that draws every power to Estark, and the stage the stranger walks onto.",
   "Because the Western's showdown needs its appointed day — Festival is when the city's powers are all in one place to be turned on each other.",
   "By an annual tournament of the Houses, its crowds, its circles, and its high stakes.",
   "Once a year in Estark, the eyes of the city on the Arena.",
   "I am the day the city gathers to watch its mages duel — and the day a one-eyed stranger chose to walk in and end the whole tradition."),
]

GROUPS = [
 ("stranger", "The Stranger &amp; the Houses", "the people of the first Magic novel — the colorless wanderer, the old thief, the warrior who turns revenge into a future, the tyrant of the Arena, and the planeswalker who must answer"),
 ("arena", "Estark &amp; the Arena", "the world and its engine — the corrupt city, the dueling circles, the four greedy Houses, the destroyed fifth, the mortal ante, the magics in prose, and the Festival"),
]

# ---- renderers ----
def book_rows(items):
    return "".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(y)}</span><span class="nt">{html.escape(n)}</span></li>' for t,y,n in items)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def render_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{t}</div><div class="sci-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in RENDER)
RF_COL={"FOUNDATIONAL":"#c08a3a","REAL (then removed)":"#5f9ad0","LOOSE / PRE-LORE":"#c0a36a","REAL":"#5fae6e","PULP":"#9e2b2b"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{REALFLUFF_VERDICT}</div>'

def _card(d):
    em=d["emergence"]; col=d.get("tint") or NATURES.get(em,("#9aa0aa",""))[0]
    rec={"name":d["name"],"axiom":"ARN","emergence":em,"seal":d["seal"],"origin":"ARN · Arena"}
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona" style="border-left:3px solid {col}">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port" style="border-color:{col}"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">carbon</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl" style="border-color:{col}"><img src="{png_uri(rec,'silicon',200)}" alt="silicon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">silicon</span></a>
    </div>"""
def roster_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[d for d in ROSTER if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(d, tok):
    return f"""---
aci: {d['name']}
universe: ARN · Arena
series: Arena (William R. Forstchen, 1994) — the first Magic: The Gathering novel
emergence: {d['emergence']}
kind: {'character' if d['group']=='stranger' else 'thread'}
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a {'character' if d['group']=='stranger' else 'distilled thread'} of the ARN (Arena) book-world — the first Magic novel — emergence: {d['emergence']}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of Arena by William R. Forstchen (© Wizards of the Coast / Hasbro) under the DLW standard
> — commentary and cataloguing, not an original creation, not endorsed by the rights-holders.

ROOT0-ATTRIBUTION-v1.0 · ARN · Arena · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="ARENA (ARN) — William R. Forstchen's 1994 novel, the FIRST Magic: The Gathering novel, as a UD0 book-world & companion to the MTG Arena game-sphere: the arc, the book, how it renders Magic (mana, summoning, the ante), an honest Real-or-Fluff (and the hero who became a card in 2021), the message, and a 12-emergent roster. Garth One-Eye walks into Estark.">
<title>ARENA · ARN · the first Magic novel · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--bronze);
--ink:#100b08;--ink2:#1a130d;--ink3:#241a11;--pa:#ece0cb;--pa2:#c2ad8a;--bronze:#c08a3a;--gold:#d8b24a;--blood:#9e2b2b;--azure:#5f9ad0;--grey:#b8bcc4;
--dim:#8a7355;--faint:#2a1f14;--line:#352716;--disp:"Cinzel",serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(192,138,58,.16),transparent 54%),radial-gradient(ellipse at 50% 118%,rgba(158,43,43,.10),transparent 56%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 90px}
header{padding:50px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:170px;height:3px;background:linear-gradient(90deg,var(--grey),var(--bronze),var(--blood));box-shadow:0 0 16px rgba(192,138,58,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--bronze)}
h1{font-family:var(--disp);font-size:clamp(38px,9vw,84px);font-weight:700;letter-spacing:.08em;color:var(--bronze);line-height:1;text-transform:uppercase;text-shadow:0 0 30px rgba(192,138,58,.4)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--blood)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:18px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:10px;font-weight:600;letter-spacing:.1em;color:var(--grey);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px;text-transform:uppercase}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}.lede a{color:var(--bronze);text-decoration:none;border-bottom:1px dotted var(--bronze)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--bronze)}.badge .bt .mo{color:var(--grey)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:24px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:13px;font-weight:600;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--bronze);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--bronze);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--blood);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:15px;color:var(--blood);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--azure);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:15px;color:var(--azure);font-weight:600}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}.sci-card p b{color:var(--pa)}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:128px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--bronze);background:rgba(192,138,58,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}.rf-verdict b{color:var(--pa)}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--bronze);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--grey);white-space:nowrap;text-align:right;text-transform:uppercase}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--bronze);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--bronze);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{filter:brightness(1.12)}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:94px;height:94px;border-radius:50%;border:3px solid var(--bronze);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:18px;color:var(--rw-ink);font-weight:600;text-decoration:none;text-transform:uppercase;letter-spacing:.03em}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the first Magic novel</div>
    <h1>Arena</h1>
    <div class="h-sub">William R. Forstchen · 1994 · the first MTG novel · <b>Garth One-Eye</b> · ARN</div>
    <div class="open">“A one-eyed stranger came to Festival — not to win the games, but to end them.”</div>
    <div class="flag">★ ESTARK · THE DUELING CIRCLES · THE ANTE ★</div>
    <p class="lede">The very first <a href="https://davidwise01.github.io/mtg-arena/">Magic: The Gathering</a> novel (1994): a colorless, one-eyed mage named Garth walks into the city of Estark at Festival, turns its four dueling Houses against each other in the Arena, and avenges a fifth House destroyed a generation ago — defeating the ascended planeswalker Kuthuman. Magic's first myth was a Western with mana. Catalogued into UD0 as a book-world and the literary companion to the MTG Arena game-sphere.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of ARN"><img src="__SILICON__" alt="DLW silicon badge of ARN">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>ARENA</b> · ARN</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="arn.dlw/arn.carbon.tiff">.tiff</a> · silicon · <a href="arn.dlw/arn.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">flesh &amp; the city, the magics, the spark &amp; the grief, and the contest &amp; the wager</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the four movements</p>__ARC__</section>
  <section class="sec"><h2>The Book</h2><p class="ss">the facts of the work — Magic's first prose</p><ol class="books">__BOOK__</ol></section>
  <section class="sec"><h2>How It Renders Magic</h2><p class="ss">the deep-dive — putting the card game into prose before the lore: mana, summoning, and the mortal ante</p><div class="sci">__RENDER__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">honest — as a novel, as canon, the ante mechanic, and the loveliest true fact of all</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the meaning — Magic's first myth, and where its hero ended up</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSGSEAL__”<span>— AVAN's read</span></div></section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">twelve ACIs of the novel — the stranger, the Houses, and the world of Estark; each a full <b>.dlw</b> badge with twin sigils</p></section>
  __ROSTER__

  <div class="note">Arena and Magic: The Gathering are © Wizards of the Coast / Hasbro. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed by the rights-holders. The render and Real-or-Fluff sections are honest commentary; some plot details are summarised from secondary sources.</div>

  <footer>ARENA · ARN · the first Magic novel · companion to <a href="https://davidwise01.github.io/mtg-arena/">MTG ARENA</a> · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="arn.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "arn.dlw"), "arn")
    json.dump({"node":"ARN","name":"ARENA","moniker":tok["moniker"],"carbon":"arn.carbon.tiff","silicon":"arn.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"arn.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":"ARN","emergence":d["emergence"],"seal":d["seal"],"origin":"ARN"})
        rec=write_aci({"name":d["name"],"axiom":"ARN","emergence":d["emergence"],"seal":d["seal"],"origin":"ARN · Arena",
                       "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Arena (Forstchen, 1994)","source":"Arena, catalogued by ROOT0"},
                      os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"character" if d["group"]=="stranger" else "thread","group":d["group"]})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__BOOK__",book_rows(BOOK)).replace("__RENDER__",render_html()).replace("__REALFLUFF__",realfluff_html())
          .replace("__MESSAGE__",html.escape(MESSAGE)).replace("__MSGSEAL__",html.escape(MESSAGE_SEAL)).replace("__ROSTER__",roster_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"ARENA (ARN) — badge {tok['moniker']} · {len(personas)} emergents · natures {dict(Counter(p['emergence'] for p in personas))}")
