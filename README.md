# Money Management App (Odoo + Docker)

This project is a custom **Money Management App** built on top of **Odoo**, containerized using **Docker Compose** for easy setup and deployment. It helps you track income, expenses, and view current balances from a simple interface.

## New features added so far
-- A popup message to show current balance (See `Show Balance Popup`)
-- A website navigation to show income/expense and the balance in a web/clinet view (See `Show Balance On Website`)
-- A Kanban view added

---

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Setup Instructions

### Step 1: First-Time Odoo Initialization

1. Open the `docker-compose.yml` file.
2. Uncomment the first-time setup line and comment out the others as shown:

   ```yaml
   command: ["odoo", "-d", "odoo", "-i", "base", "--stop-after-init"]  # only for first-time setup
   # command: ["--", "-i", "base"]
   # command: ["odoo", "-d", "odoo", "-u", "money_management", "--without-demo-all"]
3. Build and start the container:

   ```yaml
   docker-compose up --build

4. Once setup completes and the terminal stops updating, press Ctrl+C to exit the CLI console.

5. Then run the following command:

   ```yaml
   docker-compose down

### Step 2: Normal Startup Configuration

1. Edit the docker-compose.yml again and update the command lines like this:

   ```yaml
   # command: ["odoo", "-d", "odoo", "-i", "base", "--stop-after-init"]  # only for first-time setup
     command: ["--", "-i", "base"]
   # command: ["odoo", "-d", "odoo", "-u", "money_management", "--without-demo-all"]

2. Restart the app normally:

   ```yaml
   docker-compose up --build


## Accessing the App

### Open your browser and go to: http://localhost:8069

### Login Credentials
- Username/Email: admin
- Password: admin

## Using the Money App

    After logging into Odoo, use the top search bar and type: Money App.

    Click to Install/Activate the Money App.

    You can now:

    Add Income entries.

    Add Expense entries.

    View Balance summary.