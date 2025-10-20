#Sifts through History DB from Chromium-based browsers 

#Imports
import sqlite3
import sys, os

#Function to 
def get_history(cursor):
    cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
    site_results = cursor.fetchall()

    print("SITE HISTORY")
    print("____________")

    for row in site_results:
        url, title, visit_count, last_visit_time = row
        print(f"Site: {title}")
        print(f"URL: {url}")
        print(f"Total Visits: {visit_count}")
        print(f"Last Visit Time: {last_visit_time}")

#Function to handle retrieving downloads from browser history
def get_downloads(cursor):
    cursor.execute("SELECT target_path, total_bytes, start_time FROM downloads")
    download_results = cursor.fetchall()

    print("DOWNLOADS")
    print("__________")

    for row in download_results:
        target_path, file_size, start_time = row
        print(f"File Path: {target_path}")
        print(f"File Size: {file_size}")
        print(f"Download Time: {start_time}")

#Main Function
def main():
    #variable declaration
    username = os.getlogin()

    if len(sys.argv) < 1:
        path = sys.argv[1]
    else:
        user = input("Google Chrome (G) or MS Edge (E): ")
        if user.upper() == "G":
            path = fr"C:\users\{username}\AppData\Local\Google\Chrome\User Data\Default\History"
        elif user.upper() == "E":
            path = fr"C:\users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\History"
        else:
            print("NO INPUT - Using Chrome")
            path = fr"C:\users\{username}\AppData\Local\Google\Chrome\User Data\Default\History"

    conn = path
    connection = sqlite3.connect(conn)
    cursor = connection.cursor()

    get_history(cursor)
    get_downloads(cursor)

    connection.close()

#Calls the main function/starts the app
main()