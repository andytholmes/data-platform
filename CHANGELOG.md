# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Created a health check Jupyter notebook (`notebooks/health_check.ipynb`) to monitor the status of all services
- Added Spark History Server documentation to README.md
- Added Jupyter Notebook password configuration
- Added trino Python package (v0.330.0) to requirements.txt for Jupyter notebook integration
- Added comprehensive .gitignore file to exclude unnecessary files while keeping important configurations
- Added .gitkeep files to maintain data directory structure

### Changed
- Moved Spark configuration from `conf/spark-defaults.conf` to `spark/conf/spark-defaults.conf` for better organization
- Updated Trino SQL Server connector configuration to use correct Docker service name
- Updated Jupyter service configuration to use password authentication instead of token
- Updated .gitignore to specifically ignore data/input and data/output directories while maintaining directory structure

### Fixed
- Fixed Trino SQL Server connection issue by updating hostname from `sqlserver2019` to `sqlserver`
- Fixed Jupyter Notebook password authentication issues
- Fixed Spark event logging configuration

### Security
- Set up Jupyter Notebook with password authentication
- Configured SQL Server with secure password
- Enabled SSL for Trino connections

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