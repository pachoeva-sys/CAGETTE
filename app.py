import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Mon Panier Local", page_icon="🥗")

# Données locales (Simulées)
PRODUCTS = [
    {"nom": "Pommes (1kg)", "prix": 3.50, "cat": "Fruit", "origine": "Ferme du Verger (15km)"},
    {"nom": "Carottes (1kg)", "prix": 2.20, "cat": "Légume", "origine": "Maraîcher Bio (8km)"},
    {"nom": "Panier Étudiant", "prix": 15.00, "cat": "Panier", "origine": "Mix local (Direct producteur)"},
    {"nom": "Œufs (x6)", "prix": 2.80, "cat": "Autre", "origine": "Ferme des Plumes (22km)"},
    {"nom": "Miel de fleurs", "prix": 7.50, "cat": "Autre", "origine": "Rucher du Campus (2km)"},
]

# Initialisation du panier
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- UI ---
st.title("🥗 Mon Panier Local")
st.markdown("Soutenez les producteurs de votre région et mangez sainement !")

# Section 1: Sélection des produits
st.header("🛒 Boutique")
col1, col2 = st.columns([2, 1])

with col1:
    selected_product_name = st.selectbox("Choisissez un produit", [p["nom"] for p in PRODUCTS])
    product = next(p for p in PRODUCTS if p["nom"] == selected_product_name)
    st.info(f"📍 Origine : {product['origine']}")

with col2:
    quantity = st.number_input("Quantité", min_value=1, value=1)
    if st.button("Ajouter au panier"):
        st.session_state.cart.append({
            "Produit": product["nom"],
            "Prix Unitaire": product["prix"],
            "Quantité": quantity,
            "Total": product["prix"] * quantity
        })
        st.success("Ajouté !")

# Section 2: Panier et Total
st.header("📋 Votre Commande")
if st.session_state.cart:
    df_cart = pd.DataFrame(st.session_state.cart)
    st.table(df_cart)
    
    total_general = df_cart["Total"].sum()
    st.metric("Total à payer", f"{total_general:.2f} €")
    
    if st.button("Vider le panier"):
        st.session_state.cart = []
        st.rerun()
else:
    st.write("Votre panier est vide.")

# Section 3: Suggestions de saison & Origine
st.divider()
st.subheader("💡 Suggestion de saison")
st.info("C'est le moment idéal pour les **asperges** et les **fraises locales** ! Elles arrivent chez nos producteurs cette semaine.")

with st.expander("🌍 Voir la carte de nos producteurs"):
    st.write("Voici les fermes partenaires à moins de 30km :")
    # Simulation de points sur une carte locale (Fictif)
    map_data = pd.DataFrame({'lat': [48.85], 'lon': [2.35]}) 
    st.map(map_data)
