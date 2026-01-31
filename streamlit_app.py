import streamlit as st
import hashlib
import base64

PASSWORD_HASH = "869e5d7131758252277d337f7690f058145214643034237839368d4a7c065f0e"

MENSAJE_CIFRADO = "SG9sYSBWaWNreS4uLiBRdWVy7WEgZGVjaXJ0ZSBxdWUgZGlzZnJ1dG8gbXVjaO1zaW1vIGNhZGEgbW9tZW50byBxdWUgcGFzYW1vcyBqdW50b3MuIE1lIGVuY2FudGEgdHUgc29ucmlzYSB5IGxvIGJpZW4gcXVlIG1lIGhhY2VzIHNlbnRpci4gVGUgcXVpZXJvIG11Y2hvIHkgbWUgYWxlZ3JhIHF1ZSBzZWFzIHT6IHF1aWVuIGVzdOEgYXF17S4gwqFGZWxpeiBTYW4gVmFsZW507W4h"

def check_password(input_pass):
    input_hash = hashlib.sha256(input_pass.strip().lower().encode()).hexdigest()
    return input_hash == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Para Vicky 🔒", page_icon="❤️")

    st.markdown("""
        <style>
        .main {
            background-color: #fff5f5;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("🌹 Un mensaje especial")
    st.write("Hola, Vicky. Introduce el código que te envié para desbloquear lo que hay aquí guardado.")

    # Input de contraseña
    password_input = st.text_input("Código de acceso", type="password", placeholder="Escribe aquí...")

    if st.button("Revelar Mensaje"):
        if check_password(password_input):
            st.success("Acceso autorizado")
            
            # Descifrado del mensaje
            mensaje_decodificado = base64.b64decode(MENSAJE_CIFRADO).decode("utf-8")
            
            st.balloons()
            
            st.markdown("---")
            st.subheader("💌 De mi para ti:")
            st.info(mensaje_decodificado)
            st.snow()
        else:
            st.error("Ese no es el código... ¡Inténtalo de nuevo! (Pista: es tu nombre y el año actual)")

if __name__ == "__main__":
    main()
