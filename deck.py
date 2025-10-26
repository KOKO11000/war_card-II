import random
optional_suitses=["H","C","D","S"] 
ranks = {
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":11,
        "Q":12,
        "K":13,
        "A":14,
    }
def create_card(rank:str,suite:str) -> dict:
    if (rank not in ranks or suite not in optional_suitses):
        return None
    return{
        "rank":rank,
        "suite":suite,
        "value":ranks[rank]
    }



def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if ("value" not in p1 or "value" not in p2):
        return None
    p1 = p1_card["value"]
    p2 = p2_card["value"]

    if p1 > p2:
        return "p1"
    elif p2 > p1:
        return "p2"   
    return "WAR"
    

def create_deck() -> list[dict]:
    full_deck = []
    for i in ranks:
        for j in optional_suitses:
            if (full_deck != None):
                full_deck.append(create_card(i, j))           
    return full_deck


def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        while True:

            index1 = random.randint(0,len(deck))
            index2 = random.randint(0,len(deck))
            if(index1 != index2):
                break
            tmp_card = deck[index2]
            deck[index2] = deck[index1]
            deck[index1] = tmp_card
    return deck
print(shuffle(create_deck()))

def create_player(name:str) -> dict:
    return {
        "name": name,
        "hand": [],
        "won_pile": []
    }

def init_game() -> dict:
    player1 = create_player("Netanel")
    player2 = create_player()
    deck = create_deck()
    shuffle(deck)
    player1["hand"] = deck[:26]
    player2["hand"] = deck[26:]
    return {
        "deck":deck,
        "player1": player1,
        "player2": player2
    }
    
