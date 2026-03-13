import streamlit as st
from PIL import Image
import os

# --- Page Setup ---
st.set_page_config(page_title="Fashion Outfit Recommender", page_icon="👗", layout="wide")

# --- Background and Styling ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #CCA25A 0%, #FFB16E 33%, #FFF5B8 66%, #45ADAB 100%);
    color: #000000;
}
h1, h2, h3, h4, h5, h6 {
    color: #333333;
}
.big-card {
    background-color: #FFE4C4;
    border-radius: 20px;
    height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 22px;
    margin: 10px;
    cursor: pointer;
    box-shadow: 4px 4px 10px #aaaaaa;
}
.big-card:hover {
    background-color: #FFDAB9;
}
.nav-btn {
    background-color: #45ADAB !important;
    color: white !important;
    border-radius: 10px;
    height: 50px;
    width: 120px;
    font-size: 20px;
    margin: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state: st.session_state.page = 1
if "category" not in st.session_state: st.session_state.category = None
if "child_type" not in st.session_state: st.session_state.child_type = None
if "temperature" not in st.session_state: st.session_state.temperature = None
if "place" not in st.session_state: st.session_state.place = None

# --- Navigation Functions ---
def go_to_page(page_num):
    st.session_state.page = page_num

# --- PAGE 1: Title ---
if st.session_state.page == 1:
    st.title("👗 Fashion Outfit Recommender")
    st.subheader("Your Personalized Fashion Assistant 👠")
    st.markdown("Welcome! This app helps you pick the perfect outfit based on **category, weather, and location**.")
    if st.button("➡️ Next", key="next1"):
        go_to_page(2)

# --- PAGE 2: Category Selection ---
elif st.session_state.page == 2:
    st.header("👕 Step 1: Select Your Category")
    categories = ["Men", "Women", "Children"]
    emojis = ["👨", "👩", "🧒"]

    cols = st.columns(len(categories))
    for i, cat in enumerate(categories):
        if st.button(f"{emojis[i]} {cat}", key=f"cat_{cat}"):
            st.session_state.category = cat
            if cat == "Children":
                go_to_page(2.5)
            else:
                go_to_page(3)

    if st.session_state.page > 2:
        pass
    else:
        st.button("⬅️ Back to Start", key="back1", on_click=lambda: go_to_page(1))

# --- PAGE 2.5: Child Type Selection ---
elif st.session_state.page == 2.5:
    st.header("🧒 Step 1a: Select Child Type")
    child_types = ["Boy", "Girl"]
    emojis = ["👦", "👧"]

    cols = st.columns(len(child_types))
    for i, ct in enumerate(child_types):
        if st.button(f"{emojis[i]} {ct}", key=f"child_{ct}"):
            st.session_state.child_type = ct
            go_to_page(3)

    st.button("⬅️ Back", key="back2", on_click=lambda: go_to_page(2))

# --- PAGE 3: Weather Selection ---
elif st.session_state.page == 3:
    st.header("🌤️ Step 2: Select Temperature / Weather")
    weather_options = ["Hot", "Cold", "Rainy", "Sunny", "Overcast"]
    cols = st.columns(len(weather_options))
    for i, w in enumerate(weather_options):
        if st.button(w, key=f"weather_{w}"):
            st.session_state.temperature = w
            go_to_page(4)

    st.button("⬅️ Back", key="back3", on_click=lambda: go_to_page(2 if st.session_state.category != "Children" else 2.5))

# --- PAGE 4: Place Selection ---
elif st.session_state.page == 4:
    st.header("📍 Step 3: Select Place")
    places = ["Beach", "Park", "Restaurant", "City", "Mountains"]
    cols = st.columns(len(places))
    for i, p in enumerate(places):
        if st.button(p, key=f"place_{p}"):
            st.session_state.place = p
            go_to_page(5)

    st.button("⬅️ Back", key="back4", on_click=lambda: go_to_page(3))

# --- PAGE 5: Final Recommendation ---
elif st.session_state.page == 5:
    st.header("🎯 Step 4: Your Outfit Recommendations")
    if st.button("⬅️ Back", key="back_final"):
        go_to_page(4)
    if st.button("🔄 Restart", key="restart_final"):
        st.session_state.page = 1
        st.session_state.category = None
        st.session_state.child_type = None
        st.session_state.temperature = None
        st.session_state.place = None

    category = st.session_state.category
    child_type = st.session_state.child_type
    temperature = st.session_state.temperature
    place = st.session_state.place

    # --- Fashion Rules ---
    default_rules = {
        "Women": {
            "Hot": {"tip": "👗 Light cotton dress or sleeveless top with shorts.",
                    "samples": ["White sundress + sandals 🌼","Crop top + denim shorts ☀️","Linen jumpsuit + flats 👡","Tank top + skirt 😎"]},
            "Cold": {"tip": "🧥 Layer with sweaters and coats for warmth.",
                     "samples": ["Wool coat + jeans + boots 🥾","Sweater dress + tights 👢","Puffer jacket + scarf 🧣","Turtleneck + gloves 🧤"]},
            "Rainy": {"tip": "☔ Rainy-day outfits with waterproof layers.",
                      "samples": ["Raincoat + boots 🌧️","Umbrella + trench coat ☂️","Waterproof jacket + jeans 👢","Hoodie + rain boots 🥾"]},
            "Sunny": {"tip": "😎 Bright sunny-day outfits with light fabrics.",
                      "samples": ["Sundress + sunglasses 🌞","Tank top + shorts 🩴","Light blouse + skirt 👡","T-shirt + linen pants 🩳"]},
            "Overcast": {"tip": "🌥️ Overcast weather, layer comfortably.",
                         "samples": ["Cardigan + jeans 👖","Long sleeve top + skirt 👡","Light jacket + trousers 🧥","Sweater + leggings 🧤"]},
        },
        "Men": {
            "Hot": {"tip": "👕 Light T-shirts and shorts for comfort in the heat.",
                    "samples": ["Cotton T-shirt + shorts 🩴","Linen shirt + chinos 👞","Tank top + sneakers 👟","Polo shirt + sunglasses 😎"]},
            "Cold": {"tip": "🧥 Layer with sweaters and jackets to keep warm.",
                     "samples": ["Wool sweater + jeans 🥾","Jacket + hoodie + cargo pants 👖","Coat + turtleneck 🧤","Puffer + jeans 👢"]},
            "Rainy": {"tip": "☔ Waterproof layers for rainy weather.",
                      "samples": ["Raincoat + boots 🌧️","Hooded jacket + jeans 👢","Umbrella + sweater 👞","Parka + sneakers 🥾"]},
            "Sunny": {"tip": "😎 Cool outfits for sunny days.",
                      "samples": ["T-shirt + shorts 🩴","Short-sleeve shirt + chinos 👟","Tank top + sneakers 🩳","Linen shirt + sunglasses 🌞"]},
            "Overcast": {"tip": "🌥️ Light layering for cloudy days.",
                         "samples": ["Sweater + jeans 👖","Light jacket + chinos 👞","Hoodie + cargo pants 🧤","Long sleeve shirt + sneakers 👟"]},
        },
        "Children": {
            "Boy": {
                "Hot": {"tip": "👕 Cotton shirts and shorts keep kids comfy.",
                        "samples": ["T-shirt + shorts + sandals 🩴","Sleeveless top + shorts ☀️","Light shirt + sneakers 👟","Printed tee + cap 🧢"]},
                "Cold": {"tip": "🧥 Keep warm with layered clothing.",
                         "samples": ["Jacket + jeans + boots 🥾","Sweater + pants 🧣","Hoodie + joggers 👟","Coat + gloves 🧤"]},
                "Rainy": {"tip": "☔ Rainy weather gear for boys.",
                          "samples": ["Raincoat + boots 🌧️","Hooded jacket + pants 👟","Waterproof hoodie + sneakers 🥾","Umbrella + jeans 🧢"]},
                "Sunny": {"tip": "😎 Light sunny-day clothes.",
                          "samples": ["T-shirt + shorts 🩴","Cap + tank top ☀️","Light shirt + sneakers 👟","Printed tee + sandals 🩴"]},
                "Overcast": {"tip": "🌥️ Comfortable layered outfits.",
                             "samples": ["Long sleeve shirt + jeans 👖","Hoodie + shorts 🩳","Sweater + pants 🧤","Light jacket + sneakers 👟"]},
            },
            "Girl": {
                "Hot": {"tip": "👗 Dresses or tops with shorts are perfect.",
                        "samples": ["Sundress + sandals 🌼","Top + shorts + hat 🧢","Skirt + T-shirt 👟","Tank top + leggings 👡"]},
                "Cold": {"tip": "🧥 Keep cozy with sweaters and leggings.",
                         "samples": ["Sweater + skirt 🥾","Jacket + jeans 🧣","Coat + tights 👢","Hoodie + leggings 👕"]},
                "Rainy": {"tip": "☔ Rainy-day outfits for girls.",
                          "samples": ["Raincoat + boots 🌧️","Hooded jacket + leggings 👢","Waterproof poncho + skirt 🥾","Umbrella + shoes 👡"]},
                "Sunny": {"tip": "😎 Light sunny-day outfits.",
                          "samples": ["Sundress + hat 🌞","Tank top + shorts 🩴","Top + skirt + sandals 👡","Light dress + sneakers 👟"]},
                "Overcast": {"tip": "🌥️ Layered outfits for cloudy days.",
                             "samples": ["Long sleeve top + jeans 👖","Cardigan + skirt 👡","Sweater + leggings 🧤","Light jacket + pants 👟"]},
            }
        }
    }

    try:
        if category == "Children":
            rec = default_rules[category][child_type][temperature]
        else:
            rec = default_rules[category][temperature]
    except KeyError:
        rec = {"tip":"No tip available","samples":["No sample outfit"]}

    st.subheader("💡 Fashion Tip:")
    st.write(rec["tip"])
    st.subheader("👕 Sample Outfit Ideas:")
    for s in rec["samples"]:
        st.write(f"- {s}")

    # --- Images ---
    base_path = "C:/Users/harsh/OneDrive/Desktop/fashion/images"
    if category == "Children":
        image_folder = f"{base_path}/{category.lower()}/{child_type.lower()}/{temperature.lower()}/{place.lower()}"
    else:
        image_folder = f"{base_path}/{category.lower()}/{temperature.lower()}/{place.lower()}"

    st.subheader("📸 Outfit Inspiration:")
    if os.path.exists(image_folder):
        image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            cols = st.columns(4)
            for i, img_path in enumerate(image_files[:4]):
                with cols[i % 4]:
                    img = Image.open(img_path)
                    img = img.resize((300, 400))
                    st.image(img, caption=f"Look {i+1}", width=300)
        else:
            st.warning("⚠️ No images found!")
    else:
        st.warning("⚠️ Image folder not found!")
