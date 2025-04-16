import streamlit as st

st.markdown(
    """
    <style>

    .stApp {
        background-color: rgb(27,47,57);
        color: white;
    }

    button[title="Copy to clipboard"] {
        background-color: red !important;
        color: white !important;
        border: none;
        border-radius: 5px;
        padding: 4px 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("# PASSAGE CUTTER ✂️")
st.markdown("### Paste your passage and cut it into pieces of :blue-background[required word limit] for each piece")
st.markdown("Useful for websites which has input limit like AI-checker, plagarism checker and chatGPT")



genre = st.radio(
    "✨You can seperate your passage into different chunks acc. to required :rainbow[no. of words] or :rainbow[characters] per chunk",
    ["Word Limit", "Character/letter Limit"],
    captions=[
        "Split the text into different chunks acc. to a given word limit for each chunk",
        "Split the text into different chunks acc. to a given character/letter limit for each chunk",
    ],
)


if genre == "Word Limit":

    def split_passage(passage, word_limit):
        words = passage.split()
        passages = []
        current_passage = []

        for word in words:
            current_passage.append(word)
            if len(current_passage) == word_limit:
                passages.append(" ".join(current_passage))
                current_passage = []

        # Add any remaining words as the last passage
        if current_passage:
            passages.append(" ".join(current_passage))

        return passages
    
    input_passage = st.text_area("### ✏️ Enter your original passage")
    word_limit = st.slider("🧮 Words per chunk", 1, 1000, 25)

    if st.button("🚀 Split Now"):
        if input_passage.strip() == "":
            st.warning("Please enter a passage before splitting.")
        else:
            result = split_passage(input_passage, word_limit)
            for i, chunk in enumerate(result, 1):
                st.markdown(f"**Chunk {i}:**")
                st.code(chunk)

else:
    def split_by_characters(passage, char_limit):
        passages = []
        start = 0

        while start < len(passage):
            end = start + char_limit

            # Try not to cut off in the middle of a word
            if end < len(passage) and passage[end] != ' ':
                while end > start and passage[end] != ' ':
                    end -= 1
                if end == start:
                    end = start + char_limit  # just hard cut if no space found

            passages.append(passage[start:end].strip())
            start = end

        return passages
    
    input_passage = st.text_area("### ✏️ Enter your original passage")
    char_limit = st.slider("🧮 Characters per chunk", 1, 1000, 25)

    if st.button("🚀 Split Now"):
        if input_passage.strip() == "":
            st.warning("Please enter a passage before splitting.")
        else:
            result = split_by_characters(input_passage, char_limit)
            for i, chunk in enumerate(result, 1):
                st.markdown(f"**Chunk {i}:**")
                st.code(chunk)


st.markdown("""
    <hr style="margin-top: 50px; border: 0.5px solid #444;" />
    <div style="text-align: center; color: #ccc; padding: 10px 0;">
        Made with ❤️ by <strong>Nitheesh</strong> &nbsp;|&nbsp; 2025
    </div>
""", unsafe_allow_html=True)
