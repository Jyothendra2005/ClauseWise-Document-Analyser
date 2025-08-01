import streamlit as st
import requests

st.set_page_config(page_title="Legal Doc Intelligence")
st.title("Legal Document Intelligence")

uploaded = st.file_uploader("Upload legal document (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

if uploaded:
    files = {"file": (uploaded.name, uploaded.getvalue())}
    try:
        resp = requests.post("http://localhost:8000/upload/", files=files, timeout=10)
        if resp.ok:
            text = resp.json().get("text", "")
            st.subheader("Extracted Text")
            st.text_area("Document text", text, height=300)
            if st.button("Simplify Clauses"):
                simplify_resp = requests.post("http://localhost:8000/simplify/", json={"text": text})
                if simplify_resp.ok:
                    st.subheader("Simplified Clauses")
                    st.write(simplify_resp.json().get("simplified_clauses", []))
        else:
            st.error(f"Upload failed: {resp.text}")
    except Exception as e:
        st.error(f"Error contacting backend: {e}")

question = st.text_input("Ask across documents")
if question and st.button("Ask"):
    qresp = requests.post("http://localhost:8000/query/", json={"question": question})
    if qresp.ok:
        st.subheader("Answer")
        st.write(qresp.json().get("answer"))
    else:
        st.error("Query failed")
