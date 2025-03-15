# **PubMed Paper Fetcher**

This Python project fetches research papers from **PubMed** based on a user-specified query. It identifies papers with at least one author affiliated with a **pharmaceutical or biotech company** and saves the results as a CSV file.

---

## **🚀 Features**
✅ Fetches research papers from **PubMed API**  
✅ Filters papers with **non-academic authors** (pharma/biotech affiliations)  
✅ Saves results as a **CSV file**  
✅ Supports **command-line interface (CLI)**  
✅ Uses **Poetry** for dependency management  

---

## **📌 Project Structure**
```
pubmed_fetcher/
│── pubmed_fetcher/        # Source code folder
│   ├── __init__.py        # Initializes package
│   ├── api.py             # Fetches and processes PubMed data
│   ├── cli.py             # CLI commands
│── tests/                 # (Optional: For testing)
│── pyproject.toml         # Poetry dependencies & settings
│── README.md              # Documentation
│── .gitignore             # Ignore unnecessary files
```

---

## **📦 Installation**
### **1️⃣ Install Poetry**
Ensure **Poetry** is installed:
```sh
pip install poetry
```

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/pubmed_fetcher.git
cd pubmed_fetcher
```

### **3️⃣ Install Dependencies**
```sh
poetry install
```

---

## **▶️ Usage**
Run the command-line tool to fetch PubMed papers:

```sh
poetry run get-papers-list "biotech" -d -f papers.csv
```

### **CLI Options**
| Option        | Description |
|--------------|------------|
| `-h`, `--help`  | Show usage instructions |
| `-d`, `--debug` | Print debug info |
| `-f`, `--file`  | Save results to a CSV file |

---

## **📊 Example Output (CSV Format)**
| PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|-------|-----------------|-------------------------|-------------------------|---------------------------|
| 12345678 | AI in Biotech | 2024 | John Doe | Biotech Corp | john.doe@biotech.com |

---

## **🛠️ Development & Testing**
### **Run CLI in Debug Mode**
```sh
poetry run get-papers-list "cancer research" -d
```

### **Run Inside Virtual Environment**
```sh
poetry shell
python pubmed_fetcher/cli.py "biotech"
```

---

## **🔧 Tools & Technologies**
- **Python 3.8+**
- **Poetry** (Dependency Management)
- **Requests** (For API Calls)
- **Pandas** (For CSV Processing)
- **Click** (For CLI)

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **👨‍💻 Author**
Developed by **Shreya Prasad**  
🔗 [GitHub](https://github.com/Shreyaprasad21)

---
