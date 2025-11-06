# Railway Reservation Management System

> A command-line railway reservation system built with Python, MySQL, and Pandas.

![Python](https://img.shields.io/badge/Python-3.12-blue?style-for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql)
![Pandas](https://img.shields.io/badge/Pandas-2.x-purple?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-grey?style=for-the-badge&logo=matplotlib)

## Overview

This project is a console-based **Railway Reservation Management System** developed for the All India Senior School Certificate Examination (AISSCE) 2025.

The application is built with **Python 3.12** as the front-end and **MySQL 8.0** as the back-end database. It provides a comprehensive command-line menu for managing train schedules and passenger reservations. The system utilizes the `pandas` library for clean, tabular data display and `matplotlib` for data visualization.

## Features

* **Train Management:** Add new train details (name, number, source, destination, fares, and seat capacity).
* **Passenger Management:** Add new passenger bookings.
* **Data Display:** View all train or all passenger details in a tabular format.
* **Ticket Reservation:** A menu-driven interface for booking tickets.
* **Ticket Cancellation:** Cancel a reservation by PNR number, which updates its status in the database.
* **PNR Status:** Check the status of a booking using a Train No..
* **Data Visualization:** Generate graphs for:
    * Passenger Count by Destination (Bar Chart).
    * Train Occupancy Status (Pie Chart).
* **Data Export:** Export the `passengers` or `trainsdetail` tables directly to a CSV file.
* **Database Setup:** Dynamically creates the required tables (`passengers`, `trainsdetail`) if they don't exist.

## Technology Stack

### Software Specifications
* **Operating System:** Windows 11
* **Front-End:** Python 3.12
* **Back-End:** MySQL 8.0
* **Core Libraries:** `pandas`, `mysql.connector`, `matplotlib`
* **Documentation:** Microsoft Word 365

## How to Run

### 1. Prerequisites
* Python 3.10+
* MySQL Server 8.0+
* The following Python libraries:
    ```sh
    pip install pandas mysql-connector-python matplotlib
    ```

### 2. Database Setup
1.  Ensure your MySQL server is running.
2.  Open your MySQL client (like MySQL Workbench or the command-line client) and create a new database:
    ```sql
    CREATE DATABASE railway;
    ```
3.  **Important:** Open the Python script (`main.py`) and update the `sql.connect` line with your MySQL username and password:
    ```python
    # Connect to the MySQL database
    conn = sql.connect(host='localhost', 
                       user='YOUR_USERNAME',  # e.g., 'root'
                       passwd='YOUR_PASSWORD', # e.g., 'root'
                       database='railway')
    ```

### 3. Run the Application
1.  Once the database is ready, run the Python script:
    ```sh
    python main.py
    ```
2.  The script will print "Successfully connected."
3.  From the main menu, first run **Option 1: Create Table Passenger** and **Option 3: Create Table Train Detail** to set up your database schema.
4.  You can then use **Option 4: Add new Train Detail** to add trains and **Option 2: Add new Passenger Detail** (or Option 8) to add bookings.

## Database Schema

The system uses two main tables in the `railway` database.

### `passengers` Table
| Field | Type |
| :--- | :--- |
| pname | varchar(30) |
| age | varchar(25) |
| trainno | varchar(30) |
| noofpas | varchar(25) |
| cls | varchar(25) |
| destination | varchar(30) |
| amt | varchar(20) |
| status | varchar(25) |
| pnrno | varchar(30) |

### `trainsdetail` Table
| Field | Type |
| :--- | :--- |
| tname | varchar(30) |
| tnum | varchar(25) |
| source | varchar(30) |
| destination | varchar(30) |
| fare | varchar(10) |
| ac1 | varchar(25) |
| ac2 | varchar(30) |
| slp | varchar(25) |

## Authors
* **Samarth Khandelwal**
* **Aradhya Gupta**
* **Arav Kilak**

## Acknowledgements
* **Mrs. Himanshi Sharma** (Project Guide & HOD, Computer Science)
* **Mrs. Jayshree Periwal** (Director, Jayshree Periwal High School)
* **Mrs. Madhu Maini** (Principal, Jayshree Periwal High School)
