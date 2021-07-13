# pv_simulator
<br />
Receives home power consumption values (in W), and Generates simulated PV power values (in kW).

The output will be saved to a .csv file along with a timestamp.

### Built With

* [RabbitMQ 3.8.19](https://www.rabbitmq.com/#getstarted) as message broker.
* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [pipenv 2021.5.29](https://pypi.org/project/pipenv/) for creating Python virtual environment.
* [pika 1.2.0 package](https://pypi.org/project/pika/) for using RabbitMQ in Python.

## Prerequisites

You need to have the RabbitMQ server installed on your machine before getting started:

  * [Debian and Ubuntu](https://www.rabbitmq.com/install-debian.html)
  * [Windows](https://www.rabbitmq.com/install-windows.html)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/osamahasanone/pv_simulator.git
   ```
2. Inastall pipenv:

   ```sh
   pip3 install pipenv
   ```
   
3. Create a Python virtual environment and install all required python packages in one command:


   ```sh
   pipenv install --ignore-pipfile
   ```
  
    Make sure to supply **--ignore-pipfile** option, this will make us on the same versions of used packages.
  
## Usage

There are **TWO** Python files to be run:
* **meter.py**:
  - Open Linux bash (or Windows CMD) from the project directory.
  - Activate the virtual environment:
  
    ```sh
    pipenv shell
    ```
  - Execute meter.py file:
    
    **For Linux**:
    ```sh
    python3 meter.py server queue interval
    ```
    **For Windows**
    ```sh
    python meter.py server queue interval
    ```
    
    Here we are passing (3) arguments to meter.py:
    - **server:** RabbitMQ server name or IP address.
    - **queue:** RabbitMQ queue name.
    - **interval:** seconds to  wait between two messages.

    Example:
    
    ```sh
    python3 meter.py localhost pv 2
    ```    
    
    This means that home power consumption values will be sent to **pv** queue in RabbitMQ server installed on **localhost** every **2** seconds.
    
* **pv_simulator.py**:
  - Open **ANOTHER** Linux bash (or Windows CMD) from the project directory.
  - Activate the virtual environment:
  
    ```sh
    pipenv shell
    ```
  - Execute pv_simulator.py file:
  
    **For Linux** 
    
    ```sh
    python3 pv_simulator.py server queue filename.csv
    ```
    
    **For Windows**
    
    ```sh
    python pv_simulator.py server queue filename.csv
    ```
    
    Here we are passing (3) arguments to pv_simulator.py:
    - **server:** RabbitMQ server name or IP address.
    - **queue:** RabbitMQ queue name.
    - **filename:** csv file to write the output to.

    Example:
    
    ```sh
    python3 pv_simulator.py localhost pv pv_values.csv
    ```   
    This means that home power consumption values will be read from **pv** queue in RabbitMQ server installed on **localhost**, and the output will be written to **pv_values.csv**.

* Open the filename.csv in VSCode (to see live changes), and check the output.

**Note:**

PV simulated values are generated by my own dummy formula, so it could be alittle bit different from its correct values.

Below is the output of my formula for one day:

![alt text](https://github.com/osamahasanone/pv_simulator/blob/main/output/pv_simulated_own_calculation.png?raw=true)

## Contact

Osama Hasan: [LinkedIn](https://www.linkedin.com/in/osamahasanone) - osamahasanone@gmail.com - [Whatsapp](https://wa.me/96176430029)





