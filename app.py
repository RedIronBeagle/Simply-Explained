import streamlit as st
from google import genai

# This securely grabs your key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)
import time
from google import genai
from google.genai.errors import APIError

# Page layout configuration
st.set_page_config(
    page_title="Simply Explained", page_icon="💡", layout="wide"
)

# Custom CSS for font scaling, sidebar harmonization, clean UI styling, and exact title/subtitle sizing + Print Mode Fixes
st.markdown(
    """
    <style>
    /* Increase font size inside the main output body blocks by ~2 points */
    div[data-testid="stMarkdownContainer"] p, 
    div[data-testid="stMarkdownContainer"] li {
        font-size: 1.2rem !important;
        line-height: 1.6 !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox label, 
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] .stTextInput label {
        font-size: 15px !important;
    }
    
    .app-title {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        text-decoration: underline;
        margin-bottom: 0px;
    }

    .app-subtitle {
        font-size: 1rem !important;
        margin-top: 5px;
        margin-bottom: 20px;
        color: inherit;
    }

    .bottom-line-container {
        background-color: transparent;
        border-left: 4px solid #ffffff;
        padding: 5px 15px;
        margin-top: 10px;
    }
    .bottom-line-title {
        font-size: 44px !important;
        font-weight: bold !important;
        color: inherit;
    }
    .bottom-line-text {
        font-size: 20px !important;
        font-weight: bold !important;
        color: inherit;
        margin-top: 5px;
    }

    /* Print-specific styles: forces clean white background and black text for paper/PDF export */
    @media print {
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        .stButton, .stTextInput {
            display: none !important;
        }
        header, footer {
            display: none !important;
        }
        body, div, span, p, h1, h2, h3, h4, h5, h6, li {
            color: #000000 !important;
            background-color: transparent !important;
        }
        .bottom-line-container {
            border-left: 4px solid #000000 !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Localization dictionary for UI elements based on selected language
UI_TEXT = {
    "English": {
        "api_label": "Gemini API Key",
        "depth_label": "Would you like your answer...",
        "topic_label": "What topic would you like to explore?",
        "topic_placeholder": "e.g., Quantum Computing, Photosynthesis, Inflation",
        "button_label": "Let's get your answer",
        "no_api": "Please enter your Gemini API key in the sidebar to proceed.",
        "no_topic": "Please enter a topic to explain.",
        "ready": "Your answer is ready and it is",
        "subtitle": "Answering complex questions simply.",
        "subtitle_translation": "",
        "bottom_line": "Bottom Line",
        "bottom_line_trans": "(Bottom Line)",
        "spinners": {
            "Easy": "Hey, one second, let me go find it.",
            "In-between": "Pulling together the details...",
            "Hard": "Let me drag the library with us."
        }
    },
    "Spanish (Español)": {
        "api_label": "Clave API de Gemini",
        "depth_label": "¿Te gustaría que tu respuesta sea...",
        "topic_label": "¿Qué tema te gustaría explorar?",
        "topic_placeholder": "ej., Computación Cuántica, Fotosíntesis, Inflación",
        "button_label": "Obtener tu respuesta",
        "no_api": "Por favor ingresa tu clave API de Gemini en la barra lateral para continuar.",
        "no_topic": "Por favor ingresa un tema para explicar.",
        "ready": "Tu respuesta está lista y es",
        "subtitle": "Respondiendo preguntas complejas de manera sencilla.",
        "subtitle_translation": "(Answering complex questions simply)",
        "bottom_line": "En Resumen",
        "bottom_line_trans": "(Bottom Line)",
        "spinners": {
            "Easy": "Oye, un segundo, déjame ir a buscarlo.",
            "In-between": "Juntando los detalles...",
            "Hard": "Déjame traer toda la biblioteca con nosotros."
        }
    },
    "French (Français)": {
        "api_label": "Clé API Gemini",
        "depth_label": "Aimeriez-vous que votre réponse soit...",
        "topic_label": "Quel sujet aimeriez-vous explorer ?",
        "topic_placeholder": "ex., Informatique Quantique, Photosynthèse, Inflation",
        "button_label": "Obtenir votre réponse",
        "no_api": "Veuillez entrer votre clé API Gemini dans la barre latérales pour continuer.",
        "no_topic": "Veuillez entrer un sujet à expliquer.",
        "ready": "Votre réponse est prête et elle est",
        "subtitle": "Expliquer des questions complexes simplement.",
        "subtitle_translation": "(Answering complex questions simply)",
        "bottom_line": "L'essentiel",
        "bottom_line_trans": "(Bottom Line)",
        "spinners": {
            "Easy": "Hé, une seconde, laisse-moi aller le chercher.",
            "In-between": "Rassemblement des détails...",
            "Hard": "Laisse-moi apporter toute la bibliothèque avec nous."
        }
    },
    "German (Deutsch)": {
        "api_label": "Gemini API-Schlüssel",
        "depth_label": "Möchten Sie, dass Ihre Antwort...",
        "topic_label": "Welches Thema möchten Sie erkunden?",
        "topic_placeholder": "z.B. Quantencomputing, Photosynthese, Inflation",
        "button_label": "Antwort erhalten",
        "no_api": "Bitte geben Sie Ihren Gemini API-Schlüssel in der Seitenleiste ein.",
        "no_topic": "Bitte geben Sie ein Thema zum Erklären ein.",
        "ready": "Ihre Antwort ist fertig und sie ist",
        "subtitle": "Komplexe Fragen einfach beantworten.",
        "subtitle_translation": "(Answering complex questions simply)",
        "bottom_line": "Fazit",
        "bottom_line_trans": "(Bottom Line)",
        "spinners": {
            "Easy": "Hey, eine Sekunde, lass mich das kurz suchen.",
            "In-between": "Details werden zusammengetragen...",
            "Hard": "Lass uns am besten die ganze Bibliothek mitnehmen."
        }
    }
}

# Comprehensive list of global languages
all_languages = [
    "English",
    "Spanish (Español)",
    "French (Français)",
    "German (Deutsch)",
    "Mandarin Chinese (中文)",
    "Japanese (日本語)",
    "Portuguese (Português)",
    "Italian (Italiano)",
    "Hindi (हिन्दी)",
    "Arabic (العربية)",
    "Russian (Русский)",
    "Korean (한국어)",
    "Dutch (Nederlands)",
    "Turkish (Türkçe)",
    "Vietnamese (Tiếng Việt)",
    "Polish (Polski)",
    "Swedish (Svenska)",
    "Indonesian (Bahasa Indonesia)",
    "Greek (Ελληνικά)",
    "Hebrew (עברית)",
    "Tagalog",
    "Swahili (Kiswahili)",
    "Ukrainian (Українська)",
    "Farsi (فارسی)",
    "Bengali (বাংলা)",
]

# Sidebar setup: Clean layout without configuration header
language = st.sidebar.selectbox("Pick your language", all_languages)

# Get localization dictionary safely
t = UI_TEXT.get(language, {
    "api_label": "Gemini API Key",
    "depth_label": "Would you like your answer...",
    "topic_label": "What topic would you like to explore?",
    "topic_placeholder": "e.g., Quantum Computing, Photosynthesis, Inflation",
    "button_label": "Let's get your answer",
    "no_api": "Please enter your Gemini API key in the sidebar to proceed.",
    "no_topic": "Please enter a topic to explain.",
    "ready": "Your answer is ready and it is",
    "subtitle": "Answering complex questions simply.",
    "subtitle_translation": "",
    "bottom_line": "Bottom Line",
    "bottom_line_trans": "(Bottom Line)",
    "spinners": {
        "Easy": "Hey, one second, let me go find it.",
        "In-between": "Pulling together the details...",
        "Hard": "Let me drag the library with us."
    }
})

st.sidebar.markdown("---")

api_key_input = st.sidebar.text_input(
    t["api_label"], type="password"
)

st.sidebar.markdown("---")

# Translate depth option keys for display if non-English language selected
if language.startswith("Spanish"):
    display_difficulties = {"Fácil": "Easy", "Intermedio": "In-between", "Difícil": "Hard"}
elif language.startswith("French"):
    display_difficulties = {"Facile": "Easy", "Intermédiaire": "In-between", "Difficile": "Hard"}
elif language.startswith("German"):
    display_difficulties = {"Einfach": "Easy", "Mittel": "In-between", "Schwer": "Hard"}
else:
    display_difficulties = {"Easy": "Easy", "In-between": "In-between", "Hard": "Hard"}

selected_display_depth = st.sidebar.radio(
    t["depth_label"], options=list(display_difficulties.keys()), index=0
)
complexity = display_difficulties[selected_display_depth]

# Creator signature tucked neatly at the bottom of the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='text-align: center; font-size: 0.85rem; opacity: 0.7;'>Built by Ciecor & Gemini</div>", 
    unsafe_allow_html=True
)

# Larger underlined title
st.markdown('<div class="app-title">Simply Explained</div>', unsafe_allow_html=True)

# Subtitle styled smaller (~2 points down)
if t["subtitle_translation"]:
    st.markdown(f'<div class="app-subtitle">{t["subtitle"]} <strong>{t["subtitle_translation"]}</strong></div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="app-subtitle">{t["subtitle"]}</div>', unsafe_allow_html=True)

# Main input field using localized text
topic = st.text_input(
    t["topic_label"],
    placeholder=t["topic_placeholder"],
)

submitted = st.button(t["button_label"], type="primary")

st.markdown("---")

if submitted:
  if not api_key_input:
    st.warning(t["no_api"])
  elif not topic:
    st.warning(t["no_topic"])
  else:
    try:
      api_key = st.secrets["GEMINI_API_KEY"]
      client = genai.Client(api_key=api_key)
      model_choice = "gemini-3.5-flash"

      if complexity == "Easy":
        depth_instruction = (
            "Keep the language extremely simple, use everyday analogies, avoid"
            " heavy jargon, and explain it as if to a beginner or child. At the"
            " very end, include a dedicated section with all references, key"
            " dates, and source details."
        )
      elif complexity == "Hard":
        depth_instruction = (
            "Provide technical depth, precise terminology, structural"
            " mechanics, and advanced nuances suited for a professional or"
            " expert. Seamlessly embed all references, direct quotes, and"
            " active hyperlinks directly within the text of the answers."
        )
      else:
        depth_instruction = (
            "Keep it balanced, clear, and accessible with moderate technical"
            " context. Include references, dates, and background notes as a"
            " second paragraph under each pillar/column answer."
        )

      prompt = f"""
            Explain the topic "{topic}" thoroughly using the following strict structure. 
            
            Special Instructions:
            - If any words in the topic "{topic}" are in ALL CAPS or bolded by the user, pay special attention to them and explicitly emphasize them in the response.
            - Include proper spelling verification, auto-corrections, or recommended spelling/naming notes for key proper nouns, names, or places relevant to the topic if any ambiguity exists.
            
            Style & Depth Directive: {depth_instruction}
            Language Directive: Write the entire response in {language}, translating all sections and explanations into this language (keep the main title 'Simply Explained' in English).

            Structure required:
            1. Big Picture (Core summary of what it is)
            2. Origins (History or background)
            3. How It Works (Mechanism or workflow)
            4. How did it affect us? (Why it matters / real-world effect)
            5. What did we give up? (Limitations, downsides, or risks)
            6. Hidden Facts (Surprising or lesser-known details)
            7. Where did it come from?

            At the very end, include a standalone section titled "Bottom Line" (without a number) 
            containing an enlightening, concise 2 to 3 sentence takeaway.

            Format your response clearly with headings for each section.
            """

      loading_message = t["spinners"].get(complexity, "Processing...")
      with st.spinner(loading_message):
        try:
          response = client.models.generate_content(
              model=model_choice,
              contents=prompt,
          )
        except APIError:
          # Fallback to standard model if flash version is unavailable
          model_choice = "gemini-2.5-flash"
          response = client.models.generate_content(
              model=model_choice,
              contents=prompt,
          )

      st.success(f"{t['ready']} **{selected_display_depth.lower()}**!")
      st.markdown("\n\n---\n\n")

      response_text = response.text

      if "Bottom Line" in response_text:
        parts = response_text.split("Bottom Line")
        main_content = parts[0].strip()
        bottom_line_content = parts[1].lstrip(":#* \n")

        # Display main content without an extra trailing divider, flowing straight into Bottom Line
        st.markdown(main_content)

        # Only show the parenthetical translation if the selected language is NOT English
        sub_title_html = (
            f'<span style="font-size: 1.1rem; font-weight: normal; opacity: 0.8;">{t["bottom_line_trans"]}</span>'
            if language != "English"
            else ""
        )

        st.markdown(
            f"""
            <div class="bottom-line-container">
                <div class="bottom-line-title">{t["bottom_line"]} {sub_title_html}</div>
                <div class="bottom-line-text">{bottom_line_content}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
      else:
        st.markdown(response_text)

    except APIError as e:
      st.error(f"API Error encountered: {e}")
    except Exception as e:
      st.error(f"An unexpected error occurred: {e}")
