def drunkard_game(boris_cards, nursik_cards):
    boris = list(boris_cards)
    nursik = list(nursik_cards)
    moves = 0
    
    while boris and nursik and moves < 1_000_000:
        moves += 1
        b = boris.pop(0)
        n = nursik.pop(0)

        if (b == 0 and n == 9) or (b > n and not (b == 9 and n == 0)):
            boris.append(b)
            boris.append(n)
        else:
            nursik.append(b)
            nursik.append(n)
    
    if not boris:
        print(f"Nursik {moves}")
    elif not nursik:
        print(f"Boris {moves}")
    else:
        print("blin nichya")

boris_cards = list(map(int, input().split()))
nursik_cards = list(map(int, input().split()))
drunkard_game(boris_cards, nursik_cards)
