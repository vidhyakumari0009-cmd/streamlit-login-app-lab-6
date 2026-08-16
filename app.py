import streamlit as st
st.set_page_config(
    page_title="Vulnerability Management System",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #0b1120;
}

h1 {
    color: #00e5ff;
}

h2, h3 {
    color: #38bdf8;
}

.login-box {
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #1e40af;
    background-color: #111827;
}

.status-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #111827;
    border: 1px solid #1e3a5f;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("VULNERABILITY MANAGEMENT SYSTEM")

st.subheader("Security Operations Portal")

st.write(
    "Centralized platform for monitoring, analyzing and managing "
    "security vulnerabilities across organizational assets."
)

st.divider()


# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

st.markdown("### SYSTEM STATUS")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Critical Vulnerabilities", "12", "-3")

with col2:
    st.metric("High Risk", "27", "-5")

with col3:
    st.metric("Assets Monitored", "248", "+12")

with col4:
    st.metric("System Status", "Online", "Stable")


st.divider()


# --------------------------------------------------
# LOGIN SECTION
# --------------------------------------------------

st.markdown("### SECURE LOGIN")

col1, col2 = st.columns(2)

with col1:

    username = st.text_input(
        "Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

with col2:

    role = st.selectbox(
        "Select Role",
        [
            "Security Analyst",
            "Administrator",
            "Security Auditor"
        ]
    )

    security_level = st.selectbox(
        "Security Level",
        [
            "Standard Access",
            "Elevated Access",
            "Restricted Access"
        ]
    )


remember = st.checkbox("Remember this device")


# --------------------------------------------------
# LOGIN BUTTONS
# --------------------------------------------------

col1, col2, col3 = st.columns([2, 2, 2])

with col1:

    if st.button("Login", use_container_width=True):

        if username == "admin" and password == "vms123":

            st.success("Login Successful!")

            st.info(
                f"Welcome {username}! "
                f"Access granted as {role} with {security_level}."
            )

        else:

            st.error(
                "Invalid username or password. "
                "Please verify your credentials."
            )


with col2:

    if st.button(
        "Reset Fields",
        use_container_width=True
    ):
        st.info("Please clear the fields manually.")


with col3:

    if st.button(
        "Forgot Password",
        use_container_width=True
    ):
        st.warning(
            "Contact the system administrator to reset your password."
        )

st.divider()

if st.button("Refresh Status", use_container_width=True):
    st.success("Status refreshed successfully!")



# --------------------------------------------------
# SECURITY INFORMATION
# --------------------------------------------------

st.markdown("### SECURITY INFORMATION")

info1, info2, info3 = st.columns(3)

with info1:
    st.write("ENCRYPTED CONNECTION")
    st.caption(
        "All communication is secured using encryption."
    )

with info2:
    st.write("THREAT MONITORING")
    st.caption(
        "Continuous monitoring of security vulnerabilities."
    )

with info3:
    st.write("RISK ANALYSIS")
    st.caption(
        "Vulnerabilities are categorized based on severity."
    )


st.divider()

st.caption(
    "Vulnerability Management System | Secure Operations Portal"
)
