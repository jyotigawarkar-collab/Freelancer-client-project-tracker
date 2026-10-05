import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector


# ==========================================
# MYSQL CONNECTION
# ==========================================

def connect_database():
    try:
        connection = mysql.connector.connect(
            host="YOUR_HOST",
            port=YOUR_PORT,
            user="YOUR_USER",
            password="YOUR_PASSWORD",
            database="YOUR_DATABASE",
            ssl_disabled=False
        )

        return connection

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            "Unable to connect to MySQL.\n\n" + str(e)
        )
        return None

# ==========================================
# LOGIN FUNCTION
# ==========================================

def login():

    username = username_entry.get().strip()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter username and password."
        )
        return

    connection = connect_database()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
            SELECT * FROM users
            WHERE username = %s AND password = %s
        """

        cursor.execute(
            query,
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            messagebox.showinfo(
                "Login Successful",
                "Welcome to Freelancer Project Tracker!"
            )

            open_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# ==========================================
# CLEAR LOGIN
# ==========================================

def clear_login():

    username_entry.delete(
        0,
        tk.END
    )

    password_entry.delete(
        0,
        tk.END
    )

    username_entry.focus()
# ==========================================
# CLIENT MANAGEMENT
# ==========================================

def open_client_management():

    client_window = tk.Toplevel(login_window)

    client_window.title(
        "Client Management"
    )

    client_window.geometry(
        "550x900"
    )

    client_window.configure(
        bg="#F4F7FB"
    )

    client_window.resizable(
        True,
        True
    )

    # ======================================
    # HEADER
    # ======================================

    header = tk.Frame(
        client_window,
        bg="#243B6B"
    )

    header.pack(
        fill="x"
    )

    title = tk.Label(
        header,
        text="CLIENT MANAGEMENT",
        font=("Arial", 18, "bold"),
        bg="#243B6B",
        fg="white"
    )

    title.pack(
        pady=(15, 3)
    )

    subtitle = tk.Label(
        header,
        text="Manage your client records",
        font=("Arial", 9),
        bg="#243B6B",
        fg="#DCE6FF"
    )

    subtitle.pack(
        pady=(0, 15)
    )

    # ======================================
    # MAIN FRAME
    # ======================================

    main_frame = tk.Frame(
        client_window,
        bg="#F4F7FB"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=12,
        pady=10
    )

    # ======================================
    # FORM CARD
    # ======================================

    form_card = tk.Frame(
        main_frame,
        bg="white"
    )

    form_card.pack(
        fill="x"
    )

    # ======================================
    # FIELD FUNCTION
    # ======================================

    def create_field(label_text):

        label = tk.Label(
            form_card,
            text=label_text,
            font=("Arial", 8, "bold"),
            bg="white",
            fg="#444444"
        )

        label.pack(
            anchor="w",
            padx=12,
            pady=(7, 2)
        )

        entry = tk.Entry(
            form_card,
            font=("Arial", 9),
            bg="#F4F7FB",
            fg="#222222",
            relief="flat",
            bd=0
        )

        entry.pack(
            fill="x",
            padx=12,
            ipady=6
        )

        return entry

    # ======================================
    # CLIENT FIELDS
    # ======================================

    name_entry = create_field(
        "Client Name"
    )

    email_entry = create_field(
        "Email"
    )

    phone_entry = create_field(
        "Phone"
    )

    company_entry = create_field(
        "Company"
    )

    address_entry = create_field(
        "Address"
    )

    # ======================================
    # SELECTED CLIENT
    # ======================================

    selected_client_id = tk.StringVar()

    # ======================================
    # CLEAR FORM
    # ======================================

    def clear_form():

        selected_client_id.set("")

        name_entry.delete(
            0,
            tk.END
        )

        email_entry.delete(
            0,
            tk.END
        )

        phone_entry.delete(
            0,
            tk.END
        )

        company_entry.delete(
            0,
            tk.END
        )

        address_entry.delete(
            0,
            tk.END
        )

        name_entry.focus()

    # ======================================
    # ADD CLIENT
    # ======================================

    def add_client():

        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        company = company_entry.get().strip()
        address = address_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter client name."
            )

            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            query = """
                INSERT INTO clients
                (
                    client_name,
                    email,
                    phone,
                    company,
                    address
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
            """

            cursor.execute(
                query,
                (
                    name,
                    email,
                    phone,
                    company,
                    address
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Client added successfully."
            )

            clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # UPDATE CLIENT
    # ======================================

    def update_client():

        client_id = selected_client_id.get()

        if client_id == "":

            messagebox.showwarning(
                "Select Client",
                "Please select a client from the records."
            )

            return

        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        company = company_entry.get().strip()
        address = address_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter client name."
            )

            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            query = """
                UPDATE clients
                SET
                    client_name = %s,
                    email = %s,
                    phone = %s,
                    company = %s,
                    address = %s
                WHERE client_id = %s
            """

            cursor.execute(
                query,
                (
                    name,
                    email,
                    phone,
                    company,
                    address,
                    client_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Client updated successfully."
            )

            clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # DELETE CLIENT
    # ======================================

    def delete_client():

        client_id = selected_client_id.get()

        if client_id == "":

            messagebox.showwarning(
                "Select Client",
                "Please select a client from the records."
            )

            return

        result = messagebox.askyesno(
            "Delete Client",
            "Are you sure you want to delete this client?"
        )

        if not result:
            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM clients
                WHERE client_id = %s
                """,
                (client_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Client deleted successfully."
            )

            clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # BUTTON FRAME
    # ======================================

    button_frame = tk.Frame(
        main_frame,
        bg="#F4F7FB"
    )

    button_frame.pack(
        fill="x",
        pady=(10, 5)
    )

    def action_button(
        text,
        command,
        bg
    ):

        return tk.Button(
            button_frame,
            text=text,
            font=("Arial", 8, "bold"),
            bg=bg,
            fg="white",
            activebackground=bg,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8,
            command=command
        )

    add_button = action_button(
        "ADD",
        add_client,
        "#243B6B"
    )

    add_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    update_button = action_button(
        "UPDATE",
        update_client,
        "#5B4B8A"
    )

    update_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    delete_button = action_button(
        "DELETE",
        delete_client,
        "#B42318"
    )

    delete_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    clear_button = action_button(
        "CLEAR",
        clear_form,
        "#687386"
    )

    clear_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    # ======================================
    # VIEW RECORDS BUTTON
    # ======================================

    view_button = tk.Button(
        main_frame,
        text="VIEW RECORDS",
        font=("Arial", 9, "bold"),
        bg="#243B6B",
        fg="white",
        activebackground="#243B6B",
        activeforeground="white",
        relief="flat",
        bd=0,
        pady=9
    )

    view_button.pack(
        fill="x",
        pady=(5, 0)
    )

    # ======================================
    # RECORDS WINDOW
    # ======================================

    def open_records():

        records_window = tk.Toplevel(
            client_window
        )

        records_window.title(
            "Client Records"
        )

        records_window.geometry(
            "600x500"
        )

        records_window.configure(
            bg="#F4F7FB"
        )

        records_window.resizable(
            True,
            True
        )

        # ==================================
        # RECORDS HEADER
        # ==================================

        records_header = tk.Frame(
            records_window,
            bg="#243B6B"
        )

        records_header.pack(
            fill="x"
        )

        records_title = tk.Label(
            records_header,
            text="CLIENT RECORDS",
            font=("Arial", 16, "bold"),
            bg="#243B6B",
            fg="white"
        )

        records_title.pack(
            pady=12
        )

        # ==================================
        # TABLE FRAME
        # ==================================

        table_frame = tk.Frame(
            records_window,
            bg="white"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "ID",
            "Name",
            "Email",
            "Phone",
            "Company"
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

        tree.column(
            "ID",
            width=50,
            anchor="center"
        )

        tree.column(
            "Name",
            width=130
        )

        tree.column(
            "Email",
            width=180
        )

        tree.column(
            "Phone",
            width=110
        )

        tree.column(
            "Company",
            width=150
        )

        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        tree.pack(
            side="top",
            fill="both",
            expand=True
        )

        vertical_scroll.pack(
            side="right",
            fill="y"
        )

        horizontal_scroll.pack(
            side="bottom",
            fill="x"
        )

        # ==================================
        # LOAD CLIENTS
        # ==================================

        def load_clients():

            for item in tree.get_children():

                tree.delete(item)

            connection = connect_database()

            if connection is None:
                return

            try:

                cursor = connection.cursor()

                cursor.execute(
                    """
                    SELECT
                        client_id,
                        client_name,
                        email,
                        phone,
                        company
                    FROM clients
                    ORDER BY client_id DESC
                    """
                )

                records = cursor.fetchall()

                for record in records:

                    tree.insert(
                        "",
                        tk.END,
                        values=record
                    )

                cursor.close()
                connection.close()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        # ==================================
        # SELECT CLIENT
        # ==================================

        def select_client(event):

            selected = tree.selection()

            if not selected:
                return

            values = tree.item(
                selected[0],
                "values"
            )

            selected_client_id.set(
                values[0]
            )

            name_entry.delete(
                0,
                tk.END
            )

            name_entry.insert(
                0,
                values[1]
            )

            email_entry.delete(
                0,
                tk.END
            )

            email_entry.insert(
                0,
                values[2]
            )

            phone_entry.delete(
                0,
                tk.END
            )

            phone_entry.insert(
                0,
                values[3]
            )

            company_entry.delete(
                0,
                tk.END
            )

            company_entry.insert(
                0,
                values[4]
            )

            connection = connect_database()

            if connection is None:
                return

            try:

                cursor = connection.cursor()

                cursor.execute(
                    """
                    SELECT address
                    FROM clients
                    WHERE client_id = %s
                    """,
                    (values[0],)
                )

                result = cursor.fetchone()

                cursor.close()
                connection.close()

                address_entry.delete(
                    0,
                    tk.END
                )

                if result and result[0]:

                    address_entry.insert(
                        0,
                        result[0]
                    )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        tree.bind(
            "<<TreeviewSelect>>",
            select_client
        )

        load_clients()

    view_button.config(
        command=open_records
    )

    name_entry.focus()

# ==========================================
# PROJECT MANAGEMENT
# ==========================================

def open_project_management():

    project_window = tk.Toplevel(login_window)

    project_window.title(
        "Project Management"
    )

    project_window.geometry(
        "550x1400"
    )

    project_window.configure(
        bg="#F4F7FB"
    )

    project_window.resizable(
        True,
        True
    )

    # ======================================
    # HEADER
    # ======================================

    header = tk.Frame(
        project_window,
        bg="#243B6B"
    )

    header.pack(
        fill="x"
    )

    title = tk.Label(
        header,
        text="PROJECT MANAGEMENT",
        font=("Arial", 18, "bold"),
        bg="#243B6B",
        fg="white"
    )

    title.pack(
        pady=(13, 2)
    )

    subtitle = tk.Label(
        header,
        text="Manage your project records",
        font=("Arial", 9),
        bg="#243B6B",
        fg="#DCE6FF"
    )

    subtitle.pack(
        pady=(0, 13)
    )

    # ======================================
    # MAIN FRAME
    # ======================================

    main_frame = tk.Frame(
        project_window,
        bg="#F4F7FB"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=12,
        pady=10
    )

    # ======================================
    # FORM CARD
    # ======================================

    form_card = tk.Frame(
        main_frame,
        bg="white"
    )

    form_card.pack(
        fill="x"
    )

    # ======================================
    # FIELD FUNCTION
    # ======================================

    def create_field(label_text):

        label = tk.Label(
            form_card,
            text=label_text,
            font=("Arial", 8, "bold"),
            bg="white",
            fg="#444444"
        )

        label.pack(
            anchor="w",
            padx=12,
            pady=(5, 1)
        )

        entry = tk.Entry(
            form_card,
            font=("Arial", 9),
            bg="#F4F7FB",
            fg="#222222",
            relief="flat",
            bd=0
        )

        entry.pack(
            fill="x",
            padx=12,
            ipady=5
        )

        return entry

    # ======================================
    # CLIENT
    # ======================================

    client_label = tk.Label(
        form_card,
        text="Client",
        font=("Arial", 8, "bold"),
        bg="white",
        fg="#444444"
    )

    client_label.pack(
        anchor="w",
        padx=12,
        pady=(5, 1)
    )

    client_combo = ttk.Combobox(
        form_card,
        font=("Arial", 9),
        state="readonly"
    )

    client_combo.pack(
        fill="x",
        padx=12,
        ipady=4
    )

    # ======================================
    # PROJECT FIELDS
    # ======================================

    project_name_entry = create_field(
        "Project Name"
    )

    category_entry = create_field(
        "Category"
    )

    start_date_entry = create_field(
        "Start Date (YYYY-MM-DD)"
    )

    deadline_entry = create_field(
        "Deadline (YYYY-MM-DD)"
    )

    budget_entry = create_field(
        "Budget"
    )

    amount_paid_entry = create_field(
        "Amount Paid"
    )

    # ======================================
    # STATUS
    # ======================================

    status_label = tk.Label(
        form_card,
        text="Status",
        font=("Arial", 8, "bold"),
        bg="white",
        fg="#444444"
    )

    status_label.pack(
        anchor="w",
        padx=12,
        pady=(5, 1)
    )

    status_combo = ttk.Combobox(
        form_card,
        values=[
            "Pending",
            "In Progress",
            "Completed"
        ],
        state="readonly",
        font=("Arial", 9)
    )

    status_combo.pack(
        fill="x",
        padx=12,
        ipady=4
    )

    status_combo.set(
        "Pending"
    )

    # ======================================
    # DESCRIPTION
    # ======================================

    description_label = tk.Label(
        form_card,
        text="Description",
        font=("Arial", 8, "bold"),
        bg="white",
        fg="#444444"
    )

    description_label.pack(
        anchor="w",
        padx=12,
        pady=(5, 1)
    )

    description_text = tk.Text(
        form_card,
        height=3,
        font=("Arial", 9),
        bg="#F4F7FB",
        fg="#222222",
        relief="flat",
        bd=0
    )

    description_text.pack(
        fill="x",
        padx=12,
        pady=(0, 8)
    )

    # ======================================
    # SELECTED PROJECT
    # ======================================

    selected_project_id = tk.StringVar()

    # ======================================
    # LOAD CLIENTS
    # ======================================

    client_map = {}

    def load_clients():

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    client_id,
                    client_name
                FROM clients
                ORDER BY client_name
                """
            )

            records = cursor.fetchall()

            cursor.close()
            connection.close()

            client_map.clear()

            client_names = []

            for client_id, client_name in records:

                display_name = (
                    str(client_id)
                    + " - "
                    + client_name
                )

                client_map[display_name] = client_id

                client_names.append(
                    display_name
                )

            client_combo["values"] = client_names

            if client_names:

                client_combo.current(0)

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # CLEAR FORM
    # ======================================

    def clear_form():

        selected_project_id.set("")

        if client_combo["values"]:

            client_combo.current(0)

        project_name_entry.delete(
            0,
            tk.END
        )

        category_entry.delete(
            0,
            tk.END
        )

        start_date_entry.delete(
            0,
            tk.END
        )

        deadline_entry.delete(
            0,
            tk.END
        )

        budget_entry.delete(
            0,
            tk.END
        )

        amount_paid_entry.delete(
            0,
            tk.END
        )

        status_combo.set(
            "Pending"
        )

        description_text.delete(
            "1.0",
            tk.END
        )

        project_name_entry.focus()

    # ======================================
    # ADD PROJECT
    # ======================================

    def add_project():

        selected_client = client_combo.get()

        if selected_client == "":

            messagebox.showwarning(
                "Missing Information",
                "Please select a client."
            )

            return

        project_name = project_name_entry.get().strip()
        category = category_entry.get().strip()
        start_date = start_date_entry.get().strip()
        deadline = deadline_entry.get().strip()
        budget = budget_entry.get().strip()
        amount_paid = amount_paid_entry.get().strip()
        status = status_combo.get()
        description = description_text.get(
            "1.0",
            tk.END
        ).strip()

        if project_name == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter project name."
            )

            return

        try:

            budget_value = float(
                budget
            ) if budget else 0

            paid_value = float(
                amount_paid
            ) if amount_paid else 0

            if budget_value < 0 or paid_value < 0:

                raise ValueError

            if paid_value > budget_value:

                messagebox.showwarning(
                    "Invalid Amount",
                    "Amount Paid cannot be greater than Budget."
                )

                return

        except ValueError:

            messagebox.showwarning(
                "Invalid Amount",
                "Please enter valid numeric values for Budget and Amount Paid."
            )

            return

        client_id = client_map.get(
            selected_client
        )

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            query = """
                INSERT INTO projects
                (
                    client_id,
                    project_name,
                    category,
                    start_date,
                    deadline,
                    budget,
                    amount_paid,
                    status,
                    description
                )
                VALUES
                (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
            """

            cursor.execute(
                query,
                (
                    client_id,
                    project_name,
                    category,
                    start_date if start_date else None,
                    deadline if deadline else None,
                    budget_value,
                    paid_value,
                    status,
                    description
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Project added successfully."
            )

            clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # UPDATE PROJECT
    # ======================================

    def update_project():

        project_id = selected_project_id.get()

        if project_id == "":

            messagebox.showwarning(
                "Select Project",
                "Please select a project from the records."
            )

            return

        selected_client = client_combo.get()

        project_name = project_name_entry.get().strip()
        category = category_entry.get().strip()
        start_date = start_date_entry.get().strip()
        deadline = deadline_entry.get().strip()
        budget = budget_entry.get().strip()
        amount_paid = amount_paid_entry.get().strip()
        status = status_combo.get()
        description = description_text.get(
            "1.0",
            tk.END
        ).strip()

        if selected_client == "" or project_name == "":

            messagebox.showwarning(
                "Missing Information",
                "Client and Project Name are required."
            )

            return

        try:

            budget_value = float(
                budget
            ) if budget else 0

            paid_value = float(
                amount_paid
            ) if amount_paid else 0

            if budget_value < 0 or paid_value < 0:

                raise ValueError

            if paid_value > budget_value:

                messagebox.showwarning(
                    "Invalid Amount",
                    "Amount Paid cannot be greater than Budget."
                )

                return

        except ValueError:

            messagebox.showwarning(
                "Invalid Amount",
                "Please enter valid numeric values."
            )

            return

        client_id = client_map.get(
            selected_client
        )

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            query = """
                UPDATE projects
                SET
                    client_id = %s,
                    project_name = %s,
                    category = %s,
                    start_date = %s,
                    deadline = %s,
                    budget = %s,
                    amount_paid = %s,
                    status = %s,
                    description = %s
                WHERE project_id = %s
            """

            cursor.execute(
                query,
                (
                    client_id,
                    project_name,
                    category,
                    start_date if start_date else None,
                    deadline if deadline else None,
                    budget_value,
                    paid_value,
                    status,
                    description,
                    project_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Project updated successfully."
            )

            clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # DELETE PROJECT
    # ======================================

    def delete_project():

        project_id = selected_project_id.get()

        if project_id == "":

            messagebox.showwarning(
                "Select Project",
                "Please select a project from the records."
            )

            return

        result = messagebox.askyesno(
            "Delete Project",
            "Are you sure you want to delete this project?"
        )

        if not result:
            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM projects
                WHERE project_id = %s
                """,
                (project_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Project deleted successfully."
            )

            clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # BUTTON FRAME
    # ======================================

    button_frame = tk.Frame(
        main_frame,
        bg="#F4F7FB"
    )

    button_frame.pack(
        fill="x",
        pady=(8, 5)
    )

    def action_button(
        text,
        command,
        bg
    ):

        return tk.Button(
            button_frame,
            text=text,
            font=("Arial", 8, "bold"),
            bg=bg,
            fg="white",
            activebackground=bg,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8,
            command=command
        )

    add_button = action_button(
        "ADD",
        add_project,
        "#243B6B"
    )

    add_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    update_button = action_button(
        "UPDATE",
        update_project,
        "#5B4B8A"
    )

    update_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    delete_button = action_button(
        "DELETE",
        delete_project,
        "#B42318"
    )

    delete_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    clear_button = action_button(
        "CLEAR",
        clear_form,
        "#687386"
    )

    clear_button.pack(
        side="left",
        expand=True,
        fill="x",
        padx=2
    )

    # ======================================
    # VIEW RECORDS BUTTON
    # ======================================

    view_button = tk.Button(
        main_frame,
        text="VIEW RECORDS",
        font=("Arial", 9, "bold"),
        bg="#243B6B",
        fg="white",
        activebackground="#243B6B",
        activeforeground="white",
        relief="flat",
        bd=0,
        pady=9
    )

    view_button.pack(
        fill="x",
        pady=(5, 0)
    )

    # ======================================
    # RECORDS WINDOW
    # ======================================

    def open_records():

        records_window = tk.Toplevel(
            project_window
        )

        records_window.title(
            "Project Records"
        )

        records_window.geometry(
            "700x500"
        )

        records_window.configure(
            bg="#F4F7FB"
        )

        records_window.resizable(
            True,
            True
        )

        # ==================================
        # RECORDS HEADER
        # ==================================

        records_header = tk.Frame(
            records_window,
            bg="#243B6B"
        )

        records_header.pack(
            fill="x"
        )

        records_title = tk.Label(
            records_header,
            text="PROJECT RECORDS",
            font=("Arial", 16, "bold"),
            bg="#243B6B",
            fg="white"
        )

        records_title.pack(
            pady=12
        )

                # ==================================
        # TABLE FRAME
        # ==================================

        table_frame = tk.Frame(
            records_window,
            bg="white"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "ID",
            "Client",
            "Project",
            "Category",
            "Start",
            "Deadline",
            "Budget",
            "Paid",
            "Status"
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

        tree.column(
            "ID",
            width=45,
            anchor="center"
        )

        tree.column(
            "Client",
            width=110
        )

        tree.column(
            "Project",
            width=130
        )

        tree.column(
            "Category",
            width=100
        )

        tree.column(
            "Start",
            width=90
        )

        tree.column(
            "Deadline",
            width=90
        )

        tree.column(
            "Budget",
            width=80
        )

        tree.column(
            "Paid",
            width=80
        )

        tree.column(
            "Status",
            width=100
        )

        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        tree.pack(
            side="top",
            fill="both",
            expand=True
        )

        vertical_scroll.pack(
            side="right",
            fill="y"
        )

        horizontal_scroll.pack(
            side="bottom",
            fill="x"
        )

        # ==================================
        # LOAD PROJECTS
        # ==================================

        def load_projects():

            for item in tree.get_children():

                tree.delete(item)

            connection = connect_database()

            if connection is None:
                return

            try:

                cursor = connection.cursor()

                query = """
                    SELECT
                        p.project_id,
                        c.client_name,
                        p.project_name,
                        p.category,
                        p.start_date,
                        p.deadline,
                        p.budget,
                        p.amount_paid,
                        p.status
                    FROM projects p
                    INNER JOIN clients c
                        ON p.client_id = c.client_id
                    ORDER BY p.project_id DESC
                """

                cursor.execute(query)

                records = cursor.fetchall()

                for record in records:

                    tree.insert(
                        "",
                        tk.END,
                        values=record
                    )

                cursor.close()
                connection.close()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        # ==================================
        # SELECT PROJECT
        # ==================================

        def select_project(event):

            selected = tree.selection()

            if not selected:
                return

            values = tree.item(
                selected[0],
                "values"
            )

            selected_project_id.set(
                values[0]
            )

            client_name = values[1]

            for display_name in client_map:

                if display_name.endswith(
                    " - " + client_name
                ):

                    client_combo.set(
                        display_name
                    )

                    break

            project_name_entry.delete(
                0,
                tk.END
            )

            project_name_entry.insert(
                0,
                values[2]
            )

            category_entry.delete(
                0,
                tk.END
            )

            category_entry.insert(
                0,
                values[3]
            )

            start_date_entry.delete(
                0,
                tk.END
            )

            start_date_entry.insert(
                0,
                values[4] if values[4] else ""
            )

            deadline_entry.delete(
                0,
                tk.END
            )

            deadline_entry.insert(
                0,
                values[5] if values[5] else ""
            )

            budget_entry.delete(
                0,
                tk.END
            )

            budget_entry.insert(
                0,
                values[6]
            )

            amount_paid_entry.delete(
                0,
                tk.END
            )

            amount_paid_entry.insert(
                0,
                values[7]
            )

            status_combo.set(
                values[8]
            )

            connection = connect_database()

            if connection is None:
                return

            try:

                cursor = connection.cursor()

                cursor.execute(
                    """
                    SELECT description
                    FROM projects
                    WHERE project_id = %s
                    """,
                    (values[0],)
                )

                result = cursor.fetchone()

                cursor.close()
                connection.close()

                description_text.delete(
                    "1.0",
                    tk.END
                )

                if result and result[0]:

                    description_text.insert(
                        "1.0",
                        result[0]
                    )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        tree.bind(
            "<<TreeviewSelect>>",
            select_project
        )

        load_projects()

    view_button.config(
        command=open_records
    )

    # ======================================
    # INITIAL DATA
    # ======================================

    load_clients()

    project_name_entry.focus()
   
 # =========================
# PAYMENT TRACKING
# =========================

def open_payment_tracking():

    payment_window = tk.Toplevel(login_window)
    payment_window.title("Payment Tracking")
    payment_window.geometry("600x900")
    payment_window.configure(bg="#F4F7FB")
    payment_window.resizable(True, True)

    # =========================
    # HEADER
    # =========================

    header = tk.Frame(
        payment_window,
        bg="#243B6B",
        height=80
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="PAYMENT TRACKING",
        font=("Arial", 18, "bold"),
        bg="#243B6B",
        fg="white"
    ).pack(pady=(18, 2))

    tk.Label(
        header,
        text="Track project payments",
        font=("Arial", 9),
        bg="#243B6B",
        fg="#D9E2FF"
    ).pack()

    # =========================
    # FORM FRAME
    # =========================

    form_frame = tk.Frame(
        payment_window,
        bg="white",
        padx=20,
        pady=20
    )
    form_frame.pack(
        fill="x",
        padx=15,
        pady=15
    )

    # =========================
    # PROJECT SELECTION
    # =========================

    tk.Label(
        form_frame,
        text="Select Project",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#243B6B"
    ).pack(anchor="w")

    project_combo = ttk.Combobox(
        form_frame,
        font=("Arial", 10),
        state="readonly"
    )
    project_combo.pack(
        fill="x",
        pady=(5, 15)
    )

    # =========================
    # DETAILS
    # =========================

    details_frame = tk.Frame(
        form_frame,
        bg="#F4F7FB",
        padx=15,
        pady=15
    )
    details_frame.pack(fill="x")

    tk.Label(
        details_frame,
        text="Client Name",
        font=("Arial", 9, "bold"),
        bg="#F4F7FB",
        fg="#555555"
    ).grid(row=0, column=0, sticky="w", pady=5)

    client_label = tk.Label(
        details_frame,
        text="-",
        font=("Arial", 10),
        bg="#F4F7FB",
        fg="#222222"
    )
    client_label.grid(
        row=0,
        column=1,
        sticky="w",
        padx=10
    )

    tk.Label(
        details_frame,
        text="Budget",
        font=("Arial", 9, "bold"),
        bg="#F4F7FB",
        fg="#555555"
    ).grid(row=1, column=0, sticky="w", pady=5)

    budget_label = tk.Label(
        details_frame,
        text="Rs. 0.00",
        font=("Arial", 10, "bold"),
        bg="#F4F7FB",
        fg="#243B6B"
    )
    budget_label.grid(
        row=1,
        column=1,
        sticky="w",
        padx=10
    )

    tk.Label(
        details_frame,
        text="Amount Paid",
        font=("Arial", 9, "bold"),
        bg="#F4F7FB",
        fg="#555555"
    ).grid(row=2, column=0, sticky="w", pady=5)

    paid_label = tk.Label(
        details_frame,
        text="Rs. 0.00",
        font=("Arial", 10, "bold"),
        bg="#F4F7FB",
        fg="#243B6B"
    )
    paid_label.grid(
        row=2,
        column=1,
        sticky="w",
        padx=10
    )

    tk.Label(
        details_frame,
        text="Remaining",
        font=("Arial", 9, "bold"),
        bg="#F4F7FB",
        fg="#555555"
    ).grid(row=3, column=0, sticky="w", pady=5)

    remaining_label = tk.Label(
        details_frame,
        text="Rs. 0.00",
        font=("Arial", 10, "bold"),
        bg="#F4F7FB",
        fg="#5B4B8A"
    )
    remaining_label.grid(
        row=3,
        column=1,
        sticky="w",
        padx=10
    )

    tk.Label(
        details_frame,
        text="Payment Status",
        font=("Arial", 9, "bold"),
        bg="#F4F7FB",
        fg="#555555"
    ).grid(row=4, column=0, sticky="w", pady=5)

    status_label = tk.Label(
        details_frame,
        text="-",
        font=("Arial", 10, "bold"),
        bg="#F4F7FB",
        fg="#5B4B8A"
    )
    status_label.grid(
        row=4,
        column=1,
        sticky="w",
        padx=10
    )

    # =========================
    # PROJECT DATA
    # =========================

    project_map = {}

    def load_projects():

        project_map.clear()

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    p.project_id,
                    p.project_name,
                    c.client_name,
                    p.budget,
                    p.amount_paid
                FROM projects p
                INNER JOIN clients c
                    ON p.client_id = c.client_id
                ORDER BY p.project_id DESC
            """)

            records = cursor.fetchall()

            project_values = []

            for row in records:

                project_id = row[0]
                project_name = row[1]

                display_name = (
                    str(project_id)
                    + " - "
                    + project_name
                )

                project_map[display_name] = row

                project_values.append(display_name)

            project_combo["values"] = project_values

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Error",
                "Unable to load projects.\n\n" + str(e)
            )

    # =========================
    # SHOW PAYMENT DETAILS
    # =========================

    def show_payment_details(event=None):

        selected_project = project_combo.get()

        if selected_project not in project_map:
            return

        row = project_map[selected_project]

        client_name = row[2]
        budget = float(row[3] or 0)
        amount_paid = float(row[4] or 0)

        remaining = budget - amount_paid

        if remaining <= 0:
            payment_status = "Fully Paid"
        elif amount_paid > 0:
            payment_status = "Partially Paid"
        else:
            payment_status = "Pending"

        client_label.config(
            text=client_name
        )

        budget_label.config(
            text=f"Rs. {budget:.2f}"
        )

        paid_label.config(
            text=f"Rs. {amount_paid:.2f}"
        )

        remaining_label.config(
            text=f"Rs. {remaining:.2f}"
        )

        status_label.config(
            text=payment_status
        )

    project_combo.bind(
        "<<ComboboxSelected>>",
        show_payment_details
    )

    # =========================
    # VIEW ALL PAYMENTS
    # =========================

    def view_payments():

        records_window = tk.Toplevel(payment_window)
        records_window.title("Payment Records")
        records_window.geometry("750x500")
        records_window.configure(bg="#F4F7FB")

        tk.Label(
            records_window,
            text="PAYMENT RECORDS",
            font=("Arial", 16, "bold"),
            bg="#F4F7FB",
            fg="#243B6B"
        ).pack(pady=15)

        table_frame = tk.Frame(
            records_window,
            bg="#F4F7FB"
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        columns = (
            "ID",
            "Client",
            "Project",
            "Budget",
            "Paid",
            "Remaining",
            "Status"
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=100,
                anchor="center"
            )

        y_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        x_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=y_scrollbar.set,
            xscrollcommand=x_scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        y_scrollbar.pack(
            side="right",
            fill="y"
        )

        x_scrollbar.pack(
            side="bottom",
            fill="x"
        )

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    p.project_id,
                    c.client_name,
                    p.project_name,
                    p.budget,
                    p.amount_paid
                FROM projects p
                INNER JOIN clients c
                    ON p.client_id = c.client_id
                ORDER BY p.project_id DESC
            """)

            records = cursor.fetchall()

            for row in records:

                project_id = row[0]
                client_name = row[1]
                project_name = row[2]
                budget = float(row[3] or 0)
                amount_paid = float(row[4] or 0)

                remaining = budget - amount_paid

                if remaining <= 0:
                    status = "Fully Paid"
                elif amount_paid > 0:
                    status = "Partially Paid"
                else:
                    status = "Pending"

                tree.insert(
                    "",
                    "end",
                    values=(
                        project_id,
                        client_name,
                        project_name,
                        f"Rs. {budget:.2f}",
                        f"Rs. {amount_paid:.2f}",
                        f"Rs. {remaining:.2f}",
                        status
                    )
                )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Error",
                "Unable to load payment records.\n\n" + str(e)
            )

    # =========================
    # VIEW BUTTON
    # =========================

    view_button = tk.Button(
        form_frame,
        text="VIEW ALL PAYMENTS",
        font=("Arial", 10, "bold"),
        bg="#5B4B8A",
        fg="white",
        activebackground="#4A3D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=view_payments
    )

    view_button.pack(
        fill="x",
        pady=(20, 5),
        ipady=8
    )

        # =========================
    # LOAD DATA
    # =========================

    load_projects()
  
# =========================
# REPORTS / SUMMARY
# =========================

def open_reports():

    report_window = tk.Toplevel(login_window)
    report_window.title("Reports & Summary")
    report_window.geometry("660x900")
    report_window.configure(bg="#F4F7FB")
    report_window.resizable(True, True)

    # =========================
    # HEADER
    # =========================

    header = tk.Frame(
        report_window,
        bg="#243B6B",
        height=85
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="REPORTS & SUMMARY",
        font=("Arial", 18, "bold"),
        bg="#243B6B",
        fg="white"
    ).pack(pady=(18, 2))

    tk.Label(
        header,
        text="Freelancer project overview",
        font=("Arial", 9),
        bg="#243B6B",
        fg="#D9E2FF"
    ).pack()

    # =========================
    # SUMMARY FRAME
    # =========================

    summary_frame = tk.Frame(
        report_window,
        bg="white",
        padx=20,
        pady=20
    )
    summary_frame.pack(
        fill="x",
        padx=15,
        pady=15
    )

    # =========================
    # REPORT LABELS
    # =========================

    def create_report_row(parent, title, row):

        tk.Label(
            parent,
            text=title,
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#555555"
        ).grid(
            row=row,
            column=0,
            sticky="w",
            pady=8
        )

        value_label = tk.Label(
            parent,
            text="0",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#243B6B"
        )

        value_label.grid(
            row=row,
            column=1,
            sticky="e",
            padx=10,
            pady=8
        )

        return value_label

    clients_label = create_report_row(
        summary_frame,
        "Total Clients",
        0
    )

    projects_label = create_report_row(
        summary_frame,
        "Total Projects",
        1
    )

    pending_label = create_report_row(
        summary_frame,
        "Pending Projects",
        2
    )

    progress_label = create_report_row(
        summary_frame,
        "In Progress",
        3
    )

    completed_label = create_report_row(
        summary_frame,
        "Completed Projects",
        4
    )

    budget_label = create_report_row(
        summary_frame,
        "Total Budget",
        5
    )

    paid_label = create_report_row(
        summary_frame,
        "Total Amount Paid",
        6
    )

    remaining_label = create_report_row(
        summary_frame,
        "Remaining Amount",
        7
    )

    # =========================
    # LOAD REPORT DATA
    # =========================

    def load_report_data():

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            # Total Clients

            cursor.execute("""
                SELECT COUNT(*)
                FROM clients
            """)

            total_clients = cursor.fetchone()[0]

            # Total Projects

            cursor.execute("""
                SELECT COUNT(*)
                FROM projects
            """)

            total_projects = cursor.fetchone()[0]

            # Pending Projects

            cursor.execute("""
                SELECT COUNT(*)
                FROM projects
                WHERE status = 'Pending'
            """)

            pending_projects = cursor.fetchone()[0]

            # In Progress Projects

            cursor.execute("""
                SELECT COUNT(*)
                FROM projects
                WHERE status = 'In Progress'
            """)

            in_progress = cursor.fetchone()[0]

            # Completed Projects

            cursor.execute("""
                SELECT COUNT(*)
                FROM projects
                WHERE status = 'Completed'
            """)

            completed_projects = cursor.fetchone()[0]

            # Total Budget

            cursor.execute("""
                SELECT COALESCE(SUM(budget), 0)
                FROM projects
            """)

            total_budget = float(
                cursor.fetchone()[0] or 0
            )

            # Total Amount Paid

            cursor.execute("""
                SELECT COALESCE(SUM(amount_paid), 0)
                FROM projects
            """)

            total_paid = float(
                cursor.fetchone()[0] or 0
            )

            # Remaining Amount

            remaining_amount = (
                total_budget - total_paid
            )

            # =========================
            # DISPLAY DATA
            # =========================

            clients_label.config(
                text=str(total_clients)
            )

            projects_label.config(
                text=str(total_projects)
            )

            pending_label.config(
                text=str(pending_projects)
            )

            progress_label.config(
                text=str(in_progress)
            )

            completed_label.config(
                text=str(completed_projects)
            )

            budget_label.config(
                text=f"Rs. {total_budget:.2f}"
            )

            paid_label.config(
                text=f"Rs. {total_paid:.2f}"
            )

            remaining_label.config(
                text=f"Rs. {remaining_amount:.2f}"
            )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Error",
                "Unable to generate report.\n\n"
                + str(e)
            )

    # =========================
    # REFRESH BUTTON
    # =========================

    refresh_button = tk.Button(
        report_window,
        text="REFRESH REPORT",
        font=("Arial", 10, "bold"),
        bg="#5B4B8A",
        fg="white",
        activebackground="#4A3D73",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=load_report_data
    )

    refresh_button.pack(
        fill="x",
        padx=35,
        pady=10,
        ipady=8
    )

    # =========================
    # LOAD DATA
    # =========================

    load_report_data()  
     
# ==========================================
# RESPONSIVE DASHBOARD
# ==========================================

def open_dashboard():

    login_window.withdraw()

    dashboard = tk.Toplevel(login_window)

    dashboard.title(
        "Freelancer Project Tracker - Dashboard"
    )

    # Compact size for mobile screen
    dashboard.geometry("700x1200")

    dashboard.configure(
        bg="#F4F7FB"
    )

    # Allow resizing
    dashboard.resizable(True, True)

    # ======================================
    # MAIN CONTAINER
    # ======================================

    main_frame = tk.Frame(
        dashboard,
        bg="#F4F7FB"
    )

    main_frame.pack(
        fill="both",
        expand=True
    )

    # ======================================
    # HEADER
    # ======================================

    header = tk.Frame(
        main_frame,
        bg="#243B6B"
    )

    header.pack(
        fill="x"
    )

    title = tk.Label(
        header,
        text="FREELANCER",
        font=("Arial", 20, "bold"),
        bg="#243B6B",
        fg="white"
    )

    title.pack(
        pady=(14, 1)
    )

    subtitle = tk.Label(
        header,
        text="CLIENT & PROJECT TRACKER",
        font=("Arial", 9, "bold"),
        bg="#243B6B",
        fg="#DCE6FF"
    )

    subtitle.pack(
        pady=(0, 14)
    )

    # ======================================
    # CONTENT
    # ======================================

    content = tk.Frame(
        main_frame,
        bg="#F4F7FB"
    )

    content.pack(
        fill="both",
        expand=True,
        padx=18,
        pady=10
    )

    # ======================================
    # WELCOME
    # ======================================

    welcome = tk.Label(
        content,
        text="Welcome back",
        font=("Arial", 16, "bold"),
        bg="#F4F7FB",
        fg="#243B6B"
    )

    welcome.pack(
        anchor="w"
    )

    welcome_subtitle = tk.Label(
        content,
        text="Manage your freelance work",
        font=("Arial", 9),
        bg="#F4F7FB",
        fg="#777777"
    )

    welcome_subtitle.pack(
        anchor="w",
        pady=(1, 7)
    )

    # ======================================
    # STATISTICS GRID
    # ======================================

    stats_frame = tk.Frame(
        content,
        bg="#F4F7FB"
    )

    stats_frame.pack(
        fill="x"
    )

    stats_frame.grid_columnconfigure(
        0,
        weight=1
    )

    stats_frame.grid_columnconfigure(
        1,
        weight=1
    )

    # ======================================
    # STAT CARD FUNCTION
    # ======================================

    def create_stat_card(
        title_text,
        value_text,
        color,
        row,
        column
    ):

        card = tk.Frame(
            stats_frame,
            bg="white",
            highlightbackground="#DDE3EF",
            highlightthickness=1
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=4,
            pady=4
        )

        title_label = tk.Label(
            card,
            text=title_text,
            font=("Arial", 8, "bold"),
            bg="white",
            fg="#666666"
        )

        title_label.pack(
            pady=(6, 0)
        )

        value_label = tk.Label(
            card,
            text=value_text,
            font=("Arial", 18, "bold"),
            bg="white",
            fg=color
        )

        value_label.pack(
            pady=(0, 6)
        )

        return value_label

    # ======================================
    # STAT CARDS
    # ======================================

    clients_value = create_stat_card(
        "CLIENTS",
        "0",
        "#243B6B",
        0,
        0
    )

    projects_value = create_stat_card(
        "PROJECTS",
        "0",
        "#5B4B8A",
        0,
        1
    )

    pending_value = create_stat_card(
        "PENDING",
        "0",
        "#D97706",
        1,
        0
    )

    completed_value = create_stat_card(
        "COMPLETED",
        "0",
        "#16803C",
        1,
        1
    )

    # ======================================
    # TOTAL AMOUNT PAID
    # ======================================

    earnings_card = tk.Frame(
        content,
        bg="white",
        highlightbackground="#DDE3EF",
        highlightthickness=1
    )

    earnings_card.pack(
        fill="x",
        pady=(7, 9)
    )

    earnings_title = tk.Label(
        earnings_card,
        text="TOTAL AMOUNT PAID",
        font=("Arial", 8, "bold"),
        bg="white",
        fg="#666666"
    )

    earnings_title.pack(
        side="left",
        padx=12,
        pady=8
    )

    earnings_value = tk.Label(
        earnings_card,
        text="Rs. 0.00",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="#16803C"
    )

    earnings_value.pack(
        side="right",
        padx=12,
        pady=7
    )

    # ======================================
    # QUICK ACCESS TITLE
    # ======================================

    quick_title = tk.Label(
        content,
        text="QUICK ACCESS",
        font=("Arial", 10, "bold"),
        bg="#F4F7FB",
        fg="#243B6B"
    )

    quick_title.pack(
        anchor="w",
        pady=(0, 3)
    )

    # ======================================
    # QUICK ACCESS GRID
    # ======================================

    menu_frame = tk.Frame(
        content,
        bg="#F4F7FB"
    )

    menu_frame.pack(
        fill="x"
    )

    menu_frame.grid_columnconfigure(
        0,
        weight=1
    )

    menu_frame.grid_columnconfigure(
        1,
        weight=1
    )

    # ======================================
    # MENU BUTTON FUNCTION
    # ======================================

    def menu_button(
        text,
        row,
        column,
        command
    ):

        button = tk.Button(
            menu_frame,
            text=text,
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#243B6B",
            activebackground="#E8ECF5",
            activeforeground="#243B6B",
            relief="flat",
            bd=0,
            height=2,
            command=command
        )

        button.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=4,
            pady=3
        )

    # ======================================
    # MENU BUTTONS
    # ======================================

    menu_button(
        "CLIENTS",
        0,
        0,
         open_client_management
    )

    menu_button(
        "PROJECTS",
        0,
        1,
        open_project_management
    )

    menu_button(
        "PAYMENTS",
        1,
        0,
        open_payment_tracking
    )

    menu_button(
        "REPORTS",
        1,
        1,
        open_reports
    )

    # ======================================
    # LOGOUT
    # ======================================

    def logout():

        result = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if result:

            dashboard.destroy()

            clear_login()

            login_window.deiconify()

    logout_button = tk.Button(
        content,
        text="LOGOUT",
        font=("Arial", 9, "bold"),
        bg="#243B6B",
        fg="white",
        activebackground="#35569A",
        activeforeground="white",
        relief="flat",
        bd=0,
        padx=22,
        pady=6,
        command=logout
    )

    logout_button.pack(
        pady=7
    )

    # ======================================
    # LOAD DASHBOARD DATA
    # ======================================

    def load_dashboard_data():

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM clients"
            )

            total_clients = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM projects"
            )

            total_projects = cursor.fetchone()[0]

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM projects
                WHERE status = 'Pending'
                """
            )

            pending_projects = cursor.fetchone()[0]

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM projects
                WHERE status = 'Completed'
                """
            )

            completed_projects = cursor.fetchone()[0]

            cursor.execute(
                """
                SELECT COALESCE(
                    SUM(amount_paid),
                    0
                )
                FROM projects
                """
            )

            total_paid = cursor.fetchone()[0]

            cursor.close()
            connection.close()

            clients_value.config(
                text=str(total_clients)
            )

            projects_value.config(
                text=str(total_projects)
            )

            pending_value.config(
                text=str(pending_projects)
            )

            completed_value.config(
                text=str(completed_projects)
            )

            earnings_value.config(
                text="Rs. " + format(
                    float(total_paid),
                    ".2f"
                )
            )

        except Exception as e:

            messagebox.showerror(
                "Dashboard Error",
                str(e)
            )

    load_dashboard_data()

    # ======================================
    # CLOSE DASHBOARD
    # ======================================

    def close_dashboard():

        dashboard.destroy()

        login_window.destroy()

    dashboard.protocol(
        "WM_DELETE_WINDOW",
        close_dashboard
    )

    # ======================================
    # CLOSE WINDOW
    # ======================================

    def close_dashboard():

        dashboard.destroy()

        login_window.destroy()

    dashboard.protocol(
        "WM_DELETE_WINDOW",
        close_dashboard
    )


