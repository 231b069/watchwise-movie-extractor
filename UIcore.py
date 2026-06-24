from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser


# ---------------- Pydantic Schema ----------------
class Movie(BaseModel):
    movie_name: str = Field(description="Name of the movie")
    release_year: str = Field(description="Release year of the movie")
    release_date: str = Field(description="Release date of the movie")
    director: str = Field(description="Director of the movie")
    cast: List[str] = Field(description="List of cast members")
    genre: List[str] = Field(description="List of genres")
    runtime: str = Field(description="Runtime of the movie")
    imdb_rating: str = Field(description="IMDb rating of the movie")
    themes: List[str] = Field(description="Themes of the movie")
    language: str = Field(description="Language of the movie")
    country: str = Field(description="Country of the movie")
    short_summary: str = Field(description="Short 2-3 line summary of the movie")
    useful_information: str = Field(description="Useful information about tone, style, emotional impact, strengths, soundtrack, popularity etc.")


parser = PydanticOutputParser(pydantic_object=Movie)


# ---------------- Streamlit Page ----------------
st.set_page_config(page_title="WatchWise", page_icon="🎬", layout="wide")

st.markdown("""
<style>
.title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 8px;
}
.subtitle {
    font-size: 18px;
    text-align: center;
    color: #94a3b8;
    margin-bottom: 25px;
}
.output-box {
    background-color: #111827;
    padding: 18px;
    border-radius: 12px;
    margin-top: 10px;
}
.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎬 WatchWise</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste a movie paragraph and extract movie information using Mistral AI</div>', unsafe_allow_html=True)


# ---------------- Model ----------------
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.2
)


# ---------------- Prompt ----------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert movie information extraction assistant.

Your task is to carefully read the given movie paragraph and extract the most useful information in a clean structured format for a movie recommendation application.

From the paragraph, extract the following fields if available:
- movie_name
- release_year
- release_date
- director
- cast
- genre
- runtime
- imdb_rating
- themes
- language
- country
- short_summary
- useful_information

Rules:
1. Only use information present in the paragraph.
2. Do not invent facts that are not mentioned.
3. If any field is missing, return "Not mentioned".
4. "cast" should be returned as a list of actor names.
5. "genre" should be returned as a list if multiple genres are implied.
6. "themes" should contain important concepts such as love, sacrifice, survival, time, crime, friendship, etc.
7. "short_summary" should be 2-3 lines in simple language.
8. "useful_information" should contain practical details that help a user decide whether to watch the movie, such as tone, style, strengths, emotional impact, visual quality, soundtrack, or why the movie is popular.
9. Return the output in the exact JSON format described below.

{format_instructions}
"""
    ),
    (
        "human",
        """Movie paragraph:
{movie_paragraph}"""
    )
])


# ---------------- Input ----------------
movie_paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Paste your movie paragraph here..."
)


# ---------------- Button Action ----------------
if st.button("Extract Movie Information", use_container_width=True):
    if not movie_paragraph.strip():
        st.warning("Please enter a movie paragraph first.")
    else:
        try:
            final_prompt = prompt.format_messages(
                movie_paragraph=movie_paragraph,
                format_instructions=parser.get_format_instructions()
            )

            response = model.invoke(final_prompt)
            parsed_output = parser.parse(response.content)
            movie_data = parsed_output.model_dump()

            st.success("Movie information extracted successfully!")

            # =========================================================
            # SECTION 1: STRUCTURED OUTPUT
            # =========================================================
            st.markdown('<div class="section-title">📌 Structured Output</div>', unsafe_allow_html=True)

            st.markdown(f"""
<div class="output-box">
<b>Movie Name:</b> {movie_data["movie_name"]}<br><br>
<b>Release Year:</b> {movie_data["release_year"]}<br>
<b>Release Date:</b> {movie_data["release_date"]}<br>
<b>Director:</b> {movie_data["director"]}<br>
<b>Runtime:</b> {movie_data["runtime"]}<br>
<b>IMDb Rating:</b> {movie_data["imdb_rating"]}<br>
<b>Language:</b> {movie_data["language"]}<br>
<b>Country:</b> {movie_data["country"]}<br><br>

<b>Cast:</b> {", ".join(movie_data["cast"])}<br><br>
<b>Genre:</b> {", ".join(movie_data["genre"])}<br><br>
<b>Themes:</b> {", ".join(movie_data["themes"])}<br><br>

<b>Short Summary:</b><br>
{movie_data["short_summary"]}<br><br>

<b>Useful Information:</b><br>
{movie_data["useful_information"]}
</div>
""", unsafe_allow_html=True)

            # =========================================================
            # SECTION 2: JSON OUTPUT
            # =========================================================
            st.markdown('<div class="section-title">🧾 JSON Output</div>', unsafe_allow_html=True)
            st.json(movie_data)

        except Exception as e:
            st.error("Error while calling Mistral API / parsing output")
            st.code(
                str(e))