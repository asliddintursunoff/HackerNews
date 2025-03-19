# Hacker News Scraper

This is a **Python web scraper** that fetches the top stories from [Hacker News](https://news.ycombinator.com/) using **BeautifulSoup**. It sorts and displays posts with **more than 100 points**, ranked from highest to lowest.

---

## 📌 Features  
✔️ **Scrapes Hacker News articles** from any page.  
✔️ **Filters stories with more than 100 points.**  
✔️ **Sorts articles by highest votes.**  
✔️ **Displays story titles, links, and points.**  

---

## 🚀 Installation  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/asliddintursunoff/HackerNews.git
cd HackerNews
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**  


### **3️⃣ Install Dependencies**  
```sh
pip install -r requ.txt
```

---

## ⚙️ Usage  

### **Run the Script**  
```sh
python scraper.py
```
Then, enter a page number when prompted.

---

## 📝 Code Breakdown  

- **Requests & BeautifulSoup** fetch and parse the Hacker News page.
- **hn_app()** extracts and filters stories based on votes.
- **sorted_news_by_votes()** sorts stories from highest to lowest points.
- **pprint.pp()** pretty-prints the final results.

---




## 🙌 Contributions  
Feel free to contribute! Fork the repo, make your changes, and submit a **Pull Request**.  

---

