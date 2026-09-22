import streamlit as st
import pandas as pd
import joblib
import base64
import os


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# FIND HOUSE IMAGE
# =========================================================

image_files = [
    "house.jpg",
    "house.jpeg",
    "house.png"
]

image_path = None

for file in image_files:
    if os.path.exists(file):
        image_path = file
        break


if image_path is None:

    st.error(
        "❌ House image not found.\n\n"
        "Please keep house.jpg in the same folder as app.py."
    )

    st.stop()


# =========================================================
# CONVERT IMAGE TO BASE64
# =========================================================

with open(image_path, "rb") as image_file:

    image_data = base64.b64encode(
        image_file.read()
    ).decode()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* ==========================================
       REMOVE DEFAULT STREAMLIT BACKGROUND
       ========================================== */

    .stApp {{
        background: transparent !important;
    }}


    /* ==========================================
       BLURRED HOUSE BACKGROUND
       ========================================== */

    .stApp::before {{

        content: "";

        position: fixed;

        top: -30px;
        left: -30px;
        right: -30px;
        bottom: -30px;

        background-image:

        linear-gradient(
            rgba(5, 15, 35, 0.68),
            rgba(5, 15, 35, 0.68)
        ),

        url(
            "data:image/jpeg;base64,{image_data}"
        );

        background-size: cover;

        background-position: center;

        background-repeat: no-repeat;

        filter: blur(8px);

        transform: scale(1.05);

        z-index: -2;
    }}


    /* ==========================================
       PAGE WIDTH
       ========================================== */

    .block-container {{

        max-width: 1050px;

        padding-top: 35px;

        padding-bottom: 40px;
    }}


    /* ==========================================
       TITLE
       ========================================== */

    .main-title {{

        text-align: center;

        color: white;

        font-size: 45px;

        font-weight: 800;

        margin-bottom: 8px;

        text-shadow:
        0px 3px 10px rgba(0,0,0,0.7);
    }}


    /* ==========================================
       SUBTITLE
       ========================================== */

    .subtitle {{

        text-align: center;

        color: #e5e7eb;

        font-size: 18px;

        margin-bottom: 35px;
    }}


    /* ==========================================
       SECTION TITLE
       ========================================== */

    .section-title {{

        color: #8ec5ff;

        font-size: 26px;

        font-weight: 700;

        margin-bottom: 20px;

        text-shadow:
        0px 2px 8px rgba(0,0,0,0.5);
    }}


    /* ==========================================
       INPUT LABELS
       ========================================== */

    label {{

        color: white !important;

        font-weight: 600 !important;

    }}


    /* ==========================================
       INPUT BOXES
       ========================================== */

    div[data-baseweb="input"] {{

        background-color:
        rgba(10, 20, 40, 0.75)
        !important;

        border-radius: 10px
        !important;

        border:
        1px solid
        rgba(255,255,255,0.18)
        !important;

    }}


    input {{

        color: white !important;

        background-color:
        transparent !important;

    }}


    /* ==========================================
       PREDICTION BUTTON
       ========================================== */

    div.stButton > button {{

        background:
        linear-gradient(
            90deg,
            #1677ff,
            #2f8cff
        );

        color: white;

        border: none;

        border-radius: 12px;

        height: 55px;

        font-size: 18px;

        font-weight: 700;

        padding-left: 30px;

        padding-right: 30px;

        box-shadow:
        0px 6px 18px
        rgba(22,119,255,0.40);

        transition: 0.3s;

    }}


    div.stButton > button:hover {{

        background:
        linear-gradient(
            90deg,
            #0d63d8,
            #1677ff
        );

        transform: translateY(-2px);

    }}


    /* ==========================================
       PRICE TITLE
       ========================================== */

    .price-title {{

        text-align: center;

        color: #8df5c1;

        font-size: 21px;

        font-weight: 600;

        margin-top: 30px;

        text-shadow:
        0px 2px 8px rgba(0,0,0,0.5);

    }}


    /* ==========================================
       PRICE
       ========================================== */

    .price {{

        text-align: center;

        color: white;

        font-size: 42px;

        font-weight: 800;

        margin-top: 8px;

        margin-bottom: 25px;

        text-shadow:
        0px 3px 12px rgba(0,0,0,0.7);

    }}


    /* ==========================================
       HOUSE DETAILS HEADING
       ========================================== */

    h3 {{

        color: white !important;

    }}


    /* ==========================================
       DATAFRAME
       ========================================== */

    div[data-testid="stDataFrame"] {{

        border-radius: 12px;

        overflow: hidden;

    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    """
    <div class="main-title">
        🏠 House Price Prediction
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="subtitle">
        Enter the house details to predict the house price.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HOUSE DETAILS
# =========================================================

st.markdown(
    """
    <div class="section-title">
        🏡 House Details
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

try:

    model = joblib.load(
        "house_price_model.pkl"
    )

except FileNotFoundError:

    st.error(
        "❌ house_price_model.pkl not found.\n\n"
        "Please keep the model file in the same folder "
        "as app.py."
    )

    st.stop()

except Exception as e:

    st.error(
        f"❌ Unable to load the model: {e}"
    )

    st.stop()


# =========================================================
# INPUT FIELDS
# =========================================================

col1, col2 = st.columns(2)


# ---------------------------------------------------------
# LEFT COLUMN
# ---------------------------------------------------------

with col1:

    overall_qual = st.number_input(
        "⭐ Overall Quality",
        min_value=1,
        max_value=10,
        value=7,
        step=1
    )


    gr_liv_area = st.number_input(
        "📐 Living Area (sq ft)",
        min_value=100,
        max_value=10000,
        value=1800,
        step=50
    )


    garage_cars = st.number_input(
        "🚗 Garage Capacity",
        min_value=0,
        max_value=5,
        value=2,
        step=1
    )


    total_bsmt_sf = st.number_input(
        "🏠 Basement Area (sq ft)",
        min_value=0,
        max_value=5000,
        value=1000,
        step=50
    )


# ---------------------------------------------------------
# RIGHT COLUMN
# ---------------------------------------------------------

with col2:

    year_built = st.number_input(
        "📅 Year Built",
        min_value=1800,
        max_value=2026,
        value=2005,
        step=1
    )


    full_bath = st.number_input(
        "🛁 Full Bathrooms",
        min_value=0,
        max_value=5,
        value=2,
        step=1
    )


    bedroom_abv_gr = st.number_input(
        "🛏️ Number of Bedrooms",
        min_value=0,
        max_value=10,
        value=3,
        step=1
    )


# =========================================================
# BUTTON
# =========================================================

st.write("")


if st.button(
    "🔮 Predict House Price"
):

    # =====================================================
    # CREATE INPUT DATAFRAME
    # =====================================================

    new_house = pd.DataFrame({

        "OverallQual": [
            overall_qual
        ],

        "GrLivArea": [
            gr_liv_area
        ],

        "GarageCars": [
            garage_cars
        ],

        "TotalBsmtSF": [
            total_bsmt_sf
        ],

        "YearBuilt": [
            year_built
        ],

        "FullBath": [
            full_bath
        ],

        "BedroomAbvGr": [
            bedroom_abv_gr
        ]

    })


    # =====================================================
    # MAKE PREDICTION
    # =====================================================

    try:

        prediction = model.predict(
            new_house
        )

        price = prediction[0]


        # =================================================
        # DISPLAY PREDICTED PRICE
        # =================================================

        st.markdown(
            """
            <div class="price-title">
                💰 Predicted House Price
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="price">
                ${price:,.2f}
            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # DISPLAY HOUSE DETAILS
        # =================================================

        st.markdown(
            "### 📋 House Details"
        )


        details = pd.DataFrame({

            "Feature": [

                "Overall Quality",

                "Living Area",

                "Garage Capacity",

                "Basement Area",

                "Year Built",

                "Full Bathrooms",

                "Number of Bedrooms"

            ],

            "Value": [

                overall_qual,

                f"{gr_liv_area:,} sq ft",

                garage_cars,

                f"{total_bsmt_sf:,} sq ft",

                year_built,

                full_bath,

                bedroom_abv_gr

            ]

        })


        st.dataframe(
            details,
            use_container_width=True,
            hide_index=True
        )


        # =================================================
        # INFORMATION
        # =================================================

        st.info(
            "ℹ️ The predicted price is an estimated value "
            "generated by the trained Machine Learning model."
        )


    except ValueError as e:

        st.error(
            "❌ Feature mismatch with the trained model."
        )

        st.write(
            "Please check that the model was trained "
            "using the same seven features as this application."
        )

        st.code(str(e))


    except Exception as e:

        st.error(
            f"❌ Prediction failed: {e}"
        )