# Anaconda Environment
This is a full tutorial on how to setup a anaconda environment, which is used by jupyter notebook to execute code in different python environments. The benefit being that it is easy to switch python versions and run different notebooks on different versions. 

## Windows
### Setup
Begin by installing Anaconda, this tutorial utilizes anaconda and not Miniconda which could also be used to solver the same issue. Installation of Anaconda can be found in the [installation docs](./anaconda_install.md). 

### Anaconda Navigator
When installed anaconda navigator should be able to be opened. On the left side is tab for environments, where installments and package handling of the environments can be done. 

### Create Environment
To create a environment is done within a terminal. The following example creates an environment for python version 3.7.1 and naming the environment python_3_7_1.
> conda create -n python_3_7_1 python=3.7.1 

Then the environment can be activated in Anaconda navigator under environments by pressing on the desired environment. Or alternatively by the following command: 
> conda active python_3_7_1

To verify that the correct environment is activated in terminal you can call
> where python

and 
> python --version

If the path is your anaconda path and the version is the correct one selected then the setup is completed. (Although this may conflict with existing python versions installed)

### Chose Environment In Vscode
In jupyter notebooks you can select the environment to run a notebook in the upper left corner. 

### Packages
Installing packages is simple, select environment in Anaconda Navigator then press the button that looks like a play button on the selected environment. Options for **Open Terminal** and **Open with Python** will show. Simplest way is to select **Open Terminal** then pip installing the required packages in that terminal, so they are accessible in environment. For jupyter notebooks you generally always have to install _ipykernel_, which can be done with the following command: 
> pip install ipykernel

### Delete Environments
Deletion of environments can done by selecting an environment in the Anaconda Navigator and under the environments there should be a remove button which deletes the environment. 


## Linux 
**TODO**
