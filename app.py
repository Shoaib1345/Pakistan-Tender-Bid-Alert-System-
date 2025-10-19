import requests
import hashlib
import os
import time

# -------------------------------
# CONFIGURATION
# -------------------------------
CHECK_INTERVAL = 60 * 60 * 6  # Check every 6 hours
OUTPUT_DIR = 'tender_alerts'

# Optional: Email setup (disabled by default)
SEND_EMAIL = False
EMAIL_FROM = 'shoaibahmedprogramming@gmail.com'
EMAIL_TO = 'your_email@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_PASSWORD = 'YOUR_APP_PASSWORD'

# -------------------------------
# DEPARTMENTS (Dictionary)
# -------------------------------
DEPARTMENTS = {
    "Sukkur Municipal Corporation": "https://sukkur.gos.pk/tenders",
    "Sindh Irrigation Department": "https://irrigation.sindh.gov.pk/tenders",
    "Works & Services Department": "https://works.sindh.gov.pk/tenders",
    "Sindh Education Works": "https://educationworks.sindh.gov.pk/tenders",
    "Public Health Engineering": "https://phe.sindh.gov.pk/tenders",
    "Local Government Department": "https://lgsindh.gov.pk/tenders",
    "Sukkur Development Authority": "https://sda.gos.pk/tenders"
}

# -------------------------------
# UTILITIES
# -------------------------------

def hash_content(content: str) -> str:
    """Generate a hash for webpage content."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def fetch_page(url: str) -> str:
    """Fetch HTML content safely."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return ""

def save_snapshot(name: str, html_content: str):
    """Save HTML snapshot of tender page."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    filename = os.path.join(OUTPUT_DIR, f"{name}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

def send_email_alert(subject: str, body: str):
    """Send an email alert (optional)."""
    if not SEND_EMAIL:
        return
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print(f"[INFO] Email sent: {subject}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

# -------------------------------
# MAIN LOGIC
# -------------------------------

def check_tender_updates():
    """Check all tender URLs for updates."""
    for dept_name, url in DEPARTMENTS.items():
        safe_name = dept_name.replace('/', '-')
        print(f"[INFO] Checking {dept_name} -> {url}")

        html_content = fetch_page(url)
        if not html_content:
            continue

        new_hash = hash_content(html_content)
        snapshot_path = os.path.join(OUTPUT_DIR, f"{safe_name}.hash")

        old_hash = None
        if os.path.exists(snapshot_path):
            with open(snapshot_path, "r") as f:
                old_hash = f.read().strip()

        # Detect changes
        if new_hash != old_hash:
            print(f"[ALERT] New tender detected for {dept_name}!")
            save_snapshot(safe_name, html_content)
            with open(snapshot_path, "w") as f:
                f.write(new_hash)
            send_email_alert(
                subject=f"New Tender Alert: {dept_name}",
                body=f"A new tender was detected at {url}"
            )
        else:
            print(f"[INFO] No new updates for {dept_name}.")

# -------------------------------
# RUN LOOP
# -------------------------------

def main():
    print(f"[INFO] Loaded {len(DEPARTMENTS)} departments.")
    while True:
        print(f"[INFO] Checking all tender pages...")
        check_tender_updates()
        print(f"[INFO] Sleeping for {CHECK_INTERVAL / 3600} hours...\n")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
