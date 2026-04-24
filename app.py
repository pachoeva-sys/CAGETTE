import streamlit as st

st.set_page_config(page_title="Cagette", layout="wide")

BEIGE = "#F5F1E6"
GREEN = "#1B4332"

st.markdown(f"""
<style>
.stApp {{
    background-color: {BEIGE};
    color: {GREEN};
    font-family: Arial;
}}

h1, h2, h3, p, label {{
    color: {GREEN};
}}

.center {{
    text-align: center;
}}

.card {{
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 10px;
}}

.stButton > button {{
    background-color: {GREEN};
    color: {BEIGE};
    border-radius: 10px;
    border: none;
}}

input {{
    border: 2px solid {GREEN} !important;
    border-radius: 10px !important;
}}

</style>
""", unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("<h1 class='center'>Cagette</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>Achetez local, simplement.</p>", unsafe_allow_html=True)

search = st.text_input("Rechercher un produit ou un commerçant")

products = [
    {"name": "Tomates bio", "price": 3.5},
    {"name": "Carottes fraîches", "price": 2.0},
    {"name": "Panier de légumes", "price": 10.0},
    {"name": "Salade verte", "price": 1.8},
]

merchants = [
    {"name": "Ferme du Soleil", "type": "Légumes", "location": "Marseille 8e"},
    {"name": "Le Panier Vert", "type": "Épicerie", "location": "Vieux-Port"},
    {"name": "Bio Provence", "type": "Fruits & Légumes", "location": "La Joliette"},
]

st.markdown("## Résultats")

for p in products:
    if search.lower() in p["name"].lower() or search == "":
        st.markdown(f"""
        <div class="card">
            <h3>{p['name']}</h3>
            <p>{p['price']} €</p>
            <img src="https://images.unsplash.com/photo-1542838132-92c53300491e" width="100%">
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Ajouter {p['name']}"):
            st.session_state.cart.append(p)

st.markdown("## Nos commerçants")

cols = st.columns(3)
for i, m in enumerate(merchants):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <h3>{m['name']}</h3>
            <p>{m['type']}</p>
            <p>{m['location']}</p>
            <img src="https://images.unsplash.com/photo-1542838132-92c53300491e" width="100%">
        </div>
        """, unsafe_allow_html=True)

st.markdown("## Panier")

total = 0
for item in st.session_state.cart:
    st.write(f"- {item['name']} : {item['price']} €")
    total += item["price"]

st.markdown(f"### Total : {total} €")
