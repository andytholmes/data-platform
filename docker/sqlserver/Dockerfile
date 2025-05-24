FROM mcr.microsoft.com/mssql/server:2019-latest

ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourStrong!Passw0rd
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="$PATH:/opt/mssql-tools18/bin"

COPY ../sqlserver/restore.sh /usr/src/app/restore.sh

CMD ["/bin/bash", "/usr/src/app/restore.sh"]