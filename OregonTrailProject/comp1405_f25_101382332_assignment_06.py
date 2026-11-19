from updated_base_module_for_101382332 import *
import random
import sys
import json

# Find index
def find_substring(text, target):
    # Loop over each possible starting index
    for i in range(len(text) - len(target) + 1):
        # Check if the slice of text starting at i matches the target
        if text[i:i+len(target)] == target:
            # Found the target, return the index
            return i
    # Target not found, return -1
    return -1  

# To replace RANDOM_NAME with an actual name of someone from the party with slice
def replace_random_name(event_text, name):
    # Find 'RANDOM_NAME'
    idx = find_substring(event_text, "RANDOM_NAME")
    if idx == -1:
        # If not found, return original text
        return event_text
    
    # Slice before + name + slice after
    return event_text[:idx] + name + event_text[idx + len("RANDOM_NAME"):]

# Capitalize words
def fix_capitalization(text):
    # Make everything lowercase first
    text = text.lower()
    result = ""
    # Flag to capitalize next character
    capitalize_next = True

    # Initialize loop counter
    i = 0
    # Loop through each character in the text
    while i < len(text):
        # Get the current character
        ch = text[i]

        # If character is a letter and need to capitalize it
        if ch.isalpha() and capitalize_next:
            # Convert lowercase letter to uppercase and add to result
            result += chr(ord(ch) - 32)
            # Reset capitalize flag
            capitalize_next = False
        else:
            # Add character as is to result
            result += ch

        # If character is space or hyphen next letter should be capitalized
        if ch.isspace() or ch == "-":
            capitalize_next = True

        # Move to the next character
        i += 1
        # Return corrected string
    return result

def clean_name_input(name: str) -> str:
    # Strip non-alphabetic characters from the ends
    while len(name) > 0 and not (name[0].isalpha() or name[0] in "-/"):
        name = name[1:]

    while len(name) > 0 and not (name[-1].isalpha() or name[-1] in "-/"):
        name = name[:-1]

    return name

# Intro function
def print_game_intro() -> None:
    
    splash_screen()

    # Just prints text
    print()
    print("Welcome to A Path to Prosper!")
    print()
    print("This game is inspired by \"The Oregon Trail\".")
    print("Your objective is to go on a 3 week road trip through 10 cities/towns to successfully reach a new recently booming market called \"Golden Wind\" \nto sell meals, trade, and teach about food preparation.")
    print("You are the leader of your group; you'll lead and navigate through any obstacles or special events that you may encounter along the way \nwith your party of 5.")
    print("You and your group are going there to build a name and make a profit because the market is full of opportunities to prosper.")
    print("Face obstacles, make strategic choices, and survive the journey to potentially prosper!\n")

    # Yes/No to learn more about narrative
    learn_more = input("Would you like to learn more about some of the narrative? (Yes/No): ")
    # Prints narrative
    if learn_more.lower() == "yes" or learn_more.lower() == "y":
        print("\nIt's finally happening! You and your team of five are hitting the road in a kind of rustic food truck, chasing the dream of success in the new booming market called \"Golden Wind\".")
        print("Over the next 3 weeks, you'll travel through 10 cities, cooking, trading, and surviving whatever the road throws your way.")
        print()
        print("Sounds simple? It depends. It is a straightforward adventure, but challenges may or may not occur.")
        print("Food supplies dwindle, plrenty of fuel is burned through quick, a bad stretch of weather, or a busted tire could ruin your trip.")
        print("Each day, your team needs a variety of foods — proteins, grains, veggies, dairy, seafood — to stay healthy and strong.")
        print("Miss a few meals or stick to just one food group too long, and your crew's health and morale takes a dive.")
        print("You must not forget to rest as well! Going too long without some rest, and your team gets tired, increasing the chance of breakdowns or even serious accidents.")
        print()
        print("But it's not all terrible, you and your team has skills. With the right ingredients, you can cook meals and sell them for cash.")
        print("You can also hunt or forage for food, of course with a cost.")
        print()
        print("At gas station, you may need to refuel, repair your truck, or stock up on snacks and spare parts. Running out of fuel will leave you stranded!")
        print()
        print("Choose wisely: What do you need to buy? How to manage your supplies? What will you do when you face a challenge?")
        print("Lead your crew smartly, and you will potentially arrive closer to your dream. Play it reckless, and your trip might end before you even see the market.\n")
    else:
        print("\nSkipping narrative intro.\n")

