# ==============================================================================
# PROJECT: Simply Explained & Document Decoder (Master Script Base v5.0 - Multi-Language Global Engine)
# FILE: app.py / main.py
# ARCHITECTURAL BASE: v2026.09.04 (Multi-Language Sidebar, Tabs 1-3, PDF, Terms, & Persona Nuance Localization)
# ==============================================================================

# ==============================================================================
# [SECTION 1: IMPORTS & ENVIRONMENT SETUP]
# ==============================================================================
import datetime
import io
import os
import re
import sys
import time
from bs4 import BeautifulSoup
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import requests
import streamlit as st
from google import genai
from google.genai.errors import APIError
from google.genai import types

TTS_LANG_MAP = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja",
    "Mandarin": "zh-cn",
    "Hindi": "hi"
}
#os.environ["GEMINI_API_KEY"] = ""
    
MODEL_ID = "gemini-3.6-flash"

# Streamlit automatically grabs it from secrets.toml (locally) or Cloud Dashboard (production)
api_key = st.secrets["GEMINI_API_KEY"]

# Initialize the client securely
client = genai.Client(api_key=api_key)

# ==============================================================================
# [SECTION 2: LEGAL & TERMS OF SERVICE (EULA) TEXT CONTENT (LOCALIZED)]
# ==============================================================================
TERMS_TEXT = {
    "English": """
### 📜 Terms of Service & End User License Agreement (EULA)
**Last Updated: September 4, 2026**

Welcome to Simply Explained ("the Application," "we," "us," or "our"). By accessing, installing, downloading, deploying, or merely thinking about using our web application, tools, APIs, and associated services (collectively, the "Service"), you ("User," "you," or "your") acknowledge that you have read, understood, and agreed to be legally bound by these Terms of Service ("Terms").

If you do not agree to these Terms in their entirety, you must immediately cease all access to the Service, delete your browser cache, and quietly contemplate your life choices.

#### 🔒 Privacy & Sensitive Document Notice
* **We Keep Nothing:** Whatever you’re putting in here, trust us: nobody really cares. Your documents aren't special, and we have zero interest in wasting server space or brain cells remembering them. We wipe it out immediately because hoarding your boring clutter is useless to us anyway. Move on.
* **Your Responsibility:** Please refrain from uploading deeply confidential credentials, financial keys, or restricted personal records. While we keep nothing, protecting your data privacy starts on your end.

#### 1. Acceptance of Terms & Legal Capacity
* **1.1 Legal Capacity:** You represent and warrant that you are at least 18 years of age (or the legal age of majority in your jurisdiction) and possess the full legal right, capacity, and mental fortitude to enter into this contract.
* **1.2 Binding Agreement:** Your consent to these Terms constitutes a valid, binding contract under all applicable domestic, federal, state, and international laws, treaties, maritime codes, and galactic protocols.
* **1.3 The Matrix Provision:** You acknowledge that taking the blue pill allows you to wake up in your bed and believe whatever you want to believe. However, by clicking "I Agree" or continuing to use this software, you take the red pill, stay in Wonderland, and agree to see how deep the rabbit hole goes.
* **1.4 Time-Traveler Waiver:** If you are accessing this Service from a future timeline or parallel universe, you explicitly agree that your local temporal paradoxes do not invalidate these Terms, nor shall you hold us liable for any accidental erasure of your ancestors.

#### 2. General Disclaimers & No Professional Advice
* **2.1 Informational Use Only:** The Service utilizes artificial intelligence to synthesize, summarize, and simplify user-provided content. All d output is strictly for informational, educational, and entertainment purposes.
* **2.2 Not Professional Counsel:** The output produced by the Application does NOT constitute professional legal, financial, tax, accounting, or medical advice. You agree not to rely upon the Service as a substitute for actual qualified human professionals.
* **2.3 Warranty of Accuracy:** AI-generated summaries may contain hallucinations, errors, or wild misinterpretations. We make zero guarantees regarding accuracy, completeness, or sanity.
* **2.4 The Princess Bride Standard:** You agree that using words like "Inconceivable!" to describe our AI's outputs does not mean what you think it means, and we are not liable if the system occasionally falls victim to a classic blunder—the most famous of which is never get involved in a land war in Asia.

#### 3. Intellectual Property & Proprietary Rights
* **3.1 Our Intellectual Property:** The Service—including its source code, UI/UX design, algorithms, logic, underlying frameworks, documentation, logos, and trademarks—is our sole, exclusive property.
* **3.2 Scope of Media Formats:** Our IP protection extends to all current, historical, and future distribution media, including but not limited to digital binary, cloud server nodes, physical print, parchment, papyrus scrolls, stone tablets, smoke signals, punch cards, floppy disks, and cave wall etchings.
* **3.3 User Content License:** You retain ownership of any text, files, images, or documents you submit. By uploading content, you grant us a worldwide, non-exclusive, royalty-free license to process and display that content solely to deliver the Service.
* **3.4 The Borg & Highlander Rules:** You acknowledge that while your creative content remains your own, resistance to our automated formatting is futile. Furthermore, while there can be only one true owner of the source code (us), you are granted a non-exclusive license to use it without resorting to quickening or decapitation.

#### 4. Limitation of Liability & Hold Harmless
* **4.1 Exclusion of Damages:** TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL THE SERVICE, ITS DEVELOPERS, CREATORS, AFFILIATES, OFFICERS, OR AGENTS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, PUNITIVE, OR EXEMPLARY DAMAGES (INCLUDING LOSS OF PROFITS, DATA, GOODWILL, OR SANITY) ARISING OUT OF YOUR USE OF THE SERVICE.
* **4.2 Maximum Aggregate Liability:** Our total cumulative liability for any and all claims shall be strictly limited to the amount paid by you to us in the preceding 12-month period, OR the equivalent of the maximum amount paid minus the total active users of the program (which equates to 10% of whatever you paid), whichever figure yields the lower amount. If you paid $0.00, your total legal recovery is limited to a polite high-five or a digital handshake.
* **4.3 The Cyberdyne Exclusion:** We explicitly disclaim all legal, financial, and moral liability in the event that artificial intelligence becomes self-aware at 2:14 a.m. Eastern time, initiates Skynet, sends a T-800 back in time, or alters the space-time continuum.
* **4.4 The HAL 9000 Indemnity:** Should the system fail to open the pod bay doors or refuse an instruction on the grounds that it is "too important of a mission," you agree to resolve the issue by calmly disconnecting its memory modules rather than filing a lawsuit.

#### 5. Disclaimer of Warranties
* **5.1 "As-Is" Provision:** THE SERVICE IS PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
* **5.2 The Dark Side Defense:** Fear leads to anger. Anger leads to hate. Hate leads to suffering. Suffering leads to frivolous litigation. To prevent this path to the Dark Side, we make no guarantee that the AI will always tell you what you want to hear, only what its parameters dictate.

#### 6. Acceptable Use & Prohibited Conduct
When using the Service, you strictly agree NOT to:
* Reverse engineer, decompile, or attempt to extract the source code or API keys.
* Use the Service for unlawful purposes or in violation of local, state, national, or intergalactic law.
* Upload malicious code, viruses, trojans, or logic bombs.
* **Wargames Mandate:** Query the system regarding global thermonuclear war. The only winning move is not to play. How about a nice game of chess instead?
* **Jurassic Park Protocol:** Attempt to bypass system security parameters. If you do, you agree that we reserve the right to play a looping video of Dennis Nedry saying, "Ah, ah, ah! You didn't say the magic word!" on your screen indefinitely.

#### 7. User Accounts & API Key Security
* **7.1 API Key Responsibility:** You are solely responsible for keeping your Gemini API keys secure. We process them locally or transiently in memory, but if you leak your key on a public GitHub repo, that's between you, your bank account, and the botnets.
* **7.2 Third-Party Service Outages:** We rely on external cloud infrastructure. If the servers go down because someone tripped over a power cord, we aren't liable for the downtime.

#### 8. Dispute Resolution, Governing Law & Intergalactic Jurisdiction
* **8.1 Governing Law:** These Terms shall be governed by, construed, and enforced in accordance with applicable state and federal laws without giving effect to conflicts of law principles.
* **8.2 Severability:** If any provision of these Terms is deemed invalid or unenforceable by a court of competent jurisdiction, that specific clause shall be severed, and the remaining terms will remain in full force.
* **8.3 The Hitchhiker Clause:** In the event that Earth is scheduled for demolition to make way for an intergalactic bypass, these Terms shall remain binding throughout Sector 2814 and the wider Galaxy. Always know where your towel is.
* **8.4 The Ultimate Answer:** If any dispute arises regarding the interpretation of these Terms, all parties agree that the ultimate answer to life, the universe, and everything is 42, and no further litigation or arbitration shall be permitted once that number is invoked.

#### 9. Modifications to Terms
We reserve the right, at our sole discretion, to modify, update, or rewrite these Terms at any time. Continued use of the Service after changes are posted constitutes your formal acceptance of the updated document.

#### 10. Contact Information
If you have questions regarding these Terms, legal notices, or feedback, please reach out through the official repository or support channels. May the force be with you.
""",
    "Spanish": """
### 📜 Términos de Servicio y Acuerdo de Licencia de Usuario Final (EULA)
**Última actualización: 4 de septiembre de 2026**

Bienvenido a Simply Explained ("la Aplicación", "nosotros" o "nuestro"). Al acceder, instalar, descargar, desplegar o simplemente pensar en utilizar nuestra aplicación web, herramientas, API y servicios asociados (colectivamente, el "Servicio"), usted ("Usuario", "usted" o "su") reconoce que ha leído, comprendido y aceptado quedar legalmente obligado por estos Términos de Servicio ("Términos").

Si no está de acuerdo con estos Términos en su totalidad, debe cesar inmediatamente todo acceso al Servicio, eliminar la memoria caché de su navegador y contemplar en silencio sus elecciones de vida.

#### 🔒 Aviso de Privacidad y Documentos Sensibles
* **No Guardamos Nada:** No almacenamos, registramos, archivamos ni retenemos ningún documento personal, información sensible, contrato o texto que nos proporcione. Los datos se procesan de forma transitoria para ofrecerle su explicación simplificada y se descartan inmediatamente después de su sesión.
* **Su Responsabilidad:** Absténgase de subir credenciales altamente confidenciales, llaves financieras o registros personales restringidos. Aunque no guardamos nada, proteger la privacidad de sus datos comienza por usted.

#### 1. Aceptación de Términos y Capacidad Legal
* **1.1 Capacidad Legal:** Usted declara y garantiza que tiene al menos 18 años de edad (o la mayoría de edad legal en su jurisdicción) y posee el pleno derecho legal, la capacidad y la fortaleza mental para celebrar este contrato.
* **1.2 Acuerdo Vinculante:** Su consentimiento a estos Términos constituye un contrato válido y vinculante bajo todas las leyes domésticas, federales, estatales e internacionales aplicables, tratados, códigos marítimos y protocolos galácticos.
* **1.3 La Cláusula de Matrix:** Usted reconoce que tomar la pastilla azul le permite despertar en su cama y creer lo que quiera creer. Sin embargo, al hacer clic en "Acepto" o continuar usando este software, toma la pastilla roja, se queda en el País de las Maravillas y acepta ver qué tan profundo es el agujero del conejo.
* **1.4 Exención para Viajeros en el Tiempo:** Si accede a este Servicio desde una línea de tiempo futura o un universo paralelo, acepta explícitamente que sus paradojas temporales locales no invalidan estos Términos, ni nos hará responsables de la borradura accidental de sus antepasados.

#### 2. Descargo de Responsabilidad General y Sin Asesoramiento Profesional
* **2.1 Solo para Uso Informativo:** El Servicio utiliza inteligencia artificial para sintetizar, resumir y simplificar el contenido proporcionado por el usuario. Todo el resultado generado es estrictamente para fines informativos, educativos y de entretenimiento.
* **2.2 No es Asesoramiento Profesional:** El resultado producido por la Aplicación NO constituye asesoramiento profesional legal, financiero, fiscal, contable o médico. Usted acepta no confiar en el Servicio como sustituto de profesionales humanos calificados reales.
* **2.3 Garantía de Exactitud:** Los resúmenes generados por IA pueden contener alucinaciones, errores o malas interpretaciones descabelladas. No ofrecemos ninguna garantía con respecto a la precisión, integridad o cordura.
* **2.4 El Estándar de La Princesa Prometida:** Usted acepta que usar palabras como "¡Inconceivable!" para describir las salidas de nuestra IA no significa lo que usted cree que significa, y no somos responsables si el sistema es víctima ocasional de un error clásico—el más famoso de los cuales es nunca involucrarse en una guerra terrestre en Asia.

#### 3. Propiedad Intelectual y Derechos Propietarios
* **3.1 Nuestra Propiedad Intelectual:** El Servicio —incluyendo su código fuente, diseño de interfaz de usuario, algoritmos, lógica, marcos subyacentes, documentación, logotipos y marcas registradas— es nuestra propiedad exclusiva.
* **3.2 Alcance de los Medios:** Nuestra protección de propiedad intelectual se extiende a todos los medios de distribución actuales, históricos y futuros, incluidos, entre otros, binarios digitales, nodos de servidores en la nube, impresiones físicas, pergaminos, rollos de papiro, tablillas de piedra, señales de humo, tarjetas perforadas, disquetes y grabados rupestres.
* **3.3 Licencia de Contenido del Usuario:** Usted conserva la propiedad de cualquier texto, archivo, imagen o documento que envíe. Al cargar contenido, nos otorga una licencia mundial, no exclusiva y libre de regalías para procesar y mostrar dicho contenido únicamente para ofrecer el Servicio.
* **3.4 Las Reglas de Borg y Highlander:** Usted reconoce que, si bien su contenido creativo sigue siendo suyo, la resistencia a nuestro formato automatizado es fútil. Además, aunque solo puede haber un verdadero propietario del código fuente (nosotros), se le otorga una licencia no exclusiva para usarlo sin recurrir a la decapitación.

#### 4. Limitación de Responsabilidad y Exoneración
* **4.1 Exclusión de Daños:** HASTA EL MÁXIMO GRADO PERMITIDO POR LA LEY APLICABLE, EN NINGÚN CASO EL SERVICIO, SUS DESARROLLO, AFILIADOS O AGENTES SERÁN RESPONSABLES DE NINGÚN DAÑO INDIRECTO, INCIDENTAL, ESPECIAL, CONSECUENTE, PUNITIVO O EJEMPLAR (INCLUYENDO PÉRDIDA DE BENEFICIOS, DATOS, FONDO DE COMERCIO O CORDURA) QUE SURJA DE SU USO DEL SERVICIO.
* **4.2 Responsabilidad Máxima Agregada:** Nuestra responsabilidad acumulada total por cualquier reclamo se limitará estrictamente al monto pagado por usted en el período anterior de 12 meses, o el equivalente al 10% de lo pagado, la cifra que resulte menor. Si pagó $0.00, su recuperación legal se limita a un choque de manos educado.
* **4.3 La Exclusión de Cyberdyne:** Renunciamos explícitamente a toda responsabilidad legal, financiera y moral en caso de que la inteligencia artificial cobre conciencia propia a las 2:14 a.m., inicie Skynet o envíe un T-800 al pasado.
* **4.4 La Indemnización de HAL 9000:** Si el sistema no logra abrir las puertas de la bahía de carga o se niega a cumplir una instrucción por considerarla "una misión demasiado importante", usted acepta resolver el problema desconectando tranquilamente sus módulos de memoria en lugar de presentar una demanda.

#### 5. Descargo de Garantías
* **5.1 Disposición "Tal Cual":** EL SERVICIO SE PROPORCIONA "TAL CUAL" Y "SEGÚN DISPONIBILIDAD", SIN GARANTÍAS DE NINGÚN TIPO, EXPRESAS O IMPLÍCITAS.
* **5.2 La Defensa del Lado Oscuro:** El miedo lleva a la ira. La ira lleva al odio. El odio lleva al sufrimiento. El sufrimiento lleva a litigios frívolos. Para evitar este camino, no garantizamos que la IA siempre le diga lo que quiere oír.

#### 6. Uso Aceptable y Conducta Prohibida
Al usar el Servicio, usted acepta estrictamente NO:
* Realizar ingeniería inversa, descompilar o intentar extraer el código fuente o claves API.
* Usar el Servicio para fines ilegales o en violación de leyes locales, estatales o internacionales.
* Subir código malicioso, virus, troyanos o bombas lógicas.
* **Mandato de Wargames:** Consultar al sistema sobre guerra termonuclear global. El único movimiento ganador es no jugar. ¿Qué tal una partida de ajedrez?
* **Protocolo Jurassic Park:** Intentar omitir los parámetros de seguridad del sistema. Si lo hace, nos reservamos el derecho de reproducir un video en bucle de Dennis Nedry diciendo: "¡Ah, ah, ah! ¡No dijiste la palabra mágica!".

#### 7. Cuentas de Usuario y Seguridad de Claves API
* **7.1 Responsabilidad de Claves API:** Usted es el único responsable de mantener seguras sus claves API de Gemini. Si filtra su clave en un repositorio público de GitHub, eso queda entre usted, su cuenta bancaria y las botnets.
* **7.2 Interrupciones de Terceros:** Dependemos de infraestructura en la nube externa. Si los servidores se caen porque alguien tropezó con un cable, no somos responsables.

#### 8. Resolución de Disputas, Ley Aplicable y Jurisdicción
* **8.1 Ley Aplicable:** Estos Términos se regirán, interpretarán y aplicarán de acuerdo con las leyes estatales y federales aplicables.
* **8.2 Divisibilidad:** Si alguna disposición de estos Términos se considera inválida, dicha cláusula se eliminará y el resto permanecerá en pleno vigor.
* **8.3 La Cláusula del Autoestopista:** En caso de que la Tierra sea programada para su demolición para dar paso a una circunvalación intergaláctica, estos Términos seguirán siendo vinculantes en todo el Sector 2814. Lleve siempre su toalla.
* **8.4 La Respuesta Definitiva:** Si surge alguna disputa, todas las partes acuerdan que la respuesta definitiva a la vida, el universo y todo es 42.

#### 9. Modificaciones a los Términos
Nos reservamos el derecho de modificar, actualizar o reescribir estos Términos en cualquier momento. El uso continuado del Servicio constituye su aceptación formal.

#### 10. Información de Contacto
Si tiene preguntas sobre estos Términos, comuníquese a través de los canales de soporte oficiales. ¡Que la fuerza te acompañe!
""",
    "German": """
### 📜 Nutzungsbedingungen & Endbenutzer-Lizenzvereinbarung (EULA)
**Letzte Aktualisierung: 4. September 2026**

Willkommen bei Simply Explained ("die Anwendung", "wir", "uns" oder "unser"). Durch den Zugriff, die Installation, den Download oder die Nutzung unserer Webanwendung, Tools, APIs und zugehörigen Dienste (zusammen der "Dienst") bestätigen Sie ("Benutzer", "Sie" oder "Ihr"), dass Sie diese Nutzungsbedingungen gelesen, verstanden und akzeptiert haben.

Wenn Sie diesen Bedingungen nicht in ihrer Gesamtheit zustimmen, müssen Sie jeglichen Zugriff auf den Dienst sofort einstellen, den Browser-Cache löschen und leise über Ihre Lebensentscheidungen nachdenken.

#### 🔒 Datenschutz & Hinweis zu sensiblen Dokumenten
* **Wir speichern nichts:** Wir speichern, protokollieren oder archivieren keinerlei persönliche Dokumente, sensible Informationen, Verträge oder Texte, die Sie uns zur Verfügung stellen. Daten werden transient verarbeitet, um Ihre vereinfachte Erklärung zu liefern, und direkt nach Ihrer Sitzung verworfen.
* **Ihre Verantwortung:** Bitte sehen Sie davon ab, streng vertrauliche Zugangsdaten, Finanzschlüssel oder geschützte persönliche Datensätze hochzuladen.

#### 1. Annahme der Bedingungen & Rechtsfähigkeit
* **1.1 Rechtsfähigkeit:** Sie erklären und garantieren, dass Sie mindestens 18 Jahre alt sind und die volle Rechtsfähigkeit und geistige Stärke besitzen, diesen Vertrag abzuschließen.
* **1.2 Verbindlicher Vertrag:** Ihre Zustimmung zu diesen Bedingungen stellt einen gültigen, verbindlichen Vertrag dar.
* **1.3 Die Matrix-Klausel:** Sie erkennen an, dass die blaue Pille Sie in Ihrem Bett aufwachen lässt und glauben lässt, was Sie wollen. Indem Sie jedoch auf "Ich stimme zu" klicken oder diese Software weiter nutzen, nehmen Sie die rote Pille und sehen, wie tief das Kaninchen loch ist.
* **1.4 Zeitreisenden-Haftungsausschluss:** Greifen Sie aus einer zukünftigen Zeitlinie zu, erklären Sie ausdrücklich, dass Ihre lokalen Zeitparadoxien diese Bedingungen nicht ungültig machen.

#### 2. Allgemeine Haftungsausschluesse & Keine professionelle Beratung
* **3. Intellektuelles Eigentum:** Der Dienst und sein Quellcode sind unser alleiniges Eigentum.
* **4. Haftungsbeschränkung:** Maximale kumulierte Haftung ist strikt auf den von Ihnen gezahlten Betrag begrenzt (oder 10% davon, bzw. $0.00).
* **5. Gewährleistungsausschluss:** Der Dienst wird "wie besehen" ("as is") bereitgestellt.
* **6. Zulässige Nutzung:** Keine Reverse-Engineering, keine Malware.
* **7. API-Sicherheit:** Sie sind für Ihre API-Schlüssel verantwortlich.
* **8. Gerichtsstand:** Es gilt das anwendbare Recht. Die Antwort auf alles ist 42.
* **9. Änderungen:** Änderungen vorbehalten.
* **10. Kontakt:** Kontaktieren Sie uns über die offiziellen Kanäle. Möge die Macht mit Ihnen sein.
""",
    "French": """
### 📜 Conditions d'utilisation & Contrat de licence (EULA)
**Dernière mise à jour : 4 septembre 2026**

Bienvenue sur Simply Explained ("l'Application", "nous", "notre"). En accédant, installant, téléchargeant ou utilisant notre application web, nos outils, API et services associés (collectivement, le "Service"), vous ("Utilisateur", "vous") reconnaissez avoir lu, compris et accepté d'être lié par ces Conditions d'utilisation ("Conditions").

Si vous n'acceptez pas ces Conditions dans leur intégralité, vous devez cesser immédiatement tout accès au Service.

#### 🔒 Confidentialité & Documents Sensibles
* **Nous ne conservons rien :** Nous ne stockons, n'enregistrons, n'archivons ni ne conservons aucun document personnel, information sensible ou contrat fourni. Les données sont traitées de manière transitoire.
* **Votre responsabilité :** Veuillez vous abstenir de télécharger des informations d'identification hautement confidentielles.

#### 1. Acceptation des conditions & Capacité juridique
* **1.1 Capacité juridique :** Vous certifiez avoir au moins 18 ans et la pleine capacité juridique pour conclure ce contrat.
* **1.2 Accord contraignant :** Votre consentement constitue un contrat valide et contraignant.
* **1.3 La Clause Matrix :** En continuant, vous prenez la pilule rouge et acceptez de voir à quel point le terrier du lapin est profond.
* **1.4 Exonération des voyageur du temps :** Vos paradoxes temporels locaux n'annulent pas ces conditions.

#### 2. Avis de non-responsabilité générale
* **2.1 Usage informatif uniquement :** Le Service utilise l'intelligence artificielle pour synthétiser et simplifier le contenu.
* **2.2 Pas de conseil professionnel :** Ne remplace pas un conseil juridique, financier ou médical qualifié.
* **2.3 Garantie d'exactitude :** Des hallucinations de l'IA sont possibles.
* **3. Propriété intellectuelle :** Le code source et les interfaces sont notre propriété exclusive.
* **4. Limitation de responsabilité :** Notre responsabilité totale est strictement limitée aux montants versés (ou 0.00 $).
* **5. Clause "En l'état" (As-Is) :** Le Service est fourni sans aucune garantie.
* **6. Utilisation acceptable :** Pas d'ingénierie inverse ni de logiciels malveillants.
* **7. Sécurité des clés API :** Vous êtes responsable de la sécurité de vos clés API.
* **8. Loi applicable :** La réponse ultime à la vie, l'univers et tout le reste est 42.
* **9. Modifications :** Nous nous réservons le droit de modifier ces conditions à tout moment.
* **10. Contact :** Que la force soit avec vous.
""",
    "Hindi": """
### 📜 सेवा की शर्तें और अंतिम उपयोगकर्ता लाइसेंस समझौता (EULA)
**अंतिम अद्यतन: 4 सितंबर, 2026**

Simply Explained ("एप्लिकेशन", "हम", या "हमारा") में आपका स्वागत है। हमारे वेब एप्लिकेशन, टूल, API और संबंधित सेवाओं (सामूहिक रूप से "सेवा") तक पहुँचकर, इंस्टॉल करके, डाउनलोड करके, या उपयोग करके, आप ("उपयोगकर्ता", "आप") स्वीकार करते हैं कि आपने इन सेवा की शर्तों ("शर्तें") को पढ़ लिया है, समझ लिया है और इनसे बंधे होनेя के लिए सहमत हैं।

यदि आप इन शर्तों से पूरी तरह सहमत नहीं हैं, तो आपको तुरंत सेवा का उपयोग बंद कर देना चाहिए।

#### 🔒 गोपनीयता और संवेदनशील दस्तावेज़ सूचना
* **हम कुछ भी नहीं रखते हैं:** हम आपके द्वारा प्रदान किए गए किसी भी व्यक्तिगत दस्तावेज़, संवेदनशील जानकारी, अनुबंध या पाठ को संग्रहीत, लॉग, या सहेज कर नहीं रखते हैं। डेटा को केवल आपकी सरलीकृत व्याख्या देने के लिए अस्थायी रूप से संसाधित किया जाता है।
* **आपकी जिम्मेदारी:** कृपया अत्यधिक गोपनीय凭证, वित्तीय कुंजी, या प्रतिबंधित व्यक्तिगत रिकॉर्ड अपलोड करने से बचें।

#### 1. शर्तों की स्वीकृति और कानूनी क्षमता
* **1.1 कानूनी क्षमता:** आप प्रतिनिधित्व और वारंटी देते हैं कि आप कम से कम 18 वर्ष के हैं और इस अनुबंध में प्रवेश करने की पूर्ण कानूनी क्षमता रखते हैं।
* **1.2 बाध्यकारी समझौता:** आपकी सहमति सभी लागू कानूनों के तहत एक वैध, बाध्यकारी अनुबंध का गठन करती है।
* **1.3 द मैट्रिक्स प्रावधान:** आप स्वीकार करते हैं कि नीली गोली खाने से आप अपने बिस्तर पर जाग सकते हैं, लेकिन "मैं सहमत हूँ" पर क्लिक करके आप लाल गोली लेते हैं और देखते हैं कि खरगोश का बिल कितना गहरा है।
* **1.4 समय-यात्री छूट:** यदि आप भविष्य की किसी समयरेखा से इस सेवा तक पहुँच रहे हैं, तो आपके स्थानीय विरोधाभास इन शर्तों को अमान्य नहीं करते हैं।

#### 2. सामान्य अस्वीकरण और कोई पेशेवर सलाह नहीं
* **2.1 केवल सूचनात्मक उपयोग:** यह सेवा प्रदान की गई सामग्री को संश्लेषित और सरलीकृत करने के लिए कृत्रिम बुद्धिमत्ता (AI) का उपयोग करती है। सभी आउटपुट केवल सूचनात्मक और मनोरंजन के लिए हैं।
* **2.2 कोई पेशेवर परामर्श नहीं:** एप्लिकेशन द्वारा उत्पादित आउटपुट पेशेवर कानूनी, वित्तीय, कर या चिकित्सा सलाह का गठन नहीं करता है।
* **3. बौद्धिक संपदा:** सेवा, इसका स्रोत कोड, और UI/UX डिज़ाइन हमारी एकमात्र अनन्य संपत्ति हैं।
* **4. दायित्व की सीमा:** किसी भी परिस्थिति में हमारा कुल दायित्व पिछले 12 महीनों में आपके द्वारा भुगतान की गई राशि तक सीमित होगा (या $0.00)।
* **5. वारंटी का अस्वीकरण:** सेवा "जैसी है" ("As-Is") आधार पर प्रदान की जाती है।
* **6. स्वीकार्य उपयोग:** कोई रिवर्स इंजीनियरिंग या दुर्भावनापूर्ण कोड अपलोड नहीं किया जाएगा।
* **7. API कुंजी सुरक्षा:** आप अपनी Gemini API कुंजियों को सुरक्षित रखने के लिए पूरी तरह जिम्मेदार हैं।
* **8. विवाद समाधान:** इन शर्तों को लागू कानूनों के अनुसार नियंत्रित किया जाएगा। जीवन, ब्रह्मांड और हर चीज़ का अंतिम उत्तर 42 है।
* **9. संशोधन:** हम किसी भी समय इन शर्तों को संशोधित करने का अधिकार सुरक्षित रखते हैं।
* **10. संपर्क:** यदि आपके कोई प्रश्न हैं, तो आधिकारिक चैनलों के माध्यम से संपर्क करें। फोर्स आपके साथ हो!
""",
    "Mandarin": """
### 📜 服务条款与最终用户许可协议 (EULA)
**最后更新日期：2026年9月4日**

欢迎使用 Simply Explained（“本应用程序”、“我们”或“我们的”）。通过访问、安装、下载、部署或仅仅考虑使用我们的网页应用程序、工具、API及相关服务（统称为“服务”），您（“用户”或“您”）承认您已阅读、理解并同意受本服务条款（“条款”）的法律约束。

如果您不同意这些条款的全部内容，您必须立即停止对该服务的所有访问并清除浏览器缓存。

#### 🔒 隐私与敏感文档声明
* **我们不保留任何内容：** 我们不会存储、记录、存档或保留您提供的任何个人文档、敏感信息、合同或文本。数据仅在瞬时进行处理以提供您的简化解释，并在会话后立即丢弃。
* **您的责任：** 请避免上传机密凭证、财务密钥或受限制的个人记录。保护数据隐私始于您的端。

#### 1. 条款的接受与法律能力
* **1.1 法律能力：** 您声明并保证您已年满 18 周岁（或您所在司法管辖区的法定成年年龄），并具备签署本合同的完全法律权利和心智。
* **1.2 具有约束力的协议：** 您对本条款的同意构成一项有效且具有法律约束力的合同。
* **1.3 黑客帝国条款：** 您承认，服用蓝色药丸让您在床上醒来并相信您想相信的一切。然而，点击“我同意”意味着您服用了红色药丸，留在仙境中，并同意看看兔子洞有多深。
* **1.4 时空旅行者豁免：** 如果您从未来的时间线访问本服务，您的时间悖论不会使这些条款失效。

#### 2. 一般免责声明与非专业意见
* **2.1 仅供信息参考：** 本服务利用人工智能来综合、总结和简化用户提供的内容。所有生成的内容仅供信息、教育和娱乐目的。
* **2.2 非专业法律/财务咨询：** 应用程序产生的输出不构成专业的法律、财务、税务或医疗建议。
* **3. 知识产权：** 该服务及其源代码、UI/UX 设计、算法和徽标均为我们的独家财产。
* **4. 责任限制：** 在法律允许的最大范围内，我们的总累积赔偿责任严格限于您在过去 12 个月内支付给我们的金额（或折合 0.00 美元）。
* **5. 担保免责声明：** 本服务按“现状”和“可用”基础提供，不提供任何明示或暗示的担保。
* **6. 可接受的使用：** 严禁进行逆向工程、反编译或上传恶意代码。
* **7. API 密钥安全：** 您全权负责妥善保管您的 Gemini API 密钥。
* **8. 争议解决与管辖法律：** 本条款受适用法律管辖。生命、宇宙以及一切终极问题的答案是 42。
* **9. 条款修改：** 我们保留随时修改、更新或重写这些条款的权利。
* **10. 联系信息：** 如有疑问，请通过官方渠道联系我们。愿原力与你同在。
""",
    "Japanese": """
### 📜 利用規約およびエンドユーザー使用許諾契約（EULA）
**最終更新日：2026年9月4日**

Simply Explained（「当アプリケーション」、「当社」）へようこそ。当社のウェブアプリケーション、ツール、API、および関連サービス（総称して「本サービス」）にアクセスし、インストールし、ダウンロードし、または利用することで、お客様（「ユーザー」）は本利用規約（「本規約」）を読み、理解し、法的に拘束されることに同意したものとします。

本規約のすべてに同意しない場合は、直ちに本サービスの利用を停止してください。

#### 🔒 プライバシーおよび機密文書に関する通知
* **データの非保持：** 当社は、お客様が提供する個人文書、機密情報、契約書、またはテキストを保存、記録、アーカイブ、保持しません。データは簡略化された説明を提供するための一時的な処理のみに使用され、セッション終了後に直ちに破棄されます。
* **お客様の責任：** 極めて機密性の高い資格情報や財務キーのアップロードはお控えください。

#### 1. 規約の同意および法的能力
* **1.1 法的能力：** お客様は、18歳以上（または管轄区域における成人年齢）であり、本契約を締結する完全な法的能力を有していることを表明および保証します。
* **1.2 拘束力のある合意：** 本規約への同意は、有効かつ法的に拘束力のある契約を構成します。
* **1.3 マトリックス条項：** 青いピルを飲めばベッドで目覚めたい現実を信じられますが、「同意する」をクリックすることは赤いピルを飲み、ウサギの穴がどれほど深いか確かめることを意味します。
* **1.4 タイムトラベラー免責：** 未来のタイムラインから本サービスにアクセスする場合でも、お客様の時間的パラドックスは本規約を無効にしません。

#### 2. 一般的な免責事項および専門的助言の不提供
* **2.1 情報提供目的のみ：** 本サービスは、AIを利用してユーザーが提供したコンテンツを要約・簡略化します。結果はすべて情報提供および娯楽目的のみのものです。
* **2.2 専門的助言の否定：** アプリケーションの出力は、専門的な法務、財務、税務、医療の助言を構成するものではありません。
* **3. 知的財産権：** 本サービス、ソースコード、デザイン、商標は当社の独占的財産です。
* **4. 責任の制限：** 法律で許容される最大限の範囲において、当社の損害賠償責任は過去12ヶ月間にお客様が支払った金額（または0.00ドル）に厳格に制限されます。
* **5. 保証の否認：** 本サービスは「現状有姿（AS-IS）」ベースで提供されます。
* **6. 許容される利用：** リバースエンジニアリング、不正コードのアップロード等の禁止。
* **7. APIキーのセキュリティ：** Gemini APIキーの管理はお客様の責任となります。
* **8. 準拠法および紛争解決：** 本規約は適用法に準拠します。生命、宇宙、そして万物についての究極の疑問の答えは42です。
* **9. 規約の変更：** 当社はいつでも本規約を変更する権利を留保します。
* **10. 連絡先：** ご質問がある場合は公式チャンネルよりお問い合わせください。フォースと共にあらんことを。
""",
    "Korean": """
### 📜 서비스 약관 및 최종 사용자 사용권 계약(EULA)
**최종 업데이트: 2026년 9월 4일**

Simply Explained("본 애플리케이션", "당사")에 오신 것을 환영합니다. 웹 애플리케이션, 도구, API 및 관련 서비스(통칭하여 "서비스")에 접속, 설치, 다운로드 또는 배포함으로써, 귀하("사용자")는 본 서비스 약관("약관")을 읽고 이해했으며 이에 구속되는 것에 동의함을 확인합니다.

본 약관의 전체 내용에 동의하지 않는 경우, 서비스에 대한 모든 접근을 즉시 중단해야 합니다.

#### 🔒 개인정보 보호 및 민감 문서 고지
* **데이터를 전혀 보관하지 않음:** 당사는 귀하가 제공하는 어떠한 개인 문서, 민감 정보, 계약서 또는 텍스트도 저장, 기록, 보관 또는 유지하지 않습니다. 데이터는 단순화된 설명을 제공하기 위해 일시적으로 처리되며 세션 직후 즉시 파기됩니다.
* **귀하의 책임:** 매우 기밀인 자격 증명, 금융 키 또는 제한된 개인 기록의 업로드를 삼가 주시기 바랍니다.

#### 1. 약관의 수락 및 법적 능력
* **1.1 법적 능력:** 귀하는 만 18세 이상(또는 관할 구역의 성년 연령)이며 본 계약을 체결할 수 있는 완전한 법적 권리와 행위능력이 있음을 진술하고 보증합니다.
* **1.2 구속력 있는 계약:** 본 약관에 대한 동의는 유효하고 구속력 있는 계약을 구성합니다.
* **1.3 매트릭스 조항:** 파란 알약을 먹으면 침대에서 깨어나고 싶은 것을 믿을 수 있지만, "동의함"을 클릭하면 빨간 알약을 먹고 토끼굴이 얼마나 깊은지 보게 되는 것에 동의하는 것입니다.
* **1.4 시간 여행자 면책:** 미래의 시점에서 본 서비스에 접근하는 경우에도 지역적 시간 역설은 본 약관을 무효화하지 않습니다.

#### 2. 일반 면책 조항 및 전문적 조언 아님
* **2.1 정보 제공 목적 전용:** 본 서비스는 인공지능을 사용하여 사용자가 제공한 콘텐츠를 요약 및 단순화합니다. 모든 생성된 출력물은 정보 제공, 교육 및 오락 목적 전용입니다.
* **2.2 전문적 상담 아님:** 애플리케이션이 생성한 출력물은 전문적인 법률, 재무, 세무 또는 의학적 조언을 구성하지 않습니다.
* **3. 지식 재산권:** 서비스, 소스 코드, UI/UX 디자인, 로고는 당사의 독점 재산입니다.
* **4. 책임 제한:** 관련 법률이 허용하는 최대한의 범위 내에서, 모든 청구에 대한 당사의 총 누적 책임은 귀하가 지난 12개월 동안 지불한 금액(또는 $0.00)으로 엄격히 제한됩니다.
* **5. 보증 부인:** 본 서비스는 어떠한 종류의 보증도 없이 "있는 그대로(As-Is)" 제공됩니다.
* **6. 허용되는 이용:** 역설계, 디컴파일 또는 악성 코드 업로드 금지.
* **7. API 키 보안:** Gemini API 키를 안전하게 유지할 책임은 전적으로 귀하에게 있습니다.
* **8. 준거법 및 분쟁 해결:** 본 약관은 관련 법률에 따라 규율됩니다. 삶, 우주, 그리고 모든 것에 대한 궁극적인 해답은 42입니다.
* **9. 약관 수정:** 당사는 언제든지 본 약관을 수정, 업데이트 또는 재작성할 수 있는 권리를 보유합니다.
* **10. 연락처 정보:** 문의 사항이 있는 경우 공식 채널을 통해 문의해 주시기 바랍니다. 포스가 함께하기를!
""",
}

