import streamlit as st
import random

st.title("🎅 Secret Santa Draw 🎅")

NAMES = [
    "Frame", "Paps", "Deej", "Ling", 
    "Himes", "Fik", "K mess", "Duck", "Cheese"
]

STORES = [
    "Amazon", "Temu", "Marketplace", "Dollar store", 
    "Walmart", "Spencer's", "Etsy", "Five Below", "innergeek/time warp"
]

BUDGETS = [15, 30, 50, 75, 100, 150, 200, 300, 400]

# Hardcoded secret PINs matching your master list
USER_PINS = {
    "Frame": "4812",
    "Paps": "7391",
    "Deej": "2564",
    "Ling": "9148",
    "Himes": "3625",
    "Fik": "8053",
    "K mess": "1794",
    "Duck": "6240",
    "Cheese": "5389"
}

@st.cache_data
def generate_secret_draw():
    rng = random.Random(42)  # Locked seed so matchups never change
    
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

st.write("### Private Assignment Lookup")
user_select = st.selectbox("Select your name:", ["-- Select Name --"] + NAMES)

if user_select != "-- Select Name --":
    pin_input = st.text_input(f"Enter 4-digit PIN for {user_select}:", type="password")
    
    if pin_input:
        if pin_input == USER_PINS[user_select]:
            target, store, budget = draws[user_select]
            st.success(f"🔒 Authenticated for **{user_select}**")
            st.info(f"🎯 **Buying For:** {target}\n\n🏪 **Store:** {store}\n\n💰 **Budget:** ${budget}")
        else:
            st.error("❌ Incorrect PIN. Access denied.")
