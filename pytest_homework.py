import pytest
import pyodbc
from datetime import datetime

# Establish database connection
def db_connection():
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=EPBYMINW18FC\SQLEXPRESS;'
                          'DATABASE=TRN;'
                          'Trusted_Connection=yes;')
    return conn

# Make the connection available as a fixture
@pytest.fixture(scope="module")
def cursor():
    conn = db_connection()
    cur = conn.cursor()
    yield cur
    conn.close()

def test_null_count_employee_name(cursor):
    query = """
    SELECT COUNT(*) FROM hr.employees WHERE first_name IS NULL 
    UNION ALL 
    SELECT COUNT(*) FROM hr.employees WHERE last_name IS NULL
    """
    cursor.execute(query)
    result = cursor.fetchone()[0]
    assert result == 0, "There are NULL values in name columns"

def test_no_future_hire_dates(cursor):
    current_date = datetime.now().strftime('%Y-%m-%d')
    query = f"SELECT COUNT(*) FROM hr.employees WHERE hire_date > '{current_date}'"
    cursor.execute(query)
    future_hire_count = cursor.fetchone()[0]
    assert future_hire_count == 0, "There are employees with future hire dates in the Employees table"

def test_no_negative_salary(cursor):
    query = """
    SELECT COUNT(*) FROM hr.jobs WHERE min_salary < 0 
    UNION ALL 
    SELECT COUNT(*) FROM hr.jobs WHERE max_salary < 0
    """
    cursor.execute(query)
    negative_count = cursor.fetchone()[0]
    assert negative_count == 0, "There are jobs with negative values in the salary columns"

def test_no_job_duplicates_in_jobs(cursor):
    query = """
    SELECT COUNT(DISTINCT job_title) AS unique_rows,
           COUNT(*) AS total_rows
    FROM hr.jobs
    """
    cursor.execute(query)
    result = cursor.fetchone()
    unique_row_count = result[0]
    total_row_count = result[1]
    assert unique_row_count == total_row_count, "There are full duplicates in the jobs table"

def test_valid_country_codes_in_locations(cursor):
    query = """
    SELECT DISTINCT country_id
    FROM hr.locations 
    WHERE country_id NOT IN (SELECT country_id FROM hr.countries)
    """
    cursor.execute(query)
    invalid_country_codes = cursor.fetchall()
    invalid_country_codes = [code[0] for code in invalid_country_codes]
    assert not invalid_country_codes, f"Invalid country codes found in Locations table: {invalid_country_codes}"

def test_valid_regions_in_countries(cursor):
    query = """
    SELECT DISTINCT region_id
    FROM hr.countries 
    WHERE region_id NOT IN (SELECT region_id FROM hr.regions)
    """
    cursor.execute(query)
    invalid_country_codes = cursor.fetchall()
    invalid_country_codes = [code[0] for code in invalid_country_codes]
    assert not invalid_country_codes, f"Invalid country codes found in Locations table: {invalid_country_codes}"
