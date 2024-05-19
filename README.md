## Getting Started

1. To start the project, run the following command:

   ```bash
   docker-compose up -d
   ```

2. Open http://localhost:8081 to access the Airflow UI.

3. This project includes an automated pipeline that:

- Extracts data
- Transforms the data
- Pushes the data to Google Drive using DVC
- Commits code to GitHub
