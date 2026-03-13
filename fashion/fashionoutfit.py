import streamlit as st
import os

# Title
st.title("👗 Fashion Recommender App")
st.write("Based on the temperature, place, and your company, we'll suggest what to wear and show you an example outfit!")

# --- User Inputs with Emojis ---
category = st.selectbox("👤 Select Category", ["Women", "Men", "Children"])
child_gender = None
if category == "Children":
    child_gender = st.selectbox("🧒 Select Child Gender", ["Boy", "Girl"])

temperature = st.selectbox("🌡️ Select Temperature", ["Sunny", "Hot", "Cold", "Rainy", "Overcast"])
place = st.selectbox("📍 Select Place", ["Beach", "Park", "Restaurant", "City", "Mountains"])
companion = st.selectbox("🧑‍🤝‍🧑 Going With", ["Friends", "Family", "Couple"])

# --- Fashion Tips Dictionary with Emojis ---
default_rules = {
    "Women": {
        "Hot": "👗 Light dress, 🩳 top with skirt or shorts, and 🩴 sandals.",
        "Cold": "🧥 Coat, 🧶 sweater, 👖 trousers, and 🥾 boots.",
        "Rainy": "☔ Waterproof jacket, 👖 trousers, and 🥾 boots.",
        "Sunny": "👚 Comfortable top, 👖 trousers or skirt, and 🩴 sandals.",
        "Overcast": "👚 Comfortable top, 👖 trousers or skirt, and 🩴 sandals."
    },
    "Men": {
        "Hot": "👕 T-shirt, 🩳 shorts, and 🩴 sandals or 👟 sneakers.",
        "Cold": "🧥 Jacket, 🧶 sweater, 👖 trousers, and 🥾 boots.",
        "Rainy": "☔ Waterproof jacket, 👖 pants, and 🥾 boots.",
        "Sunny": "👕 Comfortable T-shirt, 👖 trousers or 🩳 shorts, and 👟 sneakers.",
        "Overcast": "👕 Comfortable T-shirt, 👖 trousers or 🩳 shorts, and 👟 sneakers."
    },
    "Children": {
        "Boy": {
            "Hot": "👕 T-shirt, 🩳 shorts, and 🩴 sandals.",
            "Cold": "🧥 Jacket, 🧶 sweater, 👖 pants, and 🥾 boots.",
            "Rainy": "☔ Raincoat, 👖 pants, and 🥾 boots.",
            "Sunny": "👕 T-shirt, 🩳 shorts, and 👟 sneakers.",
            "Overcast": "👕 T-shirt, 🩳 shorts, and 👟 sneakers."
        },
        "Girl": {
            "Hot": "👗 Dress or 👕 T-shirt with 🩳 shorts, 🩴 sandals.",
            "Cold": "🧥 Jacket, 🧶 sweater, 👖 pants, and 🥾 boots.",
            "Rainy": "☔ Raincoat, 🩳 leggings, and 🥾 boots.",
            "Sunny": "👕 Top with 👗 skirt/shorts, and 👟 sneakers.",
            "Overcast": "👕 Top with 👗 skirt/shorts, and 👟 sneakers."
        }
    }
}

# --- Companion-specific additional tips ---
companion_tips = {
    "Friends": "💡 Prefer casual outfits for comfort and fun.",
    "Family": "💡 Consider more formal or neat styles for gatherings.",
    "Couple": "💡 Prefer comfortable and coordinated outfits for two."
}

# --- Function to find image ---
def find_image(filename_without_ext):
    for ext in [".jpeg", ".jpg"]:
        path = os.path.join("images", filename_without_ext + ext)
        if os.path.exists(path):
            return path
    return None

# --- Button to Get Recommendation ---
if st.button("Get Recommendation"):
    # Base recommendation
    if category == "Children":
        recommendation = default_rules["Children"][child_gender][temperature]
        filename_base = f"children_{child_gender.lower()}_{temperature.lower()}_{place.lower()}"
    else:
        recommendation = default_rules[category][temperature]
        filename_base = f"{category.lower()}_{temperature.lower()}_{place.lower()}"

    # Add companion tip if applicable
    if companion in ["Family", "Friends", "Couple"]:
        tip = companion_tips[companion]
        recommendation = f"{recommendation}\n{tip}"

    # Display recommendation with emoji and formatting
    st.markdown(f"<h3 style='color:blue'>👚 Fashion Tip</h3><p>{recommendation.replace(chr(10), '<br>')}</p>", unsafe_allow_html=True)

    # Display image
    image_path = find_image(filename_base)
    if image_path:
        st.image(image_path, caption=f"👗 Example Outfit for {category}", use_container_width=True)
    else:
        st.warning("⚠️ No image available for this combination.")