# Splash Screen/Title
def splash_screen() -> None:
    open_win("A Path to Prosper - Title Screen")  # Open window
    fill_win(18, 83, 89)  # Fill background
    draw_border()  # Draw border
    draw_game_title("A Path to Prosper")  # Draw title text
    hold_win(50)  # Hold the window for display

# Border Deco
def draw_border() -> None:

    # Rectangles of the border (Squares)
    draw_rect((105, 125, 15, 15), (245, 211, 176), 4)  # Top left
    draw_rect((525, 125, 15, 15), (245, 211, 176), 4)  # Top right
    draw_rect((105, 215, 15, 15), (245, 211, 176), 4)  # Bottom left
    draw_rect((525, 215, 15, 15), (245, 211, 176), 4)  # Bottom right

    # Border lines
    draw_line((123, 137), (521, 137), (245, 211, 176), 4)  # Top Inner
    draw_line((123, 126), (521, 126), (245, 211, 176), 4)  # Top Outer
    draw_line((124, 216), (520, 216), (245, 211, 176), 4)  # Bottom Inner
    draw_line((124, 227), (520, 227), (245, 211, 176), 4)  # Bottom Outer
    draw_line((117, 144), (117, 210), (245, 211, 176), 4)  # Left Inner
    draw_line((107, 144), (107, 210), (245, 211, 176), 4)  # Left Outer
    draw_line((526, 144), (526, 210), (245, 211, 176), 4)  # Right Inner
    draw_line((536, 144), (536, 210), (245, 211, 176), 4)  # Right Outer

# Game Title
def draw_game_title(title: str) -> None:
    draw_text(title, (245, 211, 176), 160)  # Draw title text in window

# Character Class Selection
def class_selection() -> tuple[int, float, str]:
    while True:
        print("\nChoose your character class:")
        print("1. Chef (Changes related to meals that you can create)")
        print("2. Vendor (Changes related to purchases/customers)")
        class_choice = input("Enter 1 or 2: ")

        if class_choice == "1":
            character_class = 1
            money = 1000.0  # Chef starting money
            while True:
                print("\nChoose a specialization:")
                print(f"1. Resourceful Cook: 10% chance to create 1-3 extra meals")
                print("2. Gourmet Chef: Meals sell for $15 more")
                subclass = input("Enter 1 or 2: ")
                if subclass == "1":
                    print(f"\nYour chosen class: {character_class}")
                    print(f"Your subclass: {subclass}")
                    print(f"Your money: {money}\n")
                    return character_class, money, "Resourceful Cook"
                elif subclass == "2":
                    print(f"\nYour chosen class: {character_class}")
                    print(f"Your subclass: {subclass}")
                    print(f"Your money: {money}\n")
                    return character_class, money, "Gourmet Chef"
                else:
                    print("Invalid input. Please choose 1 or 2.")
        elif class_choice == "2":
            character_class = 2
            money = 1200.0  # Vendor starting money
            while True:
                print("\nChoose a specialization:")
                print(f"1. Human Megaphone: 50% increased chance of attracting customers")
                print("2. Cheap Master: Reduce market prices by 15%")
                subclass = input("Enter 1 or 2: ")
                if subclass == "1":
                    print(f"\nYour chosen class: {character_class}")
                    print(f"Your subclass: {subclass}")
                    print(f"Your money: {money}\n")
                    return character_class, money, "Human Megaphone"
                elif subclass == "2":
                    print(f"\nYour chosen class: {character_class}")
                    print(f"Your subclass: {subclass}")
                    print(f"Your money: {money}\n")
                    return character_class, money, "Cheap Master"
                else:
                    print("Invalid input. Please choose 1 or 2.")
        else:
            print("Invalid input. Please choose 1 or 2.")       

