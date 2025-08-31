# 🎬 Movie Recommendation System  

An **AI-powered movie recommender** built using **cosine similarity** and deployed with **Streamlit**.  
This system suggests movies similar to the one a user selects, displaying both **titles** and **posters** fetched from the **TMDB API**.  

---

## 📑 Table of Contents  

- [📖 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [📂 Dataset](#-dataset)  
- [🚀 Installation](#-installation)  
- [⚙️ Setup](#️-setup)  
- [🖥️ Usage](#️-usage)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📌 Requirements](#-requirements)  
- [🏗️ Project Structure](#️-project-structure)  
- [📄 License](#-license)  
- [🤝 Contributing](#-contributing)  
- [🙌 Acknowledgments](#-acknowledgments)  
- [📧 Contact](#-contact)  

---

## 📖 Introduction  

Recommender systems power most of the entertainment industry today — from **Netflix** to **Prime Video**.  
This project implements a **content-based movie recommendation system** that:  

- Takes a movie title as input  
- Finds similar movies using a **cosine similarity matrix**  
- Displays **top 5 recommended movies with posters** (fetched dynamically from the TMDB API)  

---

## ✨ Features  

- 🎥 **Movie Recommendations** → Get top 5 similar movies instantly  
- 🖼️ **Poster Fetching** → Posters fetched dynamically from the **TMDB API**  
- ⚡ **Fast Predictions** → Uses a pre-computed similarity matrix  
- 📊 **Streamlit UI** → Interactive dropdown-based movie selection  

---

## 📂 Dataset  

This project uses both **offline Kaggle data** and the **TMDB API**:  

- **From Kaggle (Training Data):**  
  - [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
  - `tmdb_5000_movies.csv` → Movie metadata (title, genres, keywords, overview, etc.)  
  - `tmdb_5000_credits.csv` → Cast and crew details  

- **Preprocessed Files:**  
  - `movies_dict.pkl` → Cleaned movie metadata  
  - `similarity.pkl` → Pre-computed cosine similarity matrix  

- **From TMDB API (Live Data):**  
  - Fetches **posters** and movie details dynamically via TMDB API  

---

## 🚀 Installation  

Clone the repo and install dependencies:  

```bash
git clone https://github.com/Mohd-Muzammil7052/Movie_Recommendation_System.git
cd Movie-Recommender-System
pip install -r requirements.txt
```

## ⚙️ Setup

1. Place the following files in the project root:
   * movies_dict.pkl
   * similarity.pkl

2. Get an API key from TMDB
   Replace the API key in app.py:
   ```text
   response = requests.get(
    'https://api.themoviedb.org/3/movie/{}?language=en-US&api_key=YOUR_API_KEY'.format(movie_id)
    )
   ```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the Streamlit app in your browser.
2. Select a movie from the dropdown list.
3. Click Recommend.
4.View top 5 similar movies with posters side by side.
---

## 🛠️ Tech Stack

* Python → Core language
* Streamlit → Web UI for chatbot.
- Scikit-learn → Cosine similarity
+ Pandas & NumPy → Data handling
* NLTK → Text preprocessing
* TMDB API → Movie posters & metadata

---

## 📌 Requirements

See [requirements.txt](https://github.com/Mohd-Muzammil7052/Movie_Recommendation_System/blob/main/requirements.txt) for all dependencies:

```text
numpy == 1.24.3
pandas == 2.0.3
ast
nltk
streamlit
scikit-learn
gunicorn
```

---

## 🏗️ Project Structure  

```text
📦 Movie-Recommender-System
 ┣ 📜 README.md                   # Documentation
 ┣ 📜 app.py                      # Streamlit app
 ┣ 📜 movie_recommendation.ipynb  # Notebook for model building
 ┣ 📜 requirements.txt            # Dependencies
 ┣ 📜 tmdb_5000_movies.csv        # Raw dataset (movies metadata from Kaggle)
 ┣ 📜 tmdb_5000_credits.csv       # Raw dataset (cast & crew from Kaggle)
 ┣ 📜 movies_dict.pkl             # Processed movie metadata
 ┣ 📜 similarity.pkl              # Pre-computed similarity matrix

```

## 📄 License  

This project is licensed under the [MIT License](https://opensource.org/license/mit).  
Feel free to use, modify, and distribute it as needed.

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve this project:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 🙌 Acknowledgments  

Special thanks to the amazing open-source tools powering this project:  

- [TMDB API](https://www.themoviedb.org/)
- [Kaggle](https://www.kaggle.com/)
- [Scikit-Learn](https://scikit-learn.org/stable/)  
- [Pandas](https://pandas.pydata.org/)  
- [Numpy](https://numpy.org/)  
- [Streamlit](https://streamlit.io/)  

---

## 📧 Contact  

For queries or collaborations:  

**Mohd Muzammil**  
- [GitHub](https://github.com/Mohd-Muzammil7052)  
- [LinkedIn](https://www.linkedin.com/in/mohd-muzammil-109044290/) 
