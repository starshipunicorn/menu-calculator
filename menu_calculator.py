import streamlit as st

# Menu Items with their Prices
menu = {
    "Breakfast": {
        "Crater Cinnamon Roll Pancakes": 73.50,
        "Nebula Nosh Chicken & Waffles": 115.50,
        "Extraterrestrial Omelet": 87.50
    },
    "Starters": {
        "Celestial Caesar Salad": 70.00,
        "Alien Antenna Bites": 98.00,
        "Orbiting Onion Rings": 52.50
    },
    "Mains": {
        "Celestial Creature Gyro": 115.50,
        "Andromeda Invader Curry": 105.00,
        "Planetary Pizza": 80.00,
        "Galaxy Guac Burger and Meteorite Fries": 122.50
    },
    "Desserts": {
        "Spacecraft S’mores Shake": 950,
        "Blackhole Brownies": 66.50,
        "Martian Mousse": 73.50
    },
    "Alcoholic Drinks": {
        "UFO Umbrella Drink": 50.00,
        "Asteroid Amaretto Sour": 57.50,
        "Alien Ambrosia": 62.50
    },
    "Non-Alcoholic Drinks": {
        "Lunar Lemonade": 27.50,
        "Comet Cola Float": 32.50,
        "Galactic Grape Cola": 27.50,
        "Nebula Nectar Cola": 27.50
    }
}

# Function to calculate total price
def calculate_total(order, discount=0, fee=0):
    subtotal = 0
    for item, quantity in order.items():
        subtotal += menu[item[0]][item[1]] * quantity

    # Apply discount
    discount_amount = subtotal * (discount / 100)
    subtotal -= discount_amount

    # Apply fee
    fee_amount = subtotal * (fee / 100)
    total = subtotal + fee_amount

    return round(total, 2)

# Streamlit Interface
st.title("Space-Themed Menu Calculator")

order = {}
st.header("Select Your Items")
for category, items in menu.items():
    st.subheader(category)
    for item, price in items.items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
        if quantity > 0:
            order[(category, item)] = quantity

discount = st.slider("Discount (%)", 0, 100, 0)
fee = st.slider("Additional Fee (%)", 0, 100, 0)

if st.button("Calculate Total"):
    total_price = calculate_total(order, discount=discount, fee=fee)
    st.write(f"The total price of the order is: **${total_price}**")
