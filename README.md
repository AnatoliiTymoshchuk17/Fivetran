# My Python Project with PostgreSQL

This project is a Python application that uses a PostgreSQL database. It includes integration with pytest for running tests and Docker for easy setup and deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8
- Docker
- Docker Compose

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AnatoliiTymoshchuk17/Fivetran
   cd Fivetran
   ```

2. **Setup Virtual Environment (Optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the PostgreSQL Database with Docker**

   ```bash
   docker-compose up -d
   ```

5. **Run the Application**

   ```bash
   python script.py
   ```

6. **Run the Tests**

   ```bash
   pytest
   ```

## Built With

* [Python 3.8](https://www.python.org/downloads/release/python-380/) - The programming language used
* [PostgreSQL](https://www.postgresql.org/) - The relational database used
* [pytest](https://pytest.org/) - The testing framework used
* [Docker](https://www.docker.com/) - Container platform used

## Authors

* **Anatolii Tymoshchuk** - [AnatoliiTymoshchuk](https://github.com/AnatoliiTymoshchuk17)
