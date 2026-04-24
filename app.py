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
    padding: 12px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 10px;
    text-align: center;
}}

.card img {{
    width: 100%;
    height: 160px;
    object-fit: cover;
    border-radius: 12px;
    margin-top: 8px;
}}

.stButton > button {{
    background-color: {GREEN};
    color: {BEIGE};
    border-radius: 12px;
    border: none;
    padding: 10px 16px;
    font-weight: bold;
}}

.stButton > button:hover {{
    opacity: 0.85;
}}

.stTabs [data-baseweb="tab"] {{
    background-color: white;
    border-radius: 12px;
    padding: 10px 14px;
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

# ---------------- PRODUITS ----------------
with tab1:
    search = st.text_input("Rechercher un produit")

    products = [
        {
            "name": "Tomates bio",
            "price": 3.5,
            "img": "https://images.unsplash.com/photo-1561136594-7f68413baa99"
        },
        {
            "name": "Carottes fraîches",
            "price": 2.0,
            "img": "https://images.unsplash.com/photo-1447175008436-054170c2e979"
        },
        {
            "name": "Courgettes locales",
            "price": 4.5,
            "img": "https://images.unsplash.com/photo-1582515073490-39981397c445"
        },
        {
            "name": "Salade verte",
            "price": 1.8,
            "img": "https://images.unsplash.com/photo-1557844352-761f2565b576"
        },
        {
            "name": "Pommes de terre",
            "price": 2.8,
            "img": "https://images.unsplash.com/photo-1518977676601-b53f82aba655"
        }
    ]

    st.markdown("## Résultats")

    for p in products:
        if search.lower() in p["name"].lower() or search == "":
            st.markdown(f"""
            <div class="card">
                <h3>{p['name']}</h3>
                <p>{p['price']} €</p>
                <img src="{p['img']}">
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

# ---------------- A PROPOS ----------------
with tab2:
    st.markdown("## À propos de nous")

    st.write("""
Cagette est une nouvelle application basée à Marseille.

Notre mission est simple : reconnecter les habitants avec les producteurs locaux et rendre l’accès aux produits frais plus simple, rapide et transparent.

Nous voulons aider les Marseillais à mieux consommer en favorisant les circuits courts, les produits de saison et les petits commerces de quartier.

Grâce à Cagette, vous pouvez découvrir des producteurs proches de chez vous, acheter des produits frais, et soutenir directement l’économie locale.

C’est une nouvelle manière de consommer : plus humaine, plus responsable et plus locale.
""")

# ---------------- COMMERCANTS ----------------
with tab3:
    st.markdown("## Nos commerçants")

    merchants = [
        {
            "name": "Ferme du Soleil",
            "type": "Légumes",
            "location": "Marseille 8e",
            "img": "https://images.unsplash.com/photo-1500595046743-cd271d694d30"
        },
        {
            "name": "Le Panier Vert",
            "type": "Épicerie",
            "location": "Vieux-Port",
            "img": "https://images.unsplash.com/photo-1542838132-92c53300491e"
        },
        {
            "name": "Bio Provence",
            "type": "Fruits & Légumes",
            "location": "La Joliette",
            "img": "https://images.unsplash.com/photo-1557844352-761f2565b576"
        },
    ]

    cols = st.columns(3)

    for i, m in enumerate(merchants):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <h3>{m['name']}</h3>
                <p>{m['type']}</p>
                <p>{m['location']}</p>
                <img src="{m['img']}">
            </div>
            """, unsafe_allow_html=True)
