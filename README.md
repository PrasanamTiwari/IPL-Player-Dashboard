# 🏏 IPL Player Performance Dashboard

> An interactive cricket analytics dashboard built using **Python, Pandas, Plotly, and Streamlit** to analyze IPL player performance from ball-by-ball data (2008–2022).

---

## 📌 Overview

The **IPL Player Performance Dashboard** provides detailed batting and bowling insights for any IPL player.  
It transforms raw ball-by-ball data into meaningful visual analytics and performance trends.

This project demonstrates:

- Data cleaning & transformation
- Statistical computation
- Interactive visualization
- Dashboard development
- Real-world sports analytics use case

---

## 🚀 Key Features

### 🏏 Batting Analysis
- Total Matches Played
- Total Runs
- Batting Average (Runs per Match)
- Strike Rate
- 📈 Runs per Match Interactive Graph
- 🔥 Last 5 Match Performance
- 📊 Batting Form Rating

---

### 🎯 Bowling Analysis
- Total Matches Bowled
- Total Wickets (Accurate dismissal filtering)
- Economy Rate
- 📊 Wickets per Match (Including 0-wicket matches)
- 🔥 Last 5 Bowling Performances
- 📈 Bowling Form Rating

---

## 📊 Interactive Visualizations

All graphs are built using **Plotly**, providing:

- Hover tooltips
- Zoom & pan
- Match-wise performance tracking
- Clean interactive UI

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|----------|
| Python | Core Programming |
| Pandas | Data Processing |
| Plotly | Interactive Graphs |
| Streamlit | Dashboard Framework |
| Git & GitHub | Version Control |

---

## 📁 Project Structure

```
IPL-Player-Dashboard/
│
├── app.py                # Streamlit Dashboard
├── analysis.py           # Data Analysis Logic
├── requirements.txt      # Dependencies
├── .gitignore
├── README.md
```

⚠️ The dataset is excluded from GitHub using `.gitignore` due to large size.

---

## ⚙️ How It Works

1. Ball-by-ball IPL dataset is loaded.
2. Data is filtered player-wise.
3. Aggregations are computed:
   - Runs per match
   - Wickets per match
   - Strike rate
   - Economy
4. Form is calculated based on last 5 performances.
5. Results are displayed using interactive charts.

---

## ▶ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/PrasanamTiwari/IPL-Player-Dashboard.git
```

### 2️⃣ Navigate to Folder

```bash
cd IPL-Player-Dashboard
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run App

```bash
streamlit run app.py
```

---

## 🌍 Deployment

This project can be deployed easily using:

- Streamlit Cloud
- Render
- Railway
- Heroku (if configured)

---

## 📈 Future Enhancements

- Player vs Player Comparison
- Season-wise filtering
- Dot Ball Percentage
- Fantasy Points Calculator
- Powerplay vs Death Overs Analysis
- API-based live data integration

---

## 🧠 Learning Outcomes

Through this project, I strengthened my skills in:

- Data Analysis & Aggregation
- Real-world dataset handling
- Interactive visualization
- Dashboard architecture
- Git & GitHub workflow
- Deployment readiness

---

## 👨‍💻 Author

**Prasanam Tiwari**  
B.Tech CSE Student | Python Developer | Data Analytics Enthusiast  

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork it
- 💡 Suggest improvements

---

## 📬 Connect

Feel free to connect on LinkedIn and discuss data, analytics, or cricket!
