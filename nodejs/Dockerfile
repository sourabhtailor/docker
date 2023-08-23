FROM ubuntu
run apt-get update
run apt-get install node.js -y && mkdir /game
copy . /game
workdir /game
cmd ["node","node.js"]