# Starting Location Selection
def starting_location() -> str:

    # Flag to control the input loop
    valid_location_selected = False
    # Variable to store the chosen location
    location = ""

    # Loop until the user selects a valid location
    while not valid_location_selected:
        # Display location options
        print("Choose your starting location:")
        print("1. Coral Bay")
        print("2. Spiceport Haven")
        print("3. Verdant Grasslands\n")

        # Get user input for location selection
        start_choice = input("Enter the number of your starting location (1-3): ")

        if start_choice == "1":
            location = "Coral Bay"  # Set location
            valid_location_selected = True  # Exit main loop

            # Ask if user wants more info, with validation loop
            while True:
                more_info = input("Would you like to learn more about Coral Bay? (Yes/No): ")
                if more_info.lower() in ["yes", "y"]:
                    print("\nCoral Bay is a serene coastal town known for its fresh seafood and artisanal food markets.")
                    break  # Exit info loop
                elif more_info.lower() in ["no", "n"]:
                    break  # Exit info loop
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
        elif start_choice == "2":
            location = "Spiceport Haven"  # Set location
            valid_location_selected = True  # Exit main loop

            while True:
                more_info = input("Would you like to learn more about Spiceport Haven? (Yes/No): ")
                if more_info.lower() in ["yes", "y"]:
                    print("\nSpiceport Haven is a bustling trade city with flavors and visitors from around the world.")
                    break
                elif more_info.lower() in ["no", "n"]:
                    break
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
        elif start_choice == "3":
            location = "Verdant Grasslands"  # Set location
            valid_location_selected = True  # Exit main loop

            while True:
                more_info = input("Would you like to learn more about Verdant Grasslands? (Yes/No): ")
                if more_info.lower() in ["yes", "y"]:
                    print("\nVerdant Grasslands is a large fertile, rural countryside town, home to happy animals and organic farmers.")
                    break
                elif more_info.lower() in ["no", "n"]:
                    break
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
        else:
            print("Invalid input. Please choose a valid option (1-3).")

    # Return the chosen location
    return location

# Departure Date Selection
def departure_selection() -> str:

    # Flag to control the input loop
    valid_departure = False
    # Variable to store the selected departure date
    departure_date = ""

    # Loop until the user selects a valid departure date
    while not valid_departure:
        # Display the list of available departure dates
        print("\nChoose your departure date:")
        print("1. January 24th")
        print("2. May 6th")
        print("3. July 15th")
        print("4. September 28th")
        print("5. December 5th\n")

        # Ask the player to input their choice
        departure_input = input("Enter the number of your chosen departure date (1-5): ")

        if departure_input == "1":
            departure_date = "January 24th"
            valid_departure = True
        elif departure_input == "2":
            departure_date = "May 6th"
            valid_departure = True
        elif departure_input == "3":
            departure_date = "July 15th"
            valid_departure = True
        elif departure_input == "4":
            departure_date = "September 28th"
            valid_departure = True
        elif departure_input == "5":
            departure_date = "December 5th"
            valid_departure = True
        else:
            # Handle invalid input
            print("Invalid choice, please try again...")

    # Return the selected departure date
    return departure_date

def events(location: str, departure_date: str) -> None:
    
    # Coral Bay summer heatwave warning
    if location == "Coral Bay" and departure_date == "July 15th":
        print("\nWarning: A summer heatwave is expected...")
    # Verdant Grasslands winter road warning
    elif location == "Verdant Grasslands" and departure_date == "December 5th":
        print("\nWarning: Icy and snowy roads...")
    # Spiceport Haven street food festival notice
    elif location == "Spiceport Haven" and departure_date == "May 6th":
        print("\nNotice: The annual street food festival...")
    # No special events
    else:
        print("\nNo special events for your chosen time and place.")

# Function to gather party member names from user
def party_members():
    while True:
        party = []  # Initialize empty list for party members

        # Ask for party leader's name
        leader = input("What is your name? ")
        # Capitilize name
        leader = fix_capitalization(clean_name_input(leader))
        # Add to party list
        party.append(leader)
        print(f"Welcome {leader}!\n")
        print(f"1. Leader: {leader}")

        # Ask for 4 additional party members
        for i in range(2, 6):
            name = input(f"{i}. Member: ")
            name = fix_capitalization(clean_name_input(name))
            party.append(name)

        # Display the full party for confirmation
        print("\nYour Party:")
        for i, name in enumerate(party, 1):
            print(f"{i}. {name}")

        # Ask user to confirm names; loop until confirmation
        confirm = input("\nAre you sure about these names? (Yes/No): ").lower()
        if confirm in ["yes", "y"]:
            break
        else:
            print("\nLet's try entering the names again...\n")

    return party

