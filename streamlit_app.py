import streamlit as st
import hashlib
import base64

PASSWORD_HASH = "869e5d7131758252277d337f7690f058145214643034237839368d4a7c065f0e"

NAME_B64 = "Vmlja3k="

MSG_B64 = "UXVlcmlhIGRlY2lydGUgcXVlIGRpc2ZydXRvIG11Y2jDrXNpbW8gY2FkYSBtb21lbnRvIHF1ZSBwYXNhbW9zIGp1bnRvcy4gTWUgZW5jYWVudGEgdHUgc29ucmlzYSB5IGxvIGJpZW4gcXVlIG1lIGhhY2VzIHNlbnRpci4gVGUgcXVpZXJvIG11Y2hvIHkgbWUgYWxlZ3JhIHF1ZSBzZWFzIHT6IHF1aWVuIGVzdOEgYXF17S4gwqFGZWxpeiBTYW4gVmFsZW507W4h"

def verify_pass(input_str):
    clean_input = input_str.strip().lower()
    hashed = hashlib.sha256(clean_input.encode('utf-8')).hexdigest()
    return hashed == PASSWORD_HASH

def main():
    st.set_page_config(page_title="Acceso Privado", page_icon="🔒")

    if 'acceso' not in st.session_state:
        st.session_state['acceso'] = False

    if not st.session_state['acceso']:
        st.title("🔒 Archivo Protegido")
        st.subheader("Identifícate para continuar")
        
        clave = st.text_input("Introduce el código secreto:", type="password")
        
        if st.button("Desbloquear"):
            if verify_pass(clave):
                st.session_state['acceso'] = True
                st.rerun()
            else:
                st.error("Código incorrecto. Revisa que no haya espacios de más.")
                st.info("Pista: Es tu nombre y el año actual (todo junto y en minúsculas).")
    
    else:
        nombre = base64.b64decode(NAME_B64).decode('utf-8')
        mensaje = base64.b64decode(MSG_B64).decode('utf-8')
        
        st.balloons()
        st.title(f"🌹 Para: {nombre}")
        st.markdown("---")
        st.info(mensaje)
        st.snow()
        
        if st.button("Cerrar sesión"):
            st.session_state['acceso'] = False
            st.rerun()

if __name__ == "__main__":
    main()
