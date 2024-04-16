# Flask API Project

## Description
This Flask-based web API manages user access details to servers. It supports operations to create, retrieve, update, and delete user access details.

## Installation
Follow these steps to install and run the project:

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   ```

2. **Install Required Python Packages**:
   ```
   pip install -r requirements.txt
   ```

3. **Build and Run Docker Container**:
   ```
   docker-compose up --build
   ```

## Usage
Access the API through your web browser at `http://localhost:8080`. It supports the following endpoints:

- **GET /**: Retrieves basic server access details.
- **GET /access**: Fetches or queries specific access details.
- **POST /access**: Adds new access details.
- **PUT /access**: Updates existing access details.
- **DELETE /access**: Removes access details.

For detailed API documentation, visit `http://localhost:8080/api/docs`.

## Project Structure
- **app.py**: Main application file.
- **requirements.txt**: Lists dependencies required to run the application.
- **Dockerfile**: Dockerfile for building the Docker image.
- **compose.yaml**: Docker Compose file for service management.
- **static/swagger.json**: Defines the Swagger API documentation.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- Your Name (your.email@example.com)

## Acknowledgments
Special thanks to all contributors who have made this project possible.
