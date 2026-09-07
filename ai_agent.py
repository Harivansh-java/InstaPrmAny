import streamlit as st
import google.generativeai as genai

def configure_genai():
    try:
        # Yeh Streamlit secrets se key securely uthayega
        api_key = st.secrets["GEMINI_KEY"]
        if api_key:
            genai.configure(api_key=api_key)
            return genai.GenerativeModel('gemini-3.6-flash')
    except Exception:
        return None
    return None

# ==========================================
# FEATURE 1: Analytics Analyzer
# ==========================================
@st.cache_data(show_spinner=False)
def analyze_with_ai(post_data, language="English"):
    model = configure_genai()
    if not model: return "⚠️ Please add your Gemini API Key in the code."
    
    prompt = f"""
    Act as an elite Instagram Growth Strategist. I am providing you with the backend metrics of my recent post.
    
    Post Details:
    - Caption/Topic: {post_data['info'].get('caption', 'N/A')}
    - Format: {post_data['info'].get('media_type', 'N/A')}
    
    Performance Data:
    - Reach: {post_data['metrics'].get('reach', 0)}
    - Impressions: {post_data['metrics'].get('impressions', 0)}
    - Saves (High intent): {post_data['metrics'].get('saved', 0)}
    - Shares (Viral intent): {post_data['metrics'].get('shares', 0)}
    
    Based on this data, provide:
    0. TL;DR (Quick Summary): At the very beginning, give a 2-sentence punchy summary of the performance and the next immediate step. Highlight this section.
    1. Performance Diagnosis: Did this post perform well based on saves vs shares vs reach?
    2. Next Steps: What exact format and content angle should I use for my NEXT post to maximize growth?
    3. Formatting: Keep it crisp, use bullet points, and highlight key terms. Be highly analytical.
    
    CRITICAL INSTRUCTION: You must generate the ENTIRE response in {language} language.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        # Quota limit check
        if "429" in error_msg or "ResourceExhausted" in error_msg or "quota" in error_msg.lower():
            return "⏳ **API Quota Limit Reached!** \n\nKripya **30 se 60 minutes** ka wait karein ya thoda samay dein. Google ka free tier limit cross ho chuka hai, yeh thodi der mein apne aap reset ho jayega."
        return f"AI Error: {error_msg}"

# ==========================================
# FEATURE 2: Viral Hook & Caption Generator
# ==========================================
def generate_hooks_captions(topic, tone, language="English"):
    model = configure_genai()
    if not model: return "⚠️ Please add your Gemini API Key in the code."
    
    prompt = f"""
    Act as a viral Instagram Copywriter. 
    Topic: {topic}
    Tone of voice: {tone}
    
    Please provide:
    1. 3 highly engaging, scroll-stopping Hooks (Text to put on the video).
    2. 1 optimized Caption that creates curiosity and encourages comments.
    3. 15 highly targeted SEO Hashtags.
    
    CRITICAL: Generate the ENTIRE response in {language}. Format beautifully.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        # Quota limit check
        if "429" in error_msg or "ResourceExhausted" in error_msg or "quota" in error_msg.lower():
            return "⏳ **API Quota Limit Reached!** \n\nKripya **30 se 60 minutes** ka wait karein ya thoda samay dein. Google ka free tier limit cross ho chuka hai, yeh thodi der mein apne aap reset ho jayega."
        return f"AI Error: {error_msg}"

# ==========================================
# FEATURE 3: Screenshot Analyzer 
# ==========================================
def analyze_screenshot(image, language="English"):
    model = configure_genai()
    if not model: return "⚠️ Please add your Gemini API Key in the code."
    
    prompt = f"""
    Act as an expert Instagram Content Strategist. I have uploaded a screenshot of an Instagram post, dashboard, or competitor's content.
    
    Please analyze this image and provide:
    1. Core Concept: What is the main idea or topic of this post?
    2. 3 Fresh Hooks: Give me 3 brand new, viral hooks to recreate this concept in my own way.
    3. Suggested Format: Should I make this a Reel, Carousel, or Single Image? Why?
    4. Call to Action (CTA): A strong CTA for the caption.
    
    CRITICAL: Generate the ENTIRE response in {language}.
    """
    try:
        response = model.generate_content([prompt,image])
        return response.text
    except Exception as e:
        error_msg = str(e)
        # Quota limit check
        if "429" in error_msg or "ResourceExhausted" in error_msg or "quota" in error_msg.lower():
            return "⏳ **API Quota Limit Reached!** \n\nKripya **30 se 60 minutes** ka wait karein ya thoda samay dein. Google ka free tier limit cross ho chuka hai, yeh thodi der mein apne aap reset ho jayega."
        return f"AI Error: {error_msg}"