# ==========================================
# MAIN LOGIN WINDOW
# ==========================================

login_window = tk.Tk()

login_window.title(
    "Freelancer Project Tracker"
)

login_window.geometry(
    "500x650"
)

login_window.configure(
    bg="#EAF0FF"
)

login_window.resizable(
    False,
    False
)


# ==========================================
# HEADER
# ==========================================

header = tk.Frame(
    login_window,
    bg="#243B6B",
    height=180
)

header.pack(
    fill="x"
)

header.pack_propagate(
    False
)


title = tk.Label(
    header,
    text="FREELANCER",
    font=("Arial", 24, "bold"),
    bg="#243B6B",
    fg="white"
)

title.pack(
    pady=(20, 5)
)


subtitle = tk.Label(
    header,
    text="CLIENT & PROJECT TRACKER",
    font=("Arial", 13, "bold"),
    bg="#243B6B",
    fg="#DCE6FF"
)

subtitle.pack(
    pady=5
)


# ==========================================
# LOGIN CARD
# ==========================================

card = tk.Frame(
    login_window,
    bg="white",
    bd=0,
    highlightthickness=0
)

card.pack(
    padx=35,
    pady=35,
    fill="both",
    expand=True
)


login_title = tk.Label(
    card,
    text="LOGIN",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="#243B6B"
)

