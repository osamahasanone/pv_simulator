# pv_simulator
<br />
Receives home power consumption values (in W), and Generates simulated PV power values (in kW).

The output will be saved to a .csv file along with a timestamp.

### Built With

* [RabbitMQ](https://www.rabbitmq.com/#getstarted) as message broker.
* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [pipenv](https://pypi.org/project/pipenv/) for creating Python virtual environment.
* [pika 1.2.0 package](https://pypi.org/project/pika/) for using RabbitMQ in Python.

## Prerequisites

You need to have the RabbitMQ installed on your machine before getting started:

  * [Debian and Ubuntu](https://www.rabbitmq.com/install-debian.html)
  * [Windows](https://www.rabbitmq.com/install-windows.html)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/osamahasanone/pv_simulator.git
   ```
   
2. Create a Python virtual environment and install required python packages:

   ```sh
   pipenv install --ignore-pipfile
   ```
  
    Make sure to supply **--ignore-pipfile** option, this will make us on the same verions of used packages.
  
## Usage

There are **TWO** Python files to be run:
* **meter.py**:
  - Open Linux bash (or Windows CMD) from the project directory.
  - Activate the virtual environment:
  
    ```sh
    pipenv shell
    ```
  - Execute meter.py file:
  
    ```sh
    python3 meter.py server queue interval
    ```
    
    Here we are passing (3) arguments to meter.py:
    - **server:** RabbitMQ server name or IP.
    - **queue:** RabbitMQ queue name.
    - **interval:** seconds to  wait between two messages.

    Example:
    
    ```sh
    python3 meter.py localhost pv 2
    ```    
    
    This means that home power consumption values will be sent to **pv** queue in RabbitMQ installed on **localhost** every **2** seconds.
    
* **pv_simulator.py**:
  - Open **ANOTHER** Linux bash (or Windows CMD) from the project directory.
  - Activate the virtual environment:
  
    ```sh
    pipenv shell
    ```
  - Execute pv_simulator.py file:
  
    ```sh
    python3 pv_simulator.py server queue filename.csv
    ```
    
    Here we are passing (3) arguments to pv_simulator.py:
    - **server:** RabbitMQ server name or IP.
    - **queue:** RabbitMQ queue name.
    - **filename:** csv file to write the output to.

    Example:
    
    ```sh
    python3 pv_simulator.py localhost pv pv_values.csv
    ```   
    This means that home power consumption values will be read from **pv** queue in RabbitMQ installed on **localhost**, and the output will be written to **pv_values.csv**.

* Open the filename.csv in VSCode (to see live changes), and check the output.

## Contact

Osama Hasan: [LinkedIn](https://www.linkedin.com/in/osamahasanone) - osamahasanone@gmail.com - [Whatsapp](https://wa.me/96176430029)





