import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
from ai_agent import analyze_with_ai, generate_hooks_captions, analyze_screenshot

# Page Configuration
st.set_page_config(page_title="Insta AI Expert", page_icon="🚀", layout="centered")

st.title("🚀 The Ultimate Instagram AI Suite")
st.markdown("Analyze metrics, generate viral hooks, or steal ideas from screenshots!")

# Common Language Selector (Sab tabs par kaam karega)
output_language = st.selectbox(
    "🗣️ Choose Output Language / Bhasha Chunein:", 
    ["English", "Hindi", "Hinglish", "Spanish"]
)
st.divider()

# 3 Tabs Banayein
tab1, tab2, tab3 = st.tabs(["📊 Analytics Expert", "🚀 Hook Generator", "📸 Idea Stealer (Screenshot)"])

# ==========================================
# TAB 1: ANALYTICS EXPERT
# ==========================================
with tab1:
    st.subheader("Data-Driven Growth Strategy")
    col1, col2 = st.columns(2)
    with col1:
        post_type = st.selectbox("Post Format", ["REEL", "CAROUSEL", "IMAGE"])
        reach = st.number_input("Total Reach", min_value=0, step=100)
        impressions = st.number_input("Total Impressions", min_value=0, step=100)
    with col2:
        caption_topic = st.text_input("Post Topic / Niche", placeholder="e.g. AI Tools")
        saves = st.number_input("Total Saves", min_value=0, step=10)
        shares = st.number_input("Total Shares", min_value=0, step=10)

    if st.button("Analyze Metrics 🧠"):
        if reach > 0:
            with st.spinner(f"Analyzing in {output_language}..."):
                # Data formatting
                manual_data = {
                    "info": {"caption": caption_topic, "media_type": post_type},
                    "metrics": {"reach": reach, "impressions": impressions, "saved": saves, "shares": shares}
                }
                
                # 1. AI Report Fetch karna
                ai_report = analyze_with_ai(manual_data, language=output_language)
                
                st.divider()
                st.subheader("📊 Performance Dashboard")
                
                # --- VISUALIZATION LOGIC START ---
                col_chart1, col_chart2 = st.columns(2)
                
                # Chart 1: Reach vs Impressions (Bar Chart)
                with col_chart1:
                    df_reach = pd.DataFrame({
                        "Metric": ["Reach", "Impressions"],
                        "Count": [reach, impressions]
                    })
                    fig_reach = px.bar(
                        df_reach, 
                        x="Metric", 
                        y="Count", 
                        text="Count",
                        color="Metric",
                        color_discrete_sequence=["#FF4B4B", "#FFA07A"],
                        title="Reach vs Impressions Funnel"
                    )
                    fig_reach.update_traces(textposition='outside')
                    st.plotly_chart(fig_reach, use_container_width=True)

                # Chart 2: Saves vs Shares (Donut Chart)
                with col_chart2:
                    df_engage = pd.DataFrame({
                        "Action": ["Saves", "Shares"],
                        "Count": [saves, shares]
                    })
                    fig_engage = px.pie(
                        df_engage, 
                        names="Action", 
                        values="Count", 
                        hole=0.5,
                        color="Action",
                        color_discrete_sequence=["#00C4B4", "#0083B8"],
                        title="Engagement Breakdown"
                    )
                    fig_engage.update_traces(textinfo='percent+label')
                    st.plotly_chart(fig_engage, use_container_width=True)
                # --- VISUALIZATION LOGIC END ---

                st.divider()
                
                # 2. AI Strategy Display (Premium UI)
                st.subheader(f"🧠 AI Expert Strategy ({output_language})")
                
                # Python string split logic: Summary ko baahar nikalna
                if "TL;DR" in ai_report or "TL;DR (Quick Summary)" in ai_report:
                    try:
                        # Report ko '1. Performance Diagnosis' se do hisson mein todna
                        parts = ai_report.split("1. Performance Diagnosis", 1)
                        summary_part = parts[0].replace("0. TL;DR (Quick Summary):", "").replace("0. TL;DR:", "").strip()
                        detailed_part = "### 1. Performance Diagnosis\n" + parts[1]
                        
                        # Summary ko ek attractive colored box mein dikhana
                        st.success(f"**⚡ Quick Summary:**\n\n{summary_part}")
                        
                        # Baaki lambi report ko Expander (Dropdown) mein chupana
                        with st.expander("🔽 Read Full Detailed Analysis", expanded=False):
                            st.markdown(detailed_part)
                    except Exception:
                        # Agar kisi wajah se split fail ho jaye, toh default expander
                        with st.expander("🔽 Read Full Detailed Analysis", expanded=False):
                            st.markdown(ai_report)
                else:
                    # Fallback
                    with st.expander("🔽 Read Full Detailed Analysis", expanded=False):
                        st.markdown(ai_report)

# ==========================================
# TAB 2: VIRAL HOOK & CAPTION GENERATOR
# ==========================================
with tab2:
    st.subheader("Generate Scroll-Stopping Content")
    
    topic_input = st.text_input("What is your post about?", placeholder="e.g., 5 Ways to use ChatGPT for students")
    tone_input = st.selectbox("Select Tone", ["Educational", "Funny/Meme", "Inspirational", "Controversial", "Professional"])
    
    if st.button("Generate Content ✨"):
        if topic_input:
            with st.spinner(f"Writing viral content in {output_language}..."):
                ai_content = generate_hooks_captions(topic_input, tone_input, language=output_language)
                st.success("Here is your content!")
                st.markdown(ai_content)
        else:
            st.warning("Please enter a topic first.")

# ==========================================
# TAB 3: SCREENSHOT ANALYZER (Idea Stealer)
# ==========================================
with tab3:
    st.subheader("Steal & Recreate Ideas from Screenshots")
    st.write("Upload a screenshot of a viral reel, post, or dashboard. AI will decode it and give you ideas to recreate it.")
    
    # Image Uploader
    uploaded_file = st.file_uploader("Upload Screenshot", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        # Image ko display karna
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Screenshot", use_container_width=True)
        
        if st.button("Decode Screenshot 📸"):
            with st.spinner(f"AI is analyzing the image in {output_language}..."):
                # Pass the image directly to our AI function
                ai_image_report = analyze_screenshot(image, language=output_language)
                st.subheader("🧠 Re-creation Strategy")
                st.markdown(ai_image_report)