# Calculate amount to buy
def purchase_supply(supply_name: str, unit_cost: float, description: str) -> tuple[int, float]:

    while True:
        # Display supply name, price, and description
        print(f"{supply_name} - ${unit_cost:.2f} per unit")
        print(f"Description: {description}")

        try:
            # Ask player how many units they want to buy
            quantity = int(input(f"How many units of {supply_name} would you like to buy? "))

            # Reject negative numbers
            if quantity < 0:
                print("Please enter a non-negative number.\n")
                continue

        except ValueError:
            # User entered something that is not a whole number
            print("Invalid input. Please enter a whole number.\n")
            continue

        # Calculate total cost of this supply purchase
        total_cost = quantity * unit_cost

        # Return both quantity and cost to the caller
        return quantity, total_cost

# Process of purchase going through or not
def process_purchases(money: float) -> tuple[dict, float, float]:

    bill = 0
    purchases = {}

    # Initial message showing available funds
    print(f"\nYour starting funds: ${money:.2f}\nPrepare your supplies!\n")

    # List of all possible supplies
    supply_list = [
        ("Proteins/Meats", 6.0, "All sorts of meats and protein-rich foods such as tofu."),
        ("Fruits & Vegetables", 4.0, "Fresh juicy fruits and crunchy vegetables."),
        ("Grains", 3.0, "Bread, rice, oats, and other grains including proccessed forms, such as flour."),
        ("Dairy", 5.0, "Milk, cheese, and other dairy products and delicacies."),
        ("Seafood", 6.0, "Fresh ocean creatures with rich umami.")
    ]

    # Loop through each supply type and allow purchase
    for supply_name, unit_cost, description in supply_list:

        # Ask player how much they want to buy
        quantity, cost = purchase_supply(supply_name, unit_cost, description)

        # Check if purchase exceeds available money
        if bill + cost <= money:
            # Accept purchase when enough money
            bill += cost
            purchases[supply_name] = (quantity, cost)
        else:
            # Skip if not enough money
            print(f"You cannot afford that much {supply_name}. Skipping purchase.")
            purchases[supply_name] = (0, 0)

        # Display updated bill
        print(f"Bill so far: ${bill:.2f}\n")

    # Calculate remaining money after all purchases
    remaining_money = money - bill

    # Return all purchase data
    return purchases, bill, remaining_money

# Prints out a recipet
def print_receipt(purchases: dict, bill: float, remaining_money: float) -> None:

    print("Receipt of your purchase:")

    # Print each supply and its purchased quantity
    for name, (qty, cost) in purchases.items():
        print(f"- {name}: {qty} units  (${cost:.2f})")

    # Final totals
    print(f"Total bill: ${bill:.2f}")
    print(f"Remaining money: ${remaining_money:.2f}\n")

# Goes through the purchasing process and lets player revise
def supply_shop(money: float):

    while True:
        # Perform purchase and get purchase data
        purchases, bill, remaining_money = process_purchases(money)

        # Print the receipt for the player
        print_receipt(purchases, bill, remaining_money)

        # Ask if player wants to revise
        revise_choice = input("Would you like to revise your purchases? (yes/no): ").lower()

        # Validate yes/no input
        while revise_choice not in ['yes', 'no']:
            revise_choice = input("Please enter 'yes' or 'no': ").lower()

        # End purchasing if player is satisfied
        if revise_choice == 'no':
            print("Final purchases confirmed, moving on with your journey!")
            break
        else:
            # Restart purchasing process
            print("Restarting the purchase process...\n")

def load_descriptions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def choose_next_landmark(current_node, graph, names, descriptions):

    options = graph[current_node]

    # Only one possible path = automatically choosen
    if len(options) == 1:
        next_node = list(options.keys())[0]
        return next_node, options[next_node]

    print(f"\nYou have arrived at {names[current_node]}.")
    print("\n" + descriptions[names[current_node]] + "\n")

    print("You can travel to:")

    for node, dist in options.items():
        print(f"- {node}. {names[node]} ({dist} km)")

    while True:
        try:
            choice = int(input("Enter the number of your next destination: "))
            if choice in options:
                return choice, options[choice]
            else:
                print("Invalid choice. Choose one from the list.")
        except ValueError:
            print("Please enter a valid number.")

