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
    border-radius: 12px;
    border: none;
    padding: 10px 16px;
    font-weight: bold;
    transition: 0.2s;
}}

.stButton > button:hover {{
    opacity: 0.85;
    transform: scale(1.02);
}}

input {{
    border: 2px solid {GREEN} !important;
    border-radius: 12px !important;
}}

/* TAB STYLE */
.stTabs [data-baseweb="tab-list"] {{
    gap: 10px;
}}

.stTabs [data-baseweb="tab"] {{
    background-color: white;
    border-radius: 12px;
    padding: 10px 16px;
    color: {GREEN};
    font-weight: bold;
    border: 1px solid {GREEN};
}}

.stTabs [aria-selected="true"] {{
    background-color: {GREEN} !important;
    color: {BEIGE} !important;
}}
</style>
""", unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("<h1 class='center'>Cagette</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>Achetez local, simplement.</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Accueil", "À propos de nous", "Nos commerçants"])

# ---------------- ACCUEIL ----------------
with tab1:
    search = st.text_input("Rechercher un produit ou un commerçant")

    products = [
        {"name": "Tomates bio", "price": 3.5},
        {"name": "Carottes fraîches", "price": 2.0},
        {"name": "Panier de légumes", "price": 10.0},
        {"name": "Salade verte", "price": 1.8},
        {"name": "Courgettes locales", "price": 4.5},
    ]

    def image_for_price(price):
        if price <= 2:
            return "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce"
        elif price <= 4:
            return "https://images.unsplash.com/photo-1582515073490-39981397c445"
        else:
            return "https://images.unsplash.com/photo-1518843875459-f738682238a6"

    st.markdown("## Résultats")

    for p in products:
        if search.lower() in p["name"].lower() or search == "":
            img = image_for_price(p["price"])

            st.markdown(f"""
            <div class="card">
                <h3>{p['name']}</h3>
                <p>{p['price']} €</p>
                <img src="{img}" width="100%">
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Ajouter {p['name']}"):
                st.session_state.cart.append(p)

    st.markdown("## Panier")

    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item['name']} : {item['price']} €")
        total += item["price"]

    st.markdown(f"### Total : {total} €")

# ---------------- À PROPOS ----------------
with tab2:
    st.markdown("## À propos de nous")

    st.write("""
    Cagette est une nouvelle application née à Marseille avec une ambition simple : 
    rapprocher les habitants des producteurs locaux et rendre l’alimentation plus saine, plus transparente et plus accessible.

    Nous croyons qu’il est possible de consommer autrement, sans intermédiaires inutiles, en soutenant directement les agriculteurs, 
    maraîchers, épiceries locales et petits commerces de quartier.

    Notre mission est de créer un pont entre la ville et la campagne autour de Marseille, en mettant en avant des produits frais, 
    de saison et issus d’un savoir-faire local.

    Cagette, c’est aussi une communauté engagée qui veut redonner du sens à ce que nous mangeons chaque jour, 
    tout en soutenant l’économie locale et en réduisant l’impact environnemental.
    """)

# ---------------- COMMERCANTS ----------------
with tab3:
    st.markdown("## Nos commerçants")

    merchants = [
        {"name": "Ferme du Soleil", "type": "Légumes", "location": "Marseille 8e",
         "img": "https://images.unsplash.com/photo-1500595046743-cd271d694d30"},
        {"name": "Le Panier Vert", "type": "Épicerie", "location": "Vieux-Port",
         "img": "https://images.unsplash.com/photo-1542838132-92c53300491e"},
        {"name": "Bio Provence", "type": "Fruits & Légumes", "location": "La Joliette",
         "img": "https://images.unsplash.com/photo-1557844352-761f2565b576"},
    ]

    cols = st.columns(3)

    for i, m in enumerate(merchants):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <h3>{m['name']}</h3>
                <p>{m['type']}</p>
                <p>{m['location']}</p>
                <img src="{m['img']}" width="100%">
            </div>
            """, unsafe_allow_html=True)
