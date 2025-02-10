import random

# تعريف القيم الرقمية للأوراق
cards = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]
}

# إنشاء مجموعة أوراق اللعب (بدون الجوكر)
deck = list(cards.keys()) * 4  # تكرار كل ورقة 4 مرات (كأننا نستخدم مجموعة أوراق واحدة)
random.shuffle(deck)  # خلط الأوراق

# توزيع الورقتين الأوليتين لكل لاعب والموزع
def deal_initial_cards(num_players=2):
    players = {f'Player {i+1}': [deck.pop(), deck.pop()] for i in range(num_players)}
    dealer = [deck.pop(), deck.pop()]
    return players, dealer

# حساب قيمة اليد مع التعامل مع الآس (A) بشكل ديناميكي
def calculate_hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
            aces += 1
        else:
            total += cards[card]
    
    # التعامل مع الآس
    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    
    return total

# تشغيل اللعبة
def play_blackjack(num_players=2):
    players, dealer = deal_initial_cards(num_players)
    
    # طباعة الأوراق الموزعة
    for player, hand in players.items():
        print(f"{player}: {hand} (Total: {calculate_hand_value(hand)})")
    print(f"Dealer: [{dealer[0]}, ?] (Second card hidden)")
    
    return players, dealer

# تشغيل المحاكاة
players, dealer = play_blackjack()

