import streamlit as st
import hashlib
import base64

PASSWORD_HASH = "829557b77a7605e55e56e047434771e35967f0b8655866164f9f783626e27926"

MENSAJE_CIFRADO = "wqFGZWxpY2lkYWRlcyEgSGFzIGRlc2Jsb3F1ZWFkbyBlbCBtZW5zYWplIHNlY3JldG8u"

def check_password(input_pass):
    """Verifica si el hash de la entrada coincide con el guardado."""
    input_hash = hashlib.sha256(input_pass.encode()).hexdigest()
    return input_hash == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Acceso Privado", page_icon="🔒")

    st.title("📂 Archivo Confidencial")
    st.write("Introduce el código de acceso para revelar el contenido.")

    # Input de contraseña
    password_input = st.text_input("Código de seguridad", type="password")

    if st.button("Desbloquear"):
        if check_password(password_input):
            st.success("Acceso concedido")
            
            # Desciframos el mensaje para mostrarlo
            mensaje_decodificado = base64.b64decode(MENSAJE_CIFRADO).decode("utf-8")
            
            st.balloons() # Efecto visual de celebración
            st.markdown(f"### 💌 Mensaje Recuperado:")
            st.info(mensaje_decodificado)
        else:
            st.error("Código incorrecto. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