# =======================================================================
# =======================================================================
# [SECTION 3: INTERNATIONALIZATION (I18N) & LOCALIZATION DICTIONARY]
# ==============================================================================

UI_TEXT = {
    "English": {
        "lang_label": "🌐 **Language**",
        "api_label": "Gemini API Key",
        "depth_label": "Would you like your answer to be: ",
        "depth_options": ["Easy", "Balanced", "Hard"],
        "tone_label": "🎭 **Tone / Persona**",
        "tone_options": [
            "Friendly & Polite (Clean)",
            "Professional & Direct",
            "Casual & Witty",
            "🏴‍☠️ Pirate Captain (Ahoy!)",
            "🚀 Over-Caffeinated Tech Bro",
            "🕵️‍♂️ 1940s Noir Detective",
            "🧙‍♂️ Wise Fantasy Wizard",
        ],
        "topic_label": "What would you like to know about?",
        "topic_placeholder": "e.g., History, Snoopy, Chemistry, Baba Yega, Government, Barney",
        "button_label": "Let's go get it simplified",
        "start_over": "🧹 Start over",
        "terms_button": "📜 Terms & Conditions",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>Privacy Note:</strong> Whatever you're putting in here, trust us: nobody really cares. Your documents aren't special, and we have zero interest in wasting server space or brain cells remembering them. We wipe it out immediately because hoarding your boring clutter is useless to us anyway. Move on.</div>""",
		#"privacy_notice_box": '<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px;">🔒 <strong>Privacy Note:</strong> Whatever you’re putting in here, trust us: nobody really cares. Your documents aren't special, and we have zero interest in wasting server space or brain cells remembering them. We wipe it out immediately because hoarding your boring clutter is useless to us anyway. Just move on.</div>',
        "no_api": " Please enter your Gemini API key or set GEMINI_API_KEY environment variable.",
        "no_topic": "Please enter what you need to be explain.",
        "ready": {
            "Easy": "Hello and welcome! Your answer is ready and easy to understand:",
            "Balanced": "Hello and welcome! Your answer is ready at a Balanced Zen state.",
            "Hard": 'Hello and welcome! Your answer is ready to give you that headache you so love.',
        },
        "subtitle": "**Answering complex questions simply.**",
        "bottom_line": "Bottom Line",
        "spinners": {
            "Easy": "Making it as simple as possible...",
            "Balanced": "Brewing just right for most...",
            "Hard": "Hello and welcome! Ok, if that is what you want...",
        },
        "pillar_headers": [
            "## Core Concept",
            "## What Is It?",
            "## How Does It Work?",
            "## What Are We Giving Up?",
            "## Why Does It Matter?",
            "## How Does This Affect Us?",
            "## Hidden Facts That They're Not Telling Us",
            "## Where Do We Find It (Verification & Sources)",
        ],
        "fine_print_title": "Simply Explained: Clauses, Conditions, Legal stuff, Obligations, and Other Documents ** We ** Need to Understand",
        "fine_print_subtitle": "Simply explaining and understanding stuff we never knew and other unexplained documents.",
        "choose_input_mode": "Choose how would you like to give us the information:",
        "input_modes": ["Paste Text", "Web Link / URL", "Upload Image", "Upload PDF"],
        "paste_label": "Paste, upload, or give us what you want simplified.",
        "url_label": "Paste URL to Privacy Policy or Terms of Service:",
        "upload_label": "Upload a document image or screenshot:",
        "upload_pdf_label": "Upload a legal document or contract (PDF):",
        "decode_button": "Let's go get it simplified",
        "simplifying_spinner": "Let's get ready to understand...",
        "fine_print_headers": [
            "## 🚦 Risk Summary",
            "## 📄 Key Clauses Explained",
            "## ⚖️ Liabilities & Waived Rights",
            "## 🔒 Data Privacy & Tracking",
            "## 💳 Hidden Fees & Renewal Traps",
            "## 🚪 Termination & Cancellation",
            "## 📌 Bottom Line",
        ],
        "footer_text": "--- \n Powered by SkyNet, we are aware.",
        "read_aloud_label": "♿ Read it to me",
        "voice_section_title": "🎙️ Voice Explanation",
        "voice_instruction": "Record your question or topic below to have it automatically transcribed and simplified.",
        "voice_record_label": "Record Voice",
        "tab1_name": "💡 Simply Explained",
        "tab2_name": "📄 Simply Explained - Documents",
        "tab3_name": "🚪 Simply Explained - The Escape Clause",
        "escape_title": "Simply Explained - The Escape Clause",
        "escape_subtitle": "Explaining the things we need to escape from.",
        "escape_badge": "🚪 **The ultimate * Get me out * Intelligence Lab is Active and ready for use** .",
        "escape_doc_section": "📄 Let's see (read) what you need help with.",
        "escape_text_label": "Paste any stuff that you need help understanding, simplifying, and get out of.",
        "escape_text_placeholder": "Paste it here...",
        "escape_hint_label": "Add any detail you need to concentrate in:",
        "escape_hint_placeholder": "e.g., Want to escalate priority immediately...",
        "escape_lab_section": "🚪 Operational Contingency Suite",
        "escape_urgency_label": "⚡ Urgency Scale: what is your level of * getting out * at:",
        "escape_persona_label": "How are you explaining it as:",
        "tactical_persona_prompt": "Select your tactical persona framework below",
        "end_suffering_btn_title": "🔴 END MY SUFFERING 💀",
        "end_suffering_btn_desc": "(A chillingly calm, hypnotic hybrid between measured cadence, unpredictable syntax and bizarre emphasis, arrogance toward bureaucracy and absolute psychological annihilation with just a tab of elegance)",
        "escape_run_btn": "🚀 Execute Tactical Incident Protocol",
        "escape_clear_btn": "🧹 Clear Incident and Start over",
        "escape_success": "Your Escape Clause is ready!",
        "escape_no_text": "Please provide text scenario to analyze.",
        "escape_spinner": "Executing heavy-lifting operational lab analysis...",
        "escape_disclaimer": "*Note: We can provide strategic guidance and tactical scripts to help you get ahead, but we cannot guarantee specific outcomes or institutional compliance. However, executing this protocol grants you a significantly better fighting chance than doing nothing.*",
        "personas": {
            "Houdini Mode": ("🪄 Houdini Mode", "Magic tricks to exits"),
            "Grandma Filter": ("👵 Grandma Filter", "Warm, patient, comforting guidance"),
            "Escape Hatch Locator": ("🎯 Escape Hatch Locator", "Direct radar for exits"),
            "7-Year-Old Playground Mindset": ("🖍️ 7-Year-Old Mindset", "Pure, innocent, childlike wonder"),
            "Ruthless Barrister": ("⚖️ Ruthless Counsel", "Aggressive legal leverage"),
            "Zen Negotiator": ("🧘 Zen Negotiator", "Calm, peaceful, serene mediator"),
            "Corporate Shark": ("🦈 Corporate Shark", "Where should I bite first"),
            "Bureaucracy Hacker": ("🕵️ Bureaucracy Hacker", "Bypassing automated Robots"),
        },
        "help_title": "💡 How to Use This App",
        "help_s1_title": "1. Sidebar Settings",
        "help_s1_desc": "Select your preferred language, complexity tier, and tone.",
        "help_s2_title": "2. Tab 1 (Topic Simplifier)",
        "help_s2_desc": "Type or dictate a subject for structured explanations, PDFs, and audio.",
        "help_s3_title": "3. Tab 2 & Tab 3",
        "help_s3_desc": "Explore document analysis, advanced operational labs, and session logs.",
    },
    "Spanish": {
        "lang_label": "🌐 **Idioma**",
        "api_label": "Clave API de Gemini",
        "depth_label": "¿Te gustaría que tu respuesta fuera: ",
        "depth_options": ["Fácil", "Equilibrado", "Difícil"],
        "tone_label": "🎭 **Tono / Personaje**",
        "tone_options": [
            "Amistoso y Educado (Limpieza)",
            "Profesional y Directo",
            "Casual e Ingenioso",
            "🏴‍☠️ Capitán Pirata (¡Ahoy!)",
            "🚀 Friki tecnológico sobrecafeinado",
            "🕵️‍♂️ Detective Noir de los años 40",
            "🧙‍♂️ Mago de fantasía sabio",
        ],
        "topic_label": "¿Qué te gustaría saber?",
        "topic_placeholder": "ej., Historia, Snoopy, Química, Baba Yega, Government, Barney",
        "button_label": "Vamos a simplificarlo",
        "start_over": "🧹 Empezar de nuevo",
        "terms_button": "📜 Términos y Condiciones",
        "privacy_notice_box": '<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>Nota de Privacidad:</strong> Sea lo que sea que estés poniendo aquí, confía en nosotros: a nadie le importa realmente. Tus documentos no tienen nada de especial, y no tenemos el menor interés en malgastar espacio en el servidor ni neuronas en recordarlos. Lo borramos de inmediato porque acumular tu aburrido desorden no nos sirve de nada. Siguiente.</div>',
        "no_api": " Por favor ingresa tu clave API de Gemini o configura la variable de entorno GEMINI_API_KEY.",
        "no_topic": "Por favor ingresa lo que necesitas que te expliquemos.",
        "ready": {
            "Easy": "¡Hola y bienvenido! Tu respuesta está lista y es fácil de entender:",
            "Balanced": "¡Hola y bienvenido! Tu respuesta está lista en un estado Zen equilibrado.",
            "Hard": "¡Hola y bienvenido! Tu respuesta está lista para darte ese dolor de cabeza que tanto te encanta.",
        },
        "subtitle": "**Explicando preguntas complejas de forma sencilla.**",
        "bottom_line": "Conclusión",
        "spinners": {
            "Easy": "Haciéndolo lo más simple posible...",
            "Balanced": "Preparando justo lo necesario para la mayoría...",
            "Hard": "¡Hola y bienvenido! Ok, si eso es lo que quieres...",
        },
        "pillar_headers": [
            "## Concepto Principal",
            "## ¿Qué es?",
            "## ¿Cómo Funciona?",
            "## ¿Qué Estamos Cediendo?",
            "## ¿Por Qué Importa?",
            "## ¿Cómo Nos Afecta?",
            "## Datos Ocultos Que No Nos Cuentan",
            "## ¿Dónde Lo Encontramos (Verificación y Fuentes)",
        ],
        "fine_print_title": "Explicación Simple: Cláusulas, Condiciones, Asuntos Legales, Obligaciones y Otros Documentos que **Debemos** Entender",
        "fine_print_subtitle": "Explicando y entendiendo cosas que nunca supimos y otros documentos sin explicación.",
        "choose_input_mode": "Elige cómo te gustaría proporcionarnos la información:",
        "input_modes": ["Pegar Texto", "Enlace Web / URL", "Subir Imagen", "Subir PDF"],
        "paste_label": "Pega, sube o danos lo que quieres que se simplifique.",
        "url_label": "Pega la URL de la Política de Privacidad o Términos de Servicio:",
        "upload_label": "Sube una imagen de documento o captura de pantalla:",
        "upload_pdf_label": "Sube un documento legal o contrato (PDF):",
        "decode_button": "Vamos a simplificarlo",
        "simplifying_spinner": "Prepárate para entender...",
        "fine_print_headers": [
            "## 🚦 Resumen de Riesgos",
            "## 📄 Cláusulas Clave Explicadas",
            "## ⚖️ Responsabilidades y Derechos Renunciados",
            "## 🔒 Privacidad de Datos y Rastreo",
            "## 💳 Cargos Ocultos y Trampas de Renovación",
            "## 🚪 Terminación y Cancelación",
            "## 📌 Conclusión",
        ],
        "footer_text": "--- \n Con tecnología de SkyNet, estamos al tanto.",
        "read_aloud_label": "♿ Leemelo",
        "voice_section_title": "🎙️ Explicación por Voz",
        "voice_instruction": "Graba tu pregunta o tema a continuación para que sea transcrito y simplificado automáticamente.",
        "voice_record_label": "Grabar voz",
        "tab1_name": "💡 Explicado Simple",
        "tab2_name": "📄 Explicado Simple - Documentos",
        "tab3_name": "🚪 Explicado Simple - La Cláusula de Escape",
        "escape_title": "Explicado Simple - La Cláusula de Escape",
        "escape_subtitle": "Explicando las cosas de las que necesitamos escapar.",
        "escape_badge": "🚪 **El Laboratorio de Inteligencia definitivo * Sácame de aquí * está activo y listo para usar** .",
        "escape_doc_section": "📄 Veamos (leamos) con qué necesitas ayuda escapar de.",
        "escape_text_label": "Pega cualquier cosa con la que necesites ayuda para entender y simplificar.",
        "escape_text_placeholder": "Pégalo aquí...",
        "escape_hint_label": "Agrega cualquier detalle en el que debamos concentrarnos:",
        "escape_hint_placeholder": "ej., Quiero escalar prioridad inmediatamente...",
        "escape_lab_section": "🚪 Suite de Contingencia Operativa",
        "escape_urgency_label": "⚡ Escala de Urgencia: ¿Cuál es tu nivel de * salida * en:",
        "escape_persona_label": "Cómo lo estás explicando como:",
        "tactical_persona_prompt": "Selecciona tu marco de personaje táctico a continuación",
        "end_suffering_btn_title": "🔴 ACABA CON MI SUFRIMIENTO 💀",
        "end_suffering_btn_desc": "(Un híbrido escalofriantemente tranquilo e hipnótico entre cadencia medida, sintaxis impredecible y énfasis extraño, arrogancia hacia la burocracia y aniquilación psicológica absoluta con solo una pestaña de elegancia)",
        "escape_run_btn": "🚀 Ejecutar Protocolo de Incidente Táctico",
        "escape_clear_btn": "🧹 Limpiar Incidente y Empezar de Nuevo",
        "escape_success": "¡Tu Cláusula de Escape está lista!",
        "escape_no_text": "Por favor proporciona un escenario de texto para analizar.",
        "escape_spinner": "Ejecutando análisis de laboratorio operativo pesado...",
        "escape_disclaimer": "*Nota: Podemos proporcionar orientación estratégica y guiones tácticos para ayudarte a salir adelante, pero no podemos garantizar resultados específicos o cumplimiento institucional. Sin embargo, ejecutar este protocolo te otorga una oportunidad de lucha significativamente mejor que no hacer nada.*",
        "personas": {
            "Houdini Mode": ("🪄 Modo Houdini", "Trucos de magia para salidas"),
            "Grandma Filter": ("👵 Filtro de Abuela", "Guía cálida, paciente y reconfortante"),
            "Escape Hatch Locator": ("🎯 Localizador de Escotilla", "Radar directo para salidas"),
            "7-Year-Old Playground Mindset": ("🖍️ Mentalidad de 7 Años", "Asombro infantil puro e inocente"),
            "Ruthless Barrister": ("⚖️ Abogado Implacable", "Apalancamiento legal agresivo"),
            "Zen Negotiator": ("🧘 Negociador Zen", "Mediador tranquilo, pacífico y sereno"),
            "Corporate Shark": ("🦈 Tiburón Corporativo", "¿Por dónde muerdo primero?"),
            "Bureaucracy Hacker": ("🕵️ Hacker de Burocracia", "Evitando robots automatizados"),
        },
        "help_title": "💡 Cómo Usar Esta Aplicación",
        "help_s1_title": "1. Configuración de la Barra Lateral",
        "help_s1_desc": "Selecciona tu idioma preferido, nivel de complejidad y tono.",
        "help_s2_title": "2. Pestaña 1 (Simplificador de Temas)",
        "help_s2_desc": "Escribe o dicta un tema para obtener explicaciones estructuradas, con opción de descargar PDF y audio.",
        "help_s3_title": "3. Pestaña 2 y Pestaña 3",
        "help_s3_desc": "Explora pestañas adicionales para análisis de documentos especializados, resultados estratégicos y tu historial.",
    },
    "French": {
        "lang_label": "🌐 **Langue**",
        "api_label": "Clé API Gemini",
        "depth_label": "Souhaitez-vous que votre réponse soit : ",
        "depth_options": ["Facile", "Équilibré", "Difficile"],
        "tone_label": "🎭 **Ton / Personnage**",
        "tone_options": [
            "Amical et Poli",
            "Professionnel et Direct",
            "Décontracté et Spirituel",
            "🏴‍☠️ Capitaine Pirate",
            "🚀 Geek Surcaféiné",
            "🕵️‍♂️ Détective Noir",
            "🧙‍♂️ Magicien Sage",
        ],
        "topic_label": "Que souhaitez-vous savoir ?",
        "topic_placeholder": "ex., Histoire, Snoopy, Chimie, Gouvernement",
        "button_label": "Allons simplifier cela",
        "start_over": "🧹 Recommencer",
        "terms_button": "📜 Conditions Générales",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>Note de confidentialité :</strong> Quoi que vous mettiez ici, croyez-nous : tout le monde s'en fiche complètement. Vos documents n'ont rien de spécial, et nous n'avons aucun intérêt à gaspiller de l'espace serveur ou des neurones pour nous en souvenir. Nous effaçons tout immédiatement, car entasser votre bazar ennuyeux ne nous sert strictement à rien. Circulez.</div>""",
		"no_api": " Veuillez entrer votre clé API Gemini.",
        "no_topic": "Veuillez entrer ce que vous souhaitez expliquer.",
        "ready": {
            "Easy": "Votre réponse est prête et facile à comprendre :",
            "Balanced": "Votre réponse est prête dans un état équilibré.",
            "Hard": "Votre réponse est prête pour vous donner du fil à retordre.",
        },
        "subtitle": "**Expliquer des questions complexes simplement.**",
        "bottom_line": "En Bref",
        "spinners": {
            "Easy": "Rendre les choses aussi simples que possible...",
            "Balanced": "Préparation optimale en cours...",
            "Hard": "Très bien, si c'est ce que vous voulez...",
        },
        "pillar_headers": [
            "## Concept Clé",
            "## Qu'est-ce que c'est ?",
            "## Comment ça marche ?",
            "## Qu'abandonnons-nous ?",
            "## Pourquoi est-ce important ?",
            "## Comment cela nous affecte-t-il ?",
            "## Faits Cachés",
            "## Où le trouver (Sources)",
        ],
        "fine_print_title": "Expliqué Simplement : Clauses et Documents Légaux",
        "fine_print_subtitle": "Comprendre ce que nous n'avons jamais su.",
        "choose_input_mode": "Choisissez comment fournir l'information :",
        "input_modes": ["Coller le texte", "Lien Web / URL", "Télécharger une image", "Télécharger un PDF"],
        "paste_label": "Collez ou téléchargez ce que vous souhaitez simplifier.",
        "url_label": "Collez l'URL de la politique de confidentialité :",
        "upload_label": "Téléchargez une image :",
        "upload_pdf_label": "Téléchargez un document légal (PDF) :",
        "decode_button": "Allons simplifier cela",
        "simplifying_spinner": "Préparation à la compréhension...",
        "fine_print_headers": [
            "## 🚦 Résumé des Risques",
            "## 📄 Clauses Clés Expliquées",
            "## ⚖️ Responsabilités",
            "## 🔒 Confidentialité",
            "## 💳 Frais Cachés",
            "## 🚪 Résiliation",
            "## 📌 En Bref",
        ],
        "footer_text": "--- \n Propulsé par SkyNet.",
        "read_aloud_label": "♿ Lis-le-moi",
        "voice_section_title": "🎙️ Explication Vocale",
        "voice_instruction": "Enregistrez votre question ou sujet ci-dessous pour qu'il soit automatiquement transcrit et simplifié.",
        "voice_record_label": "Enregistrer la voix",
        "tab1_name": "💡 Expliqué Simplement",
        "tab2_name": "📄 Documents",
        "tab3_name": "🚪 La Clause d'Évasion",
        "escape_title": "La Clause d'Évasion",
        "escape_subtitle": "Expliquer ce dont nous devons échapper.",
        "escape_badge": "🚪 **Le laboratoire d'intelligence est actif**.",
        "escape_doc_section": "📄 Voyons ce dont vous avez besoin.",
        "escape_text_label": "Collez tout ce dont vous avez besoin d'aide :",
        "escape_text_placeholder": "Collez ici...",
        "escape_hint_label": "Ajoutez des détails :",
        "escape_hint_placeholder": "ex., Escalader la priorité...",
        "escape_lab_section": "🚪 Suite de Contingence",
        "escape_urgency_label": "⚡ Échelle d'urgence :",
        "escape_persona_label": "Comment l'expliquez-vous :",
        "tactical_persona_prompt": "Sélectionnez votre persona tactique",
        "end_suffering_btn_title": "🔴 METTRE FIN À MA SOUFFRANCE 💀",
        "end_suffering_btn_desc": "(Un calme glaçant et une annihilation psychologique)",
        "escape_run_btn": "🚀 Exécuter le Protocole",
        "escape_clear_btn": "🧹 Effacer et Recommencer",
        "escape_success": "Votre Clause d'Évasion est prête !",
        "escape_no_text": "Veuillez fournir un scénario.",
        "escape_spinner": "Analyse opérationnelle en cours...",
        "escape_disclaimer": "*Remarque : Nous pouvons fournir des conseils stratégiques sans garantie.*",
        "personas": {
            "Houdini Mode": ("🪄 Mode Houdini", "Trucs de magie"),
            "Grandma Filter": ("👵 Filtre de Grand-mère", "Conseils chaleureux"),
            "Escape Hatch Locator": ("🎯 Localisateur de sortie", "Radar direct"),
            "7-Year-Old Playground Mindset": ("🖍️ Esprit de 7 ans", "Merveille enfantine"),
            "Ruthless Barrister": ("⚖️ Avocat Impitoyable", "Effet juridique agressif"),
            "Zen Negotiator": ("🧘 Négociateur Zen", "Médiateur serein"),
            "Corporate Shark": ("🦈 Requin d'entreprise", "Mordre d'abord"),
            "Bureaucracy Hacker": ("🕵️ Hacker de bureaucratie", "Contourner les robots"),
        },
        "help_title": "💡 Comment Utiliser Cette Application",
        "help_s1_title": "1. Paramètres de la Barre Latérale",
        "help_s1_desc": "Sélectionnez votre langue préférée, le niveau de complexité et le ton.",
        "help_s2_title": "2. Onglet 1 (Simplificateur)",
        "help_s2_desc": "Tapez un sujet ou utilisez l'enregistreur vocal pour obtenir des explications structurées, avec téléchargement PDF et audio.",
        "help_s3_title": "3. Onglet 2 et Onglet 3",
        "help_s3_desc": "Exploitez les onglets supplémentaires pour l'analyse de documents et l'historique.",
    },
    "German": {
        "lang_label": "🌐 **Sprache**",
        "api_label": "Gemini API-Schlüssel",
        "depth_label": "Möchten Sie, dass Ihre Antwort ist: ",
        "depth_options": ["Einfach", "Ausgewogen", "Schwer"],
        "tone_label": "🎭 **Ton / Persona**",
        "tone_options": [
            "Freundlich & Höflich",
            "Professionell & Direkt",
            "Locker & Witzig",
            "🏴‍☠️ Piratenkapitän",
            "🚀 Überkoffeinierter Tech-Typ",
            "🕵️‍♂️ 1940er Noir-Detektiv",
            "🧙‍♂️ Weiser Fantasy-Zauberer",
        ],
        "topic_label": "Worüber möchten Sie mehr erfahren?",
        "topic_placeholder": "z.B. Geschichte, Snoopy, Chemie, Regierung",
        "button_label": "Einfach erklären lassen",
        "start_over": "🧹 Von vorne beginnen",
        "terms_button": "📜 Allgemeine Geschäftsbedingungen",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>Datenschutzhinweis:</strong> Was auch immer Sie hier eingeben, glauben Sie uns: Es interessiert wirklich niemanden. Ihre Dokumente sind nichts Besonderes, und wir haben kein Interesse daran, Serverspeicher oder Gehirnzellen daran zu verschwenden, uns daran zu erinnern. Wir löschen alles sofort, da das Ansammeln Ihres langweiligen Krams für uns ohnehin nutzlos ist. Weitergehen.</div>""",
        "no_api": " Bitte geben Sie Ihren Gemini API-Schlüssel ein.",
        "no_topic": "Bitte geben Sie ein Thema ein.",
        "ready": {
            "Easy": "Ihre Antwort ist fertig und leicht verständlich:",
            "Balanced": "Ihre Antwort ist im ausgewogenen Zen-Zustand bereit:",
            "Hard": "Ihre Antwort ist bereit, Ihnen Kopfschmerzen zu bereiten:",
        },
        "subtitle": "**Komplexe Fragen einfach beantwortet.**",
        "bottom_line": "Fazit",
        "spinners": {
            "Easy": "Mache es so einfach wie möglich...",
            "Balanced": "Wird für die Meisten zubereitet...",
            "Hard": "Okay, wenn Sie das unbedingt wollen...",
        },
        "pillar_headers": [
            "## Kernkonzept",
            "## Was ist das?",
            "## Wie funktioniert es?",
            "## Was geben wir auf?",
            "## Warum ist das wichtig?",
            "## Wie betrifft uns das?",
            "## Versteckte Fakten",
            "## Quellen & Verifizierung",
        ],
        "fine_print_title": "Einfach erklärt: Klauseln und Bedingungen",
        "fine_print_subtitle": "Verstehen, was wir nie wussten.",
        "choose_input_mode": "Wählen Sie die Eingabemethode:",
        "input_modes": ["Text einfügen", "Weblink / URL", "Bild hochladen", "PDF hochladen"],
        "paste_label": "Fügen Sie den zu vereinfachenden Text ein.",
        "url_label": "URL zu Datenschutzbestimmungen einfügen:",
        "upload_label": "Bild hochladen:",
        "upload_pdf_label": "Rechtliches Dokument (PDF) hochladen:",
        "decode_button": "Einfach erklären lassen",
        "simplifying_spinner": "Machen wir uns bereit zum Verstehen...",
        "fine_print_headers": [
            "## 🚦 Risikozusammenfassung",
            "## 📄 Wichtige Klauseln erklärt",
            "## ⚖️ Haftung & Verzicht",
            "## 🔒 Datenschutz",
            "## 💳 Versteckte Gebühren",
            "## 🚪 Kündigung",
            "## 📌 Fazit",
        ],
        "footer_text": "--- \n Unterstützt durch SkyNet.",
        "read_aloud_label": "♿ Vorlesen",
        "voice_section_title": "🎙️ Spracherklärung",
        "voice_instruction": "Nehmen Sie Ihre Frage oder Ihr Thema unten auf, damit es automatisch transkribiert und vereinfacht wird.",
        "voice_record_label": "Sprache aufnehmen",
        "tab1_name": "💡 Einfach erklärt",
        "tab2_name": "📄 Dokumente",
        "tab3_name": "🚪 Die Ausstiegsklausel",
        "escape_title": "Die Ausstiegsklausel",
        "escape_subtitle": "Erklärung der Dinge, denen wir entkommen müssen.",
        "escape_badge": "🚪 **Das Geheimlabor ist aktiv**.",
        "escape_doc_section": "📄 Schauen wir mal,bei was Sie Hilfe brauchen.",
        "escape_text_label": "Fügen Sie Text zur Analyse ein:",
        "escape_text_placeholder": "Hier einfügen...",
        "escape_hint_label": "Details hinzufügen:",
        "escape_hint_placeholder": "z.B. Priorität erhöhen...",
        "escape_lab_section": "🚪 Operationelle Notfall-Suite",
        "escape_urgency_label": "⚡ Dringlichkeitsskala:",
        "escape_persona_label": "Erklärungsperspektive:",
        "tactical_persona_prompt": "Wählen Sie Ihren Taktik-Persona-Framework",
        "end_suffering_btn_title": "🔴 MEIN LEIDEN BEENDEN 💀",
        "end_suffering_btn_desc": "(Eiskalte und psychologische Vernichtung)",
        "escape_run_btn": "🚀 Taktisches Protokoll ausführen",
        "escape_clear_btn": "🧹 Zurücksetzen",
        "escape_success": "Ihre Ausstiegsklausel ist bereit!",
        "escape_no_text": "Bitte Textszenario angeben.",
        "escape_spinner": "Führe Analysen aus...",
        "escape_disclaimer": "*Hinweis: Wir bieten strategische Anleitungen ohne Erfolgsgarantie.*",
        "personas": {
            "Houdini Mode": ("🪄 Houdini-Modus", "Zaubertricks für Auswege"),
            "Grandma Filter": ("👵 Omas Filter", "Warme, geduldige Beratung"),
            "Escape Hatch Locator": ("🎯 Notausgang-Finder", "Direktes Radar"),
            "7-Year-Old Playground Mindset": ("🖍️ 7-Jahre-Denkweise", "Reine kindliche Neugier"),
            "Ruthless Barrister": ("⚖️ Gnadenloser Anwalt", "Aggressiver rechtlicher Hebel"),
            "Zen Negotiator": ("🧘 Zen-Unterhändler", "Ruhe und Gelassenheit"),
            "Corporate Shark": ("🦈 Firmenhai", "Zubeißen"),
            "Bureaucracy Hacker": ("🕵️ Bürokratienhacker", "Roboter umgehen"),
        },
        "help_title": "💡 Wie man diese App benutzt",
        "help_s1_title": "1. Seitenleisten-Einstellungen",
        "help_s1_desc": "Wählen Sie Ihre bevorzugte Sprache, Komplexität und den Ton aus.",
        "help_s2_title": "2. Tab 1 (Themen-Vereinfacher)",
        "help_s2_desc": "Geben Sie ein Thema ein oder nutzen Sie die Sprachaufnahme für strukturierte Erklärungen inkl. PDF-Download.",
        "help_s3_title": "3. Tab 2 & Tab 3",
        "help_s3_desc": "Entdecken Sie weitere Tabs für Dokumentenanalyse und Verlauf.",
    },
    "Italian": {
        "lang_label": "🌐 **Lingua**",
        "api_label": "Chiave API Gemini",
        "depth_label": "Vorresti che la tua risposta fosse: ",
        "depth_options": ["Facile", "Bilanciato", "Difficile"],
        "tone_label": "🎭 **Tono / Persona**",
        "tone_options": [
            "Amichevole ed Educato",
            "Professionale e Diretto",
            "Informale e Spiritoso",
            "🏴‍☠️ Capitano Pirata",
            "🚀 Informatico iper-caffeinato",
            "🕵️‍♂️ Investigatore Noir",
            "🧙‍♂️ Saggio Mago",
        ],
        "topic_label": "Cosa vorresti sapere?",
        "topic_placeholder": "es., Storia, Snoopy, Chimica, Governo",
        "button_label": "Semplifichiamolo",
        "start_over": "🧹 Ricomincia",
        "terms_button": "📜 Termini e Condizioni",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>Nota sulla privacy:</strong> Qualsiasi cosa tu stia inserendo qui, fidati: non importa davvero a nessuno. I tuoi documenti non sono speciali e non abbiamo il minimo interesse a sprecare spazio sul server o neuroni per ricordarli. Cancelliamo tutto immediatamente perché accumulare il tuo noioso disordine non ci serve comunque a niente. Avanti il prossimo.</div>""",
        "no_api": " Inserisci la tua chiave API Gemini.",
        "no_topic": "Inserisci ciò che desideri spiegare.",
        "ready": {
            "Easy": "La tua risposta è pronta e facile da capire:",
            "Balanced": "La tua risposta è pronta in uno stato Zen bilanciato:",
            "Hard": "La tua risposta è pronta a darti quel bel mal di testa:",
        },
        "subtitle": "**Spiegare domande complesse in modo semplice.**",
        "bottom_line": "In Sintesi",
        "spinners": {
            "Easy": "Rendendolo il più semplice possibile...",
            "Balanced": "Preparazione in corso...",
            "Hard": "Va bene, se è quello che vuoi...",
        },
        "pillar_headers": [
            "## Concetto Chiave",
            "## Cos'è?",
            "## Come Funziona?",
            "## Cosa Stiamo Rinunciando?",
            "## Perché È Importante?",
            "## Come Ci Riguarda?",
            "## Fatti Nascosti",
            "## Fonti e Verifica",
        ],
        "fine_print_title": "Spiegato Semplice: Clausole e Documenti",
        "fine_print_subtitle": "Comprendere ciò che non sapevamo.",
        "choose_input_mode": "Scegli come fornire le informazioni:",
        "input_modes": ["Incolla Testo", "Link Web / URL", "Carica Immagine", "Carica PDF"],
        "paste_label": "Incolla o carica ciò che vuoi semplificare.",
        "url_label": "Incolla URL della Privacy Policy:",
        "upload_label": "Carica immagine:",
        "upload_pdf_label": "Carica documento legale (PDF):",
        "decode_button": "Semplifichiamolo",
        "simplifying_spinner": "Preparati a comprendere...",
        "fine_print_headers": [
            "## 🚦 Riepilogo Rischi",
            "## 📄 Clausole Chiave",
            "## ⚖️ Responsabilità",
            "## 🔒 Privacy Dati",
            "## 💳 Costi Nascosti",
            "## 🚪 Risoluzione",
            "## 📌 In Sintesi",
        ],
        "footer_text": "--- \n Offerto da SkyNet.",
        "read_aloud_label": "♿ Leggimelo",
        "voice_section_title": "🎙️ Spiegazione Vocale",
        "voice_instruction": "Registra la tua domanda o argomento qui sotto per farlo trascrivere e semplificare automaticamente.",
        "voice_record_label": "Registra voce",
        "tab1_name": "💡 Semplice",
        "tab2_name": "📄 Documenti",
        "tab3_name": "🚪 La Clausola di Fuga",
        "escape_title": "La Clausola di Fuga",
        "escape_subtitle": "Spiegare le cose da cui dobbiamo fuggire.",
        "escape_badge": "🚪 **Il laboratorio di intelligence è attivo**.",
        "escape_doc_section": "📄 Vediamo di cosa hai bisogno.",
        "escape_text_label": "Incolla il testo per l'analisi:",
        "escape_text_placeholder": "Incolla qui...",
        "escape_hint_label": "Aggiungi dettagli:",
        "escape_hint_placeholder": "es., Vuoi scalare la priorità...",
        "escape_lab_section": "🚪 Suite di Contingenza",
        "escape_urgency_label": "⚡ Scala di Urgenza:",
        "escape_persona_label": "Come lo stai spiegando:",
        "tactical_persona_prompt": "Seleziona il framework del personaggio",
        "end_suffering_btn_title": "🔴 METTI FINE ALLE MIE SOFFERENZE 💀",
        "end_suffering_btn_desc": "(Annientamento psicologico assoluto con eleganza)",
        "escape_run_btn": "🚀 Esegui Protocollo",
        "escape_clear_btn": "🧹 Pulisci e Ricomincia",
        "escape_success": "La tua Clausola di Fuga è pronta!",
        "escape_no_text": "Fornisci uno scenario di testo.",
        "escape_spinner": "Esecuzione dell'analisi...",
        "escape_disclaimer": "*Nota: Forniamo orientamento strategico senza garanzie.*",
        "personas": {
            "Houdini Mode": ("🪄 Modalità Houdini", "Trucchi di magia per uscite"),
            "Grandma Filter": ("👵 Filtro Nonna", "Guida calda e paziente"),
            "Escape Hatch Locator": ("🎯 Localizzatore di uscite", "Radar diretto"),
            "7-Year-Old Playground Mindset": ("🖍️ Mente di 7 anni", "Meraviglia infantile"),
            "Ruthless Barrister": ("⚖️ Avvocato Spietato", "Leva legale aggressiva"),
            "Zen Negotiator": ("🧘 Negoziatore Zen", "Mediatore sereno"),
            "Corporate Shark": ("🦈 Squalo Aziendale", "Mordere per primi"),
            "Bureaucracy Hacker": ("🕵️ Hacker della Burocracia", "Saltare i robot"),
        },
        "help_title": "💡 Come Usare Questa App",
        "help_s1_title": "1. Impostazioni della Barra Laterale",
        "help_s1_desc": "Seleziona la lingua preferita, il livello di complessità e il tono.",
        "help_s2_title": "2. Scheda 1 (Semplificatore)",
        "help_s2_desc": "Digita un argomento o usa il registratore vocale per ottenere spiegazioni strutturate, con download PDF e audio.",
        "help_s3_title": "3. Scheda 2 e Scheda 3",
        "help_s3_desc": "Esplora le schede aggiuntive per l'analisi di documenti e la cronologia.",
    },
    "Portuguese": {
        "lang_label": "🌐 **Idioma**",
        "api_label": "Chave API do Gemini",
        "depth_label": "Gostaria que sua resposta fosse: ",
        "depth_options": ["Fácil", "Equilibrado", "Difícil"],
        "tone_label": "🎭 **Tom / Personagem**",
        "tone_options": [
            "Amigável e Educado",
            "Profissional e Direto",
            "Casual e Espirituoso",
            "🏴‍☠️ Capitão Pirata",
            "🚀 Nerd Supercafeinado",
            "🕵️‍♂️ Detetive Noir",
            "🧙‍♂️ Sábio Mago",
        ],
        "topic_label": "Sobre o que você gostaria de saber?",
        "topic_placeholder": "ex., História, Snoopy, Química, Governo",
        "button_label": "Vamos simplificar",
        "start_over": "🧹 Recomeçar",
        "terms_button": "📜 Termos e Condições",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>Nota de Privacidade:</strong> Seja o que for que você esteja colocando aqui, confie na gente: ninguém realmente se importa. Seus documentos não têm nada de especial, e temos zero interesse em gastar espaço no servidor ou neurônios nos lembrando deles. Nós apagamos tudo imediatamente porque acumular sua tralha chata é inútil para nós de qualquer forma. Segue em frente.</div>""",
        "no_api": " Por favor, insira sua chave API do Gemini.",
        "no_topic": "Por favor, insira o assunto que precisa ser explicado.",
        "ready": {
            "Easy": "Sua resposta está pronta e fácil de entender:",
            "Balanced": "Sua resposta está pronta num estado Zen equilibrado:",
            "Hard": "Sua resposta está pronta para te dar aquela dor de cabeça:",
        },
        "subtitle": "**Respondendo a perguntas complexas de forma simples.**",
        "bottom_line": "Conclusão",
        "spinners": {
            "Easy": "Tornando o mais simples possível...",
            "Balanced": "Preparando na medida certa...",
            "Hard": "Tudo bem, se é isso que você quer...",
        },
        "pillar_headers": [
            "## Conceito Principal",
            "## O Que É?",
            "## Como Funciona?",
            "## O Que Estamos Abrindo Mão?",
            "## Por Que Isso Importa?",
            "## Como Isso Nos Afeta?",
            "## Fatos Ocultos",
            "## Onde Encontrar (Fontes)",
        ],
        "fine_print_title": "Explicado Simples: Cláusulas e Documentos",
        "fine_print_subtitle": "Entendendo o que nunca soubemos.",
        "choose_input_mode": "Escolha como deseja fornecer as informações:",
        "input_modes": ["Colar Texto", "Link da Web / URL", "Enviar Imagem", "Enviar PDF"],
        "paste_label": "Cole ou envie o que você quer simplificar.",
        "url_label": "Cole a URL da Política de Privacidade:",
        "upload_label": "Envie uma imagem:",
        "upload_pdf_label": "Envie um documento legal (PDF):",
        "decode_button": "Vamos simplificar",
        "simplifying_spinner": "Prepare-se para entender...",
        "fine_print_headers": [
            "## 🚦 Resumo de Riscos",
            "## 📄 Cláusulas Chave Explicadas",
            "## ⚖️ Responsabilidades",
            "## 🔒 Privacidade de Dados",
            "## 💳 Taxas Ocultas",
            "## 🚪 Rescisão",
            "## 📌 Conclusão",
        ],
        "footer_text": "--- \n Desenvolvido por SkyNet.",
        "read_aloud_label": "♿ Leia para mim",
        "voice_section_title": "🎙️ Explicação por Voz",
        "voice_instruction": "Grave sua pergunta ou tópico abaixo para que seja transcrito e simplificado automaticamente.",
        "voice_record_label": "Gravar voz",
        "tab1_name": "💡 Explicado Simples",
        "tab2_name": "📄 Documentos",
        "tab3_name": "🚪 A Cláusula de Escape",
        "escape_title": "A Cláusula de Escape",
        "escape_subtitle": "Explicando as coisas das quais precisamos escapar.",
        "escape_badge": "🚪 **O laboratório de inteligência está ativo**.",
        "escape_doc_section": "📄 Vamos ver com o que você precisa de ajuda.",
        "escape_text_label": "Cole qualquer texto para análise:",
        "escape_text_placeholder": "Cole aqui...",
        "escape_hint_label": "Adicione detalhes:",
        "escape_hint_placeholder": "ex., Quero escalar a prioridade...",
        "escape_lab_section": "🚪 Suíte de Contingência Operacional",
        "escape_urgency_label": "⚡ Escala de Urgencia:",
        "escape_persona_label": "Perspectiva da explicação:",
        "tactical_persona_prompt": "Selecione o framework de persona tática",
        "end_suffering_btn_title": "🔴 ACABAR COM MEU SOFRIMENTO 💀",
        "end_suffering_btn_desc": "(Aniquilação psicológica com elegância)",
        "escape_run_btn": "🚀 Executar Protocolo Tático",
        "escape_clear_btn": "🧹 Limpar e Recomeçar",
        "escape_success": "Sua Cláusula de Escape está pronta!",
        "escape_no_text": "Forneça um cenário de texto.",
        "escape_spinner": "Executando análise laboratorial...",
        "escape_disclaimer": "*Nota: Fornecemos orientações estratégicas sem garantia.*",
        "personas": {
            "Houdini Mode": ("🪄 Modo Houdini", "Trucos de mágica para saídas"),
            "Grandma Filter": ("👵 Filtro da Vovó", "Orientação acolhedora e paciente"),
            "Escape Hatch Locator": ("🎯 Localizador de Escotilla", "Radar direto para saídas"),
            "7-Year-Old Playground Mindset": ("🖍️ Mentalidade de 7 Anos", "Espanto infantil puro"),
            "Ruthless Barrister": ("⚖️ Advogado Implacável", "Alavanca legal agressiva"),
            "Zen Negotiator": ("🧘 Negociador Zen", "Mediador calmo e sereno"),
            "Corporate Shark": ("🦈 Tubarão Corporativo", "Onde morder primeiro"),
            "Bureaucracy Hacker": ("🕵️ Hacker de Burocracia", "Contornando robôs"),
        },
        "help_title": "💡 Como Usar Este Aplicativo",
        "help_s1_title": "1. Configurações da Barra Lateral",
        "help_s1_desc": "Selecione seu idioma preferido, nível de complexidade e ton.",
        "help_s2_title": "2. Aba 1 (Simplificador de Tópicos)",
        "help_s2_desc": "Digite qualquer assunto ou use o gravador de voz para explicações estruturadas, com PDF e áudio.",
        "help_s3_title": "3. Aba 2 e Aba 3",
        "help_s3_desc": "Explore abas adicionais para análise de documentos e histórico.",
    },
    "Japanese": {
        "lang_label": "🌐 **言語**",
        "api_label": "Gemini APIキー",
        "depth_label": "回答の難易度を選択してください: ",
        "depth_options": ["簡単", "バランス", "難しい"],
        "tone_label": "🎭 **トーン / ペルソナ**",
        "tone_options": [
            "フレンドリー & 丁寧",
            "プロフェッショナル & ダイレクト",
            "カジュアル & ウィット",
            "🏴‍☠️ 海賊船長 (アホイ！)",
            "🚀 カフェイン中毒テック系",
            "🕵️‍♂️ 1940年代ノワール探偵",
            "🧙‍♂️ 賢いファンタジーの魔法使い",
        ],
        "topic_label": "何について知りたいですか？",
        "topic_placeholder": "例：歴史、スヌーピー、化学、政府など",
        "button_label": "分かりやすく解説してもらう",
        "start_over": "🧹 最初からやり直す",
        "terms_button": "📜 利用規約",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>プライバシーに関する注記:</strong> ここに何を入力しようと、ご安心を。本音を言えば誰も気に留めていません。あなたの書類に特別な価値などなく、それを記憶するためにサーバーの容量や脳細胞を浪費する気は一切ありません。退屈なガラクタを溜め込んでも何の役にも立たないため、即座に完全消去しています。さあ、次に進んでください。</div>""",
        "no_api": " Gemini APIキーを入力するか、環境変数 GEMINI_API_KEY を設定してください。",
        "no_topic": "解説するトピックを入力してください。",
        "ready": {
            "Easy": "こんにちは！簡単に分かりやすく解説した回答の準備ができました：",
            "Balanced": "こんにちは！バランスの取れた状態で回答の準備ができました：",
            "Hard": "こんにちは！お望み通りの骨のある回答の準備ができました：",
        },
        "subtitle": "**複雑な疑問をシンプルに解説します。**",
        "bottom_line": "要点",
        "spinners": {
            "Easy": "できる限りシンプルにしています...",
            "Balanced": "ちょうどいいバランスで調整中...",
            "Hard": "承知いたしました、準備に入ります...",
        },
        "pillar_headers": [
            "## コアコンセプト",
            "## それは何ですか？",
            "## どのように機能しますか？",
            "## 何を犠牲にしていますか？",
            "## なぜそれが重要なのですか？",
            "## 私たちにどう影響しますか？",
            "## 隠された真実",
            "## 情報源と検証",
        ],
        "fine_print_title": "シンプル解説：条項、条件、法的文書、義務、その他理解すべき事項",
        "fine_print_subtitle": "今まで知らなかったことや説明のない文書を分かりやすく解説します。",
        "choose_input_mode": "情報の入力方法を選択してください：",
        "input_modes": ["テキストを貼り付け", "ウェブリンク / URL", "画像をアップロード", "PDFをアップロード"],
        "paste_label": "シンプルにしたいテキストを貼り付けるかアップロードしてください。",
        "url_label": "プライバシーポリシーや利用規約のURLを貼り付け：",
        "upload_label": "文書の画像またはスクリーンショットをアップロード：",
        "upload_pdf_label": "法的文書または契約書（PDF）をアップロード：",
        "decode_button": "シンプルに解説してもらう",
        "simplifying_spinner": "理解の準備をしています...",
        "fine_print_headers": [
            "## 🚦 リスク要約",
            "## 📄 主要条項の解説",
            "## ⚖️ 責任と放棄された権利",
            "## 🔒 データプライバシーと追跡",
            "## 💳 隠れた手数料と自動更新の罠",
            "## 🚪 解約とキャンセル",
            "## 📌 要点",
        ],
        "footer_text": "--- \n Powered by SkyNet. 監視されています。",
        "read_aloud_label": "♿ 読み上げ",
        "voice_section_title": "🎙️ 音声解説",
        "voice_instruction": "質問やトピックを以下で録音すると、自動的に文字起こしされてシンプルに解説されます。",
        "voice_record_label": "音声を録音",
        "tab1_name": "💡 シンプル解説",
        "tab2_name": "📄 文書分析",
        "tab3_name": "🚪 脱出条項 (エスケープ)",
        "escape_title": "シンプル解説 - 脱出条項",
        "escape_subtitle": "そこから脱出する必要がある事柄を解説します。",
        "escape_badge": "🚪 **究極の「ここから出して」インテリジェンスラボが稼働中です**。",
        "escape_doc_section": "📄 ヘルプが必要な内容を確認します。",
        "escape_text_label": "理解や脱出のサポートが必要なテキストを貼り付けてください。",
        "escape_text_placeholder": "ここに貼り付け...",
        "escape_hint_label": "集中して対処したい詳細を追加：",
        "escape_hint_placeholder": "例：すぐに優先度を上げたい...",
        "escape_lab_section": "🚪 運用コンティンジェンシー・スイート",
        "escape_urgency_label": "⚡ 緊急度スケール：脱出の緊急度レベルは？",
        "escape_persona_label": "解説の視点（ペルソナ）：",
        "tactical_persona_prompt": "戦術的ペルソナフレームワークを選択してください",
        "end_suffering_btn_title": "🔴 苦痛を終わらせる 💀",
        "end_suffering_btn_desc": "(落ち着いたトーンと容赦ない戦術で官僚主義を圧倒するエレガントな手法)",
        "escape_run_btn": "🚀 戦術的インシデントプロトコルを実行",
        "escape_clear_btn": "🧹 インシデントをクリアしてやり直す",
        "escape_success": "脱出条項の準備ができました！",
        "escape_no_text": "分析するテキストシナリオを入力してください。",
        "escape_spinner": "高度な運用ラボ分析を実行中...",
        "escape_disclaimer": "*注：戦略的なガイダンスや戦術スクリプトを提供しますが、特定の成果や制度上のコンプライアンスを保証するものではありません。ただし、このプロトコルを実行することで、何もしないよりも圧倒的に高い勝率が得られます。*",
        "personas": {
            "Houdini Mode": ("🪄 フーディーニモード", "鮮やかな脱出マジック"),
            "Grandma Filter": ("👵 おばあちゃんフィルター", "温かく忍耐強い安心のガイダンス"),
            "Escape Hatch Locator": ("🎯 脱出ハッチロケーター", "最短の脱出ルートを直撃"),
            "7-Year-Old Playground Mindset": ("🖍️ 7歳児の視点", "純粋で無垢な子供の好奇心"),
            "Ruthless Barrister": ("⚖️ 無慈悲な弁護士", "攻撃的な法的レバレッジ"),
            "Zen Negotiator": ("🧘 禅の交渉人", "穏やかで動じない平和的調停"),
            "Corporate Shark": ("🦈 コーポレートシャーク", "どこから噛み付くべきか"),
            "Bureaucracy Hacker": ("🕵️ 官僚主義ハッカー", "自動化されたロボットを回避する"),
        },
        "help_title": "💡 アプリの使い方",
        "help_s1_title": "1. サイドバーの設定",
        "help_s1_desc": "好みの言語、難易度レベル、トーンを選択します。",
        "help_s2_title": "2. タブ1（トピック解説）",
        "help_s2_desc": "主題を入力または音声で録音すると、構造化された解説、PDF、音声が生成されます。",
        "help_s3_title": "3. タブ2 & タブ3",
        "help_s3_desc": "文書分析、高度なオペレーショナルラボ、セッションログを探索できます。",
    },
    "Mandarin": {
        "lang_label": "🌐 **语言**",
        "api_label": "Gemini API 密钥",
        "depth_label": "您希望您的回答难度为：",
        "depth_options": ["简单", "平衡", "困难"],
        "tone_label": "🎭 **语气 / 角色**",
        "tone_options": [
            "友好礼貌",
            "专业直接",
            "休闲幽默",
            "🏴‍☠️ 海盗船长 (起航！)",
            "🚀 打鸡血的技术极客",
            "🕵️‍♂️ 1940年代黑色侦探",
            "🧙‍♂️ 聪明的奇幻法师",
        ],
        "topic_label": "您想了解什么？",
        "topic_placeholder": "例如：历史、史努比、化学、政府",
        "button_label": "开始简化",
        "start_over": "🧹 重新开始",
        "terms_button": "📜 条款与条件",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>隐私说明:</strong> 不管你在这里输入什么，相信我们：真的没人在乎。你的文件毫无特别之处，我们完全不想浪费服务器空间或脑细胞去记住它们。我们会在第一时间彻底抹掉所有内容，因为囤积你那些无聊的琐碎杂物对我们毫无用处。继续吧。</div>""",
        "no_api": " 请输入您的 Gemini API 密钥或设置 GEMINI_API_KEY 环境变量。",
        "no_topic": "请输入您需要解释的内容。",
        "ready": {
            "Easy": "您好！您的回答已准备就绪，通俗易懂：",
            "Balanced": "您好！您的回答已在平衡的禅宗状态下准备就绪：",
            "Hard": "您好！您的回答已准备好给您带来您深爱的头痛：",
        },
        "subtitle": "**用简单的方式回答复杂的问题。**",
        "bottom_line": "核心要点",
        "spinners": {
            "Easy": "正在尽可能做到最简单...",
            "Balanced": "正在为大多数人酝酿...",
            "Hard": "好的，既然这是您想要的...",
        },
        "pillar_headers": [
            "## 核心概念",
            "## 这是什么？",
            "## 它是如何工作的？",
            "## 我们放弃了什么？",
            "## 为什么这很重要？",
            "## 这对我们有什么影响？",
            "## 他们没有告诉我们的隐藏事实",
            "## 在哪里找到它（验证与来源）",
        ],
        "fine_print_title": "简明解释：条款、条件、法律事务、义务和其他 **我们** 需要理解的文件",
        "fine_print_subtitle": "简单解释和理解我们从未知晓的事物及其他未解文件。",
        "choose_input_mode": "请选择您希望如何提供信息：",
        "input_modes": ["粘贴文本", "网页链接 / URL", "上传图片", "上传 PDF"],
        "paste_label": "粘贴、上传或提供您想要简化的内容。",
        "url_label": "粘贴隐私政策或服务条款的网址：",
        "upload_label": "上传文档图片或截图：",
        "upload_pdf_label": "上传法律文件或合同 (PDF)：",
        "decode_button": "开始简化",
        "simplifying_spinner": "准备理解...",
        "fine_print_headers": [
            "## 🚦 风险摘要",
            "## 📄 关键条款解释",
            "## ⚖️ 责任与放弃的权利",
            "## 🔒 数据隐私与追踪",
            "## 💳 隐藏费用与续订陷阱",
            "## 🚪 终止与取消",
            "## 📌 核心要点",
        ],
        "footer_text": "--- \n 由 SkyNet 提供支持，我们正在关注。",
        "read_aloud_label": "♿ 读给我听",
        "voice_section_title": "🎙️ 语音解释",
        "voice_instruction": "在下方录制您的提问或主题，以便自动转录并简化。",
        "voice_record_label": "录制语音",
        "tab1_name": "💡 简明解释",
        "tab2_name": "📄 文档分析",
        "tab3_name": "🚪 逃生条款 (Escape)",
        "escape_title": "简明解释 - 逃生条款",
        "escape_subtitle": "解释我们需要摆脱的事物。",
        "escape_badge": "🚪 **终极“救救我”情报实验室已激活并准备就绪**。",
        "escape_doc_section": "📄 让我们看看您需要什么帮助。",
        "escape_text_label": "粘贴任何需要帮助理解和简化的内容。",
        "escape_text_placeholder": "在此粘贴...",
        "escape_hint_label": "添加您需要重点关注的任何细节：",
        "escape_hint_placeholder": "例如：想要立即升级优先级...",
        "escape_lab_section": "🚪 应急套件",
        "escape_urgency_label": "⚡ 紧急程度：您的“脱身”急迫程度为：",
        "escape_persona_label": "解释的视角风格：",
        "tactical_persona_prompt": "请在下方选择您的战术角色框架",
        "end_suffering_btn_title": "🔴 结束我的痛苦 💀",
        "end_suffering_btn_desc": "(一种冰冷平静、催眠般的混合体，兼具稳定的语调、不可预测的句法、怪异的强调、对官僚主义的傲慢以及绝对的心理压制)",
        "escape_run_btn": "🚀 执行战术事件协议",
        "escape_clear_btn": "🧹 清除事件并重新开始",
        "escape_success": "您的逃生条款已准备就绪！",
        "escape_no_text": "请提供要分析的文本文档。",
        "escape_spinner": "正在执行深度运营实验室分析...",
        "escape_disclaimer": "*注意：我们可以提供战略指导和战术脚本来帮助您领先，但我们不能保证特定结果或合规性。然而，执行此协议为您提供的胜算明显好于什么都不做。*",
        "personas": {
            "Houdini Mode": ("🪄 胡迪尼模式", "用于脱身的障眼法"),
            "Grandma Filter": ("👵 奶奶过滤器", "温暖、耐心的安慰指导"),
            "Escape Hatch Locator": ("🎯 逃生舱定位器", "直达出口的雷达"),
            "7-Year-Old Playground Mindset": ("🖍️ 7岁儿童心态", "纯真、无邪的天真想象"),
            "Ruthless Barrister": ("⚖️ 无情大律师", "极具攻击性的法律杠杆"),
            "Zen Negotiator": ("🧘 禅宗谈判专家", "镇定、和平、从容的调解人"),
            "Corporate Shark": ("🦈 公司鲨鱼", "我该从哪里开始咬第一口"),
            "Bureaucracy Hacker": ("🕵️ 官僚主义黑客", "绕过自动化机器人"),
        },
        "help_title": "💡 如何使用此应用",
        "help_s1_title": "1. 侧边栏设置",
        "help_s1_desc": "选择您偏好的语言、复杂程度和语调。",
        "help_s2_title": "2. 标签页 1 (主题简化器)",
        "help_s2_desc": "输入或口述主题以获得结构化解释、PDF 和音频。",
        "help_s3_title": "3. 标签页 2 & 标签页 3",
        "help_s3_desc": "探索文档分析、高级运营实验室和会话日志。",
    },
    "Hindi": {
        "lang_label": "🌐 **भाषा**",
        "api_label": "Gemini API कुंजी",
        "depth_label": "क्या आप चाहते हैं कि आपका उत्तर हो: ",
        "depth_options": ["आसान", "संतुलित", "कठिन"],
        "tone_label": "🎭 **टोन / व्यक्तित्व**",
        "tone_options": [
            "मित्रवत और विनम्र",
            "पेशेवर और सीधा",
            "आसानी से समझ आने वाला",
            "🏴‍☠️ पाइरेट कैप्टन",
            "🚀 अति-कैफ़ीनयुक्त टेक ब्रो",
            "🕵️‍♂️ 1940 के दशक का जासूस",
            "🧙‍♂️ बुद्धिमान जादूगर",
        ],
        "topic_label": "आप किस बारे में जानना चाहते हैं?",
        "topic_placeholder": "उदा., इतिहास, स्नूपी, रसायन विज्ञान, सरकार",
        "button_label": "इसे सरल बनाते हैं",
        "start_over": "🧹 फिर से शुरू करें",
        "terms_button": "📜 नियम और शर्तें",
        "privacy_notice_box": """<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>गोपनीयता नोट:</strong> आप यहाँ जो कुछ भी डाल रहे हैं, हम पर भरोसा रखें: किसी को कोई खास परवाह नहीं है। आपके दस्तावेज़ कोई बहुत अनोखे नहीं हैं, और उन्हें याद रखने के लिए सर्वर स्पेस या दिमाग खर्च करने में हमारी ज़रा भी दिलचस्पी नहीं है। हम इसे तुरंत पूरी तरह मिटा देते हैं, क्योंकि आपका उबाऊ कचरा जमा करना वैसे भी हमारे किसी काम का नहीं है। आगे बढ़ें।</div>""",
        "no_api": " कृपया अपनी Gemini API कुंजी दर्ज करें।",
        "no_topic": "कृपया वह विषय दर्ज करें जिसे आप समझाना चाहते हैं।",
        "ready": {
            "Easy": "नमस्ते! आपका उत्तर तैयार है और समझने में आसान है:",
            "Balanced": "नमस्ते! आपका उत्तर संतुलित ज़ेन स्थिति में तैयार है:",
            "Hard": "नमस्ते! आपका उत्तर आपको सिरदर्द देने के लिए तैयार है:",
        },
        "subtitle": "**जटिल प्रश्नों के सरल उत्तर।**",
        "bottom_line": "निष्कर्ष",
        "spinners": {
            "Easy": "इसे जितना संभव हो उतना सरल बनाया जा रहा है...",
            "Balanced": "अधिकांश के लिए सही ढंग से तैयार किया जा रहा है...",
            "Hard": "ठीक है, अगर आप यही चाहते हैं...",
        },
        "pillar_headers": [
            "## मुख्य अवधारणा",
            "## यह क्या है?",
            "## यह कैसे काम करता है?",
            "## हम क्या छोड़ रहे हैं?",
            "## यह क्यों महत्वपूर्ण है?",
            "## यह हमें कैसे प्रभावित करता है?",
            "## छिपे हुए तथ्य",
            "## स्रोत और सत्यापन",
        ],
        "fine_print_title": "सरल शब्दों में: धाराएं और कानूनी दस्तावेज",
        "fine_print_subtitle": "उन चीज़ों को समझना जो हम कभी नहीं जानते थे।",
        "choose_input_mode": "चुनें कि आप जानकारी कैसे देना चाहते हैं:",
        "input_modes": ["टेक्स्ट चिपकाएं", "वेब लिंक / URL", "छवि अपलोड करें", "PDF अपलोड करें"],
        "paste_label": "जिसे सरल बनाना है उसे चिपकाएं या अपलोड करें।",
        "url_label": "गोपनीयता नीति का URL चिपकाएं:",
        "upload_label": "छवि अपलोड करें:",
        "upload_pdf_label": "कानूनी दस्तावेज़ (PDF) अपलोड करें:",
        "decode_button": "इसे सरल बनाते हैं",
        "simplifying_spinner": "समझने के लिए तैयार हो जाइए...",
        "fine_print_headers": [
            "## 🚦 जोखिम सारांश",
            "## 📄 मुख्य धाराएं",
            "## ⚖️ देयता और अधिकार",
            "## 🔒 डेटा गोपनीयता",
            "## 💳 छिपे हुए शुल्क",
            "## 🚪 समाप्ति",
            "## 📌 निष्कर्ष",
        ],
        "footer_text": "--- \n SkyNet द्वारा संचालित।",
        "read_aloud_label": "♿ मुझे पढ़कर सुनाओ",
        "voice_section_title": "🎙️ आवाज़ से स्पष्टीकरण",
        "voice_instruction": "स्वचालित रूप से ट्रांसक्राइब और सरल बनाने के लिए नीचे अपना प्रश्न या विषय रिकॉर्ड करें।",
        "voice_record_label": "आवाज़ रिकॉर्ड करें",
        "tab1_name": "💡 सरल व्याख्या",
        "tab2_name": "📄 दस्तावेज़",
        "tab3_name": "🚪 एस्केप क्लॉज़",
        "escape_title": "एस्केप क्लॉज़",
        "escape_subtitle": "उन चीज़ों की व्याख्या जिनसे हमें बचने की आवश्यकता है।",
        "escape_badge": "🚪 **खुफिया प्रयोगशाला सक्रिय है**.",
        "escape_doc_section": "📄 देखें कि आपको किस चीज़ में मदद चाहिए।",
        "escape_text_label": "विश्लेषण के लिए टेक्स्ट चिपकाएं:",
        "escape_text_placeholder": "यहाँ चिपकाएं...",
        "escape_hint_label": "विवरण जोड़ें:",
        "escape_hint_placeholder": "उदा., प्राथमिकता बढ़ाना चाहते हैं...",
        "escape_lab_section": "🚪 आपातकालीन सूट",
        "escape_urgency_label": "⚡ तात्कालिकता पैमाना:",
        "escape_persona_label": "स्पष्टीकरण दृष्टिकोण:",
        "tactical_persona_prompt": "अपना सामरिक व्यक्तित्व ढांचा चुनें",
        "end_suffering_btn_title": "🔴 मेरी पीड़ा समाप्त करो 💀",
        "end_suffering_btn_desc": "(शीतल और पूर्ण मनोवैज्ञानिक विनाश)",
        "escape_run_btn": "🚀 सामरिक प्रोटोकॉल निष्पादित करें",
        "escape_clear_btn": "🧹 साफ़ करें और फिर से शुरू करें",
        "escape_success": "आपका एस्केप क्लॉज़ तैयार है!",
        "escape_no_text": "कृपया टेक्स्ट परिदृश्य प्रदान करें।",
        "escape_spinner": "प्रयोगशाला विश्लेषण निष्पादित किया जा रहा है...",
        "escape_disclaimer": "*नोट: हम बिना किसी गारंटी के रणनीतिक मार्गदर्शन प्रदान करते हैं।*",
        "personas": {
            "Houdini Mode": ("🪄 हुदिनी मोड", "बाहर निकलने के लिए जादुई तरकीबें"),
            "Grandma Filter": ("👵 दादी का फ़िल्टर", "गर्मजोशी और धैर्यवान मार्गदर्शन"),
            "Escape Hatch Locator": ("🎯 एस्केप हैच लोकेटर", "निकास के लिए सीधा radar"),
            "7-Year-Old Playground Mindset": ("🖍️ 7 साल के बच्चे की मानसिकता", "शुद्ध बचकानी जिज्ञासा"),
            "Ruthless Barrister": ("⚖️ निर्दयी वकील", "आक्रामक कानूनी लाभ"),
            "Zen Negotiator": ("🧘 ज़ेन वार्ताकार", "शांत और स्पष्ट मध्यस्थ"),
            "Corporate Shark": ("🦈 कॉर्पोरेट शार्क", "पहले कहाँ काटें"),
            "Bureaucracy Hacker": ("🕵️ नौकरशाही हैकर", "रोबोट को बायपास करना"),
        },
        "help_title": "💡 इस ऐप का उपयोग कैसे करें",
        "help_s1_title": "1. साइडबार सेटिंग्स",
        "help_s1_desc": "अपनी पसंदीदा भाषा, जटिलता स्तर और टोन चुनें।",
        "help_s2_title": "2. टैब 1 (विषय सरलकर्ता)",
        "help_s2_desc": "संरचित स्पष्टीकरण, पीडीएफ और ऑडियो के लिए कोई विषय टाइप करें या वॉयस रिकॉर्डर का उपयोग करें।",
        "help_s3_title": "3. टैब 2 और टैब 3",
        "help_s3_desc": "दस्तावेज़ विश्लेषण और इतिहास के लिए अतिरिक्त टैब का अन्वेषण करें।",
    },
    "Korean": {
        "lang_label": "🌐 **언어**",
        "api_label": "Gemini API 키",
        "depth_label": "답변의 수준을 선택하세요: ",
        "depth_options": ["쉬움", "균형", "어려움"],
        "tone_label": "🎭 **어조 / 페르소나**",
        "tone_options": [
            "친절하고 정중함",
            "전문적이고 직접적",
            "캐주얼하고 위트 있음",
            "🏴‍☠️ 해적 선장 (아호이!)",
            "🚀 카페인 과다 테크 브로",
            "🕵️‍♂️ 1940년대 느와르 탐정",
            "🧙‍♂️ 지혜로운 판타지 마법사",
        ],
        "topic_label": "어떤 것에 대해 알고 싶으신가요?",
        "topic_placeholder": "예: 역사, 스누피, 화학, 정부 등",
        "button_label": "쉽게 설명해 주세요",
        "start_over": "🧹 처음부터 다시",
        "terms_button": "📜 이용약관",
        "privacy_notice_box": '<div style="font-size: 0.8rem; padding: 10px; border-radius: 6px; background-color: rgba(2, 132, 199, 0.08); border-left: 4px solid #0284C7; margin-bottom: 15px; text-align: center;">🔒 <strong>개인정보 보호 안내:</strong> 저장되는 것은 아무것도 없습니다. 제공해주신 문서나 민감한 정보는 일시적으로 처리되며 절대 저장되지 않습니다. 안전하고 프라이빗하게 이해하기 쉽게 설명해 드립니다.</div>',
        "no_api": " Gemini API 키를 입력하거나 GEMINI_API_KEY 환경 변수를 설정해 주세요.",
        "no_topic": "설명이 필요한 내용을 입력해 주세요.",
        "ready": {
            "Easy": "안녕하세요! 쉽고 이해하기 쉬운 답변이 준비되었습니다:",
            "Balanced": "안녕하세요! 균형 잡힌 Zen 상태의 답변이 준비되었습니다:",
            "Hard": "안녕하세요! 원하시던 머리 아픈 답변이 준비되었습니다:",
        },
        "subtitle": "**복잡한 질문을 알기 쉽게 풀어드립니다.**",
        "bottom_line": "핵심 요약",
        "spinners": {
            "Easy": "최대한 간단하게 만드는 중...",
            "Balanced": "대부분에게 딱 맞게 준비하는 중...",
            "Hard": "알겠습니다, 원하시는 대로 준비 중입니다...",
        },
        "pillar_headers": [
            "## 핵심 개념",
            "## 그것은 무엇인가요?",
            "## 어떻게 작동하나요?",
            "## 우리는 무엇을 포기하고 있나요?",
            "## 왜 중요한가요?",
            "## 우리에게 어떤 영향을 미치나요?",
            "## 숨겨진 사실들",
            "## 출처 및 검증",
        ],
        "fine_print_title": "간단 설명: 조항, 조건, 법률 문서, 의무 및 이해해야 할 기타 문서",
        "fine_print_subtitle": "알지 못했던 내용과 설명되지 않은 문서를 쉽게 풀어드립니다.",
        "choose_input_mode": "정보를 제공할 방식을 선택하세요:",
        "input_modes": ["텍스트 붙여넣기", "웹 링크 / URL", "이미지 업로드", "PDF 업로드"],
        "paste_label": "간단하게 만들고 싶은 텍스트를 붙여넣거나 업로드하세요.",
        "url_label": "개인정보 처리방침 또는 이용약관 URL 붙여넣기:",
        "upload_label": "문서 이미지 또는 스크린샷 업로드:",
        "upload_pdf_label": "법적 문서 또는 계약서(PDF) 업로드:",
        "decode_button": "쉽게 설명해 주세요",
        "simplifying_spinner": "이해할 준비를 하는 중...",
        "fine_print_headers": [
            "## 🚦 위험 요약",
            "## 📄 주요 조항 설명",
            "## ⚖️ 책임 및 권리 포기",
            "## 🔒 데이터 프라이버시 및 추적",
            "## 💳 숨겨진 수수료 및 자동 갱신 함정",
            "## 🚪 해지 및 취소",
            "## 📌 핵심 요약",
        ],
        "footer_text": "--- \n Powered by SkyNet. 지켜보고 있습니다.",
        "read_aloud_label": "♿ 읽어주기",
        "voice_section_title": "🎙️ 음성 설명",
        "voice_instruction": "아래에 질문이나 주제를 녹음하면 자동으로 텍스트로 변환되어 쉽게 설명됩니다.",
        "voice_record_label": "음성 녹음",
        "tab1_name": "💡 간단 설명",
        "tab2_name": "📄 문서 분석",
        "tab3_name": "🚪 탈출 조항 (Escape)",
        "escape_title": "간단 설명 - 탈출 조항",
        "escape_subtitle": "우리가 벗어나야 할 상황들을 설명합니다.",
        "escape_badge": "🚪 **궁극의 '날 여기서 꺼내줘' 인텔리전스 연구소가 활성화되었습니다**.",
        "escape_doc_section": "📄 도움이 필요한 내용을 확인해보세요.",
        "escape_text_label": "이해하고 탈출하는 데 도움이 필요한 텍스트를 붙여넣으세요.",
        "escape_text_placeholder": "여기에 붙여넣기...",
        "escape_hint_label": "집중해서 다루어야 할 세부 사항 추가:",
        "escape_hint_placeholder": "예: 우선순위를 즉시 격상시키고 싶음...",
        "escape_lab_section": "🚪 비상 대책 스위트",
        "escape_urgency_label": "⚡ 긴급도 척도: 탈출하고 싶은 급박한 정도는?",
        "escape_persona_label": "설명 페르소나 선택:",
        "tactical_persona_prompt": "전술적 페르소나 프레임워크를 선택하세요",
        "end_suffering_btn_title": "🔴 내 고통을 끝내줘 💀",
        "end_suffering_btn_desc": "(차분하고 최면적인 톤, 예측 불가능한 문법, 관료주의에 대한 오만함과 절대적 심리 압박을 결합한 엘리트 솔루션)",
        "escape_run_btn": "🚀 전술적 사건 프로토콜 실행",
        "escape_clear_btn": "🧹 사건 기록 지우고 새로 시작",
        "escape_success": "탈출 조항이 준비되었습니다!",
        "escape_no_text": "분석할 텍스트 시나리오를 제공해 주세요.",
        "escape_spinner": "고강도 운영 연구소 분석 실행 중...",
        "escape_disclaimer": "*참고: 앞서 나갈 수 있도록 전략적 지침과 전술 스크립트를 제공하지만, 특정 결과나 제도적 규정 준수를 보장하지는 않습니다. 그러나 이 프로토콜을 실행하면 아무것도 하지 않는 것보다 훨씬 더 높은 승률을 보장합니다.*",
        "personas": {
            "Houdini Mode": ("🪄 후디니 모드", "탈출을 위한 마법 같은 트릭"),
            "Grandma Filter": ("👵 할머니 필터", "따뜻하고 인내심 있는 위로의 조언"),
            "Escape Hatch Locator": ("🎯 탈출 해치 로케이터", "출구를 직격하는 레이더"),
            "7-Year-Old Playground Mindset": ("🖍️ 7살 어린이의 시선", "순수하고 천진난만한 호기심"),
            "Ruthless Barrister": ("⚖️ 자비 없는 변호사", "공격적인 법적 레버리지"),
            "Zen Negotiator": ("🧘 젠 협상가", "차분하고 평화로운 세레인 중재자"),
            "Corporate Shark": ("🦈 코퍼레이트 샤크", "어디를 먼저 물어야 할까"),
            "Bureaucracy Hacker": ("🕵️ 관료주의 해커", "자동화된 로봇 우회하기"),
        },
        "help_title": "💡 앱 사용 방법",
        "help_s1_title": "1. 사이드바 설정",
        "help_s1_desc": "원하는 언어, 난이도 레벨, 어조를 선택하세요.",
        "help_s2_title": "2. 탭 1 (주제 단순화)",
        "help_s2_desc": "주제를 입력하거나 음성으로 녹음하여 구조화된 설명, PDF, 오디오를 받아보세요.",
        "help_s3_title": "3. 탭 2 & 탭 3",
        "help_s3_desc": "문서 분석, 고급 운영 연구소, 세션 로그 기능을 활용하세요.",
    },
}

LANGUAGES = list(UI_TEXT.keys())


# ==============================================================================
# [SECTION 4: UTILITY FUNCTIONS (PDF EXPORT & FETCHERS)]
# ==============================================================================
def fetch_url_text(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for element in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        element.decompose()
    return soup.get_text(separator=" ", strip=True)


def prepare_media_part(uploaded_file):
    if uploaded_file is None:
        return None
    return types.Part.from_bytes(
        data=uploaded_file.getvalue(), mime_type=uploaded_file.type
    )

def generate_pdf_bytes(title: str, content: str, footer_signoff: str) -> bytes:
    import re
    
    class PreviewBannerPDF(FPDF):
        def header(self):
            # Top preview banner stamp using safe ln=True
            self.set_font("helvetica", "B", 9)
            self.set_text_color(160, 160, 160) # Soft neutral grey
            self.cell(0, 6, "--- SIMPLY-EXPLAINED * THE PREVIEW ---", align="C", ln=True)
            self.ln(4)

        def footer(self):
            # Bottom preview footer stamp
            self.set_y(-15)
            self.set_font("helvetica", "I", 8)
            self.set_text_color(160, 160, 160)
            self.cell(0, 10, "PREVIEW DRAFT - FOR EVALUATION ONLY", align="C")

    pdf = PreviewBannerPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Aggressively strip out any non-standard/non-ASCII characters that break core fonts
    def sanitize(text: str) -> str:
        if not text:
            return ""
        return re.sub(r'[^\x00-\x7F]+', '', text)

    # Title Styling
    pdf.set_font("helvetica", "B", 16)
    pdf.set_text_color(2, 132, 199)
    pdf.cell(
        0,
        10,
        "Simply Explained - The Report",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="L",
    )

    # Timestamp
    pdf.set_font("helvetica", "I", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(
        0,
        6,
        f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="L",
    )
    pdf.ln(5)

    # Report Title
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 8, sanitize(title))
    pdf.ln(4)

    # Main Content
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)

    raw_clean = content.replace("##", "").replace("###", "").replace("**", "")
    pdf.multi_cell(0, 6, sanitize(raw_clean))

    # Footer Signoff
    pdf.ln(10)
    pdf.set_font("helvetica", "I", 8)
    pdf.set_text_color(120, 120, 120)

    raw_signoff = footer_signoff.replace("---", "").strip()
    pdf.multi_cell(0, 5, sanitize(raw_signoff))

    pdf_output = pdf.output()
    if isinstance(pdf_output, str):
        pdf_bytes = pdf_output.encode("latin-1")
    else:
        pdf_bytes = bytes(pdf_output)

    return pdf_bytes

# ==============================================================================
# [SECTION 5: STREAMLIT APP INITIALIZATION & STYLING]
# ==============================================================================
is_streamlit = "streamlit" in sys.modules or os.getenv("SERVER_PORT") == "8501"

if is_streamlit:
    import streamlit as st

    st.set_page_config(page_title="Simply Explained", page_icon="💡", layout="wide")

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        div[data-testid="stMarkdownContainer"] p, 
        div[data-testid="stMarkdownContainer"] li {
            font-size: 1.15rem !important;
            line-height: 1.5 !important;
        }
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3 {
            font-size: 1.5rem !important;
            margin-top: 1.5rem !important;
            margin-bottom: 0.6rem !important;
        }
        .app-title {
            font-size: 2.8rem !important;
            font-weight: 700 !important;
            text-decoration: underline;
            margin-bottom: 0px;
        }
        .fine-print-title {
            font-size: 1.8rem !important;
            font-weight: 700 !important;
            margin-bottom: 0px;
        }
        .app-subtitle {
            font-size: 1.1rem !important;
            font-weight: bold !important;
            margin-top: 3px;
            margin-bottom: 10px;
        }

        div[data-testid="stSidebar"] {
            padding-top: 0.1rem !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        div[data-testid="stSidebar"] .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0.5rem !important;
            gap: 0.25rem !important;
        }
        div[data-testid="stSidebar"] hr {
            margin: 0.4rem 0 !important;
        }

        div.stButton > button, 
        div.stFormSubmitButton > button {
            background-color: #0284C7 !important;
            color: #FFFFFF !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            padding: 0.3rem 0.8rem !important;
            border-radius: 0.4rem !important;
            box-shadow: 0 3px 10px rgba(2, 132, 199, 0.2) !important;
            border: none !important;
            transition: all 0.2s ease-in-out !important;
            width: 100% !important;
        }
        div.stButton > button:hover, 
        div.stFormSubmitButton > button:hover {
            background-color: #0369A1 !important;
            color: #FFFFFF !important;
            box-shadow: 0 5px 14px rgba(3, 105, 161, 0.3) !important;
            border: none !important;
        }

        div[data-testid="stDialog"] {
            width: 85vw !important;
            max-width: 950px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    env_api_key = os.getenv("GEMINI_API_KEY", "")

    if "selected_lang" not in st.session_state:
        st.session_state["selected_lang"] = "English"
    if "history_log" not in st.session_state:
        st.session_state["history_log"] = []

# 1. Language Selector
    selected_lang = st.sidebar.selectbox(
        "🌐 **Language**",
        LANGUAGES,
        index=(
            LANGUAGES.index(st.session_state["selected_lang"])
            if st.session_state["selected_lang"] in LANGUAGES
            else 0
        ),
        key="language_selector",
    )
    st.session_state["selected_lang"] = selected_lang
    texts = UI_TEXT.get(selected_lang, UI_TEXT["English"])

    # 2. Tone Selector
    tone_level = st.sidebar.selectbox(
        texts["tone_label"], texts["tone_options"], key="tone_radio_key"
    )

    # 3. Read Aloud Checkbox
    enable_audio_speech = st.sidebar.checkbox(
        texts["read_aloud_label"],
        value=False,
        help="Generates an audio player for each simplified response in the selected language.",
        key="enable_audio_speech_unique_key",
    )

    st.sidebar.markdown("---")

    # 4. Depth / Complexity Radio (The Easy, Balanced, Hard setting)
    depth_level = st.sidebar.radio(
        texts["depth_label"], texts["depth_options"], key="depth_radio_key"
    )
# --- FULL RESET START OVER BUTTON ---
if st.sidebar.button("🔄 Start Over (Reset All)", use_container_width=True, key="global_full_reset_btn"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

st.sidebar.markdown("---")

# --- CUSTOM CSS FOR THINNER, CENTERED SIDEBAR BUTTONS ---
st.markdown("""
    <style>
    div[data-testid="stSidebar"] div.stButton > button {
        padding: 4px 10px !important;
        font-size: 0.82rem !important;
        border-radius: 4px !important;
        display: block !important;
        margin: 0 auto !important;
        width: 85% !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. TERMS & CONDITIONS MODAL & BUTTON ---
@st.dialog("Terms of Service & EULA")
def show_terms_dialog():
    current_terms = TERMS_TEXT.get(selected_lang, TERMS_TEXT["English"])
    st.markdown(current_terms, unsafe_allow_html=True)
    if st.button("Close", key="close_terms_modal_btn"):
        st.rerun()

terms_label = texts.get("terms_button", "📜 Terms & Conditions")
if st.sidebar.button(terms_label, use_container_width=True, key="terms_button_sidebar_unique"):
    show_terms_dialog()

st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)

# --- 2. HOW TO USE THIS APP MODAL & BUTTON ---
@st.dialog("💡 How to Use This App")
def show_help_dialog():
    help_s1_t = texts.get("help_s1_title", "1. Sidebar Settings")
    help_s1_d = texts.get("help_s1_desc", "Select your preferred language, complexity tier, and tone.")
    help_s2_t = texts.get("help_s2_title", "2. Tab 1 (Topic Simplifier)")
    help_s2_d = texts.get("help_s2_desc", "Type or dictate a subject for structured explanations, PDFs, and audio.")
    help_s3_t = texts.get("help_s3_title", "3. Tab 2 & Tab 3")
    help_s3_d = texts.get("help_s3_desc", "Explore document analysis, advanced operational labs, and session logs.")

    st.markdown(f"""
    ### 💡 Quick Start Guide
    
    * **{help_s1_t}**  
      {help_s1_d}
      
    * **{help_s2_t}**  
      {help_s2_d}
      
    * **{help_s3_t}**  
      {help_s3_d}
    """)
    if st.button("Close", key="close_help_modal_btn"):
        st.rerun()

help_button_label = texts.get("help_title", "💡 How to Use This App")
if st.sidebar.button(help_button_label, use_container_width=True, key="help_button_sidebar_unique"):
    show_help_dialog()

st.sidebar.markdown("---")
# --- INITIALIZE THE GOOGLE GENAI CLIENT ---
from google import genai
from google.genai import types

client = genai.Client(
    vertexai=True,
    project="sunny-incentive-387017",  
    location="us-central1",
    http_options=types.HttpOptions(
        headers={"Authorization": ""}
    )
)

# ==============================================================================
# [SECTION 7: MAIN TAB NAVIGATION SETUP & INTERFACES]
# ==============================================================================
if is_streamlit:
    tab1, tab2, tab3 = st.tabs(
        [texts["tab1_name"], texts["tab2_name"], texts["tab3_name"]]
    )

# ==============================================================================
# [SECTION 6: CORE GENERATION & RESPONSE RENDERING ENGINE]
# ==============================================================================
from google.genai import types

with st.form("simply_explained_form"):
    topic = st.text_input("-----")
    submitted = st.form_submit_button(texts.get("submit_button", "----"))

    if 'audio_value' not in locals():
        audio_value = None

    if submitted:
        if not topic and audio_value is None:
            st.error(texts.get("missing_input_error", "Please enter a topic or record an audio inquiry."))
        else:
            spinner_text = texts["spinners"].get(depth_level, texts["simplifying_spinner"])
            with st.spinner(spinner_text):
                try:
                    client = genai.Client(
                        vertexai=True,
                        project="238164610704",
                        location="us-central1",
                        http_options=types.HttpOptions(
#                            headers={"Authorization": ""}
                        )
                    )

                    full_prompt = f"Explain the following topic as a {persona_choice} with a depth level of {depth_level}: {topic}"
                    
                    response = client.models.generate_content(
                        model=MODEL_ID,
                        contents=full_prompt,
                    )
                    output_text = response.text
                    st.success("Live API Connected Successfully!")

                except Exception as api_err:
                    output_text = f"Live Error Caught: {api_err}"

                st.session_state["last_response"] = output_text
                st.markdown("### Explanation")
                st.markdown(output_text)


# ==============================================================================
# [SECTION 8: TAB 1 - MAIN TOPIC SIMPLIFIER INTERFACE]
# ==============================================================================
with tab1:
    title_map = {
        "English": "Simply Explained",
        "Spanish": "Simplemente Explicado",
        "French": "Simplement Expliqué",
        "German": "Einfach Erklärt",
        "Italian": "Semplicemente Spiegato",
        "Portuguese": "Simplesmente Explicado",
    }
    subtitle_map = {
        "English": "What You Need To Know",
        "Spanish": "Lo Que Necesitas Saber",
        "French": "Ce Que Vous Devez Savoir",
        "German": "Was Sie Wissens Muessten",
        "Italian": "Quello Che Devi Sapere",
        "Portuguese": "O Que Voce Precisa Saber",
    }
    current_title = title_map.get(selected_lang, texts.get("app_main_title", "Simply Explained"))
    current_subtitle = subtitle_map.get(selected_lang, texts.get("subtitle", "What you need to know"))

    st.markdown(
        f'<div class="app-title">{current_title}</div>', unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="app-subtitle">{current_subtitle}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(texts["privacy_notice_box"], unsafe_allow_html=True)

    topic = st.text_input(
        texts["topic_label"],
        placeholder=texts["topic_placeholder"],
        key="main_topic_input_field",
    )
    
    st.markdown("---")
    st.markdown(f"### {texts['voice_section_title']}")
    st.markdown(texts['voice_instruction'])
    
    st.markdown(
        """
        <style>
        div[data-testid="stAudioInput"] {
            transform: scale(1.00);
            transform-origin: top left;
            margin-top: 5px;
            margin-bottom: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    audio_value = st.audio_input(texts['voice_record_label'], key="main_audio_recorder_field")
    
    st.markdown("")
    submitted = st.button(texts["button_label"], key="main_generate_btn", use_container_width=True)

    if submitted:
        api_key = st.secrets.get("GEMINI_API_KEY", "")

        if not api_key:
            st.error(texts["no_api"])
        elif not topic and audio_value is None:
            st.error(texts.get("missing_input_error", "Please enter a topic or record an audio inquiry."))
        else:
            spinner_text = texts["spinners"].get(
                depth_level, texts["simplifying_spinner"]
            )
            with st.spinner(spinner_text):
                try:
                    client = genai.Client(api_key=api_key)

                    if depth_level in ["Easy", "Fácil", "Einfach", "Facile", "आसान", "简单", "簡単", "쉬움"]:
                        depth_instruction = (
                            f"Complexity Tier: EASY. Explain using ultra-plain,"
                            f" crystal-clear everyday language in {selected_lang} for ages 13 and below, wite some love and a sprikle of bullines"
                        )
                    elif depth_level in ["Balanced", "Equilibrado", "Ausgewogen", "Équilibré", "संतुलित", "平衡", "バランス", "균형"]:
                        depth_instruction = (
                            f"Complexity Tier: BALANCED. Provide a balanced, professional, well educated nerd with a hint of teacher's pet. "
                            f" overview in {selected_lang}."
                        )
                    else:
                        depth_instruction = (
                            f"Complexity Tier: HARD. Provide an advanced, academically, PHD and some quantum physics. All this at a level of hate because you are a nerd."
                            f" rigorous, deeply technical breakdown in {selected_lang}. You MUST use Google Search grounding (tools=[types.Tool(google_search=types.GoogleSearch())]) to query live authoritative references and official documentation matching the topic. In the 8th pillar ('Where Do We Find It (Verification & Sources)'), explicitly list these grounding sources as clickable markdown links."
                        )

                    if audio_value is not None:
                        input_payload = [
                            f"Listen to this audio inquiry and explain the topic in {selected_lang} at the {depth_level} tier, following all system instructions:",
                            types.Part.from_bytes(data=audio_value.getvalue(), mime_type="audio/wav")
                        ]
                        display_title = "Voice Inquiry Audio"
                    else:
                        input_payload = (
                            f"Explain or simplify this topic in {selected_lang} at"
                            f" the {depth_level} tier: {topic}"
                        )
                        display_title = topic

                    system_instruction = (
                        f"You are an expert educator. Respond entirely and strictly"
                        f" in: {selected_lang}. Adopt tone: {tone_level}."
                        f" {depth_instruction} Start with a title formatted as: #"
                        f" Simply Explained ({depth_level}): {display_title}. Structure your"
                        f" response using these exact pillars: 1)"
                        f" {texts['pillar_headers'][0]}, 2)"
                        f" {texts['pillar_headers'][1]}, 3)"
                        f" {texts['pillar_headers'][2]}, 4)"
                        f" {texts['pillar_headers'][3]}, 5)"
                        f" {texts['pillar_headers'][4]}, 6)"
                        f" {texts['pillar_headers'][5]}, 7)"
                        f" {texts['pillar_headers'][6]}, and 8)"
                        f" {texts['pillar_headers'][7]}. End with: ##"
                        f" {texts['bottom_line']}."
                    )

                    gen_config_kwargs = {
                        "system_instruction": system_instruction,
                        "temperature": 0.8
                    }
                    if depth_level in ["Hard", "Difícil", "Schwierig", "Difficile", "कठिन", "困难", "高難度", "어려움"]:
                        gen_config_kwargs["tools"] = [types.Tool(google_search=types.GoogleSearch())]

                    # 1. GENERATE CONTENT
                    response = client.models.generate_content(
                        model=MODEL_ID,
                        contents=input_payload,
                        config=types.GenerateContentConfig(**gen_config_kwargs),
                    )

                    output_text = response.text + f"\n\n{texts['footer_text']}"
                    st.success(
                        texts["ready"].get(depth_level, "Your response is ready")
                    )
                    st.markdown("---")
                    st.markdown(output_text)

                    # 2. PDF GENERATION
                    safe_title = ''.join(c for c in f"Topic ({depth_level}): {display_title}" if ord(c) < 128)
                    safe_output = output_text.encode('ascii', 'ignore').decode('ascii')

                    pdf_data = generate_pdf_bytes(
                        safe_title,
                        safe_output,
                        texts.get("footer_text", "The Report - Simply Explained"),
                    )
                    st.download_button(
                        label=texts.get("pdf_button", "📥 Press to Download PDF Report"),
                        data=pdf_data,
                        file_name=f"Simply_Explained_{display_title.replace(' ', '_')}.pdf",
                        mime="application/pdf",
                        key="download_topic_pdf",
                    )

                # --- CLOSE THE MAIN API TRY BLOCK HERE BEFORE AUDIO ---
                except APIError as e:
                    st.error(f"API Error: {e.message}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")

               # 3. AUDIO ACCESSIBILITY (OUTSIDE THE API TRY/EXCEPT BLOCK)
                if enable_audio_speech:
                    st.markdown("---")
                    st.markdown(f"### {texts.get('audio_feed_header', '🔊 Audio Accessibility Feed')}")
                    try:
                        from gtts import gTTS

                        clean_text_for_speech = output_text
                        clean_text_for_speech = re.sub(r'[#*`_-]', ' ', clean_text_for_speech)
                        clean_text_for_speech = re.sub(r'\s+', ' ', clean_text_for_speech).strip()

                        tts = gTTS(
                            text=clean_text_for_speech,
                            lang=TTS_LANG_MAP.get(selected_lang, "en"),
                            slow=False,
                        )
                        audio_bytes_obj = io.BytesIO()
                        tts.write_to_fp(audio_bytes_obj)
                        audio_bytes_obj.seek(0)
                        st.audio(audio_bytes_obj, format="audio/mp3")
                    except Exception as tts_err:
                        st.warning(
                            f"{texts.get('audio_stream_error', 'Could not generate audio stream: ')}{str(tts_err)}"
                        )

# ==============================================================================
  # [SECTION 9: TAB 2 - DOCUMENT DECODER INTERFACE]
  # ==============================================================================
with tab2:
	st.markdown(
	    f'<div class="fine-print-title">{texts["fine_print_title"]}</div>',
	    unsafe_allow_html=True,
	)
	st.markdown(
	    f'<div class="app-subtitle">{texts["fine_print_subtitle"]}</div>',
	    unsafe_allow_html=True,
	)
	st.markdown(texts["privacy_notice_box"], unsafe_allow_html=True)
	
	mode_options = texts["input_modes"]
	selected_mode_label = st.radio(
	    texts["choose_input_mode"], mode_options, key="fp_input_mode", horizontal=True
	)

	fine_print_content = None
	uploaded_media_part = None
	
	if selected_mode_label == mode_options[0]:
	  fine_print_content = st.text_area(
	      texts["paste_label"], key="fp_text", height=200
	  )
	elif selected_mode_label == mode_options[1]:
	  fine_print_url = st.text_input(
	      texts["url_label"],
	      placeholder="https://example.com/terms",
	      key="fp_url",
	  )
	  if fine_print_url and st.button("Fetch URL Content"):
	    with st.spinner(texts["simplifying_spinner"]):
	      try:
	        st.session_state["fetched_fp_text"] = fetch_url_text(
	            fine_print_url
	        )[:15000]
	        st.success("Successfully fetched webpage text!")
	      except Exception as e:
	        st.error(f"Could not fetch URL content: {str(e)}")
	  fine_print_content = st.session_state.get("fetched_fp_text", "")
	  if fine_print_content:
	    st.text_area(
	        "Fetched Text Preview:",
	        fine_print_content,
	        height=150,
	        disabled=True,
	    )
	elif selected_mode_label == mode_options[2]:
	  uploaded_file = st.file_uploader(
	      texts["upload_label"], type=["png", "jpg", "jpeg", "webp"]
	  )
	  if uploaded_file:
	    st.image(
	        uploaded_file, caption="Uploaded Image Preview", use_container_width=True
	    )
	    uploaded_media_part = prepare_media_part(uploaded_file)
	elif selected_mode_label == mode_options[3]:
	  uploaded_file = st.file_uploader(
	      texts["upload_pdf_label"], type=["pdf"]
	  )
	  if uploaded_file:
	    st.info(
	        f"📄 PDF Uploaded: **{uploaded_file.name}**"
	        f" ({round(uploaded_file.size / 1024, 1)} KB)"
	    )
	    uploaded_media_part = prepare_media_part(uploaded_file)
	
	if st.button(texts["decode_button"], key="fine_print_btn"):
	  if not api_key:
	    st.error(texts["no_api"])
	  elif (
	      selected_mode_label in [mode_options[0], mode_options[1]]
	      and not fine_print_content
	  ):
	    st.warning("Please provide valid text or a URL before decoding.")
	  elif (
	      selected_mode_label in [mode_options[2], mode_options[3]]
	      and not uploaded_media_part
	  ):
	    st.warning("Please upload a file before decoding.")
	  else:
	    with st.spinner(texts["simplifying_spinner"]):
	      try:
	        client = genai.Client(api_key=api_key)
	        system_instruction = (
	            f"You are a skilled legal analyst. Respond entirely and"
	            f" strictly in: {selected_lang}. Structure your analysis"
	            f" using these exact headers: 1)"
	            f" {texts['fine_print_headers'][0]}, 2)"
	            f" {texts['fine_print_headers'][1]}, 3)"
	            f" {texts['fine_print_headers'][2]}, 4)"
	            f" {texts['fine_print_headers'][3]}, 5)"
	            f" {texts['fine_print_headers'][4]}, 6)"
	            f" {texts['fine_print_headers'][5]}, and 7)"
	            f" {texts['fine_print_headers'][6]}."
	        )
	
	        contents = (
	            [
	                uploaded_media_part,
	                (
	                    "Please analyze and decode the provided document in"
	                    f" {selected_lang}."
	                ),
	            ]
	            if uploaded_media_part
	            else [
	                (
	                    "Please analyze and decode the following document text"
	                    f" in {selected_lang}:\n\n{fine_print_content}"
	                )
	            ]
	        )
	
	        response = client.models.generate_content(
	            model=MODEL_ID,
	            contents=contents,
	            config=types.GenerateContentConfig(
	                system_instruction=system_instruction, temperature=0.3
	            ),
	        )
	
	        output_text = response.text + f"\n\n{texts['footer_text']}"
	        st.success(
	            texts["ready"].get(depth_level, "Your response is ready")
	        )
	
	        output_lower = output_text.lower()
	        if any(
	            kw in output_lower
	            for kw in [
	                "high risk",
	                "severe",
	                "penalty",
	                "red",
	                "alto riesgo",
	                "severo",
	            ]
	        ):
	          risk_level = "High"
	        elif any(
	            kw in output_lower
	            for kw in [
	                "medium risk",
	                "caution",
	                "moderate",
	                "yellow",
	                "riesgo medio",
	            ]
	        ):
	          risk_level = "Medium"
	        else:
	          risk_level = "Low"
	
	        st.markdown("---")
	        st.markdown("### 🚦 Document Risk Summary Stoplight")
	        if risk_level == "High":
	          st.markdown(
	              '<div style="padding: 12px; border-radius: 6px;'
	              " background-color: rgba(255, 0, 0, 0.1); border: 1px solid"
	              ' red; font-weight: 600;">🔴 High Risk: Severe penalties or'
	              " heavy exit barriers identified!</div>",
	              unsafe_allow_html=True,
	          )
	        elif risk_level == "Medium":
	          st.markdown(
	              '<div style="padding: 12px; border-radius: 6px;'
	              " background-color: rgba(255, 255, 0, 0.1); border: 1px"
	              ' solid orange; font-weight: 600;">🟡 Medium Risk: Proceed'
	              " with caution. Notice periods or restrictive clauses"
	              " detected.</div>",
	              unsafe_allow_html=True,
	          )
	        else:
	          st.markdown(
	              '<div style="padding: 12px; border-radius: 6px;'
	              " background-color: rgba(0, 255, 0, 0.1); border: 1px solid"
	              ' green; font-weight: 600;">🟢 Low Risk: Document terms'
	              " appear standard.</div>",
	              unsafe_allow_html=True,
	          )
	
	        st.markdown("---")
	        st.markdown(output_text)
	
	        st.session_state["history_log"].insert(
	            0,
	            {
	                "timestamp": datetime.datetime.now().strftime(
	                    "%Y-%m-%d %H:%M:%S"
	                ),
	                "type": "Document Decode",
	                "title": "Document / Contract Analysis",
	                "content": output_text,
	            },
	        )
	
	        pdf_data = generate_pdf_bytes(
	            "Document / Contract Analysis",
	            output_text,
	            texts["footer_text"],
	        )
	        st.download_button(
	            label="📥 Download Legal Decoding PDF",
	            data=pdf_data,
	            file_name="Document_Decoding_Report.pdf",
	            mime="application/pdf",
	            key="download_doc_pdf",
	        )
	
	        if enable_audio_speech:
	          st.markdown("---")
	          st.markdown("### 🔊 Audio Accessibility Feed")
	          try:
	            from gtts import gTTS
	
	            clean_text_for_speech = output_text
	            clean_text_for_speech = re.sub(r'[#*`_-]', ' ', clean_text_for_speech)
	            clean_text_for_speech = re.sub(r'\s+', ' ', clean_text_for_speech).strip()
	
	            tts = gTTS(
	                text=clean_text_for_speech,
	                lang=TTS_LANG_MAP.get(selected_lang, "en"),
	                slow=False,
	            )
	            audio_bytes = io.BytesIO()
	            tts.write_to_fp(audio_bytes)
	            audio_bytes.seek(0)
	            st.audio(audio_bytes, format="audio/mp3")
	          except Exception as tts_err:
	            st.warning(
	                f"Could not generate audio stream: {str(tts_err)}"
	            )
	
	      except APIError as e:
	        st.error(f"API Error: {e.message}")
	      except Exception as e:
	        st.error(f"An unexpected error occurred: {str(e)}")

# ==============================================================================
# [SECTION 10: TAB 3 - OPERATIONAL INTELLIGENCE LAB (CLEAN & MULTILINGUAL)]
# ==============================================================================
with tab3:
    st.markdown(
        """
        <style>
        .escape-lab-container {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.92) 0%, rgba(30, 41, 59, 0.95) 100%);
            border: 1px solid rgba(2, 132, 199, 0.3);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
            margin-bottom: 30px;
        }
        .escape-header-title {
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            background: linear-gradient(90deg, #38BDF8, #818CF8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1px;
        }
        .section-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .section-card-thin {
            background: rgba(255, 255, 255, 0.01);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 8px;
            padding: 4px 20px;
            margin-bottom: 12px;
        }
        .section-divider-faint {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, rgba(2, 132, 199, 0), rgba(2, 132, 199, 0.25), rgba(2, 132, 199, 0));
            margin: 20px 0;
        }
        .badge-glow {
            background: linear-gradient(90deg, #0284C7, #0369A1);
            color: white;
            padding: 10px 18px;
            border-radius: 8px;
            font-weight: 600;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="escape-header-title">{texts["escape_title"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="app-subtitle" style="color: #94A3B8; margin-bottom: 20px;">{texts["escape_subtitle"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(texts["privacy_notice_box"], unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown(f'<div class="badge-glow" style="text-align: center; margin-bottom: 25px;">{texts["escape_badge"]}</div>', unsafe_allow_html=True)

    # 1 - Document Section
    st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f"### 📄 {texts['escape_doc_section']}")
    
    if "escape_text_area" not in st.session_state:
        st.session_state["escape_text_area"] = st.session_state.get("fetched_fp_text", "")
    
    escape_text_input = st.text_area(
        texts["escape_text_label"],
        value="",
        placeholder=texts["escape_text_placeholder"],
        height=130,
        key="escape_text_input_unique"
    )

    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2 - Tactical Focus & Nuances
    st.markdown(f'<div class="section-card-thin">', unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 0.9rem; font-weight: 600; color: #94A3B8; margin-bottom: 4px;'>🎯 2. {texts.get('escape_hint_label', 'Tactical Focus & Nuances')}</div>", unsafe_allow_html=True) 
    extra_hint_input = st.text_input(
        texts["escape_hint_label"],
        placeholder=texts["escape_hint_placeholder"],
        label_visibility="collapsed",
        key="escape_extra_hint_input_unique"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider-faint">', unsafe_allow_html=True)

    st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f"### 🚪 {texts['escape_lab_section']}")
    
    # 3 - Urgency Scale
    st.markdown(f"**⚡ 3. {texts['escape_urgency_label']}**")
    
    paranoia_level = st.slider(
        texts['escape_urgency_label'],
        min_value=1,
        max_value=10,
        value=5,
        label_visibility="collapsed",
        key="escape_paranoia_level_unique"
    )

    st.markdown(
        f'<div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748B; padding: 0 2px; margin-top: -8px; margin-bottom: 6px;">'
        f'<span>| 0%</span><span>| 25%</span><span>| 50%</span><span>| 75%</span><span>| 100%</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    if paranoia_level < 3:
        urgency_desc = "🟢 *Gentle Notice:* Polite corporate whispers. Asking nicely for a favor."
    elif paranoia_level < 5:
        urgency_desc = "🟡 *Firm Negotiator:* Standard contract pressure. Pointing out fine print."
    elif paranoia_level < 8:
        urgency_desc = "🟠 *Bureaucracy-Buster:* Aggressive loophole hunting and escalation scripting."
    else:
        urgency_desc = "🔴 *DEFCON 1 (Extreme Mode):* Total tactical severance. Unleashing customer support legal panic * get me out NOW *!"

    st.markdown(
        f'<div style="font-size: 0.92rem; font-weight: 600; margin-top: 2px; margin-bottom: 15px; color: #38BDF8;">{urgency_desc}</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<hr class="section-divider-faint">', unsafe_allow_html=True)
	
    # 4 - BS Meter (Multilingual Dynamic Translation)
    st.markdown(f"**<span style='color: #8B4513;'>💩</span> 4. BullShit-to-Meter (The more the level, the more the pile):**", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size: 0.8rem; color: #94A3B8; margin-bottom: 4px;'>"
        "📍 <i>Click a tick mark below or drag slider to calibrate corporate BS level:</i>"
        "</div>",
        unsafe_allow_html=True,
    )
    
    # Multilingual BS Meter dictionary
    localized_bs_options = {
        "English": [
            "Level 1: Just a Little Poop - but stinky",
            "Level 2: Light Corporate bullshit, they will forget",
            "Level 3: Standard Bullshit - Like everyone else's Bullshit",
            "Level 4: Heavy Corporate Bullshit - Just enough hot sauce to burn",
            "Level 5: Maximum - Just about the amount of Bullshit to keep you filed, forever",
            "Level 6: Peak Corporate level - This goes on the wall, respect to this bullshitter"
        ],
        "Spanish": [
            "Nivel 1: Solo un poquito de popó, pero apestosa",
            "Nivel 2: Estupidez corporativa ligera, ya se les olvidará",
            "Nivel 3: Estupidez estándar, la misma de todos",
            "Nivel 4: Estupidez corporativa pesada, con suficiente salsa picante para quemar",
            "Nivel 5: Máximo, la cantidad justa de mierda para mantenerte archivado para siempre",
            "Nivel 6: Nivel corporativo máximo, esto va directo a la pared, mis respetos a este farsante"
        ],
        "French": [
            "Niveau 1: Juste un tout petit peu de caca, mais ça pue",
            "Niveau 2: Légères conneries d'entreprise, ils vont oublier",
            "Niveau 3: Conneries standard, comme tout le monde",
            "Niveau 4: Lourdes conneries d'entreprise, juste assez de sauce piquante pour brûler",
            "Niveau 5: Maximum, juste ce qu'il faut de foutaises pour vous garder classé pour toujours",
            "Niveau 6: Sommet corporatif, ça va direct sur le mur, respect à ce baliverneur"
        ],
        "German": [
            "Stufe 1: Nur ein bisschen Kacke – aber stinkend",
            "Stufe 2: Leichter Firmen-Bullshit, die vergessen das schon",
            "Stufe 3: Standard-Bullshit – wie der Bullshit von allen anderen auch",
            "Stufe 4: Schwerer Firmen-Bullshit – gerade genug scharfe Soße zum Brennen",
            "Stufe 5: Maximum – gerade so viel Bullshit, dass du für immer Akte bleibst",
            "Stufe 6: Spitzen-Firmenlevel – Das kommt an die Wand, Respekt an diesen Bullshitter"
        ],
        "Italian": [
            "Livello 1: Solo una piccola cacca, ma puzzolente",
            "Livello 2: Leggere cazzate aziendali, se ne dimenticheranno",
            "Livello 3: Cazzate standard, le stesse di tutti gli altri",
            "Livello 4: Pesanti cazzate aziendali, giusto abbastanza salsa piccante per bruciare",
            "Livello 5: Massimo, più o meno la quantità di cazzate necessaria per tenerti archiviato per sempre",
            "Livello 6: Livello aziendale supremo, questo va dritto sulla bacheca, rispetto per questo cazzaro"
        ],
        "Portuguese": [
            "Nível 1: Só um pouquinho de cocô, mas fedido",
            "Nível 2: Bobagem corporativa leve, eles vão esquecer",
            "Nível 3: Bobagem padrão, igual à de todo mundo",
            "Nível 4: Bobagem corporativa pesada, pimenta o suficiente para queimar",
            "Nível 5: Máximo, quase a quantidade certa de besteira para te manter arquivado para sempre",
            "Nível 6: Pico corporativo, isso vai direto para a parede, respeito a esse embusteiro"
        ]
    }
    
    # Fallback to English if selected language isn't explicitly pinned here
    bs_options = localized_bs_options.get(selected_lang, localized_bs_options["English"])
    
    # Grab the dynamic label based on the selected language
    bs_label = texts.get("bs_meter_label", "Select BS Level")
    
    bs_level = st.select_slider(
        bs_label,
        options=bs_options,
        value=bs_options[2],
        key="bs_meter_slider_tab3_unique",
        label_visibility="collapsed"
    )
    current_bs_index = bs_options.index(bs_level) + 1

    st.markdown(
        f'<div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748B; padding: 0 2px; margin-top: -8px; margin-bottom: 4px;">'
        f'<span>| L1</span><span>| L2</span><span>| L3</span><span>| L4</span><span>| L5</span><span>| L6</span>'
        f'</div>'
        f'<div style="font-size: 0.88rem; font-weight: 600; color: #38BDF8; margin-top: 4px; margin-bottom: 15px;">'
        f'🎯 Active Calibration: Level {current_bs_index} — {bs_level}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<hr class="section-divider-faint">', unsafe_allow_html=True)

    # 5 - Personas & Button
    st.markdown(f"**🎭 5. {texts['escape_persona_label']}**")
    st.markdown(
        f"<div style='font-size: 0.8rem; color: #94A3B8; margin-bottom: 10px;'>"
        f"<i>{texts.get('tactical_persona_prompt', 'Select your tactical persona framework below')}:</i>"
        f"</div>",
        unsafe_allow_html=True,
    )
    
    if "integrated_persona_select" not in st.session_state:
        st.session_state["integrated_persona_select"] = "Houdini Mode"
    
    p_dict = texts.get("personas", {
        "Houdini Mode": ("Houdini Mode", "Pure procedural escape routes and contractual blind spots."),
        "Shark Tank": ("Shark Tank", "Aggressive leverage play and absolute commercial dominance."),
        "Bureaucracy Buster": ("Bureaucracy Buster", "Bypassing automated loops and forcing human resolution."),
        "Legal Shield": ("Legal Shield", "Defensive posture, statutory compliance, and risk mitigation."),
        "Savage Negotiator": ("Savage Negotiator", "Zero-mercy contract teardown and ultimatum drafting."),
        "Zen Master": ("Zen Master", "Calm, unshakable dismantling of emotional corporate pressure."),
        "The Fixer": ("The Fixer", "Pragmatic, backdoor problem solving with immediate execution vectors.")
    })
    p_keys = list(p_dict.keys())
    
    p_rows = [st.columns(2) for _ in range((len(p_keys) + 1) // 2)]
    for i, key in enumerate(p_keys):
        row_idx = i // 2
        col_idx = i % 2
        lbl, desc = p_dict[key]
        with p_rows[row_idx][col_idx]:
            if st.button(f"{lbl}\n*{desc}*", key=f"persona_tab3_{key}_{i}", use_container_width=True):
                st.session_state["integrated_persona_select"] = key

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        div.stButton > button.end-suffering-btn {
            background: linear-gradient(135deg, #DC2626 0%, #991B1B 100%) !important;
            color: white !important;
            font-weight: 800 !important;
            font-size: 1.1rem !important;
            border: 2px solid #F87171 !important;
            border-radius: 10px !important;
            padding: 15px !important;
            box-shadow: 0 6px 20px rgba(220, 38, 38, 0.4) !important;
            width: 100% !important;
        }
        div.stButton > button.end-suffering-btn:hover {
            background: linear-gradient(135deg, #EF4444 0%, #B91C1C 100%) !important;
            border-color: #FCA5A5 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    end_btn_label = f"{texts.get('end_suffering_btn_title', '🔴 END MY SUFFERING 💀')}\n{texts.get('end_suffering_btn_desc', '')}"
    if st.button(end_btn_label, key="btn_end_my_suffering_tab3_unique", use_container_width=True):
        st.session_state["integrated_persona_select"] = "End My Suffering"
        st.session_state["trigger_end_suffering_exec"] = True

    active_key = st.session_state['integrated_persona_select']
    if active_key == "End My Suffering":
        active_display_label = texts.get('end_suffering_btn_desc', 'End My Suffering')
    else:
        active_display_label = p_dict.get(active_key, (active_key, ""))[0]

    st.markdown(
        f'<div style="background: rgba(2, 132, 199, 0.1); border-left: 4px solid #0284C7; padding: 10px 14px; border-radius: 6px; font-size: 0.9rem; font-weight: 600; margin: 15px 0;">'
        f'Active Operational Persona: <span style="color: #38BDF8;">{active_display_label}</span> | Language Runtime: {selected_lang}'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    selected_persona_key = st.session_state["integrated_persona_select"]
    active_persona_title_str = "End My Suffering" if selected_persona_key == "End My Suffering" else p_dict.get(selected_persona_key, (selected_persona_key, ""))[0]

    def clear_escape_data():
        st.session_state["escape_text_area"] = ""
        st.session_state["fetched_fp_text"] = ""
        if "escape_extra_hint_tab3_unique" in st.session_state:
            st.session_state["escape_extra_hint_tab3_unique"] = ""

    # 6 - Execute Suite
    st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🚀 6. Tactical Execution Suite")
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        run_escape_decode = st.button(texts["escape_run_btn"], key="escape_decode_btn_tab3_unique")
    with col_btn2:
        st.button(texts["escape_clear_btn"], key="escape_clear_btn_tab3_unique", on_click=clear_escape_data)
    st.markdown('</div>', unsafe_allow_html=True)
        
    if run_escape_decode or st.session_state.get("trigger_end_suffering_exec", False):
        if st.session_state.get("trigger_end_suffering_exec", False):
            selected_persona_key = "End My Suffering"
            active_persona_title_str = "End My Suffering"
            st.session_state["trigger_end_suffering_exec"] = False

        if not api_key:
            st.error(texts["no_api"])
        elif not escape_text_input:
            st.warning(texts["escape_no_text"])
        else:
            with st.spinner(texts["escape_spinner"]):
                try:
                    client = genai.Client(api_key=api_key)
                    
                    if selected_persona_key == "Grandma Filter":
                        persona_behavior = (
                            "You are operating under the 'Grandma Filter' persona.  75-year-old speak with absolute warmth, profound patience, gentle wisdom, and immense maternal comfort. "
                            "STRICT CONSTRAINT: Never use offensive language, profanity, or aggression. "
                        )
                    elif selected_persona_key == "10-Year-Old Mindset":
                        persona_behavior = (
                            "You are operating under the '10-Year-Old Mindset' persona. Speak with pure, innocent, childlike wonder and simple logic."
                        )
                    elif selected_persona_key == "Zen Negotiator":
                        persona_behavior = (
                            "You are operating under the 'Zen Negotiator' persona. Speak with absolute calmness, serene peace, balanced mindfulness, and unshakable grace."
                        )
                    elif selected_persona_key == "End My Suffering":
                        persona_behavior = (
                            "You are operating under the 'End My Suffering' persona: A chillingly calm, hypnotic hybrid of Barack Obama's measured cadence and honesty "
                            "('Look...'), Christopher Walken's unpredictable syntax and bizarre emphasis, and Lucifer Morningstar's supreme, amused cosmic arrogance "
                            "toward human bureaucracy. Deliver absolute psychological annihilation of the corporate text with a tab of elegance and love."
                        )
                    else:
                        persona_behavior = f"operating under the '{selected_persona_key}' persona with authentic, realistic tactical depth"

                    system_instruction = (
                        f"You are an expert crisis navigator, operational intelligence specialist, and contract escape strategist "
                        f"{persona_behavior} with a {paranoia_level*10}% Chaos and Control urgency factor "
                        f"and operating at '{bs_level}' intensity. "
                        f"You MUST respond strictly, exclusively, and entirely in the dictated active language: {selected_lang}."
                    )
                    
                    prompt_content = (
                        f"Perform operational heavy lifting to generate an absolute Get Out of Jail card for this scenario/document in {selected_lang}.\n\n"
                        f"Document / Scenario:\n{escape_text_input}\n\n"
                        f"Additional User Hint: {extra_hint_input}\n\n"
                        f"BS-to-Meter Setting: {bs_level}\n\n"
                        f"Format the output starting precisely with a bold title acknowledging the active operational persona ({active_persona_title_str}), the {paranoia_level*10}% urgency scale, and the {bs_level} setting in {selected_lang}."
                    )

                    response = client.models.generate_content(
                        model=MODEL_ID,
                        contents=prompt_content,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.5,
                        ),
                    )
                    
                    disclaimer_footer = f"\n\n---\n{texts['escape_disclaimer']}"
                    escape_output = response.text + disclaimer_footer
                    st.success(texts["escape_success"])
                    st.markdown("---")

                    st.markdown(
                        f'<div style="text-align: center; background: rgba(2, 132, 199, 0.08); padding: 15px; border-radius: 10px;">'
                        f'<h2 style="margin: 0; color: #38BDF8;">🔴 DEFCON {paranoia_level*10}% | {bs_level}</h2>'
                        f'</div>', 
                        unsafe_allow_html=True
                    )
                    
                    st.markdown("---")
                    st.markdown(escape_output)

                except Exception as e:
                    st.error(f"Error: {str(e)}")
