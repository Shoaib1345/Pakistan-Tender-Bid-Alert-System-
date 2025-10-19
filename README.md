# Pakistan-Tender-Bid-Alert-System-

**Sukkur Tender/Bid Alert System**

**Author:** Shoaib Ahmed
**Date:** October 19, 2025
**Location:** Sukkur, Sindh, Pakistan

---

### 🧠 **Project Overview**

The **Sukkur Tender/Bid Alert System** is a Python-based monitoring tool that automatically checks government tender or procurement pages of Sukkur and Sindh departments.
Whenever a tender webpage changes (indicating a new tender or update), the system detects it and alerts you.

It’s designed to:

* ✅ Continuously monitor tender websites
* ✅ Detect new bids or tender postings
* ✅ Save webpage snapshots for reference
* ✅ Optionally send **email notifications**
* ✅ Work without any external CSV file

---

### ⚙️ **How It Works**

1. A dictionary (`DEPARTMENTS`) in `app.py` stores department names and tender URLs.
2. Every few hours (default: **6 hours**), the system:

   * Fetches each webpage
   * Creates a unique hash of its content
   * Compares it to the last saved version
   * Alerts you if the content has changed
3. When changes are detected:

   * A message appears in the console
   * The latest HTML page is saved in the `tender_alerts/` folder
   * (Optional) An email notification can be sent

---

### 🧩 **Technologies Used**

* **Python 3.10+**
* **Libraries:**

  * `requests` → for fetching web pages
  * `hashlib` → for hashing content
  * `os`, `time` → for file and interval handling
  * `smtplib`, `email` → for optional email alerts

---

### 🛠️ **Setup Instructions**

#### 1. Install Python

Make sure you have **Python 3.10+** installed.
Check with:

```bash
python --version
```

#### 2. Install Required Libraries

Run this in your terminal:

```bash
pip install requests
```

#### 3. Download the Script

Save the file as:

```
app.py
```

#### 4. Run the Program

```bash
python app.py
```

You’ll see output like:

```
[INFO] Loaded 7 departments.
[INFO] Checking all tender pages...
[ALERT] New tender detected for Sukkur Municipal Corporation!
[INFO] Sleeping for 6.0 hours...
```

---

### 📂 **Project Structure**

```
Pakistan-Tender-Bid-Alert-System/
│
├── app.py                   # Main Python script
├── README.md                # This documentation file
└── tender_alerts/           # Folder where webpage snapshots are stored
```

---



### ✉️ **Email Notification (Optional)**

If you want to receive email alerts:

1. Enable **2-Step Verification** in your Gmail account.
2. Create an **App Password** in Gmail settings.
3. In `app.py`, edit these lines:

   ```python
   SEND_EMAIL = True
   EMAIL_FROM = 'your_gmail@gmail.com'
   EMAIL_TO = 'recipient_email@gmail.com'
   EMAIL_PASSWORD = 'YOUR_APP_PASSWORD'
   ```
4. The system will now send you emails whenever a tender is updated.

---

### ⏰ **Configuration Options**

| Option           | Description                      | Default                 |
| ---------------- | -------------------------------- | ----------------------- |
| `CHECK_INTERVAL` | Time between checks (in seconds) | `60 * 60 * 6` (6 hours) |
| `OUTPUT_DIR`     | Folder to save webpage snapshots | `'tender_alerts'`       |
| `SEND_EMAIL`     | Enable or disable email alerts   | `False`                 |

---



### 👨‍💻 **Author**

**Shoaib Ahmed**
Artificial Intelligence Student – Aror University, Sukkur
Email: [shoaibahmedprogramming@gmail.com](mailto:shoaibahmedprogramming@gmail.com)
WhatsApp: [0319-8315403]

---

Would you like me to update this `README.md` to include **Telegram alert setup (with bot token and chat ID)** next?

