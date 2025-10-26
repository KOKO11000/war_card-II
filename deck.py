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
    if ("value" not in p1_card or "value" not in p2_card):
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
        while(True):
            index1 = random.randint(0,len(deck) - 1)
            index2 = random.randint(0,len(deck) - 1)
            if(index1 != index2):
                break
            tmp_card = deck[index2]
            deck[index2] = deck[index1]
            deck[index1] = tmp_card
    return deck


def create_player(name:str = "AI") -> dict:
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
    
def play_round(player1: dict, player2: dict) -> None:
    p1_card = player1["hand"].pop()
    p2_card = player2["hand"].pop()
    result_compare = compare_cards(p1_card,p2_card)
    if(result_compare == "p1"):
        player1["won_pile"].append(p1_card)
        player1["won_pile"].append(p2_card)
    elif (result_compare == "p2"):
        player2["won_pile"].append(p2_card)
        player2["won_pile"].append(p1_card)
    print(result_compare, "win this round")


def log_winner(p1_won_pile:list,p2_won_pile:list):
    len_p1 = len(p1_won_pile)
    len_p2 = len(p2_won_pile)
    if (len_p1 > len_p2):
        print("p1 the winner")
    elif (len_p1 < len_p2):
        print("p2 the winner")
    else:
        print("Equal!")


if (__name__ == "__main__"):
    game_dict = init_game()
    while(len(game_dict["player1"]["hand"]) > 0 and len(game_dict["player2"]["hand"]) > 0 ):
        play_round(game_dict["player1"], game_dict["player2"])
    log_winner(game_dict["player1"]["won_pile"], game_dict["player2"]["won_pile"])