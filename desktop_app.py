import os
import sys
import threading
import time
import webview

from app import app


def get_project_folder():
    if getattr(sys, "frozen", False):
        # EXE is inside:
        # project\dist\Smart Attendance\Smart Attendance.exe
        # So go up two folders to reach the project folder.
        return os.path.dirname(
            os.path.dirname(
                os.path.abspath(sys.executable)
            )
        )

    return os.path.dirname(os.path.abspath(__file__))


def run_flask():
    project_folder = get_project_folder()
    os.chdir(project_folder)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )


if __name__ == "__main__":
    flask_thread = threading.Thread(
        target=run_flask,
        daemon=True
    )

    flask_thread.start()

    time.sleep(2)

    webview.create_window(
        "Smart Attendance System",
        "http://127.0.0.1:5000",
        width=1200,
        height=800,
        min_size=(900, 600),
        resizable=True
    )

    webview.start()