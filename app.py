import streamlit as st
import joblib
import numpy as np
import time

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="BrightMart Sales Prediction",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------

model = joblib.load("linear.sav")

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    max-width: 1100px;
    padding-top: 45px;
    padding-bottom: 40px;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #172033;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 19px;
    color: #667085;
    margin-bottom: 8px;
}

.description {
    text-align: center;
    font-size: 14px;
    color: #98a2b3;
    margin-bottom: 35px;
}

/* Input cards */
.input-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e4e7ec;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
    margin-bottom: 10px;
}

.input-title {
    font-size: 17px;
    font-weight: 600;
    color: #172033;
    text-align: center;
    margin-bottom: 5px;
}

.input-description {
    font-size: 13px;
    color: #667085;
    text-align: center;
}

/* Countdown */
.countdown-box {
    background-color: white;
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    margin-top: 30px;
    border: 1px solid #e4e7ec;
    box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.06);
}

.countdown-number {
    font-size: 60px;
    font-weight: 700;
    color: #172033;
    margin: 5px;
}

.countdown-text {
    font-size: 16px;
    color: #667085;
}

/* Prediction result */
.prediction-box {
    background: linear-gradient(135deg, #172033, #263452);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    margin-top: 30px;
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.15);
}

.prediction-label {
    color: #d0d5dd;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.prediction-value {
    color: white;
    font-size: 52px;
    font-weight: 700;
    margin: 5px 0;
}

.prediction-description {
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 8px;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
}

/* Information box */
.info-box {
    background-color: white;
    border-left: 4px solid #172033;
    padding: 18px 22px;
    border-radius: 10px;
    margin-top: 25px;
    color: #475467;
    font-size: 14px;
}

/* Footer */
.footer {
    text-align: center;
    color: #98a2b3;
    font-size: 13px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📈 BrightMart Sales Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Advertising Impact Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">Enter your advertising budgets to estimate expected sales</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

# TV Advertising
with col1:

    st.markdown(
        """
<div class="input-card">
    <div class="input-title">📺 TV Advertising</div>
    <div class="input-description">
        Budget allocated to TV advertising
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    TV = st.number_input(
        "TV Advertising Budget",
        min_value=0.0,
        value=100.0,
        step=1.0,
        label_visibility="collapsed"
    )

# Radio Advertising
with col2:

    st.markdown(
        """
<div class="input-card">
    <div class="input-title">📻 Radio Advertising</div>
    <div class="input-description">
        Budget allocated to radio advertising
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    Radio = st.number_input(
        "Radio Advertising Budget",
        min_value=0.0,
        value=20.0,
        step=1.0,
        label_visibility="collapsed"
    )

# Newspaper Advertising
with col3:

    st.markdown(
        """
<div class="input-card">
    <div class="input-title">📰 Newspaper Advertising</div>
    <div class="input-description">
        Budget allocated to newspaper advertising
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    Newspaper = st.number_input(
        "Newspaper Advertising Budget",
        min_value=0.0,
        value=10.0,
        step=1.0,
        label_visibility="collapsed"
    )

# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2, button_col3 = st.columns([1, 1, 1])

with button_col2:

    predict = st.button("🔮 Predict Sales")

# --------------------------------------------------
# PREDICTION + COUNTDOWN
# --------------------------------------------------

if predict:

    # Prepare input
    input_data = np.array([[TV, Radio, Newspaper]])

    # Temporary area for countdown/result
    message = st.empty()

    # ----------------------------------------------
    # PLEASE WAIT
    # ----------------------------------------------

    message.markdown(
        """
<div class="countdown-box">
    <div style="font-size:30px;">⏳</div>
    <div style="font-size:24px; font-weight:600; color:#172033;">
        Please wait...
    </div>
    <div class="countdown-text">
        Calculating your sales prediction
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)

    # ----------------------------------------------
    # COUNTDOWN 3
    # ----------------------------------------------

    message.markdown(
        """
<div class="countdown-box">
    <div class="countdown-number">3</div>
    <div class="countdown-text">
        Analyzing advertising data...
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)

    # ----------------------------------------------
    # COUNTDOWN 2
    # ----------------------------------------------

    message.markdown(
        """
<div class="countdown-box">
    <div class="countdown-number">2</div>
    <div class="countdown-text">
        Processing the prediction model...
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)

    # ----------------------------------------------
    # COUNTDOWN 1
    # ----------------------------------------------

    message.markdown(
        """
<div class="countdown-box">
    <div class="countdown-number">1</div>
    <div class="countdown-text">
        Almost ready...
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)

    # ----------------------------------------------
    # GENERATE PREDICTION
    # ----------------------------------------------

    prediction = model.predict(input_data)[0]

    # ----------------------------------------------
    # FINAL RESULT
    # ----------------------------------------------

    message.markdown(
        f"""
<div class="prediction-box">
    <div class="prediction-label">
        🎯 YOUR PREDICTED SALES
    </div>

    <div class="prediction-value">
        {prediction:.2f}
    </div>

    <div class="prediction-description">
        Estimated sales based on your advertising budget
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------

st.markdown(
    """
<div class="info-box">
    <b>How does it work?</b><br><br>
    This application uses a trained <b>Linear Regression ajna</b> model
    to estimate sales based on TV, Radio and Newspaper advertising expenditure.
</div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
<div class="footer">
    BrightMart Sales Prediction • Linear Regression Model
</div>
    """,
    unsafe_allow_html=True
)
