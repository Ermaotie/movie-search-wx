#端口转发
sudo apt update
sudo apt install iptables
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080