import streamlit as st
import hashlib
import base64

# --- CONFIGURACIÓN DE SEGURIDAD ---
PASSWORD_HASH = "42a6098e31992128126ded9c5476bd5c2fba61190c0cba734db126bb9696892c"

NAME_B64 = "VGk="

MSG_B64 = "UXVlcmlhIGRlY2lydGUgcXVlIGRpc2ZydXRvIG11Y2hvIGNhZGEgbW9tZW50byBxdWUgcGFzYW1vcyBqdW50b3MuIE1lIGVuY2FudGEgdHUgc29ucmlzYSB5IGxvIGJpZW4gcXVlIG1lIGhhY2VzIHNlbnRpci4gVGUgcXVpZXJvIG11Y2hvIHkgbWUgYWxlZ3JhIHF1ZSBzZWFzIHR1IHF1aWVuIGVzdGEgYXF1aS4gRmVsaXogU2FuIFZhbGVudGluIQ=="

def verify_code(input_str):
    clean_input = input_str.strip()
    hashed = hashlib.sha256(clean_input.encode('utf-8')).hexdigest()
    return hashed == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Acceso Protegido", page_icon="🔐")

    st.title("🔒 Archivo Confidencial")
    st.write("Introduce el codigo de seguridad para continuar.")

    code_input = st.text_input("Codigo de acceso:", type="password")
    
    if st.button("Desbloquear"):
        if verify_code(code_input):
            try:
                display_name = base64.b64decode(NAME_B64).decode('utf-8', errors='ignore')
                display_msg = base64.b64decode(MSG_B64).decode('utf-8', errors='ignore')
                
                st.success("Acceso concedido")
                st.balloons()
                
                st.markdown(f"## 🌹 Para: {display_name}")
                st.markdown("---")
                st.info(display_msg)
                st.snow()
            except Exception as e:
                st.error("Hubo un error al procesar el mensaje, pero el codigo es correcto.")
        else:
            st.error("revisa el numero debajo del QR")

if __name__ == "__main__":
    main()
