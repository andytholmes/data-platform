# Changelog

All notable changes to the Data Platform project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup with Airflow, Spark, SQL Server, Trino, and Jupyter services
- ETL pipeline implementation with PySpark
- Unit tests for ETL functionality
- Comprehensive README.md with architecture diagram
- Docker configuration for all services
- PostgreSQL database for Airflow metadata
- Airflow initialization and user creation scripts

### Changed
- Removed obsolete `version` field from docker-compose.yml to resolve Docker Compose warning
- Updated project structure to follow best practices
- Improved documentation with detailed service descriptions
- Changed Java package from `openjdk-11-jre-headless` to `default-jre-headless` in Airflow Dockerfile
- Updated port mappings to resolve conflicts:
  - Airflow UI: 8081 (was 8080)
  - Trino UI: 8082 (was 8080)
- Added platform specification for ARM64 architecture support
- Enhanced Airflow configuration with proper database settings
- Added health checks for PostgreSQL service

### Fixed
- Docker Compose warning about obsolete version attribute
- Port conflicts in docker-compose.yml
- Directory structure organization
- Java installation issue in Airflow container build
- Platform mismatch issues for SQL Server and Spark containers
- Port allocation conflicts between Airflow and Trino
- Airflow initialization and database connection issues
- Jupyter authentication issues

## [0.1.0] - 2024-03-19

### Added
- Basic project structure
- Docker configuration files
- Initial service definitions
- README.md with basic documentation

### Known Issues
- Memory limits may need adjustment based on host machine capabilities
- SQL Server container may take 5-10 minutes to initialize on first startup

### Planned Updates
- [ ] Add health checks for all services
- [ ] Implement data validation in ETL pipeline
- [ ] Add monitoring and logging solutions
- [ ] Create sample data and example notebooks
- [ ] Add CI/CD pipeline configuration
- [ ] Implement backup and restore procedures
- [ ] Add security hardening measures

### Notes
- The project is currently in development phase
- All services are configured for local development
- Production deployment configurations will be added in future releases 