# -----------------------------------------
# Easier Question Bank
# -----------------------------------------
QUESTION_BANK = [
    {
        "question": "Which fruit is yellow and curved?",
        "options": ["A) Apple", "B) Banana", "C) Grape", "D) Orange"],
        "answer": "B"
    },
    {
        "question": "Which food is made from milk?",
        "options": ["A) Bread", "B) Cheese", "C) Rice", "D) Lettuce"],
        "answer": "B"
    },
    {
        "question": "Which vegetable is green and often in salads?",
        "options": ["A) Carrot", "B) Broccoli", "C) Tomato", "D) Potato"],
        "answer": "B"
    },
    {
        "question": "Which grain do we use to make bread?",
        "options": ["A) Wheat", "B) Rice", "C) Corn", "D) Barley"],
        "answer": "A"
    },
    {
        "question": "Which fruit is red and often used in pies?",
        "options": ["A) Strawberry", "B) Kiwi", "C) Banana", "D) Lemon"],
        "answer": "A"
    },
    {
        "question": "Which food comes from chickens?",
        "options": ["A) Eggs", "B) Milk", "C) Cheese", "D) Rice"],
        "answer": "A"
    },
    {
        "question": "Which vegetable is orange?",
        "options": ["A) Tomato", "B) Carrot", "C) Spinach", "D) Onion"],
        "answer": "B"
    },
    {
        "question": "Which fruit is green on the outside and red inside?",
        "options": ["A) Watermelon", "B) Apple", "C) Banana", "D) Orange"],
        "answer": "A"
    },
    {
        "question": "Which drink comes from cows?",
        "options": ["A) Juice", "B) Water", "C) Milk", "D) Soda"],
        "answer": "C"
    },
    {
        "question": "Which food is sweet and made from sugar?",
        "options": ["A) Cake", "B) Bread", "C) Rice", "D) Cheese"],
        "answer": "A"
    }
]

# -----------------------------------------
# Random question
# -----------------------------------------
def get_random_question():
    return random.choice(QUESTION_BANK)

# -----------------------------------------
# Ask and evaluate
# -----------------------------------------
def ask_question(question_data):
    print("\n🍳 Food Quiz Time! 🍽️")
    print(question_data["question"])
    for opt in question_data["options"]:
        print(opt)
    player_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
    return player_answer == question_data["answer"]

# -----------------------------------------
# Reward system
# -----------------------------------------
def get_reward():
    possible_rewards = [
        ("Dairy", 2),
        ("Grains", 3),
        ("Vegetables", 2),
        ("Fruit", 2),
        ("Protein", 1)
    ]
    return random.choice(possible_rewards)

# -----------------------------------------
# Run the quiz
# -----------------------------------------
def run_quiz():
    q = get_random_question()
    correct = ask_question(q)

    if correct:
        reward = get_reward()
        print(f"\n✅ Correct! You earned bonus supplies: {reward[1]} {reward[0]}!")
        return {"correct": True, "reward": reward}
    else:
        print("\n❌ Incorrect! No reward this time.")
        return {"correct": False, "reward": None}

