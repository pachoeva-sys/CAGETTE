import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="Cagette", layout="centered")

# --- CUSTOM CSS (UBER-INSPIRED) ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: #F5F1E6;
    }}
    h1, h2, h3, p {{
        color: #1B4332;
        font-family: 'Inter', sans-serif;
    }}
    .stButton>button {{
        background-color: #1B4332 !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 2rem;
        width: 100%;
    }}
    .merchant-card {{
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #E0E0E0;
    }}
    .search-bar .stTextInput > div > div > input {{
        border: 2px solid #1B4332 !important;
        border-radius: 8px;
        padding: 15px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- DATA ---
merchants = [
    {"name": "Ferme de la Vallée", "type": "Fruits & Légumes", "loc": "Nantes"},
    {"name": "L'Épicerie Fine", "type": "Épicerie", "loc": "Angers"},
    {"name": "Au Bon Pain", "type": "Boulangerie", "loc": "Nantes"},
    {"name": "Le Potager Bio", "type": "Légumes", "loc": "Saint-Nazaire"}
]

products = [
    {"name": "Panier de Saison", "price": 15.00, "merchant": "Ferme de la Vallée"},
    {"name": "Miel de Fleurs", "price": 8.50, "merchant": "L'Épicerie Fine"},
    {"name": "Pommes Gala (1kg)", "price": 3.20, "merchant": "Le Potager Bio"}
]

# --- HEADER SECTION ---
st.title("Cagette")
st.subheader("Achetez local, simplement.")

# --- SEARCH SECTION ---
search_query = st.text_input("", placeholder="Rechercher des produits ou commerçants...", key="main_search")
search_btn = st.button("Rechercher")

if search_query:
    st.write(f"Résultats pour : **{search_query}**")
    filtered_prods = [p for p in products if search_query.lower() in p['name'].lower()]
    
    for p in filtered_prods:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{p['name']}** — {p['price']}€")
        with col2:
            if st.button(f"Ajouter", key=p['name']):
                st.session_state.cart.append(p)
                st.rerun()

# --- MERCHANTS SECTION ---
st.markdown("---")
st.header("Nos commerçants")

cols = st.columns(2)
for i, m in enumerate(merchants):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="merchant-card">
            <h3>{m['name']}</h3>
            <p><b>Type:</b> {m['type']}<br>
            <b>Lieu:</b> {m['loc']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- CART SECTION ---
st.sidebar.header("Votre Panier")
if not st.session_state.cart:
    st.sidebar.write("Le panier est vide.")
else:
    total = 0
    for item in st.session_state.cart:
        st.sidebar.write(f"• {item['name']} ({item['price']}€)")
        total += item['price']
    
    st.sidebar.markdown("---")
    st.sidebar.subheader(f"Total: {total:.2f}€")
    if st.sidebar.button("Vider le panier"):
        st.session_state.cart = []
        st.rerun()
