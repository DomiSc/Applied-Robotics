from pyniryo import *
import camera_test
import voice1
import numpy as np

# Connecting to Niryo
n = NiryoRobot("10.10.10.10")
n.calibrate(CalibrateMode.AUTO)
# player card position
position_counter = np.array([0, 0, 0, 0, 0])
# first row player points second row ace counter
point_counter = np.array([[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]])
# first row position unused chips second row position player chips
chip_counter = np.array([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
# worth of the bets
bet_counter = np.array([0, 0, 0, 0])


def players():
    while True:
        print("Anzahl der Spieler Festlegen (1, 2 oder 3):")
        key = input()
        if key in ("1", "2", "3"):
            amount_player = int(key)
            print(amount_player, "Spieler")
            return amount_player
        else:
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 3 eingeben.")


def turn_order(amount_player):
    global point_counter, bet_counter
    out_player = np.array([0, 0, 0])
    for i in range(amount_player, 0, -1):
        bet_counter[i] = make_bet(i)
    for i in range(2):
        for j in range(amount_player, 0, -1):
            new_values = draw_phase(j)
            point_counter[0][j] += new_values[0]
            print("Player", j, "has", point_counter[0][j], "points")
            point_counter[1][j] += new_values[1]
            if not check_points(point_counter[0][j], point_counter[1][j], j):
                out_player[j-1] = j
        new_values = draw_phase(4)
        point_counter[0][4] += new_values[0]
        print("dealer has", point_counter[0][4])
        point_counter[1][4] += new_values[1]
        check_points(point_counter[0][4], point_counter[1][4], 4)
    for i in range(amount_player, 0, -1):
        if out_player[i-1] != i:
            player_hitostand_phase(i)
    dealer_finish()
    compare_points(amount_player)
    print("Spiel beendet.")


def check_ace(points):
    if points == 1:
        return 11, 1
    else:
        return points, 0


def draw_phase(amount_player):
    give_card()
    points = camera_test.detect_card()
    print("Player", amount_player, "has drawn a", points)
    if amount_player == 4:
        place_card(0, amount_player, position_counter[amount_player])
        position_counter[amount_player] += 1
    else:
        place_card(1, amount_player, position_counter[amount_player])
        position_counter[amount_player] += 1
    return check_ace(points)


def player_hitostand_phase(amount_player):
    global point_counter
    var = True
    while var:
        voice = voice1.recognize_speech_offline()
        if voice == "hit":
            print("Hit")
            new_values = draw_phase(amount_player)
            point_counter[0][amount_player] += new_values[0]
            print("Spieler ", amount_player, "hat ", point_counter[0][amount_player])
            point_counter[1][amount_player] += new_values[1]
            var = check_points(point_counter[0][amount_player], point_counter[1][amount_player], amount_player)
        elif voice == "stand":
            print("Stand")
            var = False


def dealer_finish():
    global point_counter
    turn_card()
    while point_counter[0][4] < 16:
        check_points(point_counter[0][4], point_counter[1][4], 4)
        new_values = draw_phase(4)
        point_counter[0][4] += new_values[0]
        point_counter[1][4] += new_values[1]
        print("Dealer has ", point_counter[0][4], "points")


def make_bet(amount_player):
    while True:
        try:
            print("Enter bet for player:", amount_player)
            key = int(input())
            if key >= 0:
                break
            else:
                print("Bet must be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    split_bet(key, amount_player)
    print("Player ", amount_player, "has bet", key)
    return key


def split_bet(key, amount_player):
    # black
    chip = key % 100
    buffer = (key - chip) / 100
    if int(buffer) != 0:
        place_bet(int(buffer), 0, amount_player)
    # green
    key = chip % 25
    buffer = (chip - key) / 25
    if int(buffer) != 0:
        place_bet(int(buffer), 1, amount_player)
    # blue
    chip = key % 10
    buffer = (key - chip) / 10
    if int(buffer) != 0:
        place_bet(int(buffer), 2, amount_player)
    # red
    key = chip % 5
    buffer = (chip - key) / 5
    if int(buffer) != 0:
        place_bet(int(buffer), 3, amount_player)
    # white
    place_bet(key, 4, amount_player)


def check_points(points, ace, amount_player):
    global point_counter, bet_counter
    if points > 21:
        if ace >= 1:
            points -= 10
            ace -= 1
            point_counter[0][amount_player] = points
            point_counter[1][amount_player] = ace
            print("über 21! Punkte werden angepasst. Neuer Punktestand:", points)
            if points == 21:
                split_bet(bet_counter[amount_player], amount_player)
                point_counter[0][amount_player] = 0
                print("Black Jack Player", amount_player, "wins:", bet_counter[amount_player])
                return False
        else:
            point_counter[0][amount_player] = 0
            print("Player", amount_player, "has lost")
            return False
    if points == 21:
        split_bet(bet_counter[amount_player], amount_player)
        point_counter[0][amount_player] = 0
        print("Black Jack Player", amount_player, "wins:", bet_counter[amount_player])
        return False

    return True


def compare_points(amount_player):
    global point_counter, bet_counter
    for i in range(amount_player, -1, -1):
        if point_counter[0][i] != 0:

            if point_counter[0][4] < point_counter[0][i]:
                split_bet(bet_counter[amount_player], amount_player)
                print("player", amount_player, "wins:", bet_counter[amount_player]*2)
            else:
                print("player", amount_player, "has lost")


# turn card i.o.
def turn_card():
    n.move_joints(-1.04, -0.178, -0.993, -0.106, 1.339, -1.497)
    n.move_joints(-1.217, -0.994, 0.184, -0.396, 0.65, -1.377)
    n.close_gripper(500, 100, 100)
    n.move_joints(-1.153, -0.323, -0.389, -0.181, 0.612, -1.385)
    n.move_joints(-1.151, -0.317, -0.399, -0.209, 0.615, 1.692)
    n.move_joints(-1.215, -0.99, 0.133, -0.362, 0.793, 1.764)
    n.open_gripper(500, 100, 100)
    n.move_joints(-1.214, -0.175, -1.049, -0.334, 1.028, 1.692)


def give_card():
    n.move_joints(-0.174, -0.094, -0.798, 0.261, 0.702, 1.322)
    n.open_gripper(500, 100, 100)
    n.move_joints(-0.393, -0.863, -0.017, -0.149, 0.643, 1.6641)
    n.move_joints(-0.346, -0.985, 0.152, 0.057, 0.782, 1.46)
    n.close_gripper(500, 100, 100)
    n.move_joints(-0.393, -0.863, -0.017, -0.149, 0.643, 1.664)
    n.move_joints(-0.174, -0.094, -0.798, 0.261, 0.702, 1.322)


def place_card(player_dealer, amount_player, pos):
    amount_player -= 1
    card_position = [
        [[-2.087, -0.837, -0.305, 0.368, 1.124, -1.733],
         [-2.338, -0.787, -0.396, 0.081, 1.107, -1.606],
         [-2.574, -0.735, -0.433, -0.15, 1.031, -1.512],
         [-2.827, -0.755, -0.305, -0.523, 0.857, -1.397]],

        [[2.538, -0.991, -0.096, 0.391, 0.937, -1.798],
         [2.311, -0.952, -0.201, 0.129, 1.018, -1.644],
         [2.087, -0.982, -0.222, -0.087, 1.117, -1.555],
         [1.8, -1.026, -0.086, -0.463, 1.038, -1.454]],

        [[0.753, -0.881, 0.075, -0.078, 0.589, -1.42],
         [0.607, -0.869, 0.095, -0.187, 0.454, -1.419],
         [0.412, -0.902, 0.152, -0.497, 0.518, -1.195],
         [0.258, -1.006, 0.257, -0.523, 0.701, -1.201]],

        [[-1.202, -1.079, 0.255, -0.365, 0.834, 1.826],
         [-1.007, -0.952, 0.046, -0.07, 0.782, -1.589],
         [-0.826, -0.963, 0.064, 0.112, 0.762, -1.637],
         [-0.622, -1.028, 0.205, 0.427, 0.761, -1.795]]
    ]

    pre_position = [[-2.419, -0.358, -1.172, 0.068, 1.391, -1.585],
                    [2.11, -0.463, -1.152, -0.129, 1.465, -1.506],
                    [0.537, -0.228, -0.613, -0.092, 0.784, -1.583],
                    [-1.04, -0.178, -0.993, -0.106, 1.339, -1.497]]

    if player_dealer == 0 and pos == 0:
        # posi 1 Dealer
        print("Placing card for Dealer at Position 1")
        n.move_joints(card_position[amount_player][pos])  # Platz an den die Karte gelegt wird
        n.open_gripper(500, 100, 100)
        n.move_joints(pre_position[amount_player])

    elif player_dealer == 0 and pos >= 1:
        # posi 2 Dealer
        print("Placing card for Dealer")
        n.move_joints(-0.179, -0.108, -0.816, 0.198, 0.793, -1.805)  # Karte wird gedreht
        n.move_joints(card_position[amount_player][pos])
        n.open_gripper(500, 100, 100)
        n.move_joints(pre_position[amount_player])  # Arm fährt zurück

    elif player_dealer == 1:
        n.move_joints(-0.179, -0.108, -0.816, 0.198, 0.793, -1.805)
        n.move_joints(pre_position[amount_player])
        # Karte wird gedreht
        n.move_joints(card_position[amount_player][pos])
        n.open_gripper(500, 100, 100)
        n.move_joints(pre_position[amount_player])  # Arm fährt zurück
        n.move_joints(-0.179, -0.108, -0.816, 0.198, 0.793, -1.805)


def place_bet(amount, value, amount_player):
    global chip_counter
    amount_player -= 1
    position_pickup = [
        [[-1.308, -0.402, -1.029, -0.403, -0.023, -0.017],
         [-1.55, -0.437, -0.937, -0.675, -0.025, -0.017]],

        [[-0.599, -0.41, -1.04, 0.345, -0.02, -0.017],
         [-0.917, -0.367, -1.096, -0.067, -0.023, -0.017]],

        [[-0.715, -0.569, -0.719, 0.143, 0.014, -0.017],
         [-0.976, -0.537, -0.773, -0.061, 0.005, -0.017],
         [-1.209, -0.566, -0.719, -0.345, -0.008, -0.017],
         [-1.407, -0.629, -0.604, -0.52, -0.002, -0.015]],

        [[-0.753, -0.696, -0.46, 0.072, 0.052, -0.017],
         [-0.949, -0.673, -0.492, -0.06, 0.051, -0.017],
         [-1.159, -0.7, -0.46, -0.271, 0.052, -0.017],
         [-1.325, -0.76, -0.367, -0.425, 0.047, -0.017]],

        [[-0.753, -0.914, 0.03, -0.07, -0.282, 0.259],
         [-0.955, -0.864, -0.148, 0.008, 0.067, -0.017],
         [-1.112, -0.903, -0.083, -0.196, 0.064, -0.017],
         [-1.252, -0.947, -0.01, -0.321, 0.058, -0.017]]
    ]

    position_player = [
        [[-2.014, -0.897, -0.154, 0.741, 0.251, -0.432],
         [-2.136, -0.878, -0.33, 0.502, 0.515, -0.175],
         [-2.319, -0.803, -0.396, 0.319, 0.405, -0.167],
         [-2.494, -0.843, -0.405, 0.226, 0.526, -0.207]],

        [[2.492, -1, 0.193, 0.279, -0.373, -0.19],
         [2.303, -0.922, 0.061, 0.135, -0.379, -0.19],
         [2.118, -0.922, 0.069, 0.009, -0.384, -0.19],
         [1.937, -0.976, 0.16, -0.161, -0.388, -0.19]],

        [[0.868, -1.15, 0.276, 0.23, 0.166, -0.196],
         [0.667, -1.097, 0.217, 0.175, 0.06, -0.245],
         [0.5, -1.093, 0.217, 0.011, 0.078, -0.175],
         [0.322, -1.19, 0.304, -0.046, 0.294, -0.11]],
    ]

    preposition_player = [
        [-2.494, -0.135, -1.219, 0.075, 0.149, -0.19],
        [2.183, 0.154, -1.111, 0.112, -0.379, -0.19],
        [0.591, -0.363, -0.792, 0.017, 0.497, -0.159],
        [-0.964, 0.054, 0.186, 0.026, -0.279, -0.19]
    ]

    for i in range(amount):
        print("placing Chip")
        n.open_gripper(500, 100, 100)
        n.move_joints(preposition_player[3])  # vorposition aufheben
        n.move_joints(position_pickup[value][chip_counter[0][value]])
        n.close_gripper(500, 100, 100)
        n.move_joints(preposition_player[3])
        n.move_joints(preposition_player[amount_player])
        n.move_joints(position_player[amount_player][chip_counter[1][amount_player]])
        n.open_gripper(500, 100, 100)
        n.move_joints(preposition_player[amount_player])  # reset position
        chip_counter[0][value] += 1
        chip_counter[1][amount_player] += 1


turn_order(players())
