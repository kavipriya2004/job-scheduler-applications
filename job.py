import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QStackedWidget, \
    QTextEdit, QMessageBox, QLineEdit, QGroupBox
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QPieSeries, QPieSlice
from PyQt5.QtCore import pyqtSignal, Qt


class LoginPage(QWidget):
    login_successful = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 300, 150)

        # Set a dark background color for the login page
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(palette)

        overall_heading_label = QLabel("Job Scheduler Application")
        overall_heading_label.setAlignment(Qt.AlignCenter)
        overall_heading_label.setStyleSheet("QLabel { color: black; font-size: 20px; font-weight: bold; }")

        # Create a group box with a dark border for the whole layout
        login_group_box = QGroupBox(self)
        login_group_box.setStyleSheet("QGroupBox { border: 2px solid black; }")

        # Set a brighter background color for the login box
        login_box_palette = login_group_box.palette()
        login_box_palette.setColor(self.backgroundRole(), Qt.lightGray)
        login_group_box.setPalette(login_box_palette)

        # Create a layout for the login box
        login_layout = QVBoxLayout(login_group_box)
        login_layout.setAlignment(Qt.AlignCenter)  # Align the content in the center

        heading_label = QLabel("Job Scheduler with Resource Allocation")
        heading_label.setAlignment(Qt.AlignCenter)
        heading_label.setStyleSheet("QLabel { color: black; font-size: 16px; font-weight: bold; }")

        username_label = QLabel("Username:")
        self.username_edit = QLineEdit()

        password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.check_login)

        login_layout.addWidget(heading_label)
        login_layout.addWidget(username_label)
        login_layout.addWidget(self.username_edit)
        login_layout.addWidget(password_label)
        login_layout.addWidget(self.password_edit)
        login_layout.addWidget(login_button)

        # Set layout for the login group box
        login_group_box.setLayout(login_layout)
        login_group_box.setMaximumSize(400, 240)

        # Set the main layout and adjust the size policy
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(overall_heading_label)
        main_layout.addWidget(login_group_box)
        main_layout.setAlignment(Qt.AlignCenter)  # Align the login box in the center of the main window
        self.setLayout(main_layout)

    def check_login(self):
        # Add your login logic here
        # For simplicity, let's assume a valid username and password
        username = self.username_edit.text()
        password = self.password_edit.text()
        if username == "admin" and password == "password":
            self.login_successful.emit()  # Emit the custom signal on successful login
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")


