import streamlit as st
import requests
from pathlib import Path

ASSETS_PATH = Path(__file__).absolute().parents[1]  /"assets"

def layout():
    st.markdown("# Ragbit")
    st.markdown("Ask a question about different dwarf rabbits")
    text_input = st.text_input(label="Ask a question")

    if st.button("Send") and text_input != "":
        response = requests.post(
            "http://127.0.0.1:8000/rag/query", json={"prompt": text_input}
        )

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])

        if data.get("filename") and data["filename"] not in [None, "None", "N/A"]:
            image_path = ASSETS_PATH / f"{data['filename']}.png"
            if image_path.exists():
                st.image(image_path)
            else:
                st.warning(f"Image not found: {data['filename']}.png")


if __name__ == "__main__":
    layout()