import streamlit as st
import hashlib
import base64

PASSWORD_HASH = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

MENSAJE_CIFRADO = "wqFGZWxpY2lkYWRlcyEgSGFzIGRlc2Jsb3F1ZWFkbyBlbCBtZW5zYWplIHNlY3JldG8u"

def check_password(input_pass):
    input_hash = hashlib.sha256(input_pass.strip().encode()).hexdigest()
    return input_hash == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Acceso Privado", page_icon="🔒")
    st.title("📂 Archivo Confidencial")
    
    password_input = st.text_input("Introduce el código de seguridad", type="password")

    if st.button("Desbloquear"):
        if check_password(password_input):
            st.success("Acceso concedido")
            mensaje_decodificado = base64.b64decode(MENSAJE_CIFRADO).decode("utf-8")
            st.balloons()
            st.markdown("### 💌 Mensaje Recuperado:")
            st.info(mensaje_decodificado)
        else:
            st.error("Código incorrecto. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
