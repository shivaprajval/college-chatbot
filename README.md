# 🎓 College FAQ Chatbot

A simple rule-based chatbot that answers common college-related questions such as admission criteria, course offerings, hostel facilities, campus location, and more. The project includes:

- A command-line chatbot using Python.
- A beautiful, full-screen web interface using HTML, CSS, and JavaScript.

---

## 📁 Project Structure

```
📦 project/
├── chatbot.py         # Python CLI-based chatbot
├── index.html         # Full-screen web-based chatbot interface
└── (Optional Flask)   # You can add Flask backend for dynamic integration
```

---

## 💡 Features

- 🎨 Stylish full-screen web interface
- 💬 Rule-based keyword matching (no ML required)
- 🔎 Instant answers to 20+ college FAQs
- 🧠 Covers key topics: admission, fees, courses, location, hostel, events
- 💻 CLI version included for demonstration

---

## ⚙️ Technologies Used

| Component     | Technology Used              |
|---------------|------------------------------|
| Backend (CLI) | Python                       |
| Frontend      | HTML, CSS, JavaScript        |
| Chat Logic    | Rule-based matching (keywords)|
| UI Design     | Flexbox + Gradient CSS       |
| Optional API  | Flask (for future integration) |

---

## 🖥️ How to Run

### ▶️ CLI Version (Python)

1. Make sure you have Python installed.
2. Run the chatbot:
   ```bash
   python chatbot.py
   ```
3. Choose a question number from the displayed menu to get your answer.

---

### 🌐 Web Version (Browser)

1. Open `index.html` in any modern browser.
2. Type your question in the input box.
3. Chatbot will respond instantly based on matched keywords.

---

## ❓ Sample Questions You Can Ask

- What are the admission criteria?
- Where is the campus located?
- What courses are offered?
- What is the fee structure?
- Are hostel accommodations available?
- Do you have industrial visits or trips?
- Tell me about the placement support.
- What are the college timings?
- Is ragging allowed?

---

## 🧩 How It Works

- The chatbot checks if any keyword from the user's input matches those in the predefined FAQ dictionary (`faq_dict`).
- If a match is found, it returns the corresponding answer.
- If not, it returns a fallback message.

---

## 🚀 Future Enhancements (Optional)

- ✅ Integrate Flask backend to connect HTML frontend dynamically.
- ✅ Store FAQs in a JSON file instead of hardcoding.
- ✅ Add voice support or animations.
- ✅ Deploy on GitHub Pages or Render.

---

## 🧑‍💻 Developer

- **Prajval** – College Website Chatbot Project

---

## 📄 License

This project is for academic and demonstration purposes only.
