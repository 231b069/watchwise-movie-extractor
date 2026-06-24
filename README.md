# 🎬 WatchWise – LLM-Based Movie Information Extraction System

WatchWise is an **LLM-powered movie information extraction application** that converts unstructured movie descriptions into **structured movie metadata**.
Built using **Streamlit**, **LangChain**, **Mistral AI**, and **Pydantic**, the app extracts important movie details such as **title, release year, director, cast, genre, runtime, themes, language, country, summary, and useful watch-related information**.

The application presents the results in **two formats**:

* **Structured Output** – human-readable movie information
* **JSON Output** – machine-readable structured data

---

## 🚀 Features

* Extracts movie information from **natural-language movie paragraphs**
* Generates **structured movie metadata** such as:

  * Movie Name
  * Release Year / Release Date
  * Director
  * Cast
  * Genre
  * Runtime
  * IMDb Rating
  * Themes
  * Language
  * Country
  * Short Summary
  * Useful Information
* Displays output in:

  * **Structured Output View**
  * **JSON Output View**
* Uses **Pydantic-based structured parsing** for reliable schema validation
* Built with a clean **Streamlit UI**

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Mistral AI**
* **Pydantic**
* **python-dotenv**

---

## 📂 Project Structure

```bash
watchwise-movie-extractor/
│── app.py
│── requirements.txt
│── .env.example
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/watchwise-movie-extractor.git
cd watchwise-movie-extractor
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Mistral API key

Create a `.env` file in the project root and add:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📌 Usage

1. Open the app in your browser after running Streamlit.
2. Paste a movie paragraph into the text area.
3. Click **Extract Movie Information**.
4. View the extracted data in:

   * **Structured Output**
   * **JSON Output**

---

## 🧾 Example Input

```text
3 Idiots is a 2009 Indian Hindi-language comedy-drama film directed by Rajkumar Hirani and loosely based on Chetan Bhagat’s novel Five Point Someone. The film stars Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor, Boman Irani, and Omi Vaidya. It follows the journey of three engineering students at an elite college, where they deal with academic pressure, friendship, love, and the search for true success in life. Known for its emotional depth, humor, memorable soundtrack, and strong social message, the film explores themes such as friendship, self-discovery, education, ambition, and societal expectations.
```

---

## 📤 Example Output

### Structured Output

* **Movie Name:** 3 Idiots
* **Release Year:** 2009
* **Director:** Rajkumar Hirani
* **Cast:** Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor, Boman Irani, Omi Vaidya
* **Genre:** Comedy, Drama
* **Themes:** Friendship, Self-discovery, Education, Ambition, Societal Expectations
* **Language:** Hindi
* **Country:** India

### JSON Output

```json
{
  "movie_name": "3 Idiots",
  "release_year": "2009",
  "release_date": "Not mentioned",
  "director": "Rajkumar Hirani",
  "cast": [
    "Aamir Khan",
    "R. Madhavan",
    "Sharman Joshi",
    "Kareena Kapoor",
    "Boman Irani",
    "Omi Vaidya"
  ],
  "genre": [
    "Comedy",
    "Drama"
  ],
  "runtime": "Not mentioned",
  "imdb_rating": "Not mentioned",
  "themes": [
    "Friendship",
    "Self-discovery",
    "Education",
    "Ambition",
    "Societal Expectations"
  ],
  "language": "Hindi",
  "country": "India",
  "short_summary": "The film follows three engineering students navigating academic pressure, friendship, and love at an elite college. They search for true success in life beyond societal expectations.",
  "useful_information": "Known for its emotional depth, humor, and memorable soundtrack. The movie delivers a strong social message about education and ambition."
}
```

---

## 🧠 How It Works

1. The user provides a **movie paragraph** as input.
2. A **LangChain prompt** is sent to **Mistral AI**.
3. The LLM extracts movie details according to a predefined schema.
4. **PydanticOutputParser** validates and structures the response.
5. The app displays:

   * a **human-readable structured output**
   * a **JSON representation** of the extracted information

---

## 📌 Future Improvements

* Add **movie recommendation insights**
* Add **download JSON / export feature**
* Add **history of extracted movies**
* Improve UI with cards and tabs
* Support multiple LLM providers

---
