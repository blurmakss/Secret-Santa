import streamlit as st
import random

st.title("🎅 Secret Santa Draw 🎅")

# Default setup for your group
default_names = "Jake\nSam\nChris\nDave"
default_stores = "Amazon\nTemu\nSpencer's\nWalmart\nDollar store\nMarketplace\nGas Station\nThrift Store\nFive Below"
default_budgets = "15\n30\n50\n75\n100\n150\n200\n300\n400"

names_input = st.text_area("Names (one per line):", default_names)
stores_input = st.text_area("Stores (one per line):", default_stores)
budgets_input = st.text_area("Budgets (one per line):", default_budgets)

if st.button("Run Secret Draw"):
    names = [n.strip() for n in names_input.split('\n') if n.strip()]
    stores = [s.strip() for s in stores_input.split('\n') if s.strip()]
    budgets = [b.strip() for b in budgets_input.split('\n') if b.strip()]

    if len(names) < 2:
        st.error("Need at least 2 people!")
    elif len(names) != len(stores) or len(names) != len(budgets):
        st.error(f"Mismatch counts! Names: {len(names)}, Stores: {len(stores)}, Budgets: {len(budgets)}")
    else:
        # Shuffle targets so nobody gets themselves
        targets = names.copy()
        valid = False
        while not valid:
            random.shuffle(targets)
            valid = all(names[i] != targets[i] for i in range(len(names)))

        random.shuffle(stores)
        random.shuffle(budgets)

        st.session_state['draws'] = {
            names[i]: (targets[i], stores[i], budgets[i])
            for i in range(len(names))
        }
        st.success("Draw finished! Everyone can now select their name below to view their assignment.")

# Reveal section
if 'draws' in st.session_state:
    st.write("---")
    user_select = st.selectbox("Select your name to reveal your secret assignment:", ["-- Select Name --"] + list(st.session_state['draws'].keys()))
    
    if user_select != "-- Select Name --":
        target, store, budget = st.session_state['draws'][user_select]
        st.info(f"🎯 **Buying For:** {target}\n\n🏪 **Store:** {store}\n\n💰 **Budget:** ${budget}")
