# Simple Movie Recommendation Model

&#x20;

A movie recommendation system built using **Streamlit** that suggests similar movies based on a selected movie. The recommendations are powered by a precomputed similarity matrix.

## 🚀 Live Demo

🔗 [**Try the App**](https://simple-movie-recommendation-model.streamlit.app/)

## 📌 Features

- Select a movie from the dropdown.
- Get **top 5 similar movies** as recommendations.
- View **movie posters** for each recommendation.
- Click on movie posters to visit their **TMDB webpage**.
- Interactive **user-friendly UI** built with Streamlit.

## 📂 Project Structure

```
Simple-Movie-Recommendation-Model/
│── app/
│   ├── app.py                # Main application script
│   ├── movies.pkl.gz         # Preprocessed movie dataset
│   ├── similarity.pkl.gz     # Precomputed similarity matrix
│   ├── requirements.txt          # Required Python dependencies
│── README.md                 # Project documentation
```

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/G0zi/Simple-Movie-Recommendation-Model.git
cd Simple-Movie-Recommendation-Model/app
```

### 2️⃣ Install Dependencies

Make sure you have Python installed. Then, run:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

## 📜 Dependencies

The project requires the following Python libraries:

- `streamlit`
- `pandas`
- `numpy`
- `requests`
- `pickle`
- `gzip`

## 🖥 Deployment

The app is deployed using **Streamlit Cloud**. To deploy on your own, follow these steps:

1. Push your code to GitHub.
2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app and connect your GitHub repository.
4. Specify `app/app.py` as the main file.
5. Deploy 🚀

## 📌 Future Enhancements

- Improve recommendation accuracy using deep learning.
- Add user-based filtering.
- Improve UI/UX with additional features.

## 📜 License

This project is licensed under the **MIT License**.

---

💡 *Built with ❤️ by *[*G0zi*](https://github.com/G0zi)* | Powered by *[*TMDB*](https://www.themoviedb.org/)

