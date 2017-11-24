from fabric.api import*
env.hosts=['192.168.0.19 ,192.168.0.18 ']
env.ser='vagrant' 
env.password='vagrant'

def apache_install():
  sudo("apt-get install apache2 -y")

def apache_start():
  sudo ("service apache2 start")

def apache_enable():
  sudo("sudo update-rc.d apache2 enable")

def push_index():
  put("index.html","/var/www/index.html", use_sudo=True)

def apache_restart():
  sudo("service apache2 restart")

def disable_firewall():
  sudo("service ufw stop")

# Calling all the functions defined above a single fnction.

def assemble_apache():
  apache_install()
  apache_start()
  apache_enable()
  apache_index()
  apache_restart()
  disable_firewall()

# Define all the fabric methods to clean apache setup in just one function.

def dismantle_apache():
  sudo("service apache2 stop")
  sudo("apt-get remove apache2 -y")
  sudo("sudo update_rc.d apache2 disable")
  sudo("service ufw start")
