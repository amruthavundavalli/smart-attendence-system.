import streamlit as st
from datetime import date, datetime

from database import (
    init_db,
    get_dashboard_stats,
    get_all_students,
    add_student,
    get_attendance_records,
    mark_attendance,
)

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Attendance System",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# DATABASE
# -------------------------------------------------

init_db()

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    .app-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .app-subtitle {
        color: #6b7280;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .stat-card {
        background: white;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .stat-title {
        color: #6b7280;
        font-size: 15px;
    }

    .stat-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 8px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .welcome-card {
        background: white;
        padding: 28px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <h1 style="font-size:25px;">📋 Smart Attendance</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "MENU",
        [
            "🏠 Dashboard",
            "👨‍🎓 Students",
            "➕ Add Student",
            "📸 Photo Attendance",
            "✅ Attendance",
            "📊 Reports"
        ]
    )

    st.markdown("---")

    st.caption("Smart Attendance System")
    st.caption("Python • OpenCV • Streamlit")


# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

if page == "🏠 Dashboard":

    stats = get_dashboard_stats()

    st.markdown(
        '<div class="app-title">Smart Attendance System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="app-subtitle">Manage students and attendance easily</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="welcome-card">
            <h2>Welcome 👋</h2>
            <p>
                Use the menu on the left to manage students,
                record attendance and view reports.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">Total Students</div>
                <div class="stat-value">{stats["total_students"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">Present Today</div>
                <div class="stat-value">{stats["present_today"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">Attendance Rate</div>
                <div class="stat-value">{stats["attendance_rate"]}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">Quick Actions</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("➕ Add Student", use_container_width=True):
            st.info("Open 'Add Student' from the left menu.")

    with col2:
        if st.button("📸 Photo Attendance", use_container_width=True):
            st.info("Open 'Photo Attendance' from the left menu.")

    with col3:
        if st.button("📊 View Reports", use_container_width=True):
            st.info("Open 'Reports' from the left menu.")


# -------------------------------------------------
# STUDENTS
# -------------------------------------------------

elif page == "👨‍🎓 Students":

    st.title("👨‍🎓 Students")
    st.write("View all registered students.")

    students = get_all_students()

    if not students:
        st.info("No students found. Add your first student.")
    else:

        for student in students:

            with st.container(border=True):

                col1, col2, col3, col4 = st.columns(
                    [2, 2, 2, 1]
                )

                with col1:
                    st.write("**Name**")
                    st.write(student["name"])

                with col2:
                    st.write("**Roll Number**")
                    st.write(student["roll_number"])

                with col3:
                    st.write("**Department**")
                    st.write(student["department"] or "-")

                with col4:
                    st.write("**ID**")
                    st.write(student["id"])


# -------------------------------------------------
# ADD STUDENT
# -------------------------------------------------

elif page == "➕ Add Student":

    st.title("➕ Add Student")
    st.write("Register a new student.")

    with st.form("add_student_form"):

        name = st.text_input("Student Name")

        roll_number = st.text_input("Roll Number")

        department = st.text_input("Department")

        email = st.text_input("Email")

        submitted = st.form_submit_button(
            "Add Student",
            use_container_width=True
        )

        if submitted:

            if not name or not roll_number:
                st.error("Name and Roll Number are required.")

            else:

                try:

                    add_student(
                        name.strip(),
                        roll_number.strip(),
                        department.strip(),
                        email.strip()
                    )

                    st.success(
                        "Student added successfully!"
                    )

                except Exception:

                    st.error(
                        "This roll number already exists."
                    )


# -------------------------------------------------
# PHOTO ATTENDANCE
# -------------------------------------------------

elif page == "📸 Photo Attendance":

    st.title("📸 Photo Attendance")

    st.write(
        "Capture a photo using your device camera."
    )

    st.warning(
        "Face recognition will be connected to this camera "
        "page after the Streamlit website is set up."
    )

    photo = st.camera_input(
        "Take a photo"
    )

    if photo is not None:

        st.success("Photo captured successfully!")

        st.image(
            photo,
            caption="Captured Photo",
            use_container_width=True
        )

        if st.button(
            "🔍 Recognize Student",
            use_container_width=True
        ):
            st.info(
                "Face recognition module will be connected next."
            )


# -------------------------------------------------
# ATTENDANCE
# -------------------------------------------------

elif page == "✅ Attendance":

    st.title("✅ Attendance")

    st.write(
        "Record attendance manually."
    )

    students = get_all_students()

    if not students:

        st.info(
            "No students available. Add a student first."
        )

    else:

        student_options = {}

        for student in students:

            label = (
                f'{student["name"]} '
                f'({student["roll_number"]})'
            )

            student_options[label] = student["id"]

        selected_student = st.selectbox(
            "Select Student",
            list(student_options.keys())
        )

        if st.button(
            "✅ Mark Attendance",
            use_container_width=True
        ):

            student_id = student_options[
                selected_student
            ]

            success = mark_attendance(
                student_id
            )

            if success:

                st.success(
                    "Attendance recorded successfully!"
                )

            else:

                st.warning(
                    "Attendance already recorded for today."
                )


# -------------------------------------------------
# REPORTS
# -------------------------------------------------

elif page == "📊 Reports":

    st.title("📊 Attendance Reports")

    records = get_attendance_records()

    if not records:

        st.info(
            "No attendance records found."
        )

    else:

        report_data = []

        for record in records:

            report_data.append(
                {
                    "Name": record["name"],
                    "Roll Number": record["roll_number"],
                    "Department": record["department"],
                    "Date": record["date"],
                    "Time": record["time"],
                    "Status": record["status"]
                }
            )

        st.dataframe(
            report_data,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "⬇️ Download Report",
            data="\n".join(
                [
                    ",".join(
                        map(str, row.values())
                    )
                    for row in report_data
                ]
            ),
            file_name="attendance_report.csv",
            mime="text/csv",
            use_container_width=True
        )