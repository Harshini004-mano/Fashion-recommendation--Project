import streamlit as st

# 🌟 Page config
st.set_page_config(
    page_title="Fashion Recommender App",
    page_icon="👗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🎨 Custom CSS for colors and layout
st.markdown("""
    <style>
    body {
        background-color: #f9f6ff;
    }
    .main {
        background: linear-gradient(to bottom right, #ffffff, #e8d9ff);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }
    h1 {
        color: #5e17eb;
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
        text-shadow: 2px 2px #d1c4e9;
    }
    label, .stSelectbox label {
        color: #4a148c !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 🌟 Title
st.title("👗 Fashion Recommender App")
st.markdown("### _Style suggestions based on weather, place, and your company!_")

# 🌤️ User Inputs
weather = st.selectbox("🌦 Select Temperature", ["Sunny", "Rainy", "Cold", "Hot", "Overcast"])
category = st.selectbox("🧍 Select Category", ["Men", "Women", "Children (Boy)", "Children (Girl)"])
place = st.selectbox("📍 Select Place", ["Beach", "Park", "Restaurant", "City", "Mountains"])
companion = st.selectbox("👫 Going With", ["Friends", "Family", "Date", "Solo"])

# 👕 Recommendation Logic
if st.button("✨ Get Outfit Recommendation"):
    if weather == "Sunny":
        outfit = "Light cotton clothes, sunglasses, and a hat 🌞"
    elif weather == "Rainy":
        outfit = "Waterproof jacket, boots, and an umbrella ☔"
    elif weather == "Cold":
        outfit = "Coat, gloves, and warm boots 🧤"
    elif weather == "Hot":
        outfit = "Sleeveless top and shorts 🩳"
    else:
        outfit = "Comfortable layered outfit with light jacket 🌥️"

    st.success(f"👕 Recommended Outfit for {category}: {outfit}")
    st.balloons()  # 🎈 Fun animation
