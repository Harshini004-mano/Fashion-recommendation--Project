import streamlit as st
import os

# --------------------------
# Your full default_rules dictionary here
# --------------------------
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

# --------------------------
# Streamlit App UI
# --------------------------
st.set_page_config(page_title="Fashion Outfit Recommender", page_icon="👗", layout="wide")
st.title("👗 Fashion Outfit Recommender 👕")
st.write("Select your preferences and click the button to get outfit recommendations!")

# Dropdown inputs
category = st.selectbox("👤 Select Category", ["men", "women", "children_boy", "children_girl"])
temperature = st.selectbox("🌤️ Select Temperature", ["hot", "cold", "rainy", "sunny", "overcast"])
place = st.selectbox("📍 Select Place", ["beach", "park", "restaurant", "city", "mountains"])

# Recommendation button
if st.button("🚀 GET RECOMMENDATION"):
    folder_path = f"images/{category}/{temperature}/{place}"

    # Map category to dictionary keys
    if category == "children_boy":
        dict_top = "Children"
        dict_sub = "Boy"
    elif category == "children_girl":
        dict_top = "Children"
        dict_sub = "Girl"
    else:
        dict_top = category.capitalize()
        dict_sub = None

    # Lookup the rule
    rule = None
    temp_key = temperature.capitalize()
    try:
        if dict_sub:
            rule = default_rules[dict_top][dict_sub].get(temp_key)
        else:
            rule = default_rules[dict_top].get(temp_key)
    except Exception:
        rule = None

    # Display results
    if rule:
        st.subheader("🧠 Fashion Tip")
        st.write(rule.get("tip", "No tip available."))

        st.subheader("🎀 Sample Outfit Ideas")
        for outfit in rule.get("sample_outfits", []):
            st.markdown(f"- {outfit}")
    else:
        st.warning("No fashion tips available for this selection.")

    # Display 4 images
    if os.path.exists(folder_path):
        image_files = sorted([
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ])[:4]

        if image_files:
            st.subheader("🖼️ Outfit Images")
            cols = st.columns(4)
            for i, col in enumerate(cols):
                if i < len(image_files):
                    col.image(image_files[i], use_container_width=True)
        else:
            st.warning("⚠️ No images found in this folder.")
    else:
        st.warning("🚫 This combination folder does not exist.")
