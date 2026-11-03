import streamlit as st
import random

st.title("🎅 Secret Santa Draw 🎅")

# Permanently set participants, stores, and budgets
NAMES = [
    "Frame", "Paps", "Deej", "Ling", 
    "Himes", "Fik", "K mess", "Duck", "Cheese"
]

STORES = [
    "Amazon", "Temu", "Marketplace", "Dollar store", 
    "Walmart", "Spencer's", "Etsy", "Five Below", "innergeek/time warp"
]

BUDGETS = [15, 30, 50, 75, 100, 150, 200, 300, 400]

# Fix the seed so the shuffle result is locked permanently across all users/devices
@st.cache_data
def generate_secret_draw():
    rng = random.Random(42)  # Shared seed for consistent results
    
    # Shuffle targets ensuring no self-picks
    targets = NAMES.copy()
    valid = False
    while not valid:
        rng.shuffle(targets)
        valid = all(NAMES[i] != targets[i] for i in range(len(NAMES)))

    stores = STORES.copy()
    budgets = BUDGETS.copy()
    rng.shuffle(stores)
    rng.shuffle(budgets)

    return {
        NAMES[i]: (targets[i], stores[i], budgets[i])
        for i in range(len(NAMES))
    }

draws = generate_secret_draw()

st.write("### Choose your name to reveal your assignment:")
user_select = st.selectbox(
    "Select your name:", 
    ["-- Select Name --"] + NAMES
)

if user_select != "-- Select Name --":
    target, store, budget = draws[user_select]
    st.success(f"🔒 Assignment for **{user_select}** locked in!")
    st.info(f"🎯 **Buying For:** {target}\n\n🏪 **Store:** {store}\n\n💰 **Budget:** ${budget}")
