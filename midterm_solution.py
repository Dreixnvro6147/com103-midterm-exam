heroes = [
    ("Layla", "Marksman"),
    ("Tigreal", "Tank"),
    ("Gusion", "Assassin"),
    ("Kagura", "Mage"),
    ("Chou", "Fighter")
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\n=========================================")
print("MOBILE LEGENDS -- HERO ROSTER")
print("=========================================")

for i in range(len(heroes)):
    print(f"{i+1}. {heroes[i][0]} [{heroes[i][1]}]")

print("=========================================")

matches = []
wins = 0
losses = 0

for match_num in range(1, 5):
    print(f"\n--- MATCH {match_num} ---")
    hero_num = int(input("Hero number (0 to skip): "))

    if hero_num == 0:
        print("Match skipped.")
        continue

    if 1 <= hero_num <= 5:
        hero_name = heroes[hero_num - 1][0]

        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ")

        if deaths == 0:
            deaths = 1
        kda = (kills + assists) / deaths

        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        if result == "W":
            wins += 1
        else:
            losses += 1

        matches.append({
            "hero": hero_name,
            "kda": kda,
            "result": result,
            "tag": tag
        })

matches_played = len(matches)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
    best_match = max(matches, key=lambda x: x["kda"])
    best_index = matches.index(best_match) + 1
else:
    win_rate = 0
    best_match = None

print("\n=========================================")
print(f"{ign} -- MATCH LOG ({rank})")
print("=========================================")

for i, m in enumerate(matches, start=1):
    result_word = "WIN" if m["result"] == "W" else "LOSS"
    print(f"[{i}] {m['hero']} | KDA: {m['kda']:.2f} | {result_word} | {m['tag']}")

print("-----------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins} | Losses : {losses}")
print(f"Win Rate : {win_rate}%")

if best_match:
    print(f"Best Match : [{best_index}] {best_match['hero']} (KDA: {best_match['kda']:.2f})")

print("=========================================")heroes = [
    ("Layla", "Marksman"),
    ("Tigreal", "Tank"),
    ("Gusion", "Assassin"),
    ("Kagura", "Mage"),
    ("Chou", "Fighter")
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\n=========================================")
print("MOBILE LEGENDS -- HERO ROSTER")
print("=========================================")

for i in range(len(heroes)):
    print(f"{i+1}. {heroes[i][0]} [{heroes[i][1]}]")

print("=========================================")

matches = []
wins = 0
losses = 0

for match_num in range(1, 5):
    print(f"\n--- MATCH {match_num} ---")
    hero_num = int(input("Hero number (0 to skip): "))

    if hero_num == 0:
        print("Match skipped.")
        continue

    if 1 <= hero_num <= 5:
        hero_name = heroes[hero_num - 1][0]

        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ")

        if deaths == 0:
            deaths = 1
        kda = (kills + assists) / deaths

        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        if result == "W":
            wins += 1
        else:
            losses += 1

        matches.append({
            "hero": hero_name,
            "kda": kda,
            "result": result,
            "tag": tag
        })

matches_played = len(matches)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
    best_match = max(matches, key=lambda x: x["kda"])
    best_index = matches.index(best_match) + 1
else:
    win_rate = 0
    best_match = None

print("\n=========================================")
print(f"{ign} -- MATCH LOG ({rank})")
print("=========================================")

for i, m in enumerate(matches, start=1):
    result_word = "WIN" if m["result"] == "W" else "LOSS"
    print(f"[{i}] {m['hero']} | KDA: {m['kda']:.2f} | {result_word} | {m['tag']}")

print("-----------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins} | Losses : {losses}")
print(f"Win Rate : {win_rate}%")

if best_match:
    print(f"Best Match : [{best_index}] {best_match['hero']} (KDA: {best_match['kda']:.2f})")

print("=========================================")
