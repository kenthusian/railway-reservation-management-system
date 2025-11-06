import warnings
import pandas as pd
import mysql.connector as sql
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=UserWarning, module="pandas")

conn = sql.connect(host='localhost', user='root', passwd='root', database='railway')
if conn.is_connected():
    print('Successfully connected')

def menu():
    print()
    print("******************************")
    print(" RAILWAY RESERVATION SYSTEM   ")
    print("1. Create Table Passenger")
    print("2. Add new Passenger Detail")
    print("3. Create Table Train Detail")
    print("4. Add new Train Detail")
    print("5. Show All from Train Detail")
    print("6. Show All from Passenger Table")
    print("7. Show PNR No.")
    print("8. Reservation of Ticket")
    print("9. Cancellation of Reservation")
    print("10. Export Data to CSV")
    print("11. Create Graph (Passenger Count and Train Occupancy)")
    print("0. Exit")

def create_passengers():
    c1 = conn.cursor()
    c1.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            pname VARCHAR(30),
            age VARCHAR(25),
            trainno VARCHAR(30),
            noofpas VARCHAR(25),
            cls VARCHAR(25),
            destination VARCHAR(30),
            amt VARCHAR(20),
            status VARCHAR(25),
            pnrno VARCHAR(30)
        )
    """)
    conn.commit()
    print('Table passengers created')

def add_passengers():
    c1 = conn.cursor()
    L = []
    pname = input("ENTER NAME: ")
    L.append(pname)
    age = input("ENTER AGE: ")
    L.append(age)
    trainno = input("ENTER TRAIN NO.: ")
    L.append(trainno)
    noofpas = input("ENTER NO. OF PASSENGERS: ")
    L.append(noofpas)
    cls = input("ENTER CLASS: ")
    L.append(cls)
    destination = input("ENTER DESTINATION: ")
    L.append(destination)
    amt = input("ENTER FARE: ")
    L.append(amt)
    status = input("ENTER STATUS: ")
    L.append(status)
    pnrno = input("ENTER PNR NO.: ")
    L.append(pnrno)
    pas = tuple(L)
    sql_query = """
        INSERT INTO passengers (pname, age, trainno, noofpas, cls, destination, amt, status, pnrno)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    c1.execute(sql_query, pas)
    conn.commit()
    print('Record of Passenger inserted')
    df = pd.read_sql("SELECT * FROM passengers", conn)
    print(df)

def create_trainsdetail():
    c1 = conn.cursor()
    c1.execute("""
        CREATE TABLE IF NOT EXISTS trainsdetail (
            tname VARCHAR(30),
            tnum VARCHAR(25),
            source VARCHAR(30),
            destination VARCHAR(30),
            fare VARCHAR(10),
            ac1 VARCHAR(25),
            ac2 VARCHAR(30),
            slp VARCHAR(25)
        )
    """)
    conn.commit()
    print('Table trainsdetail created')