class Job:
    def __init__(self, name, arrival_time, burst_time, resource_requirements, start_time, finish_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.resource_requirements = resource_requirements
        self.start_time = start_time
        self.finish_time = finish_time


class Resource:
    def __init__(self, material, capacity):
        self.material = material
        self.capacity = capacity


class JobSchedulerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Job Scheduler")
        self.setGeometry(100, 100, 800, 400)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(173, 216, 230))  # Light blue color
        self.setPalette(palette)

        self.jobs = [
            Job("Web Development", 9, 6, 2, 0, 0),
            Job("Data Analysis", 10, 8, 3, 0, 0),
            Job("Graphic Design", 11, 7, 2, 0, 0),
            Job("Database Management", 12, 3, 1, 0, 0),
            Job("Mobile App Development", 13, 5, 2, 0, 0),
            Job("Machine Learning", 14, 10, 4, 0, 0),
            Job("Content Writing", 15, 4, 1, 0, 0),
            Job("Network Administration", 16, 6, 3, 0, 0),
            Job("UI/UX Design", 17, 5, 2, 0, 0),
            Job("System Analyst", 18, 7, 3, 0, 0),
            Job("Cybersecurity Analyst", 19, 8, 4, 0, 0),
            Job("Quality Assurance", 20, 6, 2, 0, 0),
            Job("Data Scientist", 21, 9, 4, 0, 0),
            Job("Mobile Game Development", 22, 7, 3, 0, 0),
            Job("Social Media Management", 23, 5, 2, 0, 0),
            Job("AI Research", 24, 8, 4, 0, 0),
            Job("Frontend Development", 25, 6, 2, 0, 0),
        ]

        self.resources = [
            Resource("Computer", capacity=5),
            Resource("Graphics Tablet", capacity=3),
            Resource("Server", capacity=8),
            Resource("Mobile Device", capacity=2),
            Resource("Data Center", capacity=15),
            Resource("Writing Desk", capacity=4),
            Resource("Router", capacity=5),
            Resource("High-Performance Workstation", capacity=6),
            Resource("Cloud Servers", capacity=10),
            Resource("Testing Devices", capacity=3),
            Resource("3D Printer", capacity=2),
            Resource("AI Server", capacity=6),
            Resource("Content Creation Station", capacity=5),
            Resource("Cybersecurity Software", capacity=5),
            Resource("Augmented Reality Devices", capacity=3),
            Resource("Big Data Server", capacity=10),
            Resource("Quantum Computing Machine", capacity=2),
            Resource("Virtual Reality Lab", capacity=5),
        ]

        self.stacked_widget = QStackedWidget(self)
        self.login_page = LoginPage(self)  # Create an instance of LoginPage

        self.init_ui()

    def init_ui(self):
        self.stacked_widget.addWidget(self.login_page)
        self.create_job_page()
        self.create_resource_page()
        self.create_result_page()

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        self.stacked_widget.setCurrentIndex(0)  # Show the login page initially
        self.login_page.login_successful.connect(self.show_main_application)

    def show_main_application(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to the main application after successful login

    def create_job_page(self):
        job_page = QWidget()
        layout = QVBoxLayout(job_page)

        job_list_label = QLabel("Job List")
        job_listbox = QListWidget()
        job_listbox.setSelectionMode(QListWidget.MultiSelection)
        self.populate_listbox(job_listbox, [job.name for job in self.jobs])

        next_button = QPushButton("Next")
        next_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        layout.addWidget(job_list_label)
        layout.addWidget(job_listbox)
        layout.addWidget(next_button)

        self.stacked_widget.addWidget(job_page)

    def create_resource_page(self):
        resource_page = QWidget()
        layout = QVBoxLayout(resource_page)

        resource_list_label = QLabel("Resource List")
        resource_listbox = QListWidget()
        resource_listbox.setSelectionMode(QListWidget.MultiSelection)
        self.populate_listbox(resource_listbox, [resource.material for resource in self.resources])

        schedule_button = QPushButton("Schedule Jobs")
        schedule_button.clicked.connect(self.schedule_jobs)

        layout.addWidget(resource_list_label)
        layout.addWidget(resource_listbox)
        layout.addWidget(schedule_button)

        self.stacked_widget.addWidget(resource_page)

    def create_result_page(self):
        result_page = QWidget()
        layout = QVBoxLayout(result_page)

        selected_jobs_groupbox = QGroupBox("Selected Jobs")
        selected_jobs_layout = QVBoxLayout(selected_jobs_groupbox)
        self.selected_jobs_text = QTextEdit()
        selected_jobs_layout.addWidget(self.selected_jobs_text)

        selected_resources_groupbox = QGroupBox("Selected Resources")
        selected_resources_layout = QVBoxLayout(selected_resources_groupbox)
        self.selected_resources_text = QTextEdit()
        selected_resources_layout.addWidget(self.selected_resources_text)

        result_groupbox = QGroupBox("Schedule Results")
        result_layout = QVBoxLayout(result_groupbox)
        self.result_text = QTextEdit()
        result_layout.addWidget(self.result_text)

        balance_groupbox = QGroupBox("Balance Overview")
        balance_layout = QVBoxLayout(balance_groupbox)
        self.balance_pie_chart_view = QChartView()
        balance_layout.addWidget(self.balance_pie_chart_view)

        layout.addWidget(selected_jobs_groupbox)
        layout.addWidget(selected_resources_groupbox)
        layout.addWidget(result_groupbox)
        # Commented out the line below to remove the scheduled graph
        # layout.addWidget(graph_groupbox)
        layout.addWidget(balance_groupbox)

        self.stacked_widget.addWidget(result_page)

    def populate_listbox(self, listbox, items):
        listbox.clear()
        listbox.addItems(items)

    def generate_balance_pie_chart(self, available_jobs, available_resources):
        pie_series = QPieSeries()
        pie_series.append("Available Jobs", len(available_jobs))
        pie_series.append("Available Resources", len(available_resources))

        chart = QChart()
        chart.addSeries(pie_series)
        chart.setTitle("Balance Overview")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        self.balance_pie_chart_view.setChart(chart)
        self.balance_pie_chart_view.setRenderHint(QPainter.Antialiasing)

    def schedule_jobs(self):
        selected_jobs = self.get_selected_items(self.stacked_widget.widget(1).findChild(QListWidget))
        selected_resources = self.get_selected_items(self.stacked_widget.widget(2).findChild(QListWidget))

        jobs_to_schedule = [job for job in self.jobs if job.name in selected_jobs]
        resources_to_use = [resource for resource in self.resources if resource.material in selected_resources]

        if not jobs_to_schedule or not resources_to_use:
            self.show_error("Error", "Select at least one job and one resource.")
            return

        available_jobs = [job for job in self.jobs if job not in jobs_to_schedule]
        available_resources = [resource for resource in self.resources if resource not in resources_to_use]

        current_time = 9  # Assuming the workday starts at 9:00 AM
        while jobs_to_schedule:
            available_jobs = [job for job in jobs_to_schedule if job.arrival_time <= current_time]
            available_jobs.sort(key=lambda x: x.burst_time)

            for job in available_jobs:
                for resource in resources_to_use:
                    allocated_job = self.allocate_resources(job, resource, current_time)
                    if allocated_job:
                        job.start_time, job.finish_time = allocated_job.start_time, allocated_job.finish_time
                        jobs_to_schedule.remove(job)
                        resources_to_use.remove(resource)
                        break

            if not available_jobs:
                current_time += 1

        selected_jobs_text = "\n".join(selected_jobs)
        self.selected_jobs_text.setPlainText(selected_jobs_text)

        selected_resources_text = "\n".join(selected_resources)
        self.selected_resources_text.setPlainText(selected_resources_text)

        result_text = self.generate_result_text()
        self.result_text.setPlainText(result_text)

        # Removed the line below to skip generating the graph
        # self.generate_graph(jobs_to_schedule)

        self.generate_balance_pie_chart(available_jobs, available_resources)

        self.stacked_widget.setCurrentIndex(3)

    def generate_result_text(self):
        scheduled_jobs = [job for job in self.jobs if job.start_time != 0]
        header = "{:<20} {:<20} {:<20} {:<20}\n".format("Job", "Start Time", "Finish Time", "Resource")
        rows = [
            "{:<20} {:<20} {:<20} {:<20}".format(job.name, self.format_time(job.start_time),
                                                  self.format_time(job.finish_time), job.resource_requirements)
            for job in scheduled_jobs
        ]
        return header + "\n".join(rows)

    def format_time(self, time):
        return f"{time % 12 or 12}:00 {'AM' if time < 12 else 'PM'}"

    def get_selected_items(self, listbox):
        return [listbox.item(index).text() for index in range(listbox.count()) if listbox.item(index).isSelected()]

    def allocate_resources(self, job, resource, current_time):
        if resource.capacity >= job.resource_requirements:
            start_time = max(job.arrival_time, current_time)
            finish_time = start_time + job.burst_time
            return Job(job.name, job.arrival_time, job.burst_time, job.resource_requirements, start_time, finish_time)
        return None

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)


def main():
    app = QApplication(sys.argv)
    scheduler_app = JobSchedulerApp()
    scheduler_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
