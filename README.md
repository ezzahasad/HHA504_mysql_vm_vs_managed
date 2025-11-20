# README — MySQL on VM vs Managed Cloud SQL

## Project Overview
This project compares two different approaches for running MySQL on Google Cloud Platform. The first approach uses a self-managed MySQL server installed on a Compute Engine virtual machine. The second approach uses Google Cloud SQL, a fully managed MySQL service. Both environments were tested using SQLAlchemy and pandas to create a database, insert sample rows, and read back results.

---

## Loom Link: https://www.loom.com/share/40cb79eedd52461e952ff2f995804e6e

---

## VM Setup Overview

A full walkthrough is documented in **docs/setup_notes_vm.md**.

The VM portion includes:
- Creating a VM in GCP (Ubuntu 24.04, e2-micro)
- Installing MySQL manually using apt
- Editing the MySQL configuration file to allow external connections
- Opening port 3306 with a custom firewall rule
- Creating a database and user inside MySQL
- Running the `vm_demo.py` script to write and read back table data

All supporting screenshots are stored in:
`screenshots/vm/` and `docs/setup_notes_vm.md`  

---

## Managed Cloud SQL Setup Overview

A full walkthrough is documented in **docs/setup_notes_managed.md**.

The Managed SQL portion includes:
- Creating a Cloud SQL MySQL instance
- Setting version, storage, and connectivity options
- Adding an authorized network for access
- Creating the class database and SQL user
- Verifying the connection in Cloud Shell
- Running `managed_demo.py` to confirm read/write operations

All supporting screenshots are stored in:
`screenshots/managed/` and `docs/setup_notes_managed.md`

---
## Comparison Overview

A detailed comparison between VM vs Managed SQL is included in:
`docs/comparison.md`

The comparison discusses:
- Which method took longer
- Which method was easier
- Hands-on vs simplified configuration
- When to choose a VM vs when to choose Cloud SQL

---

## Environment Variables

A template for environment variables is included in the .env.example file.
This file shows the correct format for all required fields, and these placeholder values were copied into the personal .env file on the local machine.

## Script Overview
Both connection tests for this assignment are contained in the scripts/ folder. The vm_demo.py script connects to the MySQL database running on the virtual machine, while the managed_demo.py script connects to the Cloud SQL managed instance. Each script uses the credentials stored in the local .env file, creates a sample table, inserts test rows, and reads the data back to confirm that the connection is working. The full execution of both scripts is demonstrated in my Loom recording, so no additional steps are required to run them manually.

Both scripts:

- Connect to the assigned MySQL instance  
- Create a table called `visits`  
- Insert test rows  
- Read back the row count to verify successful connectivity  

---

## Security Notes

- The actual `.env` file was not committed to GitHub  
- Passwords were only entered temporarily during the video demonstration  
- database instances were safely deleted after submission  
- All secrets remained local and referenced through `.env`  

---

## Additional Documentation

Detailed screenshots and step-by-step build notes are included in:

- **setup_notes_vm.md**  
- **setup_notes_managed.md**

These files contain all provisioning settings, MySQL commands, firewall configuration, and Python test outputs. 