# -----------------------------------------
# Menu triggered by key press
# -----------------------------------------
def travel_menu():
    while True:
        print("\n--- Travel Menu ---")
        print("1) Take the Food Quiz")
        print("2) Quit Game")
        choice = input("Choose an option (1/2): ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            show_references()
            print("\nExiting game. Safe travels!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

def show_references():
    print("\nReferences / Attribution\n")
    print("1. Generated with the help of ChatGPT, by OpenAI (accessed November 30th, 2025).")
    print("2. Wagon sprite (green food truck) used in this game: from game-icons.net, credited to Game-icons.net.")

def travel_stage(party, travel_events, graph, names, descriptions, debug):

    open_win("A Path to Prosper - Journey")
    sprite = read_sprite("wagon_sprite_for_101382332.png")

    current = 1   # start at First Michelin Restaurant

    while True:
        print(f"\nYou begin your journey to {names[current]}.")

        # Ask player for next destination
        next_node, distance_remaining = choose_next_landmark(current, graph, names, descriptions)

        wagon_x = 280
        tree_x = 100
        tree_y = 210

        # Animation Loop
        while distance_remaining > 0:

            fill_win(57, 128, 198)
            draw_rect((0, 240, 640, 240), (125, 174, 81), 0)
            draw_rect((0, 300, 640, 40), (105, 105, 105), 0)
            draw_line((0, 320), (640, 320), (255, 255, 0), 2)

            speed = random.randint(50, 90)
            wagon_x -= (speed - 70) * 1.0
            wagon_x = max(0, min(600, wagon_x))

            tree_x += 50
            if tree_x > 640:
                tree_x = -random.randint(100, 300)
                tree_y = random.randint(190, 230)

            blit_image(sprite, int(wagon_x), 250)

            draw_rect((int(tree_x), 230, 20, 40), (100, 50, 20), 0)
            draw_rect((int(tree_x) - 10, tree_y, 40, 20), (0, 128, 0), 0)
            draw_rect((int(tree_x) - 5, tree_y - 15, 30, 20), (0, 100, 0), 0)
            draw_rect((int(tree_x) - 15, tree_y + 15, 50, 15), (0, 150, 0), 0)

            render_smaller_text(18, (255, 255, 255), (0, 0, 0), 
                                f"Speed: {speed} km/h", 40, 320, 5)
            render_smaller_text(18, (255, 255, 255), (0, 0, 0), 
                                f"Distance remaining: {distance_remaining} km", 
                                80, 320, 5)

            trigger_chance = 0.1 if not debug else 0.75

            if random.random() < trigger_chance:
                if debug:
                    rn_events = [e for e in travel_events if "RANDOM_NAME" in e]
                    event = random.choice(rn_events)
                else:
                    event = random.choice(travel_events)

                if "RANDOM_NAME" in event:
                    selected_name = fix_capitalization(random.choice((party[1:])))
                    event = replace_random_name(event, selected_name)

                event = fix_capitalization(event)

                render_smaller_text(16, (255, 0, 0), (0, 0, 0), 
                                    f"EVENT: {event}", 120, 320, 5)
                display_update()
                wait_pause(2000)

            display_update()

            if was_any_key_pressed():
                travel_menu()

            distance_remaining -= 1
            wait_pause(300)

        print(f"\nYou have reached {names[current]}!\n")

        # End of journey
        if current == 8:
            print("\nYou have arrived at the Golden Wind Market!\nJourney complete!")
            show_references()
            break

        # Choose next destination based on adjacency list
        current = next_node

def main():

    # Debug mode from command-line
    debug = False
    if len(sys.argv) > 1 and sys.argv[1].lower() == "debug":
        debug = True
        print("DEBUG MODE ACTIVE\n")

    travel_events = [
        "RANDOM_NAME accidentally drops a crate of fresh seafood!",
        "Your truck hits a pothole and a tire blows out.",
        "RANDOM_NAME burns a batch of meals!",
        "A sudden weather change slows your travel.",
        "RANDOM_NAME gets bad motion sickness and needs to rest.",
        "A rival vendor steals some of your supplies overnight!",
        "You find a farmer's market to stop at and earn some bonus cash!"
    ]

    # Load landmark descriptions from external file
    descriptions = load_descriptions("Assignment6 External File.txt")

    # Graph with distances (weighted adjacency list)
    landmark_graph = {
        1: {2: 79, 3: 110},     # From 1 - 2 is 79 km, 1 - 3 is 110 km
        2: {5: 205},            # 2 - 5
        3: {4: 115, 7: 150},    # 3 - 4 OR 3 - 7
        4: {6: 147},            # 4 - 6
        5: {6: 163},            # 5 - 6
        6: {8: 120},            # 6 - 8
        7: {6: 90, 8: 180},     # 7 - 6 or 7 - 8
        8: {}                   
    }

    # Index-to-name
    landmark_names = {
        1: "First Michelin Restaurant",
        2: "Rocky Chocolate Mountains",
        3: "Pomelo Alley",
        4: "Soda Waterfall",
        5: "Duck Broth Lake",
        6: "Cookie Fair and Giant Cookie Statue",
        7: "Sugarland",
        8: "Golden Wind Market"
    }

    print()

    print_game_intro()

    party = party_members()

    character_class, money, subclass = class_selection()

    location = starting_location()

    departure_day = departure_selection()

    events(location, departure_day)

    supply_shop(money)

    print("You may press anything to exit when on the window screen.")

    travel_stage(party, travel_events, landmark_graph, landmark_names, descriptions, debug)

if __name__ == "__main__":
    main()
