# Django Expense Manager

This repository contains a simple expense manager project created using Django and Python.

## Documentation

The project uses three Django apps:
1. **Default**: Shows default views and the home page.
2. **ManageUsers**: Helps to manage users.
3. **ExpenseManager**: Contains a dashboard that can split and download CSV files.

## Features

1. **Authentication and Authorization**  
   You can sign in/sign up and access the dashboard.
  
2. **View User Data**  
   You can view all user data, which contains user name, email, and phone number from the SQLite3 database. It uses pagination and shows 10 results per page. Please note that this feature does not require any authorization.

3. **Dashboard**  
   Dashboard to perform operations, such as splitting by equal, partitions, and percentage.

## Test Credentials

For testing, you can sign in with the following credentials:
- **Email**: `test1@gmail.com`
- **Password**: `123456`
