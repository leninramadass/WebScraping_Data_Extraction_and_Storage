from bs4 import BeautifulSoup
import requests
import mysql.connector
import openpyxl
def connect_to_mysql():  # MySQL database connection
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="root",
                                                 password="Password",
                                                 database="book_data")  # MySQL connection details
            if connection.is_connected():  # If MySQL has successfully connected to python this statement will execute
                print("MySQL connected")
            cursor = connection.cursor()  # Create a cursor here
            return connection, cursor
        except mysql.connector.Error as err:  # If MySQL is Did not connect to python this statement will execute
            print(f"Error connecting to MySQL: {err}")

def create_table(cursor):  # Table was created in database
    create_table_query = """CREATE TABLE IF NOT EXISTS BOOK(
                            Id VARCHAR(300),
                            Name VARCHAR(500),
                            Price VARCHAR(50),
                            Category VARCHAR(100),
                            Stock_status VARCHAR(100),
                            Availability VARCHAR(100))"""
    cursor.execute(create_table_query)

def insert_table(connection, cursor, product_data):  # Extracting datas are stored in database table
    insert_data_query = """INSERT INTO BOOK(Id,Name,Price,Category,Stock_status,Availability) VALUES
                        (%s,%s,%s,%s,%s,%s)"""
    data_to_insert = product_data
    cursor.execute(insert_data_query, data_to_insert)
    connection.commit()

def create_xl_file():  # Excel file was created
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "Book list"
    sheet.append(["Id", "Name", "Price", "Category", "Stock_status", "Availability"])
    return excel, sheet
def store_data_xl(product_data, excel, sheet):  # Extracting datas are stored in Ecxel
    data_values = product_data
    sheet.append([data_values[0], data_values[1], data_values[2], data_values[3], data_values[4], data_values[5]])
    excel.save("Book_data.xlsx")

def extract_product_data(full_url):  # Every datas are extracted
    try:
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, "html.parser")

        try:
            product_id = soup.find_all("tr")[0].find("td").text.strip()
            product_name = soup.find("h1").text.strip()
            product_price = soup.find_all("tr")[2].find("td").text.strip().replace("Â", "")
            product_category = soup.find("ul", class_="breadcrumb").find_all("li")[2].a.text
            stock_status = soup.find_all("tr")[5].find("td").get_text().split("(")[0].strip()
            availability_1 = soup.find_all("tr")[5].find("td").get_text().split("(")[1].strip().replace("(", "")
            availability = availability_1.replace(")", "")

            return product_id, product_name, product_price, product_category, stock_status, availability

        except Exception as e:
            print(f"Error extracting data: {e}")
    except Exception as e:
        print(e)

# code will be started this line
def book_scrap():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"  # Every page we need so get common base url
    page_number = 1  # pagenumber initialize

    connection, cursor = connect_to_mysql()
    create_table(cursor)
    excel, sheet = create_xl_file()
    while True:
        url = base_url.format(page_number) # A single page url
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            product_details = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

            for product in product_details:
                product_url = product.find("a").attrs.get("href")
                full_url = f"https://books.toscrape.com/catalogue/{product_url}"
                product_data = extract_product_data(full_url)

                # Check all required data is available before proceeding
                if product_data:
                    insert_table(connection, cursor, product_data)
                    store_data_xl(product_data, excel, sheet)
                else:
                    print("Error: Missing data in the product details.")

            next_button = soup.find_all("li", class_="next")
            if next_button:
                page_number += 1
            else:
                break
        except Exception as e:
            print(e)
            break

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")

if __name__ == "__main__":
    book_scrap()
