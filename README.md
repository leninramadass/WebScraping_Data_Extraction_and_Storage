

# Web Scraping Project: Extracting a data from Book Selling E-commerce Websites

This Python project demonstrates web scraping capabilities using BeautifulSoup and requests to extract book details from a sample website (https://books.toscrape.com). The extracted data is stored in a MySQL database and an Excel file. The primary purpose of this project is to showcase my skills in web scraping, data manipulation, and database interaction.


## Tech Stack

- Python 3.x
- MySQL
- Excel
- BeautifulSoup
- requests
- mysql-connector
- openpyxl



## Project Explanation

#### Extracts Book Details:
- The script uses BeautifulSoup and requests to extract essential book details including ID, name, price, category, stock status, and availability from a sample website (https://books.toscrape.com).
#### Stores Data in MySQL Database:
- The extracted data is stored in a MySQL database table named 'BOOK'. The connection details for the MySQL database are configured in the `connect_to_mysql` function within the script.
#### Creates Excel File:
- The script generates an Excel file named 'Book_list.xlsx' to store the extracted data. This file is another way to present and analyze the collected data.
#### Handles Pagination:
- Handles Pagination: The web scraping logic includes pagination handling to systematically scrape data from multiple pages. The script iterates through each page, extracting book details and storing them in the MySQL database and Excel file. This ensures efficient collection of book data from across the web.
    - The script identifies and extracts the 'Next' button on each page to determine whether additional pages exist.
    - If a 'Next' button is found, the script proceeds to the next page and continues the scraping process.
    - Pagination is a crucial feature for handling scenarios where book data spans across multiple pages, ensuring a complete and thorough extraction.
#### Clear and Modular Code Structure for Maintainability:
- The code is organized in a clear and modular structure, promoting maintainability and ease of understanding. Key components are organized into functions, making it straightforward to comprehend the purpose of each section.




## Challenges


####  Error Handling: 
-  Ensuring the script gracefully manages errors, interruptions, and network issues is crucial for maintaining reliable scraping.
####  Long-Running Execution: 
-  Balancing performance optimization while scraping data from multiple pages is a constant challenge.
####  Pagination Handling: 
-  Navigating the website's pagination presented a complex challenge. The script had to identify, traverse, and adapt to various page scenarios for a comprehensive data extraction.



## Screenshots

#### 1. Website Page Screenshot
- Books displayed on the source website from which the data was scraped.

![Website_picture](https://github.com/user-attachments/assets/3c52e0d2-1d87-45aa-87aa-0c3587d0ef3f)

#### 2. MySQL Output Screenshot
- MySQL database table displaying scraped book data with fields such as ID, Name, Price, Category, and Availability.

![Extracted_data_picture](https://github.com/user-attachments/assets/122cea35-85e3-44c4-bd6a-192eddadb842)

