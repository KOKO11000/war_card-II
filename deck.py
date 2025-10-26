optional_suitses=["H","C","D","S"] 
def create_card(rank:str,suite:str) -> dict:
    ranks = {
        "1":1,
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
    pass
def shuffle(deck:list[dict]) -> list[dict]:
    pass