login_title.pack(
    pady=(35, 30)
)


# ==========================================
# USERNAME
# ==========================================

username_label = tk.Label(
    card,
    text="Username",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#444444"
)

username_label.pack(
    anchor="w",
    padx=40
)


username_entry = tk.Entry(
    card,
    font=("Arial", 13),
    bg="#F4F7FB",
    fg="#222222",
    relief="flat",
    bd=0
)

username_entry.pack(
    padx=40,
    pady=(8, 25),
    ipady=10,
    fill="x"
)


# ==========================================
# PASSWORD
# ==========================================

password_label = tk.Label(
    card,
    text="Password",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#444444"
)

password_label.pack(
    anchor="w",
    padx=40
)


password_entry = tk.Entry(
    card,
    font=("Arial", 13),
    bg="#F4F7FB",
    fg="#222222",
    relief="flat",
    bd=0,
    show="*"
)

password_entry.pack(
    padx=40,
    pady=(8, 30),
    ipady=10,
    fill="x"
)


# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(
    card,
    bg="white"
)

button_frame.pack(
    pady=10
)


# ==========================================
# LOGIN BUTTON
# ==========================================

login_button = tk.Button(
    button_frame,
    text="LOGIN",
    font=("Arial", 11, "bold"),
    bg="#243B6B",
    fg="white",
    activebackground="#35569A",
    activeforeground="white",
    relief="flat",
    bd=0,
    padx=30,
    pady=10,
    command=login
)

login_button.pack(
    side="left",
    padx=8
)


# ==========================================
# CLEAR BUTTON
# ==========================================

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    bg="#E8ECF5",
    fg="#243B6B",
    activebackground="#D6DDED",
    activeforeground="#243B6B",
    relief="flat",
    bd=0,
    padx=30,
    pady=10,
    command=clear_login
)

clear_button.pack(
    side="left",
    padx=8
)


# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(
    card,
    text="Secure Freelancer Management System",
    font=("Arial", 9),
    bg="white",
    fg="#888888"
)

footer.pack(
    side="bottom",
    pady=20
)


username_entry.focus()


# ==========================================
# START APPLICATION
# ==========================================

login_window.mainloop()