# Global Well-Being: Human Development Index (HDI) Predictor

An end-to-end Machine Learning web application designed to evaluate and predict regional well-being scores using the United Nations Human Development Index metrics.

---

## 📌 Project Overview
This repository features a complete data science pipeline consisting of exploratory data analysis, machine learning model training on historical socioeconomic indicators, and a production-ready Flask web deployment. Users can input specific country statistics via an intuitive web interface to instantly compute dynamic HDI value predictions.

The evaluation relies on four critical pillars of global development:
* **Health:** Life Expectancy at Birth (Years)
* **Education (Expected):** Expected Years of Schooling (Years)
* **Education (Mean):** Mean Years of Schooling (Years)
* **Command over Resources:** Gross National Income (GNI) Per Capita

---

🛠 Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* HTML
* CSS
* Bootstrap 5

📊 Machine Learning Models

* Linear Regression
* Random Forest Regressor ✅ (Best Model)
* Decision Tree Regressor
* K-Nearest Neighbors Regressor

📈 Model Performance

| Model | Accuracy / R² Score | Status |
| :--- | :---: | :--- |
| **Random Forest** | **94.50%** | **✅ Selected Best Model** |
| K-Nearest Neighbors | 91.20% | Alternate Model |
| Linear Regression | 88.70% | Alternate Model |
| Decision Tree | 85.40% | Baseline Model |

## 📂 Repository Structure

The project repository is structured cleanly into modular environments:

```text
├── Dataset/
│   └── HDI.csv.csv          # Preprocessed historical development data
├── Training/
│   └── HumDevIndex.ipynb    # Jupyter Notebook detailing EDA, modeling, and evaluation
├── Flask/
│   ├── app.py               # Main Flask server processing inputs & inference
│   ├── HDI.pkl              # Serialized trained machine learning model
│   └── templates/
│       └── index.html       # Dynamic HTML5/CSS3 frontend user interface
├── .gitignore               # Excluded execution caches and system files
└── README.md                # Project documentation


👨‍💻 Developed By

Kalluri Charishma

B.Tech – Computer Science and Engineering (Data Science)

📜 License

This project is developed for educational purposes.
