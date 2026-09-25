
---

# 🎬 Movie Recommendation System

A simple **content-based movie recommendation system** built with Python, Pandas, and Scikit-learn.  
It suggests movies similar to a user’s favorite by analyzing features such as **genres, keywords, tagline, cast, and director**.

---

## 📌 Features
- Preprocesses movie metadata (`movies.csv`)
- Combines multiple features into a single text representation
- Uses **TF-IDF Vectorization** to convert text into numerical vectors
- Computes **cosine similarity** between movies
- Suggests the **top 30 most similar movies** to the user’s input

---

## 🛠️ Tech Stack
- **Python 3.x**
- **NumPy**
- **Pandas**
- **Scikit-learn** (`TfidfVectorizer`, `cosine_similarity`)
- **Difflib** (for fuzzy matching of movie titles)

---

## 📂 Project Structure
```
Movie-Recommendation/
│
├── movies.csv                     # Dataset containing movie metadata
├── Movie recommendation system.ipynb   # Jupyter Notebook version
├── Movie recommendation system.py      # Python script version
└── README.md                      # Project documentation
```

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/Ighayin1/Movie-Recommendation.git
cd Movie-Recommendation
pip install -r requirements.txt
```

> Create a `requirements.txt` file with:
```text
numpy
pandas
scikit-learn
```

---

## 🚀 Usage
### Option 1: Run Jupyter Notebook
```bash
jupyter notebook "Movie recommendation system.ipynb"
```

### Option 2: Run Python Script
```bash
python "Movie recommendation system.py"
```

You’ll be prompted to enter your favorite movie name:
```
Enter your favourite movie name: Avatar
```

Output:
```
Movies suggested for you:

1. Avatar
2. Guardians of the Galaxy
3. Star Trek
...
30. The Matrix
```

---

## 📊 How It Works
1. **Data Preprocessing**  
   - Fill missing values with empty strings  
   - Combine selected features into one text column  

2. **Feature Extraction**  
   - Apply TF-IDF Vectorization to convert text into numerical vectors  

3. **Similarity Calculation**  
   - Compute cosine similarity between all movies  

4. **Recommendation**  
   - Find the closest match to the user’s input  
   - Sort movies by similarity score  
   - Display the top 30 recommendations  

---

## 📝 Future Improvements
- Add collaborative filtering (user-based recommendations)
- Integrate with a web app (Flask/Django/Streamlit)
- Use a larger dataset (e.g., TMDB API)

---

## 👨‍💻 Author
Developed by **Osayi**  
GitHub: [Ighayin1](https://github.com/Ighayin1)

---
