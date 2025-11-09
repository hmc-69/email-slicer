import streamlit as st
import matplotlib.pyplot as plt
import re
from datetime import datetime

st.set_page_config(page_title="Email Slicer with Insights", page_icon="📧", layout="centered")

# 🎉 Title
st.title("📧 Email Slicer with Insights")

# 🕓 Greeting based on time
hour = datetime.now().hour
if hour < 12:
    greeting = "Good Morning 🌞"
elif hour < 18:
    greeting = "Good Afternoon ☀️"
else:
    greeting = "Good Evening 🌙"
st.subheader(greeting)

# ✉️ Input field
email = st.text_input("Enter your email address:")

# 🔍 When user clicks "Slice Email"
if st.button("Slice Email"):
    pattern = r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z0-9-.]+)$"
    match = re.match(pattern, email)

    if not match:
        st.error("❌ Invalid email format! Please enter a valid email (example: name@gmail.com)")
    else:
        username, domain, extension = match.groups()

        st.success(f"✅ Email processed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.write(f"**Username:** {username.upper()}")
        st.write(f"**Domain:** {domain}")
        st.write(f"**Extension:** {extension}")

        # 🌐 Provider Info
        providers = {
            "gmail": "Google’s email service 🌐",
            "outlook": "Microsoft’s email service 💼",
            "yahoo": "Yahoo Mail ✉️",
            "icloud": "Apple’s email service 🍎",
            "protonmail": "Privacy-focused email 🔒"
        }
        info = providers.get(domain.lower(), "Unknown or custom email provider 🌍")
        st.info(f"**Email Provider:** {info}")

        # 📊 Modern Bar Chart
        lengths = [len(username), len(domain), len(extension)]
        labels = ["Username", "Domain", "Extension"]

        fig, ax = plt.subplots()
        bars = ax.bar(labels, lengths, color=['#0077b6', '#00b4d8', '#90e0ef'])
        ax.set_title("Character Count Comparison", fontsize=13, fontweight='bold')

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.2, str(height),
                    ha='center', va='bottom', fontsize=10)
        st.pyplot(fig)

        # 🧾 Download Report Button
        report = f"""
📧 Email Report
-------------------------
Email: {email}
Username: {username}
Domain: {domain}
Extension: {extension}
Provider Info: {info}
Processed on: {datetime.now().strftime('%A, %d %B %Y, %I:%M %p')}
"""
        st.download_button(
            label="📥 Download Email Report",
            data=report,
            file_name="email_report.txt",
            mime="text/plain"
        )

# ℹ️ Footer
st.caption("Made with ❤️ using Streamlit")
