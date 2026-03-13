import streamlit as st
from PIL import Image
import os

# --- Must be first Streamlit command ---
st.set_page_config(page_title="Fashion Outfit Recommender", page_icon="👗", layout="wide")

# --- Background Gradient ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #CCA25A 0%, #FFB16E 33%, #FFF5B8 66%, #45ADAB 100%);
    color: #000000;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: #fff3e0;
}
h1, h2, h3 {
    color: #333333;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Title ---
st.title("👗 Fashion Outfit Recommender")
st.write("Select your preferences and get personalized outfit recommendations with inspiration images!")

# --- User Inputs: Updated Order ---
category = st.selectbox("Select Category", ["Men", "Women", "Children"])

# Gender type only if Children
if category == "Children":
    child_type = st.selectbox("Select Type", ["Boy", "Girl"])
else:
    child_type = None

place = st.selectbox("Select Place", ["Beach", "Park", "Restaurant", "City", "Mountains"])
temperature = st.selectbox("Select Temperature", ["Hot", "Cold", "Rainy", "Sunny", "Overcast"])

# --- Fashion Rules ---
default_rules = {
    "Women": {
        "Hot": {
            "tip": "👗 Light cotton dress or sleeveless top with shorts. Keep it airy and fresh!",
            "sample_outfits": [
                "White sundress with straw hat and sandals 🌼",
                "Crop top + denim shorts + flip-flops ☀️",
                "Tank top + flowy skirt + sunglasses 😎",
                "Linen jumpsuit + flats 👡"
            ]
        },
        "Cold": {
            "tip": "🧥 Layer up with sweaters and coats for warmth.",
            "sample_outfits": [
                "Wool coat + jeans + boots 🥾",
                "Turtleneck + trench coat + gloves 🧤",
                "Sweater dress + tights + ankle boots 👢",
                "Puffer jacket + scarf + jeans 🧣"
            ]
        },
        "Rainy": {
            "tip": "☔ Choose waterproof jackets and boots to stay dry!",
            "sample_outfits": [
                "Raincoat + leggings + rain boots 🌧️",
                "Waterproof jacket + jeans + sneakers 👟",
                "Hoodie + windbreaker + boots 🥾",
                "Trench coat + umbrella ☂️"
            ]
        },
        "Sunny": {
            "tip": "🌞 Light cotton or linen clothes work best under the sun.",
            "sample_outfits": [
                "Floral dress + sandals 👗",
                "Sleeveless top + wide-leg pants 👖",
                "T-shirt + shorts + hat 🧢",
                "Skirt + crop top + sunglasses 😎"
            ]
        },
        "Overcast": {
            "tip": "🌤️ Mix comfort and style — light jacket or hoodie.",
            "sample_outfits": [
                "Denim jacket + jeans 👖",
                "Sweater + skirt + sneakers 👟",
                "Cardigan + leggings 👚",
                "Long-sleeve tee + trousers 👖"
            ]
        },
    },
    "Men": {
        "Hot": {
            "tip": "👕 Light T-shirts and shorts for comfort in the heat.",
            "sample_outfits": [
                "Cotton T-shirt + shorts + sandals 🩴",
                "Linen shirt + chinos + loafers 👞",
                "Tank top + cargo shorts + sneakers 👟",
                "Polo shirt + shorts + sunglasses 😎"
            ]
        },
        "Cold": {
            "tip": "🧥 Layer with sweaters and jackets to keep warm.",
            "sample_outfits": [
                "Wool sweater + jeans + boots 🥾",
                "Jacket + hoodie + cargo pants 👖",
                "Coat + turtleneck + gloves 🧤",
                "Puffer + jeans + boots 👢"
            ]
        },
        "Rainy": {
            "tip": "☔ Wear waterproof jacket and shoes.",
            "sample_outfits": [
                "Rain jacket + jeans + boots 🌧️",
                "Hoodie + waterproof coat + sneakers 👟",
                "Parka + joggers + boots 🥾",
                "Windbreaker + trousers + hat 🧢"
            ]
        },
        "Sunny": {
            "tip": "🌞 Go for cotton or linen for breathability.",
            "sample_outfits": [
                "T-shirt + shorts + sneakers 👟",
                "Linen shirt + chinos 👖",
                "Polo + cargo shorts + loafers 👞",
                "Sleeveless shirt + shorts ☀️"
            ]
        },
        "Overcast": {
            "tip": "🌤️ Casual layers for uncertain weather.",
            "sample_outfits": [
                "Light jacket + jeans 👖",
                "Hoodie + joggers 👟",
                "Sweatshirt + chinos 👕",
                "Long sleeve + denim jacket 🧥"
            ]
        },
    },
    "Children": {
        "Boy": {
            "Hot": {
                "tip": "👕 Cotton shirts and shorts keep kids comfy.",
                "sample_outfits": [
                    "T-shirt + shorts + sandals 🩴",
                    "Sleeveless top + cotton shorts ☀️",
                    "Light shirt + sneakers 👟",
                    "Printed tee + cap 🧢"
                ]
            },
            "Cold": {
                "tip": "🧥 Keep warm with layered clothing.",
                "sample_outfits": [
                    "Jacket + jeans + boots 🥾",
                    "Sweater + beanie + pants 🧣",
                    "Hoodie + joggers + sneakers 👟",
                    "Coat + gloves + boots 🧤"
                ]
            },
            "Rainy": {
                "tip": "☔ Use raincoats and waterproof boots.",
                "sample_outfits": [
                    "Raincoat + boots 🌧️",
                    "Waterproof jacket + jeans 👖",
                    "Parka + sneakers 👟",
                    "Hoodie + rain pants ☂️"
                ]
            },
            "Sunny": {
                "tip": "😎 Simple cotton tees and shorts work great.",
                "sample_outfits": [
                    "T-shirt + shorts + sandals 🩴",
                    "Polo + shorts + hat 🧢",
                    "Sleeveless top + joggers 👕",
                    "Light shirt + flip-flops 🩴"
                ]
            },
            "Overcast": {
                "tip": "🌤️ Add a light jacket just in case.",
                "sample_outfits": [
                    "Hoodie + jeans 👖",
                    "Sweatshirt + shorts 👕",
                    "Light jacket + joggers 👟",
                    "T-shirt + pants + cap 🧢"
                ]
            },
        },
        "Girl": {
            "Hot": {
                "tip": "👗 Dresses or tops with shorts are perfect.",
                "sample_outfits": [
                    "Sundress + sandals 🌼",
                    "Top + shorts + hat 🧢",
                    "Skirt + T-shirt + sneakers 👟",
                    "Tank top + leggings + sandals 👡"
                ]
            },
            "Cold": {
                "tip": "🧥 Keep cozy with sweaters and leggings.",
                "sample_outfits": [
                    "Sweater + skirt + boots 🥾",
                    "Jacket + jeans + scarf 🧣",
                    "Hoodie + leggings + gloves 🧤",
                    "Coat + tights + boots 👢"
                ]
            },
            "Rainy": {
                "tip": "☔ Raincoats and boots to splash safely!",
                "sample_outfits": [
                    "Raincoat + leggings + boots 🌧️",
                    "Hoodie + rain jacket ☂️",
                    "Waterproof pants + sneakers 👟",
                    "Poncho + boots 🥾"
                ]
            },
            "Sunny": {
                "tip": "🌞 Light and bright outfits for cheerful days!",
                "sample_outfits": [
                    "Dress + sandals 👗",
                    "T-shirt + shorts 👕",
                    "Skirt + top + sneakers 👟",
                    "Cap + summer frock 🧢"
                ]
            },
            "Overcast": {
                "tip": "🌤️ Add a cardigan or jacket for comfort.",
                "sample_outfits": [
                    "Sweater + jeans 👖",
                    "Hoodie + leggings 👕",
                    "Cardigan + skirt + shoes 👟",
                    "Jacket + pants 👖"
                ]
            },
        },
    },
}

# --- GET RECOMMENDATION BUTTON ---
if st.button("🎯 GET RECOMMENDATION"):
    if category == "Children":
        rec = default_rules[category][child_type][temperature]
    else:
        rec = default_rules[category][temperature]

    st.subheader("💡 Fashion Tip:")
    st.write(rec["tip"])

    st.subheader("👕 Sample Outfit Ideas:")
    for outfit in rec["sample_outfits"]:
        st.write(outfit)

    # --- Display Images ---
    base_path = "C:/Users/harsh/OneDrive/Desktop/fashion/images"
    if category == "Children":
        image_folder = f"{base_path}/{category.lower()}/{child_type.lower()}/{temperature.lower()}/{place.lower()}"
    else:
        image_folder = f"{base_path}/{category.lower()}/{temperature.lower()}/{place.lower()}"

    st.subheader("📸 OUTFIT INSPIRATION:")
    if os.path.exists(image_folder):
        image_files = [os.path.join(image_folder, img)
                       for img in os.listdir(image_folder)
                       if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            cols = st.columns(4)
            for i, img_path in enumerate(image_files[:4]):
                with cols[i % 4]:
                    img = Image.open(img_path)
                    img = img.resize((300, 400))  # Same size
                    st.image(img, caption=f"Look {i+1}", width="stretch")
        else:
            st.warning("No images found in this category. Add some outfit images!")
    else:
        st.warning("Image folder not found! Please check your folder structure.")
