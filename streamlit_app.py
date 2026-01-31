import streamlit as st
import hashlib
import base64

# --- DATOS CIFRADOS ---
PASSWORD_HASH = "869e5d7131758252277d337f7690f058145214643034237839368d4a7c065f0e"

NAME_CIFRADO = "Vmlja3k="

MENSAJE_CIFRADO = "UXVlcmlhIGRlY2lydGUgcXVlIGRpc2ZydXRvIG11Y2jDrXNpbW8gY2FkYSBtb21lbnRvIHF1ZSBwYXNhbW9zIGp1bnRvcy4gTWUgZW5jYWFudGEgdHUgc29ucmlzYSB5IGxvIGJpZW4gcXVlIG1lIGhhY2VzIHNlbnRpci4gVGUgcXVpZXJvIG11Y2hvIHkgbWUgYWxlZ3JhIHF1ZSBzZWFzIHT6IHF1aWVuIGVzdMOhIGFxdcOtLiDCofRlbGl6IFNhbiBWYWxlbnTDrW4h"

def check_password(input_pass):
    return hashlib.sha256(input_pass.strip().lower().encode()).hexdigest() == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Archivo Privado", page_icon="🔒")

    # Estilo visual
    st.markdown("""
        <style>
        .main { background-color: #fffafa; }
        .stButton>button { border-radius: 50px; width: 100%; background-color: #e63946; color: white; }
        </style>
        """, unsafe_allow_html=True)

    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if not st.session_state['authenticated']:
        st.title("🔒 Acceso Restringido")
        st.write("Este contenido ha sido creado para una persona específica. Por favor, identifícate.")
        
        password_input = st.text_input("Introduce el código de seguridad", type="password")
        
        if st.button("Validar Identidad"):
            if check_password(password_input):
                st.session_state['authenticated'] = True
                st.rerun()
            else:
                st.error("Código incorrecto.")
    else:
        nombre_real = base64.b64decode(NAME_CIFRADO).decode("utf-8")
        mensaje_real = base64.b64decode(MENSAJE_CIFRADO).decode("utf-8")
        
        st.balloons()
        st.title(f"🌹 Para ti, {nombre_real}")
        
        st.markdown("---")
        st.subheader("Un mensaje especial:")
        st.info(mensaje_real)
        
        st.snow()
        if st.button("Cerrar sesión"):
            st.session_state['authenticated'] = False
            st.rerun()

if __name__ == "__main__":
    main()
