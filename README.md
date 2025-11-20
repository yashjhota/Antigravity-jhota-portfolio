# 🚀 Yash Jain - Portfolio

A premium, dark-themed personal portfolio website built with **Streamlit** and **Python**. This application showcases my professional experience, projects, skills, and certifications in a sleek, responsive interface.

## ✨ Features

*   **🎨 Premium Dark UI**: A custom-styled black and gold theme (`#000000` & `#FFD700`) for a modern, professional look.
*   **📱 Responsive Design**: Optimized for all devices with a sticky top navigation bar.
*   **📄 Resume Download**: Integrated button to download my latest resume.
*   **📧 Contact Form**: Fully functional contact form integrated with **Google Sheets** for real-time message storage.
*   **📊 Dynamic Content**: Sections for Experience, Projects, Skills, and Publications.

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/) (Python)
*   **Styling**: Custom CSS (Inter font, Glassmorphism effects)
*   **Database**: Google Sheets (via `gspread` & Google Cloud Service Account)
*   **Deployment**: Streamlit Cloud

## 🚀 Running Locally

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yashjhota/Antigravity-jhota-portfolio.git
    cd Antigravity-jhota-portfolio
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Secrets**:
    Create a file at `.streamlit/secrets.toml` and add your Google Cloud Service Account credentials:
    ```toml
    [gcp_service_account]
    type = "service_account"
    project_id = "your-project-id"
    private_key_id = "your-private-key-id"
    private_key = "-----BEGIN PRIVATE KEY-----\n..."
    client_email = "your-email@project.iam.gserviceaccount.com"
    client_id = "..."
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "..."
    ```

4.  **Run the app**:
    ```bash
    streamlit run app.py
    ```

## ☁️ Deployment

This app is designed to be deployed on **Streamlit Cloud**:

1.  Push your code to GitHub.
2.  Connect your repository on [share.streamlit.io](https://share.streamlit.io/).
3.  Add your `secrets.toml` content to the Streamlit Cloud "Secrets" settings.

## 📬 Contact

*   **Email**: jhotayash@zohomail.in
*   **LinkedIn**: [Yash Jain](https://linkedin.com/in/yashjhota)
*   **GitHub**: [yashjhota](https://github.com/yashjhota)
