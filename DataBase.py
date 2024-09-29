class DataBase:
    def get_connection_string():
        # Connection string to SQL Server
        return (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=(localdb)\MSSQLLocalDB;"  # Change to your server name
            "Database=PythonTaskManagementDB;"  # Name of your created database
            "Trusted_Connection=yes;"  # Or provide username/password if not using Windows auth
        )
