FROM jupyter/datascience-notebook:latest

USER jovyan

# Set the working directory
WORKDIR /home/jovyan/work

# Expose the port
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"] 