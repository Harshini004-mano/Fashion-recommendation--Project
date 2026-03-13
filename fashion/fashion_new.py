import streamlit as st
import os
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="👗 Fashion Outfit Recommender", page_icon="🧥", layout="centered")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        /* Background Gradient */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #d8b4fe, #a78bfa, #fcd34d);
            color: #1f1f1f;
        }

        /* Title */
        .main-title {
            text-align: center;
            font-size: 40px;
            color: #4b0082;
            font-weight: 800;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        /* Buttons */
        .stButton>button {
            width: 230px;
            height: 75px;
            font-size: 18px;
            border-radius: 15px;
            background-color: #e5d4ff;
            color: #222;
            font-weight: 600;
            border: 2px solid #8a63d2;
            margin: 10px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #c5a3ff;
            color: white;
            transform: scale(1.05);
        }

        /* Subheaders */
        h2, h3, h4, .stSubheader {
            color: #3d0075 !important;
        }

        /* Image Styling */
        img {
            border-radius: 12px;
            box-shadow: 0px 3px 8px rgba(0,0,0,0.2);
        }

        /* Centering text */
        .center-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
if "page" not in st.session_state:
    st.session_state.page = 1
if "category" not in st.session_state:
    st.session_state.category = None
if "temperature" not in st.session_state:
    st.session_state.temperature = None
if "place" not in st.session_state:
    st.session_state.place = None
if "child_type" not in st.session_state:
    st.session_state.child_type = None

# --- Helper Function ---
def go_to_page(page_num):
    st.session_state.page = page_num

# --- PAGE 1: CATEGORY SELECTION ---
if st.session_state.page == 1:
    st.markdown("<h1 class='main-title'>👗 Fashion Outfit Recommender</h1>", unsafe_allow_html=True)
    st.subheader("👥 Choose Category")

    cols = st.columns(3)
    with cols[0]:
        if st.button("👨 Men", key="men"):
            st.session_state.category = "Men"
            go_to_page(2)
    with cols[1]:
        if st.button("👩 Women", key="women"):
            st.session_state.category = "Women"
            go_to_page(2)
    with cols[2]:
        if st.button("🧒 Children", key="children"):
            st.session_state.category = "Children"
            go_to_page(2)

# --- PAGE 2: CHILDREN SUBTYPE ---
elif st.session_state.page == 2:
    if st.session_state.category == "Children" and st.session_state.child_type is None:
        st.subheader("🧒 Select Type")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👦 Boy", key="boy"):
                st.session_state.child_type = "Boy"
                go_to_page(3)
        with col2:
            if st.button("👧 Girl", key="girl"):
                st.session_state.child_type = "Girl"
                go_to_page(3)
        st.button("⬅️ Back to Page 1", key="back_to_1_child", on_click=lambda: go_to_page(1))
    else:
        go_to_page(3)

# --- PAGE 3: TEMPERATURE ---
elif st.session_state.page == 3:
    st.subheader("🌡️ Choose Temperature")
    temps = ["Hot", "Cold", "Rainy", "Sunny", "Overcast"]
    cols = st.columns(3)
    for i, t in enumerate(temps):
        with cols[i % 3]:
            if st.button(t, key=f"temp_{t}"):
                st.session_state.temperature = t
                go_to_page(4)
    st.button("⬅️ Back to Page 1", key="back_to_1_temp", on_click=lambda: go_to_page(1))

# --- PAGE 4: PLACE ---
elif st.session_state.page == 4:
    st.subheader("📍 Choose Place")
    places = ["Home", "Office", "Party", "Beach", "Casual", "Travel"]
    cols = st.columns(3)
    for i, p in enumerate(places):
        with cols[i % 3]:
            if st.button(p, key=f"place_{p}"):
                st.session_state.place = p
                go_to_page(5)
    st.button("⬅️ Back to Page 1", key="back_to_1_place", on_click=lambda: go_to_page(1))

# --- PAGE 5: RECOMMENDATIONS ---
elif st.session_state.page == 5:
    category = st.session_state.category
    temperature = st.session_state.temperature
    place = st.session_state.place
    child_type = st.session_state.child_type

    st.markdown(f"<h2 class='center-text'>🎯 Recommendations for {category} ({temperature}, {place})</h2>", unsafe_allow_html=True)

    # --- Fashion Rules ---
    default_rules = {
        "Men": {
            "Hot": {"tip": "🩳 Light cotton shirts and shorts are perfect.",
                    "samples": ["T-shirt + Shorts", "Light Shirt + Jeans", "Tank Top + Linen Pants", "Cotton Kurta + Pajama"]},
            "Cold": {"tip": "🧥 Layer up with jackets and scarves.",
                     "samples": ["Sweater + Jeans", "Hoodie + Cargo Pants", "Jacket + Scarf + Boots", "Pullover + Denim"]},
            "Rainy": {"tip": "☔ Waterproof jackets and shoes recommended.",
                      "samples": ["Raincoat + Jeans", "Windbreaker + Waterproof Pants", "Boots + Hoodie", "Umbrella + Casual Wear"]},
            "Sunny": {"tip": "😎 Sunglasses and caps add style.",
                      "samples": ["T-shirt + Shorts + Cap", "Linen Shirt + Pants", "Half Shirt + Jeans", "Casual Blazer + T-shirt"]},
            "Overcast": {"tip": "🌥️ Slightly warm clothing recommended.",
                         "samples": ["Full-sleeve Shirt + Pants", "Light Jacket + Jeans", "Sweater + Cotton Pants", "Casual Hoodie"]}
        },
        "Women": {
            "Hot": {"tip": "👗 Flowy dresses or tops are great for comfort.",
                    "samples": ["Sundress + Sandals", "Top + Skirt", "Sleeveless Blouse + Jeans", "Cotton Kurti + Leggings"]},
            "Cold": {"tip": "🧤 Layer with warm coats and boots.",
                     "samples": ["Sweater + Jeans", "Long Coat + Boots", "Cardigan + Dress", "Woolen Kurti + Leggings"]},
            "Rainy": {"tip": "☂️ Go for waterproof outerwear.",
                      "samples": ["Raincoat + Jeans", "Boots + Jacket", "Poncho + Leggings", "Umbrella + Dress"]},
            "Sunny": {"tip": "🌞 Light colors keep you cool.",
                      "samples": ["Dress + Hat", "Tank Top + Skirt", "T-shirt + Shorts", "Cotton Saree + Sandals"]},
            "Overcast": {"tip": "🌤️ Mix of warm and cool layers.",
                         "samples": ["Cardigan + Jeans", "Hoodie + Pants", "Sweater + Skirt", "Light Jacket + Dress"]}
        },
        "Children": {
            "Boy": {
                "Hot": {"tip": "🧢 Cool cotton outfits are best for summer.",
                        "samples": ["T-shirt + Shorts", "Cap + Tank Top", "Light Shirt + Jeans", "Printed Tee + Sandals"]},
                "Cold": {"tip": "🧣 Warm hoodies and jackets are great.",
                         "samples": ["Jacket + Jeans", "Sweater + Trousers", "Coat + Cap", "Pullover + Track Pants"]},
                "Rainy": {"tip": "🌧️ Stay dry with raincoats and boots.",
                          "samples": ["Raincoat + Pants", "Umbrella + Hoodie", "Boots + Shorts", "Windbreaker + Jeans"]},
                "Sunny": {"tip": "😎 Light shirts and caps for sun protection.",
                          "samples": ["T-shirt + Shorts", "Hat + Vest", "Shirt + Jeans", "Printed Tee + Sneakers"]},
                "Overcast": {"tip": "🌤️ Layer lightly for comfort.",
                             "samples": ["Long Sleeve + Jeans", "Hoodie + Shorts", "Sweater + Pants", "Light Jacket + Sneakers"]}
            },
            "Girl": {
                "Hot": {"tip": "👒 Dresses or skirts are great for hot days.",
                        "samples": ["Sundress + Sandals", "Top + Skirt", "Tee + Shorts", "Dress + Hat"]},
                "Cold": {"tip": "🧥 Layer with sweaters and leggings.",
                         "samples": ["Sweater + Jeans", "Jacket + Dress", "Cardigan + Skirt", "Coat + Tights"]},
                "Rainy": {"tip": "☔ Raincoat and boots make rainy days fun!",
                          "samples": ["Raincoat + Boots", "Jacket + Leggings", "Poncho + Skirt", "Umbrella + Shoes"]},
                "Sunny": {"tip": "🌞 Light frocks and cotton wear.",
                          "samples": ["Frock + Sandals", "Top + Shorts", "Tee + Skirt", "Dress + Cap"]},
                "Overcast": {"tip": "🌥️ Cozy yet comfy layers.",
                             "samples": ["Sweater + Leggings", "Cardigan + Skirt", "Light Jacket + Pants", "Top + Jeans"]}
            }
        }
    }

    # --- Fetch Rules ---
    try:
        if category == "Children":
            rec = default_rules[category][child_type][temperature]
        else:
            rec = default_rules[category][temperature]
    except KeyError:
        rec = {"tip": "No tip available.", "samples": ["No sample outfit."]}

    st.subheader("💡 Fashion Tip:")
    st.write(rec["tip"])
    st.subheader("👕 Outfit Ideas:")
    for s in rec["samples"]:
        st.write(f"- {s}")

    # --- Load Images ---
    base_path = "C:/Users/harsh/OneDrive/Desktop/fashion/images"
    if category == "Children":
        image_folder = f"{base_path}/{category.lower()}/{child_type.lower()}/{temperature.lower()}/{place.lower()}"
    else:
        image_folder = f"{base_path}/{category.lower()}/{temperature.lower()}/{place.lower()}"

    st.subheader("📸 Outfit Inspiration:")
    if os.path.exists(image_folder):
        images = [os.path.join(image_folder, i) for i in os.listdir(image_folder)
                  if i.lower().endswith((".png", ".jpg", ".jpeg"))]
        if images:
            cols = st.columns(4)
            for i, img_path in enumerate(images[:4]):
                with cols[i % 4]:
                    img = Image.open(img_path)
                    st.image(img, caption=f"Look {i+1}", width=250)
        else:
            st.warning("⚠️ No images found.")
    else:
        st.warning("⚠️ Image folder not found.")

    if st.button("🔄 Restart (Go to Page 1)", key="restart"):
        st.session_state.page = 1
        st.session_state.category = None
        st.session_state.temperature = None
        st.session_state.place = None
        st.session_state.child_type = None
        st.rerun()

