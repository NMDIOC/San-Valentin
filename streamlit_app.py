import streamlit as st
import hashlib
import base64

# --- CONFIGURACIÓN DE SEGURIDAD (TODO CIFRADO) ---
PASSWORD_HASH = "42a6098e31992128126ded9c5476bd5c2fba61190c0cba734db126bb9696892c"

NAME_B64 = "Vmlja3k="

MSG_B64 = "SG9sYSBWaWNreS4uLiBRdWVyw61hIGRlY2lydGUgcXVlIGRpc2ZydXRvIG11Y2jDrXNpbW8gY2FkYSBtb21lbnRvIHF1ZSBwYXNhbW9zIGp1bnRvcy4gTWUgZW5jYW50YSB0dSBzb25yaXNhIHkgbG8gYmllbiBxdWUgbWUgaGFjZXMgc2VudGlyLiBUZSBxdWllcm8gbXVjaG8geSBtZSBhbGVncmEgcXVlIHNlYXMgdMO6IHF1aWVuIGVzdMOhIGFxdcOtLiDCoUZlbGl6IFNhbiBWYWxlbnTDrW4h"

def verify_code(input_str):
    # Limpiamos espacios y generamos hash
    hashed = hashlib.sha256(input_str.strip().encode('utf-8')).hexdigest()
    return hashed == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Acceso Protegido", page_icon="🔐")

    # Título en pantalla inicial
    st.title("🔒 Archivo Confidencial")
    st.write("Introduce el código de 6 dígitos para continuar.")

    # Input del código
    code_input = st.text_input("Código de seguridad:", type="password", help="Introduce la fecha acordada")
    
    if st.button("Desbloquear"):
        if verify_code(code_input):
            # ÉXITO
            vicky_name = base64.b64decode(NAME_B64).decode('utf-8')
            vicky_msg = base64.b64decode(MSG_B64).decode('utf-8')
            
            st.success("Acceso concedido")
            st.balloons()
            
            st.markdown(f"## 🌹 Para: {vicky_name}")
            st.markdown("---")
            st.info(vicky_msg)
            st.snow()
        else:
            # ERROR
            st.error("Código incorrecto. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
