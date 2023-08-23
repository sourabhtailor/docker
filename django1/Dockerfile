FROM ubuntu
RUN apt-get update && apt-get install unzip wget -y
RUN apt-get install nginx -y
workdir /app
add https://www.free-css.com/assets/files/free-css-templates/download/page295/esigned.zip .
run unzip esigned.zip 
copy esigned-html/* /var/www/html
cmd ["nginx', "-g"," daemon off"]

