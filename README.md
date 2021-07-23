# pv_simulator
<br />
Receives home power consumption values (in W), and generates simulated PV power values (in kW).

### Built With

* [RabbitMQ 3.8.19](https://www.rabbitmq.com/#getstarted) as message broker.
* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [pipenv 2021.5.29](https://pypi.org/project/pipenv/) for creating Python virtual environment.
* [pika 1.2.0 package](https://pypi.org/project/pika/) for using RabbitMQ in Python.

## Prerequisites

You need to have RabbitMQ server installed before getting started, please follow the link appropriate to your OS:

  * [Debian and Ubuntu](https://www.rabbitmq.com/install-debian.html)
  * [Windows](https://www.rabbitmq.com/install-windows.html)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/osamahasanone/pv_simulator.git
   ```
2. Install pipenv:
   
   ```sh
   sudo pip install pipenv
   ```
   
3. Create a Python virtual environment and install all of the required Python packages in one command:

   ```sh
   pipenv install --ignore-pipfile
   ```
  
    Make sure to provide *--ignore-pipfile* option, it will make us on the exact same versions of packages.
  
## Usage

There are two Python files need to be run:
* **meter.py**:
  - Open Linux Bash (or Windows CMD) inside the working directory.
  - Activate the virtual environment:
  
    ```sh
    pipenv shell
    ```
  - Run meter.py file:
    
    ```sh
    python meter.py server queue interval
    ```
    
    Here we are passing *(3) arguments*:
    - *server:* RabbitMQ server name or IP address.
    - *queue:* RabbitMQ queue name.
    - *interval:* seconds to  wait between two messages.

    Example:
    
    ```sh
    python meter.py localhost pv 2
    ```    
    
    This means that home power consumption values will be sent to *pv* queue in RabbitMQ server installed on *localhost* every *2* seconds.
    
* **pv_simulator.py**:
  - Open another Linux Bash (or Windows CMD) inside the working directory.
  - Activate the virtual environment:
  
    ```sh
    pipenv shell
    ```
  - Run pv_simulator.py file:
  
    ```sh
    python pv_simulator.py server queue filename.csv
    ```
    
    Here we are also passing *(3) arguments*:
    - *server:* RabbitMQ server name or IP address.
    - *queue:* RabbitMQ queue name.
    - *filename:* csv file to write the output to.

    Example:
    
    ```sh
    python pv_simulator.py localhost pv output.csv
    ```   
    This means that home power consumption values will be read from *pv* queue in RabbitMQ server installed on *localhost*, and the output will be written to *output.csv*.

* Open the filename.csv in VSCode (to see live changes), and check the output.

## Output

An **output** folder has been included. It contains two files:

- *output.csv:* contains the output for a whole day (code has been left running from 00:00:00 to 23:59:59).

- *pv_simulated_own_calculation.png:* curve of the pv power for a whole day. 

  PV simulated values were generated by my own dummy formula, so it could be a little bit different from its correct values.

## Contact

Osama Hasan: [LinkedIn](https://www.linkedin.com/in/osamahasanone) - osamahasanone@gmail.com - [Whatsapp](https://wa.me/96176430029)