def add_traindetail():
    c1 = conn.cursor()
    df = pd.read_sql("SELECT * FROM trainsdetail", conn)
    print(df)
    L = []
    tname = input("ENTER TRAIN NAME: ")
    L.append(tname)
    tnum = input("ENTER NUMBER OF TRAIN: ")
    L.append(tnum)
    source = input("ENTER SOURCE OF TRAIN: ")
    L.append(source)
    destination = input("ENTER DESTINATION OF TRAIN: ")
    L.append(destination)
    fare = input("ENTER FARE OF STATION: ")
    L.append(fare)
    ac1 = input("ENTER No. OF SEATS FOR AC1: ")
    L.append(ac1)
    ac2 = input("ENTER No. OF SEATS FOR AC2: ")
    L.append(ac2)
    slp = input("ENTER No. OF SEATS FOR SLEEPER: ")
    L.append(slp)
    f = tuple(L)
    sql = """
        INSERT INTO trainsdetail (tname, tnum, source, destination, fare, ac1, ac2, slp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    c1.execute(sql, f)
    conn.commit()
    print('Record inserted in Trains Detail')

def show_passengers():
    print('ALL PASSENGERS DETAIL')
    df = pd.read_sql("SELECT * FROM passengers", conn)
    print(df)

def show_trains_detail():
    print("ALL TRAINS DETAILS")
    df = pd.read_sql("SELECT * FROM trainsdetail", conn)
    print(df)

def disp_pnrno():
    print("PNR STATUS WINDOW")
    a = input("Enter Train No.: ")
    qry = "SELECT pname, status FROM passengers WHERE trainno=%s;"
    df = pd.read_sql(qry, conn, params=(a,))
    print(df)

def ticketreservation():
    print("WE HAVE THE FOLLOWING SEAT TYPES FOR YOU:")
    print("TNAME is 1 FOR GOA EXPRESS FROM NEW DELHI:")
    print("1. FIRST CLASS AC RS 6000 Per PERSON")
    print("2. SECOND CLASS AC RS 5000 Per PERSON")
    print("3. THIRD CLASS AC RS 4000 Per PERSON")
    print("4. FOR SLEEPER RS 3000 Per PERSON")
    print("TNAME is 2 FOR JAMMU EXPRESS FROM NEW DELHI:")
    print("1. FIRST CLASS AC RS 10000 Per PERSON")
    print("2. SECOND CLASS AC RS 9000 Per PERSON")
    print("3. THIRD CLASS AC RS 8000 Per PERSON")
    print("4. FOR SLEEPER RS 7000 Per PERSON")

    a = int(input("ENTER YOUR CHOICE OF TICKET PLEASE: "))
    n = int(input("HOW MANY TICKETS YOU NEED: "))

    if a == 1:
        print("YOU HAVE CHOSEN FIRST CLASS AC TICKET")
        s = 6000 * n
    elif a == 2:
        print("YOU HAVE CHOSEN SECOND CLASS AC TICKET")
        s = 5000 * n
    elif a == 3:
        print("YOU HAVE CHOSEN THIRD CLASS AC TICKET")
        s = 4000 * n
    elif a == 4:
        print("YOU HAVE CHOSEN SLEEPER TICKET")
        s = 3000 * n
    else:
        print("Invalid option. PLEASE CHOOSE A TRAIN")
        return

    print("YOUR TICKET PRICE is =", s, "\n")

def cancel():
    print("Before any Changes in the STATUS")
    df = pd.read_sql("SELECT * FROM passengers", conn)
    print(df)
    pnr_no = input("Enter PNR No. to cancel: ")
    c1 = conn.cursor()
    c1.execute("UPDATE passengers SET status='cancelled' WHERE pnrno=%s", (pnr_no,))
    conn.commit()
    print(f"Reservation with PNR No. {pnr_no} has been cancelled.")
    df = pd.read_sql("SELECT * FROM passengers", conn)
    print(df)

def export_to_csv():
    print("Choose the table to export to CSV:")
    print("1. Export Passengers Table")
    print("2. Export Trains Detail Table")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        df = pd.read_sql("SELECT * FROM passengers", conn)
        filename = input("Enter the filename (e.g., passengers_data.csv): ")
        df.to_csv(filename, index=False)
        print(f"Passengers data exported to {filename}")
    
    elif choice == 2:
        df = pd.read_sql("SELECT * FROM trainsdetail", conn)
        filename = input("Enter the filename (e.g., trains_detail_data.csv): ")
        df.to_csv(filename, index=False)
        print(f"Trains detail data exported to {filename}")
    
    else:
        print("Invalid choice! Please choose a valid option.")

def create_graph():
    print("\nChoose the type of graph to create:")
    print("1. Passenger Count by Destination (Bar Chart)")
    print("2. Train Occupancy Status (Pie Chart)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        df = pd.read_sql("SELECT destination, COUNT(*) as passenger_count FROM passengers GROUP BY destination", conn)
        destinations = df['destination']
        passenger_count = df['passenger_count']

        plt.figure(figsize=(10,6))
        plt.bar(destinations, passenger_count, color='skyblue')
        plt.xlabel('Destination')
        plt.ylabel('Number of Passengers')
        plt.title('Passenger Count by Destination')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    elif choice == 2:
        df = pd.read_sql("SELECT trainno, COUNT(*) as booked_count FROM passengers GROUP BY trainno", conn)
        trains = df['trainno']
        booked_count = df['booked_count']

        plt.figure(figsize=(7,7))
        plt.pie(booked_count, labels=trains, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightgreen', 'lightblue'])
        plt.title('Train Occupancy Status')
        plt.axis('equal')
        plt.show()

    else:
        print("Invalid choice! Please select a valid graph type.")

while True:
    menu()
    opt = int(input("Enter your choice: "))
    if opt == 1:
        create_passengers()
    elif opt == 2:
        add_passengers()
    elif opt == 3:
        create_trainsdetail()
    elif opt == 4:
        add_traindetail()
    elif opt == 5:
        show_trains_detail()
    elif opt == 6:
        show_passengers()
    elif opt == 7:
        disp_pnrno()
    elif opt == 8:
        ticketreservation()
    elif opt == 9:
        cancel()
    elif opt == 10:
        export_to_csv()
    elif opt == 11:
        create_graph()
    elif opt == 0:
        print("Exiting...")
        break
    else:
        print('Invalid option. Please try again.')