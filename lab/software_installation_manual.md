# Miniconda Installation for KTH Ubuntu Rooms

If you're in the Ubuntu rooms at KTH, follow these steps to install Miniconda in your personal folder and add it to your `$PATH`:

1. Go to the [KTH IT support page for Ubuntu installations](https://intra.kth.se/en/it/programvara-o-system/programvara/installera/kth-ubuntu/personal-1.811003) and download the Miniconda installer suitable for Linux. Check out the "Miniconda – minimal conda environment" section.

    ```bash
    wget 'https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh'
    md5sum -c <(echo "bec6203dbb2f53011e974e9bf4d46e93 *Miniconda3-latest-Linux-x86_64.sh")
    bash Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"
    ```

2. To ensure you can access the `conda` command from any location in the terminal, add Miniconda to your `$PATH` by executing:

   ```bash
   echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Installing numpy

    ```bash
    conda install numpy
    ```

# Preparing Your Computer for Bioinformatics Labs

The computer labs will run in computer classrooms (highly suggested). Nevertheless, it is possible that you work on your own laptops. To avoid delays during the first lab, we want you to prepare your computer environment beforehand.

We will explore several bioinformatics tools during the lab sessions. Some tools will be possible to run online, while others need to be installed and run locally.

## Setting up Conda

[Conda](https://conda.io/) is a popular package manager and sandboxing environment for data science software, including many bioinformatics tools. We recommend that you set up a Conda environment by following the steps listed below to make it easier to install the software that you will need for the computer labs.

### For Windows Users

If you are using a Windows computer, you are encouraged to use a **Windows Subsystem for Linux (WSL)** shell, as some of the tools that we will work with are not available for Windows. 

- [Follow the instructions for WSL before proceeding.](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

### Installing Conda (Windows and Linux)

First, [install a Conda distribution for your operating system](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation). If you are using a Windows computer with WSL, you can download the installer by typing in your WSL shell:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

and then follow the instructions for **installing Conda on Linux**.

### Creating the Conda Environment

We are now ready to create our Conda sandbox for the bioinformatics tools that we will use. Run the following command in your shell:

```
conda create -n bioinfo python=3.8
```

After you have installed the new dependencies, you can activate the sandbox by typing:

```
conda activate bioinfo
```

### Installing VS Code


Visual Studio Code (often referred to as VS Code) is a free and open-source code editor developed by Microsoft. It offers features like debugging, syntax highlighting, and even Git integration out of the box. Below is a guide on how to install it on both Windows and Linux.

#### Windows


   Navigate to the [official VS Code download page for Windows](https://code.visualstudio.com/Download).


   Click on the `Windows` option to download the `.exe` installer.


#### Linux (Ubuntu/Debian)



   ```bash
   sudo apt update
   sudo apt install software-properties-common apt-transport-https wget
   wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
   sudo apt update
   sudo apt install code
   ```

### If problems persist:
Sometimes there are compatibility issues that we may be unaware of. If this is the case, consider using the computer provided in the computer lab rooms.
