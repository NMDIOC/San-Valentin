import streamlit as st
import hashlib
import base64

# --- CONFIGURACIÓN DE SEGURIDAD (TODO CIFRADO) ---
PASSWORD_HASH = "42a6098e31992128126ded9c5476bd5c2fba61190c0cba734db126bb9696892c"

NAME_B64 = "Vmlja3k="

MSG_B64 = "<BASE64_MESSAGE_AQUI>"

def verify_code(input_str):
    hashed = hashlib.sha256(input_str.strip().encode('utf-8')).hexdigest()
    return hashed == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Acceso Protegido", page_icon="🔐")

    st.title("🔒 Archivo Confidencial")
    st.write("Introduce el código de seguridad para continuar.")

    code_input = st.text_input("Código de acceso:", type="password")
    
    if st.button("Desbloquear"):
        if verify_code(code_input):
            # ÉXITO
            try:
                name = base64.b64decode(NAME_B64).decode('utf-8')
            except Exception:
                name = "Usuario"
            try:
                msg = base64.b64decode(MSG_B64).decode('utf-8')
            except Exception:
                msg = "El mensaje no está disponible (Base64 inválido)."
            
            st.success("Acceso concedido")
            st.balloons()
            
            st.markdown(f"## 🌹 Para: {name}")
            st.markdown("---")
            st.info(msg)
            st.snow()
        else:
            # ERROR PERSONALIZADO
            st.error("revisa el numero debajo del QR")

if __name__ == "__main__":
    main()
