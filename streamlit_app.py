import streamlit as st
import hashlib
import base64

# --- CONFIGURACIÓN (TODO CIFRADO) ---
HASH_VALOR = "869e5d7131758252277d337f7690f058145214643034237839368d4a7c065f0e"

NOMBRE_B64 = "Vmlja3k="

MSG_B64 = "UXVlcmlhIGRlY2lydGUgcXVlIGRpc2ZydXRvIG11Y2jDrXNpbW8gY2FkYSBtb21lbnRvIHF1ZSBwYXNhbW9zIGp1bnRvcy4gTWUgZW5jYWFudGEgdHUgc29ucmlzYSB5IGxvIGJpZW4gcXVlIG1lIGhhY2VzIHNlbnRpci4gVGUgcXVpZXJvIG11Y2hvIHkgbWUgYWxlZ3JhIHF1ZSBzZWFzIHT6IHF1aWVuIGVzdMOhIGFxdcOtLiDCofRlbGl6IFNhbiBWYWxlbnTDrW4h"

def main():
    st.set_page_config(page_title="Sección Privada", page_icon="🔐")

    # Título principal (Visible antes de entrar)
    st.title("🔒 Archivo Protegido")
    st.write("Introduce el código de seguridad para revelar el contenido.")

    # Input de la contraseña
    entrada = st.text_input("Código de acceso:", type="password")
    boton = st.button("Desbloquear mensaje")

    if boton:
        # 1. Limpiamos la entrada (quitamos espacios y pasamos a minúsculas)
        password_limpia = entrada.strip().lower()
        
        # 2. Generamos el hash de lo que el usuario escribió
        hash_entrada = hashlib.sha256(password_limpia.encode('utf-8')).hexdigest()

        # 3. Comparación
        if hash_entrada == HASH_VALOR:
            nombre = base64.b64decode(NOMBRE_B64).decode('utf-8')
            mensaje = base64.b64decode(MSG_B64).decode('utf-8')
            
            st.balloons()
            st.success("✅ Acceso Concedido")
            st.markdown(f"# 🌹 Para: {nombre}")
            st.markdown("---")
            st.info(mensaje)
            st.snow()
        else:
            st.error("Código incorrecto.")

if __name__ == "__main__":
    main()
